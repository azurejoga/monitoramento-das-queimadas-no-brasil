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
| df1bbffb-f3e7-38a3-872a-65d3c9ebb087 | -12.0941 | -50.5951 | 2026-08-24 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 4247a5d3-181f-320f-8165-0d718693a34e | -12.1128 | -50.6143 | 2026-08-24 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| e0945d3d-d38d-3057-aba3-a52ba96b4c35 | -14.9392 | -52.664 | 2026-08-24 06:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 73ebfede-00b8-3179-a67c-efffda956176 | -12.0944 | -50.5737 | 2026-08-24 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 6d7de0cd-dfc2-3844-81d7-1e3eec0ccacf | -14.9396 | -52.6428 | 2026-08-24 06:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 33301acf-c65a-36c5-a327-8672484affde | -14.9202 | -52.6454 | 2026-08-24 06:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| a44688e0-3175-3a51-a55a-e618b1473c06 | -7.7034 | -63.3249 | 2026-08-24 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e07b5fe4-75e2-3886-a89f-e2622165749c | -7.7033 | -63.3437 | 2026-08-24 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 8fcf4c4e-86db-351f-b1c0-1da6a0620dea | -12.0941 | -50.5951 | 2026-08-24 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 09b43a5a-51aa-3f2d-b78f-941f305be334 | -12.1128 | -50.6143 | 2026-08-24 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7440ee48-ac47-3ccd-9590-387617d9a9ac | -14.9399 | -52.6215 | 2026-08-24 06:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| a8db5e89-caf8-3f4f-a017-9dd00cbb0ee0 | -7.685 | -63.3255 | 2026-08-24 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 30a0be32-52a8-3068-975d-2ddaa65087b9 | -7.6849 | -63.3443 | 2026-08-24 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4f4ab9e6-2a0c-3cbb-b80e-911091bfdf24 | -12.1132 | -50.5929 | 2026-08-24 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 3c8cedec-9272-365b-a17a-44a76b371b38 | -14.9198 | -52.6666 | 2026-08-24 06:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7dd0da58-f0ed-305c-8737-ebc4254c54b8 | -7.6849 | -63.3443 | 2026-08-24 06:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 576190e5-d6c7-3333-bdae-a9b561c8eb98 | -14.9202 | -52.6454 | 2026-08-24 06:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1272edb2-8433-3f52-b331-0b32749d3d64 | -14.9198 | -52.6666 | 2026-08-24 06:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 342ac105-06b2-3f4c-9fb6-455cd3ecf7bb | -14.9396 | -52.6428 | 2026-08-24 06:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 2d88c573-f529-303f-b1b2-ba5159827933 | -7.263 | -49.864 | 2026-08-24 06:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 5c512e71-633a-3498-a992-f3c894b01077 | -14.9392 | -52.664 | 2026-08-24 06:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 196.5 |
| a5997980-2e20-3b86-9cc8-81299ee21706 | -7.6665 | -63.3261 | 2026-08-24 06:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d4bbcb93-57a5-315a-9bd9-428d32f3fa64 | -12.1132 | -50.5929 | 2026-08-24 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cf042027-10c8-3553-9ec3-76c5dd36601e | -7.685 | -63.3255 | 2026-08-24 06:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 91119d72-1029-324a-befe-dd177ca06488 | -12.0941 | -50.5951 | 2026-08-24 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| ca8e4431-6f78-3811-9aa6-5bd688ae55d9 | -21.9065 | -49.6404 | 2026-08-24 06:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| f0a82982-c09d-3581-8ee6-2e56d25e3d91 | -12.0944 | -50.5737 | 2026-08-24 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cdf468f0-e7c0-3cb2-a691-5c861a6fbe8f | -14.9392 | -52.664 | 2026-08-24 06:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 61b130a6-fd3b-34cb-b9a5-59e6400f9d2e | -12.1132 | -50.5929 | 2026-08-24 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c06b3266-0bbf-3331-9043-94a92438915a | -21.9065 | -49.6404 | 2026-08-24 06:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| 1e8fab6f-2704-3c51-bc6b-de9e3f9bcd0c | -7.685 | -63.3255 | 2026-08-24 06:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| eb7f7d38-d274-3e40-b110-7ddfc38b694e | -14.2982 | -51.75 | 2026-08-24 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 21ca4173-63b7-3b9c-a990-420b65de00f5 | -12.0941 | -50.5951 | 2026-08-24 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| ff224a6a-0a89-3399-9da2-ce8dde981f3a | -14.3175 | -51.7474 | 2026-08-24 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 3996b2dc-4ee1-349f-8954-8f29029c054d | -7.6849 | -63.3443 | 2026-08-24 06:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 15cdf05a-f189-3eb4-925e-186a47975311 | -14.3171 | -51.7688 | 2026-08-24 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d73105df-5e2b-36e5-9873-28896a91f1e3 | -12.0944 | -50.5737 | 2026-08-24 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 5fd57690-9dcc-3dd4-882d-33522a5a7a5f | -14.9396 | -52.6428 | 2026-08-24 06:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 68328304-cf1a-381a-a697-76acbc289356 | -12.0944 | -50.5737 | 2026-08-24 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ac0ea8f3-d241-3c1a-896e-043cd0fc922f | -14.2982 | -51.75 | 2026-08-24 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9fa5dfa8-6f81-30e7-903a-e8bed8903545 | -14.2978 | -51.7713 | 2026-08-24 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7f94186f-1580-316a-b4f7-f6f2a97fb914 | -21.9065 | -49.6404 | 2026-08-24 06:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| d4079c50-2780-3c0f-8aab-25a21ca3329b | -14.3175 | -51.7474 | 2026-08-24 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 665725e1-3c63-3d01-949f-5afbc2032e01 | -12.1132 | -50.5929 | 2026-08-24 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 42e655b1-9820-3b33-9a63-af3a40ef605d | -12.0941 | -50.5951 | 2026-08-24 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ec6750e3-c87e-32ac-90b7-47ef978abd06 | -14.3171 | -51.7688 | 2026-08-24 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 8218611d-cfc6-3da3-b7f9-79ca5017c114 | -7.685 | -63.3255 | 2026-08-24 07:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 70974a9e-2e47-34da-b0d0-a3632ce9813c | -14.9392 | -52.664 | 2026-08-24 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 9f16c9f2-563e-32b2-91e4-876272f55617 | -12.0563 | -50.5782 | 2026-08-24 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 036c4fe0-3741-35d9-9901-58950d4aea11 | -6.60621 | -58.38886 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 257d289d-4060-30c7-b796-c7d02de48ac5 | -6.8147 | -58.65163 | 2026-08-24 07:18:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6c74718d-90ec-3dd9-b704-5efdd77a2918 | -6.18577 | -53.52497 | 2026-08-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 54e68c4d-0f16-35e0-8eef-294d20d74c3a | -6.17615 | -53.52359 | 2026-08-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ee23c643-6dfb-3d3b-a9a9-48acae82b052 | -6.11838 | -57.83691 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 908140ba-1672-3d4b-8988-284d9afb61ab | -6.34389 | -54.76059 | 2026-08-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b038ee39-6ab0-3bea-a7dc-1a87278ca62e | -6.79707 | -59.59012 | 2026-08-24 07:18:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1690f046-efd5-3478-9c6e-e927a4671a22 | -5.94061 | -57.73052 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cd589e1a-ba6f-3eee-85f5-5612c143447c | -6.60773 | -58.37909 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2855150b-c3bf-3df6-b721-76316ccf6426 | -6.85633 | -59.40471 | 2026-08-24 07:18:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b4476af3-b0b2-3529-be64-8576b32caaa6 | -6.79438 | -59.8014 | 2026-08-24 07:18:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fb21b1f9-05be-3d52-a0d5-1520bec11295 | -6.59785 | -52.45364 | 2026-08-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| fa036366-d84e-3cc6-beae-eff72dc1bde6 | -6.14005 | -57.93626 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f1969005-725c-3fa8-9eed-f45a9a9fd327 | -6.5567 | -58.58339 | 2026-08-24 07:18:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6ede501b-9a08-3d8d-a8df-8ab4d26c2450 | -6.55018 | -58.52469 | 2026-08-24 07:18:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7cc93198-d778-314b-9720-7e74ed32b8d3 | -5.78041 | -57.57084 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fea864cd-76bc-31d3-98b7-b4a84d7619e1 | -6.33623 | -54.74989 | 2026-08-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 91f64426-9384-3a03-9866-f386de873fbe | -6.79257 | -59.813 | 2026-08-24 07:18:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6ecc07f3-1d72-36e9-b514-9f3e12e9a9eb | -9.06705 | -60.4345 | 2026-08-24 07:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 53d7938a-b1fc-32e3-9dbf-b8d2591b109a | -6.83539 | -52.50502 | 2026-08-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 4d9b1a35-db14-3473-8281-3c093799b3c6 | -6.14912 | -57.93764 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6dc1423-12ff-3162-b0b5-4e7c40f98b94 | -5.78184 | -57.56166 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2ee20a3f-081a-31cc-ad45-121e181c49e3 | -6.62946 | -58.48281 | 2026-08-24 07:18:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 99a29d24-25df-3ecf-ab4a-8ddfbb60a526 | -5.79081 | -57.56303 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 142bf611-7431-3d42-b04f-c2cd74ad0746 | -6.83718 | -52.4923 | 2026-08-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b738b13a-df61-3e4c-a4ca-49efa75949e7 | -7.25034 | -49.86163 | 2026-08-24 07:18:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| aaad956b-6d8b-3a54-b75c-7c56f69d4f17 | -9.19556 | -59.57133 | 2026-08-24 07:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f618c204-e4f9-3ef1-a30e-40f5da070591 | -6.96176 | -59.07504 | 2026-08-24 07:18:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a8db9298-7fd4-397c-93b8-e151d81e4fd9 | -6.11983 | -57.82755 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27aea5ba-3df2-3aa0-88a8-08c882de736c | -9.11241 | -60.34459 | 2026-08-24 07:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6c506118-7a64-358c-a3bc-8bdbdf715fe8 | -6.12887 | -57.82888 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61abf74e-30c2-3b8a-ac21-66edfe52383a | -7.7894 | -56.28255 | 2026-08-24 07:18:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd67d14c-5c5e-3b49-a7c7-a6d7b06fc153 | -7.25311 | -49.85438 | 2026-08-24 07:18:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 144bb202-2633-30e2-8636-d41729190dfb | -6.80693 | -58.65488 | 2026-08-24 07:18:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 19019e40-eb0d-3390-9a1e-d27359b6d901 | -6.14767 | -57.94707 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ab3fcb5b-1f94-3690-8c7f-924f460bbd9c | -6.22549 | -55.61491 | 2026-08-24 07:18:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 767731d2-1780-38df-8b35-ef5c260a4cea | -6.34528 | -54.75122 | 2026-08-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bee47767-b69a-3f23-b749-436443d1b91a | -6.61696 | -58.38043 | 2026-08-24 07:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bd4dd66-3e39-37a4-85f8-0632eefadfa4 | -8.37722 | -62.68823 | 2026-08-24 07:18:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3a53fbd9-7c42-30b4-8c9a-536561e4c178 | -7.6849 | -63.3443 | 2026-08-24 07:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fd34ac50-1828-389e-977b-349a24af649e | -7.685 | -63.3255 | 2026-08-24 07:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| b68395ca-5590-3feb-a1cb-3ee0a6dff73d | -7.6665 | -63.3261 | 2026-08-24 07:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7471819d-9541-3ecf-9948-efc2befc5037 | -12.0563 | -50.5782 | 2026-08-24 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 7a7c2388-3485-3668-bb8f-64e892ea7c9c | -12.0566 | -50.5567 | 2026-08-24 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| aca7a66f-97da-3c2a-acac-f04d17824bec | -12.05938 | -50.56895 | 2026-08-24 07:20:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 5cd08709-9d93-31d8-a08f-b3dc71e5609e | -10.79742 | -50.93374 | 2026-08-24 07:20:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bed9fc24-9f29-374f-a584-59b8de0c79c7 | -13.17071 | -51.38626 | 2026-08-24 07:20:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 227885c8-462d-3f6e-89d5-074836704ad5 | -10.79734 | -50.94102 | 2026-08-24 07:20:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 2ed85704-7f1a-3f73-b877-53c213ba61da | -10.79479 | -50.95331 | 2026-08-24 07:20:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 919f99b6-b5c1-3464-a3e0-93cf5981fb74 | -11.91161 | -55.89905 | 2026-08-24 07:20:00 | AQUA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 179a6426-1e61-31cf-9dc4-d5c2745aaa18 | -13.87459 | -54.00851 | 2026-08-24 07:20:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |


[Clique aqui para ver as próximas entradas](README49.md)
