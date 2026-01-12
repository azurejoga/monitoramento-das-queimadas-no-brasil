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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47e9eb7a-bd07-313f-8ae7-38015cad2d4f | -17.14937 | -47.72673 | 2026-01-12 12:16:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| bc2ce3ee-304d-3166-a189-f36adcd8614d | -13.97972 | -45.76884 | 2026-01-12 12:16:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cad630d4-469c-37ce-9441-ac1747f90bb8 | -17.13947 | -47.72544 | 2026-01-12 12:16:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f03486e2-d783-39fd-ae7e-abe4f7141ee9 | -19.03089 | -44.63729 | 2026-01-12 12:16:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 948e921c-aa63-3cc3-82bb-6f6819ea0e6d | -17.15082 | -47.71523 | 2026-01-12 12:16:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c9f069a8-3079-3ca5-9adb-89044ee36c0b | -16.1774 | -47.03356 | 2026-01-12 12:16:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 621b6a7f-e28f-30e4-bb7f-93f0e78e904f | -12.66479 | -46.75332 | 2026-01-12 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| a211447c-19e0-397d-919b-b19dbc2a7110 | -13.9773 | -45.76207 | 2026-01-12 12:16:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 7f44bbd8-8c57-3584-82a6-acbbfc800d69 | -19.2264 | -43.7867 | 2026-01-12 12:16:00 | TERRA_M-T | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 576adbf9-7ff6-3169-8214-bad5937977ea | -21.13332 | -45.02282 | 2026-01-12 12:18:00 | TERRA_M-T | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 461becb9-a009-355b-b3b1-faa2cf148fd9 | -21.17664 | -44.85543 | 2026-01-12 12:18:00 | TERRA_M-T | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 36804b37-7dc7-37e5-b49a-a4b565839b44 | -20.44559 | -44.76886 | 2026-01-12 12:18:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| e80d0131-b4ed-3382-8878-a7daf15e15bb | -21.1376 | -44.98086 | 2026-01-12 12:18:00 | TERRA_M-T | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| be463597-0183-3a0f-a8ff-ebb05a2b0942 | -21.21453 | -43.76007 | 2026-01-12 12:18:00 | TERRA_M-T | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| a3bf051f-e7bf-33d9-8d4d-326d3488cc66 | -21.12233 | -42.93383 | 2026-01-12 12:18:00 | TERRA_M-T | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 840455d3-e0df-3e02-a8a0-2167325913d3 | -29.17955 | -51.23903 | 2026-01-12 12:18:00 | TERRA_M-T | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 47d5f24d-40a9-3b97-a1ed-5626ac8984de | -6.9433 | -41.0887 | 2026-01-12 13:10:00 | GOES-19 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 263.7 |
| 66018941-2a6a-3ae2-8bef-554376a06919 | -6.9433 | -41.0887 | 2026-01-12 13:20:00 | GOES-19 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 398.7 |
| 21548b2e-af43-305b-bb23-bc5a0f3b2912 | -6.9433 | -41.0887 | 2026-01-12 13:30:00 | GOES-19 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 219.3 |
| 751450bf-c673-3bfc-92f4-53956bd1e0cd | -3.982 | -42.516 | 2026-01-12 13:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 457841b5-8981-3c23-aecd-d2b4fb4d3b27 | -4.5026 | -40.442 | 2026-01-12 13:30:00 | GOES-19 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 97.8 |
| f46d601c-658d-3a9f-8e0f-c9f1f5e06ad1 | -6.9433 | -41.0887 | 2026-01-12 13:40:00 | GOES-19 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| 3bd6e79a-b9fa-3996-bc5b-9330cbb56b37 | -4.5026 | -40.442 | 2026-01-12 13:40:00 | GOES-19 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 98.2 |
| c6e62e63-04fe-3529-b67e-58c0da871b69 | -13.9862 | -45.7761 | 2026-01-12 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |


