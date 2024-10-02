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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0889719-d019-3af3-ab78-144b2f6daa15 | -11.5564 | -63.774502 | 2024-10-02 01:25:46 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2116522f-09c6-3719-8c6f-13ced91f65a4 | -11.5593 | -63.788399 | 2024-10-02 01:25:46 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a74b773e-1d93-378f-832a-a39ad0c98a28 | -11.5426 | -63.8064 | 2024-10-02 01:25:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50ddf217-c0b9-3a42-a42e-92305de56edb | -11.5455 | -63.8204 | 2024-10-02 01:25:47 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd7e10cd-9e57-3d3e-8711-3c0fccff8a81 | -11.6678 | -64.979301 | 2024-10-02 01:25:48 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6296d5f2-dbc2-3437-8cb6-fd239abe03d3 | -11.6711 | -64.996201 | 2024-10-02 01:25:48 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff986147-0e4d-377f-b5e3-c0640cf119ad | -7.7129 | -42.995 | 2024-10-02 01:25:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 3b40b42b-d07e-3fcf-af66-c15594631b8f | -8.9616 | -52.811001 | 2024-10-02 01:25:49 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 540d2846-aaaf-3fd1-aff9-eebcb63b2383 | -11.6546 | -64.964401 | 2024-10-02 01:25:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99f4c421-df01-3b8f-bb1d-eecfb58c2020 | -11.658 | -64.9813 | 2024-10-02 01:25:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f380fe67-bd4c-345a-b2b6-800b32f2fb80 | -11.6613 | -64.998199 | 2024-10-02 01:25:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7618bd3-e1ec-34b0-b0c1-36619616c25f | -11.6647 | -65.015198 | 2024-10-02 01:25:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b713945-4817-316b-add8-378014c4a36b | -11.6483 | -64.9832 | 2024-10-02 01:25:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3ac99b5-1261-36a3-aed3-9de9fdcf8349 | -11.6516 | -65.000099 | 2024-10-02 01:25:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b380c60b-1dee-3fab-a85c-369256f32ea7 | -11.655 | -65.017097 | 2024-10-02 01:25:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5f71af1-494e-352d-a9e0-eef995c06985 | -11.6053 | -65.224403 | 2024-10-02 01:25:50 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12358ece-fdbc-3e3c-a123-113bb06ae829 | -8.205 | -44.365 | 2024-10-02 01:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| bd8b9612-7a40-392c-a125-af0e38e6681b | -8.2053 | -44.3419 | 2024-10-02 01:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 764ec13d-7e73-327f-b923-bec38f62c0e7 | -8.4756 | -46.8498 | 2024-10-02 01:25:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 84024260-a597-3f0e-ad1d-85196c5aa5ec | -8.4944 | -46.8479 | 2024-10-02 01:25:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 14b19052-71b6-30b8-87aa-feac0a79331b | -8.4643 | -62.7124 | 2024-10-02 01:25:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| df27f576-ced8-3723-b4e1-92824caa0f56 | -7.17 | -46.927898 | 2024-10-02 01:25:54 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 697adbc8-bc12-3305-b343-371b406c9e6c | -7.1769 | -46.9543 | 2024-10-02 01:25:54 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31d0c039-b09b-3f63-b961-5cf1b6516f06 | -7.1673 | -46.956799 | 2024-10-02 01:25:54 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f2fa3d1-b367-3618-9b4b-402c084b228f | -10.9895 | -63.933998 | 2024-10-02 01:25:56 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb8fdd3b-e496-3af9-b509-aa1d71aa5569 | -10.9798 | -63.936001 | 2024-10-02 01:25:56 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f710f1e2-fa97-357e-98a9-e5e8682644f0 | -10.9827 | -63.950001 | 2024-10-02 01:25:56 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de7bc4bd-5efe-39bd-ad91-1c1c11e52042 | -10.6323 | -62.800499 | 2024-10-02 01:25:58 | METOP-C | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2f9d917-829e-3d0e-9b7b-78d7153e3c60 | -10.6347 | -62.812099 | 2024-10-02 01:25:58 | METOP-C | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7179564-f4cc-3820-8012-27b32d43982d | -9.9277 | -59.899799 | 2024-10-02 01:25:59 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfeed71f-6e30-3d03-b928-73a52478bfe0 | -9.9329 | -59.923401 | 2024-10-02 01:25:59 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05af88e6-cbba-3fbc-8b9a-2a4f2fff21da | -16.46391 | -57.36087 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| c974fe7e-803a-3210-bb20-14acc73c3cbc | -16.46539 | -57.37255 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| da134a04-6636-33c8-a553-bff24cd5c339 | -16.4679 | -57.31293 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| b02e15d8-9892-3020-8b05-288ff361582c | -16.46938 | -57.32454 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.4 |
| 5cf5dac8-4802-35fd-b4cf-eb4022dd3935 | -16.4743 | -57.44302 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 18d93c07-789f-3700-a94e-959ae09f6fca | -16.47632 | -57.3 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 5798e9fc-e009-3cf0-8f07-4d7823d11065 | -16.4778 | -57.31158 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 6802d51e-7b87-326e-941e-6cca6562d4e6 | -16.47816 | -57.30512 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.3 |
| ec524c29-7dba-355d-b681-334dff72fc7d | -16.47958 | -57.31674 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| f00c8844-8c65-3161-afd0-d3dd8081b7e6 | -16.48663 | -57.29216 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| f4a52469-f61a-354f-95c7-50351157fb5e | -16.48806 | -57.30376 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 1e35cc3d-4210-3173-8c3d-7a42e01de457 | -16.48949 | -57.31539 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 98a71f6a-7374-35a1-890c-32fa8d2a5573 | -16.4994 | -57.31404 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| f502b2a3-8bb5-3f92-9790-05d706854fd0 | -16.50643 | -57.2895 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| bd61bb7f-32a9-3dc0-9d70-da35a6e6c27b | -16.50787 | -57.3011 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 41b500ba-7adf-3125-b476-9cf84edd4bc7 | -16.50931 | -57.31271 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 55e04f1b-827b-3c8c-a888-87d7110338c7 | -16.51632 | -57.28817 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| d2f6093e-aa68-3a91-9c78-500a03ad3023 | -16.51777 | -57.29976 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 561c125f-a590-3cd6-a27e-cb0c1560f97b | -16.52622 | -57.2868 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 4f9fa237-ad2c-3326-a63d-ce6566db71f9 | -16.52767 | -57.29841 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.1 |
| e7eba203-3033-3165-9f3c-ec6d9f23da14 | -15.90041 | -57.18196 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 444b4468-ed04-3520-9291-0d042e85c43e | -15.91438 | -57.44769 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1f009e2d-9cde-37b9-916e-2988925fe036 | -16.09795 | -57.52887 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b9d16773-c487-3a60-942d-2adeeafac08b | -16.57599 | -57.27425 | 2024-10-02 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 4417a0d6-5b06-3daf-a8e4-093926801ffc | -16.61121 | -57.23413 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| d7d67010-a914-3fb7-aa5b-78965601c885 | -16.61266 | -57.24567 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| f0009f5b-f6bd-366d-9306-1b6fd5b4d45e | -16.62108 | -57.23278 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 6fe06758-81e1-3402-8376-64542e8f83ad | -16.62287 | -57.32706 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 1bad853f-08a5-32b5-b4b1-3da9134b84cb | -13.10769 | -56.42745 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20611295-8cea-378d-b989-5403f0f16a13 | -14.5708 | -44.83379 | 2024-10-02 01:26:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 116.4 |
| e22a8f2a-2f64-31b6-b4d4-357211cd2080 | -14.56098 | -44.8289 | 2024-10-02 01:26:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4e3e5836-109d-32c5-b344-e1ab925fdf6d | -12.29788 | -47.64304 | 2024-10-02 01:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 22de03e6-0cbe-3c8c-a878-4d209656de2a | -12.29421 | -47.66125 | 2024-10-02 01:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 76171a2e-cd1a-31a3-befc-399411cbf698 | -12.29017 | -47.63778 | 2024-10-02 01:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 9d02df3e-5ca2-37d1-a173-dd9186eaa656 | -12.28805 | -47.66906 | 2024-10-02 01:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c14bc08d-a73a-3a49-bc6b-631d3d5b9b5d | -12.28418 | -47.64561 | 2024-10-02 01:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| b625a9c5-9d50-3234-93ad-0ab813f402cb | -12.28052 | -47.66376 | 2024-10-02 01:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 1dbf833d-b3dd-3ac1-89b2-bd493c08b966 | -12.27647 | -47.64041 | 2024-10-02 01:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| af35f0a0-1dd2-3279-9c69-2df16d8515cc | -15.20092 | -47.95076 | 2024-10-02 01:26:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 50966f00-e07e-3bf5-8f84-167a0e2d8dd6 | -15.20089 | -47.94516 | 2024-10-02 01:26:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| be0d2117-0373-3cf8-8671-6ff60f00899f | -10.71308 | -48.73666 | 2024-10-02 01:26:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3e64c45a-59b5-3e34-a8d5-d1e56126873d | -10.71222 | -48.72269 | 2024-10-02 01:26:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ce1f92fd-b146-36e8-a43b-0aca1eb865d2 | -10.55733 | -48.02211 | 2024-10-02 01:26:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ee0d4906-30fa-3be9-84ba-652a0f09397f | -13.7613 | -48.31406 | 2024-10-02 01:26:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| af1326a6-02b5-3803-bd4e-323277208711 | -13.74852 | -48.31553 | 2024-10-02 01:26:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c1df1162-1c7d-3076-beea-25a27799f5fa | -13.20883 | -48.62661 | 2024-10-02 01:26:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |
| bd11955f-69dc-3c0a-ab2c-23d39ba8f323 | -13.20562 | -48.6075 | 2024-10-02 01:26:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 42.3 |
| dc07eea0-d974-360d-a800-1d281121b3ba | -13.23983 | -48.58101 | 2024-10-02 01:26:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e780f9a4-20b6-3634-b031-5b98bdfd3edc | -13.23681 | -48.56268 | 2024-10-02 01:26:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 93dd88d7-1fd1-3294-8a9b-a22a7d6fd5a5 | -13.22728 | -48.58298 | 2024-10-02 01:26:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 0da41106-8c79-378d-8783-ee242c971578 | -13.22422 | -48.56455 | 2024-10-02 01:26:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 0847eb79-2c00-30a7-8f13-978fdf29b54e | -14.81483 | -48.781 | 2024-10-02 01:26:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 935e4120-3391-3993-85e0-cffe9c859313 | -14.81308 | -49.05993 | 2024-10-02 01:26:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| fb1042a4-4ff3-3dad-a0b6-bf0a7bf3668b | -14.81169 | -48.7622 | 2024-10-02 01:26:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| b841a26f-f38d-3a81-bc77-a7472cbb0291 | -14.80623 | -49.06672 | 2024-10-02 01:26:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 02025eb3-54bc-316c-aa34-81eb595c3c38 | -14.80354 | -49.05014 | 2024-10-02 01:26:00 | TERRA_M-M | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dac7552b-f31e-3540-8725-15970934949d | -14.80299 | -48.78373 | 2024-10-02 01:26:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 38081200-aa6f-3f60-a3aa-31b5c2431686 | -14.74988 | -48.79657 | 2024-10-02 01:26:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b2f9af5f-9ef8-39d4-9e1a-54eb5c19d98d | -15.107 | -49.50311 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 45d17fc7-e6f3-31d6-bbcb-37a9fee00965 | -15.10449 | -49.48781 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e9e54b51-2034-3228-8af7-58de03e73e49 | -15.09582 | -49.50541 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 35.8 |
| e3b0597a-d2b1-3cab-ae93-4e60ab7c7d7c | -15.09327 | -49.48998 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| de7db57d-764d-3cf4-9a48-055dab983e6c | -14.8432 | -49.29493 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 9caf80b9-86c1-3e8d-b660-82ac91d86577 | -14.84058 | -49.27868 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1931531c-3c7f-3293-ab98-b06f96102061 | -15.796 | -48.84384 | 2024-10-02 01:26:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 454e9e49-e292-3c55-b694-616d9dc9eea3 | -15.79414 | -48.8544 | 2024-10-02 01:26:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9a05ba7b-7969-3043-ba79-25e75da6130b | -16.09923 | -50.29878 | 2024-10-02 01:26:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 73426c4f-c1d0-3d4c-a228-d3ca99890e82 | -15.9178 | -50.14703 | 2024-10-02 01:26:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1ff0e0b8-c3cf-396b-84e2-9e9c7cd3d41f | -15.9135 | -50.15402 | 2024-10-02 01:26:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README33.md)
