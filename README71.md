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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2849cfef-2796-3e3f-930a-fb5445af706e | -6.9699 | -59.0658 | 2026-08-23 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c58355c5-9ec7-3126-ae16-c86516addd88 | -16.0509 | -50.4363 | 2026-08-23 07:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e703f31a-2d4d-3bed-8e4f-e19d5c791243 | -6.1285 | -57.8393 | 2026-08-23 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5a52fddd-0220-30e8-b161-5bdccbcc9022 | -13.1697 | -51.4258 | 2026-08-23 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9d43347c-d4e3-3c8f-8ea6-d3f07fc7c993 | -6.6766 | -58.7299 | 2026-08-23 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 775a6d1a-ca03-3fda-acad-3ebc78296ca0 | -12.8554 | -48.4541 | 2026-08-23 07:20:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d8eec3b7-e821-36bf-9b52-6f4c684ccc13 | -6.695 | -58.7291 | 2026-08-23 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1d9ea821-1feb-3b14-9727-f4c195a3ae62 | -6.695 | -58.7291 | 2026-08-23 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8959fe1e-1d61-3592-8839-2bb847aeb5bd | -6.6766 | -58.7299 | 2026-08-23 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| bd84dbfc-356c-3ac4-9e67-d664d2850a63 | -6.9699 | -59.0658 | 2026-08-23 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bdbf0afa-8aa9-3739-9da9-e91597075e31 | -13.1505 | -51.4281 | 2026-08-23 07:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 43ccba93-b4a5-3383-8cea-0ae6939ab993 | -16.0509 | -50.4363 | 2026-08-23 07:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a14e9946-a94b-3c53-9180-43d855cbbce6 | -6.1285 | -57.8393 | 2026-08-23 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9fb41a88-87c1-36e6-b82e-2ccb7faf3f17 | -6.9514 | -59.0666 | 2026-08-23 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9a35b115-d1c5-3568-af76-d72bc2d772f0 | -16.0706 | -50.4332 | 2026-08-23 07:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3b479246-f431-3ec5-beb3-b665791a3946 | -6.8062 | -58.6469 | 2026-08-23 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5a370877-9c9d-3ff0-8239-c4d090d98113 | -6.6766 | -58.7299 | 2026-08-23 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 88f823a3-a860-3666-9396-2b0a98e2a7a5 | -13.1701 | -51.4044 | 2026-08-23 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 61f25a32-de1c-3e7e-8b16-c6fc484f94ab | -16.0509 | -50.4363 | 2026-08-23 07:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 9f288b81-86f0-3ac3-a66b-1e72548708a4 | -6.9514 | -59.0666 | 2026-08-23 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 5a1507d7-b923-36e8-b803-54739c6cad12 | -6.695 | -58.7291 | 2026-08-23 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a38927b1-6271-37e5-a479-165161621cc3 | -13.1697 | -51.4258 | 2026-08-23 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 979064a7-9964-37d9-ad42-29ed69b91dea | -10.4905 | -49.9604 | 2026-08-23 07:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0669d0f4-5232-319c-a86c-17f04ae784de | -10.4716 | -49.9624 | 2026-08-23 07:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 2884bc25-f8e1-3ccf-a0ce-271c7d4bdb38 | -6.1285 | -57.8393 | 2026-08-23 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 46668728-600c-3a8c-8fe0-50eb0c132690 | -6.6765 | -58.7492 | 2026-08-23 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 999de9e8-87e7-3989-9518-245d81666008 | -10.4713 | -49.9838 | 2026-08-23 07:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 54cca59c-817a-3656-9bc8-64796eb88ff7 | -6.9699 | -59.0658 | 2026-08-23 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e23cc595-444c-3b37-ae43-70eafabf95bf | -10.4902 | -49.9818 | 2026-08-23 07:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2c8f24f2-b7fd-3c41-9f6a-f8238f884f94 | -10.4905 | -49.9604 | 2026-08-23 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 27a683dd-0bd5-3d82-bb8e-4f556ed88d44 | -10.4902 | -49.9818 | 2026-08-23 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 41cf73e5-dba8-39b9-b3e7-c5b442691883 | -6.8062 | -58.6469 | 2026-08-23 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 64f01ad0-f3ad-32b9-8054-0748c5dde22f | -10.4713 | -49.9838 | 2026-08-23 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| df4fbeb5-c37f-34df-ba92-c83a021728b1 | -16.0509 | -50.4363 | 2026-08-23 07:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a8815ede-3052-313b-9db2-50deef70a276 | -10.4716 | -49.9624 | 2026-08-23 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 167.9 |
| d2ee3a4a-d4a1-3cf5-9405-485a956ed3fa | -6.9514 | -59.0666 | 2026-08-23 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 19bb035a-6cae-31d5-b9b6-b2141a9595d9 | -6.695 | -58.7291 | 2026-08-23 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 4d3d4b8f-e638-351b-b800-595a3795d273 | -6.6766 | -58.7299 | 2026-08-23 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 30d2819f-5762-32a6-aae7-b570539cf42e | -6.6765 | -58.7492 | 2026-08-23 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| eda4172f-2bae-3aec-af76-4afffa0c9542 | -6.9699 | -59.0658 | 2026-08-23 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 10cc2c53-7641-3b15-8d08-7cc3f97db22d | -6.6949 | -58.7485 | 2026-08-23 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 0a160fac-c1b3-37dd-9b4c-d42ff793192b | -6.9699 | -59.0658 | 2026-08-23 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 31ce89be-c7c7-3be9-9445-5080c353088e | -10.4716 | -49.9624 | 2026-08-23 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 35d53217-c2b9-377a-8a14-04a142f091d7 | -10.4905 | -49.9604 | 2026-08-23 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4928ab07-fa04-3400-a27c-ba1a26e3ab1f | -6.6765 | -58.7492 | 2026-08-23 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 98b37b06-e589-3d1d-bf60-38cf8899b075 | -6.8062 | -58.6469 | 2026-08-23 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 077bdfe4-aed4-38c5-a4cf-654bf8fc4c1c | -6.1285 | -57.8393 | 2026-08-23 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 539fc71a-5250-32cd-99e2-a6feb90e4a5d | -16.0509 | -50.4363 | 2026-08-23 08:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8f82303f-57b4-3f98-91d5-6ce07bacedce | -6.695 | -58.7291 | 2026-08-23 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 43698ffb-d8c1-3556-bb4b-4e2f46513be7 | -6.6766 | -58.7299 | 2026-08-23 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2709e0b9-cfe9-3c91-93a1-eb7ae5fd1600 | -10.4905 | -49.9604 | 2026-08-23 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 6f85198e-f095-3e73-864a-fb3959ada714 | -6.6766 | -58.7299 | 2026-08-23 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 798c1431-f800-3635-b835-67f9a8186ebd | -10.4902 | -49.9818 | 2026-08-23 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 87b99553-535b-3706-b557-920f60f54207 | -6.9699 | -59.0658 | 2026-08-23 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1d2ac391-0398-375b-9980-fb8b4d957ebf | -10.4716 | -49.9624 | 2026-08-23 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 14b060b3-95c0-35f9-bc68-788810826b3a | -16.0509 | -50.4363 | 2026-08-23 08:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3c28af04-8459-3691-aee1-abdd8d0da4a6 | -6.695 | -58.7291 | 2026-08-23 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ce29df8b-db9b-3f9e-8cd6-b1a70c6950da | -6.1285 | -57.8393 | 2026-08-23 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1398fea8-d217-3c68-bdfe-a80a0a028f60 | -10.4713 | -49.9838 | 2026-08-23 08:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 30063e20-acd9-33b6-a614-11619533eaf9 | -6.6765 | -58.7492 | 2026-08-23 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 05e27d62-44f3-3082-b5b5-3eb59dbc4f52 | -16.0509 | -50.4363 | 2026-08-23 08:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 7dd9d184-341d-3b6d-9214-ae218aa342ab | -6.8062 | -58.6469 | 2026-08-23 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d4620b08-c6a0-3520-b35f-939dacdfab8c | -6.9699 | -59.0658 | 2026-08-23 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ba671d69-bec2-3257-be61-33baa2ed7151 | -6.8188 | -59.6696 | 2026-08-23 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 0326cd68-cc8b-36bb-b949-d9d8674175c8 | -6.6765 | -58.7492 | 2026-08-23 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b2099328-ba91-375d-94e0-4022b49f1945 | -6.695 | -58.7291 | 2026-08-23 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 68dffcad-13a7-3d42-afbe-b8221f10a14c | -6.1285 | -57.8393 | 2026-08-23 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 00886e05-0630-3b3a-96a0-17caf0cb2087 | -6.6949 | -58.7485 | 2026-08-23 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 249bdb4a-e3bc-3aef-bab6-abfb5e16fd0c | -6.6766 | -58.7299 | 2026-08-23 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c03b87f4-7092-387a-b442-b4becba922a6 | -10.4905 | -49.9604 | 2026-08-23 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ce29ee24-3915-339f-bff9-9875d95ffefd | -6.9699 | -59.0658 | 2026-08-23 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c9935d6f-ae94-3999-87e9-a6c8c6c1f75e | -16.0509 | -50.4363 | 2026-08-23 08:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ee32e338-788e-308a-bcf5-70b54c011dbf | -6.6766 | -58.7299 | 2026-08-23 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 45bb697c-3ad5-315a-9b23-477330b183b3 | -16.0706 | -50.4332 | 2026-08-23 08:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1a0454c0-e0fa-3c84-b15c-2aeb6a4a05a4 | -6.6765 | -58.7492 | 2026-08-23 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 9f293dfa-9c73-30e1-9dd1-eec551c37525 | -6.695 | -58.7291 | 2026-08-23 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6f29b66d-f7ac-31bf-b2b0-b18c11440899 | -6.6765 | -58.7492 | 2026-08-23 08:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 0efc3296-e0d0-35e2-a2b9-66adbc78683f | -16.0509 | -50.4363 | 2026-08-23 08:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 67bd0269-b1ec-3cec-9c34-85a129beccc9 | -10.4716 | -49.9624 | 2026-08-23 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 72dc3edf-9a94-367d-b4f2-179f28cf08ac | -10.4905 | -49.9604 | 2026-08-23 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 88e4515b-02f4-3e92-b8fc-3acdf22b6d44 | -6.695 | -58.7291 | 2026-08-23 08:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a81deba4-97e5-3338-a983-2bf3b6c6b8f0 | -10.4902 | -49.9818 | 2026-08-23 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| cd9c0995-0cfe-3d94-ad8b-d8d4b58c9697 | -10.4713 | -49.9838 | 2026-08-23 08:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 0dc0807f-c20b-318c-9446-5c0917be5095 | -6.6766 | -58.7299 | 2026-08-23 08:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8907e51e-0646-3f32-8f3a-2dee0d3881f5 | -6.9699 | -59.0658 | 2026-08-23 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3c1db49e-d202-3d5b-b26f-4b26f3cec671 | -6.6766 | -58.7299 | 2026-08-23 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7c241c33-4502-3cc9-9b0c-9b41a09a7d1c | -16.0509 | -50.4363 | 2026-08-23 08:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 7a1db5ae-07ca-396e-9567-6905faadfca0 | -10.8172 | -50.9711 | 2026-08-23 08:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| dbf8755e-0e05-3de0-9683-b942002d1e97 | -10.8358 | -50.9903 | 2026-08-23 08:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 71f6fa87-cc29-3ed3-8e8a-b7b916f4d9f5 | -10.4902 | -49.9818 | 2026-08-23 08:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ed0ee7f7-c0a2-3e64-88c4-961ccd5fd91a | -10.4905 | -49.9604 | 2026-08-23 08:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 9c5312e6-d03c-3bab-b135-4d0ea8d461d8 | -6.695 | -58.7291 | 2026-08-23 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 182ab98e-257f-32dd-ac46-2c1a3cdb5235 | -6.9699 | -59.0658 | 2026-08-23 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0a01e152-5e64-3049-b64c-e2b69896ff4d | -10.855 | -50.9671 | 2026-08-23 08:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7e9d59e7-0025-3044-b698-09349df22354 | -10.8547 | -50.9884 | 2026-08-23 08:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 21c9a162-7b8d-3bc1-8d8d-a50eda38f8b7 | -10.4716 | -49.9624 | 2026-08-23 08:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| bb4a0897-0978-3f70-a7f0-81d25b97065e | -10.8361 | -50.9691 | 2026-08-23 08:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 11778e36-25b9-32d9-8f44-57a4297427fa | -6.6765 | -58.7492 | 2026-08-23 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a78d9e7e-4b72-35d8-8eee-586176e65298 | -6.6765 | -58.7492 | 2026-08-23 09:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f93c8ca6-ac2e-371f-b2f1-a6ce4d65842a | -6.9699 | -59.0658 | 2026-08-23 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |


[Clique aqui para ver as próximas entradas](README72.md)
