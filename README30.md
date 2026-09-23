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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edbf6093-5c2c-386c-a967-b82a486c7506 | -8.2404 | -55.245399 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9bd615b-bfb7-3dae-be1a-a8114503d513 | -11.7059 | -50.9034 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d04fa7e-b515-392c-8a23-cf6db84e5bef | -3.1013 | -60.694698 | 2026-09-23 00:58:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e149f3d0-3a19-358d-814d-6a7868ce6ab1 | -5.872 | -52.0532 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26533820-4041-3c23-b593-7b8b4076fc82 | -7.3999 | -55.215 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76546224-86b6-33ce-b136-b0f004e1cbb0 | -7.5631 | -57.6628 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3c0d079-fd71-34ff-8b5d-981718f338b5 | -3.6786 | -60.529202 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee98514-bf82-3c25-8f0d-a7df816eadbf | -3.4758 | -59.5788 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccd3519-01f7-3822-86ff-241caf94b7a6 | -10.7116 | -48.714699 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 184b41c4-b855-3fd3-8dcc-a85f155d628a | -11.8676 | -45.773399 | 2026-09-23 00:58:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe9312c0-4853-37af-a781-ae34fbdc503c | -11.5217 | -45.347301 | 2026-09-23 00:58:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf0a47d8-ae5d-3af9-b844-510887aa3a36 | -5.5131 | -51.708599 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb17a19-a8e7-33ec-8753-bf56d2ed4c6e | -10.2691 | -49.976501 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad2cae43-32a6-31a2-abd7-75e2db538633 | -10.3028 | -50.5131 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2caa35fd-9844-356c-aea9-033fb41337fb | -8.0893 | -48.852402 | 2026-09-23 00:58:00 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4efbfa60-8854-3f05-a4ab-0e0ba0c73a7c | -3.2229 | -46.913101 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba0a3c9-58f5-3e47-92d2-71e3e1816872 | -7.7861 | -50.221901 | 2026-09-23 00:58:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec5da4c3-1279-32a3-bc3b-d77e69eb31bb | -6.5762 | -51.487598 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1678b59-0554-342e-8752-84a4e3eae56a | -4.9718 | -56.955898 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba27bf6f-5a03-34c6-8f0d-fc81ac79a9f3 | -2.4588 | -57.899101 | 2026-09-23 00:58:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc3688f-32df-3cc7-b184-26eb6f94250b | -12.4867 | -47.006302 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb406f27-a148-31ad-a392-9dfc2f7900cd | -5.879 | -52.1278 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e96dca8-1f02-39b3-ba58-cf8b522415e4 | -3.2498 | -53.965801 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37986e1c-72c7-3fb2-ad8e-f387500816a4 | -8.2011 | -54.702599 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c89f8f89-0a5d-3b86-ba84-baac1092ae89 | -12.815 | -50.877499 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 992313c6-b0c9-3206-9dc7-a8607117f0c5 | -8.7848 | -60.790401 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8afca4ce-88b5-3200-b91b-5505b46a9bff | -10.6004 | -53.970402 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad7f3f03-2496-3f17-a3f5-2220586454f8 | -5.8069 | -52.083401 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 565a46be-190a-3bde-9acf-e4274bdb3d39 | -11.7229 | -50.799198 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65a812ed-641b-3696-9e73-a9b05de6c806 | -13.8611 | -48.564999 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91ca7c62-8783-358f-b501-18f6123e9755 | -3.5345 | -59.611698 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db157359-2035-30ee-906a-6683d9ae2c8c | -11.7046 | -50.942101 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59485bcf-331d-3639-b666-1df97a09feb5 | -11.5041 | -51.503201 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b26d9433-3ee6-3d4d-a620-736a21d8eafb | -6.0817 | -57.6917 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08449207-0076-38fe-ba63-1d2486971f6b | -7.331 | -55.5956 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 668807cd-2705-3505-9e8b-e8fdb1290d2d | -6.6051 | -59.887299 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1e3322-3170-34cf-9465-f01b3bbba405 | -11.6863 | -50.9081 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 525a1ae3-81ed-3e2b-99c5-b7da9766c6f7 | -10.2556 | -49.962799 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c20d0c6-3f15-3c34-8505-cb15497c09fc | -6.7168 | -44.124901 | 2026-09-23 00:58:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e97a2310-4bc7-3eae-962d-a335a9aa79fb | -5.2765 | -47.242802 | 2026-09-23 00:58:00 | METOP-C | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8720864-45b7-320b-bd22-9fe5bed16eef | -3.4636 | -59.57 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55fac124-7cde-31e2-9a4b-e7f4244bf871 | -7.3293 | -55.5881 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68e0f742-9e55-36b3-949b-292343b8ad3d | -8.4441 | -55.006302 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a999ca03-8bb4-385e-9363-b07672502090 | -11.6628 | -43.454399 | 2026-09-23 00:58:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcfe9aac-b42c-352f-9941-2bda0796e1e6 | -10.878 | -50.1483 | 2026-09-23 00:58:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9ffb6e1-7d4c-334a-8a12-d7dfaf39ad05 | -8.4657 | -48.700298 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1faa6336-9007-3505-914d-75c4db6a645d | -3.2833 | -57.859901 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eedc36cd-0d74-38db-9fcc-f4ac3b5904d1 | -12.8117 | -50.863098 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45a4f5c0-86f9-3ecb-9713-75ba7fa9b091 | -7.0946 | -52.7421 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d40ccc-f9b9-366a-9e06-57ec7e50679f | -11.105 | -48.332199 | 2026-09-23 00:58:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35dc4edc-4813-3a64-900e-4e83cda7c8f8 | -11.6931 | -50.937199 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 872a8e87-e643-302d-a81a-33836d5cec29 | -12.4093 | -46.944698 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2fe1d5-aa07-3f54-8687-9b474361ba14 | -12.7645 | -50.882 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c809fa6a-c6a2-3cfc-8fc0-dbb6acaaf661 | -6.9243 | -46.567402 | 2026-09-23 00:58:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55b7421d-ca35-3e46-acd4-d0c4c7dd082a | -4.3012 | -56.265301 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ea3aa5-da92-3b9b-80ab-e26897ef1352 | -11.685 | -50.9468 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5f68dc1-4ff7-3601-bdb5-6bec88f46341 | -12.8006 | -50.9039 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4fadff8f-607c-382a-9ab9-9e94cadadfbe | -8.8295 | -50.4856 | 2026-09-23 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541e7842-7b07-3787-be71-477727948350 | -6.686 | -55.062401 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af3b53cd-fb5c-391d-a8a7-5345c78303fc | -11.7029 | -50.934799 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c7a26be-37da-36e4-b67e-39dd6463a74d | -13.4481 | -46.253799 | 2026-09-23 00:58:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 453a19c4-cc48-3183-9261-d9df91f59fe5 | -3.7792 | -60.750702 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76498c49-d665-39d3-9520-c46088345cfc | -6.1254 | -57.749298 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54c2785a-2a7b-3d24-97bb-7633368a5987 | -4.1609 | -60.765301 | 2026-09-23 00:58:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03188500-2f40-3969-a11f-0e981decd432 | -5.8295 | -52.0476 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b663191e-5284-3956-b857-193fefa57170 | -3.6801 | -60.5821 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0589a008-85c7-3a99-88eb-1106fe1df40a | -3.8881 | -51.9533 | 2026-09-23 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aced7b10-576b-3807-825c-55f1f9eba3cb | -6.1564 | -57.704102 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f97989-4e0a-3db8-8853-593040189824 | -2.9531 | -57.719501 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba71171-f16d-3623-bedf-5e1584feaea6 | -5.7579 | -45.094601 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88c4a2ca-1271-3387-9ffa-ceb06f4c51a4 | -1.3262 | -54.661999 | 2026-09-23 00:58:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52bcd274-3547-3bf9-9948-cef45d2b93d7 | -4.0636 | -56.2164 | 2026-09-23 00:58:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d37e9830-4f5c-38f3-bc75-96d77361dfa0 | -10.7094 | -48.705502 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b1b7814-f5d6-32db-9f81-9e794f4d7089 | -6.5994 | -59.955299 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 867d8cc4-717d-3a8e-80b0-5b6eda324e0f | 4.1058 | -60.989498 | 2026-09-23 00:58:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0496d157-7b3e-3221-ab67-62e08e4e5db6 | -7.124 | -43.0634 | 2026-09-23 00:58:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38db4036-effc-3449-afd7-29135692ca20 | -4.3079 | -49.131199 | 2026-09-23 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51cb12d1-5285-34b3-9cea-716c3085348f | -6.6301 | -59.9086 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac80e4b2-deb4-387a-bb83-b5d566135179 | -7.4197 | -49.852798 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c14017-58b6-3ea9-9db3-6986fb02b292 | -6.0013 | -45.247601 | 2026-09-23 00:58:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b778905-a125-35ad-962f-f29eb66261ac | -3.6052 | -59.0131 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7697230-ccff-39cf-9938-e6a012b180f1 | -1.826 | -55.715401 | 2026-09-23 00:58:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71607ad8-affb-36d0-8a7f-7c6b18e1ab89 | -6.5977 | -43.694599 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b74b19de-9352-32ae-b68f-fb9bdfc1ba59 | -9.5332 | -45.368301 | 2026-09-23 00:58:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 73c273af-3d1d-301f-a85f-d336e5133f4e | -7.4233 | -49.824402 | 2026-09-23 00:58:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cef6f10-3446-37a9-9313-5171c144f10e | -5.8919 | -52.094398 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56083a49-e418-3c2a-ab68-3d906af7d646 | -11.7815 | -50.9622 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2200fd99-1743-3b87-b1c7-a2204661404c | -2.2418 | -48.7537 | 2026-09-23 00:58:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6833d6-c22c-38e8-bd65-7f3435dade52 | -8.461 | -48.680698 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cb705eeb-5e8b-3a37-b17b-64b74e13287f | -5.8828 | -51.568199 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1d675df-496a-32dc-a064-c5f231d76302 | -3.0081 | -54.170799 | 2026-09-23 00:58:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc22f87-5626-3115-a9ee-800aa0997927 | -7.4351 | -49.830799 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed13303-2148-3d55-9534-879b477c9cbe | -6.6186 | -43.7369 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc3a73b8-dc6f-3594-938d-dbb05912eb97 | -3.8443 | -58.660999 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97fda889-4199-39fe-8c57-778d13897bd9 | -3.068 | -54.386398 | 2026-09-23 00:58:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75aae366-0bfc-3059-a35f-013558b0ee8b | -11.6769 | -50.956402 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea707cd0-c2ad-3b56-993e-824ea451957e | -4.5558 | -54.9389 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09efa880-1e9a-389d-bada-3090928cb990 | -10.3884 | -54.404701 | 2026-09-23 00:58:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a49b62b-cca8-3f8f-af0b-cd82d1a305a0 | -6.4366 | -48.4613 | 2026-09-23 00:58:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 668a1a8d-4453-31aa-9e8e-382eb38edd09 | -2.8696 | -49.6278 | 2026-09-23 00:58:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README31.md)
