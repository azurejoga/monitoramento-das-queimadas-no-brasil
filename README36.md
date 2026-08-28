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
| 390a7df3-f352-3ac1-8bcf-8269a9560068 | -11.2077 | -53.99358 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ada7051-cf8b-359a-9eb4-0c2a2e32dcfa | -9.61304 | -55.1152 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5f527675-e9ca-3d3a-b36e-32802b650ea3 | -10.91769 | -50.53619 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae1223f9-20df-3e1c-adc3-4139b6062efb | -15.60119 | -46.57689 | 2026-08-28 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95a78242-858b-3026-8dfa-dbac7039760c | -10.06111 | -46.93845 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06d7241a-f743-390b-b9fa-9dff9416f572 | -10.50386 | -64.50382 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 17ffa7c9-0179-389e-bfb4-d152e8c301ef | -14.49277 | -53.4061 | 2026-08-28 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd651218-6c6f-37ed-a194-aafefee042d1 | -10.50006 | -64.50869 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 1afc6b37-23d2-39a7-9b57-4abde333c2a4 | -11.72245 | -54.54533 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2532ab8-886e-3539-a2b8-1c6f61a2c603 | -14.86193 | -52.61259 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a67381e9-977a-3959-9617-ecdb71ad2add | -11.21462 | -53.9927 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55555f9a-c740-30d6-a282-588a66e59cd3 | -8.60047 | -54.78106 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56a251bf-8e8e-35f5-acf0-b0f29c481c62 | -8.94969 | -50.18345 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1bacc47-b22b-3f39-85e9-279518249652 | -14.97044 | -52.58943 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1faaf5d9-1538-358e-afb2-4f78b46f7225 | -13.40433 | -51.81139 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71e34c2b-f135-39da-bde4-6477b519d7fe | -7.69681 | -55.36582 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da1e78b4-cae4-3d2c-955e-066f343bf1ec | -11.72927 | -54.52795 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a74e84f9-cc10-3501-96d0-53aed8076654 | -11.62237 | -54.58581 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 2c723d7d-6e99-369d-b9c2-1d4e23c0e3e0 | -11.61615 | -46.73568 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c50e454-66f8-38ff-8e43-3c16d02eaf5e | -8.01736 | -48.01509 | 2026-08-28 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c56d1985-3844-37b2-88a3-780be27034f0 | -11.83073 | -47.21733 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ede40ba-17b2-3c67-a758-d76e097380f2 | -10.93057 | -50.53447 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5dc16e28-ddc3-30a5-b540-80f8f705c559 | -8.94712 | -62.39434 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 207867a9-9623-3df6-9153-cd77261c6bd1 | -11.23501 | -54.00517 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3be28fc0-b8e1-3a08-84b3-ba0f824bd2e6 | -11.33956 | -48.38309 | 2026-08-28 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d68de56f-e9fb-3453-934d-97e0f8eaedbe | -8.59289 | -54.76213 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f838037e-8599-36c1-919d-964d97daa46c | -10.78963 | -50.63803 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30c5c20b-0958-37b9-961c-e8b99f5ada4f | -10.93389 | -50.535 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 21923973-44e4-3c5a-bcd4-0b0ba5aad809 | -10.88613 | -50.52027 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc3ff0d4-712f-34ab-866d-2c739d4131f3 | -12.50243 | -43.80607 | 2026-08-28 04:51:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df28297c-cfea-3bdb-9fed-6c1230a3830c | -10.5538 | -50.41598 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af4475cf-a078-32ef-b475-49696546625a | -14.59736 | -53.15836 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5c174c9-4b30-332e-be5d-4cb988de4fd1 | -14.33126 | -51.70579 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d69caa9-79ab-3ccc-acd9-37fa051ea1eb | -13.8345 | -54.04633 | 2026-08-28 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7ba9fa5-dcf1-39d5-8e0d-7c38beac7042 | -12.28495 | -50.59462 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1174dc4a-63c2-3ed7-9b8a-38c77a8ed08f | -9.16023 | -49.96648 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c76204e5-b1ff-343e-8300-37ddf6b32216 | -11.01204 | -49.65309 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 491ab12c-db17-37b6-bf75-2f639428e612 | -10.89278 | -50.52135 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd5bd52c-641e-30e8-8351-4e87af3527f2 | -10.32967 | -46.74868 | 2026-08-28 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1bcf0fb-b78c-3b72-be2c-834d8770c20b | -8.98822 | -52.38863 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66409c37-f258-3a9d-a30e-60eb78014e7e | -9.43442 | -51.57744 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9042baac-86ae-30a3-ab91-b9c31492038a | -12.01873 | -47.17282 | 2026-08-28 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7df1714e-861f-3586-a5be-a01d9e83647a | -8.56026 | -54.71468 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9c998b6-8ffb-3557-bdec-9b69be9721e3 | -8.7683 | -50.4909 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e090b40-b65d-3561-a71a-8741ad184cfd | -9.45708 | -51.71885 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b8ae2dd-feeb-36d0-970e-cd31172c6c61 | -11.28608 | -54.03629 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a5ecf6e-2ee9-3b0b-931b-3de17bca9db6 | -14.91038 | -43.41508 | 2026-08-28 04:51:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ccc71e8b-8dbc-34f5-bef5-c3b48a426678 | -13.40269 | -51.41646 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f9737bf-aeaf-33d7-a22c-cae4d2142f4a | -9.61609 | -55.12112 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 069487d1-9404-3510-8e45-e42341c0e5ae | -11.76137 | -54.51974 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fb7d7fb-3170-328a-b497-8b670fbce1da | -11.57426 | -45.52523 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deb5f3d6-7779-30a9-842d-74c619041d9b | -10.7593 | -53.97075 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a1b5a51-4d98-391e-920d-1a1b32c5687e | -11.38089 | -45.14343 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f91b04f0-4726-38f7-b453-bf9b4a81b422 | -9.98997 | -48.58985 | 2026-08-28 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 59a9fc68-2932-3780-8921-05210455ea56 | -11.81659 | -47.21062 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 108b55b8-99a3-3282-bec7-b423a76511e6 | -10.76224 | -53.97568 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7164809e-ac9a-3519-8875-31080a704dcf | -15.53172 | -41.92319 | 2026-08-28 04:51:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 5c573a20-ed9a-3a3a-b199-50f16dc36a41 | -11.47504 | -46.9419 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d1f7c91-2aa2-3c48-9a9b-8c4c3eedee1e | -11.74648 | -54.51707 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de8061e0-1c64-3488-a4c9-96adedf6a008 | -11.21388 | -53.99699 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0e0f665-cf9b-3811-b530-5d68f1a14240 | -8.21574 | -54.95522 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0b5cffd-2321-38a1-8ba9-7c8486926aa7 | -14.42266 | -52.60577 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09502cee-cdad-326f-9e9a-47fca059b792 | -8.0323 | -51.81842 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 466ae167-9cb2-3ccd-b5ef-fecee57b1db7 | -14.86073 | -52.61993 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4f35916-b6e5-3225-9cf4-bcd8b0d3948c | -14.85977 | -52.60468 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e5831be-1f03-3ba4-9717-f9d42559ae5f | -11.72991 | -54.54667 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7085a74c-7ad5-3ef5-a738-38a608941f35 | -13.41047 | -51.41047 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1f49d7b2-4ec5-3b40-a07e-4865946c3e38 | -8.9461 | -62.39973 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 114bf5ee-fe2e-3fb9-943b-0ec1fd6df160 | -14.45392 | -53.3481 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b3ebc13-090f-39e3-ad79-4a04555915f3 | -10.88825 | -46.63493 | 2026-08-28 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08905790-af06-3c10-af6d-49d5ce10f62d | -10.8961 | -50.52189 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 76841b86-6f1c-3b9c-84c0-aa8fc6e2b24f | -13.61149 | -45.78455 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ee263ec-8003-3478-bd98-45f2ea29a7f0 | -8.2232 | -54.96013 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26ff3521-70bf-31ac-aecf-819bf6a3e370 | -11.89618 | -44.86338 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abb5282e-343c-38c2-a750-5b832f741874 | -9.4543 | -51.71458 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34977c03-d009-3edd-8a9d-c385ced16c5c | -10.75711 | -53.98374 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6182fc8d-1634-3e7a-bd5d-e20f90e0c698 | -11.80984 | -47.20509 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a7c5d184-3327-3a5b-834a-d80d273dcddb | -9.05732 | -45.78046 | 2026-08-28 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63ebb1d3-5880-3481-9cb8-737450f2bf42 | -7.4944 | -55.28521 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7a296d8-a216-39dc-a670-bead4e0bd237 | -9.2219 | -51.57306 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbac265f-5656-3e52-bcc9-a6d96752347d | -8.59344 | -54.7832 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72f76ab6-17fc-3122-85c0-6be39b239233 | -9.44473 | -51.7093 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13629b58-2259-327e-916d-29ed0649e1b7 | -13.40658 | -51.41347 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 01b86a30-d1e7-342c-b210-7d3c6ff6d41d | -15.60051 | -46.58122 | 2026-08-28 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2d973c5c-35db-3168-a4eb-8b8f62e41fc9 | -10.50238 | -64.5108 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 01e176e0-0b74-37ce-b276-3b51eda03035 | -12.28772 | -50.59869 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e80fe8ec-2556-3651-9529-5caf67b58bf5 | -12.27941 | -50.58646 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e7dcd34-cf67-3841-af77-4798b4f977a9 | -12.61637 | -47.89006 | 2026-08-28 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09c85c95-b97d-3265-87e9-a0762d458aae | -6.83615 | -55.61404 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acdc4133-d766-3476-afea-2505f466175b | -10.92392 | -50.53339 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a49f24d-8f23-306a-bac2-424cbe0ff2f5 | -13.46975 | -57.04772 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01548b81-b99c-3049-9fca-419dcbced299 | -14.9799 | -52.59484 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6d84f7b-0367-38a3-b8bf-03bb511c90e6 | -8.56207 | -54.90722 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7dccd2-2f1a-37ee-8cf2-c46249cd2d1e | -8.59344 | -54.77462 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9da7efe3-2143-3405-97e9-69dc260c2ce9 | -6.83543 | -55.61815 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15500782-36a3-33f9-9c5d-9516f819103c | -11.78197 | -47.6466 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ddf418df-de33-3e85-9a1a-e9e73b4e7814 | -11.21428 | -53.99915 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47178c2a-7e59-3237-b6d8-185e566b0479 | -14.153 | -52.82157 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8126b5e-47e8-392e-a264-ea4e3ff0033f | -10.78795 | -54.00244 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eed42030-d95a-367e-b78f-fc81f5e11557 | -9.66703 | -55.08735 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
