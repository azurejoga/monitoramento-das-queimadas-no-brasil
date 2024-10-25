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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cfdfb54-f49e-3349-ad77-7aa3f3236d53 | -5.50473 | -44.82874 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bc447a8-9632-3a56-a6d0-366ee33e6b14 | -5.32679 | -44.8431 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cd305ea-3586-3467-a248-c00733636072 | -5.27226 | -44.78905 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0a18e9b-bbca-377e-854f-497282d34151 | -6.55853 | -43.91505 | 2024-10-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64ba68d7-47b2-3c28-b89d-6af96b375342 | -6.55521 | -43.91451 | 2024-10-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18577422-7df1-3cc8-a9df-e148d61c1091 | -6.48274 | -43.87809 | 2024-10-25 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57735d74-ef9d-34e4-b75f-ee4fbc262386 | -6.05387 | -43.89928 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6a4f136-de4a-3224-82b7-f70baf1e527c | -6.05332 | -43.90279 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b075dc9-ce21-33b2-8f5d-250b8d6f1244 | -6.05166 | -43.89175 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 872b797d-45a3-3af0-845d-adb15937902e | -6.05111 | -43.89525 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0f932c5-1681-34bb-9f4a-a2e6bf57ab41 | -6.05055 | -43.89876 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dba39855-b364-33d9-b4ef-c75c9626c90d | -6.04999 | -43.90227 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f9eab85-a7a2-3dc7-b1d6-355c68bda6c1 | -6.04722 | -43.89824 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63cc819c-50e1-37aa-bb3b-0d260b897f2d | -6.04667 | -43.90174 | 2024-10-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e515e0f-c394-3c61-a685-91281a9f603a | -5.91318 | -43.94846 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 063e01d8-29af-362f-839a-7ddc0bc27d28 | -5.83096 | -43.65266 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c903c0e-454c-3235-b52b-4be85c796a6b | -5.82764 | -43.65214 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e79821dd-4b6e-37df-8b20-4bfcda6075d6 | -5.72235 | -43.77842 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb4e95ce-5ea9-35eb-9c69-9ac9f2ba1157 | -5.71954 | -43.83894 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5f075c4-731d-3f5e-922a-2356c3fe3bee | -5.71903 | -43.77789 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c3f25c4-5eb6-32fe-8223-e84354664277 | -5.71898 | -43.84245 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d3328e5-2182-3238-94a8-483ee63f0b20 | -5.7223 | -43.84297 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 385d3e76-07dd-3e05-bd4f-f2488e669c4d | -5.71959 | -43.77438 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9661715-bc8c-3642-8d0f-426eea414a84 | -6.40072 | -44.00866 | 2024-10-25 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 271b9037-dbca-3ed1-926d-75690123a924 | -5.72009 | -43.83543 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46e668d8-9a3b-3213-b5c7-6888ccc7359b | -5.71621 | -43.83841 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b0731ba-fb3f-38eb-bff8-7545905ff910 | -5.48893 | -43.66234 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d794b36a-9415-35a9-bf6d-bdebab8383a1 | -5.72286 | -43.83946 | 2024-10-25 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab6e0bf2-ba3f-3916-b69d-da6b65fd3e58 | -5.46243 | -43.74402 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 626caab4-6857-3241-99d3-01d0c28856c0 | -5.45404 | -43.582 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c6e3d42-5c4d-3880-8351-b3d2ce99a3e3 | -5.45072 | -43.58149 | 2024-10-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 105744de-febd-301e-9700-96bf36094334 | -5.11316 | -43.84311 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edcff36b-7761-34c4-a414-1c69f7a80ea0 | -6.4569 | -44.67798 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ebb21bca-7729-3762-87be-3acc797205ce | -6.45631 | -44.68163 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bd9a1d38-8bfd-3662-9d47-8299464d9982 | -6.45425 | -44.42346 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84878ebb-3452-39b9-b9a0-bab95494fb67 | -6.25402 | -44.13968 | 2024-10-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a05ba0c-8aca-32a1-b74b-0783c4ab9d3c | -6.21114 | -44.56111 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12d5e158-053d-3ca0-b68d-941f8cc1ff09 | -6.19717 | -44.54027 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f858e84c-3b5e-3432-83d7-b19b9fe27407 | -6.1966 | -44.54387 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fa95933-fbc4-38cd-a097-b2c8ab0d4bac | -6.19608 | -44.52541 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7efa00af-59ca-3634-947e-f7c659a4ed14 | -6.19602 | -44.5475 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 353b548b-2bad-32b6-b5e1-54f03034e51f | -6.19552 | -44.52896 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 781459df-87f6-3b91-9dfa-3929d55d394b | -6.1938 | -44.53976 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00525f68-16b2-3b3e-be79-79681c90d8e0 | -6.19322 | -44.54337 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1c748b4-40d9-3573-b626-cf27d9ca6b4c | -6.19272 | -44.52488 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2f497f2-75ae-3bd3-875f-ecca9b5ec1b8 | -6.19264 | -44.54699 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 599d0dad-da66-3037-b22d-e1f3125b975d | -6.19215 | -44.52843 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1baeec56-8e69-3ff4-9e44-c229cf7172e0 | -6.18927 | -44.54649 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1abf6bd1-6fc7-3897-a8f6-14f44af41015 | -6.18598 | -44.52382 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3d3bd26-05ca-35c1-8a13-6066a9c5cd89 | -6.18453 | -44.29603 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 759a37df-1e3f-3e65-915f-d6d2a7b8d07f | -6.1806 | -44.29913 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ded648c-b7c4-3b62-82d4-c3b59191b5ad | -6.12377 | -44.58819 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bc4ca87-50cc-36cc-9b8a-96bfd459358c | -6.12319 | -44.59181 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab7dab93-742c-3577-9577-81eda0408c33 | -6.07127 | -44.62471 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 329d6adc-430b-3e17-962f-8503f5e58861 | -6.01267 | -44.52647 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90d6bd80-f53d-3c8e-b65e-514cda60ecd5 | -5.93664 | -44.65574 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a58963a8-b62d-377d-a16e-a991993d1861 | -5.92707 | -44.65046 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32193f93-130e-3fc7-a5f9-e45ce020871d | -5.90928 | -44.25241 | 2024-10-25 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 919e4171-9105-3160-82dd-8c7cd1b56b40 | -5.89776 | -44.15234 | 2024-10-25 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7fc8136-703e-34a7-9140-8a312849311f | -5.8932 | -44.64507 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2fb3884-950e-36e7-a5d5-000616b7cb98 | -5.89262 | -44.64869 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e11b4c74-2e09-3f2e-aa20-15211319078c | -5.89203 | -44.65231 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ee7864c-eab6-39f1-ae74-487ef9527dcb | -5.88981 | -44.64454 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46356047-ed54-3e27-8188-60aefd9f1214 | -5.88923 | -44.64816 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71b9a4dc-e6c4-3d78-a078-647dd1a7d67f | -5.88865 | -44.65177 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a0288d3-cd25-3df0-ac78-ba1b398c8a44 | -5.88584 | -44.64762 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e9d0467-b884-35c8-871f-78ffd9214aef | -5.88459 | -44.64722 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb7bd294-5320-3e2b-a631-af6705d3dc1b | -5.87202 | -44.68273 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a195173-7358-368d-9eb8-fa5d77234edd | -5.86862 | -44.68221 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d831a33-9deb-39cc-92cb-af263e39f064 | -5.86804 | -44.68588 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e8f4617-0cbd-367e-b118-f5cf431128e7 | -5.81535 | -44.4948 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bb5e6ed-1d4a-32a4-b981-13a360adbca0 | -5.81256 | -44.49065 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee29051c-837b-3f10-aeb5-5062d82acf52 | -5.81198 | -44.49428 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e71110a9-3c15-31c4-a8b1-999480154eff | -5.68882 | -44.48612 | 2024-10-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 967c63c9-864e-32ce-9c5f-27214877505a | -5.57975 | -44.31347 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39355b07-f8ef-3e2a-bd23-958b2965b614 | -5.51687 | -44.68673 | 2024-10-25 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9dc9b91-54c8-37b0-811b-22e31e1cdf8c | -7.62261 | -44.70973 | 2024-10-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4990ef3d-4b39-33a1-9e8d-f5a362fcaca6 | -7.19611 | -44.73743 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 616d1087-4dba-3caf-b9ae-3f583acc72c9 | -7.19553 | -44.74104 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dff7c324-f649-3904-972c-510f0d5e7d0d | -7.19505 | -44.72256 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73b726b5-3011-3c62-aa1d-1990a15bf382 | -7.19332 | -44.73331 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a348411e-e434-322b-be95-7aca05812208 | -7.19274 | -44.73691 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9f0348b-3aad-32a6-ab69-a652526a05d4 | -7.19168 | -44.72205 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4f1cd26-317f-3039-8606-1b1797db800f | -7.17868 | -44.99588 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4b56c9e-1494-3091-858f-1832b86b2949 | -7.17808 | -44.99956 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce8a6d1-835e-355f-9d31-7be419b6cca2 | -7.17241 | -44.72233 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4de1869-df36-3528-b89f-a611e9681bc7 | -7.14272 | -44.8436 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 918a3bf8-617b-3154-884a-5104180f8da3 | -7.06664 | -45.23198 | 2024-10-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f0724c-028c-3856-9fa8-611da4e25cf6 | -7.06382 | -45.22766 | 2024-10-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2502ef9f-f5d6-3e8f-abea-7b043b48aea2 | -7.06322 | -45.23141 | 2024-10-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f08f50db-ab67-3f65-9a2e-d09c0b81775b | -6.84748 | -44.75515 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 841b7c3a-284d-32da-9182-7ee671cb2bc0 | -6.84415 | -44.38694 | 2024-10-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 492e13cb-7791-3f46-b77a-cd7e4c3b8b34 | -6.8441 | -44.75464 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3ae1fca-c066-317f-a4b5-891d1883c30d | -6.84358 | -44.3905 | 2024-10-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aba0fcea-9da5-3e07-8b69-76cf778bef7c | -6.84072 | -44.75414 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e251e8c-611d-3509-bd5b-ae2a5b1e4c3e | -6.84015 | -44.75776 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a7f1881-1ceb-3a51-b395-7e16352b8235 | -6.83677 | -44.75725 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99920285-77d8-3cb3-b047-2180768e259d | -6.83619 | -44.76087 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db799e17-7da9-33de-b5e3-9d7178623d42 | -6.83281 | -44.76038 | 2024-10-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49e7c396-ddd8-33d2-b8fa-7aadb760a9b3 | -7.54707 | -44.09857 | 2024-10-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
