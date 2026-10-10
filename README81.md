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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8b3bc61-925e-3105-82b5-df09f461ef78 | -11.8396 | -46.80722 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57af7776-b967-3065-a51a-7bb099d8d7ea | -10.89571 | -44.82113 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 21f2b5c1-a2df-34d2-b8c3-ac72feb8f08f | -11.02 | -49.11414 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1e317bf-39bb-3377-b742-491f1b557ee3 | -11.0208 | -44.02967 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee91a77c-2608-3ff0-bc72-8438a9d7f1e4 | -8.77135 | -49.60947 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c3f63b3-6c43-38b4-97cc-da75286f2586 | -7.75568 | -54.79332 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cb4d0a0-ef81-3762-a4cf-6c6bbbd4ca92 | -12.36102 | -46.59391 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b1091f4-afc7-32f5-bb01-348b32525bae | -11.75282 | -46.78315 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79b3e338-a878-3ea2-95d4-7a9fd740e15b | -7.23391 | -55.18249 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f842631e-a512-3edd-9940-a2aa04ca633d | -7.06182 | -46.45494 | 2026-10-10 04:46:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20ed7b88-8d72-306e-958f-e6ee0ffa4b1b | -11.18398 | -45.32399 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebf0c0d6-dc40-3c77-abf9-95f352e11219 | -13.03776 | -47.17007 | 2026-10-10 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c2624edb-77f2-33d6-a169-899851b4544d | -6.75157 | -48.72464 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f1063da-cb73-39c4-bd3d-f5732f3a299e | -11.472 | -43.38592 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0dbc7eda-ec6d-39b6-904c-474beac9dec7 | -14.46073 | -43.96039 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af3130cc-f648-38fd-8a90-669651155c94 | -8.34523 | -45.0066 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb4707bd-9955-3aaf-89a0-77768654c3b6 | -7.00068 | -47.71161 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f62eb20-28dc-3875-b4e4-81e4e9f0c87e | -7.18875 | -55.16449 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19ae5627-0e57-3100-8250-ba9761f700fd | -6.12469 | -55.70496 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24cb0aad-0101-3968-9c37-4495daea8336 | -6.64532 | -55.32915 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 558e63d3-9cdb-3db2-ab03-883c2b5236c1 | -11.75691 | -46.77971 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 526e49eb-c92f-3c14-aeea-d9e405be6eb8 | -14.01278 | -48.76985 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce317a9c-6a9f-33f4-8e25-b145633ef443 | -6.9374 | -59.24777 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df97bdef-e35e-3940-8cea-e44db11d5048 | -8.24926 | -46.41734 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b59c44-484f-3617-a421-acfa3c8853b3 | -7.22662 | -55.14065 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 33185ac1-2f21-309d-8338-2b3d5a4d4f68 | -11.59443 | -43.74387 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f6f0cd5-62a0-36d6-9777-bd1c7db94887 | -11.96842 | -43.48956 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c63c6bd6-3ab2-31ed-9fc1-fdd7cc863661 | -13.74239 | -48.5121 | 2026-10-10 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e17fec44-ff87-321d-965d-d951138cdc94 | -6.33243 | -58.30793 | 2026-10-10 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e04909-f257-3e2d-941f-9a51c48b9944 | -8.77532 | -49.60641 | 2026-10-10 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73735ea5-b93f-3753-a4c8-4746a1538ed1 | -13.89692 | -43.91685 | 2026-10-10 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5983467d-fa5c-3e14-bc2c-7491e1f0d7ff | -7.02836 | -47.66606 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ca87b155-58c6-339c-af9d-928d76dda3f1 | -11.25521 | -46.24513 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2814e4c1-f095-362a-914e-a5abf5a9730a | -9.21438 | -51.88037 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17195499-55ed-332b-ad5b-4912ab8ecf36 | -8.1781 | -54.7171 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de175259-8123-38b4-81e0-ac32ba02767b | -6.64832 | -55.34029 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 050ce4ce-7724-3769-adec-81a9f1c4d6b7 | -10.60183 | -60.48977 | 2026-10-10 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 63c3188c-790e-379a-adf5-f8ede65c1896 | -10.8937 | -44.83504 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e5ea10d7-d9c8-39d0-9449-750fec36daf8 | -11.74996 | -46.77863 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46e2ee88-05de-31e1-a7b8-045c52978296 | -11.0804 | -44.12223 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f5c4b5a-f895-3ae7-972b-f0c315e0fb69 | -6.93656 | -59.25243 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24d0f3c8-c88e-3dc7-b816-13bd53392c1c | -8.50511 | -54.60586 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| de7ce564-a2a1-36fd-a191-5fcde6c95aa1 | -13.10164 | -46.35614 | 2026-10-10 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86e89c37-849f-31fb-b600-ac7f29f8ad22 | -13.77291 | -48.13575 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84395f5e-e109-3da9-a57b-7a57fedb310c | -11.89756 | -47.36134 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4aa9da7-a34d-3eb5-a4d3-bd7efb869bc7 | -14.46126 | -43.95647 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea318099-3ad7-37d1-9edf-55632db012e1 | -6.3769 | -56.23022 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ca678ce-5a80-3cce-a34f-7961dbf29255 | -6.67515 | -55.0993 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e5beff9-9532-3cc6-a2ab-4fb95deaf520 | -12.22015 | -44.64293 | 2026-10-10 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7735dc30-4dc0-3a4c-85d6-1e8558feaaca | -10.24265 | -49.67186 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84dc3b72-3247-38eb-83bb-cb2f0658d9df | -7.00729 | -47.66985 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27c21755-a65c-3bc3-a64e-5f0e52a5a9af | -13.68263 | -44.28866 | 2026-10-10 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca281750-8bb4-32a1-8ff2-4b461586d699 | -13.50496 | -48.60373 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a224765-dc65-3586-ab0c-f9d790b7e371 | -13.26312 | -44.00478 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd12ff82-1411-3444-9f6a-83152d31f871 | -13.36292 | -43.89213 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6233d8c1-4271-3cc3-a6ab-34507756b408 | -7.90469 | -54.71989 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e6aa00b-0585-3d92-bcee-bebcd0c8f82b | -10.89907 | -44.79776 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 594c031f-120c-3c3b-9879-be8bb5f7c6dd | -11.36985 | -54.02942 | 2026-10-10 04:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 095c8bdc-c58a-3b0b-b623-507971d59e1e | -11.68504 | -46.85537 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ab1bc33-048f-3a5c-8db4-b29b083ed056 | -13.20448 | -48.13652 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f649cf2-a8f2-3b1b-a49f-67ed8e946750 | -6.93045 | -59.25102 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d1a2fab-ea21-3189-82ab-2ffe43e3e244 | -9.74047 | -57.36485 | 2026-10-10 04:46:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42312411-817a-32ac-b5c8-dc6001d49c79 | -10.35112 | -46.55912 | 2026-10-10 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d1a1af7-740d-3122-9a57-3ae6305c80e7 | -9.78367 | -44.77238 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8b82b45-e716-38a9-8547-21c32c2d260d | -11.84139 | -43.60292 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6d7ccad-0acb-33cf-abbd-9c63489d6801 | -11.08231 | -44.09884 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb2df198-c6fc-309f-9188-ccb577a2dfd9 | -11.59699 | -43.69547 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8060673d-72be-34b3-9950-46235f1f3ee4 | -11.46056 | -43.37641 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8d0131a-60b9-3a12-a0ac-b4e1363ef101 | -7.77975 | -42.31472 | 2026-10-10 04:46:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| afb22a8e-1a94-359d-8e7a-d0298a33d2c4 | -13.35915 | -43.91892 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d8e870c-ce82-3840-8f65-3b4f7d7eee44 | -6.37794 | -56.22422 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9262c1b-559c-3f9b-a0f4-a19837918d0e | -11.38697 | -46.6618 | 2026-10-10 04:46:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d313f85-346e-3431-97ec-d15d8c5f4f1a | -13.26416 | -43.99714 | 2026-10-10 04:46:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ac30fbb-13dc-3ff8-82a0-7661b75f473b | -7.49792 | -55.00198 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4912c6a3-86fa-38e8-bd2f-0e493080435a | -9.31433 | -47.44996 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b86b9f3-288a-3bc3-882b-d7cae5d2dffb | -10.28188 | -43.93598 | 2026-10-10 04:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62d322ab-052f-3833-90b8-548259130068 | -14.45915 | -43.94014 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 510e22a6-53b1-3f2f-a8f8-dc1a200abeca | -13.12522 | -48.58283 | 2026-10-10 04:46:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56fa5f36-7826-3dfc-be42-416659645192 | -10.89638 | -44.81646 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca9e2b7e-7bab-3f64-91ea-810b0e6b4888 | -11.99576 | -43.44643 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2213c5e7-c337-3936-b716-b281a4fdd1c6 | -6.43675 | -55.2039 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 68b3bb25-80d7-3bec-887c-1028e6685c05 | -6.44202 | -52.70799 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed485638-6c0c-312a-84f7-ef5dd708d856 | -11.28732 | -45.19705 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b8c19e4-a19d-3b3f-86e5-8f55453c8bb9 | -7.04167 | -47.66814 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b62ec841-2ccf-37fc-89c3-25d2707b7ca9 | -11.32578 | -46.63369 | 2026-10-10 04:46:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bce2fbba-506b-32ee-ae26-48a9e73cb9dd | -11.90439 | -47.3624 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77fbccb1-8bb4-309e-8a7e-2d59a6563e12 | -7.23592 | -55.17924 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b325aafa-10bb-3b0a-a367-6996456bc354 | -8.49187 | -54.60364 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a770ca0-a211-3fb2-9120-0a32b9e77b65 | -12.03558 | -43.37803 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ce6a2f-bbc9-357e-a360-bedbc5a48268 | -8.40846 | -46.90211 | 2026-10-10 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b757bfd4-92c2-3904-bbc6-db0fa7e13ae2 | -10.44808 | -47.85043 | 2026-10-10 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c3b1e96-295f-393c-9164-02734251b823 | -12.49822 | -51.29509 | 2026-10-10 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a11c81b-0ce0-3344-930d-8105441b7d38 | -14.32534 | -44.65476 | 2026-10-10 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a10fe93-614c-335c-9180-196881fe990a | -11.03349 | -44.02621 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08ee2656-891d-37bd-89de-c356f7021171 | -15.10686 | -43.63407 | 2026-10-10 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3e50b47-d471-3ee7-9f88-2ede5c07d373 | -13.386 | -43.88648 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8f9e118-4881-3763-873e-c4b70a1a8d74 | -11.6021 | -43.68884 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 141e0caa-cdd0-3d69-8a90-93ecaf220f94 | -8.9859 | -47.54019 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37d60f0c-b3cb-3512-b774-f53cf2d83b63 | -9.63313 | -48.87788 | 2026-10-10 04:46:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| caffe620-6235-33d2-821c-e00e47670c0b | -9.01096 | -44.37334 | 2026-10-10 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README82.md)
