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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ead143a-1666-32c6-8fd0-5bf0eacb8b8f | -3.2182 | -61.0661 | 2026-09-22 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 903a8129-0457-3e28-b0da-538c611945f7 | -3.3184 | -57.8483 | 2026-09-22 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| eacd6b04-cfd5-38f5-9c90-96a081615126 | 1.4269 | -50.7657 | 2026-09-22 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.7 |
| dfe724cc-e3a5-35d8-a3ca-2cce22224984 | -3.7364 | -58.8818 | 2026-09-22 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 3376e986-ca66-37ba-9848-7165ea7e204d | 1.5282 | -56.0424 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 49327379-ae73-3bf9-a0b8-c43573c363a0 | -10.7999 | -50.8455 | 2026-09-22 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 3e30bc9c-cb30-39c1-b21f-dc4b907f5051 | -5.4179 | -60.2166 | 2026-09-22 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 97fc02b5-65fb-3bdf-9ad4-07be4d04ddef | -2.4206 | -58.2712 | 2026-09-22 16:00:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 58c48b20-19e9-3868-926c-564532a14c72 | -3.6033 | -60.5664 | 2026-09-22 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 183.7 |
| a9eb7afd-4d1a-3403-8746-88f4e1a5a5d6 | -3.6449 | -58.8647 | 2026-09-22 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| db699ef8-9cb4-3461-b16e-835a51942778 | -3.6447 | -58.9224 | 2026-09-22 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 1ae3253f-1edc-346e-ae50-3a049fb4d52d | -3.6264 | -58.9228 | 2026-09-22 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| d2337c4a-230f-3ad5-a8ec-ef0143abd09d | -1.4302 | -48.9955 | 2026-09-22 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 62c10743-934c-3b70-b185-4bc6fd7a51be | -11.3813 | -44.0554 | 2026-09-22 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 293.7 |
| 11166dde-c71b-3d12-8754-11f16fdc81f5 | 1.3817 | -56.0636 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3fb186be-dfb1-37e6-947a-0edffe4ac9ff | -4.1513 | -60.7827 | 2026-09-22 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| be1a637e-1d14-361d-822b-155068193f3a | -7.0033 | -59.6622 | 2026-09-22 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| dde9858a-0b36-38e0-8254-2e0c5ea79c95 | 1.968 | -55.8989 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| dba6bf6b-d523-3d44-9f65-f89c8f33e12e | -10.3729 | -50.2722 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 0c6ab87e-afbf-3402-8f00-1032bc5f7a59 | -5.7431 | -57.5814 | 2026-09-22 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| f0cfde36-b079-3f5b-8917-62075bf6549e | -3.4368 | -61.3081 | 2026-09-22 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 645effa0-1a0d-3064-9d9a-7bf308f72b53 | 2.6715 | -60.6012 | 2026-09-22 16:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 258d64df-1b7d-33bd-b2df-93d356a0d88c | 1.4453 | -50.7655 | 2026-09-22 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 7b12d98c-d6eb-3e6f-8351-b0d3512e0fa4 | -3.3726 | -58.0796 | 2026-09-22 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d57e803e-fa90-3624-abc1-ec297605f5c1 | -6.728 | -59.423 | 2026-09-22 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8f5ef834-cfff-36d8-9f9e-14c1577c229c | -3.4215 | -60.1896 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 35c0d04d-9635-3471-b1c0-7df4e0d7e315 | -11.7079 | -50.9811 | 2026-09-22 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 01da55e3-4606-355c-a86c-4383469095e8 | -6.0925 | -57.6847 | 2026-09-22 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 339.6 |
| 9d572d7a-ca1a-3a06-bbfe-00792b04759e | -3.3358 | -58.1384 | 2026-09-22 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| cfb44c37-31bf-3727-be03-87760e759a37 | -3.8957 | -60.5984 | 2026-09-22 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 9e6141b8-1c07-3359-b02a-10301a0d9bd2 | -3.1698 | -58.5859 | 2026-09-22 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| cd2aa7ed-12a8-3db0-8bd0-f6d8b436562d | -11.3976 | -44.2167 | 2026-09-22 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ed312d8a-5a81-3daf-9a52-f1d278a716dc | -10.3919 | -50.2702 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 735eb492-1f0a-3ef3-846f-33d8be036a61 | -3.0352 | -61.2581 | 2026-09-22 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 62cdf763-ce4d-3941-b8e6-c16be78cb068 | -3.1816 | -61.1045 | 2026-09-22 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 1a287bfb-6e7c-31c3-afe5-f93813060152 | -3.7181 | -58.8823 | 2026-09-22 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 06dac1d6-1499-362c-a693-d46199b93012 | -10.2787 | -50.2605 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 1a1d876d-756b-317f-8de3-71edc72ce49e | -3.4463 | -57.9424 | 2026-09-22 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f7c813ea-ffae-30ed-b2c8-dbf389db8f40 | -3.0535 | -61.2578 | 2026-09-22 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5574f268-bbbc-3c70-8b8d-1343231d5035 | -3.4447 | -58.4645 | 2026-09-22 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c6087138-b3f8-3987-83b1-1458a5458ccb | -3.1095 | -60.7271 | 2026-09-22 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 28ba495d-4e20-365a-be8d-b277a8c75834 | -3.1095 | -60.7081 | 2026-09-22 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 110b5788-0379-3fc5-96c1-0fb18bd996ac | -1.4487 | -48.9526 | 2026-09-22 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8dba3fa0-a6cb-3ab7-88ac-336923e89f73 | -6.9849 | -59.663 | 2026-09-22 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| f224563c-5aa1-3e85-829e-c78e748a28d9 | -3.5893 | -59.0773 | 2026-09-22 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c7af4a0c-03f9-36b3-96a6-bcf8a9022583 | -3.3309 | -59.8673 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 3295d4bf-3c81-3eba-b9b1-4ae836d91f20 | -6.1111 | -57.6645 | 2026-09-22 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| d2c0b1ba-3676-3ed5-bfbf-9be59f29da62 | -10.6875 | -50.7722 | 2026-09-22 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 77c215ba-81e5-3ba5-bc89-5bee5de970cc | -3.7313 | -60.5638 | 2026-09-22 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a7cdf91f-8a41-3bf0-8c38-6ce4208b90a6 | -1.4302 | -48.9529 | 2026-09-22 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 4874ab9b-d60c-3d6e-bb3b-20248324d79e | -2.9525 | -57.72 | 2026-09-22 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| faed19d6-a26b-3295-834a-f58665f3118b | -10.4102 | -50.311 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 01bb12b2-0116-3563-80a4-ed2d4269b77a | 1.39 | -50.7662 | 2026-09-22 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 35eda038-d28d-3379-b738-29425a39947c | -2.9997 | -60.8047 | 2026-09-22 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ae2922ac-d47a-3b98-8f34-3585c2044127 | -3.331 | -59.8483 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| e8b2c9a1-57cc-32e9-92bd-8dc12cdaa86e | -6.583 | -58.9658 | 2026-09-22 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7d1857b5-9ebd-37f3-9652-45de49da80f8 | -3.1851 | -59.6982 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 77e715ab-5f9d-32ad-b57d-40b02803def4 | 1.3818 | -56.0439 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| eabc30bd-5abc-3c02-a817-f982a11ecc92 | -3.3134 | -59.5812 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 4750d6b7-037c-3e41-bb37-c80303f3ea65 | 1.547 | -55.7466 | 2026-09-22 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| e8d66041-7c59-3bfb-a982-31fa1460505a | 1.5836 | -55.7856 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6aa45952-5016-3097-82aa-f937f7b232d9 | -3.7707 | -59.5909 | 2026-09-22 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 082c704c-c8f9-3891-b89c-472e83332f39 | -3.6078 | -59.0193 | 2026-09-22 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c9705de6-31af-336d-99eb-e78d629467ce | -5.4732 | -60.1767 | 2026-09-22 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 982089bc-2ccb-3525-813c-56848c8797ac | -1.0244 | -48.8087 | 2026-09-22 16:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d256ab4a-08eb-322c-9a1a-90a2717bb1d7 | 1.3634 | -56.0834 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e366af1f-d7bd-3ed2-8920-5b0ed45ecf41 | -7.6079 | -57.616 | 2026-09-22 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| dce7391e-9702-3ad2-81ee-93cd2852fd2a | -1.0243 | -48.83 | 2026-09-22 16:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1fd316d9-4737-3cb4-a948-2c968b4cfd90 | 1.5287 | -55.7468 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 12d13de9-51be-32df-9e37-88d976b14296 | -3.5501 | -59.9584 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 988b94e9-228d-3021-b44b-a60352a07d52 | -10.4108 | -50.2683 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 6da6d173-d931-3c23-9167-f79d22c0890a | -12.8 | -44.2073 | 2026-09-22 16:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d9eb1fc4-47ea-301f-bddb-0a9157bbefcf | -10.3913 | -50.313 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 054c69b0-57ac-3628-bf22-23534b2f5729 | -9.7693 | -46.0615 | 2026-09-22 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 70097e57-55b6-3b6e-8234-9d8561742135 | -2.8534 | -60.9206 | 2026-09-22 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 51ea3ada-580d-30af-b80f-51fa3442e7ab | -3.6632 | -58.8643 | 2026-09-22 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 283a1f70-9bd3-3141-9d01-14687af168f8 | -3.3322 | -59.3894 | 2026-09-22 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 89917c75-39af-3ec5-891d-55fcd2592a41 | -3.4215 | -60.1896 | 2026-09-22 16:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c0ebda5f-3af3-342f-86ec-b05cce26df67 | -2.4023 | -58.2715 | 2026-09-22 16:10:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c03129be-bc98-3297-a6f8-9f23e3231768 | 1.547 | -55.7466 | 2026-09-22 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| aba034a5-9aa1-3abd-8e37-6804a6c49f10 | 1.3818 | -56.0439 | 2026-09-22 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 5deff1c7-c408-3983-a540-984bb77d2418 | -10.7897 | -50.2071 | 2026-09-22 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 6021a358-ce33-3dad-9914-c1bb114b2647 | -3.6066 | -59.403 | 2026-09-22 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| dd40977b-af3d-3561-9661-4b3ae8f8a59f | -3.7313 | -60.5638 | 2026-09-22 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c4f7cd94-c42e-331c-a497-d88ab31c3dd9 | -3.7364 | -58.8626 | 2026-09-22 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 56fc5c9e-991b-34cb-8dc5-8ed13d94fe86 | -3.1718 | -57.8708 | 2026-09-22 16:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| a38f5a21-ad1c-3e7a-9498-8fa595cb3770 | -9.8118 | -48.453 | 2026-09-22 16:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f1d24ae0-127d-3aef-8488-ee79a366fced | -10.3729 | -50.2722 | 2026-09-22 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 5fc49f36-691a-3411-84a9-4c0f167dd06f | -6.7463 | -59.4416 | 2026-09-22 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f33b3d5e-69d1-3fb1-81e7-2bdd6004e448 | -3.1079 | -61.408 | 2026-09-22 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 85649a48-c8e1-3a93-bc0e-1ab846d9a35c | -2.9326 | -58.3397 | 2026-09-22 16:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 693dab7a-f001-3a0d-975e-fc8ad4239188 | -9.788 | -46.0819 | 2026-09-22 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 6bcf1bc3-7c63-3e01-afe6-dbbcfe84eebb | -3.6076 | -59.0769 | 2026-09-22 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 8496af87-bd1a-3d44-8a79-93458d8a7294 | -8.7706 | -45.8567 | 2026-09-22 16:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 28fc6390-9208-3e55-bcb9-80c4a4a2c900 | -10.7804 | -50.89 | 2026-09-22 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 1175ff47-d7ff-3bfc-a1d8-4de4f7b3504c | -10.7715 | -46.3001 | 2026-09-22 16:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| ae98b71f-bfc8-3eca-82bf-bb5eee44bff9 | 1.4453 | -50.7655 | 2026-09-22 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a45d73f1-6507-3d7c-a215-d9f18220b1e2 | 4.3702 | -61.0053 | 2026-09-22 16:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e46f24ca-3e53-393b-a9c5-c87a3420bc9c | -6.1111 | -57.6645 | 2026-09-22 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| cb5abcd5-a5a4-3f30-a7ec-8f29b3bc571c | -1.4302 | -48.9529 | 2026-09-22 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |


[Clique aqui para ver as próximas entradas](README156.md)
