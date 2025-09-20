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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f495ace9-ce64-3009-94fd-2d8aed651d6b | -3.46235 | -51.21345 | 2025-09-20 04:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a20e102e-5622-3639-9a51-1f0a1f36e9ac | -3.83886 | -52.31617 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 209642f4-42c6-3489-9122-60da1741de2e | -5.22029 | -45.42123 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 523b02d2-4874-3800-a8a3-4d9565412e52 | -2.83281 | -48.65648 | 2025-09-20 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1ea698b-db0c-3547-ac77-1c8e0444cf75 | -5.82986 | -46.28212 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 603adc0c-2800-3bd2-8c5b-21aa0cac5dce | -3.15946 | -49.47733 | 2025-09-20 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f455fea-d27c-3d60-bb2b-35c5f851077c | -4.35554 | -46.2918 | 2025-09-20 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dc177a3-5480-3761-a85a-39a154217b31 | -5.30389 | -45.58356 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6e1b7df-bded-37fc-9eb1-3ee7c851d5b8 | -4.13881 | -43.01176 | 2025-09-20 04:53:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dff4a8c9-463f-3818-a55b-4345b1ca1a3e | -4.28221 | -55.75496 | 2025-09-20 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef38fb96-a66e-3879-a639-5cd877bbae02 | -7.25303 | -45.49353 | 2025-09-20 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 942666e6-6b9f-3032-941f-686fbe100301 | -5.10636 | -43.20403 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 70b6200b-59af-3bf7-9a16-d18e191d4f81 | -5.79737 | -43.63551 | 2025-09-20 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fbc8811-7da1-3e63-97f5-3f55da244a60 | -7.25333 | -45.49472 | 2025-09-20 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c4d99cc-9856-324a-8078-a4e6ea2b7c52 | -8.606 | -45.34674 | 2025-09-20 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3109eaf-ab75-30ad-b726-9ceaf09d59f9 | -5.83717 | -46.28995 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb860f02-20cd-3408-bd28-025bd9cfe502 | -2.14481 | -53.65034 | 2025-09-20 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae31798-b304-3514-a492-004968258158 | -5.19244 | -45.48667 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 231637b6-2221-3655-b4d3-25ca97c3643a | -4.31265 | -48.10305 | 2025-09-20 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35f5c986-2cec-3804-bf83-6886ef06ae1b | -9.11358 | -44.67817 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 161cc8a0-ad0d-3aac-8d2c-e14a46db897b | -5.97397 | -47.66635 | 2025-09-20 04:53:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aeca668-1363-338e-bac1-f15f51c85a67 | -5.50892 | -45.46199 | 2025-09-20 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84aae283-19b5-3a22-9291-61acc66cac59 | -8.03772 | -45.69245 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7586d12a-f44f-3a62-a99a-2d65265f40f0 | -9.17225 | -44.633 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50473e28-0686-366a-98cf-bf2038bd0300 | -3.59808 | -48.98669 | 2025-09-20 04:53:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fc14d7d-b6a4-3368-972c-c1ccf5e29a2f | -7.44622 | -42.62258 | 2025-09-20 04:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ebbd289-81b6-328c-96ad-715e5337994c | -2.79828 | -49.62007 | 2025-09-20 04:53:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 849013c8-2d4f-3d86-9a4a-dac79bba0df2 | -3.98251 | -51.06423 | 2025-09-20 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64eada33-1e11-38bd-b4dd-af5bd765619a | -8.14404 | -43.63543 | 2025-09-20 04:53:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07ff79ae-9d3d-33be-857a-c66a5c4a0e8b | -5.62791 | -51.70032 | 2025-09-20 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22285ade-cba0-32b7-be5b-0cb03382369b | -4.08354 | -47.9584 | 2025-09-20 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4444c2d-aa6a-31aa-a1a9-38508ef57c30 | -7.44024 | -42.62359 | 2025-09-20 04:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 50837329-0edc-364f-9fea-017613133820 | -9.17283 | -44.64136 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd3f777f-ea2b-3a76-82b3-3d5c3aa9c57b | -2.43527 | -49.3358 | 2025-09-20 04:53:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7c91d1c-2141-3343-b309-033941adbe49 | -3.5172 | -52.74992 | 2025-09-20 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86046e70-cc58-392b-83b9-74dd77a051ed | -6.30861 | -42.93016 | 2025-09-20 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dfd1f2c-0ad4-3d95-b11b-7fd7cda525fa | -6.1949 | -41.22753 | 2025-09-20 04:53:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7e6bb3db-482b-32a7-8e37-f2e41003c2a1 | -7.44046 | -42.62177 | 2025-09-20 04:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c85ecf9-374d-35f0-a2f9-eb9a47be4ee4 | -5.04026 | -45.57027 | 2025-09-20 04:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13f9959e-c7e8-3991-a480-9910aedc2351 | -5.96497 | -42.91236 | 2025-09-20 04:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02d40720-ef01-358a-8170-b2c977b4df20 | -3.51386 | -52.7494 | 2025-09-20 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10c68688-2163-317c-b0a6-5153664245db | -4.78962 | -50.78904 | 2025-09-20 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cae5c4e-5c89-3a87-bd5d-2e5bd27e3921 | -5.19703 | -45.48736 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25c54659-13fc-3864-837d-1184bd1c24ea | -5.62995 | -45.00301 | 2025-09-20 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffd73d50-405c-3b73-b706-f2c911736f40 | -6.3482 | -55.56184 | 2025-09-20 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea43be00-69df-31fa-beca-69c373a8f848 | -4.66171 | -46.03681 | 2025-09-20 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01ab2d71-57e5-3821-b198-9487edd7a6b6 | -5.04967 | -47.90189 | 2025-09-20 04:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bbb639f0-1fba-3a58-bbcb-8521b59bdd5e | -7.25405 | -45.48953 | 2025-09-20 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42018736-ee8e-3dde-b04f-65967dce1033 | -5.93552 | -45.07975 | 2025-09-20 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16e3b960-1694-362d-8c76-e83a98e2f7e2 | -6.22776 | -47.31404 | 2025-09-20 04:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 765b54c7-efed-3a02-834c-c7d7ca87ae52 | -2.98992 | -49.29387 | 2025-09-20 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49bbff46-81b7-38b4-a749-2f8b0d179eb0 | -9.17182 | -44.63611 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7867a06a-a204-3978-818a-9c1f2bfa2860 | -5.08601 | -41.14309 | 2025-09-20 04:53:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a1e28bb1-0808-357e-90ed-15fa548c4ef1 | -5.79692 | -43.63871 | 2025-09-20 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e10a677-11b2-3c59-bce9-58e5ea09844d | -6.02096 | -49.86471 | 2025-09-20 04:53:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7936b473-9bce-32ec-b114-24d8d4112df4 | -2.69556 | -59.42525 | 2025-09-20 04:53:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 392996de-0937-3dfe-aff4-10598ada8b25 | -5.10307 | -43.20586 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 003bd78b-3cfd-3cc4-ab76-a8993b22d2a0 | -6.18695 | -45.42152 | 2025-09-20 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a16a880b-eed2-3039-bc15-de29b72a6df7 | -5.85769 | -43.81271 | 2025-09-20 04:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 751242ee-eb76-37e5-906f-b93992a25acb | -6.10155 | -47.86026 | 2025-09-20 04:53:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3edb44d-01bd-3141-83f1-a23f2d16c7cf | -3.73991 | -53.80844 | 2025-09-20 04:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e734f6d-d672-32e0-b0af-9e08fa6fa01d | -5.60711 | -52.1511 | 2025-09-20 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a05beef-c1aa-3b61-bd92-216f18a755c4 | -2.96026 | -48.60131 | 2025-09-20 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44871fc6-2fcc-3fb8-9af3-e040512719d9 | -5.19774 | -45.48261 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5404a5d2-cdde-3a58-be6e-21db3e9f3e6f | -5.52024 | -43.86007 | 2025-09-20 04:53:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b273f18c-02ea-3543-8fc5-1dc565f461da | -5.74459 | -42.58453 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a7974f2-259b-3909-a046-13ac876432af | -8.60672 | -45.34153 | 2025-09-20 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 330df622-1fe5-3c43-b147-545d50b6820d | -9.11916 | -44.67565 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0b620a4-e4d8-3872-97f0-4851d639f414 | -8.03301 | -45.69173 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3353f208-cff6-39cb-9a7b-49476bb3e002 | -5.80935 | -53.44336 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1f2ba9f-37dc-3de7-a8b7-83151d75781f | -9.45814 | -54.6724 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2ea0ad3-9d52-3aaf-8939-f51bbff547cd | -10.34855 | -45.2413 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb517500-6686-32cd-9b4a-34416c271285 | -12.07436 | -44.82 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf1bf896-3f07-305d-b52f-4d4d3ada748d | -12.09112 | -44.81563 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29de3dc9-5a0a-3c18-83ce-5c30d466b828 | -12.89923 | -46.78632 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 151e52e8-0b18-36a0-b416-204e18a00002 | -12.07319 | -44.82935 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3938610e-6dca-3867-91bc-b21af53bda67 | -15.27673 | -56.8555 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2b46da0a-bac2-366a-8654-c1a8d95a0b42 | -9.39627 | -54.68497 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f608bd7f-4a3f-3da3-bd60-5f7b0bce2f28 | -12.15543 | -44.93856 | 2025-09-20 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eaef830-0081-36a8-a1b9-f3a57f039d2d | -12.85353 | -53.00214 | 2025-09-20 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10ee6ed0-f3d2-3882-b3be-98dc75715cc6 | -12.08497 | -44.8215 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 359095cd-a4d6-3122-a014-674bd1b44513 | -14.43182 | -46.51497 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab097ed2-76c1-337f-afe4-df8874c69cac | -9.89816 | -59.60153 | 2025-09-20 04:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8736a00-dba0-3d86-8692-d81b14ec31c6 | -13.23004 | -57.12983 | 2025-09-20 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f69769a-93cc-333f-85b0-a29eed8e3824 | -13.96287 | -45.04813 | 2025-09-20 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d8b3d8e-031b-3c4d-8750-4697f1b414ef | -11.63997 | -52.8602 | 2025-09-20 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f5e5bfa-cedc-3a5a-877b-f4789954d834 | -9.51179 | -54.66254 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| feb3a0e8-d1f3-397b-ad09-f80d4f6f681f | -11.99835 | -63.52624 | 2025-09-20 04:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b0a2cd-ba25-3cf7-821c-509029580e3f | -12.90518 | -46.77734 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a1ba44a-474c-312e-b405-a8f4e8cdaa3f | -8.9685 | -47.68029 | 2025-09-20 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ffa5c60-1e7f-394d-a7ab-2e0437eb575c | -9.39172 | -54.69165 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 666ee90a-c064-3631-af7f-4ef6acab1772 | -10.01776 | -46.24239 | 2025-09-20 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5e83c92-fc4b-3a05-a9dd-cfbf3ced8605 | -10.61199 | -46.44999 | 2025-09-20 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8947a059-84ea-3b68-b427-68fd150e68f8 | -15.29453 | -56.83446 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82e290ac-bc60-3016-b1ca-7a699278f394 | -14.43112 | -46.52059 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d3f2c49f-fb7f-3527-ac3c-fbcdae8302d3 | -12.39719 | -43.82314 | 2025-09-20 04:55:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba8b1613-4c5f-3210-8d91-81b211a5e1f8 | -9.39966 | -54.68552 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2c3f0ef-66f2-316b-9265-9e08c7492691 | -15.29024 | -56.81754 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f20dd34-5a76-32ef-95c8-e5549ed24988 | -14.44177 | -46.51498 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dbe0db79-0891-3923-9675-a3def2163d82 | -9.40187 | -54.69333 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README23.md)
