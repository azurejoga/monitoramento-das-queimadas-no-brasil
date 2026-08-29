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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c73cc2f3-18f9-3da3-bffd-e62722d4a82d | -11.0441 | -57.2421 | 2026-08-29 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e573b0ce-faaa-3b24-afcf-c6c6ecd15bfd | -4.3774 | -47.7627 | 2026-08-29 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ed749f98-4cb4-34c9-87ed-c719cdfcc848 | -8.9428 | -63.2797 | 2026-08-29 01:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| acac16dd-aad6-3bc8-ac67-eea6d936bd03 | -4.3772 | -47.7844 | 2026-08-29 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 6daa6a8d-cdf0-302c-a0ec-9d68984e5c1a | -20.2295 | -47.3875 | 2026-08-29 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 8f0392a8-4923-3707-87ff-8b2d66c7e58b | -8.5822 | -54.819599 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2807e61-f3d4-38e9-84f6-5b76f2906f6c | -8.6003 | -54.764801 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c06f3df1-f92a-3410-b55a-24998a25f74d | -10.4581 | -64.474503 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3de30a41-b769-3efb-a2fd-566473931850 | -14.1786 | -52.838501 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b1ed02b-0714-3f1c-81a4-1c35f6b5d9ec | -6.7422 | -55.4706 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8f25e43-7bf7-37cf-b2dc-758381eb3695 | 3.1102 | -60.712299 | 2026-08-29 01:16:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 93636a71-9e89-3037-9896-a7bbf5a37ee4 | -6.7279 | -60.015202 | 2026-08-29 01:16:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7461441-bed6-37ea-9f5b-5e9191dad470 | -6.8884 | -59.399601 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa09012-42c6-33ba-aaff-42e249ad7258 | -14.9022 | -52.6203 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e42c4f9e-c33e-3c66-ba55-1b1cf0072f5f | -9.2596 | -57.079498 | 2026-08-29 01:16:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2420585f-1ac8-315a-be7e-c869ec43cd84 | -11.0242 | -57.223701 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1823737d-cb53-333c-8bdf-ce6f5f652200 | -6.8678 | -59.032902 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5474efa9-5b1a-3bf8-a122-f0dc4a13ed42 | -15.6107 | -56.406601 | 2026-08-29 01:16:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f6178a7-489e-3c25-a7c6-5646ef4077c7 | -14.2099 | -52.839802 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc9b335-1065-3eb6-bd1f-d78357358521 | -6.5761 | -56.533699 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f909032e-d03f-3b62-8946-9b1a7c27368e | -6.2473 | -55.428299 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 885467db-830d-300b-a5cf-c683cb5bd891 | -6.579 | -55.434502 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43976b4e-cc01-3b8f-8ac4-1576dfc0900e | -14.1903 | -52.844601 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 098ed147-6f6e-362e-ba73-68b021d6d003 | -11.6259 | -54.587101 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcd91010-dc27-33e7-84dd-ae16703edd9b | -7.5981 | -61.345901 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff4b70cd-4e4f-3b82-a1d5-474ae509aa48 | -7.5079 | -55.3018 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 561aa360-2206-3b2a-94dd-4175e309e26b | -10.2882 | -62.816002 | 2026-08-29 01:16:00 | METOP-C | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49bcedb8-32e5-3812-895f-67a44a017d24 | -7.5006 | -55.270699 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7ead5dd-cd83-3658-917c-911fa0d1bb15 | -14.9217 | -52.615398 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e6834b5-153c-390f-9be2-f1da046886fa | -7.5592 | -61.309101 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 567fb4ae-d4d4-30c5-8543-c7f9e4e5fc03 | -14.9156 | -56.3372 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5247da1e-ad6f-324f-af35-92c5d44b34ff | -8.9442 | -63.267399 | 2026-08-29 01:16:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 804cce96-20db-38d2-a67f-29429605c7f8 | -8.5559 | -54.7076 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cecf2f5d-5515-339b-9549-7deef0cff678 | -6.7621 | -55.644402 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e22d004-ad7a-3d8c-a633-9f72890b8d4c | -6.1291 | -57.6861 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e836cf94-1c74-32c5-ba1a-8be8c84669cb | -13.4659 | -57.041801 | 2026-08-29 01:16:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| baea057e-c3ee-3aaa-a595-2501e69cde22 | 0.1412 | -60.390301 | 2026-08-29 01:16:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6de58f53-a4fb-3fa4-871d-b21d91157690 | -6.5446 | -55.243099 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93bccafd-72d1-3b53-8bac-6f57259cb8e3 | -11.2714 | -54.046398 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8b16b0-ca8f-3a3e-a452-29dcd62b3b79 | -14.9035 | -47.7356 | 2026-08-29 01:16:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a89e070b-b3e8-3b63-b438-e21fc6ec0a54 | -15.119 | -53.576099 | 2026-08-29 01:16:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| accf1997-22b8-3cef-9594-0e1ed353aa15 | -6.8672 | -59.396801 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c17b7d4-3249-36e6-8e2d-f95a3d88f0b4 | -15.6205 | -56.404301 | 2026-08-29 01:16:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7169c922-2395-3372-a4c5-ff82001b007a | -19.2862 | -49.505402 | 2026-08-29 01:16:00 | METOP-C | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63093af9-1ab5-323c-a0bb-6f8ba81f459f | -7.5061 | -55.294102 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76faa2a0-9027-3b18-9d10-bc4c8a0bc267 | -11.0386 | -57.242298 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0c6363f-d90e-3ebd-83fa-898a6f661f54 | -9.4251 | -51.572201 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f166b282-9846-30ba-ab3a-ac51fb41524a | -14.8945 | -52.631401 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4fea519f-34d1-3f80-9688-63301ebeff6a | -8.5417 | -55.264599 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a159cd-4a73-3d4b-88dc-f9bc224305de | -15.5741 | -56.2883 | 2026-08-29 01:16:00 | METOP-C | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4a0de09-35ea-3675-87ca-f4cb37e7af8b | 0.1495 | -60.3993 | 2026-08-29 01:16:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0b715d25-d5b6-3d68-a8ef-c4631514d3fd | -20.220301 | -47.376099 | 2026-08-29 01:16:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d0d73fbf-49c7-3634-8561-9dbcefc3bdd5 | -6.5464 | -55.251099 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 865d6f16-d08a-314d-b33b-d1a61edd6d2c | -14.898 | -52.602798 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39f9e861-8296-396f-8a11-6a70505bbbe0 | -10.7554 | -54.049099 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2df7c7b-be53-39df-b745-7330fc07d9fa | -8.5864 | -54.7934 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc4fbcbf-7e8f-3c83-97c6-34b26bcc64f7 | -6.5808 | -55.442299 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 436b85ba-eca8-3b27-aa77-b23fdfe8d4ec | -9.9432 | -60.429699 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 326489a7-c573-3ecc-b547-dc15c532749e | -11.0438 | -57.219299 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f22aea6a-809c-3e2e-ae63-357442fbc82d | -9.1345 | -61.0051 | 2026-08-29 01:16:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 696123ad-fa0d-3f8f-994d-a255ba9b6966 | -11.7068 | -54.5354 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd6e8d3-aacc-35fa-ac44-cda7546d909e | -4.3634 | -47.7766 | 2026-08-29 01:16:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adc3d42f-e1d5-31ed-8890-7af10a713895 | -11.7246 | -54.522999 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29097ef9-56c8-341b-b383-d53cebfb8c74 | -14.1667 | -52.832199 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01cde676-9fa2-39e0-9de5-b9ce93750f08 | -9.9705 | -53.9193 | 2026-08-29 01:16:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa55102-f65e-3991-905d-fbdbeb433b88 | -19.226601 | -57.654598 | 2026-08-29 01:16:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 66c6bc7f-c35c-3ca8-80e1-cb9fe7b8bea9 | -7.9209 | -61.367401 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3635b57-9f9c-3aab-a3bd-02a0914bf5bc | -14.9119 | -52.617802 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3f11d14-e309-3a06-b979-59543e219fdb | -9.6125 | -55.118999 | 2026-08-29 01:16:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bfcf34b-7c9a-3cea-8fdf-274de8cc6e47 | -7.6136 | -61.369801 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f269556c-4aa2-3c97-994c-ea59828413e9 | -6.7825 | -55.687698 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa2a0673-f60a-3b63-8e22-0b6640d08bb1 | -8.5942 | -54.7831 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17791790-e548-3d73-9bf9-6b6bd70dcb69 | -6.7576 | -55.669399 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 726ee86c-6925-3fa7-bc60-b94f9e02f4e2 | -8.6073 | -54.838799 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8e91be5-bb53-38ee-9dc8-5f86d23f022d | -11.2266 | -53.988201 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3621553-5414-3345-95e8-629cb27c3944 | -4.357 | -47.750702 | 2026-08-29 01:16:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a377843-1838-3bef-9be3-e1e834b40d45 | -6.9337 | -58.959499 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1cf964-8214-3ee0-81ea-7fcb777fb267 | -14.2043 | -52.859501 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5234593-a27a-3f56-b470-ef40259f29ef | -5.9808 | -57.668999 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c23c48-d63b-3831-bae5-e2677ab87325 | -11.2695 | -54.0383 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2c380e9-38e8-38a6-931c-5420b9f2e85d | -5.8902 | -57.7687 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df175cdd-313f-3ccd-93bc-8de74ec13a68 | -3.6131 | -60.538601 | 2026-08-29 01:16:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cefcf346-3484-3f44-8602-05420deb054b | -6.1542 | -57.795898 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba92000-82f8-3db3-a27a-6bba9dc8784f | -7.3519 | -55.164799 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3cde34c-fdb9-326e-b031-44e66ee575e2 | -20.949301 | -57.570499 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0ccec357-7a83-384c-984f-8b0ebe36324d | -5.882 | -57.777802 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c945933-0c79-3ee1-80c5-af3d1e6a9559 | -11.1925 | -51.280899 | 2026-08-29 01:16:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20bcd9fe-42ff-39d0-8920-f73923166529 | -22.604601 | -54.974899 | 2026-08-29 01:16:00 | METOP-C | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5567c236-8ce9-3a28-801b-2e4c4332989b | -11.7148 | -54.525398 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92438298-1a48-3a06-b232-2ca7201283c3 | -6.8165 | -59.445499 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d489056-ed72-3984-b81c-635f9a937b03 | -14.9517 | -56.313999 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4002c4d-aed3-3646-81e4-631e8fed1143 | -8.532 | -55.355099 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 222e887e-e5c7-3a7a-9635-8e5a67b8989a | -7.5043 | -55.286301 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b598b2a-2e4f-301c-9925-a9489d6e6538 | -7.4764 | -61.399399 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3608df-6a5d-38fe-87fb-e0cb356165e1 | -10.4679 | -64.472603 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 954e926c-6644-3cc0-8485-fe9da31293b1 | -6.7386 | -55.455101 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe04078-bb2a-35d0-8eb3-2f59e17d03d0 | -9.21 | -51.537102 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6c40ea-c109-3482-8ea3-e1fa48562489 | -6.7656 | -55.659599 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd006a6-66d3-3fff-a232-586b07e94ff0 | -7.5845 | -61.3307 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4d3e5fb-2175-3bc4-9c4c-92011b9b1af2 | -7.5097 | -55.309601 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
