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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14389ff0-fc00-398a-b321-61c10cff352f | -11.672 | -52.168 | 2025-09-02 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6e4cb3c2-c85a-3e45-8487-0d9dea61eb5b | -10.4452 | -50.5206 | 2025-09-02 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c4bbac19-6ad9-3996-b4ca-292282c30466 | -11.5694 | -47.6081 | 2025-09-02 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4003a8f6-2313-36cf-ba58-0c896789fdc5 | -11.8328 | -51.5399 | 2025-09-02 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bf04c8a2-a9b1-3554-ae53-39f538171731 | -11.8138 | -51.542 | 2025-09-02 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 90eb4b62-06c3-3781-b1d4-13fb97c22c31 | -11.6527 | -52.191 | 2025-09-02 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 53501fde-a991-38da-b64a-193301fa9a7c | -6.9632 | -44.3477 | 2025-09-02 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6e152198-2bd8-3e1b-957b-97f8a64a60a6 | -11.0841 | -44.6575 | 2025-09-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 633f4df4-857e-305b-85f5-9d1bca383c36 | -11.1037 | -44.6315 | 2025-09-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 45f40f25-ee8b-345c-893c-0a3bd88902f6 | -7.9351 | -46.4559 | 2025-09-02 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 94d658ba-ed78-3ee5-bb78-60ab7bb03b40 | -8.7339 | -50.4688 | 2025-09-02 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 9f5fe31c-77de-3bed-a596-47ff468bf74c | -8.8659 | -45.7788 | 2025-09-02 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0f7fd468-b822-3877-81f4-a55c6e88ee40 | -7.1089 | -44.7703 | 2025-09-02 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c6b628d4-5b76-3646-8bbd-11d2807b8570 | -11.6717 | -52.189 | 2025-09-02 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 1fce559a-9fd5-36a8-b88f-a62feda16869 | -6.5305 | -44.454 | 2025-09-02 13:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 41da028e-be53-3fad-a22c-dc288efc3ec1 | -12.5769 | -44.7814 | 2025-09-02 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f123c7fb-90ae-3d74-b46a-0362b639c976 | -6.2676 | -44.4984 | 2025-09-02 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9675124d-5164-32a4-a8b0-94a919bfba91 | -10.0623 | -48.0978 | 2025-09-02 13:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 47a4dbd4-8fcf-3a18-8701-eff3d2ac05a4 | -7.9165 | -46.4354 | 2025-09-02 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2f67197a-8b2f-3c99-a52a-842bf1d2f051 | -9.7483 | -48.9814 | 2025-09-02 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 579.6 |
| dd179916-bd40-33ea-9044-f13ace187d9e | -5.9698 | -44.2923 | 2025-09-02 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| b5f2d20d-acc8-3968-a4f5-e6ce281c7cc4 | -14.0508 | -44.5543 | 2025-09-02 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 09336201-63ea-3cee-a713-f5a22c114f37 | -8.8281 | -45.7828 | 2025-09-02 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 15cdff03-cadd-3c4a-89ee-ae46ab746f23 | -8.8451 | -50.5864 | 2025-09-02 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| ca06e92e-561c-338e-8827-904af46d679f | -8.847 | -45.7808 | 2025-09-02 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 272a9792-8a46-3355-bad9-6931e077b3b6 | -11.9224 | -50.6153 | 2025-09-02 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b8b1462a-7b44-35dc-8e5c-734bf15a62d2 | -7.9163 | -46.4577 | 2025-09-02 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 268.4 |
| 2e937ebb-e9cb-3c50-8847-30d8ce3f48d2 | -4.9122 | -43.2103 | 2025-09-02 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 376229b0-6100-3664-be79-913cb9ca14ef | -8.8638 | -50.5847 | 2025-09-02 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 40590267-7440-3018-ad33-20cc4ec3d927 | -11.653 | -52.17 | 2025-09-02 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 2ce84458-343e-3f83-8b15-013b040c8df6 | -6.9754 | -43.2326 | 2025-09-02 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 196.0 |
| 637a75a8-8d78-3066-8a8f-efcde7d3ff4a | -10.062 | -48.1197 | 2025-09-02 13:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 941dce3e-9326-3615-a94a-0a9eb2fd636a | -17.901 | -47.1801 | 2025-09-02 13:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 97d8c775-376b-38b7-9eee-e4a8d1f3813c | -7.1091 | -44.7474 | 2025-09-02 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 276e0cf6-c703-31fb-874c-f34da1cb0f52 | -4.9124 | -43.187 | 2025-09-02 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| f52d9e11-cd81-360d-972b-ac47f822969c | -13.3082 | -46.8229 | 2025-09-02 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 579ca66e-49a0-3223-9914-438b1ba357a0 | -11.6647 | -57.3533 | 2025-09-02 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ff0e7e1d-8d9b-3f8a-88a7-d567c2440a98 | -11.1033 | -44.6548 | 2025-09-02 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 5927c324-8d93-3624-889e-0e7b8bf61c56 | -12.996 | -48.1022 | 2025-09-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3aa3cb68-54b0-3341-87cb-5262adefaae2 | -9.7297 | -48.9617 | 2025-09-02 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 724ead13-6e6b-3a29-b98c-bda698c97144 | -11.6715 | -52.21 | 2025-09-02 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 152b7e4c-ebb3-3994-b9e2-bbcffcf7b8b7 | -8.8641 | -50.5635 | 2025-09-02 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 8bac4e41-ccb4-3d5e-a8dc-3ca6ccfedea2 | -9.5025 | -57.8032 | 2025-09-02 13:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c4c03d88-7c1f-30cb-8490-df9e288c1309 | -9.7485 | -48.9598 | 2025-09-02 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 5f1de35e-e11a-3384-9135-8fe217f9000d | -11.8518 | -51.5378 | 2025-09-02 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 7b1d5b3d-afdc-3f2e-b710-d618c014c0ad | -5.9511 | -44.2937 | 2025-09-02 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 170e65a0-d192-394e-9177-9166f4c2429d | -10.2976 | -47.5201 | 2025-09-02 13:10:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| af0d8b28-2086-33a5-b778-ac8799f1205c | -9.4987 | -46.4749 | 2025-09-02 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 432be195-be72-38b5-bcd9-cd58c122f3e0 | -9.7294 | -48.9834 | 2025-09-02 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 01c7f72a-7d28-37f6-bd77-d6267140dab7 | -6.2038 | -43.3475 | 2025-09-02 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 2679e09b-c295-3dd9-86b6-cca78e0e4d57 | -9.1207 | -61.4864 | 2025-09-02 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d628d0a3-4ed6-3879-a185-97dee62416ba | -5.9513 | -44.2707 | 2025-09-02 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1f80d7d6-5784-391f-a971-576442388bf4 | -6.2038 | -43.3475 | 2025-09-02 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fa055c30-23ea-32f2-b60a-240ade009212 | -4.9124 | -43.187 | 2025-09-02 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 3af7a38b-5ca1-3328-a873-da4c812a45f9 | -11.8653 | -50.6219 | 2025-09-02 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 9590dbf7-436d-3158-92c9-da3a188a8e52 | -7.1091 | -44.7474 | 2025-09-02 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f38cf7f2-cc5b-3135-bc6e-868eb424a30b | -6.8724 | -45.8554 | 2025-09-02 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 4bfaa101-4b1a-3707-942e-80989b46cc96 | -11.8138 | -51.542 | 2025-09-02 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 77770bb2-07cd-3fe6-be70-4a06526547df | -10.2596 | -47.5245 | 2025-09-02 13:20:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| c49f8b30-4088-310d-912c-dda3454f57b2 | -8.02 | -44.084 | 2025-09-02 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5dac2f0c-68b1-307e-9901-be57d17518f7 | -11.653 | -52.17 | 2025-09-02 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 3c075163-40ab-38e0-af39-5a590af9a04d | -11.1252 | -50.5982 | 2025-09-02 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| aaae03e5-84b2-324a-94f4-601061c26c35 | -7.1089 | -44.7703 | 2025-09-02 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2b66169f-46a2-3efb-b1f3-ff9d1f5f8bad | -5.9511 | -44.2937 | 2025-09-02 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b49c6609-9541-30b2-aa59-a96153ab2500 | -8.8467 | -45.8034 | 2025-09-02 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 3bbef831-13c7-3b53-9335-dd3777c5148a | -1.1576 | -46.3289 | 2025-09-02 13:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8ef8d73d-1f21-36fc-a700-798fcf94eab0 | -11.6715 | -52.21 | 2025-09-02 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| aaba4451-9d72-3a35-b77d-d3204dbcf15a | -6.9942 | -43.2308 | 2025-09-02 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.0 |
| 7599a672-56b0-3c87-a206-82f1c98177b0 | -4.8936 | -43.1882 | 2025-09-02 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| d9ff18ff-20c4-3125-998d-5d888c2910da | -8.8451 | -50.5864 | 2025-09-02 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 034ceb66-10c5-3415-8019-e98cb8353370 | -7.5476 | -61.3437 | 2025-09-02 13:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b7a1989d-9007-3777-aa85-6e3c5cb9f8eb | -11.9224 | -50.6153 | 2025-09-02 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6cac3837-dbbf-3d46-ab10-f368ab2aa54c | -11.5694 | -47.6081 | 2025-09-02 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 172d866f-6806-32d1-831b-6ba89e7e71e4 | -11.8328 | -51.5399 | 2025-09-02 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| bc4c7c9d-288a-3500-bffa-3fa9113c671e | -11.1029 | -44.678 | 2025-09-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 4e1b1886-586c-36a9-9921-c3e859a12d67 | -8.0203 | -44.0608 | 2025-09-02 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 24a572da-2c42-3279-8d96-93fecab46f8c | -9.4791 | -46.5218 | 2025-09-02 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ba31a409-9458-3a71-8106-5c1cb6938ae3 | -6.5305 | -44.454 | 2025-09-02 13:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 106d4502-dd3c-3c93-965b-319b04804669 | -8.8659 | -45.7788 | 2025-09-02 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5406fcf8-2016-3abd-a82e-58dd728dc587 | -10.062 | -48.1197 | 2025-09-02 13:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 5e0d1a6d-896b-3de3-94ad-958d1a01a3fb | -10.0623 | -48.0978 | 2025-09-02 13:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d9ec2135-4c91-33e8-881d-53f3580d069a | -11.6647 | -57.3533 | 2025-09-02 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 6cc0d0c6-a04d-3b47-bca4-e5c2996f80ae | -14.0508 | -44.5543 | 2025-09-02 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 769853fe-4859-3325-bb35-7eb316ba346c | -11.1033 | -44.6548 | 2025-09-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 397.2 |
| 61403a06-f32a-3101-9e7c-b6ff87809389 | -12.9194 | -48.0909 | 2025-09-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 94c3ccad-b753-3186-9d74-d9f831dd73fa | -6.8914 | -45.8313 | 2025-09-02 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 0dede384-3015-3172-bb46-03edd82b485f | -9.1207 | -61.4864 | 2025-09-02 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fedb8d9c-8476-39eb-ba0d-33f1aa7d08b9 | -11.6527 | -52.191 | 2025-09-02 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 964705b8-db20-3d83-9520-d584d888edd5 | -5.9698 | -44.2923 | 2025-09-02 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1ae2341e-56cd-3f44-b664-58d639824ea8 | -11.9415 | -50.6131 | 2025-09-02 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| c52df52d-616d-31c4-858a-91ec4412ee32 | -11.8518 | -51.5378 | 2025-09-02 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 274.2 |
| 497f6756-b7b8-3f11-9fc8-fe7da48e0a47 | -16.2953 | -52.9443 | 2025-09-02 13:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d59275a1-7579-383f-9c7c-c26eaeb3cbf0 | -11.1037 | -44.6315 | 2025-09-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 30ef1bd3-315f-3334-b106-c489e50589ca | -11.0841 | -44.6575 | 2025-09-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| f51782a3-6632-33e9-bc77-961ec0ead951 | -8.8656 | -45.8014 | 2025-09-02 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9508432f-e886-3f33-94d6-dbc3d4707030 | -8.8641 | -50.5635 | 2025-09-02 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 1c43677c-17cd-3a1a-9b94-842669ab1bf3 | -9.7483 | -48.9814 | 2025-09-02 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 307.6 |
| 59a2ed49-18d9-3373-920c-7984a7de7be7 | -11.6717 | -52.189 | 2025-09-02 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| ea0647c7-459a-36a6-aa64-9eee4fbb7768 | -6.9632 | -44.3477 | 2025-09-02 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0ccb646b-2c21-35a2-9e56-fcf836bf1c47 | -11.3907 | -46.8724 | 2025-09-02 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |


[Clique aqui para ver as próximas entradas](README96.md)
