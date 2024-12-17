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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9491850b-65a3-3008-be45-2a54bd11669e | -5.0936 | -43.9176 | 2024-12-17 00:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 06022afb-29b0-3710-afc1-c18fc406ee8d | -3.2968 | -53.3749 | 2024-12-17 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f23b589b-770d-3bb0-a02a-32c3e92054fd | -5.1123 | -43.9164 | 2024-12-17 00:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4a19e9f9-8192-3ae3-9e0e-6d31beb30914 | 4.4435 | -60.9657 | 2024-12-17 00:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f99a03b2-9c8f-3365-a84d-3ea69a3b68d1 | -6.1953 | -46.2215 | 2024-12-17 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e0aa4c38-3332-3079-ac60-5115cabc83e5 | -5.0749 | -43.9189 | 2024-12-17 00:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 7f754ccf-35fb-316a-827a-d25eca7c0d60 | -5.0751 | -43.8958 | 2024-12-17 00:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 248353e6-d744-3ac1-9270-bb38266a44f1 | -6.214 | -46.2202 | 2024-12-17 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ebb8cc06-ce4a-3f48-bdde-43b60d6f9d4a | -5.0938 | -43.8945 | 2024-12-17 00:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 89d301aa-8771-3207-a714-d1bfd00b55cb | -3.2969 | -53.3547 | 2024-12-17 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b86728ab-2f2b-33ba-8a19-d4b3b40e2dea | -4.7952 | -46.4012 | 2024-12-17 00:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| db7ba58d-faa1-3514-a588-a96a7dc809c1 | -3.3152 | -53.3744 | 2024-12-17 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 61ed4337-83f9-3209-96f7-996de61f8ccf | -1.2216 | -46.7635 | 2024-12-17 00:47:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5109537-fcfa-35aa-a4eb-f2b1e15542c9 | -3.4369 | -54.042099 | 2024-12-17 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f635838-a185-319d-a7d8-34b71e2980f2 | -4.6428 | -44.3102 | 2024-12-17 00:47:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f467d715-fa13-3ba2-aeaf-b02eb67d274d | 4.4372 | -60.965199 | 2024-12-17 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 801ac2ec-1a0b-31ac-bca5-72a141f2bdd0 | -18.909201 | -56.024101 | 2024-12-17 00:47:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4135f32b-d576-3300-8a06-4f4739dd51c6 | -3.7809 | -47.114201 | 2024-12-17 00:47:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a54b308-e11d-36d4-9e7e-f038c1ee743d | -18.899401 | -56.0261 | 2024-12-17 00:47:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a50cd362-0d18-3caf-a34f-24f180c6a985 | 4.4417 | -60.946098 | 2024-12-17 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 75c1d658-c6e6-329b-a80b-b86f68e9fa15 | -6.1981 | -46.194801 | 2024-12-17 00:47:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 972d770f-90ee-335d-ba17-4921e99f5bf8 | -1.4004 | -47.447399 | 2024-12-17 00:47:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc950c0b-197c-36e1-9fce-d6610a6aaf70 | -1.3704 | -53.4702 | 2024-12-17 00:47:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d73182da-3fa2-3dd2-b5be-59dec25e2e37 | -5.0721 | -43.8946 | 2024-12-17 00:47:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f0713d0-bb7f-3af9-a5f2-4b4ce1662c14 | -4.87 | -44.153 | 2024-12-17 00:47:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5086a64-792a-3b43-bdbc-695e3e15a2fd | -0.7533 | -47.746799 | 2024-12-17 00:47:00 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27fe4174-2c3d-3e62-a0aa-88f484e7141f | -3.4353 | -54.035198 | 2024-12-17 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0362ba27-3480-35b8-8d96-01635771b143 | -3.4424 | -53.975399 | 2024-12-17 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d81ea4e-4731-3131-ace3-64cc5c0236ee | -1.5404 | -53.720299 | 2024-12-17 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca184ec-040a-3a9e-b1a2-3e1d539b6cf9 | -18.9014 | -56.036499 | 2024-12-17 00:47:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44310803-dd66-3858-9705-58b760395d1e | -3.8404 | -45.8564 | 2024-12-17 00:47:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54fef07b-efbe-3bcf-97b0-3306384c30b2 | -1.2696 | -53.025101 | 2024-12-17 00:47:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b63b04-1d9d-3f0e-b6fc-2f89dc5f1fa0 | -19.0669 | -52.843899 | 2024-12-17 00:47:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 21838213-c578-3f67-bae8-04613f056476 | -2.569 | -49.395 | 2024-12-17 00:47:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc9fb42-e51b-3187-8b74-47e6b8f6bdf7 | -3.1585 | -53.268799 | 2024-12-17 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f55972c1-8d47-3d2c-8fb6-003ed06da6cf | -3.8594 | -47.012402 | 2024-12-17 00:47:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17e3ae8e-776e-3a82-a2c1-7844293385f4 | -1.3944 | -47.465801 | 2024-12-17 00:47:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f5f4af-5a30-3d27-a6df-43edab318bfa | -3.1567 | -53.170502 | 2024-12-17 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adcd9fd8-fd09-3f73-aa74-bed56d01c3fc | -2.0036 | -54.310299 | 2024-12-17 00:47:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b122e87e-18d1-3f2b-a128-2f69625508d2 | -3.1551 | -53.1632 | 2024-12-17 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c873abf5-4a8f-3091-aec6-62827592483b | -3.1584 | -53.1777 | 2024-12-17 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 351bbf28-9fc5-309f-aa9b-6fe22a39c1e4 | -19.065399 | -52.8363 | 2024-12-17 00:47:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ca8f837f-22ce-3f12-88fe-7f39d704ec6b | -2.1407 | -48.034302 | 2024-12-17 00:47:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1bda471-c11b-31f8-8f0a-73b619bf7d81 | -1.5453 | -53.4235 | 2024-12-17 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9edbb8f-5d85-3f41-b654-e4d26e7fb96f | -18.8974 | -56.0158 | 2024-12-17 00:47:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0ff1155b-31f6-3c28-97ed-416025c3111e | -6.2021 | -46.211399 | 2024-12-17 00:47:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b551ca49-2bd7-3847-ae75-3ae738c61ccb | -15.8811 | -53.2589 | 2024-12-17 00:47:00 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd29f991-fcfd-380c-b9ce-877c09cfd98d | -1.2967 | -52.826801 | 2024-12-17 00:47:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12704da4-37bc-320d-a1cd-de80aaea6e37 | -6.1884 | -46.197201 | 2024-12-17 00:47:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e197e1a8-f5d8-3f36-b958-4171b306694b | -3.3006 | -53.349998 | 2024-12-17 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a55c5f85-8aa7-326e-ad85-a3610ecbda09 | -3.7772 | -47.098499 | 2024-12-17 00:47:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84b3fba7-68a2-3187-835e-a6188f35f179 | 4.4492 | -60.957901 | 2024-12-17 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf49dea-a36a-3c2a-afbb-114ff76a266d | -6.2078 | -46.192402 | 2024-12-17 00:47:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f955f804-f596-3146-aa0a-af4af91be410 | 4.4395 | -60.955601 | 2024-12-17 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a46616c8-7069-3603-abd3-32130ad362d5 | -1.542 | -53.727402 | 2024-12-17 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c851c61-8663-31da-ae4e-5c7117e19943 | 4.447 | -60.967499 | 2024-12-17 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1d595ca9-2dd6-30e3-8188-a6e86f01101d | -2.9381 | -52.707401 | 2024-12-17 00:47:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa45fca8-f084-3e80-b541-bd05a65d1c7e | -3.2343 | -46.796101 | 2024-12-17 00:47:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca7b0ba8-8321-3cc9-8e74-201158858fed | -3.3039 | -53.3643 | 2024-12-17 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53911fd8-5360-3f8b-8689-0f356e436974 | -1.4042 | -47.4636 | 2024-12-17 00:47:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dceafd1-de64-340e-b408-f4d63876a073 | -2.1374 | -48.019901 | 2024-12-17 00:47:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51710b64-9d2c-32e5-9015-b2470135a7d3 | -4.0384 | -46.902599 | 2024-12-17 00:47:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad6d9960-2558-362f-a2d6-da1259e113c8 | -1.3688 | -53.462898 | 2024-12-17 00:47:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c836c123-5479-3848-90f1-623e114b7368 | -1.2271 | -46.742901 | 2024-12-17 00:47:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e66f3b5-7b38-3c8e-99f5-6524f2226e3d | -2.9364 | -52.699902 | 2024-12-17 00:47:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99dde394-8abe-3647-a1d7-502200120767 | -4.6641 | -44.021301 | 2024-12-17 00:47:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 070434a0-cc80-3a38-a0df-005d9814b891 | -4.8796 | -44.1506 | 2024-12-17 00:47:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ea2d90c-bb7f-35da-997c-a8e3ea6c43ef | 4.4514 | -60.948299 | 2024-12-17 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bc43df79-a456-36ab-80f5-eb76a73df76a | -2.9266 | -52.702099 | 2024-12-17 00:47:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5567ef-e545-39c2-ace7-673349491852 | -3.7592 | -47.1525 | 2024-12-17 00:47:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d120e4-803b-390a-83d9-d1aadc5db058 | -1.3802 | -53.467999 | 2024-12-17 00:47:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd25410-28f8-3140-b3ab-200a8d0f9045 | -3.4408 | -53.968498 | 2024-12-17 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b6844c-106e-39ec-9098-8984356d32aa | -1.2313 | -46.7612 | 2024-12-17 00:47:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67917b31-e164-3e56-9626-520cd495f1c4 | -2.843 | -52.561199 | 2024-12-17 00:47:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d79a7903-4eb3-31f8-98c0-bb6837c8584b | -4.7589 | -46.697601 | 2024-12-17 00:47:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb4d7ff3-031e-3ce3-af34-0fb5fc061f6b | -3.2303 | -46.779301 | 2024-12-17 00:47:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b669e84-6bff-31d0-9f63-33df3e8cf83b | -3.8358 | -45.8372 | 2024-12-17 00:47:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b8e32b9-c2c6-393d-9381-b0284b8c1272 | -1.2756 | -53.460602 | 2024-12-17 00:47:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9fae657-123a-3c63-8203-902d547b554f | -3.4902 | -54.642899 | 2024-12-17 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0dd230a-a51d-32e2-a080-d9fd1cafafb7 | 4.4439 | -60.936501 | 2024-12-17 00:47:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c5d40bbc-0833-3aac-895b-af715e4fbd6e | -5.0756 | -43.867199 | 2024-12-17 00:47:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2b0a49e-b919-31ac-ae32-b8db4a1f180a | -2.5716 | -49.406502 | 2024-12-17 00:47:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f389f0ef-8120-3028-a692-c2a96f899ffb | -5.0659 | -43.869499 | 2024-12-17 00:47:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62683edc-3720-3262-9e4e-688d6a83c7d7 | -2.0051 | -54.3172 | 2024-12-17 00:47:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5e78476-4f43-3795-acc9-1d3291baae61 | -0.7435 | -47.749001 | 2024-12-17 00:47:00 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38647807-f11a-3332-b6da-a2d8b725c12f | -6.214 | -46.2202 | 2024-12-17 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| fa95baf1-a905-3967-9fb6-837685230cb9 | -4.886 | -44.1843 | 2024-12-17 00:50:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ebb9abcf-80eb-36c2-9cc0-ac94c2b80c11 | 4.4435 | -60.9846 | 2024-12-17 00:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 81dd82e2-3dfc-3851-b1ce-f2516e899f7a | -3.232 | -46.8056 | 2024-12-17 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b2da596a-190e-3ce9-9069-3aa19c4cb1f3 | -3.2968 | -53.3749 | 2024-12-17 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ed33bdaf-bce6-307b-bc9b-aa385ee0e91c | 4.4435 | -60.9657 | 2024-12-17 00:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 63a3fb13-fbe1-3041-b948-e375c0fcaecc | -4.7952 | -46.4012 | 2024-12-17 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4ba57cb9-c616-3cba-b84c-3a3fb8179ff7 | -3.2969 | -53.3547 | 2024-12-17 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ebf0d32c-e067-3b4f-81cc-76d9da32a63d | -1.2309 | -46.7691 | 2024-12-17 00:50:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c611e153-61ae-3be6-a012-c2fc961f6c46 | -6.1953 | -46.2215 | 2024-12-17 00:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3aff5b71-c78f-34b3-a23e-cabee9841a86 | -6.1953 | -46.2215 | 2024-12-17 01:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6aaab72e-f8d3-3aed-9ae5-75adedb29d57 | -19.1038 | -52.8711 | 2024-12-17 01:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 69481c9d-0e0e-3266-af76-8cee96659621 | -19.0842 | -52.8527 | 2024-12-17 01:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 174e46fe-b46e-3d88-839d-6cb68b000c97 | -4.886 | -44.1843 | 2024-12-17 01:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6711a4f0-a9b4-32f9-961f-9c3e4a1ed970 | -18.8994 | -56.056 | 2024-12-17 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |


[Clique aqui para ver as próximas entradas](README5.md)
