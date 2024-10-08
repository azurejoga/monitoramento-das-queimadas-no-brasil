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
| a6cb18be-2445-3b70-aebe-5032b685ef72 | -2.3228 | -50.5215 | 2024-10-08 01:03:08 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 585bd3e6-03f1-33b8-ad57-6b0e102005b8 | -2.8705 | -52.898701 | 2024-10-08 01:03:08 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 060de1b1-443c-36fd-bf05-e7032fa12a63 | -2.8721 | -52.905499 | 2024-10-08 01:03:08 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0770cf-ca9a-3538-864d-18eb18a21fa9 | -2.8607 | -52.900902 | 2024-10-08 01:03:09 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5ab55c-012c-3723-8fb5-adda68aa3254 | -2.8623 | -52.9077 | 2024-10-08 01:03:09 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86ff4cbd-3fd8-39d6-a855-b3c1c9d6565e | -2.8421 | -53.3144 | 2024-10-08 01:03:10 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c74b8034-f3e0-36c9-a29e-8a9a096d5579 | -2.7761 | -53.206699 | 2024-10-08 01:03:11 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 136efa44-282e-3eab-8040-622d3373bb69 | -2.1369 | -50.6987 | 2024-10-08 01:03:12 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cabeb9d-0557-3341-8ec9-4b953b0ad985 | -20.34 | -48.78 | 2024-10-08 01:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6671da2d-d4ea-3992-8908-42f5b0e3012e | -20.37 | -48.86 | 2024-10-08 01:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 39994e51-ee2e-31df-86f9-5013e819e484 | -20.37 | -48.8 | 2024-10-08 01:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1c8a94-3680-3c98-9ebf-164ea488cfa3 | -20.4 | -48.87 | 2024-10-08 01:03:27 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9092b79-3894-3d8e-a369-30b7563b37d2 | -20.4 | -48.82 | 2024-10-08 01:03:27 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca21bca-f9b6-32f9-b5cc-ff14c45f666c | -20.4 | -48.76 | 2024-10-08 01:03:27 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 670d6477-77ed-3ca4-9367-4c17b7548f76 | -20.43 | -48.84 | 2024-10-08 01:03:27 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 29f7e2a8-5417-31a9-aed1-ecbd99abe1df | -1.6308 | -52.573898 | 2024-10-08 01:03:39 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3efb1d-3198-38ee-b33f-1d3c15daa2b8 | -1.6324 | -52.5807 | 2024-10-08 01:03:39 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9b1adf8-aaae-34df-83e0-e7cda5066196 | -1.3221 | -52.8008 | 2024-10-08 01:03:45 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7075779-0fc7-35a9-8cb9-a08029f8ec53 | -1.3236 | -52.807598 | 2024-10-08 01:03:45 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69a8636a-ba09-37fb-ae96-62ba5f7b14da | -1.0291 | -53.7258 | 2024-10-08 01:03:53 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf7c4c1-b194-322c-8a00-4cb23b8b2f33 | -1.0275 | -53.718899 | 2024-10-08 01:03:53 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| def516ab-18e5-332a-96d3-d5ebc3fc796e | -11.32 | -51.02 | 2024-10-08 01:04:20 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d816deb4-3352-3801-b490-4f41186d44d6 | -3.2862 | -47.133 | 2024-10-08 01:05:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e5aae808-daae-3d28-84d2-e1ba0c68ac95 | -5.5716 | -44.8927 | 2024-10-08 01:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 561df2cc-3785-37ea-8cc4-82891fee17ea | -5.5718 | -44.87 | 2024-10-08 01:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 40b79f2b-7bb4-3985-978f-8c93a3871961 | -9.39 | -66.563 | 2024-10-08 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a65ecf98-8518-367a-ab30-03c98b452912 | -9.3901 | -66.5444 | 2024-10-08 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 71aab32b-8d9d-37fe-a6c2-dd2902ffeabe | -9.4086 | -66.5624 | 2024-10-08 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 24eb9e6b-d66e-3d46-975a-32c8cffeb391 | -9.4087 | -66.5438 | 2024-10-08 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 217c913e-5be4-3ac9-811e-2f641cec29ca | -9.445 | -66.7289 | 2024-10-08 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 38e3cda5-a653-31b5-8121-0e2e07ade0ac | -9.4635 | -66.7283 | 2024-10-08 01:06:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 888b3c60-e705-3836-bbb1-f356aec5d4da | -9.572 | -67.4315 | 2024-10-08 01:06:01 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 02fdb46e-63c1-32e2-9a71-c75f80970604 | -10.1263 | -55.1891 | 2024-10-08 01:06:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9380bb21-90d7-360d-83ad-07f7fc0a2e5c | -10.1451 | -55.1876 | 2024-10-08 01:06:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7d849d74-2c5d-3514-9616-554c100f925b | -10.6256 | -55.9154 | 2024-10-08 01:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9aca3eef-2008-3f8f-8d18-87765a82d3d2 | -10.8754 | -63.9169 | 2024-10-08 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 0616188f-6197-3a02-80cf-22697c290924 | -10.8755 | -63.8979 | 2024-10-08 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 4e54abd7-ec9e-31ba-9b6b-81eb3860bb59 | -11.2289 | -51.3091 | 2024-10-08 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d18ed0ac-3dd2-335d-b048-967201ba1a0b | -11.2292 | -51.2879 | 2024-10-08 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 582be094-4728-3f6f-9496-270eabf194e3 | -11.2479 | -51.3071 | 2024-10-08 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 153.4 |
| fe90ec71-32ae-317a-829c-adb2d52c0f3b | -11.2482 | -51.2859 | 2024-10-08 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 196.4 |
| e6d2dd7b-7f2d-37f5-8a00-67cc0f52684a | -11.2485 | -51.2647 | 2024-10-08 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a38eee49-e303-3a6d-8d06-28de4e675536 | -11.2669 | -51.3051 | 2024-10-08 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 791051c0-4236-3135-9d82-a88385d2307b | -11.5233 | -65.137 | 2024-10-08 01:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6a3cd28b-7a11-38d8-b15d-b547bea421be | -12.3616 | -47.0986 | 2024-10-08 01:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c918fa11-2ae3-3eea-a5d2-a6f987fda36a | -12.8242 | -62.4573 | 2024-10-08 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f57527a6-f584-3ed2-8772-e3f3d7e75b6a | -16.5897 | -46.4979 | 2024-10-08 01:06:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a9ee9a09-9575-35e2-90c0-8b2af793d08d | -16.5902 | -46.4746 | 2024-10-08 01:06:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0fa032d5-4298-317d-8d4a-5521dfeae486 | -16.6095 | -46.494 | 2024-10-08 01:06:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| cf93cd76-e944-3d2f-beeb-ae81202c8e8c | -16.9924 | -56.7003 | 2024-10-08 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| b7b8b758-9388-30e1-8526-5f035bc6aabb | -16.9927 | -56.6797 | 2024-10-08 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.5 |
| d4a22e8a-5cc5-39cc-a8cb-93fc59c0a411 | -17.0123 | -56.6773 | 2024-10-08 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 3bc1e6fc-fa29-3872-bed1-aed9e4105373 | -17.3353 | -55.0156 | 2024-10-08 01:06:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 35.5 |
| 9bb846e2-4910-3506-b3bf-71474f8fe9d5 | -18.6192 | -57.2603 | 2024-10-08 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.3 |
| e9e741a1-6631-316b-a394-a35071de3dee | -18.6195 | -57.2396 | 2024-10-08 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.2 |
| fdc1808d-3c47-394b-a580-f1cdeacfc291 | -18.6394 | -57.237 | 2024-10-08 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.6 |
| fcdc7dc2-029e-3660-a982-69da55320a9d | -20.3732 | -43.9468 | 2024-10-08 01:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 190.9 |
| 1e0bcf56-7800-38a6-9a12-93523b894e40 | -20.374 | -43.922 | 2024-10-08 01:06:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| aadaff76-ad06-3430-8425-a3c47edabfb3 | -20.3938 | -43.9412 | 2024-10-08 01:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 231.5 |
| 807749e3-400c-349c-b5e5-17c1915fca16 | -20.3946 | -43.9163 | 2024-10-08 01:06:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.9 |
| ed24b255-4138-390c-982f-d3c31eb9248d | -20.4144 | -43.9356 | 2024-10-08 01:06:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 0510d2bd-79d6-3074-a234-e9267839b6d2 | -20.4251 | -47.6688 | 2024-10-08 01:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 109.7 |
| f05d2156-9878-33e4-b389-22e93d990684 | -20.4258 | -47.6453 | 2024-10-08 01:06:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 4d3ff7e4-e15f-35da-bb9f-03aaff443561 | -21.0712 | -47.2331 | 2024-10-08 01:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 58.5 |
| aa8a4a62-ee64-3ddd-bd89-4d02e2f6d31d | -2.9797 | -49.5342 | 2024-10-08 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 84d00b37-d079-3b3b-9ba1-015a8234efe8 | -3.2862 | -47.133 | 2024-10-08 01:15:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 04a406c1-6f28-3e19-b204-36655ee00d46 | -5.5716 | -44.8927 | 2024-10-08 01:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d704f04b-9fbb-3017-bf6b-d7a8a207e7c1 | -5.5718 | -44.87 | 2024-10-08 01:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 09253a3d-7012-3562-af06-0f67142eb52f | -6.4402 | -38.8327 | 2024-10-08 01:15:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 13d706aa-84d5-3d38-988c-292973f402cb | -9.39 | -66.563 | 2024-10-08 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| afaebc5a-83d0-3e85-b6be-cb3c5e708199 | -9.3901 | -66.5444 | 2024-10-08 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0b23b176-7eda-3902-88b2-7740c4d46049 | -9.4086 | -66.5624 | 2024-10-08 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f4729536-61b4-358e-a729-468abfe1de4d | -9.4087 | -66.5438 | 2024-10-08 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| b68607b6-cbe0-3019-b2bf-b89073a914f1 | -9.445 | -66.7289 | 2024-10-08 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f99ceee9-1603-30eb-93a6-03b76bac281a | -9.4635 | -66.7283 | 2024-10-08 01:16:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 358c8e4d-1921-3cbb-9021-d4f1496a7f32 | -9.572 | -67.4315 | 2024-10-08 01:16:01 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b66db668-35ee-3856-93b7-b2424a048b7d | -10.1261 | -55.2093 | 2024-10-08 01:16:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ca10074d-0c9c-364d-9875-8ca544e8db45 | -10.1263 | -55.1891 | 2024-10-08 01:16:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| ad4c0758-610b-3a0b-a64b-11a6582579d3 | -10.1448 | -55.2078 | 2024-10-08 01:16:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 1c7113e3-93d4-35b4-86a4-12cc97d3857c | -10.1451 | -55.1876 | 2024-10-08 01:16:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 4cad2bb0-10f5-30a7-bde6-ec859286c93d | -10.5942 | -36.8375 | 2024-10-08 01:16:05 | GOES-16 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 88.5 |
| 8c9781ef-3413-3caf-8a31-42e85c1f2a3f | -10.6256 | -55.9154 | 2024-10-08 01:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 14b4e044-3267-3041-8246-c9e94a5f438a | -10.8754 | -63.9169 | 2024-10-08 01:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| f76ccc73-eba4-3b2e-bbc7-c63c2a66728b | -10.8755 | -63.8979 | 2024-10-08 01:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.4 |
| a6c5f37b-5144-3ec2-a285-75231b565ca8 | -11.2094 | -51.3535 | 2024-10-08 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c8071f81-6eb3-384a-a849-2cbf1da4a65a | -11.5233 | -65.137 | 2024-10-08 01:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 17008537-4885-3bdc-a3f1-3a0005854e8e | -11.6806 | -64.0312 | 2024-10-08 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d7220aae-bdde-306a-8614-e2ad5740c5e5 | -11.6808 | -64.0121 | 2024-10-08 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7cb1040f-e815-361f-a39c-59617065aa47 | -12.3616 | -47.0986 | 2024-10-08 01:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| cc65cf4e-cb35-3a4a-a8d6-ae784ec4733c | -12.4414 | -63.018 | 2024-10-08 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a43ebaee-09e8-3fa2-a2b3-8972000c2a3d | -16.5897 | -46.4979 | 2024-10-08 01:16:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 4504d7ab-7c90-3480-8692-c306fbdc1f4d | -16.5902 | -46.4746 | 2024-10-08 01:16:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1168db65-309f-3051-8e59-6516290664d1 | -16.6095 | -46.494 | 2024-10-08 01:16:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1f759aaa-e58c-3179-90fd-4ce3a5a32794 | -16.5267 | -57.7365 | 2024-10-08 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| 80102fa3-70c4-343f-85cd-da4ab9092e0a | -16.5462 | -57.7344 | 2024-10-08 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.4 |
| e623e18c-daa0-386b-a2db-7261fa6481ad | -17.0123 | -56.6773 | 2024-10-08 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 95c28edc-5e9b-3ff5-94b8-b9987f034c90 | -16.992 | -56.721 | 2024-10-08 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.5 |
| 9a7f233f-b555-39b4-a571-34139fc5b1c8 | -16.9924 | -56.7003 | 2024-10-08 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 6fcd3fa3-bacb-3f53-8e93-4b127bde8c6b | -16.9927 | -56.6797 | 2024-10-08 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.8 |
| 32f2d3e0-9968-3425-b250-4b9e71ca34ed | -18.6192 | -57.2603 | 2024-10-08 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |


[Clique aqui para ver as próximas entradas](README21.md)
