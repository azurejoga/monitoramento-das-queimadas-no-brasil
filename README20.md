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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7618d75a-a393-305e-a0a2-83ec402807b6 | -5.98664 | -57.73174 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a966049-c07c-3e6f-8218-5d2a19989470 | -4.35728 | -54.77842 | 2026-09-11 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0b2f8e00-6a7a-3460-9529-f25596266dfd | -4.29317 | -49.10384 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 828c491a-a6d5-3faa-878d-7bac65901667 | -3.37427 | -50.75215 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f7ccbe3-1cab-3f98-872a-4bb994d1c6e5 | -9.6379 | -49.01813 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0b9b7ff0-7233-3106-a846-55e551511bc4 | -6.84226 | -59.35649 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4b78e1a-c2f3-3080-81d5-84953fd6d8bc | -9.77485 | -43.44183 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9701c486-f650-3f88-bbaf-07d6e8c323d9 | -7.84634 | -56.58811 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82effd70-c19a-3323-b085-22a0f564fc09 | -6.76516 | -58.61889 | 2026-09-11 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78373b7f-f39e-323a-b0a4-bf8dc92a14c1 | -4.24557 | -49.94117 | 2026-09-11 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 24f2b597-66c7-38f0-948c-895d8705d20a | -6.13001 | -43.74553 | 2026-09-11 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1fc28e8-6826-3e10-b887-3a47d3fe1f37 | -2.94354 | -50.47767 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc003ed3-7e34-3353-9160-843563966a6b | -3.37762 | -50.75267 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17c7b8fd-b752-30db-b631-e36c9d7e5142 | -8.39008 | -46.3023 | 2026-09-11 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6cdcc3fd-a4b0-3429-ab82-d5dcce45dcc6 | -2.94072 | -50.47355 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddc560be-8ad8-3616-92fc-b2e99f7e123f | -5.29474 | -49.01552 | 2026-09-11 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a87755e-b34b-32e7-84ad-95cf30c73079 | -4.24152 | -49.94448 | 2026-09-11 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85bd7535-bc29-3335-8954-ccc341b228e0 | -8.93863 | -44.40338 | 2026-09-11 04:51:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46f933aa-1dfc-3060-b521-ba82aac4090a | -6.31838 | -55.85123 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f48c26a-8327-3e87-9c81-752cbc4cbe47 | -9.50698 | -40.34332 | 2026-09-11 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7a77104c-cb79-3585-aad2-6de0d9daf542 | -10.2196 | -45.22005 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b1746d46-0e13-3b7f-8448-81e3f26b03e1 | -3.15341 | -60.65049 | 2026-09-11 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2065dc7a-fac5-32de-a28b-a510a3eeb0f2 | -4.82401 | -46.81018 | 2026-09-11 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c27c9e42-0487-3dd7-957e-183d4707910e | -2.94127 | -50.46996 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e710837-22a7-3982-be3c-2cce0bf895d0 | -4.85721 | -56.00599 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2cc8ce9-c43d-333f-9b41-949f499dc084 | -8.70974 | -49.62104 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2cf1eebd-82da-3a59-a371-6e068e9afdac | -8.94184 | -44.41963 | 2026-09-11 04:51:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cb9c410-9b0f-368b-ba0c-2ab126e84cda | -9.77745 | -43.44282 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a55bdc2-64a4-3982-8182-73f77a0ada4c | -6.32131 | -55.85592 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d9e8f71-d420-3955-a1fc-bbde94a70b49 | -4.82919 | -42.88486 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 66f0ddc8-786a-3d61-986c-55d57582a7a6 | -6.79426 | -44.81338 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 00405098-af2f-33a2-b7f5-52e9626ff0f8 | -9.7805 | -43.4427 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 238cd29b-05f7-3147-b750-31c8b8780d2b | -4.52724 | -54.96375 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf9df584-8e1c-3f7b-ac95-43fcd6457ebb | -4.82466 | -42.87718 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ed8e3da5-97c6-374c-a00d-d7c2bffedcfd | -4.47658 | -54.89268 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7c072c-2143-3b13-ba46-e3788e61a16a | -4.89878 | -55.91073 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de32f31b-c825-3e58-a76c-df7144e3f312 | -4.86088 | -56.00664 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4caf451-dfe2-3f5c-9b19-cfecc3740dd5 | -10.22155 | -45.2049 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c008b6ba-dd08-3d09-800b-59c85253f65b | -4.47972 | -50.68137 | 2026-09-11 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdffbc13-eab0-314d-99fe-e50f99897480 | -5.97626 | -57.7697 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6313512b-22b5-3fad-a827-afea3a949332 | -6.79267 | -48.66349 | 2026-09-11 04:51:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1db09a26-ff0e-368a-988f-d7f737274596 | -3.07268 | -51.33838 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cc3f10e-554b-31a6-9a0c-cee705a50413 | -8.73998 | -49.99592 | 2026-09-11 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef876d2-2c65-3ff8-b8fa-ecc7e44634ab | -3.07052 | -49.51759 | 2026-09-11 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97c43cf1-ef5f-325a-8276-5dfd1a792a48 | -8.70808 | -49.62294 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5260d499-b76b-3a8e-9ec1-0442137fee43 | -9.38743 | -49.38531 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeb88115-402a-3ab7-973d-b73711b7facf | -2.93907 | -50.4843 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1738595-f718-3742-ac78-363e7d98245c | -3.53438 | -48.17943 | 2026-09-11 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c566b1e0-e11c-3c3d-b092-667cc6654e9b | -9.63748 | -47.68604 | 2026-09-11 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7721fd10-3bb4-3c3a-a291-a0082a147c92 | -5.97916 | -57.77724 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99e651f8-c51e-3ff4-b914-2f0559f2389c | -4.53075 | -54.96429 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d254de9-84b5-31e6-aedb-8b11b1474bef | -6.24183 | -51.68632 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abaa7bd1-1503-3632-b3cb-b3939db510fb | -8.65743 | -49.13914 | 2026-09-11 04:51:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df3f208d-b1fd-3fc3-bb12-81b614e185e2 | -2.78627 | -47.62059 | 2026-09-11 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6d22f07-b4e9-3aae-b698-0981b03f2978 | -5.82283 | -53.80364 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54566955-8b4f-3361-a6c3-609aea8149d1 | -5.82787 | -53.79351 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddba22d8-ea21-3f21-a190-7813f34a72eb | -6.75635 | -55.83349 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edc70b81-c533-377f-abc1-9d96ce9be8ae | -9.50816 | -40.34452 | 2026-09-11 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7a1009f3-efa9-33a6-a2ef-7aa48c756001 | -3.36755 | -50.7511 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf6a0461-95cc-3a7b-a1f3-fdeb0846c4fe | -5.76788 | -45.08053 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b9aa297-5e92-3680-bfb4-c8b46b5e33ad | -2.86054 | -49.53814 | 2026-09-11 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9d0cc042-c9a8-3ed9-bb6f-b45e55ec3e83 | -8.93856 | -50.26768 | 2026-09-11 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c30430c6-0dd5-3006-bfa8-beb28ef985c1 | -9.31253 | -44.37049 | 2026-09-11 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8927632-c63a-3291-ae4e-e1fbda6afe58 | -3.26588 | -50.08932 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05cc1d66-6b63-33f3-bda5-beb403b3b1b2 | -10.05898 | -46.26851 | 2026-09-11 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 468b001f-9e5c-3b56-9e7a-f528cf76e723 | -2.9452 | -50.46688 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20a4ff07-661a-3e2e-8c5c-81092fcad3bf | -6.32065 | -55.86003 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2b36233-381c-33c2-bae8-2a15eef06ff7 | -8.28414 | -47.78598 | 2026-09-11 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2e555ed-cc2f-3018-8202-eab5f786c158 | -9.36562 | -49.37534 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88ff806e-22ba-3bef-95f9-af43b86658e0 | -6.82896 | -58.98541 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20904694-44e8-3dbe-a8b0-758eb45a782f | -3.24856 | -50.81684 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a2ebd1d-624c-3230-a505-f3f979c92aae | -6.92176 | -55.63885 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1e88204-5338-378b-ac6c-c181f6d01599 | -8.71344 | -49.62162 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7990b76b-fadc-3811-a784-7225618cb68f | -10.74203 | -49.5933 | 2026-09-11 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97ebf24a-f33d-3c6c-9a9a-4c4cc2f5f8e2 | -10.78853 | -45.94954 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9f9a2524-994d-3bb8-a018-b6db53b35e86 | -12.15331 | -64.13725 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b0e4b73a-c694-37ed-a97a-9e9df0d84285 | -9.40048 | -65.86074 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30059550-6149-31c2-983d-823c47a81e6f | -11.19729 | -45.02138 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b66a5089-cd7f-3f4d-8e39-1cce405d3ffe | -10.54701 | -51.35006 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b5a998e-6bdf-37ea-83f7-6268257ab4b0 | -9.22468 | -65.58913 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f759964-7a72-3eb9-b92b-f4423d11dc7b | -12.18813 | -47.17346 | 2026-09-11 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 948c8c85-9bfb-3cab-850d-1c2e41fc990e | -14.60221 | -48.86366 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc6577fc-0009-370e-8a2b-1ff0bafb824a | -9.37657 | -55.96721 | 2026-09-11 04:53:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30898df8-f954-3641-8f47-14d4a88e5b87 | -9.03628 | -65.41682 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8da58d61-bbb2-38c3-9ff4-eaa4e9780651 | -9.42048 | -65.86285 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8bb2d1ca-0aa0-3a52-b3f1-ef76bf697707 | -9.67674 | -55.1162 | 2026-09-11 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f6510b-f467-3e57-94d2-2867ebdf801e | -14.59851 | -48.85927 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0955a2ed-e01b-3d03-bb2d-69a54b4f48cf | -9.70764 | -54.34529 | 2026-09-11 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeeb5cf4-e761-3bbb-aa07-689d7018850f | -13.48396 | -48.55194 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd0d953e-085e-3d06-8b0f-08d3c27726b1 | -9.03827 | -65.40649 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c99e313d-ecef-397e-b283-93b9609b4969 | -13.88599 | -51.58371 | 2026-09-11 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1615f8eb-13ee-3c57-8caa-28048fbd3516 | -14.58171 | -48.85671 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1fe965d1-4710-3255-914d-4c5dee072564 | -8.63836 | -66.51604 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 83bbc30a-cfa8-38c6-829d-af32e1344547 | -14.88607 | -49.22899 | 2026-09-11 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44ff511c-7eb0-3eea-bfd7-b6a4ee17f6f4 | -13.32416 | -61.67897 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae5454c8-1263-3554-937a-863ee6961e87 | -13.50558 | -44.07035 | 2026-09-11 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dde9a6a6-eae1-3a25-976b-3694e6e5989a | -10.64296 | -46.12912 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a261541-31f2-318d-b98c-586ee873454e | -13.32507 | -61.67405 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6db6ac8d-e1b5-3c4e-a4b1-00db7172cfb0 | -14.58638 | -48.85369 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e32df3e5-cc7d-3f41-9e2a-226a468bc476 | -9.42153 | -65.85757 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README21.md)
