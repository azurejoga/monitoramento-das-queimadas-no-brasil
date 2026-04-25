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
| 818bc109-88f3-3614-a572-68f2b8606eb1 | -18.5082 | -55.491699 | 2026-04-25 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| acb9bcfc-1759-30f5-ad0d-663623b5dfbd | 2.7412 | -61.3512 | 2026-04-25 00:52:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| df530a89-d367-36dc-8a5a-f66d6319e4c8 | -23.079901 | -48.608398 | 2026-04-25 00:52:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1b0a956a-75da-3208-b0d8-cc4f4ad2127e | -16.4221 | -54.9104 | 2026-04-25 00:52:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e2ee052-b419-364d-8d48-26c9f1f68ac6 | -11.9475 | -58.067001 | 2026-04-25 00:52:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f9e945e-c398-3a0f-8e38-07173269cb18 | -11.9491 | -58.074001 | 2026-04-25 00:52:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdc4e097-7693-3fc8-bcd7-a3687a7f06d7 | 2.7428 | -61.344299 | 2026-04-25 00:52:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0db89294-d9fc-347f-9273-fa4fab27edcb | -14.2025 | -57.421501 | 2026-04-25 00:52:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1e8507-86af-3d57-9465-0b9ee66b3cba | -18.51 | -55.499298 | 2026-04-25 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6a5a2849-ee5f-397f-9b8e-26ae0a6a67c4 | -23.076 | -48.5938 | 2026-04-25 00:52:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5f6328da-506a-3463-9439-0d6cd9a2dc24 | -13.72 | -57.475101 | 2026-04-25 00:52:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58e92a16-7b6b-36e8-b5ff-582dd7692bce | -13.9929 | -56.634399 | 2026-04-25 00:52:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c57a635e-b430-3c71-8206-9d1451d31d27 | -13.9946 | -56.6418 | 2026-04-25 00:52:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 117c2421-28ff-3cab-9ca3-0cca2c3d1c0d | -18.506201 | -55.498299 | 2026-04-25 01:24:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2a1cdd1f-162f-3e47-9e7b-6955166602e5 | -18.5159 | -55.495899 | 2026-04-25 01:24:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d97bac59-5128-3ff4-9d6d-2fed6b92cd2f | -18.5079 | -55.505798 | 2026-04-25 01:24:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1787aea0-33b6-3dbf-9a11-a6c7988ac2d6 | -9.08934 | -40.51415 | 2026-04-25 03:17:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| edf27d77-cee0-37d9-afe1-31aaf335591e | -9.0902 | -40.50967 | 2026-04-25 03:17:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97dab0d5-59e0-33ad-9468-b5829e0465be | -11.77676 | -43.66126 | 2026-04-25 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e40234b5-5a63-33c7-b9f3-8cd4b5fe7771 | -11.77765 | -43.66095 | 2026-04-25 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa5f0be6-c581-3371-b383-db9f49b38601 | -15.86492 | -43.59886 | 2026-04-25 03:19:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c519336c-cf98-36ec-b1d7-f9e86e7bed6e | -15.86372 | -43.60437 | 2026-04-25 03:19:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7067904d-4bec-3506-a4ca-936c27e06fd3 | -11.77205 | -43.65317 | 2026-04-25 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0282e85b-4a3d-3e47-9272-f05580b0e1c8 | -13.68493 | -44.29704 | 2026-04-25 03:19:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 570fe549-3da5-3424-8bc3-7bde34cad6fd | -10.55919 | -42.44383 | 2026-04-25 03:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 90464b6a-ac98-3dc6-88e3-5f9b27aef2ea | -11.77119 | -43.65353 | 2026-04-25 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47022bef-2bdd-34e6-bfd0-d2906fb1c814 | -10.55805 | -42.44947 | 2026-04-25 03:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9acce7fc-dae5-3bde-b666-4c7be8787a74 | -11.78373 | -43.66238 | 2026-04-25 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ec3ec32-c75a-3168-bc60-4da7b0aebccd | -20.19876 | -46.87561 | 2026-04-25 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 616e31b6-fa36-3728-9ce9-3987a3b9b954 | -20.19527 | -46.87475 | 2026-04-25 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5aa7ec55-7ee4-3b2d-afe6-586114259326 | -20.19024 | -46.87959 | 2026-04-25 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37502f40-e422-39ff-b80e-eec52e594622 | -20.25573 | -46.76852 | 2026-04-25 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cc0c599-37ff-3bb9-bce6-18f707220bb0 | -21.85829 | -46.97967 | 2026-04-25 03:21:00 | NOAA-21 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a7ad7d5d-6c87-39ee-86e6-ff68988a1a6f | -20.18666 | -46.87926 | 2026-04-25 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06a7a5dc-186b-3da6-83db-e15f30a37ab1 | -18.89389 | -39.92674 | 2026-04-25 03:21:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e4aa77a9-f39e-33d6-a2bc-a57e00ca723b | -20.24885 | -46.76623 | 2026-04-25 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2d27c58-a033-393f-bea6-878cb315ef87 | -20.25156 | -46.76757 | 2026-04-25 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| acc91ecb-87b8-36f0-af09-f0e8fcf5f7a6 | -9.0926 | -40.51141 | 2026-04-25 03:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8848f557-3525-3750-91fb-c9537d2172ce | -8.90978 | -37.88052 | 2026-04-25 03:49:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2096c919-055f-3402-a502-fcf0ccb0016d | -13.4154 | -44.32056 | 2026-04-25 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdf043e8-f32e-39ac-baf5-0ab5cdc8d9ed | -11.76344 | -43.63579 | 2026-04-25 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1efb0d40-7ea8-3b05-ae7c-3330bca0e307 | -11.76255 | -43.64056 | 2026-04-25 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 974d73c1-4a3e-3832-bfe7-08884766a531 | -11.78209 | -43.66385 | 2026-04-25 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5358b960-f3e3-30dd-81e6-8920a90b0e69 | -11.75246 | -43.64364 | 2026-04-25 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efc2f3de-6c17-37ad-b17a-1a58c4b34834 | -11.77001 | -43.65182 | 2026-04-25 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0949976-108c-352a-a7b2-c26322a04ca8 | -15.86086 | -43.59863 | 2026-04-25 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 294c8ec0-cfc5-3005-8a08-d9c1cd439aa2 | -10.7714 | -40.84496 | 2026-04-25 03:51:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 35be8fa2-928f-3b76-b658-4e45421f6a45 | -10.5598 | -42.44714 | 2026-04-25 03:51:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e82a75c9-56d5-3a37-8e20-59bc75b8af33 | -15.86513 | -43.59949 | 2026-04-25 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d406afc3-9e45-3ed6-b56d-43f7ae51f621 | -11.75706 | -43.6445 | 2026-04-25 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| becfe2b9-500c-3a0c-adec-bedc2a6ca8c9 | -11.77747 | -43.66306 | 2026-04-25 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4859e28-a31d-3e13-9626-e65ee594f26b | -20.19761 | -46.79956 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d06b96f7-c3d9-3891-9f9a-52467ef1ef29 | -20.17588 | -46.93088 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06bf02f0-5be0-32d0-a505-42e722be0062 | -20.62961 | -41.68035 | 2026-04-25 03:53:00 | NPP-375D | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b75b4ca5-9037-3366-93a9-defd2baea2d7 | -20.81415 | -45.18218 | 2026-04-25 03:53:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 246adf3d-9b08-39ed-9d68-c12250254806 | -20.18645 | -46.87909 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcaed032-6537-3a54-a8a2-499c27e5d383 | -20.17944 | -46.89679 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68acc603-4184-389a-8396-0232527c7e7d | -20.16814 | -46.86933 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef4f5ecf-091a-3dd6-98ce-2f2f5bd2eb33 | -20.18172 | -46.95226 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7981f03c-04a4-3f1a-a793-31e9f990c5e4 | -20.24754 | -46.76548 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce78eca5-2690-3a3b-8a6c-2c6b5b353886 | -20.19876 | -46.79395 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9de72da1-12e7-3fda-9387-c6c068a2804d | -20.52459 | -48.75234 | 2026-04-25 03:53:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 64405608-b534-3aba-9318-2ff798cc45c5 | -20.25233 | -46.7667 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5b200b0-9131-3ef8-a66c-7c2f81c79a64 | -20.16925 | -46.86391 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52746b0b-8185-3bfa-8740-fb61e5196c87 | -20.16763 | -46.9284 | 2026-04-25 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d65d6d3-60bf-37a4-a376-81ecc02e41c8 | -20.52378 | -48.75605 | 2026-04-25 03:53:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7b20be89-f46b-3b25-a226-209137c9806a | -20.17713 | -46.93175 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a07d1a14-1d31-33c5-8bc3-89eb28a21c62 | -20.46354 | -45.57364 | 2026-04-25 03:53:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1756b5ce-f729-34c0-a1cb-357a4762002b | -20.19129 | -46.88027 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0146b89-0039-3ebe-860e-58924d21e32d | -20.17037 | -46.85847 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ed53d2a-2555-3d76-84c3-6c290502a1c6 | -17.22303 | -44.30481 | 2026-04-25 03:53:00 | NPP-375D | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46a6bf57-4844-3e6c-9da8-d6b846090de2 | -20.17113 | -46.92916 | 2026-04-25 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23054f50-5312-3cfa-840b-0827be743df7 | -20.17356 | -46.92449 | 2026-04-25 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f3b2d3d-1f93-3858-9183-9af2f2440adf | -20.1828 | -46.95319 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b516f7b8-4301-32ef-bb7e-6d52ebaf1107 | -20.18928 | -46.87432 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 943fa315-1739-36c0-87b9-280bc69c4cda | -20.19296 | -46.88096 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d09dcee-6a53-3187-8088-2fd35e1bdb78 | -20.19606 | -46.79432 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d03fdc49-dbcb-3cd9-9b77-53962ef8cf2f | -20.18062 | -46.93261 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d71f5287-5ed0-3775-9864-3e484abdffc3 | -22.33591 | -41.77315 | 2026-04-25 03:53:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7f043866-7bdf-3c02-af49-f38908e6eb97 | -20.15636 | -46.85257 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3f791a4-0000-3659-a27e-5285d81c9211 | -20.25138 | -46.77124 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ce3eebf-4ad7-37a9-99b5-f2674067570e | -18.89505 | -39.92752 | 2026-04-25 03:53:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bc694357-5003-3b56-8f7d-66af99e9a0a8 | -20.1999 | -46.80011 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c9636f2-36d3-3df4-950c-f46ee8d9ce4f | -17.21868 | -44.30389 | 2026-04-25 03:53:00 | NPP-375D | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32ed13fb-e230-39d0-9ac0-a62b16222646 | -20.16637 | -46.92752 | 2026-04-25 03:53:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dd30144-474f-36cc-b4de-31288be85c1a | -20.18763 | -46.8733 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87e30103-4e32-32ff-88d7-c7ab9f5238c1 | -20.18806 | -46.88006 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e76f13c-50bb-376b-bf62-1e52b132a7b3 | -18.8957 | -39.92368 | 2026-04-25 03:53:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58b9325b-d8b7-3e12-a347-9d2a08431a61 | -20.51839 | -48.75468 | 2026-04-25 03:53:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 34004f8b-5ef3-3d2d-af16-7210f76c1e8b | -20.17702 | -46.92528 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd413ceb-c923-3080-b56c-05fbc7181c37 | -17.22309 | -44.30248 | 2026-04-25 03:53:00 | NPP-375D | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fffbb907-543b-359a-b52f-a4de90613fff | -20.19408 | -46.87564 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 155e51a9-396b-3b03-b5b4-5252da068e53 | -20.2486 | -46.76043 | 2026-04-25 03:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65112dcd-b7cd-3084-8a5a-e04e03a08e69 | -20.18336 | -46.87829 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a020cf22-259f-37e9-b36b-d2f8ffdf61bc | -20.1924 | -46.87483 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0302d09e-68bd-3bba-abe2-421620d3e25e | -20.1972 | -46.87618 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 281ef7e6-948a-3d6d-8184-203ea142d552 | -20.17832 | -46.92614 | 2026-04-25 03:53:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ed19f46-8e41-32d1-a2db-d085f11cf2b3 | -21.86029 | -46.97722 | 2026-04-25 03:53:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c83e871a-583e-3469-b0c8-55ed8e10cf77 | -20.67847 | -48.96304 | 2026-04-25 03:53:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 554953d7-7f7c-38e9-b09d-32ee89458d37 | -23.07828 | -48.61626 | 2026-04-25 03:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
