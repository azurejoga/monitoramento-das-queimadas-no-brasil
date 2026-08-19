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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf3710a8-3dbd-3b54-86f9-b04ca206ef64 | -8.57587 | -54.70363 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94ea8414-2981-35e0-8b11-21d972fab357 | -11.23652 | -46.14837 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de7a869a-cc32-3c6d-aa6f-c75ee8590eff | -12.77241 | -48.45015 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2416823f-1bd3-340b-a861-730bd374f133 | -9.58368 | -48.26434 | 2026-08-19 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b654b83a-c276-32eb-a395-46b251a30ef0 | -8.55992 | -54.74355 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de928162-d6b3-3210-b3ad-f4e67a458343 | -8.5592 | -54.74763 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9cf4d9e4-7867-3301-a355-805cf4f5a978 | -9.13564 | -60.61398 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78952638-2361-3910-823a-8d93c569cfe7 | -8.49919 | -54.85642 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68db4c49-2bb4-35a6-bde8-3f40d172e341 | -11.21074 | -54.00348 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 384557a1-d206-35da-8d12-959459a6ac6c | -9.44341 | -60.29844 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faf1ab44-cc57-3e95-bbd8-b5756c92c9ce | -8.61401 | -54.71489 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f67066d-d214-3193-bf9e-dc18056a4920 | -9.05877 | -50.84119 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 491386fc-80cb-3031-bfb9-ca1257162526 | -8.53812 | -54.7656 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdf87697-3544-3820-9d70-b81f5cb45403 | -15.00882 | -41.94946 | 2026-08-19 04:40:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16aa1875-76f6-37cc-b181-63eaf84c83a5 | -9.46237 | -51.60691 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e596b2ec-b0a1-35d4-9884-9f2182c47d97 | -8.56931 | -54.74096 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65a9c0a3-c163-3d05-836f-46eaf2e2b0f0 | -12.37833 | -46.44986 | 2026-08-19 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 195fd930-ad00-3c02-a0ed-44b6a4c065b5 | -15.27867 | -56.5011 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391399af-0045-3297-862a-0fa9d72328ff | -8.53106 | -54.72274 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db5176d6-0ef2-3e16-9b51-852d836626f0 | -9.39609 | -60.57986 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 388527b5-1918-3c2f-862c-cebd3596fbe8 | -15.98894 | -54.17657 | 2026-08-19 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa0cc58e-ed81-3fa1-934c-cd440f7122db | -11.22646 | -55.0705 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 555e310b-d4bc-3fdb-824a-16154b7f6ab8 | -9.49757 | -51.67488 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a77d21c5-b5b6-39ab-869d-10e658b69f5f | -9.40539 | -60.58342 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1f791a7-ec0a-31b2-b5a8-28cdc1c42934 | -7.60726 | -60.96977 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48ebbb62-ff71-3ef9-98a0-503527353bb5 | -13.45092 | -51.80595 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbb74ad6-6ef2-31af-aaa5-e9c627c30b2c | -8.55124 | -54.74207 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d88922f2-88c4-337a-a7a3-9f56e2e40aa6 | -9.15579 | -59.70871 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cee4c368-6c9a-3156-95b6-c2e35d26a7a6 | -11.2251 | -55.05377 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76a17e78-40e9-3d8e-a81e-7e1eb5959999 | -9.72969 | -46.77954 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f22e46-a779-3466-a61f-dcc1d082dd70 | -11.69743 | -54.56574 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b661f4d-5753-321b-a8aa-0d38bf47bd2b | -9.72855 | -46.7871 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37736072-444a-332a-bf9f-95e992f05089 | -11.63694 | -54.52817 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 208179b5-379f-35f1-a8d8-efb536e220b8 | -8.53109 | -54.74872 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95e02aff-1029-3710-b193-95338bb236a5 | -11.22439 | -55.05771 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2626a64-b768-3df2-b9f6-0fd41ee0355b | -8.58019 | -54.67902 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7464de65-8bc2-3e7b-a5f2-131e6ceb0da4 | -11.22791 | -55.06245 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b7645dd-416e-39d8-b5d3-b57b4a0221ec | -8.52732 | -54.75082 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7422f1f-1e63-3ca4-973f-bdde4ac2fa0f | -8.53977 | -54.75022 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2599756a-1f71-3619-aff5-f19acf316890 | -8.55485 | -54.74693 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5716358d-c9b9-3fb1-b99a-15f66bc2c2d7 | -15.27569 | -56.51172 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5648bf78-8236-3c0d-b5a3-9fde16a64f75 | -14.21496 | -52.91078 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f14396d8-cf4e-3bb6-93c6-78dba48d4897 | -8.53611 | -54.71928 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d970e75-caec-3248-8b33-1967f4040442 | -8.58013 | -54.7302 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f676118c-1ca3-30b8-a24a-00a3bb2e9a0b | -11.61994 | -46.91358 | 2026-08-19 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b84b93f2-2df4-345c-8f16-fdb796d8d41b | -12.88917 | -52.82267 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96116370-86c4-3bbd-ab01-4d076193d4ab | -8.53033 | -54.72697 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6791d754-7d87-3beb-84a5-643c84276ec0 | -9.38967 | -60.56446 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc1163c9-3140-31eb-af7c-6d12d1bfb490 | -15.71045 | -47.80449 | 2026-08-19 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6c1f6e8-4b1e-3565-8236-f7b2d5c25b6b | -15.27647 | -56.50744 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 708716d3-1d04-398c-a6e6-72b89c0a7fb4 | -8.57073 | -54.75833 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 775dad39-5031-3dcb-93b1-46796979488a | -8.58445 | -54.73098 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15db7588-ebeb-393b-b041-6c8fd270ae8a | -15.06589 | -45.32947 | 2026-08-19 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47cbc764-e451-3f27-b796-0acb694639ef | -11.5886 | -46.81358 | 2026-08-19 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5264843-f52d-3b8e-9acc-07be9e2008fb | -9.81179 | -46.63267 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da22bbfc-60cd-3434-a5e9-8cf3ecb0869e | -10.19433 | -54.24389 | 2026-08-19 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 077f87ce-fa1e-3b9b-8759-5d298d5303ef | -15.06981 | -45.33004 | 2026-08-19 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aab2c7f5-7174-3733-b124-8c96ca7819fe | -8.21459 | -55.03767 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 967ea334-8a08-3e8e-a387-3a7b7dbdc21f | -13.44385 | -43.84253 | 2026-08-19 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b8d08c80-5077-30e6-ab1f-0e242d4c269b | -9.40759 | -60.58762 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16d1a916-c69e-3e3a-a788-eb8f9026c753 | -11.16244 | -49.61999 | 2026-08-19 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b48f1792-4a3d-3f7f-8911-7ffb90814933 | -11.63629 | -54.5318 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffc5fd89-96d0-329f-9783-b9ce6f1fd3f4 | -8.54987 | -54.72456 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea69e175-9496-327b-88a7-153e12a80ce0 | -12.24846 | -43.16405 | 2026-08-19 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f73f45c4-1ba1-367d-b8e7-2a42063e3c79 | -12.83876 | -48.42001 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a65aee05-ad2a-3e38-8254-96a066d4d488 | -7.42829 | -59.78732 | 2026-08-19 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec1d639b-734d-353d-83b0-8ad2306d945f | -13.73016 | -51.87742 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b08ca4a6-c896-3802-8feb-ac18c3c2f45e | -13.45692 | -51.79117 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db5d1fc9-ff0f-3508-8652-b86f4461b233 | -14.24502 | -51.90489 | 2026-08-19 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d3c01b3-7323-305d-8347-6e8bfc55183f | -8.57717 | -54.77263 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f29d723a-0b69-3493-9711-5c1f7e2e97f6 | -14.21139 | -52.91013 | 2026-08-19 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b98c79c3-3833-340a-bd12-74b3d834a6c1 | -11.19301 | -54.81799 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f80204a1-fa8f-34ef-8192-b1827b313031 | -8.21537 | -55.03321 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2068036-c341-3459-ae60-3125223fb3b2 | -8.53472 | -54.75365 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1578b740-0090-3c3f-ad19-33cedddaf035 | -9.39589 | -60.5658 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d2032ab-62ad-3469-a565-1299f7b1e3c7 | -9.72912 | -46.78332 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4e9cb72-e2c9-39e7-9a0e-d92c74626af4 | -11.23565 | -55.06804 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1c057a2-09fe-359c-9d4f-8b8219a07261 | -8.52807 | -54.74662 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a9e6bfc-d066-3f5a-9e3f-f89f843d9f12 | -11.09484 | -49.91319 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d7b8a18-8cf1-3d72-94c6-e6ea17e0b73c | -11.24355 | -46.13966 | 2026-08-19 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7cc0cd6-7220-3164-a8be-6d46b625c6ec | -8.56571 | -54.73602 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 694d2a00-d256-3d9c-8617-d66a66e01a45 | -8.56583 | -54.68475 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dd7d65c-2342-3f93-bc62-74bd57769a51 | -8.5448 | -54.72797 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2f8e79c-4bfd-3a8e-a6e6-665d4b9fe107 | -10.8144 | -50.30018 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04cfe60f-b0ee-33e9-a706-de7789cf7820 | -12.52228 | -47.84241 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55b246f7-e00c-3377-adf1-5d95a733d610 | -9.73151 | -46.83737 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca43abd8-73e8-3023-9a11-8d2f9bba2fbf | -14.49106 | -45.67227 | 2026-08-19 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 370cdcd1-55b2-34d7-baea-2b04cebc37a1 | -13.45284 | -51.79443 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 002f43c9-072e-30bd-944a-c431c55c9afa | -8.50213 | -54.86556 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2b0b676-34d1-3785-9dad-d6c7483da765 | -11.24029 | -54.8252 | 2026-08-19 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3f61f10-b404-34de-9aef-8f3040eaf20e | -12.69822 | -48.51513 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63a403c0-9adf-3f8d-809a-e0babb9f2d9b | -8.58161 | -54.72172 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63fe1ed5-40a2-32a9-979a-ded4c7eb78bf | -15.77673 | -55.57248 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0b2fd92-5327-3645-b62c-c0c5db3221ee | -8.55112 | -54.76803 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c32b684c-973f-30fb-9cf1-370a94eac92b | -8.50649 | -54.86642 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f845cff9-9a76-330a-b305-7301b2042806 | -8.54048 | -54.74607 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bf5fcf6-9d4f-3268-afea-1e0c0ef6c776 | -8.57878 | -54.68708 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6060313-b024-37d7-a180-72bd07e84422 | -11.20408 | -54.0182 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 185947f7-b38b-353b-811c-425f568e0cba | -8.58585 | -54.77418 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d714cb0-5e9b-3cdc-903f-0a7a8c6cb414 | -9.45813 | -51.61045 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README45.md)
