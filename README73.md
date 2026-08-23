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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d400841-e6fb-3ab9-b34c-b104b1dc7212 | -14.44592 | -51.80427 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2033566a-cb5a-3c3e-8a77-a05b740e4b99 | -14.31179 | -51.83964 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d5e9b625-5813-3225-9d71-2a3578462477 | -14.33986 | -51.77209 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 87416134-17d8-366c-a784-149fd749d433 | -15.33387 | -46.07494 | 2026-08-23 11:55:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6b55158e-22a1-395b-8e01-062bb0adf6b3 | -13.23682 | -51.43513 | 2026-08-23 11:55:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 48f988c5-eed9-3a37-8414-4087ed614de9 | -14.34892 | -51.77348 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7889f2e9-2189-3638-924f-e47090ee7768 | -13.15362 | -51.4358 | 2026-08-23 11:55:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 536a5fb6-79d9-388d-b472-b4705c5f1152 | -15.44748 | -43.06618 | 2026-08-23 11:55:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 3f411d95-c1eb-3fdd-ae5d-839e4f47c1ce | -16.05746 | -50.42372 | 2026-08-23 11:55:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| d06e4f23-3b7e-3076-a2dc-965ef1d7be6f | -16.04732 | -50.43157 | 2026-08-23 11:55:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| a299a0bb-b50e-3bdb-8cc2-c493521a3a92 | -14.36753 | -51.835 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ec6b5130-a953-3b48-b908-7f1a0c685df3 | -15.43951 | -43.07191 | 2026-08-23 11:55:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 4c4a23d9-938c-33e2-9275-9a8bf551fb3b | -14.37609 | -51.77763 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 23ce09e9-f810-38aa-9956-acbb99a446aa | -14.99557 | -52.69215 | 2026-08-23 11:55:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c573569a-2ee4-39b2-aeeb-e339a5ecf9f2 | -15.34422 | -43.97814 | 2026-08-23 11:55:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b9c80a6e-0245-379e-87b2-74689c3759b6 | -15.3466 | -43.95748 | 2026-08-23 11:55:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 28c3d137-b5a6-354e-a4fd-4e33e214e86b | -14.57494 | -53.02948 | 2026-08-23 11:55:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8b1f4ca9-69d5-3abe-a761-2a91baa69e09 | -15.5141 | -49.83118 | 2026-08-23 11:55:00 | TERRA_M-M | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d80f1cc7-bfa7-3f35-a8b4-047749e002da | -15.25235 | -52.82479 | 2026-08-23 11:55:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 11d5648e-576d-3aca-b4e9-7658fa629ae7 | -14.58782 | -53.00925 | 2026-08-23 11:55:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7c54ff3e-2937-3ae7-a011-5cb21e021f6a | -14.57659 | -53.0187 | 2026-08-23 11:55:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2404f6a3-c99f-3a1c-89c3-79477f859bdc | -14.4109 | -51.79275 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9d7de29e-93a9-3629-9ee5-5dd78cf70015 | -16.06502 | -50.43417 | 2026-08-23 11:55:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| aaef0d3a-ab98-376b-82a8-4b0632703a35 | -15.34554 | -43.96393 | 2026-08-23 11:55:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9f999b76-2f6d-32f5-92ad-47052bbf88f1 | -13.23821 | -51.42569 | 2026-08-23 11:55:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| db195d93-a45c-3898-8115-a74743826706 | -15.00493 | -52.69359 | 2026-08-23 11:55:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1a7ab2e0-3507-3d3d-986c-d9a083c9e2fc | -15.58694 | -49.30585 | 2026-08-23 11:55:00 | TERRA_M-M | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 030d3a34-0924-3306-a697-6c0df399c648 | -19.64274 | -46.05147 | 2026-08-23 11:57:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 33.1 |
| acfd8a7f-3803-3c3c-95c2-4b742ab0ec3a | -19.02598 | -47.05796 | 2026-08-23 11:57:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8cfcee1c-3eee-3402-b25f-bc9fc687bd73 | -17.54612 | -45.33833 | 2026-08-23 11:57:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 37147d59-7eb0-367d-b744-e20af18fd589 | -23.10191 | -52.13595 | 2026-08-23 11:57:00 | TERRA_M-M | UNIFLOR | PARANÁ | Brasil | 4128302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| f3cd7854-f826-316c-9b56-d9fc67688908 | -16.39756 | -51.32941 | 2026-08-23 11:57:00 | TERRA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 727d68ef-ee47-3905-bf29-3eee7955c59e | -19.02246 | -47.05106 | 2026-08-23 11:57:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 407a4ad8-1c3e-36de-bebb-a6afa39eac4a | -18.54118 | -47.15366 | 2026-08-23 11:57:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e37c7d36-ef41-37f9-8ad3-125f4b4ea708 | -15.55804 | -56.31015 | 2026-08-23 11:57:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a759175d-6bfc-3a8e-8a7b-2ddf2bddab22 | -16.57551 | -51.63121 | 2026-08-23 11:57:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 9acd2b24-6e86-3ef1-94f2-238bac8ce407 | -16.39622 | -51.33864 | 2026-08-23 11:57:00 | TERRA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3d1ce5a6-7374-396a-ac84-49c812a91931 | -18.54618 | -47.1599 | 2026-08-23 11:57:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0014861b-fe26-3834-910c-1e5cc34b1e85 | -16.92898 | -48.76498 | 2026-08-23 11:57:00 | TERRA_M-M | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7194542d-a5e3-3883-9e79-a245d3f31025 | -16.40563 | -51.84133 | 2026-08-23 11:57:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d189f567-a5ae-32e8-9468-2787604e76c3 | -17.22197 | -45.86813 | 2026-08-23 11:57:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| be8c340a-711f-3339-9852-43d1965a4ef4 | -19.02074 | -47.06511 | 2026-08-23 11:57:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 79ac30a3-86c1-3198-a559-13fc46a82b6a | -18.53957 | -47.16675 | 2026-08-23 11:57:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 0fdc43b5-9245-30cd-9ffb-72100044832b | -23.10327 | -52.12637 | 2026-08-23 11:57:00 | TERRA_M-M | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 85f744ce-7547-3c7e-9bfc-dde68bc0adb3 | -17.22385 | -45.85232 | 2026-08-23 11:57:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1e4ee280-ce99-3a2e-afa2-02df78e408bc | -16.57688 | -51.62192 | 2026-08-23 11:57:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| eb7e9921-ae22-30df-96cd-7dc68ff438ae | -19.02436 | -47.07189 | 2026-08-23 11:57:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b64db4a3-07ca-3b72-9a6a-77282fc8ead8 | -19.6544 | -46.05281 | 2026-08-23 11:57:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| cf14bd3b-b7fe-37fe-ba20-98240b385dee | -11.5804 | -46.9369 | 2026-08-23 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| b6e23f00-9864-308b-ba07-98e3adc29e66 | -8.8174 | -46.615 | 2026-08-23 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| d80dfb7a-77e6-3c09-b9cd-d2f46d8f0adf | -8.8171 | -46.6374 | 2026-08-23 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 16018a26-cec6-3b83-ba25-3d59bb595084 | -11.5804 | -46.9369 | 2026-08-23 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 409a611d-b825-338a-b784-170b8885feef | -10.5217 | -50.4489 | 2026-08-23 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a3f48f84-8447-394b-aaa5-fd7d9280d8ce | -13.1505 | -51.4281 | 2026-08-23 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9d17f3e2-c264-3a2d-b913-d7079853df1f | -5.9628 | -51.9579 | 2026-08-23 12:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a97c2796-49e0-30c3-8d4b-6e19ec01b912 | -10.5217 | -50.4489 | 2026-08-23 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 82559392-1d64-3d6f-a0c5-c3d19db46586 | -8.8174 | -46.615 | 2026-08-23 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| b229f1b1-e7bf-3055-9c8b-64ffd19cc69b | -14.5659 | -53.0292 | 2026-08-23 12:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 291afdb1-dc13-35ce-b8b1-081547beb633 | -11.2746 | -50.7524 | 2026-08-23 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 73caea3d-c034-3475-9167-fdb0dd9e4191 | -12.2806 | -43.1813 | 2026-08-23 12:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 117.9 |
| ce603879-1026-3981-8a43-e13bb2f8a477 | -6.1285 | -57.8393 | 2026-08-23 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 6c7f2b70-4263-3a20-9841-a93c363f9a38 | -5.9628 | -51.9579 | 2026-08-23 12:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 661ae8c7-2998-3291-9588-ecf0d2bc8eb1 | -8.8171 | -46.6374 | 2026-08-23 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c7e79c95-e238-3f12-bb68-6719db4a2902 | -6.9699 | -59.0658 | 2026-08-23 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 271626e5-e3ae-3e0d-8cb1-d7850672fb6a | -11.5804 | -46.9369 | 2026-08-23 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 5ef00e76-9493-3a5c-9416-42ad46aa7de0 | -10.5217 | -50.4489 | 2026-08-23 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9300856d-f122-3d69-b552-61ae810f9b71 | -11.2746 | -50.7524 | 2026-08-23 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| f2033b44-7df8-3bdb-a4b2-15f86b0fd9be | -14.5659 | -53.0292 | 2026-08-23 12:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 25f2b708-14b3-3ff0-809b-f4edebb4eacd | -13.1694 | -51.4471 | 2026-08-23 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 19856aee-fa0e-3b1c-901e-79312b170477 | -11.2749 | -50.731 | 2026-08-23 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1e740454-1fee-38d5-b758-f3f563654d54 | -14.5852 | -53.0268 | 2026-08-23 12:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| ad553961-714b-3eca-9e90-445db186572f | -11.5804 | -46.9369 | 2026-08-23 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 2f38faa7-91ae-3c34-813a-d6f1851de1d0 | -12.2806 | -43.1813 | 2026-08-23 12:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 93041e89-5c86-36ad-bcf0-08cf35395917 | -11.9872 | -45.5187 | 2026-08-23 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 618b4945-3440-35a4-997f-e8221af67dc9 | -13.1886 | -51.4447 | 2026-08-23 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 62cf11e9-2e3f-30cd-a0c9-f69d746648b4 | -11.9872 | -45.5187 | 2026-08-23 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b5bd5b5a-7625-3fdf-b08c-19c196e5e8a2 | -13.1886 | -51.4447 | 2026-08-23 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3c2865a7-60be-3d90-9766-c29e06a172cf | -14.5659 | -53.0292 | 2026-08-23 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8f83f4eb-3890-3d97-b855-5ac25193928c | -13.1694 | -51.4471 | 2026-08-23 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7ba6e042-ca42-35f9-bdeb-9fe5a6009462 | -10.804 | -50.5473 | 2026-08-23 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f6814a52-ac60-396a-a441-9d3fe041f40a | -14.5852 | -53.0268 | 2026-08-23 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| aab183e4-4e41-3eab-9cdb-2029017d733f | -12.2806 | -43.1813 | 2026-08-23 12:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 145.3 |
| d9e91518-9489-3b9c-9715-451e43c0ad20 | -7.9868 | -45.2573 | 2026-08-23 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9b1f00e2-4138-3677-a3c1-6d298c600941 | -11.5804 | -46.9369 | 2026-08-23 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 014b538d-2e11-36e7-bcf1-d5d166c96231 | -10.8358 | -50.9903 | 2026-08-23 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8a0fdbdf-404b-3a6f-ae86-949f58f09392 | -6.1285 | -57.8393 | 2026-08-23 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 0953555a-e69b-366c-9efe-b16afdd2b958 | -11.58 | -46.9594 | 2026-08-23 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c0bfd42a-9678-3443-9914-6f4a686de183 | -14.5659 | -53.0292 | 2026-08-23 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d064ebde-16a5-3b97-aa2f-0cd2ee9f0d0d | -7.0193 | -48.0106 | 2026-08-23 12:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 12d7f60f-2ae7-3c74-a8bf-73467d91d25a | -16.0509 | -50.4363 | 2026-08-23 12:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2b47cca1-bef9-3d66-917f-29e50763b0ce | -12.281 | -43.1574 | 2026-08-23 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 4c7589e0-edbb-35a6-a419-558f207a7e53 | -14.5852 | -53.0268 | 2026-08-23 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2e0a8837-f15a-3bf1-825c-b29eb7d1e2cd | -11.5995 | -46.9344 | 2026-08-23 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 98219ae8-680d-3291-8cae-ca1b3f6d52e1 | -16.0706 | -50.4332 | 2026-08-23 12:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3e6aaa5e-8692-39b7-b00e-1299614a4d02 | -15.5368 | -53.9763 | 2026-08-23 12:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 2f386af1-73e5-34cd-9a53-252afae98fbf | -13.1505 | -51.4281 | 2026-08-23 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 102509f3-b3d8-37c0-889d-2fbd71929612 | -12.2999 | -43.1781 | 2026-08-23 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 217.4 |
| 68c0af4e-5278-364f-9ce0-e2e37a2e9c7f | -11.5804 | -46.9369 | 2026-08-23 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| f908a8c1-8bc0-3600-8688-1c128368b820 | -12.2806 | -43.1813 | 2026-08-23 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 242.2 |
| b011147c-79e4-3fc0-8464-d912bc0cf5a9 | -7.9654 | -43.9274 | 2026-08-23 12:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |


[Clique aqui para ver as próximas entradas](README74.md)
