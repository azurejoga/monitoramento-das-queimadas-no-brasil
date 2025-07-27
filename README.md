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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cf0476d-161d-30b9-9a09-5ec43d9d40a2 | -4.0754 | -42.5344 | 2025-07-27 00:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 5ee2cbae-42cd-39b6-a83e-e2f63ef50fc8 | -16.4162 | -48.9164 | 2025-07-27 00:00:00 | GOES-19 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 791abbaa-26f1-3713-9ffc-34e98839af0a | -8.1822 | -43.2034 | 2025-07-27 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 2c2bc2b1-ac3b-3050-bf04-df8d8b930144 | -3.4235 | -49.4773 | 2025-07-27 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d43c2180-4a00-3408-85b1-6a9e8308c5ac | -4.1166 | -47.9269 | 2025-07-27 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| edc05942-b423-3f07-82a5-b6de173786f9 | -6.5445 | -56.1915 | 2025-07-27 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| aa0c69e1-a4b4-33d2-aca5-895ef957e8d8 | -3.4235 | -49.4773 | 2025-07-27 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ae268c9e-1581-386d-9f5a-0d76865904d2 | -4.0754 | -42.5344 | 2025-07-27 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 20ad7649-a67a-3af2-95d7-668deef53067 | -6.6576 | -58.8274 | 2025-07-27 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 30515e73-1a7d-3675-a5bf-0d8e50135bf5 | -6.6389 | -58.8669 | 2025-07-27 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 97dc439f-f712-35f2-bc42-16aaa45bc6cd | -6.6574 | -58.8661 | 2025-07-27 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 442edaab-8f84-3e45-8c39-5343c0d038aa | -6.6391 | -58.8282 | 2025-07-27 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e1bdf2e7-cb3e-3f72-9547-542fa7c5bf7e | -17.9634 | -53.1431 | 2025-07-27 00:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ec56b77e-3ebb-3928-a21c-267ef9b786c4 | -4.0754 | -42.5344 | 2025-07-27 00:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| ad77c3f6-e1d1-30d6-9320-5372dc474ab4 | -6.6575 | -58.8468 | 2025-07-27 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 862c7dd2-8753-323f-94ea-f291c6603cf0 | -17.9828 | -53.1615 | 2025-07-27 00:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 0a9782aa-cbee-3ddb-bf67-648cc105b565 | -6.639 | -58.8475 | 2025-07-27 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 0ab465c2-f150-3b67-976a-14fd387c3005 | -17.9833 | -53.14 | 2025-07-27 00:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ba49d8e3-ecd9-3875-b6a5-578b321652d1 | -17.963 | -53.1646 | 2025-07-27 00:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 6e97ae46-b776-38ba-a4fa-647c05eac661 | -3.4235 | -49.4773 | 2025-07-27 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9360ec81-84b9-3cba-acc1-4487d0b0722c | -15.55932 | -42.60107 | 2025-07-27 00:24:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 27c56448-42ba-3d91-b7d4-82ac8e4da413 | -12.67935 | -46.98853 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 29c35c84-8fee-37a6-880a-c165561c1f4e | -12.71186 | -46.2697 | 2025-07-27 00:24:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e58bbf83-c497-304f-8bb0-1a1113b262a8 | -17.96041 | -53.16843 | 2025-07-27 00:24:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 174.5 |
| cf4edd33-e45a-3b97-90e7-e590267c168a | -12.68194 | -47.00817 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cfe9c3e9-d79b-343b-9fcc-785826922e2d | -20.95892 | -48.91442 | 2025-07-27 00:24:00 | TERRA_M-M | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 84fbb06c-677e-3402-aae5-26a1f6f30201 | -12.7062 | -46.99905 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 044e1bd1-03cc-33b6-8fd6-37a517b136c2 | -20.19376 | -48.69292 | 2025-07-27 00:24:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 60b7e3d4-25b2-37d7-939a-1030f4060c2e | -15.99024 | -42.65265 | 2025-07-27 00:24:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| 1a0dead0-40cb-3844-95b8-bba659568bfe | -17.04391 | -43.77133 | 2025-07-27 00:24:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 3fab4be0-2e22-3642-8e53-59e91687b267 | -13.71727 | -45.67836 | 2025-07-27 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| cf293be4-cf15-38be-bdc2-c775a45e2be1 | -12.70801 | -45.03205 | 2025-07-27 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe447809-5555-3c61-a983-3aa9a263d1b4 | -12.6833 | -47.01834 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d7db65a6-2e58-3210-9742-200501f543fb | -21.34148 | -45.63695 | 2025-07-27 00:24:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 64b25b94-e067-390c-b032-b9fb683599e2 | -15.56078 | -42.61103 | 2025-07-27 00:24:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5734d12b-a903-3f07-96a0-5266a246bd14 | -15.04264 | -49.25234 | 2025-07-27 00:24:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bd0c5099-bc9c-3fe2-b811-cb1c6fc05474 | -20.35321 | -45.98668 | 2025-07-27 00:24:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 558837e7-6e1f-3d6d-ae89-f5a99cae60ff | -17.21215 | -44.85612 | 2025-07-27 00:24:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6ea3e0f7-700d-3a7f-9577-791130b8c2c4 | -21.33676 | -45.6322 | 2025-07-27 00:24:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 238cc013-7d48-3dd3-b022-36b8ac3ad547 | -18.00181 | -53.15925 | 2025-07-27 00:24:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 1eb30111-c133-35b2-a021-f994f24132d3 | -18.21029 | -44.6202 | 2025-07-27 00:24:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 74c8be55-1500-3d19-941f-7c6c9a64861b | -15.52995 | -42.65671 | 2025-07-27 00:24:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ec8cdc4c-51fd-399c-8d91-66f3fe339816 | -13.09252 | -47.33418 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cd0f1a67-be26-3867-b7f2-3b49c88f3511 | -17.97023 | -53.16275 | 2025-07-27 00:24:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 323.9 |
| 8bc0670c-1e8e-36e0-9dca-12855b4018c8 | -13.13579 | -47.33337 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4892cac9-035a-3f08-926a-c824a88c11f4 | -17.99204 | -53.1655 | 2025-07-27 00:24:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| dcec549f-c482-368f-b6ee-2aff1935cd15 | -13.5315 | -45.52337 | 2025-07-27 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3dbdd607-0ab5-3c52-9a48-f9af131b0bcb | -16.41031 | -48.93872 | 2025-07-27 00:24:00 | TERRA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a597a138-4df3-3964-bd73-793d7ec4d90c | -15.18803 | -43.28227 | 2025-07-27 00:24:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 61541440-1aa3-3cad-b5d9-b46a721e628a | -21.33817 | -45.64336 | 2025-07-27 00:24:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 29ea1963-391d-37cf-90c7-b0ebffcafc4d | -13.71601 | -45.66911 | 2025-07-27 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 52928295-851a-349b-b1c1-e0dd4fbe50fa | -12.71549 | -46.99755 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d16ab975-3a76-370f-b566-c9ac06a3e174 | -20.96082 | -48.93202 | 2025-07-27 00:24:00 | TERRA_M-M | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 0544440e-4cec-3d68-8e45-51f28a8ba82f | -16.40854 | -48.92386 | 2025-07-27 00:24:00 | TERRA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| e374bc6c-7b36-3c40-89ae-8bb16b035c5b | -13.49175 | -45.50738 | 2025-07-27 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8fb20e6e-e53e-3a22-b15f-ca8f11140f92 | -13.71853 | -45.68762 | 2025-07-27 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1135afff-8998-32b1-a74d-7bcba57765bb | -12.71684 | -47.00795 | 2025-07-27 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bb5cd9d1-452a-3060-b715-e35cec88a6c9 | -12.71315 | -46.27945 | 2025-07-27 00:24:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 838dead6-0afe-3da6-ae93-d7a7c4947251 | -15.18667 | -43.2728 | 2025-07-27 00:24:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 300d35f7-4479-3c9f-89ce-82e1474b8902 | -13.69169 | -45.6915 | 2025-07-27 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8174f0f5-b82a-3b72-b960-129ed3917db5 | -17.97625 | -53.16718 | 2025-07-27 00:24:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 014d410c-3448-31b2-b667-3a30e11cfdbf | -20.1956 | -48.70954 | 2025-07-27 00:24:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4150245a-676a-3f28-a60d-ab9f3ef1e513 | -14.60398 | -47.98668 | 2025-07-27 00:24:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fc8d0c62-6c53-39d6-af64-bc77905e8e5c | -17.8569 | -40.96914 | 2025-07-27 00:24:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 81b041ef-d74b-3c93-b534-bd09d7c8aaa4 | -17.97314 | -53.19487 | 2025-07-27 00:24:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 711440da-b2f8-3e64-b8a8-e0f489da43a9 | -20.35459 | -45.99768 | 2025-07-27 00:24:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7d0d4121-7548-3f78-bdf0-381f0265bb0a | -14.02234 | -44.616 | 2025-07-27 00:24:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9d18e9df-db84-3889-8b73-bd974e7ce3c6 | -15.98881 | -42.64296 | 2025-07-27 00:24:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |
| 6a5db6cf-6549-3895-af11-9014b3f78d66 | -8.17335 | -43.2051 | 2025-07-27 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 9a97dabb-77bc-3876-8938-9c580376bb4f | -4.96398 | -43.73448 | 2025-07-27 00:26:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| d3f955be-cc1f-3145-add0-60f9eb882371 | -7.81176 | -46.57542 | 2025-07-27 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ca3d472-b4c3-30d4-aa22-14610e60cacb | -6.89483 | -52.86285 | 2025-07-27 00:26:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| cdced5be-cd30-3f80-a2ea-0e037016cd5d | -9.72306 | -42.6683 | 2025-07-27 00:26:00 | TERRA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| bbe03219-085a-3f50-a863-9de9e2d2adab | -7.80165 | -46.56773 | 2025-07-27 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f199d4f8-f9e3-3bc8-9e2c-60e02d062a11 | -11.30783 | -55.13715 | 2025-07-27 00:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 178cab2f-bcce-3aec-94a6-d13e0655b045 | -4.07484 | -42.54787 | 2025-07-27 00:26:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 42a2870a-2fde-3aac-9f2f-ecf9c92ce66d | -4.61853 | -43.31688 | 2025-07-27 00:26:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ad07f954-66b6-3d95-ad8e-4f7417ea6f7b | -9.57945 | -43.87703 | 2025-07-27 00:26:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 018dc903-ab85-3abc-a4db-88f9d62339b8 | -4.07284 | -42.53437 | 2025-07-27 00:26:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 9f96cd5d-d691-3c33-b1f8-e2ac3e27e013 | -5.74123 | -43.9538 | 2025-07-27 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d881fd86-c999-3c12-8a07-fa0b784385ad | -11.10999 | -45.12237 | 2025-07-27 00:26:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b49c8205-ebec-343d-b44f-b678be67870a | -4.95419 | -43.73591 | 2025-07-27 00:26:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 23f2a5ae-988f-389a-a30e-0d4bb963317e | -6.5525 | -41.5014 | 2025-07-27 00:26:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 283c05c5-5d70-36a7-b603-7ff3686f77d6 | -7.09762 | -44.04861 | 2025-07-27 00:26:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 41bcceca-2c52-3707-8d4f-df99eb1ba0e1 | -8.17492 | -43.21587 | 2025-07-27 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ba5a27e1-532e-3b15-a942-0eaff385f96c | -6.01225 | -44.05404 | 2025-07-27 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a1b2aa8c-c5a9-3f34-94ef-ec6c7ce9c556 | -6.87103 | -43.68591 | 2025-07-27 00:26:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6a1dfb4a-4216-3ce9-9653-f7a5199059df | -6.95207 | -50.45964 | 2025-07-27 00:26:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 163712fd-6c35-3c12-97ec-deb7b34f7947 | -6.52626 | -43.34974 | 2025-07-27 00:26:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7c222e08-4831-38d3-a0f2-112655ae9aa4 | -7.51021 | -44.42229 | 2025-07-27 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2a2fad17-915d-3251-86a6-b626ee2ca9e1 | -5.78391 | -43.60336 | 2025-07-27 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 93cc213d-d24a-307b-b81a-01be64d8374d | -4.03366 | -42.51891 | 2025-07-27 00:26:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 345a575c-6e40-3d14-bf31-e9e7c8ed1c69 | -4.06998 | -42.54132 | 2025-07-27 00:26:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 7d1a80b7-786b-3cb6-bfe1-d63f7444cbce | -4.96243 | -43.72351 | 2025-07-27 00:26:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1c2348eb-e64e-3ef0-88b6-fb9096b19e08 | -5.60371 | -45.07507 | 2025-07-27 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c47f10a8-f811-3944-b609-c345b907afbb | -8.17178 | -43.19431 | 2025-07-27 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| ab637150-bc7a-3872-aa20-30c2dfdc1792 | -8.30309 | -45.00786 | 2025-07-27 00:26:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8a6db7bb-0148-385e-8314-a50395ec9c18 | -5.77571 | -43.61581 | 2025-07-27 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| da4c05fa-17a2-3445-ba62-1692f133678e | -7.81053 | -46.56648 | 2025-07-27 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6d7d76e1-48af-306d-bf28-65f8770e7e90 | -10.51331 | -42.55321 | 2025-07-27 00:26:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |


[Clique aqui para ver as próximas entradas](README2.md)
