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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2668e4f-d1c1-3455-99aa-a3ba190b9345 | -9.4813 | -46.3646 | 2026-09-28 19:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a1a03894-a821-34ce-88c4-d95729050526 | -7.0674 | -55.4896 | 2026-09-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| bf754378-27c6-3410-8834-d25afccbee29 | -5.4762 | -45.1262 | 2026-09-28 19:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 4b3308b2-dea9-3204-9e9f-3b5d8af2d3bb | -15.112 | -53.8838 | 2026-09-28 19:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 570dba0a-1c19-34ac-ae26-f8a4553d9e4f | -12.7871 | -54.0069 | 2026-09-28 19:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 2165d5b4-d2a7-3673-a81d-4b1123cfe430 | -11.4966 | -47.3951 | 2026-09-28 19:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c0b21e60-ac84-3b15-ba1a-f62b1adbfd92 | -8.2291 | -45.4602 | 2026-09-28 19:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 3a149633-89e2-38f7-89bb-a19dad9bf0f3 | -11.3444 | -54.047 | 2026-09-28 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1056.4 |
| 7ec12ff1-3e31-380d-af0c-33f311a6ea75 | -9.6864 | -58.1258 | 2026-09-28 19:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 3f84cd54-a175-3e45-a775-472e9edc0e15 | -5.7384 | -45.0626 | 2026-09-28 19:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 13a9d263-8f71-34ff-8afa-8086fa395166 | -9.4999 | -46.385 | 2026-09-28 19:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ab8197de-af7e-3c53-8a41-2638e1c84a7d | -9.1335 | -49.987 | 2026-09-28 19:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 99fad38c-df10-3f71-a678-82839cf2e511 | -10.6869 | -44.4576 | 2026-09-28 19:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| c12f72ca-192b-3a57-88cb-ea46dd4c1392 | -11.3436 | -54.1086 | 2026-09-28 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 188.5 |
| d85118cc-5fd0-3ad2-a64d-639b0b671d15 | -11.1771 | -44.8064 | 2026-09-28 19:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 988ad16e-f92f-3b35-bb05-de42fac31208 | -11.5904 | -44.1411 | 2026-09-28 19:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d94f6d7e-a03d-362b-8783-3c71892995dd | -12.1391 | -57.1751 | 2026-09-28 19:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| f2c85df5-a35d-39b9-bdc4-ab1c828d4446 | -12.1204 | -57.1567 | 2026-09-28 19:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 0804c970-3920-33aa-b99a-19444201ed06 | -8.9826 | -44.14 | 2026-09-28 19:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 00db7d50-75e6-36aa-b241-e3db421cd575 | -5.7388 | -45.0172 | 2026-09-28 19:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 4fce6cfc-06cf-35d8-8a76-dccebee8443b | -15.0984 | -54.7189 | 2026-09-28 19:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| de291176-3e74-3f67-be7f-00a40f22a74f | -11.7178 | -43.4623 | 2026-09-28 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| a218ff1b-33ae-3c4a-92c2-da826502e1f6 | -8.2994 | -54.7146 | 2026-09-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 0ae27a0d-d02b-3d3f-9d28-4d639067e85b | -9.9781 | -50.1626 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ccd685f7-98dc-32cb-8ee2-656532ff9f6e | -10.6505 | -50.7123 | 2026-09-28 19:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 7a212c8b-ab49-39fe-a8dd-96ac68ce7f86 | -9.9396 | -50.2304 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| b08e3113-680c-3657-9ca6-303196eaf310 | -20.0991 | -57.2067 | 2026-09-28 19:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e8c546d1-f4d0-313d-89b5-42703a8f3182 | -12.5234 | -49.9834 | 2026-09-28 19:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b97241e0-2606-32a6-9553-bbd6e68dbbf5 | -7.0675 | -55.4697 | 2026-09-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| a88b583c-c8ef-39d5-b324-6a910e7af5fd | -9.9882 | -45.3542 | 2026-09-28 19:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1ec545b0-8829-3af8-8148-60750fe0f087 | -10.9637 | -43.8821 | 2026-09-28 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 880e152c-a901-322b-93a8-71afd2025bbd | -8.9823 | -44.1633 | 2026-09-28 19:40:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| edd69aad-97dc-30a9-b405-1563290e105f | -7.9928 | -43.2475 | 2026-09-28 19:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 9995e5f1-908f-3776-98ac-0288cbe650b6 | -7.7038 | -54.7521 | 2026-09-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 6ebdec1f-562f-3c6b-93e5-d8b575585a68 | -12.8061 | -54.0048 | 2026-09-28 19:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 80907cff-03a9-33ab-818b-c6179fcc49ea | -9.481 | -46.3871 | 2026-09-28 19:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| d4324a6c-0e63-38eb-a676-ab6c9ada3c30 | -7.9925 | -43.271 | 2026-09-28 19:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| a8e7e7a7-06c0-3c9d-88c2-ef4b95aeebda | -7.437 | -55.6291 | 2026-09-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 5c2e32df-eb4b-3546-b9b4-92352650923b | -7.6851 | -54.7734 | 2026-09-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 357827ab-1092-346c-86db-71ead2ea9104 | -10.8377 | -57.1979 | 2026-09-28 19:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| f1b6530d-556b-31bc-b935-b6c405cebc96 | -9.9593 | -50.1644 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 4c16cfe2-01c2-3af3-8519-1a912985de56 | -9.9595 | -50.1431 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 174.1 |
| beb39594-2fbd-358b-b6ab-91630a6df920 | -10.8371 | -61.418 | 2026-09-28 19:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 3c9f3072-31b5-3fe9-ac79-b47adfed8d3d | -11.1517 | -50.0603 | 2026-09-28 19:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 12d60588-d0f6-38e3-997e-0ed7cb0c5f87 | -11.1775 | -44.7832 | 2026-09-28 19:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 59fb3f71-ecf1-3fad-9b2f-3fb2c025f74c | -13.3267 | -43.9523 | 2026-09-28 19:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d83e3ee7-e0d6-3245-b6c6-146e814633df | -9.1337 | -49.9656 | 2026-09-28 19:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 38db95f9-0db4-39ef-bc63-cf74f6bad86b | -10.8238 | -60.744 | 2026-09-28 19:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 169.8 |
| b7d2ecb7-d5e7-37f5-8660-6fc5914f254d | -11.0223 | -54.1379 | 2026-09-28 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 31fb257a-24dd-3ee2-8582-cbad9f5fe336 | -10.9912 | -50.6978 | 2026-09-28 19:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c9a7c53a-06e8-39a1-b6be-0a31783c1261 | -5.1887 | -46.0888 | 2026-09-28 19:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 236.8 |
| 9e347d61-7635-3403-a968-32366fc97457 | -9.7051 | -58.1247 | 2026-09-28 19:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 3672fcdc-f0b4-33ec-8068-827354034367 | -11.1514 | -50.0818 | 2026-09-28 19:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.8 |
| b62748d8-5c56-3f35-a7e9-4e7229fee2c9 | -11.6096 | -44.1382 | 2026-09-28 19:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 245.9 |
| f484bd25-4fa6-35ce-a8c3-16b54df2daad | -7.6852 | -54.7532 | 2026-09-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d4ecb36a-f35d-35ee-8d97-1b02a4b30563 | -11.1966 | -44.7805 | 2026-09-28 19:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 619da7b9-0785-302c-a5bb-a12952433ac5 | -6.1251 | -43.7262 | 2026-09-28 19:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 1a4e2eb0-7430-354d-b181-0489178f20b8 | -7.7037 | -54.7722 | 2026-09-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 522750de-28e6-30f1-9de1-9d8866945056 | -12.6267 | -47.2851 | 2026-09-28 19:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8bed7d35-5a3f-3ff6-8f69-5dbecc8b147a | -11.1962 | -44.8037 | 2026-09-28 19:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6317c89e-ca6a-3903-a30c-c1c8ff5d938a | -9.768 | -44.8543 | 2026-09-28 19:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c72bfa19-26f9-3562-8d71-b198f5d27e28 | -10.7916 | -48.7377 | 2026-09-28 19:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 380d2d77-0e5c-367e-8b8c-6f427c1d1059 | -5.4949 | -45.1249 | 2026-09-28 19:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 1347beb8-3d60-388d-8927-e3f48e040345 | -0.4889 | -49.1327 | 2026-09-28 19:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 8b3375bb-44f7-3db3-957a-bef34d7d0795 | -9.9784 | -50.1412 | 2026-09-28 19:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 7f15d44c-bf0b-3d50-ba2b-ceb993dea190 | -9.1523 | -49.9853 | 2026-09-28 19:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 8b51cb81-f430-3544-9793-564352b2e75e | -15.081 | -54.5964 | 2026-09-28 19:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| b8a7e199-0009-3b81-85aa-324b41a69df7 | -10.8426 | -60.7429 | 2026-09-28 19:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 194.9 |
| b8d370c9-50b2-3982-a143-b49c5430519a | -13.3943 | -57.0645 | 2026-09-28 19:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| e679b74e-5712-3e7a-90a2-ad5d98cb2383 | -8.2479 | -45.4583 | 2026-09-28 19:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ba654ee5-433e-3e0a-b17d-e8da3dcc85ea | -7.5159 | -55.0245 | 2026-09-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 22522ce9-c53e-3005-9786-9437e628cfce | -10.9154 | -50.7059 | 2026-09-28 19:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 560b00b4-b824-37fa-811e-5d50341d3a2f | -12.9456 | -46.652 | 2026-09-28 19:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 7ec3afb9-b4c9-344d-8d5c-c754eb3a4f1a | -10.8189 | -57.1993 | 2026-09-28 19:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 189.4 |
| bf5f7006-7aff-3ba7-9290-ec95b5e01311 | -7.2181 | -45.0797 | 2026-09-28 19:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0e791ea6-2be7-348c-b261-55da2723f227 | -12.1202 | -57.1767 | 2026-09-28 19:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 360dee31-8bd8-3f77-8eeb-d40ee1280c4a | -10.9445 | -43.8849 | 2026-09-28 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 23a4df89-7e47-3d5c-a06c-50b5f3283120 | -18.6834 | -48.6234 | 2026-09-28 19:40:00 | GOES-19 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 57a7f755-3fff-311c-b585-8b82b22503cd | -13.9012 | -53.6757 | 2026-09-28 19:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 4a6c38ab-7aae-3356-adc8-8e06740b10eb | -11.5157 | -47.3926 | 2026-09-28 19:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |


