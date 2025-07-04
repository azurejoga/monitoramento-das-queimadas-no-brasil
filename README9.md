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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bd1b28b-814e-3995-856a-1250d8881bc5 | -10.34595 | -47.29087 | 2025-07-04 04:17:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e395447e-cc1f-3ef5-8869-7aa3673bb352 | -6.6099 | -43.88626 | 2025-07-04 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| b5b2a768-66f4-35a7-bc7c-d3a22dd901c5 | -11.92585 | -45.39949 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 065eca5c-d08a-3269-838b-f06ae195b93e | -6.74306 | -43.15499 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9596c2ca-b1a8-39af-9f31-641a5f30e26f | -10.55813 | -49.13165 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| bd1e0dbf-0cb3-39a7-b13f-633973b398d1 | -10.96049 | -48.37542 | 2025-07-04 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71e394bd-0b40-3637-ad4a-754121272ccf | -6.89381 | -43.2108 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04b806ce-c377-3321-adaa-890fcacb15df | -10.64673 | -44.48743 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcc6665c-17b8-36ba-9fae-dfe44e883af6 | -7.1093 | -47.84963 | 2025-07-04 04:17:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 74894192-a1b5-3a18-8fae-e005c62a978d | -10.32701 | -49.93601 | 2025-07-04 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10e134d6-6eef-362d-a580-eb64af2281e7 | -6.84859 | -43.30321 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7aa30b02-477f-34e4-b7ce-8f0924ce5c9b | -9.6117 | -49.02064 | 2025-07-04 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78672ad1-a029-3afb-bef9-a73d9c00d17a | -11.93255 | -45.4006 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38cd46d6-7712-3749-a2ba-57302193e9f4 | -12.16592 | -45.53196 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 294f1fad-35d7-3244-ada5-32832f619193 | -11.48615 | -48.44625 | 2025-07-04 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ac11d8f-1319-31f3-b669-52a3ae3b9b4c | -6.61267 | -43.8903 | 2025-07-04 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baa55cd8-08ac-3090-80c1-20c60c7ebacf | -10.2775 | -47.88291 | 2025-07-04 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f9c84f5-7a94-3f5c-9251-211d6a745ddb | -9.79694 | -47.75157 | 2025-07-04 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2011cda3-1638-369b-bc11-c2aede09cbdf | -10.98549 | -45.0983 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58574a9d-fda3-3647-a876-6f2c1911a0bd | -11.9209 | -45.3876 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac3b8abc-7df8-3431-b4c1-37a60be783ed | -8.32707 | -46.29033 | 2025-07-04 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdcf7705-962f-36bf-b665-e3792d6652ec | -11.20628 | -49.00016 | 2025-07-04 04:17:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4a9ca57-ffac-3de4-80d8-7a370cde87a0 | -5.91784 | -43.45085 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 30e5eb06-a669-33fe-9ed7-b36a9c1dbf8e | -6.66256 | -43.17437 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 185ae917-ebbb-36e5-9002-e54ffd0fdf0d | -10.62127 | -48.42079 | 2025-07-04 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1f85049-8c7a-3338-87a6-b81766247459 | -7.35121 | -44.8371 | 2025-07-04 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25c1a2f6-f3a7-36f1-9a69-ed6a79d159ff | -11.91696 | -45.39067 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f80cf1d-e1c2-39ba-b8c1-7beab385f77b | -7.07458 | -43.22201 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 52338219-5db8-31a0-a8cb-0f9d2d922620 | -5.9151 | -43.45037 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26359935-39e2-3c2d-9112-19a0f4f78308 | -7.22069 | -43.0884 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 33fd24be-dd42-30df-a756-acb39d79f4d2 | -10.66405 | -49.45047 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5756a9b-c8d6-3dac-ab9a-f0a2ab5a5349 | -7.84476 | -44.21616 | 2025-07-04 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b99b815-9d27-3f6f-8c6b-7c4f90b26700 | -11.92978 | -45.39645 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d18d9774-e9d2-3f59-9611-c2b125c4cdb3 | -15.98432 | -43.61322 | 2025-07-04 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ab9c8cc-973b-339f-b5a9-66ebf5a7da08 | -7.20272 | -43.58737 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd6f86d6-c934-3fd7-8a76-62be12cac4d7 | -11.9225 | -45.39893 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7c6eab2-53fb-34d3-99a3-b9fa3f45c0e1 | -8.45144 | -49.63285 | 2025-07-04 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94c42d83-0309-3a4e-b589-1570e8f1c81c | -10.64617 | -44.49094 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6beba67-0a89-32d7-b12b-8c6a3d5ceb62 | -6.74361 | -43.15152 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da971ac2-09d2-321b-ae1e-968958f86e75 | -18.715 | -46.61133 | 2025-07-04 04:17:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d953f3d-c3ad-3f94-9780-f24ed7e9e709 | -6.83794 | -43.71478 | 2025-07-04 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67276982-d9d4-340a-a702-86d5d237ccca | -6.11083 | -46.18417 | 2025-07-04 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eedddce-faa2-361e-a374-db75955da413 | -10.86795 | -54.04701 | 2025-07-04 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 483a6666-58c8-3397-a970-a2379ddc50a0 | -7.11015 | -47.84456 | 2025-07-04 04:17:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8667a90a-2b55-37cc-8d86-bf8ff44222d0 | -7.42323 | -37.20808 | 2025-07-04 04:17:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 384b828f-072f-319b-bc9b-4feb9e6dd352 | -8.20477 | -44.93913 | 2025-07-04 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dc86528a-9f47-3d65-90ba-c706925e6e1f | -11.47129 | -47.92229 | 2025-07-04 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b124735-483e-3e93-9bd2-78d6a21887bc | -12.13627 | -44.91173 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 217bbebe-b98d-3a0e-bdcb-0c5ef964fa66 | -7.22291 | -43.09587 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3d6b9035-e619-3e22-92a3-e8c613d8cd3f | -7.00028 | -43.54115 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b340c81-3c98-3f6f-9438-c9d5e911f4ed | -7.22846 | -43.10387 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e07aacf-884b-3b1e-a6b8-d6763b2fc4e1 | -11.92192 | -45.40252 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d4442d8-65c2-34dd-aabb-62934176402e | -10.88879 | -56.45513 | 2025-07-04 04:17:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a34b9ca-4fad-3929-9580-764c9bdd8ee6 | -7.35576 | -44.83042 | 2025-07-04 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c524a8c-f33d-3eaf-8c4a-594a9e68f2b4 | -11.52672 | -48.95864 | 2025-07-04 04:17:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5af76f7-7945-3453-be11-830ab40f0a07 | -6.60914 | -43.04099 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44088e6f-ee28-35b9-aa11-2afe85c7bef3 | -11.91638 | -45.39426 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ebe0ce31-7567-33cb-8edf-737280c29c4e | -16.60644 | -49.36925 | 2025-07-04 04:17:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86011d9b-218e-3f4e-9d7f-2329b08151c7 | -7.35062 | -44.84071 | 2025-07-04 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbf8a7ca-d2a5-35e3-b444-6955c8b40599 | -11.93487 | -45.38626 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4388a220-93be-3ed8-8d63-ea33fba6c81d | -6.73197 | -43.13902 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 219424c0-e9ca-3d57-a50f-ec1e8462aaec | -18.90946 | -47.01271 | 2025-07-04 04:17:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a30f5c20-c42e-3f8b-849d-9606ecfcede4 | -9.08587 | -48.32157 | 2025-07-04 04:17:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d596b0b0-5c8c-3e8c-8ba7-17153d43d807 | -11.92425 | -45.38815 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a899d94-bca9-3211-a54b-64e63c27e97f | -7.88069 | -47.88562 | 2025-07-04 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc1ade0-4395-363f-9798-b48d07bbdd6d | -10.24677 | -47.67741 | 2025-07-04 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b7d58fd-5afb-30d0-b393-3d209b009be4 | -8.86657 | -47.27542 | 2025-07-04 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85d3f6ed-cf06-3518-9b5e-08de7aa07280 | -10.55876 | -49.12803 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ada76cb-566b-33e8-984d-742d8e31b024 | -7.0779 | -43.22254 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c559db1-91ef-3ee1-8f8e-48a713e25fc7 | -6.93334 | -43.04635 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c29648dc-0099-3195-9dec-754b5dcfbee8 | -7.12814 | -43.16288 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d4328ae-e25b-3f32-ae46-88380efa3ea6 | -7.8543 | -47.87611 | 2025-07-04 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ab5793-f34a-39ee-bbeb-d422e489421a | -7.19468 | -43.42591 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f6cb06c4-3913-3896-9254-3fe4b2f7daa0 | -8.30445 | -49.07475 | 2025-07-04 04:17:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd35ee6-4f81-34c7-b56a-5616d2e5faf9 | -11.24545 | -44.89297 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1c3a3ce-8a1a-345c-a2af-8eff6b156150 | -6.88608 | -43.21668 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 264b717d-ab34-3b63-bca1-164211dc1022 | -9.74213 | -48.35209 | 2025-07-04 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 357f9193-792f-3fa9-a949-e6930ee14f19 | -16.94752 | -46.08596 | 2025-07-04 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e75e485a-bca0-3143-a80e-42409f5a6461 | -7.22401 | -43.08892 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 65c4e5c1-b084-3e1c-a760-b407334b2bb1 | -8.38104 | -44.05378 | 2025-07-04 04:17:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99acb6e2-8c93-358c-ac16-c18bdf23eb71 | -6.59312 | -43.05623 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae1bd3cb-777c-3683-be16-46825fb8851b | -17.86535 | -44.57325 | 2025-07-04 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 031ecaaa-e7a6-3ac0-8f7a-30e631f9a283 | -11.84171 | -47.55056 | 2025-07-04 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7865ade-7fe3-3d26-811c-ce7d73dda44c | -15.13512 | -47.47343 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5be9d8eb-8da3-3d85-b27a-0e2f8ac7ab33 | -6.65734 | -44.3098 | 2025-07-04 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2be2dc7-9eb9-30d5-9a80-6c987b4fed6f | -6.80225 | -44.75372 | 2025-07-04 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3deab7b1-ad13-3bd9-a531-e74334883361 | -8.44713 | -49.63205 | 2025-07-04 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4dbc1e77-9eba-3350-af4e-4a03ba662b4e | -6.89272 | -43.21773 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3eaf2e75-cd88-3a06-a222-58991416fc17 | -6.77432 | -45.54262 | 2025-07-04 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e309585-3104-3077-8154-955982c19f50 | -8.44783 | -49.62797 | 2025-07-04 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9c211ace-2704-36b7-a231-3def1ce6136e | -8.21491 | -44.94078 | 2025-07-04 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f18a8730-07d7-3b48-98a7-3d13350afeaf | -11.92643 | -45.39589 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71ecb002-d120-3831-8a5b-f828a4d570e2 | -7.08725 | -44.16787 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9873a73-caec-365b-bd76-972f9f4874ab | -11.4729 | -47.9248 | 2025-07-04 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b250fd5b-d7be-3412-bd39-3d3fdf44e9aa | -6.99585 | -43.54758 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 727b85eb-0090-3b6f-9c26-42ea1b567f51 | -6.74255 | -43.17979 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df6f68d0-9fb1-300d-aa2e-1fea4934b403 | -7.91289 | -44.54315 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08790972-c614-350d-ac97-200d36d4b6d2 | -7.09207 | -44.38659 | 2025-07-04 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a19ceba4-50e7-37fb-9a98-92e9d7492210 | -11.5105 | -48.45343 | 2025-07-04 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89d996e0-c9f0-3db3-80f8-cc2e440b3403 | -11.49486 | -48.07468 | 2025-07-04 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
