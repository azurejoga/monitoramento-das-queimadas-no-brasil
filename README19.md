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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfa96b5d-6a92-3d39-a14a-58b92d0efc4d | -6.10625 | -43.95692 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| fb25384d-48d5-3fad-bb4f-b6d50db6e549 | -3.9462 | -41.49448 | 2024-11-05 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef0075c7-b67d-3d39-9f5f-e7be050df7cb | -6.18854 | -39.22239 | 2024-11-05 04:08:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa46b43d-5671-3507-a2a4-a44cb0904d4e | -5.9203 | -43.64616 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93dd546e-3c07-356a-baa5-fa46d226183a | -5.56596 | -42.29458 | 2024-11-05 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bad6d31-5067-3e65-b579-006f2100fd49 | -5.45428 | -45.52832 | 2024-11-05 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b9369f1-1b41-391f-bcef-a70593a1d3ee | -2.96612 | -40.23106 | 2024-11-05 04:08:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 625a1aa4-5883-3233-bca4-7d58319ec0de | -6.54574 | -45.93603 | 2024-11-05 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 566cf8f0-d6f9-306f-b852-6b4811e1ec2e | -2.65542 | -48.56029 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b46d488b-bb13-3d63-b340-1ffb947d37f8 | -3.08545 | -54.50981 | 2024-11-05 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4f436a55-e3af-37bf-9361-207be68fdf14 | -7.21917 | -42.53552 | 2024-11-05 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a45d553-0769-3110-ba8e-8902330eda23 | -2.55515 | -47.49184 | 2024-11-05 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0276d1be-823d-3eb2-99f9-e7bf88f5cde3 | -8.13921 | -35.32963 | 2024-11-05 04:08:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a5b1cbc9-631e-37d9-abf3-680468bd1d21 | -3.39062 | -41.56615 | 2024-11-05 04:08:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c7b3efb1-c197-3969-ac72-2eb9fa10fa35 | -3.55352 | -47.37868 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 34e89c25-aa24-3723-9a08-2c4c05f7c9fa | -2.65272 | -48.57641 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bee91594-6d1e-38e1-8a03-368ff044175f | -5.48478 | -41.66246 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0e1a188-91c9-3b3d-b0ac-cacca9d21772 | -4.02651 | -43.23318 | 2024-11-05 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d50af771-e6ec-390d-9d74-e204c984e6f0 | -2.81991 | -48.5511 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 383a3b6d-722a-306a-a2f5-50954f526259 | -5.45097 | -43.26213 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75a077ac-89fc-3c04-8a1f-041c0b9342ff | -2.65096 | -48.56877 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 38a7a665-8043-381f-ba34-73477a2a4185 | -6.51657 | -41.41573 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 158ea3c0-df1e-3fb6-9570-5c42eba6f80c | -7.09387 | -39.67711 | 2024-11-05 04:08:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c5a43bd1-c76f-3511-9307-9aaf74918a67 | -3.70142 | -44.62018 | 2024-11-05 04:08:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 886be742-639f-3b17-ab9c-423fae55b090 | -3.56169 | -47.3843 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03620a5a-ea97-32e4-9d17-269234091059 | -3.5542 | -47.37448 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| cb2e71a4-66ee-36c9-84c1-aca188d7a0ef | -3.55059 | -47.39653 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 8bd9e4b6-a601-3052-88ce-e27e7c19ddc7 | -5.07364 | -43.71893 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b23ace5-43f8-318f-9d2d-9b938cb28936 | -3.78192 | -46.0546 | 2024-11-05 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7698d431-5068-37f1-87e0-21d93381b1c0 | -5.38104 | -46.4429 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea51308-bf81-3c22-91f2-643e7cd4d9d1 | -5.58166 | -41.67458 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3883b35b-c75d-35d2-b7f9-3a061f665668 | -4.62772 | -45.69989 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 10125a09-cca9-3c05-8488-13265a76f300 | -3.62301 | -39.23352 | 2024-11-05 04:08:00 | NOAA-21 | SÃO LUÍS DO CURU | CEARÁ | Brasil | 2312601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 990246d7-22dd-372f-8464-99c1a6b0552a | -8.31643 | -43.57597 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed5c15fb-9120-3f3a-9c6c-3c30586c7890 | -4.27951 | -48.64531 | 2024-11-05 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f14770d-02fa-37dc-aaab-7436905f4286 | -4.05588 | -46.93386 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 740d2a48-9c21-33ea-9f8c-ebb6ef1b54e4 | -3.032 | -53.27061 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc7ad832-27ef-3e4f-b1c3-4505a07704fb | -4.35031 | -45.50586 | 2024-11-05 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d3cdff2-fafd-37ab-9637-7b84ff355562 | -4.50297 | -45.65129 | 2024-11-05 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eda7954-0731-3a5b-accd-33343cfe75e8 | -5.33456 | -47.31649 | 2024-11-05 04:08:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 954c64a0-c9b3-3804-9391-0e52155308d1 | -5.46778 | -46.2252 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93066b1e-7b98-3d9c-869b-83f607b4f8a5 | -5.83297 | -43.64392 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ca6b02c-bca1-34bb-813b-7bde21125ec9 | -5.47625 | -48.61786 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33b64944-a3ac-3319-af20-eaaed11ef9f7 | -4.34959 | -45.90234 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db726f2c-1bd9-3f34-9b44-bcc0bc24aafb | -5.4814 | -43.17993 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd0894d4-a4ad-33d9-9991-453e6044d904 | -4.25602 | -45.56309 | 2024-11-05 04:08:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92dd6120-eac7-34a9-97d1-20c92e12c9b7 | -3.5243 | -40.66743 | 2024-11-05 04:08:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c577ad1-adc5-346e-b86f-c9b6675921a9 | -5.79373 | -40.90294 | 2024-11-05 04:08:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 395d1582-b32c-3f96-a449-1e4995897843 | -2.65498 | -48.57495 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 805a5ee4-3b49-3dce-ba15-3e8e3986830d | -3.30653 | -46.02523 | 2024-11-05 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5630a75b-f44a-3be9-b1f9-423ba85857c4 | -5.98133 | -45.36888 | 2024-11-05 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b5cc001-b5f8-3ae0-bb01-b617bb6e1a21 | -2.09108 | -46.50269 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e566259d-4bbe-39c3-8925-8454424d8f6c | -6.51051 | -41.41125 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 305b171f-1e56-3377-b5ae-0f9d8e5d36de | -6.63421 | -39.90755 | 2024-11-05 04:08:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c36ada8-8702-3e8f-9665-8eb7618947c8 | -5.48586 | -41.65556 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 968d40c3-7262-38ed-856c-968434bde6ea | -4.5412 | -46.57148 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b8561a6-d276-3c8c-9965-a26f31ded4c7 | -4.37286 | -47.25537 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 612335c2-0f24-3a0c-8538-4fc741a8db7a | -5.69234 | -45.83648 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9674673-b20a-30e6-a8ea-4f03e24e8b0e | -4.38743 | -43.10468 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06f3f201-eaaf-3953-b0c8-2bef9062f9c5 | -6.47028 | -42.21272 | 2024-11-05 04:08:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ce2dd693-b1b9-3b57-921d-6ca5e16a4906 | -5.47395 | -48.61535 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18969077-0630-3dc6-a897-d3343ca1de46 | -2.64874 | -48.57024 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b6cfd859-7368-3838-a3d6-dc4c0d203df6 | -2.66158 | -48.56496 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e9e46f2e-0b5e-310d-b372-6665c8f489df | -8.34402 | -43.57674 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6eecb316-9137-3682-9501-fd2c7715e1f9 | -6.24965 | -43.56208 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f7618cb-be2c-3172-ac00-8a8d64728c7b | -4.9581 | -46.78065 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55eaa47b-2cb4-3246-8154-3f1ded983d3d | -3.54836 | -47.38239 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 63168e9b-9269-3c01-9e66-66a41abaf3aa | -4.06079 | -44.80752 | 2024-11-05 04:08:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b55e0950-9bc9-33c9-9e22-aa3e11a9391e | -3.21464 | -53.09842 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c810eba2-cae7-3cab-97fb-b55030382794 | -7.6324 | -46.57927 | 2024-11-05 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 006960fa-ae91-354c-9136-5eae5e745f83 | -4.88693 | -46.70802 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25b29b4d-4444-33d7-9d4b-3967836e620b | -2.56219 | -47.27921 | 2024-11-05 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab58c073-8525-3ce1-a9f4-1559569da570 | -8.10581 | -38.96721 | 2024-11-05 04:08:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae4dc5c6-01fe-3bdc-9a85-c243887e7e53 | -3.96444 | -46.37302 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 430c6d80-6d17-3c0b-a04f-e95114070ae9 | -5.21871 | -46.72318 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dcb95694-ff17-3a9c-8a66-4c34011edd30 | -4.26242 | -50.73046 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 760d6ab7-0c2b-3b48-8126-00c97b066d8b | -3.22017 | -53.10506 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e5b27e96-12ef-31d9-aba4-3a56d413ec96 | -4.62657 | -40.18285 | 2024-11-05 04:08:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8df3d736-f99e-30d6-874b-f7bc4de193e8 | -3.89443 | -42.82363 | 2024-11-05 04:08:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d32348b-af7d-3ab5-b1a8-43514f58016a | -4.26635 | -50.61012 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6ef7720-3e92-33c2-b062-40493e297f8c | -3.12121 | -51.10715 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dc52139f-427b-3f2e-8a87-2753a460a327 | -4.38626 | -43.11211 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd8638f0-8078-327d-be95-82445d8963a0 | -4.47076 | -45.70189 | 2024-11-05 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d123ae4-545d-3960-9e42-617c83ffbe0a | -2.8097 | -51.49597 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| be9fc966-5c5c-3c1c-8f07-12270b6434f1 | -6.2848 | -43.38552 | 2024-11-05 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c33c064a-f2aa-38da-8859-c790228aa75d | -3.36073 | -44.26187 | 2024-11-05 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dda054b-7d59-3056-ba3d-aa534584ecdc | -4.39461 | -44.6008 | 2024-11-05 04:08:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ee0b239-b034-3e4c-a1ea-418946aac249 | -4.3756 | -47.23842 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0968e8d7-6a2a-37e4-ba29-c28a91cb8f74 | -6.26008 | -44.13206 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b0518ce-6d3a-328a-92a8-66c5a0ff83d9 | -2.80159 | -51.48298 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7abad810-cddc-36b4-9a2b-839e4c996493 | -3.78256 | -41.60637 | 2024-11-05 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e14fd930-de18-385b-8001-e4e77585c274 | -3.96689 | -48.15754 | 2024-11-05 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8dbb095f-70df-387b-9e65-327c8ac48d20 | -2.64657 | -46.765 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25711e41-a49a-3547-840f-ca26028694fc | -3.56097 | -47.3887 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64e49f15-83cc-3702-84f1-307e16d3ad8a | -5.59936 | -46.18505 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fe93151-b15e-3f31-a338-4e9b166ad013 | -8.94035 | -40.77683 | 2024-11-05 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef3d9eb7-21db-3c63-b0df-a218bcb0f633 | -4.37056 | -47.24209 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 284e22c5-6eea-32dc-ad0a-a400055f9421 | -5.98888 | -43.36911 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 73c42e81-206f-3e1a-9e48-5a32455e4922 | -7.53914 | -35.12726 | 2024-11-05 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 73573bf3-31b4-3923-9781-623523baba34 | -2.71836 | -47.73282 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)
