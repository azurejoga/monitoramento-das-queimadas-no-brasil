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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3c73d36-b747-3c67-916b-0d6274949f9c | -10.2773 | -47.611 | 2025-07-14 00:00:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 052b90ef-2dbe-3243-b625-78a25c828a9d | -8.5022 | -43.3085 | 2025-07-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| df106838-bc37-348e-816e-408752f3f6ec | -8.921 | -47.3595 | 2025-07-14 00:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f6334565-0fab-3ed6-bbc2-d9e03066c117 | -8.5211 | -43.3063 | 2025-07-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3682d3e2-4505-32a5-92a3-80cd926a936c | -3.581 | -47.5149 | 2025-07-14 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c2c6627a-1149-3a51-916f-a9ea53a5f2e6 | -8.9021 | -47.3614 | 2025-07-14 00:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f2ba4335-7435-3724-86eb-425bc429c050 | -8.9213 | -47.3374 | 2025-07-14 00:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6223d199-647e-3945-a762-0f3ea89add9b | -18.9141 | -41.95396 | 2025-07-14 00:03:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| 5e820df8-d18f-308a-9372-12f30e0b7fcd | -18.92151 | -41.96048 | 2025-07-14 00:03:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 6e856037-6bdb-3995-a537-8e1550510236 | -18.91999 | -41.94725 | 2025-07-14 00:03:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 44759ce5-33ea-3f53-acc7-7dbe169b670c | -17.81987 | -40.19477 | 2025-07-14 00:03:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 0cde96b9-68f0-3d67-9f51-9ecfd53243e4 | -9.50324 | -47.55952 | 2025-07-14 00:05:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| aad16dd7-a29b-32ef-98a5-f2968cf8c729 | -8.90451 | -47.35752 | 2025-07-14 00:05:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| eaeb78dc-e5c5-3e05-95d1-38439ec77752 | -7.32074 | -39.85896 | 2025-07-14 00:05:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 295d8107-9501-356d-9cc2-dbc44b99a908 | -10.28789 | -47.63657 | 2025-07-14 00:05:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 85c830a5-5358-34fc-a4a5-4d083599efcc | -8.50857 | -43.31052 | 2025-07-14 00:05:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| 5d053a45-36b9-3006-a095-6a0feea1fc22 | -8.91814 | -47.35563 | 2025-07-14 00:05:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| bcae0a64-29c7-337e-a75f-d0fc05a89bd6 | -8.51696 | -43.29797 | 2025-07-14 00:05:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| b039ad72-6599-3d69-8e8d-b9ef4f33d066 | -7.31186 | -39.86024 | 2025-07-14 00:05:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d9def78c-498b-3bd1-abae-4fb206eed90f | -8.51845 | -43.30918 | 2025-07-14 00:05:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ac46b0e7-25c4-3826-96db-823e21866985 | -7.58298 | -44.73558 | 2025-07-14 00:05:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8aa87ce8-63bb-351d-ba30-ecf65aa170dd | -10.28499 | -47.61125 | 2025-07-14 00:05:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| e7e3afa3-66b0-39b8-b15a-cba76d15a2e8 | -8.91537 | -47.33286 | 2025-07-14 00:05:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 7df1885a-943e-35aa-bfca-8be742e0f93d | -8.50709 | -43.2993 | 2025-07-14 00:05:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 158d7252-5c29-3cd6-8e09-8d213a3d9f49 | -8.25088 | -41.92948 | 2025-07-14 00:05:00 | TERRA_M-M | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 0f17a303-3708-389c-a823-1938b1af8b27 | -9.16717 | -43.35229 | 2025-07-14 00:05:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 56bd4b40-6a3a-35fc-bb40-9ec1a786145e | -10.28163 | -47.61699 | 2025-07-14 00:05:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 57a92a44-031a-39c5-a260-a46ab4506f45 | -11.59499 | -43.20455 | 2025-07-14 00:05:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1231f437-82c8-3af9-9a8e-622ff1457f5b | -8.24173 | -41.93075 | 2025-07-14 00:05:00 | TERRA_M-M | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 58b9f683-c01e-3e99-b407-65dba62d0f91 | -9.362 | -40.42105 | 2025-07-14 00:05:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 04d72474-9b54-3d17-a707-88db44891ff4 | -12.762 | -44.40939 | 2025-07-14 00:05:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 39f02a36-620d-3cae-a1df-e228d2661aa4 | -4.86357 | -43.22598 | 2025-07-14 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4c27430e-b722-320a-93a5-21e5eae8d193 | -5.28705 | -44.88484 | 2025-07-14 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 953d6883-1d77-327e-80eb-6d22d532c81f | -5.62684 | -44.36078 | 2025-07-14 00:07:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| b94224aa-de44-3684-b049-d838ef9fda28 | -6.84478 | -42.76832 | 2025-07-14 00:07:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 82abbd39-9a76-3569-ba05-e11f44674739 | -5.2502 | -39.48073 | 2025-07-14 00:07:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2a9667df-0122-3761-b121-c47e6b30ecc0 | -7.26717 | -45.30576 | 2025-07-14 00:07:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| c4f8d6f4-ed1a-3e71-a381-a66caff3e72a | -5.16108 | -37.68622 | 2025-07-14 00:07:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 4f6024a3-ca91-3e49-8e90-734d80f2b649 | -5.24169 | -40.87202 | 2025-07-14 00:07:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b478a966-d6ea-38b2-ad8b-f5e6339e5461 | -3.57748 | -47.52934 | 2025-07-14 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5c333cb3-c60e-3705-b39c-5aa51fd0bfba | -5.27152 | -45.13319 | 2025-07-14 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 389123b1-f69d-3a57-b349-39667d3f3090 | -5.73817 | -39.54454 | 2025-07-14 00:07:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1cc0d300-e3d9-380e-a4bf-2a78c3553448 | -6.96107 | -42.73618 | 2025-07-14 00:07:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 1f540d25-0e54-3fcc-9e41-bdd95485d681 | -4.50824 | -38.54843 | 2025-07-14 00:07:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f89e1ade-f2d4-3a24-8cf0-8a2b9dde3a11 | -7.26905 | -45.32054 | 2025-07-14 00:07:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 24fca997-5950-3c07-a380-fc496ccdfbd2 | -3.57486 | -47.51006 | 2025-07-14 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ef842956-0aa5-3435-bf5b-518dbe66f8c5 | -3.58751 | -47.50835 | 2025-07-14 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| fe1c172c-7c0a-365d-96db-f0a9bbc52e52 | -6.94232 | -42.73872 | 2025-07-14 00:07:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 6059be7b-b0fd-3c6a-ac98-982d9097dcfe | -3.59015 | -47.52762 | 2025-07-14 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 0f464eae-fdf1-3d9a-b7c4-c13655b795a0 | -2.91572 | -48.2445 | 2025-07-14 00:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ddfe957a-4ed2-3d0d-87b0-e5f1e3a47682 | -5.27651 | -44.88625 | 2025-07-14 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 73e95fc5-7d2d-3e96-8e9e-c36ca9dc8835 | -5.46748 | -44.86113 | 2025-07-14 00:07:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b2a8b228-6f0f-30e5-9baa-45e6fcc2d82e | -3.59072 | -47.52103 | 2025-07-14 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 712e0205-443e-3294-acf0-e725d12e30f8 | -4.24513 | -46.63791 | 2025-07-14 00:07:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 98bdbf9a-b5b5-386e-818b-d4d4101a1519 | -4.51932 | -38.55748 | 2025-07-14 00:07:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 89931327-55cd-3113-91ff-7156844c50e1 | -4.51782 | -38.54702 | 2025-07-14 00:07:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 927f01db-bbb0-3c28-afd2-2c3ed21f18ec | -6.96242 | -42.74616 | 2025-07-14 00:07:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ecaf0776-e012-3c46-9ecb-c47d4529eaa5 | -6.84612 | -42.77838 | 2025-07-14 00:07:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 37e11be2-90ef-31ee-8d2e-839797165865 | -3.581 | -47.5149 | 2025-07-14 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c63730f5-2bfc-32e8-be2b-2ee22b725dc9 | -10.2773 | -47.611 | 2025-07-14 00:10:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f5310b59-e17c-3283-9ba0-af96a11d6b8e | -8.9213 | -47.3374 | 2025-07-14 00:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6e65915d-4b4b-381e-99a4-7b96ece6687c | -8.921 | -47.3595 | 2025-07-14 00:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 050c7b4e-5c8a-341e-91b4-79ce71bb0fa3 | -8.5211 | -43.3063 | 2025-07-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 307941e6-a5ce-360f-bbd5-519dd25e7170 | -6.0923 | -47.3129 | 2025-07-14 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e27cecb0-57ef-3f43-9107-c227a40eb365 | -8.5211 | -43.3063 | 2025-07-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 898df12e-387f-3a5f-8c11-f2bc3e31859f | -6.0925 | -47.291 | 2025-07-14 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 924a3dfc-672d-3c86-b13b-8ac09dc82cfb | -10.2773 | -47.611 | 2025-07-14 00:20:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a7eff1bc-e6e8-3a48-ade7-163dd4d41e4f | -8.5022 | -43.3085 | 2025-07-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 60a3def8-1a21-3832-acdf-7e1ba9d61ff8 | -3.581 | -47.5149 | 2025-07-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 63f5e1d8-0734-3b2d-b88e-7b695726759a | -3.5809 | -47.5367 | 2025-07-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9c88e077-afe5-3197-8d16-6bafa03f8567 | -6.1112 | -47.2897 | 2025-07-14 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| cc347fce-9bd2-352a-b5eb-9f7f0df96567 | -8.5211 | -43.3063 | 2025-07-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9f2a0b78-7989-3516-9fc8-7507027981a2 | -10.2773 | -47.611 | 2025-07-14 00:30:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7f483c41-eff5-3a92-86fc-a0971001e505 | -8.5022 | -43.3085 | 2025-07-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 8f57937e-c125-3981-9c18-eae7fbacd90b | -3.581 | -47.5149 | 2025-07-14 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 273b89c6-beae-3376-b81e-0b59221bf974 | -3.5809 | -47.5367 | 2025-07-14 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3b9cc0cd-37d7-3655-aed3-388084a88262 | -3.5884 | -47.5187 | 2025-07-14 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbc9ba4e-3b6f-3683-ba6d-6077d83c5a01 | -3.5758 | -47.508801 | 2025-07-14 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 431026f3-6a36-3361-8b37-dfe765f5f146 | -10.5844 | -49.144901 | 2025-07-14 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae540cd9-78ef-3384-aa14-029478400e4a | -7.2493 | -46.9841 | 2025-07-14 00:31:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7ec1077-a893-3eb2-89fa-970399847b71 | -10.284 | -47.601601 | 2025-07-14 00:31:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91d62ec4-0c4e-3fab-b237-6e6adefc9872 | -8.0409 | -50.102402 | 2025-07-14 00:31:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b73f6cdd-2231-3353-82ec-ff350c67efb1 | -8.9112 | -47.3396 | 2025-07-14 00:31:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e858291e-f811-38d8-9707-f42c048096e2 | -7.2704 | -45.315399 | 2025-07-14 00:31:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1a0f03e-b6a6-3870-bfd3-de13eaf0c593 | -9.4985 | -47.5532 | 2025-07-14 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14da9599-7e7b-318e-95ee-de52e80ea8ca | -13.1 | -47.282799 | 2025-07-14 00:31:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 037feb56-d7a6-3bec-be91-6d5c1576584a | -4.2454 | -46.638199 | 2025-07-14 00:31:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5c115dc-7bc5-3e41-823b-5faa95739cc9 | -10.2743 | -47.604 | 2025-07-14 00:31:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab1b59b5-b849-382d-8595-722587dcc5e3 | -9.4686 | -57.305599 | 2025-07-14 00:31:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07f53725-fc8d-35bd-9bb7-50a1f2d99836 | -23.0909 | -54.177101 | 2025-07-14 00:31:00 | METOP-B | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98aef67a-a1f0-3c15-a5f0-40c62be52c8e | -2.9117 | -48.2351 | 2025-07-14 00:31:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a20df9ad-cb6e-3131-9c0c-2cc8c97bd6ae | -6.7534 | -50.9188 | 2025-07-14 00:31:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d308e1d-983d-35c3-9ff8-f45a20354229 | -7.2571 | -45.302799 | 2025-07-14 00:31:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e31ca9a1-ac5f-3353-b065-d48423bfe1f6 | -23.0889 | -54.166 | 2025-07-14 00:31:00 | METOP-B | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c1e1101-758d-3b92-b7b8-8c72af363432 | -9.5009 | -47.563099 | 2025-07-14 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fcd7d4c-1a26-3afd-97a6-575f417e4f2b | -8.5126 | -43.304298 | 2025-07-14 00:31:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| be0e9bdb-3827-36a0-9abe-9c186d476eb4 | -12.5648 | -52.2117 | 2025-07-14 00:31:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73c81cfb-e168-3249-8988-5f9544c5ed81 | -8.5077 | -43.284599 | 2025-07-14 00:31:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 25e8d549-62b2-380d-bf98-5ec07139bb1e | -21.491301 | -54.251099 | 2025-07-14 00:31:00 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d13c1e40-468b-3662-9f38-a1c3ffeb2963 | -8.0426 | -50.1101 | 2025-07-14 00:31:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
