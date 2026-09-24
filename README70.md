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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51b364bd-dd6b-33f9-be17-f2969c722f82 | -3.70426 | -54.18854 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50f26316-5dbd-367b-bcd5-acd16698f2f4 | -3.79215 | -52.42593 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 730b5ae6-f973-36b4-924e-84b52a674ca7 | -5.0003 | -45.5494 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d13235b0-d2ff-3bb4-a9a6-5e53ae4527bd | -6.77639 | -42.36867 | 2026-09-24 05:04:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c8892c50-e75d-3ab8-91f2-87caccea57a6 | -1.83158 | -55.72233 | 2026-09-24 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 75151213-750b-33e0-9f15-a7d0fa05b00c | -3.62738 | -58.92861 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fecbdfc6-e113-3986-8bca-94f3329bb9ee | -3.16977 | -51.36262 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 498123ec-ff63-3a73-b4cc-8d34cda5f3f9 | -10.07909 | -46.01511 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14784bcc-a051-3d7b-83ce-5f04652d67ba | -6.25376 | -55.48147 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a993a373-7401-3d7e-9f7b-1d3639d8725e | -9.58985 | -47.7742 | 2026-09-24 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5e4dc86-3546-364f-a776-9fbea1b1c5e4 | -6.16327 | -57.70616 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48eca7a8-1438-3a8f-adea-bb17ffc3e8f9 | -6.6841 | -58.55796 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7843b6bc-bc54-31af-887c-3b8aa59e50af | -5.84319 | -57.62401 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5b554ab-695f-3010-9adf-ed67e32d2661 | -6.69366 | -58.45514 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60b9bd9a-12c0-36c1-a248-a79fb4ca7b71 | -3.62796 | -58.92502 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 255b7b0a-926e-3811-85e9-7f1c72f98e50 | -5.77473 | -45.09538 | 2026-09-24 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8d1a1137-ff81-362a-b351-1e5ed01049b0 | -3.493 | -54.68216 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2c31dd2-4a85-30da-9c57-4c52e589c8d7 | -2.88556 | -54.08044 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 972485f3-262a-3a2c-acbe-0e2a138db162 | -8.12937 | -54.81921 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73f112d0-bcba-3982-9fa7-33de26b63317 | -2.71429 | -57.51006 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d24fafe-4fc2-3ea5-88fe-2d405fc11e9d | -9.24925 | -47.34649 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 526d81eb-9663-3d6f-b42d-5416ae7c1859 | -9.25968 | -47.34232 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f304d04-cbee-3db6-afa2-ab469bd85af8 | -2.88116 | -54.08683 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e0c8378-fcb6-3023-a279-70a373ce1f5d | -3.48463 | -59.19198 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a51ec6dc-57af-3c8a-8ce9-b7ab27cd7ef8 | -8.93573 | -45.94245 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3282e2ee-d7ef-3e9c-b7a4-75e7476897cc | -8.59296 | -54.61541 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 851c80cf-bf54-3a68-b1e6-c8782472971d | -9.25917 | -46.23989 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6003543a-8f18-3b7b-92ac-ef23934f65ac | -6.16409 | -57.72375 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88964246-5cc7-3360-bf7e-9ac6ad6b5ad9 | -6.26547 | -43.27188 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0784d51d-1b80-3b95-907e-ef62b43affbb | -6.64874 | -59.93098 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c16665b-62d9-31e0-95db-c882198d3055 | -2.43228 | -56.55476 | 2026-09-24 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1547dfa2-aa36-3e65-96c8-ca02b2205867 | -2.71003 | -57.51172 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e58aa18c-e2e2-3d01-ae05-eca670eb2e1e | -3.83115 | -48.99998 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 629f939c-dabc-340e-b3e1-98c2253bc6ef | -7.42248 | -47.35743 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13b0d015-13ef-36d8-be9d-d5ea2fd82607 | -6.10239 | -59.87943 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7447f5e3-3577-3e46-9f3c-4ba79ff80823 | -6.60798 | -59.91997 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57ba2879-0302-3889-9e97-f74d60716f2e | -6.62039 | -59.92215 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 027021da-9a8f-3bf7-a12c-f1003c03d282 | -3.69108 | -60.54993 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 40d47518-f7a0-318b-a96b-34b64276205c | -6.03924 | -53.2746 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c1e0c9-5910-329c-a432-3e3fede93cfe | -6.68224 | -55.0537 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 134ed2d8-7b40-3c0e-8e4f-070bca835580 | -7.46194 | -55.00032 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ed2aa65-d2cc-3d2f-ade7-32df49bcb2ef | -8.42826 | -47.45674 | 2026-09-24 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dcb71789-3328-3381-bb3e-2d0d44122863 | -6.44997 | -59.95931 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d642eae0-b997-3f10-a561-bfc8655c051e | -3.03529 | -50.43623 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12051baf-008a-3f31-bc83-4e631f010e8c | -9.25836 | -47.34374 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f53256b0-8b81-38fd-bf31-4b4a8b4fb6a8 | -2.96136 | -54.16003 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb117c76-5f96-3201-ad3f-23089a33b58f | -3.44008 | -59.20383 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd2d4b30-e6b3-3fde-a4af-391db67ab936 | -2.97944 | -54.02487 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0442b096-4ed3-3724-a8b4-1f65b1ab6416 | -6.40685 | -46.20277 | 2026-09-24 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ab22b91-99ee-3862-9845-dd3bd60648a2 | -4.53397 | -54.9332 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01eb493c-0199-3aea-a277-05f4b02aa683 | -3.81786 | -58.88664 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97a165f3-1207-3442-90f0-ac7e7917363f | -9.24442 | -47.34586 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ed22e99-9a11-3173-84a3-4115cc5c1ec1 | -3.06814 | -54.40738 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 607d53e1-183c-379e-b92e-a3c73dd01a61 | -4.99422 | -45.55498 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 160e72e3-3ce7-34db-95fe-9672344dd61e | -3.42291 | -54.01369 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d90df4a-0289-3416-88ba-257fce831827 | -8.08743 | -54.76272 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ae15c4-fa17-3b6f-a171-5dc22c811c01 | -4.47332 | -54.97038 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c017542-3273-32e0-b56c-24d07d702c33 | -3.21888 | -53.41327 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aef59fe8-a7b5-3494-804e-2c13e3a3a3aa | -3.32645 | -59.80855 | 2026-09-24 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be7bb242-523f-3b05-bc80-45c77db62483 | -2.64196 | -54.69246 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a88941e-1cc2-3faf-bf62-7caca88928a7 | -6.89478 | -55.5736 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6ff49d-bd32-39f9-af67-0fd527a28420 | -8.26189 | -54.77665 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24d399c6-f0ac-3217-a267-d1f56c24d8cf | -8.26134 | -54.78012 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b082d8bb-24a6-328c-b766-0d6bf253710b | -6.26662 | -43.27288 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2456238-1b35-3f59-8084-cd8d77d9fab5 | -5.59738 | -60.20545 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd9320c3-6bb7-3932-a7c6-e9d33cb0888e | -6.6978 | -59.95436 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc495a6-92b2-32f9-83ad-6e9927dfd02d | -3.45301 | -50.08851 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f83cc373-e944-3145-b057-5a2d269cdcac | -2.70977 | -57.51402 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae546151-4403-3475-a1b8-0618b912b0f1 | -6.66511 | -58.55484 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7deed8e-c450-3e03-8440-6cab86a8823d | -5.57236 | -42.73199 | 2026-09-24 05:04:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| efdcf338-655f-3ae6-bcb9-f63e1690c30b | -3.21161 | -53.37339 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72076929-935a-3aed-8d24-691de00ac114 | -3.68201 | -60.57667 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c3ffcaa-4ea8-3464-a73e-88f161acdfac | -2.88502 | -54.08389 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7174e16c-0986-39a8-8e21-7b80f1bcdca6 | -3.29156 | -57.91332 | 2026-09-24 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76c371d6-6f20-3cd4-881f-08a03535f5a8 | -5.83684 | -53.85104 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1fea274-9188-36cb-801b-7cb2d31a9f35 | -8.27511 | -54.7574 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff0c3cd-72bb-3556-bd85-ac4533febc72 | -6.64657 | -59.92986 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9083cdfb-84ef-3b52-a5c1-b494de663896 | -3.00613 | -54.1777 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 270d8b91-9e39-39e2-9a34-c7f369f81b74 | -6.03979 | -53.27108 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2a2d13f5-5395-3d92-8ffb-3a1d4b918414 | -5.8352 | -53.86142 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea7fb19b-f27e-3fe2-ba02-b528d8a7daa3 | -7.19072 | -47.45493 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40164ce9-9bc0-3a6e-a8f7-8cd24fb93e74 | -8.25621 | -54.7683 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22826475-e3b1-3acd-928c-64aee7f0f860 | -2.89663 | -54.09634 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3844ec36-7c9a-34f8-ba28-08efd75a03d8 | -3.16267 | -54.605 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29a313f1-5ba1-3430-a001-e0447f80b5f3 | -6.43267 | -59.96029 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e976cacb-cb14-38c0-a524-37b50291af96 | -3.4449 | -50.09182 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d62008f6-e3c6-3319-a478-4bdffb08135c | -6.10655 | -59.88015 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aac0f19-f641-3971-84ea-162b58ad7829 | -6.04076 | -57.76676 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b3bac90-040d-3a01-925c-cf21f2a0dd3b | -7.48788 | -54.96533 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccd922c7-0de7-3cec-95b8-c0463b317229 | -6.10455 | -57.67619 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ffe2191-b963-3df3-bb51-3be462854548 | -9.14641 | -49.95907 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1a17447-bb47-344c-b4c9-2288bf755ac4 | -6.06803 | -57.80662 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9459b77f-2d97-3b85-818b-48358ab232fe | -3.7352 | -51.28451 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b4186d6-325f-3da4-a525-4b290134611f | -3.44769 | -51.67022 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95d9b958-d90b-34ab-a517-17b636cd773d | -3.78356 | -60.75872 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57b0df0e-05af-3b38-8c25-29a237f72bc1 | -9.25276 | -46.2481 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8916f613-7d86-3ff1-9f23-7517572e198b | -6.20624 | -53.57423 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ea90448-b3ff-3400-9736-1b80e20ebe1c | -6.67255 | -50.94992 | 2026-09-24 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65ad2e36-24b7-38fa-bf1a-e4ee823a0b47 | -6.46029 | -54.99658 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e9e34b1-e62a-3806-9a9d-912d9a9c19d2 | -1.16126 | -54.20014 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README71.md)
