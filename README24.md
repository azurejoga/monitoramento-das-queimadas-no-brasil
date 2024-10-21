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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9b50792-e4ee-3c15-b053-68d6aa9aa14c | -6.07119 | -49.55518 | 2024-10-21 04:12:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43e6ab7a-5072-3df4-9ec5-14f444612cd5 | -6.07043 | -49.55968 | 2024-10-21 04:12:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22444b6d-5363-31cd-b600-1d02775bcfa3 | -6.01031 | -44.52234 | 2024-10-21 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a567940-8970-3479-95ac-ed5f8d3fcdd8 | -6.00971 | -44.52602 | 2024-10-21 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34e9737b-2460-398e-bb21-d65852932f36 | -5.94676 | -51.69658 | 2024-10-21 04:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d77df4d-c27b-3254-9239-696d39427f9f | -5.84396 | -46.2346 | 2024-10-21 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40bbed5c-900f-35b0-9e98-4c32f29e5c92 | -5.8242 | -49.96795 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47a8fe48-7982-3c6c-bbe6-aab7539dac39 | -5.69559 | -46.43095 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0d4ec21-7675-3ffc-8f67-3df57270f067 | -5.6926 | -46.42594 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b00d10e4-f6cc-3a4d-8c64-b47a7c94edd9 | -5.69188 | -46.4303 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa869075-3685-3d66-a2ca-610b692a1bb5 | -5.69115 | -46.43474 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e70f94c9-5832-3edf-b1b3-3ef31f36467e | -5.6889 | -46.42535 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5e51c8d4-94cb-3860-a113-258c569c09d1 | -5.68818 | -46.42967 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4c7c8e56-508f-3c26-911c-c1d1fad6b5a5 | -5.68745 | -46.43408 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 025c3fbc-1b59-3bd3-bbd6-fe628b23ff3d | -5.68519 | -46.42475 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0185a066-93a3-3ace-9f82-1399922bfe0a | -5.68448 | -46.42905 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1a0835be-fa14-3009-ad68-6fb63cd7b12b | -5.68301 | -46.43792 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d277d13-1c0d-38ed-9779-802531e487a4 | -5.67569 | -46.48208 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97b740b2-2158-34c9-bc67-6c86ad5712e9 | -5.59723 | -50.15775 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbe46381-b30c-3e1d-bffb-377ddcfe3f16 | -5.59707 | -50.15975 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02bbdded-19e4-3866-ac51-a369a0a7d63c | -5.50695 | -50.58205 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc56845f-3a50-33b0-8ac6-1d5a86e307ec | -5.50605 | -50.58743 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 124ad343-7fd4-3155-a853-4625102adaf9 | -5.50445 | -50.57784 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5537518c-3d6f-3433-a0e2-8dad178f3a36 | -5.5035 | -50.58322 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a487b5cf-9dda-3171-a601-75fdd2bb4220 | -5.50297 | -50.57584 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21ee1e4f-f19e-34f1-993b-eaa6f406063f | -5.50256 | -50.5886 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d246d5c1-f52a-314d-8828-31026b6fcea6 | -5.50207 | -50.58124 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b07ec3e1-e4eb-315d-8501-bc0fddac3a62 | -5.50117 | -50.58664 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6add356-fee3-33ad-b267-5f459d416031 | -5.49957 | -50.57706 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34543992-594f-3c11-9456-15b7a72510c9 | -5.49862 | -50.58246 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd089adf-cc4b-3df3-8e7a-e5a7b449df77 | -5.49809 | -50.57506 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5420e1-8007-3261-b235-8a453e56d029 | -5.49767 | -50.58783 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73dc0047-f01c-3211-8329-662f32c43a4d | -5.49718 | -50.58046 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0888a056-5128-325a-9595-5cc453762f50 | -5.49628 | -50.58586 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f61c677f-b0ec-325b-be44-7e0a37afac8f | -5.49538 | -50.59123 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95a8345b-2b30-3bff-b850-a06c013bd50c | -5.4914 | -50.585 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91e40643-c2ec-3be5-86aa-7da99353a6d0 | -5.47831 | -50.54384 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1e9ab6f-faf1-3064-a080-885673402bf4 | -5.47435 | -50.53765 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea167bcf-af33-3dc7-86e5-b7ec94f7f54a | -5.45203 | -49.56281 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d58d74db-c2df-3036-ad7c-a1125bdb34ae | -5.43668 | -46.35328 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 01975cbc-9728-3d8d-bc74-950bae9aaaf6 | -5.43598 | -46.35762 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0215d7e3-9500-3b8e-845f-1d2a6f974c4d | -5.43226 | -46.35706 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e6b1574-0e31-3df9-b4b1-42e2c69f1948 | -5.34836 | -45.63226 | 2024-10-21 04:12:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c57fa5dd-1e1d-3cfb-abd2-be5287fa8337 | -5.2797 | -49.29784 | 2024-10-21 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 71de4940-e399-3b9f-a799-18f0da2f384f | -5.22995 | -49.92939 | 2024-10-21 04:12:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39ac6366-ab90-332a-b7c0-148899c02276 | -5.16828 | -50.71431 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4e2d94f-9f2e-3092-9ca8-1aef55cd99f9 | -5.16729 | -50.71336 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed9dd67c-1cf2-3838-babc-7e4eb885ee4f | -5.16319 | -50.71426 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e77eccfb-6e84-3519-b855-6896e8f99ec8 | -5.16261 | -45.53694 | 2024-10-21 04:12:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51fb191a-9e18-3f85-866f-ff2ed463625b | -5.16223 | -50.71325 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e89b622-8347-3d14-a88f-00352e60977a | -5.06154 | -49.59167 | 2024-10-21 04:12:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81381fa8-0b2e-3002-b68c-8064bd8c0b6c | -5.05773 | -49.58629 | 2024-10-21 04:12:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66b05b1f-f912-344a-a40a-c8d36f1e780a | -5.05693 | -49.59099 | 2024-10-21 04:12:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02f0076f-5b3b-358f-add9-af62e5c71df6 | -5.0137 | -45.8194 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c8f456-91aa-31c2-8a1c-6796c6dfd111 | -5.01329 | -45.8208 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7979aa1-3232-31b2-90fb-dd93b962de22 | -5.01302 | -45.82354 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b90cf15-4740-3b10-bbaa-28168e0205d2 | -5.01273 | -50.84021 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 713520d2-20a1-3d88-9e73-497e4aca9c96 | -5.01178 | -50.84589 | 2024-10-21 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 649bda51-c1e6-35ca-ab1b-192b2c95bbef | -5.00653 | -47.65351 | 2024-10-21 04:12:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d204c6db-0262-3800-bbc6-956090970bab | -5.0025 | -47.65284 | 2024-10-21 04:12:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cafcefb4-9694-3086-a9d9-9b3bddd396bd | -5.00193 | -47.65635 | 2024-10-21 04:12:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bb1827c-8aea-3e7e-88bc-98c85c8c091d | -4.96588 | -45.90773 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0af9d662-aa8e-39d7-bfc6-59fabed44fa8 | -4.943 | -44.8648 | 2024-10-21 04:12:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a2e743a-08d6-32bf-a56d-949f61428f3e | -4.93953 | -44.86425 | 2024-10-21 04:12:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 890a7997-e3d2-34d3-acce-c6ec4b7217cf | -4.93015 | -46.84667 | 2024-10-21 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03d36cd7-a6be-37b9-9524-7af5951b1792 | -4.92139 | -45.88289 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfd6e612-692f-3e5b-981b-e4c276c39abe | -4.91081 | -45.83377 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9746060e-f5e2-3264-a327-7a5a602cb5b0 | -4.91011 | -45.83798 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cdebcec0-2c75-35fa-a20f-b537025dceba | -4.90942 | -45.84223 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9f6998b2-9a06-340e-a87f-cdf85bd635e1 | -4.90717 | -45.83326 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e9d49dd-3cac-3cd3-bc9e-199875f40b47 | -4.90647 | -45.83749 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09beb1bb-caa1-3256-912e-56f452ef6cbb | -4.90577 | -45.84175 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93e9c45a-72d5-300a-84f2-2926809ee568 | -4.90353 | -45.83274 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b6359fb-5eca-3db9-b0ce-39600a8c1b34 | -4.90283 | -45.83697 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddb4b9b0-3ffe-38f9-8a88-51712846596b | -4.90088 | -45.83563 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfb3c66b-8bd7-36d7-99c0-3a30880cb7d7 | -4.90058 | -48.27587 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74bcc426-29ed-3132-9172-8c3b06516ea0 | -4.89995 | -48.27974 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e6694ae-c021-36d1-9584-beeec2b2176d | -4.89699 | -45.82724 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4164881a-2579-3235-b1c1-18078ad19b91 | -4.89638 | -48.27518 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce56c84-2801-321a-b838-67bc0208bcc4 | -4.8963 | -45.83147 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0032619a-2f8d-3e25-9fb9-d7856e46e61d | -4.89575 | -48.27902 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0574d92-c6e6-3ab8-bb22-757e5cf091cb | -4.89559 | -45.83577 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71e40a1a-b4ef-3630-9958-7bfec24aaa27 | -4.89432 | -45.83009 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a3deb2ad-4734-30db-887c-90a06ae733df | -4.89364 | -45.83438 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7981a57d-4dbb-3eec-b88c-a3997d90b06a | -4.89002 | -45.83375 | 2024-10-21 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 104d61bb-37d4-35ad-8553-c1f29797d653 | -4.87559 | -48.65128 | 2024-10-21 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3761c5cb-e620-3c56-bc1d-66a3d345ad26 | -4.8744 | -48.65152 | 2024-10-21 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce13f13a-aa85-3cf3-876b-5abc0551940e | -4.87406 | -48.62628 | 2024-10-21 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9153bc6e-e5b9-34f5-b245-bf05169b721f | -4.87235 | -48.2118 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2febc1fb-5a6f-3970-a310-e44cf1876b96 | -4.84996 | -45.57792 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad0dc420-c83b-312c-8a92-5618e89e6653 | -4.84637 | -45.57736 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0997655-b0a7-3588-a77a-d3b92052235b | -4.75113 | -45.7919 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 085529d0-1ae3-346e-8cf5-7789291954e0 | -4.7475 | -45.79136 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5fc1409b-9a9c-3979-a8ba-5beb1f8cc2f7 | -4.74682 | -45.79554 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efd2a8c5-5ba6-36ad-b156-8ad6331c9afd | -4.73087 | -48.31233 | 2024-10-21 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23660fd7-cf0b-347e-9369-b71862f623cf | -4.69861 | -45.83989 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 465399f2-74a8-3453-ae28-96bbefd08e41 | -4.69604 | -44.59006 | 2024-10-21 04:12:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0523315b-39aa-3f69-ae07-f61da09d3549 | -4.69267 | -45.64275 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf70441e-5ff6-34a6-af8a-2ff784f0337e | -4.6872 | -45.81683 | 2024-10-21 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19faf779-9f24-3078-82da-c7d4a06a28a4 | -4.6851 | -44.59216 | 2024-10-21 04:12:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
