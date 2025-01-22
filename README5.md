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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e5e966d-058c-3d6d-8d73-153a90695715 | 3.62635 | -61.65576 | 2025-01-22 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3750fcb9-5036-36a9-a766-f41d03950d46 | -1.64631 | -60.21672 | 2025-01-22 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 433bd2d0-25bd-3619-8c2f-eda3132748eb | 2.83889 | -60.88542 | 2025-01-22 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d92e1ae9-129e-3582-8d5c-bfc6244dfc43 | 4.42278 | -60.65087 | 2025-01-22 05:31:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c20673a-1b78-3f6b-91b4-0f45e15d1b16 | 4.72635 | -60.83068 | 2025-01-22 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1d05cfd-2329-34a4-91bd-b58ab7ab0257 | 0.7678 | -60.45528 | 2025-01-22 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 287c71f1-a891-3dab-b20c-9df6b3f55758 | 4.0941 | -61.40948 | 2025-01-22 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaab0126-9600-3195-8ce6-94c934fb69df | 4.42556 | -60.64693 | 2025-01-22 05:31:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d4f01dd-c480-31a8-a8f9-e21fc0769ea6 | 2.74243 | -60.74688 | 2025-01-22 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f1da9b8-3287-3154-b570-74f291d28b91 | 2.83832 | -60.90332 | 2025-01-22 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12e8cbfd-808a-395e-832c-3f55b6507ae6 | 2.74298 | -60.75037 | 2025-01-22 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89894b3c-a143-3454-aee9-73225e874942 | 3.6076 | -59.9654 | 2025-01-22 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7a1cac3-009f-38f3-a6e3-3df43c6aee0a | 2.83944 | -60.8889 | 2025-01-22 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70008fd1-397a-35f0-bb0f-857b2c5fd9c6 | 4.41946 | -60.65137 | 2025-01-22 05:31:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65f80655-f9bd-3d2a-8728-f982d59b77c1 | 2.20423 | -60.24587 | 2025-01-22 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab04790b-5dc7-3f75-9ee4-dca6fedf6541 | 4.08733 | -60.50772 | 2025-01-22 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13b8fbbb-ee51-3de3-b3cf-ba1154cadb11 | 4.44321 | -60.67259 | 2025-01-22 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5612be0-4b46-3358-9cf8-92b95930254d | 4.08788 | -60.51121 | 2025-01-22 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c12f92ac-f387-3e0a-bd41-8c10f4429f0e | 3.61155 | -59.96847 | 2025-01-22 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46419068-6dad-3a9f-a050-261335e44f45 | 2.83834 | -60.88194 | 2025-01-22 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb799065-cc7b-3bf6-9893-bc3af2778b4a | 2.83777 | -60.89985 | 2025-01-22 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77a792e9-62f8-3773-bde3-72d0f55c25db | 4.72359 | -60.83464 | 2025-01-22 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e238da19-7a64-390d-9f03-36c36ce13524 | 1.71579 | -60.28744 | 2025-01-22 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e8c727e-b11f-3f02-a954-e148a655e4f8 | 4.09065 | -60.50719 | 2025-01-22 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f53920ab-9a71-3b55-aef0-c38c5c5b2b2a | 3.62965 | -61.65524 | 2025-01-22 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ea0dcdd-b8c5-3161-811b-a2d9c839c379 | 2.17738 | -61.81981 | 2025-01-22 05:31:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21d155fb-efbe-3e85-9a76-bcb5a1327b90 | 3.63019 | -61.65867 | 2025-01-22 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5891d094-bf93-3266-a0d9-cf5e4e6ceac4 | 4.42224 | -60.64744 | 2025-01-22 05:31:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18e89fd9-99d7-3a93-9260-184aaf6a9fa7 | 4.0974 | -61.40897 | 2025-01-22 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e834448-0c56-332e-8576-faa02e82bf07 | 2.18564 | -60.25969 | 2025-01-22 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e37504c4-a85c-383b-97af-781ababf2922 | 1.7124 | -60.28796 | 2025-01-22 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d443a0e-7f8c-36e1-b38c-32f3d5d45ae0 | -20.69668 | -55.43684 | 2025-01-22 05:37:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68906eae-0a2e-3846-856b-0727c9427abf | -20.69708 | -55.43217 | 2025-01-22 05:37:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 536497a7-fa92-3b3c-9412-c1e311d012fd | -20.69642 | -55.43049 | 2025-01-22 05:37:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36a04ffd-cced-3e52-8e59-24f3159ec08e | -20.69748 | -55.42744 | 2025-01-22 05:37:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a216abc-94f5-3897-83d0-a2bb54e1ab4d | -20.70205 | -55.4359 | 2025-01-22 05:37:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7d58425-38aa-34cc-a28a-a7e58a7200d6 | -15.83 | -43.46 | 2025-01-22 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7d65c2e-f76d-334a-af68-6c41fd2ad21e | -15.39 | -43.78 | 2025-01-22 12:00:00 | MSG-03 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |


