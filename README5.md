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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d7e1745-3389-3307-85e0-067b4d337e23 | -9.01648 | -40.26719 | 2026-07-24 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3baa0f2c-cac9-319a-bc89-d3c09194b326 | -12.66034 | -48.20139 | 2026-07-24 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d93205c3-320c-30a0-acc0-e0b4e75209ce | -8.71503 | -54.54626 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47718e03-3ad6-3d53-89d7-5ac613296963 | -7.43219 | -46.88542 | 2026-07-24 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 721b7ff1-bf75-3f12-8b13-915c2590e4d9 | -7.00832 | -45.43396 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 73699181-9090-3ecc-a5a8-7647a7bdc59a | -9.17133 | -58.32246 | 2026-07-24 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a7f080b-f93c-33d9-b23d-3fb89e7a3365 | -11.62087 | -50.147 | 2026-07-24 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdab7115-eef6-3659-a442-2617ed10c278 | -7.43278 | -46.88174 | 2026-07-24 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 096854ab-501f-3d71-918d-19edfa3549ec | -11.40313 | -47.4805 | 2026-07-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 171d9ac5-cfd7-3bbd-a689-fba2d92ebecb | -12.44937 | -49.58694 | 2026-07-24 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc2804de-6113-381f-b754-72bea187548e | -7.01494 | -45.43503 | 2026-07-24 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 204453d4-64be-3021-ba51-f97747b24b4b | -6.29577 | -47.70593 | 2026-07-24 04:25:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c3d8c74-2d7d-3282-838f-9464ae4d8c3c | -9.15685 | -58.32602 | 2026-07-24 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0e7978a-6215-337a-aee6-0a3e4fbdec53 | -6.56783 | -55.143 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 00ebc6ff-8df3-3c1d-9fec-f340c4abf009 | -7.30565 | -47.01728 | 2026-07-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b32b55f2-8366-31ff-80a4-cd747bb580d1 | -6.56548 | -55.14683 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23ccc614-7ef0-3d3f-b4ad-94ee98bf8ff9 | -7.1473 | -48.6786 | 2026-07-24 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3dd6f7d-9a1e-376a-a75a-99ee4e5a0afb | -12.66096 | -48.19759 | 2026-07-24 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42d272ef-d646-3f1b-bf6b-12f7efa4c20b | -11.40708 | -47.4775 | 2026-07-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d82a7248-d557-3043-9f65-6f672efddcd6 | -6.56621 | -55.14272 | 2026-07-24 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0163c47a-4084-329a-9bcc-924ab2c8185d | -11.58475 | -48.39706 | 2026-07-24 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dcf0b95a-4298-3bb7-b315-74603e03906e | -7.30504 | -47.02102 | 2026-07-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d85d2d4-94f5-349b-a83a-f37eddd79755 | -9.52419 | -47.12076 | 2026-07-24 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feeeb61c-bb1e-3096-acb0-58850e8ed6e8 | -11.5854 | -48.39317 | 2026-07-24 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7b9f32d-51af-3131-a650-0135941a3367 | -13.45064 | -51.5223 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 53881a1c-46c4-380f-8fae-85d1e6dc4f2d | -14.3751 | -50.33159 | 2026-07-24 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d50a248-e428-3a0b-b2af-3d1d21f025ad | -21.33365 | -44.22446 | 2026-07-24 04:27:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c2e705b-efc9-3669-8798-7f6a1abab1f6 | -21.10162 | -48.5744 | 2026-07-24 04:27:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 65f97c04-67fe-3651-9a3e-5d09c0e99138 | -19.99435 | -43.98396 | 2026-07-24 04:27:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e7a9ef9-3f8c-3e73-b958-2663afee2d79 | -18.79956 | -53.13795 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 180e0dad-fd62-33a2-befe-a82e70878d12 | -13.44138 | -51.52789 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 704859ef-276c-3406-b498-7729186f3d8c | -19.72228 | -46.17017 | 2026-07-24 04:27:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ac21b0f-35c5-3c22-bb2b-405b7fafca62 | -14.37724 | -50.33498 | 2026-07-24 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3e64c0a-117c-39f1-b07e-75fa9a7e8e60 | -17.77647 | -49.13122 | 2026-07-24 04:27:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01a94b7a-1251-3345-9cc7-64c1e6170f56 | -17.06217 | -45.03559 | 2026-07-24 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3acd81f1-1ba1-325b-b6ad-3ef2a00a41b0 | -13.33107 | -54.30577 | 2026-07-24 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e8cec5a-2f80-39cb-a204-9c7882b43e9a | -19.81432 | -44.12291 | 2026-07-24 04:27:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4fd6bd9-97df-3440-8225-e31828f7e926 | -17.91922 | -44.40679 | 2026-07-24 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43988f2c-0097-30e8-a446-a266f28bfff3 | -13.44074 | -51.53144 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb3021bb-1e0c-3374-9f96-a2932fa87b5a | -12.71396 | -59.99231 | 2026-07-24 04:27:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4ad5a89-b4ef-385c-b8cf-2a9ff8a15e19 | -17.84684 | -49.4239 | 2026-07-24 04:27:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5385ab1-50b1-3a36-9485-7b7f7e2ae3b9 | -13.43211 | -51.53349 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0da3c8b8-c910-3897-9202-fc05b0c45c30 | -16.25333 | -47.93093 | 2026-07-24 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a530949-8d07-35da-be9e-67353e1de11a | -13.45 | -51.52585 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 022a1999-42f1-3e1f-af36-d39f6a72e0f0 | -18.80429 | -53.1351 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33f73a2d-4682-332c-b662-eeaf74502c23 | -17.91982 | -44.40261 | 2026-07-24 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ed44442-fb6f-3336-863d-2f82ced8e2db | -13.30785 | -54.32878 | 2026-07-24 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8232bdc-008c-370d-9906-51660c585718 | -12.71397 | -59.99371 | 2026-07-24 04:27:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10dbd5a5-7b0a-3aed-bb6b-33bc0f121cb4 | -13.34648 | -54.30329 | 2026-07-24 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbac89a0-63bb-3b53-ae83-7fe2a3417363 | -18.25245 | -42.52819 | 2026-07-24 04:27:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 431fbe5c-9569-3c8a-8775-3e5e480ecf3c | -18.20082 | -44.73065 | 2026-07-24 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4418a116-2498-39a6-92fa-eb12bb100d10 | -17.41892 | -43.81047 | 2026-07-24 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af75900c-06ad-37e0-990f-b80c90c10bca | -13.33205 | -54.30585 | 2026-07-24 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e597ed3-c210-3793-86b9-809005ff42d6 | -12.72081 | -59.99392 | 2026-07-24 04:27:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a82d658-8d23-3b59-ba4a-05197754a5b3 | -16.14501 | -43.61891 | 2026-07-24 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4004d71a-7ddd-38a1-a75f-0727bea3c6d7 | -17.7771 | -49.12744 | 2026-07-24 04:27:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 165bd825-de33-3ea1-bf51-72b07f6bb474 | -17.84749 | -49.42004 | 2026-07-24 04:27:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e394975-2a37-3c87-9160-3c8d0675c6e3 | -13.44601 | -51.52509 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c83e3d7a-91d5-338c-8644-f0170229f207 | -13.44202 | -51.52434 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 707f44d2-7a63-3c62-bf4e-68a9b55379b5 | -19.22877 | -48.68244 | 2026-07-24 04:27:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 394e7a37-9664-3d92-be5f-b29ed4db5335 | -21.09661 | -43.25711 | 2026-07-24 04:27:00 | NOAA-20 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 830966bd-3bae-3cee-bfb2-25693d048eb2 | -19.71996 | -47.97041 | 2026-07-24 04:27:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2c40602-ae21-3186-9768-4843962a83e6 | -17.73754 | -48.46529 | 2026-07-24 04:27:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed6868d9-aff3-3a50-a41f-30a1861ae9a6 | -20.73481 | -51.36553 | 2026-07-24 04:27:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fb4b1980-e9da-399c-b62b-4248ab438f0a | -16.14866 | -43.6195 | 2026-07-24 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a4705f-b329-30e3-a864-97f6ffc9c34d | -17.7731 | -49.13058 | 2026-07-24 04:27:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f54785a3-e8c1-3470-9fc4-ab671ab34fa4 | -17.61394 | -46.6505 | 2026-07-24 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ba00945-86b8-3e12-9d6a-6fde3d6b0d2d | -18.80287 | -53.1426 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22c311dd-7d9f-3fe1-8899-f7b24f172473 | -14.37878 | -50.33227 | 2026-07-24 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e9d444ef-d36d-3450-9e0c-6531ca13c2e8 | -13.72506 | -52.024 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1af6bda3-0ef9-3db7-b2ff-6b2e1bd9f6f9 | -18.80357 | -53.13887 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d3caf76-c985-33cd-bd0b-102461d90202 | -13.31167 | -54.33501 | 2026-07-24 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c301800c-ecf4-3a34-bd2f-701dfa86f816 | -17.77373 | -49.12679 | 2026-07-24 04:27:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eda2f076-888d-31e3-9cbb-255832e3c253 | -21.53334 | -45.06612 | 2026-07-24 04:27:00 | NOAA-20 | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f6729af8-ed6d-355c-863d-a126ece70c62 | -18.79884 | -53.14173 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 315cb5ee-148e-3721-8122-015b07790584 | -18.79482 | -53.14083 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d49c944-5a87-3dde-9b71-0c3967831e83 | -16.71124 | -50.78147 | 2026-07-24 04:27:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b9fb60d-29fd-35ac-abfa-4046781b99aa | -21.32989 | -44.22386 | 2026-07-24 04:27:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4d56895-7eb6-3cc7-b6cf-404be7fcf130 | -18.79555 | -53.13701 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07e61dea-9127-33a5-964c-05f9c553beec | -13.43675 | -51.53068 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3e98c02-d038-37a5-b741-f03d5a72ba6c | -20.73348 | -51.36388 | 2026-07-24 04:27:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c264d4c2-2f19-36c3-a379-d28105a82d5d | -13.43147 | -51.53704 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 525afb9e-6d6e-3b6f-88dd-e3359dfc7bf6 | -13.31046 | -54.33488 | 2026-07-24 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c13a6ee8-c739-3da9-9c53-41bef5a2840d | -19.07014 | -46.78061 | 2026-07-24 04:27:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 445f2138-45ad-353b-a188-9c2a6bee948b | -21.7155 | -47.13487 | 2026-07-24 04:27:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62836e46-9ba3-3c12-8220-eaa761b453af | -18.19729 | -44.73005 | 2026-07-24 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d8e6dc1-7586-35bb-96db-f2124d3b956a | -17.61118 | -46.64629 | 2026-07-24 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6933dad7-d812-344b-8481-d2a2352b9647 | -16.70758 | -50.7808 | 2026-07-24 04:27:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b00e3715-3ee7-3a64-adc4-1cd1e34aa7a6 | -14.37433 | -50.33608 | 2026-07-24 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6d513bc-4e5d-3737-b8ff-053964b42ea7 | -21.09512 | -43.25786 | 2026-07-24 04:27:00 | NOAA-20 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69378d4f-ebf7-315c-b9f0-4fa3eb518224 | -18.54582 | -56.82415 | 2026-07-24 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0304b0df-39a5-3ada-89b3-5121cc8476a0 | -17.74147 | -48.4622 | 2026-07-24 04:27:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3da7ebf-9b7b-38ec-8faf-92b1aba4d31a | -13.72573 | -52.02023 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 321ff606-485c-3dbb-b82a-49ba4607e107 | -14.38171 | -50.33118 | 2026-07-24 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb8f6e0f-e369-31d7-84eb-52dfcf94e9bd | -18.5407 | -56.82298 | 2026-07-24 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7d7a3c2b-8912-358d-b3ac-15d8462f22ef | -14.37356 | -50.3343 | 2026-07-24 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07e3a8b3-f692-3383-8d7d-4e59e81d419a | -13.43611 | -51.53424 | 2026-07-24 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ede84721-2cb6-3442-8c52-7a91bcab8d24 | -18.80028 | -53.13414 | 2026-07-24 04:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b99d9d16-1da4-3371-8dfc-c1eeb58ace9d | -21.97435 | -47.66375 | 2026-07-24 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 619e668c-3ca4-3b96-94e7-e966c73e0f2d | -22.45454 | -46.84639 | 2026-07-24 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
