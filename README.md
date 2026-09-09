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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73a75800-4e5c-3c36-9c36-45dac5e1254a | -6.1536 | -44.6675 | 2026-09-09 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b98d51a7-3a5b-3cfa-9f41-a75dce6d9b9a | -5.7758 | -45.0599 | 2026-09-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 142d3377-50ef-3cab-9610-09bec61d643d | -10.6535 | -58.7698 | 2026-09-09 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 61c78ab1-96e2-3856-ade9-4df5c77c1ca6 | -2.9392 | -50.4622 | 2026-09-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 1ec381b7-a421-38a8-9a81-6e8921833d6a | -6.0231 | -42.6348 | 2026-09-09 00:00:00 | GOES-19 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 0e4f00be-2f5e-3f4a-b9ce-bd6b53f94a53 | -5.7569 | -45.084 | 2026-09-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| d20926e8-6963-33f9-93a4-aa86ca552007 | -6.1723 | -44.666 | 2026-09-09 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 7ce54e6c-ed58-3d36-ad69-c642234aacfc | -11.0006 | -45.0847 | 2026-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6e33a8bb-3d15-3862-80c5-8bb4432687bf | -2.9391 | -50.4832 | 2026-09-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 4096eb48-0b63-3182-8417-b6ea271e1a7a | -13.2485 | -61.6565 | 2026-09-09 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 155.7 |
| ad12e785-3d5a-3a26-a3ed-6acec41bedae | -3.2486 | -47.2438 | 2026-09-09 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| b049329e-41ef-30c4-a9a6-8b464aef40aa | -6.3703 | -43.5898 | 2026-09-09 00:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| ec9bdb1e-2bec-38dd-a439-19fe6fb1162d | -8.7438 | -62.4169 | 2026-09-09 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| fdf202e7-e071-3494-b437-6bab92ddd92e | -5.8206 | -53.8052 | 2026-09-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| eb36f80e-af07-3a6e-9455-583770543787 | -5.8021 | -53.8061 | 2026-09-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c14c7aa5-5ce9-3b88-a9a8-f0f8c8c42256 | -10.7574 | -45.9852 | 2026-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e6ff1557-ee79-3c13-b897-8822398f47d3 | -13.2295 | -61.6578 | 2026-09-09 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 641d030d-9a6e-3686-9e87-3c59e30e91dc | 0.6167 | -50.8153 | 2026-09-09 00:00:00 | GOES-19 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 50.9 |
| cc9fd6da-21ba-375c-b79c-5acbc7939472 | -10.7387 | -45.9649 | 2026-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b743605d-bb91-36b8-bd3b-6dbc89d9829b | -5.7756 | -45.0826 | 2026-09-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 8420e5e5-267c-3f28-b58c-0a6fe1947a86 | -2.9576 | -50.4826 | 2026-09-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 14d666ca-3472-3e70-ac27-f6aabe998ee9 | -10.7391 | -45.9422 | 2026-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ff5495f4-aa52-3d01-a741-cf56fffa2f17 | -6.1726 | -44.6432 | 2026-09-09 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| fca1c8ff-0371-3467-b7bb-989a1d26ca83 | -6.1538 | -44.6446 | 2026-09-09 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 309bad9c-c795-30b4-a198-ed97944fbbe6 | -5.7571 | -45.0613 | 2026-09-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 0cacc068-9abc-3a75-a016-1749f58d661e | -8.7439 | -62.3979 | 2026-09-09 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 98a31748-533c-3f4d-87e7-1690e054a051 | -13.2293 | -61.6772 | 2026-09-09 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 528adf71-1c0a-303a-b21f-2a1e739338b4 | -3.2731 | -50.0741 | 2026-09-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b9d7ee1b-6301-354b-b807-1f6f5dca88d3 | -10.7578 | -45.9624 | 2026-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| feac2c25-5668-3168-b5b3-2d381d453eaf | -13.2483 | -61.676 | 2026-09-09 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 146.3 |
| c25e5e60-d7f1-3aa5-9fb7-7c5ca9a8414d | -13.2293 | -61.6772 | 2026-09-09 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d80b168c-c514-3a90-b109-0de1b950682b | -10.7578 | -45.9624 | 2026-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 3ec6f50b-fe46-3d22-85cb-57a24388cd5b | -5.7569 | -45.084 | 2026-09-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 1cc20b09-b3af-3848-a945-c89390ed2d77 | -10.7391 | -45.9422 | 2026-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| bfa93f8e-4991-38b5-a3ee-87ba455a4ca2 | -5.7758 | -45.0599 | 2026-09-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| d1194a33-5151-3b34-b816-c1da748901f8 | -8.7253 | -62.4177 | 2026-09-09 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a8af0c41-cae0-323e-a549-4f508f441a0f | -6.1536 | -44.6675 | 2026-09-09 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 28cf9a31-3be1-31cf-92c9-3bb8445a0bc0 | -10.7574 | -45.9852 | 2026-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 653781e3-d772-35ec-bd7c-ea98d5c21439 | -1.1991 | -55.7106 | 2026-09-09 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c64ac78b-e141-36bd-9cfd-e9940ceb3214 | -3.2486 | -47.2438 | 2026-09-09 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 8d6a8064-5c0c-33ef-b0b7-e6721c97df29 | -5.7571 | -45.0613 | 2026-09-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| aeb89fd3-3efb-3fe7-a04f-dae375cc012b | -5.7756 | -45.0826 | 2026-09-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 178.7 |
| d9d6f924-25e3-3f58-84fe-c636774da1a3 | -8.7438 | -62.4169 | 2026-09-09 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2c2ef6d2-f4dd-342f-9a28-b1a200194934 | -2.9576 | -50.4826 | 2026-09-09 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 35856319-fe11-3e2f-9cd4-ce6ac40294c2 | -10.7582 | -45.9397 | 2026-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| cdac65e7-7a83-3e6d-ab1c-c10d211458bc | -13.2485 | -61.6565 | 2026-09-09 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 2b87712b-da2c-3102-ab55-befe0c335296 | -5.8021 | -53.8061 | 2026-09-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6b979017-4151-34dc-8522-6f92a05fbc9a | -8.7439 | -62.3979 | 2026-09-09 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d5955f85-353b-3449-8bc8-2375474a92f4 | -3.798 | -52.4024 | 2026-09-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6a579109-d50d-3304-8b7c-8be609c463ed | -13.2295 | -61.6578 | 2026-09-09 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6e62d059-7cfb-3e7e-ac40-7618131af438 | -6.1726 | -44.6432 | 2026-09-09 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8d6ca317-ed4d-3ecc-b2b3-3e292085dddb | -5.8206 | -53.8052 | 2026-09-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| aaabba81-4548-3c1b-be9a-0c4a4f1fcb5d | -10.3067 | -46.8964 | 2026-09-09 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 14eda8c0-73f9-3610-8482-3558796a45e5 | -2.9392 | -50.4622 | 2026-09-09 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 4fcb1064-43e5-3144-a7f1-34bac52acdcc | -6.1723 | -44.666 | 2026-09-09 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 262f465f-efcf-3a48-bbc2-3574c025d4f1 | -10.5314 | -47.0926 | 2026-09-09 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 50baf347-a53c-3697-969c-56cdf71dc341 | -13.2483 | -61.676 | 2026-09-09 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 130edb96-681f-34cd-91fa-2d44ac4ffc4d | -6.1538 | -44.6446 | 2026-09-09 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 74d62ede-c6be-322a-a940-8c3928bb00fa | -10.7387 | -45.9649 | 2026-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 76147a36-12b5-3aad-9dc7-04cd1c5ce273 | -11.0006 | -45.0847 | 2026-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 151ec041-fcbf-3004-906a-b4be2e936d4f | -6.3703 | -43.5898 | 2026-09-09 00:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| c17022de-d2c5-3725-954b-a8727488e590 | -2.9391 | -50.4832 | 2026-09-09 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 0315a3ea-7269-3434-91ec-0bdf88a14ba1 | -10.5311 | -47.1149 | 2026-09-09 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| e8e0b599-827b-3ed8-9ee5-d6c4420f8ab7 | -10.2877 | -46.8986 | 2026-09-09 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| df33a417-e972-3a84-9a60-c4615d735abe | -5.76 | -45.09 | 2026-09-09 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12d9db95-7072-381c-9949-c5907701dd74 | -6.16 | -44.68 | 2026-09-09 00:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d966b69d-1b68-3648-9156-f8ba5d351b50 | -10.5314 | -47.0926 | 2026-09-09 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a64ff8d1-dc65-32c5-9cb7-8300f0294a64 | -10.307 | -46.874 | 2026-09-09 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2878e559-2afe-3454-b7fc-19c68bee4895 | -10.7582 | -45.9397 | 2026-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 54152c90-d2e9-3023-9793-745879ed0940 | -10.7574 | -45.9852 | 2026-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 2156e5a4-f06a-31fd-85a3-7ee9786de445 | -13.2293 | -61.6772 | 2026-09-09 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 57eff886-59df-3660-b9c0-543a7618ad81 | -8.7439 | -62.3979 | 2026-09-09 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 3722ec5a-9869-3417-ba63-5cfd5fe1621f | -5.7758 | -45.0599 | 2026-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 45899365-329d-3542-9f0d-fc57e0364e66 | -6.1726 | -44.6432 | 2026-09-09 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 6b8b3e47-daff-3032-b9f9-184ac9b3d7c9 | -10.3067 | -46.8964 | 2026-09-09 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| fb342e74-8a6e-36f9-949b-407c6e3892e9 | -6.3703 | -43.5898 | 2026-09-09 00:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| e042bde2-5e13-3f91-87a0-0a4015f6ea25 | -9.7695 | -43.506 | 2026-09-09 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 93812012-9f1a-33b2-b748-8d1541a57ac6 | -5.7571 | -45.0613 | 2026-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| fd5eb86d-80cc-36b2-b34f-a50355ba6d90 | -2.9576 | -50.4826 | 2026-09-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d5e2907a-5157-3c46-9a8b-bdfc60d8698a | -10.5501 | -47.1126 | 2026-09-09 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7a3f3621-12a6-3346-b8ce-7d4e5175323e | -2.9392 | -50.4622 | 2026-09-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| b3d3c029-dc39-3f81-acb8-ab3cb8ed8849 | -10.7387 | -45.9649 | 2026-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5bab2b30-3986-3035-9334-5c0b461f01f2 | -5.7569 | -45.084 | 2026-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| d1ef5925-6ab0-3985-81cf-c00dd28f05f4 | -3.2486 | -47.2438 | 2026-09-09 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7cb7cb50-cf6c-3103-8f08-a4a1591f485f | -13.2483 | -61.676 | 2026-09-09 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1d9aac89-1aff-3f66-8ce1-7efa5eb013a2 | -10.7578 | -45.9624 | 2026-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 340.7 |
| e9831017-62dd-39b3-8d2a-563066670532 | -2.9577 | -50.4617 | 2026-09-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e48d2946-56d5-3768-92f5-301ebe81a773 | -2.9391 | -50.4832 | 2026-09-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 05907102-137f-37b1-aaa5-a54fad905a42 | -6.1723 | -44.666 | 2026-09-09 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 404da760-12ba-3182-873e-5d20c023a567 | -5.7756 | -45.0826 | 2026-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| cc296f6e-452f-3afb-8069-2e330679d327 | -5.8206 | -53.8052 | 2026-09-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b1d6d769-84ff-312c-a6ba-f2c9bd917dc7 | -10.5311 | -47.1149 | 2026-09-09 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4b9cf61b-0e44-3262-9726-1d2a378bdcdc | -6.1538 | -44.6446 | 2026-09-09 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8ed0e454-9fd5-365d-8936-1d597cc05fd6 | -10.7391 | -45.9422 | 2026-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c48b8f83-bc73-3d91-bf51-be460a938210 | -10.087 | -36.1511 | 2026-09-09 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| aabe07c9-3b56-331d-a09e-f0d9a4d3a4bd | -6.0419 | -42.6332 | 2026-09-09 00:20:00 | GOES-19 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| a1388d83-e6dd-3ea9-88fc-d8b021d640ec | -10.0677 | -36.1546 | 2026-09-09 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 18a6ba70-65ff-373e-8eab-e0f72157745e | -11.0006 | -45.0847 | 2026-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c10a1ef8-0839-332b-ae07-a888b886c49d | -13.2485 | -61.6565 | 2026-09-09 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 279ecfd1-1368-3b58-8f75-52ef7e9e131e | -6.1536 | -44.6675 | 2026-09-09 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |


[Clique aqui para ver as próximas entradas](README2.md)
