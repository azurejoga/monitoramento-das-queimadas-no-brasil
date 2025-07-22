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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b7fd0b6-c3c5-3c8e-b263-d513897a3dae | -12.50389 | -57.76861 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7256f845-e7e1-3b81-be4e-a9a13eb8f8cc | -11.73271 | -48.18956 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95cd29a1-46a6-3d1b-bfe2-8ac1ca0e0b8e | -11.31282 | -55.11741 | 2025-07-22 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daa31833-62c9-32b7-a703-fce9fbf8530a | -10.04808 | -59.10183 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c079829a-3853-3f0d-a0ff-13e5d988da47 | -11.30612 | -55.11631 | 2025-07-22 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f06f100c-ad77-3087-8c3d-32845a02873c | -13.69087 | -45.68583 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 381fb7c1-b423-385f-976a-d07ec90d5c93 | -10.23419 | -56.76904 | 2025-07-22 04:53:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b6c4584-0add-3320-97e3-81b476d0a30b | -19.94939 | -54.38457 | 2025-07-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cede6702-0d6e-3737-8f3a-089728135353 | -19.61175 | -43.14963 | 2025-07-22 04:55:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ff993160-e5fd-3479-8810-3122f279fa2a | -18.95986 | -45.73717 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58d61cfc-afdb-3e3e-8ab5-2a81a9de4fea | -20.4772 | -53.67717 | 2025-07-22 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7704a6bb-86d3-3e0a-87df-e64cd54884da | -21.11327 | -48.64221 | 2025-07-22 04:55:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ff1c93d0-757b-3fe3-9fd2-c16633200ce3 | -21.01925 | -56.0057 | 2025-07-22 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14c7546a-5edc-3b11-bfa5-e92346a7a762 | -17.59972 | -50.64954 | 2025-07-22 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 125c4270-0c8a-3de5-b2a3-79cb2ff63f39 | -18.19937 | -45.04702 | 2025-07-22 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 00a7f2a8-1620-3041-906a-b4600eed22fe | -17.98469 | -46.00126 | 2025-07-22 04:55:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b641392-9e58-3d95-a192-e96963c1f3bb | -18.38178 | -47.16956 | 2025-07-22 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7da151d-198b-3b62-90e1-5f91de6e5a8f | -21.68226 | -57.39881 | 2025-07-22 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d194940a-3519-3a3b-8fab-7b0961f096ab | -20.31244 | -46.6762 | 2025-07-22 04:55:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 512a0231-a3bb-3e1e-8661-47585a2ee00e | -23.33997 | -51.90275 | 2025-07-22 04:55:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8de7351a-7856-3bde-a757-0dfcf38ec722 | -19.15914 | -46.56128 | 2025-07-22 04:55:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82e63f23-9e72-3cff-86e6-e0dd9ff97bdf | -22.29036 | -56.00517 | 2025-07-22 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6b4ec63-6315-34ea-bf0a-f6081afbd00d | -20.30667 | -46.68068 | 2025-07-22 04:55:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1802f76a-bc85-36a0-9c2a-056ae5eb9d41 | -20.06335 | -41.39864 | 2025-07-22 04:55:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 32cb23f5-dd2c-3302-a2ea-901ba1c48f86 | -18.66364 | -55.72078 | 2025-07-22 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3e485ade-8cc4-3e50-82ea-68fa62a8df34 | -20.64415 | -56.55335 | 2025-07-22 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 54081ad9-1211-3019-8bad-5053774b330b | -19.61202 | -43.14896 | 2025-07-22 04:55:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9d9d8b11-71ad-3955-ba6a-d3f245a74959 | -18.47918 | -44.35843 | 2025-07-22 04:55:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58e33565-9ff6-3432-88b5-c5fd1605755c | -19.57418 | -46.95663 | 2025-07-22 04:55:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09c12f74-df92-3465-bb6c-0dfa6663ac16 | -19.50974 | -45.93598 | 2025-07-22 04:55:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f339a6b-4736-3753-9f81-028e7764d79d | -19.164 | -46.56522 | 2025-07-22 04:55:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4894cab-8eeb-3a39-b9a0-ea97933773cb | -18.3733 | -49.2695 | 2025-07-22 04:55:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2f86f81-14a0-3d4e-8828-56bba68dd0c2 | -18.98858 | -45.78359 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50f60a4f-91f8-3b4a-9caf-ca269001d901 | -20.26529 | -54.80049 | 2025-07-22 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8c2d12da-84c8-34b8-828f-d1efab8016ab | -18.65976 | -55.72384 | 2025-07-22 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9519f284-9f85-3599-a78e-c2a79b9e5679 | -22.61275 | -54.93382 | 2025-07-22 04:55:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8694c575-d92e-3fb6-a618-5d358561b95e | -18.61767 | -44.2666 | 2025-07-22 04:55:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 551bd00c-3746-36d8-8c0a-f24e614b4478 | -22.17171 | -52.69975 | 2025-07-22 04:55:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6341bfc3-6112-346d-90ea-8a7689bef159 | -21.02313 | -56.00259 | 2025-07-22 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 650095d9-a0a2-32b2-9e12-092166af23b1 | -22.1622 | -47.37086 | 2025-07-22 04:55:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 5d209e44-4d5a-3751-9e82-2b4ebdecbd59 | -22.82593 | -46.14643 | 2025-07-22 04:55:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e7eed6db-230a-3d66-9b0d-0f9ff8f6fb74 | -18.95939 | -45.73702 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 973c55d6-d5ee-30af-b76d-f181a5f39976 | -18.66307 | -55.72441 | 2025-07-22 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7d8a96ec-6d55-34e6-b460-710f82c4d962 | -22.61218 | -54.93773 | 2025-07-22 04:55:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c09e242a-e544-3ebd-81c6-13c1192754f2 | -22.17233 | -52.69503 | 2025-07-22 04:55:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 29f8b4b3-625f-3e36-ba6f-869b92db5a28 | -18.20191 | -45.04477 | 2025-07-22 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| daa5b123-df3c-3880-97ab-4845f4e739c1 | -20.20548 | -56.61634 | 2025-07-22 04:55:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 15d6993e-f005-3e06-ad4b-d077c779a204 | -21.68479 | -57.34109 | 2025-07-22 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1de92cea-eba2-34ac-b5f2-30cd5400ade2 | -19.41523 | -44.96258 | 2025-07-22 04:55:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca3393dc-2348-3fd8-b5df-62d05c213511 | -21.01982 | -56.00201 | 2025-07-22 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f64ae28-f6e4-3f93-9f89-c6464b2cdbd1 | -22.17296 | -52.6903 | 2025-07-22 04:55:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8bde15d8-04a1-3e4b-9a5b-80cb1d12f50d | -23.30029 | -46.95644 | 2025-07-22 04:55:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 70d7f375-ed88-3c53-8a7b-593d311c9854 | -20.05997 | -41.40539 | 2025-07-22 04:55:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8152da3f-ac13-385e-b1c9-bff6bc33b77b | -20.47922 | -53.6749 | 2025-07-22 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e345317d-d5e8-3797-a71a-c26188e10983 | -17.59581 | -50.64898 | 2025-07-22 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea5fe41-4599-345c-9c45-b6494068a8a2 | -20.64142 | -56.54907 | 2025-07-22 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 218d10e7-4b91-338c-8ba7-9c0a263c81c0 | -22.48438 | -51.52934 | 2025-07-22 04:55:00 | NOAA-21 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8d51031c-2c19-3a48-a01e-fcd605b7ec42 | -21.4681 | -57.10517 | 2025-07-22 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fa0eb1d-2b10-36db-b848-0cc39773262c | -18.99406 | -45.7843 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c793addb-cdfd-3a65-8168-583701ade54a | -21.47034 | -53.06753 | 2025-07-22 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 002be11f-e7d0-389e-a01c-424cdbb6bfeb | -23.30065 | -46.95243 | 2025-07-22 04:55:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0a20a7d6-03e9-355d-bece-31b8ed488309 | -20.06251 | -41.4109 | 2025-07-22 04:55:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 86480ecb-a921-3462-a377-01203efb7f57 | -22.16926 | -52.68976 | 2025-07-22 04:55:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f00ee789-3e43-34a8-9d55-b523e455786e | -21.28758 | -56.20435 | 2025-07-22 04:55:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43bf0c48-fb5e-3254-9a54-bd4c554cb933 | -21.01593 | -56.00512 | 2025-07-22 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5841b265-8a1c-3f6a-8bed-06c3af3dc747 | -22.8315 | -46.14728 | 2025-07-22 04:55:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 37d55e4d-905e-3f94-a9cf-cca3affa73fb | -20.30697 | -46.67775 | 2025-07-22 04:55:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c6f4df2-eab9-368c-948c-38ad0e00d398 | -18.19981 | -45.0428 | 2025-07-22 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d9ec17c9-fe4c-31b1-8694-4954db6f09a8 | -22.82561 | -46.14991 | 2025-07-22 04:55:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fc6e9c5f-9274-3fb0-9c46-d08ce79921b6 | -18.13025 | -44.2796 | 2025-07-22 04:55:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 871bd6f5-65b7-3cc8-8fdb-9607d8ee8fbd | -21.68349 | -57.39126 | 2025-07-22 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c11a9797-98cf-3cd6-b71d-45316b809863 | -21.03924 | -55.98646 | 2025-07-22 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1849895-ae4f-36f7-98f1-0ea0f4ea4458 | -20.30639 | -46.68348 | 2025-07-22 04:55:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 040a4f51-1f28-3bcc-96fd-fac322f95841 | -18.99916 | -45.78872 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69f730fa-e8da-3b34-84cf-86c0b74a630d | -19.61834 | -43.14912 | 2025-07-22 04:55:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 44acea7d-5caf-3c6b-a159-8f47b7a65817 | -21.68418 | -57.34486 | 2025-07-22 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2e4e198-b8c7-3f2f-9101-70af48574ecc | -22.48098 | -51.53268 | 2025-07-22 04:55:00 | NOAA-21 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| da636a16-59e5-3151-a9d5-2877f80a2df6 | -19.92153 | -52.30613 | 2025-07-22 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d827f940-5981-31b9-b85c-fe42e421df14 | -18.19624 | -45.04385 | 2025-07-22 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f245a245-30a2-373a-9bc8-4d0631061c37 | -18.9893 | -45.77644 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8ba1fcd-497d-3ea2-b558-648040b52a41 | -18.19414 | -45.04192 | 2025-07-22 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9703521c-247c-3ef6-9169-3a8b5eaf14fc | -23.30282 | -46.95271 | 2025-07-22 04:55:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1f8f7119-9c7c-3d13-a95c-1335a8aaf6a7 | -21.34713 | -48.67546 | 2025-07-22 04:55:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cc57425-5285-3994-8a05-9ddb3d41361f | -17.59649 | -50.6438 | 2025-07-22 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6f8025f-9521-3ea3-8121-e85ec5e49668 | -21.04256 | -55.98705 | 2025-07-22 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6cae622-42d2-3c48-8ed8-6969c97c8506 | -18.19666 | -45.03952 | 2025-07-22 04:55:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f73dd63d-8c50-3796-8d26-5644d844195b | -18.98894 | -45.78004 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d62c9715-8e2d-3d32-8152-36f15d7198f6 | -20.06736 | -41.40317 | 2025-07-22 04:55:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 957b3e21-1f3d-3da2-95b5-eff5ed9de33b | -21.66271 | -46.93918 | 2025-07-22 04:55:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22c05d81-6fa1-38d5-a8e7-ec1d92ed7153 | -23.30243 | -46.95672 | 2025-07-22 04:55:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 897bc6e2-9bc7-38a2-b12c-2264ae24c807 | -19.61859 | -43.14846 | 2025-07-22 04:55:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 180a396c-2174-3a35-9470-f8338bf37c0f | -18.99442 | -45.78071 | 2025-07-22 04:55:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b15da42-7e73-3255-9cf4-7c5ba68f01d3 | -27.27765 | -50.84895 | 2025-07-22 04:57:00 | NOAA-21 | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 899e5fdc-6875-3331-9f0b-b5ada7dc4224 | -27.19945 | -50.5813 | 2025-07-22 04:57:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ece01b8-7fd7-3ac1-9a0f-3a5d948422ab | -8.5211 | -43.3063 | 2025-07-22 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 37a7be3e-3248-309c-9ab5-825ce389aaa6 | -4.388 | -43.2896 | 2025-07-22 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| fb46c691-22d8-3bf5-8a0e-ab812346ef9a | -11.7317 | -48.1849 | 2025-07-22 05:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 98053a35-72a7-300a-89a4-5007ef364ef0 | -8.5211 | -43.3063 | 2025-07-22 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d255e11e-48a8-35f6-bce2-6e1319726912 | -11.7317 | -48.1849 | 2025-07-22 05:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 363d98d4-b946-3af5-b6c6-4aac7a6d9398 | -4.388 | -43.2896 | 2025-07-22 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |


[Clique aqui para ver as próximas entradas](README17.md)
