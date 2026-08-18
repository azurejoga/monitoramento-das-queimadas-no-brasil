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
| 6d47891d-f272-3c96-929c-5ad3131292df | -6.841 | -59.0132 | 2026-08-18 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 2bb706cb-66e9-3bea-9a82-b665fda5efbe | -8.4899 | -48.821 | 2026-08-18 13:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 154.4 |
| aaa1a561-f5b0-31cb-a4d1-431a84e0c2ee | -6.7815 | -59.748 | 2026-08-18 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a4848621-d75f-3d9c-8b67-91306a5525c7 | -10.2765 | -50.4313 | 2026-08-18 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 132.3 |
| f6bfd828-8593-3b5c-8240-018ef5d5f64f | -12.7597 | -48.4453 | 2026-08-18 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 50d46b62-b29a-31f5-bd9f-a6041a6bf781 | -12.5399 | -47.8554 | 2026-08-18 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 924e236a-e6a8-3fbf-b276-cc3da4cff542 | -11.3606 | -46.381 | 2026-08-18 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d32f818e-a9d2-34bb-85d6-9c41b8f164f3 | -11.3491 | -45.9292 | 2026-08-18 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 8235b12f-f552-36bc-a168-116703e0b425 | -10.2767 | -50.41 | 2026-08-18 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 997725d7-248c-366d-817e-895dd84cd8e8 | -15.6395 | -54.7982 | 2026-08-18 13:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b35d2d88-e880-348c-bbe9-f25bfb1c38b6 | -12.7793 | -48.4205 | 2026-08-18 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 222b507a-befa-3f11-8de4-fa29ddb3722d | -12.7789 | -48.4426 | 2026-08-18 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| babd8d4b-950c-36c4-b5ea-243e6345a228 | -8.604 | -50.3527 | 2026-08-18 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 8099f136-d959-3424-a31d-f7f9b926004b | -8.997 | -45.855 | 2026-08-18 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ecc80e08-e77c-3dff-bf1f-2fb1e990c5b0 | -14.3529 | -51.9345 | 2026-08-18 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 49826140-69c4-3da9-b600-8b640299e875 | -12.7793 | -48.4205 | 2026-08-18 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f10175e0-5a5c-3858-ae8f-52e0de68a136 | -7.2007 | -43.2814 | 2026-08-18 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 0ab73aea-1d73-37e2-86ff-38a82a1edfc5 | -14.4656 | -52.1112 | 2026-08-18 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| dc00060c-a33d-33b4-abe3-6968182ecbfc | -12.7597 | -48.4453 | 2026-08-18 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| dc3f358e-8282-3852-883c-b9d563a86c03 | -14.3529 | -51.9345 | 2026-08-18 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 162.1 |
| b46407b2-46f6-36bc-b0da-4038be744dd0 | -6.9884 | -59.0457 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 694b72ed-008a-3458-8d52-b6b9999cbbea | -13.5676 | -51.7166 | 2026-08-18 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 92c33f47-5e3d-3f33-85fa-bc486752306a | -7.0069 | -59.0449 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2abdceed-55f6-3b57-a6f8-45557f8e0dd5 | -8.5087 | -48.8193 | 2026-08-18 13:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 81.8 |
| fd20b86f-c002-3de5-92b5-c2f8eea8be69 | -6.7814 | -59.7672 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |
| d34e5ce9-44f1-317f-8b0f-7ae33be886c1 | -6.841 | -59.0132 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 1ae276d5-8fcf-39b8-b4a8-f257b4b521bb | -8.4899 | -48.821 | 2026-08-18 13:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 75730fd5-16a9-3a88-8ae2-b0ee604623b4 | -14.3525 | -51.9559 | 2026-08-18 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| fac1db81-ec2d-32c3-807a-aee22e26e9c5 | -6.7478 | -59.1716 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4b1d2f0e-243e-32fe-b266-11ba5c62e2d7 | -9.0673 | -50.8419 | 2026-08-18 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| a4d4eae3-9477-3450-90bf-006682f98ec1 | -6.8596 | -58.9931 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 059a2cf4-c3d8-38fc-b363-7505b4b23480 | -13.4117 | -54.3737 | 2026-08-18 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| aa46f26f-7492-34b9-b743-3ffa78a6f523 | -13.568 | -51.6953 | 2026-08-18 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 34fd6d16-c8a7-3bb5-90c6-f865243dd888 | -12.5399 | -47.8554 | 2026-08-18 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3e4d6705-4d18-374f-95ff-e83e80ea05f8 | -6.8594 | -59.0125 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 0440673a-2ae0-3732-a7f3-e482fe6de386 | -6.7123 | -58.9412 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| be98ebb6-1164-3492-95a0-c28806ba60a7 | -14.4704 | -51.8337 | 2026-08-18 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| cd234eee-1f77-36ce-ae97-0f9fa6498378 | -12.5207 | -47.8581 | 2026-08-18 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 8ed49470-717a-3918-b338-b4084cf54944 | -7.7881 | -47.8607 | 2026-08-18 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a887378e-f4c2-3f70-8af0-6c7e92b21a49 | -11.3606 | -46.381 | 2026-08-18 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a6de4473-f712-3a7e-a7f1-b0b101782de4 | -6.8411 | -58.9939 | 2026-08-18 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3b727a83-7293-3dc6-ba77-e60b2dbadf4b | -12.7789 | -48.4426 | 2026-08-18 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b86f0361-53c3-310e-b164-603ca1963c38 | -13.5676 | -51.7166 | 2026-08-18 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e218acd2-1427-3d73-9b88-0c8039aa25d5 | -13.568 | -51.6953 | 2026-08-18 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| c1ef8089-f5fa-3fe1-807d-01f94bbe2c7b | -14.3729 | -51.8893 | 2026-08-18 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| be0cad00-7e9c-3d8c-b9a4-262f9dddc996 | -12.7789 | -48.4426 | 2026-08-18 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 60c987d3-fe41-3aad-8fe3-a5dcfef3a4bb | -12.7597 | -48.4453 | 2026-08-18 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 64106b3e-4be5-3981-82f7-04ea957151d7 | -9.1267 | -46.044 | 2026-08-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 58bc054e-2b06-31ba-87c3-e93ee3c2c800 | -14.3525 | -51.9559 | 2026-08-18 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 6e1b2e9a-1caa-3e63-b1a9-a858701e0d22 | -10.2765 | -50.4313 | 2026-08-18 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 8454d46d-2c80-36e8-acee-9bfbccfbd624 | -14.3733 | -51.8679 | 2026-08-18 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e4e1b4ec-59b6-39d0-a954-0c09ca5cd442 | -7.2007 | -43.2814 | 2026-08-18 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 0b3b2d33-a221-3168-9bae-a917854dd33f | -6.9884 | -59.0457 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 80b87752-9fbf-3a08-a332-0813e43b43a7 | -9.1705 | -59.6955 | 2026-08-18 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ea655dfd-eb6e-3abc-9762-92d2dfdaed10 | -14.5079 | -53.0365 | 2026-08-18 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| cb844ebf-2569-3281-8362-868ef81f1c75 | -6.0179 | -57.8437 | 2026-08-18 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b82d2fd1-5b1d-3341-bc25-75f80e62916c | -9.7709 | -47.2917 | 2026-08-18 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 95e8294a-6f2a-348a-9cdf-88da305a99b6 | -6.8411 | -58.9939 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c05a0d61-1858-37a6-9db7-cf6d826012ce | -7.2195 | -43.2796 | 2026-08-18 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 5d49cda3-718a-3ec7-84f3-911abac4ba08 | -17.4667 | -47.864 | 2026-08-18 14:00:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c32b21a8-a7fa-3b75-8945-cb37be3f4e9c | -8.4899 | -48.821 | 2026-08-18 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 110.7 |
| d3c0c65a-64b0-3ec0-b8ea-bcf559e08ea5 | -7.8068 | -47.8591 | 2026-08-18 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 91f26eda-56d4-3f36-ad51-05288e7d7a50 | -7.7881 | -47.8607 | 2026-08-18 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9d38fcdc-65f3-32ac-9266-f81ee8444ee8 | -14.466 | -52.0899 | 2026-08-18 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e1259169-8ea0-3496-97ed-12c48f80e338 | -6.7123 | -58.9412 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a4a54f21-39d2-3deb-b20c-5cdb720a79c5 | -6.8594 | -59.0125 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| cdbb4695-e01a-3390-93c1-2513a2bf5629 | -12.7601 | -48.4231 | 2026-08-18 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ea3d9632-8e83-3473-8156-3f40ab8c458c | -6.9516 | -59.028 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e85fcd2b-bbfc-33cc-9dda-39db07a203e7 | -6.7478 | -59.1716 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 720b972b-5ac2-307a-982c-6ffbb9336a47 | -6.8596 | -58.9931 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fb5bb819-b83d-311f-bd25-be65f8129365 | -6.7814 | -59.7672 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e5bf6203-079c-388f-8170-b47384e32fa1 | -6.841 | -59.0132 | 2026-08-18 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 7628aa6a-eed7-34de-b228-edac3907dfca | -12.7793 | -48.4205 | 2026-08-18 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| cd46dec5-af26-30e5-a1af-4369aa3133f7 | -14.4656 | -52.1112 | 2026-08-18 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b25812e2-1a77-3915-baed-774b12f952bc | -8.997 | -45.855 | 2026-08-18 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 2156c769-e18a-3d7c-9bd7-d3a78023753c | -7.8071 | -47.8372 | 2026-08-18 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 99edb22b-4d62-3113-a69f-806846655e8e | -14.3529 | -51.9345 | 2026-08-18 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 6ca24049-816f-3db7-b26e-6327a6f3fb37 | -9.0673 | -50.8419 | 2026-08-18 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 53b60bfb-ce4a-38f7-9fdb-d381e92f3ac5 | -8.5087 | -48.8193 | 2026-08-18 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 109.6 |
| bc770d52-cf4d-3b42-934d-7ee92b0edcde | -6.7123 | -58.9412 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5d3f69db-16da-3056-8708-6148e597d9c6 | -17.4667 | -47.864 | 2026-08-18 14:10:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| fca12c51-8625-3844-b816-d5872248e2dc | -14.4704 | -51.8337 | 2026-08-18 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| dadd32bf-2cdb-31b8-b1e9-a18820fde8a3 | -8.4899 | -48.821 | 2026-08-18 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 93f396f7-e1bd-32c0-80dc-a1dc41606f4d | -13.568 | -51.6953 | 2026-08-18 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5dd1c0f7-78e2-302c-91f9-923076bbe0c8 | -6.841 | -59.0132 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 21aec8c5-7fbf-3c32-a198-8ea90797b4e1 | -6.6014 | -58.9844 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e77e20e9-0f2e-3bfa-945d-aea4a1ebbeae | -6.9884 | -59.0457 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 1bbb4489-f330-338a-ac38-62f1a25a1d0f | -6.7478 | -59.1716 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5bd8d9c2-98e7-3b26-835a-b7bdcd589e55 | -6.8596 | -58.9931 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d3876cbf-c2aa-31c9-bc9c-378d618a4d9c | -12.7789 | -48.4426 | 2026-08-18 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 79d360a6-64a8-3bb2-b1ba-de57c369d78a | -13.5676 | -51.7166 | 2026-08-18 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8515a3ad-5b08-3a90-9ea7-231f49bbb7ed | -7.8068 | -47.8591 | 2026-08-18 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| b3fa3afb-0be4-3c29-a2fd-23c919ebd8df | -6.748 | -59.1523 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9f1c4563-29df-3361-941b-d40a238ed426 | -6.0366 | -57.804 | 2026-08-18 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 092e9289-0121-3ca3-9a2b-60d282dd0671 | -6.9516 | -59.028 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a2d24a2a-15a6-3feb-9b75-b84a8256a26f | -12.7793 | -48.4205 | 2026-08-18 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e2401ba1-7675-35f4-98f9-9075583c903f | -6.8594 | -59.0125 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 57231ca7-091f-3629-8406-79ecdede9960 | -9.1705 | -59.6955 | 2026-08-18 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| bcd49b78-e1eb-3d3b-8e94-96ad249b7055 | -7.7881 | -47.8607 | 2026-08-18 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 73ac60ed-d2bf-3ba3-9188-631b339d7167 | -14.3529 | -51.9345 | 2026-08-18 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |


[Clique aqui para ver as próximas entradas](README68.md)
