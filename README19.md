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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7b54997-4b50-36be-81a7-62ef4acc69a9 | -7.8135 | -44.0126 | 2025-07-02 05:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 69a658a4-3b9f-3690-826c-5510bdf03a64 | -7.7947 | -44.0145 | 2025-07-02 05:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 397408dd-7d28-340a-afac-dfcab01f6926 | -7.6051 | -45.7464 | 2025-07-02 05:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 819c4a2b-3bde-38fe-bd69-5642eca40906 | -7.8133 | -44.0358 | 2025-07-02 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1dd79ed2-b605-3995-bca0-b4cd8e32e4bf | -7.6051 | -45.7464 | 2025-07-02 05:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c623600d-178f-31f7-a781-671f44ab1e62 | -7.8135 | -44.0126 | 2025-07-02 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| c09acc44-2b6d-3b16-8203-a5c90aaa2264 | -7.7947 | -44.0145 | 2025-07-02 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9e1af50c-e782-3cf6-bffb-a8b9016c5eb0 | -7.6051 | -45.7464 | 2025-07-02 05:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| fd70dd97-09e2-383f-a5dd-d1fd5c9c83e6 | -7.8133 | -44.0358 | 2025-07-02 05:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 43dc86db-9183-3a9a-9785-4b11304095e5 | -7.8135 | -44.0126 | 2025-07-02 05:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 613329e1-bdb4-3744-b6b2-1b1fe86bfe72 | -7.7947 | -44.0145 | 2025-07-02 05:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 01ed4329-19ad-3902-83cd-0b5145496638 | -7.8135 | -44.0126 | 2025-07-02 06:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 72d4cab3-0ab9-3759-b97b-53aa49bb9d57 | -7.6051 | -45.7464 | 2025-07-02 06:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 95700605-4a0c-3696-9561-095a298852a6 | -7.8133 | -44.0358 | 2025-07-02 06:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c53cce7b-9a7d-371f-9248-90b5336ad5eb | -7.7947 | -44.0145 | 2025-07-02 06:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9f9249fe-c27a-3f2c-8c86-4a9c921f36e0 | -9.04497 | -63.98887 | 2025-07-02 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 478decf5-cd0c-3154-9b2c-8829d08e8a44 | -9.95758 | -64.99764 | 2025-07-02 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aee7fbf-eb3d-3b6f-a454-1a50c909b891 | -9.04583 | -63.98804 | 2025-07-02 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e92fd847-e79d-3fef-823b-9deb120cf9c0 | -9.04543 | -63.99098 | 2025-07-02 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e394c651-a014-321a-9cfe-80cd7111d712 | -10.29989 | -67.41174 | 2025-07-02 06:08:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a13b70a2-b3f8-31a1-bf72-6428e6f7a55b | -10.29979 | -67.4126 | 2025-07-02 06:08:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa8eff5-f01d-3333-905f-376868c323e0 | -9.25057 | -58.75113 | 2025-07-02 06:08:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1477843f-175a-3ecf-b7cc-43e9d3afa150 | -7.7947 | -44.0145 | 2025-07-02 06:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d774144e-7cb3-324c-84fc-744a34248f3f | -7.8135 | -44.0126 | 2025-07-02 06:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5aca2a63-ac7a-3564-b24f-bcb3a9b47e1d | -7.6051 | -45.7464 | 2025-07-02 06:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 8953f2fe-47e9-3826-b0fe-dff1bf0a1886 | -10.52594 | -68.04058 | 2025-07-02 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56369c48-55d7-3713-93c2-7cfba6e811fa | -7.7947 | -44.0145 | 2025-07-02 06:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| df3d5f54-eea6-3cbb-b24e-06203ae05d58 | -7.6051 | -45.7464 | 2025-07-02 06:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f6ca9c7b-3789-3fbf-96cd-909f25cc0b25 | -7.8135 | -44.0126 | 2025-07-02 06:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ad99b2c6-fcd3-3a47-b495-1ee6356cc542 | -7.6051 | -45.7464 | 2025-07-02 06:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d0e73d6a-1bb5-3b2e-bf9d-f8fbfdc5f551 | -7.8135 | -44.0126 | 2025-07-02 06:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 30e96d4a-d02c-3b80-b0bc-36d829ae1a98 | -7.7947 | -44.0145 | 2025-07-02 06:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 7cb8a831-6ac0-33ee-93b4-66f205170459 | -7.8135 | -44.0126 | 2025-07-02 06:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a532a3a1-a6da-3a1b-9d3f-70cbe7a0feb6 | -7.6051 | -45.7464 | 2025-07-02 06:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d72125ea-f77d-3f54-8333-9afcc763f3f2 | -7.7947 | -44.0145 | 2025-07-02 06:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 826895ae-5496-3729-82fd-3bdf1f7e8865 | -7.7947 | -44.0145 | 2025-07-02 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b8e3c5f5-5c6c-3f26-8a1e-e2a397e1b061 | -7.8135 | -44.0126 | 2025-07-02 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3bd4c01e-b1db-303b-8722-06c7be4ce19d | -7.6051 | -45.7464 | 2025-07-02 06:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c4862e33-ae67-3daa-8d55-0b89dff5d626 | -7.7947 | -44.0145 | 2025-07-02 07:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f1fa4a0b-27b8-3054-9244-aaa90e7dc5af | -7.6051 | -45.7464 | 2025-07-02 07:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ab6c3ac0-1167-3f2d-ba2c-0101326f2e48 | -7.8135 | -44.0126 | 2025-07-02 07:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d64d87b3-6a5e-3c26-b45a-d953738bab63 | -7.7947 | -44.0145 | 2025-07-02 07:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f2e5d2c8-d2c4-30bf-b246-2b60b1c45a26 | -7.8135 | -44.0126 | 2025-07-02 07:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| db9abd51-e717-3758-8434-a6541004428b | -7.6051 | -45.7464 | 2025-07-02 07:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c9814c19-20c9-31a1-9425-1891e437e2be | -7.8135 | -44.0126 | 2025-07-02 07:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 8ca14f25-992c-38f0-a194-37725a3a4547 | -7.6051 | -45.7464 | 2025-07-02 07:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4d1cc108-0c8a-3c21-a007-a01fc209f7cb | -7.6051 | -45.7464 | 2025-07-02 07:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 15fc638c-d6c5-3de7-bc2f-f34121deaaa7 | -7.6051 | -45.7464 | 2025-07-02 07:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 53f58bc5-aed1-368c-bd32-04d4a4018e10 | -12.4274 | -50.0171 | 2025-07-02 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e662cd3f-b9cc-38ce-aa35-24d9235f33de | -12.427 | -50.0387 | 2025-07-02 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 6b5edfc5-b39b-3437-b6e3-b4df71d30a7d | -12.4274 | -50.0171 | 2025-07-02 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 611948e0-0c3f-37d4-894f-32e2c2d9ba73 | -12.4274 | -50.0171 | 2025-07-02 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 722da0e3-9c71-3297-ba4e-a19560674f37 | -12.427 | -50.0387 | 2025-07-02 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| e8cf4c29-3aa4-3ac6-84ff-db609a86ece3 | -7.6239 | -45.7447 | 2025-07-02 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 86db0969-f96f-39ae-939f-ab2b0be6e33f | -12.4274 | -50.0171 | 2025-07-02 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 72c5c0d6-2efd-3d0e-b08a-f8a36e2c7be1 | -12.427 | -50.0387 | 2025-07-02 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 74c7fd73-3fe8-3021-b3d8-aef25ea81987 | -7.6051 | -45.7464 | 2025-07-02 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4bb6670b-b83e-3950-b5ad-a30e1b1d4ced | -12.4274 | -50.0171 | 2025-07-02 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 3f79061d-d16e-3cf1-bfe1-f2703da54f08 | -12.427 | -50.0387 | 2025-07-02 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f08ccc33-3bf8-30d3-8c93-f4852f66ce3c | -6.9605 | -42.8816 | 2025-07-02 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 32296e1c-0a3b-3bc4-ad57-33084b17c4f1 | -7.6239 | -45.7447 | 2025-07-02 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5b329c48-a8d0-35e4-8102-2c1d687d23c6 | -7.6051 | -45.7464 | 2025-07-02 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9b0c8a15-bd3c-3426-ae63-19248d7be01f | -7.6239 | -45.7447 | 2025-07-02 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 822d7827-f77c-3c69-902f-7e89d20237f6 | -6.9605 | -42.8816 | 2025-07-02 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 420.0 |
| 460e6a5a-236d-3356-8e4e-bcf171934a50 | -7.6051 | -45.7464 | 2025-07-02 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d6da7e05-4ff9-35c2-961d-cbfdee409b1c | -12.4274 | -50.0171 | 2025-07-02 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 548cce10-8ddc-3351-a743-c44586c66c17 | -7.6051 | -45.7464 | 2025-07-02 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 21ee0710-efe6-3021-bfce-265e4522db06 | -7.6239 | -45.7447 | 2025-07-02 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ce7ebf63-0e14-3ddc-a736-e5a268a7425c | -12.427 | -50.0387 | 2025-07-02 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| bb7116b9-4d0b-3ba8-8992-0fdf54a59aab | -12.4274 | -50.0171 | 2025-07-02 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 75495b6b-e6e1-32cd-a357-867f03614a72 | -7.6051 | -45.7464 | 2025-07-02 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 3e8e4800-fc37-34ab-b683-1bb1f4660d84 | -7.6239 | -45.7447 | 2025-07-02 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ad6f4f08-7f4a-332f-8fdf-b1f3f8fc98f5 | -9.8461 | -44.7065 | 2025-07-02 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 30dcee3a-fab8-3381-aac1-06ea77f659eb | -6.9605 | -42.8816 | 2025-07-02 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 216.9 |
| 4ce5712f-febf-30b2-87aa-5b511d9b3ae4 | -9.8461 | -44.7065 | 2025-07-02 13:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 185a2e3f-f340-3853-ab13-3631b79d6f7f | -7.6051 | -45.7464 | 2025-07-02 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| cfb2526a-20ee-31f8-9fda-d10991a66174 | -7.6239 | -45.7447 | 2025-07-02 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 0969d777-b8d5-329d-b77b-9a63124b7bc2 | -12.4274 | -50.0171 | 2025-07-02 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 3ffe9d14-efc2-3484-88e8-d45df0f9da21 | -6.9605 | -42.8816 | 2025-07-02 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 337.0 |
| 0549c0de-b428-34cc-877f-94f875a897f3 | -12.427 | -50.0387 | 2025-07-02 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| da19b71d-06de-3464-b24a-c25a58dc17cb | -12.6632 | -45.3008 | 2025-07-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| bb28b328-977a-3768-9f44-b5088671d027 | -12.4274 | -50.0171 | 2025-07-02 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 53103d13-e004-33aa-a98f-308bdfc5324a | -5.9216 | -43.4403 | 2025-07-02 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 928fe75e-f6a8-3c0f-8c16-054ce3a827c0 | -7.6051 | -45.7464 | 2025-07-02 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 5fa4319e-9ef3-318e-b230-48c24c4fb804 | -12.427 | -50.0387 | 2025-07-02 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 9fc31c89-1d90-3ce8-ab17-93c45f7308ec | -12.6632 | -45.3008 | 2025-07-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 0580b6bb-bc9e-3e65-8fac-a8ea407c87c1 | -6.9605 | -42.8816 | 2025-07-02 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 56c0c135-8b25-378a-b03e-4b8ca32a4c22 | -7.6239 | -45.7447 | 2025-07-02 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d77de554-9298-3b60-be20-8d9a818da5ee | -5.9216 | -43.4403 | 2025-07-02 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f8d89077-a792-35ab-b94c-5c02b7153662 | -12.6632 | -45.3008 | 2025-07-02 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 62f6c8e4-adfa-3580-87e4-bd85ed6c5925 | -7.6051 | -45.7464 | 2025-07-02 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 2545bb25-ff8a-3772-b3a0-d5e0bd8e0e69 | -12.4274 | -50.0171 | 2025-07-02 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| f3e0e5f4-3a8e-3537-b316-f3b1f11986d2 | -12.427 | -50.0387 | 2025-07-02 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 157.4 |
| e013d7ae-9085-331c-9480-eab3ad2905ea | -7.6239 | -45.7447 | 2025-07-02 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a1689f73-3531-368e-9e8c-05e0ea9fc34b | -7.6239 | -45.7447 | 2025-07-02 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2c9ef7b3-cea3-3c10-bbab-6ef177ba32f6 | -12.427 | -50.0387 | 2025-07-02 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 5146e6e4-ccd9-3652-98f0-186b391ed445 | -12.6632 | -45.3008 | 2025-07-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| b3996d86-3fca-3aab-a26e-db6dc5fd18e3 | -9.9761 | -46.1725 | 2025-07-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d5411c30-6307-3a71-9989-118f1635c71f | -5.9216 | -43.4403 | 2025-07-02 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4eaf5db5-8069-3737-8ea5-4ab27e53b7a7 | -7.6051 | -45.7464 | 2025-07-02 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |


[Clique aqui para ver as próximas entradas](README20.md)
