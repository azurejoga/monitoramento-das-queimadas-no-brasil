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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d37d8f34-205b-3490-a333-ec098980093c | -3.97001 | -46.73664 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b1936a8-261f-3220-98c3-9cbab67d692d | -1.27382 | -54.54677 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1eaad12-3d8e-325c-8951-ce2a141e856e | -2.60031 | -54.07057 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93047d82-ec7c-3086-8850-af6a81fd92e3 | -3.49706 | -53.80677 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5f6a3da3-74f5-3bd8-8401-aedf56648416 | -4.29427 | -48.19521 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17c8b56e-e792-355a-83b1-1a38ef42550f | -4.39159 | -45.90131 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f97f674-5d9c-3177-bbca-bef337c9ef7a | -3.51184 | -50.30521 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e0d2715-ef0d-317b-90ce-2c25a6fb303d | -4.14354 | -50.41454 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4019a0e-95f0-3759-b4cf-d512dc30f356 | -4.22049 | -50.8961 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1a8c34a-b398-3d6b-9d7d-ea573019d894 | -4.83425 | -45.83169 | 2024-11-27 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b0818d2-48a0-371a-b99c-fd8af70fe8fb | -3.08007 | -53.25604 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 000db752-8a24-3119-ac49-be2b80ef2c19 | -3.17498 | -50.2201 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 756fd3e7-b0fa-38fc-98b3-61d67ba5a1d5 | -1.06847 | -47.22177 | 2024-11-27 04:42:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa7cd4cc-7ecc-3c5e-8b5c-863e20e5ec1c | -2.72951 | -48.64093 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e68df79c-3b05-369e-a0ac-f9c2e4cec82f | -1.64427 | -52.44678 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f5d1dc9-f507-323c-ac51-037e83c9d004 | -4.38564 | -48.08754 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 627dafdf-40ce-338d-b1a8-89df9597dab4 | -2.44171 | -50.41183 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34237787-b27c-3a6f-9db6-f38cf386fa4c | -2.26671 | -50.46518 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf56c278-1ebc-3b4e-a42b-830d397fbced | -5.02824 | -43.60101 | 2024-11-27 04:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f5ecd97-93df-3e47-be20-a3ceb2fde30c | -3.57007 | -53.0238 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1dcca65-ba37-3379-a309-01d9d7a3e502 | -3.12669 | -50.26888 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13740f18-f79d-32a9-95be-600bbb592cf7 | -4.10779 | -48.24921 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db8650a-694d-39a4-86ca-d04c7bb6350a | -3.41273 | -50.20169 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eba1864-6e03-34c9-a758-a7dfa8c34406 | -1.49265 | -48.03332 | 2024-11-27 04:42:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9857f74-fddc-36a8-98db-d98503208ca9 | -3.97187 | -48.1979 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c9138d-90cc-3082-8d57-1a388e07939d | -3.50072 | -50.46191 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70358d8b-c93a-3593-b3cf-3a424d139336 | -4.10928 | -48.85052 | 2024-11-27 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2450a71b-7d13-3c7c-a153-bb6935e59f0c | -4.21387 | -50.89507 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2fcd597a-c417-3add-bc83-9049100270bc | -2.00802 | -48.47934 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81e32f90-3b03-3537-b619-cba79b1c5029 | -4.21664 | -50.89903 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2156dcb3-1209-331b-aa3c-49aa3e879e79 | -3.83304 | -46.08786 | 2024-11-27 04:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3491d194-e487-333d-b81f-02225c50cd8d | -1.696 | -52.53357 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3bbec35-4dba-3efa-a5b6-b68493e38ae5 | -2.59208 | -51.8311 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b4b8f08-16df-38c1-b8d4-390852f52e19 | -3.9703 | -48.06905 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9005d82d-7d26-3bbf-ab5f-7e8ad78e812e | -3.31389 | -53.29042 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9057a50c-cb7e-337f-ba5c-33af41085ada | -2.61088 | -51.75574 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e0d204d-b7e4-33aa-bb9b-bfe41bde6bdb | -2.54839 | -46.40667 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 015b51c6-ef3e-33d0-9ed6-7a42da65c994 | -1.36664 | -52.12784 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e421ad1a-9631-3f56-a77a-ff95b3af8b41 | -2.00668 | -51.16682 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9597ef35-3b46-3162-8271-e11a68853698 | -3.01538 | -48.04071 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5751da60-b029-3b4d-9822-55c7c64a0879 | -2.69232 | -48.59097 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19608574-d929-3ee6-b04e-f51d71facb82 | -4.2447 | -48.67706 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6d8c7efc-83eb-3912-a946-b7b2681f86d1 | -3.14647 | -51.1362 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c58778f5-09e1-324c-9b24-89f10793e99c | -4.29194 | -48.21047 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2715b9d-a7da-35fb-aaf2-f398be17c1c5 | -2.68839 | -48.59405 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e84e710d-5997-34fb-974a-c6f923c7c666 | -5.75559 | -43.07635 | 2024-11-27 04:42:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c66d84f5-0b8e-37ba-9db2-c2c8c2685b88 | -3.80362 | -51.16776 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f00755b0-5635-30f4-bf63-acf3f72dec53 | -1.1993 | -51.74924 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6f8d0b5-0bd0-38ea-a30b-818a371a3e0f | -2.24516 | -53.46422 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26364442-5eb8-3db7-8216-2b56a8b7efb0 | -2.78397 | -53.20831 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f02bd2ef-6847-3094-8ee5-851936efbcc8 | -2.83541 | -54.12711 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 8bcd7cce-da29-375b-86b2-7cd42854b086 | -1.69949 | -52.76147 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0147edce-ac1e-3478-b08d-f01b6091f462 | -1.19524 | -51.77522 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4a31187-eb46-319e-8be5-6c39cfa1041a | -2.94072 | -51.53381 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c9c7328-7d8f-388e-9422-655d43ad2043 | -3.28204 | -51.11475 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dd65a4e-6762-305d-adfa-bedd2d9f76b2 | -2.68368 | -48.59353 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e133d7b-5aea-30ee-9bf2-3cd0b5727d0b | -2.89984 | -51.7703 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 935519e4-273d-30f9-a33d-8bab1667dd7f | -3.89884 | -50.11208 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 588798eb-88d8-3014-8b2d-3532c33fe085 | -3.58856 | -50.37701 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06de5ccc-998a-33d9-a689-ed1e2b2ff4cc | -3.11594 | -53.2617 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db074d66-6869-3e74-a4ce-332532b59281 | -2.43523 | -53.89107 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06e1e217-3e7b-3704-8f04-01ad4e2ca0a7 | -4.2122 | -50.8842 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4a66790-efb4-3553-9a79-570e73ecbcb3 | -4.05364 | -48.32568 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e3e3d6e-6937-3baf-bfdc-7b094e2cf010 | -2.83008 | -54.11219 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e68eb732-7184-3fa6-b879-010d4440a202 | -2.80273 | -53.04432 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87d26c53-3d46-3728-89a0-619d019e702a | -2.53499 | -47.33065 | 2024-11-27 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4661865c-d2fd-3857-a9c3-461c5097736a | -1.64349 | -52.50119 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9a87cdd-7192-3697-b4dd-921a302e9d85 | -3.10889 | -48.5878 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46ea6d1d-2a69-3d4b-bed6-aee83cef17b2 | -2.57715 | -53.97033 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89b24ce1-c825-38ec-80d3-4b55f61455dc | -0.80424 | -53.06158 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49acae16-454f-39c8-880b-78fbe4c6d080 | -4.35317 | -48.56526 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16b5249f-89e9-3364-b27b-e4f73305bcb1 | -3.18213 | -50.21769 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5da5f2ad-219f-36ca-81d0-c5cb10243a8d | -4.15148 | -43.82188 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2a0f415-61de-33ed-826b-8e370f6d9310 | -3.90272 | -50.60609 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1165bb5-8fad-3f4b-80f4-fd69255a2b76 | -2.83385 | -54.1128 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dca38f5c-7f92-34f5-9afb-a7ea6031edc6 | -4.92551 | -47.14124 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce9d31e8-fb7c-3393-ac33-3117ba06cd4a | -2.26063 | -50.4607 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99f791d4-d0df-3696-b373-27e44afc8de5 | -3.9933 | -49.96439 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb6098b5-5ac6-34b0-89de-298c9c684734 | -2.82341 | -46.8273 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d0e3fcb-9500-32c9-90e0-0636b4a82ad8 | -3.67908 | -50.88151 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40c2b32f-1804-3d41-a791-f07523891e39 | -0.58049 | -51.71592 | 2024-11-27 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 966df7df-0536-3b1c-bea1-84fbb43eeb7e | -3.00285 | -45.46333 | 2024-11-27 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ef70ab08-bcb5-3845-b7cf-65127d57bf8f | -2.58745 | -54.05447 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4966af2f-82a0-3e60-bedb-b56f894c258b | -2.18662 | -53.77746 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb1db84b-9262-371d-bc6f-2d11818e046f | -3.59456 | -50.36034 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ca9c1bef-fb03-391e-8de2-aa2be4ef1878 | -3.59078 | -50.3844 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21133d09-4f73-303d-9da6-0a633f1cf8e0 | -2.82209 | -46.83577 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e14683b0-a265-39c8-8f6d-be21db70afc0 | -3.83748 | -52.18138 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1eb9321-993d-33c8-be98-7bcc157f9755 | -1.79614 | -52.29437 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55e89783-64f1-3596-8a6f-c75bcf3fec7f | -4.11694 | -48.48415 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0517376-9a8f-3986-b9d6-0b9e3a90291e | -2.69579 | -51.99741 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16171075-0901-3536-803c-25eddcd18d91 | -1.64463 | -52.44928 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fdae354-8447-325a-8fab-062236017b44 | -1.897 | -50.5916 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0f04f0d-b434-3abe-9aa8-808edfb17633 | -4.19473 | -48.41224 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a94b3098-c304-38a6-8ae9-2867207d3fa6 | -2.8053 | -53.02819 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d56e97b4-d7c9-33c6-b009-b8cbd9571efa | -3.15434 | -49.22545 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e780d2c5-5123-398c-bf6f-c051c6999cbd | -3.21452 | -50.91862 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d950e380-0719-3cbf-928e-1175119cfb60 | -3.28587 | -53.83857 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf18b6e9-6f59-3f72-9ad2-b4c7bf55dee3 | -4.27176 | -42.44293 | 2024-11-27 04:42:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f1b84f1c-2b0b-39b1-b335-a668480bbafa | -3.10387 | -53.26823 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README58.md)
