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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bfdfa42-7e1a-3ff8-a56c-850e6811a334 | -21.09516 | -57.46582 | 2026-07-01 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63725e04-cb56-34b2-83a8-c7da9ab7b0f9 | -23.56627 | -47.50951 | 2026-07-01 04:42:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f15a1988-791d-321a-b305-4eb7bb76bad8 | -22.43555 | -51.8707 | 2026-07-01 04:42:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c3b2457d-72d7-3e38-87ab-d0d24de7e9eb | -23.40619 | -46.42359 | 2026-07-01 04:42:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 03682e2d-6156-3958-be20-898e115206c1 | -22.8047 | -49.3479 | 2026-07-01 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f472f683-1319-35de-80ad-c88fd87ba65e | -23.81874 | -48.71459 | 2026-07-01 04:42:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6372cbc-a3cc-393e-9fcc-e6314b98bd22 | -21.8135 | -52.71868 | 2026-07-01 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be247669-4dbd-31ea-bf2c-2082ebb99178 | -24.03988 | -50.49933 | 2026-07-01 04:42:00 | NPP-375D | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 411f63a5-7eb4-3425-a17a-ee8772c8193b | -22.69725 | -53.96125 | 2026-07-01 04:42:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 8be4797b-f444-323d-864d-0f92ea2bfdf0 | -21.09414 | -57.47089 | 2026-07-01 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3e60494-0a35-3c76-a09b-a13719a3fb79 | -21.81001 | -52.71798 | 2026-07-01 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0e3cc6e-8f87-38c3-8f49-c82e8af94287 | -22.79126 | -49.34556 | 2026-07-01 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb1cbef-b7d0-3d47-b044-b242ea442ccf | -22.70008 | -53.96655 | 2026-07-01 04:42:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5b03948-1362-3ad3-92d7-dc6872e28fc1 | -22.94704 | -52.58926 | 2026-07-01 04:42:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e8ca0a3b-c772-3f8e-8499-624e124a759f | -22.80134 | -49.34732 | 2026-07-01 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 742b1d1d-a75b-396c-9cf9-6308f3b04bad | -22.79069 | -49.34937 | 2026-07-01 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38114d9a-3b85-3379-b731-b13252ba7b39 | -22.69642 | -53.96583 | 2026-07-01 04:42:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7977f7f5-5f55-3533-8b15-9853ea80fc94 | -22.80076 | -49.35112 | 2026-07-01 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4796f5d-eff7-35e3-aa59-f45ea6caa01b | -24.3176 | -53.59251 | 2026-07-01 04:42:00 | NPP-375D | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b041d912-7c39-3e23-aae3-db3b183d169a | -12.7746 | -44.5162 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b7eb5ccc-494c-3692-abd5-62cd876551e8 | -11.4336 | -56.0711 | 2026-07-01 04:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 05a061d1-b3a2-3a1f-b94a-06400145ad92 | -10.9397 | -43.0593 | 2026-07-01 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ac6bdc9a-335e-38d3-8412-a1849a5b2660 | -12.8548 | -44.3625 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4d6d866e-34eb-38aa-bf1f-3bb1aa6d99e9 | -10.9205 | -43.0622 | 2026-07-01 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| c61a5abe-6cd5-3d9b-aa8c-af1b1c976d87 | -10.6784 | -54.5356 | 2026-07-01 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ec4a5157-4fdb-3f5a-a057-0045a8847fe2 | -12.7755 | -44.4693 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 322.0 |
| 6daf1d5e-c73d-3275-9dd9-58ad1908b802 | -10.6787 | -54.5153 | 2026-07-01 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 56336b42-f5e3-3e5e-87e2-14f61a2f941e | -12.8354 | -44.3657 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 225.1 |
| e7821eb7-69ed-34ba-b726-25796c3b5a94 | -10.9209 | -43.0384 | 2026-07-01 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| fc59e0b5-7937-3813-aec5-490fd28256c0 | -12.7751 | -44.4927 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 410.7 |
| c50c8f34-3d25-321f-b5c2-061c4a7597c5 | -12.7557 | -44.4959 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| c117ea54-80e9-3f3b-8e50-6818411c9f8f | -10.6598 | -54.5169 | 2026-07-01 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9d6839b4-2665-3916-9884-dc3b8cbcb075 | -12.8165 | -44.3454 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 939c6773-d7f6-389e-b335-a0dd59bc56cf | -12.7562 | -44.4724 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| bf695c0f-3844-3da4-bf72-beec880ac8a0 | -11.4338 | -56.0509 | 2026-07-01 04:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 2090e6a8-cdae-3cfc-a6a9-3e9568c8b93d | -12.8552 | -44.3389 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| cd79d9f0-513c-31ce-8f57-5e0dd1f9cc01 | -12.8359 | -44.3422 | 2026-07-01 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 432.7 |
| 7c1fa2a4-bd74-3a84-8aef-ee72eb9bb254 | -3.50681 | -48.03836 | 2026-07-01 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| aa1cf343-844d-332e-a3ae-1fa1e0cdf69b | -3.50375 | -48.03312 | 2026-07-01 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ea3fb4de-364a-3508-9bc0-7b7c126305b8 | -3.5113 | -48.03438 | 2026-07-01 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4480ce43-31fe-3234-9629-de86aa6250b7 | -2.51614 | -51.08076 | 2026-07-01 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5b8038f-4ccc-30ce-9d91-b03ee05bf0ae | -3.67504 | -48.98436 | 2026-07-01 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41653224-3ab0-3fc3-bf76-f8d121db9543 | -3.51508 | -48.03497 | 2026-07-01 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef57b0bf-eadc-3852-aec0-9ae6aba80056 | -3.50752 | -48.03375 | 2026-07-01 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| da94b7fd-f5ec-3af0-b7c5-7cdcb128a3d8 | -3.7118 | -47.1688 | 2026-07-01 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ad41beb-e450-3c85-abb3-0914fb350d31 | -5.79314 | -43.88645 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae1a8c3a-29f4-3b7d-b1f1-9b7c7135a581 | -10.81002 | -49.33623 | 2026-07-01 04:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 289c9829-4df6-380f-8ec3-66b7f45b09ab | -10.92905 | -43.03953 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75117383-9ef8-3d4c-808e-46f2dda35fdf | -5.78923 | -45.03559 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f3ce568-7587-39d9-9204-a7a7744efbec | -8.12148 | -47.87941 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46c2deb2-690f-3477-9606-5197c2459559 | -9.17626 | -58.0598 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b81c619-235c-38e5-b754-9eaa4fd5b10a | -10.91731 | -43.04774 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 033b1b36-fecb-35a8-8a9a-9893cd94fb5c | -5.81139 | -43.80337 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00a69f67-2559-32fd-a822-e4aef646d976 | -9.16776 | -56.9402 | 2026-07-01 04:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a219e2b4-354f-3d76-a3a5-8c58dab9fd47 | -9.60496 | -56.92706 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45322672-7ef3-3a6a-b33b-e6a5d68675e0 | -8.59619 | -48.01474 | 2026-07-01 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0c36ef6-6630-314f-ad97-7df3790a6a5d | -9.09141 | -59.49426 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1ce2041-f597-327b-a8aa-32e221ef729a | -10.1275 | -52.09008 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e00b81c1-e577-3f6f-b06d-ab4cde9d23fe | -9.88401 | -50.39522 | 2026-07-01 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6132cfb3-b497-349b-a89e-78a92bc370e7 | -11.5444 | -47.45852 | 2026-07-01 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a428ecde-cb7e-3b28-a89d-22bbeafea24f | -10.12412 | -52.08954 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 622224c7-5677-3037-b58f-ee769ff039f5 | -5.55664 | -43.96325 | 2026-07-01 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 257b49b8-4b2d-3914-9ebd-3b78dcc233de | -8.50585 | -50.42825 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 736b074e-bbfa-38df-a318-83c44f29e604 | -10.92265 | -43.05271 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 221e5cb7-beb1-3382-b058-04e0362496a5 | -8.59247 | -50.97586 | 2026-07-01 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53665fae-77cf-38e5-aef8-f846a6bf43a4 | -4.35095 | -47.76563 | 2026-07-01 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b38464c4-77d0-3363-be7e-3a2cd83c04ce | -9.88698 | -50.39994 | 2026-07-01 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 775d8ef1-e51a-3483-9c9d-a459972358f4 | -11.5488 | -47.45921 | 2026-07-01 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1eb6009c-d107-3364-a9c8-c6b0de58309f | -10.12583 | -52.10099 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3bc37e74-592e-3d3e-aa00-beae4e7aafb8 | -9.19032 | -45.3235 | 2026-07-01 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bb82c59-8e8c-33e4-818a-20a35bc19876 | -9.75208 | -49.04018 | 2026-07-01 04:55:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59c11b56-37f2-3762-bf71-8f36c21ee403 | -6.83492 | -49.27774 | 2026-07-01 04:55:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f087d31-f4b7-30de-b891-35491a0c1591 | -5.79903 | -45.06885 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baa170bc-859e-3f05-8f67-0c33cffc5fcd | -5.79402 | -45.03625 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 380c9cae-3925-38d5-84b5-c7262cca3fa6 | -8.98436 | -45.72117 | 2026-07-01 04:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ead2cc0-eaf5-350f-b5cd-a01be8ba35d5 | -10.92853 | -43.04378 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56951203-37aa-30c0-a0cb-a2319a0ce838 | -5.55107 | -43.96547 | 2026-07-01 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 345f44e5-9278-3dc1-ba2b-c9dfe0f8ccb4 | -8.12895 | -47.88436 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b24ac7d-79cd-3f68-98bf-ce0888eba60f | -10.92111 | -43.05582 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 0134ea30-f353-3277-b58f-4b3852e9c049 | -8.12501 | -47.88366 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caaa535e-c1b6-3dd8-a7dd-6f5a53866171 | -9.69149 | -56.10235 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e67de13-0366-37bf-abbe-b28161c86139 | -10.12357 | -52.09318 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3e158823-e740-3a70-8131-b406beca6673 | -5.8065 | -43.7956 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ae765de-e50d-342c-893d-6556760510f7 | -10.92157 | -43.06122 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fa5ee47e-71cc-3839-8754-370a8311d364 | -8.50577 | -50.42713 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f18d8c92-b4c9-371c-87c2-703aea1887ac | -8.6526 | -47.77061 | 2026-07-01 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae11da27-9826-32f2-b60f-514607df95fd | -9.08959 | -59.49484 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82ae629e-59ee-33a5-9749-f8f1b26da627 | -8.59776 | -48.00388 | 2026-07-01 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 80d84273-8e58-3f06-ad0f-268e7f522488 | -10.92482 | -43.03574 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af4e19d3-e9e4-35af-9edb-38a605e58bbb | -4.34707 | -47.76501 | 2026-07-01 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74ad8c42-4686-39a6-8294-0811659dece0 | -6.8464 | -47.93381 | 2026-07-01 04:55:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d47faa3-ac23-3bee-93cb-2b9ff61096b8 | -10.1202 | -52.09265 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95c48179-f142-3fd1-87a8-2839a80fa667 | -5.79979 | -45.06363 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f704f9d-9cbb-3d71-9d2e-3214f6deeb40 | -9.18719 | -58.0669 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deb143c1-e2ed-3228-97ab-6c88042304d2 | -9.19526 | -45.32415 | 2026-07-01 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8adb597-f1ec-3d73-b8a8-76a134ff31fb | -9.60934 | -56.92337 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db4539e9-2fdc-3470-9caf-47e0d9ea4563 | -10.91677 | -43.052 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| c45dd905-e3a2-308e-bdcf-9f56f58d0d3b | -6.95823 | -44.55258 | 2026-07-01 04:55:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5681d378-72d2-3e3f-a909-4852fd41fa3f | -9.08875 | -59.39648 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e75f7a0-aa00-391e-ad0a-d408a30fa946 | -7.48055 | -44.759 | 2026-07-01 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README21.md)
