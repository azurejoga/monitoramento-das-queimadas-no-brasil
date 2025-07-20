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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1460e86-acdc-30e8-85fb-6ede701dc3ce | -5.6131 | -42.3128 | 2025-07-20 13:30:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 0960641a-85ea-3cc9-8eaa-750c381ffe45 | -10.3775 | -49.9293 | 2025-07-20 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ab3dfcc6-7bc8-35a1-9750-d75bbe7124aa | -12.1541 | -44.778 | 2025-07-20 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e5355c6f-89d3-39f6-9cca-9d0b882ac23c | -8.949 | -62.2184 | 2025-07-20 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e2ec4240-47a3-3807-b98d-a86c3b4c5821 | -5.6131 | -42.3128 | 2025-07-20 13:40:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| cff01610-d8ac-37f6-aadd-0af5ecdacd6f | -12.3736 | -46.42 | 2025-07-20 13:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 15a680c4-b7b0-3587-a58b-d6c19c390a31 | -6.4656 | -45.3249 | 2025-07-20 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 33fa4b45-02cb-3c43-b58b-9664f29b5d7f | -6.4469 | -45.3263 | 2025-07-20 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b2656f46-6bf3-3f95-8de9-f50301f5b164 | -6.8958 | -45.4026 | 2025-07-20 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 89e16bad-be35-35f5-adca-14e8ce08241b | -10.3775 | -49.9293 | 2025-07-20 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 08ca5d35-7032-35d1-a518-eec991385d66 | -5.6131 | -42.3128 | 2025-07-20 13:50:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 5d7c0f26-38a6-3188-a62f-83f17d1d7c0b | -6.896 | -45.38 | 2025-07-20 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e6af6dd4-3f48-3b15-92c4-daff43362139 | -7.9462 | -43.9526 | 2025-07-20 13:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d101da44-565f-3a86-b9ce-7e2338bf8a0e | -12.6491 | -47.1022 | 2025-07-20 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 2b421480-f79e-3112-a3de-e3e1cec838d5 | -6.3715 | -45.3775 | 2025-07-20 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| df9e48fa-bb13-325d-a6f3-3ac86504f275 | -6.896 | -45.38 | 2025-07-20 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 82e9bf9d-a778-37c4-ac87-57f82b2ece33 | -5.6131 | -42.3128 | 2025-07-20 14:00:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| ad2da72c-6513-34b4-b422-cadacd7928f6 | -6.8958 | -45.4026 | 2025-07-20 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 79feeb23-697d-30b5-9002-398f2d046449 | -2.8813 | -42.2377 | 2025-07-20 14:00:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ad8a1c8a-e3d9-3f0a-9221-04a907e7c33f | -9.4034 | -47.9487 | 2025-07-20 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f92ddb92-4a3f-30de-ae84-185ab54bc088 | -12.6684 | -47.0994 | 2025-07-20 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 597a40e2-1273-397d-9657-1b66fb1a4ad9 | -6.896 | -45.38 | 2025-07-20 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0c2a562a-ebd6-3115-853c-d3d393ea7a02 | -7.4338 | -44.2812 | 2025-07-20 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 4bc2abe7-2f51-39ed-ac52-b68edb85dbd7 | -6.8958 | -45.4026 | 2025-07-20 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 44cfe1ee-fe21-350b-a611-1ef8377328e0 | -5.6131 | -42.3128 | 2025-07-20 14:10:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 727ec344-1e76-3ac9-bd8c-e1555e2c40d9 | -10.3775 | -49.9293 | 2025-07-20 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1f28c360-7086-3b9b-b289-0e6a8fd9cc4e | -12.6491 | -47.1022 | 2025-07-20 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 503fff65-46e8-319e-831e-b3078af4d09b | -5.8865 | -45.2332 | 2025-07-20 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 54c80941-1304-3378-9e15-cbb0ab061825 | -5.6131 | -42.3128 | 2025-07-20 14:20:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| d42c124d-2d66-373e-b4e5-bcaeda4fa24c | -12.6684 | -47.0994 | 2025-07-20 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9b5ca3c0-e61d-3f09-be6b-35f82659d3c3 | -6.8187 | -43.8063 | 2025-07-20 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 58edce7a-9bda-3312-b0fb-1ee370122857 | -5.6065 | -45.1852 | 2025-07-20 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c048bbc4-d4ed-3681-a675-1d7e07104436 | -7.4338 | -44.2812 | 2025-07-20 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 0ba0c3db-e03e-310e-ba01-41eb3b06b6c1 | -6.4469 | -45.3263 | 2025-07-20 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 77480a92-1562-32b4-b562-7c6d79e126a3 | -7.301 | -44.3858 | 2025-07-20 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| c14bcf21-f314-341e-8330-3e184bd062c7 | -5.6131 | -42.3128 | 2025-07-20 14:30:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| a1a22139-0b43-3c01-84e5-5e46e178be2e | -2.8983 | -42.5909 | 2025-07-20 14:30:00 | GOES-19 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b9d4f6b4-cb86-35d8-a1a4-761ab3fef147 | -7.9462 | -43.9526 | 2025-07-20 14:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6ce3a80b-3e27-36d6-a718-f5cfeb7e1e8d | -12.6684 | -47.0994 | 2025-07-20 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e8b2bb38-90d3-306d-9f35-90fc10cff317 | -6.8958 | -45.4026 | 2025-07-20 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4ddd71ed-16ea-337a-a70e-12648175bea8 | -5.8865 | -45.2332 | 2025-07-20 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d36789c7-5948-3f97-8131-9e87f761b120 | -7.301 | -44.3858 | 2025-07-20 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f7c14bc5-b0f7-396b-95c9-0923e097b849 | -6.7446 | -45.5282 | 2025-07-20 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fe792d3f-da0f-3cc8-a47c-1752fae9f6a7 | -12.6684 | -47.0994 | 2025-07-20 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d2a65eda-47b5-3f79-bbda-cc9fbc1956bc | -5.6131 | -42.3128 | 2025-07-20 14:40:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 120.8 |


