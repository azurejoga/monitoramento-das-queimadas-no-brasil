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
| 49fb9d89-c778-3778-a7b5-2956a86b02f9 | -5.79703 | -45.04378 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e1bddc2-dc81-3901-a911-638b0b696f61 | -3.97496 | -47.21013 | 2026-07-03 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad6eaa6d-f2ed-3ae0-9359-19448799d00d | -10.94384 | -43.05023 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.6 |
| d0d8436c-ec49-32ad-9a64-d372c55ee332 | -11.43866 | -46.53363 | 2026-07-03 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9bd6a3b1-4164-37e3-83d6-4c14b40cfdde | -5.80902 | -43.79888 | 2026-07-03 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f3032b9-2a38-3a1b-93f6-966ab3b8c58f | -3.51696 | -48.03465 | 2026-07-03 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb006eec-b701-366b-ba4e-dc7e5634a2fc | -5.94273 | -43.47156 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e74bf36d-acfd-392f-84df-fceb7ed13455 | -5.79241 | -45.05065 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b5c6f75-dc48-30bc-86a0-a39bd4373cbc | -6.03403 | -42.61544 | 2026-07-03 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 18b7086b-1000-386c-96b5-e22532e5d59a | -11.354 | -55.41663 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8661f83-630d-341d-ba44-c6985eae73c4 | -17.30696 | -42.65043 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 21ba368c-10f0-3275-968e-1bda124a2e5b | -4.00961 | -48.06367 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c4f56f4c-0b0c-36c3-ab8b-2bb19b9a83cc | -4.41065 | -42.13688 | 2026-07-03 04:19:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6d7d4399-6661-319c-b568-535da2cf3546 | -10.9819 | -43.70412 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c749b77-d64d-3d7d-8049-6e4fad72efac | -5.79421 | -45.03947 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29eb9398-d0c7-392a-87b2-43a2434cbaa1 | -5.48076 | -45.41376 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1575f92d-9bf6-38bc-8b48-220d418ea3e3 | -3.50803 | -48.03708 | 2026-07-03 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3250663e-59e0-38e0-82d8-6f60bc6f40c2 | -10.94439 | -43.04663 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 96e9d51a-e632-36b8-aacb-dcaa9c7bd3bd | -12.7478 | -44.52594 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bb608c65-354c-3dc7-b0b4-919818aae70a | -11.31148 | -54.47419 | 2026-07-03 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6441f5e7-a792-3c72-9a96-63e2e18eede5 | -17.3183 | -42.64779 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e09ac40-8adb-31e0-8730-2396d54cb12f | -5.90915 | -43.61884 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68827c63-83ed-3e68-9482-1adc40430e58 | -11.35489 | -55.41222 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15b0405e-36c3-3c0a-b04b-09cd66de6004 | -13.98035 | -47.43849 | 2026-07-03 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa482ce0-f1d4-3ec3-a5de-0d267ccbc75e | -13.30014 | -43.55166 | 2026-07-03 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1742ad47-7150-37ce-8114-13e3fb58a838 | -11.35242 | -55.40951 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5972af82-75ad-3d4f-924f-d43e49eb59fc | -5.80507 | -45.03744 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 775dc3af-034a-3627-9ab7-7ffcd1dd8c83 | -17.3171 | -42.65628 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f2c822b-88d0-379e-85ff-4e519daaaf2e | -17.31292 | -42.65993 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66f10603-bf94-3aee-bb34-96cb02753b2b | -11.31852 | -54.46775 | 2026-07-03 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84effd06-7c17-34e5-91b5-027a5b09911e | -11.92076 | -43.38723 | 2026-07-03 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dee22e51-532f-3332-a2d5-432a9db881fd | -11.34716 | -55.41993 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0600498-2379-3603-a3c5-10a99dda1ee4 | -12.75441 | -44.52703 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d0892ae9-8744-3b06-a240-e1f83181f4ed | -12.74505 | -44.52188 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a91d8b-424f-339b-915f-30358a393c5b | -3.51633 | -48.03847 | 2026-07-03 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4338d3c-9f30-3838-a8d9-2f5272275523 | -12.50087 | -43.80501 | 2026-07-03 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b622c02f-85a5-3074-a502-560b9248273a | -11.9202 | -43.39082 | 2026-07-03 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 183dc059-306c-38b1-bc3a-b311f29b6221 | -17.31054 | -42.65095 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7ceb0ff2-8991-3d77-9124-17c15c1fb7ce | -17.31234 | -42.63823 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7205d0eb-9ca4-3ad9-833b-75b5deff47f9 | -5.81178 | -43.80289 | 2026-07-03 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 951fc4aa-cb2a-3ec4-a8e5-520740a10d1c | -12.74669 | -44.53298 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 449f6429-8665-39e1-8b7e-2a73b75f60b3 | -12.75218 | -44.5411 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7df1aa38-f714-39b3-8fcd-f7c8de9494c2 | -12.7548 | -44.5428 | 2026-07-03 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0f4e792b-dfb6-3c38-a85f-c3ad27de3e84 | -10.9588 | -43.0565 | 2026-07-03 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 74ef66da-a4b1-3bed-9674-dabf79de875e | -10.9401 | -43.0355 | 2026-07-03 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 304.2 |
| b5a7b9b0-f334-3759-b4c9-ef8bb2f2c282 | -12.7359 | -44.5225 | 2026-07-03 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 59d2e58f-443e-3cfa-a70c-c0165e2ad5f6 | -5.7945 | -45.0586 | 2026-07-03 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ce2d7682-d5d3-319d-9bcc-3b9afc597fa0 | -12.7557 | -44.4959 | 2026-07-03 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| d69f41f7-ccde-3917-990c-c30f3c751be8 | -10.9593 | -43.0326 | 2026-07-03 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| cc5345b3-856d-3b37-ac00-d7b896c277a9 | -10.9397 | -43.0593 | 2026-07-03 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.3 |
| f206a090-2fbb-3722-a7b1-1b56c4c12479 | -12.7746 | -44.5162 | 2026-07-03 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 57128dda-6955-3999-8b4e-0f4c47ef2860 | -12.7553 | -44.5194 | 2026-07-03 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 472.1 |
| 8b3083de-246b-3222-9f40-766e90890fef | -19.51044 | -52.74214 | 2026-07-03 04:21:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f0c9d5f-4962-30cb-9aab-4d053592eea7 | -18.40876 | -44.34747 | 2026-07-03 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 995df9e4-4432-3002-be2b-1ceeb763ccd7 | -21.49545 | -48.54027 | 2026-07-03 04:21:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 176811f3-244a-397b-a8b9-9949b40ab5e9 | -21.58807 | -49.08496 | 2026-07-03 04:21:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2249e6e2-89d6-3a7c-a7ad-9f8eb1f21e58 | -17.71848 | -46.78524 | 2026-07-03 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaeee70a-cf59-37fa-9ffb-1dcaff5f536b | -19.50604 | -52.73394 | 2026-07-03 04:21:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5003e351-92a2-3b59-b3e5-a25f2b46a241 | -18.52342 | -47.24149 | 2026-07-03 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52f643a5-e5b3-35b3-84b2-f27248036954 | -19.50702 | -52.73673 | 2026-07-03 04:21:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6be0aca-b86f-3bec-a3d7-61ba75f6d700 | -20.56957 | -47.85615 | 2026-07-03 04:21:00 | NOAA-20 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f859c526-d8dc-3050-8911-f76a31545d13 | -17.71575 | -46.78099 | 2026-07-03 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 058de559-4ec4-305d-857c-007a89cd6e83 | -23.44106 | -45.09308 | 2026-07-03 04:21:00 | NOAA-20 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 13ad5c7b-fb4e-3bf3-b937-35e8a771fd7c | -18.50634 | -51.66396 | 2026-07-03 04:21:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4892d3e6-8d64-3879-bab8-4c2243e97cc5 | -20.18348 | -45.80853 | 2026-07-03 04:21:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3b07968b-3371-30f6-b538-8a28ad06da2d | -23.79863 | -46.0831 | 2026-07-03 04:21:00 | NOAA-20 | BERTIOGA | SÃO PAULO | Brasil | 3506359 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e1c0a3b6-d0e6-3cbd-8e5c-def6e8ef2466 | -19.18503 | -42.43771 | 2026-07-03 04:21:00 | NOAA-20 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| defef190-90dd-3e2b-99e1-689d31c10953 | -21.61636 | -48.86333 | 2026-07-03 04:21:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b93c807c-0d06-3896-adf5-db1f3f9424e5 | -19.50522 | -52.73827 | 2026-07-03 04:21:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3036e08-7589-3314-aafe-882b1d7e16ae | -21.06169 | -43.19947 | 2026-07-03 04:21:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 15293ff0-76da-3a5f-9f14-34d473e550e6 | -22.79485 | -49.34995 | 2026-07-03 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45113561-3a79-3f95-b876-4d638a3996ac | -18.50768 | -51.66451 | 2026-07-03 04:21:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee80e4ee-1880-3cf6-a514-6f8dda7bfc0f | -23.82023 | -48.71169 | 2026-07-03 04:21:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eae9378-e5b1-3b96-a8cc-e4c082ff0c27 | -17.71515 | -46.78466 | 2026-07-03 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ca01d82-5db2-3a15-86ed-7b307ba1c86d | -22.79141 | -49.34924 | 2026-07-03 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 789bac45-e8cf-3304-b53a-a105a286b101 | -18.52677 | -47.24209 | 2026-07-03 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4711de1-86b1-3c9c-a362-c6dc64eda59d | -20.51774 | -44.08319 | 2026-07-03 04:21:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 384bf946-c9b7-3c1f-9831-496b64108de8 | -22.34253 | -41.78428 | 2026-07-03 04:21:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0e6449ac-7a3e-3c8c-9565-97709658c080 | -21.11093 | -49.00051 | 2026-07-03 04:21:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3e046ecd-4e8e-33ae-b4a4-288ff9986379 | -22.53832 | -46.96981 | 2026-07-03 04:21:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 512dbd9c-88b0-3762-b38d-d2d4d353245d | -18.63894 | -51.83178 | 2026-07-03 04:21:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b21475c4-75e1-3002-ad2e-f7a36cacce0c | -22.34508 | -41.7834 | 2026-07-03 04:21:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f2c5c9cb-10a5-33ad-8b3c-6340d462ed8a | -19.4487 | -44.64484 | 2026-07-03 04:21:00 | NOAA-20 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6fe837b-96ad-387c-96a9-3604cff139f4 | -20.76676 | -48.56718 | 2026-07-03 04:21:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fb2fa3b-4d91-39d3-a1c9-0ff001701014 | -22.82815 | -47.15644 | 2026-07-03 04:21:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a3b5e7fa-8b7b-37bf-ab6b-ac412ea49dfa | -20.42953 | -47.55132 | 2026-07-03 04:21:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03221495-a73e-30e5-8654-28d96b2949ca | -21.58921 | -49.08598 | 2026-07-03 04:21:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35c08cf9-a803-38cc-b1d8-5cb0736c1067 | -21.11162 | -48.99649 | 2026-07-03 04:21:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| de3c920a-f3b9-35fa-a1f9-7fd9ff78af4e | -22.53501 | -46.96921 | 2026-07-03 04:21:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.1 |
| f85b97d0-6d4a-3366-ac91-8cd542e5e261 | -21.70543 | -47.16499 | 2026-07-03 04:21:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 88239fab-f62d-35ee-9d82-4555073c2321 | -22.72668 | -43.84539 | 2026-07-03 04:21:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0e03e316-dc71-3993-a625-4da51b3c3327 | -21.49207 | -48.53962 | 2026-07-03 04:21:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4fac42c2-2310-35d4-b428-c5847479e91e | -19.5113 | -52.73774 | 2026-07-03 04:21:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a168ce2-334d-30ea-be1e-81d4346c36c6 | -21.10748 | -48.99984 | 2026-07-03 04:21:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b5f5d9b5-e0f9-3545-80ae-9ad7223b6de5 | -20.05996 | -41.86644 | 2026-07-03 04:21:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6a4ebc6b-6a9c-3488-b895-1fa69678f7cc | -20.43177 | -47.55115 | 2026-07-03 04:21:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a457667-ae8d-3658-8586-99623101230c | -22.72482 | -43.84307 | 2026-07-03 04:21:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d7e441f-0453-30b1-81e2-e1064c6beda6 | -22.79555 | -49.34586 | 2026-07-03 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba3a551-ba15-3286-b479-11e3d95d0f04 | -12.7548 | -44.5428 | 2026-07-03 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 2b4ee277-c2e0-3c9c-8892-8e83da8b80e4 | -5.7945 | -45.0586 | 2026-07-03 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |


[Clique aqui para ver as próximas entradas](README14.md)
