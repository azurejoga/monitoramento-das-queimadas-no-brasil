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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e4f59ba-2a42-33eb-85d9-d65a7935629f | -8.6757 | -69.9611 | 2026-09-24 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2e318d97-ee7e-31cb-ba6f-13ef9a76e8e5 | 2.145 | -50.8784 | 2026-09-24 16:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 261e385c-32b5-31c1-873d-80ab33345f62 | -12.8059 | -54.0255 | 2026-09-24 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 11956a64-8228-33ac-ba50-d0cc036cb057 | -12.8246 | -54.0442 | 2026-09-24 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| fe42a888-568e-388a-83d0-a367483e760a | -6.5756 | -45.5645 | 2026-09-24 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e82be85a-498e-3f0f-add1-2a182a007246 | -11.7357 | -54.5227 | 2026-09-24 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9de2d5d2-14c7-34b8-8b70-10333c1d4bc9 | -12.8437 | -54.0422 | 2026-09-24 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c41531bb-87bf-3aa5-a2d2-c1c343d1e8a4 | -6.5759 | -45.5419 | 2026-09-24 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d7607033-7b97-33d0-913f-fd6404222e33 | -13.2787 | -51.795 | 2026-09-24 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5fb56eb0-fb3e-3da1-8acc-2666eb259c1c | -6.5759 | -45.5419 | 2026-09-24 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| cb6a9882-cf5c-3caf-9d26-1ab1709fc0ad | -13.2983 | -51.7713 | 2026-09-24 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c15be27d-f206-3bdf-8c65-a5e45164b443 | -11.2488 | -54.1378 | 2026-09-24 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4fc139ab-8d7f-334b-bb09-748a27b13786 | -13.2791 | -51.7737 | 2026-09-24 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 599aacd0-c96d-32cb-9730-ddf53cf051b0 | -13.2794 | -51.7524 | 2026-09-24 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c3269d93-dcf3-3bf6-b72a-85819ecef4aa | 2.458 | -50.9756 | 2026-09-24 16:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 77.3 |
| bbd0f2d0-7dac-33c8-aa91-74be5213635d | 1.9976 | -50.8813 | 2026-09-24 16:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 8a8b55d2-4c30-32c1-aff5-f2d069ce2abc | -11.2488 | -54.1378 | 2026-09-24 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 1f789bc7-c667-3b75-898e-89db59d5d37f | -6.5759 | -45.5419 | 2026-09-24 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1f532afb-984e-3a84-bd7d-1bd2ad4f02d8 | 2.458 | -50.9756 | 2026-09-24 16:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 44a1adce-9a75-3b7c-a823-4d4895de4951 | -6.5759 | -45.5419 | 2026-09-24 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a422e5e5-c85b-3c64-99b6-769e7914c0e0 | -6.5759 | -45.5419 | 2026-09-24 17:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 7a4eb6ac-3eff-3fba-a9cb-508b442eb1e8 | -13.2054 | -51.5916 | 2026-09-24 17:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.2 |
| feba34ea-5c1f-37f1-a676-75171f903c44 | -4.4 | -55.55 | 2026-09-24 17:15:00 | MSG-03 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f69c951f-65d7-325d-8a7c-1224b0a9ce06 | -14.75 | -45.61 | 2026-09-24 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eaa12655-2900-3763-b5c1-acd15cb7b8b0 | -14.79 | -45.67 | 2026-09-24 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33b16413-3363-36f9-8170-e797e9dbc414 | -14.76 | -45.66 | 2026-09-24 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d208a49-5140-3279-9901-2f3f71aaa4b7 | -9.64 | -43.95 | 2026-09-24 17:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c88d8abc-e1cb-3c8b-b93a-fa887e15942c | -8.95 | -45.91 | 2026-09-24 17:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be52cb29-cc9c-32b9-96c2-9d0a39e61390 | -4.43 | -55.56 | 2026-09-24 17:15:00 | MSG-03 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 232f43a9-6503-3180-ab44-c658e6b461ed | -14.79 | -45.62 | 2026-09-24 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 915fe99f-8dd2-31cd-95e5-ab43485f0cc0 | -1.3932 | -49.0387 | 2026-09-24 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 6bc591c6-3330-313a-ab3d-9456b0d7de1c | -10.7115 | -60.7312 | 2026-09-24 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 51f0ed72-81d0-3c4d-8c4b-f5fb5e4170b4 | -13.2057 | -51.5703 | 2026-09-24 17:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 187.3 |
| b6cc4d89-6368-3841-892f-9a040bcb4a4d | -10.6928 | -60.7322 | 2026-09-24 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 78c1cfbc-e9df-3b6d-8334-a082e30736ab | -13.2054 | -51.5916 | 2026-09-24 17:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 2f27b7bf-7c0e-3f03-8b11-339dc9665cee | 2.145 | -50.8784 | 2026-09-24 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 430039e0-41cc-3e64-8f0f-c55eb712c8f8 | -10.7115 | -60.7312 | 2026-09-24 17:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| e695826b-c71c-3f48-b649-c347af190884 | -7.86 | -72.8781 | 2026-09-24 17:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 98e8ea53-ee6e-391e-b547-efcf8748e87f | -14.3696 | -52.0813 | 2026-09-24 17:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 44715740-dd66-3c06-a6d8-c0c250ea9795 | -1.4116 | -49.0597 | 2026-09-24 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ca30d8c2-9781-3667-b1fe-01b72992fa79 | -8.8922 | -62.4107 | 2026-09-24 17:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 110.6 |
| fb1d96f5-f611-3a37-ba1a-15b32d722fbc | 2.4581 | -50.9548 | 2026-09-24 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c644718b-4dc8-384f-b0ae-408c806b9821 | -10.6928 | -60.7322 | 2026-09-24 17:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 3d8c9250-25df-3bb0-be45-c5e3a39912f5 | -6.9797 | -71.5911 | 2026-09-24 17:40:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 636c1527-81bc-303d-a318-b04457664b2e | 2.145 | -50.8992 | 2026-09-24 17:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d221456c-f818-3929-97de-cec8739fd622 | -10.7114 | -60.7505 | 2026-09-24 17:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| b3ba882f-4490-30ce-a270-506d2acd1b97 | -8.6016 | -70.0357 | 2026-09-24 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 16bc27dd-d789-399e-884a-004578438af5 | -6.2026 | -47.5026 | 2026-09-24 17:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6d430ab6-0fb0-38ba-8ee2-edff65d03b87 | -10.7115 | -60.7312 | 2026-09-24 17:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 6bf63011-9ff0-3d7f-b25c-a532934e35c4 | -7.1987 | -72.6818 | 2026-09-24 17:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 43c64fe2-342f-3e29-9e1d-9b779efa8495 | -8.7898 | -68.7263 | 2026-09-24 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8afa2926-20ca-3aa4-abb8-08ca0cdb4085 | -8.6757 | -69.9611 | 2026-09-24 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c49620c3-8ccb-31ea-9a34-5817e06b4667 | -7.3089 | -72.6447 | 2026-09-24 17:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 9a89eea6-a6ae-399b-8ac9-e7b0795a3b3c | -8.8081 | -68.7812 | 2026-09-24 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 13705a65-0d6e-3a84-8153-adb32f59203f | -14.3503 | -52.0838 | 2026-09-24 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| eb8a23ed-f6c3-34ba-8d99-38dced665bc4 | -14.5864 | -54.1362 | 2026-09-24 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| be3422ea-98f1-3d3f-bd02-8c8c2e6b9b10 | -8.6017 | -70.0173 | 2026-09-24 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 103.2 |


