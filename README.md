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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c13181b9-8b03-3cfd-8dd1-cdba6236dd4b | -12.8896 | -50.991 | 2026-09-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 0aa2a054-5013-3dfd-9ddd-8d220fbd003d | -12.7428 | -46.183 | 2026-09-20 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 59dd8a3d-051a-306e-a419-9520cfd489f2 | -3.6946 | -60.6025 | 2026-09-20 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| db398ff8-08fa-37ab-b419-60723efc9301 | -11.398 | -51.418 | 2026-09-20 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 538c1fd1-fbd7-359a-9c6e-7c8b7108dc1c | -11.2118 | -54.0797 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| b7b39b83-3425-336c-b5a6-997c7ed45681 | -5.8276 | -47.768 | 2026-09-20 00:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 49165161-4bdd-348d-a68e-4170dc5a28ba | -10.872 | -54.0899 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3a5132b1-1e52-367b-9d79-dcc5c38bfa4e | -11.0259 | -48.2944 | 2026-09-20 00:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 15247e07-b889-382b-a99b-16130a8f097a | -9.131 | -45.7273 | 2026-09-20 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e930e20a-21a4-30b3-8b8c-c1fcb977ae57 | -3.6945 | -60.6215 | 2026-09-20 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9ddd3158-cb7d-3218-8df9-299ac08a44f0 | -13.0366 | -46.9322 | 2026-09-20 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1696a106-2dfe-3b78-92e0-1aeb36c75094 | -11.3793 | -51.3989 | 2026-09-20 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 4f509ff3-c289-31e6-a100-f7c692218f42 | -12.8893 | -51.0124 | 2026-09-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 113c40d6-2337-37c7-a8fc-235e3e74df84 | -12.7432 | -46.1601 | 2026-09-20 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6e5388ea-a93b-3107-96a7-2413aa097c6d | -11.1369 | -54.0251 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 4035a3c9-dd7f-3fb4-90dc-603c70cc0b5e | -8.1874 | -54.742 | 2026-09-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 2d134a56-1cb0-3062-83d7-8c3a9e5f4011 | -5.8088 | -47.791 | 2026-09-20 00:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| f326c8c9-ffe7-343d-9362-579fd1ec004d | -12.9088 | -50.9886 | 2026-09-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| bfe2c067-722e-3453-8318-da2d41ca9875 | -11.0991 | -54.0285 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| b9d187c3-a192-32cd-93be-536effa1c467 | -3.3367 | -57.8673 | 2026-09-20 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 43548bf3-b55f-39e9-bbfc-d2d5440cf2c9 | -5.348 | -44.8171 | 2026-09-20 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8330e165-e87a-3f41-86c6-b8c97a2f466c | -8.028 | -61.3435 | 2026-09-20 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4d3f4d3a-3ea9-3b31-9ebe-9ad677bb290c | -7.5522 | -45.435 | 2026-09-20 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b0733683-6368-3974-84b0-720fa76ec9c9 | -11.8547 | -47.6596 | 2026-09-20 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8b306cdf-2305-3cba-ad41-98789f7f1b85 | -8.0279 | -61.3626 | 2026-09-20 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d1252978-f5a2-3d1f-84db-c4104b55fc7a | -11.0989 | -54.049 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c4808edb-56b1-392a-811a-82d747d4241f | -11.8739 | -47.657 | 2026-09-20 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c6f95811-04dc-325c-bc5b-3f999f21dc59 | -2.8791 | -57.8184 | 2026-09-20 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e50706ef-85a5-39cd-a333-bebc9e540014 | -2.8974 | -57.7987 | 2026-09-20 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 3dbadca3-6dce-3df1-ba5f-a7936de851c2 | -11.041 | -54.1567 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 61d2be5f-903c-33a3-b473-d11f6bdd11d2 | -8.0465 | -61.3427 | 2026-09-20 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| dc2c595b-dedc-30a6-8cef-e2d90bcaea6a | -3.3492 | -59.867 | 2026-09-20 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4bb56850-5216-3324-bd09-809dfca7d7db | -5.8274 | -47.7898 | 2026-09-20 00:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 302.2 |
| 11062bd6-7a75-3529-b735-56d0ec7ab2e1 | -12.7625 | -46.1572 | 2026-09-20 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 3488c9ad-15c4-390f-ac39-148c37b75af0 | -8.1686 | -54.7634 | 2026-09-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 9d77fe65-fe44-3421-833a-d26767335646 | -8.1688 | -54.7432 | 2026-09-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| dca71d7d-39e0-351a-b46c-0d95a0c95e86 | -12.8701 | -51.0148 | 2026-09-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 09529e28-7920-3154-8148-eed85d7e8bf3 | -8.7911 | -60.7935 | 2026-09-20 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b2b57934-58bc-3bd0-bff0-f3bf53b6270e | -11.1183 | -54.0062 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1df5fafc-df1e-3247-9b4e-1664a4a6e808 | -2.4451 | -49.2093 | 2026-09-20 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| ac5f98fd-5c11-31c7-a1a9-cdfba2d3a3f8 | -12.8704 | -50.9933 | 2026-09-20 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 52e7d4d6-ed88-3cd0-896d-2d1ffd42cf48 | -5.4085 | -44.2874 | 2026-09-20 00:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6c833088-b0d6-3f92-a897-4dda3220adb0 | -9.4769 | -40.3365 | 2026-09-20 00:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 1e1e102f-28db-3ee1-a296-8cf83f0d7bb1 | -8.1872 | -54.7622 | 2026-09-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 96e3e783-8b43-361b-b940-fbe4a5973e8f | -12.7621 | -46.18 | 2026-09-20 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 9ac817ba-ef0b-3dc4-b132-52fccd27415b | -13.0177 | -46.9125 | 2026-09-20 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 70330649-0f79-3767-924c-ffce04fd9b5a | -2.8974 | -57.8181 | 2026-09-20 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ce6f5364-e62a-353e-b398-016cacd9698f | -3.6763 | -60.6029 | 2026-09-20 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5c7753e1-605d-3775-a102-254b131a5923 | -5.3478 | -44.8398 | 2026-09-20 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d729c3c8-4c61-3e4c-b5b8-6c5640aa235c | -13.037 | -46.9096 | 2026-09-20 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| ded4c0c3-23f7-3178-aadb-ad0997c9f641 | -5.4087 | -44.2644 | 2026-09-20 00:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| cad0fc74-faf0-32f2-a389-d3a8f25095d3 | -2.8791 | -57.799 | 2026-09-20 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 17ac6d09-f475-380d-9605-b3a18cd97fa8 | -9.4773 | -40.3116 | 2026-09-20 00:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 156.3 |
| ec9518f7-23c6-3434-a26e-b6e3c9e4e2d8 | -8.0464 | -61.3618 | 2026-09-20 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 033b4f17-e2ba-3f03-8130-7db6a50e0620 | -14.6856 | -46.6886 | 2026-09-20 00:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d690c246-f58c-37a1-badd-284db51da582 | -3.6946 | -60.5835 | 2026-09-20 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 148bcb70-40c3-34a1-9a36-43061a0fca26 | -2.4636 | -49.2089 | 2026-09-20 00:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| bede91ff-5f54-31aa-9e80-75c1e61bbc8a | -9.112 | -45.7294 | 2026-09-20 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1c436be8-8c9c-31b1-95f6-020e2d51aff4 | -7.3259 | -55.6153 | 2026-09-20 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a085a655-6d1d-3c1b-b8d9-15cca78c2930 | -11.118 | -54.0268 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 51387977-d243-323e-bb58-f0697a777f7e | -11.3983 | -51.3968 | 2026-09-20 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ec2cd8fd-7ad6-3fe2-ab61-7c74a1a9f315 | -11.2307 | -54.078 | 2026-09-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 12d1590f-5bfc-3467-8f9a-fbe3a8036bb5 | -3.6762 | -60.6219 | 2026-09-20 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 66328c5b-b0b0-35d9-b179-ade91993f113 | -5.809 | -47.7692 | 2026-09-20 00:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 39a2f328-be46-38e7-bc97-2c0df880457a | -11.379 | -51.42 | 2026-09-20 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 3047647f-23b0-348e-94c4-58e8057a5fca | -11.2307 | -54.078 | 2026-09-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 08e4708b-eeae-300b-b517-7b3605b1ccd1 | -9.1313 | -45.7046 | 2026-09-20 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 0fd456fa-eb15-30b9-acf1-e87edccb56c5 | -2.8974 | -57.8181 | 2026-09-20 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5783ffed-8544-3e8c-8af8-ee4a5e3f68f2 | -3.6946 | -60.5835 | 2026-09-20 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 9a069942-6f43-3dbc-a794-496a4ad1574f | -2.4451 | -49.2093 | 2026-09-20 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b2eb8696-b322-30aa-9a55-219e63340401 | -12.8896 | -50.991 | 2026-09-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 245.2 |
| d5b4645c-a2c2-3bb2-bf0c-dcbbf9491251 | -5.8274 | -47.7898 | 2026-09-20 00:10:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d4de1768-4f31-3c06-b7b6-7538a38db79a | -14.6856 | -46.6886 | 2026-09-20 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9ad9c4db-c314-3500-b5ec-18d086710dc7 | -12.7432 | -46.1601 | 2026-09-20 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d345e145-2aa5-3260-8a53-816bbac87ee1 | -7.5334 | -45.4367 | 2026-09-20 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 826ecb3f-4c0e-3e84-995c-34e319a44ab5 | -8.1688 | -54.7432 | 2026-09-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4ae62f6c-ddab-3cff-aa39-d73293bf753b | -5.3478 | -44.8398 | 2026-09-20 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1b250eb2-fd44-310c-9478-964828deba64 | -11.8547 | -47.6596 | 2026-09-20 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 467adad4-f010-3efe-93a4-ee0a3684e955 | -12.8893 | -51.0124 | 2026-09-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 196.0 |
| f365fb22-7a20-3035-9574-1e33972f9b2a | -11.379 | -51.42 | 2026-09-20 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 39fcffde-d726-3abd-b8b7-25e4d7e78c16 | -3.6945 | -60.6215 | 2026-09-20 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4eb1c94f-910b-37d4-93c0-526bebf092db | -8.0464 | -61.3618 | 2026-09-20 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0731ab72-66d3-30ce-a968-60b2c257dc57 | -11.0802 | -54.0302 | 2026-09-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 47d2a471-3896-3d59-ac8a-dd9418b97b94 | -12.7621 | -46.18 | 2026-09-20 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| c69c4cf2-8c92-3f82-97c8-b3d6816abef7 | -12.9088 | -50.9886 | 2026-09-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 4b165a57-aff8-3215-9486-d33e3037dcad | -7.5522 | -45.435 | 2026-09-20 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 93db5244-a98f-354c-acd7-83287be1cd4e | -5.4085 | -44.2874 | 2026-09-20 00:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 77e73e8b-0af4-322c-a4ec-52fe7c48517f | -12.8701 | -51.0148 | 2026-09-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ca466f3e-3689-3aa4-b3b8-2fd216789962 | -12.8704 | -50.9933 | 2026-09-20 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 6c432db2-aab8-3c7a-8088-0bc5b37887ae | -8.1686 | -54.7634 | 2026-09-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| cd11a32a-c1dd-3134-9ef6-d30793e3250b | -3.6946 | -60.6025 | 2026-09-20 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| a61efcb2-d39f-32dd-843f-2c5a2d3d6632 | -7.3259 | -55.6153 | 2026-09-20 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 7d98ff64-a17a-392b-94d4-f0a61dacaa6c | -7.3073 | -55.6163 | 2026-09-20 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 33ceb8ca-f2d2-321e-92bb-03111e0513b9 | -12.7625 | -46.1572 | 2026-09-20 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| bb3e49c8-fdcc-34cf-a37a-552b2c084bfb | -12.7428 | -46.183 | 2026-09-20 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 256.6 |
| a08a547f-f686-3dfa-9ecb-1420a54f5286 | -11.3793 | -51.3989 | 2026-09-20 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2c13c940-39b2-37e6-972a-98381498fc90 | -13.0177 | -46.9125 | 2026-09-20 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 640b73f6-c2c9-3d32-b2fb-1686093dbdd4 | -10.3917 | -48.8915 | 2026-09-20 00:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| fbaf2cca-a1ef-3c64-94be-08ef1417553a | -7.502 | -44.894 | 2026-09-20 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 4b2fe91b-f3ba-35eb-b7ff-aeddd2970519 | -7.5525 | -45.4123 | 2026-09-20 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |


[Clique aqui para ver as próximas entradas](README2.md)
