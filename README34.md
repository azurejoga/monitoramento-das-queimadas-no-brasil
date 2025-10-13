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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ceff17d-1ee7-39e3-87e8-9a5959cbe9d1 | -13.53362 | -51.29448 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| a0d0f3bf-b174-3b51-b9b2-b9907a1b3b66 | -11.741 | -64.966 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e4d1e31-5376-3efe-a44b-a4e200e3d6d7 | -17.33933 | -53.80999 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf386a50-0951-3ef2-ac58-a96a5423a5a2 | -13.52503 | -51.30799 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 35f0efd6-71c0-373b-bd39-5def4c12fad2 | -12.3925 | -63.87436 | 2025-10-13 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fa1f54a-e68a-3ef3-9cbd-978eaa363f9b | -17.33257 | -53.79759 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a2e852e-c3a6-3183-aaa9-9ca71d4b6a92 | -14.30019 | -51.53782 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9c3281c4-18fd-349e-a237-d6b1a25d098c | -11.80865 | -64.98766 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bba5263-feb6-3545-b34f-1c83787d2ad3 | -14.2483 | -51.48132 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f662327c-90c0-32e3-80ba-e018349486f4 | -17.3274 | -53.79838 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 046551ae-2106-3742-9d32-fbb59b886453 | -10.38012 | -67.95036 | 2025-10-13 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f337c386-0862-328d-90f3-f563f50ef64e | -11.73771 | -64.96548 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb29be5f-7584-3de8-a9ed-99b78003a821 | -14.30399 | -51.53981 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7afd6754-e55c-3ea1-a994-f776e882744c | -13.4972 | -51.29733 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 178fb1e2-448b-3615-886e-0c96bf3e165b | -16.12727 | -53.96605 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a28dc43d-ef6a-3d76-b71f-84a6fe302009 | -13.51789 | -51.30713 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| f0b02a0a-af83-3221-9c85-515fde30df1d | -14.30467 | -51.53273 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8f9bf6e8-9cd8-3074-a06e-943a72bd5c83 | -11.73605 | -64.95445 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31dc97b0-233b-3aee-9a5b-271ad476278b | -10.71592 | -68.60906 | 2025-10-13 05:38:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13d4b47b-2902-3648-ba86-b0ee1691d3eb | -17.33108 | -53.81272 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d671e95-9841-3574-a700-a3e3d65fe4e6 | -17.34026 | -53.79989 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30b42be1-4a9f-375e-9cd7-1cbe7551a0ff | -13.51933 | -51.29275 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 997cce1a-2de4-322d-b7bd-71f5602e496b | -11.12573 | -62.8387 | 2025-10-13 05:38:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b8a8400-1e03-396f-abdb-4ccc280eb2a5 | -10.92362 | -68.24882 | 2025-10-13 05:38:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8245ef5-3140-3125-a1dc-f65aae3f549e | -14.27115 | -51.50705 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a717b939-821b-3642-823a-9370b4c2d6b2 | -11.97433 | -63.06971 | 2025-10-13 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc7d530e-1833-35f8-9c79-754cdbc3a3ad | -14.22348 | -51.5144 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aaba2690-d905-3bd7-9dec-568b06b7c5e4 | -17.33801 | -53.80837 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fdecea0b-2d13-320c-87a0-da033b2d417e | -17.34442 | -53.80931 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27425504-95cf-35c3-a411-4cd7c137711e | -12.39585 | -63.87488 | 2025-10-13 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ce1746-480e-3ed4-ae17-614dfbe48112 | -10.88055 | -68.2147 | 2025-10-13 05:38:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb535840-cc2a-3cd2-b81a-de9907bd0e8d | -13.49791 | -51.29015 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 05923971-23e4-39cd-ad9d-71c6e5823ea8 | -17.32465 | -53.81209 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1dcc834e-f0dd-3c43-9edd-0e1091d1e256 | -14.31294 | -51.55363 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| dfcaa58e-94f0-3726-abe0-12c282e8ebd5 | -14.30972 | -51.55487 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 842bea39-8b00-323b-acef-2290059eaa3c | -10.13195 | -68.19638 | 2025-10-13 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 804c1621-b6c6-374a-a3f1-6d9fc0e44374 | -16.21709 | -59.13199 | 2025-10-13 05:38:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 0c9e9602-8e0b-3933-85d9-41ac8a574fb2 | -10.88492 | -68.21102 | 2025-10-13 05:38:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 515c9886-f734-3cc6-94ff-4915d71a46c2 | -14.66461 | -60.26458 | 2025-10-13 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9325ce41-f8cf-3e94-ac82-c0d2abe46c34 | -17.32004 | -53.80787 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46edb2b6-85e5-3a3d-b34a-e2f0a9d71a25 | -12.39775 | -63.70445 | 2025-10-13 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3af9c4d4-92e1-39d1-a9ef-26ac031364d4 | -11.83238 | -64.88378 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77e07b0a-e317-3687-9fa0-e43bddfe407f | -13.53216 | -51.30886 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 26b849ba-3435-3b49-85c0-b8d4370833c7 | -12.5953 | -62.97163 | 2025-10-13 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4093fc69-231f-350a-bed8-c9b02faaa5e3 | -11.74155 | -64.96251 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ea7989f-d9ba-33ef-86a0-b7f1af064087 | -13.53289 | -51.30166 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 0f6bdf52-ec94-3bb1-9d89-e0da72f124ef | -16.12362 | -53.96526 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4125f534-53f4-3751-b75c-ec7d57f3cd8d | -10.97973 | -59.02219 | 2025-10-13 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f51479ef-d3ba-381c-9344-e53f8285432e | -16.12678 | -53.97114 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 86a571d2-7072-3903-8f3a-23a4bc6d2023 | -14.30657 | -51.54572 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a5289d44-2eaa-33c9-895d-62a71c021f02 | -11.7355 | -64.95795 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 013dc6b6-1725-37b6-9730-099694a33a09 | -17.33336 | -53.80422 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c09634-7600-3e2a-a207-9bc6cba1ab91 | -11.7322 | -64.95742 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a68524f-1230-3635-9679-010dee89b38c | -14.27464 | -51.50609 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a793eb1f-2fab-3183-9dd6-aefe3ab5da97 | -16.12937 | -53.97123 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 86a0b4da-596c-34a8-8cdf-f0c2c3ee4d83 | -13.51219 | -51.2919 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 2c29e12f-5475-3398-a2ff-ef0c1464931f | -16.21949 | -59.13074 | 2025-10-13 05:38:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 47b7e333-8285-385e-af8c-510db2668519 | -13.50137 | -51.29377 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b1d24ebc-6832-36c1-a6e9-23995312bbbc | -12.59526 | -62.94807 | 2025-10-13 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71de45e3-63f0-3cbe-ac40-a33e79735464 | -13.49423 | -51.29292 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e67849f-f03f-3e2b-84b1-f6591f36047a | -17.32647 | -53.80854 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9975cf3d-6d48-3c57-8af4-aa61856eebdb | -10.64511 | -68.86401 | 2025-10-13 05:38:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e191d3c-510f-385d-a186-81c543afc83b | -17.34574 | -53.81099 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3cdfe6a3-fdb0-3646-9821-299192296ddb | -14.29381 | -51.5299 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6e1c24fe-c289-30e8-a562-90fa501b38a8 | -10.92728 | -68.24944 | 2025-10-13 05:38:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f235535d-f1fc-302b-8df3-3e02a3486463 | -13.50505 | -51.29102 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c203076c-32b6-3cfb-97ad-bf8efff738d7 | -12.58668 | -62.95852 | 2025-10-13 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d917bf53-e634-30b3-b92f-6fa0a736b8dd | -10.10904 | -68.63 | 2025-10-13 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7516d13d-c548-393f-aa8c-b0c909bea851 | -16.12311 | -53.97029 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 77d6f6ce-313b-3c1d-b145-78ac4b28e121 | -12.60215 | -62.94913 | 2025-10-13 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dd35cbb-47fd-3e5b-be0f-7dcd5fed265c | -17.32515 | -53.80698 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b791dca-5587-38e2-b26f-6e5172070938 | -17.32693 | -53.80348 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f476f8c8-ab59-35c8-bf45-c8ba4f1884cf | -16.12629 | -53.97628 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a67646ed-9ac5-3fc1-ba57-f3046d2f92b2 | -14.29757 | -51.53186 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cb0a3bf7-9fc8-3ce2-83c9-4eaff20459b0 | -14.25542 | -51.48217 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 37e86568-72bc-3308-8c5e-fe06877a962d | -11.7388 | -64.95848 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9126ea7-2926-3687-84f6-41b97ce03204 | -14.25472 | -51.48933 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0d58a98e-f7a7-3534-b224-fe526d1cdfb7 | -14.31439 | -51.53947 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 97a5f558-45ce-33a9-a8d9-0c881ac59977 | -17.33207 | -53.80265 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 105bb4e4-76e5-3f72-843c-efd5fbe44d0a | -16.12989 | -53.96612 | 2025-10-13 05:38:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82c478c5-a938-36de-b1c9-dc4ba92fcaff | -17.339 | -53.79826 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23be5a26-3a88-34ee-b3a9-61d2a6055e2b | -16.215 | -59.13014 | 2025-10-13 05:38:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 8220308c-24c1-31a1-b72b-c0b2ed375447 | -10.73395 | -69.44596 | 2025-10-13 05:38:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 141320c5-39d9-337d-9981-02439193bece | -17.33291 | -53.80923 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0fd36341-2805-3d29-b9c6-82dbc52b5d94 | -17.3385 | -53.80337 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d624fa1-f084-3773-840d-1593651ef731 | -13.51147 | -51.29909 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 6e715d78-d3c6-3ac1-8819-1d0313823422 | -14.30729 | -51.53864 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 39d961e6-0e79-3c23-845d-19d8d7833cf6 | -13.50433 | -51.29822 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 43b72ac5-2a12-32f0-ad50-3308fd8b2224 | -17.32601 | -53.81368 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bde4be26-0257-35fa-a1e7-5f212d23078f | -11.73825 | -64.96198 | 2025-10-13 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f480b83-bb5c-37f1-990b-84feec3081f2 | -14.26404 | -51.50618 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94f9f8b4-698f-3981-a805-81053afe17de | -14.27826 | -51.50793 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 797bc624-80bb-31ef-bbeb-42a078e13a9c | -12.35058 | -63.65228 | 2025-10-13 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f29fba9-6fd5-3d6c-aa2a-34c6b4aa9e7a | -14.29046 | -51.53101 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb48260f-5e6e-31c2-beb0-b72f6bdfb7c9 | -14.29689 | -51.53896 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5e4f4b7b-591a-3f76-9f60-4ede78f80eb6 | -17.33383 | -53.79916 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dd327de-6cf5-3eef-b850-e2286a797cfe | -13.52647 | -51.29361 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| cdfc337c-2268-3383-9b46-3f108354320b | -14.31109 | -51.54069 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 6b7da673-6ee3-3da9-af48-460e8f1ec71c | -14.21637 | -51.51353 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7b2bf5c3-dac9-3ab7-9cbf-ea654950661f | -13.52575 | -51.30079 | 2025-10-13 05:38:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |


[Clique aqui para ver as próximas entradas](README35.md)
