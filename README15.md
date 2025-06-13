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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f0126c6-033b-37a7-8dee-e6e7703c927a | -11.17956 | -46.87893 | 2025-06-13 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5008b9dd-930b-36be-9a61-0b62ad1954fe | -6.15519 | -47.27075 | 2025-06-13 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25b53d62-b01c-30be-9331-194dcd752041 | -8.59299 | -45.86276 | 2025-06-13 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc69ac67-b27f-346a-b1dc-0f00f798b387 | -9.40137 | -48.42189 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1fb4437-0b06-306d-bdba-6db45b2356d9 | -10.36392 | -57.23566 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ba8bb6a-41b5-38dc-b62a-35e981ba1b85 | -9.21885 | -62.46873 | 2025-06-13 04:32:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0a00485-32b2-3e51-89bb-ab4f3b22ec22 | -11.12818 | -54.21583 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da06f00-b2d6-3ec9-aa27-be85310fff1e | -6.94671 | -42.89193 | 2025-06-13 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| edb40d07-00e2-3e88-ac29-b0fb5f394d1e | -10.64575 | -44.47987 | 2025-06-13 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7cb61ef-2581-3c44-adce-aa4865525ded | -12.05566 | -48.07371 | 2025-06-13 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bb1dec3-c608-3873-a855-5c588f4f8bf1 | -9.41129 | -48.42348 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6f9e4bc-820f-3ba4-a394-e0c2da6598a9 | -8.81668 | -46.99022 | 2025-06-13 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e1c3d32-3626-3fcd-9d0f-f6d4d9d91d4f | -11.74211 | -54.71777 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f027edb0-8028-30a0-b5ff-e43ef12f4f7a | -9.68221 | -56.99173 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6982346c-9e2d-3f3f-919b-5485a525e429 | -11.36879 | -56.55742 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3afc902a-fe95-395d-a048-19902d45c030 | -10.36484 | -57.23715 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ee94003-38ea-3fce-881e-96f5db3fd244 | -11.93444 | -49.48081 | 2025-06-13 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 676af1f4-c8f7-3a6d-9848-d6d227154d02 | -10.80687 | -55.87476 | 2025-06-13 04:32:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d001fae6-440a-3b90-8de0-654705676a6f | -10.63033 | -49.4339 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4eb843b-e776-3c8f-aa4f-34faeacd856b | -8.46736 | -47.14236 | 2025-06-13 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac4a401a-74f1-3e4f-94dc-2809102946fc | -8.87755 | -48.51294 | 2025-06-13 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 129fbe05-e2dd-39b7-a241-e752c0af4080 | -8.96618 | -47.97076 | 2025-06-13 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23084c75-5e69-3a2e-8381-f4525120558d | -11.7878 | -54.78064 | 2025-06-13 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d98a36-835e-3ac4-861c-ae70a11918a8 | -11.14195 | -53.92132 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fe45294-5ba1-384f-905f-1f1be1f5e250 | -9.39976 | -57.55218 | 2025-06-13 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2df2bed0-4f65-362b-9bf7-93e47b97c9ee | -9.25175 | -57.53387 | 2025-06-13 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ae865f7-0c09-3fad-b006-099b79ab08da | -13.28819 | -48.20436 | 2025-06-13 04:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f834bedd-c913-3df6-bdf3-dabbf10b8116 | -6.94015 | -44.56555 | 2025-06-13 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 851bf0ad-a0d5-33b8-b700-42bf03e4cfa8 | -10.64918 | -49.42252 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ab620ee-cec6-3e40-8954-2fe03deeab04 | -8.07354 | -43.11472 | 2025-06-13 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| a49a3a9c-77a7-3287-a3d8-90d9e1382cd4 | -9.8432 | -44.69432 | 2025-06-13 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8293234e-1c86-3bfa-ace1-ceb718114423 | -11.87297 | -52.29707 | 2025-06-13 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9de6ac3e-5605-3ea2-b2d4-d745820eba00 | -11.36784 | -56.5627 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ddfe18-30e9-30ac-b198-66b21a404c39 | -9.40799 | -48.42295 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 596713fa-cc5f-3d9c-a079-0b6df11696c7 | -11.36973 | -56.55218 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07e97114-0828-3436-bf00-6eb9af2255f8 | -10.69882 | -49.49571 | 2025-06-13 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e02653d0-b934-36cb-b0ad-9f00973eb6aa | -8.07759 | -43.1153 | 2025-06-13 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc7759c2-654b-303c-a965-0da98e208a82 | -9.68329 | -56.98592 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dc33545-1dc8-3bd2-8cea-7a28c000ff5b | -9.67059 | -48.76131 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0693881f-b8ad-34e0-98b1-d484a131d7ef | -10.64975 | -49.419 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 466fbdad-a88d-3a8e-a429-acb34a4f985f | -9.84498 | -44.70869 | 2025-06-13 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e14e5d97-841e-3e42-9d22-88f568b1e22f | -7.82923 | -50.62159 | 2025-06-13 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aa69ce0-d824-38b3-893f-e463d9eb14b1 | -13.11713 | -44.07411 | 2025-06-13 04:32:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fbc60c7-bd2e-3eaf-b5d5-2bcfbf329021 | -10.86616 | -54.30625 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47761006-ad11-3de3-af39-13f50987ae51 | -10.64862 | -49.42603 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de79bf07-4884-358b-a90e-6e0565f6207e | -8.07811 | -43.11171 | 2025-06-13 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 42756a1e-3dcb-3f8f-bda3-fdbaf26683cc | -10.63754 | -49.43145 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fa8d2e12-7075-3966-b0b2-c8aef0411ea1 | -8.95194 | -47.27558 | 2025-06-13 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 631e7334-afc2-3e8b-808a-16875ad18722 | -10.92862 | -56.83559 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b30dd3b0-d73a-3344-9c2f-dd7bd651c79d | -10.65274 | -44.4859 | 2025-06-13 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 970ed31f-4d05-3f3a-9dc2-38e24c1e7d16 | -10.86681 | -54.30252 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 406a175b-ead9-3a93-b019-d9044878a83a | -10.6559 | -44.49132 | 2025-06-13 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d971c9af-18e4-3033-96d6-021ea9b05cdf | -7.4502 | -45.50584 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53476f51-fc96-38da-98a2-ddc12ee01911 | -8.31242 | -47.91708 | 2025-06-13 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35797c03-1061-3a7c-9e5d-7a5578fa01df | -11.79616 | -43.78925 | 2025-06-13 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59ea1f6f-9763-3966-910f-bfb057df0e8b | -8.59239 | -45.86675 | 2025-06-13 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aefac31f-6290-3dc0-8d3d-93977e230b1a | -11.13225 | -54.21658 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 186976c2-318f-35c9-9f97-41890eaa387a | -12.13228 | -54.66889 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7162243-779a-3542-af93-953a4c48a359 | -10.36646 | -57.22821 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5778b8c-f0ef-3574-a1be-47fb47bfbe35 | -6.94444 | -44.56184 | 2025-06-13 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4191464-ce03-3b53-8e0c-06fc86125b31 | -8.09412 | -47.57523 | 2025-06-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c86f6d14-79fb-3003-bede-eba54ff27e76 | -11.17612 | -46.87839 | 2025-06-13 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9af09ca4-a9df-397b-bd3d-181fcd942b87 | -7.45253 | -45.51425 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b810b0c9-3f8c-335f-9694-3b815f20073d | -7.46186 | -45.52372 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b0e7fe5-5939-3ac8-93c5-d05045b7bfc1 | -7.45662 | -45.51088 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f998014-3ae4-3a56-954f-1f709a856f12 | -11.17269 | -46.87785 | 2025-06-13 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 425d1598-409a-3123-930a-300722feabbf | -11.58639 | -51.33686 | 2025-06-13 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cf5202a-b83f-3a4b-8760-681e0380e8db | -11.56424 | -54.5671 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 684ce441-843f-38cb-870c-bf5b74224875 | -8.07735 | -49.85772 | 2025-06-13 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8287e473-a2c1-3b9f-9812-d0259c981f6b | -12.13667 | -54.65795 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a03d04c8-9c82-3749-ab74-f5158e81afa4 | -11.56771 | -54.57164 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9fbc42e7-dd4c-3bc9-89ee-1f3f4caf91d4 | -10.64198 | -49.42495 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3b87accc-4e77-3e73-b610-150df63d0e1e | -7.46013 | -45.51142 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b526010-102d-3240-a7fd-0f4d0908347a | -10.65307 | -49.41954 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32d8de3a-3a0d-31ac-9321-ffbe88e74c71 | -8.09084 | -47.57502 | 2025-06-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d69593e3-2b34-3a55-8ca8-070be2c04081 | -9.40689 | -48.42991 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9e75930-4ac2-3c65-b9e6-4306b8dfb5ae | -9.12072 | -46.92995 | 2025-06-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 317766b0-21ac-35bb-a213-66aea1beff57 | -7.69625 | -45.78486 | 2025-06-13 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17a14e45-1141-3614-b444-fb87e3870b46 | -11.81473 | -54.49952 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 945bf7fc-0692-3e22-ba2d-0e9574279e1c | -10.64587 | -49.42197 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| be595b7b-abad-3728-bf2d-71592d9d1d3a | -10.36505 | -57.22969 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76c06165-7941-3734-a1e2-96feefeddba8 | -9.64717 | -48.5644 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3e0aec6-410c-3ceb-9ff3-4f2c9c2611b1 | -11.56291 | -54.57468 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8fbb4392-f99f-3369-b042-32fd33973bb6 | -11.74696 | -54.71466 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27e46de8-1163-3548-a58f-9e8471e2fae8 | -11.73762 | -46.96151 | 2025-06-13 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7b7edda-12a5-3372-9d24-28e77448e603 | -11.80997 | -54.50251 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b4f46e5-2b5d-3d65-a604-f68033267949 | -8.06949 | -43.11413 | 2025-06-13 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| e2bd54c6-06fe-3736-9558-e3e11abed737 | -9.87829 | -46.27644 | 2025-06-13 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 984ac3dd-a63b-357b-9684-8e55dbbcb730 | -9.66948 | -48.76829 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 521778e9-418c-3995-beda-7552ee292cdd | -7.86515 | -47.88902 | 2025-06-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db937aec-2821-3d2a-ad63-90dd3694c26c | -7.45603 | -45.5148 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f71fc2f-6bdf-3863-a62e-fcd2e232edeb | -12.00458 | -45.12964 | 2025-06-13 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 37b54fb6-7920-3a29-8396-735fa5d56f53 | -10.79426 | -48.46188 | 2025-06-13 04:32:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7aa3c341-35a7-30c5-afc9-1c13b5a02a84 | -11.01351 | -47.76777 | 2025-06-13 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5868d629-bbe9-3b00-a399-d0c8acada836 | -11.5774 | -44.85037 | 2025-06-13 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a123d34-e960-3f57-8011-6b66f8c3e4a4 | -7.79928 | -40.55188 | 2025-06-13 04:32:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0c0f2cb4-53ee-3a7e-84c4-7c2638eed79b | -10.02144 | -57.32689 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31b33703-36ed-326a-9269-d63b7dfce96f | -11.12963 | -53.94477 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06a25c59-c4a5-334f-8aea-a25ac9bb82c0 | -10.85277 | -53.77946 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3926ea2c-74d9-3851-83be-653ea19c81e0 | -11.13795 | -53.92063 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README16.md)
