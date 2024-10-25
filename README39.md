# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7fe9dfa-2a67-3c6b-b2b7-d4654f706aac | -17.81252 | -57.60413 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e646400b-7275-3ce0-9551-0c828b052748 | -17.80399 | -57.55668 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 82a7926f-b3a7-312e-a708-dcf98c2ec1e0 | -17.80186 | -57.56624 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 98d644e2-c215-36a1-b554-aca552ce4954 | -17.79583 | -57.56481 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a6f66f39-45bb-313e-9fbd-fefa3c421fc9 | -17.78981 | -57.56336 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 44478224-1309-3782-9ddc-86121df19b91 | -11.13674 | -40.1919 | 2024-10-25 04:17:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee52b2c5-be1b-301d-81a7-4edf1461a5fa | -11.1361 | -40.19654 | 2024-10-25 04:17:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9307eeda-962a-32e6-9a03-387902aaa2de | -11.13544 | -40.19455 | 2024-10-25 04:17:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cd7e7bc1-b183-39e9-99c4-a75f2acde7c4 | -10.7383 | -41.38289 | 2024-10-25 04:17:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8c4baf80-f813-3db3-b4a9-e92244b1bf25 | -15.0358 | -42.29244 | 2024-10-25 04:17:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4d49e704-e1b1-3ba0-8260-f6830dffd8e8 | -14.95472 | -42.25436 | 2024-10-25 04:17:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05f8578c-d4a2-30e3-a88a-8e80607b1da8 | -13.64672 | -44.29815 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 121cfaf7-db5c-3695-887d-c7ad95700fba | -13.64617 | -44.3017 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a17567b-6188-3cd5-a391-3acdcad42485 | -10.26361 | -36.57215 | 2024-10-25 04:17:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| 61eb9853-f11e-391c-93e1-d68d063d56f6 | -10.2589 | -36.5715 | 2024-10-25 04:17:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| 8730ee57-c75c-3d84-9177-6d7dc24820ec | -12.34569 | -38.05345 | 2024-10-25 04:17:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e86c5218-0d2d-3a51-9554-e79cf9db8142 | -12.34455 | -38.0621 | 2024-10-25 04:17:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f4de0bba-03c9-3637-bb2d-4d671d2c01eb | -16.1276 | -40.60833 | 2024-10-25 04:17:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 07b3559c-24a4-3775-8a0b-efb300c08bd6 | -9.89543 | -40.43732 | 2024-10-25 04:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97336e26-6680-319f-9277-e84f70a58d26 | -14.95424 | -42.25587 | 2024-10-25 04:17:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 38b44884-9b77-3a3f-810c-ab252bc45563 | -14.95414 | -42.25847 | 2024-10-25 04:17:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4ff0cca-ca84-33c5-9b6d-80b0381b9167 | -14.86494 | -41.69333 | 2024-10-25 04:17:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1879c5f5-58e2-3349-94ce-9544fd0882c7 | -14.13613 | -41.69069 | 2024-10-25 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82ad71b4-f0d7-3fab-a6ea-74f8b53b26ea | -15.17446 | -40.99879 | 2024-10-25 04:17:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b89970e1-f951-393b-975a-bc0cc136ea54 | -15.0435 | -41.93598 | 2024-10-25 04:17:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 76d00340-2c03-3481-bcf4-cc7267388727 | -16.32694 | -42.31119 | 2024-10-25 04:17:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 716fa47c-6719-3033-8cc5-38f4ef1bfe5b | -15.43342 | -41.13997 | 2024-10-25 04:17:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9ac81fca-6b0b-3030-bbf6-d477d55b8d7b | -15.43243 | -41.14182 | 2024-10-25 04:17:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 114dc7ba-74c0-3fe9-98b1-5649195bbd47 | -15.32027 | -41.74701 | 2024-10-25 04:17:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f648b750-0b7a-379a-be39-452cc57111ff | -10.51185 | -42.3966 | 2024-10-25 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7431521c-35c4-3034-9e88-fe6ee2d2899f | -13.6563 | -43.16521 | 2024-10-25 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c93dd90f-ad3f-3816-9fc5-95d6ea9c0d61 | -13.35738 | -43.07769 | 2024-10-25 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2309a75-98d6-34b3-aa6a-98d6e1609218 | -13.31859 | -43.00409 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e13b081-16aa-3cb7-9db6-4be6706dc964 | -13.08884 | -43.08543 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bcca71da-cfa0-3d31-9760-07cf3bf0d23f | -13.07705 | -43.09485 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a4fddce-553f-35cd-9e5c-f49be74745b6 | -13.01255 | -43.13354 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a491a79f-68f1-31cb-bebc-77f060eb506a | -12.96369 | -43.21616 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e017315b-bf3e-3e1a-85ef-97f2ee946986 | -12.92339 | -43.20978 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4cf3f326-9b7e-3e5c-8976-ffa9be14dbd2 | -12.88809 | -43.193 | 2024-10-25 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6093fd31-29e8-3eb6-89e8-03f838ce7414 | -13.57301 | -43.43057 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50a613bd-f25b-34fa-a954-e1361836bd27 | -12.34588 | -42.53071 | 2024-10-25 04:17:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f11e8e6b-d228-38d7-b189-c36ef310b44a | -12.52159 | -43.26263 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbef1386-0865-3a26-9531-cde3a2c09f60 | -14.94873 | -43.16785 | 2024-10-25 04:17:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 21fa4135-0db4-3b92-a1d5-98c97f488207 | -14.75723 | -42.42025 | 2024-10-25 04:17:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f7ce91ea-428f-3974-9998-3704ea67f020 | -14.25097 | -43.26115 | 2024-10-25 04:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f3691912-1270-3779-844e-6c2269601815 | -13.83064 | -43.23441 | 2024-10-25 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2112c5b3-72b6-3012-a7b8-65ef5935cea0 | -13.77374 | -43.17618 | 2024-10-25 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 90fda4f4-c41e-30cf-8ef7-96786585fcb4 | -13.66566 | -43.37764 | 2024-10-25 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 117a4d80-a901-3745-90ef-b77d9cbaa8e1 | -13.75142 | -43.59652 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 686931e6-35bf-3826-b44a-6f72a185e0eb | -13.74808 | -43.59599 | 2024-10-25 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3b5343b-f335-38eb-a9f1-b21f2081e2b6 | -13.62523 | -44.34911 | 2024-10-25 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0708ae0d-5971-31bf-9570-aa709877ce86 | -15.4555 | -43.62281 | 2024-10-25 04:17:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c65b5a3-1c62-34fc-ba89-feca28c99deb | -15.26125 | -43.6304 | 2024-10-25 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 237c59f7-33d8-3a20-83ec-02b32da018b2 | -15.25788 | -43.62986 | 2024-10-25 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 0c0e7401-d18e-345b-820e-999fc0e2bc16 | -16.34819 | -43.69632 | 2024-10-25 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47233fd9-33d0-3fcc-9d0f-a9eb71fc344f | -15.93858 | -43.03004 | 2024-10-25 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9857e9f6-6257-329e-b410-5fb25b395526 | -15.86235 | -43.52834 | 2024-10-25 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1842d6f5-4940-3099-9e05-22640ff08f35 | -16.68209 | -43.88322 | 2024-10-25 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41de872c-1a80-3646-ad9d-b83bb89c3e3b | -9.35321 | -43.36652 | 2024-10-25 04:17:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0b8f1dd2-6306-34bb-a743-24ed59554f1d | -9.35267 | -43.37 | 2024-10-25 04:17:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eaf78d9f-3d46-3349-8503-fa421cd4fd66 | -9.34497 | -43.37592 | 2024-10-25 04:17:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8a634feb-93d3-3f51-a53f-d6faf7d7e1fc | -9.26161 | -43.19134 | 2024-10-25 04:17:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4652bae2-2dd6-3eb7-8ec0-c0958f135002 | -9.10859 | -43.19183 | 2024-10-25 04:17:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ed242c07-0380-3621-9f50-5b9e191b1f4e | -9.10804 | -43.19531 | 2024-10-25 04:17:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a9e0952-e56a-35c1-83e9-31a7138041e6 | -9.12198 | -43.93121 | 2024-10-25 04:17:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1de0ce8-645f-3a7c-9901-35cd25f05008 | -9.11813 | -43.93416 | 2024-10-25 04:17:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 871a49b3-08a5-3408-99dc-4ec3758dd523 | -10.76424 | -44.26478 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e2a6b60-5aef-3bf3-90a8-6aae6bcd868d | -10.71627 | -44.30725 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5987bba-9ecf-34ba-b744-0a77ee447a66 | -10.58713 | -44.28579 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84e57c50-00ef-3f40-b633-ec9b12cb6f24 | -10.58659 | -44.28927 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cb66b35-2684-3547-82ea-a2df16ff502a | -10.58438 | -44.28177 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ef1956b-28b4-345a-9227-62afb36b62fc | -10.58383 | -44.28526 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c72ae210-5b20-3216-bdd2-b4ad1a1673c1 | -10.58328 | -44.28874 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dedce056-a69d-3136-b522-2f1ff28df821 | -10.58108 | -44.28123 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aecbeab3-36a9-3b78-bb32-396242b29b2c | -10.58053 | -44.28473 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15000b24-d52c-3cb7-a17e-001da8fc77c7 | -10.47643 | -44.21094 | 2024-10-25 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10dda9ba-ef92-3dee-9a24-2c6c03f15abe | -10.71671 | -44.04626 | 2024-10-25 04:17:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76af2f39-73a8-36eb-bb29-65cdcc37610e | -9.66594 | -43.89048 | 2024-10-25 04:17:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e74d75e1-20d0-3077-abb8-c45800a00c70 | -11.97133 | -44.13841 | 2024-10-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba273e8-2675-3032-a9f6-839298dc5ede | -11.94956 | -44.16666 | 2024-10-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea040d09-035b-3f03-947a-78c2d0a48aae | -11.91159 | -44.17132 | 2024-10-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2c403c1-0286-318e-84ca-268ce77c731a | -11.91104 | -44.17483 | 2024-10-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fb184f5-9403-3031-9da9-cf3465b1ea31 | -11.75308 | -44.46545 | 2024-10-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21ae196e-25a6-3280-b448-f8b86f87e64a | -10.90335 | -44.30873 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64f7eb4f-552f-37fb-918c-fa99643ab791 | -10.9028 | -44.31222 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4eded94f-6b10-38bc-afd1-e7537fc73775 | -10.77468 | -44.34881 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f89a20c2-9fe0-30bf-b6ad-4121683a96ae | -10.76809 | -44.26183 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eff86b74-aa97-3039-80f2-b64644cd0ac5 | -10.76754 | -44.26532 | 2024-10-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5e07963-e21a-3169-a8a2-a0500a85adbd | -11.53357 | -43.25449 | 2024-10-25 04:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45d144bd-155a-3527-a552-52c88e4ddc12 | -11.53024 | -43.25397 | 2024-10-25 04:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59c66cf8-33ba-3af8-8ccb-92dbf7db1fda | -11.48524 | -43.23588 | 2024-10-25 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d386327c-2327-3f4b-a1aa-6e0ae28bca1f | -11.48469 | -43.23945 | 2024-10-25 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ce69b88-2ca9-3bcf-aa60-8322e9b1e4e6 | -11.48415 | -43.24302 | 2024-10-25 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 94a266ea-6ba7-3cb6-a089-e3b7eb071120 | -12.30804 | -43.56646 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13daf553-a4cf-3f50-9396-43e236eb2bf0 | -12.30471 | -43.56593 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fff5634-0488-3d46-9aeb-df615ddc2d58 | -12.30417 | -43.56949 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 080f0d5b-e1e5-3f0d-b9f2-ee023998439c | -12.30139 | -43.5654 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b246115-d476-38e5-a5a2-57a725a64406 | -12.30084 | -43.56896 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edf0a867-6925-30b4-961d-b8facba17806 | -12.17507 | -43.45789 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d220a90a-ad06-32af-b244-a47b7bd84828 | -12.17174 | -43.45737 | 2024-10-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
