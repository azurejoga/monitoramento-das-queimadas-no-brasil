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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e869545-a9d2-301e-8b5a-f224e67b9aa7 | -4.59216 | -47.7239 | 2025-06-24 12:25:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7713e3c8-1db0-3af4-9256-0f70aeba68e5 | -4.54093 | -48.01223 | 2025-06-24 12:25:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 50f0bd34-2508-3fdf-bd70-f1f84ce9c778 | -3.03061 | -49.42571 | 2025-06-24 12:25:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0b8566fc-4fc7-3a29-bc1c-3baf116bb9df | -7.74829 | -47.5937 | 2025-06-24 12:27:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6bb4cdfb-ac95-3ae7-b4dd-da0fad947a30 | -7.02449 | -44.56935 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 190.0 |
| ac18ed95-9130-3d2f-a196-8d0c0f56c9f2 | -11.18074 | -48.6114 | 2025-06-24 12:27:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6edf4823-3307-368f-93fe-95c251306650 | -9.50566 | -45.43931 | 2025-06-24 12:27:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6549c77a-1f10-3868-89d8-bb2d0dc5832c | -10.50775 | -47.58229 | 2025-06-24 12:27:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 23565669-4246-3a9a-91df-35bbc1464a3a | -8.05663 | -43.10688 | 2025-06-24 12:27:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 8a4fa37b-1176-3d39-a6fd-a27129b4b72d | -9.92107 | -52.44561 | 2025-06-24 12:27:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6fa756b5-7216-3759-b8ba-6ddb0ebb6e41 | -12.32385 | -50.0561 | 2025-06-24 12:27:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0ced0a46-60d9-398b-8c74-c583c79a9bf0 | -10.50902 | -47.57332 | 2025-06-24 12:27:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| efa5bd28-2834-31ff-944d-ef244342b0a0 | -11.75219 | -46.32634 | 2025-06-24 12:27:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f168810f-8fe1-3282-b6b8-f1f67832259a | -7.02606 | -44.5582 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ed613f3e-289b-390a-8116-584672086652 | -9.88832 | -51.12463 | 2025-06-24 12:27:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b22a3429-ba36-3008-a23d-bca4d1b2ba06 | -5.78677 | -43.61307 | 2025-06-24 12:27:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 39ed7791-d78b-382f-b70f-5693a0dc96e7 | -11.92831 | -47.83834 | 2025-06-24 12:27:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f1f29184-7483-3816-bf59-9fd976492526 | -6.23203 | -43.34893 | 2025-06-24 12:27:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0767b7fd-5984-3b5a-b70a-c56d4b76b327 | -7.08559 | -49.59012 | 2025-06-24 12:27:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e24191b2-7785-3bd8-9017-0e7c8cf069ed | -11.76148 | -46.32762 | 2025-06-24 12:27:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3d30ab37-4f0b-3a01-9f88-9e1c54a3487e | -5.91782 | -43.47717 | 2025-06-24 12:27:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 585e41e9-8cc2-3640-b3f6-2ba19cb48fd4 | -4.94637 | -47.56469 | 2025-06-24 12:27:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 29b95382-5df9-37fb-86cd-8512d12ecb9b | -9.88654 | -51.13613 | 2025-06-24 12:27:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| be7d7726-8b14-337d-a941-8627087e83f9 | -11.18828 | -48.62166 | 2025-06-24 12:27:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 2825a20c-697a-3cd7-a261-361d4bf3a455 | -10.85778 | -44.79268 | 2025-06-24 12:27:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8ecb1b44-701e-3b7a-890e-c281ebab2fdc | -8.5605 | -51.55936 | 2025-06-24 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 645398a3-1add-3409-9665-e1f90b4727b4 | -12.31474 | -50.05471 | 2025-06-24 12:27:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9e4a6c91-887c-3e2f-b4e8-0381f1bc733e | -11.5786 | -44.66627 | 2025-06-24 12:27:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 01062cd7-7839-3310-905d-b10e37a016ef | -6.37391 | -43.65696 | 2025-06-24 12:27:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 973d7321-5ca6-3fa3-ab26-6622c6633900 | -10.7204 | -48.85301 | 2025-06-24 12:27:00 | TERRA_M-T | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0887d455-be30-36fa-90ed-363b92ca171b | -7.88262 | -47.87835 | 2025-06-24 12:27:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d016424b-4406-3c0c-9b1b-32795250031f | -11.8069 | -43.7856 | 2025-06-24 12:27:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c18beb8d-8720-362a-afd2-61483a4f2d26 | -7.01633 | -44.55704 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e1547137-c1c4-31d0-8750-49a7f6f54707 | -8.06388 | -43.11568 | 2025-06-24 12:27:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 7475a1cf-63b3-3cdd-acae-5e2f6cb407a2 | -5.7911 | -43.7338 | 2025-06-24 12:27:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 99f147d6-ff2c-3a64-8dba-9c06f0bcb54a | -8.06756 | -43.10831 | 2025-06-24 12:27:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.2 |
| ddf555b2-b77a-3cd4-9b27-61a9e8fb2a9f | -7.85358 | -47.11182 | 2025-06-24 12:27:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48881a3b-ee27-35e1-a08e-f861d1aef10f | -8.06579 | -43.10168 | 2025-06-24 12:27:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| f863a07c-efc7-324b-90f9-8e2ba5ee1f68 | -11.0995 | -46.64556 | 2025-06-24 12:27:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e90e0716-fce0-3bc2-be06-0cd369260299 | -6.23031 | -43.36164 | 2025-06-24 12:27:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f59a3fb4-cb6e-3210-9738-6b025dc5fb9a | -11.66873 | -47.71824 | 2025-06-24 12:27:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8161c5cb-b1db-3293-bc23-2592ff82756b | -7.74702 | -47.60255 | 2025-06-24 12:27:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e1c2ff05-63a6-36a8-9d43-139e871cebc8 | -8.06575 | -43.12231 | 2025-06-24 12:27:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| b43b0d54-2aa3-3334-bbe5-b7b26f7add7a | -9.92323 | -52.43163 | 2025-06-24 12:27:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3c90c46e-853e-3eea-a60a-7c2a94bb64c6 | -10.0574 | -49.65677 | 2025-06-24 12:27:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1380e25d-09e0-34e3-8ba0-5addc170c412 | -11.92703 | -47.84737 | 2025-06-24 12:27:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 86b72de0-8c75-390f-90f8-57fab11cf84c | -8.67941 | -51.45471 | 2025-06-24 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 85d2f61b-dc14-321c-b4ba-2515ebe56544 | -8.47085 | -48.39832 | 2025-06-24 12:27:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 26d2e2be-614c-3888-bb75-87eda652f3c6 | -8.68353 | -46.20126 | 2025-06-24 12:27:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b5cc7d1-f617-3557-8872-3b735e7df289 | -7.27208 | -47.05619 | 2025-06-24 12:27:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 35ea425f-1d6c-352a-8426-ae99839aea2f | -7.4542 | -45.56475 | 2025-06-24 12:27:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 824f2d27-1c76-3671-a24e-af09bb8176b8 | -7.03423 | -44.57038 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 1891434f-eb07-3fc5-b9f6-a492c72c4572 | -7.01484 | -44.56778 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 895555b5-50fc-3d5b-85e8-8f4ab280805a | -4.9375 | -47.56342 | 2025-06-24 12:27:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| fb287af8-fcd4-3f29-b3d3-44f6a990f4fe | -10.28075 | -47.61387 | 2025-06-24 12:27:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22fb7244-6d74-366a-8b5a-d9b5c6b0de51 | -12.36799 | -41.57753 | 2025-06-24 12:27:00 | TERRA_M-T | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| c67ad116-36f9-367c-8f09-02e353a9756b | -11.17943 | -48.62037 | 2025-06-24 12:27:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 6840dd64-6b60-3b72-a472-6991c3b18fda | -8.64328 | -45.43756 | 2025-06-24 12:27:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 89b9e1e2-de63-34fb-abe2-4724e8443b01 | -7.09408 | -44.3723 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a5522de-dd93-34a6-840d-6de15bf85d17 | -7.08408 | -49.60022 | 2025-06-24 12:27:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0de5c0e0-cc1b-3726-8d1d-47826bf833d6 | -9.86889 | -49.55754 | 2025-06-24 12:27:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 536380eb-9dd5-3f79-9cf6-52c14e9bbefd | -12.37164 | -41.57245 | 2025-06-24 12:27:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 00003f43-515b-3557-9ee3-e69bb1dec014 | -7.88134 | -47.88722 | 2025-06-24 12:27:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| c81d45c4-aab3-32cd-83d3-1427122c8b26 | -7.03659 | -44.57652 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 1c4f44f3-5a2a-3fed-aa0e-1d6983f61491 | -7.03805 | -44.56563 | 2025-06-24 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| d70ce8fd-a624-31a8-bf66-8a7614c29c25 | -10.94986 | -47.38444 | 2025-06-24 12:27:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0de50d6b-af81-36ce-ae9f-432e4115a651 | -7.44628 | -45.56757 | 2025-06-24 12:27:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c70f73b5-84df-32f1-95ae-c0f836a275f5 | -5.78717 | -43.61871 | 2025-06-24 12:27:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7924619a-22ef-3bdf-bf01-1d47581fd5d8 | -11.80505 | -43.79984 | 2025-06-24 12:27:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| ef05e135-39ef-35dd-b3c6-7a05952faace | -14.95985 | -47.29216 | 2025-06-24 12:29:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e8e931af-f82c-3e5e-8fa9-1af6ad73b5ab | -13.77405 | -45.10996 | 2025-06-24 12:29:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7c40a5f1-90c9-3555-8b00-4022f578ed7a | -16.3122 | -43.4076 | 2025-06-24 12:29:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d643cac8-2965-3fed-8c53-763c2bbb6ee4 | -16.30811 | -42.98164 | 2025-06-24 12:29:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fb6769b4-e8c7-3879-be65-e1c0b23970f7 | -14.43777 | -48.91235 | 2025-06-24 12:29:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0c8cbc66-bf72-3596-b782-0c9bceab1417 | -16.30918 | -42.98849 | 2025-06-24 12:29:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fff8aa7f-6b67-3887-871c-84f1d9e88965 | -11.5812 | -44.6554 | 2025-06-24 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1b1c016d-b634-3827-928a-9319683d2990 | -6.1055 | -45.8255 | 2025-06-24 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 5917d55a-dc34-3822-9d74-e2ed0a800088 | -6.2224 | -43.3693 | 2025-06-24 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| c87cf945-893b-39ac-b0cb-3687872f84ac | -6.2224 | -43.3693 | 2025-06-24 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 675b2b47-df95-3884-96e8-22fc41458d8b | -6.2224 | -43.3693 | 2025-06-24 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 2f01903c-2497-39e8-bcb4-4978fc2c25e7 | -5.9522 | -44.1787 | 2025-06-24 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f5561308-489e-348f-a581-e9546c8ba206 | -6.2224 | -43.3693 | 2025-06-24 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1e9c84fa-485d-3116-9fc5-2eb4f624d869 | -10.5241 | -47.5822 | 2025-06-24 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1192558f-4cab-33a8-ae1e-80da1b793f12 | -10.5241 | -47.5822 | 2025-06-24 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d6d53c31-9f84-326d-957e-ae0d16d38a0f | -6.2224 | -43.3693 | 2025-06-24 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e8b0f11a-ab0d-374a-85a9-728f5177df54 | -10.5051 | -47.5845 | 2025-06-24 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |


