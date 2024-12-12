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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0f25a03-946b-3010-9506-fa592b66fe15 | -14.7457 | -52.6683 | 2024-12-12 05:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b3b5bfe0-c340-349e-9610-690d7c59701d | -3.2503 | -46.8709 | 2024-12-12 05:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 732b55ad-3968-312b-9063-e1120cc80aed | -14.7461 | -52.6471 | 2024-12-12 05:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| ab45c412-c8eb-32aa-9947-888c20929c7d | -11.1959 | -53.8348 | 2024-12-12 05:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 4ab41383-9fbb-3f5d-9ec8-38cacfb4d4ca | -6.9346 | -43.5168 | 2024-12-12 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d559b178-bb6d-38d2-85d3-590ff846d01c | -14.7655 | -52.6446 | 2024-12-12 05:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3cf1e300-ebf4-351a-ad7c-d6f01822c3e0 | -5.9185 | -48.0449 | 2024-12-12 05:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| ef3835f6-6206-306c-9825-4ae25f99d640 | -6.9344 | -43.5401 | 2024-12-12 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d48e54dd-e7b6-3474-9034-c0d9499135dd | -14.7461 | -52.6471 | 2024-12-12 05:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| c818880e-a5d0-3f8d-ae72-82215a4ce24f | -14.7457 | -52.6683 | 2024-12-12 05:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 92b62396-44de-33db-a009-241b91e249e9 | -6.9346 | -43.5168 | 2024-12-12 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 11df909e-6749-340f-b2a4-083ca91b4aa2 | -12.5682 | -57.7579 | 2024-12-12 05:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5623963e-fa56-325e-8a27-860b07adc0c0 | -14.7655 | -52.6446 | 2024-12-12 05:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e7e87422-9daf-3684-b022-1d81f413fdce | -6.9158 | -43.5185 | 2024-12-12 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 956e787d-41f1-3902-9bff-afae47f1173c | -6.9156 | -43.5418 | 2024-12-12 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| c130402c-7373-3aba-bcad-07311c312853 | -3.2503 | -46.8709 | 2024-12-12 05:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0af18627-7911-3cd7-8423-a3f4b10a9ecc | -14.7461 | -52.6471 | 2024-12-12 05:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3f74372b-d82c-35c1-9b63-e260c71e61e1 | -3.2503 | -46.8709 | 2024-12-12 05:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e7589b08-a3ce-3753-a3eb-582df68433f1 | -12.5615 | -58.3546 | 2024-12-12 05:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 202f18fd-97a7-3668-9365-890419fafc0c | -14.7457 | -52.6683 | 2024-12-12 05:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1a176e04-0c9a-3b6c-88c9-7a45e655a68f | -14.7655 | -52.6446 | 2024-12-12 05:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| be17f12b-e3fd-3f6c-b06f-d45b7f769002 | -3.2503 | -46.8709 | 2024-12-12 05:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ef64ab48-e4be-3357-864c-69b878049d4b | -11.2148 | -53.833 | 2024-12-12 05:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ef1a79b8-68c5-337c-a13e-556395f6d70e | -6.9346 | -43.5168 | 2024-12-12 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 060e1b11-d9a4-3cdd-af83-a0e1ceac3bfc | -14.7461 | -52.6471 | 2024-12-12 05:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0a99c16b-53f1-31ae-87ca-f688c19e142a | -6.9344 | -43.5401 | 2024-12-12 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 1fc0e9da-f0c4-356f-bafc-aa3aa87cea7c | -11.2148 | -53.833 | 2024-12-12 05:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 082b4c54-8e6a-32c9-9cb6-73e05be51232 | -3.2503 | -46.8709 | 2024-12-12 05:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1f0dc600-8df4-38a7-ac7d-a1a7243612eb | -14.7461 | -52.6471 | 2024-12-12 05:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 7ae9e233-9906-377b-b03b-e7c366605655 | -14.7655 | -52.6446 | 2024-12-12 05:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d20fd00a-f79e-377a-bddc-aec5a7ccc778 | -11.1959 | -53.8348 | 2024-12-12 05:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 09f11dfb-1ed9-35d4-b51d-636590fc30ce | -14.7457 | -52.6683 | 2024-12-12 05:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 205e898b-992f-3181-bc67-c98dc9ac6798 | 3.48438 | -60.21161 | 2024-12-12 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e6912cd-8236-365d-83e6-0bc4ab37599f | 2.47561 | -60.69064 | 2024-12-12 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40a2484c-d073-3d0e-b4c0-308687aabf58 | 3.17151 | -60.46173 | 2024-12-12 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 604da768-511e-3e7f-a71c-a816ff2329f6 | 2.37062 | -61.25669 | 2024-12-12 05:54:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fb29a85-5dfe-3212-bd9f-87bacc32f087 | 3.30334 | -60.07164 | 2024-12-12 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca030dbe-3268-3fc4-a361-dfae25d63c81 | 3.16785 | -60.46658 | 2024-12-12 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c668095f-ca99-36c8-a744-cb996ee238aa | 3.48316 | -60.20948 | 2024-12-12 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12f287f4-4e46-3a85-9d94-a43a983b9444 | 2.47426 | -60.69283 | 2024-12-12 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62fedc91-ba4d-30c9-b8b8-6f1bad79631c | 3.30262 | -60.06722 | 2024-12-12 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff924fff-464a-3bd3-9652-4c5bb1e5fb6a | 2.47855 | -60.69213 | 2024-12-12 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 083c2ee0-c79e-3fda-8a06-87bdc6c97e49 | 2.47624 | -60.69469 | 2024-12-12 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc24d2ef-a36f-39db-9a1f-24e46a00fd04 | -7.45413 | -72.62801 | 2024-12-12 05:57:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da140799-2fe8-32dc-a48e-cad0a4348afd | -15.08349 | -59.63518 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3eccd9d-0b15-36e6-9d18-3b1442c6df92 | -15.08395 | -59.63077 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14391ef8-ab9c-3b8e-ad13-5c7c3879feb6 | -15.094 | -59.64985 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2704472c-3cb7-3523-a4ab-b25b4ab2829b | -15.09588 | -59.6321 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a48f0a19-cdc4-32d7-900c-d4d32eeb2b6d | -15.07707 | -59.63881 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3819e3b2-f39f-3ca9-804c-a74a3fd0f4ec | -12.83338 | -62.01112 | 2024-12-12 05:59:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfa36b8c-0be7-3cad-bde2-60b063744d7b | -12.56822 | -57.76068 | 2024-12-12 05:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 21e8100e-635d-3864-8f85-53615c306e7c | -12.56111 | -57.7655 | 2024-12-12 05:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7fb7efb7-257f-3eaf-bf4f-96a156e75d2d | -15.02888 | -57.6138 | 2024-12-12 05:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4b629a98-bb93-3c83-9b60-d69ebef58c34 | -15.03294 | -57.61039 | 2024-12-12 05:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfbd4bee-258a-3de4-94e1-8e9e2e68ca52 | -15.07566 | -59.65222 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d95f6f85-8578-3827-b798-430e913eca60 | -12.56759 | -57.76635 | 2024-12-12 05:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f29749c6-9df7-38e4-ac29-5eb529c631da | -15.08302 | -59.63959 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c58ee89-57d1-3688-ad90-644637234d6c | -15.08442 | -59.62627 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c832ced9-2e28-38f7-8f3d-39ab71dc2a4c | -15.08945 | -59.63591 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78fea090-e13b-319c-ada7-fac49760a596 | -15.02948 | -57.60746 | 2024-12-12 05:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 56f940f4-7e80-31d7-97bf-a91bd71726e0 | -15.02561 | -57.61568 | 2024-12-12 05:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e020b7b1-6cc5-314d-b3d6-873250b24e0d | -15.02623 | -57.60947 | 2024-12-12 05:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d04b26d9-8f3e-3889-9b98-5e75b5bb52c9 | -15.07847 | -59.62541 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e5a793-f4ac-38f8-956b-f3be2df9e7f8 | -15.08255 | -59.64403 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbb6b2ba-2969-33c2-b5e4-3658f0ad6151 | -15.09447 | -59.64542 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e3aac9b-5e71-3657-a7fe-dfa804279b77 | -15.08805 | -59.64914 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbb1a46a-c2a6-359e-8bd4-b7a0810c16d5 | -15.97108 | -57.1683 | 2024-12-12 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 852d4cf8-d76d-332d-a791-8a49a51069d0 | -15.92406 | -59.81198 | 2024-12-12 05:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8232a03-95f6-369a-8106-250c94bada8e | -15.0849 | -59.62169 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 246560de-1d65-3eda-9657-21652be18292 | -15.92453 | -59.8074 | 2024-12-12 05:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87a40e19-7813-3e37-b66d-d63a2da4bb7d | -15.06925 | -59.65588 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c24d13e2-9dbd-3173-a3bf-3bb51a830c31 | -15.96473 | -57.16068 | 2024-12-12 05:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a41ed7ee-5f73-3402-85cd-8953f4f561d3 | -15.06972 | -59.65144 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbd02ba5-0db5-36f1-8583-7b112c0e8b62 | -15.08898 | -59.64031 | 2024-12-12 05:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9af69c1d-2130-30da-b8c1-a2ce54c1671b | -11.2148 | -53.833 | 2024-12-12 06:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ef21a59a-0fd3-3ce8-9dc9-7002b8df2c73 | -6.9344 | -43.5401 | 2024-12-12 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| fb31672d-bb03-33f6-8005-85597fe10cc7 | -6.9346 | -43.5168 | 2024-12-12 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 31472393-90e4-3c4e-9162-c48ac196c4db | -6.9158 | -43.5185 | 2024-12-12 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a18a7c43-55f9-3bef-9760-8cd48121b66c | -11.1959 | -53.8348 | 2024-12-12 06:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 22b344ec-358f-3e03-a811-e85bb12328ac | -6.9349 | -43.4934 | 2024-12-12 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c83baa92-497b-3f14-b2dd-e9fba268e736 | -2.97356 | -53.11122 | 2024-12-12 06:07:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4d68edef-1f25-3d8b-b91f-549e6d863b92 | -3.03571 | -53.25248 | 2024-12-12 06:07:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1f4f3b4e-6c30-3ecc-97fa-9a40abd57209 | -3.04386 | -53.83029 | 2024-12-12 06:07:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8326da9a-b079-3590-9450-fa400fd543d6 | -3.24253 | -46.86466 | 2024-12-12 06:07:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 1995fe1a-1317-3bf7-860a-ef6e61b3f466 | -11.19401 | -53.82743 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0eef2411-fa91-3d67-aabb-02d7b6d07d0f | -12.91635 | -55.04736 | 2024-12-12 06:09:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5336e344-2a4b-3d4d-8ad6-345c811f6833 | -11.20662 | -53.81529 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| b0a36661-a189-3299-8ace-13c00d26c394 | -11.20288 | -53.84261 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 89008242-e606-3c3d-a095-96404092cf03 | -12.91554 | -55.72716 | 2024-12-12 06:09:00 | AQUA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8af8cab0-b064-386e-8c1d-eb65eb554831 | -11.81467 | -57.8235 | 2024-12-12 06:09:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5a6cb51a-9b56-3587-89f9-32fab3b0ea6e | -11.11107 | -54.65551 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 94fd6ae6-bbfc-3b6c-b104-b345e771a8b7 | -12.92645 | -55.04876 | 2024-12-12 06:09:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f4a25d64-acb6-3752-a20a-f0244dc7dd95 | -13.68878 | -54.76259 | 2024-12-12 06:09:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 37578045-a43d-3156-990a-2c2ce04723c0 | -4.07221 | -54.3023 | 2024-12-12 06:09:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5337d7ea-0fbb-3f7a-bb0a-5f9bd371d78b | -11.11274 | -54.64368 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 466e902f-4f28-347a-80cd-e18bd404c785 | -13.69921 | -54.76398 | 2024-12-12 06:09:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b1c78d3a-af03-3803-9025-6c6fa799cdd4 | -11.19586 | -53.8138 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c4bab061-a188-3445-88e2-27c13379ad5e | -11.20474 | -53.82899 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1b81670b-c6c7-3b1a-8a0d-73cf709d5872 | -11.11172 | -54.64918 | 2024-12-12 06:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 96034bb1-6fdc-32a2-8e97-cba7067e0ca3 | -6.9158 | -43.5185 | 2024-12-12 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |


[Clique aqui para ver as próximas entradas](README34.md)
