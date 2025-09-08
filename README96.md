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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4e4de32-885a-33e7-9ed8-6f50c5235252 | -15.0635 | -50.1089 | 2025-09-08 12:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 85717018-cd8b-3b86-a6e8-b52a7df9a49c | -6.1024 | -44.144 | 2025-09-08 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3462c0e6-3ac2-3bb3-967e-77cf3618da77 | -15.0445 | -50.0899 | 2025-09-08 12:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 95dffbf4-194b-31a4-8dd2-a26b2b6c07e2 | -14.2752 | -44.9592 | 2025-09-08 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 648839ec-4341-3a50-b6c7-3bba764000bd | -9.8278 | -53.2976 | 2025-09-08 12:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| ee60cd6c-1779-381f-b1cd-6deaf557da6f | -5.6106 | -44.7078 | 2025-09-08 12:40:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 8a15f4f9-e6b9-36c4-aebd-9d9ac4db4bda | -16.9615 | -45.8411 | 2025-09-08 12:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 1aef562f-698c-32fd-8b78-ac0c5991506e | -11.2007 | -54.9992 | 2025-09-08 12:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fcc1f9d6-9149-3eaa-973e-27ae2ee8ed64 | -11.0234 | -46.0184 | 2025-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 80ed8f3c-8d6b-3525-8a63-d61d75fbf43c | -6.6384 | -53.3566 | 2025-09-08 12:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f5c8ad37-fd71-3337-8b58-5b7cc466ab81 | -6.4683 | -43.1848 | 2025-09-08 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5b2c1763-55a2-3011-a61f-80be30bea455 | -6.2036 | -43.3709 | 2025-09-08 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 420ae74e-6ee0-3318-9c90-0e3a52792c3b | -12.2938 | -50.0121 | 2025-09-08 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 6261c68b-1b09-370f-8950-a06498a05960 | -15.0635 | -50.1089 | 2025-09-08 12:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 19e5cfca-1692-3f29-bbce-8fe97638047b | -12.8223 | -52.8806 | 2025-09-08 12:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a3999cb3-78ae-3978-a1cb-52c2f266be78 | -12.8411 | -52.8994 | 2025-09-08 12:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 0ca25414-8a37-3b45-8e37-cec52bb82145 | -11.282 | -46.5269 | 2025-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6e587cf9-d1f0-3aac-80c6-3eb71b0f3afe | -6.6382 | -53.377 | 2025-09-08 12:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0cf3cde5-7443-32ee-8795-eea6bb2596e4 | -6.1024 | -44.144 | 2025-09-08 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f9077b98-018f-3e55-a542-bcf860ed0142 | -7.2248 | -46.2067 | 2025-09-08 12:40:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 87843816-27aa-3c71-b270-b4b74575b666 | -11.2823 | -46.5043 | 2025-09-08 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| f6c763e6-7a65-3001-ad77-08c358c6d617 | -15.044 | -50.1118 | 2025-09-08 12:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| e502f4e7-9434-37c5-99c3-d1cc4c2b101b | -14.4359 | -48.4644 | 2025-09-08 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 19c28abb-3dcd-39dc-b495-eb93df250b94 | -7.6559 | -47.9593 | 2025-09-08 12:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| fbbc99e0-48e2-310e-947f-56bd8784dafd | -5.211 | -43.2833 | 2025-09-08 12:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 297.7 |
| 78b8ed12-dcdc-3b38-b3ea-b1fe930854f1 | -6.4683 | -43.1848 | 2025-09-08 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 239753f9-1c31-37a1-a709-e2b9967b7770 | -5.7113 | -43.8972 | 2025-09-08 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| ecab8a93-5914-3881-bf86-9e95079dc76d | -14.4359 | -48.4644 | 2025-09-08 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 413.8 |
| 43ea543e-0e6a-3b90-af56-18584937f576 | -12.2941 | -49.9904 | 2025-09-08 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d16c4921-7b21-331a-b259-2bbcd697f7e2 | -11.4128 | -50.374 | 2025-09-08 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 53bec301-3484-369e-8737-67c5f959b647 | -5.2298 | -43.282 | 2025-09-08 12:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 934e4223-0388-34df-a22d-7d9bfd154121 | -11.6723 | -47.1487 | 2025-09-08 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4868a1b7-8818-3906-8546-d63dd2f20d21 | -10.8911 | -55.7131 | 2025-09-08 12:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 0efe01c9-fe49-3efb-b3fb-39a29b1bcd95 | -11.2007 | -54.9992 | 2025-09-08 12:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9ccb6fdb-1481-316f-84c3-86399a241541 | -14.4364 | -48.4421 | 2025-09-08 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3da0cacc-8c16-3a41-87e1-31e962206645 | -11.3011 | -46.5244 | 2025-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 54aa32dd-a455-36ef-8a01-0c38b0a818cb | -14.4165 | -48.4674 | 2025-09-08 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| dc1e6a60-eb34-32a5-adcf-e9d24e0dac33 | -5.211 | -43.2833 | 2025-09-08 12:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 47871dec-bf0c-323e-917b-ede3f0f79965 | -15.0635 | -50.1089 | 2025-09-08 12:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 80f86ae8-e66b-3637-8b25-a05fc56bd487 | -6.6382 | -53.377 | 2025-09-08 12:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 3737c092-82e3-3f2a-bce7-58784bc6bcb1 | -12.2938 | -50.0121 | 2025-09-08 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3302b47b-6edc-334d-8e98-bdff181145ea | -15.0445 | -50.0899 | 2025-09-08 12:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| a4d8b125-336c-3b29-a8bd-6fbf8e740273 | -11.3932 | -50.419 | 2025-09-08 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 149a9b5e-e990-37ad-947b-0f46a4f45334 | -12.8411 | -52.8994 | 2025-09-08 12:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 33210ffb-65cc-3910-821d-588d2f71754d | -12.822 | -52.9016 | 2025-09-08 12:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| d72804f6-3a9f-3751-84c5-92724b0591ea | -11.2827 | -46.4817 | 2025-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 93499cfa-8f80-39ff-97f3-5ac70df67990 | -12.8223 | -52.8806 | 2025-09-08 12:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 6ee07254-c1b9-34b4-97b2-6176c094ec8c | -9.8278 | -53.2976 | 2025-09-08 12:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3b3d2d2f-f17b-3789-a97d-f0ed5d36c2cf | -15.044 | -50.1118 | 2025-09-08 12:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 184.0 |
| ceb509da-4a98-30c6-867d-9011e022881e | -16.9422 | -45.8217 | 2025-09-08 12:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 112.6 |
| f7259049-e57e-302c-8df0-3d9c4c192269 | -7.6559 | -47.9593 | 2025-09-08 12:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 04eb5186-f592-30a3-984b-51ae23891e82 | -11.282 | -46.5269 | 2025-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 206a8e54-a669-3dd8-b958-d60c4f5abd82 | -14.5266 | -48.7833 | 2025-09-08 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4e9d7fed-0223-3ee1-8821-804cb3cc9759 | -11.3014 | -46.5018 | 2025-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 7377a1e7-a559-3e46-8798-0da7a33ece44 | -14.4554 | -48.4614 | 2025-09-08 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 163.7 |
| a8fe8f63-5e07-3ebb-ab90-1511cc83058f | -11.2823 | -46.5043 | 2025-09-08 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 317.6 |
| 9235bad2-4207-3920-a99d-3a171f10ad2a | -6.6384 | -53.3566 | 2025-09-08 12:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| aef1f0d3-e86f-3469-94e5-05192a4f2aa2 | -5.8354 | -42.6265 | 2025-09-08 12:50:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 3298506c-a276-3cc9-a36e-423c4b9b4eff | -6.2224 | -43.3693 | 2025-09-08 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 242df79b-5341-31d6-ad24-0ba6178399dd | -15.2545 | -52.3666 | 2025-09-08 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 210ced4b-0980-326a-94b0-fab1c450634d | -15.044 | -50.1118 | 2025-09-08 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 1d7ef331-026f-3cc1-8a54-63f30c0dc28f | -6.4683 | -43.1848 | 2025-09-08 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 278a1aa6-4323-336c-a2a7-a395da28d215 | -12.2941 | -49.9904 | 2025-09-08 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| af758474-bb46-346e-a548-0814e15563fe | -12.8223 | -52.8806 | 2025-09-08 13:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 4cbb0620-9045-3bb3-92c6-eae7a9ea9b8a | -6.2036 | -43.3709 | 2025-09-08 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ece56a61-1870-3827-8ea1-17d7c6699383 | -15.0635 | -50.1089 | 2025-09-08 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 3e628429-8d7c-306d-bfdd-86ceb09f9111 | -16.3349 | -52.9173 | 2025-09-08 13:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 581420b6-bf15-3da8-8a0a-8660b1fbad5b | -9.74 | -51.14 | 2025-09-08 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0dbcfbb2-321c-3135-b84e-39579ef0da9c | -10.8911 | -55.7131 | 2025-09-08 13:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 4d6580d0-94a5-3aac-bed0-295de48c56fd | -6.6384 | -53.3566 | 2025-09-08 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 1d5457f7-7481-3d6e-82c9-1eee850844e3 | -6.6382 | -53.377 | 2025-09-08 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 975c579e-4eb1-39ad-b010-b66b151eedc0 | -11.2007 | -54.9992 | 2025-09-08 13:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 0350b916-72ab-3af3-ad84-3db6ebdb2198 | -4.8825 | -42.2239 | 2025-09-08 13:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 3d80ad37-bb88-3063-b6a8-1f463daf9a01 | -5.211 | -43.2833 | 2025-09-08 13:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| d9dbeedb-91d4-304e-8dbe-ff50c2e26e80 | -16.9422 | -45.8217 | 2025-09-08 13:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e7241fc7-207d-363b-ae7b-20b85e3afb81 | -6.6198 | -53.3576 | 2025-09-08 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7b978b89-bac2-3355-8ef1-ed9959a47981 | -14.741 | -47.7668 | 2025-09-08 13:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7009eb08-6818-34a4-86bf-c2149549e63d | -8.0592 | -45.4998 | 2025-09-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 955bbfff-e11b-3b98-a584-a947cda8ae89 | -16.3345 | -52.9387 | 2025-09-08 13:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 58ac0e59-6213-3d38-ae49-f35f3d8e48a6 | -7.6559 | -47.9593 | 2025-09-08 13:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 3da146e3-ab49-397a-a33e-c47bc14b13be | -11.4076 | -43.6519 | 2025-09-08 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cb306fe6-9c32-3280-bea8-0fe3f3016376 | -7.7484 | -44.7332 | 2025-09-08 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| f5ea277b-63a6-3054-b38d-c7c259d8c77a | -14.2557 | -44.9627 | 2025-09-08 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b9c994dd-4d6f-3ab6-bbdf-80959f68cfcb | -12.822 | -52.9016 | 2025-09-08 13:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 15d3257e-b0c3-3640-80b1-5a20586c713b | -14.2752 | -44.9592 | 2025-09-08 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| eea0808b-c822-38e8-b5de-d6f2c7334329 | -5.7113 | -43.8972 | 2025-09-08 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 04465cef-d43c-3b2e-bb79-2a022c03dc60 | -11.282 | -46.5269 | 2025-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8126fd78-f455-3a9c-8fb2-89bf7d8fc291 | -11.4268 | -43.649 | 2025-09-08 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 2adaea4d-fa7c-3325-bb38-76e297f4478f | -11.2823 | -46.5043 | 2025-09-08 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 308c1b84-57f3-3d04-9c6f-5c58caedb0bc | -12.8411 | -52.8994 | 2025-09-08 13:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 323.6 |
| 0037067f-b351-3bee-aa90-bf44e71a36f2 | -15.0445 | -50.0899 | 2025-09-08 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 453a12a3-f1d6-34e0-9c44-201ed0b0fad5 | -9.4611 | -46.4566 | 2025-09-08 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 82ca2574-8dcb-3bd0-89f2-ac1b74d1a504 | -6.4683 | -43.1848 | 2025-09-08 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 40c7ec17-87a3-384f-a846-a3e3bdc2a615 | -14.4165 | -48.4674 | 2025-09-08 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 217014c0-ffb3-3446-ae52-ce28b35a3472 | -6.6384 | -53.3566 | 2025-09-08 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 1e8f1be9-0b36-3708-bbc1-ba9e0182a387 | -6.2036 | -43.3709 | 2025-09-08 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| bbfcae28-30f6-3cc0-9bd3-2575c59939e1 | -11.2827 | -46.4817 | 2025-09-08 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d03ff812-161a-3fe2-99c5-df7855d8f29f | -7.6559 | -47.9593 | 2025-09-08 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| a1a06e03-ab18-3dcc-beae-bd947cd87420 | -11.4268 | -43.649 | 2025-09-08 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 7a953119-0f84-3a66-a192-b8aff168aa3e | -15.0635 | -50.1089 | 2025-09-08 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 171.9 |


[Clique aqui para ver as próximas entradas](README97.md)
