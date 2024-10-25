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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d47b4e6b-a941-3f0f-aae6-7d278a9927ed | -8.73133 | -46.53097 | 2024-10-25 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e43ec1f5-458c-3814-9e89-9df642f38eae | -8.51266 | -45.87396 | 2024-10-25 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7526408d-b37e-3624-b39c-c787528168e2 | -8.5082 | -45.87799 | 2024-10-25 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 469abe95-6b8a-3aca-85a5-be374811376a | -8.40549 | -46.62217 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb12f233-71f0-38d1-9080-8b8457d43022 | -7.89604 | -46.68765 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9d989f3-30ed-3eeb-961e-485f370d85d3 | -7.89474 | -46.73216 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 997b7a1c-4e0f-303e-b21b-bec975b16c3b | -7.89308 | -46.68298 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72e8c726-51e7-3d13-9913-14d486a7502e | -7.89275 | -46.73331 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a9af3ee-a895-3acb-8427-55b453b0dedb | -7.89245 | -46.68711 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bf7671f-5733-3ba0-8711-46ba1fb9cc25 | -10.08049 | -47.39901 | 2024-10-25 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b322d80f-0ced-3752-a6af-41403fd3be5d | -9.703 | -46.26173 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09236eea-8135-30a5-9e1e-9b465824b51a | -9.69925 | -46.26114 | 2024-10-25 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72f125ec-a8b8-30e8-b199-0ba1e196a8cb | -9.53256 | -46.69467 | 2024-10-25 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c423232-403d-3fb7-b280-31c15c04abed | -9.5289 | -46.69411 | 2024-10-25 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d84348-3fbb-327e-91d0-ebcbcb81c290 | -3.49809 | -46.30801 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d6ef343-db0e-3331-938a-7097507600b4 | -3.41819 | -46.36271 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3f781b4-c54a-33f1-872d-aa3d3da0e0be | -3.41677 | -46.36331 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20c737f7-36b9-33d4-978e-0fd31c54bb63 | -3.30567 | -47.0251 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c191b634-9a88-38b7-a65d-7c40d768db3c | -3.30227 | -47.02457 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eb139a2-01cb-3d61-a66c-d2b7aa637886 | -3.23706 | -46.50394 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8919614-da01-33e4-b1a4-6928e4e48c38 | -3.2336 | -46.50341 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1280ceb6-ba56-3fe3-84be-cd07b96446be | -3.21181 | -46.80138 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 0c5c9db8-5c45-30c8-857a-39f9ae0d2681 | -3.21123 | -46.80505 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 0c722d40-16b7-3cec-be09-22043a6fec51 | -3.20896 | -46.79716 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 521321bf-0c82-3dd4-91c8-0a01565a4767 | -3.20839 | -46.80084 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 2c51bde2-5ccc-3689-b7d9-470d0a5ec07f | -3.20781 | -46.80452 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 52df8fa3-e1a8-3642-a84d-edc0613ac47a | -3.20496 | -46.80031 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3bc4aa00-9db6-33de-952c-bc4a95fedae9 | -3.20439 | -46.80399 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a59a604f-41e2-304e-adc9-40b9aae238ab | -4.77536 | -46.41447 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c6a2b019-3f98-34a7-a87c-df6b444ff01d | -3.10382 | -46.61835 | 2024-10-25 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29d74f41-600b-311b-81fe-71468f685bd7 | -2.81942 | -46.61029 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ce84fe9-cc1f-3487-ab13-33b6962d276c | -2.81883 | -46.614 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12396a88-2b55-36fb-a05d-1902cd7e561b | -2.81534 | -46.63624 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ec8e459-f12d-3cd7-87f4-3d2de684de90 | -3.1909 | -46.17269 | 2024-10-25 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f79a7db-b20c-3a2b-be7f-09d6df8307f4 | -3.18679 | -46.17602 | 2024-10-25 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c702598-3238-3da3-bb79-37e43ad67146 | -5.01609 | -46.48933 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 802e751d-f58f-37f6-bf5a-f5085ba55d39 | -5.01596 | -46.48885 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f916a7ae-b04f-377c-a2e8-a48d3165233a | -5.01317 | -46.48493 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cbe2601-840a-3f0a-a253-aeefc80a24e9 | -5.01256 | -46.48882 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d4829cd-5ae7-33e3-bf4c-9b10edfc363d | -5.0032 | -46.47948 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 624aefb2-81ef-3431-9557-c4e46f48016d | -5.0026 | -46.48335 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 60ebbd34-19e0-388e-b8b6-1ee88da7a64d | -4.99967 | -46.479 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b49a568-218a-3259-9340-e705fa69a092 | -4.99907 | -46.48287 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f9f9de9-6caa-36a5-91c3-f5b8e19ddc60 | -4.99847 | -46.48674 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5968287-8c74-39b9-9eb7-30972cef884c | -4.99614 | -46.47852 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deae8db3-e8d7-3d61-96e5-8f7db34eaefc | -4.99262 | -46.47797 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db81d784-5e1a-339c-86c3-c1500ea38cba | -4.98911 | -46.47741 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 087944a0-1c8c-34b9-bbb5-b2f6cd6de0a3 | -4.98559 | -46.47685 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e32654a7-e3ac-3fff-8a2e-f565b338fffd | -4.98498 | -46.48081 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8c715b5-8c56-35bf-990e-7e1ae0abf54b | -4.98146 | -46.48027 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cdf1d7b-87ed-32f7-8a0a-7fbb77fa5cd3 | -4.97788 | -46.50352 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3034653-02c0-32ce-8fb6-ea2ba891880c | -4.97733 | -46.48367 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb05d8bf-d1a2-346a-b453-9f8b3a04a846 | -4.97436 | -46.50299 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03d37966-ae9b-3b9c-b088-ef2e54af9fd7 | -4.97321 | -46.48705 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8675556a-9fab-3fbe-86a7-96ef498b9e72 | -4.97262 | -46.4909 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aff7441d-bc4d-3898-91b6-9215466eb0c7 | -4.77476 | -46.41836 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a645f08a-f661-397b-b560-53eb4961033b | -4.77416 | -46.42227 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ee7d710-4529-3e88-86ee-f9da513fa2cb | -4.77125 | -46.41777 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 098c0456-c0d9-34c9-96e4-c2bb364d6d20 | -4.77064 | -46.42168 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5215e471-7358-3f61-8f54-b335052ccc81 | -4.77003 | -46.42564 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8413f9f3-9bfe-35d5-9a5e-32ffb0eed531 | -4.76773 | -46.41721 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dedc3e64-1bec-3e81-ba84-bc7fc53ee9bb | -4.76713 | -46.42112 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98e2246f-1b72-39e1-a4a8-0067c362b2aa | -4.76267 | -47.55684 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d36d9567-5c02-367a-a34b-e943231d6aa5 | -4.76249 | -46.40437 | 2024-10-25 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b93dfe7-7775-33a2-96a1-f58ed50ba02e | -4.76211 | -47.56045 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c82485b6-a016-3c2d-abd8-079520e8e157 | -4.75929 | -47.55632 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b8ec9ef-84cb-324d-a9a5-9af19cde311c | -4.75873 | -47.55993 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c5aba8a-7e43-37c8-beb3-5b154bbdb7aa | -4.75817 | -47.56355 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 884fd45a-86cc-3027-9787-252ec222215b | -4.75535 | -47.55942 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8e2edbe-649c-3374-9069-8bb176b1e7d2 | -4.75368 | -47.57027 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77c9fd0a-f7af-35de-a0c1-bd02c8e998bf | -4.75029 | -47.56976 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 325f38ef-56e3-31dd-a270-ca99539d72ef | -4.6947 | -46.61278 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee1f9ff6-f842-337f-aac7-ec1e8803a661 | -4.69435 | -46.84678 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da1682a2-f0d5-31de-a955-8358548931f3 | -4.69089 | -46.84624 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| cd1c1473-afd0-3779-b539-4118d7de305e | -4.65746 | -46.8565 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce5997aa-74ab-3e36-83e1-0d691e425940 | -4.65689 | -46.86026 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbe62170-6e7b-3ba6-9490-5b41e0e3a5e7 | -4.62032 | -46.55478 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee3b4833-037c-39a3-a6b7-8f43090101a5 | -4.54172 | -47.40176 | 2024-10-25 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa48e0dc-14f2-32cb-8b2d-7bf1c9527f74 | -4.53021 | -46.62498 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68bdbc19-c80d-32e6-879a-c829cfd167ef | -4.52673 | -46.62444 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802e9dec-d059-3584-945b-6defe8ad3512 | -4.49439 | -47.0764 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6387d1c0-0c98-36df-874f-e5349a79b9cd | -4.49163 | -47.07672 | 2024-10-25 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e402509f-ae64-3702-8006-fe97f520ea6d | -4.47268 | -47.7325 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f850010b-fa5f-305d-8479-918bad2728b1 | -4.45072 | -46.55389 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef90897c-288e-3f6b-b00b-de10ec1a8788 | -4.43351 | -46.64151 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| da33be1b-2402-3572-bb14-21fcc000417a | -4.43003 | -46.64096 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e9416adc-480f-3412-9387-387bc16cd5ab | -4.39625 | -47.597 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 615cc808-a044-3252-9551-f5310155660e | -4.38953 | -46.60332 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db53c465-1b79-3531-838d-95d2f6351981 | -4.37672 | -47.72166 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 748de0aa-fa66-3e5d-a33b-c7bdf8413881 | -4.37246 | -46.80636 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1342ac6c-0e2f-36e3-81ac-84a6f8e20f6c | -4.37187 | -46.81015 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63be8c2e-00d4-3473-ae5d-6ef8029083fd | -4.369 | -46.80588 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8c8b618-bf28-341e-a897-35da3d31ab01 | -4.36841 | -46.80966 | 2024-10-25 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 756ec71c-2252-30e7-8c23-99b2ff3a7767 | -3.91848 | -47.53121 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0a7e4d8-deca-3bb9-bc10-e690d39ddc0c | -4.36574 | -47.48214 | 2024-10-25 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46733e56-8380-364f-9d70-926017e750fb | -3.60473 | -47.25925 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3727b5e2-d15f-3cf0-b33c-d4f44152f919 | -3.60417 | -47.26287 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a3ea5ae-6708-32d8-a2ff-1fc9cb11b531 | -3.60362 | -47.26645 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73479b9b-402f-3fa0-919b-18e774385f3b | -3.6019 | -47.25507 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d38a6af-4131-31e1-83db-872dabfbf8e2 | -3.60136 | -47.25542 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README53.md)
