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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 623db081-e73c-3833-88b3-a4838df1c8d4 | -11.61172 | -64.08042 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4224aeb9-5149-3339-9ecd-2e6a58c3b9ae | -11.61172 | -63.67831 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d1e42bd1-19fd-30a0-8073-1a6db086a93a | -11.61151 | -63.7235 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7b2e397-5d1d-32d7-97ae-2cf7680049ac | -11.61124 | -63.94747 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14b4d5b4-cb46-3963-b6ae-d3bd6557bbdf | -11.61093 | -63.68292 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca52556-8065-3d5d-a410-1d002148abf3 | -11.61075 | -63.72793 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a357b0a6-3e8e-34c3-93f1-4f6fc6617256 | -11.61003 | -63.82051 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb81d087-dd78-3bf4-a19a-1e6532f069f4 | -11.60887 | -63.72458 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9763ec35-62d4-37ae-aa98-da8089fb19f7 | -11.60883 | -63.67936 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4d8aaae-4c75-3171-b8c6-361ce7f07efe | -11.60784 | -63.72277 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7c77748-19a6-37de-888c-209b64db6e66 | -11.60519 | -63.72385 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8fb82603-251c-3d68-9db5-f8954c19cf15 | -11.60367 | -63.71022 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0e270a4-c590-39c8-98e1-de45f4de2613 | -11.59852 | -63.76381 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1c1fa28-5495-378b-a7ae-e3956b555c08 | -11.59644 | -63.76663 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ccc9bb3-01cb-38ed-aa3e-01aacc5da8ac | -11.59402 | -63.76802 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7725cb8-a585-3556-a5fb-dac58c332316 | -12.0236 | -63.77725 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c91496fd-0f4a-3c77-a193-8e3ee690972d | -12.02285 | -63.78168 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a33ef7d0-1952-31c8-b8f8-5e9d89950232 | -12.02065 | -63.77219 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ecf7cca-02df-3030-8246-268c50ba71dd | -12.01917 | -63.78102 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da33cad1-f854-32cd-8d3d-06b0e80bfed6 | -12.01623 | -63.77595 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df077bbc-a5f9-3221-9a22-20f1296a08f3 | -11.78317 | -63.66597 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 502f4669-9c2e-322d-9aa7-90486b86bb8f | -11.77877 | -63.66966 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a6265bc-31a2-3b5c-b511-6454f5407c36 | -11.77509 | -63.669 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8948c099-6063-3f83-9e16-0cecc00bc6c3 | -11.74209 | -63.7958 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2903df17-ca17-3ce2-af47-2b0b62eb1aec | -11.73954 | -64.08167 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02215098-1d95-3054-bfda-f15590b2ab68 | -11.73917 | -63.79065 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 295ebd92-3fe1-3d4d-bf58-c1b37a6f9049 | -11.73908 | -63.81345 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8781d5f8-6b23-3370-86c7-c6ab1fe93086 | -11.73841 | -63.79508 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b459bd10-40ca-3a03-87c7-c72bb1665572 | -11.73766 | -63.79945 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55aa1794-625d-3da0-99f1-288f80706f81 | -11.73691 | -63.80383 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72e1de70-9653-3060-b321-f0f9ffd72c85 | -11.73615 | -63.80828 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7181ab01-50b4-36fe-ad98-f7c270bfa7f3 | -11.73579 | -64.081 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9193ed4e-610f-38d5-9b97-16a02a245ebb | -11.73547 | -63.78999 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 248f9df2-f853-3c9b-80fa-eb777854241f | -11.73471 | -63.79441 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c53ea036-ada7-30ae-9770-bba43bb5f378 | -11.73203 | -64.08031 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13d7bb25-80f6-3735-b9fa-24a6658ea6c4 | -11.72907 | -64.07496 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ea9f21e-7c00-32c1-84a3-52252cb5e62e | -11.72531 | -64.07428 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df3cfc99-1cc2-32e4-a4bd-18c6b2d032eb | -11.71561 | -64.06309 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a552df0-35f7-3216-adaf-8701fc4c684f | -11.71483 | -64.06765 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea183e68-5a22-3046-b5da-ac6c36979baa | -11.70968 | -64.05255 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8e29df7-c25c-30a4-ace5-5de003af990d | -11.68799 | -64.04372 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0c756e3-7fd0-37b8-9693-4536eafb0682 | -11.68719 | -64.04837 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99dadba9-28cc-3b96-89c3-6a4c38c173c6 | -11.68346 | -64.04755 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9b039c8-8511-3a4b-bbda-3b4a17a42369 | -11.67974 | -64.04668 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65ed60a0-ee40-39ca-be0c-09675e03a5ba | -11.67683 | -64.04118 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 628fb416-a767-3495-b026-4fb94f4ac757 | -11.67602 | -64.04583 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b554eb7-52c9-3516-b9ed-1c0aad2a96ca | -11.67577 | -64.00273 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d004413-5e06-3917-8c00-5b25e6b79ebd | -11.67549 | -64.00029 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af158f4c-dc2a-33e2-96c5-b604629e5a62 | -11.6752 | -64.05058 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05cbff11-05c7-33f9-b18f-ce57e30c901c | -11.67471 | -64.00499 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c54f7f4d-378d-3022-970a-380087c4c4fa | -11.67437 | -63.98859 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6dbb0185-af2f-39da-9638-4b1009767360 | -11.67399 | -63.98629 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9308344d-8123-37f7-880d-625739102aba | -11.67285 | -63.99736 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21445ed5-8fb4-3d0b-a540-2bc16dc539b8 | -11.6723 | -64.045 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fdae9e9a-c4c3-38c4-81d8-6d67f695ddc2 | -11.67203 | -64.00204 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5457f09c-c84d-37f5-bdca-2d8bb6ab0a4d | -11.67176 | -63.99955 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b165ef1-9f27-3580-a762-9089f558efff | -11.67097 | -64.00427 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53e2dfe0-0cc0-39a8-9c5e-6339eec93016 | -11.66749 | -64.00596 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a15df44-8a61-350c-ba5e-9a127808227b | -11.66215 | -64.01449 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fa3b041-f2e5-388d-8a31-bf11701b4074 | -11.66118 | -64.01664 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cef9008c-0158-31d0-95d0-d841f7adde40 | -11.66041 | -64.0212 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4976b59-c576-3677-b1cb-778adbbec481 | -12.47567 | -64.02772 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7d63bb3-007f-359b-9406-3e52740b1f37 | -12.47119 | -64.03157 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e486766-10c8-3186-99be-c26ecc5b0328 | -12.44133 | -64.04942 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1187e72e-48cc-3705-af3a-26b934f9e76b | -12.43762 | -64.04874 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1704221a-16e1-3750-ba8b-959039711d23 | -12.35246 | -64.31479 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8bfa35f-620c-3fb1-aafe-a942e44d4640 | -12.35173 | -64.31905 | 2024-10-03 05:16:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45e91a92-45c3-38cf-a796-6869c2941777 | -5.88869 | -63.89866 | 2024-10-03 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 100c40d5-c622-3506-9ad9-8ee033d7c551 | -7.48571 | -63.98636 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d081238-3e73-31fb-90b5-84e5cfe1e036 | -7.46831 | -64.68069 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaf7351e-76ed-38ec-a79d-f2a481780051 | -7.45896 | -64.44524 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43f581e9-1e71-32a1-bae5-12bab6ec5f95 | -7.45077 | -64.44379 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbc47ccb-0291-3a70-87ac-5e4997db82d7 | -7.38574 | -64.67999 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a344eb1-c5d1-3379-b799-398484271a9d | -7.38157 | -64.67927 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 781f6d86-3ffa-32c1-8da8-bc563bc518aa | -7.29335 | -64.66033 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0b43a8f-faa2-3ec3-9c93-effcb5ee5163 | -7.28982 | -64.65578 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d16b211-aa4f-3ae1-95e6-ceb9409ed4da | -7.48173 | -63.98568 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8461e2f3-7379-3b85-9b17-dfafa324a9c0 | -7.46415 | -64.67997 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddfe4696-3b37-3e8e-8f4b-d03d9e14eeca | -7.45548 | -64.44084 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 434ea671-e703-3b84-8f57-bae77bcc31bf | -7.45487 | -64.44451 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c25f3c1-875c-3556-a1b0-c6ad1d73a3de | -7.29271 | -64.66417 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37ae92d5-27c7-3721-a8b8-2165a296e314 | -7.28918 | -64.65962 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e927e75-43ba-3d33-b5ef-55faa7e60481 | -9.02094 | -64.46741 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22b9456e-5ebf-3ef2-ac22-b8f8cec2ab0d | -8.95158 | -64.35831 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 789e11f1-9024-3bc8-8a54-e2c8191dd6c3 | -8.9504 | -64.36524 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d269c5a8-468f-3e78-a7a7-19b91f5b6254 | -8.74204 | -64.19286 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8eba38d-17dc-3bbc-a64b-86c43b7c3de5 | -8.73809 | -64.19216 | 2024-10-03 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef91281f-1dd2-30bd-a42f-57e2040e92ea | -9.3095 | -65.3614 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 823c79e3-612c-3c2b-88c8-891b4aa3c0f6 | -9.30881 | -65.36539 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d5cdd6c-bd30-3fa4-b85b-9b34057a38b1 | -9.30812 | -65.36935 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76ebd7c0-aa8e-389a-9511-2d111a90f311 | -9.30742 | -65.37334 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e5d6f54-b22d-3f09-9ac1-bd7cc5ff6c83 | -9.30672 | -65.37737 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09522f60-2d5c-3121-bcf7-60eec28a5704 | -9.30596 | -65.3567 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f2f392b-712c-311b-b228-dc8547292b91 | -9.30526 | -65.36075 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 667efe13-b804-387d-811f-565da26406b5 | -9.30456 | -65.36475 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5543ca86-cb83-3971-afd3-997e583190df | -9.30387 | -65.3687 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0a40f1f-78e5-3349-8d7e-ca63d105e835 | -9.30103 | -65.36005 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14506156-4ca9-31dd-8044-aa177f4ff4f9 | -9.30033 | -65.36401 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05b09b65-2267-34b7-84c1-1b6f41d63a4b | -9.29603 | -65.33881 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e12a8421-13bb-32be-8f30-161c006c4766 | -9.29534 | -65.34276 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README174.md)
