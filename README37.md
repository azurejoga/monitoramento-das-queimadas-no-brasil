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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8303f13e-c022-3739-976f-9bd098a8407f | -18.6586 | -57.2759 | 2024-10-06 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.2 |
| e93f8c0d-28f6-337f-9ce2-fe50d7571f21 | -18.659 | -57.2552 | 2024-10-06 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 295b87fb-23b6-3211-b43b-8a42663b908f | -18.7165 | -57.372 | 2024-10-06 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 43ea116f-1241-3537-a698-fbe75f9582aa | -20.5813 | -49.3865 | 2024-10-06 02:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 167.6 |
| d71350c9-f784-33c3-b919-d3b39cfb7964 | -20.582 | -49.3635 | 2024-10-06 02:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 7cdc955a-be11-35e7-8f92-1b1bc554ab02 | -20.6018 | -49.3821 | 2024-10-06 02:37:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 26472c1e-b501-3a42-acae-4a075925f781 | -21.5218 | -50.9088 | 2024-10-06 02:37:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.0 |
| d447987a-3d65-328c-bae3-76e6fa284370 | -21.5224 | -50.8862 | 2024-10-06 02:37:05 | GOES-16 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| ff0fa477-9f9b-38d4-aa70-cd5fe343e19d | -3.1129 | -48.6131 | 2024-10-06 02:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 1f01afa5-2ea2-3b93-8949-60ee0d7c2c4e | -3.1314 | -48.6125 | 2024-10-06 02:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| a4daba96-69c1-31ff-a2b7-bd1acd19aa92 | -3.1315 | -48.591 | 2024-10-06 02:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8ac89b8b-aea4-380a-8001-6c401c01d6c1 | -3.4195 | -50.3844 | 2024-10-06 02:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1c8904d9-67a7-3791-8e24-6fb9a536f396 | -3.8008 | -41.5989 | 2024-10-06 02:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 5e22ea21-5882-337a-9c0d-ad28ff029d02 | -3.7934 | -49.4849 | 2024-10-06 02:45:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2f327028-1dea-3396-a9b1-bfae179a5de5 | -3.7935 | -49.4636 | 2024-10-06 02:45:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 87b9685f-75cd-3694-af1b-4888d62da9e9 | -5.5718 | -44.87 | 2024-10-06 02:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| fcf6c9c6-092d-375c-9158-5952b9b3fce6 | -5.5905 | -44.8687 | 2024-10-06 02:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| fd269644-7b53-3460-9289-4d6f0a42214e | -7.9825 | -54.7752 | 2024-10-06 02:45:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 57ae825a-65d2-387f-ac67-f35a8c5120a2 | -9.1573 | -61.5803 | 2024-10-06 02:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 22b1ea73-49b9-310b-bfae-0a6b314a57e8 | -9.1759 | -61.5794 | 2024-10-06 02:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| b1caa715-e172-35e9-a9c2-045ed50ea909 | -9.3464 | -46.5589 | 2024-10-06 02:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e50d0f80-914f-3077-b3df-a9820d5bfe36 | -9.3467 | -46.5365 | 2024-10-06 02:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 5306ee5a-1c27-35fe-a5b2-0cdf25148dbb | -9.3637 | -64.3378 | 2024-10-06 02:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 06f8286d-d165-399d-ade0-0662391337e4 | -9.3638 | -64.319 | 2024-10-06 02:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 3d2644d9-cf7f-3006-9da0-cad0d615aa75 | -9.8552 | -60.2966 | 2024-10-06 02:46:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 11f7e053-786d-3c0f-a2a2-04af894d0dce | -11.0966 | -54.2336 | 2024-10-06 02:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 28a2bc6f-bbfe-3fc3-bf27-790d4a04e5d5 | -12.2645 | -41.0969 | 2024-10-06 02:46:14 | GOES-16 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 3b6f973d-cbd7-3322-b236-15876af75f6a | -12.0211 | -63.7478 | 2024-10-06 02:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 3978fd22-c854-3b6f-9fcd-bd442b4cd0e9 | -12.6089 | -53.1338 | 2024-10-06 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| dee418f9-e523-3a71-8bc9-e75297aaac88 | -12.6092 | -53.1129 | 2024-10-06 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 9a08f8ea-2750-3fe4-9b88-72f7c36ce9f3 | -12.628 | -53.1317 | 2024-10-06 02:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| b1574fb2-b448-3b27-a15f-f91132afc37d | -12.6283 | -53.1108 | 2024-10-06 02:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| b044c413-7d79-313d-8d8f-e5eddeb74871 | -12.7627 | -50.5567 | 2024-10-06 02:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 37738953-1465-3a79-ab12-90c60ea39327 | -12.763 | -50.5352 | 2024-10-06 02:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 307.5 |
| 14becffd-e28b-37b4-841d-cd788f6331d1 | -12.7634 | -50.5136 | 2024-10-06 02:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| be79de76-d456-3b72-a450-f4712a3cfbef | -12.7822 | -50.5328 | 2024-10-06 02:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 4922227f-8336-3913-929e-76a3d1ac402d | -13.6724 | -51.1911 | 2024-10-06 02:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a9a6e720-7923-38a7-8f24-00ff9a5678df | -13.8943 | -44.6058 | 2024-10-06 02:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 1b33f454-dc49-3bed-bc3c-c212c7a3511f | -15.768 | -49.9334 | 2024-10-06 02:46:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e647677e-2820-3367-b1e0-7616db3c7499 | -16.4951 | -57.2509 | 2024-10-06 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| f41fb38f-9602-34b1-9bae-c360f0b9da6c | -16.5147 | -57.2486 | 2024-10-06 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.7 |
| 167d7d44-cc8c-3043-9890-f683ddb43929 | -16.515 | -57.2282 | 2024-10-06 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 07cd98a7-fbe5-3af4-9a7d-dbef214e7120 | -16.5342 | -57.2464 | 2024-10-06 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| ae7d5d16-5eed-39a2-b501-902dbf874782 | -16.5345 | -57.2259 | 2024-10-06 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 2b9b4622-9fcf-3a61-8310-5c8927f46a62 | -16.554 | -57.2237 | 2024-10-06 02:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 91f8aa10-519e-3bf6-a14e-a40a986176df | -16.614 | -55.9214 | 2024-10-06 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 6582dfc9-b8d6-3cca-8a39-caf720317397 | -16.6398 | -55.5452 | 2024-10-06 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 2b5cd7fd-3476-33ec-aff6-609b7aba772d | -16.6923 | -55.9117 | 2024-10-06 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| a16aa768-fb3e-37fd-a814-5d21f6fd7b99 | -16.8238 | -57.4584 | 2024-10-06 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 33a36da5-c637-39f0-b697-10ad2c1d2790 | -17.0007 | -55.0607 | 2024-10-06 02:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 784bef63-34ef-3bad-a68b-4a01794532ea | -17.0203 | -55.0581 | 2024-10-06 02:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 181.1 |
| b7078d36-08e8-3984-9572-492a25074dfb | -17.0207 | -55.0371 | 2024-10-06 02:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3d05e1f8-1db1-3005-8ad9-6ee2c2a6d496 | -17.1182 | -57.4039 | 2024-10-06 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 96232635-956e-3c13-a315-bcd0a013441f | -17.1375 | -57.4221 | 2024-10-06 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 1761480b-50fd-38d7-ba94-219d04be1547 | -18.6387 | -57.2785 | 2024-10-06 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 8feda86d-6f1a-3a38-877b-c93d1d6fd47e | -18.6586 | -57.2759 | 2024-10-06 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| cbe9dcbe-7aa2-3d36-8f83-373d4fdbf5cc | -18.659 | -57.2552 | 2024-10-06 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 0dce8c8b-45c0-3145-bf41-34e3c8e8731a | -18.7165 | -57.372 | 2024-10-06 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.4 |
| dfe57525-5cf4-3123-8852-0eccb5fcd014 | -18.7169 | -57.3512 | 2024-10-06 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 130e31b0-ee51-3f22-8b53-a8cdd05d4551 | -20.5813 | -49.3865 | 2024-10-06 02:47:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 6c1f9172-1b9d-3659-871d-daaf02fb7e1d | -20.582 | -49.3635 | 2024-10-06 02:47:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3ee42b84-23c3-3a29-9629-fe71f46af028 | -20.6018 | -49.3821 | 2024-10-06 02:47:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 70.2 |
| cc8b01d6-18c4-33d8-b37b-15b975f40d14 | -20.6024 | -49.3591 | 2024-10-06 02:47:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1ce8be54-d073-3852-8f13-d1252d2fa23f | -21.5218 | -50.9088 | 2024-10-06 02:47:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 174.9 |
| 4ed5cf14-ad39-36c4-a2b4-d5b92acd8aba | -21.5224 | -50.8862 | 2024-10-06 02:47:05 | GOES-16 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 283d3604-34d2-3f36-86f5-774bc93cf197 | -3.1314 | -48.6125 | 2024-10-06 02:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 6300adbc-c349-3a11-b4e1-e2f243d34e8c | -3.113 | -48.5916 | 2024-10-06 02:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 53b5e121-1a14-347b-b760-7cf724743bc9 | -3.1129 | -48.6131 | 2024-10-06 02:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 58136912-b021-3d3f-bcd8-e5dc06e48b74 | -3.8008 | -41.5989 | 2024-10-06 02:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 419080d7-d8bf-3c1d-b81f-b0658b951778 | -3.8464 | -46.4714 | 2024-10-06 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 78ff0794-b1ca-3ec2-9884-7d3df575050b | -3.7935 | -49.4636 | 2024-10-06 02:55:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 06d01d7c-ee5c-3bb3-9c0f-b696f54627dd | -5.5718 | -44.87 | 2024-10-06 02:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 0bda23fa-9103-3631-9f91-7a82777cc5a6 | -7.9825 | -54.7752 | 2024-10-06 02:55:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6006ed2e-b097-3b1b-8c36-e5f3e97d9820 | -9.3467 | -46.5365 | 2024-10-06 02:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 37cb1afa-4d15-33bc-8053-c7b9ad4c1c7f | -9.3278 | -46.5385 | 2024-10-06 02:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 1ca3340b-1b04-3d20-bb9a-e49444c114d3 | -9.1759 | -61.5794 | 2024-10-06 02:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| df476db6-16fe-3bb4-9971-9bc44ad75a27 | -12.2645 | -41.0969 | 2024-10-06 02:56:14 | GOES-16 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 5041cee2-beb8-34b8-9890-2bec38780b42 | -12.6089 | -53.1338 | 2024-10-06 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d30cc606-af9b-35d6-91c2-eae1d240b272 | -12.7825 | -50.5112 | 2024-10-06 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d3e1b5d9-2966-332f-98b3-8e4e8654be5d | -12.7822 | -50.5328 | 2024-10-06 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 4f15189b-1b04-38b5-80a6-2680ac48925a | -12.7634 | -50.5136 | 2024-10-06 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| b69ff0c5-a2e1-3470-a2cd-326c1caff0c4 | -12.763 | -50.5352 | 2024-10-06 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 308.6 |
| 14172e5b-bc88-30cc-8044-62356f3a602e | -12.7439 | -50.5376 | 2024-10-06 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1e4e7a37-d532-3b10-9eb0-a6aa01dbefc5 | -12.6726 | -54.0189 | 2024-10-06 02:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 88e719b6-4098-38e7-b737-ce8bca17925a | -12.6535 | -54.0208 | 2024-10-06 02:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a2246ef4-f710-328a-b608-c9b0a1bbb9ba | -12.6532 | -54.0415 | 2024-10-06 02:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 056acd9e-597d-3e4f-861c-98d524cec81f | -12.6283 | -53.1108 | 2024-10-06 02:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 3263962f-7d42-3955-8aa2-5c23103b5861 | -12.628 | -53.1317 | 2024-10-06 02:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 47915b18-1282-35fc-ac27-6b1cd28e24a1 | -13.6724 | -51.1911 | 2024-10-06 02:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 37fa5ae2-458d-3922-8a44-afd3bcf33ab5 | -16.5736 | -57.2215 | 2024-10-06 02:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| b16c69d5-c2d4-38ec-88af-9f5846a1803d | -16.5544 | -57.2032 | 2024-10-06 02:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 9d7fdc07-6795-3879-b5bf-0e39bb6ba4c5 | -16.554 | -57.2237 | 2024-10-06 02:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 710f92e2-22c5-3b26-9ccd-064e40b77f20 | -16.5345 | -57.2259 | 2024-10-06 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 9e4825e2-dc88-31fc-a6db-fe96676baeca | -16.515 | -57.2282 | 2024-10-06 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| a0db93c1-b361-3224-9774-42568db2eab4 | -16.5147 | -57.2486 | 2024-10-06 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| ec00bb34-ac54-395e-b951-5a830c26431a | -16.6923 | -55.9117 | 2024-10-06 02:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| ec66f390-2728-3f78-acfe-e8c82bd534c6 | -16.6398 | -55.5452 | 2024-10-06 02:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 2f821b30-b517-3849-8a0c-f89ba8f9c28f | -16.8238 | -57.4584 | 2024-10-06 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 66b0bb42-933a-392b-84f2-5b3c94c798e3 | -16.7647 | -57.4856 | 2024-10-06 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| a9aa966c-7628-3a5d-9819-b800bebd5cc7 | -17.1185 | -57.3834 | 2024-10-06 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |


[Clique aqui para ver as próximas entradas](README38.md)
