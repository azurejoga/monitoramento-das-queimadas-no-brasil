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
| 99406f3d-16d6-3161-9874-37ad9330db66 | -3.81121 | -52.3547 | 2026-09-07 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf2a4b75-2191-38b7-b8d7-ad8cd5da13ab | -3.26452 | -57.87363 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab69e4b7-8dc7-329d-a721-75b6fb094b58 | -8.72904 | -62.44772 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fd5f8e6-7bfd-3a34-b5e5-0f1217ee625f | -3.42445 | -59.64905 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93a7e5fe-28fc-3f56-8f52-4a2f33deb180 | -6.02496 | -60.16975 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3af4a1b-c89a-3a19-b810-aaae4ca7c9e1 | -1.56435 | -55.24887 | 2026-09-07 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d85f258f-7d85-3723-9bc3-c1c178f3c5e7 | -3.44031 | -59.25225 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c443175-2098-3a22-99d6-1b95fa82cf9d | -3.19861 | -61.23494 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 586a2ac3-0f1d-3d9e-9a88-e5365a2b07ed | -3.66257 | -58.90021 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b975b317-1bad-357d-91a4-75983d5defdc | -6.13904 | -59.88492 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da95ac3-19cf-3405-ac56-e885bb562d57 | -6.14894 | -57.75714 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ad74e5-4212-3db0-a62a-d5b8ad7c15e7 | -6.11236 | -57.6372 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dbc12710-715d-30f4-958a-61d28815913e | -4.97977 | -50.62939 | 2026-09-07 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e8dbe4e-3303-3e5f-af98-a529bb0d6f76 | -4.66523 | -55.64231 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc98b52e-9ee1-3819-b150-301b1e543081 | -3.38988 | -61.3289 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bed3a3d-fd36-3d4e-9094-01e3837b53ce | -5.36311 | -56.0313 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1931b6a3-5207-3de6-be1a-091873bbbdd6 | -2.91649 | -54.12053 | 2026-09-07 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5ff54c1-20f5-3a53-8dd2-f40dd16afe97 | -5.59294 | -60.64556 | 2026-09-07 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8751c28d-8c29-3fd7-a190-212c426341fc | -4.35253 | -48.97363 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 127dec28-c3ef-3dc8-897b-6b5796823dcd | -3.96009 | -59.3597 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1c31da7-7744-356c-92a2-0415c6dfbeff | -5.29764 | -60.13041 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9669507d-085a-399b-80f0-9268e09cb38c | -4.12469 | -54.41044 | 2026-09-07 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 414aff54-77d0-3ca7-a8f2-f3fe3adac487 | -6.05574 | -57.79009 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2bf8d580-a3df-3129-b7b7-7da7e7b585b6 | -5.98837 | -57.6917 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f13fcf40-6086-37cc-ada5-cb22ead681df | -5.51511 | -61.10886 | 2026-09-07 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 399fee17-d923-3c1e-98b5-e6259a4b5ede | -4.48607 | -55.50168 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1349929-39ad-380c-9dd3-556e0a7eff08 | -5.36607 | -56.03589 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4345f2bc-4467-3e31-9a49-b110a50a1a77 | -5.29592 | -60.14107 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0daf258c-8974-3f08-97cf-923b76dbcea7 | -5.15128 | -55.95787 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bf14a64-b239-3690-b05c-806857472483 | -4.66462 | -55.63214 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06980518-f9e8-3d35-838e-efa09806adca | -3.49027 | -50.60468 | 2026-09-07 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91422311-ab34-34c9-9eb6-a0b380a5bf0b | -5.68098 | -60.24565 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ce75725-4cc3-3ef9-b388-acd59b825d6a | -11.65178 | -52.86714 | 2026-09-07 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8e84f40-bfb1-35b8-b729-e48cd36eca8d | -3.90675 | -59.65273 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20707c0f-8851-316a-82e4-f81a3e215dfb | -3.79217 | -55.88045 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9873324-fab8-3f0a-87b1-6640e3eac0f1 | -3.41426 | -59.24458 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 350e2677-567a-37f7-8694-49029b805038 | -1.86988 | -47.98433 | 2026-09-07 05:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ccb611da-9772-313b-bcd5-7366dfb45446 | -2.45265 | -57.91619 | 2026-09-07 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 417f505b-7f6b-3f08-b31a-1716754b02eb | -4.28088 | -59.96949 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6b9dad1-3b91-3348-aa8b-38173a9a4511 | -2.63694 | -46.77063 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f3e9c278-81e1-3592-8ea1-72c8f840aa95 | -3.77852 | -58.85522 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c35eab8-b0c0-3fbe-a48f-9b86f9dbc574 | -5.36841 | -56.04452 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3ba7b53-5712-353e-b61e-6a9155e02156 | -5.35161 | -56.01834 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ae87f7e-aa5d-326b-b526-15147ed52a6b | -4.66716 | -55.62995 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de82452f-9181-352f-99a5-bdbad1a9c860 | -4.41253 | -60.0746 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b5190ba-9930-3f20-bba1-3eaefc80f1e0 | -3.64476 | -58.77733 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 837fc96d-12b8-3ff8-b21a-4df98bac68a9 | -3.14576 | -60.66387 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 16f7d97e-5521-399a-9074-bb4f728a5a36 | -8.76615 | -62.42102 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02c752a5-3a6c-3030-8bf4-73931799b14c | -5.26899 | -60.15867 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc282889-d135-363a-9f33-e019ab8b3522 | -5.29207 | -60.12222 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0116a8a3-2998-3b75-9faa-97e9b1998fa0 | -1.6238 | -55.16642 | 2026-09-07 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90250713-34fb-3b43-8291-b427cdb458f7 | -5.36232 | -56.01994 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36e9d1d6-8391-3b4d-8d41-370ab2ff462d | -5.36605 | -49.20152 | 2026-09-07 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 67106940-2887-3335-837d-3fc4230bfacc | -3.43181 | -60.41218 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55cdb5b1-3c6c-3190-a90e-b0dfdaa859ee | -5.25055 | -59.98095 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e861ba2-a80e-3de0-8e9c-d187148107f1 | -6.25384 | -57.78046 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b857562e-a481-3024-94ba-0d7166c03051 | -5.99174 | -57.69221 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fb526f1-5eb8-34f9-bb76-bd70b6a69cd5 | -4.97477 | -55.85257 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c54e2e7e-8c6e-352c-b173-391b0da2355d | -8.71203 | -62.44074 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ddaeb4e-08fb-3928-bffc-5cf754cc6ff2 | -5.2539 | -59.98148 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20fab97-aa16-3315-941e-de1bb74104f5 | -3.12008 | -57.6914 | 2026-09-07 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38dc900-cdc1-352f-ac6f-571937b8d04e | -5.3732 | -56.03696 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93297b30-5944-3eeb-9c2d-ea32d5ac3a6a | -8.76483 | -62.42902 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50d35d95-54eb-381c-be80-287173edef6d | -4.29322 | -59.95684 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fae4f420-882c-363f-811b-27d306e3ed95 | -4.2848 | -59.96646 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92795abc-f4f6-3e35-af81-fdd1f5742bee | -5.36494 | -56.01914 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61a82cf7-fca5-3496-a3e3-d4552d6b3d43 | -5.57173 | -60.16327 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9123ea6d-aa18-38eb-8119-23a79aae4654 | -5.36042 | -56.03207 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e08b5bb-67ed-3ecb-8426-fa938a949180 | -4.46603 | -55.09228 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ae11e37-9239-3751-9c8a-a13d74b37da8 | -8.70631 | -62.43153 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8756a97f-dbcf-3712-8755-13d98f842757 | -4.97423 | -50.63268 | 2026-09-07 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdbec294-3f5e-3dbc-8a59-8abfc26e516d | -1.20212 | -55.73685 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 078bab37-f1f0-3ac5-b973-88dff636f74c | -3.83903 | -59.3081 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 567cdee0-d79e-34ad-963d-bde1661a4f17 | -3.14005 | -60.65521 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f023144e-bb59-3c32-a3a5-cddcda6e9122 | -6.05349 | -57.80438 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cc8b5bb-f556-3b19-b292-96fa307ebab8 | -3.1076 | -61.50346 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bda511d-24c5-399a-9c37-9d903779a19e | -3.04918 | -57.4514 | 2026-09-07 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8ed525a-58dd-37a6-b9d1-b1e98775cda1 | -6.13099 | -57.73964 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72b3722b-43f3-3b37-8310-0cf186b153c8 | -5.36668 | -56.03184 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cbb05f9-e268-3393-9ea7-0f2be416e798 | -4.54331 | -55.98062 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4801d6e9-8628-31db-8b33-3fe14707d331 | -5.35266 | -56.03505 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d930e03e-684e-396a-b7a2-fbba097b9825 | -5.13995 | -55.96027 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5acbcb6-244d-353f-a7ec-553b1f3a94ec | -5.14352 | -55.96083 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a75e8ff8-9db9-3342-8a67-91a526f8de30 | -2.82267 | -49.22943 | 2026-09-07 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89b33911-cfa4-367d-85c3-3ebaceffb900 | -3.14698 | -60.6563 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e31c2059-53dd-3d27-abf9-1641cc81ffe9 | -3.78721 | -59.72036 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 774cb873-9a73-3fb6-85ca-1e0ea334152d | -6.1815 | -57.7254 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ecec64c-9f7a-35f6-a98f-36b33ae7897d | -5.14709 | -55.96138 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 903f7c86-091f-3bdc-a2de-d5be31030da7 | -5.26842 | -60.16223 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e0b8183-ea28-396c-af96-cc7a2c3211ec | -2.45596 | -57.91671 | 2026-09-07 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ceeae37a-ebfd-3971-9d76-e7dbda6c59be | -2.96115 | -48.708 | 2026-09-07 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43566185-2459-315a-ba61-cd3500ee2808 | -4.42767 | -55.09549 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51dc799e-34c7-35aa-906b-b2885facc1fb | -4.27974 | -59.97662 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b32b78c1-7090-3ed5-9720-a4ea539817e0 | -4.28816 | -59.96699 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69675235-2841-3d5f-8619-c764afbd9d62 | -5.30484 | -60.1498 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cf6373f-71a2-30ad-8934-98b46553e5fc | -8.75358 | -62.43118 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcf5725d-2499-3fbe-9b6b-7a94e51d575a | -3.38697 | -61.32431 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 925f7187-17f3-3836-99b5-484870331743 | -5.29707 | -60.13396 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce82da47-2413-3c96-b8ce-2f2aa791e999 | -3.78665 | -59.7239 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ae5c8ca-6ab7-39ef-bbca-303f914d2f03 | -3.42178 | -58.31925 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
