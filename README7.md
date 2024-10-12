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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2509133-fa9a-31cb-835e-e740580b6d88 | -3.6546 | -49.622002 | 2024-10-12 00:25:17 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52372210-d3f3-3835-82ab-798e21adf21e | -3.709 | -50.098499 | 2024-10-12 00:25:18 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06dd7922-1c7d-3de1-846c-237e721cd1d0 | -3.7109 | -50.107201 | 2024-10-12 00:25:18 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c244cb-4073-3ec0-941c-99f1dbc3a403 | -3.7129 | -50.116001 | 2024-10-12 00:25:18 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed3b2217-9c90-31a5-a7c9-4354e2e72a9a | -3.6838 | -50.031101 | 2024-10-12 00:25:18 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce6a0f82-c6f3-3369-a12e-ae6c84e391c8 | -3.6992 | -50.100601 | 2024-10-12 00:25:18 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21ac653b-fe93-3d5b-bc87-da2f1006ded6 | -3.7011 | -50.109299 | 2024-10-12 00:25:18 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41c1f51b-64f3-322b-aa90-b315b1b13fbc | -3.7031 | -50.118099 | 2024-10-12 00:25:18 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d55ad5d-2d8e-3e7d-a95a-d996a9fcd20e | -3.6894 | -50.102798 | 2024-10-12 00:25:19 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903a14d3-2e41-3c33-ba4b-4eecaf5b3661 | -3.6913 | -50.1115 | 2024-10-12 00:25:19 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c705a05b-69a4-3860-a49c-adcf85c22eda | -3.9245 | -51.213501 | 2024-10-12 00:25:19 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a65628b-1346-3034-9adb-1b90c8a82dbf | -3.9268 | -51.223701 | 2024-10-12 00:25:19 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d79c88c-24f1-386f-a98c-1d8c792519ea | -4.896 | -55.881901 | 2024-10-12 00:25:19 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c377e00-925a-3174-8248-128a82b55f78 | -3.5303 | -49.709702 | 2024-10-12 00:25:20 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31eadd60-e48a-3838-8f4f-ce321943fbc6 | -3.789 | -51.296299 | 2024-10-12 00:25:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6cf5b65-ed0c-3f4d-9db8-1a319a5cd0dc | -3.7912 | -51.306599 | 2024-10-12 00:25:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5327d26b-61e1-388b-9eaf-412a5d595051 | -3.7935 | -51.316799 | 2024-10-12 00:25:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34f99e9b-7c14-347d-b9f0-91d8426d8f9a | -3.7792 | -51.298401 | 2024-10-12 00:25:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee1c160-78ca-3921-a0cc-aa6cf5cca0a9 | -3.7814 | -51.308701 | 2024-10-12 00:25:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 587be057-1621-3a77-9ad8-bfc123d60e48 | -3.7837 | -51.318901 | 2024-10-12 00:25:21 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa37583c-8be4-3be7-b0d6-bc8bf9141920 | -2.7799 | -54.0133 | 2024-10-12 00:25:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b09e0fc5-9815-3cdd-b622-cbb61bb86f6b | -4.8128 | -56.1087 | 2024-10-12 00:25:22 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad962831-00df-3fc5-b4df-88088bfb3b60 | -4.8176 | -56.131401 | 2024-10-12 00:25:22 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30de3542-c1c7-30af-8526-094d11d36b79 | -3.7063 | -51.060902 | 2024-10-12 00:25:22 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee3096a2-dc0d-309c-b40e-bc042f03e830 | -4.8031 | -56.110699 | 2024-10-12 00:25:22 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aca148a8-aa2a-3f1d-ab89-fb726d789783 | -4.8079 | -56.1334 | 2024-10-12 00:25:22 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e53bf21a-76ec-3c2a-9433-97b3502caa79 | -3.5827 | -50.548199 | 2024-10-12 00:25:22 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a975d2f-a398-309d-b38d-f0e0e17ee915 | -3.5848 | -50.5574 | 2024-10-12 00:25:22 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 861648f7-301b-38d1-8405-575ddf78cee8 | -3.5868 | -50.566601 | 2024-10-12 00:25:22 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd0313ad-0cd4-30a6-8a09-a6d885de30d3 | -3.575 | -50.559502 | 2024-10-12 00:25:22 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94c6e556-cd4d-381c-afcd-c49860dd1b5b | -3.3957 | -49.844101 | 2024-10-12 00:25:22 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d2740e0-de1f-3574-9f2c-e3e842972a70 | -2.8611 | -51.6699 | 2024-10-12 00:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8e744df4-9b8a-35fa-ac7b-bc9c87d97a37 | -2.8795 | -51.6695 | 2024-10-12 00:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e29f08e7-8498-350f-b2c4-8f3a5cdae7ab | -3.0311 | -50.5642 | 2024-10-12 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7174d84c-831b-3652-8f38-ac7880a9519f | -3.4523 | -50.145199 | 2024-10-12 00:25:23 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3fdb10a-82b0-36d5-9706-e9a1fdc79bee | -3.4543 | -50.1539 | 2024-10-12 00:25:23 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a279f0cb-2a87-3739-abcf-58d2dce63f16 | -3.4562 | -50.162701 | 2024-10-12 00:25:23 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88bf579c-8476-3439-8828-5f5f39e5e6a6 | -3.4445 | -50.156101 | 2024-10-12 00:25:23 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4ebb396-16f7-33ac-85b4-7f97d384ecd4 | -3.2136 | -46.7843 | 2024-10-12 00:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 3edad6a3-be51-3d63-84ea-7904840e71ff | -3.2137 | -46.7623 | 2024-10-12 00:25:24 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f7108c2d-fdbe-3746-80be-3464ee920ceb | -3.4692 | -50.592098 | 2024-10-12 00:25:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723be3b3-3eb4-3f8a-bde9-97bea1858adc | -3.5255 | -51.310398 | 2024-10-12 00:25:26 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 479a94ee-7dfb-34f9-8bcf-35b8d6d83154 | -3.6978 | -50.1225 | 2024-10-12 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 592baaf1-4b13-38a6-8c68-50a4571e6dfc | -3.6979 | -50.1015 | 2024-10-12 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| dfe51d43-ff64-336b-8787-ec2d7ddd5ac4 | -3.7163 | -50.1219 | 2024-10-12 00:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 567d66c5-22b5-3416-b25b-a9b239e1c9b4 | -3.4734 | -51.538502 | 2024-10-12 00:25:27 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 339bf59b-f799-30bc-b95f-1fa9205f91d1 | -3.4636 | -51.540699 | 2024-10-12 00:25:27 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2f5157a-fac8-35e2-852f-b71d8a929ec6 | -3.2806 | -50.7598 | 2024-10-12 00:25:28 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 503ae95c-476b-37a4-a622-bdbc588223a1 | -3.2827 | -50.769199 | 2024-10-12 00:25:28 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcbe1137-d78f-3091-b31c-f4015afc4ba2 | -3.2847 | -50.778599 | 2024-10-12 00:25:28 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a55b6bc-3bbb-358f-a729-88b6c15c72ba | -3.1582 | -50.347301 | 2024-10-12 00:25:28 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c47e99c-bb9c-3422-bffc-ccffdf486409 | -3.2869 | -50.927299 | 2024-10-12 00:25:28 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 166ca153-18c8-3efe-bc21-020f01f21c1a | -3.289 | -50.936901 | 2024-10-12 00:25:28 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13ea2f08-8a93-37b5-b7e0-f8a703ffbb61 | -3.2911 | -50.946499 | 2024-10-12 00:25:28 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce92f68-fd28-39c7-984d-d6d2c4d8c326 | -3.1642 | -50.4207 | 2024-10-12 00:25:28 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 839e2805-135b-3520-b6fa-f823e6826929 | -3.1662 | -50.4296 | 2024-10-12 00:25:28 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16908319-a6ae-3b13-823d-b59d7f4a61cc | -3.1564 | -50.431702 | 2024-10-12 00:25:28 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3cd2a40-bda0-365d-b6b2-9ed60be4f3ae | -3.9394 | -46.445 | 2024-10-12 00:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 38193ff0-3767-3206-a333-d633f533e574 | -3.9396 | -46.4229 | 2024-10-12 00:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4144c9e2-0ca7-34f2-8fad-26fa90b45690 | -4.0062 | -60.3869 | 2024-10-12 00:25:29 | GOES-16 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f7bc65b0-7c88-3ff0-ba7e-f8e1f1c18a0e | -3.2364 | -50.838501 | 2024-10-12 00:25:29 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5e88313-53f1-3f27-8239-3c5f4e7630c3 | -4.1148 | -48.2515 | 2024-10-12 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 0c1ff92d-934d-3cd1-b870-169f8a626388 | -2.8402 | -49.519501 | 2024-10-12 00:25:30 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27185648-1024-321a-b2d1-c49a5428012f | -4.2665 | -50.9594 | 2024-10-12 00:25:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 15ba9557-d5a6-3726-9335-00cdacbf3c32 | -4.3782 | -50.8087 | 2024-10-12 00:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 024037f3-22e2-3adb-96a1-4c6ec5a3d76a | -2.7367 | -49.148102 | 2024-10-12 00:25:31 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ec29e8-6b47-35fb-983b-4dde8cbcd7f1 | -3.0393 | -50.551601 | 2024-10-12 00:25:31 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed286d8c-b7b4-34d7-b1f4-0d954c7d3706 | -3.0413 | -50.560699 | 2024-10-12 00:25:31 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94d8c5f8-a986-3be9-a26e-840ec1ca027a | -3.1887 | -51.225101 | 2024-10-12 00:25:31 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebca3c55-2db1-37e3-ba05-e790daef8a11 | -3.1909 | -51.2351 | 2024-10-12 00:25:31 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c917302-24c1-3931-b58a-89e865d10c6c | -4.5957 | -45.6315 | 2024-10-12 00:25:32 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 464a623c-1b1c-3b44-972d-8dd5b187190b | -2.7244 | -49.461399 | 2024-10-12 00:25:32 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0172ed7e-c9eb-38e2-8fe1-e0b0b573e22a | -2.7261 | -49.469398 | 2024-10-12 00:25:32 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6221d5c-68d3-3b41-9586-62132d752a37 | -2.7386 | -49.525002 | 2024-10-12 00:25:32 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 679b0ac0-0405-3d58-b8a9-ed1b35050d5d | -3.0409 | -51.021099 | 2024-10-12 00:25:32 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffad653a-a7b6-324d-8405-b9f63899a989 | -4.7004 | -60.8077 | 2024-10-12 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9af21772-0e9f-3627-b079-28f57aa669d5 | -4.7188 | -60.8072 | 2024-10-12 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7d41ebe0-17a1-3ed6-b54b-a5645873e9fc | -4.7188 | -60.7882 | 2024-10-12 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 128.5 |
| e4c1706f-5941-3360-a1ba-808901b7161e | -4.7189 | -60.7692 | 2024-10-12 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 94da778a-1a9b-3bdd-b21c-2ddb8a256d76 | -4.7371 | -60.7877 | 2024-10-12 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d9c40cc9-37b2-3890-9984-7efef905580d | -3.0504 | -51.1105 | 2024-10-12 00:25:33 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d94d6a-36e1-3af6-9521-311847b75c5e | -3.0526 | -51.1203 | 2024-10-12 00:25:33 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059e33d3-015c-3080-897c-2a66b5e7e8a0 | -3.0548 | -51.1301 | 2024-10-12 00:25:33 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6c5a92-c313-3303-b42e-673836de0454 | -3.0406 | -51.112598 | 2024-10-12 00:25:33 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349c5ee2-8d16-375d-8f2f-862b1a1c780b | -3.0428 | -51.122398 | 2024-10-12 00:25:33 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb7530bd-961a-3c70-8948-bb240d335ab1 | -2.9681 | -51.0168 | 2024-10-12 00:25:34 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d311a07b-af4b-35a3-8fa3-e8d62f925466 | -2.9702 | -51.026402 | 2024-10-12 00:25:34 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b84f324-a17a-32cf-9e6a-7c9774c3a3c2 | -2.9516 | -51.266201 | 2024-10-12 00:25:35 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a36f5dc8-44bb-3060-9788-d4d43a228aea | -2.9538 | -51.276199 | 2024-10-12 00:25:35 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 578a54ed-c140-3a9b-b6ce-bf44a534e771 | -2.8105 | -51.000801 | 2024-10-12 00:25:36 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9267956d-0cff-3650-9959-be279c2dee12 | -2.8127 | -51.010399 | 2024-10-12 00:25:36 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 978f7e5b-f8cb-3027-b90e-36ba9aba98ef | -2.819 | -51.315899 | 2024-10-12 00:25:37 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a31d647e-abdc-3a05-99ef-08c5b8f13cc9 | -2.8212 | -51.325901 | 2024-10-12 00:25:37 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 888e027c-c1dc-3526-9468-75d93d74ea80 | -2.8817 | -51.644798 | 2024-10-12 00:25:37 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d51b94f0-d825-333f-ad35-fa2a539762af | -2.884 | -51.6553 | 2024-10-12 00:25:37 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0feda86-3985-3ca8-bd5b-f2e2048d0bc5 | -2.9027 | -51.7397 | 2024-10-12 00:25:37 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2bcc0f0-5cb0-3b2f-b47e-076a710bf51b | -2.9051 | -51.750301 | 2024-10-12 00:25:37 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8575f9f5-9737-3d45-8b10-144da5da3792 | -2.8719 | -51.646999 | 2024-10-12 00:25:37 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a30e8d-9fee-3310-aba5-7904ea923a92 | -2.8742 | -51.657398 | 2024-10-12 00:25:37 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 754d34b4-036f-3dd3-a921-41f68a138a4f | -5.5547 | -44.689 | 2024-10-12 00:25:38 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |


[Clique aqui para ver as próximas entradas](README8.md)
