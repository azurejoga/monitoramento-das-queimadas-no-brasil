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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b78be6a-df43-3ff3-8590-e5dd28ea86ef | -8.6135 | -62.60439 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e50b3ad-7ead-3de1-a78d-73aee4f53c14 | -7.65432 | -63.53174 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0144629-8a4d-3b75-86ca-8aa68bf6a6b0 | -6.33686 | -58.1908 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ace45768-523d-337b-a4f1-fa3dcb07358f | -8.86121 | -52.0499 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb520519-68dd-3e8b-ab6e-d128c13aba92 | -11.17523 | -55.02719 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f930cee1-cbda-3075-802c-54b7210ad305 | -11.60053 | -46.34456 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01d09731-38c6-3d54-8d3d-95c190edd30d | -8.385 | -44.95094 | 2025-08-25 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 893166cb-4371-3f0c-a59c-9adfbea59b89 | -12.74108 | -48.1394 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adb20936-2047-3f49-a879-cf35baf33365 | -11.61906 | -46.23975 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b62c66a-ade5-3265-a54b-cce5044156e1 | -11.45407 | -55.47227 | 2025-08-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6f01cf7-2d73-3f14-93f5-7a9b52ebf48a | -9.19929 | -59.47813 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae061ca5-66e9-3576-bfc6-79c0a831d01b | -6.43836 | -44.56482 | 2025-08-25 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d03a278-c523-3233-9fd0-3076d3fb147c | -4.93912 | -55.82428 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41d91e91-bb14-345b-b96c-a7b419ca2ff0 | -7.13641 | -56.40728 | 2025-08-25 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67a8f57a-7d73-3331-a6d9-345a5d45e028 | -9.15228 | -59.49559 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ef25adc-b8eb-311e-8387-01c3e1d991db | -10.782 | -46.42879 | 2025-08-25 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce2a2973-1f65-37e5-bbc2-79e68e20fe3e | -12.68694 | -47.82874 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b0b075b-a4d6-38e3-a858-100167efede2 | -9.09241 | -65.72803 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07aa1f96-32b2-3dca-b988-09f48d8ddd69 | -8.23863 | -61.42587 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 238ab668-0b0c-303c-a553-c9321c5f6071 | -6.62587 | -58.55131 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f9fa776c-f719-303f-a45f-34c49ed85a6c | -8.21649 | -49.56213 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8a4c7a7-934d-3a4e-b944-8c80048e0806 | -8.0692 | -49.64946 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f078fc20-679a-3788-9998-cb1e0a26db09 | -9.23595 | -60.92642 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5bbef8b-e4b5-3daf-85a5-282991048c0f | -8.6257 | -62.63709 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82c06f73-fb2b-34b9-a4cb-c73a30f6df4d | -12.75223 | -48.12804 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00ecd5ee-6372-39f4-8aa8-e21143959cb2 | -8.54469 | -48.8596 | 2025-08-25 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 769cbd5c-c75b-3fb8-a35e-f4eb63e87d1f | -11.63251 | -46.22779 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 343bc734-855d-3629-959c-da055ab69034 | -6.78818 | -59.6467 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e35dfba5-7fca-31b0-a8be-76a28caa3ad3 | -10.10666 | -57.76504 | 2025-08-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6d17c0c-bc36-37e8-ac4f-fab4a6f90fe9 | -6.83853 | -58.95498 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 04d212d3-00e3-3bce-a53b-7c72b2b705c6 | -9.20894 | -59.44186 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 991a2618-a171-3d80-9e37-dee557178a0f | -7.35973 | -57.6323 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 847e130b-4414-3fb7-af31-92d3999dcbff | -8.23114 | -61.42089 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 456037a3-d07a-3b04-8e11-a9c9c80873d4 | -5.41525 | -60.17386 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c361bfa1-4ba0-341a-97da-5fea8d42a15f | -9.16287 | -59.4762 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0aae146-156f-39a3-ae21-46fb7c39ebc7 | -8.99557 | -65.39986 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f995edb-f592-3894-9db2-4999fbd1f78f | -9.52072 | -60.55626 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dbc30e9-7272-3a9f-9460-31d7c03f5b6c | -8.90752 | -62.44411 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a8f479c-7ef9-3d0a-b714-1a5be116ffdc | -9.1713 | -60.80828 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f554a21-bca5-37c0-aa90-3711abac2dff | -8.54312 | -63.51057 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9bba4b2-8ba3-3e55-8249-02eacf57daa8 | -9.68944 | -48.33792 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e55907e2-24a9-39d9-9135-4c53b5589c62 | -9.21881 | -60.93352 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f39b5a80-b61d-3002-a6a5-75c89b5481b1 | -11.64002 | -46.21546 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 371fb023-901e-3ac0-a422-3f959bdf1201 | -9.17315 | -60.77413 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5942601a-1763-3de8-a7d3-f49590c2e29b | -9.2089 | -60.92173 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| afbc7ed9-e3c4-3db5-9d35-4cb786075d6d | -8.9196 | -62.42522 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a1fe3ce-8780-3922-a5ab-f061bd5ae747 | -5.40744 | -60.17255 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c19f753-8adf-3898-8ace-e25f530f2b0b | -10.58471 | -47.14421 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a14f99c4-3026-374b-987c-2d32604e0eb5 | -10.46715 | -48.32197 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 579087e1-589c-3cd0-b25e-9ce44326eabe | -10.41529 | -64.39802 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 242e0728-66d0-374c-a52e-0887eeb6f57b | -8.22102 | -61.38224 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 846dc878-25ec-3fce-b6a9-1dad962fd8d0 | -9.21169 | -59.70102 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edecf719-4ce4-395e-b041-de367abfd48a | -8.12488 | -47.13336 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ccd7e9e-4619-3a8a-b467-3c0614e518c2 | -9.17055 | -59.45217 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a732a27d-c449-35d2-a434-0cc302d10881 | -10.41516 | -57.68317 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ac7ef29-486a-3c20-86dd-3f72f1774acc | -9.0374 | -65.72773 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37c803c1-3b02-3353-a404-886164ae97ca | -9.07123 | -65.72346 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb9403ad-585a-379c-b823-b53c94170edf | -7.7269 | -67.07028 | 2025-08-25 05:04:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3007d22-e16b-3fb3-a6d6-b8253ee7a57c | -7.91406 | -45.88527 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 074993fe-7280-3f18-8153-efa991760451 | -9.16576 | -59.48091 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3538bb3c-e2c5-3555-a0dc-0f88aeac19bb | -8.87399 | -62.43393 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50536198-4157-3ca6-afc0-3fc085edf147 | -10.89692 | -55.79081 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4713e4d-4a31-3d68-8b6e-d91b904b84db | -7.29236 | -44.53027 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33c71ab7-317c-3236-a6b5-df2b366d4754 | -7.91218 | -63.07458 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b427f684-d827-3424-b910-fa2c3b263c7e | -5.75513 | -57.58146 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5270a5ce-e8f7-3513-bd79-f5771052e687 | -9.19535 | -60.78289 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e390bfd6-f09a-30d6-8a12-f7992a22d6a3 | -8.88327 | -62.45661 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7d9b83d0-ae58-32be-a45b-9cb81ca455f2 | -8.05968 | -49.68487 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 143c280a-74c1-3d25-92d4-179ef2fcc968 | -8.89896 | -62.44259 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0625ac79-f566-3d64-ab23-b47604423153 | -8.68212 | -62.88091 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8335ba25-a062-36e6-9246-469a78793997 | -8.50456 | -63.87701 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5aa5d390-3f0d-311c-99ce-3cb70ef8cc21 | -11.60435 | -46.36248 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9a4feb7-3e0c-3023-bb46-8678f9afb96a | -9.60733 | -55.34834 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d074245a-69e6-3255-8d08-b629f9682884 | -12.74265 | -48.11793 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bc1c6f8-0b17-3a22-8e91-04d9130bfa77 | -9.07061 | -65.72684 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b58bd48d-405b-3f30-94f9-74281dc66eda | -9.64468 | -59.64865 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9950bdd8-4ca7-3586-87c1-cef251e66f4f | -9.20505 | -60.91401 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ffcf388-cf83-36aa-ae14-5e7ba114a6ae | -8.89113 | -62.46221 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aef89c8-2cf5-3186-988e-c1656f2cc822 | -6.77631 | -59.6493 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bae87980-660f-31e6-b863-ad1820058b4c | -6.79296 | -58.63795 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62255c68-0b4e-34ca-a85d-43d86a79c941 | -6.53074 | -44.43288 | 2025-08-25 05:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65b84384-3729-3b3d-91af-5ca4ffd09a10 | -6.82063 | -58.95208 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 685b76d4-a8b3-34d5-8a24-a46812ac0c32 | -6.68785 | -58.86144 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc46b21-8287-3e0b-b33b-1fec2f608f58 | -9.133 | -60.73238 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83a78268-87e0-3ebe-bdcd-f4a5682ae4df | -9.0118 | -65.39958 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78f0efd7-f790-3132-8fd5-95c35d4501a2 | -8.63367 | -62.64289 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25c83f88-a421-3b7f-a7f3-42e72808e58e | -9.82423 | -64.26243 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b23ae37c-f9b1-3de4-bfbc-e34adcfc2ded | -9.25467 | -59.64367 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cd36049-fb52-3579-838e-dc6c4f00085b | -9.04398 | -65.72195 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd228776-20d0-38f6-8d56-6f6b3b15df86 | -8.91175 | -62.41967 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80c8fb0f-b416-35bb-80df-4b36fc58f063 | -9.14158 | -60.73701 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 10469c67-f687-3eb7-af9a-6cbef12e0730 | -7.27765 | -57.66762 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3518a65-286c-34a1-af82-9c59a10949f6 | -9.49468 | -58.93866 | 2025-08-25 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1d43cf6-00bd-323e-9928-3599973db20c | -9.15915 | -59.45448 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31fae684-9b77-3090-9b7e-34e229fa86c0 | -11.18095 | -55.03574 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b629c510-8299-3cd3-af2c-f1cc39bd27a5 | -9.61124 | -55.34527 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56505361-7971-3c7a-9414-d632227f8c77 | -4.96392 | -55.81757 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31897c93-6855-3d8d-a29b-1a9c2d728e97 | -9.96769 | -60.1798 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e0f93c85-7d17-347f-be46-c5be239e930a | -8.58196 | -62.62597 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7898c307-7f48-3094-933f-7026f91bd796 | -9.49516 | -60.54705 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README69.md)
