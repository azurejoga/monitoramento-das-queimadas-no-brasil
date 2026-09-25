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
| 62311eef-fbcb-3402-841c-e6f32a9cae88 | -3.08111 | -51.07763 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a531b80a-63cb-3ce0-ad91-aad64642321c | -3.05751 | -46.93093 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcb58299-b7f0-3dae-8f2b-799a75158c64 | 2.24911 | -50.90784 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af0bcb03-b1dc-35fa-9f34-4dbb6b9a67f5 | 1.48562 | -55.8552 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6d48207-9168-3d83-8852-43e742d20300 | -1.21958 | -54.56678 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 339fa13e-b9a3-330a-93c2-00a4fbd1f4cb | -1.31412 | -54.56909 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80bd3188-1164-3115-a2a7-afcf8fb4e391 | -3.6298 | -42.76092 | 2026-09-25 04:44:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccff8692-72d5-39ac-a17f-dee12edd548b | 1.62876 | -55.95324 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 413c8f33-8e40-3fe4-9301-aa9e62003005 | -3.20546 | -53.40504 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab87bd33-f2c1-33de-8d94-e31a66d3f9a5 | -4.34946 | -47.76491 | 2026-09-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4c8a9ad-391b-30cb-800b-f623ef596557 | -1.6942 | -48.2113 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 056ab593-a941-3ddb-84bb-a05ca3487596 | 0.70356 | -51.43288 | 2026-09-25 04:44:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e828b23d-b167-32fd-9c6f-5d63e762df28 | -3.71228 | -54.20862 | 2026-09-25 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82bdcf72-d4ff-3f9a-9d7a-d293ef2d7218 | -3.21015 | -53.40082 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4fcf498-4aba-3742-a99d-7d5609d93aab | -0.24074 | -52.95911 | 2026-09-25 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e03b254-dfd1-3f45-aa2a-d447373be29e | -3.23618 | -46.93038 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5446edd6-f75b-3102-a851-a86d9d37edee | -1.67345 | -50.11928 | 2026-09-25 04:44:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a22ad3c2-bceb-3f86-84e5-fe7edb3891fa | -1.14181 | -54.10083 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 275f37b6-8b11-3869-bf61-c01efff16f15 | 0.07151 | -51.14593 | 2026-09-25 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 523d8802-c346-3513-b058-1516e7283696 | -1.02569 | -53.73699 | 2026-09-25 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 339af815-a656-34cf-967c-55913dc2e7ae | 0.50315 | -60.60137 | 2026-09-25 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40e0edbf-0faf-368d-94b1-07b65613198b | -1.09543 | -49.20397 | 2026-09-25 04:44:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae3a7394-cbd0-3608-9cda-1f08d2114bae | -1.21464 | -54.56992 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5329689-ab87-3d9b-bed1-5307491d670d | -1.14367 | -54.08926 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 525d441a-47b4-346b-a78a-d105736b1a10 | -3.703 | -54.18897 | 2026-09-25 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a9c5550-285a-36fc-b1f2-045a5994c375 | 1.5866 | -55.84437 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cd505cb-8d15-3f45-913f-3a2125fea22a | 2.12682 | -50.70148 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c076f89a-4d68-3c9b-8707-08ddc94ff3fa | -4.11414 | -51.08337 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f211bc19-09f3-3e25-b365-b48b1cc15859 | -1.1454 | -54.10535 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38ab3004-f28e-3308-b88f-4d8b8e7d50f9 | -3.77173 | -47.54342 | 2026-09-25 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be7a4482-63ce-3649-887b-89b833af2e4c | 1.57818 | -55.82234 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6969cbd2-a2aa-3490-a1b9-f004228b8213 | 1.61916 | -55.8911 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 336f8a83-000c-3f1d-bd4a-a57767a7e1fc | -2.42637 | -48.54499 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d22a1956-a2a0-3485-82fa-c3968b4e8bdd | -1.09821 | -49.20797 | 2026-09-25 04:44:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e5940c9-010c-3877-8392-2c9e234e4be5 | -3.9834 | -48.4288 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cda7bfe5-3668-3904-8d45-e453dfd098e6 | 2.24419 | -50.90005 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 425ca6fc-334c-356c-b15e-68625967caaf | 1.62694 | -56.00798 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc893c31-c2fa-3682-9745-3c7dc723cd55 | -3.62542 | -42.76027 | 2026-09-25 04:44:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f006c84b-52f7-313d-aa01-d13626465c77 | -3.23961 | -46.93091 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 791ce732-6aea-3312-b47b-4c65486dc4e4 | -3.7969 | -52.36985 | 2026-09-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 412b60ee-5867-3214-9a2d-9c7302f29c64 | -4.93353 | -45.66324 | 2026-09-25 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44f97871-9cf5-36dd-b76f-63c0f3d95697 | -3.08051 | -51.08142 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f331fb-e1d8-38f2-a7a9-1ce1fce9aea5 | -3.20936 | -53.40567 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1580967b-9ccd-37f6-a023-c790fc3ed9ce | -3.97954 | -48.43176 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02fabeba-2dab-3a14-87f9-c670fce6de2e | -2.81916 | -51.33647 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bea3f55f-c434-389b-8931-73c2c50e9c08 | 2.13543 | -50.77979 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3189d200-372b-31f7-99ec-4f82aee2708e | -3.20157 | -53.40442 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fabfba8d-6b8f-3349-a9ad-148d659e7ce3 | 2.24716 | -50.89531 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23990027-1311-378d-a3cd-edb355778a09 | -3.23903 | -46.93463 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc48d0e9-0944-35e9-885d-f7a69de1f74c | -3.08457 | -51.07817 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8d9361a-e2d7-33aa-baa1-e1b78cfae82b | -3.49923 | -50.74252 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08749234-0f91-3597-ad47-6b3d7ce218a4 | -3.01165 | -51.53778 | 2026-09-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a578d2cf-2907-3f04-b8c8-f4df7b36ce78 | -3.72675 | -49.06403 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5b9816f-dbba-3b6d-b1db-88aea1d26a56 | -3.23675 | -46.92666 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 83758c3a-ffff-3c8f-908e-f186148ebbe2 | -5.37698 | -45.99501 | 2026-09-25 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5d766c4-7f12-36eb-b954-ba12685d6404 | -1.14243 | -54.09699 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 84a04eb2-f62e-3045-8c85-1beb6333c054 | -3.50264 | -50.74303 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a919a7ad-171a-3a1f-9198-d728ac3b0e42 | 0.50227 | -60.596 | 2026-09-25 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a64b72b-0fad-3760-93e6-d3f08a62808b | -3.05809 | -46.92722 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 912f92d4-1364-3a6c-8fe0-04eb71c1e9df | 1.62438 | -55.92487 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 152ba1c0-4529-31c7-a9c7-d7331f71dee0 | 1.28722 | -50.83923 | 2026-09-25 04:44:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75e4ab11-c9b8-3649-b90f-873c646e1629 | 2.11123 | -50.69556 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7e28250-f7a8-3e0a-97fe-db2e5757a2a4 | -2.56502 | -49.08497 | 2026-09-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 440297ae-6153-3d6d-8f71-64c39022be1d | 0.50041 | -60.60109 | 2026-09-25 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39e2cf3b-db7b-375d-b726-918b2f51c013 | -1.13761 | -54.10013 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 35f6da46-782f-35c4-a7a0-29f292e7d285 | -3.23217 | -46.93358 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 32f0a89a-1457-33b9-971a-97bc03f71d08 | -4.11474 | -51.07962 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73ca45a0-48f7-35e8-9c49-2016e50d8364 | -3.20389 | -53.41473 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b49fa20-c891-3bbc-86ad-0c9a0ee61583 | 1.6235 | -55.91919 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4eb82290-70ba-3126-80e7-58686117f175 | -3.70184 | -54.19593 | 2026-09-25 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7a8c4c2-21e3-30a5-8a30-3fa7fcadef43 | -3.98286 | -48.43227 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2d26fa0d-02c3-308f-b626-958446b0aa19 | 2.25208 | -50.9031 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fafeec04-8716-3e39-9515-1e43fae2aaaf | -4.15248 | -48.75705 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1daba5c-419d-30df-b406-e9ec830a3f08 | -3.49583 | -50.74199 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99a723d1-083e-3904-804b-1b438deac988 | -1.137 | -54.10396 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f405c354-ca31-32a6-b51c-ca55bfda1865 | 1.58572 | -55.83865 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 305ef336-ba87-3dae-ad3e-955ac3b558db | 1.59231 | -56.01635 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae05d41-150d-35e7-9a18-b63e7a6b133b | -2.99722 | -51.01137 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d679c12-8130-30f0-abd1-7d027e53051a | -1.13823 | -54.0963 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c298ca24-8552-3db5-97ea-18330fe7d1c8 | -2.14988 | -48.46621 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 321f21cd-f6f9-3bb6-9954-06879021a0aa | 1.58643 | -56.01139 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38538c96-03d0-3d8c-ae72-b93a7f54bf3a | -3.83148 | -49.00297 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc739a4d-1469-3084-ae20-fbff5995cdec | -2.73884 | -51.54535 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 596a4985-dedd-3717-910a-2e03ae3a0d68 | 1.03023 | -49.94713 | 2026-09-25 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c349daf-0c88-352d-868a-8c9db83b9b23 | -1.53023 | -54.29735 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9da91f68-1478-3349-983f-d137956fc34f | -1.96301 | -48.38014 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9290521-21b7-37ce-8aed-d54580c6f7ed | -3.17912 | -48.01431 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09af9b51-b7b8-3672-97d9-2f9a608dc305 | -2.86429 | -52.41864 | 2026-09-25 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 179c7561-98de-371d-af4e-171472989ad6 | -1.34413 | -55.47252 | 2026-09-25 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f24ae18-01c5-3493-a424-cf80a29ce81c | -1.14725 | -54.09383 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3403afd5-b08f-32e2-a6f7-ff5b905e3581 | 0.60522 | -51.57008 | 2026-09-25 04:44:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6f3c68e-2633-36eb-8087-526608b1c428 | -3.50323 | -50.73939 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b889641-ec3c-3c70-9aa4-403ba59d2cd6 | 1.62788 | -55.94757 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 120d3a83-fd5c-3504-8288-531faa72b540 | -1.21897 | -54.57063 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb91d47d-e9c0-3a0b-8c66-aa7e4c51d301 | -3.44505 | -50.42573 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66eb8adc-6c66-317d-bc68-d33d94344740 | -3.19999 | -53.4141 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1225bde-1b32-3f5d-a17d-8ca53e67ca50 | 1.48903 | -56.04501 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e63e78c7-169c-3cf5-b156-33187b232e06 | -3.76835 | -47.54289 | 2026-09-25 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5721d346-cc73-30d3-81c1-c27fc9b3be0c | -15.43623 | -48.48493 | 2026-09-25 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e682160-db99-3ebf-b69c-a20d44333e12 | -17.04562 | -50.87586 | 2026-09-25 04:46:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
