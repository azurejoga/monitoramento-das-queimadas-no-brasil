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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3d76b52-9dbc-3cee-a212-382125ff15a3 | -16.65572 | -57.23754 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2e3c6d36-da1c-3c2c-af44-2a90e328bd8f | -16.65529 | -55.97862 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8b699309-2719-3fb6-b33b-f96d217bdd16 | -16.65513 | -57.24248 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f00fe5f6-7cc3-34b6-b3ba-8ec1386ebc14 | -16.65389 | -57.29221 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 92b55793-9b83-321b-91db-4120ce47933d | -16.65318 | -57.23566 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ff75f369-f9ce-34a3-96c6-c97bca3c8706 | -16.65256 | -57.24058 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 1d79dead-e45f-3e9c-8f01-30400f7b7785 | -16.65235 | -55.96001 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ab19444f-339d-3fba-a8ea-9a18b65e1602 | -16.65165 | -55.966 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b463525e-4e59-3f0d-8e4c-5355409b6b46 | -16.65108 | -57.23692 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| d6da9e2d-d8ef-3a9b-bfa3-670d68282e26 | -16.6505 | -57.24186 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 5ede5e5b-f220-3fb6-bb24-13f83cedc017 | -16.64871 | -55.94736 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c29a9125-10c4-372c-8b13-aa398ceec95c | -16.64855 | -57.23504 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 123eb21c-70b1-3017-9365-49b6170a9e93 | -16.648 | -55.95337 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 394e3f65-6a52-362b-8d25-f8613d56a897 | -16.64793 | -57.23997 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 13506ab7-8428-3143-99dc-7f5a962b3926 | -16.64731 | -57.24489 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 2bfb674f-ec5b-3f1a-8cec-348e12cdeb38 | -16.6473 | -55.95938 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d0177c3b-1283-3c82-9b82-b462913530bb | -16.6466 | -55.96537 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8d5cbd37-14fe-31d5-8ad3-8c0593025858 | -16.64645 | -57.2363 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 6e55c6f1-877a-3539-bbf7-5a6bb05a6cc8 | -16.64591 | -55.97136 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7cdb1bb7-cfff-3e7f-85c3-6d895611be01 | -16.64587 | -57.24123 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| b1beec48-b253-367f-af62-4714d6891a56 | -16.64528 | -57.24616 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fc23a84d-c279-3792-a5cd-7f0a60c1cbe7 | -16.6447 | -57.25109 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fbf9b598-7421-3834-b5fa-f7fa5e37294e | -16.64392 | -57.23443 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| be93b67a-9121-3e0b-9a23-3877156ed75b | -16.6433 | -57.23936 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 27908929-f76c-38b1-aed5-6c830f28baeb | -16.64268 | -57.24428 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 7ca4efed-d42d-3fda-9021-0895d0db8755 | -16.64226 | -55.95872 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 46668522-ce3e-357d-8580-20a0be48c0ce | -16.64207 | -57.2492 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| f0d6a9ce-48de-3913-93f8-aaab924d087c | -16.64182 | -57.23568 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| eaf1e898-bd47-3d28-b88e-7f996f605370 | -16.64124 | -57.24061 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f583a226-7c50-337a-8bfc-30ec157cb45c | -16.64066 | -57.24554 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 99758c94-6631-3020-bd20-3e87d5b5f7d5 | -16.64007 | -57.25047 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| fb78bb11-daed-3f75-b57b-57114b45a6c4 | -16.63963 | -55.1994 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 530f49a4-91ff-34cf-b28e-49e829600cfb | -16.63949 | -57.25539 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 21c2ce07-1964-3be8-91c6-611f9a13be93 | -16.63925 | -55.20275 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a375fe49-de02-3369-ab05-c40c9e1b5fb7 | -16.63867 | -57.23874 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| fddef706-aa74-35fd-acfa-fa2f63f0e51d | -16.63861 | -55.94605 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 03642c4b-7d3f-3664-93d9-c2663e063a0a | -16.63848 | -55.20949 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7e0d8388-81aa-3a7c-8e70-fe983130ea1c | -16.6381 | -55.21286 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 67f27efd-b591-3034-90f3-69d32caf8a24 | -16.63805 | -57.24366 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 30e5bbb5-b661-37a6-a97a-54c51ee0ce95 | -16.63791 | -55.95205 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 427002d6-2d3a-3033-ae45-6a51e40ccc4a | -16.63744 | -57.24858 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| d7e09c91-a6f0-3364-84a3-394aed853e39 | -16.63719 | -57.23506 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 216301f3-54ec-37f6-8d06-83710d287c58 | -16.63682 | -57.2535 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| c79b46f4-edfe-337e-ad68-3e21cb3a808d | -16.63661 | -57.23999 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0ffed326-e3db-3cac-bca7-55a404436071 | -16.6362 | -57.25841 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 20d8dbc5-fa4c-3be4-9464-dcd6318529f7 | -16.63602 | -57.24492 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 94e1cf78-4401-3497-995d-9878c740b0ad | -16.63547 | -55.18864 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e16e66ba-ff42-3ac2-b30b-196b6063ca57 | -16.63545 | -57.24984 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 6894b0fa-1bcf-3582-95c6-129fa65cde48 | -16.63487 | -57.25476 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 38089e50-9b58-3a54-b39a-6f55168faa9b | -16.63433 | -55.19874 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1018ebba-678a-39f7-8866-3fa55a0fe266 | -16.63429 | -57.25968 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9e5cde8e-e764-3de9-ae92-ef689b641edc | -16.63394 | -55.2021 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d9ddc008-c190-3dc0-9e40-32821fce0f46 | -16.63343 | -57.24305 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ba57bdfb-7543-3f53-974b-e0b43bd01530 | -16.63281 | -57.24797 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| 8aafa3a1-01f2-37b3-81e5-6df03d2653a0 | -16.6322 | -57.25288 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| c3d34604-03b4-30b1-94ee-ec2f7fbc7352 | -16.63158 | -57.25779 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 8ab6748c-e0c8-30bb-8647-efebc18ae0ea | -16.62978 | -55.19135 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f2b2860e-27ba-3d46-a138-c455dfb3a6ae | -16.6294 | -55.19472 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 703bba83-f1c0-3d84-b5b5-314dc804ba15 | -16.62902 | -55.19809 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3dd25f29-9db7-399d-8fcf-065c06ba593c | -16.6288 | -57.24244 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 21164dc2-d5f3-3e82-8d46-5fa75d26634d | -16.62864 | -55.20145 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 89527387-1e23-38a7-ab69-ca8dfe90b44b | -16.62826 | -55.20481 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7610fb67-c603-3826-b5a7-2c43eb9b8aaa | -16.62819 | -57.24736 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| d3ee8d63-5c5a-3c6a-aece-5180612a6342 | -16.62757 | -57.25227 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 1e98cd9c-d12f-33eb-8b9f-ba2169b62aef | -16.62696 | -57.25718 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 6866719d-3935-38df-94a3-7ad0d8974365 | -16.62295 | -57.25166 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| ca14fed7-200c-3f39-8424-b435d196af0d | -16.62233 | -57.25657 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 4835aea9-2841-361b-8289-790c4546e361 | -16.62173 | -57.26148 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| f356891b-74ab-3145-bbc2-08521622ced1 | -16.61005 | -57.27983 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 6b3b2763-5484-342e-9b94-51108c981230 | -16.52292 | -57.34438 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cb3423d7-9f31-3a0e-9c26-335eccbbdf6e | -16.45722 | -53.93085 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69cdd2c0-430e-3644-8d39-b0c0dff86b4e | -16.45679 | -53.93483 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1870877-0e88-30a8-88fb-0fab47a8dd11 | -16.45195 | -53.92576 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1baebc99-55c4-3551-88ee-92912a5d8f5c | -16.45149 | -53.92998 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e2a24f1-7ff8-34c2-9c6a-bfe49636ed4b | -16.45067 | -53.93759 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dff8f4b1-69cf-3b01-8055-c885b56f9b5d | -16.4462 | -53.925 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a126daca-2018-35f6-a9a4-3a9300dbbddb | -16.43522 | -53.91879 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7f3e882-07a3-35e6-a43c-b77e19abb9d0 | -16.4295 | -53.91775 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0509bc7-0455-3cfa-92d4-de0668c6647b | -16.42333 | -53.92101 | 2024-10-01 05:31:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7a2f2bd-141c-34b6-a0db-3dca78b2656e | -16.18192 | -58.42665 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e03f4094-be17-310e-a864-58906ab8fc24 | -16.18138 | -58.43072 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 452f8622-aea1-3b66-ae3d-3a82c357f610 | -16.18136 | -58.42504 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b9007cbc-53e3-3af2-83ca-16b3df5546df | -16.18085 | -58.42909 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 255f1557-cccf-376c-95a9-d5b0cefa540e | -16.17767 | -58.42606 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0e88a3b0-2e87-3ffe-9211-6ac3874eb824 | -16.17713 | -58.43011 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2bfee5f2-4af5-3cc9-b57e-4d393cc13aae | -16.1771 | -58.42444 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 96016999-a938-390e-82ac-d738d9dad21d | -16.1766 | -58.42849 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a0d22448-e2cc-38a1-af79-60e6826b2f87 | -16.17289 | -58.42952 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 65b09d64-0481-365d-a8bb-0b84cdb3fc58 | -16.17235 | -58.42788 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4fb356ed-39d8-3b1c-a79d-a389756614df | -16.14736 | -55.42284 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e03dd7be-1fd8-3610-85db-74da95ad503a | -16.14704 | -55.42566 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6fb32f3b-f76f-3c13-a7db-e1f5f1b40d6e | -16.14228 | -55.42115 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07272444-02f5-34f8-a06f-46ac38763423 | -16.14194 | -55.42416 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1dccf99-e2ff-3972-8d1d-06ef38a2c531 | -16.14159 | -55.4272 | 2024-10-01 05:31:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8956762-4c94-3e66-b7e6-6a8f7be05a99 | -16.10162 | -57.52596 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7fd85f9-c471-367f-9902-9154f1f8c811 | -16.10111 | -57.53014 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a940efbc-d751-33aa-934e-fa4e765476d5 | -16.09711 | -57.52543 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80a2fc4a-6294-357b-922d-9404ee3ba08b | -16.08894 | -53.54299 | 2024-10-01 05:31:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51c2d249-42c9-31be-8b18-0813cd97142f | -15.91268 | -57.21164 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5fdb24c-bda9-3fa5-84cd-6d3487ec4c4a | -15.91258 | -57.21461 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README150.md)
