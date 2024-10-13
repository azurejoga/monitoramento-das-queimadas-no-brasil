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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ff95737-d453-34b1-8929-fa36f826cd8f | -18.2364 | -56.4806 | 2024-10-13 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| c650b3e2-f39a-37b4-8acf-7e5c34f53436 | -18.236 | -56.5014 | 2024-10-13 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 6277e7b9-7255-3f12-8c0d-05b113d3b6c3 | -18.2166 | -56.4832 | 2024-10-13 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| d4d55849-a46e-3d21-b5e7-1c04d216e238 | -18.2155 | -56.5457 | 2024-10-13 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 20671f15-39ce-30be-811a-ba0de7473edf | -18.2151 | -56.5665 | 2024-10-13 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| e02a711d-27c6-3f35-aded-084b2b79c503 | -3.114 | -53.0554 | 2024-10-13 04:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 11766366-eb81-396f-8537-2c03dab77c27 | -3.0957 | -53.0355 | 2024-10-13 04:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| c56b01d5-555e-371d-a72d-8190237b7cd6 | -3.1141 | -53.0351 | 2024-10-13 04:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 32b0535a-01d3-3ff4-86f5-51ca8403fc60 | -3.0956 | -53.0559 | 2024-10-13 04:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 088a9cb6-c372-356f-8427-090a6e60b2ec | -4.1149 | -48.2299 | 2024-10-13 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 75d02852-e44b-35c2-8faf-d58c3f3d1756 | -4.1148 | -48.2515 | 2024-10-13 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4b9a25a9-2df1-36e4-b7a1-f512a5181d8f | -4.3986 | -44.4652 | 2024-10-13 04:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 411bd1f7-634d-3f70-846d-07e94eda479a | -4.3985 | -44.4881 | 2024-10-13 04:15:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d6a550d2-91cc-32c2-bc08-1261ec5a9f2b | -10.9506 | -44.653 | 2024-10-13 04:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 18215f87-dc6c-3040-98a8-378155fc23f9 | -10.9502 | -44.6762 | 2024-10-13 04:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ec8734a2-4096-39a5-8dec-0a67e96c9d5d | -10.9311 | -44.6789 | 2024-10-13 04:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 202e1bc1-2f72-384b-8afb-339bfa777c00 | -12.4794 | -62.9967 | 2024-10-13 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c35b1e6d-ec11-38cf-9c47-12fe46e57da1 | -12.4792 | -63.0159 | 2024-10-13 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| dc22c296-259c-31e3-a992-b683fe19616c | -13.7346 | -60.6079 | 2024-10-13 04:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 9af5f8e0-53a0-36c1-9612-0e45c0b9e034 | -13.7541 | -60.5672 | 2024-10-13 04:16:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 66e14afb-fafa-3e56-a43f-084978cfe65a | -15.3251 | -41.8663 | 2024-10-13 04:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 16bb0299-ee76-3d7c-88a4-08fce1cf1d1e | -15.3244 | -41.8911 | 2024-10-13 04:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 182.6 |
| 76a097f9-12e5-3911-a0fe-792c60d5d63d | -15.3238 | -41.916 | 2024-10-13 04:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| fe7047a1-4358-3abd-838a-28a81c3abcef | -15.3047 | -41.8955 | 2024-10-13 04:16:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| 13f2fef8-9bdd-3325-9f51-71a6d9238c1d | -15.6419 | -59.9767 | 2024-10-13 04:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| dd83e1e0-fb52-3e49-9906-8014ef0f0598 | -16.9995 | -57.4791 | 2024-10-13 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 8b95423d-aeb8-3e1c-a7de-a6effc12f3f3 | -16.9998 | -57.4586 | 2024-10-13 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 88d22157-6b24-38af-a828-a7f10ddb951a | -17.1758 | -57.479 | 2024-10-13 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 92381f28-fdf9-3cd2-bc59-8a3180d97665 | -17.6478 | -56.2668 | 2024-10-13 04:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 205.5 |
| b842e231-f292-3ced-a59a-cd071d63a8a4 | -17.6474 | -56.2876 | 2024-10-13 04:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 238.4 |
| 8e1a7e1c-4538-3595-bc30-d93448e01faf | -17.628 | -56.2694 | 2024-10-13 04:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 2b0d5f8b-f0a3-302e-8658-9391634f9fe2 | -17.6277 | -56.2902 | 2024-10-13 04:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 91886cf7-9176-327f-a62c-bfdec08c4a35 | -17.6675 | -56.2643 | 2024-10-13 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 8096ecde-c708-3ad3-9509-b3440dfdad96 | -17.6672 | -56.2851 | 2024-10-13 04:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 2bab8c66-05d3-37b4-9ca5-18f5746d8aad | -17.9837 | -57.3819 | 2024-10-13 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 7eebd635-29ad-35df-a023-eefcf5877acb | -17.964 | -57.3843 | 2024-10-13 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 7d68d3d2-9652-3136-bf40-0c09041f846d | -17.9643 | -57.3637 | 2024-10-13 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| dc771e6f-3ac9-30b6-8d12-cee25c5be5b6 | -17.9841 | -57.3612 | 2024-10-13 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 221801fe-5e3a-3552-a442-b8aefd2d4b68 | -18.2166 | -56.4832 | 2024-10-13 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 564b550a-9493-3fe9-a354-ff14d5b51ea2 | -3.1792 | -50.4551 | 2024-10-13 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| ccf295e0-eb8e-3a31-8fb4-8f7b18872b85 | -3.1791 | -50.476 | 2024-10-13 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f8ba9d10-6405-398f-abf8-1dd95cae9fa8 | -3.1141 | -53.0351 | 2024-10-13 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a84fde13-8c51-33cd-8b95-75f7c5bd54ed | -3.0957 | -53.0355 | 2024-10-13 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 7201f2f9-07f3-3e77-8fd7-172aaafebe25 | -3.0956 | -53.0559 | 2024-10-13 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 572df5d8-2c6e-3816-b687-ab8610c32e8c | -4.1149 | -48.2299 | 2024-10-13 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f40fc010-1756-3ea4-a472-9fe843fabe6d | -4.1148 | -48.2515 | 2024-10-13 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 67449c40-4284-34ea-a62d-43a51d04c4a1 | -6.3911 | -41.5775 | 2024-10-13 04:25:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 86064f88-8e6a-3c12-8950-8b64f7717af2 | -6.3909 | -41.6016 | 2024-10-13 04:25:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 195.0 |
| 73afbddb-eb32-30c8-8635-4eb505dee9a7 | -7.6627 | -47.3229 | 2024-10-13 04:25:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c815d1a4-e8ce-3d3c-a29d-47b61d5df11b | -9.7359 | -64.2295 | 2024-10-13 04:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 801082d5-be33-3f1d-81fd-d77e79663a95 | -10.5097 | -42.5023 | 2024-10-13 04:26:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 3d4a950f-d55b-3ed1-8f26-cad1987167f7 | -10.4693 | -63.1384 | 2024-10-13 04:26:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 23844977-8240-3b11-80dc-fb32f6e0ce56 | -10.9506 | -44.653 | 2024-10-13 04:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 864bdd7d-8dca-3520-967c-ad1625ec98bf | -10.9502 | -44.6762 | 2024-10-13 04:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 74930219-ebaf-361e-b10d-f19595aa1483 | -11.6334 | -48.3736 | 2024-10-13 04:26:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 225f85cd-dd69-3baa-a3be-526ea04f1062 | -12.4794 | -62.9967 | 2024-10-13 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 77d6acee-1fdb-3e9d-84a5-69b30fa1185b | -12.4792 | -63.0159 | 2024-10-13 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| af18227b-3dd1-3274-8586-1e8ea68d8265 | -13.7348 | -60.5883 | 2024-10-13 04:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5157bfbf-c50f-30cd-8a72-91767d81a161 | -13.7346 | -60.6079 | 2024-10-13 04:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 34d0502a-a172-3c9f-9809-71910e3b598f | -15.3244 | -41.8911 | 2024-10-13 04:26:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.0 |
| bcd4f246-835c-3f64-ad24-9a7968e2cc02 | -15.3047 | -41.8955 | 2024-10-13 04:26:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 8c5a9bf2-11a6-32e1-943f-946d5416c532 | -15.6419 | -59.9767 | 2024-10-13 04:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 053eee6d-bc7c-308f-9360-a43d999174db | -17.0626 | -56.01 | 2024-10-13 04:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| f3aa3248-1db5-3e0f-a99f-d5a33b3fe5aa | -17.1758 | -57.479 | 2024-10-13 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 6d60ec8e-2311-3f4d-a99c-ade2d6e1a482 | -17.6478 | -56.2668 | 2024-10-13 04:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.2 |
| 4a41f7fd-db57-3128-8846-193b3f1a36a2 | -17.6474 | -56.2876 | 2024-10-13 04:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 234.7 |
| fee75363-5ad8-3ee8-95cc-603c5dc3be8e | -17.628 | -56.2694 | 2024-10-13 04:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 3f9de426-15ae-33c6-9275-4268ffc9cd90 | -17.6277 | -56.2902 | 2024-10-13 04:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 2d86d2c5-99d0-30c0-9dde-64627a947de0 | -17.6675 | -56.2643 | 2024-10-13 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 606c68e9-b4ac-3ffc-acba-a6c3cbbbab4b | -17.6672 | -56.2851 | 2024-10-13 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 0c4bc889-9a4a-3309-aed3-12a9a0ed0cf1 | -17.9841 | -57.3612 | 2024-10-13 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 3aca28d3-3629-3609-a58d-2dac83e95d3c | -17.9837 | -57.3819 | 2024-10-13 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| c1b9e48b-6a52-340a-9433-d7835f39a7bd | -17.9643 | -57.3637 | 2024-10-13 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 0c2efb9b-08ba-353b-b3c7-bbb18854d22c | -17.964 | -57.3843 | 2024-10-13 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 57a0705c-216b-31d1-afb0-cbe2c3b6f3d1 | -3.1141 | -53.0351 | 2024-10-13 04:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 886f0881-ff05-3430-8dc3-948bc772d6b5 | -3.0957 | -53.0152 | 2024-10-13 04:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 22d2bfc8-a25d-342c-a990-6a7e7d2ac055 | -3.0957 | -53.0355 | 2024-10-13 04:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| abc53d55-ef0b-3005-84ac-936dc6457e34 | -3.1792 | -50.4551 | 2024-10-13 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| fcee30b1-ce72-3cd5-9ce7-b9a5657afcfa | -4.1149 | -48.2299 | 2024-10-13 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 431c6bde-64b7-3b8b-a2ee-e446c72f2bc0 | -4.1148 | -48.2515 | 2024-10-13 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d8a3b970-6cb8-31f8-9feb-9eded915f336 | -4.3986 | -44.4652 | 2024-10-13 04:35:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b2082fa7-d306-3658-9188-92f8781de04f | -10.5097 | -42.5023 | 2024-10-13 04:36:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 46d48ae6-67ad-3d21-84d8-5559d1e48586 | -10.4693 | -63.1384 | 2024-10-13 04:36:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 050d632c-cf42-3097-8c5e-0209b9fa844a | -10.9506 | -44.653 | 2024-10-13 04:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0ec34f7e-9f81-35c7-aa13-9029c41ece1e | -10.9315 | -44.6557 | 2024-10-13 04:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c56a4e66-2e86-370f-bb6c-9d506acf01ec | -11.2766 | -60.4455 | 2024-10-13 04:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0530de9e-7d9f-3e1f-aae7-fe3fa64d16b8 | -11.6334 | -48.3736 | 2024-10-13 04:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9811919e-52a3-3584-9a1a-c78eb2d4502b | -12.3982 | -63.7284 | 2024-10-13 04:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 9fdbbffb-99c5-3c8f-9123-260a834aa9f5 | -12.4794 | -62.9967 | 2024-10-13 04:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9c66ad56-f6f8-3c13-a27e-c86e3b088b57 | -12.4792 | -63.0159 | 2024-10-13 04:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 7b3fda66-5a43-3a67-8d37-4d055b096fea | -13.7348 | -60.5883 | 2024-10-13 04:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2295cc9e-1d53-368e-8de9-23465bea3dec | -13.7346 | -60.6079 | 2024-10-13 04:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7f9c9a47-318b-3bb6-a114-8e9ecd8c4c91 | -13.7155 | -60.6093 | 2024-10-13 04:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 49cbf2af-28ef-3a59-add1-336cd1aab324 | -13.7541 | -60.5672 | 2024-10-13 04:36:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 158ad708-2a91-3a12-8412-d130a4bcccd8 | -15.3251 | -41.8663 | 2024-10-13 04:36:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 806e2c61-c8fc-3710-b5ef-1a5c242511b6 | -15.3244 | -41.8911 | 2024-10-13 04:36:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| 80a8f839-fcb1-38b1-88eb-edb1e20da62a | -15.3053 | -41.8706 | 2024-10-13 04:36:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| 50cd46e2-e068-3cae-869e-b8b05d32a786 | -15.3047 | -41.8955 | 2024-10-13 04:36:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| bb1f9582-e5da-32c5-9141-b85656aee9f6 | -15.6419 | -59.9767 | 2024-10-13 04:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 208deac0-9178-37fd-82fc-2ca737f67e9e | -16.9998 | -57.4586 | 2024-10-13 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |


[Clique aqui para ver as próximas entradas](README48.md)
