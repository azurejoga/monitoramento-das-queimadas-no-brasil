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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d7df500-36e2-386d-91da-9e5419bbd17e | -13.7999 | -52.7875 | 2025-10-29 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 53676608-f4e8-3e0c-849f-836d42b9b145 | -3.5521 | -42.5383 | 2025-10-29 14:20:00 | GOES-19 | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 4bc0386c-3dfa-33b1-9c8b-562309e8c601 | -7.0695 | -44.9335 | 2025-10-29 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 9a704d4c-3f61-3ebe-bc73-d255afc1e0ed | -15.0706 | -48.7638 | 2025-10-29 14:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d1311d70-9c48-3092-9bbf-f6fe40ec8c8d | -7.6114 | -43.5914 | 2025-10-29 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 0cf84225-0a1e-3b11-b3af-3932b1adb2ad | -13.1104 | -47.1015 | 2025-10-29 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d87269cc-c3f2-3573-9cd7-c555a1e150d9 | -6.0999 | -42.4628 | 2025-10-29 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 147.1 |
| 395bbab2-df14-3e41-9c62-37a27d27d706 | -8.7622 | -46.509 | 2025-10-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 08c20d04-2ca2-3461-92ee-a9ac81cd2588 | -7.5054 | -46.2717 | 2025-10-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7f5c72fb-1811-387a-865e-cfc70d27d1fa | -7.3421 | -42.4656 | 2025-10-29 14:20:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 179.9 |
| 55e5c96f-90a7-390f-af66-8dd81c09d239 | -7.8037 | -46.4458 | 2025-10-29 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| d2a46da1-4a15-3dfa-8c19-00aa5e8aa986 | -6.6414 | -44.6051 | 2025-10-29 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 84903310-6150-3227-8866-88c4adf4da1f | -7.2943 | -44.9817 | 2025-10-29 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 8eece71b-2678-3de2-bca0-6f345cfa2efb | -6.8808 | -45.041 | 2025-10-29 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 386.4 |
| e2246cb6-babd-3584-a57a-98a9ffe0026b | -13.7348 | -48.748 | 2025-10-29 14:20:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3f595c9e-9971-3045-84b0-0cc796e8ac8f | -3.6887 | -41.581 | 2025-10-29 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 7a8b2255-87c7-34cd-8729-071918edfe81 | -7.2755 | -44.9834 | 2025-10-29 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d2b6a724-7217-37ee-8825-be2c8f9ba786 | -12.387 | -50.1515 | 2025-10-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 249.3 |
| eea5c687-43ec-37f7-b1a4-c36dc358c652 | 1.6387 | -55.6665 | 2025-10-29 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| db104d75-d942-3d3b-8b12-5d5be0b716cd | -7.9693 | -46.7423 | 2025-10-29 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 558a988b-9f7e-3b78-9c2a-eb4b6987c071 | -9.45 | -45.8951 | 2025-10-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 37135c02-17c7-36f5-a650-553ad6d4f434 | -7.7842 | -46.5145 | 2025-10-29 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 68408a6a-823c-3dac-ab42-6e6d4c9b3a0d | -7.9696 | -46.7201 | 2025-10-29 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 611e9893-eefb-3ee6-ad14-f9f78f010532 | -7.3418 | -42.4894 | 2025-10-29 14:20:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 158.7 |
| c2800d73-c0df-3a70-9855-4651991ca2d9 | -3.7262 | -41.555 | 2025-10-29 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 167.0 |
| 0551b61e-a783-3c1b-a24f-ff0e83085cbf | -13.9337 | -48.4305 | 2025-10-29 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 06be21ee-93b5-3adc-be0e-2d5a5b440d57 | -8.6523 | -44.8001 | 2025-10-29 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 824dc547-0251-3d2a-be56-d8576e409dbf | -13.0639 | -47.535 | 2025-10-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| cef2723a-530e-39f4-a351-acee54b37a2d | -7.6485 | -46.9044 | 2025-10-29 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ad937384-cd5e-3b54-b47e-003cdb72bf3c | -7.7847 | -46.4698 | 2025-10-29 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 37a3612a-f8ad-3f74-988c-83c9a4c3a392 | -3.8997 | -40.797 | 2025-10-29 14:20:00 | GOES-19 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 195.6 |
| cf7576b2-3858-32a6-9e34-93ec291f240d | -8.185 | -44.4593 | 2025-10-29 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e3390704-1440-3198-bfd9-78f19c3b6c98 | -13.5682 | -47.3468 | 2025-10-29 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 008fe2f9-06ca-3dfb-9990-fa2f663b3fa0 | -5.8154 | -40.8052 | 2025-10-29 14:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 06b5c6ae-0d18-3715-8176-cb16391809da | -7.5928 | -43.5699 | 2025-10-29 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| a77dd2b2-a6d7-30e5-ac30-28021d5807d4 | -13.0442 | -47.5603 | 2025-10-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9ef1752c-1b98-3698-9320-033005587e6c | -13.5686 | -47.3242 | 2025-10-29 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b9b06f0c-6ad4-30c3-980c-0f4c61adeee4 | -13.7343 | -48.7701 | 2025-10-29 14:20:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5abfb3a6-9de4-3c8d-8794-1eb05ddb44b1 | -10.3041 | -44.5785 | 2025-10-29 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| fb13ee17-0428-3fa3-ac7e-c2392e98d7a9 | -13.7807 | -52.7898 | 2025-10-29 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 09c277db-9ec1-364a-9b16-1aacfb362a2a | -7.3054 | -45.6833 | 2025-10-29 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1f6d5f26-b187-32b7-87eb-f37bd3a51bc0 | -13.0446 | -47.5379 | 2025-10-29 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 94d70a42-7b8b-3c50-8d2b-11988e80dd5a | -6.1467 | -41.5514 | 2025-10-29 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 403ded8e-e2a6-3f67-8a67-8fd1864f8e7e | -8.0633 | -45.1587 | 2025-10-29 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a825b185-0597-30fd-b85f-cba976008850 | -14.6119 | -48.3921 | 2025-10-29 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 15db6e03-0257-301f-b86a-ff50357a75a3 | -10.3037 | -44.6017 | 2025-10-29 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 7c723684-7cc5-3544-9024-2bb25fda0279 | -14.2055 | -48.3668 | 2025-10-29 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| ebbb9f4f-3b55-38f5-b843-43b5390130db | -7.0881 | -44.9547 | 2025-10-29 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3cd37dfb-cd63-38c1-8e19-69fab8078fc0 | -7.7847 | -46.4698 | 2025-10-29 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 3ebed03a-98b0-309b-8324-0879be8f85cb | -9.1606 | -46.3326 | 2025-10-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 3e746b0e-ac3b-3fb9-b57d-621253d154f9 | -14.2059 | -48.3445 | 2025-10-29 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a1ac18a2-c258-37a2-9fa7-f4f5881df0de | -9.4916 | -46.9893 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a1fdb062-6d0d-395d-986f-18d1a33aa2cc | 1.6387 | -55.6665 | 2025-10-29 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| caf348d2-816e-3b21-8c89-a1e280bb8846 | -13.7348 | -48.748 | 2025-10-29 14:30:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b09b8e7e-d651-39cc-8eb2-a38e131c8414 | -9.4497 | -45.9177 | 2025-10-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cef65173-8549-30aa-973a-67c9396aecfe | -10.2663 | -44.5603 | 2025-10-29 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| db8878d4-571a-370e-a631-3cf7ac6ce66e | -7.6114 | -43.5914 | 2025-10-29 14:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 51047ee5-01f1-3b5e-9aa1-126b019dc0db | -9.9004 | -44.8839 | 2025-10-29 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 7875cf32-fcf8-3ee2-8ed1-ac9dd6d42934 | -10.3041 | -44.5785 | 2025-10-29 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 3d1e1eee-5277-333b-b536-3dc9b2c6de7e | -6.6414 | -44.6051 | 2025-10-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| debc56b9-c8cf-31fd-8100-d770343aedf9 | -7.7844 | -46.4921 | 2025-10-29 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 75691a5a-ae81-38a3-9fe8-24003bcf7f00 | -7.9696 | -46.7201 | 2025-10-29 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 5e7415e1-db7b-30c1-9da1-14e038455816 | -14.8981 | -46.7659 | 2025-10-29 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 55907df7-f4b6-36e1-ad12-33456c2ba42f | -9.1612 | -46.2876 | 2025-10-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c5b1a3d8-74fe-3608-9be6-80cbeba62728 | -9.4739 | -46.9021 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b8df6de4-c500-36b1-91d1-75a7a0550b7b | -3.7075 | -41.556 | 2025-10-29 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 161.6 |
| 54abf065-00d7-3ce5-a5da-01465888ac90 | -14.6119 | -48.3921 | 2025-10-29 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7579b702-4a7d-32e7-ab28-3f01aad4b0e7 | -9.455 | -46.9042 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1d3234df-294d-3d24-b41e-073caa9227b7 | -14.4566 | -51.515 | 2025-10-29 14:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 9571af35-c28c-3a11-a9f8-7fa55969893e | -8.7622 | -46.509 | 2025-10-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e6b339a6-ed2f-3937-82a2-3d4cdbb6c615 | -7.0745 | -44.4756 | 2025-10-29 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b2917199-1bcb-305c-8b12-6d0a8f9c4d90 | -6.0999 | -42.4628 | 2025-10-29 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 6750cc73-55c9-36b7-85c6-056cdf93735d | -13.0639 | -47.535 | 2025-10-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 023d9657-5ab0-3459-bc5a-9702af6d5bb7 | -7.0883 | -44.9319 | 2025-10-29 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 4c3332c1-3192-35a2-8d9b-6b20c8c3d44a | -9.059 | -46.8797 | 2025-10-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b64d801c-954e-321d-b004-8836076d89f9 | -7.8037 | -46.4458 | 2025-10-29 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| c4df4b98-c3d2-38fb-84b5-27265feb4450 | -6.1658 | -41.5257 | 2025-10-29 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 44eb1fdf-e571-366e-a104-c17a5d6a69b7 | -13.0446 | -47.5379 | 2025-10-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f5ef0520-329e-37ed-88b2-3cf45d91276e | -13.9337 | -48.4305 | 2025-10-29 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| c5ca8b6c-e00f-3c1f-afdd-ad02ab580803 | -9.4361 | -46.9063 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 38abde2d-92ad-3ebf-8195-378d98c54042 | -13.5686 | -47.3242 | 2025-10-29 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| adbe297d-924a-3c0d-8f72-09d8c8372c0c | -13.5682 | -47.3468 | 2025-10-29 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 78a3eeb1-a5d8-395b-bea9-9bc208b11353 | -9.5106 | -46.9872 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 60062de6-b43a-3124-bcd5-85dd32e7b310 | -7.3232 | -42.4675 | 2025-10-29 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| f8c91aca-9a1f-3adc-ae6f-ea04520af5eb | -9.8624 | -44.8886 | 2025-10-29 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 51192c35-0b8a-3415-a5f7-9bfdf4d8911f | -10.3037 | -44.6017 | 2025-10-29 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 036a1b7a-2bc4-3fa4-8b34-a6e1688a7296 | -13.7343 | -48.7701 | 2025-10-29 14:30:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 7632b604-ca2f-3e53-9549-372b5aba2f31 | -7.0693 | -44.9563 | 2025-10-29 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 6cef9997-d17d-338f-b41f-7f6c734ec174 | -15.0706 | -48.7638 | 2025-10-29 14:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a0160a35-91ef-36b8-b5f2-b89dc7821fb8 | -10.3024 | -47.1867 | 2025-10-29 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 81980044-8151-3544-b9bd-a383f934d1ee | -10.2261 | -45.9389 | 2025-10-29 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d994aae9-2164-3918-9059-97f97752979e | -7.2943 | -44.9817 | 2025-10-29 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| c7a3e090-ca2c-3bb3-9159-de9effaaffad | -8.6523 | -44.8001 | 2025-10-29 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| fdffcfdc-916f-3867-99bf-370dabbe7041 | -7.9693 | -46.7423 | 2025-10-29 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 4760273e-3c2d-38db-885a-bd78b75a5c13 | -9.1615 | -46.2651 | 2025-10-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 59d39534-f1a4-3526-882e-ea556e0e330c | -7.3054 | -45.6833 | 2025-10-29 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 640a8b7d-e1d0-32b9-ae96-b5611f1ae7f9 | -7.9884 | -46.7183 | 2025-10-29 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d4bef19f-b6b5-3fe2-b43c-765335eb7009 | -9.1792 | -46.353 | 2025-10-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| fd976f3a-6a07-3377-865a-1e84053219ed | -9.7946 | -45.6282 | 2025-10-29 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| b43af8ad-dc4d-309a-bb54-4d0dec7ad69d | -9.8814 | -44.8862 | 2025-10-29 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |


[Clique aqui para ver as próximas entradas](README89.md)
