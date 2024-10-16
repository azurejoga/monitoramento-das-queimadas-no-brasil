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
| 6ecd9ad1-3ef0-3c31-8fc6-a21f37b222d0 | -9.20879 | -47.94574 | 2024-10-16 01:00:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f6264ecf-d682-3ff6-a473-9ae61275793a | -9.19971 | -47.95291 | 2024-10-16 01:00:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 532ca9fe-4e40-3ed9-8651-fd6c70cdf11a | -9.0932 | -47.78207 | 2024-10-16 01:00:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f323bd10-899d-37fd-bc4c-d9e658bc5736 | -9.01894 | -47.45782 | 2024-10-16 01:00:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 6568b31b-602e-365f-ab73-f0ebb60db1cc | -8.9246 | -47.06166 | 2024-10-16 01:00:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 124f0ffd-03e9-37c6-b757-f9459c74b779 | -8.92318 | -47.05191 | 2024-10-16 01:00:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8af29476-32f5-3555-8bb2-eab2ef766f4a | -8.90827 | -47.91207 | 2024-10-16 01:00:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d744b18-708f-3f4d-82da-17f4d7459d34 | -8.86624 | -47.55023 | 2024-10-16 01:00:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ddff9c1e-7993-3902-ba11-ee00c9a156f8 | -8.84694 | -47.93045 | 2024-10-16 01:00:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bf1c412-b8dd-3f75-b493-d1837f4610ca | -8.83466 | -49.88896 | 2024-10-16 01:00:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f38812c1-c330-370b-afe4-47d97a5b4417 | -8.80086 | -47.86848 | 2024-10-16 01:00:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ee48d0e3-12d7-32ac-ae35-bf2e8ec79bff | -8.79955 | -47.85928 | 2024-10-16 01:00:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dc4a0fc-f41d-3371-a216-f86406d49de5 | -8.67996 | -47.08642 | 2024-10-16 01:00:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b1c064f-669c-36f4-a2b8-d6978540f650 | -8.48704 | -47.02727 | 2024-10-16 01:00:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| daf348b7-b622-30d9-af40-7a1b1f477954 | -8.48563 | -47.01742 | 2024-10-16 01:00:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a770b2c2-2ab4-32b4-a4c6-9a85186a08a2 | -8.47777 | -47.02871 | 2024-10-16 01:00:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 733d4608-ca22-37d4-a321-62d600af00d5 | -8.39665 | -48.92678 | 2024-10-16 01:00:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 096e906a-c0ae-321d-9419-b2c47f9209e3 | -8.22234 | -46.80351 | 2024-10-16 01:00:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f05223b-e89e-3036-90ff-de899e0c58f1 | -8.13823 | -47.03334 | 2024-10-16 01:00:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 373142cc-4322-36ad-a0c0-342f5b3ecdf3 | -7.85562 | -46.26364 | 2024-10-16 01:00:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8ad4739a-9797-3e4d-918c-9d70426162b2 | -7.85398 | -46.25266 | 2024-10-16 01:00:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 09480c9c-b76b-3150-b16a-d262d6c57242 | -7.85256 | -46.25883 | 2024-10-16 01:00:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 735d2ea7-3616-3e43-92a9-2888e1e1eedb | -7.85098 | -46.24782 | 2024-10-16 01:00:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 78160694-815f-310a-83df-e2db1655e656 | -7.63972 | -47.16851 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 987eb34d-5b29-3f54-a704-6ca2903f9a1d | -7.63904 | -47.22894 | 2024-10-16 01:00:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97619fe8-a79b-3494-b205-11409697af16 | -7.63828 | -47.15861 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f8663e6b-20d0-3698-a793-b332a5a14dc1 | -7.63042 | -47.1699 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c11256c7-6a3d-33d4-b946-bbd8ca79f892 | -7.60567 | -46.80291 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a58cba55-b2f0-3ed8-b097-2d42dd58f327 | -7.60219 | -46.84538 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d450a30e-fc68-3b7d-b312-a6a43de6b8b1 | -7.60069 | -46.83513 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff429449-c942-3c42-b605-ae0e2400ed2a | -7.50343 | -46.86614 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4051d0e8-f86e-3ff6-afdf-29feef83dcea | -7.22375 | -45.6034 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 4dd21b00-6df0-3d4d-a8ad-f8fe25fe8467 | -7.22191 | -45.59118 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| b1e7c732-f5a4-3042-9e19-616063e808f8 | -7.15908 | -46.54052 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 865d3616-2f83-30f7-b78e-1d873fe9b558 | -7.15748 | -46.52976 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a5e9479b-2c7f-3bcd-8c1c-02007fba9795 | -7.15097 | -45.04901 | 2024-10-16 01:00:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 48f1a351-2406-3ac6-8444-ba74fd013fe5 | -7.14895 | -45.03559 | 2024-10-16 01:00:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2f29b6a0-28b3-3004-bbba-04695f84ac4a | -7.13894 | -45.72181 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1cced729-aa40-3ce0-aa31-2571c7900e08 | -7.13768 | -45.43078 | 2024-10-16 01:00:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7ababd18-ef05-3783-8464-953b7ba36d65 | -7.13594 | -46.53881 | 2024-10-16 01:00:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 55bab57d-f379-32b1-86c3-d8942caaf95a | -7.10112 | -46.77112 | 2024-10-16 01:00:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bcd980fa-2735-34cf-a8a4-a19007a14f22 | -7.09769 | -46.77801 | 2024-10-16 01:00:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c8b9e7ab-b2ca-32af-b494-4172eb8a4bde | -7.06148 | -45.53876 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3da80de1-62d0-3c16-96a8-5bf798f198d7 | -7.05963 | -45.52626 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 35501ff9-15fa-3482-bf9f-c9cc35d2ac81 | -6.91196 | -44.3818 | 2024-10-16 01:00:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4e8b1a6f-ea15-3660-aae2-a9131b18c929 | -6.90458 | -47.31667 | 2024-10-16 01:00:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 01ca0cb2-3ed1-3a04-9ae3-6e727f1c9717 | -6.89892 | -47.32343 | 2024-10-16 01:00:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7e9f89eb-b85c-3bdf-a1ed-71d14cf6a6f7 | -6.89751 | -47.31351 | 2024-10-16 01:00:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 91d77eaf-77d9-346a-bb2a-a2f82eadeee4 | -6.74627 | -48.06934 | 2024-10-16 01:00:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bbafab71-d383-3781-af28-318e3da858fa | -6.68365 | -49.19911 | 2024-10-16 01:00:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 245de31e-b05a-32d4-bb54-52528f1c8b69 | -6.67335 | -44.71014 | 2024-10-16 01:00:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e6671275-f0ed-395b-a122-289ec122e829 | -6.66643 | -49.46295 | 2024-10-16 01:00:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4a90a278-1068-3eb2-95d7-4eac4470407a | -6.53987 | -44.43296 | 2024-10-16 01:00:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 489c39cf-e525-37d8-850d-f30ebcf66939 | -6.53756 | -44.41748 | 2024-10-16 01:00:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 439a8c53-b0e5-3c47-9415-8d742619c42a | -6.52618 | -44.41938 | 2024-10-16 01:00:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d22f78df-027a-3cb6-a5ed-3417e3829493 | -6.49773 | -44.15121 | 2024-10-16 01:00:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 11b98816-a55a-3e21-b75c-1409ba9993e9 | -6.45407 | -45.86325 | 2024-10-16 01:00:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a28b95b-045f-3b42-b164-e36ce2438232 | -6.18595 | -44.528 | 2024-10-16 01:00:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d26ffe7b-6b33-30ec-a569-76032e78080d | -6.1697 | -49.07727 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c625ccfd-13fe-3fc8-9ecc-6d1177f492a3 | -5.69696 | -44.49061 | 2024-10-16 01:00:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ddf69191-6c8f-3d44-a1f1-5a7b587e6375 | -5.68547 | -44.49249 | 2024-10-16 01:00:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ecc1f8c3-24cf-3a0e-a659-1222a63e4aa1 | -5.60861 | -45.2063 | 2024-10-16 01:00:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4b1d9d45-4c97-3f3f-a152-1c5cc9925713 | -5.60654 | -45.19247 | 2024-10-16 01:00:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d5869663-ae5e-39af-beec-7bf575051095 | -5.58412 | -44.89025 | 2024-10-16 01:00:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc8408d7-8af7-38d4-8689-e7b80ced5277 | -5.58198 | -44.8758 | 2024-10-16 01:00:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a693a784-962d-3120-9f75-85ce2c34db7a | -5.52093 | -46.91045 | 2024-10-16 01:00:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5a0c073d-224f-34d0-8390-6a408fdd148b | -5.51939 | -46.89973 | 2024-10-16 01:00:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 12dfbc9e-b96e-3189-abaa-6f07d24ddc0c | -5.51921 | -45.39977 | 2024-10-16 01:00:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3ffad748-3fc4-3bcd-af81-8740e417962c | -5.51164 | -45.39521 | 2024-10-16 01:00:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dea0da6c-ae9b-3950-ac70-768a9e1d150c | -5.51126 | -46.9119 | 2024-10-16 01:00:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| bdf66560-2849-3a9d-bdbe-c7bc3061f859 | -5.50971 | -46.90117 | 2024-10-16 01:00:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f7ec4a50-52e3-3ca8-bfb3-cffd3fd87194 | -5.16494 | -44.01245 | 2024-10-16 01:00:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| dbb67150-8152-346c-b97e-b4e5d707700b | -5.15287 | -44.01438 | 2024-10-16 01:00:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 05dba657-5ee2-3428-be24-302ea5e4d64d | -4.53396 | -43.48547 | 2024-10-16 01:02:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 421a62ab-6926-3a47-a943-c2a1b227e55e | -4.5212 | -43.48741 | 2024-10-16 01:02:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ad6cc10d-00e5-3d5a-9241-f799f3c2f92a | -3.66493 | -42.27336 | 2024-10-16 01:02:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| c8e465e6-d60d-39fc-85d6-09fd2c264063 | -3.66202 | -42.28035 | 2024-10-16 01:02:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| cfdaa947-99a0-39d5-8825-429a901f7ec0 | -3.65829 | -42.25506 | 2024-10-16 01:02:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 13f7a853-ecd6-34f9-a320-1eb836da930e | -3.51561 | -43.2473 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d10ee12a-25e2-3b85-a715-bd6477b3cfcf | -3.51246 | -43.22588 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 84246420-74f8-3ffa-9a01-a17b18464111 | -3.50236 | -43.24932 | 2024-10-16 01:02:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ae1fba5a-dcb3-3bdc-a49f-62bf9ec263fa | 1.30929 | -51.24708 | 2024-10-16 01:02:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c5d3671-ab48-36df-bfdd-7a45986a2b51 | 1.11513 | -50.97777 | 2024-10-16 01:02:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5a611994-aa33-3925-af00-d704baa3039b | 1.00687 | -52.21792 | 2024-10-16 01:02:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 382a3a81-f6ce-3a04-b796-47b68100ec73 | 1.00559 | -52.22703 | 2024-10-16 01:02:00 | TERRA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ef90e81f-ea6b-320a-8f8e-fca657118641 | 0.2587 | -50.84698 | 2024-10-16 01:02:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec5e2e29-08f0-385b-8ede-92e380cd6f2e | -5.40314 | -49.20595 | 2024-10-16 01:02:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 230ae34d-2dd7-3752-bfdd-8bc0d0debc63 | -5.4019 | -49.19708 | 2024-10-16 01:02:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 266ca96a-bd0c-338e-8acc-7c4365fb75da | -5.35159 | -50.61774 | 2024-10-16 01:02:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 436bf6b8-30cc-359b-bdc4-dfee77b709ec | -5.33555 | -48.72298 | 2024-10-16 01:02:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f4c812c1-5304-3508-9b69-687011fe5bac | -0.53865 | -51.86269 | 2024-10-16 01:02:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| deaa6aae-eb4f-39f6-a103-c5499b628dd9 | -0.76893 | -48.69401 | 2024-10-16 01:02:00 | TERRA_M-M | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d0de1767-654a-31c1-a711-e35db5ce0776 | -0.7703 | -48.70373 | 2024-10-16 01:02:00 | TERRA_M-M | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3be8da19-59dc-30ea-9624-3dfd0de29fb4 | -0.86386 | -48.71425 | 2024-10-16 01:02:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 470db341-d760-3777-b931-ad45812f5910 | -1.11843 | -53.70904 | 2024-10-16 01:02:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a1824bac-b352-3cba-8237-7297303711e9 | -1.43647 | -47.40965 | 2024-10-16 01:02:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a501c31c-976a-3d93-b48a-6a380e4d7e56 | -1.48657 | -47.32713 | 2024-10-16 01:02:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 54c224b9-ed40-3579-ad85-d8f9dba45faf | -1.48818 | -47.3384 | 2024-10-16 01:02:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d5734140-b718-33c0-a981-42f3fc69c42c | -1.49017 | -54.31927 | 2024-10-16 01:02:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 595abd90-e68e-3852-af49-507566f36820 | -1.56075 | -48.01642 | 2024-10-16 01:02:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README13.md)
