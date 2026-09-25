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
| 89a6f02f-5f40-3e69-8d80-9758f83bda9c | -12.17552 | -50.79361 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1910a1ba-1d15-3e6f-ad9c-f4e1097e347b | -16.90537 | -49.32393 | 2026-09-25 04:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d1130d6-3c82-3feb-a642-6a2fcb7cd1cd | -12.01442 | -42.91967 | 2026-09-25 04:27:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| adfe0640-4afb-3016-879c-c30e0835d020 | -10.62052 | -53.99683 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 374f990b-2381-340c-8cea-5782c2bab235 | -13.69466 | -48.79315 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b259cc79-2514-380c-bbf1-c232dfc0080d | -13.22545 | -51.563 | 2026-09-25 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80d40b9a-11ba-3db0-a9c2-67dd3d6273a1 | -12.19353 | -50.79032 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2b82ac7e-75da-320b-bfc4-b856c0a597b8 | -14.51391 | -48.33806 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adb691e0-ffd4-3ea3-a12e-48c50c2e56d2 | -13.69845 | -48.79377 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ef90c73-c676-3f54-b177-04f0c3d11dc7 | -15.68665 | -44.38939 | 2026-09-25 04:27:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71fdc5d2-5a48-39b8-a094-6230ac6c6959 | -10.41779 | -53.78761 | 2026-09-25 04:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b197056-2037-3bbc-957b-c5ee923a765f | -12.19552 | -50.75515 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc2d9aee-3e95-3077-a8dc-e4932c27c7c9 | -11.79835 | -51.01011 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cb201b3-75ae-3a6d-84ab-361e55a64e22 | -13.21727 | -51.5565 | 2026-09-25 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d482b33-4e92-3dbe-bcd4-d4c897b2f8c8 | -12.18316 | -50.79727 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d2a4a53e-bb81-32c8-ace2-93bf06d78c94 | -10.61348 | -54.00327 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbd57251-a875-3f58-80c6-d061a32bbf7a | -11.66853 | -43.75854 | 2026-09-25 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 98e64e50-d2fb-3558-87c3-8ad0001ef0bc | -12.20347 | -50.76108 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 3fcd5b6d-1489-3372-84b6-dfa6c7eeece9 | -14.72781 | -46.22105 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0114fd4a-a691-3599-aa21-457d4692ff9c | -15.9869 | -42.99603 | 2026-09-25 04:27:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 539ea7ee-b100-3f59-b813-6045bcf36d65 | -16.00359 | -56.32312 | 2026-09-25 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 9e5483ad-1ff8-35de-98db-c572d78b1ec7 | -12.20467 | -50.77909 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70cbf3f5-2d81-3671-adf2-2dccbb8d069f | -14.79051 | -48.55109 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb5f4e37-6fcb-3f27-9f1f-34a5d16fa3ef | -12.20863 | -50.75763 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| e4acf5d9-cc6c-35c8-b064-94564f2fccb6 | -11.15377 | -50.65643 | 2026-09-25 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6b2816ec-23b7-3205-b135-fd00136142b2 | -12.22567 | -50.73875 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62f46726-1c13-32c4-a5d0-a4da15294cf8 | -10.62198 | -53.98935 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b54fd7b-863d-3260-abd7-ee3d2a6997b4 | -10.28554 | -49.95153 | 2026-09-25 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3122966c-bdd3-386b-b29b-935da9b9c0d6 | -12.20746 | -50.78851 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 622e0c1e-9774-37e0-a3b5-1271338111d4 | -10.61588 | -54.00065 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8a92c4-c31d-31eb-accf-2a0956991f57 | -14.16852 | -44.84906 | 2026-09-25 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd9bad2d-1dd7-3c9d-9cfe-8b8c72669354 | -10.42397 | -53.78515 | 2026-09-25 04:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f58db293-b782-38c2-a35e-68a20b10de84 | -12.19481 | -50.76165 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32f4ae67-013d-3475-99d8-2d21a0574a29 | -14.72131 | -48.76669 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1abfef1d-497d-3b75-8113-e7a18cfb4b91 | -12.17164 | -50.81525 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30717d1e-55e3-3a3d-beb4-813c302bcdbe | -12.19459 | -50.78833 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 72bdba04-3d6e-3a8a-851b-1c70b2e22404 | -10.88766 | -45.07894 | 2026-09-25 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 859a21d4-1198-3cf4-8107-28f333d4e165 | -14.7272 | -46.22474 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 810b927f-5e2d-3a36-be7a-c863a363e864 | -12.65365 | -43.16151 | 2026-09-25 04:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 45f01973-c245-3fa9-ab29-968218c431ac | -12.21021 | -50.74907 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| eb815837-8f1b-3e4e-9736-24ebfd5f11da | -12.18867 | -50.79613 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9bdf858f-6c1b-30c0-b0cd-65011f716a2f | -13.01751 | -43.62859 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f554e226-cd00-3836-a9a8-73bd0611ce3c | -10.62146 | -54.00173 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af986868-4c3f-3187-b66c-c25bf079d301 | -11.28655 | -54.04195 | 2026-09-25 04:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d294aa5c-8add-3656-b016-6a1286ff7e13 | -12.20298 | -50.74107 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2506443-a055-344f-8b6c-33ca3373cbf0 | -12.53458 | -50.06795 | 2026-09-25 04:27:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb6b7b0a-23bb-3b36-abf2-0e513b1680f9 | -12.18994 | -50.78519 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f4da22ac-7cb0-3996-8fa2-bdf4fb6e61ff | -10.61517 | -54.00444 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 316bd3d2-7d5a-3006-a9df-2282e5b6554e | -12.18245 | -50.75486 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e497ccf1-84e4-34b4-8af2-7dbc6ca514c7 | -11.36888 | -43.39023 | 2026-09-25 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00d40dd0-fdc2-359f-9e6f-def869f5a4d0 | -12.19994 | -50.75819 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23d39f49-eab1-37ef-9438-ed3fb91aa77b | -14.13619 | -43.86195 | 2026-09-25 04:27:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5bc23197-c499-3047-8cb0-c3ba238bb0b6 | -13.77866 | -54.04172 | 2026-09-25 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33fe9bb9-5979-3e8a-9b33-3641aca29cb4 | -12.17878 | -50.79644 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ad3997d1-c559-326c-88cf-1900786348a6 | -12.20426 | -50.7568 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 211a1e05-afdf-32ad-a4d9-560294190322 | -12.18606 | -50.75999 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d10df05-5fdd-3b5c-a93c-0b595c29ca80 | -10.61907 | -54.0043 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb79e010-f803-32ad-8f7b-dd6e679caebe | -12.21142 | -50.76704 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d8b56ffb-43af-3fe3-9433-46ec263bfb5a | -12.19393 | -50.7637 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64786c2f-5761-3291-8350-0b3bfac8807a | -12.17834 | -50.82318 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a7299c4-5dce-3688-8f5b-d6aad3339d6f | -15.87722 | -41.52074 | 2026-09-25 04:27:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fce1a1c5-e4cd-3b46-b3b9-510e691ebe9d | -12.19074 | -50.78088 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 1a1f78ba-6b89-3318-bb60-628075f17d9d | -11.62817 | -41.82964 | 2026-09-25 04:27:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 18eebfd3-fd05-3604-9ccb-31709b2eeb4a | -13.78391 | -54.0429 | 2026-09-25 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30e0fa0e-2efc-34fb-9a7d-0ddda0fda918 | -14.70729 | -48.75889 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb066dd9-7164-3ddb-a46f-c6da46b1414c | -17.10133 | -46.46966 | 2026-09-25 04:27:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52b46476-f5f6-3699-af2a-bb7146497128 | -14.7266 | -46.22841 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c9eb3fc-6560-3dcc-9d01-cef7efc7d3a5 | -14.71773 | -48.76898 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e2ac8cf-6b3b-3380-b93b-4def68b62565 | -12.20508 | -50.80144 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 164603a1-d995-3075-a945-f0f0c6ca2b9e | -14.93938 | -41.33299 | 2026-09-25 04:27:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74a55e94-662c-3b9b-bb57-a4f1aa82520f | -14.67953 | -48.76408 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5e9a41e-7737-30e0-aa70-cf586a27eae9 | -10.6198 | -54.00055 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2b3d026-3158-3ecd-8225-706a288a4bdd | -13.6938 | -48.79808 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27fc5c9d-c017-3df9-ab3b-e8dcdeeb10c7 | -14.73118 | -46.22163 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3bbf624c-2e72-3bf7-9e82-f37946416186 | -12.18476 | -50.78866 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1cc95be1-b130-3fca-8270-7529b89c4233 | -10.90516 | -53.93591 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0375759-2099-35e0-9299-c1dcdd7d0833 | -12.2007 | -50.75391 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a233278d-7e4f-35ae-9a41-d10fba69db01 | -12.18915 | -50.78949 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c81ce220-ac81-3edb-82f0-f292cac41b17 | -14.05307 | -48.40672 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e4711e2-0e62-3613-af9b-0165697c5697 | -12.19557 | -50.75736 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf000c57-7e6c-3737-9929-c3b8333cdd70 | -12.20227 | -50.74315 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| faffe9f4-4ed5-325a-aeae-3bdfffa6e0dd | -11.47203 | -44.21164 | 2026-09-25 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 267f9aac-ae41-3ea8-b198-218d09a1d8af | -12.21179 | -50.74053 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c54a363e-377b-32a6-8e70-e86855e508be | -11.28105 | -54.04079 | 2026-09-25 04:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 898798f9-9caa-3016-b003-7da4cbe1f4cf | -10.62215 | -53.99801 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0512051a-0609-3efb-b6df-f6708f24fc5e | -17.99932 | -44.63094 | 2026-09-25 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c224f4a-cdfd-3714-9597-8b1120ec1f2f | -12.17242 | -50.81092 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d08faa7d-a04b-3bc1-81c1-576cf1997d49 | -14.72963 | -48.76681 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb36fb3d-7d80-3e8a-8db5-4e04e4dd9c52 | -13.06799 | -43.27862 | 2026-09-25 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e1ed4eca-f614-3458-9d4c-deef634ef79d | -12.18876 | -50.76717 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 898b80f4-bf8f-37c5-82aa-0ffd7748dd2f | -9.73432 | -54.80286 | 2026-09-25 04:27:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76d45220-4bd9-3a46-80cf-cc96b0381195 | -12.19791 | -50.79115 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c963cd4-c530-32bf-b95c-402f8623b82d | -10.90307 | -53.94685 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58209550-f34e-3d6e-a1fa-625098e97de4 | -12.21895 | -50.75074 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9d641891-bab6-3d2c-ab99-c4b1cc780519 | -11.61778 | -50.58519 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0358c5c3-a80d-3c77-ab6b-448142f4a430 | -12.21458 | -50.74991 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 416cd251-2c9d-3111-b2c3-de7b462ddf32 | -12.22488 | -50.74302 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26156a37-129f-3d57-9106-245b2d664b6d | -12.21616 | -50.74136 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e9d5b8b-7613-3798-b5b6-5979753c42c2 | -10.6096 | -54.00335 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7fca86a-26b1-389a-9292-ce7e11081fcd | -12.1912 | -50.75653 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
