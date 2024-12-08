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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ebbef30-fb80-3865-8260-b2713ef36391 | -12.4061 | -49.661098 | 2024-12-08 00:30:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51d7e4d3-cc8b-3cc6-a937-0edb46437556 | -12.8628 | -51.920101 | 2024-12-08 00:30:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04aaee01-72c2-315b-b09b-a9387b5bac81 | -3.0863 | -54.035702 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1f654be-3392-3b01-b63f-2001a133d6c4 | -12.8645 | -51.928299 | 2024-12-08 00:30:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74b5668a-bc8c-380b-ba9a-1ece5acaef0d | -3.0978 | -54.0415 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd376d4-0b00-3b27-a12f-95790265ea1d | -3.0898 | -54.051601 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6629f70-d840-39dc-9cab-ef188c7e7807 | -12.4189 | -49.673 | 2024-12-08 00:30:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c27168a3-e2c0-3665-aa24-9f733f10f987 | -15.3744 | -53.096199 | 2024-12-08 00:30:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d46e0e6-dfea-3f01-a504-4bd08d92aa27 | -15.2637 | -53.563702 | 2024-12-08 00:30:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f963fe2-5205-3ab6-bbba-ba34a2ae54a3 | -16.2047 | -55.932999 | 2024-12-08 00:30:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6aa0828-d719-376a-a99b-54bab7a62569 | -15.3764 | -53.1063 | 2024-12-08 00:30:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8fced3a-cfee-35fe-bdce-33a10dd2bfbc | -12.4205 | -49.68 | 2024-12-08 00:30:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2c36525-ac22-3a59-8907-54d2fc689d47 | -12.4076 | -49.668201 | 2024-12-08 00:30:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ae5a361-cf6d-3a47-9196-aa49886a6cae | -15.2714 | -53.550999 | 2024-12-08 00:30:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c6583758-8ff4-3ed4-aff7-16303f4fe67c | -3.088 | -54.043701 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b6c121f-3953-35fe-88cc-7aa3a21a4707 | -15.2594 | -53.542301 | 2024-12-08 00:30:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b196704-ed0c-3f56-bd0b-d643f4adac04 | -12.2859 | -49.489899 | 2024-12-08 00:30:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44cfa0db-1246-3e7b-8efe-9b1ff3113516 | -15.2616 | -53.553001 | 2024-12-08 00:30:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a095713-7353-372b-9a17-9ef0b4c48125 | -15.3666 | -53.108299 | 2024-12-08 00:30:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edc4c3e5-3818-3833-8438-9dbb0f88657d | -13.9032 | -54.6073 | 2024-12-08 00:30:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 80d009d3-2760-38ac-b9a9-dd45f657fa8a | -17.8069 | -42.931702 | 2024-12-08 00:30:00 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2518c012-01d6-3794-9bb2-7f34a8d240f2 | 4.0858 | -61.122501 | 2024-12-08 00:33:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b7b60b95-4393-3cea-bd14-f02ff848b1e7 | -5.4279 | -46.994301 | 2024-12-08 00:33:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cf42d5b-1f92-3887-9497-65bae8f388bf | -5.9017 | -48.019699 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9b3f6b9-e1f6-38ff-854a-73cab1f8c12d | -13.8935 | -54.609299 | 2024-12-08 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d981c58-7ac7-3d8e-b582-a77f1df8ed8a | 4.0816 | -61.139801 | 2024-12-08 00:33:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| daf95838-7608-3021-8ed8-d4a4a330446a | -5.9115 | -48.017399 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9c3823a-08b1-3e73-8a8b-438059ca8428 | -11.763 | -54.700001 | 2024-12-08 00:33:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4108c8cd-8452-3306-be3b-2de18d75bdb8 | -5.9133 | -48.0252 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb7d28f8-eb65-3a67-a696-cb43ce802cb9 | -12.9111 | -49.6647 | 2024-12-08 00:33:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf10f8ff-6b95-3f11-85cb-4a2998f86981 | 1.9985 | -61.1152 | 2024-12-08 00:33:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 214be625-656c-3bea-8be4-d684727e66c2 | -1.4327 | -52.583698 | 2024-12-08 00:33:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58146904-875c-3f46-855c-904361eb755f | -5.4986 | -46.235199 | 2024-12-08 00:33:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5841edf9-3c3d-3a8e-80da-2489c11613b5 | -5.9035 | -48.0275 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afb7e569-151b-38cf-8513-81a5627fa420 | -11.7653 | -54.711201 | 2024-12-08 00:33:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6abb51c1-016e-3091-963f-4e544422bec4 | -11.7533 | -54.702 | 2024-12-08 00:33:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06ee817d-5b5d-33c6-bb1d-366d6c702d62 | -5.9329 | -48.020699 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c293471b-d56e-3724-a1ec-f9fa67ee59f7 | -5.6419 | -46.717899 | 2024-12-08 00:33:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cf10fb5-27b5-3a41-a085-d24bc5601b98 | 4.0719 | -61.1376 | 2024-12-08 00:33:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3718d9ca-81f1-36f3-ae55-b28fbbb08cf5 | -5.9098 | -48.009602 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1e6af9b-a2b6-310b-811a-b71ce86a7c38 | -5.9231 | -48.022999 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1b9ab4a-48aa-3752-bd84-646d5259f5fb | -4.5903 | -48.0103 | 2024-12-08 00:33:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1d7153-6de2-3c93-9f29-13c755b0afe0 | 4.0775 | -61.157299 | 2024-12-08 00:33:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ef316239-01e5-3ee5-bfce-deef167398d0 | -5.4299 | -47.003201 | 2024-12-08 00:33:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64578474-a496-3a85-9306-80bb528fd147 | -5.9311 | -48.012901 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be7b965d-d040-3805-9946-5f843c23c225 | 1.9932 | -61.094299 | 2024-12-08 00:33:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 52d3eb0b-f23b-3ea1-a1db-b5c219c19a08 | -11.751 | -54.6908 | 2024-12-08 00:33:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15ccff60-b0b3-3c99-b92d-48212aa65118 | -1.4636 | -52.446201 | 2024-12-08 00:33:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66e72898-bb5c-3dbb-a219-d4e8a3a93c6f | 4.0761 | -61.1203 | 2024-12-08 00:33:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa2fc8e-6c00-3fb2-b206-fbe37ed028d9 | -9.2976 | -40.2244 | 2024-12-08 00:33:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f2e49a08-634b-3b87-8dc4-d6ce107f2740 | -12.4 | -46.582298 | 2024-12-08 00:33:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1b6e8a9-7f29-3ebb-ba63-975bccd04d32 | 2.0029 | -61.0965 | 2024-12-08 00:33:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f56f41df-43d1-377a-9ead-6d4a9ff62013 | -12.4018 | -46.590199 | 2024-12-08 00:33:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b998a6e-c8e8-38c1-8e81-4319e929e0cd | -11.7555 | -54.7132 | 2024-12-08 00:33:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b74c57d-9fd9-388f-808f-6554bebe3573 | -12.9126 | -49.6717 | 2024-12-08 00:33:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b28ef632-acac-322c-a22d-e698da712191 | -9.3072 | -40.221901 | 2024-12-08 00:33:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0b975ec5-ef38-343e-bd91-8659503ed6e1 | -5.9213 | -48.015202 | 2024-12-08 00:33:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb5749a3-b237-302a-992a-4cbc8e1d1756 | -11.752 | -54.7255 | 2024-12-08 00:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 11ffa11f-d605-3239-8fd4-dcbafb4a17bc | -11.7523 | -54.705 | 2024-12-08 00:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f5a4b4a2-56e4-33d0-869e-d22fcebe743c | 1.9955 | -61.1394 | 2024-12-08 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0623d02f-914e-3572-8583-ef837b828db6 | -5.9185 | -48.0449 | 2024-12-08 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 323bc12f-4d98-3547-bc83-0e8a65ba44b3 | -5.9 | -48.0244 | 2024-12-08 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ef7bef35-5cff-3ea3-b822-33ccb2d8ed6b | -11.7518 | -54.7459 | 2024-12-08 00:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 26aa3d4b-548c-3b7b-8356-db941e085598 | -5.9186 | -48.0232 | 2024-12-08 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 39d9918c-6ff5-3c15-bdfc-8238fb5f7ab0 | -5.9373 | -48.022 | 2024-12-08 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 298f8bee-1ec2-3d38-942a-644bc66bfd67 | -11.752 | -54.7255 | 2024-12-08 00:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 2303fd23-fddd-34c0-9f73-f242ba2a4f8e | -11.7518 | -54.7459 | 2024-12-08 00:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d90cfb27-6a58-3ca7-93e3-2728217c3c90 | -11.771 | -54.7237 | 2024-12-08 00:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 49c81f9d-d9ae-3af7-bd30-dbf4374519c6 | 1.9955 | -61.1394 | 2024-12-08 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e10ac91a-838b-3a74-8535-006503875b73 | -11.7518 | -54.7459 | 2024-12-08 01:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b9d9a67c-d022-3b7a-ab43-245e794902e6 | -11.752 | -54.7255 | 2024-12-08 01:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 938665d7-a9ff-3441-8c10-a21c60d1ed09 | 1.9955 | -61.1394 | 2024-12-08 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1a95f38d-0cb6-32ed-b3b1-8eb598c7f110 | -11.752 | -54.7255 | 2024-12-08 01:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 2e035c69-b063-36f4-8ce2-756df67756d5 | -11.771 | -54.7237 | 2024-12-08 01:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 43915745-e7fc-3523-8f38-4a0af2e3246c | 1.9955 | -61.1394 | 2024-12-08 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 88.8 |
| decb2c2b-4daf-36a4-93c1-6f3703710da2 | -5.9186 | -48.0232 | 2024-12-08 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 9e4b310d-29df-3273-a7f0-923f599edd20 | 1.9954 | -61.1583 | 2024-12-08 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 15ba2fdc-a110-3e8b-bd2e-c784a514f550 | -5.9186 | -48.0232 | 2024-12-08 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 8e967fd5-886c-33c2-8898-05798ac45c3d | 1.9955 | -61.1394 | 2024-12-08 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| cffc1bcd-28e0-3aa6-b0b4-d5a5468f920a | -5.9 | -48.0244 | 2024-12-08 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| d3cf4d23-a81e-3e2b-9782-918ee12482f4 | -11.752 | -54.7255 | 2024-12-08 01:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 1d9f4ca6-fcef-34f0-afb2-9545b903bd05 | -5.9185 | -48.0449 | 2024-12-08 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 17323aa6-d6a9-3100-89f3-2ce2748dd906 | -11.752 | -54.7255 | 2024-12-08 01:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 353fe723-f663-36be-a41c-ee191a3fdedb | -4.5986 | -48.0123 | 2024-12-08 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f88459b4-e12f-3094-b5c1-65fd089ee7a4 | 1.9955 | -61.1394 | 2024-12-08 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 61415c17-cf96-3dcd-a290-b018cebca18b | -4.58 | -48.0132 | 2024-12-08 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 93ff0fcc-490a-3e65-81b3-24d0d00b30af | -4.5799 | -48.0349 | 2024-12-08 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f30dbe57-2b92-3a8b-8b43-28f083093d2f | -15.3742 | -53.125599 | 2024-12-08 01:32:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb6a0ce-a48c-3169-b492-36b910ec3dd1 | -15.1677 | -56.4785 | 2024-12-08 01:32:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a68b31a-cccd-3523-993e-34cf87a85fa1 | 2.5685 | -60.695 | 2024-12-08 01:32:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e73a3b1-fb15-3cfd-920b-7167859f984b | 4.0805 | -61.155399 | 2024-12-08 01:32:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 17ef8181-d173-3c19-ab5a-03d87a740f49 | -1.0817 | -62.634201 | 2024-12-08 01:32:00 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd5bb0c0-d317-380c-8ebe-bc22e2e2a0c1 | 1.9946 | -61.1339 | 2024-12-08 01:32:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebc7288-3bc6-3476-8de9-7811a02164a8 | -15.2594 | -53.570499 | 2024-12-08 01:32:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ffc28912-4d6c-3be5-a486-86c7805a1eb4 | -12.779 | -54.209801 | 2024-12-08 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7ae795-7693-3839-9915-995d9bbb8f02 | -1.0832 | -62.640999 | 2024-12-08 01:32:00 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| efeb32ab-df44-35fe-9156-39b2415f77b2 | -15.3709 | -53.112701 | 2024-12-08 01:32:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3a63a8-82b0-33e5-b541-bbd72a13acd8 | -11.7581 | -54.722099 | 2024-12-08 01:32:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11d91c72-8433-3344-9354-8d8e2f0d8829 | -12.5391 | -57.7341 | 2024-12-08 01:32:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0b8b19c-1aff-3a9b-8054-786779e705fd | -11.761 | -54.733601 | 2024-12-08 01:32:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
