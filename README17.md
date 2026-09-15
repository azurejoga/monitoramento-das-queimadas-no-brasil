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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f418bb2-3c3a-3b55-a3e5-72ef160947f6 | -9.4139 | -50.1103 | 2026-09-15 03:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0560fe4a-3938-31d6-8d6c-1448b64e5fd0 | -11.884 | -43.8142 | 2026-09-15 03:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e01ce77d-e5a8-3086-9796-3e64d04fd112 | -6.8446 | -55.5611 | 2026-09-15 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f51ab01b-506f-3dbd-a397-5c0561b4cf47 | -18.1714 | -51.7466 | 2026-09-15 03:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 19ce56b0-928f-36a5-896d-08ad1aab82f3 | -13.2427 | -51.6508 | 2026-09-15 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 5293a92a-b011-357c-9b86-d708a40b8150 | -7.244 | -46.1603 | 2026-09-15 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| e2ba9ebe-9f9a-37d0-aacb-144ce35bab79 | -3.552 | -53.9934 | 2026-09-15 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 902dcd3a-f376-3c49-b4fc-24b33674a318 | -14.2046 | -47.4265 | 2026-09-15 03:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8b958532-4968-3de4-b001-03f816851875 | -6.6953 | -58.6903 | 2026-09-15 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 092a8a76-18f1-342b-9504-3aee4904daa4 | -2.9025 | -50.4214 | 2026-09-15 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d57d733b-296a-34b8-9418-a5d822a97507 | -18.1709 | -51.7685 | 2026-09-15 03:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 6a962869-baa7-3dbf-9e62-4abf5c58d70e | -3.728 | -61.7555 | 2026-09-15 03:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a503c332-4d1a-3525-b7b7-f9c23fdb2b7b | -3.7462 | -61.7552 | 2026-09-15 03:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a128971f-cfd6-3b81-9b9c-564fd1af0de8 | -3.7463 | -61.7363 | 2026-09-15 03:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 759b53bd-d2a5-3e7e-b4a7-c92344e3b182 | -3.728 | -61.7367 | 2026-09-15 03:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| a2632b9e-d5a7-3a05-a0a1-774b0fb3038d | -3.728 | -61.7555 | 2026-09-15 03:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e1848e72-d9f3-3780-8c6e-caa9843177b8 | -18.1709 | -51.7685 | 2026-09-15 03:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 9ab1b6f1-9220-3faa-bf79-d537647bb63b | -18.1714 | -51.7466 | 2026-09-15 03:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 377da6d5-79b0-3109-b535-a7d01e15cf7d | -9.4139 | -50.1103 | 2026-09-15 03:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b241187a-7f6b-3067-abb6-170132955aa7 | -3.7463 | -61.7363 | 2026-09-15 03:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| ad347a8e-9c14-3886-995c-b07f35794f47 | -3.552 | -53.9934 | 2026-09-15 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 92ebc4af-ad6c-3967-aa9a-2d39ff3af431 | -11.8836 | -43.8378 | 2026-09-15 03:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7e755c0a-a37f-3315-b556-5ccb63edbea8 | -14.224 | -47.4234 | 2026-09-15 03:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c488470f-e610-3e22-bfa6-2fc0b410ef37 | -14.205 | -47.4039 | 2026-09-15 03:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e1329740-d954-367e-b842-0cdca080c7be | -6.1109 | -57.684 | 2026-09-15 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| fe358f84-5fe0-369e-af6b-32998d416aaf | -11.884 | -43.8142 | 2026-09-15 03:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1b1e734b-57d1-3e66-96f3-5bcbd2b525bf | -14.2046 | -47.4265 | 2026-09-15 03:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 104.8 |
| fddc6d2d-e7e0-376e-a9db-c87afea7130c | -3.5336 | -53.9939 | 2026-09-15 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| f6ee893d-1288-3ca3-8e08-fe55f2b15398 | -3.7462 | -61.7552 | 2026-09-15 03:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b346d22a-a0ff-307c-9e4b-1ed955c0d1c1 | -11.5049 | -45.7481 | 2026-09-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| e97eee37-148c-3fb5-ad08-163c4c8ba0ca | -7.244 | -46.1603 | 2026-09-15 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 2a71f798-381a-314a-a65d-aeb4af72d2f2 | -11.4857 | -45.7508 | 2026-09-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 00a3d8bc-57a8-39ef-acd7-571c9a7f940c | -6.6953 | -58.6903 | 2026-09-15 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 541883f3-e63f-32b1-aba4-7e061f8f2fe6 | -6.94789 | -42.56225 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4056d5b8-fd88-3ae3-bd04-7673614cb14c | -7.09266 | -41.8243 | 2026-09-15 03:36:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c58800eb-0e46-3c5b-a1b8-e7eeb310f2bb | -4.24412 | -38.05925 | 2026-09-15 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 07ea2443-0850-3c99-83fd-66be1183d95a | -6.74133 | -43.08774 | 2026-09-15 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c604c9a2-543b-3c63-86a9-ac0a6e57e648 | -7.09847 | -41.81973 | 2026-09-15 03:36:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b47c9718-a4a0-3973-82b6-e6a7dda5243f | -6.82877 | -43.51959 | 2026-09-15 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7cf3d49-e87d-3f9c-8054-ecb51111c95b | -6.61247 | -44.20528 | 2026-09-15 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77e34a14-f75e-33ee-8130-c80916c6e3aa | -6.81071 | -43.1801 | 2026-09-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b171bb5c-5504-3667-be0b-8490cefd9006 | -6.95349 | -44.54171 | 2026-09-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5c713b7a-6f8f-3607-8ad7-49df7a158b94 | -6.61267 | -44.2086 | 2026-09-15 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e027628-81b7-3d61-97f8-22ca35b5a55a | -7.16355 | -42.09778 | 2026-09-15 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01d12756-e0ba-31ee-806e-220be3b4f095 | -7.09067 | -42.13358 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 13a929e5-2012-35dc-b545-f073bbe02714 | -3.96683 | -43.11454 | 2026-09-15 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d415cb96-e507-3282-b1e2-0b20a5f5a44b | -7.16418 | -43.52258 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6d4a865d-980d-3d12-9b2f-8d723b0944ec | -4.66341 | -42.08519 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 1c27215b-c24c-3317-a970-fff8e1d96d9e | -7.16233 | -43.52779 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 36e1976b-b26e-3425-8171-83f210755b6d | -6.96005 | -44.53872 | 2026-09-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d170ee63-407e-31e5-a63d-7343f056ed77 | -5.53273 | -43.36997 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9349598-3072-3fe0-99c7-2002c73de9a8 | -7.08407 | -42.10889 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b2dfcb0-8fb8-3bd3-af06-aa0086ad4fc2 | -7.07861 | -42.11088 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1c6bb92-5007-32ae-aea9-4ef85ba4e6af | -8.3865 | -35.34546 | 2026-09-15 03:36:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87ef4bd6-7810-3f5e-b551-ff4ca7653f68 | -3.97242 | -43.11551 | 2026-09-15 03:36:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 174e1a6f-7a29-3bf8-be31-c926d43d6c9e | -7.48364 | -42.12433 | 2026-09-15 03:36:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a6c9586-8078-36ff-8136-0b46790663b8 | -6.95354 | -42.56022 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d5810bdb-14b9-3720-86a6-dca2bf2b2d6e | -7.08058 | -42.12923 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a314b26d-d1c1-3551-a13f-f23137d34340 | -7.24783 | -39.28229 | 2026-09-15 03:36:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 90394329-f897-3464-8213-7ca10e36228d | -4.46821 | -38.50423 | 2026-09-15 03:36:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b32438a0-a700-3af7-a5fe-92be8d381d8a | -5.63417 | -40.85497 | 2026-09-15 03:36:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 581681d6-e1f7-3263-b3a5-b963d6df76b4 | -5.74173 | -43.27738 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d8bf64b-f4e7-37e8-93c4-54232b429518 | -4.66911 | -42.08293 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 82bd1a8d-8f10-335c-8bcd-c9ab4fe7c710 | -6.80804 | -43.17935 | 2026-09-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7ce8069-c63a-331b-beb4-22d3df5ad585 | -4.9581 | -45.14719 | 2026-09-15 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89468ac3-0902-3297-a53a-9de82b4e5f58 | -7.09003 | -42.10399 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65405092-c32e-3c0a-8cad-be126be87aac | -7.16905 | -43.52153 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 75fce291-0e6b-3ce8-9ce9-e0455514cce4 | -7.5609 | -41.84512 | 2026-09-15 03:36:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c692095-a04e-3e65-8057-45274d763ee2 | -8.02998 | -39.00203 | 2026-09-15 03:36:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 216b0c96-4bf7-3dca-8d1c-c0f8be3a0bb1 | -4.66393 | -42.0821 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9215f118-5fa1-3733-b97a-595dc8a757c7 | -7.24844 | -39.27858 | 2026-09-15 03:36:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0e7cd0cd-d920-32aa-8422-4c6074435784 | -3.89796 | -38.41562 | 2026-09-15 03:36:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a3c4860c-92e6-3688-a5fd-d1db27ce5b70 | -8.38372 | -35.34138 | 2026-09-15 03:36:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d8e18e86-5d0d-3896-be70-c99b00f6dcae | -8.38707 | -35.34191 | 2026-09-15 03:36:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52dbf9f3-750a-321e-aacf-62b7ff0329eb | -7.16294 | -43.52426 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 11fa65c6-cdea-37a4-8634-d12e2e4d6842 | -7.2983 | -42.35822 | 2026-09-15 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9f5b205-4dc5-32c0-beda-46ca22f30261 | -5.60308 | -44.84568 | 2026-09-15 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7af9f843-3f75-3156-ba8b-41429c55242e | -6.61341 | -44.20452 | 2026-09-15 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9938890e-850c-3fe2-a811-e4dd97ddefc0 | -4.67428 | -42.08378 | 2026-09-15 03:36:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db4a9349-4d49-3cab-b2d4-b31a33d76e3a | -7.13797 | -42.12706 | 2026-09-15 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 564232fb-3284-3b3a-8510-88d8ce9299aa | -5.61307 | -43.56102 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a69d27a-f157-3138-b2f0-5bbd6f315191 | -6.52891 | -42.2466 | 2026-09-15 03:36:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 62c199fe-bd20-35fa-a09c-2e0c47339f8e | -4.15741 | -40.85833 | 2026-09-15 03:36:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22612328-d9af-3b2b-a051-c5900c686e11 | -7.55988 | -41.85074 | 2026-09-15 03:36:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3815f7ec-fb0b-3357-9574-7e9764ff61b4 | -5.63492 | -40.85053 | 2026-09-15 03:36:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ac90ff49-3e82-3df7-a62f-23243f003ee7 | -7.16901 | -43.52697 | 2026-09-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dce14cf7-66df-341e-90bf-27d84b634396 | -5.43021 | -43.99289 | 2026-09-15 03:36:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86aafdbe-677e-3879-99dc-ff89ec5eca13 | -7.56156 | -41.84914 | 2026-09-15 03:36:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 833ebb73-4a3e-375f-a156-e458193ed13b | -7.02209 | -44.62357 | 2026-09-15 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e8be30c-f77c-3692-911f-0ac466ae0aa9 | -7.01698 | -44.61831 | 2026-09-15 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a020c369-21a5-3735-9f52-850272a69790 | -8.02544 | -39.00476 | 2026-09-15 03:36:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 280a8045-a07a-3b39-a077-bc6be67d1b05 | -5.55474 | -43.43454 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e6db8fc4-3ec5-380d-b20d-f85607a14d8f | -4.15685 | -40.86045 | 2026-09-15 03:36:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c9c1a33-bd07-3f2a-8640-5eb376ff0a1d | -5.55407 | -43.43831 | 2026-09-15 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fbcb33f2-9220-3a55-abbc-ccddd119ccef | -6.76957 | -42.74686 | 2026-09-15 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0747e8c8-003f-3cb2-a2e8-157829209f97 | -7.10664 | -42.09653 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6889cf6d-9dc2-37d4-8c62-a1584c648cee | -7.09105 | -42.10278 | 2026-09-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9962d7ac-2603-3e87-8ed2-99b27f1c5bda | -6.95861 | -44.54681 | 2026-09-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 34e2b5b7-7b51-3426-9e13-89ede45abb5f | -8.02486 | -39.00824 | 2026-09-15 03:36:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 901dd931-7b0b-3fb1-bb31-987df58cc063 | -7.24434 | -39.27794 | 2026-09-15 03:36:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README18.md)
