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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e44a1e79-2c20-3346-a307-f2f6ae1a9077 | -13.57074 | -46.96489 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c6c0a2-0899-37e4-b74b-bed57e8f21aa | -11.92657 | -43.44101 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 322735fa-6c2e-3394-914f-b07c73df2e1c | -13.14732 | -46.86113 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a5b95ea-19a8-32c3-8423-0b55b8b23183 | -12.57195 | -46.95978 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a951b7e-aa11-3b4e-a0aa-c40292f13e4d | -11.35601 | -55.41697 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 031efb9a-f989-3dc0-9465-faa1d6b0bf85 | -11.34396 | -55.42651 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 425f9751-d83a-36f7-b578-fad063e650fb | -9.93535 | -60.48554 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e453dca8-2609-34de-8c50-6689bd4eb8be | -11.40799 | -58.53901 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84eac7ee-1a7a-32eb-ba48-60027cddf56e | -9.17749 | -59.68364 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b29bbf60-1be0-34d5-84d0-685064018dee | -12.5725 | -46.95623 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac9122ef-461e-3441-8c0f-455e33eaf6cc | -11.36092 | -55.418 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cec52e91-0a49-335a-9d8a-f4a026eb82bf | -13.47594 | -56.66284 | 2025-08-15 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd19c3a6-665f-3e51-ab4c-75d39980d257 | -15.18071 | -53.83804 | 2025-08-15 04:29:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d8ac26a-98ad-3e38-9c01-f36062ea015d | -14.73796 | -46.30085 | 2025-08-15 04:29:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0722e6a0-e9b5-3ec9-9d99-ce122d019831 | -11.35768 | -55.43509 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3865dd60-e2d9-397e-b6cb-8c04760893f2 | -15.39402 | -55.78189 | 2025-08-15 04:29:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b1ceb719-d0f5-3df7-a5dd-8054dfd36b01 | -14.02326 | -52.03572 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2dea3ed-95a9-3e0f-b24c-d8473e28345d | -9.14831 | -59.69044 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7920e13-2776-30e3-89e0-1292639de007 | -13.3236 | -45.22373 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f107b83-cb33-34d0-b537-01bf7f19515d | -14.41846 | -48.4374 | 2025-08-15 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b85d6790-43c3-3304-90c6-f538c41fca5c | -14.90627 | -45.19032 | 2025-08-15 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90c19056-f603-3f38-9d02-2450a912b58c | -9.16836 | -59.68091 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 529499eb-5f05-321c-855c-489001da4337 | -14.38033 | -53.37589 | 2025-08-15 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8a603f2-7ee8-3844-8def-20f5e5cca2b9 | -9.16646 | -59.66912 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 63d64542-e0d7-3dd1-bb31-4413324261c8 | -10.01085 | -59.21907 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad7fd0b8-9316-32ef-9942-a92f8351529b | -14.01785 | -52.04438 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51252ce3-6848-3c1d-80c9-1b867265b50e | -9.16961 | -59.68831 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c04cf16-0687-3dac-85af-8181d448d3c8 | -13.5813 | -46.96312 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4be7817-95b9-3751-9604-7fc81145ef96 | -12.5059 | -47.011 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0e4fc15-8f47-3e52-b352-15cdb3d961ed | -13.14789 | -46.85741 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bc05ab9-0b72-3e91-b5b3-4df58fc0f08c | -16.52399 | -44.93913 | 2025-08-15 04:29:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fec05b7-7cf0-325c-853a-4d5f80dde353 | -11.91947 | -43.43771 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5addab6-28f8-3d9b-aa6d-baecb6a85150 | -9.49891 | -60.52494 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 28ba78d8-4528-3f54-a019-0d4b191a77d8 | -13.32653 | -45.22826 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f47b89c-8ac6-3e36-86c8-12520af29eb9 | -13.88953 | -45.55969 | 2025-08-15 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d2cc906-a619-3c6f-8df5-b9f3abe9cbfe | -12.59675 | -46.96714 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 767370b0-012f-39ce-a402-45210285361d | -12.50534 | -47.01455 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2deb152d-ce64-3507-915b-703613c2accd | -13.12343 | -57.14162 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75f55e7a-540b-3d66-953a-2b8bef73247f | -11.40708 | -58.54369 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bfff73d-e802-3fd4-bb10-3b09d5a121d1 | -9.14827 | -59.42778 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12b13ef0-712a-3136-badd-7089f026809d | -9.4992 | -60.547 | 2025-08-15 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 463922ad-d49a-39b4-8f09-c8196646c006 | -6.9302 | -59.5497 | 2025-08-15 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4d5a601b-c7ab-31a1-841f-021519bc0ff0 | -9.518 | -60.5268 | 2025-08-15 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7faed152-2e07-36c0-9d6b-43c5e84ad835 | -9.1894 | -59.6558 | 2025-08-15 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ead2465a-1ab1-3862-b2b9-0790c8e157ae | -7.5292 | -61.3254 | 2025-08-15 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1276c9b0-22c3-3ef7-943b-98a189b34f23 | -9.1708 | -59.6568 | 2025-08-15 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7bd1bb10-8b04-3314-bc98-5274538a795d | -9.1706 | -59.6762 | 2025-08-15 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f41bd191-d1ab-383c-8786-39a9c237cd1f | -6.9303 | -59.5305 | 2025-08-15 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 31dcf27f-6046-3374-8e7f-9a1342d3a24f | -11.3468 | -55.4124 | 2025-08-15 04:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 48bf81a7-b026-3403-b4b7-e490dad00a4d | -6.6945 | -58.8259 | 2025-08-15 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 85624b8c-a47b-3017-9fb6-5d9ab903f282 | -7.5291 | -61.3444 | 2025-08-15 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| c17da946-fe52-380c-8024-f30376e7a1c6 | -9.4994 | -60.5278 | 2025-08-15 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d4ac9d4c-92bd-3327-8870-2a74ea81b8cc | -21.20463 | -46.69063 | 2025-08-15 04:32:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0248769-267b-342d-b7d0-e368c9459cc1 | -23.33984 | -46.89373 | 2025-08-15 04:32:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cbf02ed4-47bb-37b9-83ee-c7267f9a62ec | -19.77998 | -43.73276 | 2025-08-15 04:32:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82a39b5e-0ded-30a1-bbee-c9c2106c0dbd | -15.66645 | -56.38419 | 2025-08-15 04:32:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9b053385-195f-322c-be6c-7e0608f75366 | -21.26632 | -43.75756 | 2025-08-15 04:32:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a3b3025a-91e1-34ae-931c-c70b80f19489 | -18.53434 | -45.45181 | 2025-08-15 04:32:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68f70ae1-dcb4-3ea6-ad9f-e65e24b5369d | -19.11644 | -44.47496 | 2025-08-15 04:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8e6f83-db18-3bba-ae96-1b9549de5dd5 | -15.9715 | -59.51548 | 2025-08-15 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3cbf691-d28a-3e73-a014-8fab3d781c65 | -19.90968 | -47.47298 | 2025-08-15 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8836be6-1952-3763-873c-b77d489cce84 | -20.32869 | -45.22942 | 2025-08-15 04:32:00 | NPP-375D | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 47a0c8e7-561c-32de-94d0-4103406fc575 | -15.386 | -59.8205 | 2025-08-15 04:32:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec70a9ac-dd35-39c7-b72a-dec0047a2422 | -18.53068 | -45.45123 | 2025-08-15 04:32:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaa587fe-0bbe-33f5-9b6b-084baafa27ea | -22.76185 | -50.35723 | 2025-08-15 04:32:00 | NPP-375D | CÂNDIDO MOTA | SÃO PAULO | Brasil | 3510005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 05256ef2-7ce2-3123-9141-fed90197c51d | -20.45873 | -48.0218 | 2025-08-15 04:32:00 | NPP-375D | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdd3adf0-a943-3cb1-88f8-e0584555de69 | -23.35482 | -46.91896 | 2025-08-15 04:32:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3f4e09d6-0349-3b4d-97d9-00f112d20830 | -17.75023 | -42.25805 | 2025-08-15 04:32:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4b6df7ba-d789-30b8-9876-af348496333a | -20.64677 | -48.69786 | 2025-08-15 04:32:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 822a0436-9116-3ac7-9dc5-7a19caedb100 | -17.56962 | -52.53081 | 2025-08-15 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 59587d77-fb81-377a-a541-bee2b2033f14 | -20.51097 | -47.41438 | 2025-08-15 04:32:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05245930-737b-3d0e-8a10-4818ced4f602 | -21.58413 | -47.00365 | 2025-08-15 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87642daf-9d5d-3976-8fb5-1a7ae9432e32 | -19.47416 | -43.61317 | 2025-08-15 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d6e284-2be8-3be6-baa5-aaf1629e55e0 | -23.27089 | -51.20704 | 2025-08-15 04:32:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 43b3865d-48f9-30ff-91f4-69d6ee73efb0 | -20.6231 | -46.30805 | 2025-08-15 04:32:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08e3f069-bf7d-36fb-b013-6b6368ddb78c | -18.29553 | -49.54527 | 2025-08-15 04:32:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b16e19d7-6275-37a5-9787-0db0cfe54d0f | -21.58059 | -47.00312 | 2025-08-15 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d025f1b-f1c1-331d-9872-59c4197e180a | -22.1879 | -45.35201 | 2025-08-15 04:32:00 | NPP-375D | CRISTINA | MINAS GERAIS | Brasil | 3120508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7edc76ba-0059-36c3-aa2f-dd318ad36340 | -18.29828 | -49.54952 | 2025-08-15 04:32:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b93e65e4-f39f-3d8c-a0c4-30a6b9baea8e | -16.38907 | -50.91178 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0d25d13-bf81-354b-8f52-ae79a89121a2 | -18.11105 | -43.9901 | 2025-08-15 04:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45c50b48-4ab9-33f4-9671-84e9cbc82ffd | -18.53314 | -45.45381 | 2025-08-15 04:32:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c13ec7c5-6ed7-37ff-9114-9185bea96189 | -17.64499 | -44.50282 | 2025-08-15 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fc0e20c-1429-3790-be74-037bcfbe6ef4 | -17.64882 | -44.50332 | 2025-08-15 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fbf5803-6a69-3ef7-9010-d51efa4a1245 | -16.3933 | -50.91142 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f81d600f-fad0-35d1-801b-aa0d6a071b91 | -17.64942 | -44.49894 | 2025-08-15 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 120e02c0-833d-3953-8fef-3223bade30fd | -18.24576 | -47.25715 | 2025-08-15 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00da2bb8-4036-3bc9-be7c-df6f7036307b | -16.31429 | -52.92145 | 2025-08-15 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f866aa9c-22c9-3770-8d0f-e2949f0a2e7e | -23.76101 | -51.90067 | 2025-08-15 04:32:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dae7da55-b641-3b9a-9853-9a838ecbb5de | -15.67243 | -56.37947 | 2025-08-15 04:32:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f81d93f-4882-39eb-80ec-0d3c83f3f817 | -22.18884 | -45.35462 | 2025-08-15 04:32:00 | NPP-375D | CRISTINA | MINAS GERAIS | Brasil | 3120508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e49623dd-d39b-308d-bcc1-1a4a81920b5a | -18.29494 | -49.54893 | 2025-08-15 04:32:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f5253e46-4fba-3f31-aff4-517c659993b7 | -16.1736 | -53.63125 | 2025-08-15 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3a79dae-4631-3449-9b5b-a6498266fae1 | -15.67132 | -56.38517 | 2025-08-15 04:32:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3fa7507-2bc9-38e4-bf06-5fc8608fe092 | -20.46504 | -46.21745 | 2025-08-15 04:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 260c78cb-13e0-3339-a45b-3a386bb1a39f | -17.06176 | -51.79918 | 2025-08-15 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2323dde7-dee7-37e9-aa2b-f57764a814a4 | -17.49891 | -47.83804 | 2025-08-15 04:32:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 590b7ee2-eaa5-3a6d-b005-ad95ad3252cf | -15.67729 | -56.38047 | 2025-08-15 04:32:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b9db9eb-5959-309f-943f-34c15cea3da2 | -16.30655 | -52.92007 | 2025-08-15 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aeed1c7d-8645-3332-93dd-5dd7c7f67c9a | -21.58 | -47.00735 | 2025-08-15 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README38.md)
