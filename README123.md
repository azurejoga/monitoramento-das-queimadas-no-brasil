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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71d6b23e-5070-3570-a253-426eef021c28 | -11.98689 | -51.90005 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ceb7a56c-80e3-3984-82fb-4ba52ef1010e | -11.98621 | -51.90413 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 285af174-e9bd-3f92-82cd-1e34e1a6d757 | -11.98265 | -51.90349 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6082916-f979-3d3c-b3f8-9b760f96e811 | -11.97909 | -51.90285 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebd44201-0e7a-321b-a6b9-21679d205c51 | -11.97553 | -51.90222 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ef0a766-a63f-323d-9215-bf1b80a1380a | -11.97128 | -51.90567 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e5e1b47-165b-34f5-9ce5-f07410a8d84f | -11.35414 | -50.8154 | 2024-10-04 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ced82c6e-6f6c-36e2-a432-536b13df73ab | -13.32718 | -51.35462 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ae6ff1e-16ff-3925-ad33-89071772571d | -13.27699 | -51.25191 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 376bfedb-16d7-303d-9518-65f4ac8ac0df | -13.27636 | -51.2557 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dc33a47-700f-3ccf-9ecb-9df21445d870 | -13.27293 | -51.25512 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ba12670-7d74-38de-91d7-46d5772b86d7 | -13.2695 | -51.25453 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 503c3d3e-82ab-3128-8789-0af244f4742a | -13.26543 | -51.25774 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f1c811-aaae-30d9-aa7a-ede83c3af014 | -13.26468 | -51.22713 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a33373-fcfc-3ef1-9fed-d4d625de2a26 | -13.26316 | -51.25812 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a8b2680-2eef-3e63-a347-9d4e9458d4a6 | -13.262 | -51.25715 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0477aea6-9a72-3054-9ec4-0b06f6180d05 | -13.26035 | -51.25372 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0d74683-b1e8-3ee8-bc3d-0dd0418e529f | -13.25692 | -51.25313 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0140caa7-8831-3919-a662-d94eece6002f | -13.2541 | -51.24874 | 2024-10-04 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0d398ef-20c3-332b-aa5d-725a1da43364 | -13.18328 | -51.22873 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7988037-4021-34ff-8fc9-7dc9f65a7d2c | -13.16193 | -51.21384 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d92eff3-b267-3847-957e-32425542839f | -13.16115 | -51.21321 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4c4b058-5d15-3225-9811-58bf4fdfe8bd | -13.16052 | -51.21701 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3174369-9be7-3216-bf4a-fb6a4b53bd8f | -13.1585 | -51.21325 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ee2c1bb-da42-3532-a5db-03ae19983a42 | -13.15789 | -51.21704 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4cf7734-bbf9-3eaa-a8ab-281b4094e2d0 | -13.14321 | -51.19892 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a84b22ad-36b8-319e-b742-1883ba8182ed | -13.13978 | -51.19833 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e3054f6-7fef-3d3c-aa7e-dc579a951c56 | -13.1336 | -51.42065 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa23e02e-01de-3513-83c0-3d0b0bbda037 | -13.05093 | -51.30831 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a96f4a8b-c495-35b8-84c7-4b080ad56730 | -13.04748 | -51.30771 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ee82ec-0575-3894-80d5-6e65e9ae2295 | -12.91022 | -51.2774 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8adaf856-da2e-365b-9a25-63fa514255d0 | -12.9096 | -51.28122 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca28ad0f-d29f-3186-8815-a8ddd000e0ae | -12.73363 | -51.97117 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9888d63c-e598-3fea-9b95-79aa5edc9fd7 | -12.7334 | -51.92951 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e331f516-befd-36b3-807c-31687eea1f0e | -12.73295 | -51.97525 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20f05ad2-12ac-399d-af32-7c456339fbb8 | -12.73225 | -51.97932 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20413d1f-abdc-3606-acc8-27c6122f85f0 | -12.72802 | -51.98277 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d101fdc-8162-3f78-b83b-66d18c7d9447 | -12.72734 | -51.98681 | 2024-10-04 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11e0feb4-7856-3002-9459-cd1740b9ba6b | -13.81859 | -52.44251 | 2024-10-04 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c91fec24-8108-34d1-84cd-dec8e1ee93a8 | -13.81501 | -52.44189 | 2024-10-04 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9733fe78-2387-3c39-b8e7-f94fd76a9f67 | -13.81143 | -52.44127 | 2024-10-04 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89f2ee0b-b222-31ad-b559-f819ff631a6e | -10.63475 | -53.69871 | 2024-10-04 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66f6b761-95af-3f8f-9eaf-410818118946 | -10.63135 | -53.69445 | 2024-10-04 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d17a626a-7b1a-3a91-89e2-2e3258400616 | -10.9228 | -52.42135 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9d3a5fc-42b6-31e8-a235-15ebb5c26249 | -10.92204 | -52.4258 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c79b24fc-6563-3e15-8497-be44bf23b66d | -10.92044 | -52.45747 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce0b98ab-3730-3eed-825a-ad10287de7d0 | -10.91985 | -52.41629 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c2c3b5-bbcd-39d9-ab85-6778d3c66960 | -10.9191 | -52.4207 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e9585ec-ec95-3ef3-9ca4-b104f7e31c9d | -10.91834 | -52.42513 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62e9bfc2-b00f-394f-8900-8f28fb54f373 | -10.91824 | -52.44796 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a3ebe23-c4a5-30c6-8e3f-06de0f956c54 | -10.91749 | -52.45238 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9fc1012-39b9-3760-9f9c-b900a01d5071 | -10.91673 | -52.45681 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ad13f9e-d70a-3828-92b2-d8bfc0f1c075 | -10.91615 | -52.41564 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ff32048-0c5b-3534-b0e9-6c1892e9180c | -10.91605 | -52.4385 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b7c446f-d75b-3364-b020-7f5667979cf5 | -10.9154 | -52.42003 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adfdb80a-2756-3b93-820b-1b82fc38dd6b | -10.91529 | -52.4429 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22bafb8d-edec-3fb9-8c03-19d8784d2258 | -10.91472 | -52.40175 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fca5e296-dcc1-31c3-a125-cf74cc78390f | -10.91464 | -52.42447 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a02414c0-a948-3e75-b306-5ff4376e9940 | -10.91454 | -52.4473 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b980be0-4538-3ed3-8cc2-0c8379e63f28 | -10.91396 | -52.40616 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35720809-627e-33c4-a7d6-076556745ae5 | -10.91387 | -52.42892 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7a6850b-53f6-30e9-bcd3-d995224289b6 | -10.91321 | -52.41058 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08b1e358-9639-325f-a231-829168e2784e | -10.91311 | -52.43338 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfde2129-bc86-3fc2-9462-5ee9ac9eb5e9 | -10.91245 | -52.41499 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b79593-4c08-3da6-bd5d-171b53b6b3d0 | -10.91234 | -52.43785 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ec77987-05da-3387-bf0a-97db3068c9f3 | -10.91169 | -52.41939 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 233078af-9205-3c80-8f2e-46fdec2c8632 | -10.91102 | -52.4011 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 903c27c2-b8f8-3021-907f-727e8b8a8135 | -10.91093 | -52.42382 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec25148b-640f-3842-bca3-df8152cc69ed | -10.91027 | -52.40551 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0a3d10f-6707-39c2-a53a-6be0f8430f38 | -10.91017 | -52.42828 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 847c3ab7-fa08-312c-8a3d-e0f723426cba | -10.9094 | -52.43275 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5052cee-9ea7-3918-929a-1e00fac41b16 | -10.90931 | -52.40306 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8e3c60e-7182-3cfd-9399-27f98eab9d62 | -10.90863 | -52.43722 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09f1ed24-bbf1-353a-831a-279cc1c8fa92 | -10.90733 | -52.40045 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b79ba238-80c1-3c04-8a50-9fd30c81b5c9 | -10.90657 | -52.40486 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5e176d8-ea97-3d23-af08-3da515160059 | -10.90569 | -52.43213 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a744c80e-217c-33d0-8a44-ff50e4b5b130 | -10.90561 | -52.4024 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 412c5e7e-5c50-3504-9999-cb7e125318a7 | -10.90492 | -52.43659 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc88711-b683-32b0-8749-e97cdfcb32ce | -10.90489 | -52.4297 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ab6d8f1-a69c-3076-a568-a9184a4012e7 | -10.90415 | -52.43418 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 212270fc-7145-3e54-acda-f40c93e58700 | -10.90287 | -52.40421 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2b77417-e7ff-38a8-ae4b-8854180988ee | -10.90198 | -52.4315 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 548c719f-49ae-30d2-9d28-b3c5364f81eb | -10.90119 | -52.42907 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a91d26a-cb08-33f8-a05f-5bd55ea94fb7 | -10.90118 | -52.40615 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00f35f4d-5994-3af5-ab47-67af621781e9 | -10.89917 | -52.40354 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52fb0a47-9d77-36bf-a888-ae459f48258c | -10.89827 | -52.43088 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c0c3b4a-7b7b-3e44-8ac2-b939ee6eb62e | -10.89822 | -52.40107 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3b4e78c-255a-347d-9e41-8687b86c8c22 | -10.89748 | -52.42844 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc46b07-8366-35a9-a6ae-4e6290db1086 | -10.89748 | -52.40549 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bd5ceee-f485-3433-9c71-bc382def2f92 | -10.89452 | -52.40042 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dbe25ee-84f1-3a45-9217-4159de0121eb | -10.89378 | -52.40484 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8744e8b-8a1a-3343-9d86-7a5a42c28606 | -10.89008 | -52.40421 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f52d03cc-3137-3711-8a2b-3ef609ce9fc7 | -10.88933 | -52.40867 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6c18060-c536-35f9-80f8-3e967c7d70d2 | -10.87377 | -52.41059 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b98d8f8-8e17-3afb-a5aa-b8fa8a2c70f4 | -10.87302 | -52.41503 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b25aea82-0e88-3adb-a63c-901cb39a25fe | -10.69235 | -53.04037 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37923fd0-dc7a-3d43-a7ca-bc09dc54d376 | -10.6915 | -53.04521 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a82bb7f7-3834-3b11-96b6-db6ef0a48bff | -10.69044 | -53.04275 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3fc68e0-87d0-3970-a917-3af3a4a9b2d5 | -10.6885 | -53.03969 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36bbf8c7-b65f-3e90-b9ed-930074a7ee7e | -10.6866 | -53.04206 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README124.md)
