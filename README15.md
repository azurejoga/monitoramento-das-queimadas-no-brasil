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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8595f34-ce10-3b92-99aa-a17db145a7ca | -4.2803 | -40.70381 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e03b1c04-cec6-372d-bc53-42861cdef1d2 | -10.46901 | -49.10672 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e33a76a-eff4-334c-8ca9-ac533b975d25 | -9.63216 | -46.8953 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cad09256-6acc-3ec7-b531-886edf2f539e | -3.05506 | -48.71278 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b34b0e2d-b161-338b-854b-29a0fa1e83cd | -9.2621 | -45.35 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b9d1c4c-ace2-3742-ad25-0fc6814d21ef | -4.91773 | -47.32588 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61e17419-7843-3178-9799-a98b99d8612b | -2.86994 | -45.25927 | 2025-10-24 04:17:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 35c51a68-50b0-3b5f-b9e3-fd13aafe31c1 | -4.8517 | -46.73075 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8e3c9b4-13a4-3152-8812-b7f4d1913300 | -9.8719 | -47.46798 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edbb2049-1f44-36e2-93fc-d575e93dc9e8 | -6.30183 | -41.88362 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 038803f7-91a9-3f08-b278-cd52e8c737e0 | -5.65356 | -45.95593 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbcdf707-ad38-34bc-b259-72a3174942a8 | -2.85519 | -50.73806 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a14b91c3-7672-3c98-b444-6017630c40d4 | -2.85833 | -50.73653 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a7b2d01-05b2-3140-8416-c428d94cfecd | -3.76538 | -48.92463 | 2025-10-24 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9221e6e7-c482-37b5-9ba0-f67bbcfddaf8 | -10.02286 | -47.08461 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8fb0ffd-c075-3c96-b85e-4189a74b8fbc | -6.31192 | -41.86323 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e6bad30-449a-341f-92d4-b366b7059cf2 | -6.31899 | -39.71774 | 2025-10-24 04:17:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e127195e-a299-3f5f-8019-34ca2e63966d | -2.26311 | -47.84275 | 2025-10-24 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9abc0e0-0e3e-318a-83b0-7deec22e927c | -12.07708 | -46.42985 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61e803a3-a5a6-3ae6-9705-d713bbb6bea5 | -5.90361 | -39.75594 | 2025-10-24 04:17:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5994409-8ae2-3ed4-acd9-eb64a102fb52 | -6.08946 | -46.23685 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b93e3f5-d300-39e8-a14f-7187b778bd4a | -5.83897 | -40.80126 | 2025-10-24 04:17:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04a5ef57-c545-340d-88bc-ad6d5add111c | -11.35988 | -45.9217 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 658e8b10-e73e-335c-92dc-b138531d8ee8 | -4.90727 | -47.65562 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2af9709d-0887-3cc5-8bd8-323205ae558c | -8.74135 | -45.83784 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 119d376d-bcb9-3be9-aa8b-c35569a42217 | -10.04295 | -47.07526 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3cf9213d-b23e-310e-8f09-7b3c8a1e8eed | -3.56026 | -47.3044 | 2025-10-24 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5628b219-b5ec-37a4-a1f5-4557193a454a | -4.47194 | -48.1188 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f995fe34-59b4-34d8-ae39-0f7e04109afb | -9.81698 | -45.72099 | 2025-10-24 04:17:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87fe1f47-345a-3dcc-b49f-f42bcffcfe02 | -5.56592 | -43.61087 | 2025-10-24 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83fc315b-9868-335d-a0be-b7a388edc670 | -4.27968 | -40.70783 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c3d96f2-9d15-3c44-8cb7-a5a2290fd61e | -4.87157 | -47.53778 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 127774f5-5d0d-308a-b374-05dce68bb353 | -6.08652 | -46.23215 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00524493-6379-3640-9d0a-9d70776bd77f | -12.06178 | -46.41541 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dae2be6-f7b2-3b6b-8626-fb1c3d715de7 | -10.88783 | -46.07034 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b68f77b0-9a5a-300f-bce6-715c5cf8d4f1 | -5.54106 | -41.36912 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b8bae4fc-4b75-375c-9b17-97d3e7bdaa6b | -3.14381 | -50.62493 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9359532a-eb68-3739-b2d5-65de70fa4caa | -10.89477 | -43.82368 | 2025-10-24 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 873a52e9-77e7-3158-b0c2-d80c03be33e7 | -2.80703 | -49.14538 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60ce92be-2454-3440-9ab7-afbcf0c5dd95 | -3.83155 | -51.74535 | 2025-10-24 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 931905f0-8162-3d21-a0d9-c68bbc5d5d3b | -3.1185 | -49.10564 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1926a03c-3cb7-3d08-b0cb-b5088364bae8 | -6.12014 | -41.75001 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2170f75d-258b-3655-a602-2b9e79e536d7 | -2.80266 | -51.35648 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2375081-f574-3461-8df4-8f4a3fae325a | -9.86166 | -44.89926 | 2025-10-24 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbfe542d-229b-3b07-8d0f-09bcfe932a7e | -11.06402 | -44.78578 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6741563b-3cf0-303b-aaed-9fb0fb0ce519 | -11.52914 | -47.10144 | 2025-10-24 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23769c39-bce9-37f8-bd12-d03d84c6392f | -3.24848 | -52.91177 | 2025-10-24 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 285c185e-d732-30ff-9c59-fc88a4e2de02 | -9.75458 | -55.34262 | 2025-10-24 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d896c892-1e6b-3cb1-8ecf-6981604ebb6c | -9.64 | -46.89255 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e02ee114-9779-391c-9056-099892b32809 | -12.0319 | -46.53191 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60369dfc-bcbf-3b7d-9b12-72c205c08cb9 | -6.53836 | -41.68747 | 2025-10-24 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b2f5c682-8691-3431-8a57-6f42b7ed9ace | -6.40492 | -44.58732 | 2025-10-24 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d796f8b-ccf8-30f3-88fc-8d977a3d4177 | -3.14529 | -50.16198 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fca270f1-5821-3be7-b9ce-b4743a12ab9c | -1.54418 | -55.41336 | 2025-10-24 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2769bc8d-c904-3d9c-a03e-a1e260f39855 | -9.23061 | -45.60622 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56d17ce7-f954-3394-a1e9-c6d299519d89 | -9.76067 | -55.34399 | 2025-10-24 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 206f846e-34d6-30f8-9a65-476827ea3faa | -10.58996 | -49.64428 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec5c9a0a-b20e-3888-97cf-b9ee6fc384f7 | -5.94169 | -46.47566 | 2025-10-24 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dadbc4ad-cb6b-33b1-8ba1-0b30fbeeb502 | -10.02217 | -47.08876 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da2645c6-2021-3c03-a425-e9a5ddfb173a | 0.36272 | -50.93291 | 2025-10-24 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 996f893c-f400-32df-a9b6-245ddedeb059 | -10.60548 | -54.00054 | 2025-10-24 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ecc1d90-967c-3e86-ad48-56f1b919ba0a | -12.27455 | -43.82294 | 2025-10-24 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fd62093-3169-3c5a-afa7-cf97cf5439c5 | -2.86692 | -50.71664 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0536f948-03b7-3e2d-93e2-ab1792b69e0f | -11.58114 | -49.53363 | 2025-10-24 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72340ded-854e-3b74-9e81-64d43038454b | -3.02754 | -49.48825 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd2d1955-de81-37f0-a10d-db3cc9b5947c | -12.25392 | -47.45475 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb63a39a-5fb8-3761-ac72-53867d63ea65 | -11.46315 | -43.70816 | 2025-10-24 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f28e71a-f8b6-3afc-a8bf-311a13e7c96f | -10.46965 | -49.10309 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd1a8853-66e5-3dc0-8f14-30c26fefc24a | -3.82782 | -52.36912 | 2025-10-24 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daca0df2-b285-3b16-873f-de5de8e3e69f | -4.30419 | -41.48912 | 2025-10-24 04:17:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 095c1b28-2202-3ae9-aba5-055200e4b8f5 | -10.01135 | -47.08688 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7859d345-fbc7-3136-b5b0-8639dd217554 | -11.01211 | -47.88076 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e1a4289-b2a7-36b3-b449-5bd3b0a02d79 | -9.60135 | -46.90294 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 401d5144-3403-3f76-9616-386dcda09ef0 | -3.82687 | -44.08942 | 2025-10-24 04:17:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d8764e-e166-379c-b2e4-95e583638496 | -9.9301 | -47.4601 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c22ccfc9-adf7-34ec-9b9b-e11ab3b198b6 | -3.0891 | -49.25426 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dffe639c-e873-36e5-8b97-9e7b2f058c75 | -11.12178 | -47.77303 | 2025-10-24 04:17:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81dc68e7-14f2-3b14-a7e9-154c15be1644 | -12.22008 | -46.51162 | 2025-10-24 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40cc0674-d76c-3f0a-a68b-2c3f00a9e7e8 | -3.13447 | -49.52302 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bede6536-2d1f-3da3-963d-b65c857032b8 | -10.5948 | -49.64124 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06ecdb0d-99ed-347b-905c-bbece2666490 | -8.83445 | -48.85749 | 2025-10-24 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78bf65aa-2b39-3fb7-a7c8-23f68424c7db | -4.54083 | -46.86272 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0b52035-9a0e-38bc-ac16-4772a7576e67 | -11.04928 | -45.40211 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96a15512-23d4-35bf-ae4a-1d7f1ef056f8 | -11.82199 | -44.16754 | 2025-10-24 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b567515-8e18-3837-b89d-207d4101bc36 | -2.58469 | -51.34565 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35796378-5dbe-3bcc-92ed-2c43b7bcfdd6 | 0.36816 | -50.93205 | 2025-10-24 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 68a25ab1-008d-3e92-b474-43412152d0bc | -6.91017 | -41.53854 | 2025-10-24 04:17:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7136382-be54-33ec-8236-8372586b4c59 | -4.54908 | -46.73928 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29d12621-8578-39ed-a7a1-f9203f4cb603 | -10.04159 | -47.08353 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87e84463-89b4-36ab-85a3-025b8c6acb81 | -9.30459 | -45.19608 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0eb09644-c7b6-349c-8a2c-307dbd4bec40 | -9.59858 | -46.91963 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c5fb6eaa-ebde-35ee-bb7b-9f3bfa964d04 | -10.59064 | -49.64048 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5d72772-1781-3cf8-bc36-baa6ac81eefe | -4.24557 | -48.12905 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb33dc66-5cff-3ce4-a4d8-5ee28529e559 | -3.01989 | -49.44722 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b9bb1df2-f4e1-3f7d-a6ff-da2e38d40589 | -2.87759 | -50.71536 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f95c7f4-5a86-399a-bca9-831b6ed2e54c | -5.7551 | -46.68637 | 2025-10-24 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd00a93-689c-3714-8482-c13c0de09651 | -9.63574 | -46.89598 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45f8d0c7-9dc7-3b6f-9517-1d80cdee58fa | -11.98971 | -43.32185 | 2025-10-24 04:17:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec83aa15-110a-3bd6-a007-04050c045cfd | -6.3052 | -41.88414 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a24a627-4ec6-3133-84e4-b593c82be3d4 | -6.90959 | -41.54223 | 2025-10-24 04:17:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
