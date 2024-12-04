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
| 62ddf212-d868-3bc0-823e-af9496551e36 | -5.5695 | -45.1425 | 2024-12-04 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| bb4baff2-dc4c-338f-a038-e05d0a4ad63e | -3.8544 | -52.1543 | 2024-12-04 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a641ca54-c538-357c-975a-40b8f55ae3cd | -3.1453 | -54.6259 | 2024-12-04 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 35c5eb9f-83dd-338f-9908-b78fa4bb2440 | -2.9608 | -45.2123 | 2024-12-04 00:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 7fe1348f-69eb-341f-b754-cc1f8247d470 | -5.6281 | -44.8433 | 2024-12-04 00:00:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 314b099a-7617-3f3c-bb60-1406a8e9ee08 | -3.1269 | -54.6263 | 2024-12-04 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 628.7 |
| 684bf3d1-cb39-3abf-bc98-7cd73b659a44 | -5.5882 | -45.1412 | 2024-12-04 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 896f408d-b56e-3c93-9fa4-05a2032f5d5f | -5.5693 | -45.1651 | 2024-12-04 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b32f64cc-8858-3689-a218-4a4eeaaf1f90 | -3.2153 | -50.6423 | 2024-12-04 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0de15d19-b61f-34aa-8ac6-c90660bb177b | -2.8975 | -51.8133 | 2024-12-04 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 48d2b863-3708-3f90-bd71-6de872ebe460 | -4.3689 | -43.3606 | 2024-12-04 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| ba991213-456e-3c00-8463-725f043c5533 | -4.3876 | -43.3595 | 2024-12-04 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 3f94556c-ca07-3b0c-821e-6cb63a2db8d1 | -3.259 | -53.659 | 2024-12-04 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 866f8564-1a96-33e4-9864-5335a1ee0041 | -5.588 | -45.1638 | 2024-12-04 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| b64b6279-9c42-3047-b6a9-a00e8f370ffc | -4.1222 | -43.9529 | 2024-12-04 00:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a1aeabd7-005a-37c6-8d54-4afb698bcc2c | -2.879 | -51.8138 | 2024-12-04 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0dcc736f-8346-33f9-a355-41f25b8ee8ca | -4.1223 | -43.9299 | 2024-12-04 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 193.3 |
| dda52197-3150-35c6-b74a-b03a664e3c47 | -3.2152 | -50.6632 | 2024-12-04 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 252ff544-52c3-3560-b6cd-1c8164a48efd | -2.8791 | -51.7932 | 2024-12-04 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1675eade-9f4f-3b69-9db7-c116edc5cb82 | -3.5572 | -44.9623 | 2024-12-04 00:00:00 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9fa5e4bd-6ef9-3a50-b6af-4abb583d7a7f | -3.586 | -50.3158 | 2024-12-04 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 676fb3b4-e089-3561-bda9-905d434d1906 | -3.1968 | -50.6637 | 2024-12-04 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f3329fcb-57c2-3f3b-8b80-c2480da75d65 | -4.3874 | -43.3827 | 2024-12-04 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 8253a6e9-64f2-3ac6-a170-b7eb77905df0 | -6.086 | -48.0557 | 2024-12-04 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| f81386db-27bd-3336-990c-2e774f401f84 | -4.1225 | -43.9068 | 2024-12-04 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 87ba341f-2ddd-3404-8422-b294ccf8479e | -2.8013 | -53.043 | 2024-12-04 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8a4d4ccb-0fdb-3396-98df-3cc53e529a44 | -2.8197 | -53.0425 | 2024-12-04 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 7fddfc76-c540-3a87-a729-b8f986455571 | -3.127 | -54.6063 | 2024-12-04 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 722.3 |
| db0d4ed6-06fe-3441-964d-ec9d5197b091 | -3.169 | -44.4332 | 2024-12-04 00:00:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| fbfd4707-55c5-341a-b212-d9717fb3d397 | -2.9609 | -45.1898 | 2024-12-04 00:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 51d0ffb8-853d-343d-8fa1-0bdf99bd6ab4 | -4.1037 | -43.9309 | 2024-12-04 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 090809ee-6e9c-31da-b8ae-68808956023b | -2.532 | -45.5638 | 2024-12-04 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 12ccd2df-fdf8-312e-9ba8-d3f94aa51500 | -2.0682 | -45.4871 | 2024-12-04 00:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 110ea34a-5ffb-3ee1-afe8-e9ebc8fcc3b9 | -2.0683 | -45.4647 | 2024-12-04 00:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 21072b8a-af53-3e26-9f69-aac2c773f063 | -3.5861 | -50.2948 | 2024-12-04 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 64cff28c-3f60-34c0-a322-59c7712b5abb | -3.1086 | -54.6068 | 2024-12-04 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 218.5 |
| 21a43a07-9032-38cb-808f-a987c13609c4 | -2.8196 | -53.0629 | 2024-12-04 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| b4a27427-21bb-3475-a847-ad9c01ec2e1a | -3.5573 | -44.9396 | 2024-12-04 00:00:00 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 107e651d-70bf-3f4f-9b18-329fb0de3ae2 | -3.1454 | -54.6059 | 2024-12-04 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 73a74850-755a-3ad1-8f62-9fa5f7c75970 | -2.8012 | -53.0633 | 2024-12-04 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 98231128-5644-3c6f-a746-0b55d70193be | -4.3687 | -43.3838 | 2024-12-04 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8520a72d-f284-3b76-b8dc-9259a3f6f884 | -2.9794 | -45.2116 | 2024-12-04 00:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 126.4 |
| f6daafe9-5af3-35f2-9370-43cfa24990f3 | -1.6623 | -52.7599 | 2024-12-04 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a5e0be4c-f174-3225-93d9-68bd26beedfd | -2.9795 | -45.1891 | 2024-12-04 00:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| a38560ce-0acb-3d78-81c9-9252bdde921d | -2.6428 | -45.7394 | 2024-12-04 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 370a9574-7d9f-3914-878b-b33858ad4162 | -3.1969 | -50.6428 | 2024-12-04 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| dbcdb820-d998-3c51-8e46-9738ed0d75da | -3.5675 | -50.3164 | 2024-12-04 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 950c347c-33c8-363e-803a-92e06f7503c6 | -3.1086 | -54.6268 | 2024-12-04 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 4bb0b255-9ff5-386f-b442-59f8aea8ed84 | -3.12 | -54.62 | 2024-12-04 00:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1191db75-a2d7-35dc-acf8-81dea252c737 | -2.9609 | -45.1898 | 2024-12-04 00:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 59f05cc1-5aec-3891-8992-8f65e0eb22cc | -3.259 | -53.659 | 2024-12-04 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 463ebae0-c4bc-37cd-992e-bc467eaaf5fb | -5.5693 | -45.1651 | 2024-12-04 00:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c16ed892-2708-3fb6-8cce-e1030909bf3c | -5.6281 | -44.8433 | 2024-12-04 00:10:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 866d34ae-e736-3449-b3a9-b2fb66ac85b1 | -3.1968 | -50.6637 | 2024-12-04 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 878f0281-ce5f-30f3-b897-e9b9d8a8c8fc | -2.9608 | -45.2123 | 2024-12-04 00:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 7ddcd25d-9478-308a-a55c-db9107bf1cbe | -2.0682 | -45.4871 | 2024-12-04 00:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 0f51b90a-a3b5-3608-8f72-09e3e4d7dee5 | -5.5695 | -45.1425 | 2024-12-04 00:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3fe57a46-8668-3711-90fd-a4be5f8250cd | -3.586 | -50.3158 | 2024-12-04 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| cee19f45-ed5e-38e0-8e51-5dbf75dc9670 | -4.1876 | -45.3836 | 2024-12-04 00:10:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c2c3c17b-2d46-338d-b147-aaad4fc55600 | -3.6572 | -47.1183 | 2024-12-04 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 5007af07-6bf5-32fd-83dd-198bf3a770ae | -3.169 | -44.4332 | 2024-12-04 00:10:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 34769a93-27b8-337d-a841-22c3ee85c30c | -3.6571 | -47.1403 | 2024-12-04 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b216a5de-97b3-33cf-8cfc-736ae744d4ec | -3.5675 | -50.3164 | 2024-12-04 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 32744fcb-629a-3eaf-bc03-54be3bab1825 | -5.588 | -45.1638 | 2024-12-04 00:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 300ed97e-a763-30ee-9fc0-df4ed28e72dc | -1.6623 | -52.7599 | 2024-12-04 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| ecdd0a64-ac7e-378a-97d2-0b199ba7aa34 | -4.1037 | -43.9309 | 2024-12-04 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d8e6cece-6c7b-3fb3-836c-49d8f16dee11 | -2.532 | -45.5862 | 2024-12-04 00:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 3098a09f-a37e-38ef-b27a-a096ab9dfc12 | -2.8197 | -53.0425 | 2024-12-04 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 9a0b0b65-fdb8-3bf6-a754-2b3576241e77 | -6.1047 | -48.0544 | 2024-12-04 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d04df913-69a5-36cc-bcc4-5bf41851d785 | -2.9795 | -45.1891 | 2024-12-04 00:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f993e9db-5e84-36f4-bf40-625900d9a0cc | -2.8196 | -53.0629 | 2024-12-04 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| ecf31db1-d20f-38bc-9bb8-efca625dc0b4 | -2.532 | -45.5638 | 2024-12-04 00:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 546edd93-c125-3de4-8b37-32e7637aebd6 | -2.8975 | -51.8133 | 2024-12-04 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6c092080-496e-3cc9-be8b-ff77a6ca6fef | -6.086 | -48.0557 | 2024-12-04 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 1d25e980-309c-339b-84a7-2e719dd8641b | -9.497 | -35.7942 | 2024-12-04 00:10:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| 3cf51d88-c73e-3cab-af4f-aa97aec4014b | -3.259 | -53.6388 | 2024-12-04 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d5e9c456-4bf3-3def-a245-0c6aad764fd5 | -2.1976 | -45.6629 | 2024-12-04 00:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1a5a433f-07d1-3b18-aec1-9c33094cdf9d | -4.1225 | -43.9068 | 2024-12-04 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1c005e28-a813-3aa8-883f-df53c4b000d1 | -3.2153 | -50.6423 | 2024-12-04 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 79be70ab-374e-3191-9cfc-e86bd7f0515f | -2.9794 | -45.2116 | 2024-12-04 00:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 124.4 |
| e807ce64-f251-37da-8727-e99ffd6c5e4a | -3.6758 | -47.1176 | 2024-12-04 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 025f1d70-6dd2-3597-8ebf-abf62e7d4c5b | -2.0683 | -45.4647 | 2024-12-04 00:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ac4f6ea9-6204-392b-95f1-7f468133e383 | -3.6757 | -47.1395 | 2024-12-04 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fcc2aac7-020c-3ae2-8c77-476029c7419a | -4.1222 | -43.9529 | 2024-12-04 00:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 62668a3c-fbc2-3cf3-8a85-d2a678ce571d | -2.6428 | -45.7394 | 2024-12-04 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 74597bc7-3ca2-365b-a531-d0234d921ec8 | -4.1223 | -43.9299 | 2024-12-04 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 3d36e45a-c66a-3214-b263-0c202e56a16f | -2.8012 | -53.0633 | 2024-12-04 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 74761881-6dc7-3755-89f3-4a34e8d3d25d | -2.1975 | -45.6853 | 2024-12-04 00:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 31c4f875-f3e4-399e-81a5-1da953576812 | -2.8013 | -53.043 | 2024-12-04 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2eec8e1b-2b1f-319f-a5fd-6bfd64919530 | -1.6241 | -53.5308 | 2024-12-04 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 04d2f18e-941d-32f9-beab-4b8c9d15a640 | -3.1969 | -50.6428 | 2024-12-04 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| c80d3ca3-7221-366a-9b39-1a7e47135357 | -5.5882 | -45.1412 | 2024-12-04 00:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a321a076-2cdc-3cef-94ef-9f62e0e75ea8 | -3.8902 | -46.668701 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9c639e5-3347-3bc7-8e38-9a317ba28c02 | -2.8861 | -51.802502 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 519bcfeb-4016-3ed3-bbcc-027ff5f0fb54 | -2.8695 | -51.7742 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f41dba95-fde3-3b0a-84d5-682ac214426d | -2.8415 | -46.6796 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dca79730-03a0-3721-9103-09ff4192287d | -3.0503 | -53.239601 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9da1f3f9-3016-3212-82c7-e9e2e192c89e | -2.9495 | -51.394299 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c140115e-d3f4-347d-b998-6f74efacf342 | -1.482 | -53.782902 | 2024-12-04 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e382c667-b216-397c-98bb-b99b03fbdd59 | -3.842 | -46.500401 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
