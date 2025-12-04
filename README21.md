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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d100ae6-9f09-3dd2-857e-a3f7d4572d0f | -19.61866 | -56.84021 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 29eda4f5-d585-3f65-bf4a-482cdb0f7f1a | -19.62911 | -56.84649 | 2025-12-04 05:14:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 97450e81-772a-3161-9e58-bdcde381486f | -21.6278 | -56.13129 | 2025-12-04 05:16:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 338b5749-c031-3c78-9f1d-109e0f95021f | -21.62682 | -56.13266 | 2025-12-04 05:16:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bb7bf275-d3ad-3ac7-987d-9c19814b8f2f | -21.62387 | -56.1307 | 2025-12-04 05:16:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9ddf6040-b317-3a37-9942-59b18ea98814 | -21.53668 | -57.51927 | 2025-12-04 05:16:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbc896de-ea05-303b-ae6c-34d1c594c1fb | -21.62709 | -56.13671 | 2025-12-04 05:16:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2739e927-552b-30c7-a5ce-f6af64f8a039 | -21.62288 | -56.13207 | 2025-12-04 05:16:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5a1c64a7-8518-3a81-9cf3-78e0c9f7fc57 | -21.62316 | -56.13613 | 2025-12-04 05:16:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1114360f-3695-38a2-bbac-404a636ec6fa | -4.40234 | -43.12958 | 2025-12-04 05:25:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| dc9c3da5-59cf-3d93-b3d6-55d3589c5378 | -4.38882 | -43.12746 | 2025-12-04 05:25:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 96c4712f-15f7-3161-8b55-b1fc02922c3e | -3.9049 | -42.8962 | 2025-12-04 06:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 125a1dc7-3c54-3af1-aeed-4da5cd75fee4 | -6.6765 | -38.0668 | 2025-12-04 06:40:00 | GOES-19 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 87.3 |
| feb88462-74ba-3c2d-b2f7-bbee9a8dfe8e | -6.6762 | -38.0926 | 2025-12-04 06:50:00 | GOES-19 | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 76.7 |
| e2d53113-be08-3b62-a801-cf8d1a7e29c4 | -3.9049 | -42.8962 | 2025-12-04 06:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 33ce36db-d712-33cd-9de2-ebee70e7e80d | -6.6575 | -38.0689 | 2025-12-04 06:50:00 | GOES-19 | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 73.1 |
| b6b5d1dc-f862-3442-9668-1ad77aeeeeb6 | -6.6765 | -38.0668 | 2025-12-04 06:50:00 | GOES-19 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 4d9643a3-9165-3803-8a06-c5c27d9ab63c | -6.6762 | -38.0926 | 2025-12-04 07:00:00 | GOES-19 | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 5dde02e5-3eb4-353c-824c-a66d6debec25 | -6.6765 | -38.0668 | 2025-12-04 07:00:00 | GOES-19 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 154.4 |
| 878388aa-551e-39ab-bc47-5c1f1e6650d6 | -6.6575 | -38.0689 | 2025-12-04 07:00:00 | GOES-19 | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 018339e3-cd3a-3ffa-858b-ad47fe96dec3 | -20.91985 | -56.36573 | 2025-12-04 07:07:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e92b3532-e7dc-39fb-a31b-5d24da076a57 | -20.91595 | -56.3578 | 2025-12-04 07:07:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 70892794-b899-32ed-99ae-28f0c9fbb9eb | -6.6762 | -38.0926 | 2025-12-04 07:10:00 | GOES-19 | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 01d63bf8-4f32-3eca-9897-172de033c00a | -6.6765 | -38.0668 | 2025-12-04 07:10:00 | GOES-19 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 163.4 |
| e833450c-a9b4-3304-a257-c21f14bb189e | -6.6765 | -38.0668 | 2025-12-04 07:20:00 | GOES-19 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 150.7 |
| 50017b35-9a1d-34ab-bb9f-a85a25717c74 | -6.6762 | -38.0926 | 2025-12-04 07:20:00 | GOES-19 | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 6beb9339-739b-35eb-b80a-0d06ec1c55f7 | -4.4079 | -43.1252 | 2025-12-04 07:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 150ef810-039b-3401-b92e-4f87e3c72a32 | -4.4079 | -43.1252 | 2025-12-04 07:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 3f335c2d-657f-35c0-988f-4f150bae9e12 | -3.0722 | -45.2307 | 2025-12-04 07:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4ffd50de-a4ff-38c4-b86a-760144d7460e | -2.9242 | -45.0783 | 2025-12-04 08:50:00 | GOES-19 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| d5b796ff-88cb-33d8-bec9-25f02650e903 | -2.9243 | -45.0557 | 2025-12-04 08:50:00 | GOES-19 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| c650a1ba-a491-3b38-b121-27921bdf2167 | -6.37557 | -37.76193 | 2025-12-04 11:17:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 2cb30949-8347-3be2-a321-e16be829d26a | -8.01787 | -37.59377 | 2025-12-04 11:17:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c95113cf-e31c-304d-ba2a-406c9614a91e | -8.01589 | -37.60655 | 2025-12-04 11:17:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 20.0 |
| da424dac-c7a9-34a8-9584-591ffe3511a6 | -7.37326 | -37.32919 | 2025-12-04 11:17:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 9dc6e290-3fe9-3039-a58e-75647a7701d2 | -6.71502 | -38.40884 | 2025-12-04 11:17:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 17.7 |
| e1283335-483e-3d8f-b8e1-2bc9b6af6399 | -8.34121 | -35.40402 | 2025-12-04 11:17:00 | TERRA_M-M | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| c9ba92bd-724d-3b3c-944e-b311038f8f82 | -8.37549 | -35.36101 | 2025-12-04 11:17:00 | TERRA_M-M | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 4b4e30f3-1a00-3b50-a206-a23191fedc74 | -8.0084 | -35.66484 | 2025-12-04 11:17:00 | TERRA_M-M | CUMARU | PERNAMBUCO | Brasil | 2604908 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 7be56e7d-dd15-3c26-8bc3-784ce6d6126f | -9.66281 | -37.1707 | 2025-12-04 11:19:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 2554bfda-4538-331e-a828-e3ea61813ee4 | -8.28391 | -36.85815 | 2025-12-04 11:19:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| a8be173c-0365-3af2-a4eb-da967f2af76f | -9.5574 | -37.12494 | 2025-12-04 11:19:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8c3ccc73-21a6-33fb-ad2a-37a05e78ae7e | -9.66456 | -37.15931 | 2025-12-04 11:19:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 17.0 |
| a46fc6c5-d999-36d8-bc0f-7ed0e73f56ab | -4.4079 | -43.1252 | 2025-12-04 11:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6b346e3f-3d20-3a12-8235-7d4f4bae3c20 | -4.3892 | -43.1263 | 2025-12-04 11:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| bbe2a465-32fb-343c-b0bf-deb54a164620 | -4.4079 | -43.1252 | 2025-12-04 11:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| c1248e98-7ea7-3d34-8ec3-cf93246e1186 | -4.389 | -43.1497 | 2025-12-04 11:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9dbcf17b-c3d8-35c3-a436-ff18ed07c7bb | -3.686 | -42.0108 | 2025-12-04 11:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| ca3580e0-53ce-3f3a-b67f-6ea6cdef70d8 | -4.3892 | -43.1263 | 2025-12-04 11:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| f8cac60e-ddce-306a-a596-cf36b42d587f | -4.4079 | -43.1252 | 2025-12-04 11:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| a7a0ec0a-2acd-37e5-8f6e-b10b7efc4af5 | -3.686 | -42.0108 | 2025-12-04 11:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 80742899-4c84-395e-9179-30c5f16a61fc | -4.3892 | -43.1263 | 2025-12-04 11:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 7e4f0eb9-9ae9-3615-a5eb-4a6d2af1b412 | -4.389 | -43.1497 | 2025-12-04 11:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| a255ba0e-43ae-3251-9bd0-bde16a2269cc | -4.389 | -43.1497 | 2025-12-04 12:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 6fdf4aa6-73ef-3f12-b1fd-bf1f5e12da04 | -3.686 | -42.0108 | 2025-12-04 12:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| 42b8fd77-a55d-3209-8f1a-f051546bb5ae | -4.4079 | -43.1252 | 2025-12-04 12:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 077d8e67-d2c3-3ed3-8d41-239e4b14f4e4 | -4.3892 | -43.1263 | 2025-12-04 12:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 227.1 |
| df810c85-ff2a-3ed8-a41f-f089131eb468 | -3.686 | -42.0108 | 2025-12-04 12:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| ed84bbf5-7180-3aab-8d8a-be9604119909 | -4.4079 | -43.1252 | 2025-12-04 12:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 0fe59e2b-9429-37d7-aff5-eff92bac138a | -4.389 | -43.1497 | 2025-12-04 12:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 176.6 |
| aed2d6f9-113a-33a5-bc67-9244d075cc0d | -4.4077 | -43.1486 | 2025-12-04 12:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 5ae348b2-9f3b-3ff3-ad58-834f4096d8ca | -4.3892 | -43.1263 | 2025-12-04 12:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 228.4 |
| a809211d-4c5a-37e1-a3c9-294f3fea53a6 | -3.4641 | -41.5925 | 2025-12-04 12:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 1fa71eb5-0be2-3d4d-86bc-5b941b1d2fea | -4.389 | -43.1497 | 2025-12-04 12:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 50739167-49b5-37d7-adfd-e72150e713b8 | -3.686 | -42.0108 | 2025-12-04 12:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| a3d66aa6-ad9f-34cd-a384-0f6802b7d1a5 | -4.4079 | -43.1252 | 2025-12-04 12:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 7afdef0e-acfb-3f79-8f93-03c73376015f | -4.4077 | -43.1486 | 2025-12-04 12:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| aeba97d8-8b88-3013-8b0f-64bba96bf42a | -4.3892 | -43.1263 | 2025-12-04 12:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 338.9 |
| a9776c8a-4fd8-3210-a8d7-837ac80d80a6 | -4.389 | -43.1497 | 2025-12-04 12:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 989c1c1c-ac1a-3548-b941-70de562b4f64 | -4.4077 | -43.1486 | 2025-12-04 12:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| aaef527b-1e78-3aae-a2b5-ed9942d6cc20 | -3.5921 | -42.0869 | 2025-12-04 12:30:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 4fafe29b-fd3b-3120-afe4-5c533acdbd50 | -4.4079 | -43.1252 | 2025-12-04 12:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 99814a72-df1b-334f-903c-ce9989eb97a8 | -4.3892 | -43.1263 | 2025-12-04 12:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 49401130-840d-3ff4-a45c-2e76f8082e8d | -3.686 | -42.0108 | 2025-12-04 12:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| bc015943-90fd-3129-a2d8-95aca977802a | -3.686 | -42.0108 | 2025-12-04 12:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 175.8 |
| 957e25b8-e7e2-36ae-bc36-3df46cfd49e0 | -4.4079 | -43.1252 | 2025-12-04 12:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 5f0ce1cb-086b-35bd-b66f-0caf10638c51 | -4.389 | -43.1497 | 2025-12-04 12:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e470e4b7-7ece-3559-8173-edbf4907a5db | -4.3892 | -43.1263 | 2025-12-04 12:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 4a618f99-1444-3d16-8375-9fd36f539f34 | -3.686 | -42.0108 | 2025-12-04 12:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 2188fa0d-5df9-3cb7-b7d1-6492407904a3 | -4.389 | -43.1497 | 2025-12-04 12:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| a8ac6e06-f104-35a3-8387-bf87ce370c15 | -4.3892 | -43.1263 | 2025-12-04 12:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 877df030-c96a-3ab2-b82e-93e7839c4d19 | -4.4079 | -43.1252 | 2025-12-04 12:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d064e2c1-6115-3102-946a-87f23f558efa | -3.0692 | -42.0164 | 2025-12-04 12:50:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 0ece244f-e959-3287-88e0-16024360dbef | -3.4275 | -41.4504 | 2025-12-04 12:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 343da2aa-93b1-3fa7-8ca0-6670be7ac252 | -3.4462 | -41.4495 | 2025-12-04 12:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 0243e183-0f52-37c0-8fb4-2ccb205c06e8 | 0.40849 | -50.75248 | 2025-12-04 12:55:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 28.9 |
| f53a95d1-8e75-39ab-909f-f95cb4908580 | 3.46264 | -51.25309 | 2025-12-04 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 614539da-bdf7-3e37-85c5-82699bc5e95b | -0.39187 | -52.04733 | 2025-12-04 12:55:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| fadc19c3-089d-3f41-b99b-9ffb2af37487 | 3.47377 | -51.25147 | 2025-12-04 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 08bfa212-af8f-31f5-8bbd-aeedcbb48b6b | 3.67404 | -51.28386 | 2025-12-04 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e030ef4c-0fa0-3834-adc4-194f2d5ee738 | -2.1437 | -47.87897 | 2025-12-04 12:55:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 476192c4-5793-3f2a-96a2-c23ecdbf7519 | -0.3807 | -52.04586 | 2025-12-04 12:55:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 40c7bd8a-c0f4-3300-b5b3-f1466c318820 | -2.13576 | -47.88366 | 2025-12-04 12:55:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1037c09f-e75e-3b16-9e38-6b69d044a443 | 2.9198 | -51.00025 | 2025-12-04 12:55:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 471ee4aa-7ef5-3012-a7c7-1682d4376fa5 | 2.91963 | -51.01035 | 2025-12-04 12:55:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 4ba6f8e4-6ed5-3189-9831-9f4e74502353 | -0.02664 | -51.38654 | 2025-12-04 12:55:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 177e7d4c-ff75-3dcf-8e1e-f52b6a4a5824 | -0.38979 | -52.06194 | 2025-12-04 12:55:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| cc288681-09f7-39b7-a38a-778955315ee8 | 2.91729 | -50.99488 | 2025-12-04 12:55:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 537b3ab8-5791-33bd-a955-981d51b80f93 | -21.62672 | -56.12751 | 2025-12-04 12:59:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9018b0b2-fd1d-3ef6-87a3-2d479584f6c1 | -20.23391 | -56.89662 | 2025-12-04 12:59:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |


[Clique aqui para ver as próximas entradas](README22.md)
