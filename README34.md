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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09dc3989-e614-318d-89e2-008b46acead6 | -8.09958 | -47.47988 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d1c5404-ce31-35c2-b8a0-958003f6121f | -6.73977 | -59.65995 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61b060f4-b0b4-300f-95c3-bc17e2e6a5d2 | -12.28041 | -44.82864 | 2026-08-24 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a3e4608-e9e5-3ded-ac10-6c540d45d617 | -15.02766 | -48.68837 | 2026-08-24 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9df946e4-00c9-3009-a4b2-25036de03bce | -11.85775 | -51.68274 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f07b0063-d4b0-3ec9-87ba-564e94c60c43 | -13.16736 | -51.39731 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 379fecf2-579d-3de7-aa96-0329d94f5922 | -14.77624 | -48.77941 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 27738cc4-3d46-36f4-b86f-f88d355ab74f | -12.73279 | -48.38851 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e5452d1-edb0-331a-b429-39fe8fb5c452 | -18.69731 | -47.46948 | 2026-08-24 04:46:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81b44b3b-d183-3b30-9086-cf80d1b500f3 | -18.52799 | -47.17237 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3725faba-a941-34cc-8e49-e31efabccc5f | -14.35607 | -51.76201 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a89df7-aa3d-3890-bd7c-557dc9a49f94 | -14.79628 | -48.79087 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9779b61c-c665-344d-89c4-a3fc23f6c113 | -11.55313 | -46.96238 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 567c0296-c674-3a94-b68f-11f0ee1f35fa | -14.39195 | -51.77168 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a832695-4c1e-31c9-8a9b-1bd10822587b | -8.37714 | -46.46997 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c265100-1fce-3d5c-9112-9aec6ffb23e7 | -13.18147 | -51.47945 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb8fd9db-8c45-33fd-8b3b-81835a54e14b | -6.79077 | -59.81541 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e0e897b-7ec0-3bb5-ab11-665d3b69ca58 | -12.86712 | -48.48223 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e22356b6-cc1a-3bb8-a12d-4d364f68a583 | -10.43139 | -50.46556 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ef113d4-4184-349e-bdde-146a4022c118 | -11.86051 | -51.68684 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f02d1d3-e17d-3ddd-8533-2ac79f552d2f | -12.22541 | -43.17572 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0c38f0bf-b639-3b72-b600-b25796ede6b0 | -11.7837 | -47.2589 | 2026-08-24 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91cab0aa-0cbe-3fa3-93d1-e733539d77ce | -11.85385 | -51.68573 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3211174-4dbe-3a64-8734-6bf58eaf62f7 | -12.09173 | -50.59621 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0425b45d-6757-3c83-9973-a6956e3f29fd | -11.58906 | -56.28963 | 2026-08-24 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1094bb7e-752e-3ea4-86cc-32fc823cbe0e | -12.74298 | -46.45985 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3e50c0b-3b7c-3d9e-b327-dcbcc6f23c81 | -19.08194 | -47.14074 | 2026-08-24 04:46:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0f0d27f-0edf-3892-9ab1-dc8aeb4ef6ad | -12.10499 | -50.59837 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32a8481c-3534-32de-a149-eb348060e48a | -12.08896 | -50.59224 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7fc45536-9d6d-3d7c-94af-e3853bcd1d66 | -12.71619 | -48.40302 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa3fe72d-e491-30ce-86bc-e8786599f158 | -12.27423 | -43.13037 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 14533ce9-09a5-3624-ad28-454e29a1aa91 | -11.20572 | -55.08001 | 2026-08-24 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b11b0e8-3de1-31b3-95eb-930a8a5ec802 | -10.80753 | -50.94255 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8152dea-a0b9-3787-87c5-2dd8adb0c44f | -19.89349 | -43.88149 | 2026-08-24 04:46:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6144ba89-5c31-3c59-8f2e-49f3cea897d3 | -11.8511 | -51.68163 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34f65101-0f89-3c5e-81ee-9e68a8062ad2 | -8.1089 | -47.48932 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 449fdda2-1f45-393f-bc3f-55f724032d2c | -13.17398 | -51.39841 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26dc33a2-0937-32b9-abbf-7fbbe658ac71 | -12.09946 | -50.59032 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef76bd45-4822-3c2b-99c7-c477c4edeb5c | -12.07456 | -50.57582 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcdf6739-a775-358d-98a4-98ba3e2bf972 | -7.49195 | -55.34023 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d740a794-4eea-3a46-b7c3-cb91bd0eb671 | -10.6285 | -52.25504 | 2026-08-24 04:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6c6293ae-e24d-3392-9d02-979403fa8fbb | -14.77567 | -48.78337 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bbf1a5a-b855-35c6-9b32-2fca70c22b52 | -6.63322 | -58.48376 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94c2b3ae-927e-3052-8281-618393e84e58 | -8.09276 | -50.04696 | 2026-08-24 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 910bb189-16a4-3d51-aabd-cc8216bcff4d | -9.72691 | -46.82546 | 2026-08-24 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1406cc92-3bd2-3644-94dc-3a2008236f32 | -19.76344 | -44.2464 | 2026-08-24 04:46:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| caac0f18-1bd2-33d3-b3d2-fceddbd0e7a0 | -11.11279 | -49.88553 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b531b9e3-8215-37c0-8182-98f9cb7d8e8b | -9.33508 | -50.35338 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53f8a935-5041-3129-a25e-ff1058dd268e | -12.86009 | -48.48115 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1d4fcac-f7ec-3b4a-bdaa-60e2de5f0d61 | -19.89313 | -43.88491 | 2026-08-24 04:46:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66027ed4-b2a5-3fba-99dd-dd787b3bfbe4 | -12.08952 | -50.58871 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3ec369c-53f9-31e0-899e-19e334186e85 | -10.6331 | -52.24824 | 2026-08-24 04:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0aaa127-3ee7-3de7-8e7e-1566191b234b | -10.46353 | -46.22318 | 2026-08-24 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b55f34a5-617b-364b-a6a3-f41f76f9f257 | -11.61931 | -51.09274 | 2026-08-24 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5caac9bd-2ebd-3853-b371-be387ece538d | -12.10388 | -50.6271 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9e3d401-7602-3fb8-8180-2e2545db4037 | -9.46495 | -56.9257 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb981f89-c6fe-3cec-b369-648ed992c593 | -12.09173 | -50.6179 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d84df367-b3db-33ac-b1bd-8599387112c7 | -13.68788 | -51.84028 | 2026-08-24 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5d20695-163e-3775-919c-c6edc687c6ac | -6.80537 | -58.66751 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2367a91-efd5-3355-a1fe-b9797ef25acc | -8.34048 | -47.70504 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c078bcbf-fafa-3013-be89-c6747fbefc93 | -10.534 | -50.78289 | 2026-08-24 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d49fd79-7313-3ab8-a342-3e7b8e3281d9 | -8.10917 | -47.49244 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ba62d19-8e15-3611-8bf7-6d5ce475655f | -10.30048 | -48.20542 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f807405-b3d8-37f3-b9bb-11264bf313c2 | -12.60568 | -52.45744 | 2026-08-24 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e801e545-7bbe-3b20-be49-7f4eee192075 | -6.85626 | -59.41534 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 683cecbb-9cd6-3d37-8bf7-b222c23d8293 | -15.06716 | -45.32497 | 2026-08-24 04:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e79a9fe-5228-3672-9e5a-4ce7d834bad8 | -8.54839 | -54.84583 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e6331da-4d20-3b2f-8e0e-1e67576a07fd | -13.44876 | -43.84573 | 2026-08-24 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 060662bc-be66-380d-a4ce-d307ac956be9 | -12.09836 | -50.59729 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d57cc013-2354-3548-b198-eefac3d8475e | -14.92473 | -51.06332 | 2026-08-24 04:46:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84444f65-4d0e-36dc-8b51-2fbc609c703b | -9.46574 | -56.92123 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b6524c-1b63-31a0-b81e-d354407dcb05 | -9.04824 | -50.76812 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d3b6db0-5884-3fe7-9316-2da05b2b0752 | -12.21161 | -43.16813 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de16bf93-3386-3a6b-8751-f2768c129f84 | -12.10333 | -50.63063 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e89eba-2aa2-3737-9d49-27c099d211f8 | -8.5386 | -55.28265 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5907f229-db5d-3460-bda8-6525bab880f7 | -14.80165 | -48.77887 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55e51ecb-0ba2-357e-9db1-ae571b18b615 | -10.47093 | -49.51854 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5e4a3ba-355c-3991-91bd-b85147ce8572 | -6.81291 | -58.65566 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f117fa4b-1059-3ef1-a7ea-f476a1394541 | -8.5752 | -49.98155 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f862f00a-2f95-3523-8cd9-95a05cc7ae4e | -12.09891 | -50.59385 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfec6fa4-89db-3040-a47d-a44d31f7fa63 | -6.8569 | -59.41172 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e977137-1850-3c1a-924c-dbc89f517ae8 | -6.81816 | -58.65646 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72a60450-8b7c-366b-9c42-bc9a8ef5acb2 | -10.79979 | -50.94848 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c908b72d-2cd5-34f1-9d08-efdc94e020dd | -6.54624 | -56.17258 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fc320f0-a900-3c66-8796-8682217cbb79 | -12.09947 | -50.61192 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0f0c40f-67b1-3840-b695-eb1b310bf9d3 | -14.79165 | -48.77303 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6523baad-274a-34a4-9bc7-f6bde9c53012 | -10.82884 | -50.55112 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61050758-66ff-3369-b234-6686e12928b2 | -12.10831 | -50.5989 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e9c1d7e-d632-3646-8676-278fff37dbb7 | -6.78496 | -59.65385 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532b9676-cc45-394b-be15-b95bdad9cd7c | -13.15798 | -51.39213 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de7debe3-7c16-3dae-87bf-b1639893c452 | -12.85139 | -48.49136 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f74c6eb9-1fdc-3132-8ab5-f2cd04e3fcec | -14.31518 | -51.76245 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0994bfef-9f8b-325f-a84a-d3ea1ec09416 | -9.46941 | -56.92642 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04407e00-4386-354e-b38e-abe76ba4bd08 | -9.17828 | -58.07376 | 2026-08-24 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7fc38fc-f737-3224-a15c-79c68d2a38d8 | -12.07787 | -50.57636 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2e11b62-50e7-30ea-96ab-26a0779a8eb7 | -12.27113 | -43.19463 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 424cd878-5d55-39f4-a2f0-b6e706c549bb | -12.89058 | -48.46955 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65b9ee30-3391-3e2d-b326-e23c6543ab60 | -19.04396 | -45.00107 | 2026-08-24 04:46:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bc1139a-6efe-3e54-9891-626fff42128a | -6.6118 | -58.38551 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ed2e39b-57b5-3b13-bfea-9730ddef08df | -12.11328 | -50.61055 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |


[Clique aqui para ver as próximas entradas](README35.md)
