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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 416bb5c8-b2c6-32a5-ab27-f136934f0991 | -9.28509 | -60.81647 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 507881c2-34de-3fed-9532-ab3c89f44d0d | -9.28454 | -60.81997 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27758cdc-c5c6-3ddd-9dd4-19d3da94f8cc | -9.28341 | -60.80545 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65b194d0-263d-3344-a3c9-d38a1bc816fb | -9.26953 | -60.78532 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 327ea7dd-afd9-3ef9-ac66-9e6446b3cd8c | -9.26737 | -60.82083 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d63a7f-765d-3715-9c2d-00f27f328fc0 | -9.26404 | -60.82029 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 051afa13-b00f-320b-b961-d7996943af66 | -9.2635 | -60.82379 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 546ec097-b8ef-31da-b06d-475a8ebf9c66 | -9.20693 | -60.79331 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c70fee65-398a-3a5b-973d-ee03fe283fbe | -9.20415 | -60.78928 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f7f008b-64ce-39e3-9ffe-20bf515a9c47 | -9.2036 | -60.79278 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07f7c64b-9cb5-39e2-89fb-32997ae0411a | -9.20306 | -60.79628 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 864d1cd4-cc5f-325b-9694-9fcd6d204642 | -9.19899 | -60.69859 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a4e6545-d1c3-32bb-ba9c-bd23f102c593 | -9.19621 | -60.69456 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf0ae1fd-2bf6-3708-abcb-7b06b3e54ba2 | -9.19566 | -60.69807 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f414982d-5eb9-3130-aa0c-61d2c1414337 | -9.19289 | -60.69404 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 035a93f0-09d4-3527-bcee-ccce0f391591 | -9.19234 | -60.69754 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0908b782-eb4f-3660-b661-4f5131a3f306 | -9.18901 | -60.69701 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cb40a79-e297-3554-8807-7ad4dd3dfc23 | -9.18846 | -60.70051 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 643fab14-a755-3b58-89bf-ccbf11c7acca | -9.18579 | -60.76104 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97df3bac-cc31-3ce0-8c59-2490c0c31d5c | -9.18247 | -60.76051 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74d1dbee-9214-3782-8453-69da384901e3 | -9.17914 | -60.75998 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0dde8f8-5291-33df-b42d-2baab40eb7aa | -9.17625 | -60.6914 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf5efd7e-a6d6-354c-9cf9-5eec59326c6e | -9.17571 | -60.6949 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 320d596f-1b67-3aa4-baab-ca45c5df99d1 | -9.14349 | -60.66111 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 833b46df-5b2e-3a7e-bc3e-18578ddb854c | -9.09519 | -60.90421 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33ba5b2a-802e-3b42-810d-dedf52aab676 | -9.08188 | -60.62279 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9806a3b-0bb5-318a-bdc1-c55f3062d343 | -9.08134 | -60.6263 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1797539-c66e-3b62-b8cc-5f7c2d0cd572 | -9.08125 | -60.58322 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8effaa67-8ff4-3503-befd-405e86b89cae | -9.08012 | -60.56868 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d0b9ff1-f1eb-3a8c-b782-87f26889a8b6 | -9.07856 | -60.62226 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e54373e5-bf9a-3db2-a3fd-c10dde396da8 | -9.07847 | -60.57919 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79023695-6d68-35e9-9413-292deb6b2a72 | -9.07679 | -60.56815 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd90834-e909-32b1-9654-e480b29f8ef4 | -9.07514 | -60.57867 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f82e0b-d1fa-3aeb-9652-8b41e4508442 | -9.07346 | -60.56762 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22baa17a-758f-3f61-b2de-4a770dcda52c | -9.06146 | -60.66619 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8522864-88d2-34ee-9628-2a96d3ac7b68 | -9.05813 | -60.66566 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c8d802f-9bd8-32aa-951b-60143b6a073d | -9.0548 | -60.66514 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aedec5a1-7c47-3ded-bc82-38663dea99be | -9.05148 | -60.66461 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e451403-d94f-3451-b7ca-2de071c1a3e9 | -9.0487 | -60.66058 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4e6b373-833b-35ee-9599-7d125dd1b99d | -9.03922 | -60.63399 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a9adac7-7a68-3641-a43a-e4873222e44c | -9.03543 | -60.68 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ec2fac3-3ecb-34d5-b38e-87535c398aeb | -9.01839 | -60.74533 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6832c2f8-4ba2-3729-bd7f-25488af5a13e | -9.00618 | -60.73623 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88343589-e60d-372b-aff0-befe1c32c350 | -9.00117 | -60.72472 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7597c744-b5c7-3876-b310-71669f20a138 | -9.00063 | -60.72818 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c56135c7-f187-3f20-8877-246c8246f190 | -8.95558 | -60.78225 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d13e9cfc-c25e-33ac-a953-6490ed8fc064 | -8.94326 | -60.70872 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2a94752-d65e-38d0-bd5f-eee442377556 | -9.28866 | -60.37837 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 591ec406-c870-39fd-aa76-54b710a01f2e | -9.28612 | -60.26217 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ce99af0-d223-3a25-8225-c316aba170e7 | -9.28332 | -60.25811 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b323d70a-0528-3ead-9e50-eacedaac515b | -9.27111 | -60.27068 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 697c4a56-9733-30f8-81df-68febdf379ef | -9.27056 | -60.27421 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ab327d7-ecb6-35e5-bc1a-d590e61f4625 | -9.26884 | -60.27375 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84a44f5b-3142-31ef-b1ee-c9a3d75a6cb8 | -9.26829 | -60.27727 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09a59281-7155-32ec-bc9f-91248d7033f6 | -9.25712 | -60.26103 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c78a6b4a-f9a3-3cf2-8417-5a00446a6f7a | -9.23782 | -60.36292 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95a524c0-aa7d-32ec-a216-e22e9321bc47 | -9.23727 | -60.36645 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cd75403-340c-34ec-9499-c2fbcf193669 | -9.23448 | -60.36239 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5b56d95-cadf-34cb-9ba2-443804b4cc03 | -9.23393 | -60.36592 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dbe2781-ba68-3365-abeb-a1f9e8b86a7b | -9.2306 | -60.36539 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1a561ec-88bb-3a23-8bac-2555ee8d380a | -9.21098 | -60.29361 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a541ea6-86ef-3594-a91b-1c7172940020 | -9.18776 | -60.35503 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46d6a6bd-cca5-369c-a66d-6ce6d965d331 | -9.18387 | -60.35803 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cca5d44-1361-32b8-ae35-5638ee21f74f | -9.18054 | -60.35751 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27214fe4-58d3-34e6-9444-d84faf09dc27 | -9.17999 | -60.36103 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37f73c5f-0537-3ce2-8fbe-23b1e2adc1c0 | -9.1772 | -60.35698 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ea4274e-50e7-3c2d-b1d5-6688369b9d91 | -9.17665 | -60.3605 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41d332d-de0a-3686-851f-b07128cd7f11 | -9.16172 | -60.39065 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ff5791-0734-3ef2-9b10-729b8caa24c6 | -9.16117 | -60.39417 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a1622a8-3bcf-3c97-989e-7f1b8fcdc4ad | -9.16063 | -60.39769 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0f0754d-36c6-371f-b947-6094004ee9f7 | -9.15839 | -60.39011 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 687a7e8c-5d43-3298-9397-34bea6529267 | -9.15784 | -60.39364 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa4c43e8-4daa-3f10-8830-d9f8b81ea580 | -9.15729 | -60.39716 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25bd2598-9935-3d08-91cf-2ade877900c1 | -9.15505 | -60.38958 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8118b70-083b-342a-98f4-14e66bae0a4a | -9.1545 | -60.3931 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5452b73-56ca-3d13-b5bd-a3e53ac26fab | -9.12753 | -60.39626 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be344026-fb78-399c-a43f-580ffe67eb1a | -9.12031 | -60.39872 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cbfca06-6380-3a60-8acb-2844901871d3 | -9.11474 | -60.39063 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c61e4125-9deb-3025-8bab-6276f40c374e | -9.03821 | -60.44342 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ab014c6-f9eb-33e1-886b-a3005daac95f | -9.01874 | -60.44431 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ba453c5-9440-30b9-8c27-1cdcfc592b3f | -8.94908 | -60.15196 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| febaefdc-1333-380e-9037-25d625d204c7 | -8.94574 | -60.15145 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09b6498f-7e0d-304f-afad-32542e5350cf | -8.94184 | -60.15445 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca7fb844-6547-3024-a7d1-20c90847ed28 | -9.2772 | -59.70765 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8916fcf3-470c-3242-8d6c-b5069664f734 | -9.22819 | -59.74855 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20f4cda1-d3a5-3f73-84cf-38b977e034b8 | -9.22763 | -59.75216 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9143ffc-d5ad-3031-a6dc-7bc9edc89a36 | -9.22481 | -59.74802 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec215e37-f788-322f-a3a1-176c04697dc4 | -9.21979 | -59.78051 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e8439f9-0d78-3d3c-952b-e47b0cc30fcc | -9.21809 | -59.76916 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fe42894-b732-3d6d-bfe4-eaba29801792 | -9.21753 | -59.77277 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| add0c82a-1cee-34ef-a847-5745edec1e8d | -9.21471 | -59.76864 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0f3714d-f6f3-3a81-b2ca-0d9c50533cfd | -9.21416 | -59.77225 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 263341c5-6e6b-32b1-b323-6fe21406ac01 | -9.2136 | -59.77586 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35c95e17-6df6-3e87-990a-3bc8d90b3184 | -9.21078 | -59.77173 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72e17391-8e05-3bbe-b423-319b0b1c36d8 | -9.21023 | -59.77533 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f761dfb-4836-35c0-9914-952ed33cf816 | -8.80142 | -61.0296 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d5a47b-3d88-3aee-9005-3f077eeba596 | -8.79755 | -61.03255 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 916b7135-5847-3853-87a5-6c66c6fc48bf | -8.79477 | -61.02854 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 292ac1ba-9a21-342c-ad9c-96529598fa44 | -8.79422 | -61.03202 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e93dc47-b0a7-3a7a-b9fe-a1ee5e94d00b | -8.79145 | -61.02801 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README111.md)
