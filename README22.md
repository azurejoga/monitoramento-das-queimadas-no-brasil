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
| 58d23efd-f4a8-35a1-a79c-5e303858c01d | -9.12728 | -47.63537 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad4ad66d-5aa8-3fd5-aab6-7abf9459ac6f | -8.8246 | -46.18885 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a9528f8-87d1-3025-9e26-23b92235f859 | -7.75781 | -46.65277 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7d7164f-61d8-3e64-ad82-07d65b19c2ce | -7.76987 | -45.74356 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a38327f-5dec-3739-8eaf-c5dc73787586 | -3.09238 | -47.01226 | 2025-09-30 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cf2e1049-41ea-3f64-bf5c-8ad2a8360e5f | -10.8331 | -47.96849 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae171437-47ec-37a7-8453-075def0174d1 | -11.43144 | -43.50572 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30b0fb84-d9ee-3945-9d34-a6f80e84ed67 | -8.09293 | -48.00918 | 2025-09-30 03:47:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a8ea001-64f1-3468-abdb-c429cc30d36f | -5.02279 | -42.99318 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32eef426-5bde-378b-bb88-39e0799a74d9 | -7.85244 | -46.7561 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d93e60e7-703a-3b43-b6ff-74691d9e8e83 | -4.40745 | -44.39845 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a4ddae7-3034-3f87-86d3-c1fd52785959 | -8.66972 | -47.71602 | 2025-09-30 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 969a936e-d9ec-333c-8504-814975782bb6 | -5.41925 | -42.29306 | 2025-09-30 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e8b78233-caa2-3d3f-9782-0dc59eeddd25 | -7.29779 | -47.3058 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64d50f98-d9fb-3c3a-9e08-8142c6986d8f | -11.67008 | -44.28847 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efd15d2c-ff7a-3a77-952f-32abf5ecb17e | -5.5145 | -42.72883 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3ab517be-acd5-3984-87a4-608378051572 | -7.76017 | -45.77434 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331d22ba-6421-3896-842b-de79828d3f91 | -9.95266 | -43.58852 | 2025-09-30 03:47:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faf1525f-27bf-30a2-85cd-17448233f8e9 | -9.32457 | -45.70294 | 2025-09-30 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c102bc-b964-34da-b2c7-10fe9db4898a | -8.14181 | -46.38105 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d61590ad-05ce-3b2f-b9a8-42a54933332d | -11.66571 | -44.28765 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29558f88-7e38-3024-8a32-3b86c595beda | -7.90662 | -44.61359 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43cb5f73-9089-3d47-9355-5c2932f05d22 | -10.0703 | -50.22604 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e13baa9a-73f7-39c1-8a03-b81454b4c15c | -11.67806 | -44.29445 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c60a8a3-8da5-3b2d-bddb-89af09411865 | -8.53187 | -44.66875 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f20f75b-f3d7-3b97-84df-57e32ff7ac53 | -4.46739 | -38.60927 | 2025-09-30 03:47:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0c8c275-84c4-369a-9b2e-551031b30a78 | -7.84346 | -47.26748 | 2025-09-30 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cda822e6-28c1-353b-b1a9-5de55faf8f52 | -3.80684 | -47.58175 | 2025-09-30 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46aa40f9-3efe-3a3e-a52f-d20e8f97c2ae | -5.79057 | -35.60008 | 2025-09-30 03:47:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a04a0ddd-2a57-314b-af89-0fbb94e0d7ca | -11.48981 | -43.51679 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84912858-cfa5-33c7-8d17-85e477f3b510 | -5.4248 | -42.28586 | 2025-09-30 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29075c6a-417b-3a6e-8073-2060127a1a35 | -4.86847 | -45.05473 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1628a9f6-ab7d-37fc-8144-54867ba5167b | -4.15489 | -40.01493 | 2025-09-30 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba0ff1f5-d9bf-3cfc-a533-a766ac7b139e | -3.60516 | -41.38065 | 2025-09-30 03:47:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9be4e16-c481-3fa0-92ff-c2dbe7af1326 | -10.18646 | -44.8843 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 55046d5a-4d32-3594-b6d3-287349ee62a1 | -11.45526 | -45.00962 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82d9b36c-6eec-32c3-b71c-e351a9ee4af2 | -8.25078 | -45.54311 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1c40eb5-1a38-39dd-9a45-464e52bd7a08 | -4.25625 | -48.55754 | 2025-09-30 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bb4b224f-4493-3280-90f6-fcaf90191b65 | -4.07364 | -48.04094 | 2025-09-30 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97cd0e65-81b2-38fc-aa60-c55478954661 | -10.07875 | -46.06484 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e1244d6-d910-3dd1-afba-f4dfba60c4cd | -5.18732 | -37.65928 | 2025-09-30 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b0acadee-8f93-3a3d-9998-68291db74346 | -4.81784 | -42.76282 | 2025-09-30 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecef73a6-0f6c-31b5-a0a1-0599ad5b831f | -11.48631 | -43.51214 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 850473a5-eb77-33df-9af6-8d807f04abec | -11.44328 | -43.51185 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 296f9cef-9a35-3dde-b0d9-ab7b2548b997 | -5.06401 | -42.99498 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d85c8a2-5341-3ab9-a8ea-a9dcfb72df55 | -4.66231 | -46.47034 | 2025-09-30 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38ed46ed-dc32-3fc5-bbc1-432f7604f694 | -3.85752 | -40.44057 | 2025-09-30 03:47:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98c11319-98cf-35b9-b005-2b637e6e07ef | -3.8517 | -48.97812 | 2025-09-30 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 066cbe2e-6782-323c-9cef-fab5a99d49e1 | -2.80867 | -41.79953 | 2025-09-30 03:47:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75bedd35-451d-3162-92cc-3b331a77ef2b | -7.36231 | -47.04961 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07edb3f9-5b0e-3fb6-af62-bd6667b9e86c | -9.37 | -47.58325 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 588bdf94-c26d-31ce-8b0c-0b8d7c11167b | -5.49891 | -43.43203 | 2025-09-30 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4914045-e867-374e-8bbf-6f3c028998d1 | -11.45574 | -44.98051 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31f71315-aca2-341e-ad68-7b36aaf26018 | -11.46037 | -44.98122 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f591039-db57-3fc0-b25b-1ac28fb6e758 | -8.54144 | -44.66998 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39f11b4a-e188-3497-ab40-6fbe5b83d531 | -4.15709 | -40.00125 | 2025-09-30 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a0f959bc-bc95-36ff-9ce2-f21832709749 | -10.6552 | -48.5465 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54fbbc0c-677e-3420-9130-144f3e29c413 | -9.12645 | -47.64622 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d4c9f98-0bd2-31ad-ac46-d0b3dbaa82ee | -10.64 | -48.59341 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a47d3933-30d1-3851-a2dc-a700e0005268 | -8.14656 | -46.38538 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d07a5521-844b-35b2-a0a6-b6225e156a36 | -3.49 | -48.94172 | 2025-09-30 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f6dd8ed-eaba-31fa-bdf2-d44e0440007b | -10.76022 | -45.36775 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b387049-c771-3e9c-ab04-d1186f5dbf26 | -8.49772 | -47.25833 | 2025-09-30 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 637529e4-ea94-3bef-9e62-0b9190341577 | -5.49781 | -42.74764 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ada8ba8-a5e7-3127-a7bb-ec470ac1bea0 | -8.70868 | -47.98751 | 2025-09-30 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55544093-bbe1-3777-80c7-aa310a3b6afc | -10.18352 | -44.88635 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61def103-0264-39ed-9bea-4557392f2f14 | -7.82096 | -46.99278 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdff3d5f-4e2e-3eab-8c66-74dfcb7b4ad0 | -4.86666 | -37.45167 | 2025-09-30 03:47:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aeb972da-9e21-38d0-a6d2-e25bc21ad3ed | -4.40197 | -44.40047 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91fc03ab-9720-3c28-9728-a51991ec49fd | -10.83165 | -47.97598 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fcacc27-3bf5-3d56-8d02-3c2c3780d333 | -11.44396 | -43.50801 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9fc63a6-52da-3d51-acf0-51519835095b | -11.46105 | -44.99881 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1744766d-b288-30c8-81cf-7f1abd8c85da | -4.40658 | -40.69518 | 2025-09-30 03:47:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 672695c8-eb0e-38e7-a566-0d35de160566 | -9.51203 | -47.69383 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f7f3353-57f2-38d7-b1af-d3a048af56a2 | -8.83549 | -46.18833 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4068366-de67-3373-9e42-f09bd741db17 | -10.06342 | -48.19685 | 2025-09-30 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eeddff0-ed5e-3454-a88a-89738456154f | -9.93128 | -47.46178 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa7cd048-4889-3992-be09-33cbc0577205 | -5.13875 | -42.76403 | 2025-09-30 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41ebbe79-857a-3e21-a22b-e8bb8db2f341 | -10.84085 | -45.41247 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 202f8457-45e0-393a-9fda-2322412cebb7 | -10.3736 | -40.54438 | 2025-09-30 03:47:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4809f9bd-b9a6-31ca-99b7-5eae7c3173c7 | -9.12654 | -47.63938 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 816e3f53-f2b2-3fdb-85b0-9c1a6a8938e6 | -8.24047 | -45.52179 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ae0a96f-ac59-3426-b110-319bbe93de19 | -10.19871 | -44.89703 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 62fecc02-cf03-34ee-8649-046945f91645 | -10.42292 | -46.14809 | 2025-09-30 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59eacec1-39f5-350d-a4e0-9faa1a9d0dd1 | -9.23948 | -48.56271 | 2025-09-30 03:47:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5caf2ee-b417-3261-b011-e62c749e9f05 | -10.17064 | -44.89177 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efe80a42-37ae-3b21-9899-09acee19c1e1 | -5.50504 | -42.73159 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c109d229-8954-373c-acd1-45de0c831311 | -9.23861 | -48.5673 | 2025-09-30 03:47:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85f90292-1605-3d5b-ab2e-e4a05fc604ce | -10.10595 | -47.7893 | 2025-09-30 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a272c39-2ed3-35e4-97eb-8ea8ebc80eca | -3.68022 | -38.93416 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43c47e2f-1853-3ca9-93ab-9ca217b77e6c | -5.28114 | -43.16613 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e16a5a59-af0e-327c-b001-cab096253876 | -9.98744 | -45.41139 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e35e7d77-4c6f-3b44-8329-d1c6dc7301da | -8.04812 | -49.70827 | 2025-09-30 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 747bbbc2-5465-390a-b295-21b0acba5c24 | -10.94447 | -46.48071 | 2025-09-30 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18390e7a-ce3a-309a-a816-92efc71920e7 | -9.4483 | -50.90092 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7522fe84-af9c-3427-98ef-0727bda2572a | -8.26211 | -45.50945 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87b3a28a-116e-3018-a090-6cc8863c6425 | -10.8139 | -45.37023 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe9fc6e9-9d2d-33d1-aa84-5a3b26748601 | -9.44781 | -50.90606 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1376411c-bf38-3046-af6d-6290bfa7e6a3 | -8.28153 | -45.37376 | 2025-09-30 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5941c139-630e-36b3-b5b1-129d1e043c4e | -8.2324 | -45.50842 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README23.md)
