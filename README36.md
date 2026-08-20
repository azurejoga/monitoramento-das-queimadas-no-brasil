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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2768c354-4d22-386d-9e99-52afb32bd2fb | -14.30482 | -51.9136 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e35b95d7-59c0-3be1-8e9d-9da55e135279 | -12.80412 | -48.43113 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b271bcd-e04c-3841-b5b6-bc4f9c6a2c5d | -13.44649 | -51.43838 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cbc8add-fbb4-3171-9e15-8a0041ce67f3 | -13.40475 | -46.10152 | 2026-08-20 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 750161fa-d719-307c-881c-b10d56354503 | -19.6585 | -45.90768 | 2026-08-20 04:21:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e6ed906-9b32-3201-aa46-dccd4cd44074 | -11.18019 | -54.01868 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f974cf1-cc45-35b0-a3e7-b6ecf5e634cf | -19.71691 | -46.23002 | 2026-08-20 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10ae120b-f3d6-3713-aaea-d69cb587b1be | -13.44729 | -51.434 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f9ecf9b0-2243-3f40-a20c-63879c47e557 | -11.21665 | -54.00431 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a9e4233-3978-3e88-993b-2ecd0571d489 | -19.46132 | -46.81305 | 2026-08-20 04:21:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37f7a42b-5c0f-3713-ad99-ecfc9eb63933 | -12.8207 | -44.84961 | 2026-08-20 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab74f777-1837-36e8-b8c5-50db2d1becff | -12.00952 | -53.44672 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c576d4a-00db-31f5-ac83-dc8075951565 | -16.4999 | -55.18347 | 2026-08-20 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 18a712ec-ed2e-3c05-842f-8077e72e494e | -11.21083 | -55.06219 | 2026-08-20 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 77fdd23a-bc56-30cc-9ec1-aa3ab6ac8b36 | -19.71864 | -46.21906 | 2026-08-20 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 681a64b8-9b25-3c72-b906-2f8bdb35efaf | -14.69657 | -46.14117 | 2026-08-20 04:21:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23a09fbb-f7c6-389d-acc1-174c64ece370 | -13.51538 | -43.81371 | 2026-08-20 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c07533cb-35e7-324a-83ab-21b9608d582f | -12.81548 | -48.44576 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0173e19b-3397-3277-b66d-fd128374872d | -13.4381 | -57.07918 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a41381d4-3126-3dc7-b11a-1c804270f224 | -13.43013 | -57.06789 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e43b988-6095-3b74-b2aa-38aa1909abe4 | -14.30121 | -51.90818 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc46bf68-f806-35bf-beeb-e0c41e9ca649 | -14.44411 | -45.61981 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf0a7740-d2d1-361b-b8f5-4673332885e4 | -11.90695 | -50.16146 | 2026-08-20 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76a728dc-fa1c-3437-818e-7aa554461ad7 | -12.00556 | -53.43939 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dab33868-0e77-34c0-8a9f-4b9d5b39d9c4 | -11.18492 | -54.02333 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2253d307-28b3-3751-9c1f-57ce7fb467d6 | -13.68451 | -53.19221 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6959d93-94c1-33de-ba96-ec5eb6994af1 | -13.54166 | -52.23073 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2913f19c-fb3b-3aab-941e-b771c2bfcd89 | -14.15373 | -53.05005 | 2026-08-20 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e015483-cd3d-3e45-b791-39c5e417fb63 | -15.53083 | -40.85641 | 2026-08-20 04:21:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b56ae7c-a283-3102-a2d8-2e5d4462394a | -14.01675 | -53.66319 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff1fa10a-f8ee-3281-a1e1-d3c7ce5bccb8 | -14.44525 | -45.61268 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f30fac2d-ee02-35c4-903d-8e05b65d76e6 | -10.32265 | -57.57094 | 2026-08-20 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d41db1f0-63bf-3b72-8eae-76dd6cfc560f | -14.01952 | -53.64874 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a93ab1e2-6ff4-368c-aeb0-a528dc9da042 | -14.44685 | -45.62393 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c092617-5e60-3dfe-a159-499555480abb | -17.77779 | -49.12965 | 2026-08-20 04:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ae85571-e08e-3276-81ad-546dc308b154 | -18.23068 | -49.37821 | 2026-08-20 04:21:00 | NOAA-20 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6372da04-56cd-321e-b2cb-06995deb14c4 | -19.785 | -42.06684 | 2026-08-20 04:21:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 964d9bb3-229a-3126-9b1a-521ab60d384c | -11.41361 | -54.31152 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d1cfe23-160c-3ada-9944-e0b701a88be1 | -12.76922 | -48.45741 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b20db128-0270-3199-b289-cdaeea9c790a | -17.94397 | -44.40632 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bee6700-a993-3922-b4a7-a7da78287cbd | -15.71052 | -47.80304 | 2026-08-20 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93f4e3cd-446b-3d56-9bcf-f9a5187e01bd | -18.04152 | -44.61803 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| adfbff00-8dbe-3369-856a-fca6a98848ab | -12.8461 | -48.42279 | 2026-08-20 04:21:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a6b8c6c-48a0-3b6e-ad35-0ba5fea94495 | -14.71077 | -47.14743 | 2026-08-20 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50c247c2-94b3-3652-8559-e10346603538 | -13.44255 | -51.79793 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50a0090d-6bc2-3f69-9dbe-57dd88ca9520 | -15.38486 | -52.72923 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a99d5dc-6134-3714-8e40-00064e70eda6 | -14.20856 | -52.88918 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9988a478-2dd9-32af-819a-9452db1502c3 | -14.73127 | -47.15105 | 2026-08-20 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2b906cd-b729-33ca-8479-d3879fcaa492 | -13.44157 | -57.07578 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 623553c1-bc1a-3c5a-bc7b-ff588a48fb12 | -18.71633 | -43.21283 | 2026-08-20 04:21:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 04ea4a79-82b1-3ffa-b0b6-d77243d9c722 | -15.58527 | -43.73664 | 2026-08-20 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d58efa1d-5b72-323a-af7f-645dc1965517 | -13.44547 | -57.07526 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e1a1470-ac61-39ad-85a6-aa5fb2a755cd | -13.44809 | -51.42963 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a29d605a-fbe7-33a0-bfeb-109bbd21bc8f | -13.47356 | -51.43722 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19cc23d0-410b-3e69-b901-5600150d0075 | -11.19236 | -54.01389 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cff1121-c534-30c4-8b00-602295965d36 | -15.54332 | -50.27276 | 2026-08-20 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81050f58-29d6-3c74-88b3-b575dc9f14fd | -16.86161 | -43.23915 | 2026-08-20 04:21:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cf264a4-8977-3f3a-9a54-de11acb35220 | -18.5565 | -48.29533 | 2026-08-20 04:21:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7aba5160-7a4b-38e4-8c52-b940dd7b2835 | -14.22084 | -52.90248 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ef3181a-cd8f-3d40-92e5-706ed5f28ca4 | -12.81227 | -48.42787 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12c71bc6-1c38-340d-9a0b-87ffc87c22aa | -16.8622 | -43.23512 | 2026-08-20 04:21:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7165b5f8-97a6-3b63-943d-7ce09e1e4325 | -14.2171 | -52.89623 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2d7ecdd-c82f-3bde-8933-18d2748272a1 | -11.82795 | -58.84491 | 2026-08-20 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 398e282c-a27a-3fa6-8c40-b9091fd898ef | -11.18695 | -54.01279 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a162b50a-b1c1-3899-8c02-0f4d81e648bc | -12.77623 | -48.41648 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0655e73f-a311-3da0-bdbc-5bf7f29e2674 | -12.8172 | -48.44379 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ede230f8-ee2d-300c-8ee1-f366d565a3f7 | -13.47798 | -51.44006 | 2026-08-20 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8fb61944-0daa-37ff-8478-edbf6ebebd33 | -19.39025 | -46.40625 | 2026-08-20 04:21:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9e78a06-8d33-314e-aeb8-b3b6f81aa9da | -17.33298 | -43.62185 | 2026-08-20 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f704ecf4-9b89-3515-82a4-aceb6cb00393 | -11.19843 | -54.01152 | 2026-08-20 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e837fa1-8d12-37b7-8148-5d3d77149b8e | -20.52633 | -44.09669 | 2026-08-20 04:21:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f2160ac9-9767-39c5-a8eb-ae05ba3eeef9 | -12.77286 | -48.45837 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33376a01-5d1e-35bb-a5ac-8266d93bbb8a | -11.42248 | -54.32451 | 2026-08-20 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1afc0321-016f-3d44-8c7a-0550fd5032ef | -14.30928 | -51.91444 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8246fe47-a612-313f-a665-6e3695f3e2bf | -14.08277 | -40.9644 | 2026-08-20 04:21:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bad32c67-b32d-355a-8d35-a4e53d1879d2 | -19.95521 | -45.05667 | 2026-08-20 04:21:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4279fc9c-d16d-3336-a494-ca56ebaacea7 | -13.249 | -51.64529 | 2026-08-20 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a33d1ade-0009-3211-bcb7-17149b089bb0 | -18.02805 | -44.61579 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abdeef6c-7afb-3961-8abb-61b9d845ebe6 | -15.71181 | -53.77472 | 2026-08-20 04:21:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50c1f6f8-96fb-3166-9acc-09d56e9bd48d | -13.35343 | -41.67598 | 2026-08-20 04:21:00 | NOAA-20 | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 90566ff4-b3b2-350f-aa01-10c21055259b | -12.80329 | -48.43608 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 474b1e84-50d8-3773-87dd-3f007f3db942 | -13.43401 | -57.06722 | 2026-08-20 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8dafb49f-42b1-3685-9090-952636565166 | -16.86509 | -43.23972 | 2026-08-20 04:21:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1e5bce2-1e23-348c-9499-47bc9ed175ea | -20.2807 | -42.87504 | 2026-08-20 04:21:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 066bd0bc-11ec-3f42-9343-480810183b56 | -13.44077 | -43.83871 | 2026-08-20 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 315ae5af-a175-3723-a686-838bf0ec76b7 | -14.25547 | -51.81795 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be3352f7-722f-349a-b2ae-b04f9e1dcb36 | -15.36495 | -52.7835 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a52bfd30-02a1-3cd6-a2c8-2aaa6c47a8f9 | -12.00101 | -53.43523 | 2026-08-20 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9980b1d-0b79-3aad-9746-e45763b03026 | -14.44799 | -45.61681 | 2026-08-20 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18073123-2989-3f68-9c30-4b07ec1d4182 | -14.20759 | -52.89421 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06773f63-6a79-3cf2-bd5c-7b36a744a2ae | -18.03142 | -44.61636 | 2026-08-20 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 19a00275-cbf5-34b7-9b68-56c810aca30b | -14.15211 | -52.95286 | 2026-08-20 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 78801e37-f68d-3359-9633-bb4e2fd26106 | -14.07967 | -40.95904 | 2026-08-20 04:21:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 256785aa-66ab-3949-8149-60b57b894544 | -20.00672 | -45.74001 | 2026-08-20 04:21:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d4a90c0-9616-3189-ba1a-2647e500822a | -12.76114 | -48.46011 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af1dce7e-5430-3ffd-8807-7b70df045133 | -14.02687 | -53.63761 | 2026-08-20 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8913fa7-78a8-3473-bb19-cfabd1ebab92 | -14.30035 | -51.91273 | 2026-08-20 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e98c6c6-f1ea-344b-9517-757b7f49924f | -12.82109 | -48.4207 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 622a534d-dbbf-3d1b-b6b9-ef7dcb21908b | -12.81512 | -48.42614 | 2026-08-20 04:21:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b286f6f3-2fba-3081-916b-3c28dadff62c | -15.36245 | -52.77138 | 2026-08-20 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README37.md)
