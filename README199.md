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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d90d77a-1b78-3f0e-b3b3-213b66a3447d | -4.52099 | -54.98853 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee39b270-ae4c-39e2-8bcf-b58bd09cb805 | -3.34538 | -50.41806 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1a280b93-e358-3a0d-8720-c399e329df71 | -2.78551 | -51.67221 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fe01cef-b5a8-33f6-8795-d4d937385762 | -6.84822 | -59.40014 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64787a08-9261-35c6-9fe2-61080fb2cd8b | -2.73899 | -54.1146 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aef6933-5203-3f37-8fee-04e34165a98d | -3.30078 | -54.06086 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dc3b98f-3379-367a-8a1d-f59c1795db15 | -3.31534 | -57.48688 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af9f5636-3f73-3e91-b0f0-534f0369cfd4 | -3.19412 | -60.43864 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4c0dd9a-b15a-34bf-a68d-0a69e6903916 | -3.53818 | -59.40376 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ce2c602f-ea06-31d2-9afb-9291d0bf8c23 | -2.89964 | -57.2137 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 178bfe89-6abc-3c6b-9dfe-1df5447dd2bd | -2.88051 | -56.66494 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2632395f-9c41-3c11-90a9-7e54e28b3c51 | -2.88572 | -59.23247 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b8d28d-1056-31bb-8248-56f00ba9c33f | -2.57579 | -56.17402 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 348852d6-64c9-3948-96b5-9c048a590bc2 | -3.25236 | -54.66849 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 718da8f3-88dd-3d5c-aabc-a4bc8f74275c | -3.54775 | -54.69007 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 147408a1-3bb9-3f90-8d46-92fba634402c | -2.33596 | -48.8622 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde91e7c-3523-3f3b-a1de-bda5c3535e08 | -3.45047 | -59.55191 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dfe0c88-8a05-3da2-9900-7025c0fd9ef6 | -3.39771 | -57.99828 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 489d1f9f-11dd-3319-ba09-1147062f027b | -2.48057 | -56.17459 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77ea9b8c-81e3-3731-b572-b2c1b8deb461 | -3.08112 | -54.25597 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4323eea7-2921-3d4d-b54d-c9cd39b93800 | -2.22754 | -58.11333 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34c62235-d5b9-3310-a1e1-8c5316e14e67 | -2.56499 | -56.15313 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74825d4f-71d1-36f1-be77-b65653a60901 | -3.50643 | -60.21834 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d825cb63-b4db-37fc-b570-d0e1d798b8df | -3.70882 | -57.10227 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c55dbe93-d1f2-3e0f-b010-7b0545c200cb | -3.35877 | -59.42244 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef997e7-f89e-3f94-9260-2c31d08b1534 | -3.65119 | -59.71405 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bff8885-cac5-3ea2-b5a3-153222381d22 | -3.89577 | -59.44293 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2055ec45-ef51-3491-9b84-9aba249d4c63 | -1.21104 | -55.64933 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b61e9b8d-aed6-3d54-9f94-8aa9252a8350 | -4.82175 | -45.83105 | 2026-10-09 05:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28f24146-cec2-3b9f-bd95-627f56abb1ce | -3.82462 | -55.97535 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80e0d191-354e-30eb-9c50-e7749ae3e83b | -2.7985 | -54.08511 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c07c8dbf-0d11-3deb-a3a8-b7a41fd97927 | -2.51241 | -56.26349 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac05bcaa-05df-38bf-b6c3-3a54a6aed1eb | -2.87845 | -57.67204 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28889312-8ae2-38e4-82d6-6caf50a6b944 | -3.69569 | -60.54706 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caf29942-13b7-3fc7-b11c-0393e2ef1bce | -3.44515 | -56.48356 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db5a110-bce7-3bff-835b-b1641ce06185 | -3.44211 | -59.56142 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad6a4176-2a15-39e9-845c-421600dbfef8 | -8.49136 | -54.63629 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70ef9587-dd9d-3ffc-b13d-cdd00d2607db | -9.29956 | -60.54196 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 170e401d-11d7-3af1-8d9b-71f4b12af701 | -3.26985 | -54.05613 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efb31084-81fd-3006-bcc4-e8880862378e | -3.93251 | -56.02671 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1c87dc5-f8e4-3c15-9bde-7ce09b761520 | -3.11707 | -60.67764 | 2026-10-09 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10da9042-d4cc-32e7-a942-72b60bd3ae24 | -4.28053 | -49.08921 | 2026-10-09 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdf52ec6-c7ba-3df4-917a-3b887b70bdc9 | -3.10788 | -53.93308 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78affbb7-4f34-348b-9031-3dbbdfbd07f9 | -3.42412 | -57.95995 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90ffa4e0-26a3-3746-b499-fce1b689d7a4 | -3.66408 | -60.63421 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9de12253-7de8-362a-96ff-d30ba1d0d4f9 | -11.11417 | -47.79666 | 2026-10-09 05:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4a835df-d470-3c72-a5aa-c47051f9c1ff | -3.72662 | -59.69335 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f8ed85c-03f9-339b-b1d4-21d64062f3c9 | -2.80424 | -60.08985 | 2026-10-09 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d113f7f-8206-3032-83b3-686b43ed1503 | -3.0123 | -54.05468 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1fcf839-0a9f-33b2-a360-c8d2bec536df | -2.33491 | -48.86914 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dea248c5-db78-385f-8c5b-4df2a7c7814f | -5.0908 | -46.22147 | 2026-10-09 05:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a827d421-431f-3cc4-9e33-637d9488c254 | -2.7507 | -54.03897 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d9c5a81-669b-387a-bc69-244e7b8fe25a | -3.02186 | -54.10709 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c54a93d-ec89-38bd-a49e-5456b0407a7e | -6.08725 | -62.51307 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 033bccdc-cd2c-3446-a8e5-2acaf5ec19e3 | -9.25859 | -60.8804 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 462c0f2c-63f7-3f8c-95ca-d3be4ffc5c91 | -3.00551 | -54.08514 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ee55060-e545-3fa3-a8af-2383c21111d4 | -1.74264 | -57.18423 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88a61b6a-3dc5-381b-81f8-bc10b4850ce2 | -3.1661 | -50.45017 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 33b0c7de-3db2-3bb0-9f22-3b501860610c | -2.39639 | -51.30254 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5504d002-2a2a-3102-b8f5-aa923791e752 | -2.58329 | -56.19028 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b58262b9-63e6-388a-a7b1-e5087681f97d | -1.89223 | -54.67715 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbdc5aa0-607f-33bd-ab27-3863a1e7a4d6 | -3.60022 | -60.57418 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4d6c591-a5c6-3de5-bc0c-f7a590b3144c | -3.18471 | -50.59296 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f7de4dd2-94af-300c-b5c3-c85e720363c0 | -6.67783 | -63.02569 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0274b210-91cd-38a6-9cf1-732bb520d4c6 | -2.50353 | -56.16286 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19d1330d-51c2-31a4-ad5e-d2f5ae3431cb | -3.30279 | -53.7073 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22964511-6429-3705-a9e6-6cce2c821cc8 | -3.49047 | -59.29956 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 009f9429-2129-32f2-8e28-b606fe4273fe | -3.26486 | -54.01085 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10e5e564-35d3-3a96-8be5-d6f38b82fa80 | -3.28143 | -57.85222 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef7b42f7-3743-324f-a403-4fc14922f0f7 | -3.04149 | -54.15858 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e48c4f8-42b3-3572-9c34-d16182c73c98 | -3.00112 | -57.75546 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cbccb938-a4ab-3735-91c9-42ad3fbb7be3 | -3.53557 | -54.67 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 362c2077-7c9d-3c64-a669-09fc531bd23c | -3.71552 | -59.65536 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 263b620c-2559-34b8-a241-e82353224013 | -2.47118 | -57.92656 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7030a1c8-2162-394f-b3f3-96264dc09e0f | -3.39046 | -50.2182 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62447a21-3f6d-36bf-b382-c00e414f04b8 | -2.50604 | -58.07276 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d65f4a73-78e5-3afd-8bd3-3945a61d872e | -3.10956 | -54.16597 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d61db82-dec5-32a4-890e-2fecb5c22e87 | -3.39291 | -61.08076 | 2026-10-09 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52cc0a56-e1e6-38d8-8967-69ea14f866a5 | -7.08871 | -59.76912 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 253c24da-a865-3450-859a-0b0ba41497b0 | -3.49824 | -54.61351 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20574797-8973-3171-949a-ebcaac7f156d | -2.49321 | -56.16122 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9da7ba2a-4b21-3fee-95e4-d8b272bbaa9e | -11.66668 | -46.77721 | 2026-10-09 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 638ae4f5-656f-3ea1-935b-fd6280ac28af | -3.8292 | -59.4109 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1fed4e4-330a-371b-b5f3-b6a6c90a2fd3 | -3.82737 | -57.17147 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc19fab-630e-321f-bdb2-0a38db072efb | -3.16444 | -50.46132 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7841c946-9ebb-307f-8295-42c8b856a83b | -8.17896 | -54.7226 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03d23836-6db1-3e7a-87f1-51d0475063fc | -2.57461 | -56.18148 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23b1c96d-785e-30fb-bf39-ccada5ef2ded | -3.30291 | -54.02148 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba91ee54-92d3-3bef-b504-c5bb224e37ab | -11.39676 | -46.67984 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e654ae5-ee44-34d6-b3a4-61fd35ddb69a | -3.45469 | -57.48702 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77905b3c-d1dd-33a5-986e-ffed2ca93ac9 | -1.53571 | -54.53949 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a1ac86b-4124-3364-a1e6-8e2889f4eb11 | -3.45808 | -50.58937 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3b01e4c5-b5c4-3ce2-9cd8-2bd4332d96d4 | -1.3876 | -55.19595 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3de71da-9519-3e1b-892d-88023cfc0d88 | -3.07155 | -53.96251 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40894c54-3110-3f23-b944-f646b33ef251 | -3.17495 | -50.59148 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 248d76d9-bd30-3480-ae9e-d764702f21ed | -3.90194 | -55.89481 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2682775f-3952-3786-9af6-f8b8772d97f6 | -3.54846 | -54.68557 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 789d52fb-51b3-3c1e-a4ae-18d632db9177 | -8.70859 | -62.39547 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd9d68d2-73a2-38a1-a962-ae008de5b516 | -3.29707 | -54.08484 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35ee4188-74a6-373f-9f95-d33bb575eaa7 | -1.11147 | -54.16959 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README200.md)
