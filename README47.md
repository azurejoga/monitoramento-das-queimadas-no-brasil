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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eceeee03-5d07-3251-ad44-5d25157ac2b5 | -1.60987 | -53.82757 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6d14956-0ae9-33f6-8dbf-0410fa01ae6c | -4.02484 | -49.93282 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b93b5c73-efb3-342d-a875-b31865471eaa | -2.88807 | -54.16241 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04754c1e-18b7-3605-91f3-9e65ca2ab004 | -4.26084 | -47.60821 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd955198-379a-33c4-96f4-a4380e44057b | -1.23836 | -46.02805 | 2024-12-01 04:44:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 548118f1-6040-3014-ad8b-23dd1a1f6556 | -4.12444 | -54.20738 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c33751f9-b81f-31cd-992e-b88ee860d039 | -3.43305 | -54.11295 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f46ad9-337f-3b5e-bd46-0b2979d75746 | -3.09781 | -54.13266 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 432aab26-b1f4-327a-8814-c551bcd5410a | -2.26915 | -51.91275 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c6138f1-0aa1-30fc-8f19-c46411fa09e0 | -2.53637 | -53.998 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7293887-97ef-3ea4-ad5b-1f68c5087464 | -2.44178 | -53.62852 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a51950d-ce34-30d2-aa82-7e41a014d4e1 | -1.24861 | -51.73739 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 472aee1b-6a47-3444-915d-3be9955eab20 | -3.26974 | -48.77244 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5ec66b0-114a-3286-995d-e111b8404c49 | -4.06919 | -49.0637 | 2024-12-01 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6489ef3-97c2-3519-bd96-a27229c8c35e | -2.31164 | -50.69163 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6125af18-3bf1-37b3-acab-b166c38ef6b5 | -4.26442 | -47.60871 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| effebcfe-7a73-3fd0-b690-bac00820b8a3 | -2.63342 | -51.7508 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a209065-8d43-3ef8-8c35-c9021fee6d7d | -3.78813 | -46.70161 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1738512-0c65-3caf-9f04-32fa4f4a6408 | -3.23277 | -53.63238 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d3eb41e-069f-3961-a427-415eb6a7de61 | -3.26575 | -53.63764 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6e6efe18-29c1-3c27-a684-3b56c05a4785 | -3.85002 | -40.98531 | 2024-12-01 04:44:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| e17e8c96-06d4-3d86-afa6-44e9402938c7 | -1.14629 | -48.33117 | 2024-12-01 04:44:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fb36051-4a69-3228-8f78-2e7159c7a1f9 | -2.42698 | -50.43289 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227117f5-ff76-3d38-b34a-d9ea7cf59648 | -2.36593 | -50.43393 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 745f19af-461a-3d30-b9a2-f58f39b61ae0 | -2.77666 | -55.34618 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b05aad0c-d486-388e-a528-85ea29b12943 | -1.32742 | -55.84764 | 2024-12-01 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 571873b1-edff-3649-b989-2be5247a6ed6 | -4.53024 | -45.74202 | 2024-12-01 04:44:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fc30ee7-4708-363c-81fa-28d59511e8e6 | -1.1115 | -52.30468 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3358624c-7f92-3563-9beb-6fe49ca9e370 | -2.75176 | -51.66498 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bee7df17-adcf-324e-8418-e60bb9467cc5 | -2.63544 | -54.22399 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42f482c1-e10e-38cc-87c0-6e54982ab96d | -2.8328 | -54.09861 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 580843b6-44c9-3861-b3aa-34a6bc8558c2 | -3.24376 | -53.63417 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c49cf214-9285-3a92-a302-1da9130e6a36 | -2.624 | -54.22205 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62a50b73-05ba-36ae-9f89-cd929dfb0026 | -2.78252 | -49.83154 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63f5b888-af29-3d7b-b3cc-ed2a36699825 | -3.35905 | -50.51196 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9c70f94-f46e-3ef7-9623-5076eb7663e5 | -2.26287 | -45.51737 | 2024-12-01 04:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c819608-2402-3c2c-983b-2549c80f41f8 | -2.0261 | -52.0821 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d83d397-a75b-3210-81db-019ff26540df | -3.59979 | -50.38031 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ac8e58a-af1b-37f5-9de0-62ad759fd40a | -3.39652 | -50.31265 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f0b322b-73ee-3de8-b76b-f70a150c1b8c | -3.9487 | -48.16927 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99b80619-1599-3b05-bfaa-5dee378fd6a5 | -1.33241 | -55.84422 | 2024-12-01 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb506d26-a837-36d2-8762-68af4bacc5ec | -3.60347 | -50.37368 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25f93040-bd28-32f2-9ca7-e6886b739fb7 | -6.92229 | -43.54239 | 2024-12-01 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d1cdd7ab-1904-3831-a683-82944680f73a | -1.60609 | -53.82698 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7f14a7f-d578-3437-885b-aa56dd1180c7 | -3.46828 | -50.2673 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ef6435e4-9801-3163-bfe1-5664fbeff018 | -2.10367 | -47.62785 | 2024-12-01 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf7dd32b-5dc8-34ea-8060-277446992708 | -3.29357 | -53.83036 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0debb228-4820-3df3-b008-485cb51e9d4c | -3.32774 | -50.19253 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 35bc4e45-95df-3157-b86e-4b73e611145a | -3.05148 | -52.7622 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a6016d6-6a3b-3d77-af8e-0515bdb271ee | -2.06582 | -51.19244 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b78d536-aa06-35ac-b988-52d9aa84e358 | -0.99888 | -51.77656 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a69465e-dc89-3382-b336-74b0c732b074 | -1.32132 | -51.74498 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c722b993-6f82-36c0-882d-9f5d521200ba | -2.43452 | -53.88589 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09ac63c5-00d2-3b6d-9fdc-bba92c0fdb46 | -2.62781 | -54.22269 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe24a672-5b37-389e-ab61-24ab36c36da1 | -3.99568 | -46.50229 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13cbac83-f14d-301a-8e93-b4ed4ba9f9c1 | -2.31932 | -50.64302 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2fee8ce-54aa-37c2-a179-13d5ca59ca34 | -2.98904 | -53.35992 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49ac0a35-89dd-3dfc-a626-4eaadba0e1cb | -4.45873 | -56.18122 | 2024-12-01 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a205ebc7-34c2-35ef-9ba3-faef913dd763 | -2.8411 | -49.88645 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d688bd90-8388-311b-84c1-871f9d7cd600 | -3.28659 | -50.51832 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc7ee730-277d-3e1c-b5b8-ea0d19b9d378 | -1.04898 | -51.74157 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56d72719-a56e-3684-b1a0-8329404aed7f | -3.69744 | -50.16559 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27731406-8e83-3454-8da0-03b0d0858dd7 | -4.00295 | -54.61622 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17c0aa3b-557d-3650-9e37-6a2221e5d9f2 | -3.15441 | -50.6251 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 561f182f-156e-3ad2-aa7a-a4b8620a18f2 | -2.95583 | -50.57589 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33a2b580-7280-3c6f-af1a-304b4e588751 | -4.06975 | -49.06012 | 2024-12-01 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d653b875-f7f1-3dab-ad66-fe2e68b1e068 | -2.12256 | -46.56512 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5dd0441-bac0-3951-91ea-902adc4ac2b7 | -1.62326 | -52.69127 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1b258be-ba1f-3aa7-b950-ade0cd51d77e | -3.65947 | -50.23394 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 939d66cf-685a-3005-a7aa-360420ec5ef6 | -2.8438 | -54.03049 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73dc340e-6795-3279-9a39-f6c48cd46be7 | -1.8987 | -53.01841 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baa0006d-16a9-3fff-aa8d-93e375a3edae | -3.76677 | -50.17641 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32dddb67-da1e-3e83-81e6-6615cfc886b4 | -2.73419 | -54.13713 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64baffb0-4efb-33f3-b435-6b43d8e2a40a | -2.6195 | -51.81583 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eceba572-dc5a-3eba-968f-04f593208b33 | -2.74858 | -51.66121 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46d0dba9-b10f-3482-9251-270d71c94358 | -4.02009 | -51.01675 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03dcef48-22de-317c-8f11-f43aa3476c2f | -1.49722 | -52.60383 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80c34441-2162-3dd6-b1c5-e44fef319265 | -3.7102 | -53.75132 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 196109f6-905f-3484-bd4b-1afce4dcad7a | -2.57799 | -55.99424 | 2024-12-01 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 113665c2-c8b4-35d5-8b9b-64928ca62816 | -1.18533 | -51.76624 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ca48d81-c1e3-37db-8aa6-c778272f09b3 | -1.27592 | -52.70602 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42dca353-60cd-3593-8f4a-8dba47ffe327 | -3.62485 | -49.85324 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1fdada21-152f-3352-a3da-ea149eda5891 | -4.3429 | -50.77257 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ba03e34-1212-32c3-a31c-cb165a046113 | -4.04304 | -46.93254 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 11df414c-93f2-3c8e-8f37-e8e01faa1d21 | -2.4662 | -46.57538 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7f1821f-e9a2-3d4c-b648-20e7e99ed894 | -3.73915 | -45.46866 | 2024-12-01 04:44:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0329afdb-8f29-32f8-bf30-862bf33e7ee3 | -2.86986 | -53.98835 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7c8656a-5faf-3997-a801-b1d18c541d65 | -3.65917 | -50.70788 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8db877c-319d-3e38-a69e-a0cad4cc7243 | -4.34412 | -48.12551 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9517159-edb0-34d2-a743-440625f05968 | -2.75484 | -51.75447 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc2a4a36-8125-3641-89c0-e2955f71e02f | -1.8242 | -50.90519 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 049c811f-0bc9-3807-bfd4-44cd820fb769 | -3.76643 | -47.71427 | 2024-12-01 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57269005-febe-31db-8f68-39f4e8ed26b5 | -1.70387 | -52.64258 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ae2ae35-5af4-387d-9b05-152762085ec3 | -1.45277 | -48.20396 | 2024-12-01 04:44:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 169ae444-303e-3cbe-b6d5-0a693bbdb68a | -1.25533 | -54.55035 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76cd1962-930e-319d-bd0c-2d7bd4be7859 | -2.52383 | -54.07619 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 822d7bd6-2256-3606-9979-57b0e645d1a1 | -3.72853 | -50.20581 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 582cd670-bc60-30f8-a1af-5227c04c4888 | -3.28208 | -50.16062 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20c9b583-0540-3954-b843-729265ec3ede | -1.47642 | -55.38194 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84cacb8c-be0f-3e49-88d5-a1e2f5f8675b | -2.57704 | -51.8845 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README48.md)
