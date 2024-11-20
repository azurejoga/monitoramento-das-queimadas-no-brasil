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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 791c7fac-c5fa-346b-a4df-73055d9ebe36 | -10.76693 | -44.82186 | 2024-11-20 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcdd5f39-4adf-3378-8d50-aaae82285a46 | -12.27382 | -43.52818 | 2024-11-20 04:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72e41ee9-bb94-3bba-9267-e6d17ad934b8 | -11.58945 | -42.97373 | 2024-11-20 04:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa588e00-e2ef-3d4f-ac2d-a685ffc0be61 | -12.93892 | -57.01654 | 2024-11-20 04:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f72e28dc-9edf-3b9a-a53d-bae553e12914 | -11.49486 | -54.2826 | 2024-11-20 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b8903a4-a239-3514-9267-d27cf0fd2588 | -12.1234 | -54.28694 | 2024-11-20 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 312d90a0-f6bc-33f6-81df-1ff1498bfe9f | -9.19332 | -44.72729 | 2024-11-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e160086b-99d9-376d-8387-2fe40147acd7 | -11.03876 | -44.5732 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 3cab7063-d42e-39e5-93b6-cb470bac5635 | -11.42919 | -44.6884 | 2024-11-20 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d3bb1f-1fda-3e62-a650-e4058eeda91d | -11.11324 | -54.63399 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63920b08-a689-3c6c-82ef-0af7a6983654 | -10.76776 | -44.82487 | 2024-11-20 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86152868-0528-39c8-a734-5b7a17f992e9 | -10.39258 | -44.47337 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f77806d-99cf-3a9a-8396-3ff0db6416e6 | -12.12616 | -54.29103 | 2024-11-20 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe2b54f-53a5-33b7-aabe-642e8f11928a | -11.51138 | -51.61207 | 2024-11-20 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5d7e104-e1c6-31ac-8e76-d2fa3c110156 | -10.42752 | -44.887 | 2024-11-20 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b342b999-9473-3b26-8e4a-59e2744d5522 | -12.03581 | -54.64902 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f32d2bd9-61dd-3100-885d-bb707168cac8 | -10.39138 | -44.47615 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 292f6ded-bcf6-32b3-ba47-49417fedce02 | -17.59832 | -57.56432 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a9039edf-2ff8-3575-9b68-75fcb370589e | -10.44644 | -44.88394 | 2024-11-20 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 948960d8-1e71-336f-9f66-4154dcdd8560 | -17.62201 | -57.59673 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b1e7e488-1c32-314a-97ee-dc9e6bc30de2 | -10.84606 | -44.90768 | 2024-11-20 04:53:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c0df18e-9454-33ba-adad-cb1fb18082dc | -9.19293 | -44.73027 | 2024-11-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d3362a7-6a4b-3fa7-aa3d-0636dbef7a3d | -17.61007 | -57.38842 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 74060cb0-4974-35fe-b110-c6e24f074ee1 | -10.40269 | -44.4712 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abd6a6e8-89da-3c22-90c8-c971553abe7a | -17.62971 | -57.59397 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 415ff0bc-69fe-3702-bddb-2323374c587e | -12.12673 | -54.28748 | 2024-11-20 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7e45ad2-c24a-3194-b076-94b88cbe710d | -18.96348 | -55.5944 | 2024-11-20 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cff68633-d12c-3d36-ae7a-1af4bad86cab | -9.79522 | -44.71508 | 2024-11-20 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5f0ab6e-1948-32f0-8427-d5611a58533e | -11.10653 | -54.63287 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f09a99eb-1158-39ad-98a9-65c62de4e1e8 | -10.44604 | -44.88701 | 2024-11-20 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d8b55f4-c108-3917-abac-6002f41e76ff | -17.6025 | -57.56092 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 017e6e5e-0591-3871-82c1-9dd340a2578d | -12.08279 | -54.5832 | 2024-11-20 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de3f5246-b6dd-3495-9fc2-c93846d4e356 | -21.22419 | -56.35596 | 2024-11-20 04:53:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8461bc47-0cfc-3f3d-92c2-38077e41b30e | -12.03668 | -54.65632 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5074997-0f67-3a8d-9944-3f7d4a1597de | -11.09645 | -54.63122 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 569d74c7-f1ee-388f-a0d6-2f15802b74fb | -10.92501 | -44.88144 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d25042e-3efe-3b8c-9a30-489c6775cf4e | -16.74287 | -45.76526 | 2024-11-20 04:53:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad2f08e3-01ce-386b-ac4d-6541cff3ee95 | -10.76814 | -44.82185 | 2024-11-20 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d07b1734-e06b-3865-8eee-ec12dcf229df | -11.11046 | -54.62983 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 59aa0b95-73b2-3ef9-a3d6-edc2586b6696 | -16.19693 | -55.95884 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e44dce5e-aeec-3098-adf3-adaecdbe0dee | -16.45113 | -55.98327 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e3300d09-02d2-325b-847b-483995a83094 | -15.30599 | -56.53136 | 2024-11-20 04:55:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4629c98a-a224-3abd-9035-19aa0f528518 | -16.44837 | -55.97899 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d3311f14-4e57-311b-bd19-d13cd3cf8c8c | -15.87274 | -53.26566 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18aab465-a516-3679-9e50-5082bc2a89be | -15.8688 | -53.2688 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cce1f91-e57e-3313-bf6e-a28b155eee24 | -15.29847 | -56.53402 | 2024-11-20 04:55:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 381750b1-95f7-3a7d-9c72-41854d500bd1 | -15.87218 | -53.26936 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32537318-10a7-34a6-9ad2-7d741be9e933 | -15.87838 | -53.27417 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 907f0c94-95b3-39e6-adbd-67e818d4503a | -17.13908 | -57.50042 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 03744dcc-d1f5-366e-835f-05d6cbedc672 | -16.44159 | -52.56023 | 2024-11-20 04:55:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afaab85a-8f53-3875-91cf-524d2d35561b | -17.0619 | -57.48756 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8de93548-9ccf-3176-812d-2a5b6011a780 | -17.13489 | -57.50383 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 44d90bdd-bb1b-37eb-8f4e-225b0dbc9ca8 | -15.30461 | -56.53005 | 2024-11-20 04:55:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2050e56e-37df-3bbc-b67b-780550b601ae | -16.43888 | -55.97352 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c3511065-3d40-3deb-b193-73a2e492c729 | -15.29503 | -56.53342 | 2024-11-20 04:55:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c08b29e2-57de-30f8-8a74-a715188bdbad | -17.13207 | -57.49913 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6d8bcb90-75ed-3008-a930-c7ccf6b5b695 | -23.26006 | -54.93548 | 2024-11-20 04:55:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5f11d4a5-2550-367f-b97d-c85e1fcc03fc | -22.05697 | -56.01368 | 2024-11-20 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e803820-9b34-35ff-8023-a5748feec51f | -17.36269 | -57.43953 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b3e3851b-8d62-3d08-a61e-3cacbb196ac6 | -16.4545 | -55.98386 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cddacd7d-a2ee-384a-abec-d6f8a58689a6 | -23.26064 | -54.93154 | 2024-11-20 04:55:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dde4129a-1ce7-3daf-9f71-7cf5fc0ea525 | -15.29911 | -56.53016 | 2024-11-20 04:55:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de103c1e-a5b5-318f-8564-b8ddbaff0806 | -15.87107 | -53.2767 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c000ba10-13a4-3e38-887f-c2e0cc9d3a02 | -15.87162 | -53.27304 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a458fe85-1974-37cb-9852-2e71cc1b6019 | -16.43948 | -55.96983 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3895f861-f2c0-3350-9e5f-8c1fbe594b32 | -16.89399 | -57.51653 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e7f93418-7369-328b-9737-3f5e7e9626d7 | -17.13696 | -57.49168 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2c08fa14-85f8-3299-91d2-689c56a68fe3 | -16.43827 | -55.97721 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 330e452a-06c8-3888-beb2-f393c32da1e1 | -22.15539 | -54.88916 | 2024-11-20 04:55:00 | NPP-375D | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e3b090f4-1e27-328e-88a3-47f8ef4e28e0 | -15.86936 | -53.2651 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e7262ac-77e9-321f-88fe-4b5ff48b8b20 | -15.87445 | -53.27728 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48f6115e-7e73-3e03-8cb0-c4a56692742e | -17.65633 | -56.4599 | 2024-11-20 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 610aa2bd-d159-3bf2-8d7a-73f0f610cbbd | -16.44164 | -55.97781 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 933851f4-df14-3aeb-8a4f-c4d65c6af2cc | -16.89048 | -57.51588 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 33b4661b-38bf-389f-b4c3-6ec018b26b3f | -17.13627 | -57.49573 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4c6a021d-f05b-38dc-88b3-dc44a77b5f6a | -22.05365 | -56.01308 | 2024-11-20 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71b3f905-be70-39df-9754-7e09c38e6f3f | -15.59173 | -55.55713 | 2024-11-20 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 990fa3eb-0f64-3eb5-b6af-8027e6ddb228 | -16.88766 | -57.51115 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cdd788ba-4e5e-3507-a8ac-f42813086c0f | -15.875 | -53.2736 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16ac3de8-328b-37a5-b079-63608d1232e4 | -17.13558 | -57.49977 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dc58e4d9-92ab-3880-bfab-730ef24b2842 | -22.15259 | -54.88474 | 2024-11-20 04:55:00 | NPP-375D | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dcda4190-59a4-3c8b-be07-219ee119fc68 | -15.30255 | -56.53076 | 2024-11-20 04:55:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc811cff-bda6-3cc2-a3a2-ce4038be4933 | -16.89117 | -57.51181 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ae6fc237-886d-34c0-923d-c9307f36f17c | -17.12857 | -57.49848 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6b2b3161-502b-3e91-8e65-425921a9a73f | -16.89469 | -57.51245 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 90b4218b-f869-3344-b7c1-5b0e0ab6e458 | -16.43811 | -52.55973 | 2024-11-20 04:55:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f07d79c-91d1-3562-8ec1-0da2be6eade2 | -24.24212 | -50.73959 | 2024-11-20 04:55:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cbf2bd1-0043-3927-bf03-f95b107c50b9 | -16.43767 | -55.98091 | 2024-11-20 04:55:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b6fbc72f-50ad-318a-866c-9b9cc1ce0790 | -17.12156 | -57.49719 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 32e91bfb-0e06-3076-81ef-584a94794cdb | -15.87782 | -53.27786 | 2024-11-20 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90726bd0-a73d-36d4-a3f5-b767ed5815b8 | -17.12506 | -57.49783 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3f505c77-d45b-35ca-81a4-ac75a5ab5058 | -17.12083 | -57.48035 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 96141450-1e17-376e-b8ff-944d9f80e30c | -17.13839 | -57.50447 | 2024-11-20 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3580565f-3bdf-33ec-96c3-a8dff9b06a12 | -2.7402 | -49.3502 | 2024-11-20 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 4660b15a-7f31-3c64-8f5f-330dab8a7afc | -2.7501 | -51.8171 | 2024-11-20 05:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 46b85bf2-bd50-3813-b6e3-4fc0ab69375c | -2.7217 | -49.3508 | 2024-11-20 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 87b4dd32-56a1-33e5-98e5-34eb6bf06ac5 | -2.9299 | -53.0805 | 2024-11-20 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f1829368-b4bc-30e7-ae8b-99b799ed40c7 | -1.2017 | -53.6769 | 2024-11-20 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 862a007a-8700-35f0-b1f6-6ffa61e7776d | -4.4405 | -46.5754 | 2024-11-20 05:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c2f8edee-4d78-349f-bcb8-6286358fbd0c | -4.4404 | -46.5975 | 2024-11-20 05:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |


[Clique aqui para ver as próximas entradas](README64.md)
