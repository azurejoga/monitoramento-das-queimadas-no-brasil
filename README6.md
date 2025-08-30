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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b466cbe5-b28b-33dd-8c06-5afbe056e3b0 | -6.5951 | -43.6403 | 2025-08-30 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 37883b56-2dec-3e8c-8647-50eed4e0bb08 | -9.0614 | -65.4355 | 2025-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 0d751f0b-b2ca-31b4-976a-570da39f6819 | -11.3125 | -43.6191 | 2025-08-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e14d2ef4-4da2-3593-ba4f-8e5be1c98d95 | -13.3817 | -47.015 | 2025-08-30 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ff100c85-c30c-3e81-bd89-0ca7cdbf594e | -13.6295 | -48.1874 | 2025-08-30 01:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 120.6 |
| e2c1c0e2-bf05-3c2a-ac3c-c7f4e751b1af | -9.1156 | -65.7513 | 2025-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b256bc55-42c8-3d67-9027-783695b55081 | -12.0153 | -43.9818 | 2025-08-30 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 334ebfb0-e0a0-3e7f-aea4-043fe52a4f11 | -11.3321 | -43.5926 | 2025-08-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 521ff403-f4d6-39a9-8c70-433c18efacd5 | -9.0799 | -65.4349 | 2025-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ee537aab-5d2d-3b45-bac1-e9c4d8b935a7 | -8.894 | -62.1066 | 2025-08-30 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 36a701ba-5b97-39ee-bfe6-bca7202f8b52 | -11.8564 | -46.426 | 2025-08-30 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3494fc9d-762e-30c8-9251-9d020e1ea4e0 | -9.0613 | -65.4542 | 2025-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ff41d966-126c-3d26-9bd6-bd2f9b2b9075 | -13.3821 | -46.9924 | 2025-08-30 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 9c63a9f3-efb9-3404-89bf-76bd7f755901 | -5.6268 | -45.0025 | 2025-08-30 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| b3e4f2e0-7a37-3ad5-b0ed-61595f261da2 | -6.5948 | -43.6636 | 2025-08-30 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 51cb157d-0773-36b5-9094-d82cbda91cc3 | -9.0799 | -65.4536 | 2025-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 39c5fd82-23a2-39e1-b740-7817cc0ff68f | -9.1155 | -65.7699 | 2025-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.0 |
| c2a42f25-7511-3f8b-ac01-066ce102ee57 | -11.3317 | -43.6162 | 2025-08-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3ea19947-74fd-3051-b350-3ae581ee0514 | -5.6081 | -45.0038 | 2025-08-30 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7d0bb195-a642-3c35-9324-7c7c05b1db7f | -13.4019 | -46.9667 | 2025-08-30 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0ba50ec3-76ed-3a16-93a2-180f203df6b2 | -11.312 | -43.6428 | 2025-08-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 9b82c52d-4b41-33df-a0a8-99b6e671c87b | -9.4432 | -60.5692 | 2025-08-30 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d58079fa-1ffa-3ea8-b0aa-4b7249c8d113 | -8.9126 | -62.1058 | 2025-08-30 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 0d515b93-718d-3ae1-9294-687b705163b0 | -13.3628 | -46.9953 | 2025-08-30 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e1391401-1e7d-3567-a6a3-0e933414c83b | -9.7044 | -49.4609 | 2025-08-30 01:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 008f2ce8-9da3-3fc7-99e3-1e6f64f55ae9 | -13.3825 | -46.9697 | 2025-08-30 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 139.5 |
| e94725cf-8fbb-3c0d-98f3-81558f918645 | -13.6488 | -48.1845 | 2025-08-30 01:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ae54b697-b3b6-3061-92d9-976ea90db124 | -9.4433 | -60.5499 | 2025-08-30 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| c9780162-b2bd-3e11-b038-31c4826f8d64 | -11.3312 | -43.6399 | 2025-08-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 966de1ae-e63c-3f78-9876-5fe2332790f8 | -8.66259 | -70.053 | 2025-08-30 01:30:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3e21c358-40f7-3ccb-8574-02e88c4ceee3 | -7.09423 | -63.13494 | 2025-08-30 01:30:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a210cf2d-743a-3098-ab38-31383333b1c8 | -8.29436 | -61.42162 | 2025-08-30 01:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 97860c31-f041-3ffb-b983-a32a783e02cd | -8.62456 | -63.95475 | 2025-08-30 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c747e34-50a7-3d37-a6f5-0dcb66e50159 | -8.53103 | -64.01263 | 2025-08-30 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 478bb3de-e836-3b5d-8b85-aeae0b41da35 | -7.09546 | -63.14384 | 2025-08-30 01:30:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6672f173-3647-3644-8139-011fd3654d2b | -8.31348 | -61.4281 | 2025-08-30 01:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38d73293-a607-3c29-b7f3-3682f0021e53 | -7.54175 | -63.84235 | 2025-08-30 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85b560df-5454-37ce-b880-0444931fd72b | -8.25363 | -61.45539 | 2025-08-30 01:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f69e9aa6-0a1b-3c2a-b4c4-0159c07d27ad | -8.64087 | -67.26078 | 2025-08-30 01:30:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 16773769-b994-3834-932d-e7c3c14f4a86 | -8.62751 | -67.24692 | 2025-08-30 01:30:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 661c5bcc-619a-3cc3-b473-8ddcad01e097 | -7.27712 | -60.61589 | 2025-08-30 01:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a2d6e2e-fcf2-3ddc-9bc2-24b20f33642c | -6.56906 | -69.95714 | 2025-08-30 01:30:00 | TERRA_M-M | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a8afe158-efc2-3e4b-8d57-1ffff9905fb8 | -7.57063 | -63.85104 | 2025-08-30 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c007ce9-26ef-34ae-835f-06dbc375a006 | -7.57188 | -63.86034 | 2025-08-30 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9c2dc9e5-e760-3f24-a1ea-c5dfc66622bf | -7.0738 | -63.18323 | 2025-08-30 01:30:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2da900ed-90c1-335c-b56a-c93eaee5a3ad | -8.85196 | -70.6261 | 2025-08-30 01:30:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4c0ee994-f4ad-3cbf-aee3-6e22e5ae8860 | -7.56108 | -63.84913 | 2025-08-30 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19dddc9a-e4da-3f5f-9909-23d2ed0812d5 | -8.52975 | -64.00303 | 2025-08-30 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a85b4f8d-18ac-3e9c-b9d5-2ceedc004c32 | -11.8568 | -46.4034 | 2025-08-30 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 756387e0-be02-3430-82e0-56ccb017d1fb | -13.3821 | -46.9924 | 2025-08-30 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 223e3a04-f407-3a40-92a1-00cb79b41623 | -11.8764 | -46.378 | 2025-08-30 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 75fad000-3f5f-3fd3-91b5-236e0e1ccccb | -9.7044 | -49.4609 | 2025-08-30 01:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 9f637584-7525-3887-b270-f4a79e51d68d | -9.4435 | -60.5307 | 2025-08-30 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5b2fb4cc-c06e-39c2-b778-5ea079b551cc | -11.8572 | -46.3807 | 2025-08-30 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 208.8 |
| d93af436-8074-3cf0-a5e9-82eaab14e66a | -9.4432 | -60.5692 | 2025-08-30 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| fc060d0d-d63e-31b4-8b71-0fc708e1b9b6 | -9.4618 | -60.5682 | 2025-08-30 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b153bcfa-d9ab-3099-a007-7831479ae71e | -9.0613 | -65.4542 | 2025-08-30 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| fa6cd2b8-e362-31a8-a965-48d01b952c58 | -11.3317 | -43.6162 | 2025-08-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4d9f0729-7bbb-392e-89a9-8e5e5d2548cf | -13.3628 | -46.9953 | 2025-08-30 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| a331e1d2-68cb-31b5-828b-bf3900f0160d | -11.3321 | -43.5926 | 2025-08-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b4fb4a27-9d6a-39e9-9d37-4d09d1d3a670 | -13.3825 | -46.9697 | 2025-08-30 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9d4a39b3-eac1-3568-b58d-1a5018d74da0 | -11.8768 | -46.3553 | 2025-08-30 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 62f222ec-19b2-3fca-acce-2f028e700b8f | -11.876 | -46.4007 | 2025-08-30 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 539ef599-91f1-31e6-8c56-e2a4e535b0bd | -9.0614 | -65.4355 | 2025-08-30 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 04280ec6-787d-3d97-a3f9-efbdeda585b2 | -11.8576 | -46.358 | 2025-08-30 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| d726d556-2010-3190-9b06-f3bc0fbe61e8 | -9.1155 | -65.7699 | 2025-08-30 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 21a5ec96-adc7-39b5-aff4-65520e0585ba | -5.6081 | -45.0038 | 2025-08-30 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8ddae7af-2386-34ee-ab1a-2d080627f604 | -13.3817 | -47.015 | 2025-08-30 01:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| f252eebd-3c59-38db-acbc-1a6eb90b866a | -9.1156 | -65.7513 | 2025-08-30 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ce7512df-d795-3f74-a388-b067c53975ca | -11.3125 | -43.6191 | 2025-08-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f0a48f63-bce5-317f-9443-e8a1fffee468 | -8.8843 | -60.7315 | 2025-08-30 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 6b738ce0-06f5-3b6a-b29c-55a6d06ef48e | -5.6268 | -45.0025 | 2025-08-30 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| f34b5b4f-f3d5-32be-92d4-a7e6c26126e0 | -9.4433 | -60.5499 | 2025-08-30 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| e40b03bc-0423-353c-85ae-8bce2a1c2f17 | -11.3513 | -43.5897 | 2025-08-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 43392712-7a52-3746-aad9-4bc311061b26 | -9.0799 | -65.4349 | 2025-08-30 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1dc6988e-f140-3b16-9b21-0a994ccbc08e | -11.312 | -43.6428 | 2025-08-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 5bc0a1d8-77c6-350c-9ed8-8cd22bc3fc1b | -8.8658 | -60.7324 | 2025-08-30 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b6800605-3cfc-3c20-a8a4-994f0c96f2ed | -8.894 | -62.1066 | 2025-08-30 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 9d8d2662-70ea-31fd-8792-3c62038ff267 | -13.6295 | -48.1874 | 2025-08-30 01:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| b3b4788b-65f1-3982-b7a3-82a0b0625c2e | -9.462 | -60.549 | 2025-08-30 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 73252eee-857e-3631-8552-c221ba534aca | -11.3312 | -43.6399 | 2025-08-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 74645bfe-dde8-3f49-abe9-52772a9fa549 | -8.9126 | -62.1058 | 2025-08-30 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 148eba88-55ce-386e-b114-5d8260b6ae8a | -9.4432 | -60.5692 | 2025-08-30 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 858a076e-47b7-3033-a9d4-c1ba4a0a9c6e | -5.6268 | -45.0025 | 2025-08-30 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 7e828bb1-3f0f-3c4a-8ef9-da581108670c | -9.0969 | -65.7705 | 2025-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 3b773a35-dad4-30d4-b14b-1dbd1adad08d | -8.8843 | -60.7315 | 2025-08-30 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| b229ec51-6f9a-312c-9add-9cc8f7cf7141 | -11.8764 | -46.378 | 2025-08-30 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 003332f0-db7e-3b88-9f19-1cb1bad180f5 | -11.3312 | -43.6399 | 2025-08-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 70ed8d9a-dbc6-319e-8d01-823aa167075d | -8.9127 | -62.0868 | 2025-08-30 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e429801e-6e89-3a59-a9c7-c421c1c01471 | -13.6488 | -48.1845 | 2025-08-30 01:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 76e24acb-2650-3ee7-89e6-8a7719685756 | -9.4618 | -60.5682 | 2025-08-30 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4774c3a2-71e7-3a80-b56b-5e68998c8ae1 | -9.4435 | -60.5307 | 2025-08-30 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 49734e60-d370-3f48-a401-27ee5dc526bf | -11.8572 | -46.3807 | 2025-08-30 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 0d502114-0b12-3bee-a5d2-5643232558e6 | -9.4433 | -60.5499 | 2025-08-30 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 3445ba32-ef10-3560-8102-150e186e4531 | -11.3321 | -43.5926 | 2025-08-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b2e54385-1d4c-3020-98fc-dcb4feb74f4a | -13.6295 | -48.1874 | 2025-08-30 01:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 526d68af-2d3b-34c1-a7a3-1dab196aeac2 | -13.3825 | -46.9697 | 2025-08-30 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 0e78d624-1a71-3d84-bd75-442ae33b5327 | -9.4247 | -60.5509 | 2025-08-30 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 12ad425a-c552-3bef-901d-0a6537ae8ab2 | -11.8568 | -46.4034 | 2025-08-30 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 6ee3096e-0f1c-3690-bbb5-3848d089bf9a | -9.0799 | -65.4349 | 2025-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |


[Clique aqui para ver as próximas entradas](README7.md)
