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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97808314-783f-3579-9d05-e5e6afd822d2 | -13.2845 | -46.0528 | 2026-06-17 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 67281ee7-83b6-3775-978f-f5d57dd1c3f9 | -12.1762 | -52.7842 | 2026-06-17 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 2a1c2dbb-3646-30fd-b9b9-775c6a2b5016 | -12.2333 | -52.778 | 2026-06-17 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 5ad3e1ce-6f13-37a6-ad2f-3f23b07b1a07 | -12.233 | -52.799 | 2026-06-17 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ce5a1bba-4589-3336-8553-52be0d1966b6 | -10.9971 | -46.4741 | 2026-06-17 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 18f2fc6a-7bd4-3a98-abad-b1895b3e9ae1 | -13.9421 | -46.0367 | 2026-06-17 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 0b7a53ee-9e9e-31c9-bbf0-36d484e5218d | -13.2651 | -46.0559 | 2026-06-17 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5082dcbd-2d3a-3e79-a2d0-275e786474ee | -11.3603 | -51.4009 | 2026-06-17 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 997dad68-80bf-35b3-8e80-6938ade4a75b | -8.9635 | -46.9785 | 2026-06-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c5cf5847-6980-3270-8f9d-0f96ea66f4fe | -12.214 | -52.801 | 2026-06-17 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 1f155a83-83a9-330f-9d8f-5c94f0bfa7b6 | -10.1493 | -56.6115 | 2026-06-17 13:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 8379cc99-3b16-3b4c-b912-d3a80d763475 | -10.7024 | -49.6797 | 2026-06-17 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 69e8f27d-0e8b-374f-8f36-96cc75e662bd | -12.1952 | -52.7821 | 2026-06-17 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 303.3 |
| 74ff6848-5cc2-3465-a23f-bf4da6346b7e | -8.9824 | -46.9766 | 2026-06-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 828c82eb-4329-341a-bf1b-aef89bcab963 | -10.168 | -56.6101 | 2026-06-17 13:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 26d655b0-0fb8-3232-9fb9-c0d3606bc97e | -12.2143 | -52.7801 | 2026-06-17 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 278.1 |
| ab7bc93f-d433-3dd4-ad03-1eeb409948b8 | -8.9072 | -46.9621 | 2026-06-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 88d66fa6-60ee-353b-8a82-a34dadba48df | -8.8883 | -46.964 | 2026-06-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 3df25f9d-8c2f-327b-8b8b-a5194795ca3e | -9.0013 | -46.9746 | 2026-06-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0fe72566-6c7d-3f7b-88e6-060ae9f24788 | -8.9638 | -46.9563 | 2026-06-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a2ab6d72-fc07-323b-bf95-d64aad489678 | -12.1762 | -52.7842 | 2026-06-17 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 66e2f4de-4096-31df-afac-058b66352d38 | -8.9824 | -46.9766 | 2026-06-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 59dc03c2-8de4-3117-8683-954e2181b4da | -12.1952 | -52.7821 | 2026-06-17 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 390.2 |
| 675d5277-bf4d-3e8d-9994-50d83aab41b1 | -12.214 | -52.801 | 2026-06-17 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 202.6 |
| e45000c6-93ba-3547-82b4-070b6e75c754 | -10.1493 | -56.6115 | 2026-06-17 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 208.8 |
| 672d2a9d-724d-36c6-8ddf-b48d9e791751 | -8.9072 | -46.9621 | 2026-06-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8c8f9fcf-36a8-39ab-bceb-72e709014e79 | -12.2143 | -52.7801 | 2026-06-17 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 321.4 |
| 429bda4f-d786-368d-a01b-a9f1ec4ba251 | -8.8883 | -46.964 | 2026-06-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| e136d33c-3641-3f5e-bf4b-c62e1fe95034 | -8.8222 | -44.8043 | 2026-06-17 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 2f9cfa6d-d19c-3277-9fc3-be13af5387d2 | -12.1955 | -52.7612 | 2026-06-17 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0b042502-b8cb-3fee-94f0-a0fee2d7c783 | -11.3603 | -51.4009 | 2026-06-17 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 085aa700-cf53-3ca9-947a-76e71fd105fe | -10.168 | -56.6101 | 2026-06-17 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 618d9ec6-75d0-3b3c-99d0-d61c9a8ea6ad | -13.9421 | -46.0367 | 2026-06-17 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 238c275f-8930-3146-82af-99637f6aaa13 | -13.2651 | -46.0559 | 2026-06-17 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c4fce3fb-97b8-3aca-ace9-cb8c2314c7a7 | -12.2333 | -52.778 | 2026-06-17 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e095708b-d9dd-3c78-9fab-e320b5dafe64 | -8.9635 | -46.9785 | 2026-06-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 935429da-fd69-3f68-8b6d-f3f54b289b62 | -11.3413 | -51.4029 | 2026-06-17 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1c38108f-2a33-32b6-9dcd-27d3960a3dfe | -7.7724 | -47.5773 | 2026-06-17 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c0b138f2-a25e-3ffd-b3f1-716c8b20418d | -10.7214 | -49.6777 | 2026-06-17 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d9de1d70-69ed-3edb-9428-bb0146a3f848 | -13.2651 | -46.0559 | 2026-06-17 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c84e32cc-92d2-36fe-81f4-df6508c6f59e | -10.1493 | -56.6115 | 2026-06-17 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 6d3c1a5b-a9ea-36ed-841c-9fac0b4c2088 | -10.168 | -56.6101 | 2026-06-17 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b2497847-c1d5-3e15-90ef-72df2eb7ea3c | -8.9635 | -46.9785 | 2026-06-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f5c7e480-d06e-3128-a75f-65da2e251f78 | -11.3413 | -51.4029 | 2026-06-17 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 091edb47-392d-3ba1-b5e5-beb23de1a7a7 | -8.8883 | -46.964 | 2026-06-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| e2871245-fbf3-38a0-8bb7-e359f9d43c68 | -11.3603 | -51.4009 | 2026-06-17 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c89dba30-cc47-329d-8625-484f0e07e274 | -10.7217 | -49.6561 | 2026-06-17 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 92a35bf3-3dde-3e1f-9571-183d0122228e | -13.9421 | -46.0367 | 2026-06-17 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8830618c-1390-38d4-9956-da735c791fe0 | -8.9824 | -46.9766 | 2026-06-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 23f95a2d-4d09-3b5a-8866-e3e3ad9f0ff2 | -9.0013 | -46.9746 | 2026-06-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 18c0c4a4-815b-3a1a-9942-54ea04d61f38 | -10.7024 | -49.6797 | 2026-06-17 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 96f490db-3288-31a7-b94d-8cd41336114a | -11.2239 | -46.5796 | 2026-06-17 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c6d9b44a-b50f-3988-95e0-15e44db2ce0f | -10.168 | -56.6101 | 2026-06-17 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| ec75eb4c-23ec-31d9-9b2e-182e49dc5954 | -10.7027 | -49.6582 | 2026-06-17 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 8b681b9a-4a89-3bd2-b18c-fe724ae6fb07 | -10.7024 | -49.6797 | 2026-06-17 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e7c7d21f-cba9-3a23-b477-8913adb98dc1 | -8.9072 | -46.9621 | 2026-06-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f20e9c82-c2f1-391b-a2df-f56552ab52e3 | -11.3603 | -51.4009 | 2026-06-17 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f1727f8d-12be-3481-b0f7-c43393a5abc8 | -13.9421 | -46.0367 | 2026-06-17 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 093580a1-a202-3eac-8d1d-35a3c79ab3f3 | -10.9971 | -46.4741 | 2026-06-17 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| aefd8875-8e9c-38cf-8e2b-b044dd06358d | -13.2845 | -46.0528 | 2026-06-17 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 2ee30852-933d-34f9-8cb8-4ff081ff373f | -8.8883 | -46.964 | 2026-06-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 74a3038b-1eda-3f33-8d1e-2afd1e0b18b1 | -10.1493 | -56.6115 | 2026-06-17 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 5a7217dc-c254-31fe-a063-be786d3dbc9b | -13.2651 | -46.0559 | 2026-06-17 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 64475f15-13db-3756-9d5b-2df6e85db9ba | -8.9072 | -46.9621 | 2026-06-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 62ef5c56-7825-3998-ac7f-4aed54705d0d | -13.2651 | -46.0559 | 2026-06-17 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c39a4954-fb30-3ea3-a63a-65c018690503 | -8.9446 | -46.9805 | 2026-06-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 391ee39c-70d3-3597-92e8-c5053a1905e4 | -13.9421 | -46.0367 | 2026-06-17 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 666e8d62-1d1e-325c-98b7-3bda03d66989 | -11.2236 | -46.6022 | 2026-06-17 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e2642ee5-7cf3-3233-8e3f-7cccc707812a | -10.1493 | -56.6115 | 2026-06-17 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| a094f9e0-8ed0-39a5-aec4-32526b289c74 | -13.2845 | -46.0528 | 2026-06-17 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 47afde53-580d-3fc0-8ebc-b24edf084795 | -10.7024 | -49.6797 | 2026-06-17 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| fe6b61dd-5094-313e-b033-067b0e662ffb | -8.9824 | -46.9766 | 2026-06-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e235c571-4910-314f-9fbb-1935897b76c1 | -10.7027 | -49.6582 | 2026-06-17 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 53157c74-1d8a-3e4b-b5e8-d5ccbf3bfe8e | -11.1125 | -50.1505 | 2026-06-17 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| eafc202f-5732-3018-b3a2-a750a3a833d5 | -8.8883 | -46.964 | 2026-06-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a384c58e-4ff8-3625-97c3-43b472e8a090 | -9.0013 | -46.9746 | 2026-06-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 415e72cf-8402-3811-853a-aca52f8720ac | -8.8222 | -44.8043 | 2026-06-17 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 777690ff-a0e8-36fd-8de5-eaf2f71e3fa8 | -10.168 | -56.6101 | 2026-06-17 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f2c4caf7-7db5-3c7a-9592-224e860ce324 | -11.3603 | -51.4009 | 2026-06-17 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 475eacda-aab0-32b3-b1d3-1e66441146c9 | -11.3413 | -51.4029 | 2026-06-17 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e18ea507-69dc-3d06-a504-0f99d02bf37d | -8.888 | -46.9863 | 2026-06-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a487e3ed-fdea-3703-a8a2-7bea4fe2ae5d | -10.1493 | -56.6115 | 2026-06-17 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 56358630-a8a5-3728-95cb-4d79c6ba279d | -11.1125 | -50.1505 | 2026-06-17 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 153ebad9-420d-3245-b65d-e6ae84f6cb7f | -10.9402 | -46.4589 | 2026-06-17 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| af9a5445-bf98-32af-80c4-f6db6d08b173 | -13.9421 | -46.0367 | 2026-06-17 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 776d842f-f503-3f0e-8d2e-485635acd0ba | -10.7217 | -49.6561 | 2026-06-17 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9779a05d-9619-3a78-9907-f90ca661b710 | -10.7024 | -49.6797 | 2026-06-17 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3f9098e0-58a3-31df-8156-cb870820bbd7 | -10.556 | -53.7283 | 2026-06-17 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6bda56b4-14bc-3bdb-b197-2af629df7e78 | -12.5367 | -57.2014 | 2026-06-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3887c677-c547-3b70-8d37-0781e89b7263 | -8.8883 | -46.964 | 2026-06-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| e1d9d0ee-ca40-3879-8bb5-faaa9f0e9c8d | -11.2239 | -46.5796 | 2026-06-17 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7c74b153-10c9-30d1-ba77-9c41b97c3217 | -13.2651 | -46.0559 | 2026-06-17 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 595006dd-f39e-3fb1-98cd-e2d084c6df3e | -12.8354 | -44.3657 | 2026-06-17 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 8f67d741-84c9-30dc-a1fe-ae550a5b83d9 | -10.7214 | -49.6777 | 2026-06-17 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ebc8319c-236b-30ae-b227-6a0f7dba1112 | -10.7027 | -49.6582 | 2026-06-17 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c0453aad-f5e9-31bb-8177-661ef00f0e59 | -11.3413 | -51.4029 | 2026-06-17 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e4286cac-18aa-3c19-b83a-b7c6b7a3a31e | -12.5367 | -57.2014 | 2026-06-17 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6893885b-0a13-39a4-9e4a-14cb7be989c3 | -8.8222 | -44.8043 | 2026-06-17 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| cce2cb34-6f23-3ac6-95f7-8098434d810b | -8.888 | -46.9863 | 2026-06-17 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 5c4ef945-6390-3631-a96c-b5279e7bcde8 | -7.8223 | -49.9492 | 2026-06-17 14:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |


[Clique aqui para ver as próximas entradas](README20.md)
