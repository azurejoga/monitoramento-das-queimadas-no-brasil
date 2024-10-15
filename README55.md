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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7123079-848a-3344-aa94-5c31ad114fd8 | -1.81782 | -53.41463 | 2024-10-15 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 964041e1-feec-30e2-b864-7df685f73dd5 | -1.54065 | -54.34837 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87614509-61f2-3444-9c13-db58142a913f | -1.53773 | -54.34381 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1079d357-ce8c-3606-87d9-d8ddb15597da | -1.5371 | -54.34781 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ccf9ca8-66a5-347f-9114-bf8da2c92e58 | -1.51385 | -54.51797 | 2024-10-15 04:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 144c8aca-8ce4-366b-8da7-1f2a5aa06e22 | -1.42315 | -53.47134 | 2024-10-15 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4fbcdc-56be-3c83-9a91-b370d7f7aa09 | -1.27772 | -54.20267 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4a5fc67-5d89-3db9-a22c-201190492448 | -1.2771 | -54.20669 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01ae7cb5-16ed-334d-a195-e7399d401289 | -1.19843 | -54.52285 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5d7709-0e0d-3418-9542-8ec464513892 | -1.19483 | -54.52231 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9148794-d6b6-37dc-bec9-98a9c5562a7d | -1.12847 | -54.11534 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6b1e328b-fcd3-3318-97f2-c5a423f93937 | -1.09202 | -54.16245 | 2024-10-15 04:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9fd7292-dc57-3919-8431-2850a1595e73 | -1.02137 | -53.73337 | 2024-10-15 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e285d90-69f8-3781-87ea-3002f79813dc | -2.25706 | -53.76237 | 2024-10-15 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e03a67ab-cdfb-35f2-aea8-9447009ed1ec | -2.25362 | -53.76183 | 2024-10-15 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e877cbf4-1581-304a-9709-b096feb4bbff | -2.11928 | -54.85665 | 2024-10-15 04:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e26ae3e8-2dfa-3969-b32f-0ad0e75d87d4 | -2.11632 | -54.8519 | 2024-10-15 04:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56a6bb97-951f-31e8-a89d-ae2e6c9e8533 | -1.34918 | -56.04266 | 2024-10-15 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75274cb6-f7c6-3078-87eb-02c04d91cd97 | -1.34607 | -56.03704 | 2024-10-15 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f1422fc-6623-3b3d-af39-9345022b8960 | -1.34526 | -56.04206 | 2024-10-15 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4061234-15a9-3940-8bb6-1cf5327486ff | -1.26188 | -55.91006 | 2024-10-15 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb88f94f-b2ba-3044-b2c5-30247669b73a | -1.18047 | -55.81592 | 2024-10-15 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e42748a9-da3e-337e-96d9-cbe7bbdaa916 | -1.93689 | -56.61393 | 2024-10-15 04:46:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 982bede1-5d8f-3f9c-b26b-0d0de4d259a3 | -1.88261 | -56.9804 | 2024-10-15 04:46:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca4bd64b-bd05-35d7-ac91-505cfe8dcce5 | 1.11885 | -60.51925 | 2024-10-15 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f47a104c-fa9b-3e1f-80d3-1dbc44b0d4a1 | 1.11333 | -60.52009 | 2024-10-15 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4499492e-1c3b-3f29-8d4f-6c9575bbff31 | -10.3713 | -61.1743 | 2024-10-15 04:46:02 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 00690285-7ce0-35dd-9963-a0437e8cbfd1 | -10.3711 | -61.1935 | 2024-10-15 04:46:02 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| dcdb117f-f3f6-30a1-a953-143b6fd398e5 | -11.6917 | -65.2243 | 2024-10-15 04:46:10 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9a8646eb-1fdf-3026-9bfc-28be03d42ff5 | -12.515 | -63.263 | 2024-10-15 04:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.1 |
| ffdeca50-9ebd-3be8-b9e1-33868d84520f | -13.9079 | -45.8124 | 2024-10-15 04:46:20 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 3a4fd5b9-8bb8-3d5c-b775-8cb0f5b08b0d | -13.9075 | -45.8355 | 2024-10-15 04:46:20 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 51afb8f3-3148-373e-aca6-c206a22df063 | -13.9269 | -45.8323 | 2024-10-15 04:46:21 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 32951a79-e96e-36ca-9b2b-ea4c6ec3442f | -13.9274 | -45.8091 | 2024-10-15 04:46:21 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 348.9 |
| aa4e0203-af64-3333-9f5e-b0dd39c3485d | -4.27858 | -48.22399 | 2024-10-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 887e93ea-a799-3097-8d43-8364c7b3b6f9 | -7.94517 | -63.63515 | 2024-10-15 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb7062b4-9a37-362d-9323-20a7e98e748c | -7.94143 | -63.63001 | 2024-10-15 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9f98c6d-db35-3ad2-8ed4-931af3b4c234 | -7.94067 | -63.63423 | 2024-10-15 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9224a964-47f6-3033-81a5-720ebcad917c | -7.94012 | -63.6298 | 2024-10-15 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de79f30b-5541-37b7-bc37-7d6ed54846c7 | -7.93933 | -63.63401 | 2024-10-15 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96c8ddfb-bb09-3d50-acfa-df3f15203f7a | -6.39149 | -41.61242 | 2024-10-15 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df666441-9701-308e-9ded-6e097917796b | -6.38541 | -41.61194 | 2024-10-15 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d2f5739-80a2-323e-9b03-e461868df711 | -7.05231 | -42.09384 | 2024-10-15 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c32142d7-679f-3420-aca6-00d6903387a6 | -7.04639 | -42.09322 | 2024-10-15 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c101baa-0a87-3110-b2cf-906277e89c87 | -9.45723 | -44.18041 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 640c92b9-c0ce-333e-a57b-9d60b605ca31 | -9.45637 | -44.18689 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 206b6325-0122-3da3-b80a-19f47d845f30 | -9.45595 | -44.19009 | 2024-10-15 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd01092b-15f6-360c-945f-0fe9c9d186cd | -9.45551 | -44.15257 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd707c8c-f71d-3eb2-b05d-7c39bf6eb2c9 | -9.4515 | -44.18291 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48f2741f-eb16-39c1-9d41-68c15bb6991f | -9.45107 | -44.18615 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c84b5ca-dcc2-3a47-9b11-9b5abf9f690b | -9.44976 | -44.15513 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f25a3fcb-ebc7-3151-a490-5e1ff272e1c0 | -7.46295 | -44.0998 | 2024-10-15 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b48f2ac9-d861-3f29-8ebe-a75fa3c115c5 | -7.46175 | -44.09826 | 2024-10-15 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21b24282-f865-334f-80d2-a8eb4ea10a23 | -5.97279 | -43.793 | 2024-10-15 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a2be295-8c25-31ee-a02b-2aa0310dbabd | -6.90206 | -43.96828 | 2024-10-15 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95ac95d9-5ccf-386c-835d-fb623811970b | -6.90162 | -43.97146 | 2024-10-15 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54e07385-d72c-32d7-a47e-7979fda0b9e2 | -6.8973 | -43.96445 | 2024-10-15 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3400991-e1dd-3153-adad-62d0a2bf134b | -6.89686 | -43.96761 | 2024-10-15 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70ae5878-6137-39a6-b349-5e79d8c006c0 | -5.04223 | -43.66309 | 2024-10-15 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b8e5d78-ffd7-3463-bbf2-c151b92b5204 | -5.04177 | -43.66623 | 2024-10-15 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e691a0ef-f74e-344f-9d73-61134fe2c00a | -5.04132 | -43.66935 | 2024-10-15 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d757daf3-8239-3d35-b312-7d82280212d6 | -4.64895 | -43.75714 | 2024-10-15 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 115d1b5d-f14b-3c78-8ce3-e507e19b16d2 | -4.64852 | -43.76016 | 2024-10-15 04:49:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8380595-03f1-3286-926f-142973f644fd | -5.22636 | -43.72774 | 2024-10-15 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ece6aa2-f3cd-389e-85f9-9ce74d7cfd0d | -5.22122 | -43.72694 | 2024-10-15 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa0c21f7-bc79-3c1c-8de9-76bea7469b5d | -5.22078 | -43.73 | 2024-10-15 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00c35131-8664-3daf-9d98-e5a735ec87eb | -5.21608 | -43.72611 | 2024-10-15 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9422387a-2f09-3472-a2b9-5b7d5fe410fc | -5.21564 | -43.72916 | 2024-10-15 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa70d6bc-946f-3e47-aabf-83315f4a9fcf | -5.21051 | -43.72831 | 2024-10-15 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c75990b3-7b26-3f19-b422-84d22ec158d7 | -5.21008 | -43.7313 | 2024-10-15 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02971ecb-e5c7-3de1-99da-15ecfb1582a9 | -10.48365 | -42.44128 | 2024-10-15 04:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bfcf52f5-0f2d-352d-a38a-283eb09ef33c | -10.48309 | -42.44592 | 2024-10-15 04:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ab5bcebe-5b2e-3f21-8be2-ff22817a5f62 | -6.09994 | -43.20772 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da6dc9f8-f72c-37d3-b38e-2ddd944c609d | -7.76339 | -43.30946 | 2024-10-15 04:49:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bca4cfc1-e663-3ac8-9a35-0cb7077fa1ff | -7.75839 | -43.30504 | 2024-10-15 04:49:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a79842a5-06cf-3fee-869b-2219a5537587 | -7.72783 | -43.19812 | 2024-10-15 04:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0494104c-1492-339e-bab2-98294d17ca63 | -7.72733 | -43.2019 | 2024-10-15 04:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45a520c1-5fa2-373a-bfbd-d88c17940e02 | -7.72684 | -43.20559 | 2024-10-15 04:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6c9801c-41e7-3db6-9c04-f52e270cf791 | -7.72231 | -43.19727 | 2024-10-15 04:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07b55393-b5a2-30df-b587-5fdad57edbfc | -7.70584 | -43.27912 | 2024-10-15 04:49:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 29bdd2d1-67cd-3e16-98dd-7af0c17b3412 | -7.43764 | -43.01766 | 2024-10-15 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0af47a3f-fdb4-3029-a9fb-01e89c7eb64f | -7.43594 | -42.98788 | 2024-10-15 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 01b5f887-58b4-34d2-a19e-a3727c1985ef | -7.43544 | -42.99157 | 2024-10-15 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af420d21-c00b-3e42-9ece-2a41c8a3e113 | -7.43157 | -43.02054 | 2024-10-15 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 158b08dd-744b-3a92-a31e-b492fe2cdaf7 | -7.17222 | -42.65308 | 2024-10-15 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 961a1a17-954a-3c32-a0b2-6f306ec61347 | -7.17171 | -42.65687 | 2024-10-15 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f64eab3f-aa7b-31bc-a477-e7e13bcb239f | -7.0867 | -43.03516 | 2024-10-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b40871de-401a-3205-a112-6c97bbde7b84 | -7.08621 | -43.03878 | 2024-10-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a41b23f9-e59a-371d-9120-6221ce890eb2 | -7.07943 | -42.63771 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e6e57366-b71a-3fe0-805a-e9246ca5159f | -7.07888 | -43.01559 | 2024-10-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9721391c-2f19-303f-b369-544b198d5e48 | -7.07835 | -43.01938 | 2024-10-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1e09576b-d4e6-3953-b58c-f7e7bfaa3c7b | -7.07808 | -43.01487 | 2024-10-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bccf9579-4c70-3516-a8c8-6fcf4aae2871 | -7.07758 | -43.01867 | 2024-10-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7e5d2572-e7f2-3ca3-bbf8-47bea89232e5 | -7.07474 | -42.67229 | 2024-10-15 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9935fa40-2ade-346e-8aab-700825631314 | -7.07377 | -42.63673 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2ede38ce-8b22-369d-83d9-8ed86e4be644 | -7.06904 | -42.67163 | 2024-10-15 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 85b6f5c1-a146-3cad-ab46-410fa0fab6f5 | -8.33751 | -42.74931 | 2024-10-15 04:49:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 436f4028-b70e-3b77-bb70-dda96af3e582 | -8.33699 | -42.7533 | 2024-10-15 04:49:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4bfedbab-ea95-34c3-818f-247b1896cf2b | -8.32764 | -42.78009 | 2024-10-15 04:49:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b56b549c-ff0f-34c3-892d-77ac6a30bc98 | -8.3214 | -42.78312 | 2024-10-15 04:49:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README56.md)
