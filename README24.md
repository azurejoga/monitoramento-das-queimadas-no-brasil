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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47454a5e-39c4-3a39-bf1f-76669a967f07 | -7.28215 | -60.64244 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92b15750-2273-373a-bd10-60ced065b07e | -8.11105 | -54.77796 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fa83818-a857-395f-a8af-93a91f7ec398 | -3.24623 | -47.25624 | 2026-09-04 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e343d42f-4561-319a-9422-f074d7a53fb8 | -3.29022 | -57.88155 | 2026-09-04 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 528bfb9f-36e4-3882-accf-3ab39de68961 | -3.01991 | -61.48911 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15e2856c-06fe-3acc-b71d-a545a20013b9 | -3.27781 | -60.1706 | 2026-09-04 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a32c77-dde6-33b2-bfa8-0227311d1aca | -3.29424 | -57.87833 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccca74fe-1253-33a9-905a-999b6e21cadd | -8.42095 | -54.71584 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6433bf9-35c4-34e3-bbfe-d050135e5f60 | -8.71462 | -62.94975 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bde7f83-e410-3fc7-bbc9-9c4cc13c2c8b | -3.19698 | -61.20942 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82f809c3-5004-3784-9213-d6d054af77d9 | -8.10607 | -54.78475 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87722007-3a63-3b47-a461-ba725b932e49 | -3.62744 | -54.60638 | 2026-09-04 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b240a148-cc8a-3a6a-86f9-6a979eaa7b91 | -6.94366 | -56.46439 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1d0eb14-df09-3541-bd34-cbe969eb88b5 | -9.51344 | -60.50182 | 2026-09-04 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bf4bacc-be4d-3faa-8810-355849e90489 | -6.56164 | -58.47559 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c691e38a-8cc3-34fd-8746-53880e06c8be | -3.19195 | -61.19775 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f330efb2-2214-36c2-9c21-287c3f97b4a6 | -6.68086 | -59.98149 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc5f3d98-9ea7-3d92-8170-c85ab34394ce | -3.13525 | -58.63789 | 2026-09-04 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3755140a-f5a3-336b-ae73-7b8b7138e427 | -1.38737 | -55.76291 | 2026-09-04 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb45fd77-fa33-36ef-b4ee-8a29f51cef1e | -6.68859 | -59.97553 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 182c0042-14ea-3df8-bdcf-ae745c5b1b78 | -3.07394 | -61.08117 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e6757d9-7265-342b-afcc-cb07e3d5a6b8 | -2.58808 | -59.40448 | 2026-09-04 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9909d52-4055-32e6-a729-274f388cc908 | -8.49358 | -54.64418 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f98af973-4ba6-39b3-81f2-bc118f714f7b | -3.16346 | -61.11728 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 595a0ea9-3aec-3051-afc8-d841aec81724 | -7.557 | -61.34243 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 96c495ad-a8c5-3c25-8367-fe05a6803ea8 | -3.29308 | -57.88583 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c14f098b-d1da-3067-9597-7f0b7298e0da | -3.18021 | -61.16331 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e61d6965-bf86-3c5a-8156-38420f19d4e4 | -8.43787 | -54.69194 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 699a236d-1044-3780-9b62-74cc01550c0b | -6.68302 | -59.96751 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 04b814c5-53b2-3f23-8345-67cacac57708 | -8.46651 | -54.67658 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9ad1620-a983-3ff3-9e52-ac47cf1fbfcf | -7.24349 | -59.52514 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f322560c-bbcb-34d2-a4e3-ff67ad59e3d2 | -3.62386 | -54.60191 | 2026-09-04 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01fe76f7-ba08-3676-8f2d-a8675a13a7c0 | -7.28162 | -60.6459 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f69369a-74a5-3a5d-8934-57d7a49e2b2e | -6.70283 | -62.85958 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47813fc7-282b-3d3c-ac71-8162865434d2 | -6.97526 | -59.78989 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87a68477-48da-323e-b460-aa9cc956c54b | -6.13918 | -59.92265 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25dba435-d3c0-3ab2-8102-20d85f408b3d | -8.81095 | -62.48825 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1720b437-8b83-3dc0-8af7-92f086501e7c | -6.75881 | -59.43263 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 317d7ddf-65b8-3482-81d1-5f21587571be | -7.27157 | -61.12292 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2dccca6-cc31-3aa0-a4bd-88181eaa9f93 | 2.44758 | -60.76441 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0a4eecd-dff5-3719-8435-4d680f9e2eef | -3.32432 | -59.45914 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b642bb-ce21-300a-9a5c-0c708d265cbb | -6.6879 | -59.93604 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c61589b-b17c-3485-9149-cd7dc62882de | -10.50192 | -51.32513 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76d2e7f9-019e-3207-b830-f003359d3812 | -8.50569 | -54.65505 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6df178ed-138f-31e2-abfa-134cf520f5c7 | -7.2649 | -61.10059 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afadf20f-440e-35e8-acf4-cbcad2624f19 | -7.09508 | -56.51892 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbdfac83-7080-352f-bc6a-57ac6b31440a | -7.55315 | -61.34534 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 15989ba3-59dc-33df-bcf7-3820d18d0289 | -8.88456 | -62.34991 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd0b9769-d34c-3581-a220-84fd09092b6e | -8.44638 | -54.69167 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ccc6383-59c9-3ac2-b83c-f8ae01a8b2aa | -8.49297 | -54.64863 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 95c1e8f4-ab6a-3407-b49a-dde73f69844d | -3.14321 | -60.64091 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 040cc704-f719-35ad-bd6a-e0490a81cb34 | -3.09465 | -61.1894 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ba636d6-30c5-30f0-a550-1438168a05ff | -7.01269 | -62.98564 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3f6735c-5f7b-3ad8-9caa-a713364bdd84 | -3.20033 | -61.20993 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66db8161-211d-3713-a30b-5e2b0398526e | -10.84022 | -51.78375 | 2026-09-04 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 112e2786-e5b8-3356-b321-d36696ac5eff | -9.50732 | -60.49725 | 2026-09-04 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28a2c0c0-49ae-3eea-a378-c7efc6d90568 | -6.71255 | -62.86498 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25029945-ef0f-393e-9a9c-a9da9d61894b | -2.59139 | -59.40499 | 2026-09-04 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86322129-b51b-3481-ab06-00ee3cce7aa0 | -7.78491 | -63.38552 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73a9277a-b320-38d5-92b1-d5fe064b248c | -2.91815 | -60.9922 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 337e84de-2c16-333b-8257-576d66e46e83 | -8.50952 | -54.66013 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dcf76267-fee7-3de3-8c95-f0c3a0a34ef5 | -10.50648 | -51.33563 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 0fe78e0c-cd6b-3cfd-ae18-98b239ce6b85 | -8.49619 | -54.65815 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3fd1f330-abd0-3417-b060-45f0c6d314a8 | -6.1503 | -59.93862 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3b3c7e-a337-3565-9c6c-88a326ad5f33 | -7.2463 | -59.52928 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fd5ee71-ad8f-3d18-a8f7-17799314bd55 | -7.3259 | -59.58518 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0366cff-53e0-38f1-9fd1-340c066c96e2 | -3.126 | -61.2306 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c3dc205-3db9-3f27-8ebd-6ab9f12a9c6d | -6.7114 | -63.18192 | 2026-09-04 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d9560364-36aa-3a54-a703-cfe36ce4e015 | -8.12182 | -54.80027 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c855a4e3-e8ab-3157-8d4e-feccac875c56 | -10.31128 | -50.34136 | 2026-09-04 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20306cb4-e8ad-3b71-8651-662ad5975c03 | -3.12822 | -61.23151 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c46d10b-89ba-324c-a944-f03918c5d640 | -6.70911 | -62.86443 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99869520-e072-3cf1-9353-dc1168a25bde | -7.56639 | -61.34742 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cece0445-9288-39e0-8489-9fede8cda810 | -8.83351 | -62.3091 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e9ef154-df50-3d39-8377-edd57fd81fdd | -7.57991 | -61.37098 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc7a4859-e4ce-329e-9676-1c1e1895ade1 | -8.6926 | -62.93486 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b0f45bf-22ad-32e5-b70c-f48dbbf86bf7 | 4.26829 | -60.05923 | 2026-09-04 05:23:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8419e3cf-3536-3e18-bbf7-1ecca162ed8b | -8.50002 | -54.66327 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3fee37c1-c7f8-3b5c-9971-7dc27d660037 | -7.55423 | -61.33844 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c301bc57-1887-3c54-b4e1-603cc0602448 | -3.44808 | -56.32198 | 2026-09-04 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ba798c9-bed3-3d36-87bc-af433c0e6e80 | -6.76217 | -59.43316 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba26009-ba90-309e-ab44-ebe0984ca97a | -8.79928 | -62.88386 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89df87ea-46cd-30c7-ba0c-de58feb9e34d | -6.69083 | -59.98303 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6f68bdd4-0004-39a3-a7ed-3646fc5eb48f | -8.49864 | -54.64036 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e9a633f1-5eb4-3f44-8b8a-9cc9cc70e48a | -7.67679 | -62.5439 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa467958-f8ed-3567-a518-f6184e62ba01 | -6.63744 | -59.44721 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da7a5c7d-57dc-37e2-b6a1-c1411535b1cf | -10.50688 | -51.33234 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 8d583019-9f16-3d09-b0aa-4ac66ff5d1ae | -8.19115 | -62.79782 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cac33891-d226-338b-9d0f-161ebd67d3a9 | -3.14279 | -61.1829 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0deaaa40-9f2d-34d5-8439-8176b2806244 | -2.64557 | -60.97115 | 2026-09-04 05:23:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa70c803-eed8-36ac-9aef-d8c5909a2504 | -3.24647 | -60.80702 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0d403b8-a45b-3833-a83e-7a8df14df2c5 | -6.67962 | -59.94552 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90987545-daee-3a8a-8f24-c57470ee9f28 | -10.5049 | -51.33559 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 89db8efe-779c-3ed6-9abb-198f19438bcd | -8.43848 | -54.68764 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bef6efcc-5c5f-3817-b25b-e81ef8b9c507 | -10.91233 | -49.61777 | 2026-09-04 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f28335de-b759-3fde-98f2-77687a2ac58d | -8.90683 | -62.36078 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 346f0072-1699-3b5d-983d-234d913d8cc0 | -8.91908 | -62.37003 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d14a2a3-cbdd-315a-aea3-28c1d605eabe | -3.12655 | -61.22705 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdfecd1e-4ad0-360c-bc4d-7344c509c069 | -8.75098 | -62.83855 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ff47f2-a286-3c16-98f2-69be01777d25 | -8.92298 | -62.36701 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
