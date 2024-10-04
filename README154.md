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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13420752-776c-3260-95a5-5ee29aee0168 | -14.52717 | -49.28937 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f4b5464-2bd3-3d69-85b0-73d5998fb564 | -14.52329 | -49.28422 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b22657d-ad77-3c1e-83e4-2756ca311dcb | -14.51485 | -49.27903 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88fe04eb-b672-36fe-bfbb-05ed276d0fcd | -14.51083 | -49.31058 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9fdb7d4-7775-323e-9700-1ba7ea738d02 | -14.51038 | -49.27843 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fce4197a-441f-304f-b238-00be1f7d5a7f | -14.50978 | -49.28313 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b3b87dd-8a8d-3e46-8171-a744eecca114 | -14.50537 | -49.28209 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee7977c1-3a8c-347c-90bf-0b5b74a454bc | -14.50475 | -49.28701 | 2024-10-04 04:57:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 603fef70-3264-3941-926a-702ce7b778a8 | -14.81281 | -48.80322 | 2024-10-04 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6881eb22-4947-3bb1-a93d-a561a412c903 | -14.80765 | -48.80675 | 2024-10-04 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bea4fa9b-e5c6-374d-875f-3c1485668138 | -14.80306 | -48.80576 | 2024-10-04 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6c4b909-15d7-3aae-8702-9dd558b7a839 | -14.79787 | -48.80962 | 2024-10-04 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df6ffa2e-3bd9-321e-a48f-bfc581391615 | -14.70334 | -48.785 | 2024-10-04 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d671d664-2ab1-30ed-ba28-7dbcfbdd0cc6 | -14.62887 | -48.71211 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7617b192-ca74-3270-bd93-e11f3ef26c6c | -13.72701 | -49.42222 | 2024-10-04 04:57:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a88bd2e-8fdc-3a71-b24e-bc9591046ea8 | -16.09111 | -50.25623 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8df5a075-6784-3d0d-b8b1-c713d0739ef2 | -16.09059 | -50.26038 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2299585-de26-3734-8c1f-df32a0ab3243 | -16.08953 | -50.26874 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f3fa608-ba6f-3d28-8bb2-bb673d263fdc | -16.08533 | -50.26753 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b79bae77-2654-3881-a041-9b2bbadcb9b8 | -16.0843 | -50.27575 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a296cf16-8618-36c2-9c96-3d0bff3212b8 | -16.08377 | -50.2799 | 2024-10-04 04:57:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e3b8da2-dce9-3332-9f9d-151832f7a54a | -10.49568 | -50.25552 | 2024-10-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3d3bf85-43b6-317e-bd57-d531402a7643 | -10.49496 | -50.26067 | 2024-10-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54b512d8-f6c9-3c0b-8581-5e7c48828f8c | -11.97885 | -50.18148 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f24f461e-58d9-308d-8dcf-92ad24f33b01 | -11.97479 | -50.1809 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fbfeea3-77d6-3d42-8dba-5f9b1ad4f6b8 | -11.96211 | -50.15305 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c712a8d-fafe-3485-b166-1d3af4b15bc1 | -11.9616 | -50.1567 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1ca54dd-5982-3390-bdd8-a1a04225732f | -11.9382 | -50.14595 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e48741ba-e293-37a4-810f-cd2b298318e5 | -11.93769 | -50.14961 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8878e95-5c0d-341a-8cab-f03e4f806718 | -11.91378 | -50.14244 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3860401b-fb15-3871-a362-1aabf6ec908d | -11.91021 | -50.1382 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e1775a4-c556-3502-be01-12a764bbb67c | -11.90971 | -50.14185 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7024d738-c5bd-3a26-a78e-41a06ef43071 | -11.90564 | -50.14126 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 948b2195-ec98-38a4-b069-0b1f3d5637ca | -11.74536 | -50.01098 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10766fb9-803c-327b-88ea-ce880b9dc898 | -11.74178 | -50.00669 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f0cc7a2-3cb6-36cf-9746-bd832d704937 | -11.3633 | -50.54204 | 2024-10-04 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 310add56-bf29-33e3-b184-6af50d2176c9 | -10.93832 | -50.17678 | 2024-10-04 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f68f8655-d96b-340c-9943-9d4db6e5ba6b | -10.87166 | -50.11691 | 2024-10-04 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74aaa4f2-9827-31b8-8be4-95bfad8ce2e9 | -11.09762 | -49.6191 | 2024-10-04 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5133e694-c6d5-3a7d-aabb-ed2c6f7493f2 | -11.08445 | -49.60965 | 2024-10-04 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac760bc3-c44f-34ac-a0af-13259ff27cbb | -11.08391 | -49.6135 | 2024-10-04 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8dee3a-384d-3a4f-a57e-0bdd3318668c | -11.08029 | -49.60905 | 2024-10-04 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83c32cff-56f0-34fa-8555-77e97c07dd79 | -13.0057 | -51.11925 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 095283d8-4c90-3870-ba5a-309328483b04 | -13.00182 | -51.11869 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| daaccb46-97a9-3052-8dbd-cd1652546168 | -12.98102 | -51.12583 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3c3148d-2939-3b9a-92ab-6bc8c41456f9 | -12.97713 | -51.12527 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38d93985-47e8-37a6-ae35-11f339f85152 | -12.78584 | -50.58089 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69d9d099-7484-3a95-a8dc-fa69eba0ee93 | -12.78183 | -50.58033 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20c90f05-78ec-3078-a80e-4ebcb2b5aee1 | -13.63009 | -51.20147 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 203b8cf3-3acf-3244-8ad0-ea78d4c6712e | -13.62689 | -51.19589 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea30ad26-ee92-3614-b33f-7f464cef48a4 | -13.6262 | -51.20092 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10aed481-3519-3ed8-9d89-e723735d69b9 | -13.62438 | -51.18527 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42c469da-9056-3048-8c0f-84efb9ea8136 | -13.62411 | -51.21595 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2a0aa69-9119-324e-9993-3c4e6b261f81 | -13.62369 | -51.1903 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ddc1f908-ecc2-37a0-90f1-0bbb1d973385 | -13.62299 | -51.19532 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3707b0bb-4142-3f3c-ac09-738f51844dfc | -13.6223 | -51.20034 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d0a9a38-3957-3959-973e-e75142983455 | -13.62161 | -51.20536 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20c04618-ca90-3d20-9bbf-64ad5e2ae44e | -13.62091 | -51.21037 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f4b66ca-3e3c-330b-bdb2-5b7b5864868c | -13.62048 | -51.1847 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60dd06fc-7c73-307a-ae19-19c49866582c | -13.62022 | -51.21537 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fed5ddac-b9b4-32ef-8dfb-bafde051299c | -13.61979 | -51.18974 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66723ede-664f-3d6b-af8c-b26af59fcd0d | -13.61909 | -51.19476 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 42a3f881-74b0-35a4-8f1d-53554e6fa49d | -13.6184 | -51.19978 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e201f75-3629-3c8d-87d3-f81df5b97c30 | -13.61771 | -51.2048 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 624f4ec4-0f3c-3a0b-8c29-a97f9b8b5163 | -13.61702 | -51.20981 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09c50529-51a8-3fea-946e-d7537cd6ed73 | -13.61633 | -51.21481 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97d70e8b-5b63-3811-87c6-60fa0106220b | -13.61564 | -51.21981 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f2e6e94-9487-3f96-9575-423c4e2fa6ea | -13.6145 | -51.19922 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 170cb847-b10c-3125-8657-0fc124335bb9 | -13.61381 | -51.20424 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf2729cd-cdf4-3dad-a698-99ec380a2f0b | -13.61312 | -51.20925 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30a0994a-44dc-307a-8ce1-de0d1acc691a | -13.61243 | -51.21425 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5134b182-8143-3869-86e1-32bfd087c6cb | -13.60923 | -51.20868 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6bc857d-f4da-3bc3-8050-6c424a0ed3a2 | -13.60854 | -51.21368 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a10f8c2c-74a3-32eb-ae29-6bb7642ca9d6 | -13.60717 | -51.22369 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adbbbd75-09b2-3706-a165-201dc9201074 | -13.5713 | -51.2541 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00b07514-84a7-350a-984e-9c658e6c2898 | -13.57066 | -51.25199 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb4be229-79da-326a-b402-b0a3871617f1 | -13.5681 | -51.24855 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8a0e5db-99b7-3084-a493-8acba0441ea0 | -13.56749 | -51.24646 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa6f7e0b-65b0-312b-b0a2-7024dfd32b02 | -13.56678 | -51.25143 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8444f8d-d3d7-3224-9a96-27e390d6823a | -13.56421 | -51.24799 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b2dea6e-9426-3f80-b2b3-c2c36c9eded1 | -13.5636 | -51.2459 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e2a663a-c9fb-3b6b-87eb-22bb8d56d60e | -13.20482 | -51.18293 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a3713be-072b-3bfd-9aa7-2ba351e4c978 | -13.14238 | -51.19709 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6570fbc-c495-3d1e-9072-c28b4ba9b8f9 | -13.12759 | -51.18991 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc8aba51-5693-33e0-bd83-c04ca98df256 | -13.11699 | -51.15299 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8d188cb8-eba2-3581-9efd-222ef016f950 | -13.11629 | -51.15795 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 42c98f70-0459-3ac8-8baa-8a354b249ab9 | -13.11559 | -51.16291 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae780cd3-f201-34fb-923f-09f13398e9ce | -13.1138 | -51.14746 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cc89995e-fcee-3e17-ba73-5d5fdafe6972 | -13.1131 | -51.15243 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 442beb74-d8ff-319c-a2bd-01568777d73f | -13.11241 | -51.15739 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eede44a-ca11-3cfc-bb6e-3cecf7fcebe1 | -13.11171 | -51.16235 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97ce85de-e6fc-3a45-ac9a-71caf29e383c | -13.11101 | -51.1673 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb002103-f79d-3566-b113-afc8e70b40f9 | -13.11032 | -51.17226 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4270a3a4-dfd1-39d6-aae5-0595fd8ae144 | -13.10992 | -51.1469 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7b6f203-fccc-3599-9a40-c0eeaeec5006 | -13.10922 | -51.15186 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ce8dc26-5f8a-3ede-9668-5369fc80320f | -13.10853 | -51.15683 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bb5674f-aa93-34b2-ae51-a4e1e4e64c55 | -13.10644 | -51.17169 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54c64ab8-b7c9-3ac6-a2f8-a8adffaf74c7 | -13.10395 | -51.16122 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71f33abc-bd1a-35ce-a7db-2ea63ce95a09 | -13.08732 | -51.13855 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 353a069c-f968-36b3-ac23-605cf61fa0a3 | -13.08662 | -51.14353 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |


[Clique aqui para ver as próximas entradas](README155.md)
