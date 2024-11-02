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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 974017a5-7c6c-3e11-9b12-686fea39dada | -2.77969 | -52.89504 | 2024-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| efed1cfb-7b28-32e1-8934-63f393b0377c | -2.67906 | -53.01799 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dff71e4a-e782-3d69-b346-a911fa5b54d8 | -2.61658 | -52.44926 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c7f675bc-c216-3df6-bf70-768029ab3489 | -2.57983 | -52.25503 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a05c422a-ba35-3599-9997-50a36401154d | -2.36436 | -52.02088 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8a71bdeb-be13-3cab-b2c5-0ea96feaebed | -3.81842 | -52.34531 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f2c9361e-b63f-33a4-8a4c-b35b48181f8f | -3.79234 | -52.31042 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6d283447-c9db-31bb-8b19-409137d507ce | -3.75013 | -52.36153 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 341db262-b92b-3b0c-a98d-216d800842da | -3.70611 | -52.43292 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| df7f482c-b6aa-301b-95af-c5ed0a469b06 | -3.7044 | -52.42007 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b3ce84b8-559f-3e1d-b1cd-2fb4b6bd5df3 | -2.18322 | -53.73976 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4e08f77f-5466-3f26-abe7-160de2fc8ac4 | -2.17691 | -53.69412 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6e781491-3f6f-3bc4-8612-2e230758244d | -2.17481 | -53.6789 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 4291916d-f6e8-346e-962b-f4a999b1322a | -2.16347 | -53.68061 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| d4bf23df-7f53-3c97-b64e-d0441fd6f273 | -2.1614 | -53.66552 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0daa86e1-d0be-3840-b887-50baf4a143e4 | -1.87044 | -54.70474 | 2024-11-02 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0f0ed021-65b1-3eb8-8398-642d9a6d24e3 | -1.86794 | -54.6868 | 2024-11-02 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3ab27d33-6155-3ee5-b70d-713b5b9bfe89 | -1.27201 | -53.37271 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 135afd99-526e-31b4-9515-8b6fcf5108bf | -1.21543 | -53.38612 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9dde2e99-cf83-3703-a3bf-402f699018e2 | -1.20606 | -53.6522 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5f712411-dc3e-3de7-8555-a2155d71eb65 | -1.19645 | -53.90885 | 2024-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 14872be5-266a-3026-b115-feb684c3c59a | -1.18984 | -53.69821 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 6676d8d1-743c-3635-8eb6-577959915fc1 | -1.18776 | -53.68353 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 254a5769-45ea-374b-8c0a-a97996f3003b | -1.17662 | -53.68525 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d2040b43-a742-3aaa-bdab-0b1e2cae02b7 | -1.16752 | -54.18839 | 2024-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f245f92d-75cc-3b7f-bdf5-3974983f2775 | -1.16539 | -53.6864 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e2b2785e-5f81-3e67-941a-4bd14e7bd0e6 | -1.16524 | -54.17236 | 2024-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 00fac0ad-cec4-3c3d-a1f4-b598b27bb139 | -1.16254 | -54.08728 | 2024-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 24e50645-044f-37cc-b9a1-7df599d86aaa | -1.07934 | -53.64615 | 2024-11-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 30fe4245-6dee-37fd-977d-775c58f97c7c | -1.5782 | -54.76217 | 2024-11-02 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d373eb0a-6104-39c1-93d4-a51feef36698 | -1.52375 | -54.28077 | 2024-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 376852c9-ee96-3480-b422-823ddc709818 | -1.38652 | -54.12469 | 2024-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b42822a6-9758-3dd3-8b42-4c90fe5e23c5 | -1.35077 | -54.6216 | 2024-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e964b285-136f-3936-881d-78178a4449f1 | -3.63331 | -53.96336 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| fee1f24c-76ff-35c6-9948-ba58e2e88f29 | -3.62752 | -53.97083 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5c6ea71f-7e7a-3ce9-af65-34f7bf6c018a | -3.62516 | -53.95383 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f3b9a8a7-5b90-3999-a907-1f613a869d23 | -3.314 | -54.13556 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 6b2c730a-6c2d-3432-8d64-cfac893f2888 | -3.302 | -54.13735 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| eaae807a-93d3-35a2-a864-e58a7f9db2ae | -3.26559 | -54.18362 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| cdd0aa7a-ac82-3d17-a668-45354cc774ab | -3.2132 | -54.94604 | 2024-11-02 00:54:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 71d439fe-dc4b-36fe-b2de-e2c33e395d59 | -3.20808 | -53.85183 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| c7c88777-9176-3513-b396-8ea90a2d7956 | -3.13065 | -54.26649 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 8067752a-332f-38b6-a248-323dc5a9174c | -3.12825 | -54.24936 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6c5249b8-5f27-3be1-b973-579a7e027020 | -3.12521 | -54.27822 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5979e55e-30b5-38cc-b669-e86ce1a95574 | -3.12337 | -54.3027 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ba85e8cd-c473-31ad-8df5-4f78f9a8e826 | -3.12293 | -54.26097 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 0869c2b1-ad05-376f-919d-9611ab2fee0a | -3.12066 | -54.24384 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 542751e9-d3cb-38f5-a07d-5f36ab3830a5 | -3.11851 | -54.26793 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b0cfbcd4-72e3-3bff-9fdf-b3115bc232e1 | -3.11612 | -54.25079 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ccc2642f-594b-3a3e-9ac5-2d388b9abd29 | -3.11537 | -54.29733 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 28e389db-79b7-3bab-97e1-1fc13656582c | -3.11308 | -54.27985 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 1b710cd5-3b91-3f4b-ab3d-bb15c07085cf | -3.11124 | -54.30451 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f1a5ad1d-4c40-3f6e-bd3a-a788821d7e1b | -3.11081 | -54.26252 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 61160e82-b55c-3d5f-8b98-8aad22a52d44 | -3.1108 | -53.72416 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0ba90cf5-4506-36b4-a5c1-8183521b6363 | -3.1088 | -54.28691 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d6f07968-fb2f-3638-849d-3ba8e1f293fa | -3.09708 | -53.71009 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 70a054ae-756b-30f8-8c69-eae5749fbcc2 | -3.09668 | -54.28858 | 2024-11-02 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8fa347d8-d6dc-321c-a396-10344cacdd33 | -3.08014 | -54.16832 | 2024-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f99a926a-7417-37f6-9cfd-2b89825ae149 | -3.06811 | -54.16985 | 2024-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 95582644-0086-35ac-b46f-c11013a1b3e1 | -3.0658 | -54.1529 | 2024-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 26df9978-ab72-39e7-ab25-d1c2f5301772 | -3.0157 | -53.87354 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c634dc9d-034b-3a6d-8d91-241d8fe48623 | -2.97321 | -53.91289 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9135633d-5c4b-3631-b532-9b8796565a83 | -2.96604 | -53.91913 | 2024-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| db77ff3f-df18-34fc-ba0d-3f46b12a648c | -2.68162 | -54.027 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d89eea1f-2dab-3393-8441-3603289d1cd2 | -2.63631 | -54.27608 | 2024-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e101383a-4928-34bb-b455-b6808dbe76d6 | -2.63395 | -54.25908 | 2024-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f4cc0b52-8e55-3201-a2d1-e649eedca122 | -2.57886 | -54.80077 | 2024-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 16bc4635-3d9b-3bad-be59-f6b4ca432ee4 | -2.55245 | -54.01625 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a07fcab5-6cda-385f-a68b-47ef1be2dd3e | -2.55026 | -54.0 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 03f2f187-a7a4-3db4-b515-2b58cc5ed08c | -2.50033 | -54.13087 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5192f1d6-0640-3c8c-b4bb-d67e6f498fef | -2.46087 | -54.15887 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1fa4b13e-9a2a-3885-ad8d-a5e88cb4a1b2 | -2.45517 | -54.15435 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ced03b26-0baf-3fc5-a5a4-ba786be193e1 | -2.39245 | -53.8401 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e2d4a6c9-65be-34a9-9306-9648b0f215b1 | -2.3809 | -53.84167 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9081c34a-e11a-3e38-a217-dacf76060168 | -2.366 | -53.73358 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a479915e-217a-38ad-a276-889c25c360ce | -2.36389 | -53.71825 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b4b159ab-5adb-3dc1-ab02-5f96ecc032d9 | -2.35451 | -53.73485 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b6e32093-9aee-3a87-9a49-82b02ee0f5dc | -2.35242 | -53.71959 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f4d78832-4e80-375d-8e90-a9661ab00f68 | -2.27664 | -53.75192 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3ccb6f06-359f-36a1-a8e3-58082044b199 | -2.27453 | -53.73662 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 1688363c-1015-3be0-9922-9c8de2a4727f | -2.26616 | -53.67595 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8875097e-a763-3b5f-be2b-2f333f0c4937 | -2.26519 | -53.75348 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3757c60e-24de-3bd7-bfe8-16e85d10d3af | -2.26408 | -53.66094 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| de606897-0c69-3c6f-a30f-43c703af8f09 | -2.26309 | -53.73818 | 2024-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ab7cc1fa-255c-3df0-b910-0fc0b558f5ff | -3.87758 | -54.14637 | 2024-11-02 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e6d810de-b0b9-35fa-81d1-511fc9a89e76 | -1.56414 | -55.88764 | 2024-11-02 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| df0b0e9e-3017-35ee-9224-52a6de006f2c | -1.26119 | -55.68493 | 2024-11-02 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 906bf9ea-32c1-3876-a152-c80c87b40835 | -2.36612 | -47.62764 | 2024-11-02 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7a942fec-1b9c-34eb-a7f4-657f02b8671e | -5.30945 | -43.07544 | 2024-11-02 00:54:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 24c911d1-8c18-3ed2-a5f4-b146f7535115 | -5.0081 | -46.03258 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 287e7bf2-5b89-3a6d-9f96-e5528f05e1db | -2.34828 | -48.41904 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 284f29d3-4456-35fe-9a58-bc86d4c93908 | -2.95624 | -51.0636 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 0ba0f2c9-5c94-3897-8a0f-02dd4b5c930d | -4.45034 | -43.64676 | 2024-11-02 00:54:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 289a1464-053d-3ca6-9934-ddf42e07b708 | -3.3919 | -41.63695 | 2024-11-02 00:54:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 3939cb25-e8bc-38de-84d9-e0b0f605d3e1 | -4.44823 | -43.63231 | 2024-11-02 00:54:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| c82ea012-32ef-3a43-8710-09db14bbc835 | -2.88799 | -40.52681 | 2024-11-02 00:54:00 | TERRA_M-M | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 21.9 |
| e89aac94-7236-380d-9440-26fb2f6342ed | -4.72837 | -42.66426 | 2024-11-02 00:54:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9a8e1e75-fdc9-36c9-99e6-b2db95017c5d | -4.58355 | -42.47907 | 2024-11-02 00:54:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 1fe7258a-da6e-3b41-a391-e6fc0c6a58d4 | -4.57714 | -42.46852 | 2024-11-02 00:54:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0cacd059-da8c-3192-a73b-056c5c8f2bb4 | -4.94272 | -43.02109 | 2024-11-02 00:54:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README8.md)
