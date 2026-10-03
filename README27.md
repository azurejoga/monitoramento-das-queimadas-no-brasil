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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35ec3c0a-e95f-379a-9097-9280fbdf9ade | -5.94505 | -43.65989 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| b7603b8b-506d-3978-acc5-1487007a7c4f | -4.27167 | -50.7412 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5ef6e80c-cef2-3086-a137-91cde2e89143 | -5.25613 | -55.92172 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38474d31-243e-3930-a188-33f5a410cd9d | -11.71614 | -43.43032 | 2026-10-03 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c058369-9335-3b60-a017-fe12dfca1f82 | -5.22089 | -46.02515 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 806713e1-7593-3427-84f1-97669dad9e7e | -4.79293 | -55.72089 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2646a910-8edd-3f9b-8429-8c5d08b3e618 | -6.91306 | -59.28011 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d109e524-05a3-3f52-8bc0-606ec2934875 | -5.55833 | -43.96597 | 2026-10-03 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c3ecdc1-92e4-3c07-a01f-d473acaed1cc | -4.78849 | -55.72032 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e84227f-d66d-38f8-9767-5731cf593418 | -4.98677 | -45.64074 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba4fd5ba-ff2f-3891-92eb-9f00d766a8fd | -5.74204 | -45.14444 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d0a9d24e-42b2-36eb-8b96-453072ec2529 | -6.21932 | -53.26106 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71fb2939-8f1d-3c77-8e2b-bba97a1bed03 | -5.94313 | -43.64338 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2ed7ec9b-e900-3dc9-b0be-3a41cdafe81f | -4.30311 | -50.78311 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fbda2d7-a7d5-3e6a-a953-767849c6150a | -6.00707 | -53.5285 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8f0ab43-90d2-3a30-bfe3-1c18f5d802b5 | -3.5891 | -54.53507 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 092309c3-3da5-335a-9477-26aa0accf78f | -6.09925 | -47.66087 | 2026-10-03 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e7184ca-ab57-3693-8afa-dc693a407186 | -5.09571 | -56.25496 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e01eef9-e300-3667-8617-c80535ec33ac | -9.95761 | -55.33334 | 2026-10-03 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c39ace4-4763-39bc-a0b6-9911c74669a9 | -5.75576 | -45.29261 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20e9c238-3cdd-3f93-881c-ef0c8abdd5f4 | -3.85175 | -55.80344 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eaf38eb1-2032-36db-b5fb-a04bcb2e22d3 | -4.29073 | -50.77378 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc6900c4-62f2-3fe9-bab8-999792731777 | -6.31697 | -43.62481 | 2026-10-03 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da4a203c-6c9f-3d4e-95f6-b1639abfae0d | -4.81335 | -49.87686 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56530b0f-6a32-3bab-b976-738b68fd0d25 | -5.72449 | -48.94417 | 2026-10-03 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52734ea9-8fac-3065-b0e6-ea301c4b9e7b | -5.15363 | -46.04626 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ca64923-7464-3c5e-ab91-0070f70709d0 | -7.23284 | -46.01276 | 2026-10-03 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 614d3d6c-c6d2-3c0d-ac80-cdb117eb44a9 | -5.37368 | -56.05856 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 959edb9d-3d51-348d-9d7a-61040bedf5e6 | -5.8636 | -53.47604 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22f669d0-ff9c-34cc-9b32-5b0bd913ce26 | -3.58194 | -55.55339 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e05fc92a-728f-30e0-988e-b6ca7049f03a | -4.78554 | -55.71072 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cc27dc1-7b67-3958-a7c2-e0960622cb48 | -5.75958 | -45.2932 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52f36406-f545-3f0e-be04-7acd38c099e1 | -9.4597 | -40.36762 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.6 |
| a6a882cb-cde4-34bf-b28c-aa12622601c5 | -6.92338 | -44.56406 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40ce256f-30f7-36c4-8250-b819354a5297 | -6.50185 | -41.7451 | 2026-10-03 04:40:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dcd0c973-54d3-327b-a7ff-8dafc11446b2 | -7.47079 | -44.42357 | 2026-10-03 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4adcf3c-a135-3bc8-8cf9-1f1c87d9dbb3 | -5.75101 | -45.14912 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f889b960-fcf8-394d-afe7-cca46b56167d | -5.96288 | -43.6527 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d93b4e75-baaf-368f-868f-4dad6bba35f5 | -6.86437 | -59.33333 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeba68d7-15fa-3b36-83d2-46dee69185e1 | -4.12712 | -55.018 | 2026-10-03 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b37ec9ef-f28a-330d-bd1b-ddd126943daa | -5.73818 | -45.14388 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b6f26773-7393-3642-9e89-2b66c3466110 | -5.59997 | -44.90401 | 2026-10-03 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9bee8e5-9195-3f0c-acf2-33611b5c0617 | -5.73094 | -43.28338 | 2026-10-03 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 016cc409-d731-3ec6-9c20-2ebd52169a64 | -5.74905 | -45.15045 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a1c5f77a-5d67-3ba3-a59c-d71448529ab0 | -6.02389 | -43.59207 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3d30bca-37d4-36af-aa91-968206dfd5dd | -5.74331 | -45.14797 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4f5b6a99-16c6-3311-95bf-86e503db1739 | -5.87169 | -50.15843 | 2026-10-03 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d8a6640-3ae1-374b-93b2-65820a235793 | -5.43172 | -43.44608 | 2026-10-03 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3a4de0c-dad3-35f5-88d6-2e5e3cd5df19 | -6.01389 | -53.53405 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc14f6d7-123f-3c87-8638-604648eb6264 | -5.94989 | -43.65658 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 561f516b-a392-307d-80a2-55a481bcaa17 | -4.21308 | -53.56438 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7adb02e-f6ea-313f-b438-61c2e675f881 | -11.7185 | -43.42654 | 2026-10-03 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ca4067f7-d388-3ed8-b252-975bdc390f62 | -4.81058 | -49.8729 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18a35f43-a572-3dbd-b9ff-8e10a0840a54 | -4.53534 | -50.77892 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a87e057-4e98-34a7-8e1f-a5e2da21f9e4 | -5.88627 | -55.48695 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c583f7c-c904-3146-88c6-cce84a1452a3 | -6.31756 | -43.62069 | 2026-10-03 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c005994b-ef76-3a8d-8c80-8452ade78e86 | -10.36375 | -39.49516 | 2026-10-03 04:40:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ff3ba9a-2eaf-3348-8693-379ef28b1902 | -5.74569 | -45.15821 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b796e5a-2d8b-3cf7-964c-6c54765a683d | -6.83983 | -59.27406 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed793a12-dfc0-3fdd-b398-8f0bcb9591a6 | -6.84284 | -59.25668 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ed7874d-6c75-35c2-a6e5-fb761828268f | -6.20399 | -53.26875 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a715ac3-019e-3763-9593-49ea57bf54e2 | -6.2382 | -53.14764 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 005b8ae0-2ce3-3ca6-af43-2a85c54625c2 | -6.85642 | -59.25238 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7695fa6b-5c10-3c67-aef4-12b7402f432c | -4.26096 | -50.74326 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 438fee56-ad0c-3972-b484-8323421dc355 | -6.23831 | -53.14914 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e53c6ed1-1f11-32d1-b553-f9152a6008eb | -5.95106 | -43.64867 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 50b1487c-18ef-3f49-b13c-e4f6e09dd295 | -9.70161 | -57.45255 | 2026-10-03 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6730688d-1798-3463-ad32-a1d0b864a278 | -3.58555 | -54.53068 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f24aee4f-da7f-3394-82eb-b914252b7597 | -6.31963 | -43.34864 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1eb92d30-0ce9-3c02-a99f-5a59c3127159 | -4.79068 | -55.70709 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5d09c3b-ffb0-34fa-9179-32a568084dfa | -11.71484 | -43.49313 | 2026-10-03 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b0d40d9-122a-3cc2-8193-532939704df0 | -5.73888 | -45.13905 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e6c7c1e2-db5c-30f9-929f-93e3517bec7b | -6.18322 | -44.64507 | 2026-10-03 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96dd64b4-9731-30db-a1f0-db06b3de5950 | -5.7356 | -45.14683 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 510d6ced-2221-3b62-9245-cba5803b9da7 | -4.26887 | -50.73706 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fa14201-6785-3824-bbfa-aeb3bf757974 | -5.42519 | -44.78265 | 2026-10-03 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 754f9472-05cc-3d46-bb45-c72682c23406 | -6.83893 | -59.25631 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d4704f2-8223-38ee-97e0-fbfea22cbd0e | -6.02818 | -43.5927 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8862052e-f943-34a7-a4d9-102906356f18 | -7.23351 | -46.00829 | 2026-10-03 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 454f22c5-b0fb-30e5-8c2f-854ac75ba1cf | -4.26549 | -50.73656 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 55f2a4d8-08d4-3b55-8e1f-46e0f5e21b8b | -5.40721 | -45.19288 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99b0d10e-b64f-3708-8345-62655fde99d4 | -4.81666 | -49.87738 | 2026-10-03 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92d5966e-ea3d-3842-a13b-12b99630f827 | -4.41116 | -49.96633 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3feef098-6dc1-341a-abaf-d086a081a48b | -9.95453 | -55.32751 | 2026-10-03 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0aa95b9d-3f9f-38e3-9c5a-7e4fb4b59823 | -4.68561 | -55.79605 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c75e57c3-2e01-3d5b-8601-f1a1842ffc76 | -5.95415 | -43.65724 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98186d39-082e-3c73-b512-708ea7e5685e | -4.79218 | -55.72544 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a428df2f-c5f2-3b9b-9c62-01df339ef3e8 | -5.43602 | -43.44667 | 2026-10-03 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f3df0fb-a44c-39eb-8ed7-86bbd9782890 | -5.95473 | -43.65328 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78b12bff-9069-3624-8e16-a238b1435c1f | -5.7459 | -45.145 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bfda9d4-ac5f-3c7e-bf82-27c021bff0d5 | -11.7142 | -43.49817 | 2026-10-03 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a575f6df-d040-3e8d-adcc-629b77232bb8 | -6.50109 | -41.75053 | 2026-10-03 04:40:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d2374f64-93dd-3e30-ab86-634384c0bd0f | -6.85702 | -59.24906 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a148bd30-9db9-3ec3-ab87-0b90f8dc97f5 | -3.58971 | -54.53128 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2d5143d-e181-3c14-a4b2-80e8fb87a3da | -4.80727 | -49.8724 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b49a224-a408-36c9-b430-6b52e03ef2aa | -9.46066 | -40.35996 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 324c46fb-172d-3d7b-8c76-19e72bd9c761 | -5.73748 | -45.14875 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 633e8535-e1f6-3b30-9a2f-c0b0fed696bb | -4.30087 | -50.77536 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbbab6c9-fe8a-30d1-a674-7977a7408958 | -6.05079 | -59.9286 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3ce2c70-cc94-34d0-abea-63e10f3fd020 | -7.83362 | -47.9253 | 2026-10-03 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README28.md)
