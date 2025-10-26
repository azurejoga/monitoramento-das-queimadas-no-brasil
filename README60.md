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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0fa8604-595b-3f01-a303-00040757c7cb | -7.8884 | -47.259 | 2025-10-26 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 7bd20ea7-5382-3470-b85e-a1530a1b2fea | -4.912 | -43.2337 | 2025-10-26 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b28403d7-b378-32e5-b834-2d49a5aa55d9 | -4.8935 | -43.2115 | 2025-10-26 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| ca6cf4c2-06dd-3155-8fe8-7d15c3050c73 | -17.4311 | -46.884 | 2025-10-26 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e2663bf1-bcf2-32b0-b8e3-117b2728f8c7 | -12.2977 | -47.4658 | 2025-10-26 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a927c6d7-b774-3b49-8e22-093b90c6c909 | -13.6249 | -48.4323 | 2025-10-26 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| c2c60d16-37ca-36b6-b6eb-37d6804b9263 | -7.795 | -43.9913 | 2025-10-26 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 641f0431-aee8-30fb-91bd-a997725ca37c | -4.3426 | -41.7828 | 2025-10-26 14:20:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| a43f086b-476a-360c-a288-59b11c564636 | -6.3866 | -45.7594 | 2025-10-26 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 77a230eb-c06d-37cc-ba52-4911ffbd0293 | -13.2777 | -54.3882 | 2025-10-26 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 198.9 |
| 8915800d-1e5b-3f92-899e-dcf8446a0711 | -13.2482 | -47.9768 | 2025-10-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a5e79402-1eea-3389-8e7b-fda33fbaa987 | -3.964 | -45.4173 | 2025-10-26 14:20:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d3f8c109-4e2c-319a-ae69-4362963cf676 | -7.2382 | -44.964 | 2025-10-26 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d6bc212a-a8e6-3fa6-8c36-e3c727a881b7 | -9.2042 | -44.5305 | 2025-10-26 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 4936ec86-a88f-33d9-8bad-1537d9047327 | -4.8933 | -43.2349 | 2025-10-26 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 261.4 |
| 20275149-15c7-316a-a8b6-d3e1beaaabcd | -11.1419 | -55.1869 | 2025-10-26 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 32d7a2dd-238a-3e6e-8f2f-29e23c48f602 | -14.6031 | -53.1087 | 2025-10-26 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| bbe92e90-4f79-3e36-9878-89b87817bdbb | -11.346 | -53.9236 | 2025-10-26 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1997ef60-817d-397d-add8-edcc78c80964 | -12.3169 | -47.4631 | 2025-10-26 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 9771fa97-0cfb-32e8-9500-3583cc764913 | -7.1581 | -45.4253 | 2025-10-26 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 65d9ddf5-f38e-31eb-b47c-c79ddb564f5b | -7.3424 | -42.4418 | 2025-10-26 14:20:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| d5d6c6d2-1d28-3de5-932f-2e22a5115a42 | -8.0446 | -46.7353 | 2025-10-26 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ad80986f-e384-3acc-a29c-731e31f6c910 | -12.3634 | -48.1016 | 2025-10-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| eef82880-d5f8-35d5-8c85-c995fb48ac8e | -5.5908 | -47.1045 | 2025-10-26 14:20:00 | GOES-19 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a18b6a5e-4833-3675-91b0-c302cdda1893 | -16.1901 | -45.0841 | 2025-10-26 14:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 3936a911-4948-3570-9dce-6f3a701768db | -13.2586 | -54.3902 | 2025-10-26 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| eda49ad5-0f37-35ed-9cfb-e81fdcbbcccd | -8.0443 | -46.7576 | 2025-10-26 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 61ca1030-f618-3eae-8123-db151860f630 | -5.834 | -40.828 | 2025-10-26 14:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 1252f565-af5b-3d4a-844d-a8971961329e | -6.2567 | -41.8298 | 2025-10-26 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 166bc464-6364-3a96-a730-678ce34a5cb9 | -7.121 | -45.3833 | 2025-10-26 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 0af1d4f6-1cbf-3faa-a348-e2fbffaaeee7 | -17.3158 | -43.6674 | 2025-10-26 14:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 9d34af70-3ace-3d90-ab78-4ebeb7003998 | -7.4578 | -47.2082 | 2025-10-26 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2f1ce9fd-8eb2-35af-ab62-81d5c984c13d | -16.1703 | -45.0881 | 2025-10-26 14:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b147753d-bd4e-3b78-b671-9c8d6222aea2 | -13.8945 | -48.4586 | 2025-10-26 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c59dc8aa-4ebc-3863-8f5c-fca9d4fe7a5a | -17.4317 | -46.8608 | 2025-10-26 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 5e8be5ce-f6fa-3648-a6e5-f13be0322568 | -6.5417 | -41.5876 | 2025-10-26 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| a963edcb-c018-38ff-9763-c6309090869b | -7.4229 | -48.7812 | 2025-10-26 14:20:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 4cfaad8c-174a-30ff-bfea-6a72eedf4b07 | -3.7896 | -43.4153 | 2025-10-26 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f810e320-e197-3889-8554-8d4d81e17de9 | -4.3239 | -41.7839 | 2025-10-26 14:20:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 0e3605b1-fcf8-38af-8eec-092b7dccffa9 | -13.8949 | -48.4364 | 2025-10-26 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 27248271-b7de-3d30-86e2-150ea73b823a | -4.0338 | -46.1965 | 2025-10-26 14:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 76651cb1-39f3-37ce-9acd-9cbff0132efa | -11.327 | -53.9254 | 2025-10-26 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 8dbd97ed-3d19-3a37-ba6d-085c4bcd6691 | -7.8138 | -43.9894 | 2025-10-26 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 0d667702-d616-3a24-b909-7b93bd5b9e31 | -13.0315 | -47.2033 | 2025-10-26 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b35429c6-7965-3da5-a71d-87341499dd2d | -6.3864 | -45.7819 | 2025-10-26 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 8d6b3e1d-c018-3ad6-aef1-259b8fdfda37 | -12.363 | -48.1238 | 2025-10-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 9bbe5da9-94e0-395c-9085-f126ea6df312 | -6.5062 | -45.0041 | 2025-10-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3110b42b-bc6a-395f-99dc-865c5854a713 | -5.014 | -37.8416 | 2025-10-26 14:20:00 | GOES-19 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 140.4 |
| 8623bcf3-a3e0-31ee-ad0e-64cae862557c | -3.9166 | -44.0097 | 2025-10-26 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b1ca7dbd-f77a-33f7-8140-972ab6fa1088 | -4.8931 | -43.2582 | 2025-10-26 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| b263163f-9710-31e1-9bbb-df4f4d31c2cc | -13.547 | -49.5434 | 2025-10-26 14:20:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 94b0d066-72ba-3413-b9d4-5f42a19a818d | -14.3168 | -51.7901 | 2025-10-26 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 84e17ccf-4ed0-3c49-bed7-8ffa8bb6dab7 | -3.7024 | -42.3892 | 2025-10-26 14:20:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 674b8fc7-22c1-3b29-b84a-e14bf5dfc9f2 | -2.9961 | -41.6859 | 2025-10-26 14:20:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 1fab2248-bb17-3eb1-8d7c-76cff3b56ac0 | -7.8413 | -46.4423 | 2025-10-26 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 95cf082a-7ba6-38b2-bedf-ce681aacc4da | -3.0148 | -41.6851 | 2025-10-26 14:20:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 154.8 |
| 411d4b63-0163-3801-a207-f0f5e7fd3238 | -6.4053 | -45.758 | 2025-10-26 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d28b716a-ed40-3b33-aef5-c131e81d72cd | -6.4051 | -45.7805 | 2025-10-26 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 07cd4d31-abda-3015-9083-1b287c37c9f4 | -7.7971 | -45.3893 | 2025-10-26 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 629a88fc-b38c-301c-b788-69cf1ff66556 | -6.5605 | -41.5859 | 2025-10-26 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 05a9168b-57ee-3088-8be3-dc5370071cf7 | -6.5414 | -41.6117 | 2025-10-26 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 6f62131f-ca09-3c47-b59b-16a9f1bc7fb2 | -4.4787 | -43.6789 | 2025-10-26 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 64af0f95-d0f4-37e0-a91c-db785bc68d40 | -6.4051 | -45.7805 | 2025-10-26 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 50883298-8eec-30d4-876f-a939a17fcbeb | -13.8953 | -48.4141 | 2025-10-26 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a9254453-0687-3919-89c4-19e12a7ebce7 | -6.9388 | -44.8766 | 2025-10-26 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b1252d6b-b415-30f7-9265-fc504e329e32 | -11.3268 | -53.9459 | 2025-10-26 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| d07173ee-ea0b-3353-a124-da599920b93d | -7.2382 | -44.964 | 2025-10-26 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 2995a025-c6ca-35b2-a1a2-8c68b0ff168a | -3.5439 | -43.9818 | 2025-10-26 14:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a0fdf846-1b46-3648-896a-1f54069bb1bd | -4.8935 | -43.2115 | 2025-10-26 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| fa814913-caee-348c-a458-93aba9c9c2bc | -5.6221 | -43.3934 | 2025-10-26 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d6e61a9f-e079-31a4-9bca-e41a99b8659d | -6.3864 | -45.7819 | 2025-10-26 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 212.4 |
| bce79807-4b05-35e4-914c-458a79642ccd | -2.8994 | -42.3552 | 2025-10-26 14:30:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 6b16e048-d6f9-3abc-8dbb-1893c15fa90a | -3.7896 | -43.4153 | 2025-10-26 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 160e5979-c2fb-3aa5-90b3-bc471d29bf8e | -9.8624 | -44.8886 | 2025-10-26 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 69eceac3-5ef4-3efb-bcf6-90e77d3b63d6 | -8.563 | -47.3948 | 2025-10-26 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| d4472e25-9ec3-3e9a-a551-ead459161b83 | -17.4311 | -46.884 | 2025-10-26 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a0d0567f-7f99-3222-afd8-d5a49269db5f | -8.6715 | -44.775 | 2025-10-26 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6260a6ed-8eb4-396a-b083-f3afcf7de022 | -7.6737 | -46.3236 | 2025-10-26 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9fe408ec-0777-3321-85e3-f09a81118fef | -7.8696 | -47.2606 | 2025-10-26 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1147f692-6a55-39a8-982e-7e94dd2fceed | -3.6956 | -43.5359 | 2025-10-26 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0bc58329-4e26-3bda-92d2-25859b33eec3 | -6.257 | -41.8059 | 2025-10-26 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 217e6470-c2d9-373f-a4ee-16e918dae5a4 | -2.9181 | -42.3544 | 2025-10-26 14:30:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 730efc35-cbf8-30b9-9c21-d4e549bd3841 | -9.2682 | -45.3712 | 2025-10-26 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| f9123316-c6f7-35e6-aa22-b79af6406041 | -3.6531 | -41.2705 | 2025-10-26 14:30:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 09c1060b-b368-3566-b82e-30da2bdfac2d | -7.4578 | -47.2082 | 2025-10-26 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0b0ff722-63d7-387a-8133-edd0354bb152 | -9.2728 | -46.4101 | 2025-10-26 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b4d6fcfe-2084-3f99-a743-9f5ba5e28d78 | -8.0443 | -46.7576 | 2025-10-26 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 3ffadb40-65da-3c2c-bb1d-99518c868099 | -14.6031 | -53.1087 | 2025-10-26 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| dd545e85-82df-3da4-b7d5-5df2d430062d | -4.8931 | -43.2582 | 2025-10-26 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| c4f076af-fce2-3089-8292-fe877cf50c77 | -9.1981 | -46.351 | 2025-10-26 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 7b564c37-7b94-3751-a465-95b6367e6faf | -13.8949 | -48.4364 | 2025-10-26 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| dd0ff913-9baf-307b-94c0-0e5aa6edcd3e | -3.403 | -42.4748 | 2025-10-26 14:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 6c2d89f9-d641-349f-8b53-65cdb62ec845 | -13.8945 | -48.4586 | 2025-10-26 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 757b2b91-ea0f-3d20-bd09-73b56f72a275 | -3.7024 | -42.3892 | 2025-10-26 14:30:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 14d08d8c-40ac-307f-9e76-e8b98f95c62a | -4.2019 | -43.1838 | 2025-10-26 14:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 77142b74-08ac-3ca5-803a-da644592e2ef | -7.4231 | -48.7596 | 2025-10-26 14:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c61bd87b-b79d-3cbe-9999-b68cc9e03529 | -7.7971 | -45.3893 | 2025-10-26 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 6b7094b6-d274-329d-bcd7-03b2626e7af2 | -9.5078 | -45.8206 | 2025-10-26 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| be5b90bf-9d72-3762-9ac0-753a86fade46 | -10.4065 | -45.3244 | 2025-10-26 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c7f14e62-8be2-39d4-8c45-753c68d2936d | -9.217 | -46.3489 | 2025-10-26 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |


[Clique aqui para ver as próximas entradas](README61.md)
