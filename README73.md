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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8401265-b1ea-3b1e-b8ff-d17e34a5fe20 | -9.13169 | -65.85485 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ce7edd-ba7b-3b92-9ceb-571fde93c469 | -11.82415 | -51.54764 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adfafac3-e304-388c-be09-88673e23d342 | -11.93983 | -50.61606 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ecfacbf-8618-30cb-821a-b7575ddfa64d | -9.33899 | -55.22255 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58b43117-d5e8-3f7c-8c59-93de538df63d | -6.86014 | -52.81214 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fb59b51-7f09-3362-be8d-d626d6f5ae5d | -3.40647 | -59.58296 | 2025-09-02 05:31:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a587a31b-6328-3baf-b9d2-25686820f9a0 | -7.28397 | -60.65115 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6959377d-5073-319c-bce2-37395e7adfd5 | -8.05702 | -52.35365 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bfc5bcb-1bfa-3289-9514-d9433bccd3b6 | -6.8407 | -64.32806 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31831056-d98e-37c0-8001-e03599f0fb8d | -8.63665 | -62.60996 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edbb8ded-b8e0-3b88-898a-d3d824fd2d29 | -7.2834 | -60.65482 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e26830dc-1c80-3fd7-a752-72383af2e2a6 | -8.64643 | -67.24677 | 2025-09-02 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04d92866-9c22-3db8-a8fa-55cd1c6675eb | -7.55125 | -61.33644 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 539f0189-b1f4-321c-bea2-d9a24e76741b | -8.55292 | -63.00854 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f9e440d-b6ef-3097-9d2b-38cce667b3fe | -6.81524 | -52.81633 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f73d5a0-cab4-34fb-ab6a-ca6ffb39cb61 | -7.69708 | -50.27088 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ea3b3f4a-e6d9-3d52-b4e0-7378f3f3846c | -6.79156 | -52.82086 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b6c8965-5f78-3eab-ae35-c590add8e21e | -9.54602 | -65.94519 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2fb9b85-e88e-322d-9106-0ef2113325d0 | -8.68739 | -62.39624 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 115a3413-6060-3f56-8682-8297664ccb59 | -7.48147 | -63.82659 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d45108ab-d7ce-344e-8657-dee1462bf038 | -7.36361 | -61.65025 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d8cf946-be56-3820-b053-efe2f03db1c3 | -11.66379 | -52.22101 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5172a19f-299b-3ff3-a0eb-30b4fcfb4ba7 | -11.66755 | -52.22487 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2c888e54-bf8e-37dd-ad68-546c2332dbe1 | -7.07776 | -63.07516 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecf1b841-d12c-349d-b7f0-414605312ec3 | -11.66951 | -52.17172 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b8b01a87-48bb-3f04-a473-55772ea9ada1 | -9.8253 | -60.76864 | 2025-09-02 05:31:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3015fb64-c347-30d7-9635-4bf552e413c6 | -8.75494 | -62.41764 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d171638-e7e5-3e8e-9760-bbcdab2571a6 | -6.80888 | -52.82244 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eabcb273-c9f4-3910-88de-524eb6bbd4d2 | -6.7866 | -52.81678 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dea7d2df-395a-3ce4-a3bb-a3df58aeb002 | -11.65385 | -52.18663 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 599f4411-14e6-3f2f-83b5-0031b83f5e17 | -6.83796 | -52.81219 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 779b4d44-0c75-3f7b-93de-43e9eb36a8a9 | -11.67634 | -52.20336 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8b4c8b26-839e-35bf-9b38-d35cc4acc46c | -8.84923 | -50.57875 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dd3f933-eac6-39f3-a180-f6df9dd3ce87 | -5.32223 | -55.99816 | 2025-09-02 05:31:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeb23c58-731d-3fb4-aea3-6b2411a6262f | -7.2855 | -60.66596 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b422c0b-2297-3d17-b602-8d0c7f844c08 | -7.59311 | -61.63202 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee43bb0d-060b-3c6f-a4ae-0c978c038567 | -6.78117 | -52.81596 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a91dcbe-4b5a-3abc-a294-2261cf191326 | -6.80935 | -52.81895 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45218e9a-f8ee-39b1-a2a4-ffeecec67956 | -6.837 | -52.81923 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d43f81d4-7456-3432-96a6-4d3074c55fb6 | -6.80833 | -52.81977 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9c0d6b0-71f2-3c92-ba1e-68bd45d4ce6a | -7.58977 | -61.6315 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 843ee0d3-bd6f-3330-b09d-ebe3967343ad | -6.86298 | -52.79149 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f26cc7e-7722-3eeb-89d7-d7605bae4e4c | -11.84641 | -51.46835 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cb29cd0-486f-3941-8b75-893e4cb15f68 | -9.46172 | -60.3173 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f0ac07a-995b-34e5-8a3b-28f35503974d | -7.58752 | -61.62394 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c3eeffa-4a3e-3e43-b23c-552e8ef846e3 | -10.76096 | -49.58042 | 2025-09-02 05:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b709f0-eb9a-366d-bea6-37d7e8d85ef4 | -6.85233 | -52.82862 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2df15558-e9cd-3e5b-9533-d79d22103911 | -6.40004 | -58.20766 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d3fd454f-6fda-302a-9398-dff1a0018b01 | -6.85966 | -52.81564 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43be9562-acab-3f6e-8b51-4f42a7f20711 | -8.5123 | -63.91298 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e3715ab-ad8c-31a6-a590-4b10e1c7d016 | -6.43082 | -55.61628 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 614785e1-dcd7-3dee-9b5c-76b9d4cf91d7 | -7.67616 | -61.0963 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3912bf49-2adb-37dd-8bc6-a83068361adb | -9.40212 | -60.54599 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d25e6cd3-3886-3b51-bad9-fa26033db815 | -8.6361 | -62.61345 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bc6f488-f263-38fe-bf98-f0f63ba380ba | -8.66337 | -62.82901 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a812c7-c4a1-34c6-b29d-e8c0cf62e499 | -7.25635 | -57.54195 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfeb9a63-b3da-36f8-97f6-bf3be3620993 | -7.7185 | -50.25568 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2e0332d5-bd1d-35c4-8cba-4e26c7a6b899 | -9.21167 | -59.53279 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6564994-374f-33bd-8425-1d784d80e1be | -6.83252 | -52.81142 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d666d1-0ed7-3f30-b0e6-61fa4319d184 | -8.69184 | -62.41126 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 244ccdac-b258-359a-9fb9-0ded6bcd6600 | -6.77033 | -52.81427 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eea23a42-1a5d-3ba2-9773-e29ff5510527 | -8.65037 | -67.24745 | 2025-09-02 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76a4e354-2a83-3c34-b1a2-10f7e57ddfe8 | -7.09733 | -63.03852 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f5e2b22-7a96-35c8-98a3-2728441f1cd6 | -9.09091 | -58.88607 | 2025-09-02 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5578739c-8422-3309-b554-31857edc410b | -7.56696 | -63.85865 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e500cd-a505-3854-b754-119c6528bce9 | -6.83157 | -52.81224 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c435e93-25c8-38e5-99d4-33ed09d60769 | -11.66085 | -52.19348 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d7f0e197-7c39-34ee-aecb-0cfe441ebe5a | -6.84291 | -52.81651 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac65efe-c758-3eea-863f-40fa0808fea5 | -6.34411 | -58.16822 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f3d8c18-e7ef-3bcd-89c6-0ed549202be4 | -8.73785 | -62.42216 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 827119bf-e7a6-3249-84ab-f51869dd1744 | -10.27582 | -54.2593 | 2025-09-02 05:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f71517da-b137-3fb4-b6c7-495fb4e6d352 | -9.18364 | -67.77851 | 2025-09-02 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dc71088-ad17-3b14-9c8e-3468c8e4e326 | -8.73453 | -62.42163 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fddb4bc4-3c2c-3ce0-ad09-a1d4340350cf | -9.18179 | -59.45661 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2334d315-ddbd-3648-9c7d-ab01fb70c85c | -11.66293 | -52.17548 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2e3416f-511c-30ff-8b8a-5630c30206ce | -11.66452 | -52.16168 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3169ac27-293f-34f6-bfbe-2d0192f046ed | -8.72898 | -62.41359 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de209b3-1d23-3953-967f-7a2758a61520 | -11.85215 | -51.47416 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b30563f-e516-318a-918f-7720151c9d28 | -11.66483 | -52.21212 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 47ab5ff5-c51b-3532-950b-7fb0a08eaceb | -7.47866 | -63.8224 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c5e2427-420e-3c36-92b2-8081a81542c3 | -7.59979 | -61.63306 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28015839-abe7-3316-a097-6fbb409cbe24 | -8.64664 | -63.27215 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16bfc970-5b95-3e84-bff1-e212b6483ac2 | -6.74476 | -61.93488 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2582c112-10ee-3b45-a5ad-01f29872e523 | -6.81871 | -52.82469 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfd4f7c5-67ca-389c-af97-4d008b78d1a0 | -9.48787 | -62.18884 | 2025-09-02 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7837e411-b830-31e1-87d3-5428f4625d6d | -7.54679 | -61.34301 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6469944e-6155-35a3-8a47-aa6a46afe165 | -6.84881 | -52.81392 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3747b69-1bfc-3ecf-816e-a7fbf47d5883 | -11.679 | -52.19573 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5078dcf3-1791-3f63-a77b-70a67a8696f9 | -6.85917 | -52.81917 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b84ad51b-d2c7-3cca-a0f2-8e628f5cbf30 | -8.65948 | -62.83196 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 87bc9dd2-c95d-339b-8e99-a80a3a3f94e4 | -6.81883 | -52.83076 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db634469-246e-3b80-9b8b-06d75d9f2a3b | -7.70541 | -61.10822 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b87c4dd-8c68-3f8c-a493-f41670af6123 | -6.43351 | -55.61425 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8468be6-a641-320d-9659-73836081f656 | -9.4507 | -60.57697 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 024725d9-f845-3f01-9b11-5b0228971a0a | -6.81969 | -52.81781 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f65ba3b7-61b8-37af-93a7-fb32e54bad74 | -8.75771 | -62.42166 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aa16653-e093-3246-b2e8-812f09bfb4f1 | -8.6505 | -62.60859 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfc62e7a-abd8-381b-9509-f2603ca25982 | -9.20241 | -60.24716 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9151aed9-c0aa-3125-9643-8c4a11ded6a2 | -8.97789 | -65.97009 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d82260-227c-3dc6-a8ee-dea1e46e5fce | -11.66899 | -52.17624 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README74.md)
