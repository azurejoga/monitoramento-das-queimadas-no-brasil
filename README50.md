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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73b70958-6af7-3053-bf58-f0b4b36bf284 | 1.90945 | -55.76691 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6820fd7-d119-33d6-bd30-29ea5022d7c1 | 2.09852 | -50.73634 | 2026-10-04 05:14:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f345e49-b31d-38ff-b44c-805872459e72 | 2.87518 | -60.54264 | 2026-10-04 05:14:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1f38433-2840-392b-8006-bf001f4fd6cb | 3.4224 | -51.3037 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99de278d-0278-35a6-9b59-87f70cc02c7b | 1.81203 | -55.56114 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67aab93e-2929-32e6-a7f5-414163408209 | 1.88625 | -55.81268 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bcca222-3d59-306a-b956-b361242ca9ed | 3.64438 | -60.76124 | 2026-10-04 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a31ef03-19ab-3310-8be8-761c243533f6 | 1.83837 | -55.55308 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c03fe206-f807-3014-aec1-863007444405 | 3.3594 | -51.34456 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab27a187-99dc-3bc6-ba1a-2ade5a1d1845 | 1.84004 | -55.54227 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67807930-865a-3d7a-94e1-13f4e8fbc37a | 3.7845 | -60.97458 | 2026-10-04 05:14:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f5365d0-bc55-3f67-8d07-dadfa4bfb95c | 2.09397 | -50.73352 | 2026-10-04 05:14:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5d96340-fdc2-3c23-9f55-e8feeb1bd6ad | 2.35107 | -50.75531 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cce77393-91e2-361a-9601-b9c6dce6e498 | 3.42676 | -51.30538 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f8040c0-4c01-3bae-b1be-9310ddfbe160 | 1.9105 | -55.79483 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 987f5cc3-beab-340d-97b1-203f508a9e27 | 1.89231 | -55.80822 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99789c2a-9a63-38d2-b318-3bf42f32084c | 1.90059 | -55.79638 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde43c24-11d8-359a-8c48-5e007df1563e | 3.36016 | -51.34915 | 2026-10-04 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5369e626-3854-366d-b8b3-54309401922d | 1.83674 | -55.54279 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92dd7bc9-9614-3b9f-b110-4b1a3f76884a | 2.00156 | -50.93316 | 2026-10-04 05:14:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1d1513a-5907-3d14-8f7e-bbca4259fa6f | 2.87168 | -60.54683 | 2026-10-04 05:14:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875cefb0-80a9-37b1-9bb8-72e81519c617 | 2.09907 | -50.7398 | 2026-10-04 05:14:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bd84b6d-d86b-31c4-8a8e-5382cd632266 | 1.83507 | -55.55359 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d50a8bf2-0f62-36fb-8a05-bda0fd068329 | 2.87222 | -60.55039 | 2026-10-04 05:14:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f6c9bad-e2e1-3324-a686-52b2f08a88c8 | 1.89177 | -55.80478 | 2026-10-04 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1974d23-5fe6-3700-b59a-b8ef0157f108 | 2.36011 | -50.76088 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35956f48-4a42-3c20-b0f5-36fd329d12b4 | 4.05594 | -60.29072 | 2026-10-04 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7266534-2efd-3d3c-91de-0a07d516255b | 2.3471 | -50.75595 | 2026-10-04 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abdcffe9-45c8-3dc6-bd2a-ce37682b3afa | -4.28 | -50.32 | 2026-10-04 05:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eb87104-3090-3602-a8a6-b2bffe089e95 | -4.28 | -50.26 | 2026-10-04 05:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b591f02-13fd-3d7c-88c1-2f2c7388e629 | -3.76319 | -49.56173 | 2026-10-04 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 62dc7ff4-1348-333f-9a49-01c91ecff562 | -3.58448 | -55.55226 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dca531be-c07e-38b3-a836-c7e7783e1e75 | -3.12118 | -53.73473 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 016adaa3-6cac-3a00-bb80-df66d72f60ef | -2.79962 | -54.09914 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7038821a-33e0-3f1a-963f-ca5de0e3600b | -3.11141 | -53.75006 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 99d55ec2-8c3c-3243-83a7-ff208442b242 | -2.58001 | -51.88402 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 757b4092-f552-3497-b41a-2798af0d6911 | -3.157 | -53.07035 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da855cc4-6493-32f1-97e0-44e70760a12e | -3.47437 | -50.09663 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b82e4ce-b452-36ae-a4b5-0f6d4cae1d62 | -1.08859 | -54.11124 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9a35acd-9707-32a5-919b-11bdf0551386 | -3.58706 | -54.52823 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7560705-b2b2-3148-9efe-f38bd1556cb0 | -4.28179 | -50.27276 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 7d05979e-d1ee-3454-a8bd-89d217cd9c9c | -1.73562 | -56.07356 | 2026-10-04 05:16:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 557fe968-38fa-31bb-a42a-7a90de4f5d56 | -4.96621 | -47.97523 | 2026-10-04 05:16:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 346c7b8b-7c9d-385b-872b-5f5cad17cb16 | 1.76123 | -55.64639 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 542fc0dc-6bd1-391c-a698-5800c6b1ed79 | -6.20458 | -52.8042 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f389866-0a36-38c1-b0f5-de52bbf9048b | -2.88574 | -54.12695 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 958361b8-cdac-33b6-8ac7-ab1fb6b61b4a | -2.75509 | -51.55505 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef54a1e6-6d76-3a28-a2a4-7d9f8e97b7aa | -1.76805 | -55.027 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 747df7d2-1114-39f2-b6ef-b3040aa5cf9b | -3.13001 | -53.74871 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba1aa828-812b-3d01-aba4-f16ee69b3edd | -1.37359 | -54.63786 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76529693-f67b-34f4-931c-c09567ba62c5 | -3.49091 | -58.53699 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 279410a7-37d7-3b37-95a4-9e0aacf51c9f | -2.25295 | -51.9265 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b880bc51-2c2a-3122-8329-83ca8951123d | -2.58118 | -51.87634 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 60f5dc4d-bcbf-35a7-b40a-77fc5cbb6a77 | -3.11104 | -53.72895 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 35608fb3-f216-3fcb-9c98-253a2f672367 | -3.5321 | -59.40032 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8aa903b5-3cfe-3ad8-b2ac-d8c7a8a2d31b | -5.37532 | -56.06519 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 024bcc79-c6af-3ba8-a26b-9dba7e3cba00 | -3.70166 | -50.65688 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9c6b3110-354d-37f5-90ae-bc73869b91a9 | -1.05524 | -53.59003 | 2026-10-04 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8a95674-fae8-3a96-a304-8fd7689a6d87 | -3.71277 | -53.39833 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21ab4daa-4818-341f-83b6-864cb226fe4d | -4.11422 | -54.41559 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b5658e0-cfb0-3614-8ce0-43e3bb69411e | -4.43294 | -55.23939 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4832459f-b5a3-370e-b5a2-23df1c6024d3 | -3.04436 | -54.19906 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f83ef2fd-f4ac-3a73-9e97-444aa254a21f | -2.6966 | -49.03718 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fb235357-b700-32c0-91a2-034001291a1e | -2.97808 | -54.09216 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8df2150d-1e26-3e09-9f11-c104846f100f | -2.81493 | -54.09346 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7924ac3-14d0-3176-962c-cafc73f58cec | -2.25123 | -51.88487 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de884bd3-fa15-3879-9b46-614b541397de | -3.61538 | -55.50949 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7cff1da-db25-30c7-9e28-49e8377a226b | -4.2825 | -50.26811 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a50febeb-a11b-3120-9614-b5d3eca79733 | -2.78845 | -54.10142 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f2a5510-5f22-302b-b42d-dad3e714d774 | -2.81996 | -54.1304 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9e6c8b7-33e8-39a4-9fd5-0fe396926a62 | -3.32033 | -54.17047 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3b6e434-a4cb-3fee-bf69-4868cc4ce939 | -4.39079 | -45.99341 | 2026-10-04 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20ae397b-94fc-3975-af0e-207af2798bbc | -3.17092 | -54.08439 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 037f29ea-5031-3d40-b794-cb014676aa7c | -1.8068 | -53.76022 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d00bf746-1570-3cf4-8045-10c53e81233d | -2.15462 | -59.22683 | 2026-10-04 05:16:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 537cb95a-b73a-33e0-94c0-43b7c23fb56e | -3.11952 | -53.72184 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 9c720e15-8296-39d4-b60d-fd547710d272 | -3.71417 | -50.6631 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41c1647a-e8d8-396f-a5f2-7166d927f984 | -3.06656 | -49.53681 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce8ef9d8-dfc0-3784-b3bd-5ebe5f3f7a38 | -2.15966 | -58.11085 | 2026-10-04 05:16:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89092ce9-3867-3f25-929c-f92cef35a2d6 | -3.16739 | -54.08384 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 745bc830-354b-3b69-a9ea-d2215cd76ab7 | 1.79221 | -55.56424 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d3e29b96-f788-35b9-8cf9-c728c6abbc46 | -3.05696 | -54.16486 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6bb29bd1-b0a7-3877-8f71-ef9e954dd4a9 | -6.0661 | -53.47864 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d80649ee-271a-329a-97e3-9a76690327df | -2.06663 | -56.85812 | 2026-10-04 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3301f283-087f-32eb-8a42-6a45c5b19475 | -1.49513 | -49.45338 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71741437-0c94-3dbf-a295-a3aa7152998f | -3.8543 | -55.9746 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c27d7ce9-4f13-3f01-ab89-3586310bfb2b | -2.96112 | -54.10629 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4346ade-1fce-34f8-8088-4d5f39b3b2a3 | -1.21274 | -55.85732 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 053d42a3-33c5-3c8a-bc56-fc9ba90367ee | -3.52565 | -54.6131 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74ed2f4a-5530-3507-acd8-3d5a362eb662 | -2.77194 | -57.70154 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec2bc60d-d7ab-3e96-b5a0-e90cff64fafe | -3.94293 | -55.84039 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7479bb2d-6ad0-3e31-808c-448436efb476 | -3.08812 | -59.18962 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b297575b-cfa4-31f0-bffe-508276560505 | -3.08217 | -49.52899 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e6210ec-3c4b-339b-8e41-271c774041f2 | -3.11233 | -53.72073 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 262b582e-24b1-383d-b772-bca4dc4b1a01 | -2.58275 | -51.86605 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79d44378-b68e-3174-ad95-c6a887bf598b | -4.20701 | -53.46493 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62f75ded-39dc-399a-bc56-fbdf26547359 | -2.95821 | -54.10183 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 202f4b4b-dfec-300e-a8ba-6a0076e59bb3 | -3.18674 | -54.09889 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 258cc2c6-8e2c-3ceb-b497-40bbf4cf6ff5 | -1.19976 | -54.13956 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fc9bba0-c727-3cc2-b2e0-2dd76bc8380e | -3.20183 | -50.75034 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README51.md)
