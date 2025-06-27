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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b475834-4f46-3ead-9609-a01fbd1a3ab1 | -21.17758 | -43.98223 | 2025-06-27 03:32:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5cc3a132-0667-3e4b-ae51-49bbe84d03db | -18.9496 | -39.9103 | 2025-06-27 03:32:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e805428a-b190-3708-b981-4a65d9fcecf9 | -17.04037 | -45.8916 | 2025-06-27 03:32:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 140599f0-12fa-35d7-a5df-96c5edaf0272 | -17.04378 | -43.77259 | 2025-06-27 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 130f0940-ac8f-378e-bdb2-acd1534fa485 | -16.24988 | -46.29277 | 2025-06-27 03:32:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7709313b-07ca-30d5-9551-02c8141f17fb | -21.10526 | -43.80772 | 2025-06-27 03:32:00 | NOAA-20 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d5b65776-3279-3beb-a467-df46a771fa8a | -20.90787 | -44.1219 | 2025-06-27 03:32:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1d0c68ed-6c92-3d93-885d-252d7e26f625 | -17.09174 | -43.80444 | 2025-06-27 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53c25a50-915f-3776-9843-ee3b78dc6bb4 | -20.90983 | -44.11687 | 2025-06-27 03:32:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f67d6cbe-431f-3cf2-b88d-30ef8b530a15 | -17.04314 | -43.77578 | 2025-06-27 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a8ad0a4c-5e3f-36a1-89e5-b9271125eae9 | -17.04249 | -43.779 | 2025-06-27 03:32:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c21bdd22-f6c0-36b7-b108-3ab192cd0db8 | -15.47327 | -41.887 | 2025-06-27 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8ed2c7d5-1519-3f78-82b1-f99a4273cda4 | -18.95352 | -39.9111 | 2025-06-27 03:32:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e75a2f5c-6579-37b3-88ca-156391b05747 | -22.50971 | -43.50533 | 2025-06-27 03:32:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 419210f7-65b4-3bef-a827-01616783cb9c | -22.79825 | -44.70424 | 2025-06-27 03:34:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 42c5ef5d-0548-3962-8bbd-78762834b779 | -22.90057 | -43.7529 | 2025-06-27 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4c445f86-07cf-3f33-8de6-83328e7630b4 | -6.9602 | -42.9052 | 2025-06-27 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 361.2 |
| 342b3fc1-ebd2-35c4-9b4c-ae8d3f4179cd | -6.5631 | -51.1126 | 2025-06-27 03:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fc3edb3c-7385-3b44-8080-04fb348a8fcc | -6.9791 | -42.9034 | 2025-06-27 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 163.9 |
| 2ef2699e-06f1-3636-a756-a9c5c5284a73 | -11.5592 | -52.096 | 2025-06-27 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c3c40573-6075-3cc9-92df-e473fe3bf4cb | -6.9793 | -42.8798 | 2025-06-27 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.6 |
| 5f2e4b2a-303e-3952-8276-4a12988796b0 | -6.9605 | -42.8816 | 2025-06-27 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 310.9 |
| 39de0b6c-829c-354e-998b-ec07b5080e1e | -11.5782 | -52.094 | 2025-06-27 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| ff4c9226-1c4c-32a1-aef3-b78ef011a3a4 | -6.9414 | -42.907 | 2025-06-27 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 254fbf04-0f71-3e44-9b95-86acf5795932 | -11.5779 | -52.115 | 2025-06-27 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 353.5 |
| 34202cc0-3a2b-368c-8e85-57c87a9a8a20 | -6.9416 | -42.8834 | 2025-06-27 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 8a41b327-1362-35e7-88d1-e54fcc842720 | -11.559 | -52.117 | 2025-06-27 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 76cf6502-ff1e-3684-9069-6b2b8c0ef88d | -11.5776 | -52.136 | 2025-06-27 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a85b953c-f265-319b-a67b-3a804a8daee9 | -6.9414 | -42.907 | 2025-06-27 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| b5124c30-068b-30ab-996b-8d0dfbaa485c | -11.5776 | -52.136 | 2025-06-27 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3b5b837c-1abd-35f8-8009-f0da421fdfb8 | -6.9602 | -42.9052 | 2025-06-27 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 328.9 |
| 796789b2-7bdf-38bd-8598-630c6f8588a2 | -6.9793 | -42.8798 | 2025-06-27 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 156.9 |
| e65965a3-f838-3122-b179-359c3b74d4a2 | -11.559 | -52.117 | 2025-06-27 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 373a12f8-6e98-3152-a82d-1ce6a770fe7d | -6.9605 | -42.8816 | 2025-06-27 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 293.9 |
| 028b2470-d2ef-3590-8519-8d0beaebfed8 | -11.5782 | -52.094 | 2025-06-27 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 5815c576-5720-317f-8b77-3af72aceceaf | -6.1789 | -48.0929 | 2025-06-27 03:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 68ccc8c4-2c82-35dd-a27c-ac66c727f2b4 | -6.9416 | -42.8834 | 2025-06-27 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 6ff3dac3-f167-3d2b-9132-f8d16986a566 | -6.9791 | -42.9034 | 2025-06-27 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 178.6 |
| 6015410d-3f2e-34c4-8494-1daf8723b5cd | -11.5779 | -52.115 | 2025-06-27 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 370.7 |
| 14fc20d1-f7ae-3135-800c-cd9158b13d7b | -6.9414 | -42.907 | 2025-06-27 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 6279e91b-0d01-348b-92ea-fc8126a50f1b | -11.5782 | -52.094 | 2025-06-27 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| b8f0be8d-ffb2-3e25-80dc-5c7c7bb86d16 | -6.9793 | -42.8798 | 2025-06-27 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 157.7 |
| 47964367-75d4-34e2-96bd-8a1d7d9d267e | -11.559 | -52.117 | 2025-06-27 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6b201d62-9d7e-3c61-b61f-217ea2e891ae | -11.5779 | -52.115 | 2025-06-27 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 376.2 |
| 0cf9b2ce-2726-3749-b698-463d7926c462 | -11.5969 | -52.113 | 2025-06-27 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0cf1356d-dc53-3729-8813-b5d3a3942fb3 | -6.9416 | -42.8834 | 2025-06-27 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 4da5547a-7cd9-3a34-bbe5-6288e56e2405 | -11.5776 | -52.136 | 2025-06-27 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5020693e-d400-30a0-8a63-76e7051498bb | -6.9605 | -42.8816 | 2025-06-27 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 328.0 |
| 80e7b00f-99c0-3e23-80e3-2d3b99011964 | -6.9791 | -42.9034 | 2025-06-27 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 22f09985-e060-33bc-afbb-9b5f42fdc13a | -6.9602 | -42.9052 | 2025-06-27 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 291.3 |
| 4ece9841-d3f2-3726-98b9-cf480cf34fd9 | -6.1789 | -48.0929 | 2025-06-27 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 9268b7e1-340b-37c2-8ddb-499fb17b752b | -6.9793 | -42.8798 | 2025-06-27 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| 4a315a51-43f0-37ee-996d-cbfbbe6236f9 | -6.9602 | -42.9052 | 2025-06-27 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 305.6 |
| f26a1417-96fa-3831-962f-5227b9e8a785 | -11.5779 | -52.115 | 2025-06-27 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 303.7 |
| c9abcfab-112e-36d4-bea0-5122b50c075e | -6.9605 | -42.8816 | 2025-06-27 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 336.8 |
| b4120af3-0f8a-3f03-b6ac-2a222a21068f | -6.9416 | -42.8834 | 2025-06-27 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 02b8e43d-b7a6-3974-b801-c8bc839be158 | -11.5782 | -52.094 | 2025-06-27 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c8a8828e-9329-36ea-968f-2ae68bcc6190 | -11.5776 | -52.136 | 2025-06-27 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0d1f3fab-9593-3acc-89a9-c873e35b78d4 | -6.1789 | -48.0929 | 2025-06-27 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8d288a31-710d-3d34-92a1-0139342584db | -11.559 | -52.117 | 2025-06-27 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| aa2215f1-af61-3a38-b56d-59a2fb4ae544 | -6.9791 | -42.9034 | 2025-06-27 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 7c0ae145-a5ac-3375-a7bb-6da1b5c9d6f5 | -11.5969 | -52.113 | 2025-06-27 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 269561fc-ff2f-360d-87ad-1c601f63a661 | -6.9414 | -42.907 | 2025-06-27 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| e9e26e76-a4f8-350e-bcbc-ba525089abaa | -8.43852 | -46.97677 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2468ca15-8cd5-384e-9b8c-df284dfb0369 | -7.53965 | -45.82969 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8a8a38d2-19b0-3085-9d9b-ea5d76182f2d | -8.00712 | -40.15327 | 2025-06-27 04:19:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 616cfe22-fc6a-3fae-8e09-d716f2a06d73 | -9.06267 | -46.93485 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8cb9396-ea76-3d78-8967-4473ab8e4774 | -6.77909 | -46.3283 | 2025-06-27 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0679ed00-8877-3952-9500-11d8b190fc6f | -2.44453 | -47.46861 | 2025-06-27 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88cc9cd1-3145-3f1a-ad01-40e795c612fb | -7.56007 | -45.6364 | 2025-06-27 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9eb05333-109a-3363-a117-45d1534f9da4 | -6.27267 | -43.68069 | 2025-06-27 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| dc5d2674-7cfc-3db3-9b0c-8b90b9b02058 | -7.21176 | -43.07178 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 9a60bd90-31bd-3ef4-80a0-a73e8a8f0712 | -7.54629 | -45.83073 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0ea3d745-3a02-32c3-88de-9051fc143f63 | -7.20742 | -43.19227 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5754e75f-03a2-379d-bcbe-d0227e98151d | -3.02764 | -49.43917 | 2025-06-27 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b7e5000-f41f-33cf-8854-4e07f99310a0 | -6.97266 | -42.89157 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| e7172c49-e872-3eaa-a047-5d5646abc3b0 | -5.92226 | -43.48133 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fcc2106-a593-33bd-b59f-625cfe3b1ad3 | -6.96808 | -42.89855 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 07336e07-1996-3d57-9ccd-67a948f275ae | -6.95551 | -42.88898 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| ccc14403-9285-3514-9323-1c9dfac272de | -6.72532 | -47.20796 | 2025-06-27 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a98c1335-642e-3e69-bd1b-2ac2aa4151f9 | -3.03709 | -49.43306 | 2025-06-27 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9e1c059-063f-3051-9852-75c39b405472 | -6.96237 | -42.89001 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 1394e1e0-f76d-303d-8c8e-4c81598b0ec9 | -9.06612 | -46.91319 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19ba4174-eb84-3b30-8621-5bc0f43317c8 | -6.95722 | -42.90071 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| f65264f1-4066-31e0-9678-e52655dc5cb1 | -6.17193 | -48.0894 | 2025-06-27 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df9c1d14-9028-373a-b0cc-d3ace26ac799 | -7.63411 | -49.53986 | 2025-06-27 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4623b0ba-9642-32fd-9d1a-c90f034f0133 | -6.2165 | -43.36191 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ed0ce27b-0781-329e-9b7f-42ef4b398eb8 | -8.38025 | -46.96395 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f45abda-a9cd-33da-a842-ac1634e7428a | -6.69455 | -43.05913 | 2025-06-27 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3eb89fb0-d308-3081-9dbe-e04a864c4e2d | -8.06369 | -46.96592 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b7bf3aa-3419-32ea-afd5-2cb98bdbef2e | -3.02825 | -49.43546 | 2025-06-27 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea8b8506-d228-388a-aa6b-9d666479e073 | -8.47426 | -48.26809 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c84e53d4-90e6-3a3d-bf95-b9af392fe990 | -6.97323 | -42.88781 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 00e85830-f32e-3398-9685-3525a8ba66ee | -7.2112 | -43.07551 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 9488a71c-6894-3f18-8100-b9efde1ef67f | -6.95379 | -42.90018 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 88d28e41-ea36-3b53-9c14-19cb56f5a318 | -5.17671 | -46.10818 | 2025-06-27 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312ae91b-b4ce-3b07-a006-56861a62f92b | -5.91891 | -43.48082 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d651a911-a824-3809-99fa-d5b0a4bbc330 | -6.37172 | -43.65582 | 2025-06-27 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e7d0be1-b40f-3203-8ebf-576c61955210 | -4.68765 | -48.86518 | 2025-06-27 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fcf7298-249e-37b0-9724-2643ebe20972 | -8.2602 | -47.01195 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
