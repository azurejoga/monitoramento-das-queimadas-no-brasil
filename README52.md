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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddddc4ce-a322-3a03-9d29-bbd1df968cf3 | -2.33385 | -50.58827 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15364005-3e10-3a11-90f4-b5bd3ef360db | -2.33054 | -50.58776 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa1f1794-c239-3c57-b466-32bd31214aa1 | -2.32944 | -50.44325 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8229efbf-dbac-37bb-b1ab-b584768e3973 | -2.32891 | -50.44669 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d340fb4-a858-3eee-807a-c91b04da0636 | -2.32723 | -50.58725 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eceea955-1e09-32e6-a779-32faa98afbe3 | -2.32614 | -50.44275 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f823effb-a6d9-30a7-88ae-6bd9c0492a26 | -2.3256 | -50.44617 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db5636cd-4723-3c91-8f1c-b4905032b594 | -2.32461 | -50.47416 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f77f401-6299-3dfa-be3b-642021935d13 | -2.32337 | -50.4388 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a0be1e-e701-39d9-a05e-5fb8877dc822 | -2.323 | -50.48447 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aef17512-b71e-3275-b73b-f132c756174e | -2.32284 | -50.44223 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fff3f3d-059a-3322-b3ff-abd64e49971e | -2.32023 | -50.48053 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d03575d-2a93-3ce0-83d9-308de02ae4af | -2.3197 | -50.48396 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39463113-ddd8-3b17-ab44-eb53fd20c1dd | -2.31916 | -50.4874 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e10b0e26-354f-35a1-8fc6-9b7ee44c267b | -2.31846 | -50.4486 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed523369-9a86-3221-988b-dcf2fbc81bec | -2.31255 | -50.48638 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 858e27d5-5996-349c-a0d9-e791083c0be3 | -2.30541 | -50.4888 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18d75d58-a1f0-3e0c-8016-74592998e4ec | -2.3021 | -50.48829 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfdec095-d3a9-35f2-b1cb-51dc10299a41 | -2.30157 | -50.49173 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8816fa32-7856-3872-955b-634503a6e148 | -2.29334 | -50.50102 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 409dccc0-bb2a-34f6-83b7-ac19f511c611 | -2.28774 | -50.47201 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11555f02-fd52-38f4-b094-fcfbdd958f28 | -2.28634 | -50.54572 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e971ba2b-f7f4-3abb-b92f-da6a30910607 | -2.57559 | -50.6298 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37c31242-70b5-3227-a223-d10660c1428b | -2.56852 | -50.6534 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d2bd3a-8038-3fd5-8d7c-383517489d46 | -2.56521 | -50.65289 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cb1efc6-7cea-326c-9b90-dfef4b2f2401 | -2.47862 | -50.48804 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1ddb08e-cdc2-336e-bacd-4f0ad7ffc3a8 | -2.43246 | -50.50205 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6d6f3b4-bc99-3ed2-b29a-62c0f5dada0c | -2.42808 | -50.50842 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c591bb0-7b72-3192-9e8c-51382845ee53 | -2.42478 | -50.50791 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e35ae2-073b-3b47-aaed-7248f7d869fb | -2.42255 | -50.50053 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1887278b-7183-3d6f-806c-b6bf4d970833 | -2.41978 | -50.49658 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28ca0192-336a-3676-ac88-923640d33b0b | -2.41925 | -50.50002 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71ffbbf5-f152-3deb-9efd-042303f5ba74 | -2.41901 | -50.43667 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aced12b-cdf3-3343-86b6-cb95918eb18d | -2.41625 | -50.43274 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b578a27-ff57-3b68-9f5d-e6f2de0a877e | -2.41594 | -50.49951 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fb4c470-f8bf-3a23-8ca5-af88e257a061 | -2.41571 | -50.43616 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03fd04f4-8d5e-3d6c-96da-6eebd725c91a | -2.41294 | -50.43222 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 576c99c3-dac0-3312-8ea6-f6f768a9ae1c | -3.13508 | -51.12159 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d114d6-5ee4-3d58-8ab8-e68e3dc099ff | -2.82884 | -51.03443 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57c17be4-4152-344b-bd4a-2b87b61293a8 | -2.79196 | -51.35807 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 214620bf-e795-3434-9c8e-83662ad1eb78 | -3.54827 | -50.87433 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd5e2259-3d08-3be7-ae29-f224f958bfb3 | -3.54604 | -50.86694 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd799ca8-248b-3d2b-84b3-70defacb00bd | -3.54442 | -50.87727 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9649997c-e567-3867-8e06-9486d9792648 | -3.54219 | -50.86987 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d9e8a2b-23d0-36be-98e6-2ec13b266e07 | -3.54165 | -50.87331 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8d63b2-9bf8-34c7-9280-205498a03a38 | -3.51785 | -51.32782 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0eab5d5-b113-3f48-9e9a-41fcccdd04ad | -3.44867 | -51.11746 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2318f446-b573-3359-ae3d-00922cb0c468 | -3.44813 | -51.12094 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d65cf56-2883-3126-9c9d-b3034fd5e075 | -3.38231 | -50.95465 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4734f160-611f-3433-abce-aecf22dbf914 | -3.38177 | -50.95811 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ad79d63-5894-3bdd-89f9-38e68ec83ed5 | -3.379 | -50.95414 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dd5dc6d-2e51-37ee-b98c-d8a02c63547e | -3.37846 | -50.95759 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9016082f-2842-32ac-b17c-d6bc3d24f816 | -3.37515 | -50.95708 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e64d8bf-5d42-381a-ad02-a7b5630095d4 | -3.29083 | -50.90809 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db0adc44-7be0-3a29-a38e-0e6ee95b820e | -3.29029 | -50.91154 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9435b685-2658-3adb-a71e-393764431057 | -3.28968 | -50.89376 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b00517e-a9b4-3c4d-b95e-9d96071507c1 | -3.28752 | -50.90757 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65a84a16-6ad4-3b10-89c5-190131b13edc | -3.28644 | -50.91449 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 315f8ba2-545a-3b89-b42c-fb71793d718b | -3.28367 | -50.91052 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e0e84df-b5f1-3501-85ca-9586550e0614 | -3.26084 | -51.01322 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f625444-12ff-3120-8bb1-bec73ffeb401 | -2.27964 | -51.92477 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2532631-ca25-3e7b-b0c6-60e778ead2ff | -2.27624 | -51.92425 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a421c607-9b00-3a98-9a37-8cd15aaae610 | -2.27532 | -51.92441 | 2024-11-03 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57bdaa1b-f396-3294-aa74-444f56b1ae45 | -2.35794 | -50.69432 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49e1ebf4-39be-3b05-b7e1-8bc5470ef985 | -2.30384 | -50.67186 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35f2dfa7-fc5f-39ab-bea6-fad73c3f19cf | -2.29831 | -50.66394 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e5f386c1-b6cf-3c31-a4ba-a58cbea7b86b | -2.295 | -50.66343 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1efc7999-cb4a-31a6-a087-a18d555b214e | -2.29446 | -50.66688 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae012352-4779-3946-8974-b29ee832a9fd | -2.29223 | -50.65948 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84f44e5a-1f4b-367f-9bae-b9b7034f0ba0 | -2.29061 | -50.66982 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 534bfa43-6c47-3739-8166-c49ef665e189 | -2.29007 | -50.67327 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abe50827-3d62-30e8-8418-a9ca5c293fed | -2.28892 | -50.65897 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81d69270-e8c0-3d1f-8ab1-1911395397ea | -2.28831 | -50.64123 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2811b30f-48cc-309b-871c-d07af29b0177 | -2.28784 | -50.66587 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f1db3ce-5081-397d-ae37-846ab4b5ef2b | -2.28676 | -50.67276 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f866a798-a644-3731-a7b8-317fc44592aa | -2.26792 | -50.64162 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e514bfa-a98f-3b83-a3cf-e2f5ccf2108a | -2.26366 | -50.69041 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d5b1cc8-7f2b-3a58-8c2d-c2b0c2a50792 | -2.26035 | -50.6899 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f88251fc-e5f3-349f-80ff-42ddfcb78903 | -2.24728 | -50.70555 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcc44351-f9f3-3fd2-a83a-4c9657a77ec4 | -2.24666 | -50.68778 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f313e6e7-ef15-35d4-8cc6-4fceac32dfe9 | -2.24612 | -50.69123 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29c9f675-789d-3a12-b096-99ce4f43d2dd | -2.24397 | -50.70504 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 631ef253-bb67-3a61-9f19-1dcb6478e432 | -2.24343 | -50.70849 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b7eb068-d0b3-39b5-97b8-0adf5078791c | -2.24281 | -50.69072 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 403119d2-35c0-3a3d-9951-ac84e69f40bd | -2.24227 | -50.69417 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 448a73c8-7979-3ea5-b234-24cc66c5148c | -2.24066 | -50.70453 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f71e168-c8a7-3c11-abb3-8a5f53f0b798 | -2.2378 | -50.67934 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fb5a744-3184-360d-bda5-4912b6375a9d | -2.23627 | -50.71093 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58b9ff1f-58a2-34e7-9cb0-4feec6c7f0ac | -2.23573 | -50.71438 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dbd8fb5-2870-3bea-9e92-84a171904420 | -2.23457 | -50.70006 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 731e8a73-8516-3d93-a0aa-3e53a2262baf | -2.23403 | -50.70351 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2c51808-9f24-3aab-8dd2-ea916a544277 | -3.63277 | -50.78861 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81351d0e-a355-3477-9bee-4712e4f4f100 | -3.55559 | -51.34797 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e022c19a-776e-3563-a201-abc6c9aa0b8e | -3.5455 | -50.87038 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7181a9f-c1ed-39fa-bc56-83a8d73b222e | -3.54496 | -50.87383 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba54a29f-ec61-37d4-ae9e-be106f94aa49 | -3.51452 | -51.32731 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc1c115-40ca-3524-b299-305bc8aff7b5 | -2.35588 | -50.86113 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62e32fe5-b530-37ae-8bb2-ecb330c547f3 | -2.2994 | -50.83043 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56e1cb39-fcf0-3a63-8b13-c6ad05d6bad0 | -2.29387 | -51.27712 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 281a802c-d118-31a3-a20d-7780a9f7f7da | -2.29331 | -51.28064 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README53.md)
