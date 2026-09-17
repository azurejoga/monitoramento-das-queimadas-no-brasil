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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fa04312-4aa2-3dfe-9974-664b5400adaa | -12.45809 | -50.79953 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1d8955c-3406-3b53-93fb-abf7397326ee | -12.46853 | -50.77597 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5fcff366-bb57-3c9c-be18-3361343710e1 | -14.18472 | -45.1489 | 2026-09-17 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53cbe734-770a-3bc2-81f8-137019be502a | -12.50357 | -50.70557 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ad9f9aae-6446-31ff-8cc7-fb23e710487f | -12.44543 | -50.81554 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cac5dfdc-c4fc-3353-9879-290cd22a0049 | -12.47193 | -50.86304 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1d69c65-2122-32ad-96c0-c64fe9ee748a | -12.10841 | -57.19984 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7341f170-a223-35ff-b073-adcd2c962b7e | -12.45915 | -50.77085 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1945a78-8a54-3bb3-8a44-c73ac2b9ddd0 | -12.44712 | -50.84824 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0487af6f-91e6-31e1-9824-070fe5530085 | -12.47238 | -50.77298 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2a799728-1385-39bc-b682-9b210f890557 | -12.47626 | -50.79163 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2edd691-4da9-39cf-b43e-ca803523265b | -12.48449 | -50.7605 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6387fd65-edb4-380e-acaf-63912841c82b | -12.46532 | -50.86198 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86770fdb-be92-3c76-8547-1f24d42b718f | -13.60915 | -46.94232 | 2026-09-17 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ce34f1f-1fa8-3c2b-b2f0-ad06bd2e0a7b | -12.45595 | -50.85687 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87badb14-76ba-3e7f-a461-73d6e5cb0dcb | -12.47845 | -50.77756 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d10b6ce6-4776-3689-bc44-d65ae22093ed | -12.46082 | -50.78194 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36e9291c-da3d-3f07-8417-2effda02cef5 | -12.46972 | -50.85548 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd9b6571-ed2a-37a1-a42e-ffc7c2432074 | -12.46199 | -50.83982 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f988e6c-4833-39e0-b2fa-d1077145aaa9 | -12.45485 | -50.8639 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0af0bc60-fab5-32ef-9880-326e770a7a3c | -10.27672 | -60.53694 | 2026-09-17 04:42:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dafe39a-6408-3c0c-99a7-f2fdb5b68786 | -11.98721 | -52.46449 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d68092d-dc6e-3827-88aa-e14107195b35 | -12.47134 | -50.8233 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e5234b-fab9-3a5a-ad29-fe810758bdb5 | -12.48014 | -50.81029 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b2efede-f425-3c89-b52a-f722d4badde8 | -12.378 | -48.45882 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23bbc269-413a-306a-8180-670ec7810a11 | -12.44322 | -50.80797 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2ca560f-f1b4-3cdd-8104-7987ce966bef | -12.44988 | -50.85229 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d95d0b1-ab11-3b39-b042-b9f309152149 | -12.44324 | -50.8296 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8bdaad7-93f9-3fb5-b640-50c16b50a972 | -13.65121 | -43.74609 | 2026-09-17 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82ac21ee-1917-34d6-bfae-e939a9b7bd81 | -12.46365 | -50.8509 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f56c1c3b-893c-3b46-b03d-b6d58ccb3a67 | -12.45202 | -50.79495 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a68cbef-117b-35f3-8044-5a5f8ca20ff4 | -12.46358 | -50.78599 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3a959c2-2c6c-3c0a-aa3f-a3753553feb4 | -14.82072 | -59.55333 | 2026-09-17 04:42:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 572ab83f-bb25-3cf6-9b2f-47d49d2ed00a | -12.46311 | -50.85442 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d78b1dbc-945d-3050-89cf-d3ce7e48bec3 | -13.35276 | -48.47149 | 2026-09-17 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14a09bd3-d1d8-36e4-891f-4bf80c1a3625 | -12.78152 | -51.27758 | 2026-09-17 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1519d50-80e0-3fcb-8d4f-ed8f669ece94 | -12.44655 | -50.83013 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32cdc5ef-aacf-3810-8a09-ba58cbd72069 | -12.42604 | -48.48178 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5ba8748-6ddd-3ab4-9b9f-5a0b81f7407f | -12.48016 | -50.83193 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8388deb2-dfc5-3ca7-a717-86e0de6b920d | -12.7158 | -48.27734 | 2026-09-17 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45904640-8e7f-3025-822a-5d520a274ba0 | -15.47043 | -53.77828 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a236734-80cd-38c8-a00d-0d7ee7c032bc | -12.37683 | -48.46671 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34000d38-b5c6-39de-8d0f-2e9739de96ff | -12.43303 | -48.48282 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8eb60401-26bb-39a6-9a06-26b5fa601431 | -12.48943 | -50.81876 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12e71eed-9e67-3795-bb3f-6e4036e59c7b | -16.30977 | -53.84745 | 2026-09-17 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c668c99-4527-3a6e-834c-818ad11c59d9 | -12.4554 | -50.86039 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2688d27-7607-30f4-9f9a-7f74b16262e6 | -12.49001 | -50.7686 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ad50e69-98f3-3d6a-9a79-1a7e11ebc2b1 | -15.467 | -53.77768 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c28a72a-f034-3156-a7bc-b8102e42ebb0 | -12.4867 | -50.76807 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19ae3402-e4c8-332b-8aa6-f28c75b23f43 | -12.4042 | -48.47493 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69eff316-f018-3e35-8857-859c21187915 | -12.44379 | -50.82608 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 890afbce-a161-3850-b81f-a6c98638925e | -11.98603 | -52.47185 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4e99e09c-f333-353c-8f46-46d61715fba0 | -12.44598 | -50.81202 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f3279437-c156-397c-ac83-78f31bd3edd2 | -12.49267 | -50.776 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fcfe714-b439-300c-85fb-4ccc794f4333 | -13.68248 | -48.58942 | 2026-09-17 04:42:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ccea65a-1722-3263-974e-d03b0f9d31e0 | -12.47352 | -50.80923 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef987ab6-3111-3b2b-b39d-91196f05faaa | -12.50412 | -50.70205 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 194f8990-7c43-3bdc-bc77-fa877373dcc4 | -12.46139 | -50.80006 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a4a6667e-3366-39c1-9d49-0f0c126909fa | -12.47357 | -50.8525 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a24f6ab-5061-3e79-a1b3-055f0e05c406 | -14.18417 | -45.15322 | 2026-09-17 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eed01505-7ca2-33b2-baea-de3e2b3864fa | -16.8547 | -45.42876 | 2026-09-17 04:42:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ade2df57-676b-37a7-a34c-476a52ca26fe | -12.10995 | -57.1913 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 476b427f-b4ea-30bf-a5d3-857ba0bcad30 | -12.85154 | -44.38796 | 2026-09-17 04:42:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 468d2577-135b-3cbd-b923-4976dbc1261b | -12.45649 | -50.85336 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2195e519-986a-3550-ba40-5f36ac3e422f | -13.5829 | -45.47165 | 2026-09-17 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3058f07d-b14d-3623-a2ea-5c478ef01a89 | -12.46191 | -50.77491 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af949613-7ec9-337a-a89b-73ca66b4797a | -12.46862 | -50.86251 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0466ae57-45bb-36f7-b492-409426290f00 | -12.48394 | -50.76402 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 272cac80-dfbb-3e8a-a15b-537af7b196e6 | -12.47521 | -50.84195 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63014d8d-22ac-33d0-972c-536a6b3d31ee | -12.47959 | -50.81381 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb832d09-0156-3584-a248-4969602bfb45 | -14.57171 | -46.59695 | 2026-09-17 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 417fe3f9-7f06-3667-9197-2b7a1e4713bc | -12.45095 | -50.82363 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84f7ff4c-5894-35a7-9367-609b2528b67b | -12.46917 | -50.859 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a7f6a79-a033-31f2-9b76-562d1d7b0189 | -12.44876 | -50.8377 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfe164d7-4fac-3fb8-b117-f04641c75b37 | -12.47017 | -50.76542 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2c081e3-bf95-3c5d-ba1e-4e2bcbb9fc9d | -12.45207 | -50.83823 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f57b6c8e-743e-3ea5-8a33-6a6cc12c3a5a | -14.33131 | -48.93024 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e871b3ae-37d9-3bbd-84a6-c3c23aa148a7 | -11.49673 | -54.47058 | 2026-09-17 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a6eec0a-1b86-3076-8592-5df8cb951abd | -12.46089 | -50.84685 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc59be1e-05fe-38c4-81fe-ae82b8b012e5 | -12.46194 | -50.79654 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e794590-901c-3e43-b2e0-be326b3342da | -12.99125 | -44.83565 | 2026-09-17 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a1b6f53-f031-3cc8-8b9b-a3cba72f5879 | -12.47077 | -50.80518 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 118dc2d4-1813-38b1-bf38-ffab58c6d969 | -16.86615 | -51.39874 | 2026-09-17 04:42:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67ac8bd4-ee93-30f3-9f14-8dd524502f91 | -13.15806 | -43.24611 | 2026-09-17 04:42:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4b056621-65f5-3198-9287-4e6476a0b028 | -14.23378 | -48.62826 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4cebf966-7045-300c-b9fe-08d57b6fd737 | -12.48834 | -50.75751 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33be9d2c-9eb6-3932-91a0-e8fcbd8fcaf2 | -12.4597 | -50.76734 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29d1532c-ee45-35b0-a8e7-8c9f5ca39c97 | -12.47027 | -50.85196 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8329389b-8519-38e3-b3cb-f0f35455c18b | -14.84298 | -59.54154 | 2026-09-17 04:42:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbe34ab4-a8b0-36cb-96cd-9ab42a7129e0 | -12.41498 | -48.48411 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2c9055c8-cddf-3843-ae5f-b0fb84e2aedf | -12.45423 | -50.80252 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0761a1eb-7884-3157-a234-0babc853a841 | -12.46256 | -50.85793 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 576ab7ee-657a-3ab9-9ac3-34d13b1f1a06 | -12.47248 | -50.85953 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01a187ea-628c-36da-afaa-14953879e0a9 | -13.60075 | -46.9467 | 2026-09-17 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08d36ade-f1ca-3010-b408-a56104ca5ab5 | -12.37741 | -48.46283 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10a16c6b-50bf-3424-910c-921d2a0d6a70 | -12.47688 | -50.85303 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65d50bcf-dcab-35fa-8443-96de9415db10 | -14.56238 | -46.60622 | 2026-09-17 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5d9769cf-424d-3b44-be6f-a80f42610975 | -13.3563 | -48.47197 | 2026-09-17 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67bf7964-1665-3302-9bd4-3462bd1b7e2c | -12.43711 | -48.47931 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68026c97-b79c-3efb-9599-a3253494c8ed | -12.46798 | -50.77948 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README51.md)
