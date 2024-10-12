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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d913c42-6822-35d6-90ee-ae03a3908745 | -4.73111 | -60.79554 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d8ddc7c-8941-3b54-88cc-981fc15d84a9 | -4.72998 | -60.78101 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 592313d8-1c0b-3e1c-b20d-8134e1f609ed | -4.72943 | -60.7845 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dfcc8515-3961-34d9-b920-6ddcf948ff93 | -4.72887 | -60.78801 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f4ba3b5-c8ba-30fe-b9b8-41d88c993c16 | -4.72777 | -60.79501 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094f8a1c-74b8-357e-b5fd-3e7051d908cf | -4.72687 | -60.51973 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 434e38b3-ac84-3d19-94b5-74233e5fddce | -4.72664 | -60.78048 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d35c0b87-c15f-3f90-b64e-77c139cd5b5e | -4.72609 | -60.78398 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cef9b84d-9134-3fda-be20-79779f3d18c9 | -4.72553 | -60.78748 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d1aa7e8-6800-3051-8b20-4621b1a360cd | -4.72443 | -60.79448 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3fecc0a-167b-3cf4-8c8a-f760285a41be | -4.72354 | -60.5192 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61054d8e-5a64-3d01-97c5-64b376bef7f0 | -4.7233 | -60.77995 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb33ce94-0c26-3456-99c8-dc491dbcbef1 | -4.72275 | -60.78345 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9acddd5-35f3-38a1-a6e4-6bf5c685b4e7 | -4.72219 | -60.78696 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaa47575-26f3-30e2-bdb0-762f704dfa7d | -4.72168 | -60.83354 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32eb8f5c-e8b5-3b2f-a42d-51ad463f5c44 | -4.71998 | -60.80096 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a62c244a-62c8-305f-9550-d7dd0c58b336 | -4.71996 | -60.77943 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b93bc71c-96ff-3ac9-b547-e3f1d9d76374 | -4.71941 | -60.78292 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4eee9009-5cf3-331d-9192-73dc207cd4b8 | -4.71889 | -60.82951 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83ed6cf6-d3ce-3bfc-aa55-8f98029ad4dc | -4.71885 | -60.78643 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfcc13a1-9b54-3929-b54e-03e3c3e10d58 | -4.7183 | -60.78993 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22cbb6cc-0d12-31ac-b660-2cdf3098f49a | -4.71799 | -60.51121 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f9c4fe6-15ef-3167-949f-2663c849bcc9 | -4.71775 | -60.79343 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcfa84f8-db24-3ab0-8984-3d29bdece1aa | -4.71719 | -60.79693 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56324235-55b1-3eac-bfe8-59c3524ca7f9 | -4.71664 | -60.80043 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c08f138-4df9-3ad8-8d5d-f5cf26ca9bf9 | -4.71555 | -60.82898 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1735b3c9-c608-3432-b34b-9ffce0b58a37 | -4.715 | -60.83249 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c329fcd1-a729-3ce3-b517-58bbcb422634 | -4.71411 | -60.51416 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32e7c9c4-68ba-3e4a-9010-702b373927a3 | -4.71276 | -60.82495 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c314c67e-f5cd-39e7-b1cc-0f22c4d5863c | -4.70998 | -60.82092 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca91be7d-a64a-378d-85a0-2638aae00222 | -4.70942 | -60.82442 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9425763a-c310-3233-bb2c-809978e6d8a4 | -4.7083 | -60.80988 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61b8cb75-26c4-394e-8400-6f3d09d435cd | -4.70663 | -60.8204 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ce2f563-842c-3c79-9aaa-23d85ab182f1 | -4.70551 | -60.80585 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 335fa6aa-b07c-3304-8461-81d2684e4433 | -4.70496 | -60.80936 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4d16eb5-5ceb-30a9-81fe-218372801a26 | -4.70329 | -60.81987 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d00f522-1f0d-3401-8e67-2b05e828dee6 | -4.70106 | -60.81234 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 175859fd-c8ae-376c-b322-6d58a45f753a | -4.66488 | -60.61716 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba2c0c77-6a5a-3db9-9fde-1edd2d352f0c | -4.47372 | -61.07655 | 2024-10-12 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53247fe3-95d7-325f-9185-4fe2417b9a06 | -4.47316 | -61.08009 | 2024-10-12 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 054ea5bc-bc9d-3586-9718-4c2700296e38 | -4.4698 | -61.07956 | 2024-10-12 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a1bd8a-3cfd-3a1b-a89c-1cad2af4db8e | -4.00358 | -60.38877 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abde30a8-97b4-3d7a-b373-f9498dd88674 | -4.0019 | -60.37783 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0ef1115-4f5b-3beb-9f4c-8b72e7243f05 | -4.00135 | -60.38131 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2e321e5-0db6-3c3e-b3b8-10d00ff5b031 | -4.0008 | -60.38478 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9444b093-5b28-38a6-8d51-6c2d324235d4 | -3.99692 | -60.38773 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64ef3194-7370-3d06-8d7c-a2c0ee660564 | -3.99637 | -60.39121 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b901fcf7-256a-3589-ab36-64be4b5aa730 | -3.97993 | -60.53841 | 2024-10-12 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7267226b-7c10-3932-b54c-fccd05093afd | -3.81475 | -60.74503 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3744a83-db5e-3cad-a26b-4b78b1c55fd7 | -3.81419 | -60.74854 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5839c943-304f-3391-b082-af0dff50d3b3 | -3.81364 | -60.75205 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35766381-d5e4-3754-95ca-60e9c6e35775 | -3.78077 | -60.71107 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cf4700b-c284-3388-81f7-3bd69f28b38b | -3.73165 | -60.63148 | 2024-10-12 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43ba67cf-b23b-32af-a3c0-17cc812ddd5a | -7.93326 | -61.55508 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35bf0a69-08cf-3c6f-906f-f455a4e1d444 | -7.92992 | -61.55455 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c05c2a33-4a5f-307a-91a9-bfb092c76593 | -7.92601 | -61.55754 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb641c4e-91e2-38fa-b840-427412e69b9a | -7.90609 | -61.46765 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aeaec202-b136-3600-ae21-6925f39e50f4 | -7.90603 | -61.51095 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52266b96-f6ab-32be-8f76-bbd2719ce641 | -7.90276 | -61.46712 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 532a3f8f-dadf-3fc2-9e74-62900b7e7837 | -7.90219 | -61.47064 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44c2da08-ce2f-39a9-ae60-1832f62eb188 | -7.89179 | -61.66441 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 413ef0b5-7def-3fd5-94c5-05b97d769849 | -7.89162 | -61.47255 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7430282-fd30-322d-8b8b-1822e1ba6a2d | -7.89106 | -61.47607 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b82b94f0-f59a-362a-8583-d42377b985da | -7.83637 | -61.50359 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8684e18d-a1ca-333a-9124-e374312368c0 | -7.82226 | -61.63531 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37af27e8-0a17-3847-88eb-950f7bbec369 | -7.81993 | -61.69305 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffcfc553-b3f3-39bd-9c2f-77f0e4440ccd | -7.81947 | -61.63124 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0673f26-a336-345b-8354-95c58c5a0760 | -7.81891 | -61.63477 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a12e3720-3a61-327b-86f5-b52829a8d507 | -7.81835 | -61.63831 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 387b3538-750d-38b6-8793-3e98976210aa | -7.81778 | -61.64185 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 974c1400-1200-3391-a59e-c22d71e2b0aa | -7.815 | -61.63777 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62850e42-224e-389f-aebb-f1f55fb06241 | -7.80774 | -61.64024 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28aee3e5-28cf-3166-871f-21b2eb37a81c | -7.79908 | -62.39231 | 2024-10-12 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89d3b5fb-d658-3d5e-a5ce-d1e55d523ea7 | -7.79568 | -62.39177 | 2024-10-12 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 976710cb-dd4f-3e28-88c5-f100f40f4c1a | -7.73269 | -61.45469 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88a3c0d4-424e-30d9-b6c8-89b448a2d223 | -7.73213 | -61.45821 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4454d0f-febd-3b48-b228-f163bc7c8f3e | -7.42566 | -61.5355 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8ecb5c3-b7a6-3da4-96b2-1821c858a6de | -7.98012 | -61.21715 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea9cc921-ee3f-31a7-b4e8-f176264980d1 | -7.97957 | -61.22064 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21180367-1164-3f6d-b54d-d764ed2c54c1 | -7.97679 | -61.21661 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d172de6-07a9-3fb1-abb8-abf614f0e6c6 | -7.94239 | -61.26131 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 179ba369-3220-33ba-acc1-d9be5c083eb2 | -7.92795 | -61.26618 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed05c1c6-45d2-3891-8070-93e66ac2ae3f | -7.92739 | -61.26968 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c38447e-1556-387b-aff3-1ea0833acad7 | -7.92462 | -61.26566 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 670031b0-b4cd-313e-b9ce-1e61d52fedf9 | -7.83092 | -61.36577 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b712f7ce-9b14-3878-89a2-efea7678483e | -7.83036 | -61.36928 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| decf3313-c1e5-399e-bf4d-0d6069b3a9d6 | -7.82989 | -61.22195 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cf4a4ee-0f0e-3c5c-97ca-b63afeda418f | -7.82933 | -61.22545 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b0430e7-1aa7-3ac7-a8f8-be29b8e16542 | -7.82657 | -61.16426 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a78fd2bb-c455-3bdd-a4c6-2cf572c99693 | -7.82656 | -61.22142 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e46f21c-c881-3ac4-b1e3-15764051016e | -7.826 | -61.22492 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7980aace-47b7-35d2-8ad7-0e30eac65822 | -7.82324 | -61.16373 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2427c5ea-1402-30bb-9676-5ff5dadf1671 | -7.81991 | -61.1632 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c784089-c9ed-3484-9209-fcd625670f47 | -7.77943 | -61.18184 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 974c10f8-e025-30cd-8a65-43549e021e1c | -7.77666 | -61.1993 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 235ef0c9-6e36-3413-8622-8ce51ecd432a | -7.77612 | -61.3536 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ca02ba8-e7b8-344d-b4a9-dbaacc3e35e0 | -7.77333 | -61.19878 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92e5dd30-1fd5-3b92-954c-38cfe9643622 | -7.75169 | -61.2276 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90e9717e-2e64-3f6a-8e83-1e13be28d768 | -7.74836 | -61.22707 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9353ef60-b765-3144-a090-9281fb5b2641 | -7.74503 | -61.22653 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README113.md)
