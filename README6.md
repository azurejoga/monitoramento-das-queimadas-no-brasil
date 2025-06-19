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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e20d95cd-174e-3da5-84a1-e9f066939cb9 | -16.3047 | -58.2676 | 2025-06-19 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| b1736373-b5b9-3c36-aa77-7f33d528cbbe | -11.952 | -58.7376 | 2025-06-19 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 37f0ba7f-9526-336e-a33b-7d6f7590ce84 | -8.07 | -43.1216 | 2025-06-19 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 653a95bc-c6a4-3c58-900c-873c966ddee3 | -7.2408 | -43.0664 | 2025-06-19 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 5ecb9541-8b61-3cd3-8255-d4d94efc8b7b | -11.9707 | -58.756 | 2025-06-19 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3ad0fbfb-2364-3871-90f7-27c37a2e8b05 | -16.305 | -58.2474 | 2025-06-19 02:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| b0a1c116-56a0-3dd0-a0bb-4e000ef0416d | -11.9518 | -58.7574 | 2025-06-19 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 570d1fc9-fa16-30ca-91ef-c29d8b13b699 | -11.9709 | -58.7362 | 2025-06-19 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 745779a1-44c5-3b44-8780-b3dcaaf29ed7 | -11.9518 | -58.7574 | 2025-06-19 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 47f2a48a-d315-3f3c-90cc-884281526a09 | -16.3047 | -58.2676 | 2025-06-19 02:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| d973740a-e3d5-3953-b061-6a5e7cfc8d86 | -8.0703 | -43.0981 | 2025-06-19 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 6d621950-074c-320d-aac1-9ea5aadf328e | -11.952 | -58.7376 | 2025-06-19 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| f09704d9-92bd-385f-b8b2-3b226d60dbe7 | -14.4467 | -48.9063 | 2025-06-19 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c774b4fa-50fb-3f23-8733-524c651d10d5 | -8.07 | -43.1216 | 2025-06-19 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 00d43f35-787f-3dfc-8e50-cb6493190dca | -7.2405 | -43.0899 | 2025-06-19 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 153.7 |
| c4c3cb17-0230-3c9e-b1ca-af9e706f83eb | -7.2408 | -43.0664 | 2025-06-19 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 0d58c8b4-f0b0-3e43-b04c-02ea15113a71 | -11.9707 | -58.756 | 2025-06-19 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2313ae66-0bcd-394c-83b8-0ecef7e836a3 | -7.2408 | -43.0664 | 2025-06-19 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 8c569967-9820-3d4f-add6-2c8cde3f6d41 | -11.9518 | -58.7574 | 2025-06-19 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 73536e88-b176-3123-93ce-9bff54718faa | -11.9707 | -58.756 | 2025-06-19 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d83fa2eb-0c17-36ee-a937-7a22d392873f | -8.07 | -43.1216 | 2025-06-19 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 4f9578cd-ac39-3252-8e69-607a4230f7d6 | -8.0703 | -43.0981 | 2025-06-19 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 224883f1-2448-34fa-bd48-1294193c15d9 | -14.4467 | -48.9063 | 2025-06-19 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 475b81a8-34a1-386b-8a29-a74a3a42e749 | -11.9709 | -58.7362 | 2025-06-19 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b0ea84a3-3970-3147-9564-3158ecd73e9b | -16.3047 | -58.2676 | 2025-06-19 02:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 6d949870-c195-3682-86eb-c7b7d04bd09b | -7.2405 | -43.0899 | 2025-06-19 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.8 |
| 3d17981d-117a-3bcc-9c68-d80dd2e5a2e8 | -11.952 | -58.7376 | 2025-06-19 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 9498c617-4afc-3c3b-845b-0f7dcf837d19 | -11.952 | -58.7376 | 2025-06-19 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| bee532e6-b66d-3f50-b52b-3d630cf2a2ad | -8.07 | -43.1216 | 2025-06-19 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 8fb2af06-eb1f-3563-beb4-dd2d82eb1d6b | -11.9709 | -58.7362 | 2025-06-19 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4e380546-8ef4-3acd-9b22-9b9c4b6a3d4b | -7.2408 | -43.0664 | 2025-06-19 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| bb357e63-4b63-3d35-a241-4cd99374ff71 | -8.0703 | -43.0981 | 2025-06-19 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 7e5919a5-2684-3fb0-b48b-367ee2d5001d | -11.9707 | -58.756 | 2025-06-19 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| d94e1b97-f815-316b-a13e-3473f2ecaf3a | -7.2405 | -43.0899 | 2025-06-19 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 654aed82-556f-33f3-8f7b-775b0bc61039 | -14.4467 | -48.9063 | 2025-06-19 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b0a41270-8c1d-36a9-af40-56e1f5d69356 | -11.9518 | -58.7574 | 2025-06-19 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 95ac503e-b90c-392f-bd4b-33e92f9089e9 | -11.952 | -58.7376 | 2025-06-19 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| c81cd714-c169-3a84-8a07-47c1f4d384e8 | -7.2408 | -43.0664 | 2025-06-19 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 3d08a27b-9f95-37d1-a487-33f7df2f2bbf | -7.2405 | -43.0899 | 2025-06-19 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| c9646431-82bc-3ddf-9afc-183b0808701b | -8.07 | -43.1216 | 2025-06-19 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 462d55c5-7218-3a37-ad2b-991f75e96cff | -16.3047 | -58.2676 | 2025-06-19 03:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| a6f0f1a2-b1ab-34cd-95ec-8e91cf18f570 | -11.9707 | -58.756 | 2025-06-19 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1764531e-82df-34fc-97d4-4057f971f283 | -11.9709 | -58.7362 | 2025-06-19 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 3813ef70-305d-3292-9df0-da7bf97a30fd | -11.9518 | -58.7574 | 2025-06-19 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| b5da55ec-328f-33d2-8dfd-817102c0ddfd | -8.0703 | -43.0981 | 2025-06-19 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 5c767a75-b03f-3f90-9962-2568d674b37b | -8.0703 | -43.0981 | 2025-06-19 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 12fee314-b5a2-3a48-a51e-bcf4d277afec | -7.2405 | -43.0899 | 2025-06-19 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| b1527390-784a-3283-bd5e-828514d8cb38 | -7.2408 | -43.0664 | 2025-06-19 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 6915fd8b-4521-3836-9253-3e983e516475 | -11.952 | -58.7376 | 2025-06-19 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 1e8ad5d3-19ee-3fd7-9b24-7759b8455e05 | -14.4467 | -48.9063 | 2025-06-19 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b97aaed4-2aae-3c04-a48b-8258565677c3 | -11.9707 | -58.756 | 2025-06-19 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| dbf6310c-ee2b-3730-9140-7966f325828d | -11.9709 | -58.7362 | 2025-06-19 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 00a102de-4bfd-3f4f-a286-ceca2694bb31 | -8.07 | -43.1216 | 2025-06-19 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 357aa724-c94f-39a3-8ce6-d06040cdcd23 | -11.9518 | -58.7574 | 2025-06-19 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 92b40434-8d24-391e-800f-32ce356a4fdb | -11.952 | -58.7376 | 2025-06-19 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 88342f36-115b-32d2-9a25-d5d6ae2c2e14 | -7.2408 | -43.0664 | 2025-06-19 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 80c4757a-76cd-3129-baf5-88392529edad | -11.9707 | -58.756 | 2025-06-19 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d3cd3ead-5041-39d3-99ef-25ba35481499 | -11.9518 | -58.7574 | 2025-06-19 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 04466488-d8c2-3e68-95ca-5cc7531b75d2 | -8.0703 | -43.0981 | 2025-06-19 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 670df5c4-fd1b-39fb-9e3b-8a5beaf2d9c1 | -7.2405 | -43.0899 | 2025-06-19 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 3a280dc5-937f-312c-867d-11b9d4f824c1 | -14.4467 | -48.9063 | 2025-06-19 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| e6128418-f0e4-31fb-b5bc-69dd4a30fe88 | -11.9709 | -58.7362 | 2025-06-19 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0d9d6e5f-e7cd-3af7-b540-b36e8c1b1de2 | -3.77838 | -41.66594 | 2025-06-19 03:28:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44309f9e-0b83-3b30-bad8-239c60f28723 | -3.08291 | -40.07818 | 2025-06-19 03:28:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ad21f8a-05c1-351b-a985-155fbac7b2a4 | -3.0824 | -40.08131 | 2025-06-19 03:28:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f830fd72-0838-372d-bfb6-659f2d29df2b | -7.2405 | -43.0899 | 2025-06-19 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 93362c6a-2dec-3f6f-9ce4-eb75d3b5e820 | -8.07 | -43.1216 | 2025-06-19 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.5 |
| d7aac5fc-4f26-3dd7-a402-f07433c36c8b | -11.952 | -58.7376 | 2025-06-19 03:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 2ff3e6b6-8f15-3e84-9c3a-8a932244cdb5 | -8.0703 | -43.0981 | 2025-06-19 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| ef3ec472-e3e1-3207-9596-40fef020ce21 | -11.9518 | -58.7574 | 2025-06-19 03:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 4fc73b02-7c3e-3991-96d6-eedb501e4231 | -11.9709 | -58.7362 | 2025-06-19 03:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| d4cd883b-4d46-3000-bce5-b5b6f965e65a | -11.9707 | -58.756 | 2025-06-19 03:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| fd463a44-1ac5-3707-a281-cd5146f0d873 | -16.3047 | -58.2676 | 2025-06-19 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| d656fcfa-fb21-311e-b29b-a76f3f5b1605 | -6.66304 | -42.48611 | 2025-06-19 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50d21581-bd34-3180-a050-f47975bdb83b | -6.71064 | -43.25579 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 82ca4349-7880-3987-8bec-44843c65e196 | -4.83981 | -43.18559 | 2025-06-19 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19f650b2-3de1-365a-96b2-010255a3da3f | -6.28503 | -44.23491 | 2025-06-19 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 979a39c8-35c5-38d5-892c-5eb72c6d0de7 | -7.21679 | -34.95819 | 2025-06-19 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 43e360ca-5ce6-3887-b1e3-c3bd57280219 | -6.68952 | -43.20184 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 915e3a51-f814-35e8-9005-a218a28455c8 | -4.8399 | -43.18283 | 2025-06-19 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bea60ba-f166-3ea1-9ed3-3941640c4162 | -5.84586 | -43.49136 | 2025-06-19 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6dd857c-6913-30e0-88e7-f958f7776499 | -6.24774 | -44.65774 | 2025-06-19 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fa36367-e3c3-33df-8810-0ccf0bdba05f | -8.07219 | -43.1075 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 1bcfc4ac-d464-36b5-9b62-5d8e6d5e3e5c | -7.23428 | -43.0775 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| f31bab34-2db1-3152-8371-a8dc55586698 | -7.24413 | -43.08176 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 430d0758-89fb-3721-bf21-276614e0f531 | -5.13609 | -37.84511 | 2025-06-19 03:30:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0843fd43-d07c-3692-8f9e-a430954801df | -4.84599 | -43.18651 | 2025-06-19 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbdf3c51-3e61-3f48-ab7d-f57be7fe9df4 | -7.24175 | -43.09471 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bc0130ee-ba01-3322-9e6c-5a460695171d | -5.91022 | -43.45215 | 2025-06-19 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33efd98e-33e0-31a9-864d-15df1266b73a | -6.66711 | -42.4731 | 2025-06-19 03:30:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bb6db34e-5dd4-3fda-ab77-9446400c8558 | -7.24254 | -43.09044 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| fb389d36-7225-32fc-b410-ff9fa8a55ac7 | -5.13541 | -37.84918 | 2025-06-19 03:30:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| afa5017f-665d-3ee8-b8ca-493beb3108dd | -8.07798 | -43.10864 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| f6c6afd1-f87d-33c7-8505-b31f7f81fef4 | -6.6705 | -42.48676 | 2025-06-19 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 564badbe-22bb-3c47-9e2e-32aeb8903347 | -5.90934 | -43.45707 | 2025-06-19 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88a94abc-83ef-3237-b77d-819e3b705b87 | -7.54062 | -43.8054 | 2025-06-19 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 021d319e-724a-372f-932b-22a1295a0707 | -6.687 | -43.21561 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6f0b1d6b-34b9-3019-b9de-eb78bb437853 | -7.23352 | -43.10633 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 62b257d2-a991-3a02-a669-8877199a8343 | -6.68784 | -43.21103 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b4f0a82b-fcbf-3433-911b-c5d95adb5da9 | -7.23351 | -43.08183 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |


[Clique aqui para ver as próximas entradas](README7.md)
