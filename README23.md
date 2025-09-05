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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 223b3afe-b753-3ce5-ad45-5ebd970fffef | -6.24917 | -43.28267 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6cf1e93b-8454-356b-8118-44835f6aec14 | -6.65687 | -44.10122 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59949ae6-eecb-305c-94ad-53513854ff8d | -6.27112 | -52.82252 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed6253d7-6c62-3f02-8a22-4ae41cc822fa | -7.2581 | -41.896 | 2025-09-05 04:34:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 941662f6-99cb-3a73-83b8-9bb3ea93a621 | -5.53797 | -43.77637 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 622cfb22-6eb6-355d-9b06-4f988e5f8294 | -5.54617 | -43.77298 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3003892-8a01-3237-899f-5b6a9a2b62e1 | -6.02723 | -43.69703 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3a45791-1ba4-344a-a042-989f1d5724f0 | -6.24817 | -45.16002 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c98e65a-baa4-36db-b93b-b63ba4a34cba | -5.21046 | -43.70035 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c27d9fb7-86d3-3985-a27e-b98951a22755 | -4.16759 | -46.82082 | 2025-09-05 04:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3699a7b5-88ec-326b-b344-bc64891ae718 | -6.24393 | -43.29391 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8044525d-7853-38d3-9bbf-cc7c43404e51 | -7.34597 | -46.26835 | 2025-09-05 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfbe6c51-f1fa-39f6-8f2c-2f40d4324efe | -4.17427 | -42.03252 | 2025-09-05 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| be596a69-16b0-3506-8293-4e491660b946 | -6.78933 | -44.49642 | 2025-09-05 04:34:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 898b4696-2dc2-382c-a858-b4fceaf41d91 | -6.16572 | -44.31175 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a2f0294-b38a-37b2-aabe-1b9324f8ed9b | -6.11408 | -44.15242 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dacb046-abb0-3e35-8d95-2d0af7301177 | -6.13719 | -43.31008 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0923ae2c-3f8a-3744-8cda-c893fe4986e8 | -6.81291 | -45.6586 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb23e0cc-756a-33f0-a91f-c990595068f6 | -5.90165 | -43.36675 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37f90399-dc5a-33c6-ab24-02f05cf0ba72 | -6.3884 | -43.83179 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| befad384-f48f-366f-a46c-3638a1e86b4b | -7.98086 | -44.51617 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c898c03a-1b20-34d4-ac3f-1f961b3466dc | -7.22508 | -44.82869 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 747fef94-fe9e-3e49-8ec6-e0363628f198 | -5.99062 | -44.77062 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 450c5c06-f029-3976-9717-cf8e98a013e3 | -10.91544 | -50.81998 | 2025-09-05 04:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aac7403-5715-37ae-be1a-218b7763310a | -11.39675 | -43.57662 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8d7f7ed-6279-3085-b9f5-39706ff9b143 | -12.46824 | -48.0927 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8499ace8-bdf1-3ca6-9d17-a303d59380bd | -8.01273 | -44.77382 | 2025-09-05 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84a89465-2d0d-3fd3-b915-5da293258120 | -13.73711 | -46.93036 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f807e595-debe-3ef2-ac80-d758709fe69a | -9.70048 | -48.98931 | 2025-09-05 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5c6ad2c-78ce-389e-beef-c01ed047486e | -11.88132 | -51.54535 | 2025-09-05 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b7b1d4f-0786-3a52-a01d-47d39ef17647 | -11.61112 | -47.78542 | 2025-09-05 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f107f6ab-d905-35b8-8604-e0ad1856e4fa | -9.76117 | -46.91452 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c97edf2f-46e8-3853-a8c5-e41b55c8ddcd | -12.87496 | -48.01152 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69c8134f-e8a1-3360-a396-b1d7a3b82e35 | -9.43992 | -46.8057 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27698f47-04fc-3580-9ada-fcfd74fcb7ab | -12.32365 | -47.04744 | 2025-09-05 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ffa24e4-1fce-35cf-95d6-246a555d78f5 | -11.64688 | -52.22056 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2340b43a-64eb-3820-ad71-bbfeb0561eeb | -12.90366 | -48.02732 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 483f9318-a7c9-3af3-8e5c-7bd01d0424a9 | -11.86316 | -51.45785 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a59a7ef-681f-3dde-a418-f9bb76a138a4 | -12.51586 | -53.83564 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bbedd6a-8d75-3c77-9932-b82610af3e72 | -11.92757 | -46.66412 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5887828-40a9-3523-8275-4c2e12ff56ce | -5.48415 | -60.13232 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 537f6802-c768-322a-9277-3fbfe3da6fcd | -12.71472 | -45.08547 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 60515652-365d-3325-81e1-5cb0b7140c79 | -8.77617 | -49.62761 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee997b54-cc75-3141-ace1-211c65708a02 | -12.48967 | -53.84653 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 640bcc36-e49a-313d-a93e-3cf1940c2698 | -13.85675 | -46.26251 | 2025-09-05 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9b96a9c-9edc-3b8b-8276-2d4b8756bfe1 | -9.07664 | -47.01318 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ba0a30a-7d5a-3e3e-b6a6-cede9ef6a8c0 | -11.00805 | -45.93216 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54551dc6-ddc5-3080-8105-05244176ccc9 | -8.52346 | -51.33097 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ac5f337-bbd2-3dc0-88d1-8443b2461812 | -7.97474 | -46.33803 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d04229f-3693-3d99-9034-804386984c9a | -13.85312 | -46.26195 | 2025-09-05 04:36:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75c0fd96-9db2-3982-b68f-a4b41e4d5dda | -11.97173 | -46.77481 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e96ca36-4823-3266-a885-02e8944dae75 | -12.51924 | -48.07486 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f754891-495c-3ab8-b077-bb32b2ed63be | -9.0693 | -47.01586 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63de9fac-f39c-3dca-82ea-902e2439ccb4 | -11.86667 | -51.45839 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3288291-484e-382c-9709-ab09aafc88be | -10.9709 | -45.98516 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7febdfad-8c2b-30df-84ad-3094ae8a2626 | -11.72275 | -48.34968 | 2025-09-05 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cfbc14f-032e-35e6-88cd-917b96198d93 | -9.71565 | -51.07752 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aeac6064-06d3-3b52-92a7-3a34dc4f7ddd | -8.34418 | -48.30848 | 2025-09-05 04:36:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 874e6970-a2da-3fd6-a2d7-2b889bb3bf3c | -12.91158 | -48.04337 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3c95908-9ab4-33a0-aad0-dd6d2b3d5648 | -8.52195 | -51.31759 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bd4ac5b-6108-3f21-b06c-57ff3b15705f | -12.98946 | -48.05876 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a92c41f8-f6a6-3a8b-855e-82bd450745e1 | -8.52706 | -51.33155 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1fc46a2-9a65-3397-8abb-9602967755c6 | -8.44818 | -45.09379 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3de96696-992f-344d-95fd-ea532660e610 | -11.67812 | -52.16743 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93aa4908-8165-3e1f-8fc0-172567ee2276 | -7.69377 | -50.29341 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a55fedcf-aab1-33bb-8c9d-8a36ccb6f32e | -11.6149 | -52.18869 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75b27150-f09e-3cc6-993b-33a7371fbad9 | -11.00169 | -46.02324 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5fe6442-9ee9-3399-accf-83a841c17981 | -9.38239 | -50.3887 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b829590-6275-3aec-85b6-67376da3f486 | -12.52483 | -48.06098 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cbba70f-c713-3f5b-bf34-a3ec4a22989d | -11.5876 | -47.89271 | 2025-09-05 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de5f6258-7533-387f-8727-5510165b46ab | -12.29346 | -50.01956 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b561977e-721c-36f6-9656-838ac3a56a25 | -8.1832 | -47.41929 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c3a89b7-6be8-3afe-8ba0-9a52f7ff0c08 | -12.11478 | -43.34563 | 2025-09-05 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dc1a959-aa69-37bb-bdf2-687242cac1f1 | -12.9656 | -48.05169 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f69a142a-0574-399c-a51a-02ba969c6969 | -8.00581 | -45.44157 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23ef06d8-a5f8-3976-88f4-ef9480f1915c | -8.35349 | -52.54829 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01347d5b-522d-335f-96a3-0720d92cdec9 | -7.23329 | -56.85484 | 2025-09-05 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a024b5ec-84ad-3880-ac33-148e3c9188bd | -7.79867 | -52.13601 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa45b8bb-c887-3479-9c26-0f548032d368 | -9.98236 | -51.62675 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c15fb3a-4b81-3461-ad88-dbe4817bf7de | -10.9886 | -49.77615 | 2025-09-05 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3150ef2b-c991-33f0-baf0-048abda281e7 | -10.1398 | -55.16515 | 2025-09-05 04:36:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad632564-af67-37ba-bf20-7712c75f4405 | -6.33143 | -58.17258 | 2025-09-05 04:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1992891f-fe85-33d7-a2ea-d57997bfbef8 | -8.87838 | -47.92469 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69da4d4b-ce34-39a3-82ed-ac04ae46583d | -11.63601 | -52.2186 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6cf57319-b69f-3431-a443-df7919ef2b3b | -9.71732 | -48.3054 | 2025-09-05 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2708d655-9649-355e-bb88-68303790efc0 | -9.07887 | -46.9987 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc69d233-cc56-36a9-a8bd-128e4572b7c2 | -5.50314 | -60.12333 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2169cc95-68e2-3364-bcf3-6d6ae215e154 | -13.2964 | -46.84562 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b863776b-bcff-33f0-9cdd-5acdfd10e8a5 | -11.39107 | -43.58732 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7bd5fa8-c5f9-3fbf-850d-cd0c4731b0a4 | -13.74538 | -46.92308 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14e3e976-edae-3a51-83e4-986ce1d1d939 | -11.64863 | -54.52959 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e54fec43-901b-3abe-8404-dfaff2a7bcbe | -11.62655 | -52.20819 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41ee6f5d-b423-3d4a-95c5-ab8a9fb824e0 | -10.03472 | -48.14042 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 807db908-c8d8-37d6-a875-c8f6ffe89990 | -8.01115 | -45.45435 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08788bd8-9f57-3511-a3f0-e8ed9a16a471 | -9.70071 | -51.05869 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55c7e46b-8f70-387f-85bf-b33f9212fad2 | -12.52427 | -48.06462 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13aa00b7-e52c-3a2d-96ff-351c516673ab | -10.47831 | -53.62763 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d3cdd56-4f45-3dd9-a252-e37d2789b474 | -11.92523 | -46.65574 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1088d675-ccd3-3c38-986d-3b7903287fe3 | -8.75384 | -46.1109 | 2025-09-05 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87ea1119-e2a7-3354-9fff-9e3b4ce3b13a | -13.467 | -46.83444 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
