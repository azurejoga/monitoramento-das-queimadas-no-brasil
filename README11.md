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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68340185-8677-35f2-ae14-500e8f32e63e | -17.47451 | -51.82789 | 2024-12-08 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47486fab-450b-3b21-9257-c70c229e636d | -18.70895 | -40.57255 | 2024-12-08 04:40:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 16111cb4-d3be-3c55-8313-d69d7022eeab | -15.97753 | -57.16974 | 2024-12-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69567c90-0c06-3a8e-96cf-5f615de8989a | -16.34743 | -43.69916 | 2024-12-08 04:40:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 719c1a3a-c117-3838-ba7f-4e15f5ca85f7 | -15.16183 | -56.47824 | 2024-12-08 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0146f22b-ad13-3cfe-9f65-186d6b725786 | -15.36758 | -53.12842 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13b8ddcf-feca-3786-9402-1f1d18c96a85 | -17.15666 | -53.8105 | 2024-12-08 04:40:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b30047e-b48d-37c3-b690-4da205b16c55 | -15.37098 | -53.129 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ed2f09b-1dfe-39ef-9c50-9054ba73991d | -15.80032 | -49.01497 | 2024-12-08 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 561b153f-660c-312a-97e5-1c1a5e18ffba | -18.94257 | -54.92393 | 2024-12-08 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6473e505-0dbb-30a6-8031-817251aebc86 | -20.26968 | -41.33048 | 2024-12-08 04:40:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b083d0ef-fe91-3c45-8ac1-dd7eb0d71721 | -15.26182 | -53.57592 | 2024-12-08 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d067894a-08f0-318c-8746-282a140457df | -15.08414 | -59.63545 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9474be83-d718-3a6d-94da-752716249b6a | -18.70997 | -40.57082 | 2024-12-08 04:40:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ee9118a6-82d6-36f7-811d-f8f97f119865 | -15.09283 | -59.6434 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74dd1f3f-1d9d-3518-a1e4-f8d90273056d | -15.25837 | -53.57528 | 2024-12-08 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 480b6470-a6f0-3501-a61f-0daa38d9a582 | -15.09397 | -59.63762 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6abe96a0-5d5b-3cc4-8d57-952769643c95 | -15.36141 | -53.12346 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a86e68a-b7c9-3771-8c1e-a3bfa471141a | -17.82146 | -45.31836 | 2024-12-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d5d8620-c56c-38ee-8e2f-28f184140852 | -17.48114 | -51.82902 | 2024-12-08 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02c86aa3-ca00-375a-b4de-d6e8c478dc12 | -18.71502 | -40.5735 | 2024-12-08 04:40:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9687a95d-2ca5-3e0c-b3f9-1683ac56830f | -15.87767 | -53.26964 | 2024-12-08 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69c35b4d-0c1c-3f6a-9653-9062c0a20280 | -15.06974 | -59.65651 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6271171d-017e-3627-8e94-71bd690726bd | -15.0648 | -59.65553 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5402a44-cfd4-33d7-a5fc-c98ee15da0cc | -20.27 | -41.327 | 2024-12-08 04:40:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| adf5df5e-2370-3bf0-b3d6-0084974489f8 | -16.01278 | -51.88057 | 2024-12-08 04:40:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2263dfdb-3ef1-3ba3-9674-57efe4408a66 | -15.36544 | -53.12028 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75ad9f29-6197-329d-9e06-b5b7cd3a949e | -17.6598 | -53.86703 | 2024-12-08 04:40:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1a74f90-a1d4-3c60-9c6d-ada151027b86 | -15.36481 | -53.12405 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7482171a-1c18-391b-b878-59e400147bde | -17.16074 | -53.80723 | 2024-12-08 04:40:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6a7c0aa-ed6a-3027-ad5f-421054dc51eb | -15.36821 | -53.12465 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef859889-c58b-37e6-94ca-39f440460b49 | -15.1538 | -56.47675 | 2024-12-08 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e35df5c-1bb5-3670-81d2-b8f62983c2c9 | -15.37161 | -53.12523 | 2024-12-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 397847f3-b2e2-33d3-8dd7-ac263195364a | -17.23234 | -54.46069 | 2024-12-08 04:40:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22ef0b45-8229-338c-bba9-4b73decfa58d | -15.08565 | -59.6539 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c85c36e-a73c-33a5-9151-af055f455542 | -15.84382 | -54.10893 | 2024-12-08 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae6b649e-cbdd-362d-9f38-3a04bd5e745f | -17.98818 | -52.4007 | 2024-12-08 04:40:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67f5903f-d18d-3e2b-a1e2-fdf1388ce977 | -18.94608 | -54.92458 | 2024-12-08 04:40:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 682dacd8-ab91-37a2-ae81-f218dca0bf7c | -16.66385 | -52.10129 | 2024-12-08 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b0edf80-567b-3476-bdf4-b4472a5701db | -17.26948 | -46.26502 | 2024-12-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d8141ed-8d22-3a5d-abc9-3255f3c7fe88 | -15.15781 | -56.4775 | 2024-12-08 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f80bb8a6-6512-368f-bf79-8017d6dce435 | -15.97681 | -57.1736 | 2024-12-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b44af162-2e1b-3199-bdc5-10feb3852028 | -15.98166 | -57.17056 | 2024-12-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fe21a4f-52b7-3d45-87be-cff9dab672df | -17.46235 | -47.86718 | 2024-12-08 04:40:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58b48f5c-a5fc-30a0-b38a-b2f0ca4ec0af | -19.3608 | -41.51675 | 2024-12-08 04:40:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 98da5aff-0e2a-38c7-b84e-3f019aaae86f | -15.84103 | -54.10759 | 2024-12-08 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d92e929-6358-34b6-98be-3f22173bb583 | -15.08792 | -59.64233 | 2024-12-08 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2791de4-fae3-315b-9e67-74e03a7cfe75 | -5.24841 | -37.50622 | 2024-12-08 05:08:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e78e2e1e-51f5-3562-81c6-2e9da402bbe6 | -5.47592 | -39.41624 | 2024-12-08 05:08:00 | AQUA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 054e68d7-1e5c-3181-9d8a-2d81540f87e1 | -5.25034 | -37.49273 | 2024-12-08 05:08:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 497b047e-133c-3c1a-a42c-5e50c281d25f | -6.87127 | -47.23292 | 2024-12-08 05:10:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fb30148a-3a03-3603-bdf5-73e9505c4353 | -6.04975 | -44.04682 | 2024-12-08 05:10:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 183f9914-74ff-3a5a-b723-a88db680a6ef | -7.9861 | -45.79442 | 2024-12-08 05:10:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d39ebea1-a607-31e9-be1c-075ea4bfb67a | -13.98352 | -50.29154 | 2024-12-08 05:10:00 | AQUA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 55b66eec-0f55-30e7-88a8-d4c314382550 | -18.70981 | -40.56297 | 2024-12-08 05:12:00 | AQUA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 52f8bbb0-cd5d-32e0-a4a6-97e6965cd80d | -18.70809 | -40.57632 | 2024-12-08 05:12:00 | AQUA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 6de797fe-7cb9-3fe4-a676-05c5923dbc58 | 1.97882 | -60.92156 | 2024-12-08 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f50b55bf-20d7-305f-b492-129310782fe1 | 2.57299 | -60.69479 | 2024-12-08 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a693eabb-6f05-37fe-87d1-35f6bf2fc955 | -6.23464 | -55.62851 | 2024-12-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 108b1129-a287-3ad7-9b1c-206bf1fed2e9 | 1.99673 | -61.14483 | 2024-12-08 05:29:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36b686c1-d54b-3789-8b37-156d3e79341b | 3.60412 | -61.83907 | 2024-12-08 05:29:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ed286a8-eeb3-3096-bae1-9aadce6cb025 | 3.32807 | -60.06006 | 2024-12-08 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b68179e7-8b9a-3699-9a70-e981a84ee8eb | 1.99619 | -61.14138 | 2024-12-08 05:29:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35ba3774-b03b-39ba-a310-32bdb0923074 | 2.56965 | -63.94246 | 2024-12-08 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53e7b970-4b30-36e6-8805-9fcaf30ebf33 | 0.75086 | -59.65812 | 2024-12-08 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bbc0271-0657-32c9-99ae-32e5eb0a79a5 | 3.69617 | -60.54399 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b507308-f1fc-354f-8fe4-6203a0c68223 | 4.06036 | -61.18245 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f60d8f60-c69d-31c5-8f8a-4bd8b33d7b2a | 1.97829 | -60.91811 | 2024-12-08 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b70b29b6-3f95-36ca-9a3f-5b053b5b0214 | 3.64965 | -60.77056 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7de089b5-cbd0-33c4-8a95-d80470f13c23 | 3.75421 | -60.0003 | 2024-12-08 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 716c1335-72e4-363d-b6ac-294e7d78f67f | 3.64858 | -60.76363 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e8ad025-0509-372b-99e3-8091981e4b66 | 0.908 | -59.44656 | 2024-12-08 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95f6cb1d-6d76-360b-b043-1739e143f025 | 1.9995 | -61.14088 | 2024-12-08 05:29:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35f52236-3521-30d0-acef-8012cf2da5d0 | 4.60269 | -60.5999 | 2024-12-08 05:29:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5245fa16-5a35-34ac-9c36-1ebc49cfa97b | 1.99341 | -61.14535 | 2024-12-08 05:29:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 010fef4d-d2ad-3f5a-9e3f-5312a5505585 | 3.64912 | -60.76709 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a7be995-2b30-3e00-905f-f6afaabca912 | 4.65989 | -60.81558 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17c84bee-6f5a-3041-83dc-1a9928ca21e0 | 2.28403 | -60.21676 | 2024-12-08 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 315ced64-fe80-3143-bd00-774ec49bdbbe | 2.57353 | -60.69822 | 2024-12-08 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e293eee0-c722-39e4-a564-de36d08b1431 | 4.0838 | -61.15718 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af7f4065-2f32-39a4-ad0d-54703b8162f3 | 4.07592 | -61.19453 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e669dd1-19bf-32c5-8182-16e1d7cf4d11 | 3.68411 | -60.53173 | 2024-12-08 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f69d7018-0436-30ca-b603-ff09a15e23ac | -12.78368 | -54.22232 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 889c24b6-cdd0-39a0-a718-6288a20c7fc7 | -9.37897 | -57.5545 | 2024-12-08 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 466acb0a-6fa4-3b64-9388-e88f2bbdd6f5 | -12.85244 | -58.22285 | 2024-12-08 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d8b3e70-e982-38b5-8198-818e767e2989 | -9.29208 | -64.24917 | 2024-12-08 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 475a1f27-60cc-311d-be8a-44308dc27b83 | -9.3725 | -57.55479 | 2024-12-08 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe7da4c7-7cf8-3262-816f-863b78c2a8a3 | -12.85954 | -51.94114 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 010ad909-08a2-3e22-984b-603f28fcdebc | -11.75406 | -54.73376 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 68160629-5e35-3eb4-8175-793a28b588e4 | -11.75485 | -54.72749 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7612ac0e-ed60-3cf7-8d4d-0a396a233345 | -13.89682 | -54.6309 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 637ec3ef-cca9-3973-a38a-d5e209573440 | -11.75445 | -54.73063 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| caee044e-73fa-3032-8419-568f81157492 | -12.78411 | -54.21875 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8aac768c-a7a5-3de0-8654-74336adac173 | -12.85378 | -51.93516 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9a090d6-dd2f-379a-883f-7fc5fbd5f55f | -9.37482 | -57.55392 | 2024-12-08 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 006da9be-3ae2-3b63-ac02-92cb1eaeb032 | -12.85667 | -51.93826 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7de044dc-1ee7-36e9-9a3f-7ab203518181 | -9.92972 | -59.93352 | 2024-12-08 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c9ad4f8-75dc-3489-ae4c-f32e560897a4 | -9.37949 | -57.55069 | 2024-12-08 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f619739-ccfa-3411-afbc-cc05178c0d29 | -12.7778 | -54.22513 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9ee059a-00de-3069-ad65-53fdd9549079 | -11.20483 | -53.82191 | 2024-12-08 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README12.md)
