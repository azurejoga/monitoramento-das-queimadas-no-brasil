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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf2d786e-5c07-3932-a690-f28e887f1570 | -19.5252 | -56.647598 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 925299fc-2b93-37bc-9dd0-be078b24d14e | -19.5317 | -56.677898 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 96bbdafc-f32c-3de4-b0cb-0c9d7823a6bf | -19.5333 | -56.685501 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c765037-7799-386a-947b-02bfe4dcb0fd | -19.534901 | -56.6931 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44b57d7a-98e5-3847-9e0f-1c567fbd0270 | -19.536501 | -56.700699 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87942616-d475-3047-ad83-3c47aaaf59de | -19.5058 | -56.6045 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 70a35040-be03-370f-8bff-179505146c03 | -19.507401 | -56.612 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c76041af-1234-37e7-91d1-e26826b2c8b3 | -19.512199 | -56.634701 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 81156750-c138-359e-affe-3537b2d55c79 | -19.5138 | -56.6423 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 63b33671-04ab-308b-b586-e1a518b9a747 | -19.5154 | -56.649899 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ef1fe674-7a01-38a9-b883-f11fba51f348 | -19.5235 | -56.687801 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 353728e0-69b6-3d73-b9c2-ba85d6a93b95 | -19.525101 | -56.6954 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 596a993a-4ec7-3aca-9d02-63e09db7a9ac | -19.526699 | -56.702999 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 21c5d633-7604-306f-b6d4-e782a5896198 | -19.505699 | -56.6521 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e974a9d1-0712-3e6b-aaf8-0e542d147f1b | -19.507299 | -56.659698 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 07960155-0256-3869-9b6f-9269566b78bf | -19.5154 | -56.697701 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f115cea0-c1e4-305c-90d3-ef75860b3aa5 | -19.517 | -56.705299 | 2024-10-31 01:23:08 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9c8d70bb-e874-30e9-85fe-92b9434832bd | -17.6015 | -52.389301 | 2024-10-31 01:23:23 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de2fe42e-bacc-3bd6-80c0-0e9719d0df31 | -17.599501 | -52.380798 | 2024-10-31 01:23:23 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c64cdcc1-115a-3e61-b695-ed7936d8382f | -17.6035 | -52.397701 | 2024-10-31 01:23:23 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 14629708-8947-3ebc-be12-dbdbaeab0ce7 | -18.295401 | -55.951302 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f3b7fd9d-a322-3327-812a-50c7133e873b | -18.297001 | -55.958599 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1a74046e-898b-3a89-a8a8-a4b54f2b4c1b | -18.284 | -55.9464 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72728a36-5e7b-34fb-af68-699de18668cf | -18.285601 | -55.953602 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 22353a3f-92aa-3122-b9c8-61af4dd1b2b2 | -18.287201 | -55.960899 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e70f2f0-9ca9-3c1c-ad8c-3b701d174d65 | -18.2903 | -55.9753 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3cdcaf36-5f68-3e5c-86c0-3368216d2296 | -18.291901 | -55.982601 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 30f3b860-d3ef-3f85-9f07-d83028bd8663 | -18.2938 | -55.944099 | 2024-10-31 01:23:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6a72b65d-e572-3c38-a9c6-6e3debca2eb4 | -18.084499 | -57.2108 | 2024-10-31 01:23:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 35a0e3ce-4a5d-364d-a9f8-b7074f32a161 | -17.8479 | -57.353001 | 2024-10-31 01:23:37 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 601ae536-52ca-306c-b584-22ed3b57c64b | -17.849501 | -57.3606 | 2024-10-31 01:23:37 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72d772c5-bd11-3abe-a5e7-311fc8ef9589 | -17.8512 | -57.368301 | 2024-10-31 01:23:37 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 64681c70-9ea0-3acd-9767-ab9d1f743d97 | -17.8528 | -57.3759 | 2024-10-31 01:23:37 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 23e19b06-17f6-3316-8997-c5642ef43ea8 | -17.8284 | -57.357399 | 2024-10-31 01:23:38 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b27b0280-f4ea-3e0d-a8a6-bcfae7d1d2c0 | -17.83 | -57.365002 | 2024-10-31 01:23:38 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41bf0bea-5169-38b9-9158-ea58e47323dc | -17.816999 | -57.352001 | 2024-10-31 01:23:38 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 87700e25-9f84-3957-9bf7-06d284253534 | -17.8186 | -57.3596 | 2024-10-31 01:23:38 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 425d9118-3600-313b-8b0f-9007001eaeae | -17.8381 | -57.355202 | 2024-10-31 01:23:38 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58352500-7c67-3945-a006-abcfde9bbd13 | -17.8398 | -57.362801 | 2024-10-31 01:23:38 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7e3201e4-056d-3e31-b8be-2c0b10621af1 | -17.8414 | -57.370499 | 2024-10-31 01:23:38 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 511aa644-4484-378b-9fd8-6eab1c3f2d5b | -17.7665 | -57.500301 | 2024-10-31 01:23:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8171585b-2f66-3eb4-9ec4-c42c5518aff9 | -17.7616 | -57.5257 | 2024-10-31 01:23:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 493c0902-20d8-3790-a1d4-6de65d2af351 | -17.763201 | -57.533501 | 2024-10-31 01:23:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77d82162-e2c2-31bc-b185-53ac96e22ec1 | -17.7649 | -57.541199 | 2024-10-31 01:23:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce52fbe7-f32d-363d-9e2b-6bdf4b945122 | -17.753401 | -57.535702 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 015509c0-d3dc-3025-b515-dd681ec764bb | -17.7551 | -57.5434 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 779b7c38-752a-30cc-83a0-3745ab7f3f6e | -17.710899 | -57.480598 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ef6bdfc-666b-31b9-9f4a-ca305c939b29 | -17.7125 | -57.4883 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17721a9e-646f-375f-98ac-f76a5321241c | -17.686399 | -57.462101 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3715e200-37a7-321e-b7c4-743ef3127649 | -17.688 | -57.4697 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ded3163-fe59-3c4d-ab71-1780df60d993 | -17.689699 | -57.477402 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59297e77-992c-3099-8451-376cc7a95117 | -17.691299 | -57.4851 | 2024-10-31 01:23:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f69e6ae8-717a-3f47-9303-c33344addfeb | -17.007099 | -54.800301 | 2024-10-31 01:23:42 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 514256df-8550-3502-9fd5-4806aeb0d69d | -17.008801 | -54.807499 | 2024-10-31 01:23:42 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f80b2b5d-738f-3004-9813-086fea1eb9d9 | -17.3111 | -57.4832 | 2024-10-31 01:23:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 626a7f4d-59c4-375e-8245-ab645db9a479 | -17.312799 | -57.490799 | 2024-10-31 01:23:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56aafdf2-772b-3436-9145-bd6028c6efda | -17.3013 | -57.485401 | 2024-10-31 01:23:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d76fffd9-5da7-3be5-ac8c-33c40cf73c1b | -17.302999 | -57.493 | 2024-10-31 01:23:47 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f2c2509-185c-3e10-9629-4f4800ba7fc8 | -16.4559 | -54.827301 | 2024-10-31 01:23:51 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4dc2b316-496e-3ea1-acea-782d2f306a4f | -16.8591 | -56.6759 | 2024-10-31 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76e5d6dc-61fe-3cac-be0d-6518a7376e7e | -16.860701 | -56.683102 | 2024-10-31 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10313182-3174-356e-a34f-50de1d9b91d7 | -16.862301 | -56.690399 | 2024-10-31 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c363a1f7-69ec-384d-afe0-13a74ad556c5 | -1.9684 | -47.9552 | 2024-10-31 01:25:17 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fa949eb1-b8e2-322d-bc93-3452c8a5a67d | -2.1718 | -47.9506 | 2024-10-31 01:25:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 84234a85-b443-3c4b-a29a-c09d910ee8eb | -2.5215 | -48.4806 | 2024-10-31 01:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e459e68a-a85e-33e3-a4fa-71886971160a | -2.5216 | -48.4591 | 2024-10-31 01:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 41c64d18-7fa7-3a38-8f26-6c2f863bb1c9 | -3.1787 | -50.5807 | 2024-10-31 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d8da93ff-04b0-3b67-94e7-fc5afe9c04d4 | -3.35 | -45.4447 | 2024-10-31 01:25:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8b591f70-8389-3cd6-bcdd-6730255d444b | -3.3502 | -45.4223 | 2024-10-31 01:25:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b2f622d4-52b8-389f-b575-fcd3737e6e4a | -3.3686 | -45.444 | 2024-10-31 01:25:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9cc40040-6acf-326f-91c5-b1ac9e338499 | -3.3688 | -45.4215 | 2024-10-31 01:25:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0c6ae810-7b1c-3321-b387-575c367be96f | -4.4969 | -46.4839 | 2024-10-31 01:25:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ef1a9545-702b-3a2a-b013-b0875b5a7955 | -4.6511 | -43.1104 | 2024-10-31 01:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 906e7e01-20f1-3eae-86f4-c96a6292008b | -5.0464 | -45.1768 | 2024-10-31 01:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 645d847f-d251-36f3-bf9f-92f0d92fdecf | -5.0466 | -45.1542 | 2024-10-31 01:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 65955b92-953c-3686-a836-864c4295a9aa | -6.1229 | -43.9578 | 2024-10-31 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 752b9ea2-4818-3911-a01e-c07a1d848547 | -6.1416 | -43.9563 | 2024-10-31 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 05b8b3bc-be1a-32df-b4a6-dadf647f2040 | -5.9788 | -45.3621 | 2024-10-31 01:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| afd796cd-12e2-3fd6-b057-ff65735031ec | -10.0118 | -64.8023 | 2024-10-31 01:26:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 534c20e6-c964-3b3b-b6b4-9f6b960c7d1e | -10.0444 | -64.777901 | 2024-10-31 01:26:10 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| faa9040f-6624-31db-88de-1e87bb53f3cc | -10.0346 | -64.7799 | 2024-10-31 01:26:10 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3b0a048-758d-30eb-86db-1176fc0ec8ac | -12.4433 | -43.7242 | 2024-10-31 01:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c1f47dee-b995-359d-84fc-35773a969d42 | -12.424 | -43.7274 | 2024-10-31 01:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| fb6ce9cb-7430-33cf-b361-589af3ffa51a | -2.9741 | -53.8703 | 2024-10-31 01:27:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4f8b47-1d34-3c09-a2cd-74534461e2ac | -2.9765 | -53.880699 | 2024-10-31 01:27:25 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e7657e-c20d-3a18-b903-cc921f9b9ba1 | -2.5367 | -54.112999 | 2024-10-31 01:27:33 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 303d4688-60a7-30b3-bb66-4d60a6371020 | -2.5391 | -54.123299 | 2024-10-31 01:27:33 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47c7a862-6d31-3c91-a724-43e1364ebc3c | -1.8713 | -52.1129 | 2024-10-31 01:27:36 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa32b2a8-4617-3539-b258-5cc50c0c6b3c | -2.2367 | -53.711399 | 2024-10-31 01:27:36 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a86c23-6bc8-314c-870f-702c3ee0a5df | -2.227 | -53.713699 | 2024-10-31 01:27:36 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 409aeadd-392f-3d59-aa5f-d22e4d2fa9ac | -1.4725 | -52.249699 | 2024-10-31 01:27:43 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| addb97c4-1fd8-30b9-979d-8a1529707ab6 | -1.4758 | -52.263802 | 2024-10-31 01:27:43 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34524027-60e4-34c5-91c4-0d0ddd6f169d | -1.466 | -52.265999 | 2024-10-31 01:27:43 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49935d30-4b0a-3b4c-a41f-50e26129e6df | -2.62 | -57.575901 | 2024-10-31 01:27:45 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6670430-4bae-31b4-ba51-ab09a509bd0b | -2.6216 | -57.583 | 2024-10-31 01:27:45 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03262638-7a9f-35af-bf66-0976cb12d7ca | -1.65 | -55.257301 | 2024-10-31 01:27:52 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14b0aedc-6a30-33a8-941b-94283bd55d0d | -0.793 | -62.875401 | 2024-10-31 01:28:34 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 708cbb95-c600-3818-bf76-8a19df4250de | -0.7949 | -62.8839 | 2024-10-31 01:28:34 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aae6605f-9ae6-354c-96c7-7757a0bd16fd | -0.7832 | -62.877602 | 2024-10-31 01:28:34 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7014247-1167-3210-b52a-d9858cf548ac | 1.6137 | -55.8367 | 2024-10-31 01:28:47 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
