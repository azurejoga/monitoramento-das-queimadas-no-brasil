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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6949e234-4111-3275-8033-8acda0196838 | -10.5757 | -64.0248 | 2024-10-05 00:36:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d82ced03-5af5-3e88-a581-07faf2b6ac6e | -10.5943 | -64.024 | 2024-10-05 00:36:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 1d1ed10e-2ba5-3d56-af09-2130d7072215 | -10.5945 | -64.0051 | 2024-10-05 00:36:07 | GOES-16 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f496bc9d-830e-3992-be76-a9556633c266 | -11.0966 | -54.2336 | 2024-10-05 00:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0270b919-0de6-34ec-9b60-b6d86ed34d0d | -11.1155 | -54.2319 | 2024-10-05 00:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8643bc97-1ad1-3911-b45d-bcfdb3e4cfca | -12.7623 | -50.5782 | 2024-10-05 00:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 16083f20-0548-306c-900b-82c8a38a1148 | -12.7627 | -50.5567 | 2024-10-05 00:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| f2a91817-7e62-3ce8-8f9f-21dc81f2e663 | -13.1543 | -51.1931 | 2024-10-05 00:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.2 |
| dbbd2fd0-84f9-3ba0-aa86-1be45ea547d8 | -13.3786 | -61.9582 | 2024-10-05 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7eade2c1-f747-39c4-b5e1-25111f78e4c4 | -13.3976 | -61.957 | 2024-10-05 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 477.3 |
| 31bbd439-aa6d-3782-a0d4-090c05abe324 | -13.3978 | -61.9376 | 2024-10-05 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 148.7 |
| c191e949-0d9a-3ec5-b69a-114094d02efe | -14.0517 | -46.362 | 2024-10-05 00:36:25 | GOES-16 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 78557f18-02f6-3d4e-a3c4-7a963c07e277 | -15.5597 | -57.4553 | 2024-10-05 00:36:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 725b4957-922d-3f27-abb4-b845c1a31262 | -15.5791 | -57.4532 | 2024-10-05 00:36:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| d3598056-32b2-3b63-b60a-1c2945cecbe0 | -15.7149 | -57.4388 | 2024-10-05 00:36:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e1bb74d3-9ace-3b4a-aaf6-483b0bfed431 | -15.7151 | -57.4184 | 2024-10-05 00:36:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 9bae5d3c-1d8d-3ef6-ac10-2b234f8d1c2d | -15.7346 | -57.4164 | 2024-10-05 00:36:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a98ae46b-4980-3db0-83e2-a500591b21ef | -16.554 | -57.2237 | 2024-10-05 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.6 |
| f09e5449-152e-3234-8b07-14e49be52f9c | -16.5544 | -57.2032 | 2024-10-05 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 46217610-4aa9-3f94-bb8f-7d4113126013 | -16.5736 | -57.2215 | 2024-10-05 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| d0eac25a-2bfe-3291-8434-36653c7f2577 | -16.5742 | -57.1805 | 2024-10-05 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 194.9 |
| 2e6d4b0e-400f-396b-a707-41a005c117e9 | -16.5745 | -57.16 | 2024-10-05 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 215.1 |
| bec6381b-bf12-3dba-85fc-a9a94089d1ba | -16.5938 | -57.1783 | 2024-10-05 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| b62ad9f3-af17-3733-9f0f-6ab38e4f0f3b | -16.5941 | -57.1578 | 2024-10-05 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 93ceb2d3-b001-3d02-b1bb-fa8e23d23a95 | -16.6598 | -55.5219 | 2024-10-05 00:36:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 8710ef82-04c9-3805-8884-58a6398e41c5 | -16.6871 | -57.4536 | 2024-10-05 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 605b01b1-744b-3e42-a623-985c62febb79 | -16.7455 | -57.4674 | 2024-10-05 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| f313491c-47c2-36b7-bdc4-75f4c71025be | -16.7647 | -57.4856 | 2024-10-05 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.7 |
| cce83548-747c-315e-8531-7e57ff8a879b | -16.765 | -57.4652 | 2024-10-05 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| e1bce6d8-4aaf-3212-a25e-5f52376c4dce | -16.7843 | -57.4834 | 2024-10-05 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 0d2178f1-6452-35f3-81af-f2b8d35fb903 | -17.0888 | -56.7915 | 2024-10-05 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| d12906aa-4821-30ce-b02e-5185e357aaf3 | -17.0892 | -56.7709 | 2024-10-05 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.2 |
| d9e9e4e4-ec96-3103-aed1-980613540a01 | -17.1085 | -56.7892 | 2024-10-05 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 6346b2e3-7b30-3422-bf41-90ce32346154 | -17.1178 | -57.4244 | 2024-10-05 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 150.4 |
| 0a740a08-1e5e-371b-b7bc-13543afcd0a3 | -17.1182 | -57.4039 | 2024-10-05 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 240.7 |
| 87571c1c-dce4-3e28-9fed-344ef4dc8186 | -17.1185 | -57.3834 | 2024-10-05 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| 8052aadd-1ced-3da7-b307-80e423b0e942 | -17.1375 | -57.4221 | 2024-10-05 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.3 |
| f86a0254-2e6c-3f9f-82d2-714e0c2f661d | -17.1378 | -57.4016 | 2024-10-05 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 274.0 |
| 0318c3f0-31f4-314a-bcca-b06592c3b7d6 | -17.1381 | -57.381 | 2024-10-05 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.1 |
| 42b06653-0b41-3a29-be61-8b3e60b71748 | -18.2985 | -54.2231 | 2024-10-05 00:36:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 57eb74d5-0ada-3ee8-8c19-5951d4c85665 | -18.4867 | -52.8009 | 2024-10-05 00:36:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 02c5da37-7e5e-32d4-8f20-4fbf0f852aff | -18.4872 | -52.7792 | 2024-10-05 00:36:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b49799a9-bb2b-38a1-b80c-8724c7a5602a | -18.8809 | -43.6032 | 2024-10-05 00:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| 6c04446e-456e-3340-9592-0b84db29ee08 | -18.8816 | -43.5785 | 2024-10-05 00:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.8 |
| 062c5408-9926-32a2-9e13-2cd4206bca90 | -18.6582 | -57.2967 | 2024-10-05 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| b69e0c4e-d77a-3ce3-94d4-c87a8bbc0b24 | -18.6586 | -57.2759 | 2024-10-05 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| e7bf449d-765d-3842-b4f8-0f165711ab2a | -18.6782 | -57.2941 | 2024-10-05 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 9f80cc8b-3f89-3fab-b6fc-00c5a8abcc3c | -18.6785 | -57.2734 | 2024-10-05 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.8 |
| b34a6818-404b-3833-80f1-54627ae5604d | -19.0156 | -43.15 | 2024-10-05 00:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 837e0690-8638-36f5-b520-107398db096a | -18.6981 | -57.2915 | 2024-10-05 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 933e05ce-b479-36db-83cb-b1d82417f5ef | -19.0944 | -48.2415 | 2024-10-05 00:36:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6707dd9e-5a9f-3bd0-99a7-a98eec7f9271 | -19.1576 | -46.6279 | 2024-10-05 00:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 143.9 |
| c151fbc1-68fb-35f3-8908-5bc1f17ba65f | -19.1583 | -46.6043 | 2024-10-05 00:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 90ccb8ce-e275-3fb5-975c-dc13934efcc8 | -20.5904 | -51.3907 | 2024-10-05 00:37:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.8 |
| 4e530f39-8d0c-3311-a83a-281d49cbdce5 | -20.7901 | -47.7465 | 2024-10-05 00:37:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e5be034a-c3cd-3372-8633-ac2680daa4da | -20.9385 | -49.0098 | 2024-10-05 00:37:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.0 |
| 3662f2b9-ea58-3417-8038-09239dc8fb33 | -21.7878 | -48.7442 | 2024-10-05 00:37:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 10c989e6-c4c6-37a3-9b65-ba842709455b | -21.8079 | -48.7626 | 2024-10-05 00:37:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 82c48b73-4895-3a94-9d1e-34120b1ff4f8 | -21.8086 | -48.7392 | 2024-10-05 00:37:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 275.0 |
| aece325b-f2c5-3c71-9b3c-2b8e2d0bef84 | -1.1942 | -46.5935 | 2024-10-05 00:45:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8e3e977f-4520-3799-b1cc-d54ec31ef548 | -2.8829 | -50.7147 | 2024-10-05 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d71cf90e-04ba-3a8f-ad0d-6a825094ecfe | -2.9014 | -50.7142 | 2024-10-05 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 630e4a54-2752-3004-a1a7-53449fa2b081 | -2.9015 | -50.6933 | 2024-10-05 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9b173bb6-4b05-310c-b5ae-9e8535ac05f7 | -3.2349 | -50.3695 | 2024-10-05 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 697f295a-9512-36c1-9b44-6ead929f49ee | -3.239 | -49.3986 | 2024-10-05 00:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a0ac3c04-1ef4-3b1e-ad4c-5b74dd730f55 | -3.2899 | -50.4725 | 2024-10-05 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ed27a230-efca-3ba6-bfd8-e1fb1a449c5e | -3.2899 | -50.4516 | 2024-10-05 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| aac8e313-07ec-3dd3-8ada-04858851e98e | -3.3083 | -50.4719 | 2024-10-05 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| a3f7f1e5-57a7-3d8b-8626-3141f28c9ff2 | -3.3084 | -50.451 | 2024-10-05 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| a7df1059-cc07-327f-a869-b0e778d5869d | -3.3127 | -49.4599 | 2024-10-05 00:45:25 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| f9e6d834-b0e2-324b-aad8-edd96a446eb6 | -3.3269 | -50.4504 | 2024-10-05 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 978c64a9-7146-3128-a989-03b829879bc0 | -3.5994 | -47.5359 | 2024-10-05 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 2773aaa2-2241-30f0-89c4-5d78c86e431e | -3.5995 | -47.5142 | 2024-10-05 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 924d9630-146e-3a2d-9210-4cc5149751d2 | -3.618 | -47.5352 | 2024-10-05 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 0d8fa9b3-9f22-381b-8242-b6d02f708be4 | -3.6181 | -47.5134 | 2024-10-05 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 159e7bff-15dd-3485-8183-541f125be307 | -4.0148 | -43.2408 | 2024-10-05 00:45:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c31837a3-db5c-3f87-995c-e47a5ff813a4 | -4.0793 | -47.9719 | 2024-10-05 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 83df9b01-01cf-3eda-9dfa-0d70dad08dcc | -4.0794 | -47.9502 | 2024-10-05 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 4c48de12-b5b6-3dc1-8d76-3d3c4152880b | -4.0795 | -47.9285 | 2024-10-05 00:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d7e83f22-5d65-3b6d-ae00-4ae5ebe880c2 | -5.3911 | -46.4322 | 2024-10-05 00:45:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 56ff80d2-01cb-34e6-a0d4-bf4a1f698f44 | -5.8214 | -44.1426 | 2024-10-05 00:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 9c7d66f4-f489-3b81-ba76-b7a379580e52 | -5.8216 | -44.1196 | 2024-10-05 00:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 6c7a08ab-0fa0-3285-a0c3-37a8b2a4a62e | -5.9155 | -53.4356 | 2024-10-05 00:45:40 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ca2c033f-1a97-36ef-946c-63c016e3f74d | -6.1838 | -45.4371 | 2024-10-05 00:45:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e1d55793-e6a4-3f85-8883-d5c3ae729f1d | -6.9514 | -59.0666 | 2024-10-05 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 674f6ff5-8606-37fc-aa8f-ea12082db8df | -7.0233 | -59.3918 | 2024-10-05 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0222b45c-a1ab-3f88-a5a9-6b87e082b5cb | -7.7362 | -49.2297 | 2024-10-05 00:45:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 6a5d9690-c3de-33f7-b516-34110e6eb9f7 | -7.7364 | -49.2082 | 2024-10-05 00:45:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 172.7 |
| 740928e3-3181-32bc-9891-fea278ac6898 | -7.7549 | -49.2282 | 2024-10-05 00:45:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| a48ecfc5-b2a8-3af6-8fb8-9df1b62f43da | -7.7551 | -49.2067 | 2024-10-05 00:45:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 28299122-bf29-3ad6-926f-1b5e91109f29 | -8.2323 | -61.2205 | 2024-10-05 00:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e54ee68c-32e5-3889-8f5f-26ddfd9a72fb | -8.7655 | -44.8106 | 2024-10-05 00:45:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| baf1c38d-350b-3568-828b-b165b049e723 | -8.6367 | -49.11 | 2024-10-05 00:45:55 | GOES-16 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3091669e-c6f7-3c27-9df7-7e70c5184e05 | -8.6555 | -49.1083 | 2024-10-05 00:45:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 086bbcc2-3086-353a-ac21-ef8fdb44d3b1 | -8.6558 | -49.0868 | 2024-10-05 00:45:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 91c10951-4e3b-3004-894d-a287e0346261 | -8.7769 | -49.9763 | 2024-10-05 00:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 062bbbd1-014f-33c2-84f1-9e4dc484b87f | -8.7772 | -49.955 | 2024-10-05 00:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 75c65109-ca56-3747-878a-50461391950b | -8.7957 | -49.9747 | 2024-10-05 00:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ac4f66ed-2747-3566-841d-f0a6a80d91ce | -8.7959 | -49.9533 | 2024-10-05 00:45:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e938ed3e-7c92-33e8-ad9e-3e3e38018554 | -10.4424 | -50.7336 | 2024-10-05 00:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |


[Clique aqui para ver as próximas entradas](README13.md)
