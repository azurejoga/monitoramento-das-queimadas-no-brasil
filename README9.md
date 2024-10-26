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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba88283-c55a-3934-b016-26460f241a6f | -17.6775 | -57.4734 | 2024-10-26 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| 07133460-1664-3f86-957b-81edf2231a7f | -17.66253 | -57.4803 | 2024-10-26 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.4 |
| 910e60e9-0bb7-3ed7-b3c9-bb6c0afa2de6 | -17.26521 | -57.26234 | 2024-10-26 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 60e09967-c046-3226-82f7-2add83b0b89a | -17.26302 | -57.26767 | 2024-10-26 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 4c7448d1-3c22-38e5-bf50-b83cca82d919 | -17.20513 | -57.27397 | 2024-10-26 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| eee2311a-baaa-3a28-bf8d-353e5ee61307 | -17.05268 | -53.47129 | 2024-10-26 01:05:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a46e16d1-a3ac-39a3-8bef-410b906c55ae | -17.05104 | -53.45731 | 2024-10-26 01:05:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 151fdc94-b55e-3b42-a8bd-d5204aab8ff1 | -17.04943 | -53.44358 | 2024-10-26 01:05:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6e154af8-7212-3a91-873a-720582cc43ad | -17.04197 | -53.47275 | 2024-10-26 01:05:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fee20096-becd-36cf-b36d-508a06e3507d | -17.04035 | -53.45886 | 2024-10-26 01:05:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7aa3881e-e76b-3173-b691-0545a981b34f | -17.03665 | -53.46522 | 2024-10-26 01:05:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d8adfc2d-9f98-3ead-bca1-74c5df022803 | -16.91318 | -57.51801 | 2024-10-26 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 2700fc0d-146f-343f-857f-0e3ade2e8c45 | -18.11145 | -57.28254 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 7b348f2f-a45b-3779-8760-4913a9a40237 | -18.07213 | -57.35018 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.2 |
| ebefdb79-f69a-3956-bf11-a96d470f7406 | -18.06224 | -57.23177 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 19f26537-0bef-3cd7-bffb-8bc23f9682bc | -18.06089 | -57.23865 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 4ca1c0ad-0718-320a-b5b2-24ff020e5b3b | -18.03067 | -57.38312 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.0 |
| 839eb720-7656-3068-a9d5-f373d708e5b3 | -18.02793 | -57.35486 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 3bbe12da-f609-3904-b0b2-bac7475e919f | -18.0252 | -57.32675 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.1 |
| 1d582eb3-b291-3d24-b229-cd843ce9eac3 | -17.94071 | -57.54473 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.3 |
| edae47bd-ff71-30d7-86bf-6858c360ee56 | -17.94024 | -57.53902 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.0 |
| ac86d574-4d51-37f1-a6cc-5001da9aac68 | -17.92848 | -57.57299 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.9 |
| 0f894354-85d6-3187-a8e1-134ea771285a | -17.92762 | -57.56511 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 41653e55-8bf1-3f20-8275-883e3856af76 | -17.92554 | -57.54397 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 7d2011ee-c5ca-3738-b790-e8a70776c0ba | -17.92506 | -57.53791 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 0b2a4971-7b0c-364c-8812-9a26cd690c75 | -17.88389 | -57.58033 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.3 |
| a530d045-4b32-30cc-a03a-6adbfe85a0ef | -17.86399 | -57.53194 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.3 |
| e7f1ad33-dc1a-394b-b4dc-3c0234a020e7 | -17.86366 | -57.52714 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| e71a3cce-665a-3a84-9f0e-439fb7db058b | -16.1778 | -48.78329 | 2024-10-26 01:05:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c73f266-466b-33cb-8cd6-0f38b7d1a1db | -16.17649 | -48.77407 | 2024-10-26 01:05:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5d3a2813-f4e8-3a60-86de-c8fa5afe1cd6 | -16.02365 | -41.20193 | 2024-10-26 01:05:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 0d282bde-e16e-30cb-866b-993f1a829d54 | -16.02175 | -41.209 | 2024-10-26 01:05:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 8f062511-6992-3697-8fad-355278802c8e | -16.01886 | -41.17608 | 2024-10-26 01:05:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| f816ce96-b628-39aa-9a6a-69c76deda875 | -16.01706 | -41.18264 | 2024-10-26 01:05:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| d1235db2-75c5-33a0-a969-fa98e2790f6f | -15.82951 | -43.59731 | 2024-10-26 01:05:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 63a07161-20c1-3af7-b0eb-377c5e87597e | -14.55226 | -42.98668 | 2024-10-26 01:05:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 84b214ef-6ee1-3ad3-97f2-f0c6d0f2c261 | -2.1929 | -53.7234 | 2024-10-26 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 52e3aa3a-ba5a-3cc1-8d2c-abd9e5b1d59f | -2.8739 | -53.3252 | 2024-10-26 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 5302e902-d56f-3a05-97f4-3d77ad685e21 | -2.874 | -53.3049 | 2024-10-26 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 680a41e3-655b-3ee3-964a-64a62752ebbb | -2.8923 | -53.3247 | 2024-10-26 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 1f4d99f2-464c-39e1-9aed-db536a4b85df | -2.8924 | -53.3045 | 2024-10-26 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 638d0ff7-5c1d-3879-851d-a29441e807ba | -2.9317 | -52.5713 | 2024-10-26 01:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 172e5439-067c-3c30-a9a9-fc5c5397c628 | -2.9501 | -52.5708 | 2024-10-26 01:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 346a9014-0222-3d8f-88c7-d64c8d31a51e | -3.2368 | -45.8077 | 2024-10-26 01:05:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 728aba20-a0b7-3e45-b85f-ed633648df0f | -3.2553 | -45.807 | 2024-10-26 01:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 390b90ab-4b15-3846-9f50-415bbe2b23b9 | -3.4729 | -43.3377 | 2024-10-26 01:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f589cc55-b96a-3768-9ac5-20ccbb5e5e17 | -3.473 | -43.3144 | 2024-10-26 01:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 34967f32-e7c9-30e7-ab49-bb40b23354c5 | -3.4915 | -43.3368 | 2024-10-26 01:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| b90e66f0-a537-34ed-aaae-7aeed240a1a5 | -3.4917 | -43.3136 | 2024-10-26 01:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b11534f8-fd9f-3023-aedc-0bfb57e2c32c | -3.613 | -44.9598 | 2024-10-26 01:05:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4a38e034-81de-3797-8d09-4b05afbb4019 | -4.5613 | -48.0358 | 2024-10-26 01:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 9ad2263b-ee7f-3d83-ad49-5c44bafd2d8f | -4.5614 | -48.0141 | 2024-10-26 01:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 11bb0164-3218-32a2-90ed-9efffc599ed5 | -4.5799 | -48.0349 | 2024-10-26 01:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.0 |
| b5a70b05-524a-3039-93da-bd1e037102a1 | -4.58 | -48.0132 | 2024-10-26 01:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 215.9 |
| b34b38e7-29ce-3e94-a5d4-bf2c1b8c20d8 | -7.6474 | -63.4584 | 2024-10-26 01:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b4703935-693f-3852-9dbb-a8e9eb791600 | -9.4996 | -47.8068 | 2024-10-26 01:05:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 81884d32-2b0b-3bed-b859-5d6d722d8c87 | -11.5037 | -45.8167 | 2024-10-26 01:06:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 3165aa00-8882-3d7c-958a-928f472ab8d5 | -11.5225 | -45.8369 | 2024-10-26 01:06:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 3a568f7a-0c74-375a-beef-112927cabb82 | -11.5228 | -45.814 | 2024-10-26 01:06:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6fc643ef-ef14-3f4a-ab48-8d633ae41a9e | -11.5416 | -45.8342 | 2024-10-26 01:06:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ebccbf63-76c2-3812-b7c2-5815b494a5d0 | -16.9012 | -57.5108 | 2024-10-26 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| b9bb4a5e-968f-3e59-ac94-b262a8721837 | -16.94 | -57.5268 | 2024-10-26 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| fc5d07dd-dc79-3548-827f-b5724a68d37c | -17.0499 | -53.452 | 2024-10-26 01:06:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ce94693b-3688-3f78-b104-b4fa8a0ddffd | -17.1987 | -57.2714 | 2024-10-26 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| b69f88ff-3b19-3b1a-84d7-8bf3a50f8500 | -17.219 | -57.228 | 2024-10-26 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| d703e9f1-900c-3438-a6ac-4dcdc15b279e | -17.2344 | -57.4926 | 2024-10-26 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| a633899b-bdb1-3c6d-87be-544f7b8a96f3 | -17.2537 | -57.5108 | 2024-10-26 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 878759f7-fb62-3d95-80dd-f705d392dd41 | -17.254 | -57.4903 | 2024-10-26 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| ece1a0ba-a79f-38c7-ab40-3ef00619089e | -17.2733 | -57.5085 | 2024-10-26 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| fc8db2b8-483a-3a74-bb39-37a5a9450041 | -17.2737 | -57.488 | 2024-10-26 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 837e07c1-9af2-35dd-8c64-de9508719e63 | -17.6667 | -57.4822 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| ff417bfe-fa2a-3282-bd38-80f516718903 | -17.6865 | -57.4798 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 7591711c-fb60-3080-ae93-8dd4906be990 | -17.7671 | -57.3673 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 3930222d-1fe3-372c-9b32-a743d81a2680 | -17.7674 | -57.3467 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| cb8c6533-00da-384d-9e57-0dc18971e98f | -17.7868 | -57.3649 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| b73b51b8-88f3-3008-a3e9-5f4652fd5b0a | -17.7872 | -57.3443 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| e5710851-7319-376c-a10d-50937adf2dbb | -17.8066 | -57.3625 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| c973b84c-7a99-3584-b532-5d1436ae436a | -17.8069 | -57.3419 | 2024-10-26 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 14373778-63db-3207-bea1-ba6e46f5df65 | -18.0431 | -57.3745 | 2024-10-26 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 711ec0a1-1c1b-39df-8a95-a0a0517f703b | -18.0434 | -57.3539 | 2024-10-26 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.3 |
| a78a293b-c6bf-357f-afa2-4c3a87139321 | -18.0448 | -57.2712 | 2024-10-26 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 456a7ae1-d15d-39be-b636-5818bfe7e821 | -18.0452 | -57.2506 | 2024-10-26 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.1 |
| c28d74df-08bb-3c1e-8948-2ef135bb4706 | -18.0632 | -57.3514 | 2024-10-26 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 8ec93bb2-59fe-38ad-b9f0-e3f4053ddaab | -18.0653 | -57.2274 | 2024-10-26 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| da5f4fc2-e267-3848-a2ef-bb14a598aded | -18.2649 | -55.9975 | 2024-10-26 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 995cfb61-9ee0-3cd6-943a-f6e43e99ae67 | -19.5067 | -56.6829 | 2024-10-26 01:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 4822fd5a-726a-3d4d-afb6-36f6f2a13e61 | -19.5264 | -56.7011 | 2024-10-26 01:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 95344808-0932-3995-949d-8a813b78ca49 | -12.72064 | -48.52957 | 2024-10-26 01:07:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a2ad7bee-aff8-3ee0-9eaa-49628454553f | -12.59978 | -48.77502 | 2024-10-26 01:07:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 4d955cf4-9589-35b0-9ad4-22384a3ed419 | -12.59842 | -48.76556 | 2024-10-26 01:07:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b96017de-2eae-3660-b5db-3cb40e9b930e | -12.59074 | -48.77644 | 2024-10-26 01:07:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 59bade95-5990-375a-a77f-bed9d48d9e8c | -12.58937 | -48.76697 | 2024-10-26 01:07:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8fb427f6-4a98-3610-9733-a187897d1193 | -12.38019 | -48.59662 | 2024-10-26 01:07:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55c26577-69f3-3133-be85-9b265b0bf387 | -11.28121 | -56.15179 | 2024-10-26 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 66f9c900-2fa7-3f03-b0cb-287f0f4a26d1 | -11.17044 | -56.29735 | 2024-10-26 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a80c9fe9-514e-39af-991d-ae7017832376 | -11.16832 | -56.27954 | 2024-10-26 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6fe99737-30b9-3e85-b75d-3bf2aa7d11fb | -11.16432 | -56.28554 | 2024-10-26 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8be779c6-da5b-3d21-b19c-1905c3ca5768 | -10.54694 | -47.77816 | 2024-10-26 01:07:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b911f02-2778-32f9-8368-ca4c0b50a2de | -10.30691 | -47.80527 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1870faf3-6cde-3bf9-b4ab-7f6edb993f1d | -10.30525 | -47.79423 | 2024-10-26 01:07:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |


[Clique aqui para ver as próximas entradas](README10.md)
