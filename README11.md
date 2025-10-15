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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f64e476a-9da8-3489-94a9-494472f6c916 | -4.15019 | -44.19007 | 2025-10-15 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecb96903-05b8-3ba4-96e2-2333ff308a4d | -0.89323 | -47.54737 | 2025-10-15 03:45:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00eadbb0-eba8-3a1f-9853-41a9a562370a | -3.05111 | -44.4637 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e31fca3-6261-361b-b3f5-69bcd3c40f13 | -3.56308 | -43.50923 | 2025-10-15 03:45:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f00e695c-550a-3521-b266-fc86664a20b7 | -3.05576 | -44.48035 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33b0e420-a406-349d-8351-61cd9764e903 | -3.05709 | -44.47266 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8ccd01b-6190-32e9-a7d3-f80b41b1a080 | -4.41955 | -42.90014 | 2025-10-15 03:45:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 433e101e-dcd5-30d7-aa09-5bd3d1e36f32 | -2.92248 | -48.31136 | 2025-10-15 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a4b104ca-061a-3720-801e-4480c61447ad | -4.1447 | -41.66184 | 2025-10-15 03:45:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2ceec46d-c7c7-3123-8b26-6c7711ae8d97 | -4.14014 | -41.66076 | 2025-10-15 03:45:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e8c10841-b0c5-3595-99f4-6ac563b7791e | -3.56207 | -43.50917 | 2025-10-15 03:45:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a080e5c-f50e-33ab-9c2c-9a99f18ba867 | -2.7744 | -45.59885 | 2025-10-15 03:45:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee206890-640e-3e77-b842-21f94ad2632b | -5.16253 | -37.42537 | 2025-10-15 03:45:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02c4deeb-88cc-3906-a299-7062a7323fe0 | -3.8353 | -44.54531 | 2025-10-15 03:45:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa07af7c-d969-3691-b701-8b21cb83a774 | -3.73571 | -44.14088 | 2025-10-15 03:45:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b23d78d-1e15-3be3-aca1-e9970de1c8ad | -4.92759 | -40.13779 | 2025-10-15 03:45:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e0aba6c8-6ab7-3f54-af27-3d9ea4b8ad9b | -4.7577 | -40.86661 | 2025-10-15 03:45:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7221bc6a-6b22-36d8-aba3-41710cf37b43 | -2.92062 | -48.30802 | 2025-10-15 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7b717ab8-1d68-3472-974b-9a0fa9b7efad | -4.15289 | -43.13463 | 2025-10-15 03:45:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 338581e3-7923-387c-98f3-feecae6f77fb | -3.83399 | -44.5529 | 2025-10-15 03:45:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaaa83b2-f651-37a2-8253-1485f8405bdc | -4.14545 | -41.65726 | 2025-10-15 03:45:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e9d97ea3-796b-3757-93c3-92f3c4cc95bd | -2.92902 | -48.30215 | 2025-10-15 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a4d96538-a2cc-3640-a986-e531bad1c689 | -7.94547 | -44.12867 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e986b17d-4cd5-3de8-ab07-6dd4f8a61720 | -8.19327 | -43.97383 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa93955c-1d4c-33e0-abef-c12cfc2bccd3 | -6.57716 | -42.95971 | 2025-10-15 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05e38b25-6b71-36a0-ada1-a347d23fe0c4 | -8.32764 | -38.08955 | 2025-10-15 03:47:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 508fa212-b08e-3c4b-9679-3be177a70a1d | -4.31602 | -44.54184 | 2025-10-15 03:47:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a4d1533-1f7f-3a5e-a473-39412782d51c | -4.397 | -43.61758 | 2025-10-15 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1af1adbb-99c0-3af9-9791-aecfde746238 | -7.50685 | -46.64669 | 2025-10-15 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8f3392e-4c6a-3286-b6dc-9c9586f33574 | -8.1997 | -43.98828 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bdef4cf-bd1f-3292-a84f-ad900e25fc30 | -6.91193 | -38.26496 | 2025-10-15 03:47:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe377c7c-7f14-3b4b-b73b-ffa1d1577f73 | -4.86872 | -45.68024 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3cbcc300-a73c-3baa-9676-1743044018eb | -5.71014 | -37.94069 | 2025-10-15 03:47:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66bdd852-2524-3efb-8992-b47883d33b67 | -5.25378 | -43.47151 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce3fe4a0-5825-3e48-ab9c-6a31b14a6247 | -6.1413 | -41.77156 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d217b5a4-38f2-30cc-9e13-cbf75b03e30b | -7.17413 | -42.20245 | 2025-10-15 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0375ae2f-cf61-3cd5-af6f-f1530bdfc8ed | -5.43025 | -44.2275 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 5c6a6fe9-9cac-3e5f-b1ef-7a144934b84a | -8.17977 | -44.02088 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8954ba9-9f6d-339c-aebf-3814ffb5f589 | -5.40141 | -40.89155 | 2025-10-15 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 892eb9ae-9d7e-3426-a9ce-b093979e9ac2 | -7.07531 | -41.96331 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cd43bd2c-b769-3aad-ad99-6ba22a0f7309 | -6.17926 | -44.30346 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df3b140f-47e1-38d8-8412-43bf945ac7de | -5.26621 | -41.01844 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3afbfe27-1417-3caf-a34d-b96ea3d7909e | -6.33638 | -44.01938 | 2025-10-15 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a829075-5ff3-3030-a04a-4b2316979b84 | -5.42956 | -44.42586 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a5627de-bbb5-3670-a05c-e2fde3566d56 | -6.16467 | -44.3872 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32e5e9ed-8f3a-3eeb-83b6-f20bee445436 | -6.17238 | -42.61303 | 2025-10-15 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 336e2f3e-8990-3d55-9f87-b5deab36094a | -4.89531 | -43.46857 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ee86c8a2-9251-3648-b334-6a6e22be574a | -5.4273 | -40.66375 | 2025-10-15 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0ce4815b-49f1-3530-be21-efe6d7196ea2 | -6.58611 | -41.51319 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d4362604-de52-3029-9575-9cf642f13e90 | -7.16742 | -42.18711 | 2025-10-15 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c27e292-7163-30b5-a101-17694fe2ae66 | -4.39747 | -43.61726 | 2025-10-15 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a19b306c-423a-3b9e-a8e8-391e117c149b | -4.65153 | -43.12965 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83ae345c-5ae5-34e8-beef-d3b8be2a4a90 | -5.11739 | -46.0572 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ba2d07a-f467-3dea-82d7-688b261e0962 | -6.24225 | -41.55464 | 2025-10-15 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21f708a6-005e-3c94-9a36-90328800738c | -6.23019 | -44.16097 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4f7589a-5a0d-3aaf-a128-35986012641e | -5.90881 | -42.84133 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 337c820a-d16e-398f-9152-e08553b880d6 | -5.25179 | -44.47483 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02072d9a-7872-35b4-b487-38621ec81419 | -5.86546 | -43.85123 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b89a32fe-c6c6-38cf-9b82-fd705b9574ea | -6.42563 | -41.8306 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7762a136-f891-3f62-a7f3-b5dfd7e47bab | -7.49499 | -42.13975 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 57cc7c0b-64e3-3364-8d03-8d1ca9d2e953 | -4.63712 | -42.52024 | 2025-10-15 03:47:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5d0d7c2-d776-3ab2-8212-038c6fad6bdd | -7.95003 | -44.13272 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f332d3e-9520-3bee-a607-2ecfc1dd8c3b | -4.75657 | -44.11259 | 2025-10-15 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bef03ac-1890-39da-94d7-5c4223eaba7f | -7.4942 | -42.14429 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 02744865-5f07-3bf5-b689-38e883179e01 | -6.82959 | -42.77782 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6b38c59-2e1e-3907-bcd4-17a6fa55ea8a | -5.39305 | -44.04215 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5d4481d2-08a3-3ca6-a7db-e6e8f8b4cd83 | -4.80108 | -45.71509 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07a03c96-ff2b-3a08-a50c-56b9735da09e | -6.89795 | -43.97025 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 641c1795-4f3a-3dee-8623-3dee47904203 | -7.03738 | -42.73951 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f2fd9f16-4a84-336a-bd92-da5a998714d0 | -6.43087 | -41.82688 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14cb5639-78a3-3230-906f-a25d09280ab5 | -5.04695 | -42.85513 | 2025-10-15 03:47:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e16f8b45-0011-3e2b-9c33-17d33e115187 | -6.23179 | -44.15778 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0f8afd1-7acb-39c3-b023-ef66799d0e31 | -5.34228 | -43.74124 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f86fd09d-120d-3fb3-a491-46696e6093d1 | -6.91261 | -38.2609 | 2025-10-15 03:47:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e6607a3-ca86-314b-9820-04e8bf11629a | -5.19087 | -43.80933 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6444ae9-2eff-349a-9bd2-3492020e4cb5 | -8.21291 | -44.03017 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 595c5683-a4fd-343c-a024-279448d300c3 | -5.56266 | -42.98587 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a61daa3b-576d-3613-b6c9-e70f692c5a50 | -6.17991 | -44.29975 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4c7e307-b5a6-36a2-9545-b0714227c3f4 | -7.03649 | -42.74457 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 543e34bb-33c7-3d57-a2a7-ef453b215795 | -5.87148 | -43.85031 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65a95202-03f9-31b0-84c1-053a65c9707f | -8.28369 | -43.40142 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5f7aaadd-0d3f-3425-a859-69dea409eee6 | -4.85339 | -43.20695 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00dfe4ef-1442-3f03-85c5-1ad05e6c6a1c | -5.42897 | -44.42932 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75a3d173-45ee-39cd-93eb-256960924a48 | -5.11818 | -46.05271 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b0ab084-066f-3832-93ae-952a5fca0b53 | -6.02657 | -44.31175 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e9bf8ea-4259-3d26-978e-1ce1633bdc2e | -5.58146 | -44.74704 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f360a60f-db74-379e-99e4-10bc45b69e23 | -7.7449 | -42.4527 | 2025-10-15 03:47:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b2c9ec69-7515-3279-8483-d94790a1c5e6 | -10.82897 | -43.96775 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 077fbf2c-db2a-3feb-88a5-5d54d75fd010 | -7.93418 | -44.13284 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80a6e024-6578-3d55-a5de-09832ed99d9e | -6.02432 | -43.3962 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086dd3a9-6055-3c0b-9daa-2f93ff6a6a55 | -7.23733 | -41.20476 | 2025-10-15 03:47:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 950fe402-6431-33d7-b2d6-e9dfb6035525 | -4.65659 | -43.1305 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 061ad498-4390-306d-9cdd-787d022c269e | -5.86639 | -43.84881 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0150f67c-fe88-3444-9838-1abea1ca2935 | -6.23195 | -41.56185 | 2025-10-15 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b7816900-9b51-3e0a-8066-0300d2066a32 | -5.42606 | -44.21976 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 404aa3a1-c35a-3bc9-a21a-46e8ea80fae7 | -5.863 | -43.86792 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 734451df-8aa4-3daf-9379-b71fd4262d1a | -5.87574 | -42.83019 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5c5170d5-fc58-32ba-9262-3a7107da32ac | -5.00569 | -44.49813 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff6c215f-8320-322e-9962-fb78575ed3c0 | -5.41953 | -44.22549 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 862a8442-f4fe-3b8f-9ac3-94238c7711d8 | -5.34121 | -43.74759 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README12.md)
