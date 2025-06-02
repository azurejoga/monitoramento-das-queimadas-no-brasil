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
| 9bb0aed1-24bb-3d85-9efb-86d226e513f8 | -17.2639 | -42.6527 | 2025-06-02 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d3b44721-ba8e-3fbe-89fc-edd5b05f7b6c | -11.9211 | -54.8322 | 2025-06-02 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 861b29fd-bc29-3515-abc9-3d34693f25df | -11.9211 | -54.8322 | 2025-06-02 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ec7427a4-5de1-3a94-8a71-c18a884becfb | -17.2639 | -42.6527 | 2025-06-02 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 01be98cd-db69-31a1-99d7-274c4b8a303a | -17.2439 | -42.6575 | 2025-06-02 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 16c76091-2aa2-362c-8f46-11f08487a982 | -17.26295 | -42.67018 | 2025-06-02 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a51bc934-5381-313a-8158-d483a67b4e03 | -17.27082 | -42.65879 | 2025-06-02 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| bd4ba879-f46c-3c32-ad62-21083a5f0046 | -17.27212 | -42.66878 | 2025-06-02 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a34fc823-5475-35ec-8108-a603df1a624e | -13.09293 | -45.26749 | 2025-06-02 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| fa963601-cd0f-3f02-ae56-affcb5e51cd5 | -16.03384 | -43.68253 | 2025-06-02 00:18:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39dbf970-e529-3b4d-9f7f-cd9c46b5ec92 | -13.0828 | -45.26884 | 2025-06-02 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 399690eb-4b7e-3a02-a76c-536e1096154e | -17.25378 | -42.67158 | 2025-06-02 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4191f57a-7d9a-3acb-8b4d-9103a81aaf9b | -13.10306 | -45.26614 | 2025-06-02 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| acec694c-289b-3897-befc-32479bbc3826 | -18.68464 | -46.99126 | 2025-06-02 00:18:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 9f8c7552-36f7-389e-8cf1-b91d1ae3caf6 | -17.25247 | -42.66146 | 2025-06-02 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 39221db4-fca2-374c-b647-915bb47f08c5 | -17.26165 | -42.66014 | 2025-06-02 00:18:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 667edbc7-c133-3d50-ac2a-00ca73bfd5dd | -17.2633 | -42.6775 | 2025-06-02 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ebe6d7f8-3f70-3276-bd10-be3f1740d16a | -11.9211 | -54.8322 | 2025-06-02 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8c596bf0-b8cd-3ff9-9606-38290ee9b3d2 | -17.2639 | -42.6527 | 2025-06-02 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 129.1 |
| de429371-750b-3bf6-9880-8cf9f3811590 | -7.01153 | -44.59816 | 2025-06-02 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ff8092cc-6dea-3c7e-984c-5a0def90ccc2 | -7.07475 | -44.93007 | 2025-06-02 00:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 94b2e271-77cc-3bb6-af54-617e7405d65e | -7.01028 | -44.58891 | 2025-06-02 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7591018b-40c6-3758-96a1-d1f09e2c8c74 | -7.07344 | -44.92037 | 2025-06-02 00:20:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a68eaca8-f037-3eb4-892f-06338596a227 | -8.77755 | -47.24178 | 2025-06-02 00:20:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7211a66a-c3a9-3f48-a92d-4257dddf809e | -5.92476 | -45.53635 | 2025-06-02 00:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 6ffbef54-f222-3cd4-88df-ca7cb98375d5 | -6.73365 | -42.91293 | 2025-06-02 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dee79cbb-c438-3f6c-bd78-f8d7a0be81e1 | -9.7865 | -37.00228 | 2025-06-02 00:20:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d8b271a6-ee99-347d-9b51-3bc2af2f9290 | -6.63802 | -43.21107 | 2025-06-02 00:20:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3ceb34fa-1d36-37a7-9492-993f1c06002a | -6.6368 | -43.20226 | 2025-06-02 00:20:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.3 |
| e8944a12-afdc-3d73-af67-cce3faf21790 | -10.54881 | -42.44273 | 2025-06-02 00:20:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 352113bc-b6ad-37ea-9a49-201bde0177f2 | -9.07513 | -47.15563 | 2025-06-02 00:20:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ea1a060e-d6e1-34a6-b9c8-eef2518e75f2 | -7.00373 | -44.60898 | 2025-06-02 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e092d50f-132d-35a3-a5c7-5fc4b6d05aee | -7.01279 | -44.60754 | 2025-06-02 00:20:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a878072f-c284-37dc-9b38-6c072fa83039 | -10.54758 | -42.43383 | 2025-06-02 00:20:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 724fa7f4-560a-39af-a82c-6b32c57b05fb | -9.1159 | -47.64638 | 2025-06-02 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 72d3056c-13ae-347e-a3d7-d17d5ecaeb22 | -5.92339 | -45.52635 | 2025-06-02 00:20:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| abd159a4-2356-38df-9b53-193c3f12df9e | -17.2639 | -42.6527 | 2025-06-02 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 1770283f-e284-32f5-b54a-bd3ac1f25325 | -17.2439 | -42.6575 | 2025-06-02 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5a11838f-11b3-3732-87b4-88530f6c355d | -17.2639 | -42.6527 | 2025-06-02 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 114.0 |
| f70590d3-36b8-36d2-be16-d17b0f19b0cc | -17.2639 | -42.6527 | 2025-06-02 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 29f3b9f8-1b7f-39de-8c26-1066beffb60a | -17.277901 | -42.647301 | 2025-06-02 00:51:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 108c466b-8412-3057-b85d-7bc03409e4c4 | -17.258499 | -42.652599 | 2025-06-02 00:51:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3be7d40a-3c95-3642-9334-e00cbe227756 | -17.271299 | -42.6619 | 2025-06-02 00:51:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed30bfc-c888-3321-a2f7-38df16eb16e6 | -13.3707 | -54.2631 | 2025-06-02 00:51:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a83fce1-3848-325f-bca3-fb2c4888c142 | -11.9161 | -54.829201 | 2025-06-02 00:51:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd6a60cf-9cb2-3149-9f88-154c09dc247b | -13.3685 | -54.252998 | 2025-06-02 00:51:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6be7f94-0c94-3a44-b5af-25ce2ed5d46a | -17.264601 | -42.676701 | 2025-06-02 00:51:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2c889089-3270-399a-ba13-8258e698ad73 | -11.9139 | -54.818699 | 2025-06-02 00:51:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11177f16-0122-3a1f-b3d2-c84a546a92e9 | -11.4524 | -55.004002 | 2025-06-02 00:51:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 388bc18a-561a-34dd-b0ff-d213b8d7c6e2 | -13.0938 | -45.2691 | 2025-06-02 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bca2e676-b343-3481-8443-a71ff5149ca6 | -11.9259 | -54.827099 | 2025-06-02 00:51:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4004992b-4b0d-396c-b3c3-8cdc730e90d9 | -9.4033 | -48.425201 | 2025-06-02 00:51:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88e216cf-9273-3ee9-8cfd-52ebd1267cd3 | -9.4941 | -40.322899 | 2025-06-02 00:51:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 96209cec-92e6-3aa3-a408-94089df91f35 | -18.6842 | -46.991501 | 2025-06-02 00:51:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2b85443-d008-3557-b8cd-ad6d56df1cf2 | -9.0741 | -47.1614 | 2025-06-02 00:51:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 672ee2a3-5a93-33d0-a118-5091c738294b | -10.8866 | -48.810902 | 2025-06-02 00:51:00 | METOP-C | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9095842-70bb-3c79-8e32-fdaf1842127a | -17.2616 | -42.6646 | 2025-06-02 00:51:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e38c1240-0c47-3dbf-906f-576d38e657f9 | -14.027 | -55.128399 | 2025-06-02 00:51:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43597132-193a-3dc6-81d7-7bfa2d4d52ba | -14.0148 | -55.118698 | 2025-06-02 00:51:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac64f42-303f-3d6d-94f0-ec2f592391bf | -5.9279 | -45.530998 | 2025-06-02 00:51:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6d004e7-be50-3bd9-bceb-1c3b7b773346 | -13.7105 | -52.908298 | 2025-06-02 00:51:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 67d8442a-c10f-3808-b1b7-afb994dd89d5 | -14.0246 | -55.116699 | 2025-06-02 00:51:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 640bc78b-acd5-357e-a718-ac502fd87129 | -9.0721 | -47.152901 | 2025-06-02 00:51:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf166996-1443-3212-8fe3-f6804fac9fa0 | -18.6859 | -46.998901 | 2025-06-02 00:51:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2b896873-b951-3986-951c-cd07b29288ef | -10.5551 | -42.434101 | 2025-06-02 00:51:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 78fe49ad-a1d5-30c1-bc1e-83a1e4af4631 | -17.281 | -42.659302 | 2025-06-02 00:51:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ba79fc5c-6ba5-365f-97e8-a1f535064db4 | -18.694 | -46.989101 | 2025-06-02 00:51:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b9554fb6-ec6d-3830-96d7-64932e9b8736 | -7.0133 | -44.609699 | 2025-06-02 00:51:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f18580c-ecd0-349a-a09d-cf81a29ad5cc | -11.9237 | -54.816601 | 2025-06-02 00:51:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 542f7838-ed46-336e-9b79-7a10246fa3f4 | -13.0914 | -45.259399 | 2025-06-02 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bcc69d0e-7e71-3828-8051-3b1e91716542 | -10.1469 | -52.140202 | 2025-06-02 00:51:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b04e93cf-ecca-3f05-acc2-2e07e5ec6708 | -17.2682 | -42.649899 | 2025-06-02 00:51:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7c3de61-79a2-3e50-994b-f0b360e325b2 | -10.8257 | -56.941002 | 2025-06-02 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49ddbf83-1aa6-3cc0-9d4e-e2905e911db2 | -11.9183 | -54.839699 | 2025-06-02 00:51:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c018df3f-bf14-35d5-9e87-90bd622cd2e1 | -17.284 | -42.6479 | 2025-06-02 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| be0f6c57-f9e9-3ea1-aa80-48ba30311190 | -17.2639 | -42.6527 | 2025-06-02 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 84.7 |
| d1ded584-46d2-3a44-8dcf-a853f43bbb56 | -17.284 | -42.6479 | 2025-06-02 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f2ecf608-34ca-34ed-a38d-801e41216030 | -17.2639 | -42.6527 | 2025-06-02 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 54ace939-6e5b-35f9-abeb-672c91134546 | -17.2639 | -42.6527 | 2025-06-02 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 0427e13a-da70-311a-bf2c-e40233787414 | -17.3041 | -42.643 | 2025-06-02 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 21f7cb0b-246a-3769-b272-d5afbb9b1ea4 | -17.284 | -42.6479 | 2025-06-02 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7a1147d1-8854-3b30-ac6a-74111b5848ab | -17.2639 | -42.6527 | 2025-06-02 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e7db72f4-5524-38e3-b1bc-f13ddca87d23 | -17.284 | -42.6479 | 2025-06-02 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7ba5764c-cb9c-3f86-971b-f0196707959d | -17.3041 | -42.643 | 2025-06-02 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 36fa1bab-2cee-3ccb-8661-3e1ff2d33a20 | -17.284 | -42.6479 | 2025-06-02 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 704788fb-fa1a-3990-9cdb-b5c6129b57d5 | -17.2639 | -42.6527 | 2025-06-02 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4405cbc8-cbef-3924-a2f7-78c87dc12de1 | -17.3041 | -42.643 | 2025-06-02 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7bff15fb-349e-3b77-9342-4d1e1cca7932 | -17.2639 | -42.6527 | 2025-06-02 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c36e10c2-af13-37c5-a706-aa6c1905901a | -17.3041 | -42.643 | 2025-06-02 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 92de783d-062a-31de-9dfb-0d9a8773e7bb | -17.284 | -42.6479 | 2025-06-02 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 107.6 |
| c98917aa-8b26-327f-af99-ef2badcf504f | -9.4 | -40.3722 | 2025-06-02 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 67d46165-0eda-3b2a-81ea-1e886b89e5e8 | -17.3041 | -42.643 | 2025-06-02 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6c731ec8-0bf6-3753-add4-9609055084a9 | -17.2639 | -42.6527 | 2025-06-02 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 5e360a00-98ee-3c6a-9dc9-450c548636f6 | -17.284 | -42.6479 | 2025-06-02 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 81a8ee69-2c2b-355f-8dfa-1420e03a3b31 | -17.284 | -42.6479 | 2025-06-02 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 95.5 |
| ed3e4a91-4351-33b9-abbb-2ead9fadb8c9 | -17.3041 | -42.643 | 2025-06-02 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f6636d05-b4fe-322d-a4b8-6b5b616e766c | -17.3041 | -42.643 | 2025-06-02 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 8ec42654-ca15-3525-bfcb-904cd2d1292c | -9.4964 | -40.3088 | 2025-06-02 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 33200a69-ac30-3b6a-a869-6698ab0df5ce | -17.284 | -42.6479 | 2025-06-02 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fa32bed3-08ff-34ca-976a-414fbe6173f9 | -17.284 | -42.6479 | 2025-06-02 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |


[Clique aqui para ver as próximas entradas](README2.md)
