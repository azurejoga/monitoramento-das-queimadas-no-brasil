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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a45751b4-0d27-3047-93be-f19bd964e466 | -3.839 | -55.7997 | 2026-10-10 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 4a2a083b-007e-3dde-b6a0-04a4b7277242 | -6.9319 | -59.2412 | 2026-10-10 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 20557a99-7dbc-3e3a-842c-c463a89d191a | -5.7378 | -45.1307 | 2026-10-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 881cefef-011c-39be-a388-81ee2b68464b | -9.6364 | -48.8845 | 2026-10-10 00:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| ef2e1db3-6ca3-3ecc-9f70-6009a8ae7373 | -3.3139 | -59.4089 | 2026-10-10 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0b75a63c-37c3-393a-8fba-8387edd122fc | -11.0937 | -44.0975 | 2026-10-10 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 710d8c42-8fa9-3c17-a6df-7d9ebaa6f86d | -7.5162 | -45.3024 | 2026-10-10 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3fbbad21-90d6-396e-9ab7-5b2d23c14cc6 | -14.453 | -43.9598 | 2026-10-10 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 248.3 |
| f4be08fc-fca3-39d1-afa1-2a348e691994 | -4.3582 | -54.75 | 2026-10-10 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c213b982-d25f-3fa5-9a2f-a200c0ca3e4a | -7.5161 | -55.0044 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 8c15feb8-f674-3087-9714-404e574c4f55 | -6.881 | -45.0183 | 2026-10-10 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6693abbb-f17f-36ce-af32-bde5b36e5040 | -3.5491 | -54.7351 | 2026-10-10 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 00a84bf3-c95f-3982-8c8b-0c041f0cdd29 | -8.9778 | -45.8797 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9fa8183e-31d5-3b7a-9740-c483c742c1d2 | -22.0903 | -48.9972 | 2026-10-10 00:30:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 550b439d-5f61-3908-9a69-29d92c21853e | -3.8573 | -55.7992 | 2026-10-10 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1c775e1c-e90f-34fb-979a-b5742cbacb3d | -7.4977 | -54.9854 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f3b7cbff-082b-384f-8822-648d7b1fff92 | -6.4903 | -62.8554 | 2026-10-10 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7a8be829-9202-3971-8cb0-0f6e42d994f5 | -3.5676 | -54.6946 | 2026-10-10 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7fd4e8d9-5d29-3c1f-9792-c44ad1d3835a | -12.2154 | -57.1287 | 2026-10-10 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4d9ed390-3a45-3c44-b25c-96c6ddca17d9 | -11.0745 | -44.1003 | 2026-10-10 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 5ead4bdd-d6d3-34cc-a943-f657e41c79a1 | -4.4025 | -49.7774 | 2026-10-10 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 23b94c79-443a-3579-82a3-ffcca79abc3d | -7.5347 | -45.3233 | 2026-10-10 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| dba762c4-ab06-3abd-92a0-48e80babd122 | -9.0156 | -45.8756 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 43cf49f3-c36b-3a9a-a66d-d679810b0374 | -7.1825 | -52.6283 | 2026-10-10 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| c791744b-008e-3003-a12f-c63e8bc555db | -7.1823 | -52.6489 | 2026-10-10 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7a1b62df-de4f-38f7-98b0-3d86dd901ee8 | -6.478 | -55.0606 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3a245132-4c0d-322c-82a0-c37192a09fa9 | -14.4535 | -43.9359 | 2026-10-10 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 148.1 |
| e43a2520-bbff-305e-9846-be33460acda9 | -3.7311 | -60.6018 | 2026-10-10 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 1d375dc1-578d-30b1-82c0-6e82f11ce97e | -7.9231 | -63.6935 | 2026-10-10 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 23c35b3e-df6a-3424-be7a-246350d6657e | -3.6397 | -60.6226 | 2026-10-10 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6e71e52c-b4e6-35de-a627-66da20c27566 | -22.0701 | -48.9788 | 2026-10-10 00:40:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 2b0b4b00-443b-347b-b2b6-1ac5948111e3 | -6.9318 | -59.2605 | 2026-10-10 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 62e8ad44-9245-3b2c-9502-219e90f78c83 | -3.7494 | -60.6014 | 2026-10-10 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 190.7 |
| ab264ac1-bc97-3a9b-afb3-66d43f3286e4 | -12.3066 | -63.3701 | 2026-10-10 00:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 6da1a8d8-15cf-3282-9034-7f2bf82e648f | -12.1017 | -57.1383 | 2026-10-10 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| aeb6d6c0-9451-3b77-994c-b270bfe6fe1c | -12.2877 | -63.3711 | 2026-10-10 00:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| bfa57912-c17f-3121-b646-c51227273962 | -3.5863 | -54.6142 | 2026-10-10 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 24e6f2a6-f73c-3ef9-b51a-2c961494dc7a | -13.3666 | -43.8979 | 2026-10-10 00:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| ada3224b-b481-3d70-8eef-ba0ca18617de | -9.0156 | -45.8756 | 2026-10-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c5c03c21-34a2-3fc7-b692-7eed6b0bfdc0 | -3.8573 | -55.7992 | 2026-10-10 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4a08f365-2f13-32b6-a1a8-71fe58031dd6 | -7.0228 | -47.661 | 2026-10-10 00:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 1c658095-e7a5-36a9-bdc4-d1e847d06a4e | -3.6048 | -54.5936 | 2026-10-10 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 2f368621-be94-39ee-84f2-30c7c3eeecff | -11.0937 | -44.0975 | 2026-10-10 00:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 7ec63504-c2fe-325f-82d4-e6d924eacdec | -8.9778 | -45.8797 | 2026-10-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6ac3273c-4b10-3306-88b5-c6124b0da8de | -3.2737 | -54.6826 | 2026-10-10 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| af20ee79-d6db-3c16-8a4a-c13f6ebddf0a | -9.2976 | -47.3871 | 2026-10-10 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bb8612ff-22d8-3200-b9ae-cece052554c5 | -3.7311 | -60.6018 | 2026-10-10 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 626061f9-4300-33d1-901d-b5dabb2848b9 | -3.5307 | -54.7356 | 2026-10-10 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d52c47d4-839a-3e83-b7b6-1b71baae171e | -3.2203 | -49.4417 | 2026-10-10 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 58970827-944c-3068-bf1b-c3992fbe9a62 | -7.9084 | -54.7396 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| a95fea4b-c2d4-3b0e-a62d-9caede253892 | -6.4411 | -55.0424 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3b4389f7-59c0-3544-afbe-704f1b77b2f9 | -3.7495 | -60.5824 | 2026-10-10 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 546f2255-ab21-32fc-917f-286910ff93d2 | -3.0375 | -53.8865 | 2026-10-10 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5144c4c4-763b-3aa6-ae9e-2b777a9dd4f4 | -9.809 | -64.4526 | 2026-10-10 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 4d431adc-ce4d-30f4-ab28-d70ab2f802bd | -5.7117 | -53.4862 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 2eadd21c-5246-315a-91e0-974f6c8d82b6 | -3.2736 | -54.7025 | 2026-10-10 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 03177f05-e3de-369a-b1e8-c5e7b83db7cd | -22.0909 | -48.9738 | 2026-10-10 00:40:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 104.0 |
| bf9e6115-27cd-3e1c-a78b-96518f5df732 | -14.4726 | -43.956 | 2026-10-10 00:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b169e3a3-8a5c-3505-8062-4727de958875 | -7.9272 | -54.7182 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c0cffda4-e5db-36ee-944a-08122536619f | -10.6013 | -60.4669 | 2026-10-10 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 550b4a94-1fb3-36b4-ab6b-f5a60da8e884 | -3.8391 | -55.7799 | 2026-10-10 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 0d70b50f-aee7-359e-818a-38779e594f5c | -11.0745 | -44.1003 | 2026-10-10 00:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8640bb9c-ec37-3baf-80b9-ddaf4ca9a24e | -10.5824 | -60.4874 | 2026-10-10 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 754bba79-f382-3fb7-b8a8-745af62525dc | -3.839 | -55.7997 | 2026-10-10 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| be8e4cb2-cae8-36a6-8e61-490525cd2a6e | -2.9267 | -54.0702 | 2026-10-10 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 43b238c2-6852-3072-9352-37fdd26dec2a | -3.2553 | -54.683 | 2026-10-10 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0bd9fb44-cf88-35b0-94cd-19a22c3b263d | -14.453 | -43.9598 | 2026-10-10 00:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 190.3 |
| ff1c47f8-7d0d-3e81-944a-5b2e7e4ba201 | -22.0694 | -49.0021 | 2026-10-10 00:40:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4eac338f-e0d1-30b1-9b43-cdf39d66edd7 | -7.9231 | -63.6935 | 2026-10-10 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 89544ba0-f382-35db-ac63-84489ca58835 | -3.6047 | -54.6136 | 2026-10-10 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| e9ced69e-43c4-3d6d-9856-61f29c5e49dd | -3.5491 | -54.7351 | 2026-10-10 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7c786f3f-3b42-3fc3-89ab-8aede4ab7f0b | -8.9775 | -45.9023 | 2026-10-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 92760d61-4fe4-30cf-be4a-cb1402b283ed | -7.2011 | -52.6272 | 2026-10-10 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| cef8e3cf-a3b4-32f2-8b4f-56de87f0ee5a | -9.3805 | -64.6567 | 2026-10-10 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ff155680-02ef-3094-adf5-692ac19ee56e | -14.4535 | -43.9359 | 2026-10-10 00:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 157.8 |
| b7e02ac3-d2c7-3cc7-b235-57ddeb9866cb | -3.9912 | -59.356 | 2026-10-10 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 22db5ff9-1c6b-3da0-93d0-8e06abb60dcb | -6.633 | -59.9457 | 2026-10-10 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 07f3e6ec-7a46-3a46-aa23-4c63ff35d9e6 | -7.535 | -45.3006 | 2026-10-10 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 9a14c12c-5824-3d0b-9dde-c02b358a2cb3 | -10.9174 | -45.5088 | 2026-10-10 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1f4e4423-dda9-321f-b0da-15f06fcb332e | -10.917 | -45.5317 | 2026-10-10 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| bdc1ccb8-e28b-3595-adec-c454697b4c6a | -3.7312 | -60.5828 | 2026-10-10 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 852b9c66-13b4-30d8-aebd-71803f908fff | -3.2577 | -54.0217 | 2026-10-10 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 93d2ed47-5d2e-3205-bb56-16ad9e45ee6c | -4.421 | -49.7766 | 2026-10-10 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a1788064-b18b-363e-993f-2142b74850ab | -11.0741 | -44.1237 | 2026-10-10 00:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b31889fe-126a-35b7-97cf-54341c0ff564 | -12.2152 | -57.1488 | 2026-10-10 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 329122ce-f870-31bc-9079-546bab752e5c | -5.7565 | -45.1293 | 2026-10-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 67be99a6-8f26-3004-bb52-a2c27bc55f5c | -13.3865 | -43.8708 | 2026-10-10 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 26771302-c99c-3252-ad1e-9f56932a43ef | -7.5162 | -45.3024 | 2026-10-10 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 0a739c47-ed8c-34fc-8620-4f9d009f7885 | -7.5162 | -54.9844 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8bf0e582-4faa-35c9-9859-414fd7f37ade | -3.5864 | -54.5942 | 2026-10-10 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 2efdd3fb-5873-32e3-b6f0-fac7e4d5ffce | -7.923 | -63.7123 | 2026-10-10 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 70836594-ccb4-3aba-bdc4-5c63bb14d0b8 | -7.5159 | -45.3251 | 2026-10-10 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 825cdd37-ee43-37d9-ba20-650dc759606e | -5.2303 | -50.6856 | 2026-10-10 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9e8c6b9f-804c-32f5-8582-f480207bd3c0 | -3.1114 | -53.7839 | 2026-10-10 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 029bf341-cebb-35f0-bdce-eddc21f998d4 | -7.2009 | -52.6477 | 2026-10-10 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 903f23df-ef54-3ce8-82f3-4c76b8eecb78 | -7.4977 | -54.9854 | 2026-10-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| cb1bd544-e42e-3105-9197-e16c1a860ca5 | -12.2343 | -57.1271 | 2026-10-10 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 04907e1d-9ae2-3675-9a52-fee7dbdd6c27 | -13.386 | -43.8945 | 2026-10-10 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 5c3d0b97-25d8-3405-8c55-3f5fb7283606 | -3.3128 | -54.0202 | 2026-10-10 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 34ba4e04-fea6-3ac9-92f6-68e6d33ccc4a | -10.6012 | -60.4863 | 2026-10-10 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 162.6 |


[Clique aqui para ver as próximas entradas](README13.md)
