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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd99ea3f-d279-3e8a-a0e7-0912786e43fa | -2.4608 | -53.9677 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88bc81d0-1f57-35a8-a8a5-a9905ddf449d | -2.63074 | -54.22715 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3c80366-e866-3b05-8eb3-a2b5984d41c6 | -2.80084 | -54.12867 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eb0d8a8-0be7-3774-aef5-69e80f5b74d6 | -3.32189 | -54.17712 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6b936b0-3276-3830-9049-c4837fb1b8a2 | -4.03601 | -46.93591 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 373f2b1a-f618-3b89-bd8c-bc3ca90e0602 | -3.99682 | -44.75533 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b0d15ad2-9ac2-328f-a951-6e0191587c34 | -3.95824 | -50.19079 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a2523a8-931a-3b16-ab6e-7bc3d047680f | -2.60367 | -54.09137 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52aa2300-2292-307a-bd55-3bc217720d89 | -1.49709 | -54.95108 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21df5d0b-55af-3b81-9894-79aa95adf34f | -3.61564 | -51.36842 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ace959d-45f6-387e-8686-10834e6e2edd | -3.29552 | -53.83439 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e574d5-a791-350d-9a5d-1e604478031b | -2.43724 | -53.62926 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7ceb108-8750-34e1-bdba-a422f338782e | -2.98639 | -53.34966 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cf40e9f-0540-36cf-af77-5adecf7e04fd | -3.1355 | -54.18529 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7b2e6db-5dbf-3d66-a7e7-a04069b9ebd2 | -1.59987 | -52.2917 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2289c1a-2869-3786-b4c1-f97b31de8329 | -3.25714 | -53.6356 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65d60fce-1b00-3982-9924-bf739ab86fe6 | -3.5865 | -51.20844 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f63fde82-a2dc-32b9-86e3-6e6447d7aeea | -1.43431 | -55.15413 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d062cc2e-1958-399d-936e-ae963382652f | -3.10986 | -53.3248 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6415e97d-4c85-3570-93a3-f11f8541ca10 | -2.98073 | -45.57405 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e446ad90-4ad8-356c-95b5-7147b16675b8 | -2.19028 | -53.77404 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46de98ba-7969-3992-9035-fb4175e3f229 | -2.10552 | -55.18571 | 2024-12-01 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8f68532-572e-3254-8029-b21569c22561 | -2.59197 | -53.9838 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ade050b-1ce8-32dc-a833-195adc800fd0 | -2.80236 | -54.05037 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6c2ef01-fef1-308f-8061-aac21e924463 | -3.24473 | -53.62113 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5b7772e-c7ee-3410-a21c-3602bf88ba8d | -3.66012 | -52.28996 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c37dc66a-023f-347d-83bb-4881ba4fc50d | -2.97456 | -53.89973 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b514089-a0d3-30d9-a79d-b5c6ba25e976 | -2.23179 | -53.62374 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 086f1003-d743-3663-b440-cd95e2f1883a | -2.26098 | -53.46064 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb527c20-3d3c-334e-8251-b52a24ccc450 | -3.29142 | -53.67379 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78ebbca7-3cd0-3434-9813-ea1352573bdf | -1.26092 | -53.37402 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9d00d4f-c069-3a2c-84c8-13df941e5d10 | -2.76502 | -51.69102 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab07eb0a-ff50-38b5-8543-8e9142abda54 | -2.87851 | -53.32239 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38973c3a-4656-318f-9f6e-183d906292d7 | -1.57726 | -53.83417 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9c144c5-0017-35c5-8607-a8aaca624c4d | -1.4261 | -54.31451 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1809bd3-4b65-3978-baef-02b8366dddd6 | -1.61777 | -52.69296 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45a10c47-5681-3cc2-8e4a-4a5b4cd07657 | -3.29251 | -53.2814 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7866931-0b74-370a-99e6-89d59c59d9e0 | -2.59325 | -54.26405 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01f56b9-ecfe-39fa-89ec-998d8d5a1b5e | -2.77046 | -55.31707 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ead4f34b-f361-3a46-9991-4e5b1b2414e6 | -3.12483 | -53.27569 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17ef98b6-8ad1-375f-9a31-3ccaedf95008 | -3.25869 | -50.0526 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| daa1311e-8ca4-34e3-97fc-c17fa1a3cc00 | -3.49583 | -53.82591 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e2ad270-c85c-3073-997f-b06147dc6966 | -3.05841 | -53.17162 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d6b8789-bb57-3af1-b804-88a8222169bc | -1.70036 | -52.64207 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b1b2957-d712-3bf4-acb9-ae69df36ffaf | -3.01439 | -51.7952 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28d6cc23-ae95-33a8-9834-87d70d8aa81a | -1.35611 | -55.15624 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8f5d4fe-a151-3542-ac23-ee759581f191 | -2.85204 | -54.10773 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ca81e0e-8b38-3e68-99b7-2d494e1eb322 | -3.24759 | -53.86354 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddffdf68-7ef1-311a-9fd2-439c62af1c5e | -2.98174 | -51.46115 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c72e8aa7-ad6d-3777-a8ab-b4cfb3485c08 | -2.68433 | -51.72445 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2856d017-67a6-3d43-b47e-2dbf0903bff3 | -3.30882 | -53.36948 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b16abb2-0698-38ab-adf4-f3214db4d10b | -3.45429 | -54.56448 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b5b7300-affc-307a-8177-0f6699ac0e2f | -2.89354 | -55.22353 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dd778a6-6585-3dff-8169-361285409109 | -3.46839 | -50.2756 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6a3a6f28-daf1-3d22-a0c8-bf9eeba17769 | -1.6832 | -53.94402 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f2dcf9b-c30f-38d3-96c9-97276fd5ad0c | -3.32329 | -50.19605 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59285974-9d7e-390b-a7f0-2cb717ee2f66 | -2.47862 | -54.01373 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21dca8d6-f3fe-3649-b95c-6393fd2aa8e9 | -3.32462 | -50.18747 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 26cb36c9-d298-3175-9066-ea44529715ba | -3.05547 | -51.06261 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ffe8ea97-0350-3196-aaed-38d587b405f3 | -2.81848 | -51.79242 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee940f8-0f77-3388-b8f8-353e887e6161 | -4.54968 | -43.31035 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 089b583f-adff-3f43-99c2-affd5b35014e | -1.44333 | -55.22701 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0e488d-681f-31c4-9932-af31f29ac03c | -3.50292 | -53.82697 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5454735e-6f22-3d15-9a5f-dadbb9cfcd87 | -1.44206 | -55.12655 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50e39c06-624d-3746-887b-bb7f520fe146 | -3.06851 | -53.80493 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6406eb4f-1819-391d-8104-368b32d32ded | -3.78543 | -51.81418 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c341f39b-6328-30d8-9634-a7492a0c2783 | -2.85499 | -54.08853 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca369ec8-671d-3135-8f05-d8e3681d581b | -5.31251 | -50.57268 | 2024-12-01 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9790cfa-d8ba-38e9-9651-6f73f523a0e5 | -2.75071 | -51.6617 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcba2d29-df74-3d77-b517-7f3013a77c90 | -2.82663 | -54.07769 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 688ed686-adcd-3e57-9fd9-fe2bcd0730f4 | -3.03748 | -54.07274 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93493745-bf01-3001-a988-7e25c99860a2 | -2.96797 | -53.8913 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75088361-63b1-3ee8-a7c2-ffd669becd57 | -3.6952 | -51.34266 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| becc5c5e-cb33-34d3-90fd-bba5ecc238b7 | -3.97309 | -54.08466 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e9a1d7d-46e3-32ff-986b-5b429218a783 | -3.2926 | -53.82988 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1cb3756-0d64-3ff0-a10a-c21a373ad776 | -2.97514 | -53.89589 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afca4047-c516-328a-97ee-f6363d8e74e0 | -1.14671 | -53.75244 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69511937-34b6-3db3-89b5-f3821b61a5ef | -3.23298 | -53.63271 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede66c13-c5b5-37c6-b806-4569fc3e1523 | -2.14118 | -54.87133 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 874ab710-2a82-3ca6-be80-fa17faad933d | -2.12211 | -50.63424 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4ebed8c-8102-35ed-8c85-e1236acba939 | -2.72726 | -54.16786 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16f5bbf1-153d-3b0e-8ed4-eb6612e8394a | -2.40871 | -53.85814 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d8fd8c7-f56f-36f0-98b8-c1f49a54cc42 | -2.98873 | -53.35851 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 571fe857-17c5-34ab-bf18-ee569fe8218c | -4.17348 | -48.6322 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a81d9f0e-7417-3319-9502-25ed4c9e9db0 | -3.38092 | -53.51032 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9f3f5b3-3b11-3a0a-9abf-475c96e390c1 | -2.63766 | -54.22817 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37831ccf-b359-36ca-8afb-bc46135b4f23 | -3.11033 | -53.27343 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd1265d4-ab34-3991-bd80-76bc7f17d507 | -1.41967 | -54.51156 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d090e7-1c32-369e-83de-18011aadbfc9 | -3.25776 | -53.63154 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f869a283-0185-36ca-a956-9e302ef8f71d | -2.90185 | -51.58148 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 68aa0bfd-d014-39ae-8e15-79d7bdb0948e | -1.60627 | -53.83076 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b15bd0c4-1d03-3103-affd-5bee72b01763 | -6.86748 | -47.24408 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b4f088b-dd49-3047-be42-d6e02e1eec5e | -4.26468 | -48.35646 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf9511df-7c52-348d-9560-e9e02f290dbc | -4.11444 | -54.41489 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d668004-0e3e-3649-af3d-51647577f95f | -3.43314 | -54.11423 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d11a4ca-cc88-3c80-898f-4953ec5273ef | -2.79389 | -54.12759 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7efa2ab4-8c6a-3713-8d0d-3d80ecbf9870 | -3.36997 | -51.12683 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b323d850-0255-30ad-b532-a67a2f112192 | -3.8311 | -50.13753 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be48e8c6-142b-351c-9a73-85da4acef774 | -3.66522 | -50.95054 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df002bc4-f99c-3230-8f6b-3c8c4133af7d | -1.49051 | -52.6449 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README97.md)
