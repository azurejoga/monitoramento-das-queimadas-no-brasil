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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c408cd77-097d-3730-b21b-b2ae00dd160e | -8.0556 | -49.67612 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39db9bda-f50b-3afe-9397-0226e1df5719 | -9.20033 | -59.46903 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff9060d7-ad7a-34ff-898e-e42c904f003b | -11.61211 | -46.23941 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 464725d5-3b7d-3093-861d-ad8654827493 | -9.61637 | -55.35572 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7ed4ec7-2548-3815-ab97-d17a97ea9877 | -13.63281 | -48.16257 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cb1c38b-86b7-364f-a27d-8269f4990286 | -10.71702 | -47.12393 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fb3382f-9799-350d-9f8b-0bfc7eac1fc0 | -13.49988 | -46.89126 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 890b8d1a-36fd-3672-9555-909f8407343b | -8.92148 | -62.43695 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1e786f1-13a2-3ee8-b552-ef159846562d | -8.22106 | -49.56707 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4021d67-f0b7-3dbd-847d-cbb0f7be66d1 | -13.65511 | -47.98405 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8eebb60-9e00-3835-a4d8-de36efb878a4 | -12.74883 | -48.13377 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbffd507-33a5-3cfe-8037-0b80f4ce64d9 | -9.7089 | -54.98372 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f19a8e75-e6bf-3359-b0d7-9127f5d5046a | -8.86539 | -52.04315 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 448cbe59-6cdc-3ac3-a0ec-02406f7247a0 | -9.49446 | -58.93714 | 2025-08-25 04:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dd318d8-f653-3ae0-b162-3f87ae78caa0 | -8.90398 | -62.42189 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47d8e3aa-80bc-305e-bb08-1b9d40ed7194 | -11.18165 | -55.02472 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 257b3a46-9d88-3580-815f-ecb3d8764122 | -9.18077 | -60.79087 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fb5a3785-0bd3-3645-bfe4-b081dd8523d7 | -12.68521 | -47.83148 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cac9b0bb-b0df-39c4-95a6-53501505ca3c | -10.23984 | -59.66553 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23e6e4b1-8658-3cd8-b23b-fd8e72cdac82 | -6.82694 | -58.9566 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ba8af1b-7cbe-3e6e-8fa2-3c5c9e3ef7c2 | -9.1721 | -60.81956 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| affa30c6-110f-3c85-b168-41b8e786287e | -11.05032 | -49.12269 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f053693-c7e3-3eb8-b66f-4f896204c186 | -8.60156 | -62.5953 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9600503f-2848-3c69-98ad-d50676bc972b | -9.15743 | -59.48276 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 277977b9-7b8f-30f7-8292-23cee191a274 | -8.57845 | -62.626 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3998d18-2d94-3e2a-b4e2-b4f89d8ff0be | -9.15002 | -59.49236 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd6c59bc-5ab3-3dc8-94b1-737bb2207486 | -9.52145 | -60.50979 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1af9277c-a260-3f13-98cd-773f2d041b1b | -11.92548 | -46.74043 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d88e733-9049-379b-9b98-19e69f9a2806 | -12.73294 | -48.11876 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d7ff211-fa47-31a6-bfcf-359ab8ea183c | -9.14394 | -60.77331 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 254af70f-15b6-3644-ad05-7db9cfecd82b | -9.25808 | -59.76943 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfdc8bb6-db2a-3ac7-b1d7-20c9f5e3b63f | -9.71289 | -54.98442 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1dd2298-a9a0-39af-9b0e-00010306e8cc | -13.4505 | -46.88401 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb241aff-6db4-33be-97e7-9e69c6d977b7 | -6.62995 | -58.41595 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8fc44be-0111-35f7-8956-79f112a58894 | -9.2057 | -60.91809 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6991bb03-6e1f-3b3e-adc1-a8e01dd36763 | -7.52855 | -63.82027 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d239ed8-8880-34e5-b4ea-e68e366da017 | -8.89518 | -62.4671 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5765cf3b-8f68-336c-953f-cc5bd5f78a1a | -13.4305 | -47.02827 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5a79968-d8fd-3fbf-bfb3-5d4f3aeea060 | -10.42053 | -64.43289 | 2025-08-25 04:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cf29541c-fe06-3269-a0ef-556e8744b913 | -13.4632 | -46.8763 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 424d43d4-8558-3318-beb7-ef8078f1645c | -11.18608 | -55.02802 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d807a187-23bd-3b68-adc9-b3aa263084be | -12.99147 | -45.22117 | 2025-08-25 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6669fb71-0890-3626-ba54-1e3910b49f38 | -8.88973 | -62.46008 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59d52dd6-6d92-3670-b140-6f8c6fce8e95 | -13.43334 | -46.90006 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 402499b2-c52b-3787-b0d2-034064705d6c | -6.7933 | -58.64262 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc58653d-769a-3557-9810-2de7a4028ba4 | -9.19678 | -59.48301 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30ba6623-9ac8-30e3-baf5-76954aef8127 | -8.53352 | -48.84264 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2853edaf-7ca3-3f51-bb5d-62827c2f6883 | -10.71548 | -48.32635 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cde96c9b-391e-319b-9099-80adac4fa051 | -9.16005 | -59.46855 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 375e3cfb-f1a0-3d5b-ae49-e4376f23c387 | -8.09935 | -62.86569 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cf64d1e-fb6d-3b26-bd19-15e0c157ffcb | -9.19614 | -59.48656 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f39ee592-126f-354a-acca-65ba7e24e92a | -8.5896 | -62.60389 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7957058-c93a-34dc-b78c-4a427c640b56 | -12.75229 | -48.1101 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 820b2667-613a-3644-935e-ee01c3b4fae5 | -8.53017 | -48.84211 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 756c68d0-5517-38a8-a3d8-d68100299cdf | -13.43054 | -47.02626 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9652e6d2-becc-311d-b357-946507e9e429 | -8.21851 | -47.17329 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 237f88ec-b78a-35c6-9532-108c3d42aa12 | -8.89083 | -62.45444 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ee845ba-eab5-3e69-8366-0348b59f782e | -9.17994 | -60.79519 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ba8a3340-1fd3-340d-bb36-1166b4e3b51a | -13.65695 | -46.89008 | 2025-08-25 04:42:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e3a0330-74d8-3270-ad18-a08def9e307a | -11.19948 | -48.46357 | 2025-08-25 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 032b3383-6cf1-3295-8354-83d639703645 | -8.21767 | -61.38762 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3e24ceaa-9ef6-3931-a8ef-f3193a6b1e5e | -11.62888 | -46.232 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b034e807-0103-3272-9500-97b82b9f9fef | -13.41551 | -51.77678 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b597f1e7-5375-3d3c-8c93-3cb46a986837 | -10.24046 | -59.6623 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fcda38b-ae17-3da9-a9f3-5bcfae0eb5db | -8.3852 | -47.99343 | 2025-08-25 04:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da8772bd-677f-3b51-96f5-43769cfcee89 | -11.46872 | -55.47316 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df8c3c92-bd01-3aed-81bb-5b6c15b44a46 | -10.88374 | -55.78969 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3b7ee2f-85eb-32a7-91ca-769947ca78c8 | -10.46803 | -48.32431 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1696218c-4ce3-3fb2-80d9-473c82287797 | -6.82145 | -58.9557 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7666ec94-c92e-35e4-ba28-c7a6a96b2827 | -11.1442 | -44.79546 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bb3ebe1-8bc6-3a35-8f35-0ac77827ce65 | -13.6557 | -47.97995 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc41ed87-e53c-3a17-82da-548d66690121 | -10.6068 | -50.14098 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07a6eefc-6e22-3f4e-a5d1-3ba6b597b2e5 | -6.79802 | -58.64716 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9eb6dc3-1ab9-380a-9411-06f6c90e0293 | -13.05387 | -46.32092 | 2025-08-25 04:42:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 526e8d18-a010-3c96-888e-ed31f865d1db | -9.52493 | -60.52324 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc4fc788-9190-3797-a233-7c854ecf8df0 | -9.19224 | -59.48202 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b030b02e-2bf4-31ef-9c05-c44952e151b9 | -10.72587 | -47.1147 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fb49a59-b3c0-3063-afc7-28be382dc925 | -11.92989 | -46.73646 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f456712-afd3-37e4-9c1f-a43f84f6d82a | -8.06944 | -49.67107 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e59104b-f953-39eb-bbb1-f94a25383a8c | -9.15676 | -59.48637 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7a7a722-7630-3177-8d18-d64c058c5a27 | -9.15483 | -59.49688 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f30e86a-3552-3fa4-a16c-e71006aca4e2 | -9.16822 | -60.82416 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 93849e18-4c21-341b-81ae-fcfcd570afc6 | -9.1559 | -59.46052 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b85b38e-e1b7-36d4-9746-f54de09ad093 | -9.31551 | -63.44009 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fe4ed21-f8b6-3f3a-8c97-342b94dfb211 | -9.18788 | -59.6248 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c6d1f96-a256-3bc3-ada5-5cf400774faf | -8.753 | -49.97338 | 2025-08-25 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ef25411-1e64-339e-8c96-6e085f97a3ad | -10.71431 | -48.31084 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac66fe6b-1932-3f73-ab2c-069e91a53014 | -8.87613 | -62.43496 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c223f8a-e16c-32dd-a871-d07e88fcbb50 | -9.20224 | -59.60889 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84d6db89-2f58-35ac-af73-320867285ba2 | -8.22536 | -61.4016 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0157001e-a23a-35fd-a2c1-a2e73637f937 | -10.89618 | -55.79166 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bad3153-e83d-3db2-94a3-23202aba7c55 | -9.16144 | -60.82743 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 460f1f0e-29f9-37e4-9fbb-5d83ac2a37a0 | -8.05837 | -49.68013 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e480722c-52f0-32ad-aa64-aa0b87b775a7 | -9.19234 | -59.44565 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7797574-6903-33ae-8266-0135f0891779 | -13.41159 | -51.77979 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffaebb75-9b2c-35cc-b8ee-9a72db1977bf | -11.18076 | -55.02975 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69dcf91-0740-3b9d-8f11-706ebbf5d4af | -12.68879 | -47.83204 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 609ace3c-446e-3168-bbf7-67fc1581aff1 | -10.58487 | -47.13578 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13ead1f9-6101-379a-a63b-45c8a18eede2 | -8.80143 | -47.31712 | 2025-08-25 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea8bd514-3e50-3223-a499-ead5ec253d95 | -10.02182 | -51.07258 | 2025-08-25 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README49.md)
