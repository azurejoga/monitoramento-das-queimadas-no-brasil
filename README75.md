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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c430a74-3ae6-3ce3-8627-48cb51694687 | -12.85133 | -46.85475 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cfe90c5-ea8d-3d70-a578-c563d3a81bec | -8.84612 | -46.77851 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1522c502-1d48-38d8-b99e-d97fc16dc709 | -13.2719 | -47.22262 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| deb0d927-324c-38b2-92e9-0ce7d81d4132 | -11.91207 | -46.2559 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0733d32d-1a21-3744-81c0-a8ecdf5f5352 | -11.92186 | -46.36335 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ad30b030-ca64-3834-aee5-172711123f77 | -11.549 | -47.67926 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46d5f9d1-3ce5-3486-b830-aaafaad9a565 | -9.93482 | -50.89915 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2de8b98c-1664-3e12-a8f3-03f7a081d2a3 | -12.30103 | -45.3608 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ae6f973-c3d3-3c83-95ce-340a2e36b65c | -13.03474 | -44.7494 | 2025-10-04 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97aa7dca-ee1d-38a1-81bf-821fd1bd4e45 | -11.00132 | -46.68218 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 013f957e-db4b-3aa2-a0aa-0e42564ff690 | -14.83753 | -48.37352 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7338e4b8-4ecf-3c82-b086-4ec1647fd8f5 | -13.99793 | -48.193 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fc98f78-40c4-3a1c-9bb8-c244f9660480 | -12.78445 | -47.71814 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dd7db51-0c14-3371-b601-ab688bf30d6f | -9.66894 | -48.22818 | 2025-10-04 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 960d4b34-254c-3f52-ac20-30640562ce85 | -12.27376 | -55.13345 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99cfc1b0-a55f-3c59-8a4c-f7eb32627516 | -9.92556 | -50.19931 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5cadcdc-77ec-38a3-892d-0109f818e7c0 | -8.85066 | -46.81844 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36393084-7836-3d49-9ab5-3dd3af1c0a4f | -12.91201 | -54.73496 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e86fd7-d6e3-3083-b7a3-eb1da7b9f2fa | -13.23388 | -48.48709 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c4b645b-df4f-3aa2-b3d1-e9e651673496 | -14.43958 | -46.11683 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 207ca821-3509-3efe-9313-1003bcb3b081 | -14.94199 | -46.86426 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1477fb70-b3e0-3513-b3f4-81a222c1faf4 | -14.38097 | -48.47776 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d1f8584-df83-37a6-9f22-53dcccdb13d7 | -11.87375 | -49.91432 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bbf6695-ce49-395d-aaae-0eb3103ee00a | -9.93196 | -50.24075 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 541edf96-a374-3483-883f-0b49425d7296 | -11.09756 | -49.85282 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3564423c-5108-3afa-8eef-9aac987c0d3f | -9.33486 | -45.75159 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29fdff4d-3278-3df5-a793-da2d98613df9 | -11.78316 | -46.82149 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e4f74d6-dc14-3b4f-a28e-71ebd7109cbd | -10.84484 | -47.20589 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15706cdd-7d52-3fa5-842f-9f8fef65b758 | -9.12113 | -44.38558 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cbaf23c-07be-35fc-bdde-f5e6a3f63bb2 | -8.84576 | -46.84797 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d0658f0-0f5b-322c-be75-0d8f8b902efc | -11.4817 | -44.98343 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4ded95d-05e8-364e-a473-25adcf64b3e9 | -11.78529 | -46.83038 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9168470a-a061-3988-84a5-1c9584588397 | -9.94072 | -50.2393 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0316c460-3e16-3229-82c2-5d7aa6cb2d33 | -13.85779 | -47.9159 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff1101f4-c402-3c2f-b0cb-89fe12591fba | -13.99201 | -48.20577 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e751c76-109b-31a1-8a63-1466f64a81f2 | -14.72942 | -42.29699 | 2025-10-04 04:14:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8d531d2a-370a-3077-9e03-431dcf457735 | -7.74342 | -46.3045 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cc95e934-c57d-3d26-9a3f-1dd8dd34c31c | -11.12509 | -55.46791 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96dca78a-de4a-32f9-8d60-68f7ca773fd7 | -11.50763 | -45.01334 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ada170a-6a42-31de-8008-c498c92f02bb | -10.53778 | -44.51377 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d68232a-bab4-3767-b357-a7a28f540fd6 | -12.27874 | -55.139 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2eebcdd4-3518-34f8-ba2b-1f3f6527e85e | -10.01892 | -45.5166 | 2025-10-04 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 838ffa9e-40a3-3b6c-a3d6-a6a9753c19c1 | -13.31272 | -48.1399 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13f3ce67-7fbc-37c5-97d7-958d137b52a9 | -15.3259 | -46.30499 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 766b5c20-e6c1-3424-932f-8d4d753e921a | -8.61734 | -54.98191 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d12e16a9-3fe3-3281-9869-d4434a648a9e | -11.62789 | -45.06982 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0339fbe1-c8a5-3853-8d83-45d382a40c9a | -11.90938 | -46.35333 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83ef69ca-7cda-3331-9aa8-51dc95854873 | -12.04421 | -45.18586 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd7968c8-4f42-39c3-8456-8153b24277c2 | -8.05857 | -44.7993 | 2025-10-04 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a0493455-58f5-3ceb-84ff-afce24a092b5 | -11.15015 | -43.38635 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4ec982ab-317d-3cda-b3ea-639c8f1f23df | -13.50733 | -47.26911 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 558d2aab-247f-36e4-9b90-0da2464e187a | -9.12878 | -47.43567 | 2025-10-04 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b4160e4-66ef-3ef7-8a54-49d797ebef0e | -11.49247 | -46.75823 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70a3d862-56f8-3e1a-b59e-bbed4c2f97b5 | -13.73839 | -48.08629 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 840b30db-b8e9-3bfd-a9e6-f43e3909b4b5 | -13.11242 | -47.92817 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55476887-f7f6-35b1-8de4-014043f418e9 | -9.32955 | -45.76242 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 01340697-15bf-3bcd-bdfd-514fb7bc54d2 | -7.73402 | -46.29455 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b8ae508-4772-3fd1-8ccd-3644c3d4eedd | -7.85985 | -48.19537 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21ca447d-94f1-3c0d-b7fe-d4929f574b92 | -13.26852 | -46.47781 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 264a88b5-23f6-30dc-808e-aff567234def | -11.90829 | -46.36565 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f922695-b085-32ac-8e41-e7db1ae4c4ac | -12.49123 | -46.92619 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aa3aceb-3d19-3c74-af5b-c747503576dc | -9.93789 | -50.22983 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f2f1003-fe15-3cc4-b313-b32e0bb15e59 | -13.7479 | -48.0527 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2715dc3b-9c89-3d7e-b304-3995dd0b4db5 | -12.08119 | -47.98591 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27002993-e425-33f7-a2fd-6c4a65ed9f93 | -13.31533 | -47.79722 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9d4fce8-e221-3d1c-9513-4ab53c613c62 | -11.48012 | -44.97613 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac049669-e62f-39f6-a5f3-ce485d420e90 | -14.86681 | -48.3563 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05781fb7-6db2-343a-90f7-d8f768d898b9 | -9.91888 | -43.76858 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f65f099e-d6c0-341f-9c94-48b340d080a8 | -9.90727 | -43.71308 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b3afdce-e16b-3d19-8015-d608c50cc91e | -10.07052 | -48.18219 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74c9300f-0cdb-3e69-9cdb-3134bb7ee7af | -11.83348 | -45.01635 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e3fb98d-d340-37ca-8126-bf7b0d3e7c16 | -9.34144 | -45.7762 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be2ef2e3-f399-3b31-8fd2-e807c7816a8f | -11.45058 | -45.13932 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16901e57-1151-3c83-8cab-1f943510ded9 | -13.11384 | -47.85431 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0ad447a7-96b1-305f-8af1-8fdd7c7f5d82 | -8.95462 | -48.68454 | 2025-10-04 04:14:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9100ccba-633e-3343-aed1-2756c9b9da7e | -14.92932 | -46.8984 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 622e9471-610f-3d3b-b04e-ce64c8ed73bf | -13.10088 | -47.88628 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 90e0a425-cbfd-332c-bea2-479c696ff011 | -9.91502 | -43.77154 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 662d99ae-7820-311d-8117-1ed30955f316 | -13.70349 | -47.35252 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55e04ac0-d4e9-3d03-a709-7bd74bf1d0ec | -11.90963 | -46.373 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adaa09f8-c73a-304f-a345-3b7f6cb0e571 | -11.11897 | -47.88555 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15cf8b16-baa0-36af-a89c-27ce4611165d | -13.98836 | -48.20308 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 277cc300-6507-3a2f-994c-11cdce30ff62 | -10.04306 | -49.20328 | 2025-10-04 04:14:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b56032c9-40a0-3cc9-ab14-7b11b947910e | -8.90823 | -46.60431 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01f60471-b0b0-35fb-9e8e-c4483805a29f | -11.8015 | -48.91433 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2153a745-a8b6-301f-9aa8-a2964049c8a9 | -9.95097 | -43.73732 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 247388c6-f18a-30c2-bed7-9595dce36a14 | -14.35172 | -46.10555 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b62b816e-2b4b-3476-9fc0-9d8e4347c96e | -12.36718 | -46.51591 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93914c92-6762-39ad-8c20-317c416632d5 | -15.33718 | -46.29932 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d6c5259-30fa-33ce-be5d-be0d2017cef4 | -8.96573 | -46.75827 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c41cfd3d-78de-337c-8de8-2e45de9ebe08 | -13.29645 | -47.8204 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d678f39-63fb-3acb-87bc-d437c43d129b | -9.91657 | -50.50011 | 2025-10-04 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6c593b95-31dc-3657-9ec0-66be533bfc3e | -8.63971 | -54.5962 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c2f724-278f-33d0-bf69-1cd9115ede47 | -7.93235 | -55.02819 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0a620e9-8294-34eb-954b-93af9740ddcf | -13.39291 | -47.28076 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96ee08aa-3928-3ea8-9c79-6a7ae5c65957 | -11.21094 | -54.9898 | 2025-10-04 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf05ff11-1c6e-3fc0-aec1-5f0a684639f2 | -14.90264 | -46.95288 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0247ec1d-f180-36d7-9fef-7eb9097fa979 | -13.96482 | -48.12276 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e91d3f3-5bc9-3e8c-96bc-c5afeb44cd8a | -13.33106 | -47.19506 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 727e1170-3b99-38bf-95b4-0baabe9775c7 | -13.72959 | -47.92055 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README76.md)
