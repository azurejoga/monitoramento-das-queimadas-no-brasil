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
| 8e645ef5-4fa7-3239-965e-d84d692a6ca2 | -10.08885 | -46.91469 | 2025-10-06 03:36:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3f87aa7-98e7-3ea1-bcd5-b94ff50dbb9b | -12.48772 | -45.55311 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f60a4875-30d2-36a5-858c-71619fc23bae | -8.62958 | -46.32006 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e9e31e46-1c1e-3980-8653-377311c181f6 | -13.86084 | -43.99303 | 2025-10-06 03:36:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f18b265-c4c4-335f-9547-9db169c01b5b | -8.61449 | -46.29394 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 91b92bd3-61e7-34d8-aad9-49bbadee9554 | -13.05074 | -47.9051 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89801bbc-2422-37f2-83c9-d4b378ec751e | -8.88268 | -47.62385 | 2025-10-06 03:36:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4526f3c8-54d6-30ed-ab7d-558f846a162c | -8.51189 | -46.3754 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 819825dc-080a-3e30-9a00-567533e062ed | -11.79987 | -45.11951 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7481095-a29b-3030-95b2-e1027a697b7e | -13.35465 | -47.19778 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32ce47b9-644c-33b9-b65b-04d41ddbad3e | -9.31075 | -45.9913 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 64e0ac7b-04a1-386c-9e37-ea01e5afedb0 | -13.07455 | -47.8802 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30454006-9c65-31a7-b9af-a8afbbde952b | -12.48775 | -45.55265 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 072042d6-a1fb-3a24-bd9d-7aba43f1eee9 | -10.27759 | -44.35963 | 2025-10-06 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18408f41-a03c-3b8b-9549-9f39ddbff8e1 | -10.38533 | -45.41714 | 2025-10-06 03:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78dd7675-875b-3d4e-845f-91467986a39b | -7.78721 | -44.12115 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a095949-f398-3ac5-b73b-a10ff9413119 | -11.1607 | -47.93575 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 832e8d2b-979b-3103-8837-48ae15a6a079 | -10.34124 | -46.9641 | 2025-10-06 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b91e607-a7ee-3544-9ade-43f4b5ed11c1 | -13.08467 | -47.87422 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a9edd57-bf4c-35d9-893b-42a2bd7cfe75 | -12.90633 | -47.30351 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cf24a0dc-7c6d-3467-96e4-b3bb156134a2 | -8.86532 | -46.801 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d17ccd1-8e6c-312b-b3c9-78e4fe857d7b | -8.61997 | -46.30029 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97db87f9-c392-395f-9505-a70fd7b13996 | -11.79734 | -45.12508 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3336c5ff-2761-31ae-8128-3239e56303c9 | -8.51509 | -46.35868 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47eea19e-4013-351b-ae68-de0498e8aef3 | -8.61255 | -46.26932 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0bf45a54-a619-32e3-9f72-17a3daca6cfe | -11.48352 | -45.04169 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdd103ec-f5d5-32e0-82ca-c4fa39f7891e | -11.04769 | -47.76354 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1556d51-230d-34c5-bead-c49fe20d07f4 | -8.52043 | -46.33078 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60160f72-6248-3c29-8382-46b322fb8a99 | -13.06509 | -47.90217 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55058b7d-5b01-302f-9358-9a56cf15542d | -12.90764 | -46.81807 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c59de190-6f29-3199-a140-35f09fbe697d | -8.514 | -46.36438 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43295932-c960-3780-9bcf-7d17fcbd9c98 | -8.51841 | -46.34132 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2175c071-eae1-372d-b68d-484227c691fa | -13.08682 | -47.82318 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cfbec01-d245-3800-a484-7e94be48a6c9 | -13.34717 | -47.18888 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 325bf63f-01e2-3376-87ec-a04192924bf6 | -7.99428 | -45.4831 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d44ac89d-2b0b-34e8-b574-4e49f32069d6 | -11.71464 | -44.31242 | 2025-10-06 03:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd396d7a-bdf0-3cc5-9b9b-f866ff4931ff | -11.84617 | -44.93265 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d965f8e-b2e3-3253-8d7d-bc34da7323d1 | -8.53455 | -47.22039 | 2025-10-06 03:36:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c93e3d40-7e3b-32b5-9078-04518d080ee8 | -13.35233 | -47.1957 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 608069c7-b2ef-3ef7-b092-d4c443025726 | -8.66359 | -41.67835 | 2025-10-06 03:36:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 480f6b33-7be9-30e1-953f-926b0eb202d7 | -13.08143 | -47.88013 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83d4b418-9b09-36dd-baa3-2f8cf740554e | -13.25858 | -47.81057 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b5d8f67-4cb2-3b23-97cd-98df81bdc3bc | -11.70677 | -45.4054 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7379c95e-a2d1-3538-9401-d86451dab55a | -11.79646 | -45.12965 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 708855fa-2cd9-30cb-bc28-ecdad4118a69 | -11.05335 | -47.72775 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 010abf49-0abd-3a35-903c-f95a6a194061 | -10.09427 | -46.92154 | 2025-10-06 03:36:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cef4c50-057b-3bd7-941d-ab2beeacfc2b | -8.51519 | -46.39335 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d893f14-2373-3861-88e8-524a538bb2d9 | -13.33645 | -47.5688 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8edef70-0b52-3a77-966c-1f56c11942e3 | -12.57483 | -46.73664 | 2025-10-06 03:36:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cee03c7-346d-3b51-8524-5a560bdc9b2d | -8.6114 | -46.27527 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a2c3cf51-c45f-3525-8334-011bb735179d | -9.30978 | -45.99627 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a04ac421-4154-3876-8d8e-845b60fb4305 | -8.61553 | -46.32336 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9f59550-f006-3414-ae8c-c36ba9bf77f2 | -12.44085 | -45.51665 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 099a60f0-9df1-3489-a1b3-5a7d97f315ef | -13.32977 | -47.56869 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4521392f-6ad1-348f-8cf5-73f901a32e35 | -8.62201 | -46.32456 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 13110d3a-1c8b-3dcd-a3a4-68841996b09f | -8.61888 | -46.30594 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f17d9f8-051d-34d7-8f53-6ab2587c0623 | -12.45316 | -45.54543 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ab5ae2c-ce32-3d79-acb1-281d58b797ec | -8.51624 | -46.38787 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9042b1ae-06d2-36f4-b782-e3ea274d93d8 | -8.87071 | -46.8443 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8ed07f6-171b-32b7-82b0-405f04154511 | -13.26399 | -47.84954 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4efb1a2b-5cd0-37ca-b3a9-93aa12d3a5c4 | -13.3555 | -47.25609 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c22ec9de-bd36-32b9-81f1-30ff284a0e22 | -12.89457 | -47.30174 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b6245368-bf52-38c8-85d8-4fde965c2bb8 | -12.24577 | -49.20927 | 2025-10-06 03:36:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ffe145a-11ec-3272-aeb9-ef3614e3ff03 | -13.27198 | -47.58789 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47fe3b41-9810-3d58-b00a-5b79251a6802 | -12.90222 | -47.29103 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e8a9c8eb-e20d-3d8f-9a00-483033c314ac | -7.71524 | -46.26424 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22440e27-2d37-3cd5-8624-6e0ea0f16cb9 | -8.61664 | -46.31759 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51761c0f-bf64-37c2-a3a9-4f094cb50c9d | -11.02283 | -46.54736 | 2025-10-06 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b8b4405b-b2a3-3773-9b71-046d8295297a | -7.79291 | -44.1224 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d4441ad4-7e34-3b66-a6c1-3079c569a7b6 | -11.67882 | -47.48255 | 2025-10-06 03:36:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aed8012e-fe29-30be-bda1-8cd209da7f8a | -11.80293 | -45.12675 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e0e3ce8-6121-3436-b7f4-22a4bd37bc77 | -8.66352 | -41.67514 | 2025-10-06 03:36:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1ca76082-5684-3c3a-931a-86319b8f4b49 | -11.80932 | -45.12432 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d8b1ac8-6f50-3310-ad6e-35e09893bb7a | -13.08136 | -47.89005 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78575789-39c0-36d1-a328-4399ba12a0ec | -10.39126 | -45.41836 | 2025-10-06 03:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd2c5521-2dbc-391f-8e1f-3486086ca14f | -12.90001 | -47.3019 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 42d1b050-b719-3374-911e-3c4490b94117 | -8.5194 | -46.33615 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01aca111-3ffe-34ce-8608-e1990ac025e3 | -13.3557 | -47.57291 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80bf1469-cee0-3792-951c-39eb6e291c05 | -7.99089 | -45.4907 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 145ed425-22f5-30ed-a02c-e3c53ed9c59d | -10.34892 | -46.9596 | 2025-10-06 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec5d8953-2acf-3a07-91c7-f2d222088529 | -8.56092 | -46.25902 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aebbbc39-117d-3307-a112-cc2cb6aeea49 | -12.90948 | -47.29408 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a8d160c3-2dc7-3018-91b6-425be23a1776 | -8.87457 | -46.84309 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5730536-46fb-3df2-9248-2dd51faf100e | -13.26517 | -47.8116 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 089cb7c0-4e9f-3455-8c00-15f7b8cae305 | -9.37169 | -45.91073 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd5b14f4-0b55-328a-a72c-b295fd341c81 | -12.4869 | -45.55686 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2f2f8cec-624d-32a8-834f-372adbd794b1 | -11.44686 | -44.957 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c7bfb2e-343e-37d5-adf6-8500df569a33 | -8.61344 | -46.2994 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55949599-329a-359f-94c7-46385c270778 | -9.96052 | -43.78119 | 2025-10-06 03:36:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 11baccb5-9a23-34b2-81f5-b2560a67eb8b | -13.08232 | -47.87601 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c7fcc79-9537-35a9-a34d-896cffbfbc90 | -8.63496 | -46.32695 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ea87940-b741-3d45-a31b-2d7d6b5713e0 | -11.15441 | -47.9364 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9796793b-05b9-386a-af0c-f8046f32cd2a | -13.26512 | -47.84418 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18f4fdb4-96b3-3a1b-9771-03266a09e29b | -10.27616 | -44.36715 | 2025-10-06 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8b46652-a875-376e-8bf9-1b97cf2b39cd | -12.9158 | -47.29566 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42009348-b24d-38ef-bc91-7c1051ef18a2 | -13.23133 | -47.81788 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9ba170c-5eb7-33b2-971a-25f51bb9ef29 | -11.80546 | -45.12115 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f895d30d-3643-37c9-a96a-cdec2bfc58bb | -8.6124 | -46.30481 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19f36cdf-20b3-320f-a7ef-bcead1ab6499 | -13.27065 | -47.85033 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88125eae-5297-3e6e-97be-d4cbb14abb52 | -11.84352 | -44.93091 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
