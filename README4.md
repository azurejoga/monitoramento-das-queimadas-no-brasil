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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d46ffa88-e9e3-31c1-839c-69349b0fa5e7 | -5.5432 | -47.054798 | 2024-11-07 00:31:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 672dab29-3188-3a3f-8854-b5cccfccf696 | -2.8474 | -48.660801 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 843f92ef-008c-3eb6-bc64-1bacfe93ed52 | -10.7355 | -49.8228 | 2024-11-07 00:31:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bee9834c-f603-3ca8-b810-147090f2b195 | -3.6168 | -50.187599 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19cbca67-bc8e-328b-aa1e-a0054cad9751 | -2.8829 | -48.726299 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c3858d-1d8f-38c0-9b2f-f82022d2d752 | -2.6602 | -48.563599 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78bd4335-852c-387a-b999-129d518c8e3f | -3.6578 | -52.333302 | 2024-11-07 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42f2498f-dad2-3357-a22a-59a2e4c3ad6e | -2.9399 | -52.700901 | 2024-11-07 00:31:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb175d2-94eb-37bd-89c1-62e5666e9954 | -2.0322 | -46.994598 | 2024-11-07 00:31:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2587dea1-0847-33ae-8ca8-f6a76dee43e3 | -3.4515 | -50.366798 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49957e47-3b30-31bc-848a-465556cf894a | -1.167 | -47.719101 | 2024-11-07 00:31:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8380b930-e637-39b1-bfda-acbcbcdc9ddb | -5.617 | -43.941002 | 2024-11-07 00:31:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6c0aac6-a7af-3c56-941d-3f5cc9f74f25 | -9.1461 | -43.141499 | 2024-11-07 00:31:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c782945-6d77-3dc5-b8ef-3f50e251ca77 | -6.0485 | -46.6036 | 2024-11-07 00:31:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16a4cb85-b1bb-3be0-ab82-9c7902350ad5 | -4.6636 | -46.3237 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47ba4678-90bd-3c9b-917d-8d11471185fb | -2.1331 | -48.739201 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c667cb2b-6523-3ded-9891-9d069208a718 | -5.7023 | -45.950298 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fad20d9-2128-34e1-b1e3-465a2c599a92 | -3.5633 | -52.690102 | 2024-11-07 00:31:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbcfc117-3b45-3d98-aa74-52736c7e78a8 | -2.7169 | -47.730099 | 2024-11-07 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7370b84-d079-3193-8225-0bd125b2b854 | -6.0754 | -44.709702 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca977dce-1d82-3cea-a869-122a49363bac | -4.4615 | -46.5215 | 2024-11-07 00:31:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c66aa65-7b13-342e-b172-0c5320fb3752 | -2.6037 | -49.264999 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 865f9535-8918-36a7-a92d-1e8edbee57aa | -5.0651 | -44.228699 | 2024-11-07 00:31:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ad1745f-8771-3414-91ba-364a41dd53ef | -3.6668 | -50.2267 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd7d81d-ffa5-3a1d-9ab1-aec1ee0aed85 | -2.1869 | -51.733799 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8117e58e-f3f1-3083-94e8-0f6b375fa72f | -2.5542 | -53.992901 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f481ba27-4513-3c6b-a8f7-e53193389a69 | -3.1985 | -53.395199 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae691022-3413-39a6-a765-a3564a18387e | -5.0315 | -46.846802 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eaa5e8c4-07d3-38c7-b7ed-9185d0a15312 | -2.029 | -46.9809 | 2024-11-07 00:31:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c057e8-71fc-3699-8ea5-aa991d4934ae | -10.7055 | -48.780602 | 2024-11-07 00:31:00 | METOP-C | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02631318-c44c-3fac-a9d5-e7afa7561524 | -7.6752 | -41.353199 | 2024-11-07 00:31:00 | METOP-C | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9742fb6b-b714-3807-870b-c12e4a99d45b | -3.3643 | -49.754902 | 2024-11-07 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4baf7d45-5ee4-3791-b6a0-aea040db99ba | -2.2351 | -53.6689 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3d3590d-1981-3b1b-bf85-b04073cc2b27 | -5.02 | -46.842201 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e935b88b-af01-31fb-91af-12a463ba34b7 | -5.4494 | -43.578602 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b799d635-0d35-3715-a46a-5262197fc295 | -8.4988 | -42.072102 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 081f910e-d83e-33ba-893e-e72b909ed9b3 | -5.3963 | -46.908298 | 2024-11-07 00:31:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de4ec18a-1ea7-387e-b8f4-a33cff9afc2b | -4.815 | -43.689499 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46f05bf3-403d-3dc0-a04a-48036ef1ec99 | -5.4103 | -43.3251 | 2024-11-07 00:31:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7657c060-c6bc-318d-abaa-9f5616df5f0f | -4.3797 | -47.2439 | 2024-11-07 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5312c25-ef53-31e0-b832-8bcfc3a39ba3 | -2.8065 | -48.662498 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b62a1706-70df-39fd-afbd-3dec5e46f982 | -10.369 | -49.168598 | 2024-11-07 00:31:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15a6d3ff-5f91-3e49-9983-6fd6da454fa1 | -4.4856 | -48.1138 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3a219e1-db48-33c5-a669-4b2f7fa65192 | -4.7056 | -43.794899 | 2024-11-07 00:31:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e36b27f1-106b-3f19-a84e-be97db4b6e17 | -2.6676 | -51.813099 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dde09d2-8cb7-3bf8-981f-7543f465568c | -4.3971 | -49.7686 | 2024-11-07 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc8f7aa-2513-3182-9e75-56ef7139dab9 | -4.9343 | -43.626202 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ddbaeac-16cb-38fb-9f8b-2ac59944cdaa | -2.8325 | -52.9072 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b23db3a-4981-3483-a940-d03882a30ce0 | -2.1347 | -48.746101 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f34c45-cc50-3049-87b5-944b690ff79f | -5.1123 | -46.076599 | 2024-11-07 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8fdd67f-6804-3290-b495-939f6e7b43fe | -9.2947 | -43.114799 | 2024-11-07 00:31:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0559f858-bea9-3460-833c-8970c985bf6c | -6.296 | -43.843399 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eeca4de6-a75f-3471-9e55-f27482fc5618 | -5.0126 | -44.3573 | 2024-11-07 00:31:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4380f5da-c41c-3cdc-899d-07e2e4a9e0ec | -6.0501 | -46.610401 | 2024-11-07 00:31:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| becf3d42-7db9-3f8b-bc4e-4be9200269bd | -3.7075 | -48.9977 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26fc5df2-5873-30a6-870f-becbcc9ec6e2 | -3.3331 | -49.027901 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16857d77-e17c-346e-8e96-26ee9d2a27a1 | -4.6751 | -46.3284 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f97165e-d54c-3348-aba1-9dc4888117e6 | -4.7036 | -43.786499 | 2024-11-07 00:31:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64acef91-fbe2-34db-a784-12cca18210a8 | -5.0413 | -46.844601 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbb893fe-0a03-32c1-99c0-6565853cadba | -2.6103 | -49.248501 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b85fac6f-f31a-3ba7-8f0e-46effa32ed72 | -3.4845 | -50.3764 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 573b3b28-5160-3c74-a55b-d0b151a73bb3 | -4.6053 | -48.685699 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f6601f-9483-3ad6-8228-a00c1a22bec7 | -13.7155 | -42.885399 | 2024-11-07 00:31:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 41e24889-e3c1-3535-9552-3f0999824c5a | -5.2229 | -44.904999 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 191f0fcc-6eb7-3603-b0fe-633807007bce | -8.9322 | -42.5886 | 2024-11-07 00:31:00 | METOP-C | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71662c07-41dc-3ef8-ac73-78335856f77b | -2.7689 | -53.216999 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a4e010-c306-3bc7-af61-439551408e63 | -3.3314 | -49.020802 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c8eb08d-348e-3018-8ce8-2a8766449ca2 | -6.3324 | -35.106499 | 2024-11-07 00:31:00 | METOP-C | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f7849f8-049c-3f88-bfc0-26ddf895bcdb | -3.9549 | -48.137402 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b3683f-6ddb-3453-9c6a-906557fefec1 | -1.719 | -45.7691 | 2024-11-07 00:31:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aab167e5-67c3-357b-96b1-536cdde2b182 | -4.5048 | -42.853802 | 2024-11-07 00:31:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bddc890b-9842-3111-9816-d02055af463d | -6.293 | -43.391701 | 2024-11-07 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60249502-b211-3dfb-a00e-c2dbb226821e | -4.484 | -48.1068 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 657ecdbb-a05c-3571-a7f1-50e7d85b70a6 | -4.4584 | -46.507801 | 2024-11-07 00:31:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b16cda1f-38db-34a8-85be-b04c6d1d76b2 | -6.0771 | -44.717201 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5095bd12-3c9f-3313-8470-db863c06fc92 | -3.4818 | -45.807598 | 2024-11-07 00:31:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd59590-2f4a-3a17-bb34-01635e38a2b1 | -7.9054 | -46.696499 | 2024-11-07 00:31:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39465b4e-7815-317d-bc70-dce5c4d45f72 | -2.4308 | -46.305901 | 2024-11-07 00:31:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db3459d2-8aed-3d9f-a0d7-f63dcd6ecbfb | -2.1947 | -48.377399 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f55a3ef-8e3a-3744-8e4c-9c0e6929df47 | -3.5127 | -50.455399 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6e7888-f851-3f41-a5df-d10f8836576f | -4.5789 | -48.071098 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b3aedf-1590-3ec3-ab04-f37dc4799c89 | -4.6069 | -48.692902 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818780cf-6daf-3b26-8e19-0442ce88f6a5 | -14.0784 | -44.138901 | 2024-11-07 00:31:00 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4898778-f6c7-32d6-83e6-f59024bd6bb8 | -4.7362 | -48.990898 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9099d53-b037-3f43-ac51-10d0935fe616 | -3.1509 | -51.677601 | 2024-11-07 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69e10e22-48fa-3c2f-a915-d6dda314fbd5 | -5.1452 | -47.705299 | 2024-11-07 00:31:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b014c79-282d-3085-b7a4-e74c979aad21 | -3.5848 | -50.228001 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9be016-d7a6-32d1-bf2c-38fef8909233 | -5.5334 | -47.056999 | 2024-11-07 00:31:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab126232-fd1e-3301-899a-608f07df3541 | -2.5057 | -49.106499 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 787302ba-2e3e-3abd-83f8-26de5780df56 | -5.4699 | -47.049702 | 2024-11-07 00:31:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 307b9dcf-d681-3c47-a438-2bc7f1d13980 | -5.0428 | -46.851398 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26af09cd-cc80-3c1f-bf30-25d87fcb19dc | -2.2272 | -46.900299 | 2024-11-07 00:31:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3112272-b74c-3d58-8b58-8ea2a1c47203 | -7.1341 | -44.823399 | 2024-11-07 00:31:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6b727ce-822a-3288-a8fa-71647138f6d8 | -5.0144 | -44.3652 | 2024-11-07 00:31:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eaf9341d-36ba-3dad-af27-ab39d9081d3c | -2.8934 | -48.591999 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a57cfc58-dc0f-36bb-aee1-0a9ad96f797d | -2.9033 | -48.589802 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b801d95b-bfb1-3520-9bc0-fba014074012 | -3.6201 | -49.611099 | 2024-11-07 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef005fa-e145-3e25-b099-74e3824e489b | -4.817 | -43.698002 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71e7f57b-9521-37eb-8447-789621b0bde2 | -6.5025 | -44.682098 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c06dd34-203d-3dbe-9d20-a010b9098aed | -3.4613 | -50.364601 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
