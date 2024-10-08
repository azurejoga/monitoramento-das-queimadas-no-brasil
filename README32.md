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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dc61d24-acc7-3b5f-b46c-f62068813045 | -20.4144 | -43.9356 | 2024-10-08 03:26:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 78014a61-9ccd-3fbc-b1b2-4e21bdb5c0c8 | -22.5767 | -46.6786 | 2024-10-08 03:27:10 | GOES-16 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| fa052923-1c42-3fcf-a691-bc0d0fcc8373 | -5.5716 | -44.8927 | 2024-10-08 03:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0e0248c4-ae5d-34fa-9488-bc69a1b8fa22 | -5.5718 | -44.87 | 2024-10-08 03:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 29da6547-e382-3070-8971-f81d4984991a | -9.445 | -66.7289 | 2024-10-08 03:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 85937352-f2c5-365b-87f5-915cbf52800e | -10.6256 | -55.9154 | 2024-10-08 03:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 7e6afbd5-50f3-34ab-9cb2-f91b8ca5616a | -10.8568 | -63.8988 | 2024-10-08 03:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 38bdbc4a-4c3c-3c5e-b0d1-336ef01b2ba4 | -10.8754 | -63.9169 | 2024-10-08 03:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7851a0e3-7f61-35f6-89a8-6b7851851add | -10.8755 | -63.8979 | 2024-10-08 03:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 444cfd88-7b57-370c-86d1-3254e3ef4c19 | -10.8941 | -63.916 | 2024-10-08 03:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| dce9a21a-1d49-36a1-b415-fd620debe896 | -11.3093 | -50.9826 | 2024-10-08 03:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| d57e810d-6083-3921-962d-384feef6de58 | -11.3081 | -51.0676 | 2024-10-08 03:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 56d8da90-d878-3087-8d97-12395d6b92da | -11.3078 | -51.0889 | 2024-10-08 03:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4335878b-7e3a-3256-b965-166aa8b9d10a | -11.5233 | -65.137 | 2024-10-08 03:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 9e31f665-a9f0-3abf-b639-96b5d9d81e54 | -12.5907 | -53.0732 | 2024-10-08 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e686ae50-7712-3840-b4f9-4e3c787f64d2 | -12.572 | -53.0544 | 2024-10-08 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 1060eaa6-c4e3-3af8-9f50-16dc97fc37ed | -12.5717 | -53.0753 | 2024-10-08 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 768e7d08-ce80-385a-b6bc-9b0de017e39f | -16.5897 | -46.4979 | 2024-10-08 03:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 53d522ff-7404-30e5-b6a2-0137d8d817af | -16.5902 | -46.4746 | 2024-10-08 03:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| cfbc5c66-2dc3-3331-9cf8-74cabb1d1343 | -16.9214 | -57.4676 | 2024-10-08 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 52996d5c-7d74-306d-a8f7-3600d87e2afe | -16.9211 | -57.4881 | 2024-10-08 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 4dcc9bd7-341c-3a4a-add9-acacef70c518 | -16.8551 | -56.7169 | 2024-10-08 03:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 51ad4db4-9c78-38cd-96fc-6a35b7281d18 | -16.8048 | -57.4197 | 2024-10-08 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 8ae2dcad-2da2-3af8-8e25-1817e3e3cbc6 | -16.8045 | -57.4402 | 2024-10-08 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 89ba7188-f924-3adb-be86-0bc49786af2b | -16.9407 | -57.4859 | 2024-10-08 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.5 |
| d293516e-f255-309b-af67-815c5b67e76e | -16.9924 | -56.7003 | 2024-10-08 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 58c28ccd-72f7-305b-b3d9-0f7e23ed9afb | -17.0123 | -56.6773 | 2024-10-08 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 32c41948-5c65-35d5-8d02-af6895d7d30f | -16.9927 | -56.6797 | 2024-10-08 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| a34cfc4d-2607-36e1-b4f3-98074fb1ad82 | -17.1274 | -56.828 | 2024-10-08 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 4c0529fa-20a9-34c9-9bf0-2b80233b84c5 | -17.1178 | -57.4244 | 2024-10-08 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 4ac45dbe-a3ad-30c8-acc8-dfe1a68ad0f8 | -17.1175 | -57.4449 | 2024-10-08 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| cca9206e-4630-32d3-a36b-0fb3e8c04901 | -17.1074 | -56.851 | 2024-10-08 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 3052abe3-6619-3ced-a4e9-3cd420f53496 | -17.0992 | -57.3651 | 2024-10-08 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| af416506-6502-31f3-b5ca-727c9f6e1bb3 | -17.0982 | -57.4267 | 2024-10-08 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| f4a7d590-e6d8-3b94-8849-1881f5268824 | -17.1471 | -56.8256 | 2024-10-08 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.3 |
| 4356fdf6-5844-3387-b648-b84a31e9d8a3 | -17.1375 | -57.4221 | 2024-10-08 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 889ea24d-12e5-3aa9-92f9-13800dd25d3d | -18.6192 | -57.2603 | 2024-10-08 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 2678cf61-855a-31bb-896c-84c3055f0313 | -18.6195 | -57.2396 | 2024-10-08 03:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 60ee1c99-baf3-3b68-969b-4a01f97be4ae | -20.3938 | -43.9412 | 2024-10-08 03:36:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 155.1 |
| fc0e803a-4efa-3b6f-9557-79d47fae8196 | -20.4144 | -43.9356 | 2024-10-08 03:36:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.0 |
| c0bda535-611f-3ffd-a6f7-5e0876b6e9fe | -3.29065 | -47.1286 | 2024-10-08 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 657db79c-55be-3d2b-98c3-e6e0d02d3faa | -3.28669 | -47.13169 | 2024-10-08 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ea29d9ed-4b09-3723-a3d6-5007068164a1 | -3.28401 | -47.12726 | 2024-10-08 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67951320-5d2e-3363-8c2c-86c63ac5ae92 | -4.3187 | -47.70866 | 2024-10-08 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a2262be-49f4-3641-bcb9-c433a5ba1f1c | -4.31711 | -47.71136 | 2024-10-08 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d28e5a3-58b4-35db-adc7-528496d553d5 | -4.31202 | -47.70681 | 2024-10-08 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7f06a35-6ba6-353d-b352-5b0a5ad72adc | -4.31039 | -47.70963 | 2024-10-08 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f527b5a-1566-3181-982f-33585793d919 | -4.27267 | -46.28709 | 2024-10-08 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 102a3012-dc02-33ae-8b20-68fd8c05edc4 | -4.2685 | -46.28828 | 2024-10-08 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e18453c5-6b33-3097-be6f-e329b89f78f3 | -4.26643 | -46.28588 | 2024-10-08 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4affde53-51ae-3f58-8053-ee20ae9499dd | -3.93592 | -46.44971 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2e40b119-733e-3241-b9a9-e85aa4839ec4 | -3.93498 | -46.45508 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ffd52ba-551b-35d5-b104-6bc1fbb97444 | -3.93411 | -46.44823 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 000b5e8a-7e79-3ccc-8374-1bd8e117abc2 | -3.93324 | -46.45344 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c22bd90c-def7-3b1c-93bf-98cabc87b0ef | -3.93047 | -46.44345 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 227fe0fd-f7d4-3530-b1ce-01a028dbc90b | -3.92958 | -46.44854 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5a60624f-ec5c-35d7-97d6-3960cc16a776 | -3.92862 | -46.44201 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 180b759f-a57c-34c3-960c-8b0d253ed982 | -3.92777 | -46.44708 | 2024-10-08 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 25d29d64-37a3-3ea5-bf4f-3a32934b34ff | -6.13272 | -47.21549 | 2024-10-08 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27a2baae-6362-39b3-8269-9c06bd3927ec | -6.13234 | -47.21425 | 2024-10-08 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 91acf5b3-59ae-3025-be40-0e4a3961a485 | -6.13171 | -47.22095 | 2024-10-08 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 591bc27d-d9c1-38a5-925e-de2fc54927a5 | -6.13137 | -47.21972 | 2024-10-08 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 61f3b2a6-f47a-341f-8200-17856b09f3f9 | -6.05027 | -46.60365 | 2024-10-08 03:40:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a2c14ce-fd97-3078-a76a-73d921ced055 | -6.04935 | -46.60872 | 2024-10-08 03:40:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28a7380b-0a53-3891-8a9a-931ea20a4a02 | -7.89211 | -47.72637 | 2024-10-08 03:40:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a3dadad-33b6-3612-9c00-5577505270a5 | -7.5989 | -47.10821 | 2024-10-08 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17ffd9d1-226b-3870-833e-ec4886f21b9d | -6.66538 | -47.11455 | 2024-10-08 03:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ed43e90-5ead-3b1a-88e0-7ea5f2b86654 | -6.66183 | -47.11179 | 2024-10-08 03:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ccedb5c-b69b-377b-8b04-6cbb0cfb46d5 | -6.66085 | -47.11699 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4be94129-086f-3ce0-9cb8-d2955055e2f2 | -6.65902 | -47.11347 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e6abf70-2762-337a-a2a7-df1b64bca302 | -3.45921 | -47.66854 | 2024-10-08 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9329909a-b552-3e8f-87cb-fd7234917856 | -3.4592 | -47.66862 | 2024-10-08 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 869a4f6a-d22d-3d5d-ae18-ceeadced8881 | -4.39369 | -48.69925 | 2024-10-08 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1035a83c-9dcb-392a-868b-d325e32dffd8 | -4.38881 | -48.69692 | 2024-10-08 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5aca2b31-5c4b-317b-bd77-9fe37ab3e748 | -4.38649 | -48.69803 | 2024-10-08 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f781275-4f87-30c5-bced-6cdd84918097 | -4.36165 | -48.21899 | 2024-10-08 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 945add67-79e2-3d57-a202-64cc8a99aa77 | -4.35683 | -48.21613 | 2024-10-08 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69ec7607-d3a6-35c8-8449-c40dbd365b9b | -4.3557 | -48.2226 | 2024-10-08 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bbe89f0-70dd-382f-bc47-d0e37956379a | -4.35362 | -48.22347 | 2024-10-08 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2171ab7-2938-3160-8e21-c3115e3d264a | -4.09314 | -48.26037 | 2024-10-08 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23c4ca8f-36c8-3553-b411-e20c6344c8b9 | -4.09192 | -48.2673 | 2024-10-08 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6e1b7a8-fe1c-3b69-85f9-f49d3d2d21a0 | -9.35403 | -40.237 | 2024-10-08 03:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab569f18-fbb7-3932-8286-296dfb85868e | -7.98716 | -41.0694 | 2024-10-08 03:40:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4c8ade1-ddbb-316d-9dd2-bc7d95debac6 | -7.98649 | -41.0733 | 2024-10-08 03:40:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4dac868b-576b-3efd-9d2e-5b76f2319cba | -7.8278 | -42.22194 | 2024-10-08 03:40:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 26263e97-c9fe-3227-84e4-b4942cb2b50a | -8.80342 | -41.03954 | 2024-10-08 03:40:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 257c41b2-5f25-3634-9695-f38ccd501200 | -8.42079 | -41.95375 | 2024-10-08 03:40:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0f4b3bf0-30d0-3c04-b416-cfc0410fdb43 | -7.92359 | -42.45721 | 2024-10-08 03:40:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1ea2ea0d-3f8a-33f8-8ba5-bf86ea03a26a | -7.78414 | -43.09398 | 2024-10-08 03:40:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 486d05df-e593-3125-98b1-e6fde887bc7d | -7.65812 | -42.49306 | 2024-10-08 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fda87382-0a0a-31c3-8db7-1f87694ed54d | -6.82466 | -38.34444 | 2024-10-08 03:40:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd0c6654-503a-36c2-ac1a-1838ef71fa50 | -6.9385 | -38.33643 | 2024-10-08 03:40:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d711a84-fbec-3781-85bb-015d1db85941 | -7.33861 | -39.1557 | 2024-10-08 03:40:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b836cd12-f6e4-37c5-8ec9-40fe395abb5f | -4.81484 | -42.75738 | 2024-10-08 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e369a553-0fef-3b88-9c8f-23f1bc621d15 | -4.80991 | -42.75654 | 2024-10-08 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b565d72-45cc-3551-879c-6d5f99c02e9e | -4.80499 | -42.75566 | 2024-10-08 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a121e3c4-9ee5-3d0c-83c4-54a32f0fd270 | -4.45147 | -42.90067 | 2024-10-08 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 191a2b54-e807-39d7-9ecf-e4784ac7cab5 | -4.45098 | -42.90352 | 2024-10-08 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0c59d28-9952-3086-9fcc-c6d02126c133 | -4.44598 | -42.9027 | 2024-10-08 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7faec2f-cebb-3e17-9662-d39457429d94 | -4.44549 | -42.90555 | 2024-10-08 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README33.md)
