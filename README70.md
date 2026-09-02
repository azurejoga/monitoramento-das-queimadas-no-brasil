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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0563488c-42ff-359c-bbfc-b4b6ed715a47 | -11.3048 | -45.1575 | 2026-09-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ef557a83-33fa-30bd-b1ef-0e1d955933b9 | -11.677 | -50.4939 | 2026-09-02 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f8d32801-f301-3e9c-a63d-4a926d119a02 | -9.4538 | -45.6228 | 2026-09-02 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| edb3d91a-35fc-33a9-9193-663a9860ba41 | -8.4673 | -54.6833 | 2026-09-02 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 307ac87c-b2ae-3d26-bd13-9436702e253f | -8.7819 | -46.4399 | 2026-09-02 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 90a151b2-fa7f-3c6e-bf8c-0f8a302c2962 | -10.7774 | -44.7463 | 2026-09-02 12:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 68b86d4d-93e4-3f4d-b339-7b17b63b5731 | -11.5483 | -45.4446 | 2026-09-02 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 19603e63-e5f8-3f05-8d92-601f66505732 | -6.1474 | -57.7605 | 2026-09-02 12:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 23f50aea-891f-3e2d-95a0-e1b23e40c675 | -10.9204 | -45.3253 | 2026-09-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 7f8f3e15-e100-36b5-8197-8ebff241081a | -11.3767 | -45.423 | 2026-09-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cf05dfe2-00a6-34b6-bb0e-9dd4e03d8c77 | -8.45 | -54.69 | 2026-09-02 12:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4996947d-3b3a-3a83-a8c5-c686c02c3ae0 | -8.48 | -54.7 | 2026-09-02 12:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4dd7bad-1acf-30d5-be7f-6d4b4fadafce | -10.9204 | -45.3253 | 2026-09-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 6ac7e722-8031-38f8-8da3-99f8a3d06c32 | -8.4485 | -54.7048 | 2026-09-02 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| fba03917-5850-3a9a-ab24-8568bc3cf6d3 | -9.7154 | -47.2091 | 2026-09-02 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 28a678a1-c9f8-3a18-83a9-3959af3ce875 | -11.3048 | -45.1575 | 2026-09-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 6055ac65-ea7d-3cdc-8cda-90ba1be246c5 | -8.4669 | -54.7237 | 2026-09-02 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| a3d2adda-31e1-3071-b108-9ce320a9f66f | -11.3044 | -45.1805 | 2026-09-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 49b0e717-d41b-3577-814d-faa0b72cd888 | -11.3767 | -45.423 | 2026-09-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 3c1bcd75-c9f1-3c0e-9ab0-5668db7c6107 | -8.4858 | -54.7023 | 2026-09-02 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 7106ec6f-b0ea-3eb6-9c8b-a6ebd702e093 | -11.3521 | -50.6373 | 2026-09-02 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 2cbf6809-860f-3a66-b5e5-376d9b4a6dce | -8.4673 | -54.6833 | 2026-09-02 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 5b46b541-936d-36cc-be3d-e64d65ff1b29 | -10.9562 | -50.4884 | 2026-09-02 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 9dae9b2f-019c-3e2b-8668-be039dfed257 | -11.5483 | -45.4446 | 2026-09-02 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| bc8c4f27-4d71-368f-a275-f736411878e5 | -11.3524 | -50.6159 | 2026-09-02 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 68fc6927-7752-301c-9e2a-495d23cb1f79 | -11.3579 | -45.4027 | 2026-09-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 343688df-de1a-3dfe-b7ea-20455dc7a2bf | -6.1474 | -57.7605 | 2026-09-02 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| a0348fbd-61e7-3800-bdff-1046d51732b9 | -11.3575 | -45.4257 | 2026-09-02 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ff7d9c2e-a45b-328b-8084-1c7f870e205c | -6.1475 | -57.741 | 2026-09-02 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a3c3e4b6-7cf2-38b4-bd00-69cbec7ffd04 | -10.3196 | -50.0211 | 2026-09-02 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 420584ae-4571-3d4b-873f-a9bb68a5a3b7 | -9.423 | -37.8286 | 2026-09-02 12:20:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 120.5 |
| f6954f31-15a3-32d4-bc80-1729ecfc9759 | -8.4671 | -54.7035 | 2026-09-02 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 290.5 |
| 568efa12-988c-3fac-bdde-02d53fe38b05 | -10.9562 | -50.4884 | 2026-09-02 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b0352a64-628b-328f-a5fa-210fc6272968 | -8.4669 | -54.7237 | 2026-09-02 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 44b5f3b5-dedc-3e60-a4c7-134f73f44cc0 | -11.3044 | -45.1805 | 2026-09-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9547e417-c034-3c30-9979-4b7777e8fe04 | -6.1474 | -57.7605 | 2026-09-02 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 5762cb0a-b2d8-365b-8416-7ebb8a9829d2 | -6.1475 | -57.741 | 2026-09-02 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 60840685-2c23-3e3d-a7a2-0771d27658a6 | -10.3196 | -50.0211 | 2026-09-02 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3f6ee1e0-c4d7-3754-8521-1eee83a5e752 | -11.6434 | -50.1976 | 2026-09-02 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 913e42ad-7de1-3d73-9017-bd47de381d1e | -8.4485 | -54.7048 | 2026-09-02 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| d28cc1a1-7d20-365e-8877-ec82a7ee0877 | -9.6964 | -47.2112 | 2026-09-02 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 74452bb4-7989-3b25-9050-6c6260cdf566 | -8.4671 | -54.7035 | 2026-09-02 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 293.1 |
| 821c7a64-19c3-32e4-a726-b36b1d58921d | -11.3579 | -45.4027 | 2026-09-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| dda9c41e-8726-39b9-ad1f-997a4ee1e70e | -7.9614 | -44.2519 | 2026-09-02 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 79743c6b-876c-3c7e-b7a3-8b719884a338 | -11.677 | -50.4939 | 2026-09-02 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| c50568d5-4760-302a-9453-a7b55a358a23 | -13.9662 | -58.6936 | 2026-09-02 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 7ee01791-6d1a-3768-9c19-4d8813738a0f | -11.3767 | -45.423 | 2026-09-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 3601cdbf-edb8-39b5-82fb-a6fa9e025295 | -8.4673 | -54.6833 | 2026-09-02 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 881742e0-ee54-3fbe-a78d-24d855f62db3 | -11.5483 | -45.4446 | 2026-09-02 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a9402029-f7f9-360f-bbc6-05d2e12f8d7a | -12.1504 | -47.1283 | 2026-09-02 12:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5ffe001b-7799-3eca-b4c0-19e56e3bcfbe | -11.3575 | -45.4257 | 2026-09-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 21aefb2e-6ef0-3754-8b1e-560def29869f | -8.4483 | -54.725 | 2026-09-02 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ca9c43cd-7014-34dd-b13c-ede04aef90dc | -11.3048 | -45.1575 | 2026-09-02 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 535eccef-d7cc-3cfe-8782-7d39ed6cf68e | -11.3044 | -45.1805 | 2026-09-02 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 5f881c2f-d44b-3ee8-bd46-03f8f3fde96e | -6.2113 | -53.4815 | 2026-09-02 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 54b458d3-835b-3e79-bc80-4ee2217fc5ab | -12.1504 | -47.1283 | 2026-09-02 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 3f0fd8ad-9076-3077-a63f-95c91014fbb8 | -8.4298 | -54.706 | 2026-09-02 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 2896ed6f-4f58-391c-a123-c1d5afed7537 | -6.1474 | -57.7605 | 2026-09-02 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| a11577b2-f5fb-3517-9063-27f8076e037e | -8.4483 | -54.725 | 2026-09-02 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 0e6c1d05-9134-32b1-9af7-a2722aa38679 | -11.0933 | -51.5345 | 2026-09-02 12:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| fd6126f3-ba38-329e-b255-110175f06bb5 | -10.9562 | -50.4884 | 2026-09-02 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 09886391-2747-3752-b12c-4d5f70cc6856 | -6.1475 | -57.741 | 2026-09-02 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 695fb62d-ba3f-383b-8eac-44b8e047f4c6 | -11.3521 | -50.6373 | 2026-09-02 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c782c37b-4f22-30dc-b787-ec7de928fce7 | -8.4235 | -44.9849 | 2026-09-02 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d3c8b47c-3ddd-3cfb-8154-0fb4cfc2a905 | -7.9428 | -44.2307 | 2026-09-02 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4fb458be-3c7a-351c-bf35-62c28a702409 | -8.4673 | -54.6833 | 2026-09-02 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| e1574856-6ff3-3d79-8480-64b2dc9e4c6c | -8.4485 | -54.7048 | 2026-09-02 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| f4917e9b-bacc-3432-9347-c3d0a1afd3f9 | -8.4671 | -54.7035 | 2026-09-02 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 236.1 |
| 60d04331-b0cb-3ea6-9a03-c1341f52f4a1 | -10.3196 | -50.0211 | 2026-09-02 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 83a708dc-44fa-3735-9936-760a0cb5a9ad | -9.6964 | -47.2112 | 2026-09-02 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| e2dd1f43-cd13-3d3a-ad8d-4653f260bf25 | -7.9614 | -44.2519 | 2026-09-02 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2a601ded-0f3d-3c7e-a4b3-6cf58b570c99 | -8.7613 | -62.5869 | 2026-09-02 12:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 76881b31-ddfc-3290-8e2a-058dd1ad85ef | -8.4669 | -54.7237 | 2026-09-02 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| ba0de140-85b6-3843-b3cc-97af45a7490c | -6.6948 | -58.7678 | 2026-09-02 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 84cf2769-a1b5-3447-b8bd-7b4506c3d4e1 | -9.6968 | -47.189 | 2026-09-02 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7de175cc-0c22-391b-8cec-537be3cd2747 | -8.4483 | -54.725 | 2026-09-02 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 0591bd08-6d2c-3f3d-9398-6ce91a8197d1 | -6.2113 | -53.4815 | 2026-09-02 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d9cb495a-9e76-30b3-bd65-1d4feff78492 | -6.6764 | -58.7686 | 2026-09-02 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| dd891eef-af41-39b4-a07f-ad3da164ac4a | -12.0936 | -47.0913 | 2026-09-02 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3b29b6fd-7372-384c-ad79-12e6d834e32f | -8.4673 | -54.6833 | 2026-09-02 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 4dad0271-0946-3659-999c-9ec50ff09ec4 | -11.3048 | -45.1575 | 2026-09-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| ab3676a5-f227-3d98-bc20-9190bedeeeb2 | -12.1312 | -47.1309 | 2026-09-02 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4c18f6fc-6eb6-3704-8521-419ec5155c92 | -8.4671 | -54.7035 | 2026-09-02 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 306.4 |
| 54f63bca-10f5-3282-8ede-c1c980c6c726 | -8.4485 | -54.7048 | 2026-09-02 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 044c2bbb-9927-3c87-91e3-3db2a05252cc | -10.9562 | -50.4884 | 2026-09-02 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 4055a73a-53c5-3319-b741-3b3c932bfa5b | -11.3579 | -45.4027 | 2026-09-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0241e600-6bf8-363e-8c34-ac24cd5a9de2 | -11.093 | -51.5556 | 2026-09-02 12:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 769c2ea6-ffbc-3be8-b57e-87fecd6938dd | -8.4669 | -54.7237 | 2026-09-02 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 15067bfc-41c1-3e9d-8638-83020dde22cc | -3.2455 | -47.9187 | 2026-09-02 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 08cde169-308d-3f6d-a698-ef68e66b02a0 | -11.3044 | -45.1805 | 2026-09-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 43f2d31b-f086-3143-97f1-8affec20e62a | -6.1474 | -57.7605 | 2026-09-02 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 950b2ba0-1538-3ee8-a9de-e1a424c613d9 | -6.1475 | -57.741 | 2026-09-02 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 86999ff5-810c-3e3d-b3af-3ddef7c493e6 | -10.9752 | -50.4864 | 2026-09-02 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| b8dd102c-8302-397d-8672-0cf45ea5bb25 | -7.9428 | -44.2307 | 2026-09-02 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 46c9ee35-3799-3e38-870d-7639ac67d173 | -11.6434 | -50.1976 | 2026-09-02 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| c4b7637c-e642-36dd-bca0-db99d0676694 | -11.3767 | -45.423 | 2026-09-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| c3a8e2e9-7f32-33fd-92b6-a906532d1eda | -12.0741 | -47.1164 | 2026-09-02 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 754d240a-671e-365b-aed0-9fc1571c5904 | -12.1504 | -47.1283 | 2026-09-02 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| c10dfb3a-2646-36c7-a87e-bbf5ee209099 | -11.3771 | -45.4 | 2026-09-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 9af48f58-efee-3db4-863e-8bbb040c2d02 | -11.3239 | -45.1548 | 2026-09-02 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |


[Clique aqui para ver as próximas entradas](README71.md)
