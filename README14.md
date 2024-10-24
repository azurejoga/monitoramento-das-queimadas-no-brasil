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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7091faa1-8e71-3030-8ad4-3144ec41a9a6 | -17.0207 | -57.3743 | 2024-10-24 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| befcdabf-ff2f-3722-9ec1-66e8bf5da551 | -17.2383 | -57.2462 | 2024-10-24 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 34b57786-1ffe-319d-8912-ee6537a37b1d | -17.2579 | -57.2439 | 2024-10-24 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 7e6c5bf0-96d7-3028-a075-0540be48ad0a | -17.7062 | -57.4774 | 2024-10-24 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| e229279a-6600-3b81-a076-16ab920ab329 | -17.7844 | -57.5091 | 2024-10-24 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 6db3ed13-0560-38cd-8acc-434f26c264ef | -17.7834 | -57.5708 | 2024-10-24 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| a1638a72-ff77-3514-9a0c-1217f7a0494a | -17.7831 | -57.5914 | 2024-10-24 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| a29031a6-4b19-3a9f-8130-a39ef36b1da1 | -18.0837 | -57.3076 | 2024-10-24 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 439a5b45-ece4-3f63-a604-d06fa45b4ff3 | -18.3199 | -56.2404 | 2024-10-24 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 4c988440-df9a-39f3-aec9-bc6bb7c7c272 | -18.3203 | -56.2195 | 2024-10-24 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 7b226e66-1be1-3061-9113-f1e2246a8ea3 | -19.548 | -56.6143 | 2024-10-24 02:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 73aad4b5-8f00-3f9e-976e-5e47327b027c | -19.5681 | -56.6114 | 2024-10-24 02:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.3 |
| ca393d29-8b79-3746-9531-9f69f305e831 | -19.6438 | -56.8521 | 2024-10-24 02:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 07e0777d-b654-3f3b-920d-22550a937f52 | -19.6442 | -56.8311 | 2024-10-24 02:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| cc6dc8d0-7de5-3e80-8d31-70e88dbb5630 | -23.816 | -55.2713 | 2024-10-24 02:27:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| d35e2d71-55c0-3883-a9e2-adfe5271b55f | -1.4945 | -54.1962 | 2024-10-24 02:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 82ee9f8e-b2ce-3b13-9f9a-f846c37d8503 | -1.4945 | -54.1761 | 2024-10-24 02:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 044fc4fa-7d1a-3fee-84e1-9cc151c64130 | -1.5504 | -53.6931 | 2024-10-24 02:35:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 83a2ecc3-9547-305b-b895-775d16227b1d | -1.5878 | -53.3292 | 2024-10-24 02:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 7bdc7fb4-ef2d-3164-ae30-0bfe14989ad8 | -1.5878 | -53.3089 | 2024-10-24 02:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ae36ac60-83c6-337d-9a43-25df1518d6c1 | -1.6062 | -53.3087 | 2024-10-24 02:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 00f80c38-bfed-30c4-a616-f2910c35db30 | -2.9578 | -50.4198 | 2024-10-24 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 10450adc-db1c-3c38-b6ef-715744e1699b | -2.9763 | -50.4193 | 2024-10-24 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0c637aaf-b14c-3421-bc54-e0eedd0ae40f | -3.0745 | -53.8252 | 2024-10-24 02:35:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 74f079a8-653d-370e-891c-7a8109b69725 | -3.1101 | -54.1661 | 2024-10-24 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 274fa4ec-66ca-32da-995e-d1968db161a8 | -3.1102 | -54.146 | 2024-10-24 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e5fab602-8d0c-3fe6-8d36-3735fd5aa564 | -3.1606 | -50.4766 | 2024-10-24 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5ab812cf-8b65-3893-8fa7-e99bef1c9c80 | -3.1607 | -50.4556 | 2024-10-24 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b8a30511-01ce-326b-a9d0-02df82adc828 | -3.6612 | -54.2715 | 2024-10-24 02:35:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8f11f3b9-e078-3293-95a4-7100d29b5bb0 | -3.9394 | -46.445 | 2024-10-24 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e370a934-5932-368b-9653-290cfeed2755 | -3.9396 | -46.4229 | 2024-10-24 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c2e4cd04-0b2c-3247-bc8c-ac943f2814f8 | -4.758 | -46.4033 | 2024-10-24 02:35:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 02425f2d-9007-3db4-ab16-d61d22d54964 | -5.4373 | -47.6833 | 2024-10-24 02:35:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 25fae58e-032f-3e9a-93e1-66d92cfa5882 | -5.4559 | -47.6822 | 2024-10-24 02:35:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 5d28a8a6-9f20-32e5-a689-b001cfa41c2a | -10.1969 | -53.8822 | 2024-10-24 02:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 88aa14cb-1cc1-3d1c-9a03-444213c1a005 | -12.6914 | -43.8484 | 2024-10-24 02:36:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ed9ce2a8-824f-35ab-ad74-51574ac6a0c5 | -13.7609 | -54.0661 | 2024-10-24 02:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b2242752-8ed4-33d8-aeb4-d08903548c6f | -13.7612 | -54.0453 | 2024-10-24 02:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e35b8b7e-c248-3a4f-b15a-cae413ccb22e | -16.94 | -57.5268 | 2024-10-24 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 9a6a74a9-8732-34d7-8b1c-f6bbbdbb9e3c | -17.0011 | -57.3766 | 2024-10-24 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| ef611c69-8cd5-3054-8b0a-623f51b96b46 | -17.2383 | -57.2462 | 2024-10-24 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| f1af5b3c-8db3-3c7e-8bc9-0d4f2510b0fd | -17.2579 | -57.2439 | 2024-10-24 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 4c0b78f3-2196-3642-90b6-d9b6db238ce7 | -17.7834 | -57.5708 | 2024-10-24 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 4bb8c797-27d4-3a7a-a7c5-949673d30610 | -18.0837 | -57.3076 | 2024-10-24 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 0e9dbfe6-feed-33be-8977-864298e0071a | -18.3 | -56.2431 | 2024-10-24 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 4c3a1e54-3e80-3b8e-9c40-b43b58ef3593 | -19.5681 | -56.6114 | 2024-10-24 02:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.7 |
| 07aef420-0f81-3822-9447-debe91726bb4 | -19.6438 | -56.8521 | 2024-10-24 02:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 8e7c4714-ba97-39fc-a238-162466406324 | -19.6442 | -56.8311 | 2024-10-24 02:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 881402c4-987b-336d-9cb6-372ef830360d | -1.4762 | -54.1964 | 2024-10-24 02:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 72846315-9c22-3c9f-b11d-17b5c4fbdae9 | -1.4762 | -54.1763 | 2024-10-24 02:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| a9a52afb-3ec9-32c9-9a7a-cb22b99b3bdc | -1.4945 | -54.1962 | 2024-10-24 02:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5d8e1d14-ecda-3911-a3df-63595365622d | -1.4945 | -54.1761 | 2024-10-24 02:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 90c5b623-b3dd-3297-b5e1-337eaac065f2 | -1.5504 | -53.6931 | 2024-10-24 02:45:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| f7b8cb3f-fef6-342c-83c6-c86ede143385 | -1.5878 | -53.3089 | 2024-10-24 02:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0574952a-273e-36a5-b538-6f11450a9af7 | -1.6062 | -53.3087 | 2024-10-24 02:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 440acb2d-a308-3eba-a07d-57bb78da531b | -2.9578 | -50.4198 | 2024-10-24 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 4f3cfe51-5cdf-35e4-8c21-a31b5b4a4e02 | -3.0745 | -53.8252 | 2024-10-24 02:45:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c629d228-70b8-3aea-9538-3cbbcbb53bec | -3.1101 | -54.1661 | 2024-10-24 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1a3fcc5c-1ab4-3b8f-8ce8-c6529ed38057 | -3.1102 | -54.146 | 2024-10-24 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 86320dcb-a5a9-3a44-ac05-4d04d13ef370 | -3.1606 | -50.4766 | 2024-10-24 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 10c70903-96ad-3d37-a632-fbad41331245 | -3.1607 | -50.4556 | 2024-10-24 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fab9a564-fe69-3f4c-8c96-02d576990c8b | -3.9394 | -46.445 | 2024-10-24 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 51d39165-43ec-35be-ba9f-d1f03494cab4 | -3.9396 | -46.4229 | 2024-10-24 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 709e1192-96aa-3ba0-b1d3-a6955ead8927 | -3.9581 | -46.422 | 2024-10-24 02:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e013356b-5025-3762-a134-bcc0e8a3a6e8 | -5.4373 | -47.6833 | 2024-10-24 02:45:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 84f8adbd-8376-3390-84e4-e6bd32c85ef6 | -5.4559 | -47.6822 | 2024-10-24 02:45:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2e88c59f-4ea0-3f95-a5a2-0750d523a679 | -10.1969 | -53.8822 | 2024-10-24 02:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 8b10ced7-6cb5-3e20-859a-95c7988090b0 | -14.2703 | -51.1328 | 2024-10-24 02:46:27 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 6012b9d1-ff47-3c23-86ed-f30b139bdd66 | -16.9596 | -57.5245 | 2024-10-24 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.9 |
| 9c43cbf0-28f2-3e19-b121-ff73dcd8ee8f | -17.2383 | -57.2462 | 2024-10-24 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 19c892fe-b475-3077-bdb1-d8a32c211568 | -17.2579 | -57.2439 | 2024-10-24 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| f214b482-e4a8-3c91-a08a-99e66cce1c73 | -17.776 | -40.1748 | 2024-10-24 02:46:44 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| fd38a49a-3b33-3a21-b210-753344c372fb | -17.7834 | -57.5708 | 2024-10-24 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 0fe03743-eae7-3061-ad5c-4f35b5570f4d | -17.7844 | -57.5091 | 2024-10-24 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 18ce5bed-27ab-394c-9bf2-dbcbad373d6b | -18.0837 | -57.3076 | 2024-10-24 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 47573934-92e5-374c-801a-c3ad5861c5f2 | -19.5681 | -56.6114 | 2024-10-24 02:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| ce421a03-fd5d-3a4c-bca5-52bb410b737e | -19.6438 | -56.8521 | 2024-10-24 02:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.3 |
| e9143b32-205d-3fb5-b2db-d4716cfcb5fd | -19.6442 | -56.8311 | 2024-10-24 02:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 3293324f-1ff2-3383-a8c4-76bfcb84a52a | -8.7281 | -35.11836 | 2024-10-24 02:51:00 | NOAA-21 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d7d01563-c1e7-3db7-9ea8-4f99fa2f36de | -6.8571 | -35.22738 | 2024-10-24 02:51:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9264c98d-2240-3342-8d41-e7ed9c76dc80 | -9.78173 | -35.92643 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 46943b3c-a790-3107-92b0-1b4658745e29 | -9.78059 | -35.93232 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 96e374dd-9c3b-3c04-b4ac-f9153ba76f49 | -9.77984 | -35.92783 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 74b30dfc-1bdb-39e5-bc76-2989b5b49c90 | -9.77943 | -35.93831 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2a24812e-9e45-3d0d-8450-220325cfcce9 | -9.77866 | -35.93372 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d4d960d5-c96e-37ae-ad90-f898eb8996a4 | -9.77827 | -35.94428 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| afe8c470-b7b1-31e5-8fc1-e29e7dcf2b6c | -9.77745 | -35.93977 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 896ac598-fe77-3b06-8d1f-79fcf9efcb90 | -9.77407 | -35.93083 | 2024-10-24 02:53:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 98f4c17d-ef4a-3d98-bb85-88cd388129dc | -1.4945 | -54.1962 | 2024-10-24 02:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9e54ac19-33f8-34a9-bf9c-38ca8eb4b69a | -1.4945 | -54.1761 | 2024-10-24 02:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 96310c7e-b8c9-36a6-b0b3-d1ccf6d4ef32 | -1.5878 | -53.3089 | 2024-10-24 02:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 9de6f156-1385-3645-a474-e2358236688e | -1.6062 | -53.3087 | 2024-10-24 02:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 0c4dc2af-a7b6-3159-b21f-6c4d52154695 | -2.9578 | -50.4198 | 2024-10-24 02:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6e08e07c-04d8-3611-9495-70b5bedfe9e5 | -3.0745 | -53.8252 | 2024-10-24 02:55:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 713b035c-9c35-340d-b024-bbce5f91535d | -3.1101 | -54.1661 | 2024-10-24 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ab6a4569-1caf-33a0-8edf-7dafcb89ab7f | -3.1102 | -54.146 | 2024-10-24 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9fafb4b6-a218-382e-b75d-33472c8315ca | -3.1607 | -50.4556 | 2024-10-24 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4eb5c54e-a05a-38fd-ab2f-34b3ac67ca2e | -3.9394 | -46.445 | 2024-10-24 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ec246491-35e5-34cd-ad19-e8059ab5f448 | -3.9396 | -46.4229 | 2024-10-24 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 29bcb67c-6cf7-39e6-b944-91643b8390b4 | -3.9581 | -46.422 | 2024-10-24 02:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |


[Clique aqui para ver as próximas entradas](README15.md)
