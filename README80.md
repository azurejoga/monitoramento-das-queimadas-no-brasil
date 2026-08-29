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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 517421de-bac7-3af9-bb36-0e66e0304c9d | -8.948 | -62.3894 | 2026-08-29 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4a3e0b5d-a377-36ac-8b88-d48cc7db2f73 | -14.4661 | -58.5291 | 2026-08-29 14:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5934fa49-422a-37a1-b2c4-1231543586a7 | -6.1657 | -57.7793 | 2026-08-29 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| fa470158-d03e-31ef-9aa5-c36db3e99522 | -6.7832 | -59.4401 | 2026-08-29 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 06c2ee3c-8ed3-3e52-bcd8-b65d6d1d21df | -11.7028 | -47.6129 | 2026-08-29 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| dd17d412-a957-3c7a-a41a-f75747b92e92 | -8.5968 | -54.7957 | 2026-08-29 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f2374dcc-624f-30a7-9910-bdc17f96dea0 | -11.0057 | -49.6677 | 2026-08-29 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7322f3e3-ee77-3d13-86bc-054043a07bfa | -12.2093 | -50.5386 | 2026-08-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 43ecf1c6-e055-3823-8133-7bbfffe25c80 | -10.8235 | -50.5026 | 2026-08-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 701e384d-5d63-3937-8a4f-e16484df147e | -12.9221 | -45.8582 | 2026-08-29 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 7e76db6c-28f0-31b0-9281-9794d81ced67 | -9.9708 | -53.9419 | 2026-08-29 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 40145be1-9180-3925-9ebd-368aa50ac62a | -14.2024 | -52.8643 | 2026-08-29 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 61fdbf83-b4ee-3455-8930-69137914d50a | -13.9919 | -54.0189 | 2026-08-29 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 21e81092-3f80-352d-81df-340807f8e656 | 2.2375 | -50.7515 | 2026-08-29 14:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ebf77992-a681-3873-bf9c-4f5a0aac3517 | -6.1656 | -57.7988 | 2026-08-29 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bfb69343-2d50-39d6-8a98-dbb91c52e9aa | -12.1902 | -50.5409 | 2026-08-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1ee0849f-e03b-3f3b-a284-11665e9b1ec9 | -8.5969 | -54.7755 | 2026-08-29 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 4e9b2fad-19f4-31fa-8ef7-8a5e647e3ab2 | -7.9838 | -45.5072 | 2026-08-29 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3e1dfa63-e757-3e25-92ac-7dbc970733d4 | -11.7024 | -47.6352 | 2026-08-29 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 82dc51b4-59ca-32d1-a74b-ad4fe76a9daf | -11.7167 | -54.5244 | 2026-08-29 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 6a58809a-c3d5-38c8-a861-97a4f5f6abab | -9.971 | -53.9214 | 2026-08-29 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 4e0435a8-284a-36a5-9fbf-fe69d7d458ea | -11.2317 | -53.9958 | 2026-08-29 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 3baa3d45-6434-393a-90b5-54f181c7d205 | -6.8018 | -59.4201 | 2026-08-29 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b7fed83f-2e66-3810-9e84-e2d1f4cf9952 | -10.7791 | -53.9752 | 2026-08-29 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5fdeb882-30f6-3f5f-8f28-1892c86bace2 | -7.4952 | -55.3062 | 2026-08-29 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0cffec20-155f-3a6b-8157-8c641e8007eb | -11.7165 | -54.5449 | 2026-08-29 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ac08977b-cde5-31ca-97ab-e6640cbadc66 | -2.7948 | -49.582 | 2026-08-29 14:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 8437ba7d-c793-3b70-88a8-e63a87bf6d0f | -8.9613 | -63.279 | 2026-08-29 14:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 350a1e9c-a5d8-3db7-8b83-3709c4502036 | -12.2284 | -50.5363 | 2026-08-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| a44cbbe4-b19d-3b76-a80b-4d2ae122a74b | -10.4794 | -64.5012 | 2026-08-29 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 64ffb790-dc27-37ff-8c15-45734db94e1d | -14.2027 | -52.8432 | 2026-08-29 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3b9032a7-0797-374f-8020-db976e4f90d1 | -10.8425 | -50.5005 | 2026-08-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 12b2e0a1-e05e-3868-bc4c-f97f9976b2ab | -14.1835 | -52.8456 | 2026-08-29 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 170.7 |
| a6dfa84c-eeb4-3502-986a-089547bbeb47 | -6.6315 | -43.7533 | 2026-08-29 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 436287b9-9e33-3c9b-ba53-05745a8e5e79 | -8.7767 | -49.9977 | 2026-08-29 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6c9cfac6-632f-31ae-8252-091b4b4cc5c6 | -7.5478 | -61.3056 | 2026-08-29 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 8dbec45f-01a2-3cc3-a4fc-e4c493c2e631 | -6.6317 | -43.73 | 2026-08-29 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 500806f1-a7ea-3287-a997-6c37b83313b8 | -10.7596 | -54.0384 | 2026-08-29 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 81c493f1-2f71-38a4-8f54-bee9c0899b98 | -8.9428 | -63.2797 | 2026-08-29 14:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 1c3127b6-d254-3374-a09e-c064cf5045e5 | -7.5662 | -61.3049 | 2026-08-29 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 203.7 |
| 0b53b7aa-03f6-3cc9-af0f-fdef954bc912 | -10.8804 | -50.4965 | 2026-08-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| f3fa83d5-10b0-3ec7-a2fa-478f887fd298 | -11.5039 | -46.9471 | 2026-08-29 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c025cf33-6c2d-39ea-844e-e54bc1132327 | -9.2094 | -51.5444 | 2026-08-29 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 48821288-ed2f-319e-b2a0-40c4c76c6bdb | -11.2314 | -54.0164 | 2026-08-29 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f35a1c59-ff99-3869-ab23-71eef609bb3e | -15.3849 | -52.6677 | 2026-08-29 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1fa1abc6-9eab-34fb-9dbb-631b2f63d4c8 | -14.9 | -56.3257 | 2026-08-29 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 389d54a2-fd46-3ccc-951b-d5b1b7277fe3 | -14.4142 | -51.7345 | 2026-08-29 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 2d59121b-75f4-325d-ac7f-c2ef47164d11 | -15.3849 | -52.6677 | 2026-08-29 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3aecff0a-541e-35f3-a7a3-25a2a5adafae | -6.6315 | -43.7533 | 2026-08-29 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| eb7ceee2-b9fd-3939-98dd-e83f577e239b | -10.7791 | -53.9752 | 2026-08-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 32e79ad6-0eb5-370a-b7bb-fcab07e133b3 | -11.1726 | -51.2728 | 2026-08-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 4fc22793-de88-3504-9389-1512da6810cb | -10.8804 | -50.4965 | 2026-08-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 62eeb6fe-4942-32a1-8b36-8c0fafbcd3b7 | -8.9613 | -63.279 | 2026-08-29 14:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 482c8759-2d2f-3fef-ad00-3b1dd2671560 | -11.2317 | -53.9958 | 2026-08-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 5cef47cf-ca25-37c4-9a39-5bae75a16107 | -9.9708 | -53.9419 | 2026-08-29 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 407ace10-9b14-30c0-86ba-117ea65e02bf | -12.1899 | -50.5623 | 2026-08-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d977fd3d-7086-3a43-885b-d9e997e0e2f6 | -9.971 | -53.9214 | 2026-08-29 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| c3f03006-1dfe-389f-816e-cbbb9b33f4fc | -14.4142 | -51.7345 | 2026-08-29 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 86b4e2f7-4f2f-3753-80e5-a675d6e974a1 | -6.1656 | -57.7988 | 2026-08-29 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| bd7301de-7380-3a78-bc4e-1cf8f19ebd86 | -6.6317 | -43.73 | 2026-08-29 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 272.1 |
| 1c1954d9-28e1-38f7-948b-3332975a0cf7 | -8.948 | -62.3894 | 2026-08-29 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4cce5a24-c15a-3e5d-b31d-c939e7d26e95 | -8.5968 | -54.7957 | 2026-08-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 39ca81f3-4a77-32ad-93c1-44e97b3859cd | -6.7832 | -59.4401 | 2026-08-29 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6ee714ac-5ad1-3b65-a915-e13d2de8e097 | -10.4608 | -64.502 | 2026-08-29 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9cc3c592-33dd-32d9-8169-5daf768bf3f5 | -6.7884 | -55.6635 | 2026-08-29 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 6cf489f9-c084-3fbd-931c-3744c62630b3 | -11.0247 | -49.6656 | 2026-08-29 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 7b3dd3d2-3bca-3834-8906-b2544712a14b | -6.77 | -55.6445 | 2026-08-29 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 83ba073b-e73d-347e-8544-66a95e01cd74 | -11.2503 | -54.0146 | 2026-08-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 955df746-be8a-3747-8996-6c7eb95a4f13 | -12.1902 | -50.5409 | 2026-08-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 95f12dde-1c3e-3bf8-99b4-c0f78ef426b1 | -11.5039 | -46.9471 | 2026-08-29 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c79fd790-e16c-3d8c-9875-7a7ffbfad75a | -11.2489 | -45.0732 | 2026-08-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| db43f932-dc6d-39de-ad33-4b1767152271 | -8.7582 | -49.978 | 2026-08-29 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 615bf243-5b3c-3f9b-8cf5-2fd341f92259 | -12.2284 | -50.5363 | 2026-08-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7960e09a-f2e4-3eee-ae27-2665d3a312fa | -10.8232 | -50.5239 | 2026-08-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f1aa4293-3f89-300b-b899-8b0095ab7753 | -11.7024 | -47.6352 | 2026-08-29 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ba1b9c79-95f0-3e43-b0f2-0a0c9da20520 | -6.1657 | -57.7793 | 2026-08-29 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e6d651c3-1e3c-3dfa-b608-c9b24b32af91 | -10.8425 | -50.5005 | 2026-08-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9c0cfabd-1bd5-3b75-86b9-3ddc7e4a1ab8 | -12.9027 | -45.8612 | 2026-08-29 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| ef232c64-79fc-3abc-af15-ced5f0814e0f | -10.3391 | -49.9762 | 2026-08-29 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 70c032e9-9c9b-35d4-b50a-718479ecef04 | -6.8202 | -59.4194 | 2026-08-29 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 62a2700f-b52d-3b12-a189-873a892a1c0c | -10.9673 | -51.0614 | 2026-08-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1422ad34-1fd6-35e1-8e02-874b9b19d922 | -8.7769 | -49.9763 | 2026-08-29 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f5d2a8f2-cf54-3185-bc33-153b0b9b0f3a | -11.2128 | -53.9976 | 2026-08-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b92e6284-ba0a-327b-8b60-ce23bea108dc | -10.4794 | -64.5012 | 2026-08-29 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c979fc38-e160-3b61-8d34-02c271d7b505 | -10.7794 | -53.9547 | 2026-08-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b30ba23b-673b-3fd3-9ed2-a225a26384c0 | -10.8235 | -50.5026 | 2026-08-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 758ca197-bfa2-3fde-b743-f4d64dfa2e06 | -11.1916 | -51.2708 | 2026-08-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| bdd38f4a-a4f1-350d-ab1c-b3d3e41fa83a | -2.7948 | -49.582 | 2026-08-29 14:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| aaa19f90-8735-3f70-89f8-0744f15a5af8 | -8.5969 | -54.7755 | 2026-08-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fdb83cc4-63bf-361d-8863-0cd73daccb1a | 2.2375 | -50.7515 | 2026-08-29 14:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bc3836a6-2293-3406-a491-709478e994c5 | -10.7596 | -54.0384 | 2026-08-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 353c0039-9912-31f7-9fca-7d033fba8431 | -11.1723 | -51.294 | 2026-08-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| cc56e23f-c348-31ec-8b0a-09752d5860c3 | -7.9838 | -45.5072 | 2026-08-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e63542b9-7f8e-352f-b4ec-597b26cafa08 | -10.4609 | -64.4831 | 2026-08-29 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 6e1752c5-1069-3548-bba5-cf5b34e7cc81 | -6.8018 | -59.4201 | 2026-08-29 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 578ec4fc-2a47-39fd-b43a-9179c0f19ce3 | -6.9521 | -58.9506 | 2026-08-29 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| cb03ba02-60c9-316f-befd-7b4b8dd7dccd | -6.7885 | -55.6436 | 2026-08-29 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| a14ad598-ce90-350c-8045-33d4533f15a7 | -11.269 | -54.0334 | 2026-08-29 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 72e081a2-dbc6-3173-8e59-7f6b9136d9da | -11.7165 | -54.5449 | 2026-08-29 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| bc5cda2d-3f08-3a68-8838-5268fda25929 | -13.9915 | -54.0397 | 2026-08-29 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |


[Clique aqui para ver as próximas entradas](README81.md)
