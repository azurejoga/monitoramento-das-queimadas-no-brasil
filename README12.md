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
| 5cec9788-c91a-340d-bb26-924383837da8 | -11.234 | -53.725498 | 2024-10-06 00:48:10 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 543f2199-bb73-37ab-8c62-d01acd4b74d5 | -10.9368 | -52.3974 | 2024-10-06 00:48:10 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf780edb-e992-3c88-aa08-da87bc84379e | -10.1177 | -48.801498 | 2024-10-06 00:48:10 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b138918-3083-335e-bf3f-85622d756f4f | -10.1195 | -48.809101 | 2024-10-06 00:48:10 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b15581a0-4a77-3ad3-8e62-5a5d9afcbc39 | -10.1213 | -48.816799 | 2024-10-06 00:48:10 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6c7a62c-0fac-38c5-b4af-c5e626370fb8 | -10.9285 | -52.406799 | 2024-10-06 00:48:10 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6b7987b-2c45-3650-988d-948e2b7ed71a | -11.2387 | -53.843601 | 2024-10-06 00:48:10 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f77d872-2202-34be-9099-0f3984c6e7a0 | -11.2272 | -53.837502 | 2024-10-06 00:48:10 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45d97796-2a20-3d48-bb96-c03ca741c8ea | -11.2289 | -53.845699 | 2024-10-06 00:48:10 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4e18a3-dc6b-3ac2-b006-75fe0393ce46 | -11.2307 | -53.853901 | 2024-10-06 00:48:10 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2f22982-16b7-3e63-a9b5-b878038132ba | -10.8979 | -52.3606 | 2024-10-06 00:48:10 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90ea37df-741c-35ea-809e-1b765ee0c839 | -10.8995 | -52.367802 | 2024-10-06 00:48:10 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb6c24c-6771-3b8e-8924-83437f6cf6d7 | -10.9011 | -52.375 | 2024-10-06 00:48:10 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae0b1394-659e-3968-92eb-f6d9b06f5d10 | -10.9026 | -52.382198 | 2024-10-06 00:48:10 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7eb61f-211e-3edb-9f49-ccd7246cd585 | -10.8897 | -52.369999 | 2024-10-06 00:48:11 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 664f1833-5e82-38e8-a8c8-c0d7dfe4cc81 | -10.8913 | -52.377201 | 2024-10-06 00:48:11 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61fc76a9-32f0-316d-a83d-6adf03fc85ad | -10.8799 | -52.3722 | 2024-10-06 00:48:11 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a17b9e3a-6c87-3a45-9e60-635bc41a2c98 | -10.8815 | -52.379398 | 2024-10-06 00:48:11 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbce55cf-c512-3e2e-8ab4-a788504b8e58 | -10.883 | -52.3866 | 2024-10-06 00:48:11 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5c92286-b173-390c-b7fd-f572edc5f0db | -10.8846 | -52.393902 | 2024-10-06 00:48:11 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57aad6f1-6e3b-377f-9a96-acbbb2e7daa0 | -10.5599 | -51.064201 | 2024-10-06 00:48:11 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bffc6e8-1320-351a-adf5-e863e4522b70 | -10.5191 | -50.9277 | 2024-10-06 00:48:11 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1af87c4-5e66-335c-bd6e-934fd3a6482b | -10.5222 | -50.941601 | 2024-10-06 00:48:11 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24d98a8c-8f05-361b-88c5-fae10ced568e | -10.514 | -50.950699 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dfec85a6-3b78-3d07-ac00-c8c690ca309e | -10.4465 | -50.696201 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c1bcbfe-4a47-39a9-8271-75be14976db0 | -10.4481 | -50.703098 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24db2d33-0aba-3e13-b060-eb7d7242730d | -10.4497 | -50.710098 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62e19a3c-60ac-3da4-a3e2-fa4821f93fac | -10.4512 | -50.716999 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de5978b1-df5f-303b-9e2b-298c1ff36149 | -10.4352 | -50.691399 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07d79c5f-2ec0-3cb4-8428-b18838a37065 | -10.4367 | -50.698399 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 89196568-e377-3a05-8223-9a056c1f2ab5 | -10.4383 | -50.705299 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83f783a2-6fca-3d1a-8c5b-d79058c3fd3c | -10.4399 | -50.712299 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 392b70f6-80d2-36aa-bd9d-d7fad54dfaad | -10.4238 | -50.686699 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca3f111-4172-339d-bcd1-02c3c0146eef | -10.4254 | -50.6936 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d751d69-ea80-3ece-b523-6702ebc730b7 | -10.4269 | -50.7006 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc3f70d-8af8-3e19-aae7-dd84e9ec5232 | -10.4285 | -50.7075 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1c4a894-9ede-3aa2-87d8-7972bc2b5574 | -10.4301 | -50.7145 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db4eafba-ee39-3aca-9649-3f4bf16b0782 | -10.4156 | -50.6959 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36fb1828-8a83-3c9a-b20b-d6d3266aede6 | -10.4171 | -50.7029 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 910554bb-8574-3d6f-825f-505a29a6a484 | -10.4187 | -50.709801 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d96983ee-7621-3265-b9ca-e869eceeeded | -10.4203 | -50.716801 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0d9236-9957-3c21-b993-9a9eb6ea7c9c | -10.4218 | -50.723701 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98b33b1f-38b0-3c44-9a49-bc747fc0f76d | -10.4281 | -50.751499 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8e485ee-8a21-35b6-96bf-e114c5d9583b | -10.4296 | -50.758499 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8de81fd0-1193-30ad-80c0-b285c8c61925 | -10.4327 | -50.7724 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a10b1970-e172-3b44-95cd-b7f170ece28a | -10.4995 | -51.070599 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f480e69-3d6f-3014-aff0-9193e99e0ebd | -10.4089 | -50.712002 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62191ab1-2c66-3616-9ca1-9d71e57be8c3 | -10.4105 | -50.719002 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74eb5445-8cce-3ea9-a1f3-89bde5ecaf0f | -10.4229 | -50.774601 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2787a5ca-3a6d-3a51-bbff-8a47ccdca3a1 | -10.4245 | -50.781502 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea59277d-8773-3460-bc23-76abf8e51920 | -10.4928 | -51.0867 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23d69bc3-ce2d-37a2-b6d2-80ba8a0fa248 | -10.4943 | -51.0937 | 2024-10-06 00:48:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fdc7bc29-e0ae-3cf1-9c0e-35a72064cd64 | -10.4147 | -50.783699 | 2024-10-06 00:48:13 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edf8516e-74c7-3571-a87d-44e794fa4a97 | -10.4163 | -50.790699 | 2024-10-06 00:48:13 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86a84e64-be5a-306b-9b69-272f3b5aea23 | -9.6904 | -47.8078 | 2024-10-06 00:48:13 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7e99d3c-18ba-3c9d-9f55-54f37c2c3ccb | -9.6786 | -47.801701 | 2024-10-06 00:48:13 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73517fa9-9acd-32bd-a1bb-e49cca2a8497 | -9.6806 | -47.8102 | 2024-10-06 00:48:13 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5480c759-21ab-32ba-b403-621040ece13c | -9.6826 | -47.818802 | 2024-10-06 00:48:13 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 039ac1ef-6cad-3a0b-8e01-0c67d33626ef | -9.6846 | -47.8274 | 2024-10-06 00:48:13 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1482cff1-7713-36c2-9c90-fa6ce174c01a | -10.4077 | -50.982201 | 2024-10-06 00:48:13 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 948cddc5-fb2b-310e-acac-b19f1cb3f0db | -9.6688 | -47.804001 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 780ac750-1463-3fd3-b073-80af0400cdd9 | -9.6708 | -47.8125 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 535a5012-2c68-38ce-8248-97c2d945b9b2 | -9.6728 | -47.821098 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdfffe2b-e6aa-38a5-b46e-2306cc58b6f5 | -9.6748 | -47.8297 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e77dda1-97e4-30e5-82c9-edb9612502a0 | -11.102 | -54.2127 | 2024-10-06 00:48:14 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 840d33dc-64c0-3f40-aa81-6685f2f99dad | -11.1038 | -54.221199 | 2024-10-06 00:48:14 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce28d6d7-f0c8-3c64-9cb9-24cc3490a3ca | -9.659 | -47.806301 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f88ad69c-2db1-3c18-a861-cbe88fcad9c1 | -9.661 | -47.8148 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a60ba24e-6cc6-38f0-8ca5-9853922fd5f6 | -9.663 | -47.823399 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be0733c9-fd5f-306d-8ba9-52a0fbaf2e8d | -9.665 | -47.832001 | 2024-10-06 00:48:14 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0b957bf-5990-38bd-bd9a-dab1726e55eb | -11.0922 | -54.214802 | 2024-10-06 00:48:14 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0fef27f-34f1-37dc-8eda-a585507e0b7b | -11.094 | -54.223301 | 2024-10-06 00:48:14 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc6c40f4-609a-37c0-bcca-acfceee154ab | -11.3416 | -55.401699 | 2024-10-06 00:48:14 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9a47568-c3fd-3098-9a8e-775d16f4ec82 | -9.3347 | -46.5229 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5338fe37-e2c5-3cc4-a3f1-bdcd7b07483f | -9.3371 | -46.5331 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86c83ce2-ba6a-3808-a748-dcfca1621a0f | -9.3396 | -46.543301 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b112bab6-9a9d-3656-b39c-375ad7c81abb | -9.3224 | -46.515099 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98953501-fb8e-3594-8c00-79d9261c3671 | -9.3249 | -46.525299 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5a4f884-3328-35d0-b50e-80e5faa1cec7 | -9.3273 | -46.5355 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17bea34c-a5c0-37db-8680-3a272d49619c | -9.3298 | -46.5457 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62e2e4d5-2423-351e-8a64-5cc609ee4918 | -9.3176 | -46.537899 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 733e90d8-aa4a-3946-81ad-88a7fa303e6f | -9.32 | -46.5481 | 2024-10-06 00:48:14 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc80d36-2580-3c14-8ca9-d6ef08e28cfb | -9.9737 | -49.475498 | 2024-10-06 00:48:15 | METOP-B | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fabb707a-d6a3-31cd-8555-5e9dacea4c09 | -10.9738 | -53.995499 | 2024-10-06 00:48:15 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e20abc-5631-30fc-9917-b0e32b6fff92 | -10.9657 | -54.005901 | 2024-10-06 00:48:15 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eedf6944-b6d9-3313-87c6-f1749ddf9ed3 | -11.0838 | -54.756001 | 2024-10-06 00:48:16 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d4c7927-c9aa-30f4-8a95-f411eb06ad32 | -11.0857 | -54.764999 | 2024-10-06 00:48:16 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 059742ee-e7a5-3812-bb9c-ef99723c7f3c | -10.7024 | -53.019901 | 2024-10-06 00:48:16 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 569dc6d3-06a9-38c8-8ebd-43111b993cdd | -10.704 | -53.027401 | 2024-10-06 00:48:16 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0b402d2-0dff-3197-a37c-527b454223a5 | -10.6926 | -53.021999 | 2024-10-06 00:48:16 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d343a754-9035-333f-92a6-ea7728bf29eb | -10.6942 | -53.029499 | 2024-10-06 00:48:16 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d464eabb-94fb-3a71-9ac9-139c97c51d40 | -9.4488 | -47.570301 | 2024-10-06 00:48:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cf5bfdd-edba-3ad5-8f0b-f345b792c9bb | -9.8913 | -50.063599 | 2024-10-06 00:48:18 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19d7286d-6a4d-30f9-91ba-e5d3ebec73ff | -9.7853 | -50.050701 | 2024-10-06 00:48:20 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e84e3a8a-ca5e-39af-ad52-ad9d8dd8aa7c | -9.7869 | -50.0578 | 2024-10-06 00:48:20 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8db95530-7618-3282-a36c-0d4e26d11f9f | -9.7885 | -50.064899 | 2024-10-06 00:48:20 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a61adad-d481-30a1-9fff-488af51cec5a | -9.2725 | -48.1394 | 2024-10-06 00:48:21 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 243c1376-0a41-3953-b6bc-2d1c1b26bf45 | -9.2745 | -48.147701 | 2024-10-06 00:48:21 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f760887-54b4-32ba-b49c-5eae0f537633 | -9.2588 | -48.125 | 2024-10-06 00:48:21 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d76afd66-da2f-34b6-9213-f46f7c51eb50 | -9.2608 | -48.133301 | 2024-10-06 00:48:21 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
