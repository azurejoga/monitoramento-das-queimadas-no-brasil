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

## Dados Diários - Página 215

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2396012b-fdad-3fb9-85aa-25810065ba1a | -16.95497 | -57.46926 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 1b791046-8628-3e51-b3a7-f563bc3ce07b | -16.71119 | -57.46228 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ee186860-f06c-3558-bd0e-05c297f8d47a | -16.70602 | -57.45977 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b0316e6e-8843-37db-ab9c-d75e0c34e197 | -16.70438 | -57.46153 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1989627f-50a2-36c4-af26-e292c055d0d4 | -16.70032 | -57.44615 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 159660cf-03dd-39d3-9c4e-1f606d990d16 | -16.69976 | -57.45257 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a4d5b58b-6cb1-3b33-b94f-13ad4ab1cbe6 | -16.69921 | -57.45897 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8c3c2d9d-bce8-30f7-b9c3-e03512cd9a7c | -16.69876 | -57.44797 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b2aae018-2db9-3d11-85dc-7cbcfed2ed14 | -16.69816 | -57.45437 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 99a2027f-35b1-337f-b10a-b290eedefc4a | -16.69756 | -57.46076 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ea0201df-fbf3-3e0e-9464-2538cbea5df6 | -16.69194 | -57.4472 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 78fa52f4-85e1-332c-b2f8-9ec7f853b191 | -16.69134 | -57.45362 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 76f10102-af92-3cb2-bce3-81ea58b56fe9 | -16.65785 | -57.44329 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 515c130e-5800-3b77-8490-dc1e49b9021a | -16.65726 | -57.44968 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b781c642-5edd-3a1e-b0cd-4113e7bc2bf0 | -16.95115 | -57.44764 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| f4125225-91d5-3319-bf40-3e3a55254316 | -16.95058 | -57.4541 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 80455800-0510-3531-9770-9ad9f3f28744 | -16.95 | -57.46056 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| a93a0389-8331-3f57-9813-3ca7e6d3ab58 | -16.94998 | -57.44917 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 1c1d8e51-8569-3aac-9f46-be4f9ecf9ad8 | -16.94936 | -57.45564 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| ca8318f6-6f64-3e25-a841-7ddff966bd7c | -16.94875 | -57.46209 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 811d5951-d2f0-3f88-bba3-3e461a329eb3 | -16.94374 | -57.45335 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 457acee0-d94c-3242-a0aa-1fd1982e527d | -16.94317 | -57.45979 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 10377d1a-c03d-3711-8d80-56e30778eb99 | -16.94261 | -57.46622 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b96da22a-bcd1-317c-aab9-4992ff2c8220 | -16.94253 | -57.45491 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 13ee7076-44b3-35c2-a0fc-75eee09a61d7 | -16.94192 | -57.46132 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 9f96bb3d-dbf4-3164-9809-4a6b2ef6c0dc | -16.94131 | -57.46776 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 97930cee-4865-3609-92cb-645dc7f7ab9c | -16.93634 | -57.45899 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| a031e34d-b05c-32ec-acf9-f27dbc8f4d50 | -16.93578 | -57.46543 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 636504e7-20eb-30d9-8590-ceb2a2327303 | -16.93569 | -57.45415 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 3023309d-7665-3f03-8329-403500015514 | -16.93509 | -57.46056 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 42845e76-42e7-330c-a11a-b513ebc07b51 | -16.93448 | -57.467 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| d538881c-edae-3c70-9309-9c5cafecd09e | -16.9295 | -57.45825 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 22c42da7-ee27-3af5-81dc-93ec24d05f58 | -16.92894 | -57.46467 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 36104453-9921-3850-8835-7fa26c17f605 | -16.92826 | -57.45985 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| eec5f8fe-04eb-34a8-b852-0ae68350d218 | -16.92765 | -57.46628 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 68ef4cdc-67f3-37ce-9eb1-966de598d24b | -16.92211 | -57.46395 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1a8e2657-12c1-336a-85cd-3d2953728040 | -16.95375 | -57.48205 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 81280b79-e955-330f-a209-6fe10ab6a32e | -16.94887 | -57.4734 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| cb7508f8-16e0-3c5c-aeab-24f731cc6e2d | -16.9483 | -57.47983 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 84e97f79-e8dd-3274-91b1-64aa9e49bcd2 | -16.94716 | -57.49267 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 9c0d8cd4-e6d0-3e8a-aef5-c6a6be4e6d5f | -16.94693 | -57.48133 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 21e9f3fe-99e6-366e-ab0d-fee77b4a30e4 | -16.9451 | -57.50056 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| e885650a-bf97-384c-8489-45aad2111a20 | -16.94204 | -57.47264 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 71ae0209-e15a-3866-b48d-b0840454d44e | -16.94091 | -57.48547 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 34f24a17-dbe5-3c66-b987-9605a89f5f1a | -16.94071 | -57.47418 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 709ec61e-a06d-3255-aca5-f64e8a801e84 | -16.9395 | -57.48698 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 93024047-9d90-3606-b19a-d262814eb8af | -16.93889 | -57.4934 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 0074b3ee-d4d8-332e-b393-9fd997ec8c83 | -16.93521 | -57.47186 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f27cad71-9859-3798-8ddc-397d3dd15707 | -16.93465 | -57.47829 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 01ec6b20-efce-3c04-bb86-5977aa5c6503 | -16.93409 | -57.48469 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9b1e143e-2514-313a-a106-aa0c1d0ca584 | -16.93388 | -57.47344 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| f7a6ce0a-1b83-36d6-86d9-1ea1b30d875c | -16.93352 | -57.4911 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| bb5aa566-366a-309b-9db4-bf10c42348d4 | -16.93268 | -57.48623 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 59d0d65b-43dd-3e70-8e7a-d832973b8bd9 | -16.93147 | -57.49905 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| b89851cf-67ff-3511-a978-711ce1649e1f | -16.92838 | -57.4711 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 02fb679e-ac6a-34f5-98aa-1f7da20f47bf | -16.92705 | -57.4727 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 1991cbec-2142-34a9-bbd9-c51e04f305bf | -18.6094 | -57.23279 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 47f05059-f90a-3107-bf6b-38986ba8f0c0 | -16.91988 | -57.48958 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 7bc95855-3252-37fb-b6d8-687407762382 | -17.11235 | -57.43701 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 513e0caa-33ad-3684-9a18-f54b702df918 | -17.11176 | -57.44352 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d71fecab-e396-3520-a08e-755091e432a2 | -17.11117 | -57.44999 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 55db4368-9c58-3a6a-b317-876cf4f5ffb9 | -17.1055 | -57.43625 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3e0f5a82-a011-3e8c-b6db-670ec4530241 | -17.10491 | -57.44271 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6710d2ca-9473-3b11-b1f3-b82ded9040a7 | -17.10374 | -57.45571 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| ebc9109f-ce17-3d29-80c6-be6a20b5c339 | -18.60881 | -57.23979 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0ef57bf0-a57b-33c9-ba37-c6d8530b1af0 | -18.60698 | -57.23681 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| b0ccff1e-8501-3d7c-b389-c5c1ea7fa7f3 | -17.09864 | -57.43553 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ff066c18-15f8-303a-bf08-f64c5868d3ad | -17.09806 | -57.44198 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3125a16d-e7f2-371b-8ce2-eff50b39bd0d | -17.09748 | -57.44846 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 0727184f-4704-3540-83fd-a7b7a20244e6 | -17.09121 | -57.44125 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 787e7877-6344-3ff4-bf8b-3b32616d3027 | -17.09063 | -57.4477 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 0e20792a-dd05-34a6-886e-444fed110373 | -17.13415 | -57.43436 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 14882090-8b4f-37f2-9eea-0099cab7e8c9 | -17.13359 | -57.44086 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1d19ad3a-c1f8-3d6f-8dfa-0690944f56db | -17.13351 | -57.43282 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8f0028ec-d373-3475-97ba-1933d482f6fd | -17.13303 | -57.44738 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 145baaeb-eed5-37e6-aff1-138434a1e5a7 | -17.13291 | -57.4393 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 931d0636-43d6-3dde-b6da-eeef5e9cf7c7 | -17.13248 | -57.45385 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 2e110e68-47d8-3739-b85b-01d18ccc1395 | -17.13231 | -57.4458 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c4661a2b-4005-32db-8aad-6ae831c20c2d | -17.13171 | -57.45227 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 1ded4da1-3551-38ab-bd56-720af42ccc52 | -17.12729 | -57.43359 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3f6b7e8c-e49a-3036-a396-e1ffac5e6981 | -17.12674 | -57.44009 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 70d0781e-4433-349c-aa0b-9034f419732a | -17.12665 | -57.43208 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8b3d32c4-cd72-3a95-a36b-1d4475208b73 | -17.12618 | -57.44661 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 5bcc16d5-f7b3-3475-986e-ddf2493af170 | -17.12606 | -57.43855 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| ca97624a-40e7-3d30-83ed-ad02d5661304 | -17.12563 | -57.45307 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ab4fca4a-a5ef-36c2-9dd2-c3fe79a83447 | -17.12546 | -57.44506 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 3d273b1d-be5e-31af-ab1c-222e86cdb128 | -17.12486 | -57.45152 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 3ff751b6-3294-3a42-8ba3-5bc580e0dfcb | -17.12044 | -57.43279 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| df72aee9-8eaa-328d-810a-430b0669254c | -17.11988 | -57.43929 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9dfa8de7-56c6-3f52-832c-9b5ffe668668 | -17.11979 | -57.43131 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f2625b7b-24d8-3be2-982f-d80eb564f391 | -17.11933 | -57.44582 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 94624acb-f33e-3781-8bbd-fba141611658 | -17.11921 | -57.43778 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b30f185b-ff40-34f1-964b-39833d60122e | -17.11878 | -57.45229 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 44f030dd-94a0-3866-bd9b-592e63d84cc8 | -17.11861 | -57.44428 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 92ed782e-d0a2-3108-8ca8-c0d889eb5b1b | -17.11802 | -57.45077 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 7596ecbb-c0e3-31c1-a655-d483b6d5f5e1 | -17.11743 | -57.45724 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 62ba03d5-b824-37a7-8c62-3dd7ef9c8add | -16.82615 | -57.42802 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2a0279eb-e5e2-3fcd-ad2b-92bca2c3ba69 | -16.82554 | -57.43448 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9029c8cc-073b-3a23-9d96-8a778891fd83 | -16.79821 | -57.43142 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 8d773058-94b3-3967-a134-70c60422fd32 | -16.79761 | -57.4379 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |


[Clique aqui para ver as próximas entradas](README216.md)
