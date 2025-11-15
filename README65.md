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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19018e11-626b-3bb4-aacb-ee7971456041 | -9.9567 | -44.9228 | 2025-11-15 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7eece659-9302-312a-9838-97bbf66d8777 | -11.9175 | -46.2135 | 2025-11-15 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a561a696-a0ca-3239-841a-d8e734637046 | -9.8542 | -44.1729 | 2025-11-15 14:40:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 9b98e6fd-1d7e-3ad9-8f45-0d111bebbd00 | -11.7904 | -48.089 | 2025-11-15 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0383cd8a-6eed-3504-8cbf-d335046e1fd0 | -11.7094 | -48.386 | 2025-11-15 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 8145db1e-fb18-363c-80b4-f4412a98740c | -8.5792 | -46.0794 | 2025-11-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| e8b525ad-942b-3d7c-9a74-ad1f392564d4 | -3.0574 | -44.4148 | 2025-11-15 14:40:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| ff8f8cf4-4fcf-3994-98fc-0beba55d5229 | -10.5461 | -44.9159 | 2025-11-15 14:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 316.8 |
| 77f763b2-5b83-312a-a2d3-fb2362d2f9c5 | -8.6808 | -45.5041 | 2025-11-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 759.2 |
| e2ad559c-b0e5-30b4-b813-5e7e09050ea5 | -11.7017 | -48.8692 | 2025-11-15 14:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 24f41d98-1cda-3f0d-a90c-2bac76b0b107 | -10.3232 | -44.576 | 2025-11-15 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 189.0 |
| dc5fc8af-1a41-3ff3-aafd-bb629be56955 | -4.1787 | -46.8313 | 2025-11-15 14:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8099fb8c-b9dd-3234-a1d4-295fc3941218 | -12.4436 | -47.891 | 2025-11-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e233bd36-29e3-3dd0-b931-4c7b8102de79 | -9.1384 | -45.1808 | 2025-11-15 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 09052d1b-dcf0-3a3b-86bf-738c775fad8c | -12.4109 | -47.5616 | 2025-11-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 0188132c-e1cd-337d-998e-c321ee157f7b | -11.6755 | -44.7342 | 2025-11-15 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 444b1f0d-1cd4-31a1-9d52-8e776a9488da | -4.862 | -40.1463 | 2025-11-15 14:40:00 | GOES-19 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 0071f638-3177-36eb-9509-c79d4b626739 | -6.1608 | -48.0289 | 2025-11-15 14:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 8a852ad8-c59b-39a3-8dab-ed5765df36d7 | -8.5609 | -46.0363 | 2025-11-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 484c6b19-8eff-3c39-98bb-8ce9d124c7db | -4.5033 | -42.862 | 2025-11-15 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 23322810-75da-36a4-b4ef-f7ff37da8b32 | -6.1233 | -48.0532 | 2025-11-15 14:40:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 266.8 |
| cfe98c73-badd-3007-9618-60a7d5cb8816 | -12.3914 | -47.5867 | 2025-11-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| a8da75da-f54a-3532-8535-924a44572c7e | -12.4106 | -47.584 | 2025-11-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 7a1f178f-82fa-36f8-840d-5390e212cab1 | -12.0748 | -48.2065 | 2025-11-15 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fd3fd0e0-ede8-3f28-b56f-dbf2686711bb | -3.7101 | -47.6403 | 2025-11-15 14:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e22d1439-daa8-3b6d-86c5-6b5bf513444b | -10.1722 | -44.5032 | 2025-11-15 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| bc17e0dc-7da0-39f2-812a-a2f08a9dcfce | -6.0309 | -45.8085 | 2025-11-15 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c906ce0e-e1d3-3152-91fd-043789e2a5d4 | -6.3046 | -48.6469 | 2025-11-15 14:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 65ce4942-1c30-3244-95e2-6b0e52c619a6 | -12.3917 | -47.5643 | 2025-11-15 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 7f6b63b7-eda2-3966-9640-74c2199b0ede | -12.8534 | -46.4392 | 2025-11-15 14:40:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 1e3168ee-2c99-3d29-a532-82c7e091c6bc | -9.9564 | -44.9459 | 2025-11-15 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 522.7 |
| d53f766b-543b-3fbc-8f83-bdde5c307d7b | -11.9171 | -46.2362 | 2025-11-15 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| eb8d8d03-538c-3161-a098-938d2176ffe6 | -10.6517 | -44.2765 | 2025-11-15 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 563d2690-2a02-34f0-b8b0-b431b44dcbbe | -4.0067 | -47.6711 | 2025-11-15 14:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e6d15873-3d8e-3a7e-a56a-c92fd2221de4 | -12.6741 | -46.7831 | 2025-11-15 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 6361afe5-2583-3fef-8495-1c38200a987c | -12.0557 | -48.209 | 2025-11-15 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 94605a6f-6266-3eec-a8b3-1a77e7e92447 | -10.3228 | -44.5992 | 2025-11-15 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 292.2 |
| 6fdcd392-6464-3aee-81a7-538422212a57 | -9.9754 | -44.9435 | 2025-11-15 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 4525dca3-8e69-338e-bd02-d3039cd74e1c | -9.7549 | -45.7464 | 2025-11-15 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 54214023-0baf-3391-bdc9-1346a72362c3 | -8.5418 | -46.0607 | 2025-11-15 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 07a46373-6e78-3bf8-b82f-893143fef4e7 | -1.2934 | -53.7565 | 2025-11-15 14:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fd5e3ace-6274-3b71-a3b9-8b45bcc3b345 | -8.1967 | -45.0312 | 2025-11-15 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| e8652996-85ed-35d3-b4a8-08a61c9c35b2 | -4.576 | -43.1384 | 2025-11-15 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6f598916-871c-373f-ab58-652a205e8e76 | -7.3868 | -48.6545 | 2025-11-15 14:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 56.0 |
| cb816305-c62f-3b54-ae7f-5a847218a732 | -11.9179 | -46.1907 | 2025-11-15 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 6fc227cf-86a0-3628-b744-bf173e4ed9ac | -11.4977 | -48.5223 | 2025-11-15 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6db69b26-2ed1-3570-8242-f7b37ead66fa | -12.8538 | -46.4164 | 2025-11-15 14:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 569deacf-e9fd-36f3-83ef-315319a30c4f | -9.2325 | -45.2157 | 2025-11-15 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 0bd47b81-593c-30e5-9638-9ccc6820213a | -8.5675 | -45.5161 | 2025-11-15 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 8981a5cd-075c-3390-83eb-454b0cf0be0d | -9.736 | -45.7487 | 2025-11-15 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 214.3 |


