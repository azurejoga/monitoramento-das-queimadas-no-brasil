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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df300ea7-88b8-385a-b766-036691a58925 | -0.50313 | -49.14719 | 2026-09-25 12:02:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8a14ab03-307d-309d-8c86-60233ba1558f | 2.10983 | -50.69854 | 2026-09-25 12:02:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 16f9cfc1-8db2-36f6-ae84-93e1e405fba5 | -1.56942 | -47.63098 | 2026-09-25 12:02:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 6c3b3695-d8d7-3369-a520-acac1f3d32fb | 1.58573 | -50.90638 | 2026-09-25 12:02:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ca9daec5-8c20-34b5-b261-73654084bda0 | 1.2906 | -50.84089 | 2026-09-25 12:02:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 82e6fbe9-14d7-34cc-ab53-29b8be69a024 | -0.50176 | -49.15673 | 2026-09-25 12:02:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6d141b20-5b6c-350a-85e0-9245cde253b7 | -3.20451 | -53.41568 | 2026-09-25 12:02:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| c4d7351d-72b7-3536-904c-a5c599290cbc | -3.2059 | -53.40606 | 2026-09-25 12:02:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e0cd42c5-cedb-3d2b-b932-d204044c05b9 | 1.58279 | -56.00844 | 2026-09-25 12:02:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bfa38dcb-473a-3eb4-8a7f-ab820a2af2e2 | -3.96902 | -43.10559 | 2026-09-25 12:02:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 2657104e-7905-3249-ab72-8e9b679479ed | -0.51093 | -49.15799 | 2026-09-25 12:02:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 7852d503-0e4b-394d-9593-e828cc73ff49 | -1.56983 | -47.63726 | 2026-09-25 12:02:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| b4587872-729e-3308-a307-ffce4339afd0 | -2.90301 | -54.09155 | 2026-09-25 12:02:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 06cbfb99-1d49-3623-8362-a8e9f61ddf75 | 1.42036 | -50.85228 | 2026-09-25 12:02:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 90ed928c-6aba-3b58-9b8b-f4e411dce82c | -3.21512 | -53.40738 | 2026-09-25 12:02:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6413cf20-3b79-3f2a-89a4-adce57e38f2b | -1.57155 | -47.62531 | 2026-09-25 12:02:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| a379b919-0ae0-3083-bc94-3eb1a9f667e8 | -1.56779 | -47.64289 | 2026-09-25 12:02:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 617799dd-e789-3809-afc4-fdcfddf868c9 | 1.87377 | -50.66967 | 2026-09-25 12:02:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 784f5442-fa73-3bfb-bb0b-69c308a2acf0 | 1.55945 | -55.92682 | 2026-09-25 12:02:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 991678da-5bb0-3554-8d97-238e464274c5 | -2.86853 | -49.62917 | 2026-09-25 12:02:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bada4259-adda-340d-a66b-8a7620cc7c7a | -12.01582 | -47.80201 | 2026-09-25 12:04:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 3b8630b9-99ba-335e-8a4b-0e8ba90bfa48 | -12.04056 | -50.70213 | 2026-09-25 12:04:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 4b6f0be0-fc0a-312f-9fd1-b2a58dea223d | -11.9011 | -55.51721 | 2026-09-25 12:04:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e579f363-9218-385f-8273-b1328f096da0 | -9.01704 | -44.84924 | 2026-09-25 12:04:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 54aadae0-74b4-3e84-9222-fb136167d861 | -10.31173 | -54.22702 | 2026-09-25 12:04:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a1605cbf-2049-37a3-af12-7ed1f7da960c | -10.62263 | -53.99133 | 2026-09-25 12:04:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c4d7d093-cc56-369d-83b3-9b3c21b31d1b | -12.45017 | -54.11489 | 2026-09-25 12:04:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6a5159b3-f1df-358f-8aa2-a008a521897a | -12.32766 | -52.58939 | 2026-09-25 12:04:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 523ded4d-a362-313c-b195-b9fdc891149a | -11.71974 | -50.56878 | 2026-09-25 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1ed63117-a348-3dd7-a9d6-3b869f96331e | -11.2728 | -51.28965 | 2026-09-25 12:04:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| e9ebb013-2369-30b8-b897-01dd727f06f9 | -11.71829 | -50.57957 | 2026-09-25 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 2957639e-6d8a-3c58-95d4-2625e70cb6e2 | -13.21547 | -51.54988 | 2026-09-25 12:04:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e9852730-be9f-3865-98c5-fc7654f19da0 | -11.78447 | -54.25199 | 2026-09-25 12:04:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3325db99-1943-3f57-8eca-a1ab323f0941 | -10.62131 | -54.00045 | 2026-09-25 12:04:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1962c130-914c-3585-bee2-b640273ad69c | -12.19111 | -52.77721 | 2026-09-25 12:04:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 20c3eaff-89a2-378f-8968-013ee18fd8a4 | -11.62771 | -50.49532 | 2026-09-25 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 220ab823-87f6-3924-bcbe-d77155703803 | -10.31038 | -54.23631 | 2026-09-25 12:04:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cfddf90b-90f7-3ae4-8dcc-e55ef6b68919 | -11.69224 | -50.55411 | 2026-09-25 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a33522f4-8f40-3067-b501-04731bf183e7 | -11.27145 | -51.29945 | 2026-09-25 12:04:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| cb8f9f2e-dbc0-3865-91e6-cd456f77e7bb | -11.7858 | -54.24284 | 2026-09-25 12:04:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| be39fdd5-7b11-39b6-9a0a-41be4ba5d434 | -12.76499 | -52.8221 | 2026-09-25 12:04:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a54259b-72c8-3567-8935-c995dff80d35 | -7.86517 | -45.54942 | 2026-09-25 12:04:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e2d6a8db-b65c-3953-994f-556f29ca3fb8 | -13.7324 | -50.79489 | 2026-09-25 12:04:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b1f61018-300c-36ee-a502-e585d216b7b3 | -12.12967 | -50.25268 | 2026-09-25 12:04:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 00eccb28-0f9d-3b84-87d1-c73280d2f176 | -12.9045 | -47.22723 | 2026-09-25 12:04:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 12c9b7f7-d0d4-31df-a557-c71f9822d0d1 | -11.28067 | -51.30072 | 2026-09-25 12:04:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6bcb10f4-fdf7-3f5e-bee1-639f4fe795e8 | -13.46049 | -48.62972 | 2026-09-25 12:04:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4934a679-5177-3de3-b11f-6eeab4ddcaa5 | -17.42959 | -53.12882 | 2026-09-25 12:06:00 | TERRA_M-T | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e7883442-616f-33e5-9b94-e3cf75c822a7 | -16.78151 | -51.36818 | 2026-09-25 12:06:00 | TERRA_M-T | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f52a9660-bdf1-3f4b-9528-8173ad3ab9a9 | -18.12214 | -54.51775 | 2026-09-25 12:06:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1a820ee-a1a1-398b-ac42-9ceff476203d | -17.1146 | -49.24709 | 2026-09-25 12:06:00 | TERRA_M-T | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| dff26158-b6df-3475-97aa-290a4b72c6f7 | -14.57156 | -54.11849 | 2026-09-25 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b55f76b8-744b-3170-861f-dafd7c26fbd8 | -15.30157 | -48.82011 | 2026-09-25 12:06:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0ab65241-a70a-3579-9c43-1df00c53708c | -18.90297 | -47.54976 | 2026-09-25 12:06:00 | TERRA_M-T | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d87c71c7-91b5-3e20-a2a6-b68e73a4a704 | -18.89469 | -47.5424 | 2026-09-25 12:06:00 | TERRA_M-T | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f6a57297-15d5-34a4-a5f9-96daad140056 | -14.57026 | -54.12754 | 2026-09-25 12:06:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 621e5724-d0c4-3511-b619-b607fb38910a | -14.83167 | -54.31166 | 2026-09-25 12:06:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| abec3afb-8350-31ba-a339-9ccb248b035c | -29.14826 | -51.23154 | 2026-09-25 12:08:00 | TERRA_M-T | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| d5c76d4c-d107-3c33-85a1-8f50aea5521f | -29.63523 | -51.72429 | 2026-09-25 12:10:00 | TERRA_M-T | TABAÍ | RIO GRANDE DO SUL | Brasil | 4320859 | 43 | 33 | nan | nan | nan | Pampa | 11.4 |
| 9db57a0d-cf9f-30da-9d15-5cda3f2e9249 | -13.2253 | -51.5466 | 2026-09-25 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 10dae066-90b0-38e6-bd91-4733e4babc0c | -13.2061 | -51.549 | 2026-09-25 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ea15741c-b5c6-37d5-925c-85647ea3edbc | -13.2061 | -51.549 | 2026-09-25 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 49e1785c-05a3-39ed-8bc6-6413b5bb8f04 | -13.2253 | -51.5466 | 2026-09-25 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b3f1dbfe-83b8-3db9-b719-9f0dd50bc9bf | -13.3827 | -51.2924 | 2026-09-25 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 01ffe16e-ed43-3417-a3bd-067a2e980568 | -13.2249 | -51.5679 | 2026-09-25 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9b57be0d-1182-3b57-ad10-cf7d9728b9d2 | -13.3635 | -51.2949 | 2026-09-25 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 78d29b97-0228-3bc2-9a7b-56738cdd562a | -13.3824 | -51.3138 | 2026-09-25 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 385.7 |
| 0c0b6796-2728-3b3e-84d0-9e1d7bd5665e | -13.3632 | -51.3163 | 2026-09-25 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b7c8f625-0034-3b0d-b366-e443af671e2e | -13.2057 | -51.5703 | 2026-09-25 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1188c10a-8e6d-3f8d-8fde-acba6371ab03 | -13.2784 | -51.8162 | 2026-09-25 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c5338ad3-1546-391b-856c-068349a72328 | -6.2767 | -47.5631 | 2026-09-25 13:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 108f16fa-e61f-34b0-94a5-011afcf9ee7a | -13.2253 | -51.5466 | 2026-09-25 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a7b85a10-0250-3706-aa07-8366a152e90b | -13.2249 | -51.5679 | 2026-09-25 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 51eb7916-e193-3357-b635-a9150202e3f1 | -13.2061 | -51.549 | 2026-09-25 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 46c9b801-3378-34f6-a0e4-f28e96a81a83 | -6.8985 | -41.6976 | 2026-09-25 13:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| d7b41629-4289-33e7-82ab-6584a369e1d5 | -13.2057 | -51.5703 | 2026-09-25 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| aab57178-9468-3b8c-bcfd-08ff375610be | -13.2249 | -51.5679 | 2026-09-25 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| ab4fabd0-2192-3a1a-8cd2-cae471265deb | -13.2061 | -51.549 | 2026-09-25 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7ce4c099-30d1-3ea7-9fb9-1e3da9c8acef | -13.2784 | -51.8162 | 2026-09-25 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| f42a50a0-21e5-3dc3-b210-41525887c5fb | -7.6696 | -67.1451 | 2026-09-25 13:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e1837bf4-d145-3eca-b4e9-c17e327d63f1 | -13.3827 | -51.2924 | 2026-09-25 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 4aca9855-f30a-371a-8357-eee4cea369ba | -13.3824 | -51.3138 | 2026-09-25 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 276.3 |
| 106a3585-cce0-3289-bfbd-07b5a24266a9 | -13.2253 | -51.5466 | 2026-09-25 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| feac3f0d-00f6-368e-b1d9-612a3c10f6b7 | -12.2241 | -50.815 | 2026-09-25 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0cb638d0-f751-3ce3-b87e-10501240caf1 | -13.4672 | -48.6324 | 2026-09-25 13:40:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 14710aeb-0e69-3094-b984-5a1807dbca3c | -9.3717 | -66.5077 | 2026-09-25 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 15605084-c847-37bb-a675-84773bbeeef7 | -7.67504 | -67.13687 | 2026-09-25 13:42:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 442b5986-6247-3feb-8a0b-f8067ce99f57 | -7.67109 | -67.12952 | 2026-09-25 13:42:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0d783bfc-7f9e-3dbd-8780-38754007cf6d | -12.3478 | -50.221 | 2026-09-25 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6f47df26-928c-32a0-b670-c0234e949af4 | -12.3481 | -50.1994 | 2026-09-25 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 14780ccd-73ca-337b-b297-baa6884dfdfe | -7.6696 | -67.1451 | 2026-09-25 13:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 078cdea9-75d2-32b5-91a0-a3ab4334c610 | -13.2249 | -51.5679 | 2026-09-25 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b72154cf-693b-3c4f-9c4e-85a5ef2aca9d | -13.3827 | -51.2924 | 2026-09-25 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ca31b463-c68a-390a-806d-be7525c1619e | -13.2781 | -51.8375 | 2026-09-25 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1dec64fc-cab0-3d55-8402-c4c01a9d6ee1 | -12.7699 | -51.3043 | 2026-09-25 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| cfbbe7f6-42b9-33c4-9c7b-5d9a3bdfcdd3 | -13.2061 | -51.549 | 2026-09-25 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b3921124-0711-3e58-893b-01a1ab0dd4d5 | -13.2057 | -51.5703 | 2026-09-25 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 88700146-ccd0-34c9-9ec7-fd2931553cdc | -13.3824 | -51.3138 | 2026-09-25 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 9459c404-73be-3866-9936-bace6d02aa97 | -13.8151 | -51.8553 | 2026-09-25 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 77206653-c52d-3ac2-8c07-93436ffa3f14 | -13.2253 | -51.5466 | 2026-09-25 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |


[Clique aqui para ver as próximas entradas](README41.md)
