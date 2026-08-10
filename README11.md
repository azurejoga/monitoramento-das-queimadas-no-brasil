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
| 55bb108d-9c99-3d64-8513-dce2248fb325 | -6.84258 | -56.40465 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d97303c-fe86-3c9d-b234-d49bc2e66e6c | -6.85221 | -56.41522 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c65c2292-d080-3e83-8207-e9d7a82d85ce | -5.03325 | -56.12276 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32336a79-7627-3263-bdfe-338708cfccd4 | -8.02097 | -55.11739 | 2026-08-10 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 301e7c48-d4ea-38b9-bd12-7186b21e710c | -3.39644 | -49.22285 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b2bad60-e97f-3972-9164-db77fceb8141 | -7.38685 | -59.98636 | 2026-08-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| febc06ac-d2ec-3976-9079-9bfd25eda600 | -3.31775 | -48.81669 | 2026-08-10 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6baf6253-18cc-31eb-b5f6-fb3b53f239da | -2.74454 | -54.59298 | 2026-08-10 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd30b5b8-4497-369f-9880-38f16a8fea11 | -8.16716 | -61.51569 | 2026-08-10 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227c0a9e-be0b-3624-a989-cf930170f39f | -6.83825 | -56.41468 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170257cd-316c-3fb2-a5c6-c78908248cf1 | -7.23697 | -49.86687 | 2026-08-10 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c624c224-811d-3a00-ab7d-1bfa78c4d53b | -6.24626 | -55.6228 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0ee286d0-c2b7-3c68-ac57-86f0c2b55ead | -6.84185 | -56.40905 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14ec3d40-7209-3f0b-9482-94309bd9eec0 | -7.68678 | -55.16563 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c973032-60ee-376e-a067-2bd7abafb009 | -10.2522 | -45.82155 | 2026-08-10 04:51:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 797de4d0-a93e-348c-a314-06626cc66576 | -2.09025 | -54.44267 | 2026-08-10 04:51:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c25f79d3-47a3-317f-b94c-3e870aeba28d | -2.90838 | -54.15264 | 2026-08-10 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d5a463-e12b-3512-aea4-a42bbeae3500 | -6.88108 | -56.63454 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a31bc155-37b1-3d1d-aeda-365be6b92043 | -3.49191 | -50.05272 | 2026-08-10 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7c961d64-e557-399d-a894-9743e7b359fd | -11.04255 | -44.28443 | 2026-08-10 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48560f53-c6aa-3575-b957-76bcee84e79b | -7.11902 | -40.40583 | 2026-08-10 04:51:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f05da4c4-af64-3da1-ba32-b0bb3c2bfd9b | -6.84331 | -56.40026 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c766328d-8e68-35d4-ab6d-2f49a50ddcb7 | -3.93048 | -59.13696 | 2026-08-10 04:51:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6cdf161-1d8f-33b2-b873-d40b11da4fb7 | -3.75956 | -51.60728 | 2026-08-10 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7977a830-2cd6-37ee-bd16-d89d3a354388 | -7.04706 | -50.34192 | 2026-08-10 04:51:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ff4dd69-a0b4-3644-99fd-abed0c9a1741 | -11.04298 | -44.28092 | 2026-08-10 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10b806ff-0096-3118-beba-0f24b09f073f | -15.84564 | -48.13835 | 2026-08-10 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e35027e-222a-3630-a366-7d702647a7dc | -8.68181 | -62.87863 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 907b0a11-a3d8-313c-8618-90a38bb7326b | -15.15483 | -52.71873 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| f1404485-4c2e-3c33-ba6e-009ff45e6f06 | -8.95566 | -60.5413 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 646cf0c7-a27e-3a26-bf1d-534e469765b1 | -8.96184 | -60.57646 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b89d72c-30b5-3cf1-b5fd-5f136d889b86 | -13.85217 | -53.69477 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1ffc4c0-8566-37ca-8c98-cbce1e42c3e7 | -15.38296 | -53.76975 | 2026-08-10 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6ac968e9-09b7-386c-a12b-4e4d71bf882c | -11.84337 | -56.9459 | 2026-08-10 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 139d25e9-70d0-32bd-857c-aac592e4096c | -14.34271 | -52.02955 | 2026-08-10 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f59e0fc-5352-35fa-a171-fafa5985daad | -14.22684 | -48.50788 | 2026-08-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44fc3268-5f92-3627-9e6f-c99f18baab29 | -8.89359 | -60.56623 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c84e42e4-013f-3182-a4ce-c9b0443c49cf | -11.22738 | -54.02702 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26873e69-e4e7-32e6-851a-25b4b4cfb911 | -14.41138 | -45.64663 | 2026-08-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18a7a818-04c4-3ae9-9848-4551b9df9c5a | -13.80723 | -53.92105 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9561467-8338-3b75-a2ec-011f3fc901ce | -8.97828 | -60.53846 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f555db2-1297-3d84-bd5b-616569b0c493 | -9.37249 | -57.36073 | 2026-08-10 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 955f2760-d7ca-323a-920a-c596e4c52593 | -12.10137 | -47.19988 | 2026-08-10 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9aa10eab-3467-36da-b31c-2afe9b60942e | -14.29829 | -54.93597 | 2026-08-10 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c959422-7420-3863-93a4-12adbf8533f7 | -8.9472 | -60.53467 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3bb2fe5a-c257-339f-bb96-7368c397bc22 | -13.87149 | -53.65756 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b04a6edc-bbd9-3f1a-9d71-82f25d56dc1b | -11.2169 | -54.02893 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da235a21-9eee-3ea4-9be4-66defff67283 | -10.62554 | -53.8973 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c60814b-8055-36f8-ad4f-c16738828ab5 | -13.8589 | -53.7397 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fee8b84-dbd2-36b8-8add-aeb52356554c | -13.63958 | -46.22908 | 2026-08-10 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbcebeaa-379c-36d3-95ff-923a9b668480 | -8.90205 | -60.57285 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f800ae8c-775d-39e1-9e88-6f560920d91e | -12.35869 | -53.15417 | 2026-08-10 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edf2f8f8-3ed1-33ca-9fc9-28f423b7eba3 | -15.05173 | -46.55425 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a197a94f-896d-386f-90da-80c4588f668f | -8.89826 | -60.56705 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5fe4c01-10e9-3685-a2a1-dc0c007b6186 | -9.95278 | -53.3066 | 2026-08-10 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8e7b241-56f4-342a-afc9-0fe643829b1f | -12.35814 | -53.15775 | 2026-08-10 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32268a96-af69-303d-89f2-dfaae7276f6a | -8.89739 | -60.57197 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1503e07e-0e03-3394-8069-2588d37101c8 | -9.95224 | -53.31009 | 2026-08-10 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f819c12a-09a7-3073-bcac-38c162702350 | -13.84199 | -53.89388 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cef13b85-472c-3bcf-98b8-46a72aebc955 | -13.80005 | -53.92352 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04235108-9891-3a3a-855c-c9463e48c941 | -9.81976 | -54.89793 | 2026-08-10 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| addd467e-3c3f-32e0-bda6-bac31f06e1d6 | -15.04975 | -46.57082 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0001283a-95ea-3162-969c-0f6939a0e1a4 | -13.85381 | -53.68402 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 344d8df4-fa9a-3f4e-acc5-fb6c2ea97c93 | -8.95778 | -60.55682 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 37d4eb26-c302-3cce-9290-01ed947b141a | -8.94634 | -60.53964 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 77bec6f5-756c-3978-880b-4378dcba5174 | -8.95827 | -60.5963 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5679ebd-ba70-3fbc-8a7b-7a7b2fab42e2 | -8.94255 | -60.53384 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f7bf4b4-2a85-3d43-9018-b1b746bbc38f | -8.97049 | -60.53877 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae8a53f7-85ce-3a79-9440-192583e48038 | -11.46844 | -50.56364 | 2026-08-10 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3f0230d-8bd8-30ef-8364-6f1eb2c8c220 | -8.95898 | -60.56563 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb18ac9c-a7f8-3c0d-a999-522c07d3d337 | -13.85882 | -53.69582 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b90f82f9-afc2-3fc3-8a3e-407e0adeab85 | -11.21745 | -54.02542 | 2026-08-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b642fc89-b685-3bd0-a1b3-a4deb1f83e80 | -8.67766 | -62.87051 | 2026-08-10 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5a6c071-0e5f-3cd4-9ead-1a4535372b77 | -13.8617 | -53.7658 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8668549-608e-3be8-a72e-85f6aa8ccce0 | -8.9643 | -60.53609 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9afada6-57f8-3eb3-a3cf-7700dec714db | -13.86225 | -53.76225 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97568454-6a46-3c7e-ac5c-442ffa6bcb6b | -8.95359 | -60.59553 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d69c2682-a826-3134-9492-3158d8212329 | -8.89565 | -60.58184 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cd17f23a-5235-3316-b6f6-833f5f612133 | -8.95946 | -60.54707 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fd3694a3-03df-303e-8f7a-d53bb3f03358 | -13.85436 | -53.68044 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94c5b577-402b-35f7-a1f8-436ca8f1e178 | -11.17247 | -54.8042 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 083af18b-0552-3aa8-9df0-733fe30e8356 | -12.12577 | -47.18931 | 2026-08-10 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81f8b116-aab6-3135-a883-e1273488bc57 | -8.95874 | -60.54027 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bef1d1ad-74db-3953-8e38-305dfcc61d02 | -10.87962 | -60.73281 | 2026-08-10 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0d20518-63d5-3370-b548-6a70ca7d9674 | -8.95648 | -60.60625 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 388a0b31-ff6c-3656-a469-9efa4c4826a6 | -14.30104 | -54.94007 | 2026-08-10 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5b7dddb-0873-3486-a386-fdc587762004 | -12.39612 | -43.65959 | 2026-08-10 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64a65a47-8635-35f6-bfe8-98b084e0619c | -15.97392 | -54.21599 | 2026-08-10 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a4a6382-9f79-3f14-b21a-ee70bc543d62 | -13.86042 | -53.6631 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef1a3c27-3de6-3d7e-af3b-8b1eddd5eca9 | -15.08413 | -52.67637 | 2026-08-10 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2dc3b21-53ce-3886-92ed-f6eee1fcd628 | -15.04616 | -46.55913 | 2026-08-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ab1fef2-f0d7-3cbf-94c8-d95a637c71f6 | -8.951 | -60.54049 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ba02a2e3-2148-31bc-a037-a953a4237fae | -11.24543 | -54.87899 | 2026-08-10 04:53:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b72f1f1f-6e13-350c-9e6f-0171feccb455 | -13.85104 | -53.6799 | 2026-08-10 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2370835-2de3-3862-a07d-010f8225fdc6 | -9.72222 | -60.20476 | 2026-08-10 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6dfa7ff4-b03a-37fa-8a51-e7bf145961e9 | -14.30273 | -54.92939 | 2026-08-10 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41617268-d56d-3de2-89d0-c362db1f9196 | -13.95608 | -58.10165 | 2026-08-10 04:53:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a44c87c-0113-3b0c-9a82-779f43008459 | -16.05999 | -50.8042 | 2026-08-10 04:53:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08466dec-40a6-3127-9171-4eee8bfb892d | -13.95519 | -58.10032 | 2026-08-10 04:53:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c106316b-75ca-3ad0-bd01-508bf4f2d824 | -8.89652 | -60.57689 | 2026-08-10 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |


[Clique aqui para ver as próximas entradas](README12.md)
