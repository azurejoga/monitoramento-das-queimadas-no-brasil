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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0df074d6-ec25-3340-9069-ac659e0c13da | -3.09462 | -53.24824 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6b6852f-6a8e-3e24-a066-c210deff9e6a | -2.81579 | -54.06136 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60d49780-f7cc-3891-ab8a-e89d7a8b051a | -3.03994 | -54.06291 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7ca9a84-0b9b-39a8-a53f-4aa60a1d92e4 | -4.07375 | -48.34177 | 2024-12-04 05:03:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd08c23e-b2a8-3b0f-b69b-9bb3b27924d7 | -4.26872 | -50.6813 | 2024-12-04 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66cc608b-9ca2-31d3-8633-c7d495b833b2 | -1.66312 | -52.75118 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6b243942-6f83-3a27-ba15-8e7b25da081d | -3.42055 | -50.17323 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dcae743-3f43-3538-89ec-985ec5fa2b3f | -3.0259 | -53.87189 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6874055-5251-3a53-990d-2835411a5b8f | -2.87308 | -54.02316 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db17e454-1b97-3140-9ba3-70de7c290127 | -1.34605 | -55.15958 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 808e93fc-d37e-3e35-8ca1-b70a17ccafa7 | -2.6227 | -54.32193 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf5dfa92-d341-3a78-8fde-f090d0430e82 | -2.43245 | -53.96985 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b70c300a-89f8-3068-a80d-bacee594b732 | -2.79384 | -54.13728 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c9ebc4e-4842-303e-abde-4f6e22ec5301 | -0.16542 | -50.40482 | 2024-12-04 05:03:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50685502-df23-3e12-ba2e-bd7130e2e99b | -3.10906 | -54.03727 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb3bd69c-e7c1-3996-b1c6-3bfbec3f7fe0 | -2.77369 | -54.11637 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adc127fb-17f3-3611-8f55-f86ec2d65282 | -2.31344 | -45.42249 | 2024-12-04 05:03:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d01044c7-dd45-38c9-834e-fc4e370141a2 | -1.42677 | -54.50819 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00cc9840-2916-3502-8eec-19be42039a0c | -2.58317 | -53.67607 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8298a93-3a75-326d-8041-17a905f59138 | -2.83195 | -46.75494 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b68cba43-81f2-3f84-aafe-47fa7abb79b3 | -2.43579 | -53.97036 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a42b4c6-0e1d-376d-8bc8-adbf8eb523e2 | -2.88563 | -51.80098 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8c6842cb-ee62-3992-91d5-7570b5b3256d | -3.10782 | -53.97895 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cb826c2-03d3-3f19-9bbc-0de56fe8fbbb | -2.8237 | -53.94297 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 433953cf-474a-3c11-b0a1-4d0fd686a86b | -2.85804 | -53.34958 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaddb401-247a-31b8-9176-eaa03d557215 | -3.01013 | -53.22816 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7593d3bf-7712-32dc-8c79-73be75716161 | -3.90254 | -52.20491 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ffbdfc9-1279-3b1a-913c-fa312d86c7f6 | -3.84918 | -52.1597 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 113531e8-fbf8-37c9-bf55-6282cdd452bf | -1.752 | -52.62773 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ceb5ef46-e612-3714-80fd-df0524fbe136 | -3.49184 | -53.97591 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac140733-512d-3bb4-872a-b801d7936616 | -1.72707 | -52.65127 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13c4b353-89ec-3f9c-8fcc-e97021362ddd | -3.00592 | -54.74334 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e72664f-3b1e-3f3c-8872-8bc9de1558ec | -3.94625 | -50.66328 | 2024-12-04 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ab46d3c-2bfb-3243-804d-d99cb1aeef37 | -3.95944 | -52.20341 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4493886b-4bc1-3528-84af-efff8feacab9 | -1.74275 | -52.61847 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 8d4aadc5-6e5d-3546-83ec-096206007180 | -1.46129 | -54.96305 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae22e9c2-7a98-3cd9-8120-f82de21a1395 | -2.77656 | -52.98932 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33027be0-054d-3e0b-9364-012e90d46f5f | -2.84608 | -53.95371 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2015b4fd-8a3c-3c42-980a-98790e81159e | -2.9718 | -53.95469 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fd0e5cd-d6fc-39c9-bf5a-9dc0cb6521e4 | -3.17809 | -54.33652 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a4a8d5b-2a0c-3e0f-b892-2a2615f63cb2 | -3.12089 | -54.61643 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d3360ac8-2cbf-394e-8471-08ddb560ef64 | -2.85477 | -54.05288 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcf699b1-6d8b-300f-9459-537ea69ad38b | -2.80525 | -53.05566 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93458710-25ec-3572-85a7-ebaa8280afdf | -3.30451 | -54.15787 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cbb3ba0-8e96-3b7f-9e28-06d5e0db9e85 | -1.82149 | -53.04211 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f8b86ee-9c7e-3dc7-8d01-77f5aee5205b | -3.09347 | -53.25572 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0608fb8-2bb3-3204-a1a1-1e9c0b070db5 | -2.59492 | -54.01632 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ba24f7b-9dfd-3cd5-a79f-52363ed1ca7e | -2.65368 | -54.10088 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aae33d7-56af-3037-bcc7-15f0a4ca962f | -2.97717 | -53.87535 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2069b43a-248b-35b6-859f-437cac591461 | -1.78692 | -52.74612 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca13fd4a-7185-3eaf-8ec6-40f81375b40b | -3.11411 | -54.04896 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 928e76da-d830-3b96-8f52-377797600b5f | -3.11297 | -54.03424 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfa73a62-37ae-3c3c-b7a9-1e1d74923848 | -2.52915 | -53.98106 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3d82f2ee-4291-3e2d-bc96-e7d153de11b7 | -3.10241 | -54.05801 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f95ff68-126d-34c1-b862-b7a726b635ce | -1.62882 | -52.36475 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d63ce3ad-d76a-30cf-8ff8-5c2960e926d1 | -3.0602 | -51.71524 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3d68b49-b8ec-3e7e-b2ea-9f549fc94d5c | -2.88569 | -54.16219 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4aad32b4-9e61-37c9-bd2d-d0d1e63c8a79 | -1.36983 | -53.65068 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74c621f6-4677-35f0-9d1d-35bf3977f913 | -2.66944 | -52.45581 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8eca1dcb-67a9-33e6-a9d0-cbcfacba2d4e | -3.42455 | -52.02295 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68122e1d-4196-3c76-9c75-940c12e3c7f5 | -2.44266 | -54.03632 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 658cf22b-c94d-3d0e-b6a8-902bab5e1c5c | -2.20243 | -45.67381 | 2024-12-04 05:03:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a127b56-7f31-3788-bff5-9dfa9e215496 | -3.12861 | -54.61053 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e8686fe-82bc-3358-b642-894265260e8c | -3.06028 | -52.76506 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef06048b-a7d4-3f60-9e2a-44d51800136a | -3.10734 | -53.75925 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93662a52-205f-34af-848b-7c05c568240f | -3.81821 | -51.66691 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 965e2a6a-89eb-3e34-9ccd-fae467d9d7d2 | -1.76013 | -52.62115 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87dc6f57-4260-3001-83c2-f6f44ed8e82c | -3.08202 | -53.37537 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4c0f680-65e4-36f9-b959-22dad9f8bd5e | -2.99343 | -54.12469 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8883d2e7-66f0-300a-82bb-f3c6927ad76a | -2.44753 | -53.98298 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 376eb844-2767-3d9e-ac64-c79d9c5ac3e1 | -2.87253 | -54.02669 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc1b9ca4-3ee2-3f1d-bf96-f3188f4269f0 | -2.58876 | -53.97228 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee20be28-2d5c-309d-82e5-a5f18cc469cd | -1.71368 | -52.78516 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50b9992b-97ca-3c60-a214-1591eb4bd92d | -2.69703 | -45.65342 | 2024-12-04 05:03:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 898819b7-9b42-3b64-a1ed-18b13d3bb801 | -3.93494 | -50.52124 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 242a172a-2c3b-3f83-b126-b4c2f5d87369 | -3.13084 | -54.61797 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3fc64e54-c7a6-32bc-82c2-ef85b6660ef9 | -2.45855 | -53.71225 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e98e954-0639-37da-8ce3-7c38ab602708 | -1.73247 | -47.05444 | 2024-12-04 05:03:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5ffb2c5-f3a8-3685-9667-1c3d4c9252fa | -2.554 | -53.40893 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 038bd804-17a6-3805-a289-2384e70093e8 | -3.37571 | -52.78691 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4277fff9-3395-3a35-9f73-6e54cd4c5a70 | -3.9806 | -50.51769 | 2024-12-04 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5eeb8d4c-81f1-33f4-8bce-df34deebf73e | -1.88289 | -53.30326 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c85ea99f-e4cd-33b4-b0dd-d226f813a950 | -1.7497 | -52.61954 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 024b68a8-d75f-34e5-bc0c-82f7e7f78a69 | -3.12699 | -54.62091 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| c6931311-42db-352f-af84-01c8fede0bb2 | -2.78939 | -55.36813 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b3d8110-8c39-3bcd-aad5-179cb2159b1b | -3.33708 | -51.2058 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aab58bd3-dee3-359b-8445-8aac5b29015b | -2.02364 | -53.29843 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2f4e32f-90c2-3364-a3f8-362868c3da83 | -3.11118 | -53.97947 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13ed9dea-ff1f-3ad7-ad67-6eb91e184af1 | -3.10374 | -53.28016 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a702db66-dd84-3dbc-b2cb-ce0025600e16 | -2.46228 | -53.62086 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 656a92df-1125-3e3a-b2ed-4ee3849d4e6a | -1.36594 | -53.65371 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e56b69-c48b-34f0-b192-3698dca892ea | -1.49744 | -51.94613 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47295fde-9f2a-3c7e-8ad0-c42bb1eb6ba8 | -3.07227 | -54.05337 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 377196a8-720f-30d8-9f5c-8c52c1f92c77 | -2.58172 | -54.80491 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af8206fd-b327-3bf8-8d44-35c6f08d1ee8 | -3.33921 | -53.30018 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ebd9baf-b02b-3500-bedc-130682450346 | -2.58191 | -51.92348 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 216666fe-9787-355a-ba7d-9e4b61e65fb0 | -3.10774 | -53.27697 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8e63674-fa07-3f90-ad33-456f179e3e61 | -2.52922 | -54.00273 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 71dca159-0204-3c33-b5ce-931a97232b9c | -2.89808 | -53.97262 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 109a2dd1-46e7-3a87-aacf-bae6bc19f9d1 | -3.25931 | -50.61143 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README51.md)
