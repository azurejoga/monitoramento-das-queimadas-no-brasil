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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a72b170f-6fdd-3f89-8136-c157af7977e1 | -6.62417 | -53.38844 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7525a2b2-1c51-34db-82f2-841644a111d0 | -6.9939 | -46.22966 | 2026-08-18 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1b5f6f7-4423-35f5-820d-f83b2c099471 | -6.75217 | -59.17732 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8cf52927-ec12-336b-94b3-911834e217fa | -9.00366 | -45.83853 | 2026-08-18 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11cef514-da51-3523-965f-e4771b2445a8 | -8.55528 | -55.31287 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf2395aa-b484-3380-a7e3-ff4c4b5055b1 | -8.56477 | -54.71749 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7af862a3-7cc4-386e-98b1-0b0fa6a384b8 | -8.22027 | -55.02847 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fda88f8f-e0cc-3302-8b4e-6f6d12c5da22 | -3.51263 | -48.03616 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2868c2e8-1bab-37b4-aef2-36b7ff15c4fe | -8.0846 | -44.35879 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e24d30cb-3bf3-3fb4-846d-89d6824ae906 | -7.63293 | -55.62716 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 970def9d-8ff9-3f9f-8c67-cae871176730 | -8.55579 | -55.30995 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aaef1db-4b74-3bf7-ad26-f764710343e3 | -8.55867 | -55.31085 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57358e20-c899-35c7-ac0e-9b4ab0b3d9d8 | -9.42037 | -48.25101 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaa280e9-2141-34a4-982b-d7e797e19680 | -9.07203 | -50.85454 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57063c78-7d50-38ad-a731-49efa8c9a1c7 | -3.67839 | -47.64993 | 2026-08-18 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1eb9615d-41fc-322e-9b97-9a461a9d334f | -8.58029 | -54.71488 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 231e8268-daec-3f4b-aa10-50cc0033184b | -6.83965 | -59.00485 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| deb83d0c-15ed-30f7-8251-feebb8853833 | -7.16815 | -43.14342 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| be82dcf6-86cb-392c-a825-66172bfec303 | -9.21319 | -50.09884 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b48efe27-1141-35b0-ae63-113c0d3cc4e8 | -8.58316 | -54.69899 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 20a66cbc-4c4a-381d-a11a-0a689d68f961 | -9.77751 | -46.71094 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6a9dbc6-fbc1-36f8-b128-4a675df6729d | -6.70663 | -58.93955 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b5d2908-343d-32ec-a206-d0893327d343 | -6.53216 | -43.11397 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9eeabd8-e5ee-349a-80dd-6bb72bcb89ee | -8.60399 | -50.34669 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 17e27bcf-75e9-3a18-bbd2-f562cbcc359d | -6.17484 | -47.81386 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f60da89-828e-36d9-8dbb-0d0217874ecd | -9.89982 | -47.72867 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40c93a59-5aa8-3dab-9ca6-965529227bf5 | -6.72732 | -48.65332 | 2026-08-18 04:38:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 075aa415-0172-319a-9664-56fbb3799a2a | -6.74978 | -59.17448 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6df13290-73c0-33b8-affe-a10912f11cd4 | -8.2182 | -55.03998 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0053351e-3b49-37af-9410-57e45c95cdbc | -9.06478 | -50.82894 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f74a456-0457-34ab-b816-2331caed7550 | -6.17764 | -47.81802 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b8c3374-9068-3626-a3dc-67fecdb34d6b | -6.39895 | -54.9479 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a1c06c-9fef-3f0a-bd3c-6f36bdb9d0ca | -8.35935 | -46.47458 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28771862-4318-3923-b005-9521a4376ca9 | -3.265 | -49.5257 | 2026-08-18 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ecfd79a-0299-3af7-9c34-562b65479cc9 | -9.13041 | -46.00495 | 2026-08-18 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bcf14488-e00a-3d1d-be44-c05ce7ff82a6 | -8.58509 | -54.68832 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c43dd10e-7f4c-3b22-9eea-fa432049fc9b | -7.62951 | -45.73764 | 2026-08-18 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15bd21bc-cd18-3ae6-a2cb-ff8e9bad2e1b | -3.50975 | -48.03181 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 932dbc75-5d93-3a32-8146-301df61882b1 | -4.0095 | -48.90344 | 2026-08-18 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e7c6751-0197-3578-9685-542e8561439f | -10.85925 | -44.96861 | 2026-08-18 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 227a202f-c893-3b40-8e18-5af9ee44ea3a | -7.6071 | -55.62576 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a988ab09-67c1-31bd-b0c1-c8688ee587c4 | -8.35811 | -46.37417 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccced569-dd62-35bb-a0f0-bdae589dab20 | -6.69812 | -58.94894 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1853da1b-6623-3b27-b3ed-c6c2f9570489 | -8.10766 | -51.65626 | 2026-08-18 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05094d5d-3d4b-3727-bbda-bba87ee7b402 | -8.03878 | -47.28052 | 2026-08-18 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b72c0a49-5c4a-355b-91cd-8cc6dae82927 | -8.48939 | -48.79792 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c52f466-dda4-3533-a038-71dd806280b0 | -6.85066 | -59.01883 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6e42e26c-98d4-307a-8598-3f827cf32a91 | -6.7036 | -58.9461 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8000fe8-a9d9-32d9-9350-fd68c770307f | -7.37278 | -55.49137 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e76813cf-18af-33f0-b65a-2f9910bbb5e7 | -6.76734 | -59.46353 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a068eff-d604-30fd-9db3-858674a3dc6e | -7.16749 | -43.14777 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d0b5b212-9a5e-363d-be88-20f3a19021b1 | -6.58296 | -42.22952 | 2026-08-18 04:38:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e1a3fe5c-51d0-35e1-8b80-f162c9d73cec | -8.56478 | -54.68988 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 45968b6a-7e6a-3527-b347-7b07ab6e8c07 | -8.57349 | -54.72469 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 755f2391-902e-36a1-a29c-3a78808a859c | -4.0131 | -48.90402 | 2026-08-18 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| f5065d66-e654-38a5-ae06-47599ed9666e | -8.49131 | -48.82906 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c1c40205-fade-373c-854a-70d7ceb228e6 | -8.32061 | -46.48273 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72744208-d04a-3809-bf58-d39e348e71b2 | -8.20322 | -55.03726 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f80c1c34-639f-3d87-a8cb-71e43c5aedf5 | -7.63446 | -55.62415 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4658401d-644e-3cf3-aafc-7fb077c84f51 | -7.56922 | -55.56543 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a97eb67-c2ce-3822-bd19-023d60293819 | -6.95461 | -59.03449 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2509170c-2b8f-32a0-8b46-bdd056b24792 | -9.84863 | -46.75083 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fae6537-fa94-36c1-a5df-d0de9d66f638 | -9.76532 | -46.70177 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a952723d-0a9e-35d1-af2d-768066f79468 | -8.56088 | -54.71127 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16624c1f-1d87-324b-82e4-4cd00f16f82a | -5.47761 | -45.11749 | 2026-08-18 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98983940-7932-36c3-af2f-eb5045db3ff0 | -3.51017 | -48.03551 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5abf3ecc-5ea7-3736-8720-9d9156983f8f | -6.04602 | -57.96678 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df527e5-31ac-38dd-971b-77adbe1b0b0d | -9.47395 | -51.60654 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fa61d01-b1b5-3244-a122-9c38f7936dd3 | -6.39949 | -54.94485 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55ca6559-b915-3cbe-a5ca-f981c4be57e0 | -7.38381 | -55.48996 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a0f513b-3605-3333-bd95-17ad1370d9cb | -4.01605 | -48.9087 | 2026-08-18 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| e2cc37f5-7acb-3e97-abcf-a3994cd336e8 | -6.74625 | -59.15632 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3886f6a9-d4d6-3d23-b03a-f990f17d3077 | -4.33077 | -48.71763 | 2026-08-18 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58978f97-0da6-3ec6-b568-1ae6a7039020 | -10.28958 | -48.23481 | 2026-08-18 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bda69d76-12b6-339f-a590-2ae23469d96c | -7.36232 | -55.48956 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6c11bb2-14d2-396c-9608-06bfcfdead34 | -8.32448 | -46.47977 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e228ed7-3c7e-3779-a909-f7a4db633f8d | -9.47008 | -51.60572 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 308061bc-10c3-3942-8525-e9e190f3a70c | -4.32786 | -48.71307 | 2026-08-18 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c929159e-606e-3488-bad6-17f35d5cde42 | -7.53318 | -55.58517 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08bc8dfc-acf1-3b01-be43-bb3058024a92 | -8.57156 | -54.70768 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 858cb7ae-3f02-3d8c-b97f-bde12a0fa2dd | -9.76201 | -46.74443 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d1db38a-078e-3c4a-b3f9-7739863b42c4 | -8.56574 | -54.71214 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5bfb718e-5055-3530-9acf-aef71bfe940d | -6.73756 | -59.18163 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e927bf78-aaa5-3705-86b8-44674aef6710 | -8.21135 | -55.0208 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4afa930b-d21f-3abd-a1c9-1781f8c1a037 | -4.53386 | -42.93344 | 2026-08-18 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f53422de-34f1-32e6-b3f1-995f9f6f1160 | -8.56186 | -54.70593 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58277e19-bacd-3473-aeaa-4f2e29538025 | -9.13824 | -46.02074 | 2026-08-18 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2981df33-e782-3250-932b-bfee2c9840c5 | -8.58609 | -54.71047 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e83debbd-46a1-3108-b39e-d562872f66d7 | -8.57929 | -54.69268 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b3003d6d-b7a2-3f37-ab45-a79304ab0854 | -7.81945 | -44.60599 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72da37b5-476b-399b-a08e-b782712449c4 | -8.48912 | -48.82096 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84b7ea30-4ad2-3920-9ed0-cc23f1f40be7 | -8.58412 | -54.69368 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5d81bba2-7b93-394b-8919-8d2e6f586794 | -6.74302 | -59.17382 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| db97fbff-7c53-36a6-93fe-e5fbb867d349 | -8.5803 | -54.74256 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 0e78ad92-7fd6-3759-8567-bc1959738312 | -9.80055 | -47.31345 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35f53b6d-b60d-31fd-89a0-aa086317af92 | -8.5706 | -54.71298 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dcfa156f-3993-3e51-aed1-8d3d54e157f3 | -8.59226 | -50.34914 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| cb77fd22-d0a7-370f-a195-59f3fe930985 | -9.43266 | -48.26041 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82374194-d7bc-368b-ad73-a0134b6eb2df | -8.60766 | -50.34731 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4cd358a5-d115-3f88-992f-a746336ebd7b | -9.7609 | -46.72987 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README19.md)
