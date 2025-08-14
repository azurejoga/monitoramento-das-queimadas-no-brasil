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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9f728a0-82c2-37de-9c47-9664282d4adf | -12.68666 | -44.95423 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf929de1-3791-3c91-81e8-9665502354c1 | -16.07775 | -43.62751 | 2025-08-14 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 625f3064-91da-3d39-9b4c-0cc72102412d | -12.13597 | -39.77177 | 2025-08-14 04:21:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea24fc4e-c915-35bf-a488-bead90027488 | -7.23992 | -57.64626 | 2025-08-14 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0e089f2-0311-3dc3-bce0-0fe0aefafe63 | -10.53525 | -42.55328 | 2025-08-14 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5fbcf6ba-f4e3-3a3a-a3d0-e71cc90d3298 | -14.10761 | -48.20315 | 2025-08-14 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b30ef96e-710d-3449-a2dd-e583e16db9bc | -13.27371 | -57.25072 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15ab076a-4e45-357d-b042-cdbeb7485500 | -12.57951 | -46.95962 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a708e852-9e52-3eed-9614-d48bfae68ea4 | -9.60913 | -55.13928 | 2025-08-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 556d7611-04c7-3284-a01c-3a4443616ad6 | -15.58 | -47.3234 | 2025-08-14 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dee6e0d4-6be8-3129-a60f-16bd531d9bd0 | -9.5122 | -47.72411 | 2025-08-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c15d504-c8df-396e-bd5b-f03c0bd7d619 | -13.89165 | -45.56222 | 2025-08-14 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87b6e447-dd3c-31ad-ac53-6b0c5dfb814d | -12.30134 | -50.00681 | 2025-08-14 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aea0eed-605c-3bd2-b5a5-448e318758af | -12.49939 | -46.97215 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28b401fa-cc4d-39e5-be6c-7893b0a62572 | -9.60746 | -55.13872 | 2025-08-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 362caaba-4918-3d83-919e-80c61ac18527 | -13.07379 | -57.1378 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 041bc3ac-2b2a-3a36-86c0-e11fd7935d4d | -12.69057 | -44.95111 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dfb015c-c251-352f-916b-008f0499189e | -12.31578 | -46.06357 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7255515-b136-3855-b267-1b0e7c5f9ed9 | -12.6833 | -44.9537 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5b0c3680-fc6a-3604-857c-17a3d6f82654 | -12.57449 | -46.96974 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56a67d6f-221a-3451-b35b-b303accd14da | -13.11348 | -57.1497 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4741e656-c2d8-3a6c-9eaa-efc736ce9a34 | -11.31446 | -49.95451 | 2025-08-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d8639360-5afe-3be8-b408-331f5a943aba | -11.68313 | -51.61137 | 2025-08-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67324704-ed34-3e8f-a5da-9e21bb36d1c3 | -16.07806 | -43.62543 | 2025-08-14 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd2884a8-eae1-3d98-a1ec-33a1ee51d40c | -13.35412 | -43.77404 | 2025-08-14 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c997e3f4-1154-3298-9dff-bcc3122d87e6 | -12.3507 | -49.9182 | 2025-08-14 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 031e3090-b175-348c-aa8a-055e52c0fa90 | -12.32404 | -46.05409 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f4f20ba-f823-3759-a9dd-6c1dbd8dbdff | -8.80215 | -52.04062 | 2025-08-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 124eb646-49a7-386b-acee-b5a3fdf62355 | -7.23334 | -57.64513 | 2025-08-14 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec4f529d-8fe6-37bc-b1be-d5c6596190a4 | -13.78822 | -44.3347 | 2025-08-14 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00685207-d105-31eb-8292-fa7a17c93e09 | -14.45979 | -48.81712 | 2025-08-14 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1802d526-f13e-3292-b1b4-c3c0236499eb | -12.57618 | -46.9591 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4eab826-aa0a-38a1-ad04-96e0e3c8079e | -12.34775 | -49.91311 | 2025-08-14 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b115f38-c8b2-3d1c-803e-f03d1ebe235a | -12.68721 | -44.95058 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1450e2d-6a4b-38b8-a773-6007c3da5bb2 | -13.11435 | -57.14543 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 090c373d-7bf7-353b-9913-b234cee78eb4 | -14.32022 | -48.64074 | 2025-08-14 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 167feceb-c7b7-3ed3-9f6d-f8e8163f26a8 | -13.07427 | -49.32582 | 2025-08-14 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08dc3b43-59f9-3dcd-8c7b-8ad2a94d83c3 | -10.3656 | -50.81038 | 2025-08-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0ab6883-ed1a-3b11-a1b9-08eac50babc8 | -11.68246 | -51.61515 | 2025-08-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69763ad3-d328-35c6-9b09-28f406da3082 | -12.69283 | -44.95891 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b464e7ef-7133-32ab-8458-89cd1ce5a07b | -10.3564 | -50.81591 | 2025-08-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 425e70d8-632d-333e-977b-9eb0d3c86c30 | -9.51564 | -47.72467 | 2025-08-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8338d309-137f-3385-bffe-0e914e266c4e | -9.60846 | -55.14287 | 2025-08-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1d1cf6d-6c34-347e-92d1-76faec2aae71 | -12.30056 | -50.01133 | 2025-08-14 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a348f20c-5b70-3cb2-ac26-3346f829e304 | -16.07838 | -43.62308 | 2025-08-14 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c38d4e3-2e12-3bd8-8680-39546aadc3db | -14.47691 | -46.06765 | 2025-08-14 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7e9c161-8e0a-31bd-9f9a-ddb80bcf1e9c | -12.32458 | -46.05058 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2bb3917-b0ef-328c-a95e-5f75a99703ff | -12.58396 | -46.95303 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13292ee4-bb3d-3589-8693-25321058f80c | -9.74723 | -48.57033 | 2025-08-14 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 833027a0-e2a2-31e8-be79-a5bbe7367a84 | -15.40319 | -43.06738 | 2025-08-14 04:21:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3df0c541-578a-360c-9737-387f99a731bb | -9.6068 | -55.14232 | 2025-08-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac184bf6-ea2f-3c18-96ac-0a439190f906 | -13.78534 | -44.33029 | 2025-08-14 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44e247f9-4c05-33a6-87ca-b51d15779f8a | -13.07956 | -57.13899 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8cd73ea-d817-38bc-8774-2b7a3b42e869 | -13.88776 | -45.56531 | 2025-08-14 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68cf1073-b181-3b15-92cd-b6d352512cb7 | -13.07358 | -49.32994 | 2025-08-14 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6902f62c-94bb-374c-82fe-b12169b3438f | -12.58721 | -46.97543 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e0a4133-1aa9-3221-80aa-dec912c07a32 | -11.76213 | -43.38463 | 2025-08-14 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3c9905e-920b-38ba-b919-94ec63fbf8b1 | -12.57894 | -46.96317 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f4955f2-e7ad-309f-be52-f5fb5e3b9b0b | -12.31688 | -46.05655 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0807237b-7397-3b74-9ade-079bfe22bae6 | -13.27954 | -57.25171 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51eefb50-620d-3f24-8c8d-0a4780fd6469 | -13.11989 | -57.14765 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1101b05-558a-3f91-9a1c-a980e268e1d5 | -12.49663 | -46.96804 | 2025-08-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc183012-dc36-3bf8-9822-6c5b2c882a50 | -11.4516 | -47.31055 | 2025-08-14 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62981383-06b9-350f-b8ab-f5770b908b13 | -15.55457 | -43.15126 | 2025-08-14 04:21:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5a17b84b-ef01-31fb-8234-98314b3971fa | -9.56339 | -40.34689 | 2025-08-14 04:21:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6b349898-cf87-3bf8-9e18-5b7fb3d9080c | -13.78476 | -44.33416 | 2025-08-14 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c149858f-78ca-34b1-a33e-fe5c8c12ef39 | -13.88721 | -45.56893 | 2025-08-14 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85f8a2a0-f049-3c8a-8dff-622fe497dbbb | -10.361 | -50.81314 | 2025-08-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 919af7a2-e5cf-39a4-985b-81538779e3a3 | -10.35818 | -50.80544 | 2025-08-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7d6e5f6-825e-3832-aafb-eb2e42d11fc1 | -13.12012 | -57.1466 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c20226b-b296-320c-abdb-7bdb95b547a3 | -10.00716 | -59.21726 | 2025-08-14 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a9a21ecb-9d7f-33e2-9859-7320d5e84133 | -12.42357 | -48.69796 | 2025-08-14 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bd38309-f76b-3f9f-867b-db895ab549ed | -12.32073 | -46.05356 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e612d33-dcfa-35b4-8aca-828a5403585c | -15.92178 | -43.51485 | 2025-08-14 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b6906f-2d2f-312e-ab98-f1dd7b1b10cb | -13.28537 | -57.25273 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fc3f08e-809c-396b-8eb2-424d8161436a | -9.30531 | -46.17584 | 2025-08-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3e115e5-bd25-396b-8db4-c94643cf3a98 | -13.24691 | -43.66454 | 2025-08-14 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99af010d-80c1-35f1-be3f-d6156f951923 | -14.2373 | -44.58607 | 2025-08-14 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 618b19ec-5410-372d-98c9-464002c56ca2 | -11.76272 | -43.38062 | 2025-08-14 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 990a8dad-541c-3dd9-a7fe-dae0f647281a | -12.69338 | -44.95527 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f924f307-25dc-3a69-8ed8-d09427cadf47 | -14.79886 | -42.72258 | 2025-08-14 04:21:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb2a6282-2e77-393c-a2a5-2104d9212bb5 | -14.32427 | -48.63745 | 2025-08-14 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2f1f3a2-164c-37c7-8cb8-4907add7feda | -9.31464 | -46.22419 | 2025-08-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 067102dd-baa9-3950-ae79-d66b278e98bf | -12.42705 | -48.69855 | 2025-08-14 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a2daf10-c320-3300-87f3-02a2ed0012bf | -15.57669 | -47.32284 | 2025-08-14 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68553c5d-e503-35a4-9241-ad8320e2cad7 | -10.3616 | -50.80964 | 2025-08-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc7ad332-e76b-358c-b6e7-06d5d30c6757 | -15.92606 | -43.51097 | 2025-08-14 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aff5040-6d4b-375c-a517-7a310df3c8aa | -12.32239 | -46.06464 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 153e0c35-475d-3f6d-8ab0-fc0a50528d18 | -13.48167 | -43.29058 | 2025-08-14 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b149ebc3-d163-3dbe-be5c-6a46802aef07 | -12.3257 | -46.06517 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eef5440-c5b5-3c4c-ac2e-06bec942f32d | -14.37634 | -54.65365 | 2025-08-14 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e72e8fd6-6251-3290-87b3-b0e633ea2713 | -12.68947 | -44.95839 | 2025-08-14 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 593f7094-aae5-3431-a314-035b6be3a5d0 | -9.86849 | -44.6997 | 2025-08-14 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1ecd9f3-9a5f-3edd-b1a0-6d6c10848d33 | -13.08037 | -57.13488 | 2025-08-14 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f7aeffc-78cf-334d-a8d7-078ea89baee7 | -10.0071 | -59.21762 | 2025-08-14 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5453a6ac-a887-37a5-9954-9dc6dffbf47f | -12.32349 | -46.05761 | 2025-08-14 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 271a8076-6aec-3deb-9c36-bd9558cede7c | -15.57613 | -47.32641 | 2025-08-14 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7352b8c4-524e-309a-aa7c-82fc267c5165 | -14.32365 | -48.6413 | 2025-08-14 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8055d69-5c0d-3dc2-a8f8-9544617fffca | -7.28797 | -55.30891 | 2025-08-14 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcb102ae-afcf-3dc5-986b-d53ffe726e8e | -9.31797 | -46.22471 | 2025-08-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
