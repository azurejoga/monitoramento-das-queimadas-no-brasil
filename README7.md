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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cecfbcc-93c5-318a-9c78-d7120942a7af | -5.5695 | -45.161499 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 820fec89-ff03-37d7-a9a6-9fa9f73fb046 | -3.2022 | -50.635399 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e7528a-6d18-36f9-8389-bde110f3c01b | -3.1924 | -50.637501 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 110cbb1d-88f2-3db6-a049-7ade34c99c24 | -3.7271 | -50.037399 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f4eed5-fb9c-3583-888a-5a11e9206d91 | -2.0944 | -46.565498 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5335f272-00a9-36b6-9ed4-6c5402671c89 | -3.2626 | -46.262501 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a639cc0f-7013-3222-9421-8196520c1f76 | -3.8081 | -46.944599 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a51c8b71-9029-31ab-9c8a-6eeec40c5aaa | -3.044 | -44.980099 | 2024-12-04 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3aee8a6b-668e-3a0f-9599-03f9859dccbb | -2.204 | -48.3326 | 2024-12-04 00:17:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 574af2b8-f4c1-3142-9ab4-76bd964b1989 | -3.8665 | -48.352699 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a252c38d-f647-3bd9-a44c-01a2836c72f0 | -3.4805 | -50.222801 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 189a535f-5bdf-3786-9f6c-3342b7fed940 | -3.4688 | -50.2164 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfbab67-5cc0-399c-be79-ae0569bacf95 | -3.2788 | -53.673901 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e291343-e67e-3377-8e92-406b9e946aa3 | -2.532 | -45.5638 | 2024-12-04 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 122cd706-542b-3495-b069-777e98200d4f | -2.9609 | -45.1898 | 2024-12-04 00:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4a96351e-5e9a-394b-8a7a-05db14919e0b | -3.5861 | -50.2948 | 2024-12-04 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 047b9728-bc0c-3697-8c9b-f392563365ff | -1.4952 | -53.7945 | 2024-12-04 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d9c12eed-ddfc-356a-8423-f96ce93d7dad | -2.9794 | -45.2116 | 2024-12-04 00:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 3aeb06db-aee9-3e2a-82d4-feb6c0ff7306 | -2.9608 | -45.2123 | 2024-12-04 00:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| b1eb62a7-719a-30aa-96b2-75a09a9398be | -5.588 | -45.1638 | 2024-12-04 00:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| c1bfcbf7-a630-336a-ba4d-49266e7c628b | -2.9795 | -45.1891 | 2024-12-04 00:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 675c67ce-2e3f-32b8-893a-94ca9cbca7a5 | -2.6242 | -45.7399 | 2024-12-04 00:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9dc6f74e-cb63-3fca-ab43-a277b53c471a | -1.4951 | -53.8146 | 2024-12-04 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| b41706ff-5eec-32b8-9b9d-51f5420243d0 | -3.2153 | -50.6423 | 2024-12-04 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2e1e724d-6fd5-3cbc-9bed-e70620c89c7e | -2.879 | -51.8138 | 2024-12-04 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 81c0287e-da69-3abc-ad45-d04489149b47 | -2.8013 | -53.043 | 2024-12-04 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f45a66c3-47ae-3ed4-9da4-2e4f9f2c6b62 | -3.6757 | -47.1395 | 2024-12-04 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| f949cfb7-cc8f-3ac9-bcca-c69161b3d7b6 | -3.1968 | -50.6637 | 2024-12-04 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fd022e54-92f9-3a49-a188-33773b0b4da8 | -1.4768 | -53.7947 | 2024-12-04 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0c11e082-836f-34da-be50-2ad13f653efc | -5.5693 | -45.1651 | 2024-12-04 00:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 70de7505-565d-3593-9a09-f31d564ab412 | -3.259 | -53.659 | 2024-12-04 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3993a210-8657-3431-8827-2282ade5ee05 | -4.1037 | -43.9309 | 2024-12-04 00:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 9f0873da-4270-3bd2-9934-19aa75ed3504 | -2.8196 | -53.0629 | 2024-12-04 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 0cdf179e-1a15-3688-87fe-c805dc1adfde | -3.6571 | -47.1403 | 2024-12-04 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 733ebb50-9a05-3108-aa2d-7b4c2d442f11 | -4.1222 | -43.9529 | 2024-12-04 00:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| cf298d1a-edc3-3f4e-9313-ee1d0c369064 | -2.6428 | -45.7394 | 2024-12-04 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 133.2 |
| d7f333c5-7cda-3656-ae19-341b2a3c5b69 | -2.8791 | -51.7932 | 2024-12-04 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 88116867-32fc-3cb2-b583-8fce002805e9 | -6.086 | -48.0557 | 2024-12-04 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 18d4ac2c-f3bb-3a80-bccc-e5060dd6d6b8 | -1.4768 | -53.8148 | 2024-12-04 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 928f4356-2a38-3ad9-83c4-617385c22bce | -3.6758 | -47.1176 | 2024-12-04 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| fba42573-6bcf-34d7-8069-adcd9568aafa | -3.586 | -50.3158 | 2024-12-04 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d2891df3-18f0-3823-a9eb-ecae75998ee5 | -3.1969 | -50.6428 | 2024-12-04 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 0017295d-026b-374d-9d7c-72ed7a2900a7 | -4.1225 | -43.9068 | 2024-12-04 00:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d9cdf40f-5b6d-3e2d-bb32-8fb8999877bc | -3.259 | -53.6388 | 2024-12-04 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 328bc06a-e512-35d4-969c-996c35dda0cd | -4.3876 | -43.3595 | 2024-12-04 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 74a213d6-fb9d-300c-ac77-5392f4eeced3 | -3.5675 | -50.3164 | 2024-12-04 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0663ea63-71a6-3872-9269-835b2116380b | -5.5882 | -45.1412 | 2024-12-04 00:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 6d8c3aed-ee95-35b5-8ebb-b941a4ddffe9 | -2.8975 | -51.8133 | 2024-12-04 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 21374776-5b0f-3c70-ac2f-a4f94514fc41 | -2.8012 | -53.0633 | 2024-12-04 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 99e73577-6dad-36af-8e86-b376edd7a048 | -1.6623 | -52.7599 | 2024-12-04 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9cf39d87-b55d-3bb3-a018-6ce5394e8283 | -6.1047 | -48.0544 | 2024-12-04 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 57dfe68a-a4da-34cc-ab2c-ca342918081e | -4.1223 | -43.9299 | 2024-12-04 00:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 253.1 |
| 2aea66e4-8a50-3ef7-bbb8-19e20ad905d0 | -5.5695 | -45.1425 | 2024-12-04 00:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 14c6c51e-4206-3873-8522-e4f1f9515b46 | -2.0682 | -45.4871 | 2024-12-04 00:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 3c1fef00-c10b-3d27-8c80-6f695fe07ece | -3.6572 | -47.1183 | 2024-12-04 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |
| c740be03-4ab9-3df5-9d6d-e33c8fb5758c | -2.8197 | -53.0425 | 2024-12-04 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 3db005b9-58d8-3f44-9f96-f34c4631a665 | -5.5693 | -45.1651 | 2024-12-04 00:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 2afca95b-3dc6-37fb-929a-6f2be89e0780 | -2.6428 | -45.7394 | 2024-12-04 00:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 154.5 |
| adb50977-aacf-3d04-b237-1f34524284de | -3.6572 | -47.1183 | 2024-12-04 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| ba08901b-484a-3375-b611-3d40f5c3cc10 | -1.6623 | -52.7599 | 2024-12-04 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 649c2223-468e-322f-ac7b-1a96bbcd34cf | -1.7361 | -52.6162 | 2024-12-04 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| e4a23e30-eccf-32b4-a465-291851d19b33 | -2.879 | -51.8138 | 2024-12-04 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3645c424-f7ea-37a4-b639-327dc6ed101f | -3.6757 | -47.1395 | 2024-12-04 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| a1cab105-262e-380a-899c-30d53bcc7f41 | -3.2153 | -50.6423 | 2024-12-04 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3028ddab-be73-37bb-8319-8e926a27c6c8 | -3.586 | -50.3158 | 2024-12-04 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 59e2f886-bc30-3685-8c3d-ee7e56c6f8f1 | -5.588 | -45.1638 | 2024-12-04 00:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| cf9dc6d8-a311-3ad5-9371-f8f22ffaf7f3 | -1.5087 | -46.7647 | 2024-12-04 00:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ac219f52-7ded-3dac-8d3d-49fa462f8e39 | -2.9609 | -45.1898 | 2024-12-04 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| bf59f11e-f2c7-350a-96e0-b12ccef14d6a | -2.756 | -45.2871 | 2024-12-04 00:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 42834cf2-f2e5-3723-972b-1d026284e2cb | -4.1223 | -43.9299 | 2024-12-04 00:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 243.9 |
| aba17a37-9cb0-380e-801a-5493da5bde09 | -2.6242 | -45.7399 | 2024-12-04 00:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 406b8d43-7aab-3964-b3c2-aee32b1d784d | -3.259 | -53.6388 | 2024-12-04 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c7dabe76-4657-3222-a6f9-db21e2a88676 | -2.9794 | -45.2116 | 2024-12-04 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 791445f7-5d3d-3c6b-8894-5bdad3c003f7 | -4.1038 | -43.9078 | 2024-12-04 00:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| a2cb7206-02db-3a4f-8b75-d8fcd4dc268f | -2.8012 | -53.0633 | 2024-12-04 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 307158ad-194e-379b-b61d-b70ea4491643 | -3.1968 | -50.6637 | 2024-12-04 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d2e56319-9381-364a-9be4-8b7fdf853d4b | -3.6571 | -47.1403 | 2024-12-04 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 52ddfc02-d945-3c23-a7d5-85d7f4fb5026 | -1.7544 | -52.6363 | 2024-12-04 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7ccf6162-4de2-306e-a136-c517822da0f7 | -4.0501 | -46.5947 | 2024-12-04 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 796cb85a-f095-30d6-8805-d5a9d845b918 | -4.1225 | -43.9068 | 2024-12-04 00:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c51c0249-056b-3948-a9ed-831129bfd63b | -2.4028 | -45.3657 | 2024-12-04 00:30:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| acf5d550-4037-3f6b-a796-01d530c257b4 | -2.8791 | -51.7932 | 2024-12-04 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c332dba9-be23-3161-a934-11d1ffcd30dc | -1.4768 | -53.8148 | 2024-12-04 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 1faf2d22-0efd-3e71-805f-960d1846397d | -4.1037 | -43.9309 | 2024-12-04 00:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2691e733-3998-37b5-b2ac-98e3dc73a2bf | -3.6758 | -47.1176 | 2024-12-04 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| d052c88f-994f-30b8-8ca4-a607a1aa4009 | -2.0682 | -45.4871 | 2024-12-04 00:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 80a3c81f-b11a-34f1-ba67-156cdbd5babd | -6.086 | -48.0557 | 2024-12-04 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1c34c057-8693-3e87-aad2-d3e903ad9b14 | -2.8197 | -53.0425 | 2024-12-04 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 433270c4-1e28-3ddb-b009-c1ed510f4bbb | -2.7561 | -45.2646 | 2024-12-04 00:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 17bed4c7-6dd1-3dc4-8175-b05cc9a5068b | -5.5882 | -45.1412 | 2024-12-04 00:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2934c539-d8f3-3e18-be10-3356020fa499 | -3.5675 | -50.3164 | 2024-12-04 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| eb0382c0-1587-34ad-8562-38c5e2a9cf4a | -2.8975 | -51.8133 | 2024-12-04 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0322a061-f5a4-3c7c-8a74-f345b395d526 | -2.8196 | -53.0629 | 2024-12-04 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| a5b32b45-3f32-3c2c-aafb-33b2faf435c0 | -1.4768 | -53.7947 | 2024-12-04 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| ca390af1-be14-3e75-97a5-70356179b096 | -2.9795 | -45.1891 | 2024-12-04 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fb2fcaa7-7ec8-34e6-bd91-8589c5d2bbb2 | -3.058 | -53.28 | 2024-12-04 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 91c1917b-9aaa-30e5-9df9-64c2f1297bdf | -4.1222 | -43.9529 | 2024-12-04 00:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 26dbd479-3cc2-34bb-b5ed-d478afc4fa63 | -10.0107 | -36.1108 | 2024-12-04 00:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 112.2 |
| 3cbceda6-efb5-33bc-bcbb-00fbf097b6a1 | -2.8013 | -53.043 | 2024-12-04 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 06fc8e2c-2dc5-3a1c-bcbe-474d68d75655 | -5.4714 | -35.5817 | 2024-12-04 00:30:00 | GOES-16 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 54.6 |


[Clique aqui para ver as próximas entradas](README8.md)
