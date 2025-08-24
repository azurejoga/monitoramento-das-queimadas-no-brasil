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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff4ef76a-5192-3696-9f8b-fa2464a61d9a | -9.0151 | -65.724998 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d46647d-5d46-394e-8e17-7da730589d3b | -9.1443 | -59.510101 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 727fb503-a20b-36a7-9389-8bda212098cd | -9.1225 | -60.784599 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d81d0c24-bd33-30c2-9650-56aa5d431824 | -8.5694 | -68.158401 | 2025-08-24 02:14:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 599f9bde-54cb-317f-8227-b7c0fd251cce | -9.007 | -65.397797 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67530686-0400-327b-a83b-d81fa59f46a9 | -8.8983 | -62.419399 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4cdb07c6-1742-3528-b2f4-3a67acea32cd | -8.6091 | -62.617401 | 2025-08-24 02:14:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70c187a1-d083-33f9-a01d-481ff2679feb | -9.0054 | -65.727402 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d3f6d9d-07ef-3fe0-afe8-eb5de34a73e8 | -8.8886 | -62.421902 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd92e21f-f22c-3150-adfc-369628a51b15 | -7.5298 | -63.849899 | 2025-08-24 02:14:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 511bb6e1-4c0e-399e-a9c2-a353c8f4b8c9 | -8.8936 | -62.441399 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 47981253-293f-3fae-a184-48930a24a1c3 | -9.0541 | -65.715401 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc2aa3a-0e55-34b4-934e-168cce15996d | -8.5945 | -62.6007 | 2025-08-24 02:14:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 259718f0-90e2-32dc-a39b-50be35dcc9d5 | -9.6202 | -63.1068 | 2025-08-24 02:14:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab8bff5-afcc-36d1-8b0f-371554339766 | -8.8789 | -62.4244 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a7b1820-62dd-374c-99e5-e0aa18f2d196 | -9.1265 | -59.482201 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12175cee-05f5-30bd-a1fb-0971efde4e7f | -8.9912 | -65.375702 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2262f83-a85f-3d87-bf64-4bab7e162819 | -8.9957 | -65.729698 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce2a7c32-9a13-3ea2-9bcc-898ce538add3 | -5.4072 | -60.158798 | 2025-08-24 02:14:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88a5f18e-2ab3-3728-bf9b-68f4d6c8233d | -8.9996 | -65.704002 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf6a1a01-4f14-385d-a949-cf987f499c3b | -9.1321 | -60.782001 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da325d7e-3d85-32fc-b03f-619e83bc01cb | -8.9973 | -65.4002 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39464491-480b-3d9a-ab55-f46645c2bf7a | -5.4058 | -60.1931 | 2025-08-24 02:14:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26dd15c8-d00f-35cd-96b6-94dbea566d13 | -9.0065 | -65.689903 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0ae1feb-1115-3dd3-927e-66ccb4633d78 | -9.1802 | -60.769199 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ce83cb6-8734-37a3-ae03-cd73f5f91d67 | -9.1279 | -59.448898 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1da4dc38-1edc-341a-9bb9-0c3cbad015e7 | -8.9033 | -62.4389 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e81b4c5-c025-31c2-981f-18f8311d7d38 | -9.0277 | -65.7342 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 946ab41f-bd6e-372e-b3c0-6888e52a82aa | -8.8889 | -62.463299 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be32f95e-f802-3b41-9c4a-6c9e92d77860 | -8.5848 | -62.603199 | 2025-08-24 02:14:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83a6b1de-c603-33c8-aa77-8947dde5263a | -5.4249 | -60.188202 | 2025-08-24 02:14:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d28214f0-b05e-3849-bace-4f87b5601951 | -9.1456 | -59.477001 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59594267-f96d-36c9-99f1-2e869618d490 | -9.1552 | -59.474499 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d469306d-fd1a-3eec-92ff-3e206cbf55b0 | -8.6139 | -62.636398 | 2025-08-24 02:14:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 720e0ed7-5ba7-36e2-b071-f5aa21879daa | -9.0249 | -65.722603 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5fc6348-a078-3310-b81a-f75839235292 | -8.8095 | -69.396004 | 2025-08-24 02:14:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0e6302-0f09-3e83-ad18-13444b3910ba | -8.9899 | -65.706398 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fda53076-8cbd-3f68-a95d-6e2809252ce5 | -5.4153 | -60.190601 | 2025-08-24 02:14:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b818a2fd-1b97-3ad4-b778-d8619559fbb9 | -9.1933 | -60.819 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6ed22e-a982-385b-b080-282319199379 | -8.9968 | -65.692299 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5e325bb-40a7-3f26-8a30-52e2a1801439 | -9.057 | -65.726997 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d897b23-5553-3842-9083-4f6402ea0010 | -9.1361 | -59.479599 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c430d84c-c84f-3e9c-b5bb-e249f30d6581 | -9.0025 | -65.715698 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3c4eb7f-d320-35af-84a5-2d72e1e5be85 | -9.0472 | -65.729401 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0d36b41-8e9f-39aa-9a87-3641c1632d26 | -9.1867 | -60.794201 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b254fa9-fc1b-3e15-b773-ec8bc630e6b9 | -9.0443 | -65.717796 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d990b3cf-8b83-321f-9461-dfae9cbd9d92 | -9.0346 | -65.7202 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8882b4de-d725-39bd-87ed-7bcdb5f751c9 | -8.5994 | -62.6199 | 2025-08-24 02:14:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad8c49d5-132f-3bc3-b6bf-fb70a42aa0c5 | -8.5896 | -62.581501 | 2025-08-24 02:14:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 903b84b5-851d-3d63-9bb0-8d406024b123 | -8.8986 | -62.4608 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 809a235f-fe52-3786-8beb-5420eb737bbf | -9.0094 | -65.701599 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a2fe6ce-8a48-316d-9245-c14f9f4b32e8 | -8.6661 | -62.881699 | 2025-08-24 02:14:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 33a6ca3c-7d93-3d6d-a3c3-187b886d6678 | -9.1159 | -60.759499 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74650a09-897c-3c36-9b04-bed0ecc0666c | -7.5339 | -63.866199 | 2025-08-24 02:14:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9196ff2-a758-3781-954b-5cb7ed72e2ba | -9.0122 | -65.713303 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d98779ec-0c5a-38a7-9426-230add2bc9b4 | -9.1347 | -59.512699 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee16d53c-d263-38f4-9fa1-73c1101976c2 | -9.1374 | -59.446301 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 041ff18c-a531-3214-907a-bbac3c43c2aa | -7.5436 | -63.8638 | 2025-08-24 02:14:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad0600e-502a-306b-818b-a3b406873eaf | -16.7965 | -51.3637 | 2025-08-24 02:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8992cdc5-2e9c-3412-b821-796f9b6a67a8 | -20.3594 | -51.7023 | 2025-08-24 02:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 4b847d10-6a50-3f78-bbbc-9510a78f3586 | -20.3396 | -51.6839 | 2025-08-24 02:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 4fbe7d75-64db-3f50-8d6b-2667faa5bb60 | -17.6176 | -44.298 | 2025-08-24 02:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 2837c7fd-ad8d-3665-a4c7-4418f46f7419 | -9.0416 | -65.7163 | 2025-08-24 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b4243133-a3c7-3bec-a23c-27d6ff0b9610 | -9.1721 | -59.4823 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 9037efdb-8b6f-31ea-aeae-eaa6e5754ed6 | -10.8078 | -46.4083 | 2025-08-24 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| ed4a6145-cd67-3db8-825a-ba4df5a64914 | -9.1536 | -59.464 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 159.7 |
| cca75f16-b952-3ac1-869a-162f6a733adb | -9.1998 | -60.793 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0621df49-4cb2-36bc-8af6-8cced7343937 | -9.0231 | -65.7169 | 2025-08-24 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 643f3d53-6dbb-3c75-b13f-bf6bb65794f3 | -9.1533 | -59.5027 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 302989dc-4235-3b77-9f67-ac6287c16828 | -8.6131 | -62.5929 | 2025-08-24 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| fa808efe-037b-3bc2-b834-9021801bcc20 | -9.0232 | -65.6982 | 2025-08-24 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| d6792792-fce6-37ee-81ad-bbe01cac6486 | -9.1441 | -60.7765 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1ab614b8-d16d-3386-a9e4-ce0cec7f5b34 | -5.4364 | -60.1779 | 2025-08-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8aef7320-eeea-33fe-8356-3d0096bb535e | -23.8479 | -47.5793 | 2025-08-24 02:20:00 | GOES-19 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.9 |
| ef71f297-15b8-3ec9-a872-1ee0648b59d5 | -14.8153 | -47.9343 | 2025-08-24 02:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3ac0c8d2-f11c-382d-abf9-ec0da9cf4558 | -16.797 | -51.3419 | 2025-08-24 02:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 03d074a5-74f5-3d05-bf35-80803a1de49e | -20.339 | -51.7062 | 2025-08-24 02:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 87.3 |
| fc37d7cd-d279-360c-9a03-2880c5dfaa80 | -17.6183 | -44.2738 | 2025-08-24 02:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 26b3c058-38c6-3d33-819c-84ae15ab8a8f | -4.9605 | -55.8226 | 2025-08-24 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2e5c5408-1a56-3b1a-98d4-1e35f990fce3 | -9.1722 | -59.4629 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| e9d075ac-21d0-340a-8244-f804aa01827e | -7.9225 | -45.9193 | 2025-08-24 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 84a737d5-c67d-30f1-b2bc-54e6f9c9b988 | -20.3599 | -51.68 | 2025-08-24 02:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 0f0d7a64-ee04-3241-86b5-a3e6cb7b7ea4 | -10.6131 | -44.3051 | 2025-08-24 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 6920b55e-9942-32a0-ae73-48a8b4f350ff | -17.5975 | -44.3027 | 2025-08-24 02:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2a2deb5c-f99c-3f9d-ae9c-f22b42cd9fd5 | -14.7958 | -47.9375 | 2025-08-24 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 181dd25f-487a-37ed-a5ee-b33f34afef77 | -5.4182 | -60.1593 | 2025-08-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| bd42e10d-c32d-39de-bf28-1d277c9a5050 | -9.1538 | -59.4446 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b7b27b4d-f1d2-3223-819e-36de7b04d9df | -10.6128 | -44.3284 | 2025-08-24 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9770a766-6e46-328f-9b56-509fd027cd68 | -9.0046 | -65.6988 | 2025-08-24 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e2fdffe3-b038-3705-8e5b-09c645ca0d9c | -5.4181 | -60.1784 | 2025-08-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 526a2c75-039b-35c6-af96-0636ceacc564 | -9.1535 | -59.4834 | 2025-08-24 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 3f2ca9f3-23fb-3eb0-ad8f-6b331b9ee395 | -9.1721 | -59.4823 | 2025-08-24 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 14aa3478-d459-34dc-9a05-709727062356 | -20.339 | -51.7062 | 2025-08-24 02:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 83c724fa-76df-3de2-b7ea-5cd818be0136 | -20.3594 | -51.7023 | 2025-08-24 02:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 9c857942-34a8-3c2c-9d23-d12190933163 | -23.8479 | -47.5793 | 2025-08-24 02:30:00 | GOES-19 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| cbfaa4a9-304e-351f-b790-e3d7e1c38f83 | -5.8692 | -52.0868 | 2025-08-24 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3cdfe11f-33a2-3099-975e-5f2453ba2d63 | -9.1538 | -59.4446 | 2025-08-24 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ef602542-a8a0-3220-b612-a847ad0de1c1 | -5.8507 | -52.0878 | 2025-08-24 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7dd6d2ef-3659-3722-9809-5bb776387572 | -16.7772 | -51.3451 | 2025-08-24 02:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 0df5e7dc-38c5-35b6-a444-a3d8b1a8c955 | -5.4181 | -60.1784 | 2025-08-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |


[Clique aqui para ver as próximas entradas](README19.md)
