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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9703b466-a1d6-3ffa-b858-f757b9e6281f | -3.88786 | -52.12705 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03ca848e-b3fc-37e1-863a-9a7e2fe3a6cb | -3.86927 | -52.1352 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd962c90-558b-3058-8ffd-8fcfa6599e28 | -3.8687 | -52.13879 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6d792af-88e2-3e6d-b69e-1da3e2c13925 | -3.86532 | -52.13829 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0639369f-cfd9-38e0-b4cc-0065402d43d8 | -3.84934 | -51.88405 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b8547b-f571-3b82-a847-32899003f108 | -3.84594 | -51.88352 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d406ce90-f61f-3a7e-9dfb-905c06ad6cba | -3.83417 | -51.98208 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b8b5351-8c84-33ca-9875-51152040edc6 | -3.82942 | -52.23526 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c2b0390-cc6c-3a5d-82ae-dd1fe9cff731 | -3.78322 | -52.1769 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7505eee3-5e6d-3a9c-ab55-65821c142ecb | -3.67826 | -51.92848 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da807df2-9143-3cf1-ae65-b012f0e79395 | -3.67769 | -51.93209 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0d251d0-93c2-378d-8d08-628ffd913f06 | -3.6743 | -51.93156 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a9e5143-08d3-3f5f-969f-74aab79500ae | -3.65789 | -51.9253 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6c74dc87-5226-359a-a36c-539fe5ca4075 | -3.54791 | -52.15923 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| defde428-60aa-3aab-946d-cc4ff6de2f78 | -3.54454 | -52.15872 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccbac861-9f04-3969-9148-823010d4b88f | -3.88719 | -50.98438 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c143258-7dc6-3718-b89c-d97269edbe17 | -3.8866 | -50.98827 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48555271-1d00-3409-bf77-6b54412b7143 | -3.8718 | -51.0378 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef4f74f5-6213-344f-b677-544487b028c4 | -3.8292 | -51.36131 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2464749-fb3e-3a21-a6e2-0c534a1f4f85 | -3.82862 | -51.36508 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3caf2363-eee1-339e-baf6-a8997128c2e5 | -3.82766 | -51.20917 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93f795b0-71d4-3634-96e0-6aa438e10bde | -3.82631 | -51.35702 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05fb9f8a-c985-3dcb-8436-03a63e7853b4 | -3.82573 | -51.36079 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6902b630-52b4-3040-97bc-2b9e316348c3 | -3.74653 | -51.05466 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ba7732b-de1b-365d-a7c1-fe8025552bed | -3.7155 | -51.14063 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b81fb01a-e0d9-3b51-bbae-9a09d2d5caa1 | -3.7147 | -51.1416 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 929d80e5-2871-3acf-85ab-f87be925c044 | -3.71121 | -51.14106 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ec4ba93-1ba2-3882-a860-11c62503922a | -3.67909 | -51.16369 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c47381-3a49-3815-affa-fefc09366df7 | -6.40553 | -51.71101 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c76b57e-5740-3ff3-b628-fc23e058d956 | -5.62612 | -51.39121 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99358e2d-04cf-33b9-8fdf-c1f873a49736 | -5.62605 | -51.39004 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e820e70-794f-3b9a-8215-ca0aab559bb9 | -5.6226 | -51.39066 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0968f09-58e0-3ec8-9918-f2510e66b3ba | -6.51209 | -52.42302 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb50d57f-c7a3-35c7-bf03-07f2c4a3138e | 1.00935 | -52.21856 | 2024-10-24 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e353e64a-dc8e-3d70-8632-f36d62e93096 | 0.50075 | -51.67683 | 2024-10-24 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aced6a00-88bf-369c-bbb1-5585241339ce | -2.05186 | -52.03521 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7613d5eb-7d88-33a6-b244-a216752e5561 | -2.04906 | -52.03117 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 547481da-ee57-30dc-af2d-2d1dd54e739f | -2.04571 | -52.03065 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b92696a8-f97d-36f2-94e9-f6f49f84d4ff | -2.04515 | -52.03418 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71a7e1c9-862a-3195-8c81-8749099abf02 | -1.98195 | -52.02077 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7aa8d4ad-7cfd-3f28-a6af-aabbb5d06a78 | -1.97859 | -52.02026 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22024d92-df73-3461-9d80-dd67051a8fe3 | -1.93378 | -52.13948 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01bee14d-8dab-32ee-bc1a-a84066466f66 | -1.87392 | -52.30216 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e6a3733-4ed3-318b-84dc-044313f510b9 | -1.76607 | -52.2356 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4e13054-8c37-3717-8565-fb0f3153fa87 | -1.66027 | -52.21864 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08c7abab-3658-3109-80b4-a42b2658bfb9 | -1.55825 | -52.26731 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd4147b0-ccd5-3744-a3a0-e7b6303eb528 | -1.52203 | -51.93901 | 2024-10-24 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48954783-e021-34ac-9d19-a96dec9d673a | -1.51867 | -51.93849 | 2024-10-24 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f00fc451-b872-3afb-95db-14f5d70fff01 | -1.38365 | -52.00072 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 269846c4-4c3f-3302-9588-bd5b1a65965b | -2.08629 | -53.23443 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93103d78-802e-301c-98da-cb50028e3233 | -2.0052 | -53.29594 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222518ff-f6c5-3ca6-a9a1-df3999a0e951 | -1.89585 | -53.00384 | 2024-10-24 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b30cd3af-8f27-33d6-867c-dc091d87f810 | -1.69873 | -53.35074 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b832564a-1a20-3853-8d09-3cd39f7d43eb | -1.60089 | -53.30733 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47f3d8b9-20f4-367c-a253-e5cdefd1a869 | -1.60035 | -53.31078 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2f70ad2-2e92-391f-b4fd-38df0da3e1c9 | -1.59812 | -53.30336 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff18608a-aabc-3bf2-9240-966830ee39ab | -1.59757 | -53.30681 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56147787-842f-3392-8038-4383d3e0f8e0 | -1.59703 | -53.31026 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 689705ad-1c1b-3f15-8dce-c457bd8d4a28 | -1.5948 | -53.30284 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9aac0476-2303-3147-984f-66113c3d5885 | -1.59425 | -53.30629 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7a1e40b-8f00-3cbd-8cd5-9c6c226d8958 | -1.59371 | -53.30974 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 414bbf9e-9120-3e92-bd06-642f4d0fda5c | -1.59317 | -53.31319 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c96bc526-48c0-3f6e-a53b-ea3f1f9e810c | -1.59093 | -53.30578 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d246cd5-94cb-376e-8353-d17b0494861b | -1.59039 | -53.30923 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bf8cda60-09f9-3238-a607-22b4e7416fdf | -1.58985 | -53.31268 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9bf1bac5-f631-30a9-bb72-fd35b142ceb8 | -1.5893 | -53.31613 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b171b29-5dca-3028-ae7d-6a46a940a4d9 | -1.58761 | -53.30526 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 07414a67-9b00-3cb2-8ac9-19ba0e03387e | -1.58707 | -53.30871 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80d589e9-9839-32f1-a3d4-9244e3dd7092 | -1.58653 | -53.31216 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dd0b8e48-9bf8-34db-9b3e-920c84871623 | -1.58598 | -53.31561 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffe44141-af3f-377e-b696-49b7d9593f94 | -1.58544 | -53.31906 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 841b56df-2f1d-3860-a7db-c5537c6b02ea | -1.58429 | -53.30474 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16768d23-cfbf-3dad-b43b-95f2967f5bab | -1.58375 | -53.30819 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b85e51a9-622a-3c38-bd93-7ccec3d2b354 | -1.5832 | -53.31164 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e024b1a-4ccb-3351-b08d-b7ef40f68730 | -1.58266 | -53.3151 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 140bb4ed-2f2b-3a8d-8f98-f77568c52838 | -1.57988 | -53.31113 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa19f9f2-e187-32f3-a74a-567174428bba | -1.57934 | -53.31458 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ff415ec-776a-3814-af78-6f6ffd46f8d1 | -1.5788 | -53.31803 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96e1c91a-70b6-3886-a998-dd4f943cf08b | -1.57602 | -53.31406 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80fc2840-c4be-3c25-ab6c-a1264c6f1b84 | -1.57548 | -53.31751 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c52a8705-50ba-3a77-9df2-8462b623901c | -1.53539 | -52.73181 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bed8a278-504e-3c25-902d-45f2172bf653 | -1.51235 | -53.13754 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d139d584-a09e-3636-bd9d-3e198ed38954 | -1.50903 | -53.13702 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d31c8630-7931-3222-9717-f84673a2c259 | -1.4743 | -52.95185 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d4bb62d-7d60-3a91-ad8d-3a87c1216d5f | -1.41959 | -52.95393 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db94973f-bd0f-3325-9b02-ed76c25bf8de | -0.88452 | -52.00604 | 2024-10-24 04:55:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45d2bc80-9054-3cfc-82b0-04521cf5eb27 | -1.05457 | -53.01307 | 2024-10-24 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3376630d-18d8-3ab7-a470-5384512e152e | -3.29996 | -52.47977 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f11fa95-87c1-30f1-8e67-8d620616ca00 | -3.25269 | -53.3465 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2a6263a-460b-3f39-ad06-6dc5b17ba0a8 | -3.22234 | -53.36651 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1579c741-0917-3ad0-a10e-ebf6407d0bf5 | -3.21902 | -53.36599 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d64008b1-4cd6-3b2b-b401-742fabacdc70 | -3.21848 | -53.36944 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7feefaa7-1457-3529-b31b-15c14ae277a6 | -3.21571 | -53.36547 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4878b540-fbb4-33b6-bbae-ddd8c9995835 | -3.21228 | -52.45926 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce13e011-44b2-35f3-ba89-23649ea7b020 | -3.21173 | -52.46276 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e526680-4d2d-33ac-8b04-5c9af78ad216 | -3.17732 | -52.49288 | 2024-10-24 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0851c148-43c0-3d43-9f2d-9ded42f369ef | -3.1112 | -53.12671 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d2d9515-e49b-3468-9403-0ee4279d5947 | -3.11066 | -53.13017 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba1bde6-108e-3079-ae4f-6b0d188c380e | -3.11012 | -53.13362 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b3248ea-cb95-3482-b7e9-8e016f4f6ef5 | -3.10958 | -53.13707 | 2024-10-24 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README68.md)
