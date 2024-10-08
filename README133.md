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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e384892f-9675-3a56-bf2e-22a36b927f63 | -10.8754 | -63.9169 | 2024-10-08 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 70feeb85-364d-3af3-af23-f7393d902a65 | -10.8755 | -63.8979 | 2024-10-08 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3bba5a17-2961-3f27-abc4-3f4c6eed5860 | -10.8924 | -64.1813 | 2024-10-08 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d84c94fd-b667-35d9-9478-4fbfb55b8e36 | -10.8925 | -64.1623 | 2024-10-08 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 3fce4b99-f34a-37fa-93ac-45718da6bbb0 | -10.8941 | -63.916 | 2024-10-08 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 415e5738-d0d5-3d17-9287-b6cb19e60beb | -10.9112 | -64.1615 | 2024-10-08 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ea54ae92-e2c6-3bf2-908e-c9aa799fd580 | -10.8926 | -64.1434 | 2024-10-08 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c6b4ba5a-0f5d-39a7-b6bd-372c1101f2f1 | -12.4605 | -62.9977 | 2024-10-08 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 04868747-4fbb-3f54-bb35-9ccf0cb1e993 | -16.4184 | -55.9455 | 2024-10-08 07:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 7fe29bbc-0216-34d8-908c-fd1ccec68470 | -16.7852 | -57.422 | 2024-10-08 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| 11603dc2-3b86-3bec-8d20-f78982a1783f | -16.8048 | -57.4197 | 2024-10-08 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 15d048ce-0341-3f0b-9fd2-a67fc9505f68 | -16.9407 | -57.4859 | 2024-10-08 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| f430ae6b-793e-3477-9faf-ab1b16cd53c9 | -16.9211 | -57.4881 | 2024-10-08 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 21a34c5d-a7b2-3903-976e-8f36b7c41641 | -17.1178 | -57.4244 | 2024-10-08 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 773a8aa0-f83d-3f25-9276-6acdd6464783 | -17.0992 | -57.3651 | 2024-10-08 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.9 |
| 5d6f8b9e-ebbf-3d7c-9d0c-5b14c9faaace | -18.4931 | -53.4457 | 2024-10-08 07:26:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 3d110f93-1ede-3f6e-932a-1c4f96b7f897 | -20.3724 | -48.8372 | 2024-10-08 07:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2127f7b5-589b-34ae-9ddb-5cd52d694f33 | -20.3519 | -48.8417 | 2024-10-08 07:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 455763a8-f825-361c-9a03-da1ca7ec93c6 | -10.9113 | -64.1426 | 2024-10-08 07:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 04d0625a-d10f-34eb-a3a9-3b1559df737b | -10.9112 | -64.1615 | 2024-10-08 07:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 118.3 |
| a5951f01-1099-36db-a853-333f7753986b | -10.8925 | -64.1623 | 2024-10-08 07:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 9470ff8a-ca2c-3991-aee6-ad33523e8274 | -10.8754 | -63.9169 | 2024-10-08 07:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4b95b1b0-47eb-3fed-9d01-c2e9198ed4a1 | -10.8755 | -63.8979 | 2024-10-08 07:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 209d6909-b58d-3194-8989-7ba5856af809 | -16.7852 | -57.422 | 2024-10-08 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| bf10e15b-79c4-3f8b-8021-c9bc5e137770 | -16.8045 | -57.4402 | 2024-10-08 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 1e6c7d3d-c60e-37a4-a6f4-1c27bef861ac | -16.8048 | -57.4197 | 2024-10-08 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 08d68a73-338a-363d-84f8-8f7dd72d6162 | -16.941 | -57.4654 | 2024-10-08 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 15840a47-d35a-3c56-9c4f-3de280d3813a | -16.9407 | -57.4859 | 2024-10-08 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 44d97133-517d-33dc-83e3-dcbcf654a63a | -16.9211 | -57.4881 | 2024-10-08 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| afe56f3b-f403-3d60-b674-983faeeb36a8 | -17.0992 | -57.3651 | 2024-10-08 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 39cbc162-9dd1-30ea-b025-cff2c8c5008b | -17.1178 | -57.4244 | 2024-10-08 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 3a108de9-a05a-348e-8b8c-6ca5741a691b | -18.4931 | -53.4457 | 2024-10-08 07:36:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 9f8f6ac7-be06-3869-b280-3f3a43482cac | -20.3519 | -48.8417 | 2024-10-08 07:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 48ef1ba4-a21e-379f-8413-2f3b64d7afe6 | -10.8754 | -63.9169 | 2024-10-08 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9f50b0a9-6bbe-3f56-b6cb-28766da4e20e | -10.8924 | -64.1813 | 2024-10-08 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 363e7623-bc3d-33f2-8ad0-474f41c534c0 | -10.8755 | -63.8979 | 2024-10-08 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e09a0dfe-7c0e-3a4e-9aa0-6fab01ae8fef | -10.8925 | -64.1623 | 2024-10-08 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 74f30656-7f94-3933-b15c-1300e37b1649 | -10.8926 | -64.1434 | 2024-10-08 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f462aef4-8982-3ba8-bec3-d7207b5973f6 | -10.9112 | -64.1615 | 2024-10-08 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e5ec7a88-5aac-3cbf-b31d-15e83e21cb42 | -16.8048 | -57.4197 | 2024-10-08 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 244782a4-8c43-35f3-b1e6-7584a89cf4b9 | -16.7852 | -57.422 | 2024-10-08 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 4e734d76-783c-3868-b7aa-83ebb3bfa63f | -16.9407 | -57.4859 | 2024-10-08 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.6 |
| fc8285e1-b86d-3acd-aa85-d7f841b34bd9 | -16.9211 | -57.4881 | 2024-10-08 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 4eedf4c4-eea4-3b87-b1ab-a574ed87520a | -17.0992 | -57.3651 | 2024-10-08 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| eb6e7315-22d4-37c0-afd9-bd78f4c53a2c | -18.4931 | -53.4457 | 2024-10-08 07:46:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 1ebbcc21-f7ee-3da8-876c-1994725f6d54 | -18.6192 | -57.2603 | 2024-10-08 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 90cb6754-685e-338c-9c39-619f993d97ec | -20.4851 | -46.9986 | 2024-10-08 07:46:59 | GOES-16 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d7d82923-bfe0-3148-8923-97ef2ce10928 | -20.3724 | -48.8372 | 2024-10-08 07:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 216d919a-5ed4-30ad-9452-bc365a062c20 | -10.9112 | -64.1615 | 2024-10-08 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1c5c74b6-4f38-3940-b23d-8d954d6b65e3 | -10.8755 | -63.8979 | 2024-10-08 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d242fbc1-c1f5-3011-a561-4ca92ebbd1b0 | -10.8754 | -63.9169 | 2024-10-08 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6cef299d-76eb-330a-aee5-fe5e242f3a91 | -10.8941 | -63.916 | 2024-10-08 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 82c2617a-8229-31c7-ab86-27246d099402 | -10.8926 | -64.1434 | 2024-10-08 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 50d6d1e4-831b-3d1c-b250-03a7dbfaacc8 | -10.8925 | -64.1623 | 2024-10-08 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.4 |
| f38e9b9f-b890-3df0-87b8-7775ac594f93 | -10.8924 | -64.1813 | 2024-10-08 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| b6a0f231-16d6-3fe9-a0ce-90c5df92ef96 | -16.6922 | -57.126 | 2024-10-08 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 5d45e23d-06a5-37d7-8016-076d9c135b9b | -16.6733 | -57.0872 | 2024-10-08 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.2 |
| 33af66b4-9e97-3015-be14-a25c37ff5f42 | -16.6531 | -57.1305 | 2024-10-08 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.4 |
| 998f98f3-634c-3cf5-a12d-002040a3982e | -16.6726 | -57.1283 | 2024-10-08 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| e8e348b7-5578-3aaf-8d3b-2b411669af65 | -16.6925 | -57.1055 | 2024-10-08 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 5ec5a181-767c-3841-8088-0922cc933ae6 | -16.673 | -57.1077 | 2024-10-08 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| bbf98bdb-38b0-3664-b495-0b67d33f279f | -16.8048 | -57.4197 | 2024-10-08 07:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.9 |
| 29c0547e-230e-323d-9ca1-421215dcc7ef | -16.9214 | -57.4676 | 2024-10-08 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.1 |
| f68bcce5-0257-39cb-84ab-8f7fdb708a45 | -16.9211 | -57.4881 | 2024-10-08 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.4 |
| 5c3ad74c-73d7-3cb8-91ae-b74d4daa594b | -18.4926 | -53.4672 | 2024-10-08 07:56:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 38.1 |
| dc104e07-bf17-3b1d-833a-7253c0ee0b10 | -18.4931 | -53.4457 | 2024-10-08 07:56:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0ebf806a-4e5c-3d27-a82b-1244cfcbacf9 | -18.6192 | -57.2603 | 2024-10-08 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| b03b69c1-b39f-3a45-8e4d-13b1ae403aa0 | -20.4851 | -46.9986 | 2024-10-08 07:56:59 | GOES-16 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4ca96d9d-743d-3328-a32d-c7db138cfb48 | -10.8925 | -64.1623 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| bcd99a51-743f-3505-8d2c-0c9b5afbbe5c | -10.8941 | -63.916 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| c4792641-8d7d-3e5f-9a08-913b4fe3ffee | -10.9111 | -64.1805 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 4e841866-0a57-3849-a09c-9311ff3c253c | -10.9112 | -64.1615 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 778400d1-a6f2-38b6-b774-02cd7c4f398d | -10.9113 | -64.1426 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d7ef5841-9f1c-3cc9-8788-85f180eff3da | -10.8755 | -63.8979 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cbea3115-fa31-33f8-9fef-fe0f0393f176 | -10.8754 | -63.9169 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d6e1ccdc-c432-36d0-8719-7100965c8971 | -10.8926 | -64.1434 | 2024-10-08 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4857d56e-7d91-3c57-b91e-93296f1a3b7a | -12.4605 | -62.9977 | 2024-10-08 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 09a2c134-cbd7-3310-aecc-5e164a2da3ea | -16.6925 | -57.1055 | 2024-10-08 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.8 |
| 67728486-540a-3a3d-8c80-009bd5a41093 | -16.6922 | -57.126 | 2024-10-08 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 9ac9505c-7039-39dd-a6dc-4e05f27f1cba | -16.6726 | -57.1283 | 2024-10-08 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.2 |
| cd3a9bcf-7d30-3937-8562-58b86a925e8a | -16.673 | -57.1077 | 2024-10-08 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 9119af24-a15c-3112-b413-f07ec1dc0d5c | -16.6733 | -57.0872 | 2024-10-08 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 0a83f4a0-7194-365c-9ee4-d6c1262fb591 | -16.8048 | -57.4197 | 2024-10-08 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 6a9c804a-e991-38af-a799-0aaf37e68a2c | -16.9407 | -57.4859 | 2024-10-08 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| f3537547-37ec-30cc-80e1-20bb0c7f59de | -17.0992 | -57.3651 | 2024-10-08 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.5 |
| 88cdc864-c79d-329c-acf0-a0f68ba938c3 | -18.4931 | -53.4457 | 2024-10-08 08:06:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5ea29c7c-1912-3687-aa42-00113b73cf32 | -18.6192 | -57.2603 | 2024-10-08 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 6e240374-96bd-3ecd-9c28-a8e9777ffc87 | -20.4851 | -46.9986 | 2024-10-08 08:06:59 | GOES-16 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 98787896-078c-3058-975b-69e57df4b652 | -10.8754 | -63.9169 | 2024-10-08 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| aa596d24-65ec-365a-b3c5-f2cdca47076f | -10.8755 | -63.8979 | 2024-10-08 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f5afb296-4f0a-3c1a-a5e6-37c1868ce8f8 | -10.8924 | -64.1813 | 2024-10-08 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| e7d0a088-ecff-312f-a1fc-4fb623f8e7c0 | -10.8925 | -64.1623 | 2024-10-08 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 128.3 |
| ce4e5a1f-5082-3564-948b-6f2f532d38ba | -10.8926 | -64.1434 | 2024-10-08 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fcd8b9c5-f760-3b62-95dd-ba74345deb89 | -10.9113 | -64.1426 | 2024-10-08 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| fa1a2bcb-d1e1-375d-bbc4-80e47218f902 | -10.9112 | -64.1615 | 2024-10-08 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 146.9 |
| a9a26cc8-63a1-3d67-ad4c-fce538e5ba40 | -12.4605 | -62.9977 | 2024-10-08 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| d93c8f74-73e3-3796-9456-de4c5a21095d | -16.6726 | -57.1283 | 2024-10-08 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| e1acdc8b-1971-3a3a-91cc-b546da382e23 | -16.673 | -57.1077 | 2024-10-08 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 437993cf-9822-3afd-8063-d234d80aaba6 | -16.7852 | -57.422 | 2024-10-08 08:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| ae713336-48e0-3bfd-857a-235aa0e036a4 | -16.8048 | -57.4197 | 2024-10-08 08:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |


[Clique aqui para ver as próximas entradas](README134.md)
