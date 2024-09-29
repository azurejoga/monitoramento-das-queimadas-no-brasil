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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e62e5c1-c796-39cf-a867-c24505513e5c | -9.3861 | -50.013699 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b64a5ee8-ec63-3a3d-84c6-35ff869e9163 | -9.3878 | -50.021301 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc4ab4c8-1d7f-3401-8ea4-4ef7eb7f7fe5 | -9.3763 | -50.0158 | 2024-09-29 00:47:54 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90dafe0c-a1b3-35ae-9f77-aac4cf93b26f | -8.3284 | -45.6493 | 2024-09-29 00:47:55 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f7dc72c-12d5-3363-8d15-d6951703455f | -8.4092 | -46.348 | 2024-09-29 00:47:56 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed42d98-111e-3572-80bb-0bce930b93c9 | -8.4109 | -46.355301 | 2024-09-29 00:47:56 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10e19375-4e7d-3edc-be96-61ef88d34ece | -8.308 | -45.958599 | 2024-09-29 00:47:56 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 945d1084-3b08-37ba-b94a-6e06af41f8e8 | -8.3098 | -45.966099 | 2024-09-29 00:47:56 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21bae3c7-0d52-3dbe-9567-4e058a282b25 | -7.8613 | -44.589298 | 2024-09-29 00:47:58 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e29cf6a-258a-3395-8e56-622342826b92 | -7.8634 | -44.598 | 2024-09-29 00:47:58 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a654a7b5-f177-3dae-b583-61be360ee937 | -7.8474 | -44.5742 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea8ff3f1-cf87-35e8-b35f-c59c0428c54f | -7.8515 | -44.591599 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae938bdd-1d52-3cd9-ab43-6ec585230c33 | -7.8536 | -44.6003 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd46a60b-5ab5-3715-a8e7-2c9d9059f98e | -7.8356 | -44.567799 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8880e1de-9d4e-3f54-ae05-3d118dcdfdfe | -7.8377 | -44.5765 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 685a6f83-e17e-3901-b85f-3378a07a9da4 | -7.8397 | -44.585201 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70b38419-8423-33c1-8d70-a806a50d9835 | -7.8258 | -44.570099 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a1866b6c-04b2-35cd-9d49-0033605635b7 | -7.8279 | -44.5788 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a67e0c26-16b4-37db-825b-7608dfb802c7 | -7.8299 | -44.587502 | 2024-09-29 00:47:59 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c07c9995-83b3-303a-9492-789e465b4c29 | -8.2436 | -46.301701 | 2024-09-29 00:47:59 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e073407c-dfee-36eb-a925-5a9e435ea7ad | -8.2453 | -46.309101 | 2024-09-29 00:47:59 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7b78082-3d40-3ec4-9016-1bbfc4bf26cb | -8.247 | -46.316399 | 2024-09-29 00:47:59 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 931ddb4c-319b-3f37-9fc4-b2fffdc4fea9 | -7.5831 | -43.855701 | 2024-09-29 00:48:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60226c7e-04b4-3de1-bd0c-a13e27e1192d | -7.5734 | -43.858002 | 2024-09-29 00:48:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5bec7d6c-1b68-3d49-aa22-c0e1d2677a93 | -7.8301 | -45.461201 | 2024-09-29 00:48:02 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f91119a0-fc73-3117-b956-4d73619cbf69 | -7.8319 | -45.469101 | 2024-09-29 00:48:02 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f46d8fa-b311-3b2f-9cdb-26cd79f46142 | -7.81 | -45.507599 | 2024-09-29 00:48:03 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15c4ea5d-7d65-3a62-b104-1d0a072546af | -7.8119 | -45.5154 | 2024-09-29 00:48:03 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd977130-7a42-3586-859a-5fe5aa678804 | -8.7069 | -49.595402 | 2024-09-29 00:48:03 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b26cae5-053c-3d3f-bf1a-644d219fbdcd | -8.7085 | -49.602699 | 2024-09-29 00:48:03 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b6c01e-7850-39ca-8708-e96a20990f2c | -7.3798 | -44.0844 | 2024-09-29 00:48:04 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d62908cb-783a-3e4f-b6e8-7ec2c8e62d3c | -8.6189 | -49.478298 | 2024-09-29 00:48:04 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6deadf96-bade-3041-8e4d-53fd7ca08737 | -7.596 | -45.0811 | 2024-09-29 00:48:05 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7c921a4-f3f9-3845-96a0-68a37868b9d7 | -7.5784 | -45.050301 | 2024-09-29 00:48:05 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9b001778-bf0b-3e8f-8588-3f752ed2c309 | -7.5803 | -45.058601 | 2024-09-29 00:48:05 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 69d9a6ed-4521-30a5-b364-157155ce2379 | -7.5823 | -45.066898 | 2024-09-29 00:48:05 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 556b96af-b1e5-368d-8124-ec917b2a236e | -7.5843 | -45.0751 | 2024-09-29 00:48:05 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4c6dc15-4f33-3701-a21e-610bb297985a | -7.5862 | -45.083401 | 2024-09-29 00:48:05 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b6d82730-9c26-3bdb-95b7-344036703980 | -7.5882 | -45.091702 | 2024-09-29 00:48:05 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8559084f-404c-3ccc-b7c2-d32dd83d4b26 | -7.7462 | -46.16 | 2024-09-29 00:48:06 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75af62c6-1e72-3c9c-8509-1b430984b7b8 | -7.8787 | -46.729401 | 2024-09-29 00:48:06 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee29e612-1b16-3564-a05a-bec4801d6a80 | -7.3679 | -44.641399 | 2024-09-29 00:48:07 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 782009c3-32cb-36f2-8b4d-14ad5a8aa32e | -7.5579 | -45.796398 | 2024-09-29 00:48:08 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e7f8336-9ac4-3f2e-a426-1a15aa20d865 | -7.5463 | -45.791 | 2024-09-29 00:48:08 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2daeea29-1c26-3e0e-bdf1-2eac7ee4f42a | -7.5481 | -45.798698 | 2024-09-29 00:48:08 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aee99810-6027-3854-b6b3-1a9e41e35dac | -7.7224 | -46.5452 | 2024-09-29 00:48:08 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e76f3f5-871e-31b3-89ac-d324acae3212 | -7.724 | -46.552399 | 2024-09-29 00:48:08 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43d4d8bd-25ce-3618-8cb7-d7e554b9ce29 | -7.5383 | -45.8009 | 2024-09-29 00:48:08 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cfc4166-d8eb-348e-a712-a787a5ffee0c | -7.2963 | -44.948601 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80c478e3-ece9-382c-8fe1-15ef07ea1535 | -7.2983 | -44.957001 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ebbc700-9313-3191-8805-459b2d38a11f | -7.3003 | -44.9655 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8303b866-c59c-3f24-a0a7-c4da9aa91497 | -7.3023 | -44.9739 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22cb2dec-5c14-3ecd-9d7a-dc770997967d | -7.2805 | -44.925499 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbbf587b-b179-3336-b379-de8080dd24a4 | -7.2825 | -44.933998 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab71f02-a8cf-3e4a-babe-737c8a9ee639 | -7.2885 | -44.959301 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a90b6ca-e19b-3b58-bed6-bf34afcab875 | -7.2905 | -44.9678 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caed3a34-72b3-3cca-8418-ac784f415b29 | -7.2925 | -44.9762 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 153725f1-34f7-37b1-ae66-b27a3b2155cf | -7.2707 | -44.927799 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61219219-3315-3d64-8909-ef2bb7417b39 | -7.2827 | -44.9785 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6515e083-d8a6-3f40-997f-bfa59e73bc77 | -7.261 | -44.930099 | 2024-09-29 00:48:09 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eca40487-679b-390f-9c1c-7f4684a42cf8 | -7.2492 | -44.923901 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17225289-9fdf-3f15-8c01-a33a275b33de | -7.2512 | -44.9324 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee04e183-efd6-3ce1-8115-93601f5b9173 | -7.2532 | -44.9408 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08105588-0432-35ae-9694-1fc10ab4ff84 | -7.2414 | -44.9347 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 400cab80-9822-328f-acf6-2aa2b72f7459 | -7.2554 | -44.993801 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df44bf93-e383-3ff7-88f6-12a6b350c589 | -7.2574 | -45.002201 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 463843d7-6b79-3637-8a12-9ff64138cd12 | -7.2594 | -45.010601 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42f386bc-4dcd-342a-87ff-d03d41d89fad | -7.2613 | -45.019001 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9127aa-8082-3a80-8f2b-617aa26fa13e | -7.2633 | -45.027302 | 2024-09-29 00:48:10 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b95c2302-7317-3a28-b8dd-7564fe70544f | -7.2476 | -45.004501 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc9c986-4087-3c10-9951-70be0ee65067 | -7.2496 | -45.012901 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 065ea328-e278-3086-8574-6b640e632084 | -7.2515 | -45.021301 | 2024-09-29 00:48:10 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df5020ec-ade4-3cb0-b481-449108527a65 | -7.2535 | -45.029598 | 2024-09-29 00:48:10 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3a1ba05-b75e-3cfe-ad9b-ea84f1a31a36 | -7.4885 | -46.117199 | 2024-09-29 00:48:10 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a52fc386-7afa-3456-8d41-c4c4ea30bc03 | -7.4902 | -46.124699 | 2024-09-29 00:48:10 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f765fb9-beba-31ba-ba8c-27ca468fd263 | -8.2356 | -49.3755 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3964945f-1312-37bf-9ee8-5b5597baa059 | -8.2372 | -49.382599 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b47ca433-9df7-3500-9100-95d1e254ddc0 | -8.2388 | -49.389702 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d70e9ef-0247-39b6-82cc-60f018496d66 | -8.2404 | -49.3969 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d24edbbe-fae1-31c1-96c2-a9c7e5e233f4 | -8.2258 | -49.377602 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a655a70-8b66-37b9-9614-003a6e0772f4 | -8.2274 | -49.3848 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 400d849d-ea96-3f22-8c5f-c1ef8f7bf704 | -8.229 | -49.391899 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac49d1d-1df8-3dc2-8bad-0910068e14cd | -8.2306 | -49.398998 | 2024-09-29 00:48:10 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc31e12-c266-39a9-822f-8a0506f2ba9c | -7.215 | -45.479 | 2024-09-29 00:48:12 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43081be2-cedb-3052-b304-8ce356f2fd86 | -8.1808 | -49.819302 | 2024-09-29 00:48:13 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ba4d09-bd4b-3781-95cf-f099254662a9 | -7.1457 | -45.579201 | 2024-09-29 00:48:14 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29433502-3a05-306f-987c-c2ac0103f8f6 | -7.1476 | -45.587101 | 2024-09-29 00:48:14 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cfc03c4-a4ba-3896-bd73-45d3239c3773 | -7.1494 | -45.595001 | 2024-09-29 00:48:14 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 006a1e7b-7e65-3667-803c-22a566ddb831 | -7.186 | -45.8829 | 2024-09-29 00:48:14 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6146698-0f8a-340f-83a6-89faab7f643d | -7.1879 | -45.890598 | 2024-09-29 00:48:14 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0e4c19b-d4a2-3dbe-8b8d-afeb612cb686 | -7.1781 | -45.892899 | 2024-09-29 00:48:14 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 876d5b10-4674-3657-ab6d-d5eae152a936 | -7.3293 | -46.673901 | 2024-09-29 00:48:15 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39c0c2f8-f1a7-3ddd-8131-92f9a0126527 | -7.331 | -46.681099 | 2024-09-29 00:48:15 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebc19519-bb24-3162-abb6-65a903551501 | -7.1244 | -45.840099 | 2024-09-29 00:48:15 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8350b72-b4fa-3619-9494-c091e075320b | -7.1262 | -45.8479 | 2024-09-29 00:48:15 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ea794eb-eb98-3f89-8a27-84b1536f130b | -6.9149 | -45.037899 | 2024-09-29 00:48:15 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbca9925-1664-3879-b3e4-7e48a9579911 | -6.9169 | -45.046398 | 2024-09-29 00:48:15 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 974c31b1-229b-3c14-a9f1-302c0cbc8378 | -7.5308 | -47.949902 | 2024-09-29 00:48:16 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b83e8fe-4c95-3e02-ae07-c074b1a99ee6 | -6.9514 | -45.6744 | 2024-09-29 00:48:17 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2a52412-b57e-3092-b596-e49671a8b600 | -6.9532 | -45.682301 | 2024-09-29 00:48:17 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
