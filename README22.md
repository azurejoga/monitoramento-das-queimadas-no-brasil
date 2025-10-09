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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 250e00e6-8bd3-331c-8507-81d99a1d590f | -7.79321 | -42.41676 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 906573db-9de6-3374-85a8-e5315cf26560 | -7.6842 | -42.39302 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6f5d359b-86ef-301a-9a52-b8ffc65ebc85 | -5.13751 | -46.25597 | 2025-10-09 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d75d6f0c-38be-396b-b620-6ebd0a68a859 | -7.52384 | -42.7272 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ec6509a-b3af-3a72-b904-8da1feda68b3 | -6.72584 | -42.86909 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 98e8d5e6-c33d-34c7-ae2d-ebc2548aefad | -7.77202 | -42.40182 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 10c6377f-e8cf-3f7d-8d96-9412253cbf23 | -5.13252 | -46.25503 | 2025-10-09 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc2293d2-2713-32e3-8c08-5d1a4f7598e7 | -7.14513 | -42.17598 | 2025-10-09 03:57:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20e5283e-ae64-3ba9-a5fb-52a1bef3e81c | -4.97444 | -45.31624 | 2025-10-09 03:57:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5442afe2-af46-3558-a739-bf3dd70992ff | -7.53514 | -44.31885 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e23b8eff-111e-3985-8574-22518cec46fb | -9.61816 | -40.32896 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e18a1685-a95f-3dac-8469-cc69785b7732 | -8.50793 | -46.21297 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3f87fd9f-031f-3804-b328-9f0ee5e0854e | -8.63634 | -45.14077 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1886f78-c394-3294-bc2c-c4b273e0316a | -7.48605 | -42.72862 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4b797b9-a6c2-355d-8186-d87beb68fbfc | -5.65116 | -43.60678 | 2025-10-09 03:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| abc286d7-16a3-3253-8dfe-19f8aaf9f80c | -8.51048 | -46.17089 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e0b0d68-42f4-3285-91ad-49f0b986cb7b | -10.19558 | -44.5667 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d656c11c-c1ab-364c-9a46-2f73624e508a | -9.08489 | -47.95815 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4a04205b-e469-315d-bfab-70b6a36cfefb | -3.53907 | -48.92249 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cb1619e-9e84-36cb-bc6a-03a91862c35f | -7.69118 | -42.96929 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0fff937e-21e8-32f3-8f2c-6e289b2eae6e | -9.98604 | -43.59336 | 2025-10-09 03:57:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 141d1972-6ad9-3017-a6c0-4e4087c86942 | -6.69639 | -46.3105 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53a04304-43a8-34fd-8fc0-a18eed9fb6e4 | -7.50591 | -42.72696 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 5c2580e0-f7c7-3383-b0d6-d011e34d6efb | -5.67493 | -44.49597 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44330b7b-7bb6-3d96-945c-3b4ff8f02124 | -7.28989 | -41.97418 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e8578834-f622-3def-8af8-e58fab6fc591 | -7.78781 | -48.04491 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4c28a70-f563-32bc-86bb-6f07a01a69fb | -5.38841 | -40.98071 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 53a21c6a-0cf4-3eea-9086-4997c39572db | -5.39554 | -40.98189 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dda1ac84-e871-334e-a538-43e3953206a3 | -7.78646 | -44.18688 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 838c1719-f751-3dd2-97a8-c51e86509819 | -8.51088 | -46.22389 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9cc577ea-520a-318e-8283-025713698fd6 | -7.04867 | -37.68947 | 2025-10-09 03:57:00 | NPP-375D | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0108155-77cc-3a23-b605-8c0b2ea2de01 | -10.0906 | -40.77856 | 2025-10-09 03:57:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b13d23c0-f738-3b18-b95f-37039dd2d131 | -7.78044 | -44.24792 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 387e8473-9af7-36e7-b7f0-08d5d5cf5f81 | -8.62827 | -45.13714 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6445d4aa-7dff-3db9-b6f9-0c352f342115 | -5.90082 | -38.47622 | 2025-10-09 03:57:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7ae2e3bd-9a6d-3e61-ad5c-93a8d4752f96 | -7.78094 | -42.39412 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b3ff751-3bb7-3603-b0d3-0cdbbfb49b4a | -4.29245 | -44.52076 | 2025-10-09 03:57:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb988798-db29-335b-9258-070f8e4428de | -4.27425 | -48.88065 | 2025-10-09 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9fa54ec-51bd-33c9-85fb-cb33b4d0cc60 | -7.81022 | -46.71474 | 2025-10-09 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f5f64319-1fab-30e8-bfa0-107862d26649 | -3.38932 | -50.15121 | 2025-10-09 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7130673d-1115-30b5-b5ef-a712041a1db2 | -6.89413 | -47.34196 | 2025-10-09 03:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a757dfc-686f-3827-8ff3-2f8607cddfe8 | -7.17318 | -46.71715 | 2025-10-09 03:57:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2671e82-68e6-3517-b80a-8327aac677ee | -7.50209 | -42.72635 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6a766302-ffb2-3abb-a717-15811cc2a0fe | -6.28 | -44.30165 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebaed8b1-73d1-342e-9d99-80387aa41977 | -7.80126 | -44.20066 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b87be3c-f662-3cef-8758-cf50a70aeed4 | -3.10654 | -47.79425 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7724fefc-0862-3660-948a-bb0e202ef9f2 | -7.05482 | -37.69404 | 2025-10-09 03:57:00 | NPP-375D | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 01bf82a4-9a36-365c-8c5d-7122b7254fa6 | -7.67899 | -42.40145 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a91afb69-9554-3555-ac52-5a6a2e689071 | -6.38134 | -43.86392 | 2025-10-09 03:57:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b59ab870-7b45-3252-a161-d96c215c116c | -5.04914 | -45.62853 | 2025-10-09 03:57:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6469dbeb-3f25-3ae2-b7b1-e248480d95a2 | -5.35526 | -41.00447 | 2025-10-09 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 98e26f76-f836-318a-bbd4-b3b30b8fb964 | -6.79461 | -50.49267 | 2025-10-09 03:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b374bc21-44d2-3d0b-a974-74a0e44bddeb | -5.80595 | -44.67484 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81759f2e-74ec-33cd-80af-35efcc751437 | -7.7949 | -42.61241 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87a139cc-7a79-3266-83d9-5ebeb7db2908 | -7.79548 | -42.40339 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9a59f85e-226f-3fd5-976c-31994d51c283 | -4.72164 | -43.35331 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ffc4588-54ec-3349-b252-43fa5ff7f216 | -3.55779 | -39.11207 | 2025-10-09 03:57:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 95cb08dd-b06a-3165-baa7-fe9941d041a4 | -8.52958 | -46.20014 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7aa2f0d7-dc47-35ee-8f2f-8a59f46f1bef | -6.64626 | -40.87823 | 2025-10-09 03:57:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e0d66f91-2123-3cd4-9577-2d88df09501a | -7.17293 | -46.71827 | 2025-10-09 03:57:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70c4e586-1511-3fd1-96fd-1ad11ca4e986 | -7.46014 | -43.02875 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 873ac8ce-6113-3b21-ba90-c7eee3cdd5d1 | -7.01157 | -42.74615 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3cd550a5-6fb2-3f90-afbf-fa623c9513eb | -5.13656 | -46.26152 | 2025-10-09 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68d6e9a9-63ea-3e60-acae-899131437bbc | -7.80029 | -41.65715 | 2025-10-09 03:57:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 483a25f3-8a88-3b43-b166-d837ce12114c | -6.71313 | -42.14698 | 2025-10-09 03:57:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 36ea8cb4-fe5b-3dbe-9bff-c36bb8d29229 | -8.10376 | -39.47138 | 2025-10-09 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30591037-362d-37d7-87aa-10b7fbcd6f1a | -6.74307 | -42.83699 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| d43163ef-8977-3bfa-9ba4-283c7a56dca1 | -7.75757 | -44.0318 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3273aaba-1113-378a-89e9-e7547cdd2a53 | -5.65053 | -43.61052 | 2025-10-09 03:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27804b8b-df9d-334a-9842-64a2eac90390 | -4.61569 | -43.14781 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf65b4c9-2cba-33a2-96ff-6b0746eb6064 | -3.89158 | -44.91062 | 2025-10-09 03:57:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beebc4ce-1a6f-3ab0-a48a-6cd1d80fd42b | -8.82999 | -44.43038 | 2025-10-09 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2c0b4ae-5e3e-392e-be1f-5f3f25b87778 | -8.83478 | -44.42735 | 2025-10-09 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1741afee-8832-3e5e-8964-5688e93e4ae2 | -5.15463 | -46.0965 | 2025-10-09 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8212dcb-0470-3a56-9e12-64e4199b57e7 | -8.53812 | -46.20679 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| e7af8c6e-66c3-32b3-90ac-39128996d83e | -7.77626 | -44.2472 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2c12fb0-e209-3394-9299-f3a235c77580 | -7.42011 | -42.98169 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5c5b22af-bd92-396b-96be-7a95950e2d68 | -7.77429 | -42.41132 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fbea4580-251e-369a-84b0-0c3447c1e8a8 | -7.7944 | -42.40549 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dba9a622-e29e-36b9-bd20-e5c27d272468 | -7.6872 | -42.39814 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f56583f2-072e-34a0-9265-703fce76cc41 | -6.6995 | -46.2946 | 2025-10-09 04:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f8491205-462d-33f0-8652-2f52beee7189 | -8.1993 | -43.3424 | 2025-10-09 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 4be55fda-5e93-33ac-8dc5-4b9a03b74be3 | -8.5021 | -46.222 | 2025-10-09 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3a6e4c37-ef17-38a9-83e6-3cd556f6488a | -17.9227 | -57.4922 | 2025-10-09 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| c343ec14-b250-3b6f-98c0-a8a29458e5b9 | -6.6808 | -46.2961 | 2025-10-09 04:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| afba6bb5-d6c0-33a5-af64-0fa7bc67c049 | -17.9224 | -57.5128 | 2025-10-09 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 8b1f08e9-1425-34ff-b034-fbe2d6061509 | -9.0829 | -47.9594 | 2025-10-09 04:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ad88470e-88f4-361a-8d8b-bad4570afb92 | -13.29869 | -47.16964 | 2025-10-09 04:00:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6d8faf0-d629-3d85-8bd3-67487d7c3b43 | -15.22094 | -46.37886 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1ad28fd-396d-36de-9129-4b999cfa5645 | -11.2405 | -40.33913 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1dd74df-f994-3c7e-ac73-7125dd28da3c | -11.13055 | -47.73852 | 2025-10-09 04:00:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d45dfb1-7b1d-3e8b-9935-3b4f3028b8c8 | -15.49587 | -47.96416 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c04b6dae-000c-39f6-b21f-9c17fb94c2b8 | -10.85997 | -44.62373 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6a9b73e0-e24b-36d4-b78d-57511c69edc1 | -16.7515 | -43.97078 | 2025-10-09 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5c2d3a74-f017-30d6-830a-452a97e0b8f2 | -11.94216 | -39.99137 | 2025-10-09 04:00:00 | NPP-375D | PINTADAS | BAHIA | Brasil | 2924652 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8c065baa-2623-3823-9110-1c712c311172 | -16.19555 | -43.65858 | 2025-10-09 04:00:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81dfe122-16f4-3c42-adab-c9a8ff3855a7 | -13.79299 | -45.86641 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ebf07b-f0d2-3203-8840-75e5c2a93900 | -14.42038 | -43.98079 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c458e4d3-43a8-3eae-a840-52084ebe71a5 | -14.96251 | -42.85415 | 2025-10-09 04:00:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57ac485d-9533-3ebb-afd7-096290b5cfdd | -12.00017 | -45.18966 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
