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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 622deaa2-9d27-33dd-9112-ebc8c29208d1 | -2.59371 | -54.22237 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9f2e77a-b2f4-387f-82c4-75431950dae4 | -1.7036 | -52.76644 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1460703c-7adc-3f39-b269-016e7a86e15b | -3.17818 | -54.33552 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a123df6a-cc8d-3eaf-b445-5704b36e6c38 | -1.14517 | -53.80691 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5982825e-8c59-38d9-9bdd-6183e234195f | -2.80416 | -54.0388 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f7cd23c-497d-321c-b192-08a378ae2473 | -2.76942 | -55.34577 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37b93121-620d-38a4-9255-4bc40e395d1a | -2.59431 | -54.21859 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a5020d-df28-3022-afb3-d2d2be6dea43 | -3.25063 | -53.63037 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ceb75bd0-a633-3e5a-8640-bf4fa5d73c3e | -2.88174 | -54.0769 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af2e5c6b-27e9-3816-b86c-d47add2999a3 | -3.49229 | -53.82533 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08409f7c-1495-3135-ac01-decc5e470dff | -1.46436 | -54.49225 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb12e684-a272-397c-bafe-a4dc88cc7c99 | -3.01403 | -54.10858 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9b19dc4-0f1e-34d4-b621-b0e6faeb6bc0 | -2.52741 | -54.00905 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b1476b2-b3b6-331d-bbdd-9bad128b4db4 | -2.52799 | -54.00522 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8884a4ee-4468-3d13-b873-447ae5ca5d36 | -4.01434 | -47.00429 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 927e90f6-a839-329b-b5be-c0e0dda6621e | -3.60137 | -51.05587 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58f55cf0-68db-3274-a84f-3d31cac765ea | -3.26856 | -50.57827 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf9503ef-ca9d-35ba-874f-2639301392b9 | -2.63326 | -53.99387 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0247cf7-418d-391b-9477-5dc4d799e959 | -2.03298 | -55.77755 | 2024-12-01 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9442695a-6444-3a99-b9d8-73975cd3365d | -1.39962 | -53.39051 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d08165-99f6-3488-a1e3-84440cd1ba2f | -4.2069 | -48.12195 | 2024-12-01 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9bf5e34-0039-3cd9-8923-e4f0f9d4778a | -3.51907 | -62.75862 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 239287ed-bf84-3051-8cae-1eda25467ad6 | -2.84192 | -54.0485 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21bbaf4d-e5b5-3122-b140-884c079b1202 | -2.74759 | -51.76001 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 56549026-d473-3ef1-8825-ef4478eced50 | -2.858 | -54.04565 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4409937d-d1ea-36a2-8f76-e26915c4ecfe | -3.46526 | -50.26635 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8334d478-67da-36bc-8af9-acbc05e32e2e | -2.14399 | -54.87543 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7470afb8-ddd3-3354-a8b6-09d23d182525 | -1.59658 | -52.28482 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c95dc32-fdca-323a-ad8b-6c2cbf4208b0 | -3.76133 | -50.17694 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d9d36f9-2804-3434-9621-16b57c91b321 | -1.81923 | -55.16661 | 2024-12-01 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fafb1dbc-c263-3c21-9ad2-3d4690fd59cc | -2.88088 | -53.33104 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30d5bacb-d4f7-34e6-8e8c-dbb480fcdd34 | -1.68531 | -55.00558 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e7b3369-44b6-354a-be3c-8a10a8e33e51 | -2.80296 | -53.05776 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff85ad81-182a-3dc8-b639-68bbc367abde | -2.89663 | -51.57661 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c5d7df5-60eb-3327-90bb-8c83c3e47c89 | -1.14381 | -53.80609 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3cd9f0a-352d-3ae1-8d62-2982f1e1183d | -3.40581 | -53.03064 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c59d690a-c836-36bf-9882-776c7204f36c | -2.82495 | -54.06563 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a68f862-7f9a-3a6f-a637-2bc57628891d | -2.86458 | -53.97934 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3888c806-f104-3531-b336-88249e5db531 | -2.85322 | -54.10006 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c70a7b7c-8e58-3be6-a054-2a7da02452e1 | -3.01485 | -54.05742 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d435298a-2154-344e-9d9e-bbaf59b2947d | -3.33686 | -53.21029 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78ab2de1-e9e9-3bd5-83e0-b1cbcb9353ea | -3.08058 | -54.12592 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0929b6c4-58d9-3aa4-bc03-3ee98ea52c10 | -2.91179 | -54.11298 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9df20ba-88f9-34fd-97bb-5fef1fd7eb09 | -2.84979 | -54.07593 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd4196d4-ef29-3542-b4f0-e5f2a2cd5d3d | -2.96277 | -64.99853 | 2024-12-01 05:08:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6933f36b-bdb3-3595-8a3b-d6487bc33fe3 | -4.12415 | -54.21033 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f01fca05-3146-3eb1-8d67-ed497b40ff34 | -2.69427 | -52.91644 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0838466a-d558-3dea-b1b0-1538f91f694f | -3.26314 | -50.05333 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 758b2773-4450-3d93-9fb5-02c493b3138a | -3.10012 | -50.36453 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca5b7a2-1d3c-3682-8529-05a714e50782 | -3.08531 | -51.07409 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a683fd15-1567-3874-ae7a-728842c7321d | -1.9537 | -53.34229 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d01bac26-cdc8-3775-97c2-4e74a2c4dd22 | -2.5786 | -53.67377 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b58e802e-40bc-3500-8a11-5e13a7dd9dca | -3.45371 | -54.56823 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 993902c9-3c6b-357c-8863-00d8bbfe265a | -2.81224 | -53.04607 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 11dcf9f0-0d67-37b8-a558-f3d0f8bde32e | -2.80793 | -53.04977 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 36e6b470-0dfe-3ad8-9b56-723db0f601a9 | -3.09346 | -53.26226 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a71e0f9-8a32-32de-9800-8d3501b01954 | -1.98713 | -53.1294 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be014cba-5160-31ea-adce-1de905400769 | -2.68752 | -51.73011 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68921618-ce35-31e3-bad6-4690de28ea7d | -3.06667 | -53.81676 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9db583d0-09b0-3727-b29c-67f6fc3358c9 | -3.05918 | -54.04836 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9527e470-14c5-32ec-89c6-4a517d29c58b | -2.89302 | -54.16491 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d8dee0f-d154-3ec4-8bf6-6a1802cec1c3 | -3.25404 | -53.86858 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba94fd1a-5a54-3fff-9340-e63463c4c0f2 | -4.33998 | -50.76691 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0915c0a9-61e9-3464-b8d0-b7286d9e1afc | -6.7615 | -46.53053 | 2024-12-01 05:08:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53a6eecb-8b9c-3595-8dd3-5d2cc3f311ac | -2.12782 | -53.24114 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eccbd07-d434-3cd0-8b58-75efd3b63cbf | -1.9495 | -53.34579 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ad64269-1f3c-39d6-9927-b907c7784815 | -3.12121 | -53.27512 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a66547e0-e458-3dd2-882d-cb0be7e85e24 | -1.36709 | -53.64275 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 309077ae-8565-3937-a151-a8f8ebfc8e69 | -2.73963 | -54.04071 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e7cfa76-1e50-3f73-aec4-6bc7f2a2801e | -3.10015 | -54.02201 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bb201e9-ac62-388b-82fc-af4341967731 | -4.44492 | -45.35985 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 791b3a13-924a-3b7a-930a-1d982bf7c6b3 | -3.12229 | -53.09718 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f46540f9-53f0-3fec-acb6-3084b9a9ee74 | -3.25652 | -53.63966 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c58fec62-357c-3c11-8a4d-63ea3d66cc35 | -2.69647 | -59.50823 | 2024-12-01 05:08:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ea8ddb9-6b18-35ea-929e-cfa09987ad1a | -2.76553 | -55.34878 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4030297e-15ee-33b6-839d-8de306909e75 | -5.54097 | -45.43505 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a931055e-20ac-36f1-9489-955e58e3a00a | -1.27103 | -55.76051 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d06300b-2971-3372-ab47-e7a4950b1edb | -1.46438 | -53.69141 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9dfc7350-040d-327f-b130-9d4386c8d816 | -2.88617 | -53.97869 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46a2bd5f-1cfc-384b-94ca-9850d6c72168 | -3.11862 | -53.80777 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 476c9272-6d66-3bd0-a905-49acf394cbe2 | -2.5287 | -53.98999 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df40330f-c60e-338c-9b88-11978c76f6dd | -3.48937 | -53.82078 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36e65755-cfe0-344a-86ec-473095f32141 | -2.8657 | -53.99537 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55b6c43b-f977-33f1-be99-fd447a5e471e | -2.75154 | -51.76062 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea3d74de-7ae0-3969-99d4-ee6350fc6d98 | -2.46488 | -53.96438 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351fe494-a409-3cf1-9c68-19d6a4b001a4 | -3.38057 | -49.85506 | 2024-12-01 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5bc049d-64aa-3079-8858-011422087cac | -3.5409 | -50.179 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9d85264-f90c-3b9d-ab8a-572cfc16d62a | -3.1336 | -54.53236 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 1239f424-e791-3c07-9ecd-ed148b2c12b0 | -2.82435 | -54.06948 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf000645-3ccf-3633-8879-8a4a42dae4be | -3.24143 | -53.9268 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd04533-be9a-3348-96ac-fd9a22f36d0c | -3.07557 | -53.80604 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e05aee9-77b3-332b-ba92-73dd81eb485a | -1.71347 | -52.63069 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50e6cf6d-3734-39cd-ba0c-d4d68aaa9ecd | -2.72572 | -52.977 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e51299e-833f-305b-b78c-3cf1f8756e92 | -4.86943 | -50.86421 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd37d0b-ed6e-36dc-9e1f-3e6a8f8b0d87 | -2.43767 | -54.13999 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 549075f6-0292-394a-aea5-063439d215d8 | -3.29198 | -53.83385 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 022dcdfb-5e5c-3781-a7d8-22e6eb2b5a5f | -2.56851 | -54.33771 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6701f2b7-6d53-396d-a115-2396104b32a1 | -3.60589 | -50.37825 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3d4adb5-3d91-3c1a-913d-a0d7ff945491 | -2.60062 | -54.22342 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff364382-dd83-31e5-9636-b67ea4cbf8cd | -2.71896 | -54.11636 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README80.md)
