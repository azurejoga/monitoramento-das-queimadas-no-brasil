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
| d30441bb-f3b7-328a-80db-a2e1a5870db8 | -4.4665 | -45.4589 | 2025-10-31 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 28595f20-324f-3c42-8d08-3493cf85f58f | 1.267 | -60.4456 | 2025-10-31 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 13feb6b8-a754-30b6-9692-deb05a4fb0e9 | -2.9089 | -48.7268 | 2025-10-31 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e71b5247-e242-3244-a9ab-af4f2eab6751 | -3.5251 | -47.5607 | 2025-10-31 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 355c608c-f83a-3ef3-8db6-13522bc37622 | -7.6302 | -43.5895 | 2025-10-31 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 5ce25daa-a21c-3c04-a788-545ec401367f | -2.9274 | -48.7262 | 2025-10-31 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b867f586-f3a8-37c0-b168-2a9641f14076 | 1.5837 | -55.7067 | 2025-10-31 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 08e879fd-6c19-32ee-af5d-892b9f1fd741 | -12.141 | -51.2721 | 2025-10-31 00:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 7fcbe17f-2aed-3a8a-bf42-297444c1f86f | -7.6494 | -43.5642 | 2025-10-31 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 5eea311e-5bb6-36fb-923a-f4f4a7a01bad | 1.2852 | -60.4454 | 2025-10-31 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.4 |
| e0a201fe-b1f2-3963-8ea5-c52658dee0f0 | 1.5654 | -55.6871 | 2025-10-31 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3d443071-7ef2-3ea5-b29c-4c70d66df3ad | -4.8215 | -45.326 | 2025-10-31 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 95a9d089-14e3-39f8-9233-981384d9b0f1 | -9.5259 | -47.252 | 2025-10-31 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6e4a19f1-c3fa-3938-9bdf-05c4734a9a07 | -9.8821 | -47.4566 | 2025-10-31 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| eb12667a-0638-322d-9e83-5a9d38305490 | -3.5437 | -47.56 | 2025-10-31 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 3ec4fbfe-d69b-3765-9566-6ddcb49d4ad5 | 1.5654 | -55.7069 | 2025-10-31 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ff14f11a-2cb4-30e4-b40f-a3c6939b67c3 | -4.4477 | -45.4824 | 2025-10-31 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2332b203-30e4-3121-9997-ae3deeb1f496 | -3.1465 | -49.4229 | 2025-10-31 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| f91ee575-4f56-3699-80d0-87f174a5a9a2 | 1.2852 | -60.4265 | 2025-10-31 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 111.2 |
| ecf1ea4e-be7f-3ec5-b1a5-4368dc30db20 | -7.668 | -43.5857 | 2025-10-31 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 233.1 |
| b55667f8-2424-364b-ab97-39f5bb4a42df | -7.0883 | -44.9319 | 2025-10-31 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 49f7c643-f548-364a-8d0c-b317d0a3929c | -2.9356 | -51.4613 | 2025-10-31 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d285f04a-7cf7-3418-9b72-7897b9c87670 | -6.2167 | -43.9503 | 2025-10-31 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| bb7c2a90-6f5f-3889-bc33-8022203c2c5b | -4.4663 | -45.4814 | 2025-10-31 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 110.4 |
| cd66b48f-1668-3482-80ff-994985ace368 | -4.8402 | -45.3249 | 2025-10-31 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d0b33fbd-d799-3c3f-8478-b276e57a5b5e | -9.5067 | -47.2763 | 2025-10-31 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 91bed49f-aa49-34d2-bc6a-36f24d46d6bb | -4.3649 | -46.778 | 2025-10-31 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 8793def6-8be1-3c2e-b33a-33b9661dceda | -4.5584 | -45.6335 | 2025-10-31 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 02a7149c-e4d1-3813-a839-532498058e27 | -4.0634 | -47.4943 | 2025-10-31 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 131c7468-13c1-3ddc-8dfb-e212340b03b2 | -9.9719 | -45.1733 | 2025-10-31 00:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 9201b2d1-1ed5-3147-9841-d3da9ee8f6fc | -3.5438 | -47.5382 | 2025-10-31 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 4e64389e-7e76-3575-8d27-c039456af984 | -12.1413 | -51.2508 | 2025-10-31 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| eeeade0c-788b-3eeb-9c1f-546a52affa23 | -3.5252 | -47.5389 | 2025-10-31 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c71466a9-5afa-36b1-a292-883980b265d9 | -7.6682 | -43.5623 | 2025-10-31 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 3d59937b-3d09-3503-9c54-2bcc319b20d9 | -9.991 | -45.1709 | 2025-10-31 00:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7bb81ea2-7075-356f-ad70-0ea241a05828 | -4.0447 | -47.5169 | 2025-10-31 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 5048c3d9-db01-3eae-b73c-f4d6236c7cef | -9.5256 | -47.2742 | 2025-10-31 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| faee974d-eb7c-3d53-8191-093c8352e038 | -7.6491 | -43.5876 | 2025-10-31 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 350.1 |
| 03d1aa0b-62ee-39c0-b400-41559b9ed5bc | -4.0449 | -47.4951 | 2025-10-31 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 24f83873-d7cf-39e3-a093-420478e9270d | -4.5584 | -45.6335 | 2025-10-31 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 81185765-597c-3eca-bf68-d957918c0132 | -4.0634 | -47.4943 | 2025-10-31 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a04e205e-2f72-33ef-8d8a-d17237657e6c | -2.9274 | -48.7262 | 2025-10-31 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3676a7f7-fd16-3170-8094-e3e7168a9aef | -9.5067 | -47.2763 | 2025-10-31 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 64fc30b1-8a6e-3c7f-af31-d436817d5f45 | 1.267 | -60.4456 | 2025-10-31 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 03312588-f079-369b-9734-bc2cc4d82416 | -4.0447 | -47.5169 | 2025-10-31 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 21401389-8f0c-38dc-9e80-1732a7f1eb72 | -9.5256 | -47.2742 | 2025-10-31 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5162b5a4-dab6-37aa-b1eb-bfd08f844634 | -2.3178 | -48.5932 | 2025-10-31 00:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 5085f92f-3002-34a8-8069-ff02905a9b57 | -4.8402 | -45.3249 | 2025-10-31 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6282916b-2108-3b93-b92e-e705847b6907 | -2.9089 | -48.7268 | 2025-10-31 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 5e1b3b9f-c821-3208-b2ea-a44c2c912b54 | -3.5252 | -47.5389 | 2025-10-31 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a3a9fa48-ea68-3558-beaf-eae0f6bc68a5 | 1.2852 | -60.4265 | 2025-10-31 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 76b90e35-e30c-3bcf-84c4-0db368623bd4 | -10.9397 | -44.1663 | 2025-10-31 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ed81fceb-b1fe-3e07-ae5a-2e2c0eea0f93 | -3.1465 | -49.4229 | 2025-10-31 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| f17b6211-9fdf-3d19-bb6f-8b9be2329264 | -2.9356 | -51.4613 | 2025-10-31 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bb64d692-dd0c-3954-a725-fd746f632f6c | -3.5251 | -47.5607 | 2025-10-31 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6da8aad4-3f1a-332c-a79f-712e80af39f5 | -4.0449 | -47.4951 | 2025-10-31 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 84f1e48c-6fb3-3060-9208-1418479de28e | -9.5259 | -47.252 | 2025-10-31 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ca2369ee-ed08-3ba3-8b87-66991e5124c7 | -14.495 | -51.5312 | 2025-10-31 00:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d096a0b5-4042-343a-99e7-11ca17da9d65 | -2.3178 | -48.5717 | 2025-10-31 00:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7fc6980e-948a-3bf8-ba9a-cd2c9893c993 | -6.2167 | -43.9503 | 2025-10-31 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0d8520ca-571a-304d-94ce-19fd5c596d41 | -4.4665 | -45.4589 | 2025-10-31 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 89ef1bd2-b38e-37fa-8bd5-18acb60e0891 | -14.4756 | -51.5338 | 2025-10-31 00:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ee57bb53-77d3-34e8-93d2-877671202f80 | -4.4663 | -45.4814 | 2025-10-31 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 212.4 |
| 7b7fada6-be45-3530-8141-f2751861511c | -3.5438 | -47.5382 | 2025-10-31 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| ae2a5ed1-c557-36bc-956e-432d76955c2e | -4.4477 | -45.4824 | 2025-10-31 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 94.8 |
| c2f61473-2c71-39e3-a20a-c2aa554d6cb2 | 1.2852 | -60.4454 | 2025-10-31 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 393580e8-3985-3e83-a380-8c84dd2472b7 | -9.5259 | -47.252 | 2025-10-31 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 4a699fe4-0e27-307c-a763-0ff4ba4ce6ea | -3.017 | -49.4482 | 2025-10-31 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| aff5cc74-1da4-3da7-b245-73dab0a57bab | -4.4477 | -45.4824 | 2025-10-31 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7e3092fd-f9ee-3c30-83c1-fb7ea3f980a5 | -2.9089 | -48.7268 | 2025-10-31 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 0c968b6d-1231-37e4-aa52-93c5a417077b | -4.4665 | -45.4589 | 2025-10-31 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c8682c0c-e78e-3c44-9121-9ebb86195dcc | -4.5584 | -45.6335 | 2025-10-31 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e8ed8bec-dc05-3d47-8821-cdbcf184eef9 | -14.0985 | -44.1447 | 2025-10-31 00:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 351e4a5c-b423-3def-9c6b-c0328f0711c7 | -4.0447 | -47.5169 | 2025-10-31 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 10c550a2-5021-37aa-940f-597ab55e39af | -9.5256 | -47.2742 | 2025-10-31 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 69508392-65b0-36cd-ac4a-e9e2e52c7edb | 1.2852 | -60.4265 | 2025-10-31 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 37573f71-7ab0-3af0-98db-2b3624949662 | -7.6494 | -43.5642 | 2025-10-31 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9fe436ff-8971-35a2-8143-da748da2d353 | 1.267 | -60.4456 | 2025-10-31 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 462acd3d-d855-32d8-884f-13557c356700 | -3.5146 | -45.975 | 2025-10-31 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 31b84cc9-d24e-380c-99b1-6441b14af2d9 | -2.3178 | -48.5717 | 2025-10-31 00:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 492fd3f5-5c23-3af8-9e48-d367b05d664e | -2.3178 | -48.5932 | 2025-10-31 00:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 61a27444-6b43-32a7-b79c-d19b3835f698 | -14.4752 | -51.5553 | 2025-10-31 00:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ec93f9ab-00e1-3023-bd85-8e1c80d352cc | -4.8215 | -45.326 | 2025-10-31 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e2921172-2203-3d89-a1a2-f4448dc26da8 | -4.0634 | -47.4943 | 2025-10-31 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3c07c648-5d94-359b-8117-96c9e17c4e86 | -7.6682 | -43.5623 | 2025-10-31 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 0e75bf88-1cc8-3a62-a302-99babf55dfe5 | 1.2852 | -60.4454 | 2025-10-31 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 8783c2ca-e6e6-326c-9f39-7db60676892e | -2.9274 | -48.7262 | 2025-10-31 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2755bb74-e1bd-3dce-bdd0-40d447b8736b | -14.495 | -51.5312 | 2025-10-31 00:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6386f395-3410-37c7-bf33-73d2dca788c6 | -7.668 | -43.5857 | 2025-10-31 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 381.9 |
| 0f390c99-d262-30ca-90f4-81ddde8abe02 | -4.0449 | -47.4951 | 2025-10-31 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e1598add-2b31-38d8-9ea2-5e60668d2f5f | -7.6868 | -43.5837 | 2025-10-31 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| ff6c50a1-244e-3d82-b326-64f48cd5a96c | -14.0785 | -44.1721 | 2025-10-31 00:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| cb1a0211-ad2f-3f93-a0eb-01797547c43a | -4.4663 | -45.4814 | 2025-10-31 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 134.3 |
| f8c40b04-7e86-3ff4-a3a7-7a3d73170ee0 | -4.8402 | -45.3249 | 2025-10-31 00:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ccf9c650-5f75-3a59-b9ec-c07c178e18d6 | -3.1465 | -49.4229 | 2025-10-31 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 8d5f650a-bb2a-3991-be14-64ac7033fac9 | -9.457 | -40.3889 | 2025-10-31 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 75bd333e-c35d-336f-aaba-d3326865a7d7 | -4.0633 | -47.5161 | 2025-10-31 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| ba8111e9-e0f8-3986-9cff-98e10726d684 | -3.5252 | -47.5389 | 2025-10-31 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| ab026fee-98e9-3478-8640-fd286ba74412 | -9.4761 | -40.3862 | 2025-10-31 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 6929ec0e-16ba-3899-b8ef-8b3a0758879b | -3.5332 | -45.9742 | 2025-10-31 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |


[Clique aqui para ver as próximas entradas](README2.md)
