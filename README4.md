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
| 114d01e7-fb1e-3f79-8947-47e36aa797f9 | -11.43964 | -47.51225 | 2026-07-26 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 141d1861-102f-3396-badf-e1aa2ece9b15 | -13.74349 | -45.51958 | 2026-07-26 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 297e4b82-fd79-3ebc-929c-d5f1965ab63f | -7.89608 | -48.27603 | 2026-07-26 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae1fbdf0-dcbe-353d-a8a4-fb5ec2b8fc08 | -10.39227 | -48.27288 | 2026-07-26 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ebc2aaa-1970-3ee6-b9a2-739611fe3c01 | -13.20111 | -48.33002 | 2026-07-26 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 165279d2-6463-3625-85e9-a27b09ce7eac | -13.74653 | -42.57178 | 2026-07-26 04:34:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a02994cb-931a-302b-85df-5b386c4a247f | -9.92892 | -47.90503 | 2026-07-26 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37414360-4892-390c-9277-1309d428e32d | -13.40966 | -48.16225 | 2026-07-26 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fe6bf55-a2b5-375a-8720-4a02ddd58f90 | -9.92614 | -47.90099 | 2026-07-26 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dcef865-e274-3b6d-96f9-33ad4fc130a8 | -7.85329 | -39.90074 | 2026-07-26 04:34:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c298ecce-c1ee-3fb5-9050-e9c07b58564c | -11.85461 | -50.2234 | 2026-07-26 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f93b37d7-5000-32cd-8264-738d82c27b69 | -9.73213 | -45.42877 | 2026-07-26 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be64aaaf-b17c-3d5a-b218-8e8c4e2de996 | -9.24398 | -40.51194 | 2026-07-26 04:34:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1dc4dcc7-9259-36ce-b93e-8e76af771ffd | -11.19928 | -54.04214 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c99bbf16-6e2b-3bc6-9b18-67323e70528d | -7.82967 | -47.10123 | 2026-07-26 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 778e13bd-b32d-30fb-828d-71b055ee249d | -12.6685 | -48.21373 | 2026-07-26 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95d4214d-7562-3682-9640-c417790097a8 | -12.66182 | -48.21266 | 2026-07-26 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e81af7d-4825-3a7f-bb32-eb82a5b2b098 | -10.34301 | -46.73952 | 2026-07-26 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef112244-61c1-348c-bf89-3a353b7d29f4 | -11.85127 | -50.22285 | 2026-07-26 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18bb5300-2e2e-3d27-bdf3-0d6ccbc822b5 | -11.37881 | -50.47189 | 2026-07-26 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10660eff-5b55-34fd-b539-dcbb56c4a936 | -9.48086 | -57.32117 | 2026-07-26 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49efaf73-ea23-32f2-a4a5-4322fe689be2 | -12.95597 | -41.17883 | 2026-07-26 04:34:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f0e8dffa-f558-36e4-af0f-9ea896baf672 | -13.97334 | -43.94766 | 2026-07-26 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a32b51b-f957-302c-8133-3cc5454c91a5 | -9.12853 | -43.01563 | 2026-07-26 04:34:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3107e4f1-47b3-3b54-a131-894b7c23c256 | -9.53173 | -47.12378 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66074efd-22bd-3966-8c9c-5ece97a89c1e | -10.39281 | -48.26938 | 2026-07-26 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4e0fa26-ecd9-3957-b048-120be476d75b | -10.57299 | -46.23421 | 2026-07-26 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 082a2671-703f-3ccc-9044-8635f1efafe5 | -11.02004 | -54.32486 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2798c50b-93af-3875-80a8-8b17be5f5dd8 | -9.93556 | -47.90608 | 2026-07-26 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c374d0a-5327-3d66-9277-52e78d9993b3 | -11.58479 | -50.14597 | 2026-07-26 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ca9b314-68d5-3902-9aff-d2ee15f08478 | -12.30453 | -50.09165 | 2026-07-26 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed42efc0-c3c3-326b-a36d-244523af6eba | -9.80161 | -48.92227 | 2026-07-26 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49b21675-a2ad-39fb-91ee-b856d0ef7951 | -12.67518 | -48.21479 | 2026-07-26 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 833c40c3-fea6-3416-b307-95900ce0c68d | -8.82893 | -47.07975 | 2026-07-26 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fad4287-6343-33fb-ad70-3ba1f74095c0 | -8.57248 | -50.04683 | 2026-07-26 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23ed6663-2324-3950-9add-15ff95a754eb | -11.02541 | -54.31815 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4e558a-657c-397d-9f10-5ba8b9fd152a | -13.20166 | -48.32642 | 2026-07-26 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1271b907-3a45-3d36-8af2-2c1f00a31cd3 | -11.76161 | -46.56876 | 2026-07-26 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62c34086-c8b9-3ee9-acfe-45d4fafcf0c6 | -12.67184 | -48.21426 | 2026-07-26 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 540f5ecd-9019-368c-9812-6de274d3ec60 | -9.08845 | -44.32344 | 2026-07-26 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8288190-b729-3dd2-874e-e0cb0af286db | -9.92946 | -47.90151 | 2026-07-26 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e45bb79d-294e-3a54-8d46-470656d82e91 | -8.83173 | -47.08387 | 2026-07-26 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6298926e-b312-3663-a35d-faedf7c486da | -11.48295 | -47.52257 | 2026-07-26 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f4aab7e-e3c6-3509-b604-c9e6e8af44e3 | -11.01659 | -54.32039 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3276bf5e-16fc-3a4e-8031-829e83213b16 | -9.53675 | -47.11339 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d86e091-3b10-3370-a887-065e56f84fb0 | -7.01206 | -45.43046 | 2026-07-26 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abb68663-2a99-3969-be36-411866d1e017 | -6.63847 | -51.24952 | 2026-07-26 04:34:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e8a09e3-f55e-3dff-8d01-880549486311 | -12.55718 | -52.24556 | 2026-07-26 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cf15fb8-6737-3121-a7be-9200b7aad9b0 | -12.92026 | -46.3562 | 2026-07-26 04:34:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 384fd972-60bb-391f-98ca-bcf51a920055 | -9.80215 | -48.91879 | 2026-07-26 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6bf00bc9-53a7-339f-853c-b8a95b33ef04 | -10.80529 | -48.57199 | 2026-07-26 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52c50139-f65d-355d-b898-db3d68f4b52a | -10.32873 | -46.74121 | 2026-07-26 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6275934-956b-3349-9ad0-00a6bf4d6024 | -9.84198 | -62.22052 | 2026-07-26 04:34:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38f6b008-3dae-34e2-9fb9-00884ff65607 | -9.53338 | -47.11287 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a901065-9734-331a-8a37-4b66922bb957 | -9.53118 | -47.12742 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5c2fab9-86a0-3e4e-a5bf-794f902f39ed | -11.36076 | -47.45161 | 2026-07-26 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd696911-12e2-3780-aa60-f3c7f37d29fa | -9.52781 | -47.12691 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce4a4eaf-2a75-3827-83e0-f7ae063d4c49 | -12.43989 | -56.54161 | 2026-07-26 04:34:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fcce1d6-88d0-32de-88da-b1bc9da27aa3 | -11.58421 | -50.14956 | 2026-07-26 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a667cdea-ce97-371f-a4a4-d6ea4fb10b2b | -12.32439 | -47.17226 | 2026-07-26 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31d23949-b5fd-31ff-9bf9-e2eafa422493 | -9.94933 | -48.69581 | 2026-07-26 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3da95af-a884-3453-b789-fc949aa01754 | -10.27451 | -46.72961 | 2026-07-26 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a4519bd-b29e-3a31-a7f4-537235c55386 | -7.83301 | -47.10174 | 2026-07-26 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 081f54ba-b608-3a7b-9f79-3b47116cfb9c | -11.58813 | -50.14652 | 2026-07-26 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db5ce194-6d25-3a78-994a-d3672dc564ba | -7.00856 | -45.42994 | 2026-07-26 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb8da1fd-8ebf-3b57-82a4-9be82296bc9a | -9.73092 | -45.42614 | 2026-07-26 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4404bf9-a5ec-3239-9fb4-dcb29f85a187 | -9.24471 | -40.50634 | 2026-07-26 04:34:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 12a34381-c88d-38fe-b937-87a588c99612 | -8.67396 | -47.35833 | 2026-07-26 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adda7898-eca4-37ef-b3f9-6df8aef4e5fd | -5.66927 | -51.65117 | 2026-07-26 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b273741-d86e-317f-99ea-254fbd791fe4 | -11.30701 | -54.47967 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d0e46c8-636f-38fe-994b-2637994b6ca1 | -10.28194 | -46.72688 | 2026-07-26 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c636ccef-66a4-344b-b10c-c5f95bb798c7 | -11.30765 | -54.47594 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91e04657-b70c-3a12-8b03-60565482102e | -12.32384 | -47.17607 | 2026-07-26 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0902bfb-eca5-30dd-8ceb-62f91104110e | -9.53957 | -47.11755 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c79ac542-464a-388f-9692-eb582468e4c1 | -13.77314 | -47.12919 | 2026-07-26 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a16b8c2-3492-3a10-b964-f30c4fffed8b | -13.19777 | -48.3295 | 2026-07-26 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12d5e02b-8861-3bd7-b1ec-96ae7e83f67a | -11.02886 | -54.32265 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036a8052-0eea-3592-a2e7-af43e980a8f0 | -10.5724 | -46.23814 | 2026-07-26 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d9460f8-9d0a-3e6a-8e59-57dabbe2b457 | -8.82837 | -47.08334 | 2026-07-26 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f4024d9-b4fa-3c3a-9fc9-fdfbb34651db | -11.479 | -47.52587 | 2026-07-26 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b3dedf2-87ac-3008-b23f-0352b69b6225 | -6.73095 | -47.45739 | 2026-07-26 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a288bec-2ad0-3e71-a039-d49f630fea99 | -9.48143 | -57.31808 | 2026-07-26 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ad8b331-a44c-3156-9fdd-0acda3b18149 | -9.83509 | -62.21915 | 2026-07-26 04:34:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ef78f8d-5a0c-343c-beac-22b737edd2d7 | -8.67729 | -47.35885 | 2026-07-26 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae449cb5-7e83-3eff-b27f-14f3dd15f2e5 | -10.83689 | -49.3908 | 2026-07-26 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b1ed278-2333-3c8f-adb8-206422bbdae5 | -11.1532 | -44.4871 | 2026-07-26 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9f0ee9ee-a319-31d0-95ef-7b5395b32960 | -13.19832 | -48.32588 | 2026-07-26 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0763186e-5df7-3b8e-8408-a7c4da3678c7 | -11.15391 | -44.48219 | 2026-07-26 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4483b5b1-ccf8-3136-bb67-e277c3a37881 | -12.03326 | -47.80809 | 2026-07-26 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3f2d07a-e2da-3a2a-b8e0-bb6e2831d7bb | -11.85299 | -50.40455 | 2026-07-26 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29c7563f-4193-3793-8f6a-1a83e9a862f7 | -11.01594 | -54.32414 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfff8563-b7f0-3d64-b791-51942648c771 | -9.93224 | -47.90555 | 2026-07-26 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2122c20-51ee-3b0e-85e9-92dd9f946631 | -12.66516 | -48.2132 | 2026-07-26 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9292162a-e728-3ea4-ae75-62a6f88f7d41 | -8.83228 | -47.08027 | 2026-07-26 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af3f8d12-7049-3b28-99cb-bc75d2f79233 | -11.76511 | -46.56928 | 2026-07-26 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eba3f376-088a-3108-ac04-8f335e0fd3f4 | -11.76103 | -46.57273 | 2026-07-26 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67f455b2-b5f5-3e22-933f-09c25451b3b6 | -11.7686 | -46.56979 | 2026-07-26 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 825f2414-955f-3524-995e-c948138f763d | -11.48633 | -47.52305 | 2026-07-26 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cf82e2c-d17f-3f83-88bc-37a5f4683d32 | -8.67451 | -47.3548 | 2026-07-26 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6031f9cf-863c-349a-a8bd-e1f4a2882c06 | -9.94603 | -48.69529 | 2026-07-26 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README5.md)
