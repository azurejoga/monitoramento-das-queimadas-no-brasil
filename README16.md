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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce32beaf-f580-3076-b286-b51af5f6138e | -12.52139 | -57.21095 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7162be3-28e5-3aab-8d10-9a7a9890d4ab | -14.21146 | -45.52184 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5677d683-20d2-3b4d-9e74-7061bef2f393 | -11.07656 | -55.05626 | 2025-06-19 04:19:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a1bae5b-2d3c-3f60-98cd-00f8e62328cd | -10.23051 | -52.23469 | 2025-06-19 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be7b5cd9-91da-3e87-92c3-6f1aa664722c | -13.08194 | -43.50687 | 2025-06-19 04:19:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19d72f1a-ad02-3a3c-ba65-4113aaa93a4d | -8.32918 | -46.22909 | 2025-06-19 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54f133d5-f855-398e-95fc-c413864983e7 | -8.00838 | -46.78167 | 2025-06-19 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7574efba-19ae-3491-979f-f2cdfb56b46d | -9.48985 | -56.09118 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14a04ea4-ddf1-3e23-ab32-cfabfb3cdde0 | -10.15518 | -48.98882 | 2025-06-19 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 847a7b4b-e2a7-3c41-8db4-9e7d7ca5949b | -9.45818 | -57.85364 | 2025-06-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af5e6adf-634a-370b-8a7e-a51f64aa2e6b | -3.32181 | -48.71479 | 2025-06-19 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8427ea7-79b9-3160-a41f-abf7cde49185 | -11.81929 | -54.50284 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17fd66af-f171-3744-87e0-97319231b6dc | -10.65456 | -49.45322 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 192f0856-2030-3256-8205-7bd9daeb971a | -2.87631 | -40.38343 | 2025-06-19 04:19:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98efdca5-8eed-3033-a414-c8070e425ca8 | -13.50561 | -55.65436 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b3d6283-20d3-3ec7-a1bf-1f289bd310be | -9.48561 | -56.08653 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b67202a-16d1-366a-81a7-b373bd3893cb | -10.99175 | -49.54795 | 2025-06-19 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5aab368-5a21-3d1d-8b65-7c5a8eeba43a | -10.29192 | -57.13766 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2de50b5-b842-3f0e-bb55-65b0aeb6260c | -10.52246 | -47.58862 | 2025-06-19 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7be60e78-605b-354f-ada9-09d10722e90c | -10.95448 | -49.25228 | 2025-06-19 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ebd0539-6535-3c3b-9672-eba3bc4f606b | -12.46598 | -58.46913 | 2025-06-19 04:19:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 105350e7-816a-3f39-a84b-62f70ea0c88b | -12.06826 | -48.46548 | 2025-06-19 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ec53cc8-47c6-36fa-a1a5-09d86daea780 | -11.52022 | -56.98874 | 2025-06-19 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bece0cc-77ee-32ce-96f0-644fd96eca3a | -9.50307 | -45.45111 | 2025-06-19 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e31cab1b-aed6-303b-a553-dcecbc596bd2 | -12.52819 | -57.20773 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d72b9dd-1413-3465-bfc0-f7cd0ed90550 | -11.95824 | -58.74323 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 20b4cc47-f6cd-33c6-9540-b221e75f7c4c | -12.5829 | -56.9847 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8f439e7-d48e-327d-af6c-88d1d9332055 | -9.7241 | -48.31699 | 2025-06-19 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98f250af-8e58-3568-88f5-9b717507ed28 | -10.59034 | -49.46281 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25d6973b-6f60-3bd8-bc96-e38fab0f872d | -12.13416 | -54.66835 | 2025-06-19 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb771dde-eccb-311d-b594-3fda6367cfdd | -11.77151 | -54.36976 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d3a8c05-e040-3f3e-a77d-cd382160bfed | -14.0766 | -53.38528 | 2025-06-19 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad0d89bb-5a66-36e9-9a74-291c51552071 | -2.91409 | -48.2335 | 2025-06-19 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1eddb7e6-bee2-3b09-868e-c32003bbe947 | -11.52525 | -56.99455 | 2025-06-19 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9325d19-7559-3f23-8b19-4aa43f54b155 | -12.02644 | -57.09415 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4b6c0a3-6d7c-3596-ac95-b3bf765ccf5b | -12.52506 | -57.20826 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 637dd440-8457-3a0f-a2fe-277ae9ed8466 | -10.95486 | -49.25384 | 2025-06-19 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6a7d48c-c375-3f29-8246-d75f545f3027 | -2.87698 | -40.37912 | 2025-06-19 04:19:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fba2fd5a-50ff-3646-abbd-0c81583ae8bf | -12.5273 | -57.21224 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ea7b2d2-54ff-34e5-8f74-60e5ebf50de4 | -14.22257 | -45.51624 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21556706-c962-37dc-859e-a8ae2333fb05 | -12.02552 | -57.09872 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7faa5dc-ef91-3cf0-81ab-67adf08213b0 | -9.48642 | -56.08223 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e704446-ab9b-3aa7-b85e-acefd365a2b7 | -11.57423 | -47.87318 | 2025-06-19 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 109384cb-3405-334a-94b5-e166aaa6ca33 | -12.02289 | -57.09832 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58b79036-29f7-3aa5-a733-bf9d9d086b5a | -10.50614 | -53.57819 | 2025-06-19 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| df42eb07-f10b-3a28-aba0-b2d2ef66d695 | -12.42696 | -54.86852 | 2025-06-19 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeb5ec92-bd2e-3c8e-95c3-c1ef82512ab1 | -7.28275 | -49.99241 | 2025-06-19 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b683f05-dfcd-3f53-b116-1e40c173c86c | -11.52616 | -56.98997 | 2025-06-19 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e736237-e5d1-3fbe-8f7f-e8574a5fd829 | -3.40466 | -47.58632 | 2025-06-19 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d01bbd1-7853-3ad8-890e-a28790b45b0f | -12.07308 | -48.45819 | 2025-06-19 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 656fbd1d-4aa5-3b5a-85eb-f908d58a059c | -9.20826 | -45.34011 | 2025-06-19 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73a65572-cd5b-341b-80a7-6f36c43620c2 | -11.77241 | -54.36828 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00015291-3f05-3189-90ca-be1ef168a4e2 | -11.94816 | -58.75896 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9471d3a1-99e5-3cf4-b69a-00ccb1fe049e | -12.57707 | -56.98345 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f6f1451-5536-3c17-a125-c4807222959e | -3.00868 | -46.71999 | 2025-06-19 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7710ee32-063b-380c-a317-e8cec94f912a | -7.28335 | -49.98884 | 2025-06-19 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81f78dd7-6ccd-351f-ae1e-f6c00227e99e | -11.88696 | -49.33053 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35078ddd-9df0-3174-99c5-5980dec343ce | -11.76795 | -54.3643 | 2025-06-19 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ab851c-e0e3-308e-bffb-5ff0b115f447 | -10.64108 | -49.46486 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b8fd237-5b25-3e5e-bc9c-c3ea6bb7fa0a | -10.63234 | -49.42617 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79b983e9-c78f-3d89-8494-a3ca8f6bf581 | -9.32586 | -47.82965 | 2025-06-19 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffabe2e7-c739-3797-82da-362bf0a5bc5e | -8.91469 | -49.83753 | 2025-06-19 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba237158-63d0-3b6c-8e03-da7a06739fb3 | -11.56892 | -47.43177 | 2025-06-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce1cc0df-359d-3191-b429-49ce394dcfa2 | -2.91332 | -48.23828 | 2025-06-19 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e45aed0-a503-3b89-87f3-87d398edc9cc | -10.6389 | -49.45513 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1b4046f7-2546-393d-b946-c3e810b7e852 | -3.31702 | -48.71922 | 2025-06-19 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2981aaab-8e99-3d18-af85-4e695514429d | -14.21202 | -45.51824 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04ad4e5d-8df3-3def-a60d-c208ff09a499 | -12.022 | -57.10289 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccf4fbbe-5009-3fea-b237-6936ce3ccb1c | -11.12536 | -53.93586 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7c951c8-87b6-3c42-a39c-f86239ba38a8 | -9.79701 | -47.17595 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9526b0d-f8b7-36ca-b9e2-20c3d92b10df | -10.59187 | -49.46087 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46e85534-b059-3148-8f9a-725346602280 | -9.49727 | -56.08879 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ec5d9bb7-6bf8-3baa-aee2-2e7c22ae041e | -12.02378 | -57.09374 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb17e31c-8382-35bf-9499-8d3071ffe3e2 | -7.27871 | -49.9917 | 2025-06-19 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c60dc4fe-9f7c-3fb5-b27b-3db47bc5a340 | -14.4367 | -48.89994 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13a18e5d-3c44-3c9e-aef2-60bbc6ffb270 | -11.94276 | -58.75197 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 890cbbb2-b8cd-3849-b929-33dcc829d62d | -2.73311 | -47.3334 | 2025-06-19 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 55621c69-a2c8-3bbe-ba8f-22c0d731b1ad | -8.21643 | -47.61264 | 2025-06-19 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b477aa3-3fa1-36b3-8cfe-4fa0592eb3c2 | -11.8033 | -57.34814 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78ebab2e-8c5f-342a-a574-54749307402a | -9.49568 | -56.09228 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a52e40e-2f00-38c1-a464-c6bae987903b | -14.43951 | -48.9045 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea5bcb2e-8bd9-3434-a0c6-c19be85cc08e | -12.52414 | -57.21274 | 2025-06-19 04:19:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 101f5bd0-49d3-3fd4-8fce-f791d29a2088 | -10.45847 | -58.69161 | 2025-06-19 04:19:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb9492df-0498-3258-a134-8218616a35ef | -12.76309 | -44.4092 | 2025-06-19 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4931450-d7a4-352b-8b38-742ec5c8a516 | -10.15957 | -48.98509 | 2025-06-19 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ad1aa31-50aa-336f-9613-54a6a3899a80 | -14.21924 | -45.5157 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97aad581-0617-3b84-b86b-bf7a4fb67669 | -3.00513 | -46.71941 | 2025-06-19 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fd77e07-35f6-3df6-bc2f-777b7a2f9193 | -14.43885 | -48.90842 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24adb74e-7481-3c72-8937-e9409370bc7e | -8.95743 | -47.97734 | 2025-06-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f90fd16-9721-33ca-b4e9-afc4671a2b76 | -9.49225 | -56.08337 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 433e8140-bf65-3a08-8ddf-2cb57286cf25 | -14.06947 | -53.39843 | 2025-06-19 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97c0797a-c842-358f-9383-d843e8abe149 | -10.50509 | -53.58378 | 2025-06-19 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 74897f4f-85ac-347e-8c58-aa7725602733 | -14.21535 | -45.51877 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7bb5056-4b03-3e1a-a24f-8f3d8df3e787 | -9.32872 | -47.83415 | 2025-06-19 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d418619-9369-377c-82b9-9ac0a87f428d | -8.01178 | -46.78222 | 2025-06-19 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a32c419-8aad-3875-9b0b-3251425e211b | -9.418 | -48.43877 | 2025-06-19 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b100b2e4-a188-31c8-bdde-830a37b62d35 | -2.58622 | -51.92365 | 2025-06-19 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee601eab-70f7-3aaf-aeae-ff360ae2c835 | -11.14123 | -53.93282 | 2025-06-19 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fefe042-4802-3248-a97c-0af29bde6317 | -8.17257 | -48.87635 | 2025-06-19 04:19:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccba963a-c46d-38d2-aa6d-82cbf5b32186 | -11.94155 | -58.75784 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README17.md)
