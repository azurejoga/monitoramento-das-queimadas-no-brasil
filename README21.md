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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64910d4e-7abf-3db8-b196-302df96ef1c5 | -7.76518 | -44.03682 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 40341f3e-0155-3eb6-8009-bdff7f477e4c | -7.01926 | -42.74741 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bf59e78d-dd4e-303b-98ea-14f8e8fd4d7a | -3.53376 | -48.9167 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2f971d8-8849-3d8e-96ad-036550f40f86 | -7.69445 | -42.96794 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8353ce89-478c-358d-9261-0bdaec28a8a3 | -8.43733 | -47.19315 | 2025-10-09 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f8d4d5e-44a4-3ae9-908d-0f367d37c21d | -8.53229 | -46.19319 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8650e397-c402-3836-ab3f-68d6563b4f42 | -9.49763 | -40.6223 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb6ca97c-48f5-3886-a214-2e729e607304 | -6.46116 | -44.58382 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ca0280f-67b6-3e74-a3f8-ea40608c1bb1 | -7.76456 | -42.40059 | 2025-10-09 03:57:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02bd656a-e09f-3dbb-8f69-5c6afcade7de | -6.69513 | -46.30922 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 7957f3fb-58e0-3bfc-8d80-873e788ede3b | -6.45648 | -44.57861 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bc648c3d-2294-3481-b426-73153df35b14 | -8.5058 | -46.16993 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cde1afa-8669-3409-a908-cea3753ba188 | -9.05701 | -41.73582 | 2025-10-09 03:57:00 | NPP-375D | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0127847-406f-359c-ae78-794ec26bd5d5 | -9.08666 | -47.95142 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bec546d6-270b-3eb6-97a3-3cc9bd2100a6 | -5.41599 | -41.33905 | 2025-10-09 03:57:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6a8e1844-84ca-3572-81b7-4c35b09c6a82 | -8.22824 | -44.15698 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20d3a246-45bb-318e-8a72-66b90a1dff51 | -8.62462 | -45.13214 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58873c0a-4c8a-3c87-a000-48441412faef | -10.19902 | -44.57121 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab08d2e5-bec8-3b3f-b89c-0be493b6f79d | -8.56382 | -44.62209 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7079904e-48cf-3d74-b82b-b8b87e48a488 | -8.55461 | -44.62507 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72090c0c-42aa-3bae-bce5-d7d80f5ef947 | -7.73252 | -42.40882 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9b0ec3ef-9acc-3375-99d2-f7fc0aba015f | -8.50955 | -46.17616 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4dc7026f-aa42-32bf-a415-887706aa2001 | -8.67495 | -47.07039 | 2025-10-09 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d3c809a-0a3c-3f91-972f-4fc830ae70df | -7.78874 | -44.19871 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 828d5bc6-bde5-3e9d-940b-3e919f330735 | -5.40267 | -40.98304 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87cf7306-ce26-32c4-bdc5-92d0f935da5d | -9.21697 | -47.85558 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c47e465-8615-32f6-83bc-d5119946fd86 | -8.54191 | -46.21292 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 939fcb85-70f1-33ac-9f1d-7103902b12c1 | -4.69058 | -45.83943 | 2025-10-09 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1785671-bb40-3188-8367-adfa1d6a0d31 | -3.85863 | -41.53104 | 2025-10-09 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 769e34a6-89bf-3a56-8643-40b84f0eb872 | -4.7225 | -42.95041 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b2d66e0-426d-3b45-aedf-292371349e6e | -7.5559 | -44.29852 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2607d16-4c4a-3cac-9fe6-e63145d4e1ae | -6.68535 | -46.30755 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fd7e156b-4e92-3d7c-8d87-50e5c26569ac | -4.9021 | -41.52162 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 889fe0ab-5ca1-333b-b16a-9bc631489d56 | -7.48652 | -43.11014 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 37a787cf-3625-3647-aa23-d57d21b5bd60 | -5.29919 | -43.05624 | 2025-10-09 03:57:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc31867d-b68d-3b61-ada9-34981b158db5 | -8.59835 | -48.24587 | 2025-10-09 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe2e6c0c-0f47-3d6d-b48d-7a7695d83f77 | -6.65511 | -46.48502 | 2025-10-09 03:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa666439-1826-3984-9f03-770a198205e2 | -2.37785 | -47.71174 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 583320b0-410e-3d44-bbb6-088baf88874e | -9.21871 | -47.84623 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb5524ad-4bc2-3ed5-93ae-612e66ff197d | -7.76038 | -44.04012 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0ad8e7ab-3ae1-34ee-8673-e09db722306a | -9.08498 | -47.96078 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 64cdf6e4-283d-3f43-9256-a89ee153f557 | -6.72665 | -42.86416 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| db94b9b5-a2f8-3871-8ed0-8cd5bada78f1 | -7.27819 | -41.97663 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4f1280af-8773-32ec-8815-8b9ed3ad6b31 | -6.96682 | -40.96904 | 2025-10-09 03:57:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b44e4a53-bee5-3899-bf42-490b19bab4b3 | -8.18666 | -43.33134 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| d9b847c0-0c44-3dca-bda0-5de92fea0dd2 | -8.19724 | -43.36364 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b773a1c6-5a24-30ec-b0c9-a82ad4cab665 | -6.69605 | -46.30384 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 22d7eee4-6ace-3add-8df6-fdfebec6729f | -6.13341 | -39.30516 | 2025-10-09 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f36e101c-e50c-3715-bebc-ba5495f99572 | -9.98133 | -43.5975 | 2025-10-09 03:57:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f5e9be6-6a6f-3345-91d7-44ef79689b0e | -8.97702 | -40.557 | 2025-10-09 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ff3be79-4389-35e3-91de-77a94d036036 | -3.85344 | -41.53931 | 2025-10-09 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3733e879-3c42-37fb-bb74-4a7acb6feca5 | -7.48986 | -42.72925 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9ee933d6-9250-3de5-8594-121cae1e20cf | -4.4391 | -43.23088 | 2025-10-09 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a992f83c-7ff5-3ab0-a118-088604a502ac | -7.76931 | -44.0375 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7505a438-b026-303e-894f-440f04fbeb1b | -8.15913 | -43.32923 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10736e34-b88c-3e2a-bae9-b10daf25a0ed | -5.13757 | -44.96244 | 2025-10-09 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fce0db7a-a239-31a1-bee2-0c8b4ad6aebe | -9.98991 | -43.59403 | 2025-10-09 03:57:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 392ba923-f5d8-3045-a32e-5ffe2080ec87 | -8.22886 | -44.15327 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2993f6a-ff1f-3552-ad70-dde7ded2678d | -7.48845 | -43.07515 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 28276340-86b0-3847-82d2-fc0a342a2ad3 | -8.50144 | -46.22227 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 8fed7e92-f963-3d5c-a224-593d06487b79 | -9.08954 | -47.96227 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1409cc20-cd73-339a-bd1a-3b8ed1358d1b | -8.55956 | -44.6216 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d4b7acc-d42d-3267-a643-c05eb7440ff4 | -5.29862 | -43.0598 | 2025-10-09 03:57:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd3f7339-68e4-34e3-9333-291b62a43eca | -8.53799 | -46.21524 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| bf87a2d5-efc8-3719-a400-e47dd65e9b25 | -5.80964 | -44.67995 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 460911ef-c0d4-34c0-b47c-eb615c010a90 | -4.25681 | -48.57241 | 2025-10-09 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfcaf9e1-2fd9-39e0-a517-0d72b7c97ec3 | -6.79344 | -50.49527 | 2025-10-09 03:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 165e5c12-8ef7-3fa0-8683-971c3c959d8d | -7.72206 | -42.37969 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 08718424-d830-33d9-8c1d-d6536939d8b9 | -8.50616 | -46.2231 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ce1cc2f4-2edd-3055-9cb8-722c2209ca37 | -6.6866 | -46.30887 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4a305060-9574-3d43-af6c-14562e029d50 | -5.7138 | -44.82366 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0076b05-b84a-31fa-9e2a-075e4bc04aab | -3.36114 | -43.3772 | 2025-10-09 03:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08094017-6659-3fbc-b8d0-2eafca97b6fe | -10.19685 | -44.55936 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20a96451-3ebf-3f3f-adca-fb857a6bc80c | -9.17045 | -47.81629 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 626b8e49-5617-3f2b-bcbe-b8fc95d6520a | -4.58579 | -37.80739 | 2025-10-09 03:57:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 933a21b7-4b7b-3e83-98f3-88af569f0f69 | -7.99808 | -44.46811 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 870fb110-1dba-3c27-91dd-fde1a587714c | -3.53297 | -48.92136 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e19f8787-2fe1-3a12-b791-f15c385f4af2 | -5.95965 | -35.58068 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a3d9084-b31f-3a3b-bfbb-199e70f41d2d | -7.76583 | -44.03308 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ef3bbf20-2754-3f5e-9084-8fb52ce05fc6 | -8.16304 | -43.32996 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 203243ea-e37c-3714-8318-48a8a0347b15 | -7.75344 | -44.03115 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0d469efa-7e50-35d4-8ab4-a514ec26cacf | -6.42215 | -43.77422 | 2025-10-09 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eddb277b-137a-3460-8a3f-e2b2f4897277 | -7.78021 | -42.39856 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 97e41714-a8e0-3b6d-8518-add266bff417 | -8.18258 | -43.3335 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6df6d0fb-6194-3dc9-ac20-fab8285b3ba3 | -6.72502 | -42.87408 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| f58c3aa2-cde5-31fa-8506-b40255e642b8 | -9.17159 | -40.30488 | 2025-10-09 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe153b3a-3da6-323a-856c-d42c5739de6c | -3.39125 | -50.14014 | 2025-10-09 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24814d29-e2d5-3b36-ab65-9c4c8c8acd40 | -3.10586 | -47.79819 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9bdd8b81-73f9-36f8-b247-b7f3ec7eb5c5 | -7.77722 | -42.39349 | 2025-10-09 03:57:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 436ee6b2-06f8-3046-9d9f-f5203ecf8113 | -3.89623 | -44.91139 | 2025-10-09 03:57:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c29e1ce8-c026-3101-9ab0-85fb7af000ca | -5.79989 | -39.24149 | 2025-10-09 03:57:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e01b9de0-39dd-3996-aa31-9438b2c96517 | -5.63445 | -35.45299 | 2025-10-09 03:57:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cf2d7955-7df3-3b1e-a3e2-654a88fc6acb | -3.90399 | -44.34456 | 2025-10-09 03:57:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4854c9ad-6e72-3a3c-8b53-d5e586b44f19 | -9.22241 | -47.85511 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a84d41d-d465-3f02-a6a6-36f76160ce75 | -8.53228 | -46.21989 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| f113fccd-b750-3792-a9db-cdfea17e4ad0 | -7.11323 | -41.75635 | 2025-10-09 03:57:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2d6a2d19-91da-326b-a7ce-2a95544fed50 | -8.54181 | -46.22093 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 560e0de3-9854-3ff1-941f-cd176e5e685f | -7.17794 | -46.71901 | 2025-10-09 03:57:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffbe1a31-2321-3239-9e25-5c9ad2ce5432 | -8.20061 | -43.34393 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 2f1cbde5-0667-3a3c-a66f-5f2bc8233b89 | -3.11159 | -47.79919 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README22.md)
