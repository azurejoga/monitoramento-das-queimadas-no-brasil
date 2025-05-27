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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14d99fb3-1e9d-342c-9593-a2aa9bf1b791 | -8.43315 | -46.66185 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0eb64af8-bebb-3eb2-b02c-4728fa6b727d | -10.60158 | -52.84357 | 2025-05-27 04:27:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2c13b61-7dc6-332f-95ab-199fe7b6584f | -8.72169 | -49.38537 | 2025-05-27 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6229801d-38dc-3d22-94a8-46228d9640b2 | -8.43092 | -46.65434 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc379b53-c728-34d1-aab0-c0c0d24bc9f0 | -10.74199 | -49.28489 | 2025-05-27 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e05ba79-54b6-3e96-a39a-37eace24426a | -7.46498 | -47.05472 | 2025-05-27 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9b1697a-dad8-3b75-8ad8-98b66714d06e | -7.33968 | -43.37729 | 2025-05-27 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0cb87e7-9338-36cb-8cc5-24d6d6acdfc3 | -11.57155 | -47.62863 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14eb8ecc-c782-349d-839e-609b616998c2 | -7.23125 | -43.10609 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5d4cb6c4-df47-354d-8b52-23814f45ab60 | -9.71793 | -48.32252 | 2025-05-27 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4131fe14-af85-3db6-a32c-b4d454902dd8 | -9.15002 | -49.65218 | 2025-05-27 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27637680-af38-3976-83ae-63a8f85e4013 | -11.57283 | -47.92218 | 2025-05-27 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d86bc97-0fe7-3eaf-a216-d82091f9db67 | -11.02345 | -45.23352 | 2025-05-27 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0d7c73e-3697-3823-8f49-1c3df4a1d68a | -9.39356 | -48.4267 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bc5ff1f-b972-3416-bf7d-5219b7015cc7 | -12.15525 | -43.20675 | 2025-05-27 04:27:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 847b2853-11fa-32fd-b38c-281687f45d60 | -6.21771 | -43.33638 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23e14b02-0212-3af3-8c04-9a99b92ffdcb | -7.2015 | -43.53196 | 2025-05-27 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1ee6489-d7ff-356d-a3d7-b803002ac30f | -8.38747 | -49.65664 | 2025-05-27 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e97479d-b465-31aa-94b4-24f5460bfae8 | -6.22487 | -43.34516 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0e5a2a8a-d077-3c6b-8f5c-70919a226a17 | -6.1588 | -47.37098 | 2025-05-27 04:27:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36c59537-c3ce-39d6-8129-3a668a620dc8 | -10.95426 | -48.14894 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a890307-35f7-3c5d-812a-e26f94ac1d48 | -8.0197 | -43.18154 | 2025-05-27 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b7d8dc1-1769-35e5-b630-e8cfa92e9999 | -6.16298 | -48.05803 | 2025-05-27 04:27:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 478823ac-23e5-385e-aea7-14d5d58ef856 | -6.63481 | -43.21655 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 67bff91d-d2dd-3373-bd33-65341cfa15e0 | -7.1976 | -43.11162 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 79c2683c-eb48-38ed-a0cc-4f5076ff737c | -10.63967 | -48.08658 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ae752f3-5faa-375f-a2ea-0b5adb0d049a | -7.22763 | -43.11186 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ff5cf1ba-a4b6-3301-9f86-97f87a4c00f2 | -8.3133 | -55.11721 | 2025-05-27 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cd81baa-02f5-3166-9152-0325613c4b8f | -10.36757 | -47.96971 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51226dd6-fcb9-3c3f-a1a6-b8e8254eb75b | -10.34802 | -47.98478 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40ed8dc1-ed4f-3f8c-bea4-ecd27cc914ee | -7.19996 | -43.12082 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4c4dcd8e-0d0e-321a-8d92-04972780698c | -10.63298 | -48.08549 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bb31e09-9a5f-398e-9d12-2fac58838700 | -10.95148 | -48.14483 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00bad2e9-cd90-3e70-b7e8-5b6ec112edf4 | -8.78202 | -47.95379 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3e7caf6-19e9-37b5-8f7c-878a7d20ef00 | -7.60272 | -43.384 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 489c6df2-2545-3b78-b0ea-38cdd64a8253 | -7.20429 | -43.11706 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 08cf7f0a-6e82-39be-9222-47c01c9b3449 | -10.24177 | -47.60843 | 2025-05-27 04:27:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb8683d1-0a8c-3063-ac5e-03b1355d424d | -10.33912 | -47.97605 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb7486d3-6864-3b60-a7ad-fe44e3f42452 | -7.55239 | -43.37215 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8bc473b-93e7-32bc-9fbc-921ef7d270df | -7.40994 | -49.37665 | 2025-05-27 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dca8f41-e276-39ea-a357-fbe2fa4b63db | -9.90772 | -47.77164 | 2025-05-27 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8184987-2df0-3c85-89f7-5cb7ba5281dd | -10.53008 | -47.5868 | 2025-05-27 04:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e78d8f21-da17-354a-8412-09224031a677 | -7.19392 | -43.11108 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a35efa0d-b063-396e-96ea-c833cfcb04f7 | -6.60072 | -44.73539 | 2025-05-27 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cfc9033-5be3-3b4f-8126-f2106ee977c4 | -7.22829 | -43.10755 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 1ef1610c-99d7-36fd-acf3-9bad6c5dc4a4 | -8.29525 | -55.10197 | 2025-05-27 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dc94402-1bc4-3b8e-a35d-75cad07afac5 | -11.57488 | -47.62917 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5b94528-7f37-35f5-933a-01b4e545c0d2 | -10.49798 | -42.42262 | 2025-05-27 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c3583747-f129-39fe-995c-ea1fc620fc4f | -7.20363 | -43.12138 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| edb7bb02-36b7-3879-b431-ef1fa89aa567 | -12.27028 | -44.58594 | 2025-05-27 04:27:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 087c6ecd-1592-3f3b-b702-2c95a4336a30 | -9.38118 | -48.4172 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f79c6fdc-eb71-3184-9e5f-e54754c79d17 | -6.21708 | -43.34047 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a4263fa-d215-303c-bde0-c113f4da6274 | -8.05254 | -43.16417 | 2025-05-27 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 251b07f9-fe61-3574-b7d5-569478dd4056 | -7.60314 | -43.40566 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f06a0931-e910-37b1-9915-eb94d3b43209 | -11.57432 | -47.92579 | 2025-05-27 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b69be347-099c-3a84-b907-3e5780c45f2e | -10.24566 | -47.60546 | 2025-05-27 04:27:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c77fd916-e77d-36ca-9e2f-8c413d97f3fe | -5.95785 | -36.09896 | 2025-05-27 04:27:00 | NPP-375D | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a071834f-4be7-3321-87c7-1cb4eae32326 | -8.94814 | -47.59531 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b08d5475-840b-34e9-9dc5-557cb80ce7d7 | -7.20904 | -45.35303 | 2025-05-27 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd6c7f72-997a-320e-873b-d49e92cbb9ed | -11.80001 | -44.26951 | 2025-05-27 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d845cc0-9bba-3d09-8088-c96f7c2b0793 | -6.22426 | -43.34159 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b2cb69c-471c-3025-8fc2-b9ca91df779b | -10.2338 | -47.42698 | 2025-05-27 04:27:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faab8fbc-1294-363b-8a1a-218df1a3c020 | -12.27502 | -44.60379 | 2025-05-27 04:27:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0714820c-150c-3a96-8c6f-93a097cf6d63 | -7.16671 | -43.31565 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df017025-66d3-3fea-bfca-1a15f2220a99 | -7.20567 | -45.35251 | 2025-05-27 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d48e6d7-c180-3132-8f3a-48ed239aa489 | -7.55666 | -43.36847 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b199ab8-51ef-314b-91f3-242f5c675843 | -10.74137 | -49.28868 | 2025-05-27 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 512852b2-3c9a-3386-9b5d-d195a4d078e3 | -10.94977 | -48.1555 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1143a40e-5b9b-3b1e-9636-705e99c358bf | -9.57251 | -48.444 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 982a82bd-03d6-3cb6-87fd-2ab97e585f14 | -7.24589 | -44.77946 | 2025-05-27 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8379c675-bb4b-386b-bd27-50cfbcf40ed5 | -7.20796 | -43.11762 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e96affe4-924f-35c9-9078-64b779e310c9 | -11.05698 | -48.85441 | 2025-05-27 04:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd173e7e-c5c4-31af-bbac-53f7c1d879df | -9.03597 | -47.74329 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b15d12e-4576-34d4-a655-4afc6e58320e | -7.18359 | -43.25352 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 703ab65b-bc7b-3305-8d11-067a2c4629cb | -8.94979 | -47.60643 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3385f22c-fef5-3ecf-a466-a4f82e016cf2 | -15.52699 | -42.64862 | 2025-05-27 04:29:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f4771506-3997-35e0-b4c3-b4e72070473e | -14.15199 | -45.47483 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79d7c1b5-b29a-3621-89e5-d25a224470d7 | -14.14551 | -45.46968 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85a095c1-d517-320c-9eac-639c6c81d746 | -14.69681 | -48.11322 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01660f6d-0e9a-32c1-90de-7526a8920692 | -14.0172 | -55.1338 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40f39724-02a0-35a6-b9ea-6d243782ce49 | -10.8325 | -56.95491 | 2025-05-27 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbf81d2c-3d17-3b97-aba5-952ef1d4b7b4 | -12.39955 | -49.97847 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2dfd779-7e39-305c-8bc2-0cb9ddfffcdf | -14.59167 | -48.35221 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39a28c86-d143-3020-80fc-3676655ce402 | -14.26063 | -45.69135 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9febd61-b2f5-339d-bc95-c00c0e50c38b | -12.12363 | -54.67068 | 2025-05-27 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cd2018e-06af-3a63-9c0a-5c6e4b54dce6 | -10.83019 | -54.02433 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbc0103f-f90f-389b-a368-2808e5b70540 | -12.34819 | -49.92168 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b1a5223-2a41-371b-bd5c-9df2da796ec1 | -11.62748 | -54.94205 | 2025-05-27 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7bf43b6-a8ef-3c40-b3c1-1bece361ff0b | -10.84077 | -54.0169 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba42a1c3-09e8-3fb0-a99e-2dc2660c8c79 | -12.83366 | -47.38676 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c42de07d-59cc-3c71-acb3-5e299405fd75 | -12.07864 | -47.3524 | 2025-05-27 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46af0655-12ca-38d9-88e8-e7e168a6acdf | -12.36975 | -49.98545 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63e3a3a1-bec3-3d90-bb73-313c8d1f426c | -10.83385 | -54.02979 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15fd4730-a7da-36d6-bbc7-989cfcc699e4 | -14.14904 | -45.47023 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 051de0df-37b9-32c1-ae0a-9d5b63ffd04f | -10.30311 | -57.1446 | 2025-05-27 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7573cd75-91b1-3c3c-905d-e176477a3ec8 | -14.80392 | -48.26987 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26755e01-683d-39eb-a288-3746d5f1a18a | -12.42042 | -49.98214 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 955f4e6d-948b-3039-9e40-9a77b88d32b8 | -16.62736 | -52.13412 | 2025-05-27 04:29:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 111b5cba-03ca-3eed-9edd-87b76220ae2d | -11.40505 | -52.95374 | 2025-05-27 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80739b67-8ccb-3ab9-bf63-0e25a4b1d050 | -14.01741 | -55.13704 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README11.md)
