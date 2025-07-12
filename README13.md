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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3179f9fe-7799-34b2-a39f-a469b650d17f | -18.94537 | -54.33159 | 2025-07-12 04:44:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d5cca0a-e269-3ca3-a18c-9646737f9f96 | -20.63026 | -55.33173 | 2025-07-12 04:44:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 12ebed1c-488c-36f5-81a9-051c800c7e12 | -18.66416 | -55.72396 | 2025-07-12 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 60232b03-a881-327d-b277-fe2756ce08d6 | -21.44321 | -54.57817 | 2025-07-12 04:44:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e10f29f-ca71-394d-a16a-feefecfea3d0 | -21.30613 | -52.79657 | 2025-07-12 04:44:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 825c2917-ad79-364a-ae7e-ec40bdd9f81a | -19.09067 | -56.04302 | 2025-07-12 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7a1ca239-13d3-324c-9250-49e01c2a0e69 | -19.99844 | -52.41724 | 2025-07-12 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d2eb9c7-1ff6-3be3-aaa7-c49d70410efa | -19.0943 | -56.04372 | 2025-07-12 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1451521e-7583-3924-8c3a-706146f03fa5 | -20.51334 | -54.67328 | 2025-07-12 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5bb207fa-357a-3d1f-84c6-8630546bbea7 | -20.51399 | -54.66941 | 2025-07-12 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dae3f302-ed9f-3f73-87c6-71e8a82b526c | -18.95218 | -54.33279 | 2025-07-12 04:44:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66d05615-aff4-3283-be5f-77e6c58e28cc | -21.1318 | -47.80126 | 2025-07-12 04:44:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4450c75a-a737-38ad-ba87-2556ace2b2c1 | -18.66341 | -55.72831 | 2025-07-12 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 65da26f7-15ef-3ecc-9a36-d179d76aefdb | -19.08704 | -56.04232 | 2025-07-12 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2e2863c1-7e20-3ba5-86d2-5d7a135fe234 | -21.7014 | -56.14179 | 2025-07-12 04:44:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90baea66-2610-3251-ae3f-ef2d2721ceec | -24.87778 | -52.03335 | 2025-07-12 04:44:00 | NOAA-21 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ba8581bf-d2e4-3396-96d7-1739d22e4a6a | -22.28576 | -49.077 | 2025-07-12 04:44:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9f0e4fd-b06c-3970-bc24-d367157a4d20 | -30.72184 | -54.21152 | 2025-07-12 04:46:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| c541d9f3-a77f-3049-9107-9b58f1da40bf | -30.1519 | -52.02341 | 2025-07-12 04:46:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 8a47bec8-1137-3829-a6c1-6e7535db82bc | -10.8986 | -49.204 | 2025-07-12 04:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 6abf7e4f-8d8e-3f85-afd0-c4056579fa34 | -5.8598 | -48.3953 | 2025-07-12 04:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c870c5e4-6ce5-3c83-ba02-e91c36d262c6 | -5.8412 | -48.3964 | 2025-07-12 04:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 554e7f75-8b29-3586-abc3-a461927e0b3f | -5.8598 | -48.3953 | 2025-07-12 05:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 37dcad7f-24e8-389f-9836-99029c6e37d0 | -5.8412 | -48.3964 | 2025-07-12 05:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 21dfbbef-ea47-355d-85a9-b822c53a2040 | -4.60721 | -43.31786 | 2025-07-12 05:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7f4e6b2-55c6-3e6c-9e04-658e6a0eafe3 | -2.55062 | -47.7061 | 2025-07-12 05:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6754cedc-c374-3fbf-87ae-3b6e33c60d20 | -7.08184 | -43.50636 | 2025-07-12 05:06:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 647f8967-a54d-3bb0-b4a2-c3b1eb9ad7ac | -7.99205 | -46.4049 | 2025-07-12 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12cd41e0-4614-3d0a-923f-8aacca2dde36 | -9.50807 | -47.56424 | 2025-07-12 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4290127-cae2-3b73-9b5d-505cd5eb1c0e | -8.68764 | -47.9871 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81cf5db5-d2ee-3cc3-a774-bc1256887790 | -5.78292 | -45.1174 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f22955ab-8989-33ad-8765-0cf564dc5e51 | -8.01111 | -50.10111 | 2025-07-12 05:06:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3deba01d-1ef9-316e-8494-4a5766c44a4b | -7.08432 | -49.6063 | 2025-07-12 05:06:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15cd1685-2491-3e67-9c13-29a75cf5dcc4 | -9.50764 | -47.56751 | 2025-07-12 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7309cea8-9adf-34b0-88b3-91124b832c7e | -6.63098 | -56.27819 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d51984d-40e7-3274-bb4d-a4456d63d364 | -8.68589 | -47.98577 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 466dc9ab-f967-3c4e-8ccc-8cdc8e4e0949 | -5.84233 | -48.39408 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| d6442981-d868-3115-a0c0-fe553fedd9be | -5.78661 | -45.10117 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36f24755-0200-3810-94e1-b96767aa9a82 | -7.91904 | -61.55093 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 614c99a8-c2e9-350d-80cb-5fae41f1781b | -8.68723 | -47.99002 | 2025-07-12 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b67741a-a6e5-3600-a9c6-d53f1f79b6e6 | -5.78348 | -45.11329 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85246763-87a8-316c-80ac-4c20efae3c42 | -7.99058 | -46.41587 | 2025-07-12 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f65d68da-8657-3bc6-a962-501bed8e9039 | -8.00018 | -55.27658 | 2025-07-12 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eec758f2-fb95-37b9-9977-295f3aae6dc0 | -5.84091 | -48.39754 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 299bfe19-04ef-3860-9154-85d27418827f | -6.25002 | -43.36956 | 2025-07-12 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f297ed1f-4ebf-3c25-a286-0f6912d9fa54 | -5.84562 | -48.39824 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 002f7176-3ede-3431-ab2e-0e2a467b0240 | -7.93082 | -61.55677 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab1dea71-8df4-3769-93d3-807d8a8f396f | -7.88501 | -55.36339 | 2025-07-12 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c790897e-9fff-359e-af34-67840294b033 | -5.79073 | -45.11433 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab641ea0-4602-30da-a208-94467c2837ea | -10.87006 | -45.08038 | 2025-07-12 05:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b46d7bb8-6344-32cf-a743-e9cc7d9a8c18 | -5.84302 | -48.38918 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 467f6ce5-ed44-38b5-94a4-61cbbb8a7ca3 | -7.08371 | -49.61062 | 2025-07-12 05:06:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0053f8e1-30a9-3ea2-81e1-bba8855ff51c | -6.6138 | -43.88446 | 2025-07-12 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ad3821c-e68d-3fe2-987a-586b2e1dfbe2 | -10.87635 | -45.08127 | 2025-07-12 05:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aed900be-abf4-33b7-8a2a-2394914f157f | -8.47535 | -49.6153 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78bb6280-ab4e-3aca-8405-02176c33a56b | -7.48498 | -43.93634 | 2025-07-12 05:06:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa7bdd9c-9d42-32b8-b989-a77b8dfeac65 | -5.85033 | -48.39894 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c40c90de-6111-3418-8d3b-fc0fd4953492 | -9.85535 | -47.8753 | 2025-07-12 05:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd5157a8-f07b-3de7-b116-8c2127272018 | -9.80136 | -48.5724 | 2025-07-12 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcc6f07a-b3d9-33d5-a860-455e169c141f | -5.84164 | -48.39263 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| b51f7a6a-d970-3ca7-92d9-61a85ecb9aad | -5.78514 | -45.10106 | 2025-07-12 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 891c6a5a-73a0-37b6-9f66-bc1c33ba2158 | -4.66367 | -55.96659 | 2025-07-12 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4427e367-0842-3d09-bde9-b02c473db21e | -5.14326 | -60.37876 | 2025-07-12 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edc2c77e-2f65-3ff5-a951-469fd53d6276 | -7.60942 | -49.93792 | 2025-07-12 05:06:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 707f9f06-386a-30d9-b8ab-e04df6cdb8b1 | -8.47214 | -49.61348 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9421fb11-217c-3585-9c67-8a156b8cc4b5 | -7.49152 | -43.93678 | 2025-07-12 05:06:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd8e87c6-91db-358d-9e4a-1e5a6543fa0d | -8.01052 | -50.10529 | 2025-07-12 05:06:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdf37861-7ee7-31c8-b4df-29e0200773e9 | -5.84634 | -48.39976 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a7c589ff-adc9-3d98-be8f-670ae796d2e9 | -7.94921 | -49.65419 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73d6a59b-ef46-310a-b84f-0dcfd5d3a61a | -6.62987 | -56.28515 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bae794a3-c625-3c98-91cd-a135a27aa659 | -6.61489 | -43.88586 | 2025-07-12 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| de4de42f-6908-3b61-8f19-f2b9d9ace923 | -8.92447 | -47.34842 | 2025-07-12 05:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 617a9223-adab-3ead-b06f-8d3d50af6eed | -8.91873 | -47.35096 | 2025-07-12 05:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0fe868f-b8fb-3ff9-bf45-9e113594fe6a | -5.85107 | -48.39394 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3aba16bc-1bde-3988-9692-4e90f7a9c31c | -7.92668 | -61.55606 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a849b2a0-dbb8-3ca1-9875-fa2ed795455a | -9.5129 | -47.56829 | 2025-07-12 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 726eca13-3953-3b63-be0e-48bf312ba7ab | -8.47018 | -49.61922 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cefa0890-e80d-30d2-9b26-08640308044b | -8.04131 | -50.10624 | 2025-07-12 05:06:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09d57136-dadb-3d53-bb0c-631727bbc514 | -6.60738 | -43.88354 | 2025-07-12 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 779ac7b3-9c14-3189-8245-ce3bc77da293 | -8.47603 | -49.61862 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46ecb434-b24b-3862-beb1-40719802a094 | -7.78068 | -61.3681 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 531fbd9f-cffe-3896-b2e8-c8212bd338b0 | -7.22869 | -43.1036 | 2025-07-12 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b6632a2a-bacf-3d4c-b279-fd90bc847dd6 | -7.99011 | -46.41939 | 2025-07-12 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6130566d-25d0-3f1b-9b4d-c228b7c61ccb | -6.6142 | -43.89104 | 2025-07-12 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29b4bd90-75fa-3e37-aa93-a5d48d34dc7f | -7.86588 | -56.62173 | 2025-07-12 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2489fa46-0ae1-38d4-9ccb-f7c44d1208c7 | -8.91917 | -47.34768 | 2025-07-12 05:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdc3613e-25c3-39a8-be88-7787ef0144be | -5.84705 | -48.39474 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| c79e70f4-7b00-3f9a-aebc-c694d435cda2 | -5.14783 | -60.37594 | 2025-07-12 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c34dfaf-dcea-36ea-bf30-676554c70b65 | -8.47469 | -49.61984 | 2025-07-12 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4e2b0aff-0e51-3d36-a816-7a5b41addbab | -7.22295 | -43.10205 | 2025-07-12 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b0cb0f02-fc50-33a6-a8f6-ac52c41b9954 | -7.90725 | -61.51124 | 2025-07-12 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62505301-309e-3f73-8f3e-673422b82850 | -7.22973 | -43.10309 | 2025-07-12 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 99d64ae8-78ae-318c-9892-c8cc50887d41 | -4.23873 | -53.4908 | 2025-07-12 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66821f18-eda5-35cd-8ab7-583e3c2b67c7 | -9.79717 | -48.56631 | 2025-07-12 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2762f9d-1564-36d9-a755-0a81f1ddec07 | -7.984 | -46.42265 | 2025-07-12 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f203fd80-5522-3aae-b3c6-7001a6461bb6 | -5.85176 | -48.39545 | 2025-07-12 05:06:00 | NPP-375D | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75f36ef4-e3a6-3c42-93f9-b62c41726c07 | -9.85491 | -47.87854 | 2025-07-12 05:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da55a45-bf93-3c1c-b031-a5899967005f | -5.12312 | -56.1177 | 2025-07-12 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 136ad9c6-9154-399a-96c6-bc00fff8a40f | -9.91582 | -47.82682 | 2025-07-12 05:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a6292cf-e2fb-3e47-afdc-ead15332bbd6 | -7.98962 | -46.42301 | 2025-07-12 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README14.md)
