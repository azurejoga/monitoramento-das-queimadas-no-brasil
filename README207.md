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

## Dados Diários - Página 207

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 178a5c83-9bab-3e97-ab60-dbe96b722b66 | -16.6496 | -57.3558 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.7 |
| ff004777-aacd-3ee5-82a0-a5a6d7125922 | -16.6698 | -57.3126 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 16d6b1ec-6b49-30c5-97ff-54990637e84f | -17.197 | -57.3741 | 2024-10-03 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 848d036c-6eda-366c-ac82-599a1bfd185d | -17.1967 | -57.3946 | 2024-10-03 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 3978ed70-964e-3b46-ba46-c69474b5947a | -17.1774 | -57.3764 | 2024-10-03 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 236.4 |
| ea065924-c407-3881-aa0a-b95a02700a2a | -17.1771 | -57.3969 | 2024-10-03 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 258.5 |
| 489f2dfe-ec16-308a-aedf-56d05b7c92b7 | -17.1574 | -57.3993 | 2024-10-03 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.1 |
| 2cab24b2-9f73-302b-bfea-9d161832787e | -17.1577 | -57.3787 | 2024-10-03 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 65273052-da74-3a5d-90a1-a183dc3c4b64 | -9.0515 | -67.871 | 2024-10-03 08:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 22248629-c1cf-3e87-992a-b7f57498c3f5 | -12.4038 | -63.0009 | 2024-10-03 08:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 226.7 |
| 54fe23be-fdcf-3700-a768-de7d97f12a44 | -12.404 | -62.9817 | 2024-10-03 08:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 45cf470e-12d1-3765-a38c-5e7b40ff1d81 | -12.4225 | -63.019 | 2024-10-03 08:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9df8e257-4871-3225-96b7-8ca35a2ab915 | -12.4227 | -62.9999 | 2024-10-03 08:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 367.4 |
| 18716eb9-743a-34cc-ab2b-0ecdbcfd1674 | -12.4228 | -62.9807 | 2024-10-03 08:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 47f34d2a-ffdf-34c6-9f10-5e35622f5aba | -12.4416 | -62.9988 | 2024-10-03 08:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| cd83f1ac-cb4b-3050-92a4-87262259ff51 | -12.8049 | -62.497 | 2024-10-03 08:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b94feb69-4aae-3e35-b8ec-9a3161467cdd | -12.8994 | -62.5106 | 2024-10-03 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| b9783011-721b-3fc1-a32f-134c87764e77 | -12.8996 | -62.4913 | 2024-10-03 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 8b987178-130f-388c-b8a5-82fd874add71 | -12.8998 | -62.472 | 2024-10-03 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 116.1 |
| edeb8320-38cd-3f0f-bf38-f3a50b6c2b76 | -12.8999 | -62.4527 | 2024-10-03 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9f4b1509-0215-3368-90bb-d5677bafc0e4 | -12.9186 | -62.4901 | 2024-10-03 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f4e162ad-3944-302b-8d67-f16812c4a5db | -16.4337 | -57.4414 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| dee847ef-382c-3deb-b684-542945361585 | -16.4529 | -57.4597 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 3f60f1a4-614f-3069-abe6-53a08d0bceb7 | -16.4533 | -57.4392 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 62244359-6aaf-3266-ab93-6229baed0569 | -16.4728 | -57.437 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| f99d2eab-1806-3864-bf2b-cf6856445bc0 | -16.5317 | -57.41 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 4c884e47-b779-3135-8283-f482abb0ebf4 | -16.5387 | -58.2427 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 9577798c-b3f1-3b14-b720-14d07b8d5923 | -16.539 | -58.2225 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 86c5499a-ae9d-3975-a82d-6aba1614bd33 | -16.5393 | -58.2022 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| f3a07021-134f-3307-9472-3ddc5e37e571 | -16.5512 | -57.4078 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.9 |
| 51c8dd7a-d4ee-3755-86f5-69f9bd89004c | -16.4334 | -57.4618 | 2024-10-03 08:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 3fec78de-de27-3ea5-af6c-35a8b0e6d67e | -16.5582 | -58.2407 | 2024-10-03 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 9055bed9-1635-34d5-9bd0-e95c49fed76a | -16.5585 | -58.2204 | 2024-10-03 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 0d3319ee-6da9-383b-8b24-062e9bd94bf9 | -16.5588 | -58.2001 | 2024-10-03 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 77ebe3e2-ba15-39fb-813e-c536de884c42 | -16.5733 | -57.2419 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| f784f539-9762-34e5-bee4-230a26895453 | -16.5928 | -57.2397 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.5 |
| fe74d897-9728-3022-b625-8cfc956a5ea5 | -16.6294 | -57.3989 | 2024-10-03 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| df1a8d2a-3da8-34a9-b907-4512baa4ded1 | -16.6297 | -57.3785 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 228.7 |
| 28e8a805-bd84-3634-b84d-49bf0c9487c4 | -16.63 | -57.358 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 7c8c9b29-9088-30b0-8b65-316be1f8e2e3 | -16.6489 | -57.3967 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 158.4 |
| a9e4377a-0648-3b0e-9fcc-6947fd7500e7 | -16.6492 | -57.3763 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 479.6 |
| 971c06cd-78bf-3bf0-9171-d51af3dc71a4 | -16.6496 | -57.3558 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| deea8231-61f9-3ae8-aeec-35d3197300cf | -16.6698 | -57.3126 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| 7e35a087-87cc-343d-adb6-81753f4c8841 | -16.6723 | -57.1488 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 391a39fc-76a9-3593-b77e-5862b0d321f6 | -16.6868 | -57.4741 | 2024-10-03 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 780a3e56-6e65-3ce7-a264-71bbce4034a3 | -16.6893 | -57.3104 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 94b23124-8b12-3a70-8480-b11fd4cfed32 | -16.5931 | -57.2192 | 2024-10-03 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| a6d8b3eb-8d63-30f9-b114-110ce02dea0f | -17.0692 | -56.7939 | 2024-10-03 08:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 56cd38da-2b05-3719-a1b6-e35f35a381ee | -9.0515 | -67.871 | 2024-10-03 09:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 66c06328-0a10-3de8-8d6e-9489067897b5 | -12.4416 | -62.9988 | 2024-10-03 09:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 86c10699-2238-3054-b7fe-5e8da928275a | -12.4038 | -63.0009 | 2024-10-03 09:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 34212011-34d4-3de8-99cd-f0dcc4983b75 | -12.404 | -62.9817 | 2024-10-03 09:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 1cc42fe0-4bf3-3145-b332-eb6ec73e8a14 | -12.4225 | -63.019 | 2024-10-03 09:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| f8144d64-0b60-3d14-87cf-e356e9670abc | -12.4227 | -62.9999 | 2024-10-03 09:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 294.7 |
| c7ead86a-035c-3c96-bd66-4a4b7d7451dd | -12.4228 | -62.9807 | 2024-10-03 09:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 3bdcda8c-d4f9-3dc4-9922-d0f969281c1b | -12.8049 | -62.497 | 2024-10-03 09:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 68c71b4a-bea4-353d-bf8c-f8db6f244729 | -12.824 | -62.4766 | 2024-10-03 09:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e8201f47-0846-3312-ae49-803c3b47618c | -12.8429 | -62.4754 | 2024-10-03 09:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| ee1aeb96-d565-31a9-a89d-ab65ac92f06f | -22.3711 | -47.9225 | 2024-10-03 09:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 638d759b-c710-3249-9726-6faf949ffca8 | -12.4225 | -63.019 | 2024-10-03 09:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 204a451d-fd57-32bd-bc47-793b30325fe6 | -12.404 | -62.9817 | 2024-10-03 09:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1de2a5a3-ff59-3b8b-9986-6990598d0e22 | -12.4038 | -63.0009 | 2024-10-03 09:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 152.0 |
| af4d4fc0-daf1-3186-b430-097354be5e7c | -12.4416 | -62.9988 | 2024-10-03 09:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 42c15353-7349-369d-b76d-29dd02e926ad | -12.4228 | -62.9807 | 2024-10-03 09:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 929ea013-04c4-3e31-889c-26aaae00ff68 | -12.4227 | -62.9999 | 2024-10-03 09:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 227.2 |
| 683dc52b-8757-3922-a8be-f4e9ae0f43e1 | -12.8049 | -62.497 | 2024-10-03 09:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| faf4196b-3612-30eb-aceb-5612c8379b4e | -12.8429 | -62.4754 | 2024-10-03 09:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0bfdf99a-443c-37f2-99af-ef9fdcbb92a2 | -12.824 | -62.4766 | 2024-10-03 09:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6f50f008-fb62-30e5-b470-0b043bde7e31 | -22.3711 | -47.9225 | 2024-10-03 09:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 175.5 |
| e7ebd548-13df-3711-9847-ff6f860d4fd2 | -19.2954 | -42.6032 | 2024-10-03 09:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 163.5 |
| c4eb7566-87f6-3036-b4e2-919beb3396ef | -19.2962 | -42.5779 | 2024-10-03 09:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 183.1 |
| 59de7d11-7034-3d74-8a85-96bd0b98e3f1 | -16.6698 | -57.3126 | 2024-10-03 09:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 7a6dc204-1013-3e5c-aa8a-e5be51f70faa | -16.5588 | -58.2001 | 2024-10-03 09:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.1 |
| ba5af610-4f08-327e-8d09-96cbea9fd433 | -16.6496 | -57.3558 | 2024-10-03 09:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.5 |
| 7138f131-9324-38a8-a920-3698c3fce1fa | -16.7458 | -57.4469 | 2024-10-03 09:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 6a811922-ccf2-3808-be0a-26ac0d26aafa | -16.6297 | -57.3785 | 2024-10-03 09:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 192.5 |
| 2db45bb9-b92d-3c7c-b4f6-2ef79c86ce20 | -16.63 | -57.358 | 2024-10-03 09:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 161.1 |
| 0f21ff99-8249-388f-b91c-aac4e549118f | -16.6492 | -57.3763 | 2024-10-03 09:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 212.3 |
| 8c71a714-ef3e-3aa9-856f-2f1194fdc5ef | -16.7455 | -57.4674 | 2024-10-03 09:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 199.6 |
| aadd760c-c114-386f-a867-90a303c711d1 | -16.765 | -57.4652 | 2024-10-03 09:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 6ff463f6-1683-395c-8e57-b3dce7333e27 | -17.0306 | -56.7575 | 2024-10-03 09:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.6 |
| 0697e726-4991-318b-872a-f66e95915980 | -17.1577 | -57.3787 | 2024-10-03 09:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 202.1 |
| b5cd6e6f-9238-32d5-a820-68bb5525a39a | -17.1574 | -57.3993 | 2024-10-03 09:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 239.3 |
| f4d99c93-edcf-39b1-a2ee-15e14fad49ac | -17.1771 | -57.3969 | 2024-10-03 09:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 241.7 |
| 42d515e7-df34-3c12-8ac9-df343042961b | -17.1774 | -57.3764 | 2024-10-03 09:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 229.3 |
| dfcd98a9-331e-31ca-bd07-08859d244f66 | -16.7455 | -57.4674 | 2024-10-03 09:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 195.1 |
| a0873d6d-0951-3f0e-a048-cd12886f80df | -16.6698 | -57.3126 | 2024-10-03 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.4 |
| ad331fc0-1ddc-3738-8f0b-c3fa70d0aa75 | -16.6496 | -57.3558 | 2024-10-03 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 311.3 |
| c660da1c-804e-3261-81d5-5d1f571f40b5 | -16.6492 | -57.3763 | 2024-10-03 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 422.7 |
| 082dc419-098d-3bfc-a12c-0d6fff9b355c | -16.63 | -57.358 | 2024-10-03 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 281.6 |
| 8aaa0914-b672-3535-a5f9-fb55def4d3b6 | -16.6297 | -57.3785 | 2024-10-03 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 291.2 |
| 154c829f-5a64-31fc-ad26-5ce7b3b20d02 | -16.765 | -57.4652 | 2024-10-03 09:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 62b486b1-68c4-3261-af4f-dd5e8ef49ee2 | -17.1774 | -57.3764 | 2024-10-03 09:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 234.4 |
| c687e458-9904-356d-b1a1-9a264f5cf631 | -17.1577 | -57.3787 | 2024-10-03 09:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.9 |
| dc2c0a4e-df29-310d-aebb-d4d8a6f21eda | -17.1771 | -57.3969 | 2024-10-03 09:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 233.5 |
| 79226cfb-c6c7-3141-9962-bb3069f8a930 | -17.1574 | -57.3993 | 2024-10-03 09:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 219.1 |
| ef4e1948-2792-3d7b-9dce-f2af452c0da1 | -12.4227 | -62.9999 | 2024-10-03 10:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 632.3 |
| 1a97a1f2-bc98-3001-a61e-d2d87e4d6cac | -12.4228 | -62.9807 | 2024-10-03 10:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 328.1 |
| 1f5754be-1781-30d1-8ca8-5b384a317e74 | -12.4416 | -62.9988 | 2024-10-03 10:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 74e041d4-e396-3180-b3d9-d3b372b58b59 | -12.4225 | -63.019 | 2024-10-03 10:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |


[Clique aqui para ver as próximas entradas](README208.md)
