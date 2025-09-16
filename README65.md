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
| 308a0595-4d7f-334b-ba39-ec8a9352a76d | -5.21251 | -45.18371 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 872e729a-93b2-3276-9380-314000bf65ea | -5.79967 | -45.93719 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7011f204-44d4-35db-bfaf-f9a4a3b77b4e | -7.38877 | -50.0032 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfc2a95d-2f36-330a-8512-76fca9bd0d7c | -6.18666 | -43.47013 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c679dec0-63a1-3fd4-b778-ff3c9004baa7 | -6.34461 | -43.16757 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1da1c55-90ea-3221-a055-ab44479da840 | -4.13264 | -51.0797 | 2025-09-16 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0cb70f53-9269-3488-8d7a-e37529299fe4 | -7.52536 | -47.6587 | 2025-09-16 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fd3b103-e438-3a65-89f8-93978af0366c | -8.11733 | -48.27536 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 302b250f-847d-369a-b832-223304a01bea | -7.33675 | -44.59283 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11821bf5-5cf4-3856-830d-83f2a3ba8ce8 | -7.2727 | -46.58544 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f379954f-42a4-3010-ad27-68b6c5905783 | -7.679 | -46.28671 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0cc10073-410a-3e28-afda-6466d03e1cec | -7.99677 | -45.6678 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca351c4a-bddf-30a1-8f7c-bfdf8f34facf | -4.15462 | -46.79479 | 2025-09-16 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1adaa784-e63e-3626-becc-aa3601c0f4b1 | -7.00217 | -44.57507 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c088996-a9f4-35ac-9e19-dcd44d685535 | -3.82919 | -44.10394 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0b841a64-1aaa-3660-b72e-af7ab31cce82 | -5.79077 | -45.93576 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ed56b1b-fcac-3506-999f-1ad19a0012fd | -7.0095 | -45.638 | 2025-09-16 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 720d714f-462b-3f4c-ac29-e841f909d9f5 | -5.77662 | -43.93179 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 307bff65-9f04-3885-abb5-6e7fc0c2d87c | -5.79223 | -43.95009 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0eeab41-c4dc-3386-93d2-8ef9fcfff21e | -3.80994 | -41.57631 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e2d849e8-9e03-392e-b32d-b21372ab712a | -6.46092 | -46.01125 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 918f8580-4e69-3632-88b2-d977449325c4 | -5.93667 | -44.87277 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd294f75-b42b-35ed-8c71-33b3a6470254 | -8.11956 | -48.25997 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea5ac3d-1bb4-3b37-8da2-7f9fd2c0f74d | -6.06143 | -43.55262 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86d76192-6328-3148-a6bf-b687da59231a | -3.45242 | -53.83112 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f74e6e-38b1-3ba1-ae23-311a91c5525d | -5.92462 | -45.72791 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c2a3cde-c2ef-31db-a5ba-88250ad4ddff | -2.29923 | -48.14243 | 2025-09-16 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d774a02-116a-3e59-8f58-0a06b49f6131 | -3.17991 | -52.45056 | 2025-09-16 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1c16d3f-7898-3d55-9c53-537f43b64094 | -6.98979 | -44.77418 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66a4adc1-0fc1-31f7-84ed-778c62eee913 | -5.34254 | -44.82528 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd611616-3931-3f8f-96c7-446ae29b2d3f | -7.71211 | -49.55858 | 2025-09-16 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 24eec3cf-58f7-3b36-9618-4a665f7c547f | -6.18873 | -45.12652 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1eaefd69-fe85-3faa-ab47-9fdc8d3d386f | -6.82851 | -47.84294 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d775956-1aad-3628-9b26-3616b5565550 | -1.97586 | -47.98247 | 2025-09-16 04:49:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc1fb62e-4c34-35cc-8bc0-2c739293a69b | -2.9289 | -49.14208 | 2025-09-16 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8696ba28-f25c-3135-b229-9af13347d354 | -7.05298 | -44.11427 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 490c0cb4-39ca-32c2-9397-7de6d7dccd8d | -3.83902 | -44.10542 | 2025-09-16 04:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17f9b971-5dbf-3df8-becd-461452cee145 | -6.91949 | -44.79721 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9b1ccff-3b9b-352e-bb82-31c18b94e96b | -3.81353 | -41.55151 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a48f70fe-4866-35b1-a2fd-1c35aeed0b0e | -6.26145 | -43.46921 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78527818-ca6b-3e7e-bce1-653aa4ebcae9 | -7.21771 | -47.00068 | 2025-09-16 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5de00ab8-0a22-3e8b-9942-7330b0c9e9d8 | -7.0813 | -44.55618 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e48ca97e-22ca-35b9-bd0e-1a5e9afd73db | -6.51326 | -46.21638 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8249b33-7933-3041-a3ac-c44c23d9953f | -7.00881 | -45.64276 | 2025-09-16 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0a65cbf-6a51-3845-8fda-25b8dee2936b | -7.14008 | -47.97308 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87b3d430-84e5-34b3-9a22-24d753b8eedc | -6.63029 | -45.57794 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51f09b5c-0f26-39a5-928b-a4ea96b36b88 | -7.27095 | -46.59776 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d5960a86-9b99-3a25-aafa-c5498feb0de9 | -4.89793 | -49.9259 | 2025-09-16 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65621706-be88-32bf-9176-64c7e2e29364 | -7.59621 | -49.33077 | 2025-09-16 04:49:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01276e08-7394-33da-998a-0735b88f78ad | -5.79013 | -45.94012 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5ffdb21-1d49-308b-be2f-f6b8b24dd521 | -5.77194 | -43.92798 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 825c1e50-bd7c-3a27-8d2c-d6f6b2e827df | -5.9144 | -42.74374 | 2025-09-16 04:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9f61488f-94ee-3d86-9d32-98ed5a8b1c7e | -2.92952 | -49.13813 | 2025-09-16 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdab5261-49fd-3065-b904-909cd923c2ff | -6.11538 | -49.344 | 2025-09-16 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d85e25b0-4859-38de-ab08-f67218a2d85f | -3.21773 | -47.12756 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 85f1735a-bd43-344b-927a-c2c6bd5cec50 | -7.36762 | -44.29216 | 2025-09-16 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dec5ba19-b1b2-3a16-90c2-86730e610d89 | -3.13111 | -52.84633 | 2025-09-16 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7303b37-e802-3b62-8537-6a8df426718e | -7.68829 | -44.67061 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 836a8678-4957-33fd-9197-cfd421c9e4ed | -6.55132 | -43.99796 | 2025-09-16 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59952bc8-083b-34c8-97de-26e94874b679 | -5.77619 | -43.93474 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb8b4955-122f-397e-b583-52aff1430fc8 | -6.55577 | -54.98598 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ac5146a-83d2-3c59-b6c3-41067cdcd62b | -5.42276 | -43.19234 | 2025-09-16 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28b75f2e-0998-32d1-a1d1-3bd57384bf3f | -2.25896 | -47.85001 | 2025-09-16 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9f51691-b077-303d-8047-543574c38986 | -6.42578 | -43.31597 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 391d0214-1388-320e-9e01-0227cc92be0b | -7.2987 | -43.93224 | 2025-09-16 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66715c2a-17b0-3ccc-86f2-b086bb221d03 | -6.92364 | -44.80326 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30212edb-f911-3dec-a0b8-6929ef468a26 | -6.12223 | -42.94508 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e73d06b7-dd64-3b20-81f4-ea793d06300e | -3.21695 | -47.13264 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 159def35-2e3e-3308-b2d1-68afb0fcf865 | -5.34805 | -44.8209 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec16e645-1433-3436-9631-48ba3dd042c6 | -2.57421 | -48.39483 | 2025-09-16 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b393ece8-3da8-37a3-8b88-1d592c76cb05 | -3.0734 | -48.81824 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac98c02d-d1f4-328c-b52c-a3358d8e36a1 | -4.24209 | -54.91124 | 2025-09-16 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdfd7544-8a4b-3f38-870c-00907799507d | -6.45284 | -43.31919 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f44f9f2-76b8-39c0-9825-ce4de6b7ab00 | -2.80317 | -48.62829 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eab110f1-81a3-3136-82df-a55a9693cc1d | -3.08122 | -48.81523 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e335f564-a6da-3a07-8995-f6e475df333d | -7.43507 | -45.83539 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79c20a08-729f-3614-b784-33e2c8bfd4f0 | -4.15873 | -46.79539 | 2025-09-16 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c00cc895-46c2-3303-b50a-2d18fc0f54e8 | -3.13675 | -44.42671 | 2025-09-16 04:49:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa2bf11-c512-3cf7-98f0-4bf73c369aa0 | -3.57079 | -51.56564 | 2025-09-16 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aebeb593-c338-3ec6-a86b-224f7a5ef8c7 | -7.40478 | -49.99329 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d99e8287-5f2a-3859-8360-3c8a6f52673b | -7.1434 | -47.98836 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d176e87-5ef2-31f2-868e-26fb3cf904ea | -6.52613 | -41.83102 | 2025-09-16 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d33ef6c6-9481-38d3-a8e5-80c5fc9361c2 | -8.41667 | -45.73901 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 187b7857-5b57-3e84-8b26-21b339534bc9 | -7.51323 | -44.7155 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 284eba13-c755-3efb-911d-610f2d8e40bf | -3.82269 | -44.11417 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ca24151-4a3a-3b2d-9c64-1143f97391cf | -5.11879 | -46.13316 | 2025-09-16 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b3d76c6-ff5b-3c97-a4d0-c6e9c1771970 | -7.27788 | -46.61149 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc389cf2-ecf1-3607-9f7f-8789b4e33059 | -7.4438 | -46.16903 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2b34fd5-58fd-3459-8539-a0f877d5a35c | -6.17908 | -41.20944 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6563c436-c0b9-3345-9e36-2918fb647419 | -6.40637 | -43.33737 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2812a717-8fa1-30dd-a256-8f4a87e66e91 | -6.97131 | -44.54016 | 2025-09-16 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d955d3c-af96-3c1c-9417-7986f86bca25 | -7.26916 | -46.61034 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 76ab62aa-8717-3d04-a0ca-c28188bbd358 | -7.71738 | -50.36378 | 2025-09-16 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69219650-dc85-3543-bb5e-f00fb6f02861 | -5.99816 | -43.69981 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97862239-af4f-331f-b09e-44f8df99542a | -5.79652 | -45.92772 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fe9fc1d-e567-312e-be7b-e7cea08e3210 | -5.77372 | -43.91574 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b0b19cd-09f8-32f1-9740-5c37b2b1b056 | -7.19618 | -48.60596 | 2025-09-16 04:49:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3763e0e8-54ad-3fde-abd2-27fc6abeec28 | -5.19121 | -45.58566 | 2025-09-16 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a08b0f0f-676b-3e80-9c3a-51e68d7b935a | -6.53223 | -51.19416 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00673012-43ac-3439-8371-3546721f3788 | -3.80935 | -41.58041 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README66.md)
