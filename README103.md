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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cde010d-693f-3370-b58a-3d3057bf3acc | -12.24673 | -47.82785 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd9eb944-3641-3267-8a0a-3bef8a910a28 | -16.01709 | -50.86893 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55f35612-ec09-3235-8dd0-e9a5b016262e | -15.23946 | -48.72767 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85cd2d12-0550-3039-ae28-1c5c8fb88aa7 | -14.86772 | -48.29855 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b28b9d8-9bb6-3ae4-b90b-e37185f432a9 | -13.53696 | -47.26862 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1953161-877b-35cc-bd4e-8637b28b14a9 | -13.06921 | -47.02139 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 168db481-7408-3573-a32b-5e314c5bb765 | -13.22203 | -48.43662 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f74511a-f710-3d7c-9fcc-38b8daa9ba9c | -14.31245 | -45.99267 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1b927a2-4a65-301f-ae02-24ea6b285189 | -15.19607 | -48.16565 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17902774-c736-32c1-b5f8-875e35d8f5e1 | -22.56617 | -46.7777 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8a26cd07-65e4-376b-ad18-2091c3199328 | -21.79055 | -47.20578 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9dfd005a-4bc8-389e-93c0-55ef1f7341e3 | -20.18936 | -46.01486 | 2025-10-02 04:34:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fcac4f2f-1e5f-3745-8c3b-5324473b1baa | -20.84533 | -49.47839 | 2025-10-02 04:34:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a795f0e9-8b41-3c46-9494-cccd8908bcc1 | -20.84287 | -49.42846 | 2025-10-02 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| f38c64dc-8018-3357-bdbc-e0402cd2f6d5 | -22.98251 | -48.34708 | 2025-10-02 04:34:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d01320cb-1fd4-331d-8583-c87bd36aa1b9 | -20.84866 | -49.47898 | 2025-10-02 04:34:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 35ebfcf9-b7be-3ff6-b14c-f1b3604c5bca | -20.13727 | -46.34333 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 804e3224-40cf-3dc0-bd09-a4c7cf4a002c | -20.18448 | -46.02325 | 2025-10-02 04:34:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96662c22-e91e-3d8b-a68a-5df978d7075f | -21.78819 | -47.19686 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 46723443-2e5b-3734-b9cf-cb30e093fad7 | -21.94228 | -43.43931 | 2025-10-02 04:34:00 | NPP-375D | BELMIRO BRAGA | MINAS GERAIS | Brasil | 3106101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7a887a65-166e-3cc5-bc12-3dc13b475b46 | -22.56133 | -46.78611 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c807df3f-947a-32f1-a562-7a2bc97f931f | -21.56245 | -45.27379 | 2025-10-02 04:34:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 20a66234-5c59-30ad-9153-dd20bd43cd21 | -20.84591 | -49.47469 | 2025-10-02 04:34:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2aca246a-fb05-31da-bbb9-8a5d25907825 | -20.23165 | -43.9077 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 85e530b6-d4b4-3937-af86-4fba1b5395fd | -20.84563 | -49.43276 | 2025-10-02 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| fbee9d5d-abad-3bb7-9234-284f24ec3928 | -22.62146 | -44.5042 | 2025-10-02 04:34:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8dde61df-5ac8-3149-b883-c3b688ac7df5 | -21.57515 | -44.96217 | 2025-10-02 04:34:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1e8dbc1c-d34d-3c6a-aeb7-863c47743d46 | -23.05075 | -47.05876 | 2025-10-02 04:34:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5da88ce4-d45b-3fec-9988-459899800363 | -21.66265 | -48.79805 | 2025-10-02 04:34:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b059294b-9526-3243-95e9-fa8e362591fa | -20.21584 | -44.18405 | 2025-10-02 04:34:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e079d132-9daf-315a-99e9-dacfa0f83e5b | -22.28484 | -46.71786 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 40d4fe59-96b9-3f18-bddf-bfcfe76e7b10 | -22.27819 | -46.73935 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 0ab4bef1-8ea9-3a9b-91dd-e5b9d74ab5e9 | -20.49379 | -46.12679 | 2025-10-02 04:34:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce12486e-7a0a-3874-8d61-d5b2804e43c5 | -22.08444 | -43.08865 | 2025-10-02 04:34:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c147d6a4-79ab-31e8-8a5b-f0591b78cd1f | -20.11706 | -44.38208 | 2025-10-02 04:34:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 387d6f24-11cf-3076-bab0-fa030fd48fad | -21.79468 | -47.20217 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e33ab509-13c6-37bf-9d2f-caa4315d3c9a | -22.28 | -46.72614 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c325d0a0-50bf-33ba-a0b3-10157d7e714a | -20.24292 | -43.88563 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ea3e3781-7b2e-3e14-bd16-6da35dca50bb | -22.57343 | -46.77896 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| a859d6e7-e309-318f-a9c1-001b4a3bb982 | -22.2558 | -46.71306 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64398d55-fbd5-3224-8262-3529f27a8b74 | -19.67939 | -49.24023 | 2025-10-02 04:34:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eb1275f-85c2-3fe8-bee1-d8d8d8add5d7 | -23.31448 | -45.90638 | 2025-10-02 04:34:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6435000-5fa4-3019-80fa-1155a61b6921 | -22.56496 | -46.78672 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3808ee49-42e4-3970-aced-8e3920279d24 | -20.13264 | -46.34882 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70c37bde-c3f0-3201-93c3-dba338e181bf | -21.11814 | -43.76503 | 2025-10-02 04:34:00 | NPP-375D | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 03b5cd94-551f-3e9c-9c9e-41356b6e7097 | -21.11678 | -43.76711 | 2025-10-02 04:34:00 | NPP-375D | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3ce77092-77b9-367b-b2ae-d7b9edca2d37 | -21.31744 | -46.84641 | 2025-10-02 04:34:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 88520f9c-e8c2-37d2-a70c-44fb7a2f2db5 | -20.8806 | -43.20374 | 2025-10-02 04:34:00 | NPP-375D | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ea6bde4-b08d-3d50-b22e-5fa34c965767 | -22.62198 | -44.50001 | 2025-10-02 04:34:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b7b219d7-13d8-31a2-9f20-ae3dfd07ba78 | -21.66717 | -48.79105 | 2025-10-02 04:34:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a74c400-d66c-3fa1-abcb-99d3312a7d4c | -20.2275 | -43.90706 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e808f1e8-020c-3e3e-a8cd-b4e97090b521 | -19.31194 | -50.05708 | 2025-10-02 04:34:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b674a90e-3ca5-3687-81ff-ae95bf204575 | -20.4933 | -46.12443 | 2025-10-02 04:34:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a957e3b-1aac-3614-874b-87a2bf41f7a5 | -22.27517 | -46.73431 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8b53a4de-6db9-3c04-a907-a19487c93ca6 | -23.05003 | -47.06083 | 2025-10-02 04:34:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ba546f09-58f2-31f5-b44b-81bbc4693f86 | -20.42201 | -48.86472 | 2025-10-02 04:34:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36dbfdb6-d5b3-3d7e-b3de-2b7008def3fd | -22.24133 | -43.42413 | 2025-10-02 04:34:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bdf33c81-0ce3-3c84-ac60-c8edc3930bb1 | -20.13245 | -46.3516 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71a686d0-0158-3a9d-8a7f-e1ecd00f6d4a | -22.57282 | -46.78345 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 94751eb9-ea9a-3f91-86ec-58ee5769dcb2 | -20.28394 | -49.23759 | 2025-10-02 04:34:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15a8ee0b-70dd-3651-a387-0a52862f5c94 | -20.83954 | -49.42788 | 2025-10-02 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 91a684ae-3dff-3748-96f2-70c9fb5b2861 | -21.57588 | -44.95653 | 2025-10-02 04:34:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a9ec48bc-73a9-349c-b59f-4b47225db47b | -23.31627 | -45.90809 | 2025-10-02 04:34:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c1473ab8-73ad-398e-ac9a-6bae080bdfce | -22.60302 | -49.02896 | 2025-10-02 04:34:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b1c2296-7edb-3fff-8f14-c71635bb4f0e | -20.18876 | -46.01931 | 2025-10-02 04:34:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d1707f20-fb21-3fc2-a097-133cf82e7af9 | -22.67997 | -47.64513 | 2025-10-02 04:34:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e8bb6752-83eb-3e91-8caf-e41b25b0d8fe | -20.22799 | -43.90326 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 96f408f8-1f96-36ae-a8c2-396d0f19d1bc | -19.58354 | -49.45732 | 2025-10-02 04:34:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 733f9241-72fa-382e-8af9-d038df04c9e1 | -20.8771 | -46.46112 | 2025-10-02 04:34:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3bb4f60-8a2d-350c-a874-ff4ffdb8baf3 | -20.62047 | -46.22508 | 2025-10-02 04:34:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2caea502-96a6-35d2-91ef-450e8c5151d2 | -20.35666 | -48.78924 | 2025-10-02 04:34:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85cd83a3-5842-3d13-bd54-8c58a8d5411b | -20.80727 | -46.32275 | 2025-10-02 04:34:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 006f68f1-3d20-3c51-a6f8-6b6a746e69b0 | -20.22437 | -43.89852 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1c071764-fa49-340a-b240-5bd50ae963ed | -22.62047 | -44.51205 | 2025-10-02 04:34:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 78014532-e483-320b-b4ee-5613b4764844 | -20.42258 | -48.861 | 2025-10-02 04:34:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb237698-fc0d-39f9-8099-94a054274713 | -20.22338 | -43.90634 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 33d29a06-96ce-39e9-922f-e00abbdfc3aa | -20.13305 | -46.34721 | 2025-10-02 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1850f7e9-c22a-36fa-9d99-58deabcad2d0 | -20.35225 | -48.00798 | 2025-10-02 04:34:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 193593a4-da60-3e44-8ab3-44462d32a459 | -21.66659 | -48.79483 | 2025-10-02 04:34:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 92835553-761d-35e3-8052-e34cc48d26e5 | -21.68573 | -45.60916 | 2025-10-02 04:34:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 52c8313f-5a98-3251-a4e6-919cf10fda1d | -21.7876 | -47.20105 | 2025-10-02 04:34:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 26eac6bd-2261-30b5-8abb-e889dc6c33e6 | -20.87738 | -46.46351 | 2025-10-02 04:34:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92e4b670-966a-3521-8390-617629d4e8d3 | -20.18641 | -46.0209 | 2025-10-02 04:34:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 146fbcfa-f5bf-3c08-bf69-ed33dd651417 | -23.06888 | -46.70908 | 2025-10-02 04:34:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 320d4924-7fcd-394e-a625-413b7e078bf7 | -22.69753 | -46.2481 | 2025-10-02 04:34:00 | NPP-375D | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a1889f2-c450-3517-af9c-36e5d24ac6a3 | -20.49011 | -43.93162 | 2025-10-02 04:34:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2b27d38f-8cbf-3b52-b048-1eb75a99c176 | -21.63459 | -44.89029 | 2025-10-02 04:34:00 | NPP-375D | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 167891ff-ced1-3739-ae1b-7f6bc997a62e | -22.56557 | -46.78221 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a94710d9-920c-3216-ab7e-02191bc1c7bd | -20.07914 | -44.19322 | 2025-10-02 04:34:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 62758a75-d260-3831-9e9e-9aecd618bbb1 | -20.1254 | -44.01743 | 2025-10-02 04:34:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27148924-7d26-3ed1-b308-ca5ea103a93a | -22.57705 | -46.77963 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87743955-ca45-3651-8cea-4da13fcb22fd | -20.62103 | -46.22099 | 2025-10-02 04:34:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38eeff0b-9be0-342a-b280-212c39c3d413 | -21.73726 | -50.31071 | 2025-10-02 04:34:00 | NPP-375D | QUEIROZ | SÃO PAULO | Brasil | 3541802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 85c43752-712b-3437-9b38-0d303813ef12 | -22.56072 | -46.79058 | 2025-10-02 04:34:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ec378f3c-9418-32b1-999a-40267baeff2a | -20.73193 | -46.03159 | 2025-10-02 04:34:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| feb34235-dc16-30d2-9c7d-5585eae4e1fe | -20.22024 | -43.89782 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 099f3525-6e25-3f4e-aa65-7a5d6f4008c8 | -22.68056 | -47.64096 | 2025-10-02 04:34:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3c901700-52ba-3467-8705-5ab56d6f57a5 | -20.87287 | -46.46487 | 2025-10-02 04:34:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb8443f0-dded-3ec6-854c-35d623292b6e | -22.25942 | -46.71376 | 2025-10-02 04:34:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 11c9015e-9912-3173-9449-6a3b53883584 | -20.23213 | -43.90391 | 2025-10-02 04:34:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README104.md)
