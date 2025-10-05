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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbdf8f19-d9d6-3384-802e-f94cc4d0b4a5 | -6.25495 | -45.35194 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a63f12c4-30c5-3edb-8052-0ce39d2b101b | -5.64488 | -43.91596 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4500dfc3-22d0-3178-bc04-39dcb6925260 | -5.91387 | -42.52498 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bc8e50d6-183a-3864-a6fa-595b3268a9a2 | -4.56707 | -55.95919 | 2025-10-05 04:44:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ba7d793-27ba-3390-aebc-691421cce74a | -6.15989 | -44.6687 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 5c96dcbb-e427-3890-a254-e24fc91fb65f | -5.78561 | -45.80133 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16e2cc3c-446f-3b7c-9cbd-8f521e575203 | -1.4173 | -49.01207 | 2025-10-05 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe67c68-bc8c-3dbd-b230-89b63a692f0e | -6.41272 | -43.04926 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fe03c85-b813-3263-a2a9-7daeeba03301 | -5.85567 | -42.79227 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5bc389f2-183d-3fb5-aace-d46fc2ad302c | -3.84592 | -41.58854 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1c5258c2-7c49-36f9-a47b-493d345b5f82 | -5.34266 | -42.96999 | 2025-10-05 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a04b3edb-3279-329b-9448-6f1cd5746caf | -4.6865 | -46.82211 | 2025-10-05 04:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3853eba3-fbd8-3415-a62c-5ff9c9c425c6 | -2.60814 | -49.40684 | 2025-10-05 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 944394c1-a4d4-301a-9882-eda57a1c1d28 | -0.91288 | -47.55055 | 2025-10-05 04:44:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3401f62-bd16-3cde-bc00-3d2e3b5f9c81 | -5.78719 | -45.79068 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f51a246-eb08-315a-a759-cad301a38686 | -5.64921 | -43.91985 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 115e2487-48a5-3184-ac10-701e711a07af | -5.64555 | -43.91111 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ba5e6d29-fe16-3aa6-9992-e5b44efa2152 | -2.60482 | -49.40633 | 2025-10-05 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 924d474e-7972-34e0-b772-51165ee33b2b | -5.76726 | -43.9795 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 462bad70-f848-3034-9a29-81942fdc8fe9 | -5.49212 | -42.79632 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c9be9c61-6f94-3f36-b2f5-d1c92e2df93e | -3.80729 | -51.76898 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de9502a4-2df7-3400-bca4-bced07abe711 | -6.29577 | -43.91658 | 2025-10-05 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2c5b662-66d8-303e-b507-b24ab8e5b5ac | -5.92548 | -43.30522 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3355ee17-db4d-3e67-a921-25799d653f47 | -6.63768 | -42.80011 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 08d8bb45-bd4a-362c-9187-b0beab2fae27 | -5.78196 | -45.74205 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ac4c0d3-0d8b-347a-ac27-3050428b3724 | -6.24825 | -45.33889 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d884a55-3240-3c36-9d31-da1465a3439c | -2.68527 | -48.38903 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab6ed765-f54b-37ea-95a6-6f656a2935d8 | -3.08672 | -47.79345 | 2025-10-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54647c86-d4d9-33bf-87ee-b8dd4314f8c4 | -3.77038 | -51.93844 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 12b06018-39ee-3ab4-a5fe-b829da845461 | -6.15549 | -44.66809 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| c334817e-a714-36bf-9e4e-55231031ac66 | -5.77146 | -45.78504 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7175cec-9681-3e6b-ae23-7e69821aa3e9 | -2.6847 | -48.3927 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bb577110-6c19-363c-8009-2c70ea0be037 | -6.24959 | -45.35934 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea6dfa20-55a6-3054-9165-6b50bb303c49 | -5.35687 | -45.94958 | 2025-10-05 04:44:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8083f65-a22f-33c9-be95-cf200e63a73c | -3.05059 | -51.10418 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad2d01c3-3172-30b5-a8c3-91492302b7de | -2.89909 | -48.07434 | 2025-10-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10df0ee9-f6e8-31f3-b9fd-0abb63a608f7 | -6.40257 | -42.68671 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3cbb452c-3e77-3de8-a59d-add558abd286 | -5.34863 | -45.2985 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed34095a-5f90-3987-bb5e-ecafe8bf4c28 | -2.55364 | -45.80098 | 2025-10-05 04:44:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a404424-51bf-35a4-a6c2-43f28ff0df5d | -3.81488 | -51.07253 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe6442dd-ea48-39d2-8fdc-e958144ba12d | -5.89446 | -42.91127 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 97d8c2ee-f4de-36f2-bcab-1a3ee8a298b4 | -4.86925 | -43.42163 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39c5d5fd-5d6d-3462-a3e9-87f1d59d1456 | -5.91397 | -42.89115 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| b070d9ea-bd8c-36bd-802a-2aa59e3305d5 | -6.0711 | -42.52792 | 2025-10-05 04:44:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc43345a-1132-3ce4-936a-643567e721b3 | -6.14985 | -44.676 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5740d095-2e8f-3be4-96f5-beb67a325959 | -3.81355 | -51.29574 | 2025-10-05 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c62c9c19-3cd2-377a-9e22-f4ce26546394 | -5.88608 | -43.71128 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e86b5fe-226a-3bc2-8d09-92b2afa092fb | -6.25174 | -44.23523 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ba6897f-cded-35c4-9d88-13ec1e90c255 | -5.4759 | -42.79354 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8fa914d2-7f0b-3711-88e8-6538c53faaf3 | -5.22476 | -50.8266 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70aafaba-bfc2-3dc0-88d9-b3b38bdf4e3a | -6.70099 | -42.15457 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 439e2d79-0505-3506-8cf9-587789b03a3c | -6.25663 | -42.45441 | 2025-10-05 04:44:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a0c026a-3f42-36eb-99b0-8ad57d7007a5 | -6.14287 | -44.66217 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ac9f4364-8945-396d-ba3b-352069a56ea7 | -5.88482 | -44.39426 | 2025-10-05 04:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b0b69b-bc99-3593-9ffc-988fd9e8a524 | -6.70895 | -42.17475 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dab3f935-cbe0-3adc-b70c-619f98fdb2a0 | -3.49758 | -50.26921 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4de7b7f-c850-3a41-881a-67046a7b41e0 | -5.85287 | -42.81223 | 2025-10-05 04:44:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 992fab1e-a35b-3f21-ac84-c5832c336385 | -6.15043 | -44.64091 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 36d489c0-87c7-38e9-83ae-84dc056d83d8 | -6.02423 | -44.01841 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17f0d3c8-695c-34cc-807c-cc6fe508e1f0 | -3.38041 | -50.27909 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5805eb8f-52fb-3662-a515-35eb7c2848bc | -4.23144 | -46.75747 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bc089b13-8f64-3453-9283-71a5000db69f | -6.14225 | -44.6665 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b3fb3f16-6630-3417-bbed-77760bdd395c | -6.67484 | -42.78657 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cd82f52c-04f5-32c4-98ea-ed692611df56 | -6.32623 | -43.9021 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecaaa193-39a6-33c2-a52c-34de157a1681 | -5.85606 | -42.78954 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d1f070f-8f18-3027-bf7c-a5e4efe1a7e7 | -6.1498 | -44.64526 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 40f48021-08bb-36bc-9dbe-55a1193685e9 | -6.15797 | -44.65096 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 84f122cc-4988-3fc5-9da3-043b3e3617c6 | -6.40698 | -43.06636 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| abf65624-fb68-3a90-8b5f-8cff72dab12f | -3.84916 | -41.56663 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a4779627-00cb-3009-99a6-0b5cf107d517 | -4.31725 | -48.09215 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 536150db-4d4a-3edf-864e-b4032e153410 | -5.92317 | -43.32129 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6cf32cd-5522-33c1-8293-e311791ef6b6 | -6.0998 | -43.48994 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f38a245-cfc4-30e2-a6ac-4b786c0f2694 | -6.08825 | -46.19604 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8e21146-4c7c-3935-8269-3bf9a9c23aa8 | -5.8539 | -45.84756 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4b77897-e5b2-36ba-9acc-bde8312fe8be | -5.43124 | -42.92836 | 2025-10-05 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c442180d-d640-3a02-8820-f0c8d197ab50 | -5.01155 | -47.21626 | 2025-10-05 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da9239b1-543e-30f1-b0c5-f302ab468b3e | -6.41189 | -43.0551 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 308b2f35-ffb0-30c7-976f-436196640b69 | -6.41107 | -43.06078 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e71056be-db9a-327c-9f6c-af0c8dafbc21 | -5.25912 | -42.97435 | 2025-10-05 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 0f3f2fa5-cbae-31e7-8c4e-cb5b895193e1 | -6.1561 | -44.66387 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 65c0b2fd-e406-36a0-b214-0ca8ddf6dde3 | -3.81104 | -51.07126 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4e7e6de-9031-373d-8488-966c73dc88aa | -5.77969 | -42.93893 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7aa2412e-ee88-3489-9a7c-e32b3c2cf9c4 | -6.14667 | -44.667 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c9d9e532-9e64-3377-ad95-7676afadb869 | -1.75374 | -54.14371 | 2025-10-05 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6327d3de-dd5e-3c4a-8e16-e6bf0d10db12 | -5.76602 | -45.76574 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cb0724e-be22-36c4-bf7e-9e3b6833dc40 | -6.34093 | -43.89873 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b61d9b0-b7ec-36ef-9a4e-dde2649691ed | -5.06552 | -40.4748 | 2025-10-05 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| e0d63cef-e2b8-3d38-9bf9-5d6510b56e79 | -6.30273 | -42.4417 | 2025-10-05 04:44:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a7ba8fca-ac4c-3d2b-ae6e-f00aefd43362 | -6.0715 | -42.52501 | 2025-10-05 04:44:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ac4dba0-0065-38b1-9f21-0d777a5a984d | -6.11075 | -45.88261 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7d75640-c59c-3630-ba82-042decd5d37b | -5.91836 | -43.32057 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f8af990-a313-34ee-ae56-a5cc51552f1b | -2.40374 | -49.36422 | 2025-10-05 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7846c76-32ad-3a24-8bb8-ee34fcfd35b4 | -6.39999 | -44.77998 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cda7ccc-e558-3285-ae79-d672bdfe0928 | -2.98856 | -49.2804 | 2025-10-05 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0852d496-137d-3a14-b57e-3f491d848711 | -6.19291 | -42.72362 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62821b15-68ae-3367-890d-6922219f5773 | -0.91001 | -47.54622 | 2025-10-05 04:44:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd85c003-2c3f-3a73-ae28-2e4a0ce9827c | -5.72618 | -43.84046 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef8d7878-6ce4-3fa4-9d2f-60044de50f3c | -2.89564 | -50.72644 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce19068b-be51-3cff-ba27-09fdd00c774c | -6.15169 | -44.6633 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 82d55c24-97b3-31a0-91ff-04116bd30c98 | -5.62526 | -43.21384 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README73.md)
