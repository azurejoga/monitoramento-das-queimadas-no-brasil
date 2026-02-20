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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e8b9bc9-094c-3ce8-8437-b29408a1325a | 1.83085 | -60.84742 | 2026-02-20 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3763ad0b-99c3-3685-98e2-e2e389cb5848 | 2.54062 | -60.72074 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 286352ba-936f-3f03-90d7-a4b8cbc6a938 | 2.68234 | -60.22402 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a85fbff-1e00-31bf-a552-046e610b0be5 | 4.06381 | -61.13996 | 2026-02-20 05:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5a80e9c-23fb-3f86-b04a-75f360e756fc | 4.07435 | -60.18483 | 2026-02-20 05:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8438abdf-c7ad-3c4c-ae4a-e2c48ef9a2dd | 2.56396 | -60.56173 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13ba8f09-521f-30df-b8b6-1a0e52cc9764 | 2.56087 | -60.56721 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bbb64104-f655-3432-80c2-4141cdde1295 | 2.53677 | -60.72135 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17d19340-dd9f-313f-8f38-23c54ae0316e | 2.69744 | -60.24246 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6912048-fc51-30ee-ae10-95d78fe5ed26 | 2.53753 | -60.72612 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2786777c-1390-3b62-8d5b-fa15d357fe92 | 2.54522 | -60.72489 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5f53d67-5660-3449-9d0c-c188a7747d5e | 2.69694 | -60.24573 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68e304fa-b036-3667-b1b4-4fc5e42ff602 | 2.69349 | -60.24309 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8038b10f-677b-3290-8d50-eb73dce528a3 | 2.55699 | -60.56784 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 57e231ec-12c2-3b59-b955-9b764d557748 | 2.6872 | -60.25446 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 150deee8-f158-37b0-a8cb-ed030cb6e0ae | 4.07176 | -61.1654 | 2026-02-20 05:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eecd9c71-4ce8-3f98-a97d-ebb7f0ad81b2 | 4.37399 | -60.33827 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48a86ff0-97c0-3374-839e-be34c0853341 | 4.19085 | -60.03524 | 2026-02-20 05:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0fc1cc-891b-3ec1-bede-2829311c1d05 | 4.10631 | -60.6452 | 2026-02-20 05:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8289612-b0be-368b-97fc-3d23e9b78b1b | 2.55928 | -60.55747 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 52cd20bc-fde1-3002-a394-aef97cc3b0a0 | 4.48586 | -60.5696 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b4d9dc9-9124-3e56-9c0e-cebf9903e559 | 3.23072 | -61.20098 | 2026-02-20 05:48:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d4c77e5-c41a-36d4-a301-3d36e4c72e0a | 2.5554 | -60.5581 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 896e37b6-072a-391f-91dc-20e2d823dc3c | 2.69753 | -60.22487 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1726f8f6-d89c-3a4d-a473-89ee84d2c2d5 | 2.659 | -60.129 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb77c0bf-2e6d-3af2-9e7a-1d7a86a2393e | 4.4813 | -60.56525 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 709cd2c1-b075-370e-91b6-6148d32cee91 | 4.03813 | -60.13422 | 2026-02-20 05:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7787658-c653-36f1-96ae-7b8a6b2a3374 | 2.56008 | -60.56236 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 2ad3ecaa-8a59-3b84-9762-4eb82509daa6 | 2.69817 | -60.22153 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42d772f0-44de-3ffb-a974-06a0d493c5f2 | 3.23001 | -61.19661 | 2026-02-20 05:48:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df2ff996-f288-3b32-96c1-08230ba3eb14 | 4.07246 | -61.1697 | 2026-02-20 05:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3366b76a-0d75-3f09-8b8e-9bdf8dbe71fb | 2.70059 | -60.23676 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54736cd1-a9a9-38e3-b8dd-b1e361539ad9 | 3.99724 | -59.88519 | 2026-02-20 05:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 595d9bf2-2055-3cf7-8b5a-27a1d5b5a8da | 2.54138 | -60.72551 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e8979e1-eb92-3298-9c64-efcfa4c9bb4a | 4.48206 | -60.57003 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0669f177-fede-37b9-b491-4d4a49331b34 | 2.69921 | -60.235 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 79f79685-a853-3fb4-a14e-1142ef4bb540 | 4.49951 | -60.58076 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04224655-29d1-3637-8765-31dfedbe3b1e | 4.16501 | -60.933 | 2026-02-20 05:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a36b4e0f-b78d-3d16-8ebd-97c7505ca38a | 4.07828 | -60.18448 | 2026-02-20 05:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5ebbf28-cec8-3e4f-95c1-91c6a72a4d9d | 4.4988 | -60.57792 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 805475bc-e378-393e-bb31-979ca9001565 | 2.5562 | -60.56298 | 2026-02-20 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 067ab166-7a4c-3085-9f6d-08486c60b8b0 | 4.26742 | -59.79475 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 770341c2-844a-3a8f-8ec8-4a8c6e661ded | 4.10707 | -60.6498 | 2026-02-20 05:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 508428d1-2b1f-3b73-ba32-b0c69b003a70 | 4.26679 | -59.79098 | 2026-02-20 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c50aeab-274e-32e1-a777-987bde6b6007 | 2.68152 | -60.21894 | 2026-02-20 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d44535e8-89b2-378c-8f60-a404d0b7f2d1 | 2.562 | -60.5648 | 2026-02-20 05:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b70ad0ae-3391-31e1-887e-1e405d83ebd9 | -10.67178 | -59.3587 | 2026-02-20 05:52:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cd0ecd5-23d8-3255-b4c6-167b078afbbe | -13.48812 | -60.38519 | 2026-02-20 05:52:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 417fcab0-3f28-3e4d-b27c-9a64356dbbfc | 2.562 | -60.5648 | 2026-02-20 06:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 31294b85-8207-3730-a453-0497d1e20596 | 2.5438 | -60.5651 | 2026-02-20 06:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a162b087-be13-383e-af21-3d09112a279e | 2.562 | -60.5648 | 2026-02-20 06:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d2cb356c-c853-3772-80a3-349fdd682f7c | -18.97296 | -52.93064 | 2026-02-20 06:12:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 29e501d2-acb8-3d1d-a2f6-3c2c44089841 | -18.97576 | -52.91492 | 2026-02-20 06:12:00 | AQUA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6e8866ac-c41e-3621-a393-77c96c559a2c | 2.562 | -60.5648 | 2026-02-20 06:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7ecea77f-1d5f-3ea1-b9a2-72745f1cbeac | 2.5438 | -60.5651 | 2026-02-20 06:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ea2853af-1e8c-35f6-b6ae-64a6153c1dce | 2.562 | -60.5648 | 2026-02-20 06:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 13a21650-88b6-39b6-bc12-b796166ac160 | 2.562 | -60.5648 | 2026-02-20 06:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2626722f-1192-3e10-8a3d-2b60422ba25d | 2.5438 | -60.5651 | 2026-02-20 06:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a85ad4fc-cfd2-33f8-9c3c-38979a3f4a50 | 2.562 | -60.5648 | 2026-02-20 06:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 00b50e61-d11a-3cb6-a0bb-efa57646af29 | 2.562 | -60.5648 | 2026-02-20 07:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 47ed7ca1-d1c2-3b61-bc72-50cce1ee46de | 2.5438 | -60.5651 | 2026-02-20 07:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7ad8ff45-53be-34e2-a56e-f07744b965e0 | 2.562 | -60.5648 | 2026-02-20 07:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fd40624c-dd47-374f-b4af-b062ba949157 | 2.562 | -60.5648 | 2026-02-20 07:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e27701c8-3e1f-37e5-9865-1038a5681105 | 2.562 | -60.5648 | 2026-02-20 07:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f46d0649-fbe8-3f5c-a2d4-db066b830902 | 2.5438 | -60.5651 | 2026-02-20 07:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 49fdc78b-d91a-36ee-8bb2-73d9f9f04972 | 2.562 | -60.5648 | 2026-02-20 07:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 88771264-05b2-33b6-b891-9ded2b7a1893 | 2.55897 | -60.56198 | 2026-02-20 07:43:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9eae7cd4-d4be-32d9-82ac-680b0e99cd9d | 2.55556 | -60.53994 | 2026-02-20 07:43:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| bc00e10e-b123-3f94-9fcd-38ddeab62147 | 0.4648 | -60.3925 | 2026-02-20 07:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.6 |
| b8cf84b8-d1ca-38e5-abc7-2fa18d41cc75 | 2.562 | -60.5648 | 2026-02-20 07:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c668628d-47e0-30f3-9e79-041c629a8710 | 2.562 | -60.5648 | 2026-02-20 08:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f5f063fe-6776-391e-935b-d4518a63a5ad | 2.5438 | -60.5651 | 2026-02-20 08:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.5 |
| f15ba636-d29d-363f-89ad-c16267e679d5 | 2.562 | -60.5648 | 2026-02-20 08:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ac16b29d-0e5f-3f64-aaf8-5b8defb66de9 | 2.5438 | -60.5651 | 2026-02-20 08:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 90b639eb-6bf1-379f-af7c-154582b3e5c7 | 2.562 | -60.5648 | 2026-02-20 08:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 28116e34-0cda-32a7-ac55-0677f6c423f1 | 2.562 | -60.5648 | 2026-02-20 08:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7bb1d2cb-d45c-309e-88ab-50fd842a2dc7 | 2.562 | -60.5648 | 2026-02-20 08:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cf5c66a9-5ad0-3a3b-a57d-eb2f449271b0 | 2.562 | -60.5648 | 2026-02-20 08:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3b783fbc-267d-32a5-9353-e943a2797bfc | 2.562 | -60.5648 | 2026-02-20 09:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9d72d5eb-2d73-313a-ae96-03a9c65029ea | -11.51195 | -38.5413 | 2026-02-20 11:32:00 | TERRA_M-M | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 016902e0-3fab-30cd-9a75-8cf1e03b6928 | -9.48144 | -37.43478 | 2026-02-20 11:32:00 | TERRA_M-M | CARNEIROS | ALAGOAS | Brasil | 2701803 | 27 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b25d1e5e-c8ec-33a4-b725-3b636b976a0f | -8.09119 | -35.56121 | 2026-02-20 11:32:00 | TERRA_M-M | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 01f64071-eabb-35b6-ab74-14b2d03b74b4 | -9.0759 | -36.68202 | 2026-02-20 11:32:00 | TERRA_M-M | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2d60861a-475e-368f-99cd-13a697410f25 | -9.85613 | -37.39009 | 2026-02-20 11:32:00 | TERRA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 65bf0948-144d-3242-aa20-ae1ef658bd89 | -6.01662 | -35.40882 | 2026-02-20 11:32:00 | TERRA_M-M | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 68.7 |
| b041ed0e-528b-3923-b242-78dbd6dbe09c | -6.53781 | -35.10326 | 2026-02-20 11:32:00 | TERRA_M-M | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| a77373e1-ec09-380c-94cd-e481c6b66ab7 | -17.6613 | -40.57785 | 2026-02-20 11:34:00 | TERRA_M-M | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3209f071-055d-325f-bada-5c47b2efc3cb | -17.3924 | -39.24278 | 2026-02-20 11:34:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 41.2 |
| 2a6171bf-fe13-3e16-9d47-c9705736c10c | -17.39373 | -39.23279 | 2026-02-20 11:34:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 1cff25cf-2bc0-3f9a-b444-7abc47875b43 | -18.17096 | -39.75119 | 2026-02-20 11:34:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 267e826a-d03f-32c1-9c9d-55608119e493 | -17.40157 | -39.24408 | 2026-02-20 11:34:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 3a30c00f-c574-3c0e-89c6-8e3038c92882 | -17.2649 | -40.96332 | 2026-02-20 11:34:00 | TERRA_M-M | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 293026d5-e442-3faa-b0f9-b434959fa870 | -17.4029 | -39.2341 | 2026-02-20 11:34:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| a3851785-cb24-3475-9974-3fee5a81c5c6 | -18.67964 | -41.63865 | 2026-02-20 11:34:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 35959a2c-8be8-330a-a6da-20131a1962f4 | -17.4114 | -39.6267 | 2026-02-20 13:00:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 158.7 |
| b3ac0257-8092-3362-803f-4797f57ee9e9 | -17.4114 | -39.6267 | 2026-02-20 13:10:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 156.6 |
| a94b4092-bea8-323e-94b5-2afad87b3929 | -17.4114 | -39.6267 | 2026-02-20 13:20:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 163.5 |
| de8985aa-9fb6-3778-ad9c-aeb958eefc0f | 2.562 | -60.5648 | 2026-02-20 13:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 422f981e-e4d9-3a2e-852c-6b061ccee53c | 2.562 | -60.5648 | 2026-02-20 13:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 4385e722-7868-3f5d-be48-f442769608dc | 2.562 | -60.5648 | 2026-02-20 13:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 112.0 |


[Clique aqui para ver as próximas entradas](README8.md)
