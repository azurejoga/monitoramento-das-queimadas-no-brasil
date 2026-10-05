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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48c60c35-549a-3805-b406-16e02c8d881f | -9.0947 | -65.73151 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5f03f834-796a-37af-8ef9-f4751f6c3ddc | -2.75126 | -67.59547 | 2026-10-05 17:37:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60fef810-c995-347e-aabd-208aca36b88a | -9.97157 | -65.1178 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a05c6c99-9a5b-3c9b-9d5b-6ece29e14a09 | -9.073 | -66.09506 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 30f6e875-cf49-3e93-98c1-a177d886a17a | -9.13429 | -67.92805 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 996bc2e0-768e-36ab-a99c-04979364cf9a | -9.62355 | -65.37498 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1404cff3-70ec-3851-a111-ac92107f73dc | -9.15359 | -68.26332 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 16693aca-da80-3d39-98f2-8a3ddcd16c79 | -3.1203 | -59.3448 | 2026-10-05 17:37:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 15cbd1ac-41b2-3ee9-baaa-a09a62d60a5e | -1.42422 | -55.09321 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6b4c6de5-7bf8-3eed-ac57-6bb6d93d397d | -8.75656 | -66.9183 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cd75b71b-77d5-30ce-a06f-933f511d0c2d | -9.13271 | -64.38976 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1a85c50-058f-3d50-b89b-a6daaa66fcc0 | -2.95221 | -59.16124 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b5a40930-c018-3c2b-9b37-210d0be250fc | -9.22001 | -66.12763 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1226a5a2-87e9-38ae-b3cb-ceff8a419085 | -10.47484 | -69.57908 | 2026-10-05 17:37:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 16.9 |
| cdeeb6f7-9a81-3dd3-bd2b-0f4297790813 | 0.44244 | -60.52987 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 688f393f-1164-3f74-aa52-efb4c72c6495 | -9.07622 | -66.08571 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 63eb71c2-eb7c-38db-8ded-8869c9b1d629 | -3.63264 | -69.3994 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03301ebc-1795-391d-9619-61a350bf3acb | -8.22499 | -67.34793 | 2026-10-05 17:37:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 950d4d72-8674-3cdf-9d4d-a4adade3aa9d | -8.52904 | -54.58354 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c693c7e5-01fe-3b92-b4ce-b4ed3249f260 | -8.82951 | -67.38763 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 8ddb7f12-83db-3393-94f1-287154131bff | -2.08032 | -56.83793 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef0ddc1d-e13f-3b32-9c3e-20bc2c66dda7 | -9.26445 | -68.37287 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4b8a3e15-bb31-3c00-87b7-15d2b35732a3 | -8.86258 | -62.83134 | 2026-10-05 17:37:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a2365039-cb29-3db8-a5f8-c69c03ea2d39 | 1.86566 | -55.76876 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b983429e-7a79-3898-bd83-8f47851cba7a | 1.81296 | -55.54787 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ba4915df-19d5-3946-964b-ea0fa5d57bbb | -2.12873 | -56.69123 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fec60a54-09bf-334f-9cb5-40f69f17f39a | 4.22352 | -60.70047 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 164d7d79-4c65-3961-adcd-8d4dabfe90dd | -9.96736 | -65.11841 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8f158619-029e-3b70-920d-1ba23150eb0a | -6.5118 | -55.38943 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a9438b51-9b61-3286-9a9e-692b0a3bbb27 | -7.32879 | -55.13755 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f03f45bf-6383-3ce3-8b7f-5ef148e7686b | -7.12088 | -55.72211 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5608482e-e4ff-343f-86da-7115c1384e20 | -10.41724 | -67.97778 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2436130d-2213-3eaa-8ecf-9a7c4a287e1a | 1.99401 | -60.0211 | 2026-10-05 17:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae905281-a508-30c7-a1cb-fb46de7eab65 | -8.80533 | -69.49229 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 261a9003-0637-3961-a178-0b677ad7eed4 | -2.86063 | -60.20232 | 2026-10-05 17:37:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d04ed93a-3588-32dd-99d4-7fa3177f6f7c | -9.15779 | -65.56456 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1d36ca1d-b18c-3509-aa8f-95e2931d3f9f | -9.12116 | -67.83185 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7be1cdd8-0f96-3dfa-bfe8-bf38b048ea0e | -3.75192 | -69.47894 | 2026-10-05 17:37:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 040fee7b-64e8-3ea7-9f36-12df2214c451 | -7.23433 | -55.19777 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8eea2a10-2911-3612-9d7e-0cb0b99241bc | -9.32553 | -72.68485 | 2026-10-05 17:37:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1237d478-3f83-3f01-a5cc-97640c6538fa | 4.22011 | -60.69996 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 411fbaa3-9550-3e72-ba34-97a0dc4b3ebc | -9.04921 | -66.05368 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 88b0af09-6241-3b44-9db5-5a7b5237e931 | 0.3197 | -60.5108 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f9eaed73-f01f-3c39-b034-e3b5cc901756 | -9.50855 | -67.75294 | 2026-10-05 17:37:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9a1af1e6-724c-3f01-b89b-84369bfc9bca | -6.46543 | -55.45446 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 31f028b3-3c1d-335b-94d3-53d31e782f58 | -0.37334 | -52.06428 | 2026-10-05 17:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f403e294-8d25-3384-a0ad-18b04cea6e95 | 1.32093 | -60.71366 | 2026-10-05 17:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e3b3a515-3c16-3bb5-b6d0-dc178f776e0b | -9.52398 | -67.75389 | 2026-10-05 17:37:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8ad68da-08d6-3af5-b925-07d66ed4629d | 2.18655 | -55.9393 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cd9ae588-be07-393a-8828-cf50635e748f | -10.44353 | -67.89565 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 21.9 |
| bf7418b1-3645-3985-9018-200f21040bcb | -4.05989 | -69.56671 | 2026-10-05 17:37:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eaf64443-0be5-350f-aec6-f5193230ee84 | -9.98489 | -67.89631 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 584e067c-435c-3c6c-b21f-5b73f7201d94 | -8.52451 | -54.60638 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 5c25deb7-e6cc-310e-849f-af92b6a6bd4a | -9.34813 | -68.27552 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 197d60f0-40aa-3b5b-a235-485b03978f59 | -0.99348 | -60.37479 | 2026-10-05 17:37:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 937f6797-930b-348d-bcf4-fd90ebcbfa8e | 2.25725 | -50.82033 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fe69746b-ca01-3469-86c9-c46387893c87 | -9.10785 | -65.35538 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 34aeefb4-6158-3175-aa71-cb7530a82266 | 2.51572 | -60.99762 | 2026-10-05 17:37:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d4a84d6f-e4f0-3077-a980-78b2031adba7 | 1.87778 | -55.74866 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8faf3a7a-70f3-3f40-902c-e4f610b19a89 | 3.57002 | -61.342 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 418c2980-578e-392d-aeef-dd09556a6e3d | -0.73892 | -57.98236 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4dccca3e-688e-35c3-bbf2-071f133e64be | -8.74202 | -66.5746 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 861b8c73-abdb-3f7f-b468-d59a591458c9 | 3.56227 | -61.34806 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54c61389-01d3-34f7-9a6b-c8bd4cf6f96c | 4.05222 | -59.99025 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a5fd49e1-8c3c-34e1-a4df-8abc9b3d7868 | -9.13418 | -67.93392 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf87f441-2120-3a8f-b910-9f0266014472 | -9.91468 | -67.81868 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 21e511c0-c330-3b95-b9af-26530dc3de19 | -2.52334 | -57.81155 | 2026-10-05 17:37:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8f726782-a01e-33b4-a173-84936be590e4 | -9.21721 | -66.13048 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89667998-6eac-3512-ba5a-25446ed4e556 | -10.64628 | -69.15619 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2ad3c7c2-c8fe-32dd-ac78-dd53dfbf6d71 | -9.13127 | -64.3795 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c57f8dc7-bf2c-329b-a4eb-a3c9ca862e95 | 1.58578 | -55.98071 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9cd4942c-8a5e-319f-aef1-96e6fe2ce5cc | 0.88234 | -59.59492 | 2026-10-05 17:37:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e8aab17d-aaeb-30ff-9983-19e8c97c6a6e | -9.13565 | -68.24686 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 31869436-e229-352d-83ff-5374c472eb5e | -9.05186 | -65.45085 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 982d27fa-c1ad-3a38-afac-726e7969dd77 | -8.66157 | -54.57503 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4e1240d4-6d1a-32bd-b1c0-526d7d22f746 | -9.13037 | -67.74689 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 25389659-6cc4-3034-bdea-edf846023c94 | -1.59982 | -57.57358 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6eb4d79c-d2ad-3ef5-ac53-cce5dab1d163 | -9.01729 | -65.69463 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9803ca52-11c0-314b-8a29-534e841ae6b0 | -9.13112 | -67.7526 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| f1162540-70c1-3fe3-983a-07e7ff7e2c4e | -9.40345 | -65.89027 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 65aa49d6-e5d1-3a0a-aba5-711ee05b2011 | -9.10754 | -67.69538 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 21ad3ecb-40a5-333e-b5f5-244424d1ded1 | -9.47279 | -67.4856 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 143e7936-165f-3790-b183-f54c7416170f | -9.34375 | -64.7108 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e7b43df5-fe12-3460-8f02-ab8c3536838a | -2.10435 | -64.06795 | 2026-10-05 17:37:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 92530518-5814-325f-97d3-b88f5c19cd2a | 4.05189 | -59.98661 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 92a1ffdd-555d-3368-a2ce-525e9bf5e4c4 | 3.50023 | -51.48879 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 70099f59-e403-3af6-8d46-0fd7830ec1c2 | 1.46081 | -55.6505 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d8f801f0-20e7-3f97-82ab-373b7788fa9e | -10.42278 | -67.98024 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1b9e1e83-d569-3658-8fa0-8425ab8414f8 | -8.8559 | -62.86234 | 2026-10-05 17:37:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b5b7aefc-2c21-3a3d-b724-758c3eebd33a | -1.67493 | -55.75323 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 93fbca78-8716-33dd-9c41-6169ad42462c | -9.48111 | -64.33303 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7614f755-4b04-3e9a-8274-88297d870f6a | 3.56668 | -61.34151 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d8726f8-f05d-34ae-9544-034b1280698d | -1.2543 | -55.77554 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2408a36-0cfe-3d36-97de-2cc28aba61d7 | -2.06219 | -56.88345 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e2f60642-6625-3a9a-ae0e-e9efd778778b | -1.90336 | -56.60963 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 837eb9eb-4335-39fc-b0b9-f10ec9d508e5 | -8.93715 | -67.34583 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| adbcbbb0-a985-3e87-bf64-b2c95e65c145 | -3.41677 | -64.55305 | 2026-10-05 17:37:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fff1448-a6cd-39c5-8881-88a6dafeffaf | -8.89002 | -68.534 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 78fe6f50-77a0-33ef-abe5-f2284f4c6013 | -2.76396 | -57.67344 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 144.6 |
| d707fa8c-dd60-39a9-886a-fa9c56be2fe6 | -8.47539 | -54.91578 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README152.md)
