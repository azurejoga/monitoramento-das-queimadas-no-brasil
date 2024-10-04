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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e3bd75-a76f-3374-9e19-8e69d5a8a078 | -17.52998 | -46.74088 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79208444-5ad7-3b4f-bed2-58c758e66667 | -17.52629 | -46.74033 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c2230ac-974f-33bf-a281-a0018e5d76a6 | -17.49201 | -47.01755 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80a38d0d-d890-3f34-a19c-1557afafd95e | -17.41455 | -46.31806 | 2024-10-04 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1fc0a0e-1963-3a69-bbd3-d4080c72158b | -17.20819 | -46.86834 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66928e2e-a9cd-314f-b272-3819ccb4d6cc | -16.93525 | -47.12319 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ba5f318-433b-3725-8c1f-895147dcb2f8 | -16.93464 | -47.12752 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| efe69189-dfab-30e6-8931-8f7b249ba95a | -16.93404 | -47.13182 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b757515-11c8-364b-9786-16f340d27613 | -16.93344 | -47.13612 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f2fe76f-a992-350b-8b2f-ac90338bbec4 | -16.92684 | -47.13081 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbce7697-0de8-3cd5-b26d-c60fec1944c1 | -16.92646 | -46.37941 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c368bcd-5296-3c92-9139-5be4129d41bc | -16.9257 | -47.13258 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbe62f51-5ab7-30e4-a659-e3bca3eb7b78 | -16.92519 | -46.3818 | 2024-10-04 04:34:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bbf8e67-1a9d-3fd2-a535-b127a6700643 | -16.92443 | -47.16677 | 2024-10-04 04:34:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ed92648-52a3-390e-a3f9-9f2ca0733a2a | -16.92324 | -47.13026 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e04ca13-c94c-31b7-a2ad-4ccc071a3db6 | -16.92272 | -47.12774 | 2024-10-04 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0894303-f233-327f-9127-a08231b5ce5a | -16.92213 | -47.16451 | 2024-10-04 04:34:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6d2618b-da46-392d-b52f-a269165e83c2 | -16.92084 | -47.16621 | 2024-10-04 04:34:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a32cc2d-928d-3859-a1fb-8847e77409e6 | -18.79824 | -46.64138 | 2024-10-04 04:34:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f11532b-ea95-38b7-becf-f58bf6301bbf | -18.79383 | -46.64554 | 2024-10-04 04:34:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2fc6964-ef52-3de1-9bce-109817536e26 | -18.5711 | -46.44744 | 2024-10-04 04:34:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1c3725c-ae4b-31ff-b1f4-69656e4be5b5 | -11.9813 | -47.36686 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8c7c117-68a9-3339-8ca0-6ee059d24df3 | -11.95183 | -47.40027 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c59e50a2-197d-3253-9f04-24eba649a658 | -11.94898 | -47.39602 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69d6873f-208d-37be-97d3-04a1b013a0b2 | -11.94842 | -47.39973 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c59fae77-11e7-31b7-9103-f812134577c7 | -11.94786 | -47.40344 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55826ac3-81d3-39dc-991e-7f59094586b7 | -11.79195 | -47.56143 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9b6f3fd-cfdb-3d9a-8f78-869b8038a081 | -11.79124 | -47.56121 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d1b682b-a8fa-3c2d-8195-3f8bab4cf23f | -11.79067 | -47.56488 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2ee88c4-f727-35ad-b215-7b82bae00e6c | -11.79029 | -47.57241 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb99c020-d14c-394e-8e62-ebc8f25dfa1b | -11.78974 | -47.57602 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10535a77-4baa-3f14-b023-5109ca2ed131 | -11.78955 | -47.57218 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc0efc42-8179-3950-bf12-c36b6796146b | -11.78919 | -47.57965 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48a0ab7e-3294-31f8-b4d5-b3cc3eb7c419 | -11.789 | -47.5758 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5e18c1c-24b5-30c6-a1be-008e34284b82 | -11.78844 | -47.57943 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f2985d-f208-36b4-a376-040bfc650725 | -11.39744 | -47.21825 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba017930-bf06-3701-8989-16186035617c | -11.39687 | -47.22197 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b16525cd-f7b5-3ed3-9745-c029bc7128f7 | -11.3963 | -47.22569 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1af99766-8a84-3e8b-b9d3-62145e48ce26 | -11.39175 | -47.23261 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 298f23bc-e010-3551-9752-73a5b43d3a79 | -11.38948 | -47.22463 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f00f179e-c546-39df-a876-3f49aec6d00b | -11.38834 | -47.23208 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14397cc6-7459-3a55-bd50-417ad6149a4c | -11.38777 | -47.21294 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fa14df7-fa12-3450-a67c-9ccb4f817642 | -11.38606 | -47.2241 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbec3d1d-78b8-33f4-b252-90cf496df360 | -11.38492 | -47.2087 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f11e1ab-8f3f-3dea-9919-df77596eba3b | -11.38435 | -47.21242 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38321416-5e5a-3510-832d-79f8fe329661 | -11.38094 | -47.21189 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e015a98-18d8-3838-902c-600a09f493ca | -11.38037 | -47.21561 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3813f192-2e0b-3a1b-aa86-ecf7ff5a1ec1 | -11.37981 | -47.21933 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd9b0741-8c7f-3295-8412-78aad636c5bc | -11.37752 | -47.21137 | 2024-10-04 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 388da06f-fa7b-3ee5-ba50-18ca9c26f42b | -11.77319 | -47.68552 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bb3d35e-b375-3d1b-958f-2a20ddf87477 | -14.0646 | -47.90068 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29210d1d-29fc-39c3-ba62-f11c1a1067e1 | -11.77217 | -47.68522 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 523e6452-a3c9-3566-b3b4-d60eb9c5dac2 | -11.76879 | -47.6847 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c59b72c8-d145-396a-b304-10367301af8d | -11.76091 | -47.69094 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27631b2d-f51a-3aee-be89-4f02162fd6bb | -11.76035 | -47.69458 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bcd5de0-10be-333c-9558-87e3412f38fa | -11.72539 | -47.69705 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 897e4714-aaa2-3362-9766-389dec17296a | -11.72483 | -47.70066 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 37180565-e57e-3404-bb8d-ae4d616aca04 | -11.72201 | -47.69653 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4af3997-82c8-3fd0-a3b9-4085097a6802 | -11.72146 | -47.70013 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7e338465-4ae2-35f5-b6d2-363c37fd3251 | -11.71863 | -47.696 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38ef8802-a4e0-381e-890b-cb92c1bd9ce6 | -11.71809 | -47.69958 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 748dcfbf-28f4-382f-9944-08607348b115 | -11.71526 | -47.69546 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 806392da-8b35-3e94-aea0-1276e65bd03e | -11.71485 | -47.74331 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0625398-592f-379d-aecf-7b3d8e970e4d | -11.71471 | -47.69904 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 19e9f836-40b4-3824-991e-83c31b30efdc | -11.71025 | -47.70562 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f96293a-bcfc-3c6b-b570-493bd9daa238 | -11.70687 | -47.70515 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5c95c1e-a248-3582-8c21-644ec098638d | -11.70633 | -47.70869 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2ac4665-ffea-3899-809a-a8fbc033d94c | -11.70232 | -47.68964 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 844f1323-3b9c-3e6e-ad7c-adfb3c601450 | -11.70175 | -47.69341 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4807052c-8015-30e7-84bb-2e3aa9f3276d | -11.69894 | -47.68914 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3db1ecb0-c8fa-3da5-9ded-be963f5ddca2 | -11.69556 | -47.68864 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee133fe3-5758-361b-92da-f883b5d26949 | -11.69499 | -47.69238 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9714eec-d37e-3e23-9119-bca9e65a999d | -11.68825 | -47.69129 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ecec340-e5e4-3ac5-bfc4-3eeb667035e6 | -11.67814 | -47.68958 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ce21b0c-1b71-371e-aef7-7ffa4b3c148f | -11.67477 | -47.68901 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 435ccfba-a7ee-3b22-a72b-b7a7ea8f410c | -11.67422 | -47.69267 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1fec6026-a5dc-3106-879c-d93f29b1df08 | -11.67149 | -47.71051 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ab56ad2-83ce-3c74-b573-d8435dddff3d | -11.67085 | -47.69208 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4ebda04-8903-374d-ae81-5a1577b97432 | -13.73645 | -48.15765 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d65dd638-c3fc-38bc-a57f-3a5dc0e6b4b7 | -11.66693 | -47.69513 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54b4fb12-2700-316a-bcf2-051ff40a6f6f | -11.66411 | -47.69086 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d651f588-7b40-34df-b863-2f1858173118 | -11.66356 | -47.69452 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0388d8f8-453b-376c-9f05-f48f585f06ce | -11.66338 | -47.6913 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3e2c10e-8d03-3192-9a59-8a34ffd953ab | -14.50454 | -49.28558 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52c4f761-579d-3352-8cea-a7149c57ec5b | -11.66282 | -47.69496 | 2024-10-04 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a9e82cd-9819-3b74-a0c1-de507257a8a9 | -13.59531 | -48.1242 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 285e83be-124a-38e4-92ea-dec047a24b3f | -13.59475 | -48.12792 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 484d47fb-69db-3069-afb8-9adeb6519b5e | -13.59138 | -48.12734 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f92eb3f-bc12-315e-8f0e-db6a6b46e15a | -13.56909 | -47.63092 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aeaff32e-8557-31c5-8bc6-9c0015f1da9d | -13.56852 | -47.6347 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2dbf9e8-5d21-31ce-b1f4-0552f965f0a3 | -13.56795 | -47.63848 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b32eec1e-c2cc-39dc-8272-3e9529d635bc | -13.56566 | -47.63043 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc4cbff9-cba8-3725-8a0a-26a0cda0f649 | -13.56509 | -47.63421 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4afcc36-9ed8-3765-95e1-0354bffc3b2f | -13.36469 | -47.55305 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ee5cd5c-32da-3831-b53a-985a3c215409 | -12.88554 | -46.85628 | 2024-10-04 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 252b9c56-e536-3925-8a52-12b927975e2c | -12.79917 | -47.4404 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85cfded2-7427-3bef-9347-62e855b10fc5 | -12.79861 | -47.44417 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 65f1155a-84be-3292-9930-0fd46d329b29 | -12.79575 | -47.43986 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7a4889a8-636b-3e13-828f-3dc0061d60c5 | -12.79519 | -47.44362 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 91b597e1-d9e5-3676-9e7a-cfc6e2cd3fe6 | -12.79463 | -47.44739 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README118.md)
