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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03b99816-cec1-3624-807b-d97653861276 | -9.85246 | -44.17724 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a5fc4f6-9182-3f96-b323-195c761c3026 | -3.28303 | -53.82294 | 2025-11-15 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cd3e543-6a8c-375e-9963-e7b9232a8c16 | -4.05618 | -46.41857 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10596b51-e757-393a-a8f4-1702d2f63453 | -7.44377 | -42.76532 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3151b2fd-b818-35c2-a1a3-e2508b04cad6 | -4.22794 | -51.20102 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69d22ee7-6863-3eb2-b8e0-3685361d3989 | -6.59278 | -44.24466 | 2025-11-15 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a32ca272-79db-3331-8f49-252b8c8646b5 | -5.06078 | -42.72285 | 2025-11-15 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87af187e-681a-3420-af1c-55ebbffdd6e3 | -7.88146 | -48.39578 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84464a3f-5a4b-3d4d-8cd6-107c95bd4da9 | -8.30033 | -41.38615 | 2025-11-15 04:25:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c7ded23-044f-3fa9-ab36-b184e0dd84b1 | -3.76226 | -47.74405 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2411c22-6879-34f6-9cda-3262b15018f8 | -8.32854 | -45.4113 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b044bb6c-243e-35d9-814c-f7fb1f9b4e68 | -6.22922 | -41.73348 | 2025-11-15 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98280582-005b-321d-80ff-18de02e31735 | -6.73375 | -42.95943 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6c9cbbea-a75c-39bf-a70a-65ecea4f24cd | -6.73181 | -42.97219 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e3bcfda6-b69b-394b-b6bf-17fa534b82f5 | -1.11244 | -52.59501 | 2025-11-15 04:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41f72fd1-8c78-3807-abed-8105a2903d55 | -5.69762 | -45.96749 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71f31d1d-3941-3976-9b38-bab7734076b6 | -4.75525 | -48.83844 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75cbcc49-a321-3f26-93ca-2380c7c60825 | -5.59347 | -45.18019 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbbd6664-9f60-38c8-bf4e-165148adf6c9 | -4.53963 | -46.41368 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eadaf3fb-bd61-34ad-aba6-c479f27e2a4e | -3.22213 | -45.48183 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ab3d43f7-84b3-35e0-9af7-9ba9dfd364fc | -7.1007 | -42.73403 | 2025-11-15 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 304ca774-64aa-308a-ac86-a5479745bb48 | -5.42635 | -40.66744 | 2025-11-15 04:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba8491db-c10e-3db0-9a07-84cb036f0513 | -3.95635 | -49.91187 | 2025-11-15 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b47ecac-236f-3089-a026-21d8b374064e | -9.21048 | -48.59416 | 2025-11-15 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91f9b404-fa94-3474-8c36-40c35febf600 | -3.5346 | -49.26283 | 2025-11-15 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8f51a25-a121-32bb-bec5-7aeb4839bbe9 | -17.26737 | -42.65925 | 2025-11-15 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a2411a66-5857-340b-a44b-429a6798eefc | -12.92179 | -43.09332 | 2025-11-15 04:27:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c2f8af0-0ca8-395b-970a-2556e9b3767f | -17.15751 | -43.07809 | 2025-11-15 04:27:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99c2cf08-3b0a-3aa2-8cc3-ecf1db6308ea | -12.78834 | -48.81605 | 2025-11-15 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9918d8da-9609-3f71-86a6-595581a05530 | -10.99098 | -47.73009 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adc7c5d8-d4f8-338a-8058-98a34106053b | -10.4454 | -47.33675 | 2025-11-15 04:27:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c25b39d-6a89-3447-b1bb-43f302a49271 | -11.7122 | -48.87228 | 2025-11-15 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3be864e1-5c1c-3eec-ad60-b1528305d826 | -13.48466 | -46.72039 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88fd5eaf-ab62-383f-af1c-50c320b34b4a | -12.84861 | -46.45011 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 128fa9bf-d215-3b36-89ab-00f9eb2aeda9 | -13.06332 | -53.95831 | 2025-11-15 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d3366a5-07df-35ab-a3ca-3d0517e6808f | -12.43668 | -43.18696 | 2025-11-15 04:27:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9140d69-6b5f-3b57-a88e-80ba8185dc1f | -17.29591 | -46.82968 | 2025-11-15 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d65cd585-ec59-347d-9830-78bdf4530a1e | -11.84716 | -49.21067 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 961bb265-5674-3103-a41c-9b24185dba3b | -12.65959 | -46.74892 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1325c366-9983-3c89-8a13-c5ee3f46dda2 | -15.46094 | -39.23903 | 2025-11-15 04:27:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 535f837a-2211-3297-b825-06cd61584a92 | -11.91886 | -46.19815 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61fd3b83-c8b7-3831-af33-a0b009f2eed8 | -11.91749 | -46.19422 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6377ad2b-9674-3b2c-bcba-728dd4780cc9 | -11.71228 | -44.4494 | 2025-11-15 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51610eae-5b12-33b0-b6f6-4e5ca703487a | -12.4207 | -48.14098 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e66cbf2f-9490-3a51-b220-1d78aab15543 | -12.66293 | -46.74945 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85d99bb9-fe4a-3c44-a16c-6e4788c27ff4 | -11.70884 | -48.8717 | 2025-11-15 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f42a6a3-5da0-3358-80f6-c4c7227d3ef7 | -15.79082 | -46.60393 | 2025-11-15 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b47b2fa-1221-390e-bacc-85bce9498433 | -12.38822 | -48.11027 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1463b990-975e-39e7-a818-5e61816efa50 | -10.49866 | -48.02513 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd38c2f-c6d9-30ea-864f-281fa775c004 | -11.81151 | -45.28411 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b45150-3277-3575-a15c-082e9f70e92f | -12.3904 | -48.11788 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dc3beea-33c2-3c84-b1de-1160621994b3 | -15.36864 | -45.63795 | 2025-11-15 04:27:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8faa8012-ec0f-3012-8398-e9b686cccea7 | -11.31884 | -48.50658 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 156265cb-e881-31d6-b302-3ea989bd874a | -12.59753 | -48.37384 | 2025-11-15 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16430241-2adf-35e8-b77f-36ce3a3bdf0e | -11.71289 | -44.44524 | 2025-11-15 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b84e497-b3bf-3daf-9639-1c1963366a37 | -13.74229 | -44.16237 | 2025-11-15 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 969107e6-2d93-3383-a10f-bdf3aced0b2d | -11.70412 | -48.39079 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5cdfd3e-94ef-3dda-bd18-d502053a130a | -11.20334 | -44.66582 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efbc1bb9-7256-3c5a-90cc-6c05d5c5a455 | -14.85439 | -52.85901 | 2025-11-15 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7d3f880-d3fe-36d4-8c55-027408cf4bb5 | -11.32494 | -48.51129 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7025719c-ac1b-3e32-a330-f1564d80e494 | -10.6292 | -44.58912 | 2025-11-15 04:27:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30e2c360-5cc5-3502-8534-92da1f0e7020 | -12.77452 | -46.95089 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f9128dc-5703-3168-8262-a4043bbe995f | -12.23913 | -49.38991 | 2025-11-15 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 989b5735-bcdd-3148-8bf7-56af808a2bef | -15.31083 | -47.20675 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a98ca9e-730b-3d5b-8de1-08a6f58ac316 | -10.54418 | -47.99635 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a33f225-415a-38b5-a244-1e38768a7c35 | -12.25674 | -44.91873 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f78591b-0729-32bc-ae77-e47b9b9fbfd9 | -11.17048 | -48.13912 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eadfdec2-9e27-3c16-addc-562de7f2f73f | -14.85423 | -52.85711 | 2025-11-15 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77a5c4a4-8cfa-3a5c-87a8-a564205f0e12 | -10.44645 | -45.0788 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd56d593-4d4b-3545-a71f-a50b5955487b | -12.48127 | -43.73647 | 2025-11-15 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8085a077-c66a-30e5-9c06-e53c74895279 | -11.95629 | -44.85035 | 2025-11-15 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a1b83b8-674c-314e-98c7-a810ceb8e1b3 | -9.82283 | -49.77124 | 2025-11-15 04:27:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4dbe783-25b1-35da-9822-467596058c4c | -10.45106 | -45.07171 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8773ec0c-dd12-3894-af39-a614a152f480 | -11.92961 | -49.60588 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| babf2d59-7d52-3282-890a-33bb611279b7 | -15.34577 | -47.85913 | 2025-11-15 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc4b30d3-e3f3-3bc5-ae19-8a28876ac00a | -12.62286 | -42.39325 | 2025-11-15 04:27:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 26fc7d44-ad88-3cb3-99e0-5208034ce9d6 | -11.71408 | -48.87199 | 2025-11-15 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbedfb63-4de8-3b18-a158-913181d17fc8 | -10.56685 | -44.81267 | 2025-11-15 04:27:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b095166-90d3-3a4d-a7db-39428643e196 | -11.17324 | -48.14321 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5f68714-faee-3ca0-ac77-9db1f2c958ea | -15.34521 | -47.86271 | 2025-11-15 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07830661-7752-3cb0-859c-fd485517d8a1 | -11.84813 | -49.2261 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6247e04-f6f7-34ae-b6b9-476ddfd9e553 | -12.79313 | -46.38534 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4c0c892-b5d5-3586-84bc-10828f4927bf | -12.77397 | -46.95446 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94ccd755-c1f6-3acc-8e78-3764a4c94976 | -13.38455 | -49.0379 | 2025-11-15 04:27:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5b5e5cf-9606-38bb-bb48-201f0759d727 | -11.91693 | -46.19781 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1371c1ae-e761-30bc-bc52-8be0bab13bd2 | -17.15701 | -43.082 | 2025-11-15 04:27:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8794b8f-b752-3356-a515-e4484c2d78f3 | -13.95528 | -46.19738 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84f8765b-03ae-3556-937f-509ccf98cccd | -11.7534 | -45.34187 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef2a2c63-a4d1-33bf-84d5-f7d3eaef7531 | -11.84535 | -49.22181 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| cf4101ca-5496-3770-b62b-d2694977181c | -14.91161 | -47.37335 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b40dcf2-7e3e-3e4c-89c4-89467514e11c | -10.17307 | -49.31868 | 2025-11-15 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54ddd97d-0474-3fb3-b0ca-7d1e2b484a31 | -12.47208 | -49.57539 | 2025-11-15 04:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1f5f3f9-2b02-30da-986d-a870aa657a6a | -10.701 | -44.52147 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f014f81d-a1cb-30b4-a284-510a11ce5a25 | -15.47411 | -43.19162 | 2025-11-15 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bfc6d43a-6a71-3220-9f28-f272f3947027 | -11.32713 | -48.51905 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1c8ab3b-3c7d-3a1c-9ccf-023b682354ed | -12.90102 | -45.10476 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2267c9d2-7850-35d0-be48-2e92b5bed068 | -13.35594 | -48.20101 | 2025-11-15 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ea7cf0a-f312-3b10-a322-ffa612184fcb | -12.68071 | -46.76701 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 68b4ee72-95e0-30b7-99de-deba34894b85 | -11.62654 | -47.68633 | 2025-11-15 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a38bcec-64af-3a51-87c9-901248b9590c | -10.45047 | -45.07553 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README45.md)
