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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50e7f8b8-4c94-3bf9-b28a-dd304608aa78 | -22.66263 | -53.118 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66ac9356-5e73-3873-8f36-5b78b9aba4e5 | -22.71661 | -48.71064 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c62b342c-0cfb-3d0d-b676-4ea9f0a8455e | -23.2801 | -46.4758 | 2025-09-12 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b4d7c83-7b9f-3399-b93c-ed343800542c | -20.89417 | -55.17976 | 2025-09-12 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bba649f2-a35e-3b8a-9f6f-46bae810036f | -19.95587 | -49.27092 | 2025-09-12 04:29:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 24f7acf7-3c15-31b6-ae1f-d08cbae76643 | -23.34412 | -47.21678 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2538aba4-c42c-3aeb-b421-5d479dc3f1de | -23.19073 | -49.65464 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a4afd6f4-f7dc-3d7b-900e-38ee33554a5f | -22.70089 | -48.70002 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eb2dd60-0f38-3684-b914-cb183aefaff2 | -23.1591 | -47.48881 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d8130478-c68d-3744-b7ee-33996c838e46 | -20.91068 | -44.61181 | 2025-09-12 04:29:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f07b9ceb-64e7-3712-8370-e2a664c79242 | -22.6414 | -53.11361 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 20e4f5f0-b3e0-3b01-a241-d46b748b78eb | -23.13918 | -49.66122 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d3dc94c-d4d2-37c9-bdcc-be8993b75245 | -19.9797 | -47.62068 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5480f77b-209d-35fa-9df0-842ce1f922be | -22.33769 | -48.81625 | 2025-09-12 04:29:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c06c68b-d059-3d95-b5bb-68d1beca86cd | -23.0912 | -49.86119 | 2025-09-12 04:29:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2c83bdd3-ca38-3417-91c6-773ea60c2e45 | -20.00522 | -46.92292 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08ad9701-c90e-3e33-b11e-e71728dee510 | -20.34945 | -48.40651 | 2025-09-12 04:29:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daa9b8a3-f3c2-3055-81b8-fbe9ed06d8d6 | -23.17567 | -46.67084 | 2025-09-12 04:29:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 85e330cf-d706-3ebe-8ed6-5c27a5027881 | -24.97085 | -51.45217 | 2025-09-12 04:29:00 | NOAA-20 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3adfe26f-c83a-394d-81b6-144c3c0f8362 | -20.57198 | -43.74499 | 2025-09-12 04:29:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 60a36489-8e51-3d43-9e2d-88fa47eec1bd | -21.94893 | -47.55473 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14b5a585-6912-3bac-a905-ee064f0ad400 | -22.18884 | -49.73038 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f08aa034-25a0-36ea-b982-2c5c9affbb16 | -21.57677 | -45.38237 | 2025-09-12 04:29:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7d47a0d4-f70d-3626-be9c-345fbfc7f0b5 | -21.96112 | -47.54407 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35e24922-da84-35e0-b661-2f23f7751884 | -21.70625 | -46.25514 | 2025-09-12 04:29:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ac63843-cc7a-33e6-b472-6276ae309551 | -23.14757 | -49.65112 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 387b31c9-f1a5-3b48-a78c-d8e66799c5a7 | -22.79362 | -47.8002 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23c2086b-f414-33c2-92c3-3f23c6c62c1a | -22.25936 | -49.55785 | 2025-09-12 04:29:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ca78da4a-acf9-32a2-a3c0-0fe9032c1df3 | -23.30414 | -51.12515 | 2025-09-12 04:29:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb3954a1-03de-397c-a5b2-f4bdf5eba871 | -21.95469 | -47.56408 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ccc788d-1617-3112-b628-b5513dbac7f7 | -22.65986 | -53.11295 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4ec2c069-2c9b-3ade-8842-4a9071358f8d | -23.74464 | -53.31149 | 2025-09-12 04:29:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 36ad89a5-4063-3e1c-86f6-651ec97e484b | -22.6109 | -47.28595 | 2025-09-12 04:29:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05a7b87c-8e88-32dc-b348-8ac57779f0c6 | -23.147 | -48.25287 | 2025-09-12 04:29:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8a5ecd1e-5833-3a0e-8c8a-41398a55439f | -21.94717 | -47.56694 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f87d7309-25bf-3dbd-880c-9998a22719ec | -23.12152 | -47.50012 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 3fe3c954-53a2-39c7-b148-ad99f1a77238 | -22.19216 | -49.73098 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 20bbb82a-7a35-3f1c-89f6-ff8429ae05c5 | -24.12235 | -48.70378 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b80c0529-acca-3c04-a015-c392511831cb | -22.15306 | -45.82956 | 2025-09-12 04:29:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e0c77a02-9b32-3dcf-8758-506b3e19dfc3 | -20.56901 | -44.36552 | 2025-09-12 04:29:00 | NOAA-20 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 84f049e9-cd34-3367-8185-83b406d24f30 | -21.94834 | -47.55881 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a08830b0-4fbe-32d1-b26c-6fd290c845f6 | -21.9524 | -47.5553 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a9cc67c8-14bc-33a0-9cd1-7601e67572e7 | -23.4897 | -47.26091 | 2025-09-12 04:29:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b6f25298-88cb-3351-9d22-19e973daafc1 | -21.33942 | -45.02922 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41e6d5f1-44a0-34ff-aa9f-bf9a8ff39ef6 | -22.27923 | -45.38341 | 2025-09-12 04:29:00 | NOAA-20 | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bc9d0151-e21d-3365-82ac-67efda16e3ef | -20.00463 | -47.64093 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af630f5c-0675-3128-8927-6b83a9a5adea | -22.78839 | -47.81187 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ee32f79-1f38-371a-934d-c73bbd27ffec | -21.78288 | -52.13531 | 2025-09-12 04:29:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 70e4d313-5b1a-3577-9527-8680c86ade85 | -20.00873 | -46.92339 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84ccc6d7-56aa-3688-9908-1b14924a9300 | -20.55956 | -46.93423 | 2025-09-12 04:29:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b212b86b-cf36-33de-bf3d-539fcc84a31d | -22.18436 | -49.73724 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 290.9 |
| 70d9e725-d8b8-3894-85cc-dc5deb6dfe3d | -21.64856 | -45.284 | 2025-09-12 04:29:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b72d0060-f80d-32ae-8ae4-8d48f98ff461 | -19.98874 | -47.63034 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31a0c967-223f-38db-a429-feac8750e7e1 | -20.69585 | -46.07559 | 2025-09-12 04:29:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc79329c-ba6f-3e30-b3b5-12b749492757 | -22.83471 | -47.46253 | 2025-09-12 04:29:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f37276af-07c0-3d7d-bef7-59be58ac1c60 | -22.85927 | -46.56245 | 2025-09-12 04:29:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 856f3ebc-5e89-3a46-83e9-d3f7361b7440 | -23.30905 | -47.34529 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d68cbea-d70c-38c6-879d-5ca65322b86e | -19.9967 | -47.64732 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34a0fb72-e79c-321f-9e44-05f9192c2680 | -20.65522 | -46.53377 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3504f505-eb90-3ea2-b325-3230431aa408 | -23.28378 | -46.47641 | 2025-09-12 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f60bf17-475b-376e-aab9-524e8e95815f | -21.19492 | -47.5301 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4ed5197-7d7b-3f56-8a4e-4f2ff45abf84 | -22.91285 | -51.151 | 2025-09-12 04:29:00 | NOAA-20 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c5f2cf2a-4308-32f1-80a7-989246d98366 | -20.23662 | -49.25482 | 2025-09-12 04:29:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 84064dc1-6a3f-393e-b18d-9af5ba5f3700 | -22.78493 | -47.8113 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f487284b-d3f4-3c6a-af94-d1bfcf88c242 | -21.18743 | -47.53299 | 2025-09-12 04:29:00 | NOAA-20 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5d56803f-0fef-3aa8-9e9b-ada30e828d73 | -19.98485 | -47.60942 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cab033c1-d2d7-3809-b9e2-507af159b79e | -20.35622 | -49.95903 | 2025-09-12 04:29:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2257d0c8-f5b4-3669-8349-10e46b8e0aad | -22.18926 | -49.59636 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9422d59-9ade-32f7-b8e6-3809936de957 | -20.01029 | -47.6498 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29308bc8-f924-3549-a5d1-044f1bd196c1 | -19.99534 | -46.91713 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70fd72a0-3024-3b8d-be3e-c664651a1957 | -23.49326 | -47.2615 | 2025-09-12 04:29:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7374c73a-ffa7-38ac-ab82-0711c0c086e4 | -22.19257 | -49.59697 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7cef510e-317b-3e89-85f5-ab320ed000b3 | -22.81729 | -46.42925 | 2025-09-12 04:29:00 | NOAA-20 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| ce5822f6-81c0-38af-9d21-0bc18c100df9 | -21.624 | -46.79575 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fe607e84-5d41-3412-84c7-5179fa94b171 | -21.64916 | -50.11594 | 2025-09-12 04:29:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a372e7ae-73ae-39c2-942a-e688d1207061 | -21.94429 | -47.56227 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 784eab2f-0bb4-3012-8abf-af81bec477e4 | -22.19725 | -49.73837 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e8bc71c-7fbd-3f78-a557-614eef6a8559 | -23.13977 | -49.65742 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0a461569-79e5-337c-9247-95b87d542d01 | -23.10024 | -46.6776 | 2025-09-12 04:29:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 2fabbcda-9935-3308-accb-0eb3e8982df2 | -21.1811 | -47.5279 | 2025-09-12 04:29:00 | NOAA-20 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52a0fbfb-936f-3f6d-9e7e-2572b7e66597 | -20.00293 | -47.6524 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9a1e8b7-f6ca-3d5a-92c1-4ee53837682d | -20.54183 | -47.62495 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b513ecd7-e243-38b7-980d-b00ea3b778d8 | -21.76434 | -47.28245 | 2025-09-12 04:29:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 292b8930-8c1a-360e-9536-82258edeedb0 | -20.46217 | -44.00287 | 2025-09-12 04:29:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b389680c-80ae-3e63-bcc7-cc0e39d4c710 | -20.14767 | -47.38269 | 2025-09-12 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2133dfa5-3cc2-31bb-87df-63ef9e11f789 | -23.49683 | -47.26208 | 2025-09-12 04:29:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c2afe89-845c-3a00-9b6d-11cff5686fe1 | -21.19262 | -47.52153 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 262ed378-7918-3e5e-bf23-fb5753df5d28 | -23.39381 | -46.70766 | 2025-09-12 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f0b85629-1ff9-34e4-b5bd-229931e6a4f2 | -19.99727 | -47.64351 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16c86787-c071-3a4d-9cfc-261974079e87 | -23.13858 | -47.48117 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b0c0d3f-33e8-388c-9459-26dd121199b9 | -22.19041 | -49.58891 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3efcfff4-56c5-313d-b22f-37122c513eb2 | -23.1504 | -48.25357 | 2025-09-12 04:29:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e7e4d142-f188-30c0-913b-3f575516db3a | -22.17831 | -49.73232 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 08b8f94b-6d57-301e-96eb-6e44448d3556 | -22.18984 | -49.59263 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4dd53840-f23e-3b1d-8f16-d03c99e4492d | -23.14035 | -47.46849 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5dcb30c-7db5-3530-bfd9-c2b14bd68052 | -22.69695 | -48.70329 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 93f34f97-8641-3540-b311-484404964b8e | -23.23703 | -49.41826 | 2025-09-12 04:29:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 86de702e-0b08-3f11-82f3-a69f27b49219 | -22.52568 | -45.09849 | 2025-09-12 04:29:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 057f4895-5e13-3bc1-aa26-bff600eb5466 | -21.94199 | -47.55359 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c161541e-3e3c-3581-8901-e6d15ebc2b35 | -21.96162 | -47.56526 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README97.md)
