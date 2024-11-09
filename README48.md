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
| 71a6a50c-2f02-3878-95de-c64065525e72 | -2.96243 | -48.01829 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11228785-f8d5-3e4b-b703-a4177cbf95c6 | -5.47309 | -41.65003 | 2024-11-09 04:33:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 33be2090-3e0d-38e5-bfc8-1d270ddd6729 | -3.6511 | -50.13987 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ac87fa2-8a16-3696-9f80-66c22014d1a3 | -3.78688 | -51.32693 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d653284a-29d4-3223-ac45-0416f7ae4244 | -2.88297 | -49.39659 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1afb1172-0f86-3e26-99e2-010aaac42a46 | -3.97845 | -46.1661 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5bc492dc-321a-361e-9403-76a93d0a363f | -3.58988 | -47.35773 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4592b981-0966-3f4e-81c4-9556481d4074 | -6.2142 | -41.66214 | 2024-11-09 04:33:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 68dff73e-86db-358f-820b-484bd4948e65 | -2.67421 | -49.89596 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bf8ec4c-f22a-3cf5-a4b4-bb43987221f1 | -3.69641 | -54.61503 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64d10726-904a-331b-bbbe-cc936c1d27c3 | -5.38935 | -40.65099 | 2024-11-09 04:33:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7db3cbd-5911-333d-9770-a847656b6bfa | -3.95787 | -48.99636 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c44648d-a837-398c-b1ac-636bfcf6911b | -6.21097 | -41.62244 | 2024-11-09 04:33:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6a2e6bf-4f1c-397e-bfb8-2bca8e7ecef1 | -2.96575 | -48.0188 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 477759b0-1c05-3497-94b4-bb68cff57c15 | -4.12999 | -46.92403 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 296c3e44-ce86-3bea-8f17-cf116e0eacca | -2.9195 | -49.49559 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4114cacb-2cc4-3691-90e5-d4fc75ecfce5 | -3.81964 | -49.85996 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8d5bb87-4470-3d81-afc0-7433b5a51651 | -3.29202 | -53.11436 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7031a8a-ebdf-38b1-aad4-50d83691f73c | -3.02465 | -51.09445 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45743f37-093b-3e69-85c5-8b290534b099 | -8.11321 | -40.98653 | 2024-11-09 04:33:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a0792a48-3528-337a-8cfc-b528a9d52ed9 | -2.86571 | -49.39391 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b3575cd-aec8-3bdb-baa3-85eac8a64b91 | -3.3299 | -49.10005 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f55e41a-e1e8-379b-8ee0-45154a65fce1 | -2.83994 | -49.46754 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5f089e2-fda7-399a-bb15-b469b144d392 | -5.62956 | -44.83244 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf01bf0a-2f87-3157-a8f5-b2a655f9410d | -2.37775 | -53.84457 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12e9467c-c39d-3b4c-ae05-8d4aed7b1374 | -5.46925 | -43.65234 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c5a645d2-c867-3fea-adb9-70477ae8a056 | -3.686 | -50.19365 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 529c4717-b46b-37c0-a9c1-146eabbe1a89 | -3.25536 | -51.13123 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55a29825-c792-3f98-88c7-083ae78c0c12 | -2.86651 | -50.32563 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c7864b55-8896-3876-bd3c-dab7dff4cfa0 | -3.95152 | -46.40787 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f6c984b-5d28-3976-9d71-b312e3e82fec | -3.94971 | -48.14471 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2dbdce0-7c8a-3485-a55e-a0355bdb0499 | -3.07731 | -50.57507 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff5271f9-48af-31f4-bd01-be2bf4acfcd1 | -5.19585 | -44.92347 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a50761a7-6a1b-30fd-a19f-bf829cb28629 | -8.85145 | -47.68114 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b776066-8a29-3fde-ac13-080774552944 | -4.42837 | -45.69897 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 514529a5-d9cb-3a9b-9452-093708bd6aa4 | -3.24543 | -50.27283 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88b65b24-ed2c-3c4b-a091-735cdf572b09 | -3.0797 | -52.42431 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58f9015a-a9a7-354e-94ab-dda59a858384 | -7.45132 | -43.56957 | 2024-11-09 04:33:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d00bb51e-e2f0-36cf-9b22-2b361739a1ac | -4.75198 | -48.92596 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 609de3b4-95c1-31b1-8206-cae2d71fbe5b | -4.75322 | -43.86078 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad943cc6-398a-3274-9216-86d4a5983632 | -3.03391 | -50.3041 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 77163f3f-3e56-3298-b190-05679ad74437 | -3.97802 | -48.18123 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 02b8d757-7992-3dfb-a156-04181b17d5b6 | -3.09361 | -51.29476 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 202c46fa-fc53-3d9b-94a4-29e4851213ca | -4.05559 | -48.25021 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d516cfe9-c331-3335-a008-5258b723e48c | -3.03696 | -53.27371 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb4a75ab-a982-3c2e-9934-bcf83ea8a4f6 | -3.97085 | -48.18365 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f48119e2-28e1-3dfe-98b9-b11e51a93f85 | -4.43059 | -47.26415 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a2c183e-3a36-385b-a431-edda21fbee10 | -2.61532 | -51.74454 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 828f6c31-c412-303a-8136-8e5c2fc3454e | -6.2382 | -47.27763 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21effb05-4a7d-3222-a7b4-9ed77842bedf | -4.2526 | -47.57788 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 411ac4c7-5252-353d-a68e-14c1fe2785c3 | -2.85737 | -49.22352 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef8aed83-e2f0-39fb-bf09-9d2057187558 | -5.56592 | -46.29479 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ca621ce-c4b9-3ff2-a64f-6cc0728a7308 | -2.87118 | -50.41136 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bf7eb93-fb20-32ef-a7a3-43381a5b406e | -5.59416 | -37.86831 | 2024-11-09 04:33:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5ce4724a-0e6f-381a-90e1-9d816e3dfc83 | -4.06163 | -48.23336 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18fb98aa-200d-3cbb-88b4-c5698a22ed1b | -3.58554 | -51.20127 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 38f8ad69-4fa0-3ed1-9c48-de09a27c3a6d | -4.07018 | -50.01317 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d25c72ab-b828-371f-b758-0bc2ac1fee23 | -2.66071 | -49.8898 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0cc4aa95-0336-334d-9230-000d812ee8d0 | -3.9751 | -46.16559 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9c695085-7ab1-3982-8a7d-aa01544b8b9b | -2.24807 | -53.77488 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 096dc226-b871-3b6e-92a0-acc5ffa14643 | -3.58483 | -51.20578 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4b204e1c-037a-3f43-9e59-32e99bb972a9 | -2.85737 | -48.4475 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2a2bcf6-3844-3433-b610-22b1ff4e019b | -3.96419 | -48.1825 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ffc8ee7c-31cc-304d-aa53-aa97ae59ffa2 | -6.26768 | -44.54627 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 25883678-576c-37da-800d-9bf4cfb71fa4 | -4.08862 | -48.85855 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2548eb1-06b7-3753-a696-fc18b25a465d | -6.12965 | -43.4212 | 2024-11-09 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f7c5e97-6e41-3508-8a4c-d394eadb3535 | -3.84368 | -46.44542 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a507667a-2f77-35d8-8700-ce93bcf01fd1 | -4.20057 | -45.85537 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 19aaad32-b5bd-3335-a0c0-f78f994111a8 | -3.02899 | -53.2683 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a50a33ae-3b24-381a-a47f-c83e9a80aed1 | -2.96737 | -49.28291 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f084f44-a6d7-3b30-9c2c-1a1aeef0f58b | -4.97114 | -46.50009 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aafe0657-4d85-3f36-b0e4-faef708e64ba | -11.09317 | -43.3436 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| c80d592e-9dc0-382c-b975-f2a417b5094d | -4.37683 | -48.17625 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34a4e0cf-9b1c-3457-b04e-688410700ee8 | -3.29131 | -53.24928 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3380f9ad-c5e5-3201-9740-6ee80f8ee5f2 | -5.1994 | -44.924 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d1f3214-372f-3173-92ba-64fe3fc741fe | -3.24121 | -50.27631 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7745643f-6fcf-3e25-946c-e12ba2f01b31 | -4.10835 | -46.88877 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b93bbad0-b639-3e27-8f22-82757cd99fc8 | -2.39749 | -53.86654 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c50ff98d-4f13-32bf-be11-d7cc58229bfc | -3.83999 | -50.04686 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 960a9fc9-5b79-3752-84f9-7b8c335c39d0 | -4.73564 | -48.98557 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b79e0d27-e3b1-3b2f-914a-005876397264 | -3.82026 | -49.85612 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 70275e0a-b852-3584-b00e-be598aac19e5 | -3.60277 | -50.23912 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a7ad17-8369-3e25-9aa1-e59af68a3eb6 | -4.09554 | -48.32127 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 95ad69f3-8c7e-36e6-bb94-d4220450f183 | -6.25161 | -39.71156 | 2024-11-09 04:33:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e7dcfe4-c16a-32e8-8e38-37b998ccf556 | -3.25251 | -49.12146 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 663b0f11-1b15-3a27-a72e-c56717cec116 | -3.23158 | -46.53237 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3abb10e-3d10-3968-9ff7-891d6fddc977 | -5.2376 | -46.66735 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a570eb83-e821-36fe-bc13-ef89f8610ebf | -3.83772 | -50.03845 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31a7a1f9-23ac-3112-bb2d-89b3ffd91b99 | -3.23686 | -51.27272 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cecde259-a893-3206-934c-b85549d59eca | -2.94239 | -49.53039 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d056d065-a8e3-3583-8f7d-f3c3f402df2f | -2.77156 | -52.8697 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 882c8e34-3644-3147-ba7f-52438e6e8225 | -3.60731 | -48.9191 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 684f016c-0405-3cff-8843-bec20429fae6 | -6.23327 | -47.28756 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6723acce-8527-3d04-b8ab-1622207af80c | -4.06009 | -48.30859 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8d2543ef-315f-3836-929f-5435ceaed127 | -3.78542 | -46.14056 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27837b7f-e8f1-38d8-9d6b-d5a5c5cc33c0 | -3.86476 | -46.92484 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9ada046-3e03-3b61-875f-c8c31a55f7f1 | -4.5894 | -48.05761 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7d40c55-2564-3520-a263-af17859dccbc | -5.59224 | -37.86759 | 2024-11-09 04:33:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 01021318-ccbe-3dbd-81f1-83e8bf43d9f2 | -10.83568 | -45.15296 | 2024-11-09 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d1970e8-7d61-3c6c-be28-6fbd139e41ec | -3.0219 | -48.11663 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README49.md)
