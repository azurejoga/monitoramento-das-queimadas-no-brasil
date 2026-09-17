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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a9d646e-989b-3827-a5cc-8011ec9e3c08 | -4.5587 | -42.9523 | 2026-09-17 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 4443d391-6613-3fc3-be2e-114f621ce2be | -9.112 | -45.7294 | 2026-09-17 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 237.9 |
| 6dcbbd21-a139-381e-9403-0c1e393b7082 | -9.5251 | -45.9317 | 2026-09-17 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 93e0ce31-16ab-3f58-a273-03f153b04be1 | -5.6285 | -44.7977 | 2026-09-17 02:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 65c08b75-0406-3efb-9def-53d707ce831d | -6.3656 | -58.2966 | 2026-09-17 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e1c4ec30-587c-35d3-84c4-375b0c3f83c6 | -3.4757 | -54.7171 | 2026-09-17 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 6f13341d-2f6c-3854-89cb-d4dfd0826c7e | -9.9699 | -45.3108 | 2026-09-17 02:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 220c87e0-ca7a-31b6-b5a1-e9eec265b3ec | -3.4757 | -54.6972 | 2026-09-17 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a15b40c9-e33d-3452-8f41-48283fbfaecc | -9.6091 | -45.3544 | 2026-09-17 02:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 41c0130a-cc71-3724-8363-05e7561aa413 | -2.6965 | -57.6278 | 2026-09-17 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 28527412-5cb9-3172-8e0b-a90edce5f71c | -8.6188 | -44.4819 | 2026-09-17 02:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e5ba778a-c7b1-3f12-8266-4ddf14474ff3 | -5.7754 | -45.1053 | 2026-09-17 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 401.3 |
| 6f8c99be-c2e9-3296-9832-0a30cc945938 | -8.4983 | -57.6271 | 2026-09-17 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 055c1cfc-cb1b-36f0-ac0e-1741b19b6b12 | -8.4982 | -57.6468 | 2026-09-17 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1a1786ef-d27a-31f9-9850-a2bece2db28f | -5.7567 | -45.1067 | 2026-09-17 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 890d8999-520d-3976-96c8-476e1cdd6035 | -5.7756 | -45.0826 | 2026-09-17 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c9372c4c-4a15-383d-99e6-44167fc65911 | -3.4757 | -54.7171 | 2026-09-17 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 587f942e-00ce-3088-8989-8a42e3886b9b | -5.647 | -44.8192 | 2026-09-17 02:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 98410dd1-e606-3402-bafd-296855daeee1 | -6.3656 | -58.2966 | 2026-09-17 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a4105038-ad01-3f76-8839-d658930e8503 | -2.9582 | -50.3149 | 2026-09-17 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4ecfcdcd-fb30-3ed3-a352-a8b324cf4add | -8.4796 | -57.6478 | 2026-09-17 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0e2eb91c-a953-365b-8a24-e94ae1f9cbe1 | -5.7752 | -45.128 | 2026-09-17 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 5113c7e4-9eb5-3ec7-bfc1-7165659f30cb | -9.1123 | -45.7067 | 2026-09-17 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 1cde08c8-2e21-38fa-99aa-096eeab73154 | -10.8343 | -54.0933 | 2026-09-17 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8e0626b2-924f-3d1b-ae1f-b411a8618a05 | -4.5587 | -42.9523 | 2026-09-17 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 98286e34-ae04-33ca-bae5-24485ae80d50 | -5.6285 | -44.7977 | 2026-09-17 02:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| fd8b6eab-6fe9-331d-b04d-2d7a38de53cf | -5.6472 | -44.7964 | 2026-09-17 02:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 9fe1e12b-a983-355a-9e3e-e5d1276a096c | -2.9581 | -50.3359 | 2026-09-17 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 67cf32c4-4193-3bae-afe8-e1df70669c9a | -9.112 | -45.7294 | 2026-09-17 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 0730b3c0-64bc-39a8-920f-da38db32bbf2 | -2.6966 | -57.6084 | 2026-09-17 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5284a847-4c4f-3e55-86e9-d73437927342 | -8.4797 | -57.6282 | 2026-09-17 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 8ba60cef-d69f-3bf2-8c4d-ac4be31cedc8 | -5.647 | -44.8192 | 2026-09-17 02:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e2ba2889-327f-33a2-938d-bc1545c9c7fe | -9.0931 | -45.7314 | 2026-09-17 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 485dd29d-3a1d-3ab8-bdff-08a34d73b548 | -3.4757 | -54.7171 | 2026-09-17 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 1f77a64b-78be-3c2b-83f3-40d5c073fec0 | -2.6966 | -57.6084 | 2026-09-17 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ed6950c0-1f44-3b5f-b412-aa3d88a723b2 | -9.112 | -45.7294 | 2026-09-17 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 165.9 |
| b5bec76c-3464-3760-81b6-e3e027fe80cc | -3.4757 | -54.6972 | 2026-09-17 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9be10ef9-9472-3381-a3ce-1d6395ce2aec | -12.491 | -50.8259 | 2026-09-17 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| e543685d-4297-30ed-98a1-710637b57b9c | -5.7567 | -45.1067 | 2026-09-17 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| e15cb921-348e-3392-9b98-d8aa65a696df | -4.5589 | -42.9289 | 2026-09-17 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 47013bab-7877-351d-9fb8-b4784a633326 | -2.9582 | -50.3149 | 2026-09-17 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 232990eb-5f76-3443-9ee2-9d39c6ca2f66 | -5.6285 | -44.7977 | 2026-09-17 02:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 0f717c09-1e72-3178-9f53-974edbe38c72 | -9.6091 | -45.3544 | 2026-09-17 02:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b8363346-29d7-36cd-a39a-db9ae54e24c8 | -9.1123 | -45.7067 | 2026-09-17 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 32bb1355-94d5-33ae-ba52-c1c9d69428c8 | -5.7754 | -45.1053 | 2026-09-17 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 310.5 |
| d1fe6e3a-8862-3c41-82b4-13e45c568b1f | -9.628 | -45.3521 | 2026-09-17 02:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| d4b5e97d-6a92-31e9-af3a-9c913269fbae | -9.131 | -45.7273 | 2026-09-17 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d6c8acfc-55f9-37c8-b601-bf4f94efd0ff | -12.4725 | -50.7853 | 2026-09-17 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 14e81bec-dedf-3689-b580-75ede2fde844 | -3.494 | -54.7166 | 2026-09-17 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a834ae23-4759-39a8-88fa-4074315b96e5 | -4.5587 | -42.9523 | 2026-09-17 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 46ed7748-69f8-3932-94e5-333205e1d94b | -2.6965 | -57.6278 | 2026-09-17 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7aef5c38-63fa-3558-a8cb-926f66b751aa | -2.9581 | -50.3359 | 2026-09-17 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 7e88ef66-4bce-3bf8-b19b-d02dd00b687e | -12.4906 | -50.8473 | 2026-09-17 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| daad073e-9087-3aab-aea8-9cacba5da1d1 | -5.7756 | -45.0826 | 2026-09-17 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 79b52e36-e00e-3f4f-a7cd-63c6915fc6c5 | -9.9699 | -45.3108 | 2026-09-17 02:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 164ef515-39fb-3802-8b39-303d44a3f190 | -5.7752 | -45.128 | 2026-09-17 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f36900b3-0175-3d89-9976-120983b726f3 | -5.6472 | -44.7964 | 2026-09-17 02:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| db8f4981-f4a5-3822-99fb-416590483132 | -12.5097 | -50.845 | 2026-09-17 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 4d06bef8-7cd8-3777-9d3e-be5e6de76803 | -8.4982 | -57.6468 | 2026-09-17 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6f1555ea-9047-3e00-9357-3315cc46827a | -12.5121 | -50.6949 | 2026-09-17 02:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 5699244b-e6d0-36cd-a6a8-659ac464c1bc | -10.8343 | -54.0933 | 2026-09-17 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5e560b00-7d09-3eca-a638-f169ee042dab | -7.75764 | -35.25742 | 2026-09-17 02:58:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 33917008-980d-30f4-8890-c712b4cb49fd | -7.75178 | -35.25641 | 2026-09-17 02:58:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 43dab3bf-1027-31c6-9558-014a4936f16e | -9.4946 | -45.4134 | 2026-09-17 03:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| adab443a-f38c-3601-9f46-e0ea677d9ab0 | -3.4757 | -54.6972 | 2026-09-17 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 856ec19d-e403-3d10-853b-9a926eba7df1 | -5.6283 | -44.8205 | 2026-09-17 03:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a77f1996-395c-340e-9a1b-b38e7cba6a97 | -12.453 | -50.8091 | 2026-09-17 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8090224c-edf9-3e7b-9895-cae798ca67b9 | -2.6966 | -57.6084 | 2026-09-17 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| c51f34be-f9bf-368e-8675-7fbb15a98d38 | -9.0934 | -45.7088 | 2026-09-17 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c43f6364-8f64-38ca-93ca-94309ef0b7e2 | -4.5587 | -42.9523 | 2026-09-17 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 245c879a-e103-3e0e-beae-e4a75ae9c948 | -5.7754 | -45.1053 | 2026-09-17 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 332.1 |
| 35fcc0ad-ea59-321e-84ef-3deca55af69c | -2.6965 | -57.6278 | 2026-09-17 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1c339a0d-f27a-35d1-b135-7a905f8df30a | -12.4718 | -50.8282 | 2026-09-17 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| ee578476-6e8e-3211-932a-76929debf38c | -12.491 | -50.8259 | 2026-09-17 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b5519153-7240-31ce-b308-565b39e897da | -9.0931 | -45.7314 | 2026-09-17 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| fe3f4807-57dd-3100-b4ef-4f412e2c781b | -5.7756 | -45.0826 | 2026-09-17 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| bd32d316-2814-35f1-b586-342649155325 | -9.112 | -45.7294 | 2026-09-17 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 164.5 |
| d1072e61-7eaa-38ef-b239-7120d22bf795 | -2.9582 | -50.3149 | 2026-09-17 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 97464915-a2cf-3df2-80ff-15d8628767a4 | -10.8343 | -54.0933 | 2026-09-17 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6e85434d-adfe-383f-829e-e374bad28ea7 | -2.9581 | -50.3359 | 2026-09-17 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 637ee1e8-0d41-38c0-9e3a-0b7955b9cf0b | -5.6472 | -44.7964 | 2026-09-17 03:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 08b53708-8a43-3b49-b70e-f2ac3604e051 | -10.1053 | -36.2019 | 2026-09-17 03:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 6197a231-4a17-3f38-ab8b-de3036521f79 | -5.647 | -44.8192 | 2026-09-17 03:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| e95ebd30-8ec8-3ac3-8778-5d9237a38df9 | -12.4527 | -50.8305 | 2026-09-17 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3d225f45-f23c-3833-8b04-8d71a39b8695 | -12.4722 | -50.8068 | 2026-09-17 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 213.4 |
| b0f67f86-f6c3-32e2-940d-09281538900d | -5.7752 | -45.128 | 2026-09-17 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b80a3c93-faa1-374a-b664-9325b1e0d40c | -9.1123 | -45.7067 | 2026-09-17 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| c56ee26e-af42-3968-bc42-5c9b0250c13c | -5.7567 | -45.1067 | 2026-09-17 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 5b4fed72-f3a8-3e8f-b628-9fcbc39da585 | -12.4725 | -50.7853 | 2026-09-17 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.9 |
| a7d64283-eb99-38cc-9c30-20f2d205fbc6 | -3.4757 | -54.7171 | 2026-09-17 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| be20bc56-9665-3c2f-bceb-5eb55366dfd9 | -9.6091 | -45.3544 | 2026-09-17 03:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 869d913f-7514-3f08-935d-420e199c5a25 | -9.3065 | -40.2614 | 2026-09-17 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| d476bdd6-73a2-3e4f-b5ff-62dbd5b8ae37 | -9.3069 | -40.2365 | 2026-09-17 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 91d78e2f-f3f3-33c0-90c1-66ba5f96ca87 | -9.628 | -45.3521 | 2026-09-17 03:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7af73972-0c4c-39bb-b510-e5bc7dc18437 | -5.6285 | -44.7977 | 2026-09-17 03:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0912e6f5-5b50-3b06-a892-8a20927c0ce2 | -10.11022 | -36.19564 | 2026-09-17 03:00:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 60835198-6226-3b73-a09e-2fb51a88dbe1 | -13.74178 | -39.01715 | 2026-09-17 03:00:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 77adba93-18e7-3235-86de-272ad601b3c2 | -10.10341 | -36.19893 | 2026-09-17 03:00:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 6c01f543-bf9c-3e20-b0ce-b4c898caea12 | -10.1051 | -36.19006 | 2026-09-17 03:00:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 2d0068b7-c39c-3158-a280-83d37e4b4c44 | -13.73976 | -39.01431 | 2026-09-17 03:00:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |


[Clique aqui para ver as próximas entradas](README15.md)
