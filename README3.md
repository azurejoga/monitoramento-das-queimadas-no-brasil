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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8227ad7-93f0-3324-92d7-92658b8eeda2 | -20.956301 | -56.6138 | 2025-05-20 02:00:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 80b6c8f5-55b4-333b-8276-36b85bb34504 | -20.961 | -56.5933 | 2025-05-20 02:00:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f2425a07-d7b6-3b77-a50c-82a8aaefe240 | -20.9659 | -56.610901 | 2025-05-20 02:00:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bda1447b-3aab-3880-9b3a-bda1fe3c7289 | -20.9597 | -56.6179 | 2025-05-20 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9caa70a7-ab35-3227-a95e-2584185a4168 | -20.9601 | -56.5967 | 2025-05-20 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 19909a69-eb8e-3fae-b10e-c7e945a32f19 | -12.424 | -43.7274 | 2025-05-20 02:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 272ab42b-7371-3054-bd58-397c347ca8a9 | -20.9597 | -56.6179 | 2025-05-20 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c734410b-7194-3e40-8142-9e88cddee9e8 | -6.2226 | -43.3459 | 2025-05-20 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2beabcd6-3a04-32bc-bfb3-291b28b75776 | -20.9601 | -56.5967 | 2025-05-20 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 92fd409c-8f29-30a4-8128-99db3eaa0bb4 | -12.2946 | -52.4785 | 2025-05-20 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 946008a4-48bc-3b87-98be-57baae6868cc | -12.2946 | -52.4785 | 2025-05-20 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0e3e223d-e481-36f0-bb4b-53874915a506 | -20.9601 | -56.5967 | 2025-05-20 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 63fdea1f-9a53-33be-a67f-a01092e0b39c | -20.9597 | -56.6179 | 2025-05-20 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c96bac8e-6f35-3abe-9360-d52d3eef8011 | -20.9601 | -56.5967 | 2025-05-20 02:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 265771e7-b066-3a72-ab02-3c2e9b1e1997 | -20.9597 | -56.6179 | 2025-05-20 02:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 39523f71-ebee-3736-a96d-6826bd340542 | -9.4383 | -40.3668 | 2025-05-20 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 637b07af-36eb-3e76-87c0-f61c317fb360 | -20.9601 | -56.5967 | 2025-05-20 02:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 66.6 |
| cd0aec6e-25e4-329d-a493-e5dcf735eb0e | -20.9601 | -56.5967 | 2025-05-20 03:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8323d364-1317-390d-b193-31a690d9c97e | -20.9601 | -56.5967 | 2025-05-20 03:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 10018b12-5bd4-352a-8231-b57c4bf7c9d8 | -9.44138 | -40.37978 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cde1b93c-04f9-334d-a4c7-9c647f3c07a7 | -9.42958 | -40.37754 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f82add11-3189-3f20-a481-bc0da2c27ed1 | -12.42497 | -43.72489 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 341019f4-938e-3810-8a17-3f6a2c05fa79 | -13.02578 | -45.06907 | 2025-05-20 03:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 732b38d6-1ec0-3b58-855a-42ed58d6065f | -9.43548 | -40.37867 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| df849fee-4d29-39c3-9ece-960a2cc41e5e | -12.43197 | -43.72635 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a3649155-8aef-3a8e-b5f7-ac8227299d64 | -9.43164 | -40.37957 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 54c1860a-eaf1-3dca-af13-32eaabb9be09 | -12.4306 | -43.73277 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 86a3ba9f-b832-3ee8-bcfb-1d1e30b15595 | -9.43835 | -40.37639 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ae06002d-3f92-38e9-ae69-3fb869cc3def | -12.43176 | -43.72655 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9382aa37-ebc5-3abe-9c08-24553bacc5db | -13.03303 | -45.07077 | 2025-05-20 03:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e1859ff-a467-3e15-9bd6-9883f923f5cd | -12.42364 | -43.73129 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76e94606-a37a-3413-a55c-ce42503fb658 | -12.43876 | -43.72799 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9872d736-610c-3f57-a48b-032962e38847 | -9.43754 | -40.3807 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cbcbd17b-7b3a-3989-8908-3d1bf0522db7 | -15.20735 | -43.8256 | 2025-05-20 03:19:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 112e01d0-0a45-3544-be0d-a82fad8524db | -9.44221 | -40.37549 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 04b5f863-7f46-380d-987b-7ee6c69718ee | -12.43854 | -43.72822 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93904cee-d76b-3590-b4bb-07ecb4776284 | -9.43631 | -40.37436 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5dfec44a-7eea-3a9c-a6ba-4977ef2281f8 | -12.42517 | -43.72472 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| af91decc-c033-37d0-b6ea-55b344e60ec5 | -15.21389 | -43.82707 | 2025-05-20 03:19:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9db6873-4557-3635-8e60-8c47517d7ec0 | -13.90013 | -43.80007 | 2025-05-20 03:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 301d4fbf-824a-3578-9ce1-052309ae6413 | -9.43245 | -40.37524 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 158a45af-49ad-34f6-82a8-16e4a06075cb | -12.43043 | -43.73298 | 2025-05-20 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb871d19-e2a7-3aba-b0d7-bd668a067e29 | -9.43042 | -40.37323 | 2025-05-20 03:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8c1a6506-036d-3dfd-bd0e-dc23ed3f15f9 | -13.90679 | -43.80164 | 2025-05-20 03:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bea2bb7-9f70-3b6f-92d1-5bb448675680 | -20.9601 | -56.5967 | 2025-05-20 03:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 35.7 |
| a0aa1a0f-125a-3153-829a-84bdccb63f42 | -22.67741 | -42.85907 | 2025-05-20 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ad54161-c77e-3f53-b631-31d2c7c85056 | -17.80363 | -44.34536 | 2025-05-20 03:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5586c4ef-3609-3fc1-8458-1eb1122afd94 | -22.67823 | -42.85543 | 2025-05-20 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 887fa3bd-c2a6-3105-893d-619cd50d77cb | -22.34195 | -41.7838 | 2025-05-20 03:21:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6cc7b793-01c3-3129-b6ee-9df31e7e74a0 | -22.34127 | -41.78698 | 2025-05-20 03:21:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| da2a11ca-7ae5-30a4-ac76-c205b158dd50 | -19.71691 | -40.35563 | 2025-05-20 03:21:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d94a901-0785-3cbd-9d15-f1188a6d382f | -20.9601 | -56.5967 | 2025-05-20 03:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a57eacad-8ad0-3764-bb7c-44f30393fb54 | -5.97412 | -43.76231 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 11e76141-4642-3f1e-aa92-4fb5e34bc688 | -7.06477 | -44.93208 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ff78e870-eaf3-3f98-a2a8-21d6e6f70860 | -6.22729 | -43.34977 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80433251-0fe5-309d-80de-3df5625d6dab | -5.96841 | -43.76447 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 552bb607-3def-3f3f-a055-4ce471144ac6 | -7.06192 | -44.91668 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5fbcf8be-abd6-3cfa-b76f-86f021e6ae06 | -6.20419 | -43.33432 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| afeb7958-7a76-3eff-829a-20b1c1961170 | -5.97358 | -43.76537 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd87bd1d-d73c-39bb-88d4-a22ed97b2cf7 | -6.23035 | -43.36203 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 585204ca-9f35-39eb-81ef-871df2c53ce5 | -5.96831 | -43.75766 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f818af8b-f870-356a-8c24-5ce24a4c9580 | -3.07978 | -40.07944 | 2025-05-20 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d8dfe932-cdbe-35f3-9508-7abf2e51d778 | -5.78407 | -43.61555 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65b5d459-3d1a-32a0-bfd6-bad37afe3e05 | -6.23181 | -43.35346 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9ed9cf00-33d9-3885-9239-2f6fdc78eb49 | -5.75631 | -43.48812 | 2025-05-20 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 808d91a9-17e2-3a43-8ad9-7734f53a228c | -5.96778 | -43.76074 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 242135ea-f2a1-30c6-8b5f-5928e3f3f028 | -6.31676 | -43.74706 | 2025-05-20 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daabb922-e154-3c20-80ca-f37c59b57d2e | -5.9752 | -43.75622 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3779de66-7ddc-3d5c-ab69-a13dda96fe8a | -6.23133 | -43.3563 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| af4c805b-505a-3014-8a51-aacdfa59755c | -6.23533 | -43.36306 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1c20a8d2-ce02-3f64-a5bd-ab876fc94d84 | -5.97466 | -43.75927 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b37ba2e5-3fb6-3c08-8c0e-3bb7d077b451 | -7.63686 | -46.11936 | 2025-05-20 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8986509-3cbc-3096-932f-33722aab569f | -5.96263 | -43.75977 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6d02166-a051-35c9-9c5d-e5918aad46fb | -5.76653 | -43.48967 | 2025-05-20 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2362796-4b5d-3bbd-b05c-703e841a1981 | -6.20521 | -43.32839 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71ba480d-2ab4-378d-becc-97dda6f4b85b | -6.2047 | -43.33133 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 83d3b914-b13d-3b84-8000-b6dad6569850 | -7.07034 | -44.93262 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9cf48c8-558a-3573-ae89-55564870f94d | -6.23276 | -43.3479 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8a3d4e5-0bdd-3308-b9f0-e11c389413a8 | -5.9638 | -43.76044 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efd021ae-d728-3fc5-8227-e5c6092cfcfa | -5.75579 | -43.49115 | 2025-05-20 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f532542b-869e-3578-a176-c4136b1cac1f | -7.07296 | -44.91814 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1436b311-f0a2-37f8-9159-fc41b8866391 | -7.06745 | -44.91734 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 440b7a19-22eb-3d0f-aa44-f3c08ce8b5d8 | -7.631 | -46.11828 | 2025-05-20 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13602c4a-84ab-350b-b96e-5d801d2d64ab | -6.2057 | -43.32553 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| abb51a6e-333d-3d6b-8cda-fc4d6026fbad | -6.23485 | -43.36592 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59f70235-8d94-34bb-ae9f-b745696c6ad9 | -7.06159 | -44.91714 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cde2c2f3-ce19-35f6-8b9e-36b019e55438 | -5.76601 | -43.49273 | 2025-05-20 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f759785-6cbd-3497-81eb-9c68a0e79e11 | -5.9695 | -43.75834 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf796b96-15e2-3fed-9518-5d56f869affa | -6.22632 | -43.35542 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b01bb9bc-cd3d-33ac-9095-09e39db4dee3 | -7.06548 | -44.92821 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 66b60329-916c-3f8a-b402-01818ef4dcf0 | -5.96435 | -43.75732 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffcaf0d7-072c-35f9-87fb-e4c2afce3df1 | -5.75527 | -43.49418 | 2025-05-20 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ee20221-1b2f-3252-a645-d24236d16314 | -7.06681 | -44.92089 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e1978417-3aa1-399f-8b16-5c0571ed2087 | -7.06615 | -44.92453 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb561937-39e2-3306-8691-1d2c19210bc4 | -7.07231 | -44.92171 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7022d30c-2844-3016-ba22-83619d9413a0 | -7.07166 | -44.9253 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 134f912e-e479-308e-a0df-3970f21b681e | -5.96896 | -43.76139 | 2025-05-20 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27213e65-6e38-3c5f-acdd-bbb475ecb3f8 | -6.32194 | -43.74765 | 2025-05-20 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eae2bda-e923-3752-98c3-3639aec52786 | -7.0681 | -44.9138 | 2025-05-20 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1f6893b9-7041-36ec-b6a2-3755cd35c378 | -6.23229 | -43.35068 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README4.md)
