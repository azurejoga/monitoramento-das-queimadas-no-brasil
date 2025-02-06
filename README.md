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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d55f51b-dfc0-3d86-bad1-d18b61f1d5c5 | -29.6301 | -56.6556 | 2025-02-06 00:00:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 149.7 |
| 527e6154-21c8-3365-b917-2834362a8e2e | -29.6307 | -56.6325 | 2025-02-06 00:00:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 133.9 |
| 186c6f74-12a9-330a-9850-454ba96f095f | -29.6073 | -56.6607 | 2025-02-06 00:00:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 126.7 |
| 73383d5c-5424-3669-920f-fd54e385f398 | -29.6307 | -56.6325 | 2025-02-06 00:40:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 155.6 |
| 0f995216-a596-3037-a2d4-55f9606cf50b | -29.6079 | -56.6376 | 2025-02-06 00:40:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 117.6 |
| d2805fde-13ea-30d0-bc73-0f8bae8d2db5 | -29.6301 | -56.6556 | 2025-02-06 00:40:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 220.0 |
| f628f6f5-3681-3105-a867-f20d876a2567 | -29.6073 | -56.6607 | 2025-02-06 00:40:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 171.0 |
| 5047d5c2-626f-30e2-a615-902dcba3641d | -19.04695 | -42.5319 | 2025-02-06 00:41:00 | TERRA_M-M | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f6e71ff8-82b2-3b8f-bdd8-7daadcbd624f | -20.38866 | -43.81361 | 2025-02-06 00:41:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 60cee23b-721d-3a40-94cd-f00d932f9cbd | -20.20489 | -46.66013 | 2025-02-06 00:41:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 47d81829-cebd-375d-8ad2-8e0dd8661b28 | -20.34725 | -41.37959 | 2025-02-06 00:41:00 | TERRA_M-M | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d66fc98c-48b0-3439-b6ed-5d2ed488cf5c | -18.1744 | -40.53533 | 2025-02-06 00:41:00 | TERRA_M-M | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 113bea4c-e6a0-3a7b-ba82-e35796a6f754 | -20.90593 | -42.57473 | 2025-02-06 00:41:00 | TERRA_M-M | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1cc42bcb-d726-330a-bc65-ad8470558b1a | -20.90748 | -42.58493 | 2025-02-06 00:41:00 | TERRA_M-M | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 95d3fa57-9545-3692-8560-0651280f7f35 | -20.30924 | -40.75347 | 2025-02-06 00:41:00 | TERRA_M-M | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 3c9f765c-5cbe-3a24-b51a-681e481965be | -20.9976 | -43.37262 | 2025-02-06 00:41:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| bea00061-f731-3fcc-892f-b67bc7a2685e | -12.10346 | -44.7446 | 2025-02-06 00:43:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2f9290ad-547a-3d18-b018-e16105d10b8a | -12.41451 | -43.80207 | 2025-02-06 00:43:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7ca1f04f-9471-3d7b-be12-fac45cdac9ce | -12.41135 | -43.80899 | 2025-02-06 00:43:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 10e9eaba-e389-3ab3-a8c4-eec3418a22aa | -11.49479 | -43.2226 | 2025-02-06 00:43:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c97d29b9-fcd1-3357-8c9f-fed68d17e69c | -11.57964 | -47.63652 | 2025-02-06 00:43:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3b8b1dc4-28e8-3d43-a813-acf598d7c41d | -16.03528 | -42.14248 | 2025-02-06 00:43:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 0147137f-f72e-34c9-b279-af94ae02aae2 | -10.7785 | -44.75827 | 2025-02-06 00:43:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6856f7b1-085f-3d1a-ae0f-64c5907c0c79 | -15.64269 | -39.18538 | 2025-02-06 00:43:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| e8f3b5b3-c786-32c4-9f5f-7e22c8a19649 | -11.58858 | -47.63519 | 2025-02-06 00:43:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a6f76cb9-f650-3a61-a932-3bfe6719e6e0 | -10.6591 | -44.50509 | 2025-02-06 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 86303307-c866-30bb-a78d-a72349a2f096 | -10.65761 | -44.49483 | 2025-02-06 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| e993c3f5-ff40-340a-8d26-6719778ae682 | -16.03382 | -42.13648 | 2025-02-06 00:43:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 26d4ae79-2577-3242-96c3-aec356c59824 | -12.74454 | -44.83538 | 2025-02-06 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b071b5f0-d84b-3328-bcae-bc19fbefc38e | -12.85565 | -43.82701 | 2025-02-06 00:43:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 090e47f0-3edc-328d-844a-205bba17eb1e | -12.49098 | -43.78972 | 2025-02-06 00:43:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8a9da188-9973-3239-afc3-a000154e6002 | -8.34968 | -45.17926 | 2025-02-06 00:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b558a69-0a53-35cd-84e6-26b038884d29 | -10.34421 | -47.89753 | 2025-02-06 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 08583aa4-dc5f-3d38-8bf8-228da7a0cd8d | -7.03459 | -44.36866 | 2025-02-06 00:45:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aadc9020-6482-314a-bdb5-59a1db23df45 | -10.34546 | -47.90675 | 2025-02-06 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 35fa3738-20dc-33c4-a4cf-0a4cec420d08 | -10.35613 | -44.84665 | 2025-02-06 00:45:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 695722ea-2ad9-3963-9482-a57831244bbc | -6.39922 | -44.78218 | 2025-02-06 00:47:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5450ed98-1e17-3890-9dbe-a193f0153003 | -29.6301 | -56.6556 | 2025-02-06 00:50:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 123.8 |
| ed182abc-d654-3394-9c45-65a66239b0ae | -10.6591 | -44.4776 | 2025-02-06 00:51:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80c5d369-7597-3b87-9b79-9f7a9d5921af | -11.5925 | -47.6227 | 2025-02-06 00:51:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd33ef38-d6ee-38c9-a963-feeb8c608a0d | -29.620001 | -56.602501 | 2025-02-06 00:51:00 | METOP-C | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 09cc513b-a792-3992-bc05-bdcf8f5af390 | -10.6619 | -44.489201 | 2025-02-06 00:51:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa25b653-f367-3c77-b722-0480b281f5c3 | -11.5943 | -47.630402 | 2025-02-06 00:51:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa7289bf-81d3-32a5-8332-6a7b3cf2562b | -10.3547 | -47.892601 | 2025-02-06 00:51:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2db2f760-ce5b-3295-aff9-f5c07e0064a4 | -29.623301 | -56.628101 | 2025-02-06 00:51:00 | METOP-C | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| a0aeebe8-bab5-33cf-a8e9-aa3dca4eb75f | -12.4997 | -43.771999 | 2025-02-06 00:51:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b52f667e-3964-323a-8a75-92224d6f0a7e | -29.629601 | -56.600899 | 2025-02-06 00:51:00 | METOP-C | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| d2fed023-f748-3fff-8e01-1ef78f5b8ffa | -22.925501 | -43.7216 | 2025-02-06 00:51:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3dcfe20d-7a68-3530-a5ca-0d9a30c3d0e0 | -29.6103 | -56.604099 | 2025-02-06 00:51:00 | METOP-C | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| f3ce2448-a39b-3403-a0ac-d1a919caba1f | -29.6329 | -56.626598 | 2025-02-06 00:51:00 | METOP-C | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| f568afd9-e996-35a5-aca3-774e30b72451 | -12.5028 | -43.784 | 2025-02-06 00:51:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ad3a432-78dc-30c3-b4fc-3425eb2bb8c5 | -22.927601 | -43.730499 | 2025-02-06 00:51:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c087a296-076d-36c5-9368-89d038cc4fdf | -10.6688 | -44.475201 | 2025-02-06 00:51:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee566851-278c-35f7-b754-cc3806944b7c | -29.6136 | -56.6297 | 2025-02-06 00:51:00 | METOP-C | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 079a1152-9aab-3858-b523-b61dc4c642b0 | -10.6717 | -44.486801 | 2025-02-06 00:51:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b6aafb7-e846-315f-8623-44b6324a1f02 | -29.6301 | -56.6556 | 2025-02-06 01:20:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 126.2 |
| 4bbc617b-692f-3fd8-8afa-884f2812aef5 | -29.6408 | -56.634201 | 2025-02-06 01:36:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| f0e506c1-3dbf-3731-9e1a-b70c397d13e1 | -29.631201 | -56.637299 | 2025-02-06 01:36:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 50698b1b-05f1-34a6-ad55-2a0b26c1773c | -29.6478 | -56.620201 | 2025-02-06 01:36:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| dd33e74b-77df-31bc-b7d5-a559266ea089 | -29.6215 | -56.640499 | 2025-02-06 01:36:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| aa615de2-1feb-319a-98b1-164236f95c8b | -29.650499 | -56.6311 | 2025-02-06 01:36:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 5a8d510d-920a-3103-a655-9561891b8425 | -29.624201 | -56.651402 | 2025-02-06 01:36:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 5cd4a5b5-8f23-3933-970f-9625b3f2bb04 | -29.6381 | -56.623299 | 2025-02-06 01:36:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 7fac310b-930b-34c6-a350-f1c6dad2ba50 | -29.6301 | -56.6556 | 2025-02-06 01:40:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 130.9 |
| 76e7eb9e-43fc-30be-b849-4539f4ae13d2 | -29.6301 | -56.6556 | 2025-02-06 01:50:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 109.0 |
| 3ce3f025-76d5-3f8c-8c91-936765f0da1c | -29.6301 | -56.6556 | 2025-02-06 03:00:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 65.2 |
| 4dd048e9-3171-3fd7-9861-1a8229ce66e3 | -10.7796 | -44.75535 | 2025-02-06 03:23:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f4cb197f-2707-37ec-a730-ced32187c469 | -15.64542 | -39.18965 | 2025-02-06 03:25:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fa7a819e-f62f-3a39-999d-f8e2a512a96e | -19.47674 | -40.08505 | 2025-02-06 03:25:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 85f55dec-209e-3512-b067-2541f71443b8 | -12.41404 | -43.80296 | 2025-02-06 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dc7893e-bd8f-3215-9aa7-4ea0ce143a4d | -12.84621 | -43.82178 | 2025-02-06 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afbd990c-1a37-399a-af2b-59c464f28c67 | -12.84875 | -43.8201 | 2025-02-06 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a85ed05-b043-3467-b8f3-94db6e94cef7 | -17.62756 | -39.2854 | 2025-02-06 03:25:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9492b91f-6235-34d5-ae9b-c1ee2ed5f0b6 | -19.4903 | -43.52972 | 2025-02-06 03:25:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 734d73cc-4b0a-3452-980b-c14f4cf8055f | -13.61424 | -42.24461 | 2025-02-06 03:25:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 806884aa-cbbf-3136-9000-6a5a3489ee3e | -12.85246 | -43.82299 | 2025-02-06 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25e2c1c2-9ea4-3d9a-9e6f-5f193412019d | -12.84774 | -43.8251 | 2025-02-06 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9946ecf1-1465-3c7a-b954-62144092b9d5 | -19.49654 | -43.52706 | 2025-02-06 03:25:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16cc1fb3-585f-3785-9b06-1e6af133ba41 | -12.49214 | -43.78988 | 2025-02-06 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 04411648-89c8-36ce-b68f-67310e679591 | -12.48591 | -43.78847 | 2025-02-06 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95faaf83-b07b-3285-9893-4208d9dad99c | -17.09447 | -43.80573 | 2025-02-06 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ebbaf25-b7ae-3a2c-ac28-a1f49b2a6f9a | -12.74173 | -44.83496 | 2025-02-06 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bb860d1-d5eb-3df6-a632-9cdc3995c67c | -19.71474 | -40.07695 | 2025-02-06 03:25:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 15f337c8-ea5f-35ae-8971-81acca72d27e | -19.83747 | -40.0825 | 2025-02-06 03:25:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3f9563c8-6e66-3a44-8cd0-76cd54489aa5 | -18.61188 | -44.25412 | 2025-02-06 03:25:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 941d6f78-0fcd-342f-a0c2-ebe861dddbda | -13.90706 | -38.94857 | 2025-02-06 03:25:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bf7a4114-09a2-3178-8061-8f9f131716eb | -15.38218 | -39.21714 | 2025-02-06 03:25:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea4997d3-1d83-3a5c-b9e0-dbb6d0abd48c | -13.90258 | -38.94771 | 2025-02-06 03:25:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| be425ab1-37d1-354f-8e07-77bc462a5612 | -12.85499 | -43.82135 | 2025-02-06 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6a75714-4535-3cc8-8bcf-864a8c5c24c6 | -18.17372 | -40.1804 | 2025-02-06 03:25:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51abaaf8-2432-3bd3-a839-035d271b434e | -20.21538 | -41.09591 | 2025-02-06 03:25:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9db447a3-297a-3924-b9d9-238f5beb9b53 | -13.613 | -42.24192 | 2025-02-06 03:25:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec1f33d2-575c-365a-9063-34460ddd61d3 | -20.34359 | -41.37574 | 2025-02-06 03:25:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cd7d0cbf-7864-37ba-9a9a-fd017fe827dc | -18.61097 | -44.25837 | 2025-02-06 03:25:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3695ba3-8ecf-3361-b797-09f7b9147995 | -12.4171 | -43.80549 | 2025-02-06 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d571bff6-6e32-3568-bab4-e537ac623af3 | -19.71148 | -40.0755 | 2025-02-06 03:25:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a792f681-263f-31e5-ab24-6d9d195fce44 | -18.61161 | -44.25705 | 2025-02-06 03:25:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9c9fa06-5545-315b-a41f-92b605bb588a | -20.9094 | -42.58203 | 2025-02-06 03:27:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 219839a7-d132-3952-b88a-1e0354a737de | -22.84326 | -43.48767 | 2025-02-06 03:27:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ea2ea957-0638-378c-89d0-a3d62209b116 | -20.90449 | -42.58067 | 2025-02-06 03:27:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
