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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8219fd7-ccb4-3688-a7a2-7b8cb9bc503b | -8.14811 | -54.81372 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13e9b66e-5f93-3763-9747-c2944ce12392 | -7.44111 | -49.47198 | 2026-09-16 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8aa85f8-df28-32e3-a291-0d6c5abb40e9 | -6.65955 | -50.91402 | 2026-09-16 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e759e97-d281-3281-b60c-b0f4c8cb0bd9 | -6.32286 | -57.74541 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0796b01a-ab19-37cb-8a4a-9c81427f86e2 | -8.7979 | -46.89878 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fa4fc21-0ab5-3e49-aa22-08833277dede | -2.91759 | -50.41015 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11edcb62-755a-319d-b75d-841e0d9a7f15 | -6.11362 | -46.10629 | 2026-09-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d575196-9b86-3d84-9915-018bb15e833a | -7.338 | -44.49377 | 2026-09-16 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9576100-35cb-334c-bed1-4e16fc0a2254 | -8.78923 | -49.40162 | 2026-09-16 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5573e2d0-7b5c-345b-af82-a13fca55ea08 | -6.02028 | -51.79487 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eca81bca-5852-3c5c-916e-f6f12ccd36de | -4.36621 | -47.78047 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6dac2bb3-b710-39f1-807f-60613c45d1bd | -8.84817 | -44.89678 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17bb59bc-e675-3cab-9fc6-d9fc65bbeca4 | -5.12464 | -47.60781 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9b31726c-019f-3908-b5d2-865d7245ece7 | -4.39066 | -55.04158 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 843ca859-cc67-3fcd-8d12-ee2d7db764d1 | -4.51586 | -54.96004 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 113b182b-98d4-3ff7-b070-b0c553c2c21c | -8.85235 | -44.90849 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6ad952a-e151-338f-833d-3f4f6f2307e3 | -8.33274 | -51.30918 | 2026-09-16 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b1db965-1f7f-3084-8ff4-180598429cae | -3.59536 | -59.06699 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63020931-19f0-383c-8b02-9ce60144b1d6 | -5.83715 | -52.05086 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fbf7b7d-40e0-3cb2-a3d6-79d740492e39 | -5.99294 | -46.63182 | 2026-09-16 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 058d7839-3ba7-3b89-acb4-a4cda9715b81 | -4.46693 | -55.05346 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a23adfb0-9d7f-326e-9a8c-474f7c1a700b | -2.90253 | -50.41208 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8bd723d-19fb-38d6-9ade-0cd2964482e5 | -3.48849 | -50.37371 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df9c8af9-f586-3c72-95fb-10c25e7d02b1 | -3.16002 | -58.63644 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8ac4705-2ec3-362b-a751-9d8b4407039a | -4.57183 | -54.90781 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 081f4bf2-1c72-3706-a7b1-dceb747ea142 | -9.09941 | -45.72668 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc5dd371-3297-3ebe-ad20-107707993d56 | -1.61485 | -55.56811 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7ef13a3-a357-3a60-986c-1414777c926b | -9.23234 | -46.70092 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42267e54-ce21-3a16-83b5-8e280beae98d | -3.48043 | -54.68641 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 218da7e0-04ed-3573-ac29-84abbdc17e0f | -5.1381 | -47.60255 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1b400f2-a3ec-3dfb-85da-b6a0d48e146a | -5.63803 | -51.6951 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 926b51c0-e010-3c0d-8dbc-7416fe0bc679 | -4.53408 | -55.62162 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cedcbe54-cc3a-32b8-92b1-2b21bf352506 | -4.72864 | -46.1297 | 2026-09-16 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c11f2fb2-75df-34b6-b6c5-311028a2d2eb | -6.15978 | -55.71083 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5fcc6a8-3426-3605-bebf-5f4612390e8d | -7.51009 | -50.1539 | 2026-09-16 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32f289bd-6d03-3cb5-8541-9841364897ea | -4.09517 | -51.12051 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e28813c4-f7c4-3b0d-9cc7-fc93035dfe07 | -3.11942 | -57.68277 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfa40389-e198-3e4c-9d11-3222ffd94271 | -5.85326 | -52.06094 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e9db3eb-c859-358f-bbcd-e3ba4e3b20c7 | -5.1005 | -47.61769 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b045902c-efd9-3151-a81f-8fad4ccafb26 | -9.10919 | -45.73536 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f6f808b9-56af-388b-9355-ac3660bb3748 | -3.37429 | -61.30882 | 2026-09-16 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67f65ef7-bccf-37e7-bb05-b3860d45edd3 | -6.00176 | -47.38834 | 2026-09-16 04:57:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 17fea2d2-dce2-3611-87c8-8a2edef2c3f0 | -2.91524 | -50.40128 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeb48381-d0e1-3c64-86e0-e63c632f1bda | -5.85614 | -52.0652 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc5532e2-5f69-3c88-a33f-08138818d6f7 | -4.36442 | -47.78215 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e63e9675-3173-3a63-b899-f6392af497f3 | -5.60683 | -44.84634 | 2026-09-16 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e7c7fb6-b716-3151-8ace-57e4a0dd9015 | -4.5242 | -54.97213 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4c6ee90-20b3-3401-afde-ab07277c1fed | -3.39636 | -50.76205 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09f9df22-11e6-3180-ae97-ec98573e16bc | -6.8077 | -59.17029 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fac9e9e2-f8d3-3024-953a-073173409c98 | -5.64133 | -60.21629 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 188a3c20-5916-36bd-b03c-eb6f8f875e73 | -3.37144 | -57.7086 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b217e8f-7762-353d-87d1-c2df981f84b4 | -6.32816 | -60.00155 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e137ae2-c8ed-3d1f-acb6-23934205196d | -3.47432 | -54.68186 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dc28475-7056-3b01-a7cf-aff6fa31f20e | -3.43438 | -57.975 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 584bb5f8-07a9-3f7e-b7c8-e7367ab73ef1 | -2.89704 | -50.42399 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 934d7d6a-8765-397d-8395-3b970c849bc3 | -2.05316 | -52.08356 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f4ff8bb-7b99-3c7a-a4a9-7b6511d93488 | -3.30011 | -59.46017 | 2026-09-16 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9452b5e-3abb-3cd8-bc68-3a844ebfa596 | -5.13382 | -55.93672 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1415213b-71c5-3594-a5f0-742b0132b58a | -5.99778 | -46.63238 | 2026-09-16 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63302b3f-c0af-377b-88a2-0be67aecf5ef | -4.40517 | -55.07988 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94495a23-6c08-336d-926b-096e4f6aeecc | -3.48376 | -54.68693 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7b7e8a3-e01c-3174-95bb-fa4b3021e490 | -5.63454 | -51.67063 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7ee33cf-6b25-3b3f-826d-ae300a09e101 | -4.53693 | -54.93457 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72688fd7-4636-344d-966f-c90b10c034c0 | -8.85535 | -44.91064 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2f5f3f5-e10a-3c3b-b3d6-1112f5a76c40 | -3.21547 | -48.78584 | 2026-09-16 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 994ac2fd-4295-3c7b-9e7c-c99f46315579 | -1.81275 | -55.76274 | 2026-09-16 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72219621-6767-30b9-ae46-a7142f7cbbcf | -6.16257 | -55.71495 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ddef2fd-6307-3af0-bdaa-979dfcff8c2b | -6.39373 | -44.05711 | 2026-09-16 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 110e5ed9-a0af-3690-9364-91d743b20f80 | -6.01651 | -52.16178 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09892d75-3b6a-3954-a484-152ad365167f | -7.64529 | -45.83792 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 330b2ea6-7860-304d-9b67-78374f93b692 | -4.44574 | -55.01754 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbc0ff44-8e44-3f7c-8214-57dd5806c21b | -8.85385 | -44.89731 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17c6959c-b99a-36de-aac3-556353a541e5 | -3.08031 | -50.57559 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb96aa92-0547-3dd5-9f8f-287cbaee5b72 | -6.95785 | -44.55457 | 2026-09-16 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 010734c1-cd8f-392f-912e-7a1b90114baf | -9.48544 | -45.43373 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f95672e0-d2db-33df-b137-970c11d6c930 | -3.01697 | -51.20724 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72da5973-6049-3323-bb12-fdb912575c82 | -7.08842 | -47.49186 | 2026-09-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0ca1edeb-6bb2-37e8-97b9-0f859a636487 | -3.58847 | -58.54742 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 024ef87a-6dff-35bc-a8b8-842e309f7890 | -4.23188 | -56.38189 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cf6739c-9a47-393e-a8f5-1f05f3a3efd2 | -2.89939 | -50.43283 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d44a9321-6e42-3118-b7bb-9805fe728eb8 | -4.1853 | -49.40615 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65887618-782c-3e6c-a778-de39cbd45b4d | -2.10186 | -52.05067 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5945e831-a57d-3290-bcab-acbdac716f37 | -3.31676 | -47.14119 | 2026-09-16 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae0aa01b-7c8c-3d58-8992-812c6431da25 | -5.85671 | -52.06147 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f160cfb-6e1e-3d06-b2af-50119e6b19de | -3.11564 | -57.68217 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 756f121e-d662-3737-8b27-3b40ff87d5a3 | -2.48818 | -49.40682 | 2026-09-16 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cba6c99-7bb6-3465-8a1f-7c8eeb492af7 | -8.79971 | -46.90904 | 2026-09-16 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06153637-dd47-3961-9993-199ef8ffcd17 | -6.09493 | -57.69378 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed4c5af0-757e-30b0-8952-3731a5b4e2a2 | -6.28398 | -56.03794 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a394aee2-c027-3b27-beec-e09cfba391be | -6.33797 | -62.69628 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12814faa-bba0-30d4-a95b-0ae71bf9763e | -8.7884 | -45.89736 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82d40592-5ece-3c39-a8fb-1fce4c1b9c69 | -3.7645 | -47.55314 | 2026-09-16 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 347593a3-54fc-3265-a3a3-e957c88c00bc | -6.34956 | -62.68924 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1b6af85e-c57a-3546-941e-171f92d38956 | -2.89641 | -50.42813 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7fea0f6-d193-3feb-a557-068cc70dfb1b | -5.15544 | -55.93249 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 914b9c7c-fe62-36c7-91ad-6d28f6743bc7 | -2.63055 | -51.75845 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e15edd7-e245-3c4a-9d42-dff9bb0dff33 | -7.07643 | -45.23883 | 2026-09-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 307d4d3c-c8a3-32ae-a563-066940c26c72 | -2.88359 | -50.46427 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29ec8903-3930-37f3-acb6-6d97fe696f00 | -6.10892 | -46.10208 | 2026-09-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5325cfd-66ac-3f47-a011-429110ef2d0c | -3.67554 | -55.52177 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
