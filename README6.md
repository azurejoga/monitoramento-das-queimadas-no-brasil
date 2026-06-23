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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93801ce5-5a15-342f-98c4-f1c076472ca5 | -9.2188 | -45.32782 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 249fe742-17d2-34f0-b720-eb666b744bd9 | -11.97644 | -47.12012 | 2026-06-23 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47a8444c-1b6c-30fc-93bb-120a5e4f9c90 | -13.20384 | -48.32317 | 2026-06-23 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ffbc0bb-ca81-3330-a14a-58bb06397da8 | -9.21947 | -45.33812 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 76816257-89f1-3a12-9997-aa0b51e6aa0d | -5.82465 | -45.07143 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fbd067d0-7dd5-3416-8b35-14b68247d29e | -15.38525 | -40.82475 | 2026-06-23 03:47:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c5eb14e-c552-3a93-b79f-2620790a91e9 | -8.08496 | -46.3913 | 2026-06-23 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20fe0907-7017-38fd-ad8e-8e8cccdbb12b | -9.21801 | -45.33208 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f16160d-e503-3d99-8a01-fc72a3ee0777 | -8.87402 | -46.93852 | 2026-06-23 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4803719-0a58-3052-b37e-f94101a0b7d4 | -12.91668 | -49.47845 | 2026-06-23 03:47:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2773eeec-2d0e-342b-9c8c-2bfb778125df | -9.2203 | -45.33382 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6bec685-d8c8-3223-80fa-6ca5eb8c55eb | -9.22113 | -45.32956 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d01d4e2-9b9b-3483-8eef-04b74bffada7 | -12.50342 | -48.27036 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3a5a0c72-3f42-350d-805e-db80a9144ef5 | -11.81644 | -47.34002 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92154465-cd5c-3626-a538-6dbe7ccecbd2 | -6.50751 | -42.22192 | 2026-06-23 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 43424c6c-1ec4-346b-b1d8-aa9b19cb5e5e | -12.87419 | -44.36032 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7c995dba-c3c1-302a-91e5-37f46ac99cea | -5.80095 | -43.79355 | 2026-06-23 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fe3e1af-cf59-3b3c-87ce-a0bc218c1021 | -6.996 | -42.89488 | 2026-06-23 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 397342c8-ec8f-31d9-9430-569f63457a35 | -3.86516 | -42.96975 | 2026-06-23 03:47:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd87fa3f-7b17-3d04-9966-cc83a4fbbb73 | -12.03648 | -47.80255 | 2026-06-23 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d10c716a-7a01-36ba-bd31-3e0ccaf530c9 | -11.28167 | -43.34175 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 53a800e9-1904-3e25-9cb9-138f9a9f6587 | -11.88957 | -43.84098 | 2026-06-23 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32e48c66-5e2c-34be-94ad-aabe71bff51d | -11.90551 | -43.41202 | 2026-06-23 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 923e133b-153e-35e0-8f92-dfbc68009779 | -11.9869 | -45.14958 | 2026-06-23 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 158ed678-7b75-3cad-9082-ae9a22ad8050 | -12.01054 | -40.11436 | 2026-06-23 03:49:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 694c864a-49b8-3edd-8918-1ce494753b39 | -17.61408 | -46.70016 | 2026-06-23 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c4ae80a-0f53-3126-9045-172681071287 | -11.47322 | -46.68317 | 2026-06-23 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b87b259c-594b-3c7b-b500-e31dc61f79b2 | -20.34195 | -46.62405 | 2026-06-23 03:49:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951daffe-e948-39a3-968b-68b6d01da14c | -11.58233 | -47.43681 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 265bc147-ece3-3c6b-88a7-b79c6e2d951e | -12.12094 | -38.67294 | 2026-06-23 03:49:00 | NPP-375D | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 563c0942-afbe-392c-a037-48d481d6618a | -10.56611 | -46.22921 | 2026-06-23 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb7978a0-5a32-35fd-9e9b-2cff42251e0c | -11.99248 | -45.15072 | 2026-06-23 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b513f22d-0da0-3075-a0af-c2fdd433573c | -11.5759 | -47.43527 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd203625-36f6-3a01-aa5d-a4333848f975 | -10.97341 | -48.15828 | 2026-06-23 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9076bd7e-e4b7-36da-92b2-9ee120e88d7d | -11.76804 | -38.26464 | 2026-06-23 03:49:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c7825833-1eb7-32b5-9967-745edea0a7c0 | -11.2928 | -43.33794 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 9680bcc0-abd4-39b5-8a48-c3153374de24 | -11.28779 | -43.33686 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f0c09a88-6ee0-3311-86a3-75f5c8a6722e | -19.15914 | -40.09002 | 2026-06-23 03:49:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 32fc0ff7-39a7-3927-b87e-92a3e6fee7d8 | -19.19228 | -39.79302 | 2026-06-23 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| df72b1e7-929c-317b-93a9-7536ba7d9766 | -11.46593 | -46.6874 | 2026-06-23 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26cf33f6-49fc-33ba-8c33-a5f555187214 | -19.93522 | -40.79655 | 2026-06-23 03:49:00 | NPP-375D | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e034805-5fae-3919-8464-f8d7c0d8d9d9 | -10.56178 | -46.22477 | 2026-06-23 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f098ef4e-57b0-3d5a-9639-966321570f0d | -11.57482 | -47.44066 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8231b589-cfd2-3f4a-8078-790736d42678 | -11.89017 | -43.83786 | 2026-06-23 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10c805fd-d2e1-3b40-ae02-599f67e7acaa | -11.29225 | -43.3409 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 17690aa0-c67f-3312-a658-d7e126a3bf89 | -20.34841 | -46.6195 | 2026-06-23 03:49:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a6e442a-e0ca-3344-aac4-34e8564980e1 | -10.56517 | -46.23396 | 2026-06-23 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ceb342b-e24a-3486-8bba-2e03864eb859 | -17.61326 | -46.70402 | 2026-06-23 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c4f5dc2-e50f-36d9-ac1a-3377fb2b9f04 | -11.29335 | -43.33496 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3532ad65-0d33-39ec-b286-c16c423f9215 | -11.91156 | -43.40733 | 2026-06-23 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7513b6b-99cb-3bbe-a182-4aa6c10cedbe | -11.57402 | -47.44088 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3321a6cf-5908-3eb1-acaf-d46b3b64db8c | -22.69966 | -43.36333 | 2026-06-23 03:49:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 86c68ecb-09e8-3083-ba8c-112099b517ec | -11.58123 | -47.44223 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd051216-aca4-3e8e-9b33-5a68df404cf4 | -21.8424 | -47.24528 | 2026-06-23 03:49:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 816b69cd-456d-3b73-8bda-37c6126ed3f8 | -11.28223 | -43.33876 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 748162de-5224-3870-8885-a99964c7d3eb | -17.93157 | -47.02021 | 2026-06-23 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8eacac2-0c44-3e7b-85a2-8aac953b676c | -11.58043 | -47.44246 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d9539a3-d7b9-3816-a220-284766c09cd1 | -19.94323 | -40.77362 | 2026-06-23 03:49:00 | NPP-375D | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2ab8858f-d9f4-3fee-b0ab-09b7161e037f | -20.49082 | -46.3847 | 2026-06-23 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 10dfb939-fe48-36c7-9ffc-a2312205b25b | -17.93479 | -47.02316 | 2026-06-23 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129933d5-f25d-3002-b8f1-8a595f874a93 | -10.114 | -47.55141 | 2026-06-23 03:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7eb1997e-59ee-3690-bea9-1ae7c382fdbe | -19.94238 | -40.77828 | 2026-06-23 03:49:00 | NPP-375D | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c8345322-0e38-3e28-a898-9ee5db9ea812 | -17.83719 | -42.61604 | 2026-06-23 03:49:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ec938ca-761b-358a-b0a6-3e49819dc6ca | -11.47948 | -46.6841 | 2026-06-23 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c552dc8-1981-3f51-8270-7f2f4aa9eeeb | -11.29835 | -43.33603 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f4f80e26-db20-3b71-971d-2e601ed194fa | -17.13764 | -46.82182 | 2026-06-23 03:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd9c24d7-1844-330f-a3f2-b02cce893ccb | -11.28112 | -43.34473 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6a907b78-652b-3bf5-9065-5bf5fd7557c7 | -11.28724 | -43.33984 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c074e56f-36ca-327b-8eb6-c86abc7ebbc9 | -20.32788 | -46.63834 | 2026-06-23 03:49:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2a35a61-e4ce-393a-ac29-2ea526ae4ea0 | -19.46193 | -39.841 | 2026-06-23 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85d6ef4d-f405-3505-b5b9-1a1ed6bfbf54 | -11.90658 | -43.40632 | 2026-06-23 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45b36292-6227-31f9-bcb4-58298d88f8cc | -20.4855 | -46.38437 | 2026-06-23 03:49:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb56179e-eee3-36c1-ade4-41a2564e3991 | -20.31859 | -42.01048 | 2026-06-23 03:49:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 465c79db-6e19-320e-ac9c-cb57cea02742 | -17.83869 | -42.61785 | 2026-06-23 03:49:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5d9230a6-0adb-3338-8b42-77673bbf6b94 | -11.29699 | -43.33425 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f03076ea-490b-3cbb-af95-ffc44f2580f4 | -11.27417 | -44.52753 | 2026-06-23 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e126fa4f-39d3-3665-a55e-c6b3e4afda06 | -11.47838 | -46.68961 | 2026-06-23 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6b01be0a-933a-3e86-b866-33ccf894f7e7 | -17.92913 | -47.02211 | 2026-06-23 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d28bc831-1368-3684-af86-eac85027ef26 | -10.56001 | -46.22789 | 2026-06-23 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a095e73-a86d-39a5-98c2-101679dc03f2 | -11.2978 | -43.33899 | 2026-06-23 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 37ac5a15-d12b-3876-bbdd-f34311ebc9e3 | -10.56095 | -46.22319 | 2026-06-23 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05be3546-d359-3742-ab84-7875e635f2f9 | -11.26875 | -44.52638 | 2026-06-23 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67dc0984-fc76-3d0b-bde3-6ff604fc736c | -17.93067 | -47.02432 | 2026-06-23 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bff3c02-a966-378a-bf51-5983db7f13bc | -11.57514 | -47.4355 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad046522-8093-3d23-8e07-d52bb1a898af | -17.13679 | -46.8258 | 2026-06-23 03:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b544e970-c9e2-3745-afca-612cfd07f3f7 | -11.58156 | -47.43703 | 2026-06-23 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97c4669b-9788-36da-8d05-136c7a284eb9 | -10.56087 | -46.22949 | 2026-06-23 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7211cbf7-c1d0-357f-82ad-084303526ffd | -10.11283 | -47.55724 | 2026-06-23 03:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae555d9d-be52-398c-ac7d-57836ee4bd0d | -12.8548 | -44.3625 | 2026-06-23 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 5aeed833-ce45-3cac-99af-73173eb7d7f2 | -12.8746 | -44.3357 | 2026-06-23 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d8bca19e-f226-32dc-a994-192bcb57822c | -12.8552 | -44.3389 | 2026-06-23 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 12580b37-0afd-38e9-9b96-6c222f89f273 | -12.8741 | -44.3593 | 2026-06-23 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| e87e2f6a-e747-3e6b-9412-276de9e9ecea | -12.8548 | -44.3625 | 2026-06-23 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 39d84079-610d-30e7-8400-ab8e670967ab | -12.8741 | -44.3593 | 2026-06-23 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 81a9c1d5-b5f2-324b-b0f9-91ebcbb515d1 | -12.8746 | -44.3357 | 2026-06-23 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6d84869e-af3a-3398-a86c-c6fc4a75e7cd | -12.8552 | -44.3389 | 2026-06-23 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| dfbb63b3-ef03-3f3d-8ed5-06f5eaafd3f3 | -5.82542 | -45.05128 | 2026-06-23 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e3e8c9c-b0a8-37af-8329-8e595936f23a | -6.99464 | -42.89462 | 2026-06-23 04:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c0e2e9a2-cc4f-35eb-a8f0-a71dd11f4db6 | -5.91656 | -45.5489 | 2026-06-23 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d95f269d-f2ed-3bbc-95c4-696eea12caaf | -2.48357 | -47.08603 | 2026-06-23 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
