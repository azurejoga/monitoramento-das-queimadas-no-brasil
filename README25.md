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
| 0481114b-9966-3650-a409-fdaac60f3e72 | -18.64389 | -49.96992 | 2025-08-18 04:51:00 | NOAA-21 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9e5fe5a1-099d-3fbf-a8e2-85f54ea878b1 | -26.42478 | -53.2311 | 2025-08-18 04:53:00 | NOAA-21 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ef29b06-fdc5-32e3-8654-8793cc792925 | -29.85389 | -54.56338 | 2025-08-18 04:53:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| ca193d71-1bae-338d-b9e2-732a1d020064 | -26.00155 | -52.05373 | 2025-08-18 04:53:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 73091ffd-51f7-3ff8-8d46-397e3fc4dab6 | -26.00093 | -52.05843 | 2025-08-18 04:53:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b94b957a-53ad-3e1a-9b86-1c8ea03b8739 | -28.83656 | -54.08858 | 2025-08-18 04:53:00 | NOAA-21 | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 70183ea6-62f8-3477-b347-23f5773ca31a | -28.83714 | -54.08424 | 2025-08-18 04:53:00 | NOAA-21 | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| f5bc6755-c229-3cfb-8ced-7c22bfa50f9f | -6.4335 | -44.7822 | 2025-08-18 05:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5e5a6978-9a29-3346-9918-98a2cd06ef19 | -13.1746 | -54.9337 | 2025-08-18 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0c60ff20-fed1-3b9e-ba8f-3992c45f0568 | -2.29941 | -48.14569 | 2025-08-18 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88e2dcbb-9fb8-36b6-941f-55b72931fb22 | -2.95933 | -49.06853 | 2025-08-18 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9d135cf-30e6-358b-90c5-935cfdd4c4f1 | -2.90059 | -51.47724 | 2025-08-18 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88a1219a-c4c6-3aaf-9036-915f76af8197 | -3.38055 | -47.60859 | 2025-08-18 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aefd4358-8656-3e21-aa83-5625a994a84a | -2.959 | -49.06717 | 2025-08-18 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37bf61f4-f950-3d2a-8a16-dee292662aa4 | -3.38585 | -47.60935 | 2025-08-18 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9f3fcb5-72cc-347b-bbfc-0df9ab8ce2c3 | -5.45375 | -60.13704 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70719481-c2b4-357c-877d-6cabe1cf65a3 | -6.5647 | -44.46908 | 2025-08-18 05:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8af9467-b8d1-310e-89e3-7aacca3807bc | -7.53118 | -50.5309 | 2025-08-18 05:12:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59305b38-b55b-3052-a674-1931182a3448 | -8.78239 | -49.9982 | 2025-08-18 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 339098ea-432d-38dd-bb9c-2bc1b83ccc10 | -5.44785 | -60.12754 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26956181-4014-3b24-a372-1ef2cdcfd598 | -6.802 | -44.72611 | 2025-08-18 05:12:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a2821fe-e89f-3135-a5cb-e9ff99ee704c | -9.39386 | -48.28966 | 2025-08-18 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6810de8c-92e0-3bf2-82d8-7c65d2bc3541 | -3.66213 | -50.95162 | 2025-08-18 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e2790e4-39d9-3d5f-91d2-fc429975d108 | -6.43667 | -44.79107 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 866f7285-c776-3449-879f-923055226ada | -6.13034 | -57.93073 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe14911-4f66-3506-a427-4aa0c2ebe338 | -5.92025 | -50.00486 | 2025-08-18 05:12:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a050d513-cb46-3c70-9f02-a5075fbe3a76 | -3.82563 | -47.73692 | 2025-08-18 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 537b39db-f832-3e0a-991a-10ba0b8a8e4c | -3.59562 | -47.52719 | 2025-08-18 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 473a2680-1a2e-3783-b50c-e0652857e258 | -7.54809 | -45.4391 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b168772-2583-311a-9586-47128f3d9f13 | -8.037 | -47.68034 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12909471-f63c-3143-92a5-00056e1ffb96 | -6.43498 | -44.7796 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a4bb5ef6-77f5-3939-b4f0-6a192294a31a | -8.79257 | -52.07298 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1c1c197-1139-37b1-8526-90f003ba1ac3 | -6.55707 | -44.4746 | 2025-08-18 05:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22cde47e-7c78-3109-83f1-1995a27df893 | -8.50614 | -44.74038 | 2025-08-18 05:12:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6234eca4-2f7f-3fbe-b38d-a68759938735 | -6.14035 | -57.93236 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3e00275-56da-3aff-b720-ec17a0c1754c | -7.51079 | -44.99029 | 2025-08-18 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57e4c8a9-08ba-3733-a522-962cc5d75030 | -8.21833 | -47.29812 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca6295b5-e3ba-3c74-af5c-ee3fe9d55809 | -7.0823 | -44.94168 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baddd1ee-d8cf-38d8-81d7-e844fed5449e | -6.12978 | -57.93425 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48403726-0c70-3cea-a07d-d73b6fc3fc72 | -9.39885 | -48.28719 | 2025-08-18 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d29efe91-e58a-37d0-bcba-28cb0e3a03a1 | -5.75717 | -46.66946 | 2025-08-18 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 232b3af2-9e18-3ea3-9ceb-039b1101ae3d | -7.54937 | -45.43409 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a63df618-c4f6-3e61-b325-0bd7d2a1050e | -6.19448 | -53.52073 | 2025-08-18 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c76903d1-15f3-3489-bc6e-41c847fe974b | -5.4903 | -51.15925 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba8da8ca-239d-3855-a5ff-4be3660675de | -4.29579 | -48.06475 | 2025-08-18 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 133c27d7-e9e8-368e-ae35-1fba7a978b42 | -6.43154 | -44.77913 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f809057d-a13e-3880-894e-19d649f79d2c | -8.22328 | -47.30037 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71e10877-c7a9-3e31-aefd-b30a0936d34f | -7.53579 | -50.53157 | 2025-08-18 05:12:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e34bbe-a707-3c2a-b9f7-3cb8e04147ad | -7.70245 | -57.74512 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91fb9a42-f6dc-3289-a694-cabdebad2989 | -6.79874 | -44.7264 | 2025-08-18 05:12:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84dcce04-7593-3b50-a2ac-d5e4048fe3c4 | -3.73449 | -51.8032 | 2025-08-18 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c45822c-e1eb-3aae-ae8b-643ae3ab4b11 | -9.87438 | -44.69484 | 2025-08-18 05:12:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e983867-7cba-3ba8-ae17-38cc95ff4436 | -3.73849 | -51.80381 | 2025-08-18 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc755c16-2829-3765-9fb5-6136b5d38873 | -5.45526 | -60.15274 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 958289d8-6f37-30a9-9c3f-dc9de106d134 | -6.43355 | -44.79062 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7d5f65e6-c3a2-3860-af31-629d4b23e6ce | -6.14322 | -57.92977 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9beabb1-1f49-3cea-8c0e-f1ca0902a308 | -5.45737 | -60.13764 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49425f17-bada-34fd-bc66-55562e7360a4 | -8.22991 | -47.29984 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15dfcdb3-bc38-3685-a01d-8023a435213c | -8.03751 | -47.67656 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df695a26-f111-366c-b009-30aa9dddeaba | -5.76302 | -46.67023 | 2025-08-18 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44cca870-9993-342e-ae53-b2537a8e10eb | -8.7973 | -52.07002 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b533f287-f35c-34ca-a4d3-c3a48dffe572 | -4.301 | -48.06551 | 2025-08-18 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7310639d-3401-34b8-9c2a-9393f4fce659 | -9.86741 | -44.69413 | 2025-08-18 05:12:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6a7e5f3-affb-32ed-be54-75f0069bf487 | -6.43227 | -44.77378 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4666544b-8f1f-3e32-8d50-83c6c8ec554c | -8.79566 | -52.08158 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a78f09f-9c60-38a1-a33a-e199d2441d7f | -8.22381 | -47.29622 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61925572-5398-3c8b-94e8-9159afe9e7ea | -6.43567 | -44.77422 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e484fb6a-23b8-3962-af62-0c82fb184c1c | -3.73768 | -51.80141 | 2025-08-18 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94b726f5-516a-3220-b63c-9b407ea5ed39 | -6.80122 | -44.73179 | 2025-08-18 05:12:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12f25b6e-5eea-3280-8c8e-f3ae8181aade | -7.51377 | -44.99351 | 2025-08-18 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a4e38b1-351d-340f-9406-85041fa524eb | -8.78313 | -49.99279 | 2025-08-18 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4432dac-8287-3afa-bab1-136bbf131d17 | -6.07693 | -57.92225 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83321d8a-9fee-33f8-864f-26d43f28462c | -3.82517 | -47.74012 | 2025-08-18 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a749a84b-3a46-31f5-b682-19c99244c5e3 | -3.41195 | -52.59948 | 2025-08-18 05:12:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c94ef39-a687-332e-9a6f-ce4b1bb462f5 | -7.55528 | -45.43464 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fe405c2-84a9-3030-9428-d5b531a0a3a1 | -9.39839 | -48.29079 | 2025-08-18 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a032cace-061e-3cc1-8ce3-fbbc99d4305b | -6.4241 | -44.78415 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 78e501a6-fcb3-39ec-b206-884c91eab05c | -9.39338 | -48.29321 | 2025-08-18 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0319ebd8-5222-35a6-a128-2fd249035258 | -5.45802 | -60.13611 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f767490-a9d1-3845-b548-01cba2385bb6 | -3.66635 | -50.95233 | 2025-08-18 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1870f2a1-c870-38a0-90fe-3d73e69c5913 | -8.82122 | -52.0536 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73f8e189-e017-3fba-8b77-2b3c48957acd | -7.54867 | -45.43955 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5502e19-c9f1-3fa1-a022-8d4c9fa3eb57 | -7.56873 | -45.43706 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7f3fb17-f21d-301e-a794-9dd645c25a41 | -5.45803 | -60.13348 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d0387d9-b5bd-3a09-b71f-a7a81618ad19 | -6.49522 | -53.38795 | 2025-08-18 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 672f42c0-874f-35d4-964c-8165926a340b | -7.50494 | -44.98358 | 2025-08-18 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d06bb723-b697-361e-bc84-6bf532c614e5 | -9.17877 | -49.66934 | 2025-08-18 05:12:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0aafb96d-ec40-3aea-9b89-6d63ec0eb16d | -9.87513 | -44.68852 | 2025-08-18 05:12:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95db75d5-004b-39d7-aeb0-4fd84d9e5ba0 | -7.51441 | -44.98853 | 2025-08-18 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ee7c2a2-856e-3a5f-bb68-fd19e607ba53 | -9.39289 | -48.29676 | 2025-08-18 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dee6b8f6-bb9b-3076-8a96-f84fb0324324 | -6.19514 | -53.51627 | 2025-08-18 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1a2564e-a638-3b8d-b8ca-13bf8600bdc6 | -8.20135 | -47.33664 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9775dc4-1620-3ef9-b217-a69cb7f12511 | -8.81918 | -52.03764 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b40b30ff-4ebc-3158-90a7-76b75034516a | -6.5503 | -44.47367 | 2025-08-18 05:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 929a3a11-dacb-3927-939d-eabae7eb1c85 | -4.91856 | -43.23393 | 2025-08-18 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f125e798-8f67-3ef1-93d3-e34835ce272d | -5.50469 | -49.21922 | 2025-08-18 05:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a511acd-5dee-37cb-aaa8-b5ec071f68a6 | -4.9176 | -43.24086 | 2025-08-18 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 036e1e6f-e9cb-31e3-8810-7e42b7e8dd5f | -9.39195 | -48.29718 | 2025-08-18 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d509c295-0dcd-39a4-bb3f-33aa39142c12 | -6.13701 | -57.93182 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef8fb589-cbda-37ab-b6ca-287c74695018 | -7.57519 | -45.43798 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
