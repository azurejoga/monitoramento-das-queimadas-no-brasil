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
| e7e5a6c1-1914-31e4-98eb-84212697b047 | -10.7217 | -49.6561 | 2026-06-17 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2f200db1-f3de-3bda-a894-91607983c10b | -10.7024 | -49.6797 | 2026-06-17 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fa4d60bc-6b3f-39e1-b89c-ed67a541bb95 | -11.1125 | -50.1505 | 2026-06-17 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 370f0c41-ea09-3579-960c-abdda5ba6be7 | -13.2845 | -46.0528 | 2026-06-17 14:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bc6da7b2-7257-3377-90b7-40b40cff08e5 | -10.1493 | -56.6115 | 2026-06-17 14:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 2ba22144-4021-354d-90f7-b9f240c9f5c1 | -10.7214 | -49.6777 | 2026-06-17 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c7c1c5b6-26b9-3cce-a360-adb519ee86b5 | -5.7943 | -45.0813 | 2026-06-17 14:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ddeee73c-0d05-34d7-968f-61e6d80757a6 | -8.8883 | -46.964 | 2026-06-17 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 67e1b9da-e2e5-345e-88b2-e678d1679ead | -10.7027 | -49.6582 | 2026-06-17 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cabb55b4-2d9c-31e9-9ad5-ac4b5513868e | -7.8221 | -49.9705 | 2026-06-17 14:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1aeb19eb-e73f-3f46-a759-82971adc0cd4 | -13.2651 | -46.0559 | 2026-06-17 14:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 25eafd2b-12f3-325f-8d0c-4fd6e75d0dfa | -11.3603 | -51.4009 | 2026-06-17 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a2afa529-1bbb-310e-8dfc-73437888faee | -13.2651 | -46.0559 | 2026-06-17 15:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 214417a9-f2ff-30b4-87c5-e1d2a9b4421e | -5.7943 | -45.0813 | 2026-06-17 15:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2c735699-98f4-3c95-abdb-70b93c72db23 | -10.1493 | -56.6115 | 2026-06-17 15:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 8281b630-ca20-3b5e-b229-473990b5e47f | -10.7027 | -49.6582 | 2026-06-17 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 13c427bb-9a7c-3df5-a7b0-415fb00cc6dd | -11.2239 | -46.5796 | 2026-06-17 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dad3128e-ddc7-30fd-9eb6-553273e8a628 | -11.3603 | -51.4009 | 2026-06-17 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b54e29e3-1e0a-3169-8298-2ab9abf4939a | -13.2845 | -46.0528 | 2026-06-17 15:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 08d6a84f-928c-3d90-9f3d-317598e02f75 | -8.888 | -46.9863 | 2026-06-17 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| da2302c5-a986-32cf-af39-8f8ef9e51468 | -8.8883 | -46.964 | 2026-06-17 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e9e820f4-b09a-31a5-9c71-42c11d36883c | -10.7024 | -49.6797 | 2026-06-17 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7a2abe1a-a2c6-30b1-826c-ba9f9a037be6 | -12.1762 | -52.7842 | 2026-06-17 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| db1cbf6f-3063-3eb5-b140-e2d4823c83ac | -5.7943 | -45.0813 | 2026-06-17 15:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| eb30fdc9-911b-3f29-bb80-d0807ac513e8 | -10.5374 | -53.7094 | 2026-06-17 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 01e11b5a-93f0-3436-b464-0141cab31a04 | -10.7024 | -49.6797 | 2026-06-17 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 47fae4d6-dafd-316c-8654-2ff2551ba285 | -13.2651 | -46.0559 | 2026-06-17 15:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| b56f751b-d10b-3ac6-bf08-21326360e221 | -12.233 | -52.799 | 2026-06-17 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 192.6 |
| faf8a11a-d954-3e68-90f2-69bc880b51d0 | -11.3603 | -51.4009 | 2026-06-17 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b0d3ee54-dc06-3586-885d-1e28f62d1ed2 | -12.2333 | -52.778 | 2026-06-17 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 246.9 |
| b0bece10-a3ae-3c3f-9e19-829d7eb5f4bf | -9.0015 | -46.9524 | 2026-06-17 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 42eea927-5f02-3ed7-9070-fc75c8dd7f76 | -10.1493 | -56.6115 | 2026-06-17 15:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 26691563-10a5-36e7-9c98-8d83df3501fd | -13.2845 | -46.0528 | 2026-06-17 15:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a45b5327-8458-30f3-aa19-ac71409137bf | -12.1955 | -52.7612 | 2026-06-17 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| cb31a412-c5fc-3d24-80d9-1f18361b0cb7 | -10.5372 | -53.7299 | 2026-06-17 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 47165b38-1db1-3382-915f-a29e66c8a7e0 | -10.7027 | -49.6582 | 2026-06-17 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6dcee4ae-b56d-36db-924f-cc58ec9031e7 | -12.2143 | -52.7801 | 2026-06-17 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 683.2 |
| 9670015f-5620-32a5-b779-e912425c590f | -12.5557 | -57.1998 | 2026-06-17 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d3b8019f-062f-30ea-b697-06e1e0608edc | -10.168 | -56.6101 | 2026-06-17 15:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 464bbc7c-d6f6-3249-a4b9-6bafc1bb9042 | -12.2143 | -52.7801 | 2026-06-17 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 780.7 |
| e3ddf168-983e-37fb-bec0-f881201906e1 | -12.233 | -52.799 | 2026-06-17 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 72e770d9-19db-3e84-b6ee-5d1a430d3c2e | -12.1955 | -52.7612 | 2026-06-17 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 190.3 |
| e6259b1c-f063-3fad-a304-4eb1c20a8f40 | -13.9421 | -46.0367 | 2026-06-17 15:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c5e29be6-f9b3-3147-a417-102049a5fb79 | -11.2239 | -46.5796 | 2026-06-17 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 4a3602a6-7c62-32f7-9f03-a66555b1e856 | -9.0013 | -46.9746 | 2026-06-17 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| da3c9eab-0225-34a1-99f0-7665b76bc108 | -10.556 | -53.7283 | 2026-06-17 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c9e6bf3b-2e67-32e6-9586-f97a5aee8f5a | -10.1493 | -56.6115 | 2026-06-17 15:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| e89e6e19-85dd-3137-999d-5634d2cb9d52 | -10.7214 | -49.6777 | 2026-06-17 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c0b6efd5-d1a9-3ff9-82ab-82b86e35c06f | -8.8883 | -46.964 | 2026-06-17 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 05fadd8e-9e90-3084-bbe7-a15f757be0c5 | -12.1762 | -52.7842 | 2026-06-17 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ccc1399c-f07c-38c7-b9de-26667efa02f3 | -8.9638 | -46.9563 | 2026-06-17 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ee41dfc0-1dde-3135-bb53-7584d77fde61 | -12.2333 | -52.778 | 2026-06-17 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 975e86ae-cfba-34b6-a59e-3f88aae52f80 | -10.1493 | -56.6115 | 2026-06-17 15:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| b52158c7-269c-3b97-b19c-dcdb17db97ae | -8.9635 | -46.9785 | 2026-06-17 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 18cbec82-edb8-39f7-9b84-fb040b91e036 | -10.556 | -53.7283 | 2026-06-17 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| def6fcd2-cd85-3070-a4f2-13bf29c0abef | -8.8883 | -46.964 | 2026-06-17 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 73fe371c-90d6-3231-96b1-ba7bd775ba8a | -15.0803 | -43.8612 | 2026-06-17 15:30:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 93270c31-679a-30d2-9e17-f51eb9049e45 | -9.0013 | -46.9746 | 2026-06-17 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 5b3e3a7d-c9d5-3392-99ce-06a1f12e5ad7 | -10.7214 | -49.6777 | 2026-06-17 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 5a36c164-82de-3996-ba5a-bc2e208d4605 | -13.9421 | -46.0367 | 2026-06-17 15:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b685787c-7fee-35ec-a4be-7390fc03c072 | -10.556 | -53.7283 | 2026-06-17 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 43467588-bf1a-374b-82ba-0d5b79cb7dfe | -12.2143 | -52.7801 | 2026-06-17 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 577.1 |
| ca95f7f8-829a-3827-8598-dc0f71ecfbba | -12.684 | -54.5736 | 2026-06-17 15:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2091747e-e23e-3db2-9b85-acab2e783620 | -12.2333 | -52.778 | 2026-06-17 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 225a589c-13a2-3e4c-80e4-0b7617816d93 | -12.1955 | -52.7612 | 2026-06-17 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 152.6 |
| f57816e1-d5f1-35ae-a9d7-47e675dd459e | -10.1493 | -56.6115 | 2026-06-17 15:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 215cfc93-fbf5-3483-9721-eda2422919e6 | -9.0013 | -46.9746 | 2026-06-17 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 230.2 |
| a5064c34-004a-3da6-89e5-67fc02fad90f | -12.1762 | -52.7842 | 2026-06-17 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 40d4a160-840a-3387-a1ec-48d47a3c61c5 | -9.6989 | -47.0332 | 2026-06-17 15:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 30eb4f3c-9727-3cd9-a525-23e1f34176b3 | -12.233 | -52.799 | 2026-06-17 15:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 446f723d-07d9-3a25-9b5e-3c27f5ab2d37 | -9.6989 | -47.0332 | 2026-06-17 15:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 91773ecc-acb5-39d8-98d1-f3f4a09dd09e | -10.5374 | -53.7094 | 2026-06-17 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c5ba3a35-497f-3be2-8ced-7d332d9b94f8 | -12.2333 | -52.778 | 2026-06-17 15:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 195.1 |
| e4b14c43-387c-3db6-a66b-b9cdede5eff7 | -8.9072 | -46.9621 | 2026-06-17 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b940563e-a07a-343b-85f2-bf71e8ee4a22 | -10.1493 | -56.6115 | 2026-06-17 15:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4f634ecc-ae8b-3235-867d-31d7e6e52be1 | -10.168 | -56.6101 | 2026-06-17 15:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ff76d4de-2d9c-376e-ab63-a79e7a3ce8cd | -12.1955 | -52.7612 | 2026-06-17 15:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5b14d328-440e-3b6b-825c-38200392f25a | -12.233 | -52.799 | 2026-06-17 15:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 6499f132-762e-345b-872c-890bfa8c9547 | -10.7024 | -49.6797 | 2026-06-17 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 106b2e95-7bcd-329d-b3d6-19b1259b2605 | -10.5372 | -53.7299 | 2026-06-17 15:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b30c3824-fa2d-39f8-8614-94543aeefd4a | -10.168 | -56.6101 | 2026-06-17 16:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0baf56cb-23af-3ed9-b80e-3c02ebdaad06 | -12.233 | -52.799 | 2026-06-17 16:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 498421ec-1238-3b70-8092-830608cc272e | -12.1955 | -52.7612 | 2026-06-17 16:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b406c88b-c303-3775-995b-12a1586adfe7 | -10.1493 | -56.6115 | 2026-06-17 16:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 52208276-0623-36f3-9cff-7d98c58f94e3 | -10.556 | -53.7283 | 2026-06-17 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0d209476-6bb4-3be0-8837-14dfb4fdc8ae | -12.684 | -54.5736 | 2026-06-17 16:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| b559a23e-0b35-3ee9-a495-720366245bda | -12.2333 | -52.778 | 2026-06-17 16:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 26194261-d0fa-36e5-9896-a10dcd8f946f | -8.9638 | -46.9563 | 2026-06-17 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a405fc5c-5dcf-391c-aa5d-21e4637ac4cf | -12.1955 | -52.7612 | 2026-06-17 16:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4f28813f-b6ff-3df6-a14f-8154345dc0a1 | -10.168 | -56.6101 | 2026-06-17 16:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 32351566-ec3a-3d94-96c6-07f15c2be72d | -11.2423 | -46.6222 | 2026-06-17 16:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8dbd8a76-f6f7-3234-9c49-f460ea0fc0d7 | -12.233 | -52.799 | 2026-06-17 16:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 829d0077-ebb6-34a9-aae3-8996f7e77d57 | -10.556 | -53.7283 | 2026-06-17 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6ae57a4a-c323-39d8-bb87-f7e6cb5b5f38 | -12.2333 | -52.778 | 2026-06-17 16:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0d901da7-b180-35c2-8d1c-f630229ba15b | -11.2427 | -46.5997 | 2026-06-17 16:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| c619068b-c02d-3440-83ac-2b50c9af59d6 | -10.1493 | -56.6115 | 2026-06-17 16:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| baa178f8-4dd3-3d21-883b-db64c29e358a | -8.8883 | -46.964 | 2026-06-17 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| ef3f7134-701b-3f69-97f1-4b88dba3d920 | -12.1955 | -52.7612 | 2026-06-17 16:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 553ca60d-d7bd-3130-b896-6baad1419251 | -10.556 | -53.7283 | 2026-06-17 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8bc9f431-adbe-3537-8cb1-8d7580c77c0d | -10.168 | -56.6101 | 2026-06-17 16:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |


[Clique aqui para ver as próximas entradas](README21.md)
