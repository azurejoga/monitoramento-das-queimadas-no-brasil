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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33266467-e5fd-3220-b7b3-e0e014936e0d | -17.6415 | -46.4227 | 2025-10-16 13:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 1a31c366-ff08-3f6a-910d-fefe59f3b81e | -10.133 | -44.5777 | 2025-10-16 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 332.3 |
| c9eaeadb-c783-3fc3-9f4d-574423d71082 | -14.1343 | -51.1942 | 2025-10-16 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 79504328-9ba7-378f-b2d9-86d40b38e691 | -11.2862 | -44.0226 | 2025-10-16 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 800facc5-6e10-3e1c-9e10-155ef617ec36 | 1.8401 | -55.7232 | 2025-10-16 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 438d9853-918b-36a5-8d3b-e0395c874436 | -12.7993 | -50.6595 | 2025-10-16 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ac0c0750-b27f-3ad5-81c5-b5ec49dbb91a | -14.1749 | -47.9477 | 2025-10-16 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 0e18c45a-15c6-3d3a-93a5-c776b854ae05 | -14.1339 | -51.2157 | 2025-10-16 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 08dacbf9-0d1b-3c66-a2bc-f0884a0753a4 | 1.7479 | -56.0791 | 2025-10-16 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 8826a573-9c75-397e-a85c-b6d103fca9e5 | 1.8402 | -55.7034 | 2025-10-16 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| e4b7f8f7-ee1a-35d5-b32d-8ac67abb1246 | -12.3112 | -45.6311 | 2025-10-16 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| df11f54b-9cb8-3785-93f0-75570fe929cc | -12.9905 | -47.3442 | 2025-10-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 17b320fa-5a35-3ec0-8dea-e02d1fe8f429 | -4.3874 | -43.3827 | 2025-10-16 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 223.9 |
| 7607d0da-4ea3-3066-b8c4-31a5c9cb271c | -12.2847 | -47.1094 | 2025-10-16 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 6ee2dedf-179d-3416-acba-a234e0ee938b | -12.9909 | -47.3217 | 2025-10-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2299c2ce-af23-3344-ba88-7acddd3f2353 | -12.9179 | -47.1078 | 2025-10-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 029735e2-4264-3854-a663-466ea30883ac | -11.907 | -46.8251 | 2025-10-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 8ed358a4-1d69-3e2d-800a-e3bab9789ca7 | -4.3872 | -43.406 | 2025-10-16 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 0fdf7292-7f10-3076-98de-76211f5ed944 | 1.0766 | -51.0196 | 2025-10-16 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d61a3f1f-bc30-36d4-a955-62062df4fdfa | -4.3687 | -43.3838 | 2025-10-16 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 1eda8484-f978-3055-8c39-cd21e033fade | 1.0398 | -51.0407 | 2025-10-16 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.9 |
| a626adf6-c24d-3524-afd7-858d4e737e1b | -12.8184 | -50.6571 | 2025-10-16 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5cddfc11-8595-3721-8f80-32bfae8ae129 | -11.5921 | -44.0472 | 2025-10-16 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e45954ff-ffe7-305a-9dcd-083e82a0c967 | -15.3269 | -45.0439 | 2025-10-16 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f6742416-2fc9-352c-93bf-b6149be0d2d5 | -11.4364 | -44.1876 | 2025-10-16 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 457.3 |
| 6ab5e5a1-6edc-3826-8e1f-6a69eef3daa9 | -10.5834 | -47.42 | 2025-10-16 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 57d7a408-db5b-3dcc-9163-fe2d075236f4 | -11.2862 | -44.0226 | 2025-10-16 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| a3230a2f-128c-3ce4-aa3d-897c2af0db25 | 1.0582 | -51.0198 | 2025-10-16 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 78311dd7-8c4e-3a1f-927f-f43ffd2c4f80 | -9.3596 | -46.9813 | 2025-10-16 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3323758e-49a0-331c-9f04-4651883fca18 | -10.6539 | -45.3151 | 2025-10-16 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2a387e0e-e00c-3e55-ad17-ca304d9a79c6 | -10.514 | -43.3815 | 2025-10-16 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 17e9dbc5-20fc-32c4-8ba2-ad509e8a6dad | -13.4609 | -47.923 | 2025-10-16 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| de38e0d7-3df0-354b-b8f3-16ca3f17d460 | -3.7441 | -41.6977 | 2025-10-16 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| dc597b57-fe5d-3799-bd06-1f0c6bed83c2 | -10.6543 | -45.2921 | 2025-10-16 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3c5567a5-784c-3e6c-909b-c16469228feb | -12.2919 | -45.634 | 2025-10-16 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 44e44db4-a29d-38ed-b8ca-7652b58d2e27 | -12.7989 | -50.681 | 2025-10-16 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bcb50351-324a-32c0-b5a7-2563514b7c98 | -13.4412 | -47.9483 | 2025-10-16 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4862ee27-f356-3a9e-8c8a-e20ee621c8f4 | -9.2255 | -48.6 | 2025-10-16 14:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e9cd9ec0-0611-310a-b48d-dc224ce4618f | 1.0582 | -51.0405 | 2025-10-16 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 467d56a7-9211-3c95-b1a3-c7fdaf8cf610 | -11.7027 | -44.2879 | 2025-10-16 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e5b900e9-6750-329e-bfe6-b8e3f7f5b0ad | -9.6782 | -44.5196 | 2025-10-16 14:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ba08a048-781f-321f-a31d-ef7c1b0e9b9f | -10.6169 | -45.2512 | 2025-10-16 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| d5d996ef-448f-38c5-95eb-103479fa1851 | -10.6021 | -47.44 | 2025-10-16 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 401.0 |
| 776c3602-1289-3596-ba73-78adedb6a206 | -10.1333 | -44.5545 | 2025-10-16 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 297.5 |
| 01e4fb4e-b13d-35d6-adee-1243adc72de4 | -11.3603 | -45.2646 | 2025-10-16 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e1d32aef-a608-3064-be21-25438f492416 | -10.5331 | -43.3788 | 2025-10-16 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a7f6d405-5459-302c-90c6-8c1fb89579e2 | -10.6214 | -47.4155 | 2025-10-16 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7e4a71ed-275d-3f0f-a086-f4f2edc4c374 | -12.3107 | -45.6541 | 2025-10-16 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1da0c4c5-6189-3670-92c8-49a3ebbca799 | 1.8585 | -55.6834 | 2025-10-16 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| f105d526-ad86-3cf0-b1ba-c33965461848 | -10.4949 | -43.3842 | 2025-10-16 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 23db7ab5-f622-3e87-a913-ab5f741fadb5 | -9.2288 | -46.8841 | 2025-10-16 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 7e6550e2-db3c-33ad-81d4-0aa335ec8ba7 | -9.7162 | -44.5149 | 2025-10-16 14:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| c3022ba9-f370-3335-becf-2985e771168a | -10.8289 | -43.9482 | 2025-10-16 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| c73c069b-b545-3df1-a8e5-093602b1177f | -12.7801 | -50.6619 | 2025-10-16 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c9df7e10-93f2-3766-9730-b5dde79e4327 | -6.0971 | -40.8778 | 2025-10-16 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 10560eda-15ad-38d8-b61a-5d3cd455b1aa | -9.3788 | -46.957 | 2025-10-16 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 08111090-7a12-37e6-b0b6-44a22d2b20a7 | -11.9073 | -46.8026 | 2025-10-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 672b1379-7a6c-3274-9b59-60febe0668dc | -14.1749 | -47.9477 | 2025-10-16 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 3cb5cc6e-3721-333e-9651-e6604216e17d | -12.9372 | -47.1049 | 2025-10-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 442d02e4-fbb5-3c1d-afd2-1014abc7c60f | -13.4605 | -47.9454 | 2025-10-16 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 8fafaf3a-7d0a-3880-94b9-d0dc626b9701 | -10.1143 | -44.557 | 2025-10-16 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 281.7 |
| 854d1946-a4f2-3927-94ee-d0a60978fd64 | -13.0743 | -46.9717 | 2025-10-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c8dc33f9-4242-3d34-b5e6-934939dff14a | -10.6024 | -47.4178 | 2025-10-16 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 08366689-b1ef-3b30-a30c-94a2731166c0 | -10.133 | -44.5777 | 2025-10-16 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 359.2 |
| 8fad9d57-33eb-31b0-bd65-d4fbc2256158 | -10.673 | -45.3125 | 2025-10-16 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| a68895b0-93db-3255-a18c-26e71c668030 | -9.3599 | -46.959 | 2025-10-16 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 98e964a9-d7c3-3f9f-bc63-823afa58c003 | -11.1403 | -45.8665 | 2025-10-16 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| b0d62d0d-bba8-3617-bf1e-2db9e5f6ef6a | -12.2747 | -50.0144 | 2025-10-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 542c5d0f-2c05-39d6-8b12-bfadfd8b1a28 | -12.8404 | -50.4824 | 2025-10-16 14:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 15347046-69bc-3621-b1ae-647de9dbe1b0 | 1.8218 | -55.7431 | 2025-10-16 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ae1760d0-fb98-3d2b-bb68-888756eef33a | -12.7993 | -50.6595 | 2025-10-16 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5de06bd2-72c0-3934-bdc2-9dc6bda21c47 | -12.9565 | -47.102 | 2025-10-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ca1dbaa0-42d5-30db-b84c-4416f5862503 | -10.5144 | -43.3579 | 2025-10-16 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 7b8b9690-5a0e-391b-8114-a7ffe44a77b4 | -3.7628 | -41.6967 | 2025-10-16 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 2a163385-ffc5-3117-98b1-0b4fa28d50e7 | 1.7851 | -55.7436 | 2025-10-16 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e41fd014-317f-3db8-8ffa-e427d9e851ce | -12.2941 | -49.9904 | 2025-10-16 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 27af2285-5f0a-3ee8-819c-1484987839bd | -11.5724 | -44.0736 | 2025-10-16 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 59048b85-2e0d-3cb7-a826-6a0acf4d92fa | -12.7996 | -50.638 | 2025-10-16 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 253cea79-a955-39aa-b8ec-34b3d1899cb6 | -13.2535 | -43.752 | 2025-10-16 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9eb801a4-3115-38a9-979b-48e8300aa363 | -4.3874 | -43.3827 | 2025-10-16 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 79c6470d-03d7-304b-9312-aae46eed25d5 | -14.1343 | -51.1942 | 2025-10-16 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| d79429c9-72be-3b81-bd67-c89f8d546af0 | -5.5472 | -41.3128 | 2025-10-16 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| cbb71f6f-7124-3685-91bd-d573e0273a04 | -10.1139 | -44.5801 | 2025-10-16 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 450.6 |
| f8b9a6cc-c956-36b2-b4d2-7cbed1d04b8f | -12.9716 | -47.3245 | 2025-10-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| cbfb048a-16ff-3430-ad85-98acd3b429c2 | -12.9905 | -47.3442 | 2025-10-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1d6c1afd-2309-302b-a2e1-f3e14d73dd97 | -4.115 | -42.2011 | 2025-10-16 14:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| 2c7f86a7-bfbb-399d-8629-540556e68bbe | -3.7439 | -41.7217 | 2025-10-16 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 28d63d2d-47c8-3012-be56-4c90ac9ceb47 | -4.3685 | -43.4071 | 2025-10-16 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| fd23583b-5c96-3ae7-926d-156f5eb6b9cc | -13.9127 | -45.5808 | 2025-10-16 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| eaa0d33a-c986-3440-af72-927f10f3a2f3 | -12.3112 | -45.6311 | 2025-10-16 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 53e3c2fc-e9bc-361d-8bab-7c2be22e70cc | -9.3788 | -46.957 | 2025-10-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| fb96c9d4-2d62-3820-a8c5-1b63d759a15e | -4.3685 | -43.4071 | 2025-10-16 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 3a8dd7c5-41b6-349c-8525-ec1a380c64a4 | -13.4609 | -47.923 | 2025-10-16 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 02c4315c-f7ae-3df3-980c-c3058d041b78 | -4.3872 | -43.406 | 2025-10-16 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 289.6 |
| f74598f4-4be7-3e3d-af81-50434b32fb44 | -13.4605 | -47.9454 | 2025-10-16 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c9561618-cf6f-3be7-86a7-79c277f90d51 | -10.6024 | -47.4178 | 2025-10-16 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d3a2151e-faf7-396e-949e-45334bedf265 | 2.0782 | -55.7789 | 2025-10-16 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 05a15898-c7bd-34d1-a333-999fed1b796b | -12.9716 | -47.3245 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 0d05a233-44b9-349f-919f-c124f65ed664 | -4.115 | -42.2011 | 2025-10-16 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| eb4e52f4-4835-33d2-aff0-ffbcac0c40b7 | -12.9372 | -47.1049 | 2025-10-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |


[Clique aqui para ver as próximas entradas](README93.md)
