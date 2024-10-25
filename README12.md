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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45379594-fc6e-3bf3-b818-1ab43df3dc40 | -18.0441 | -57.3126 | 2024-10-25 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| a5bdfc0c-9ff3-340e-b4c9-60929d079d5e | -18.0639 | -57.3101 | 2024-10-25 01:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 122bf5e2-8545-3dc5-8845-c0e43624da1b | -18.3199 | -56.2404 | 2024-10-25 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 403d1bc5-6c3c-345c-923c-fd58bf41fba7 | -18.3203 | -56.2195 | 2024-10-25 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 687249b9-e026-30ce-8061-536f0b8a533f | -18.3398 | -56.2377 | 2024-10-25 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 46c3d8b9-4504-3bb3-a173-844f56c0492d | -18.3401 | -56.2168 | 2024-10-25 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 9e14f451-16a9-31a9-b2c2-77dd919c7aff | -1.0445 | -47.6237 | 2024-10-25 01:25:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 939d2b11-1d84-3423-a446-fececd75da60 | -1.0446 | -47.602 | 2024-10-25 01:25:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 249904dc-df98-36a2-ad6f-349b11b89d1a | -1.1834 | -53.6771 | 2024-10-25 01:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 312a4aac-9b4e-3fc8-8f89-3869d6feb4c9 | -1.1834 | -53.6569 | 2024-10-25 01:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0fe1dc2c-5bda-343f-81a9-c0624e27d259 | -1.1924 | -47.6219 | 2024-10-25 01:25:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b0388fa8-a2e4-3889-a905-22f20beed376 | -1.1925 | -47.6002 | 2024-10-25 01:25:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| ff3f6639-e2dd-33c4-8f2b-36ae782c0aa8 | -1.1925 | -47.5784 | 2024-10-25 01:25:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0d68b93f-4cd2-3a6e-86cb-7a5fccb2ce04 | -1.211 | -47.5999 | 2024-10-25 01:25:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 260f3d49-d10e-389d-88c3-389acce95e84 | -2.0592 | -56.1141 | 2024-10-25 01:25:17 | GOES-16 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 8cc87066-ada0-31f5-a312-bf4bdc5495ea | -2.6192 | -52.4564 | 2024-10-25 01:25:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| dfeec206-5e27-39b2-b203-8d20380d9891 | -2.6193 | -52.4359 | 2024-10-25 01:25:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 134b83df-6841-32bb-9577-96a12678bfb7 | -2.6297 | -49.247 | 2024-10-25 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 91674bbd-083e-3b2b-8b09-ba6e59bd1afb | -2.6482 | -49.2465 | 2024-10-25 01:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e6d4ae6b-0429-3cd3-9320-f6720c6a8779 | -2.796 | -49.2424 | 2024-10-25 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9297c230-1ff0-3bb1-9804-9d74d5c9017a | -2.8144 | -49.2631 | 2024-10-25 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e589b899-6457-31d1-8715-9dc6f176871d | -2.8145 | -49.2418 | 2024-10-25 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d3b605ef-7a6b-3cf9-8bde-9a5cd1627dde | -2.9578 | -50.4198 | 2024-10-25 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7958c8df-33f3-3174-8618-6c13e248ac84 | -3.1116 | -53.7234 | 2024-10-25 01:25:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6cb086f5-8626-3495-95d4-89c8ca579aae | -3.1949 | -46.807 | 2024-10-25 01:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 6d72f1e7-7350-3698-a1dc-c4bbc7b18816 | -3.2135 | -46.8063 | 2024-10-25 01:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 1c116e3f-e62b-3b50-b19e-6d0d74d8d36f | -3.2136 | -46.7843 | 2024-10-25 01:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 4aab885e-af60-3c35-a3e8-ec7318faf007 | -3.3124 | -49.5235 | 2024-10-25 01:25:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 932b69ae-1c91-3d75-9198-0fefaba7dd31 | -3.4951 | -54.4366 | 2024-10-25 01:25:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 2fff68bd-2b45-3417-98b2-73ec47ee6ddf | -3.9396 | -46.4229 | 2024-10-25 01:25:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 71378327-ea4a-3601-ab54-38c8c50e001c | -3.9581 | -46.422 | 2024-10-25 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b4aa8543-f797-3c60-b357-52a05749a31f | -4.2429 | -48.5474 | 2024-10-25 01:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 215e40e2-71bd-3a49-8abb-32691aa03566 | -4.5045 | -48.2117 | 2024-10-25 01:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2e420c2e-9ea1-3758-946f-5fda5021139c | -4.58 | -48.0132 | 2024-10-25 01:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5a1b40aa-d37f-329a-b68e-5a69889af5ad | -4.5986 | -48.0123 | 2024-10-25 01:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 61d3854f-e0e1-33a7-bedd-5e27ca9cf19b | -5.9788 | -45.3621 | 2024-10-25 01:25:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| a7ecbca4-6155-3e31-904e-176c2a67f6b6 | -6.5219 | -60.0457 | 2024-10-25 01:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 3b7b1ced-1b10-3e33-836c-04966c5b4564 | -6.522 | -60.0266 | 2024-10-25 01:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e1bc9407-2561-3a87-8110-35ad9d55c3fa | -6.6472 | -47.8642 | 2024-10-25 01:25:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| c6efd8c0-7f83-345e-ab48-3ac7abdba408 | -8.9064 | -48.544 | 2024-10-25 01:25:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 72.2 |
| db71a901-5ec8-3d1e-a690-36412486435d | -10.6519 | -47.9207 | 2024-10-25 01:26:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b7328a3d-1f84-3d4a-82a2-3e52b505340a | -11.902 | -56.4135 | 2024-10-25 01:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| da6b1e8b-c045-3d8c-a034-b212535fc390 | -11.9022 | -56.3934 | 2024-10-25 01:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2b68de53-e784-36ce-809d-51be234cdf6f | -11.9824 | -63.9022 | 2024-10-25 01:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1d58dfa7-3397-36ef-b01a-62d8bb8357ca | -12.0011 | -63.9203 | 2024-10-25 01:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e21c6cc2-a03a-3bfb-a063-7be1ddf01c10 | -12.0012 | -63.9013 | 2024-10-25 01:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3516d967-dbb3-330f-ad42-199dd8810fef | -12.0444 | -63.1547 | 2024-10-25 01:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| bb05a939-8a2c-38ec-b4a0-c4573df7d5ed | -12.0445 | -63.1356 | 2024-10-25 01:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 607ad994-2843-3b66-b2fd-e43b36f865dd | -12.0632 | -63.1537 | 2024-10-25 01:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 4f408681-c43e-3dc8-be9d-286acf98e562 | -12.0634 | -63.1346 | 2024-10-25 01:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 98.6 |
| a94dc986-f27d-3ff6-bc9f-6557f45b2c12 | -12.3782 | -63.8821 | 2024-10-25 01:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 31297fd6-9d26-350e-ab00-dd6ccfe4c8d3 | -12.3783 | -63.863 | 2024-10-25 01:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d00215d0-c91a-3b54-a00d-c01dd47f63bf | -12.3971 | -63.8811 | 2024-10-25 01:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 01f2e31b-a72e-30a7-b03f-e9ac5cd22083 | -12.4589 | -63.1895 | 2024-10-25 01:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ba9bb193-0687-3913-8542-d20a7c073de4 | -12.4591 | -63.1704 | 2024-10-25 01:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 60fc82d9-e321-3a35-a8f1-eede43bc6f56 | -12.478 | -63.1693 | 2024-10-25 01:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7621dcb3-a423-3104-9224-1f7f0c18b9b1 | -12.5167 | -63.0521 | 2024-10-25 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d8ba4c97-6fa6-3afa-a9a7-69ae22e10921 | -12.5356 | -63.051 | 2024-10-25 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2a7a0344-3e7d-3488-928e-b98156629d3a | -13.4959 | -61.6203 | 2024-10-25 01:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0151ff8a-b966-38ed-9ee4-b61e6dd63ed7 | -16.94 | -57.5268 | 2024-10-25 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 419809b7-0c51-313b-aa64-f96615c18c0d | -16.9596 | -57.5245 | 2024-10-25 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.6 |
| 5e1dfe53-7e34-354f-8c2a-d63ac05e03b5 | -16.9789 | -57.5428 | 2024-10-25 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| c1856873-c886-3c27-bd15-849889c75194 | -16.9792 | -57.5223 | 2024-10-25 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.3 |
| d1b07006-9b52-3c16-bef4-15cea35832d3 | -17.2344 | -57.4926 | 2024-10-25 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 02be6e10-4fec-3fbe-a36e-6b2eecb081da | -17.7453 | -57.4933 | 2024-10-25 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 24fbc6f1-670c-3896-b9aa-dea4fdb288d5 | -17.7634 | -57.5937 | 2024-10-25 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 256c66bd-02f7-3377-a504-52a99f55d249 | -17.7644 | -57.532 | 2024-10-25 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 84a08d5c-199f-3c71-bca4-aac09836d4ea | -17.765 | -57.4909 | 2024-10-25 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 52ff0df1-1054-3254-8010-5e3ca1b48f54 | -17.7671 | -57.3673 | 2024-10-25 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| f5bfc412-466d-38fd-b51b-c6d5b2790c23 | -17.8042 | -57.5067 | 2024-10-25 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| e384f672-4723-3064-afbb-2e1a45a8b259 | -17.8239 | -57.5043 | 2024-10-25 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 9595f10d-daeb-30f0-870c-3aae755e81a3 | -17.9268 | -57.2447 | 2024-10-25 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| b1c8afe7-835b-3622-b193-070114469c03 | -17.9272 | -57.224 | 2024-10-25 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 6358b91f-adf1-3cc5-80c0-25403a2924a6 | -17.9275 | -57.2034 | 2024-10-25 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 0053bcd9-3c3c-395d-8403-4f90d94410f2 | -17.9469 | -57.2216 | 2024-10-25 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| db84bcf1-f994-32da-badc-764781fa2c92 | -17.9473 | -57.2009 | 2024-10-25 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| f6ac9438-2bfe-3f4f-83d4-5463d32833ac | -18.0254 | -57.253 | 2024-10-25 01:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 018fac60-0ecc-38b8-8b34-aa10bbf6c514 | -18.065 | -57.2481 | 2024-10-25 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 122a2513-6ca8-3164-8643-9ba661347402 | -18.0844 | -57.2663 | 2024-10-25 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 015abd93-1ecd-3e87-82ce-8a7f9d3c79da | -18.0847 | -57.2456 | 2024-10-25 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 9024a346-33c7-30ff-b4aa-ccdb27552018 | -18.1223 | -57.3647 | 2024-10-25 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 181e6f6d-b524-36f9-aa55-aff15a2cba93 | -18.3199 | -56.2404 | 2024-10-25 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 4a07d0d2-3563-352a-858f-f82fdbed52b6 | -18.3203 | -56.2195 | 2024-10-25 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 6b695e4c-0063-3387-8942-cafb3ebc7885 | -18.3398 | -56.2377 | 2024-10-25 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 8ced1480-a42d-3a8b-80a4-1eb31cb88293 | -18.3401 | -56.2168 | 2024-10-25 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 9818871b-3204-38e2-b761-0823e200444b | -18.3405 | -56.1959 | 2024-10-25 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| c752b01e-3b83-34b6-a048-4be874b8418a | -19.7065 | -56.7176 | 2024-10-25 01:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 66ac0510-7ec9-39b4-a0ec-90a2665ace9c | -19.7266 | -56.7147 | 2024-10-25 01:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| a78b1bf0-c326-3083-8556-e07ef6a6fae7 | -1.0445 | -47.6237 | 2024-10-25 01:35:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| db61d832-635b-38f9-9a90-70b7308713a8 | -1.0446 | -47.602 | 2024-10-25 01:35:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| da09fe56-5315-3ed8-b381-31bd2401165f | -1.1834 | -53.6771 | 2024-10-25 01:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 59fc89e2-3cd4-304a-967c-22d1a3bb2e1c | -1.1834 | -53.6569 | 2024-10-25 01:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b6f57b70-3744-3373-8bff-654c79469b7d | -1.1925 | -47.6002 | 2024-10-25 01:35:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 2c6aa51b-9cc8-3723-8fc8-37c174a6b947 | -1.211 | -47.5999 | 2024-10-25 01:35:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 4cc758bc-6735-367f-b933-d2c74e1b3c6e | -2.6297 | -49.247 | 2024-10-25 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5803cbe6-9b67-35da-8645-869cb832dbf2 | -2.6482 | -49.2465 | 2024-10-25 01:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6cd74905-2330-3346-b521-84f50ec0c1e5 | -2.796 | -49.2424 | 2024-10-25 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c97caa25-560c-399a-85ab-5cec58c94dc5 | -2.8144 | -49.2631 | 2024-10-25 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 163a99f5-5df2-37b4-b3e3-caed22107b73 | -2.8145 | -49.2418 | 2024-10-25 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 59ca5b8c-0c32-35fb-b58a-c41e9af45ec4 | -2.9578 | -50.4198 | 2024-10-25 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |


[Clique aqui para ver as próximas entradas](README13.md)
