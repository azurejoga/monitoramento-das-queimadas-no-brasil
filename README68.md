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
| a717bc0b-aaab-3fd4-b467-1f358f92dcd1 | -10.12428 | -58.01691 | 2025-08-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06eb49f8-887f-3cba-9984-4b56d7ffd7d8 | -12.65421 | -48.22169 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da35fd2f-0a5f-35ab-8e62-2306f7fa8584 | -7.70992 | -50.27612 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96ed4653-cbe5-34e3-b81d-a09f8bfe6120 | -10.5099 | -59.65801 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01b1d5c8-0648-3992-a2bf-d7fb51a59cc5 | -9.58661 | -54.48407 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 991288df-70bb-3aa2-a7e1-dfea07307bc8 | -11.00621 | -46.94834 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e954ce3-5e9e-3b84-a1a1-6168ed9d0532 | -12.62201 | -57.00594 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d3b93d7-f3d3-3150-87d5-e7a7f7394ab5 | -11.01772 | -46.87232 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6949aa4c-bcbb-355b-86f8-b28d1cd92cfa | -14.2751 | -51.88465 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cdf95b71-72dc-3cba-9839-aa78d670a81d | -9.42651 | -62.34023 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fac110a4-0038-37e3-8b39-622eab718dc5 | -12.68166 | -43.16636 | 2025-08-31 04:51:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 260cc0c3-b257-3108-bb42-51e934c9aefe | -8.65559 | -62.44746 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3341f4a6-d3e3-336d-ad18-10e72322a4f1 | -10.70752 | -49.01007 | 2025-08-31 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 109cc1a6-0c26-3484-93ba-3b00425246e5 | -11.31158 | -63.27159 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf7f282d-f824-3d38-ba97-2abd6c8300aa | -13.47739 | -46.94388 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bbbcf599-8bf1-3b2c-bd70-8bce549b6255 | -14.53487 | -51.98697 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 739dd5eb-a399-3cf9-b4dc-72ef2089aef5 | -11.02553 | -46.8832 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf303680-f954-3b62-b57f-dd6a9deb9d63 | -11.30557 | -43.66493 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9674d73d-633f-3f4d-9b1c-e8e47646602a | -7.73058 | -50.25859 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a5d85d02-8a18-3416-9de7-c991d02fe534 | -11.80696 | -46.45445 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b8d8e992-0156-3317-94ab-e956d6a968cf | -7.75368 | -47.44377 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e40f5e01-aafe-3344-802f-37cee7161239 | -11.01714 | -46.86994 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a9ce90d-28ed-3c81-9702-49e97c2d1140 | -10.5786 | -52.01794 | 2025-08-31 04:51:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5a87358-e1ba-3fb9-8984-65bda2f30a8a | -9.95411 | -46.34353 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7eeb708-4e5b-3ad3-8dbe-d524e0801e62 | -11.819 | -46.4472 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 73bd115c-86ae-3327-8c02-6ebe9ca0119b | -11.8843 | -46.73661 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 235b0e0f-fd13-3f26-9a2e-4fd9813f04cf | -14.49496 | -52.98787 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 979eb632-86ae-3bf6-8e2c-4baa691f5efe | -11.06875 | -52.04333 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac971efb-90b7-3a8f-975a-145442a0858c | -11.30301 | -43.66243 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bed085ad-dbe2-362e-b45d-f2449644d1f1 | -11.15434 | -54.30673 | 2025-08-31 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faecdf6b-dbc9-3b87-bb50-14f48a828a27 | -10.94791 | -50.84719 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5e753e34-6a1d-3250-8014-89999f2ec6b9 | -8.92543 | -62.42344 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be53dee4-763e-3ed3-b720-de7bab138052 | -8.42898 | -62.29625 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d8bd181-785f-3a3a-99e9-7ec3564c8875 | -9.44621 | -62.35059 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 388dd4bc-666d-3c88-a715-dc9e4538511d | -13.43449 | -46.94434 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f14a86b-f39d-3862-bc9f-ada58d3d90f7 | -9.45557 | -62.32901 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2041d7ce-bc18-31a5-98d0-89df8aa96085 | -13.35307 | -46.96589 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aff91dda-53b2-31b2-a6f1-c871f1222d4a | -8.92014 | -62.42242 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50fc45dd-ebac-3bf8-88a4-5c8bbff1c5ec | -11.23576 | -55.06687 | 2025-08-31 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52df6cf4-8a92-376d-9453-2287392ab4aa | -8.74452 | -62.38118 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85668954-a372-36e9-a7a6-3f87db5ec3c9 | -8.33596 | -47.41527 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe2fef5b-591b-308c-9641-0890a886b98a | -13.01674 | -56.90408 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24c6da40-bba3-3c85-b789-64d61674a732 | -11.60432 | -51.9483 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 573f2f4d-cbb6-3a30-9480-65ebb9a5167f | -12.75169 | -53.97845 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5713311b-fb28-38db-807c-17726cc91253 | -13.3214 | -46.88017 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d372510-5db6-3368-9e5a-8c4c12adfb88 | -8.74107 | -62.39082 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db35b3ff-42ac-3eab-94d4-4582161bb544 | -11.82977 | -46.43827 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a1e8a8a-6a41-3592-a7fa-4f133b6d92ca | -9.68996 | -48.29745 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe5e429a-df0b-389f-9762-83c14da6fc90 | -11.88144 | -46.722 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 229a359b-926a-3526-b621-d839a38771b0 | -10.99957 | -46.9402 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8252f7e-60c9-3036-885f-bdc6eab9ab94 | -8.6523 | -62.8351 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3607cb12-517c-3a8c-b8fe-2319211f3a0d | -10.75859 | -59.81763 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6576b830-d634-3499-8b41-49dad0cafe33 | -10.94496 | -50.84257 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cebd15bb-cec9-375b-8633-a1568e30d724 | -13.47493 | -46.94614 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32b50cc1-3d16-3a36-b6c1-0d7ce7292d58 | -11.29108 | -43.64273 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df62cfc8-1fb2-3da2-9ad0-d3dd5424e161 | -12.51324 | -53.83175 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 387aae18-c486-37c2-860d-219efeadd99c | -11.91177 | -46.40183 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b560ff38-c382-3747-a921-90cb218aa1d1 | -9.06998 | -65.4483 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6bab58a9-6803-3290-b669-b34e5f388409 | -12.62487 | -57.01063 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e53615c-331f-3165-b8ec-bf9badbfa235 | -9.4386 | -62.36253 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f821258d-99da-35ad-bdac-f1caf2649c9d | -14.54539 | -51.96399 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb8f6796-63b4-371e-a70e-1e4469c1c492 | -13.3605 | -51.74897 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a9d4164-d37d-3a49-9c5b-5be050b4a461 | -12.31203 | -45.72406 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60d3a59a-ed27-39f4-8d0f-4bdcafb87c32 | -9.46247 | -62.35031 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc30e87f-149d-3bf1-b10a-569ce3bac332 | -7.96032 | -46.35247 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10e20663-ba8e-3785-8793-440c676009d7 | -11.32363 | -63.26685 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 698940ff-e747-39b2-9bf9-3c55f011b15c | -10.04122 | -46.0284 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fde3cc9-d140-3f12-b9be-d4abd06cbbd8 | -9.44959 | -60.56775 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4bf5d00-c4bf-3ea7-b2b7-f7ab31f47b8c | -12.55286 | -44.79989 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e576171d-e5eb-3a07-9da3-4cb5894ea685 | -12.43727 | -63.92662 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 897963da-d7ef-336c-b445-5948236fc6a9 | -9.68348 | -47.04086 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 417592ab-73c3-3c59-927d-5f70a3da1cfa | -8.73273 | -62.38588 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 330e354a-5f5a-3644-bdcd-b6c8dad4d447 | -9.44871 | -60.5727 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3364c25-6589-39cc-b8d1-00c8d1012248 | -12.55864 | -44.79718 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f67e644c-9ccf-30fb-bb9b-f2e38ea4370a | -9.69049 | -48.29372 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f2f1217-d1da-3e57-a8a9-bc311022ce9c | -11.06139 | -52.04596 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86bc0a3c-0726-3b08-b9cb-95fd2ff28c65 | -10.67094 | -46.2801 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a563cdf-ff6c-3f80-9f7f-c27541fbad0d | -10.58199 | -52.01845 | 2025-08-31 04:51:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b59fa1a0-5a46-3c2d-878a-43bb97e2fb59 | -12.43657 | -63.93029 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c3785bfa-b5fe-3b52-b751-b1f14923150c | -11.826 | -46.50512 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b14f6bd-0c8b-30f7-bd9c-b7ee3e213f23 | -6.88294 | -56.47164 | 2025-08-31 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff1a1f47-0815-3384-b2d0-312b597cf7d9 | -11.00712 | -46.84726 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 602949e6-45c5-3446-b94c-1a668fc98603 | -11.86095 | -46.45784 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a5dea51-d1aa-3d9d-9770-9acc7724489c | -8.95536 | -50.00921 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d33492f3-7e04-359f-9aa5-f1631b084db1 | -9.68789 | -47.04148 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31ae7df0-b0a5-3948-93b2-6632c90e5be6 | -10.60777 | -54.91563 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22cbd62d-4f0e-3cc5-b74e-f9645bd82b44 | -11.07991 | -45.12825 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 683559b4-aca6-3efa-8e64-38e22470bd20 | -9.44034 | -60.56597 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c75b442-9614-3150-be78-921e74a21d1d | -12.85789 | -48.08475 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1b956cb2-6c23-3614-a13c-4c9f44b346e1 | -9.44232 | -60.58165 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f2cf078-96f8-343b-ab8b-30f685f4a246 | -8.2944 | -46.31684 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05dfb55a-b42b-31b4-97bf-0d1ce16f4acd | -10.52141 | -51.93755 | 2025-08-31 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91aaf3cb-1339-3e24-9609-ca05188451e7 | -9.43112 | -62.34447 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfc5ab83-1b4e-3d35-9fc1-78f3b632f14b | -9.24802 | -47.07311 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2b642a80-b41d-36c7-9659-6fc225401252 | -14.49834 | -52.98841 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de3aec2e-68ac-3aaf-99a3-49ee092f9116 | -9.69226 | -47.04023 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0974da7-e990-3389-8601-8db89427f55a | -8.68304 | -62.41785 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 656e8b57-a02a-372d-bf2a-8194760ac82d | -12.5582 | -44.80059 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84711d6a-a423-3111-a9d6-c44961b68a03 | -13.47264 | -46.96437 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02190fc3-c7d8-3f7d-8e29-0db1315f3738 | -13.35202 | -46.95719 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README69.md)
