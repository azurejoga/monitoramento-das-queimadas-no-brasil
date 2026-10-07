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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd67257a-dd34-3714-9394-710f8ca9be40 | -7.75243 | -43.83512 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c9fc6d5a-e45d-3f7a-9c9f-737bebdc4854 | -6.93338 | -45.2877 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a21d961f-8b13-3981-9145-ba8773fbc414 | -4.57236 | -40.72235 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| b2b59fa3-0b21-381d-8bbb-3684741f3de3 | -7.17717 | -44.31438 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ab1c31e-3578-31ba-91cf-3728a9888250 | -5.72347 | -41.72289 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 4fa7cf07-9b8a-3670-8bce-ae35c5520d19 | -5.95092 | -43.03212 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0b4fcd4a-6fe8-38d4-ac9a-305f215a14ba | -5.74271 | -41.67579 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 2501d300-14bc-366c-87f5-fa491f7a23b1 | -2.97696 | -42.73908 | 2026-10-07 16:03:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b1f6b964-6aac-36a5-b695-451bb7032efe | -5.94369 | -46.39284 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19e02a8c-3bb1-34e1-9937-1e6fc8738823 | -6.68733 | -45.35469 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 279.3 |
| 689328cf-94c9-3bbb-ac7d-095634151ae9 | -7.47581 | -42.82166 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 4216827a-7859-3f6f-be6a-cc56761b6f7e | -7.84518 | -44.20589 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2cc4f314-cd01-3401-aae6-10b00110ef4b | -7.00203 | -44.15487 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4eaf5e8-8d75-3f83-bee5-d29e7a77f15e | -3.53363 | -39.50536 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4b6c25ec-f0fb-36c7-a08c-aec0c9da605d | -5.26253 | -47.93251 | 2026-10-07 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 07685861-40d1-39d2-a3f2-e08696aa8cd2 | -5.4808 | -44.25495 | 2026-10-07 16:03:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3bcead35-fcb2-3252-957d-bfe8deca246e | -6.43607 | -38.13999 | 2026-10-07 16:03:00 | NOAA-21 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 25c6bf02-5fb2-333d-8f65-0fc1c601d898 | -5.97324 | -40.94389 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 424aa9fc-41b5-3053-9610-e94a321ce44e | -3.65745 | -50.94699 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ba9fa2d2-1ab1-3061-b7eb-db9ee7c21c63 | -3.29701 | -39.51343 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7b0a0b88-4596-3dfc-b1fb-2c5835040410 | -6.84364 | -39.55603 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 3aca9d08-4723-311f-838c-28c6fd0bf4aa | -7.28065 | -46.1529 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebd9894c-d52c-3dcd-8842-de5a63d0608b | -3.81264 | -49.11538 | 2026-10-07 16:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6353cfd6-6e8f-3c59-b946-1503444c339e | -3.96337 | -41.53967 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4108a3bb-75c4-3ac7-ab54-51eb47ffa90f | -7.21504 | -44.2953 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 97c31c5d-3a2a-3986-bd9b-cd9a78775b5c | -5.25651 | -47.92961 | 2026-10-07 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d8fbc506-8765-3ca9-a1cc-d4377df2285e | -8.01315 | -47.17376 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f306e32d-21da-316e-8945-b20b4eb28c7f | -6.9456 | -45.30667 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c1292892-4143-3f25-a918-0aee18b697e3 | -6.48101 | -46.62305 | 2026-10-07 16:03:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f744bbc0-8f3c-3041-80b5-e815269b19d0 | -6.63824 | -43.7752 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6071fcc6-a24f-3bc0-aa46-be86c5b0d888 | -4.30428 | -50.78516 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3cc798d6-d2d7-3e5a-9f78-ab2cd1696fe6 | -5.96896 | -43.87196 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 515680db-005c-3f14-9c86-23d8911b7a55 | -7.2947 | -47.27786 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b7e2aff9-5f7d-3f64-b906-8032eb19e198 | -6.93742 | -45.28208 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 7ba217a5-f3de-31a4-bf0e-748682b891db | -7.47128 | -42.81865 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 427e774c-71b3-3c8c-bdf5-454506c1ed82 | -5.96312 | -40.94942 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 41b64d0d-0d22-32a2-a20a-b65df6300d00 | -3.82756 | -44.54473 | 2026-10-07 16:03:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b88bba7b-bca6-3e33-99e6-fa5c79d394ab | -5.96008 | -46.36409 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e917ae2c-58c9-31fe-b09d-88ac9ab82a86 | -5.72581 | -45.15012 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| e64393e5-76cc-3c5b-8689-217daab3be95 | -6.03129 | -43.76387 | 2026-10-07 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6ed9484f-421f-3016-b858-85036e4872f4 | -3.57064 | -45.21388 | 2026-10-07 16:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 927111cb-b1d9-3b5d-ae87-ee27951b37a0 | -4.58263 | -40.76744 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 97ce509c-c877-3c8b-a439-42a858fcac3c | -7.47482 | -42.81464 | 2026-10-07 16:03:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 72a9f020-04fe-3be4-bacc-ccc46618d11a | -4.08454 | -48.90418 | 2026-10-07 16:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7c9abf73-297f-38ad-8ee1-9834e44a662b | -3.18396 | -50.56435 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3965604c-e492-3b0c-80fd-c30b0a71aa2b | -3.89176 | -44.12712 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 4000f9f3-d4ca-3faa-8cdb-7a73c01b9547 | -4.28927 | -38.90817 | 2026-10-07 16:03:00 | NOAA-21 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fbad17ba-9a47-3fc8-ae32-ff43c865ef70 | -4.05709 | -42.21409 | 2026-10-07 16:03:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 223c16c4-cf23-3a5d-82d3-554bd8574936 | -6.94826 | -45.2561 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6b297229-f3f8-3443-88d4-50463161fdf6 | -3.73892 | -39.53722 | 2026-10-07 16:03:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bf3e522f-c47d-379c-843d-64ea3709f4e5 | -7.28104 | -46.15582 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67352383-dfd2-3294-bfe7-6600f569ba28 | -3.68656 | -38.81287 | 2026-10-07 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4230d895-92ff-37b0-8318-6fba34a39cfb | -3.86489 | -43.02625 | 2026-10-07 16:03:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 636d756c-385f-3164-bdcb-620a089dc494 | -6.55574 | -35.50774 | 2026-10-07 16:03:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a14546e8-3b02-3fb5-aa82-c340765f76ae | -3.80734 | -44.60545 | 2026-10-07 16:03:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9f4b1d0d-f5af-3b6f-99c7-9d02be896cc2 | -3.83773 | -42.63725 | 2026-10-07 16:03:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 14396e32-0250-34be-a45a-be73aa1772de | -7.80693 | -44.58907 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5120371a-6739-334b-b179-7a8eb21741e8 | -7.26197 | -44.21534 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0ee7cb7b-872a-38b3-a9f5-4f8e91dd29c7 | -7.11096 | -42.537 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1b07907c-c422-3f13-b030-d7d85eae26ae | -3.30587 | -42.47267 | 2026-10-07 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 378af595-1d39-31b8-ba42-47eb4e355ffd | -7.22009 | -44.29897 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed86f98b-5534-37ba-8c4a-d371eb658eb8 | -6.69277 | -44.96574 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2062457c-52d8-3dc8-956a-24d59794d019 | -5.20262 | -48.33798 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d67f97e9-463c-3ed8-8223-d951bba0684c | -7.56095 | -46.72419 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9a558b00-a717-3875-8b1f-b2ce307f506c | -6.13679 | -44.64751 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0cc48f3-0941-3c53-939d-d8f68b2e32a3 | -7.20751 | -45.09164 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3899cd9e-d0e0-394c-bb0d-ded58d9213cd | -7.47636 | -42.79658 | 2026-10-07 16:03:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d2e31850-a938-324b-8f1f-2be49553cff7 | -7.81541 | -44.58321 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 692d9ab9-f951-369c-bc7f-e5812379c919 | -7.73328 | -45.45567 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| daef8dd8-ea4f-3445-83ed-b41900f7c977 | -1.22389 | -49.04158 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a3c55151-3b93-39ec-8ef7-14afac6f2608 | -6.04406 | -42.58951 | 2026-10-07 16:03:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 37c4ec98-c8de-305c-865f-0fbdc0da499f | -3.83792 | -42.64077 | 2026-10-07 16:03:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8335cf93-9db8-32ca-a711-67ec21ecb921 | -5.72646 | -45.15479 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 67fddef5-1478-3857-b5df-2ef497a1426d | -7.60458 | -42.37319 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| f2347f00-7542-3558-b6e6-74fa5f845c4c | -5.36235 | -36.98856 | 2026-10-07 16:03:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 48fd9422-1420-3b45-a28d-fc8819f6c9b9 | -2.2755 | -48.75405 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 97c39d1a-72b5-3789-b7b5-48a8535d6871 | -4.77088 | -43.741 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8583fc10-90fe-381d-b9cd-c196e126d06f | -3.28273 | -42.26635 | 2026-10-07 16:03:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ddba047c-b278-3508-b0af-3b45b8d9438f | -4.84949 | -43.36376 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 32a4f327-d60d-3aa0-83cb-5851f522b683 | -6.93515 | -38.295 | 2026-10-07 16:03:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 054f6fd5-bbe3-3415-a6dc-49b4ad10579c | -6.99681 | -45.12524 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| eec29853-0d2a-3c67-9f08-0db09ab14b9d | -5.93907 | -46.39639 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70660115-f349-34dd-a88a-2718df0f47c8 | -3.75922 | -40.743 | 2026-10-07 16:03:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 53686ef2-0b3b-329e-92fe-4ba8d0cf569d | -5.97253 | -40.9398 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 61069969-e442-3c9a-b076-817c94047683 | -6.97864 | -40.03526 | 2026-10-07 16:03:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 118.0 |
| b2b36f40-620d-3c51-9082-29fc001283bd | -3.5455 | -50.10775 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3ea7452b-179e-3c57-8cbd-39739d5ae6aa | -6.13407 | -47.92514 | 2026-10-07 16:03:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3c1ad769-2fad-3556-bda0-a2b56f38153e | -3.54402 | -50.09788 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a8539035-fd4d-3a73-bbd8-2023d48ca912 | -6.70467 | -44.98382 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| be14235c-f057-38b0-9c93-468318fe978b | -6.23061 | -44.84153 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f14995f0-3e6c-3340-b1ef-63f92971f710 | -6.94052 | -43.06284 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c1f23f4-1022-399b-aec2-88047c46d32e | -3.70566 | -40.83166 | 2026-10-07 16:03:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 255.1 |
| 7b967695-5b7e-3306-b186-66c133ebedc1 | -7.7717 | -43.81572 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 5f265dbb-18b3-3e4a-8f09-5247eaa90d49 | -3.30033 | -39.51294 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fa55c96c-d0d1-3f5d-a083-6b5055621eca | -3.9598 | -41.5402 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 827999cf-03b8-3717-ac0c-6ac83b3991b1 | -3.20871 | -42.96339 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b27085b6-8d6d-3d4f-83de-4b4ead654a81 | -6.99212 | -45.12576 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| a8311aca-3377-3ef9-a94b-527cff280f84 | -8.0091 | -47.18489 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 413f90cd-5fd3-3ed5-94d0-3a6f73de2712 | -3.53782 | -50.09865 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5e116b37-dc7c-36a2-bf4e-3d7b409a6885 | -7.80363 | -45.5009 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README164.md)
