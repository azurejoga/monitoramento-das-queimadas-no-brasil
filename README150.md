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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f257f92f-6853-3eea-a11e-912bc79335c5 | -8.5458 | -47.264 | 2025-10-04 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c1498de9-4d49-3cf7-acbb-c61d340ec91b | -13.7473 | -51.3097 | 2025-10-04 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 774c16a2-3949-32c7-bb79-dd1c5671c795 | -7.0555 | -42.8018 | 2025-10-04 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| b1fe38cd-cbc3-3b21-8bb3-0e5ffb3c1219 | -11.7924 | -46.8184 | 2025-10-04 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| aacd3b82-7985-3f89-b9f2-3c26fe96d902 | -8.9664 | -46.7557 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| fbabe2e2-561d-384f-8eed-bf7356513fff | -15.7297 | -46.2707 | 2025-10-04 13:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9e895f09-1094-3b38-b9ee-740750480fa9 | -11.7962 | -48.9231 | 2025-10-04 13:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 45a24ada-b205-33b0-b3be-3f941902030f | -11.4414 | -43.9057 | 2025-10-04 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| a06f3326-f6b7-3a4f-837f-4a6e525f2938 | -12.9663 | -50.9815 | 2025-10-04 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bccfe998-e685-3741-b811-b70be02492c2 | -9.1716 | -49.9408 | 2025-10-04 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 1e8fe25c-9fae-3ad2-a38b-c14fea928694 | -11.6841 | -45.3333 | 2025-10-04 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| df5bbc2e-40b5-3f66-a722-db0d94e47c22 | -15.3797 | -47.952 | 2025-10-04 13:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| deb41ba7-f0ff-3cc4-9922-700312ed0660 | -13.114 | -47.9518 | 2025-10-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 386.0 |
| d203db51-b499-3552-ab12-3e9cc01c969f | -7.7679 | -46.2927 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7af3f924-98f6-333a-a557-32b9cd88be59 | -7.7684 | -46.2479 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| b5fb0d8f-a33b-3cf2-8978-fd967369f67e | -13.1144 | -47.9295 | 2025-10-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 790a9113-f224-324b-8417-4b2fa5a766fb | -13.2934 | -47.6129 | 2025-10-04 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 57119c74-717c-3299-a23b-ba4c60a4b972 | -7.7491 | -46.2944 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| d2cdbace-c682-3817-a560-417b69ccd9ed | -7.813 | -42.5349 | 2025-10-04 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 8d21d859-ea3a-3272-9ebf-29f1974db15b | -8.9002 | -46.0459 | 2025-10-04 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a4911290-a96c-3632-8a54-beacaa50ba31 | -11.5069 | -46.7671 | 2025-10-04 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 6c585190-5f39-31f5-9084-834cc20cfc3e | -8.5275 | -47.2215 | 2025-10-04 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f073ea6c-3d2a-393b-b0f5-bf535aa684f7 | -7.6458 | -45.4716 | 2025-10-04 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 07560414-39a8-359e-9dc6-29f94d8f6499 | -13.6717 | -51.234 | 2025-10-04 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 234.7 |
| b0c873dd-9435-32f6-bb67-07b54ed31776 | -11.8442 | -44.9408 | 2025-10-04 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 86d3cf70-5aa1-38f8-9631-002036de358c | -7.878 | -48.2021 | 2025-10-04 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 1813974e-dfd7-37a1-b551-05fc6170af3b | -7.7687 | -46.2255 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4ddacc28-c512-37d7-9397-5fa73b5076b2 | -15.5408 | -46.8344 | 2025-10-04 13:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 171.2 |
| c00ed589-ebc0-33d1-93a3-c1a587bc1a6b | -14.5941 | -52.4976 | 2025-10-04 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 484c57d9-bbb7-3141-8b2a-c9aab9c837e3 | -7.4229 | -46.9682 | 2025-10-04 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ad50be92-bc13-34fa-a277-bef40db5586b | -11.4486 | -43.504 | 2025-10-04 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 338ef667-2965-3618-bee9-94f92393b7d9 | -7.0604 | -45.7946 | 2025-10-04 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 910afa30-0e26-3c3b-8a26-1bb6a858c76d | -7.8595 | -48.1819 | 2025-10-04 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 2052d59a-df41-3e77-8b88-abc9853fd752 | -11.5492 | -47.6773 | 2025-10-04 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1d0bbf2d-d361-36ba-adbe-0a95fa95f47a | -15.5211 | -46.838 | 2025-10-04 13:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 4e0976d7-1256-3569-8feb-88d1f87c4ea1 | -8.8529 | -46.7897 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 716e77e6-b597-32a7-a44e-0221100a040a | -7.7938 | -42.5607 | 2025-10-04 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 139.4 |
| d14a5926-1624-35ee-8d08-188f3a108335 | -13.3032 | -48.1244 | 2025-10-04 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 5f73d511-ffeb-3e84-ac90-059f26cc8b53 | -9.3196 | -45.7515 | 2025-10-04 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| bfceccce-b675-3660-a89e-c1dfd0c9db26 | -7.7682 | -46.2703 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c6626dc7-0d7e-359b-a704-30b01be96913 | -11.792 | -46.8409 | 2025-10-04 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f0a8f5d5-eb9b-31d2-aa82-44943a82fdb9 | -16.097 | -51.0611 | 2025-10-04 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 0f6f87fa-1ed4-3943-a5f6-d9bf042fd868 | -7.0558 | -42.7782 | 2025-10-04 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 163.6 |
| c624f9ba-53a7-310a-afe5-ef8eccfa6cd0 | -12.7194 | -48.5611 | 2025-10-04 13:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1f9e2b4d-81c4-381e-8271-2642d4e62b63 | -13.5115 | -47.2881 | 2025-10-04 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8d6bec4d-4891-3cd9-b1e4-6510007ff51b | -11.5683 | -47.6749 | 2025-10-04 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 3559f1d2-9f86-38b3-bca7-39e4b4eb08e9 | -7.4416 | -46.9666 | 2025-10-04 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| f0a205d3-0079-315e-a67e-d4c819ea5799 | -13.116 | -47.8401 | 2025-10-04 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fcbf60a1-96cf-334a-9f9e-95fe133f7875 | -15.5413 | -46.8114 | 2025-10-04 13:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 6d36b09a-e230-3977-84c2-106cf217a7ba | -8.2311 | -39.6331 | 2025-10-04 13:40:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 08a17014-7b15-30cb-84e8-b6af796f1446 | -13.3127 | -47.61 | 2025-10-04 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fbd41f80-bddb-3473-8df8-114ce0b140c8 | -12.6512 | -46.9894 | 2025-10-04 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 0c39209d-4d0a-3b77-b76b-42cf4aaabc13 | -11.1268 | -47.9077 | 2025-10-04 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 5eff9e8d-245c-371b-a39e-a6b951a0b676 | -8.8526 | -46.812 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 197.4 |
| c86d1a25-b0e2-3587-9d59-9758d9defaa5 | -13.2938 | -47.5905 | 2025-10-04 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 0e54697e-e88e-3770-b1da-63c759e0e0fa | -7.7489 | -46.3168 | 2025-10-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| f3159534-4ce5-3252-a426-5e750708180b | -11.8635 | -44.938 | 2025-10-04 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9c8a3225-616b-39cb-a337-168a91e74f62 | -14.3899 | -45.9601 | 2025-10-04 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d22e9d73-f17d-30f1-902d-15b1daec22c8 | -11.4877 | -46.7696 | 2025-10-04 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| ce6ec61c-b516-3048-9b80-8a135771b9f1 | -13.9383 | -48.1852 | 2025-10-04 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| a33e6fff-42e0-3940-b173-250ea5b322ad | -11.1458 | -47.9054 | 2025-10-04 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 15129d79-31d7-32bf-bd80-a5f9af37cb61 | -12.0891 | -45.1814 | 2025-10-04 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 09c22002-1c05-3a3d-beec-c923f436d476 | -7.5504 | -42.3965 | 2025-10-04 13:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| 3551e6fd-1f73-3b07-a033-c9b7805f45c7 | -12.9471 | -50.9838 | 2025-10-04 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1234c70b-b93e-3552-ba9d-e970061b4727 | -14.5748 | -52.5001 | 2025-10-04 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 9977219c-34c5-3d78-8c99-70231ea8a751 | -13.5119 | -47.2655 | 2025-10-04 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a1e49c9e-176f-3165-9c3a-7fc43a98a6a2 | -14.2131 | -46.0596 | 2025-10-04 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 175.7 |
| b76fedf2-919e-3998-8a1a-7ccd0bfae5ea | -14.2949 | -45.8613 | 2025-10-04 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 80666d2b-e32e-33ae-895c-9d053614361c | -15.3179 | -46.3011 | 2025-10-04 13:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 03bde365-05f0-3038-9574-66eff62777c9 | -10.5838 | -48.696 | 2025-10-04 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cf028315-115f-30cc-8a9d-423c80b3dcb1 | -7.0369 | -42.78 | 2025-10-04 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 215.9 |
| f94c68d7-3053-3ab2-af94-bd016f740716 | -7.4229 | -46.9682 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 98641805-67b8-3fb9-a743-8e9d7fdfc546 | -6.2325 | -44.2487 | 2025-10-04 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ceb7be54-5afc-310d-9d9c-14dc10006dc6 | -7.4414 | -46.9888 | 2025-10-04 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8784aa76-10a5-39f5-aef1-004005689e72 | -7.0369 | -42.78 | 2025-10-04 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 195.8 |
| 07814460-73d8-3ad8-a71d-256d2359aac7 | -12.297 | -45.3574 | 2025-10-04 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| b7993173-15d5-3d41-a684-e81946b07f86 | -15.3797 | -47.952 | 2025-10-04 13:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 4359e33e-b394-3f96-8f72-98b0946cc3d7 | -10.5838 | -48.696 | 2025-10-04 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| cbb3a62b-d054-3d01-b703-dd490c329c78 | -11.7924 | -46.8184 | 2025-10-04 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a9159d59-db25-3c3c-94b3-4f6a99828555 | -6.0806 | -42.5118 | 2025-10-04 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| d7a70deb-b37f-35b6-a1cc-c495eaaea70c | -8.9664 | -46.7557 | 2025-10-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| acf2e111-5970-35d1-8656-2046ed14e454 | -14.6716 | -48.3157 | 2025-10-04 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f1d64928-8f51-39c6-a4ed-0cea37f2242e | -15.5211 | -46.838 | 2025-10-04 13:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 6f8bb2ff-4276-355e-b2f5-d6ef1aaffcdb | -12.3162 | -45.3545 | 2025-10-04 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 54b2eabe-9e5c-3e88-adf3-fc9e0476260a | -13.2421 | -47.2617 | 2025-10-04 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a28b6241-757d-3fab-b226-92b339743bdf | -8.5598 | -47.6593 | 2025-10-04 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 422.1 |
| 20ec2e83-d6e2-33fc-9928-a672a025e418 | -6.0618 | -42.5133 | 2025-10-04 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 166.7 |
| afd25789-1fc8-3cf6-9227-1223b0eb9bed | -12.0708 | -50.8757 | 2025-10-04 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e4067a0f-1b1b-3a97-9dbf-ac76fb4ed534 | -13.6717 | -51.234 | 2025-10-04 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 477286e0-93e0-3f2b-9785-e344c85a81ef | -11.5683 | -47.6749 | 2025-10-04 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 8a510e80-4ef9-3f3b-ac6d-35c1d14def4a | -6.5044 | -45.1859 | 2025-10-04 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 589a349a-e191-3165-a1c4-4094e86491c6 | -12.6512 | -46.9894 | 2025-10-04 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 3e0e49cc-0721-30bb-a8b0-76c1ba3ce364 | -7.7938 | -42.5607 | 2025-10-04 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 165.0 |
| 5e6bd280-fd9f-3c60-a608-eaa96d161bd3 | -12.9468 | -51.0053 | 2025-10-04 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 257.1 |
| 6df9c442-9e52-3299-a7d4-c067b6702fc9 | -8.9002 | -46.0459 | 2025-10-04 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0c19b695-8d4c-3826-9d5d-8be8c0a74eae | -16.3627 | -51.4752 | 2025-10-04 13:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 519668aa-d6b7-374b-b423-4beeb2f7dcfb | -11.792 | -46.8409 | 2025-10-04 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 69b7778e-0474-33db-9e49-fed14f11e72a | -15.3179 | -46.3011 | 2025-10-04 13:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b31dbba5-9bce-3cf7-815f-50b39a301559 | -9.3196 | -45.7515 | 2025-10-04 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 872e5866-c39a-3a40-a763-32fe37e57706 | -9.3276 | -54.5215 | 2025-10-04 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 222.1 |


[Clique aqui para ver as próximas entradas](README151.md)
