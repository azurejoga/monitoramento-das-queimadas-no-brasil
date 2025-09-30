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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6231d8d-c08a-3589-8f14-e43f688bd55c | -19.30572 | -43.8153 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11367307-31d6-3933-9a5e-2d3d22df1036 | -14.71201 | -48.23578 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b43c74a6-c37e-323f-b883-c6e087af2d4c | -14.78679 | -48.3188 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fd88db2-89f5-351c-9c7a-54cc3c82bfcf | -20.06606 | -46.78724 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9121ef97-c0fa-30e9-b4f0-c41b85fc08f6 | -19.85482 | -43.81292 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9edcdf4e-7828-3248-a8e5-fbc7e1dd3c53 | -14.72032 | -45.67149 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0e5ee193-22ef-3c50-b5bf-0705794738dc | -16.61069 | -43.35863 | 2025-09-30 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a721996-2b2c-3595-ad79-983c982e62c9 | -15.03517 | -46.98801 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 663a66fa-c6a9-3d48-adad-eea30fb1946a | -19.33143 | -43.81409 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63d7f566-35c8-3bfb-a5f3-bdf304d8204a | -15.68721 | -53.62992 | 2025-09-30 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a48c6624-c72f-3e95-ae2d-3dfd98333f7c | -16.40278 | -52.17175 | 2025-09-30 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c6f7ffe-af31-3e97-a73f-693ae3836912 | -15.84886 | -54.03618 | 2025-09-30 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a42c9ac-f74f-348d-9809-2f17e2b15486 | -15.24617 | -56.80041 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea1088ce-f8a1-3cdb-9094-5255601b664a | -16.06328 | -51.02939 | 2025-09-30 04:42:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bce5c62d-abc0-31c2-86c7-c57e6b200407 | -14.54776 | -48.47724 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7fd0b66c-c542-314a-b070-e6123e336484 | -14.57135 | -48.2166 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b95f31c-7948-328d-85b3-41f01202685c | -14.5502 | -48.26149 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceee4f23-4a1b-3e8d-a394-a2a5bf2d7efa | -18.61836 | -50.70872 | 2025-09-30 04:42:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 536e1ddc-84c8-30ba-ad3b-0e72ee25c4e0 | -20.1888 | -49.12049 | 2025-09-30 04:42:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c10f9855-ad0c-39a5-9fc1-5596778af157 | -19.85517 | -43.80967 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0706276c-3bed-3e4b-b0c4-805dbd6b4884 | -14.79152 | -48.31121 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29d58065-e658-3874-8ec7-91fbaa363d82 | -14.54074 | -48.2253 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88f640e6-cdb3-34c5-937e-edd304c499af | -15.86328 | -46.22966 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 981329d2-2db1-3c79-8376-1c4ed7c247fe | -15.27941 | -48.02401 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eb18a73e-a1c6-3883-861c-1319218db9b5 | -14.70936 | -45.6801 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 775c133d-bbb2-38e2-b6f3-d7c049152ff1 | -14.51242 | -48.42229 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c1ac0d7-f5ce-388b-b8dd-6c9ba5a0d8ea | -14.60353 | -48.28869 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1e31cf6-d0cd-3c4f-b40c-b275abda04fd | -14.23665 | -49.79199 | 2025-09-30 04:42:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c64f13e8-f792-3aa3-84fd-66a1c5a30cd6 | -15.17114 | -52.29478 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12c7375f-2faa-38a4-acdf-fc8a3b599e75 | -15.39851 | -44.98165 | 2025-09-30 04:42:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7194941c-ede1-36d6-bb85-23741e5546ec | -14.46721 | -52.90052 | 2025-09-30 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b6ebf82-fa01-30d0-9e81-b938492c3f21 | -15.26956 | -49.49572 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d574f19-7e33-3d18-aff2-4799c59b5407 | -15.93143 | -46.21304 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a9c47f50-16be-382b-bdbe-5268926348d9 | -20.62356 | -46.18325 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aefa8785-a48e-3a06-874d-3a75085e7d10 | -15.27935 | -47.86076 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a7bbc35b-f196-3a49-a5fe-48b05ef6555e | -17.10679 | -48.57351 | 2025-09-30 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba147fb2-f40f-3e81-9e1a-dc36e5ffe3de | -20.07447 | -46.43283 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afa35e51-bed9-38e5-97b2-191ebec90a89 | -18.12282 | -42.1985 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6ebd86ff-3462-3d0a-a97c-8f04e02ef1d6 | -14.51296 | -48.4437 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 681bde7b-ccb6-38b5-b268-f4984733fa0b | -15.49424 | -48.55904 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97404706-452c-3702-a25c-8712cb0bca5c | -14.69948 | -48.24659 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39b8cace-01c5-3772-8143-ba5c68d8242f | -19.858 | -43.81816 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1153ecc5-e7e3-30f2-9de8-51778ea13fe0 | -14.7381 | -45.66583 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 979ddb16-620b-375c-894e-99c5f5a53809 | -16.28015 | -52.53485 | 2025-09-30 04:42:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27b1427b-4d6c-357e-9d30-32ecdd8114de | -14.71086 | -45.70055 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 842b1dd2-0f31-3fc9-b0fe-08540bd7d619 | -15.85821 | -46.23653 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ca12c42-8b4e-342d-b927-b326aab1f69f | -15.28219 | -49.26816 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb6fe2c6-c4f0-383a-ac1f-e3ac41f5a018 | -15.17446 | -52.29533 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67ef56cc-bdd2-3c8d-9456-67434f0dccba | -15.07068 | -45.05761 | 2025-09-30 04:42:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 31d7ec8f-7b6b-3793-8d0e-09f8a3d83d41 | -15.26557 | -49.499 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f18a70-4daa-3dfd-b62b-6b1096c70519 | -15.48722 | -45.86907 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0597bc35-e3e4-3f73-810d-cb2d72e71933 | -15.27538 | -47.89457 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d32ba6c4-f968-3d47-8bc3-1d8da9617ecc | -15.42283 | -48.24953 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3225f4d-b02e-308c-b26c-1287b7275597 | -14.56098 | -48.26291 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67f80542-dfb9-3a06-bbb2-1265aa1a964d | -20.0649 | -46.7888 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf946491-36eb-3f08-9414-9954babd6b0e | -14.52947 | -48.47987 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e5bd0435-9932-3ed1-8478-b53c102ccd3a | -15.38874 | -47.0742 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 73499030-c1e3-3117-a111-987dcb54d5f7 | -20.42099 | -43.35024 | 2025-09-30 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6ea575c0-d131-355b-852e-0e058eb9f110 | -15.72074 | -47.59115 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 708db440-2b9d-3efd-ba4a-ec9c88a0885b | -14.75067 | -45.66757 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cce14114-6f7c-394d-9402-59c10669d7f5 | -14.56788 | -48.4631 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c755996-345d-3083-b2d6-d61ccb82961e | -20.41995 | -43.36028 | 2025-09-30 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b0c83580-f04c-3e40-b9c0-860e43b95df7 | -15.59819 | -47.83049 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b398228-4a58-3425-92ea-c89d76c36440 | -17.09287 | -48.567 | 2025-09-30 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27274179-02f9-3b5e-b972-4d21e0b685b1 | -18.47977 | -44.02343 | 2025-09-30 04:42:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9e20517-1344-3af5-b04f-e86abb1fd8e5 | -15.50199 | -48.5559 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 439d404b-5cf2-3c53-bc52-67b98a33a631 | -15.02815 | -46.98165 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8547ccb8-5e74-3c9b-952e-de4fb696eb84 | -15.20172 | -49.55172 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5be2066a-d011-3a41-b66f-1f2fb75a8d73 | -14.53949 | -48.4845 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f85df11f-77c8-353c-b8db-38e9e70cd6f9 | -19.85961 | -43.81618 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3635a87b-1465-3870-aa1e-1b0a283532da | -15.29901 | -56.78961 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1a20daf-0ff9-3eb9-8184-02b2dbc99b65 | -15.54885 | -44.33547 | 2025-09-30 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b166c981-72a3-3e55-82ed-97e71b867215 | -15.72009 | -47.59587 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5ef7e1e0-bfd0-3a24-af1e-6d27c3402b37 | -14.51947 | -48.44884 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 77cd9c48-8c91-3d02-8b30-9e37881a9270 | -14.66844 | -48.14238 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 922936e8-ba90-339a-b022-b8b4ac3ab683 | -19.86099 | -42.58815 | 2025-09-30 04:42:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 80be09d7-5a03-35f5-b17c-06589a67b384 | -19.92404 | -49.90426 | 2025-09-30 04:42:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 96422cc6-6110-3725-9701-794b9f6c71ef | -15.38174 | -47.06747 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc8b856a-0f83-3a74-9664-e84f7a075773 | -15.27997 | -47.88376 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38f8a476-a883-3cd5-8254-b9830e496783 | -17.70586 | -46.66383 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b46648e5-2f8a-3103-a51c-3d8a894f0acb | -15.06303 | -45.04768 | 2025-09-30 04:42:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64d2cddc-8ce7-3bd1-a3ea-1d1a0131adc9 | -14.53953 | -48.23377 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69d46771-cd4a-35c1-8442-ea5d3a66efd4 | -15.28943 | -51.43685 | 2025-09-30 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2101ac68-d5a3-3f57-81da-f727fb2820b3 | -15.53514 | -42.66069 | 2025-09-30 04:42:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce17e625-e188-3761-b8a3-6f23a7918099 | -14.54361 | -48.48095 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b66778a7-2ec2-368f-8e91-e1600aa248ad | -20.06541 | -46.78472 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78fbfbcb-2dab-3cf7-97e5-b00eb30425ed | -14.50887 | -48.42172 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ded3756b-8ed5-3b9f-b799-c06e09aba5b0 | -20.39689 | -43.68187 | 2025-09-30 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 460131af-1c1e-3443-89ac-b82a2608b9a9 | -14.56589 | -48.22895 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef0fd44e-8c78-3e97-9c63-1900901af0ad | -20.42136 | -43.34667 | 2025-09-30 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 63d7d915-d73c-35d9-9211-711dee231634 | -15.20681 | -50.10987 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d89e5a6-d086-3ea3-890c-0b41f7fc7b10 | -14.70787 | -45.70238 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98a3a719-5f88-320f-b6e7-b725dc976e7f | -15.59881 | -47.82605 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05390c5a-e5f7-395c-90e9-fcfb637b8672 | -15.88231 | -46.21178 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc2271cf-d1e2-3a2d-b084-15ae36b687ec | -14.78436 | -48.31006 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 325da55e-68bf-3d12-8de6-eec17f219a0e | -17.39311 | -47.15576 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d53d1b2b-f1c2-3df1-9180-f7712848562c | -14.52885 | -48.48418 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 03d7396b-2529-3a77-9e45-d93098852205 | -15.22817 | -49.89664 | 2025-09-30 04:42:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f55d9044-a69a-33a4-8c17-495c4a8618a6 | -16.52895 | -49.43139 | 2025-09-30 04:42:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cd638ed-0f1e-3796-9b98-11b91b845167 | -19.87169 | -42.59479 | 2025-09-30 04:42:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |


[Clique aqui para ver as próximas entradas](README74.md)
