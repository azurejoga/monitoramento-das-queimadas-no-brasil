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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1214b66a-5b61-3dc2-8f09-163cd552e4ae | -6.84006 | -51.0693 | 2024-10-09 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46ca5e60-a265-3cd3-a17e-ce44bb0ba8a3 | -2.14649 | -50.88667 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2809f0c1-54dc-39a9-80b5-e2430ab4297f | -2.14599 | -50.88978 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0481341-ecdb-3a0d-86b6-39973d9be6e8 | -2.13934 | -50.70165 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c2a4b3a-825a-30b5-84f4-786995a60009 | -2.13884 | -50.70471 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ab7dd6a-9215-3b4a-98bf-5907e17f7aec | -1.96025 | -50.84508 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 767da7c8-7d72-3652-bba2-2951f7d90522 | -1.95973 | -50.84819 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 49083a1b-7fe5-3297-813c-b10a89eaaee3 | -3.55252 | -51.29342 | 2024-10-09 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11416831-2520-38e0-8e66-c9508c69be6e | -3.55199 | -51.29657 | 2024-10-09 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| accb24ba-d524-357a-ab3c-d227366432f8 | -3.48369 | -50.8099 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98a0d4bc-7a12-3b3c-ac1f-49eb502b9710 | -3.48319 | -50.81285 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c06abdb-5aab-3d91-8b2a-1e4610ebb39d | -3.26469 | -51.23936 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea7faa38-031f-308b-8454-b4c08a32ab2f | -3.26001 | -51.58905 | 2024-10-09 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ec83659-0af1-36c9-a62d-aa11120f27af | -3.25948 | -51.23847 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c33c14bf-0f04-3f5f-84d1-fcd22859ceea | -3.25943 | -51.59248 | 2024-10-09 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b8dd29d4-64cb-3b67-8649-cd03203c963c | -3.25894 | -51.24171 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c77b24a-33d6-3151-80d1-cfc07678e572 | -3.21417 | -50.9212 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b41f69c1-290f-325a-babf-e0226c008aaf | -3.20956 | -50.91729 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e393280-8a60-3fa9-82e2-3291bf0f3903 | -3.20495 | -50.91338 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e2ed38d-d62e-3ceb-a362-d1a30c6f6227 | -3.20445 | -50.91643 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2853bcbf-276e-3b38-8dd8-1f86dd9c086b | -3.19985 | -50.91249 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dfdd425-3eb6-3402-8252-ce6b954f955f | -3.03429 | -51.10145 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f61cb45f-2cf2-372d-b524-418a3c46aacd | -3.03374 | -51.10474 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5ad872b-99a3-36e5-b644-9bd5cdb0d3e7 | -2.97539 | -51.02996 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1e68872-4f1c-3db0-b313-8abe7b5197e7 | -2.97021 | -51.02915 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79df6fa4-4daa-3639-bd1a-b4255e67443c | -2.83581 | -52.96731 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 782d6895-6afc-30d6-a1e0-17da297e4599 | -2.87782 | -51.67407 | 2024-10-09 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a366d41-60b9-3500-b698-8b9c64c33d68 | -2.86376 | -51.02081 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93a61b5c-60f8-3eb1-9b0c-0500f3084783 | -2.86327 | -51.02382 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69df3f25-0ea4-33cd-9459-318d61669869 | -2.85857 | -51.02005 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a031e9ce-9503-3ba6-845f-ca9ef2aec1da | -2.8086 | -51.39143 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ba722f-cc7f-39a0-a0f6-1f3852a3ee32 | -4.62882 | -50.98025 | 2024-10-09 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8608f2d5-8322-3ce2-b6ee-c2e162841d90 | -4.62834 | -50.98307 | 2024-10-09 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32de2ccb-4d28-3c56-8ecd-25a469b16125 | -4.16006 | -51.04579 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7c3b09e-9705-30c7-bf47-b2280b108be0 | -4.15505 | -51.04452 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd7ec84e-983a-3476-af58-347ebde5f4ec | -4.15457 | -51.0474 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb9e36a-ceb2-3073-9d14-914d7f2eacac | -4.06389 | -51.11904 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 257b5273-b65e-3ac6-9a15-fa0fdc3364f9 | -4.06089 | -51.11898 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7cb174b-8dfe-30b3-84af-68229b573497 | -4.0604 | -51.12193 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 920d2ac2-a0d3-3bb4-bb00-828ee575e916 | -4.05881 | -51.11803 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7005fc09-80e4-3196-a9ed-98d06c40133c | -4.05832 | -51.12091 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae6c40e3-868e-37f3-8077-29913b4eb957 | -3.92222 | -51.21 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81cdcd0e-0594-376c-bd82-bcc6e76a59f9 | -3.87279 | -51.18897 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b94d30fa-898a-3f23-89d4-9e9aea32bd73 | -6.41378 | -51.71562 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0840e79c-6e92-3751-9978-c7ae7f954811 | -6.41024 | -51.70565 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37d359d8-6afe-3fb2-8c2a-93f58516e4c3 | -6.40974 | -51.70856 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0e58c65-9581-37c2-9083-8be12d531019 | -6.40922 | -51.71151 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0081a3e0-1562-3d53-aadb-ee64ae596aa6 | -6.40867 | -51.71469 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ca7635f-6302-3163-92cc-286667cbee3e | -6.40457 | -51.70798 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8562082-654a-3b9d-97e7-ab26c9cad697 | -6.40353 | -51.71395 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f867633-6827-3d8a-b7dd-0df9d0df0a0c | -6.21151 | -51.51327 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c75af4f-6071-3c2f-adcd-8c411281b2c4 | -6.21099 | -51.51628 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e63ebd1-a49e-34a2-be28-e552e1fe6ebd | -6.08349 | -52.46935 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a05ca53d-1a8c-376b-9f9d-68d11fc1cbba | -6.07808 | -52.46836 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6098153b-e674-3928-8c11-66b5b70b7e14 | -5.90778 | -52.53688 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f15289a-c10f-3fec-ad97-c7b6d21dbb0f | -5.83323 | -51.63993 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eeaf9b8-8e67-3ce5-9ff8-74429696d6d2 | -5.83271 | -51.64293 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6efe0858-c416-3d69-80ae-1377ec135f9a | -5.76469 | -51.44349 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c33a89-a5a4-3585-868e-300d1aeead1f | -5.76366 | -51.44937 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07fdb1b0-5ba8-3ad4-9a86-8c6523ee1d2c | -5.75909 | -51.44559 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b920efa-d33d-3833-b96e-b85c836ceac7 | -5.75857 | -51.44853 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bff8e59-f865-3bb4-8dfd-6d4dae241ada | -6.8985 | -52.19144 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| becc274e-96df-38b8-88b8-6e2fa78a404d | -6.89791 | -52.19475 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edd1ccae-8f9b-33cd-960c-4951eeb691e8 | -6.89782 | -52.19421 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9df04f10-7c82-30f4-b9a3-759b9be67287 | -6.78859 | -51.65789 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e50d45a-c266-3626-b290-03a1209d033e | -6.78451 | -51.6589 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4246a0ba-9478-3462-a1f6-6d02411189f2 | -3.03365 | -52.53417 | 2024-10-09 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2f04d58-9782-3b59-b13d-24fad308afdb | -2.1999 | -51.95765 | 2024-10-09 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da756c2c-e70b-3332-b949-c9261267f4db | -2.0802 | -52.02886 | 2024-10-09 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c4a4c3ba-6830-36fa-ba34-12e6bd2e54fe | -2.07705 | -52.02465 | 2024-10-09 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6ec529ac-39af-3f73-b14c-cc1958ef1dba | -2.07645 | -52.02842 | 2024-10-09 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 14d9babd-851d-3a87-b0dc-ab839e999d57 | -2.07523 | -52.0242 | 2024-10-09 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1f8a869-162e-3af7-ab90-08484fb80bf8 | -2.07459 | -52.02798 | 2024-10-09 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d1ef617-4336-3b3d-baa2-198d203fb6a5 | -3.33179 | -53.39208 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 033963dc-a8c4-39ad-884a-4ba691073e7a | -3.32575 | -53.39127 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69171e61-baf1-33a8-8dd7-1a975a40e1bc | -3.04428 | -53.04107 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbfe0bfc-e32b-3d42-8432-3a9d7d7b0a61 | -3.04354 | -53.04542 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edbb96b9-b5c3-3467-9696-68e687ee0472 | -3.03837 | -53.04013 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aaf951e-8601-3d84-aebb-0bc7803df6fa | -3.03765 | -53.04439 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d085af41-5572-3da1-a862-4f3b6cfa07c3 | -2.86409 | -52.90651 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dadbe5ac-441f-3d0f-a755-75e986acc619 | -2.86339 | -52.91071 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d526c777-929d-3afe-99fa-5f497525b692 | -2.84729 | -53.31701 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdd185f9-a4bf-32aa-9ad8-fc65f9d84570 | -2.84652 | -53.32153 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bb340ba-5a85-3c07-a4e1-4670693f38dd | -2.84483 | -53.31895 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db45ea97-fa76-3123-9ab8-a777069f57a1 | -2.84409 | -53.32347 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fd147dd-1c7a-3c10-ac99-fc150339d196 | -2.84248 | -52.96363 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59233fe0-8d9c-3f2d-b7e9-2c1b42c3d794 | -2.84175 | -52.96798 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 108394af-5f3c-34c2-817b-03f0f507fe24 | -2.8405 | -53.32055 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 75415675-7a97-3768-828e-3138a2f9093b | -2.83654 | -52.96294 | 2024-10-09 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34e0384e-45b0-3e71-8d49-62a96ac4102d | -3.58631 | -53.26388 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8d3c252e-0415-392e-9099-494ca5764994 | -3.58555 | -53.26844 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5cbac846-701e-33bf-950b-a35f580ceab9 | -3.5833 | -53.26662 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3dddf2ab-fe26-3927-8e17-ab5bc8a67fb4 | -3.58251 | -53.27114 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7e2e1176-53f0-37b9-9eb1-1c0368a739bd | -3.57959 | -53.26757 | 2024-10-09 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62ac16eb-7f9f-3ed1-a534-735ef3a491bc | -3.89812 | -52.40855 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8e7f5e7-058d-3aff-a5d5-a23be9d326b4 | -3.82907 | -52.40899 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aebb80eb-c4b4-32b5-80c1-39d2478a271e | -3.75086 | -52.31101 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d8f5fbe-94b7-3a2e-8e13-3737b46ceb81 | -3.75025 | -52.31474 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a57614a-218b-36d8-9faf-f8e83ccb6115 | -3.74981 | -52.31076 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0dfefc83-7c49-3ec5-b9e9-e7ab92a66ce8 | -3.74917 | -52.31447 | 2024-10-09 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README81.md)
