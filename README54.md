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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4df4a9b4-f92d-35e7-ab1b-82cc4212713c | -3.72501 | -60.59767 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd4390ec-5b1f-3992-9d5c-aca7285141b5 | -2.89171 | -50.43364 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea8b3fec-5375-3f8c-9c24-373709d976b6 | -2.89379 | -50.41971 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 625590aa-255f-3bea-afc7-de55b992ea33 | -2.95855 | -50.39751 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ea853d5-7415-3190-8e79-9e324e5998e1 | -2.05412 | -52.08488 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edf8f142-b104-3b38-8637-228ed42a1c35 | -4.36152 | -47.77763 | 2026-09-16 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 754ab8e0-2e2e-3b81-85c2-85a3527e9c9e | -2.78248 | -58.1462 | 2026-09-16 05:33:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8125a59-8ac6-3124-b66e-549b670b9ef4 | -5.75719 | -57.59482 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f51f924-31dd-3850-86f4-edbce3eee83e | 0.14528 | -60.40172 | 2026-09-16 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac541c4c-e5ac-3026-84c1-566389bc0a0c | -3.32949 | -58.12817 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38e878e5-4440-3778-aec1-ef05fee0d52c | -1.61682 | -55.56658 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62cfb79a-77cf-31aa-8329-ef19a573a6e6 | -3.12551 | -61.24901 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01ebf3c5-da5c-3623-8f60-ccdfee21aac8 | -3.42234 | -58.22825 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9359d9f-72e2-3b02-8d1b-9485c47e79ff | -4.5151 | -54.94706 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05e88571-5f00-332b-a0bf-cba812b1ce5f | -6.10855 | -57.63194 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eff3c9f6-a3cb-3fb2-9613-f10850c9d068 | -5.13335 | -55.9426 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4c86b5c-9789-341a-918d-60149a6605c5 | -3.81593 | -58.89546 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3604823f-95c6-3871-a1ec-89b6c32c6a37 | -6.7858 | -48.65447 | 2026-09-16 05:33:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3aa357d-acb6-3fee-89bb-79ac4fd3d4c2 | -2.26611 | -57.0879 | 2026-09-16 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cd98b74-7aff-34bf-bb38-a4eb032372bb | -3.47908 | -54.67748 | 2026-09-16 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4a96b3c-5945-37dd-a699-e2fe66137500 | -4.55081 | -54.92587 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64b70939-0515-3fcd-85b2-87dc17a2e5ab | -3.05713 | -57.14627 | 2026-09-16 05:33:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 802cb230-6c80-3ba0-9b12-ee8de207fc27 | -3.12435 | -61.25621 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 057412d8-ed12-36f9-9c45-10a088a6ceea | -5.6323 | -51.68944 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbc4a354-9ea6-324a-9edf-7bd6ac89a3c6 | -2.96425 | -50.39751 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d87342d2-0d28-3b35-989b-578c8634b28e | -3.12075 | -61.25223 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ed581c-7f2b-3c80-b1b6-b49b0c6c8ded | -6.37165 | -55.82541 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be453afe-9f36-33a7-820b-95a1ee8455df | -3.17413 | -58.65064 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecf9cef6-18bf-3690-9abb-704776921c43 | -1.28868 | -55.71792 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b21360a3-be18-3e5d-8a65-dd239cef56ac | -5.10028 | -47.61213 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d6f6065-d587-3a8d-a234-178ab3517206 | -3.70833 | -60.61647 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c981f4da-b8e8-3649-9466-f8e8ebd3fef0 | -6.01787 | -51.79247 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfcc4ba7-b43d-38cf-b474-f94f9e9ed87b | -3.47439 | -54.68059 | 2026-09-16 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71e4d269-f2fe-3d10-9e5f-6dd975cb665f | -6.3525 | -55.55945 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee3dedd6-7072-3ea0-a42a-b112b256bd9a | -3.3622 | -50.74458 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9067ccc-f461-3897-91ac-31198fe0d1d4 | -2.57628 | -55.99257 | 2026-09-16 05:33:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 525d766b-88f0-38c7-b826-3cb22222ecfb | -5.88421 | -52.09144 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 644bbe55-2849-34e0-b716-d077325fe318 | -3.70444 | -60.61942 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98a56ad5-be5d-3b6b-b66d-a53f26905f3e | -6.3709 | -55.83048 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0080fae8-7b2a-376c-aee0-fb60f7571fac | -3.42916 | -58.22931 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23b089b6-2482-3938-9866-9e216c12046c | -3.38769 | -50.45747 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07277b22-730b-3629-a45c-613f5dd216e5 | -2.74961 | -57.61787 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a732f364-0949-3b30-bd19-329889f0bb60 | -1.38164 | -56.8893 | 2026-09-16 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23306818-35e8-328b-ad2a-4463e7b66166 | -4.36068 | -47.78344 | 2026-09-16 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9c7bcc19-d22a-31aa-aa3e-29d074c01c9d | -6.01526 | -52.16203 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 617859e8-49d8-3cdb-8a52-3e6a89364124 | -3.15278 | -49.22746 | 2026-09-16 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 310e0bb2-a674-3fed-900a-2f9a5b7180a3 | -6.10917 | -57.62788 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04ca65cf-a191-3583-95c4-2b8e7307ac39 | -3.29645 | -59.46253 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af53dff8-42f6-36ff-92ae-5a25bfdd06fe | -3.47851 | -54.68113 | 2026-09-16 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 607bf4e2-70dd-377a-b7d9-ee148d5491c9 | -3.57707 | -55.59461 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6984060c-ed03-3e46-984e-47bdbba43ff1 | -3.38148 | -50.83612 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a64456f-cf2b-34ec-bbf4-075d39f22bf6 | -4.55138 | -54.92207 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b3f1722-783c-39fd-adb9-fea23ad571b1 | -6.01567 | -52.15905 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a24ca2d4-9899-3999-92fd-b21ffbad0d8d | -4.34339 | -46.60989 | 2026-09-16 05:33:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 741885f7-54db-3362-8077-d184b27a8fb2 | -5.14712 | -55.928 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6a92b87d-fe25-373c-a765-7ead83037af9 | -5.24383 | -59.98173 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3cf60ed-23ac-3c47-af8a-9aeedf4a8ae0 | -5.10076 | -47.62365 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 881434d6-727e-3964-8ed8-8c9470d6811c | -2.89431 | -50.41623 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8455dd12-f987-3e86-8c3d-1555d3f0214e | -3.17469 | -58.6471 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8ac8293-3eb3-30c3-9076-2f661453b01b | -3.11354 | -57.6844 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 438c2cbb-237b-3c2e-a994-3ddd6b2e4c09 | -2.91381 | -50.39783 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bfb5fc2-3b96-32f9-84a4-c01eca40a4a2 | -3.1176 | -57.68115 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfd37838-80b9-346c-9815-86fead195f9d | -5.13868 | -55.93338 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e37ff4d-7e4d-3d7e-a90c-84652e1b0767 | -3.11413 | -57.68062 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75095377-a30e-3592-9a54-71b4a43b1482 | -4.49457 | -55.49449 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 804234c1-ce47-3174-a545-545da9686b0b | -3.42517 | -58.23243 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f375223f-dbf4-3db8-a7cf-0bc27c0a8674 | -5.64595 | -60.21937 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a433f0ab-eba6-3f2c-b6d5-ee422fa8d783 | -3.84787 | -51.76931 | 2026-09-16 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f551871-510d-38b4-af85-cdd347ab64a5 | -2.69259 | -57.60984 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4aa69d0-64bf-3812-888b-e7f5d2b5362e | -3.76315 | -59.39335 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b480cb3-65c3-3ce2-8ad8-edd4a5cb78f7 | -3.0844 | -50.57249 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e179e48-396d-3d28-b12e-e755ef29a825 | -2.91014 | -50.42219 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04094038-0262-3ea4-bdbc-c934ece926eb | -5.12549 | -55.93941 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d24dbf-621e-338e-8321-97a8c952e4f5 | -5.45916 | -60.22204 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e50424a7-0476-3df7-a128-cfad94612633 | -3.44482 | -58.41764 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94e408f8-970b-3961-a913-97713051ca1b | -2.91559 | -50.42302 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f781475-6b1e-3930-9b96-f1d18a364d49 | -5.15806 | -55.93655 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86e9c7be-0eb9-3505-b393-b6b5bcbd3fe2 | -3.73654 | -55.94281 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ab621bb-990c-3694-8ee1-87c62e8c92fd | -4.51753 | -54.95853 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56d81a63-155e-3ef0-9003-4375c7bf4233 | -2.82072 | -51.33886 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4303dd50-3f00-3cf5-899d-392ecbe5806e | -6.09569 | -57.69244 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe77d1ef-229c-3efb-9b19-5e37b0f3e21d | -3.73387 | -55.94023 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed45d502-05af-36a9-8938-9bb047ce4d38 | -3.61081 | -60.56892 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d7cdfa3-053b-3811-878f-24eb4ce5a5aa | -1.21313 | -47.89184 | 2026-09-16 05:33:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30095d3e-175d-3bb7-a888-1b1fd39926f7 | -2.25045 | -58.10873 | 2026-09-16 05:33:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd38f0f4-5fb7-3124-a7dd-578b81633106 | -3.45639 | -60.5162 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 355d3585-5d83-3772-9fe7-02743fe91290 | -6.16168 | -55.70676 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c947914-4438-3c0c-ac77-62ea554506b7 | -6.36298 | -55.82909 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41d0299e-83dc-3e9e-bec2-7131f10caa34 | -3.19111 | -60.50617 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c18207d5-4289-3b1c-b7e8-903a23de3aa6 | -2.46179 | -54.76754 | 2026-09-16 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33a44bb3-2007-3af2-9218-dc017878de90 | -5.45971 | -60.21857 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d02016c4-096b-3fd6-a989-bf68d2b16693 | -2.91455 | -50.42992 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e2a0abd-d308-3392-84be-4623b67786bd | -5.14635 | -55.93292 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c8cdc3fb-0092-33e4-a832-db9c16178571 | -5.12784 | -55.94992 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95fcc293-5f7e-36ff-9906-ebd9a11576fa | -3.26907 | -57.8915 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 401da876-75ae-3ad2-8ca4-1269f49c3461 | -5.14946 | -55.93844 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 027cae6f-d1aa-3522-8cba-cfd2ce420c6a | -5.97691 | -55.35989 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3095a05d-15a9-3004-8b40-7dfea7652fe3 | -3.37649 | -59.53172 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e77daef-3eff-39ec-b5bf-fca06e2d999d | -3.17897 | -61.11058 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acfe54e4-8556-3f25-a742-93c7cb460f53 | -6.23076 | -56.04852 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README55.md)
