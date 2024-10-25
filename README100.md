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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 858791e6-2e7c-331c-91f5-4297673fe32c | -7.27369 | -64.66316 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abee9b8d-b03a-3eca-8acc-37fe7572ba2c | -7.27018 | -64.65315 | 2024-10-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7d478b9-2086-3f8c-a964-63174896c1f1 | -1.1834 | -53.6569 | 2024-10-25 05:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5b770393-c9a9-35f0-ab47-f262da0a6be1 | -1.6062 | -53.3087 | 2024-10-25 05:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f9669921-1574-39f0-9690-1a4c005ba19f | -3.9581 | -46.422 | 2024-10-25 05:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5b94ee61-4d35-341e-8bf7-1111f729388c | -4.3165 | -48.63 | 2024-10-25 05:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 2b9d0b08-f020-3976-a150-4984d1b72f04 | -4.3351 | -48.6292 | 2024-10-25 05:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| f40aff43-2dc1-3683-98b9-9dc541a2d686 | -4.3536 | -48.6283 | 2024-10-25 05:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d73f47ce-c8a7-31bc-a22c-513c6016a1fe | -5.9788 | -45.3621 | 2024-10-25 05:05:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 5c8362a7-0371-3b26-a900-18919cef4646 | -17.92019 | -56.20432 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 840bd773-9ba8-35a0-94bd-e3cfde724850 | -17.88414 | -56.87513 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| d995ee0e-47bb-3a7a-a61c-d79b1f987470 | -18.33155 | -56.23265 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 150c680e-c9f6-320c-8f2f-95fc78367c28 | -18.33098 | -56.23664 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| fa1a5c7a-b93c-3677-b809-a9a622492d52 | -18.32752 | -56.23609 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2aedd457-c918-3d60-a4bc-875b0fc8d0e1 | -18.32694 | -56.24009 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f6a90135-55d0-3cb6-9e89-be7d9a59bf71 | -18.32348 | -56.23954 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b8838364-22eb-39b1-956f-1313b13b2fb1 | -18.31944 | -56.24298 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| b7426454-44c9-3105-854d-339c02d20618 | -18.31598 | -56.24243 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| be4c079a-c63c-38f6-bcdc-168fdf53f270 | -18.30848 | -56.24531 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a5edefd4-9094-316a-9572-015c1b3ecbbb | -18.30632 | -56.2457 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 52ae0e02-a5eb-371e-889d-cadb8723d3d1 | -18.30574 | -56.24969 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4532ac1f-1f43-3fdd-8625-ff88edc1fec4 | -18.30501 | -56.24476 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7cdb81a9-4286-3386-bd5e-2dd4e6409670 | -18.30444 | -56.24875 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 64e9935e-64b4-391d-9690-eafa3897b6c7 | -18.30286 | -56.24516 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b8af8198-b22a-343c-8bf5-7886f73191a6 | -18.2862 | -56.16488 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bca1d1a8-a2b0-31b8-b068-2abb4a4bc696 | -18.26356 | -56.0253 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c19536d3-b593-344f-9058-6dfbb9aa1696 | -18.26298 | -56.02935 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cbd00315-c126-33b6-ba67-ac53b6547fe5 | -18.25949 | -56.0288 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| db04d402-5acf-35ea-84e2-4f984447e1a6 | -18.25891 | -56.03285 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8012b852-fe51-322f-bc51-e84f900669b1 | -18.256 | -56.02825 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ec97e006-a3fb-3d74-ad82-83ed5f2e6c3c | -18.25542 | -56.0323 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a8dae1f2-8048-34a4-ac7b-84e0436cd5bf | -18.25484 | -56.03636 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a8cb40f9-8736-3a72-9c98-2407a80ac59c | -18.16972 | -56.29415 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e2ce9451-25bc-35bc-bc3f-5ff1699ceeed | -18.13883 | -55.9155 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 30b8612a-7877-3ab3-87a3-7d7181a1a2c5 | -18.13836 | -55.91283 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 722b0b78-7401-3781-8afe-d9150f017a57 | -20.63856 | -56.44407 | 2024-10-25 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a55aa5c-93d3-3944-8df2-1df621e4c2ec | -17.81677 | -57.60558 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 99976dd2-dbf5-3b23-a8f5-2fda337f6083 | -17.81344 | -57.60503 | 2024-10-25 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 319328fd-30c0-375e-b81a-e4e065e56091 | -17.77057 | -57.37629 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 2f18a52d-da63-3dd0-ab04-7738e47101d5 | -17.76947 | -57.36099 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| eedb848c-12a2-3eb9-b43d-84644d6bd6ec | -17.76723 | -57.37573 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 1b3f05c2-5ef4-3138-b69a-280435ce8fa2 | -17.76389 | -57.37518 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| d50bbf79-4fa6-3b9f-a32b-62473cf294bb | -17.69524 | -57.33756 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 73b7504f-e297-363e-951a-2f33ecc27597 | -17.69467 | -57.34124 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| bde0afcf-7c68-36b6-897a-723e24116218 | -17.69189 | -57.33701 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b64421aa-e210-3fd5-ad35-ff5e6d4bd0ea | -17.69133 | -57.34069 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ad8033eb-feaa-3e08-8172-5dfd1f3245cd | -17.69131 | -57.36335 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 16a91e09-35f3-3d4e-9f7f-c3c7064b3f50 | -17.69077 | -57.34438 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| eeadd90b-9106-3279-9efe-b05fe0edcded | -17.69021 | -57.34806 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d29052b2-9a98-3441-abf5-dc85feebd143 | -17.69018 | -57.37071 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4a9f928a-62a6-317e-9baf-cda346b1487c | -17.68965 | -57.35175 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| add5951c-9d61-31f2-be9e-6131cf68003a | -17.68684 | -57.37016 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0435270a-5011-3598-9a85-46da9a4e6392 | -16.13497 | -54.0164 | 2024-10-25 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da2232ad-374a-3bb4-bcd6-e7f6c01ebdff | -16.13489 | -54.01416 | 2024-10-25 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80130165-c1b0-31f8-b067-3cdecdb74908 | -16.43914 | -55.9117 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c2feab9d-bf73-3501-a487-5d05378b3493 | -16.40638 | -55.91858 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 450000ad-ac52-3b38-8fac-560d0e4246df | -16.40376 | -55.91872 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 629a8ffa-5b03-37bc-8b76-e8ae032b2e56 | -15.66728 | -55.97792 | 2024-10-25 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 42774f46-b106-3c8e-8b7c-ef7fb35f6681 | -15.66671 | -55.98175 | 2024-10-25 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 13a946e3-2032-3811-81b9-8d64c2dc3746 | -15.65701 | -55.97631 | 2024-10-25 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 724daf28-363d-36a4-87ed-1ed36e0d255d | -15.65645 | -55.98015 | 2024-10-25 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 620d2dda-60c3-39d5-b01b-4dd03810e74c | -17.22511 | -56.69864 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f6081c5a-ec23-3017-961d-f5ca0b661370 | -17.22511 | -56.67545 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b19c709c-2423-30a5-bd03-904a96a7261f | -17.22454 | -56.67922 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 99f1d32e-5124-3833-96bf-097858beb822 | -17.21551 | -56.67004 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5d95cca2-f742-3b5a-8afc-8ef4dbbd8d96 | -17.21494 | -56.67381 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 82f0427d-d247-3ab4-a4e8-bffb817e2ba8 | -17.21212 | -56.66949 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bfc8ef33-c3be-391f-bbdf-68fb6b081bc3 | -17.21156 | -56.67327 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 44324b58-411e-3484-ae41-b136099c73dd | -17.20873 | -56.66894 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d1f1e349-e22d-3980-b07a-509f7365c0ad | -17.20817 | -56.67272 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2bca1c37-7228-3c63-942e-c267892bddba | -17.03208 | -55.99605 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 694a1b01-c613-39f1-9cbc-54b718e23003 | -17.02978 | -55.98762 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d253529a-3eb0-3434-ae06-4c60bbb4a494 | -17.02862 | -55.99551 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3504c6ba-dbd6-35ba-b936-7859490f65e0 | -17.02745 | -56.00339 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9d1e2dd6-c79e-3497-924c-3baed29a64df | -17.02632 | -55.98708 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d606078a-115f-39ba-ac8d-d272c50c4741 | -17.02574 | -55.99102 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 36b9e0d1-4df3-3b0f-8b20-797e4611dfd2 | -17.02516 | -55.99497 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c4766fb-5837-3f7b-ad50-b044619fb323 | -17.024 | -56.00285 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a0a8d772-9e72-323a-ab49-d4957255939f | -17.02342 | -56.00679 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4e96883e-4617-3a5a-b1a8-d6ac8feba049 | -17.0217 | -55.99442 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5bc5b26a-ce46-3673-90e3-079a7c19d179 | -17.01996 | -56.00625 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 94d3145a-49d3-3007-a20f-b6714b93f377 | -17.01708 | -56.00177 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 6f0d04ae-7ccd-3a54-8cf3-1132bdf4f549 | -17.01651 | -56.00571 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 8ed7737c-3692-3d91-a3ed-82b63a362c9d | -17.01363 | -56.00123 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f4d9b94a-20c8-3e2e-a1fc-3af0cc47d1aa | -17.01305 | -56.00517 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9472969d-5c48-3f67-aee4-1e2cb20594f3 | -16.56526 | -56.24315 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7c9ce53a-d30b-3795-9b28-fc7dfebcabd5 | -16.56469 | -56.24698 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5a86535e-ca33-3f4e-8a0e-17c4c2863570 | -16.56411 | -56.25082 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 026050d1-5b86-3369-b61b-bcd039c1de7a | -16.56184 | -56.24262 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 87838bf2-84e5-359c-98da-0916e2b3d5bb | -16.56127 | -56.24645 | 2024-10-25 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8572507f-cd59-3a57-8a90-c32463730aa7 | -17.24887 | -57.50574 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3c805849-374b-3e6a-8503-5cb89b3e9e21 | -16.60505 | -57.07613 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 778f06d9-0424-38eb-b653-cb8557822aae | -16.60226 | -57.07192 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9f9c2223-73d7-30bf-804c-89f76c04fff6 | -16.6017 | -57.07558 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bef844a7-95c9-3607-94c6-1054c3b041f7 | -17.30829 | -57.47067 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 495cc9b4-e67d-336e-a940-1493c0b6a6ec | -17.26055 | -57.5151 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 4570bcbe-4c6b-3041-87bc-a51089500892 | -17.25722 | -57.51455 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ea1fcf70-69a1-3d9c-80a6-fc432be99f61 | -17.25556 | -57.50307 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| cbd572f0-62a5-3e8c-84cb-0d9b9fc29e84 | -17.255 | -57.50672 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| f7a6297f-6b37-35cf-857d-b4b7b5bef85d | -17.25223 | -57.50252 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |


[Clique aqui para ver as próximas entradas](README101.md)
