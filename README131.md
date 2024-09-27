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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 670c2655-73c0-387d-840f-c296a8b2456a | -12.7099 | -54.0769 | 2024-09-27 08:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 6d566427-bc44-35f6-837b-9f21d2fd3c73 | -12.7659 | -62.6342 | 2024-09-27 08:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 01788a40-b974-3a13-a5c6-081b82a51f48 | -12.7657 | -62.6534 | 2024-09-27 08:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9bc97193-448d-3ce0-98f8-3998f07eb551 | -14.903 | -51.4319 | 2024-09-27 08:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 10ab9e65-8fb8-3c0c-acb8-5cbabcf245bd | -14.9034 | -51.4104 | 2024-09-27 08:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c3acda1a-c918-37bb-99ef-4c1869710f3c | -14.9224 | -51.4292 | 2024-09-27 08:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b1ec3e0b-c179-3174-9d50-9e0018c13ba4 | -14.9228 | -51.4076 | 2024-09-27 08:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 3cb0dc95-e045-3a56-a0af-bf18c2cc4478 | -16.0989 | -51.968 | 2024-09-27 08:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 2fc3d2fa-ca40-3e30-9d31-08fe220d7014 | -16.0993 | -51.9465 | 2024-09-27 08:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2a80b266-7f5f-3e5b-831c-020409006ed2 | -7.5703 | -60.5984 | 2024-09-27 08:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a8be2d68-e85a-3937-8e7a-dac9ed182f9a | -7.5887 | -60.5976 | 2024-09-27 08:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.8 |
| e7f7ec7d-f3d8-310d-b9ec-ead4c9a94cb8 | -7.5888 | -60.5785 | 2024-09-27 08:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 8a2861ce-1036-3a1f-b59c-af209c5e9e42 | -7.6072 | -60.5969 | 2024-09-27 08:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4dabf555-87c1-3dbe-91cd-dbe552cf4600 | -7.6073 | -60.5777 | 2024-09-27 08:45:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8a939e40-22ad-3aea-9773-2e0e8e6fdd79 | -7.8156 | -54.7252 | 2024-09-27 08:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a463d5f0-cb18-3876-987e-86505d1015ae | -8.9977 | -67.3909 | 2024-09-27 08:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 56cd5040-b479-395b-bcb3-7a5bb370320e | -8.9978 | -67.3724 | 2024-09-27 08:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 137.3 |
| d70ca7d4-6a4d-3c45-b88a-63db8cbd5b49 | -9.0163 | -67.3719 | 2024-09-27 08:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3f56926b-1a36-3a2d-8c65-8f368e44ca0d | -8.9978 | -67.3538 | 2024-09-27 08:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a3422e34-dbda-3d23-92a8-d3dcb78a509b | -10.0141 | -53.4258 | 2024-09-27 08:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a175fed6-6311-3408-94be-27cdd321ff8a | -10.0139 | -53.4464 | 2024-09-27 08:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4b90d775-1af9-3db6-8fbd-208cf91aadb8 | -10.0327 | -53.4448 | 2024-09-27 08:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 3a8e093f-e79a-379c-a1c8-7493dc5a596d | -10.0329 | -53.4242 | 2024-09-27 08:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 62dd1bf2-41ed-34a2-85a1-f07b99a6171c | -12.7657 | -62.6534 | 2024-09-27 08:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| faeb00be-b515-3ee3-aa0c-b0bc14d2bfbc | -12.7099 | -54.0769 | 2024-09-27 08:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e253544e-857f-3520-9332-4b0c40f08c18 | -12.7102 | -54.0562 | 2024-09-27 08:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9c1c495b-d16a-39fd-99c4-93544e0aa345 | -12.7868 | -54.0275 | 2024-09-27 08:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 374cb58d-eb42-3601-9f5e-ea173b49c773 | -12.7659 | -62.6342 | 2024-09-27 08:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 332cf7a1-6575-3df5-a4cf-72ba997d71bb | -7.6072 | -60.5969 | 2024-09-27 08:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 60763317-643c-3b2d-99fa-a6126ecd3472 | -7.5887 | -60.5976 | 2024-09-27 08:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| c8d3a246-f63a-360e-899d-fff4284b854b | -7.5888 | -60.5785 | 2024-09-27 08:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 4e8e5c69-2b4c-3501-a0b0-0f28ea3c56ec | -7.5704 | -60.5793 | 2024-09-27 08:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c18a3e87-922f-394e-8ccd-b956f29e0cd4 | -7.5703 | -60.5984 | 2024-09-27 08:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3d1fb9fe-5d8a-3936-aaf6-b8637952f376 | -7.6073 | -60.5777 | 2024-09-27 08:55:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 72acb437-7ee4-34f0-8aa0-774f860a0905 | -12.7659 | -62.6342 | 2024-09-27 08:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 74d90d9e-a686-38d5-8751-24e5db1142bf | -7.6073 | -60.5777 | 2024-09-27 09:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 545b470c-12c0-3a28-b11f-660170cc25fa | -7.6072 | -60.5969 | 2024-09-27 09:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ff7d56e0-5d22-3858-9b9a-8ef85e85b215 | -7.5888 | -60.5785 | 2024-09-27 09:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| d68dd0d9-f3d8-341d-b23e-d60756d40d12 | -7.5887 | -60.5976 | 2024-09-27 09:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 1c05ac26-7940-3ea1-b0d6-7c97adbaa89f | -7.5703 | -60.5984 | 2024-09-27 09:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 125d6965-f2cb-374e-9089-c82208fdc9f4 | -8.9793 | -67.3728 | 2024-09-27 09:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9b993309-4c41-3da6-b55e-63537e66cf09 | -8.9792 | -67.3914 | 2024-09-27 09:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ef8d2524-fc42-36fa-a131-402f9cb700ab | -9.0163 | -67.3719 | 2024-09-27 09:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8697666c-c338-3190-9514-d48dcbd91a86 | -8.9978 | -67.3538 | 2024-09-27 09:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| bfc852be-efeb-3f8b-b50f-d15d159848f5 | -8.9978 | -67.3724 | 2024-09-27 09:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 271.3 |
| f71bb464-cfee-35f7-b1ca-3f379961d85d | -8.9977 | -67.3909 | 2024-09-27 09:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 8902023a-b7e0-369d-a30f-26718e3ccb8b | -14.9224 | -51.4292 | 2024-09-27 09:26:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| d9b8d98e-2585-33c9-8c63-f6cad1d3a717 | -14.9034 | -51.4104 | 2024-09-27 09:26:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 672da340-5817-3410-b164-28899bc6e471 | -14.903 | -51.4319 | 2024-09-27 09:26:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 334.9 |
| dcf64bec-1fdd-3e9b-b526-d8f42f210c14 | -14.9026 | -51.4534 | 2024-09-27 09:26:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 180.4 |
| f0975024-14e8-3409-8335-2dc1191e8ed2 | -8.9793 | -67.3728 | 2024-09-27 09:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| da5731e5-c729-3437-bb6a-53b455bf68f7 | -8.9792 | -67.3914 | 2024-09-27 09:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0f5f3a3d-92f0-3c2f-b845-b72056f592d3 | -9.0163 | -67.3719 | 2024-09-27 09:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 93b1e135-ce19-31ca-a36b-a9223109c487 | -8.9978 | -67.3538 | 2024-09-27 09:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 27a4ac62-d8d8-36ae-9cd2-019ed4bad008 | -8.9978 | -67.3724 | 2024-09-27 09:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 319.3 |
| 15808851-10d2-3cc0-9a5f-cc907fc0ade2 | -8.9977 | -67.3909 | 2024-09-27 09:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 87553113-8f0a-3021-ba85-f40da36d0dcc | -10.0329 | -53.4242 | 2024-09-27 09:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 13a96bbe-8988-3cfa-9c01-695c8d53ffa6 | -10.0515 | -53.4432 | 2024-09-27 09:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 88799321-894d-320d-bf56-651b0a13cba2 | -10.0327 | -53.4448 | 2024-09-27 09:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 194.6 |
| afc0413c-f880-3533-bbed-7b17eca332aa | -14.903 | -51.4319 | 2024-09-27 09:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 046c68a6-2849-3b6e-88e1-a735b7045b3d | -14.9026 | -51.4534 | 2024-09-27 09:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| b69872e1-246c-39ea-bd01-941f627bddc8 | -10.0139 | -53.4464 | 2024-09-27 09:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 378.2 |
| a5ee7c2d-59c2-35c1-83ee-2db376d67774 | -10.0141 | -53.4258 | 2024-09-27 09:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 059e500e-f4df-3cb6-a61e-c53566946665 | -10.0324 | -53.4654 | 2024-09-27 09:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| e81f5f44-d18d-3b60-b05a-4a6fe14a5564 | -10.0327 | -53.4448 | 2024-09-27 09:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 606.5 |
| 194de1b6-bf37-3505-a88f-0e051033edd7 | -10.0329 | -53.4242 | 2024-09-27 09:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 204.1 |
| e6d7dc48-5e0b-39ec-98a4-f3ed4c0cef05 | -10.0515 | -53.4432 | 2024-09-27 09:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 26009538-9702-3c7e-9672-3be77d9983f4 | -14.903 | -51.4319 | 2024-09-27 09:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 0bd9624b-cfe9-3c6a-85f8-07cb7a0b80c5 | -14.9026 | -51.4534 | 2024-09-27 09:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| b0619d89-d9f8-3fe6-ad8a-d4784c2c64c7 | -10.0329 | -53.4242 | 2024-09-27 09:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 5b1c96e1-5ad5-3bfc-a041-c5e2ceb9d171 | -10.0327 | -53.4448 | 2024-09-27 09:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 37619dc1-4abe-3c04-90b6-f688ebfba08d | -10.0515 | -53.4432 | 2024-09-27 09:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 932016ef-6b01-39d3-8131-93ea761db0cc | -14.7305 | -45.5061 | 2024-09-27 09:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 255.4 |
| fe8250e5-3dc3-3403-89f7-c56f67852480 | -14.731 | -45.4827 | 2024-09-27 09:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 2a510448-cc64-3c53-9145-02313777ea2c | -14.9034 | -51.4104 | 2024-09-27 09:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0d45f08f-406e-3bbf-a472-dca5bb4cd00d | -14.8835 | -51.4346 | 2024-09-27 09:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 9460bf72-6d33-3863-90cc-1a8cd55537e5 | -14.903 | -51.4319 | 2024-09-27 09:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 07b0eb0f-0e61-3e77-8df6-3e072f6f5eb2 | -14.9026 | -51.4534 | 2024-09-27 09:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| f5545f03-09a8-3ce5-93f7-172fc1c83e02 | -10.0139 | -53.4464 | 2024-09-27 10:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 3e17d13b-4b62-38f9-b75f-7c021eb1e694 | -10.0327 | -53.4448 | 2024-09-27 10:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 820def7e-5761-3698-b8f3-286556614ee7 | -10.0329 | -53.4242 | 2024-09-27 10:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9a3f42da-b8b1-355f-94a7-63cef0c0079a | -10.5521 | -45.7391 | 2024-09-27 10:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 37bd9df1-0a18-3f74-93ed-26eed32363ea | -10.5712 | -45.7366 | 2024-09-27 10:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5ce6d3b4-f649-30ec-8e70-e11eeab9adb5 | -14.7109 | -45.5096 | 2024-09-27 10:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 9864db3d-8be2-3f09-9813-64ff6eb8a57b | -14.7305 | -45.5061 | 2024-09-27 10:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 339.8 |
| fbc71c98-13cc-3120-a41f-13f9a9d920f3 | -14.731 | -45.4827 | 2024-09-27 10:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 176.9 |
| b2c0411f-4a39-3a9f-b8b3-0582870cbab6 | -14.9026 | -51.4534 | 2024-09-27 10:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 6834629a-8519-3128-b672-66a383013cbd | -14.903 | -51.4319 | 2024-09-27 10:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 9434bb0e-fa61-3bb6-ba84-96985358e76b | -16.0989 | -51.968 | 2024-09-27 10:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f462a526-5057-3d2d-8114-bf8cb114284c | -14.731 | -45.4827 | 2024-09-27 10:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| c1974991-2949-349b-ae8b-d7ac518e71df | -14.7305 | -45.5061 | 2024-09-27 10:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 285.8 |
| e711e58c-b2ca-36b1-9c88-2c4bb7dc1140 | -16.0989 | -51.968 | 2024-09-27 10:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1b2c6ff2-05e9-3df0-8047-a64995426b1c | -16.0793 | -51.9709 | 2024-09-27 10:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 132.7 |
| e8d7bda9-08c3-31bd-9d73-ed740f35009f | -11.0388 | -51.3713 | 2024-09-27 10:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b1c4cad7-16f9-3afe-bc2c-331c8d3b72ad | -14.731 | -45.4827 | 2024-09-27 10:26:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 98fe24ef-9c37-3057-8444-af26713c430a | -14.7305 | -45.5061 | 2024-09-27 10:26:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| a52f2961-9fc8-3200-b798-97b36977a1dd | -14.903 | -51.4319 | 2024-09-27 10:26:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 56c63730-8d1e-3df1-a920-819686b585f1 | -10.0139 | -53.4464 | 2024-09-27 10:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 607.1 |
| a99c0292-187d-37dc-aeb9-435e58f25e9d | -10.0141 | -53.4258 | 2024-09-27 10:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 313.3 |
| 2cfde28c-7a95-3ac3-8b3f-5e20b559df54 | -10.0327 | -53.4448 | 2024-09-27 10:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1163.0 |


[Clique aqui para ver as próximas entradas](README132.md)
