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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caa7a472-93fb-32c1-95d0-3ebeb50d3e9f | -2.2445 | -48.3802 | 2024-11-11 04:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c0b07aa4-7895-3253-92d0-4e000e7df4b3 | -17.2936 | -57.4652 | 2024-11-11 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 0bc1533f-4895-3207-8c44-6d7ac91f438f | -2.2075 | -48.3811 | 2024-11-11 04:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6dbf58d2-1b42-3b3f-8f8c-90c4284011e4 | -2.2298 | -53.6623 | 2024-11-11 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| a397bc23-f12f-3d32-9830-c3616f599c39 | -17.2933 | -57.4857 | 2024-11-11 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| c15edc28-814b-3d23-b396-5c6a20253140 | -2.2444 | -48.4017 | 2024-11-11 04:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b1c5e684-9af3-3bc7-85e3-e3ceae5b1c82 | -3.5346 | -45.7061 | 2024-11-11 04:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 75ae5a95-9509-349f-84b0-7335b62afacd | -3.1458 | -54.4859 | 2024-11-11 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 13ed5a73-5584-39e1-9b47-9db08a3ac754 | -1.4057 | -52.3758 | 2024-11-11 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 366599b8-2593-3baf-bca2-e73363d3c111 | -15.9982 | -59.3649 | 2024-11-11 04:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ad8f6a0d-e006-3b5c-ad7a-9c0e43dd2b81 | -2.8857 | -45.3726 | 2024-11-11 04:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 653a99dd-ea6d-32b0-b07f-0df5605a5184 | -2.2482 | -53.6619 | 2024-11-11 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 908ba1d9-50d4-3e99-97de-3c1f23e75d41 | -15.9985 | -59.3449 | 2024-11-11 04:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0143203b-cd44-33fa-980c-968c82ac5521 | -2.2297 | -53.6824 | 2024-11-11 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a57f47b6-d454-34d4-b78b-42520bcdeb1e | -2.189 | -48.3815 | 2024-11-11 04:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ddbc9d92-4a88-39c7-a96c-0e0e8ef81828 | -4.7023 | -46.3842 | 2024-11-11 04:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 87d7fc6a-a47f-3f55-9750-05e84123188d | -2.226 | -48.3806 | 2024-11-11 04:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 3d4fc269-bb52-3868-9557-9e5aee2d9d6f | -2.248 | -53.7426 | 2024-11-11 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 0642d396-9b7e-3c37-a262-87a0d7a66650 | -2.30522 | -53.81712 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92ec17ae-f7e1-3a68-ae0e-16e0b335ae93 | -1.61568 | -52.39655 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffae7726-2d69-3a8b-b119-b46c8a35543e | -2.23974 | -53.67026 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 438532ed-a935-3bb8-87a6-850e38cd7799 | -2.07035 | -53.29086 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f10727e6-b6e4-3b68-a849-1536f7332848 | -2.43052 | -48.79549 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6af0d2b0-5d8c-3cf4-a6e1-bb5ba3d019d9 | -2.4017 | -46.51155 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f9acad-ae26-3d1f-815c-995b4aaa094f | -2.59062 | -54.24607 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f7a0017-230d-33f4-8e92-8abce501c440 | -3.96071 | -46.71008 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f84ceb5a-add8-3bb5-963e-1ac4fef96260 | -0.04152 | -50.78263 | 2024-11-11 04:18:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91aa6ca1-422e-3d3d-8db5-faaa2b42736f | -2.59617 | -48.318 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bbb2efd-4f37-3dde-a0d8-e66e346d5f42 | -2.37861 | -50.32994 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa5a135-424e-383c-a1fb-43b50a070c0f | -1.6567 | -52.64693 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 264540b2-23e5-37ee-916a-c3da4a7c6100 | -2.66066 | -46.78289 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ac113a-e616-3556-89d7-cf529ef6d410 | -2.08663 | -46.22359 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f9bd599-a97e-3be4-bb58-2a65ba1600c4 | -3.53737 | -43.18114 | 2024-11-11 04:18:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18c70327-69c3-3339-b911-ce739ff7debc | -2.16924 | -48.43395 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64a6adfe-53f4-3ebc-9754-09b4f193b03a | -2.63044 | -49.4773 | 2024-11-11 04:18:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 148ed640-db03-36db-9b73-0b0ddf888b9d | -2.59771 | -51.72006 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 727f77ca-36e1-3232-bd8a-d0fb1cc792a5 | -2.25197 | -46.51795 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e4ee4a26-dbb5-374f-a9d4-6411ea8cd110 | -3.01831 | -53.25065 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 373b3810-15fa-3fd8-80c9-a250ee56e073 | -2.26028 | -48.4538 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62227cda-7183-3b2c-97fe-ea015b455bf8 | -2.86414 | -47.89684 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ad4717d-6822-3984-b8d1-cb287290f402 | -2.1684 | -48.43911 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19fb2c48-bb20-30f9-885f-ad227a776288 | -4.14165 | -48.98025 | 2024-11-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fbdda5d-3909-3140-ab1d-562196dccb26 | -2.39155 | -46.7609 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ed82036-06a1-3b83-a6ed-cfc6aeb63aba | -3.2106 | -45.22752 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aece7fcc-21cb-3db4-a800-fecd7fe691ce | -3.2463 | -46.44171 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f509b11b-112d-34e7-b4fc-8cdc42dcbf06 | -2.26258 | -53.74617 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8506e99c-37a0-389a-9dd6-5c9ae9f3de1f | -3.82818 | -46.5257 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36cf190a-d677-3ab3-b723-2821b8eec47c | -2.67835 | -46.81093 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0d2f508-0a9e-3ec5-9eb9-42017d28859b | -1.25223 | -55.77232 | 2024-11-11 04:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 777cec21-4f0b-3b64-96bb-b2d4549354d2 | -3.0308 | -50.97697 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2b88b48-1f55-3000-93b0-82e478559ccb | -3.76032 | -40.82871 | 2024-11-11 04:18:00 | NPP-375D | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1eeea626-1403-35a1-880f-710ae52c3d4e | -3.56954 | -52.30494 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 78d25719-9889-3e09-bdce-c966217d9dbe | -2.40462 | -46.51614 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecd25bab-0efe-3abc-9382-39a4b47bf78a | -2.36588 | -48.8891 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61f63e5c-3e6e-38ae-8c75-90ee90cc6cf5 | -2.16597 | -46.42667 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50f813f3-5647-3d59-a179-21c0fb275c82 | -3.83567 | -52.31065 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74e16b7b-093e-3aa5-9039-b2f1f6f04758 | -2.34099 | -46.54748 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91b5155f-6e4e-31af-a414-cc822eaf53b7 | -2.54256 | -47.32628 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99b773ef-4bb0-3240-83f0-e7d3296f7fcc | -2.19279 | -46.58008 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50191cf0-4ab7-3e6e-94c3-6b598deea1f5 | -1.39107 | -52.36573 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15fa6f6e-7dd4-354a-8283-afa09b24a580 | -3.14056 | -45.97285 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e00eb018-d1f3-38ed-903a-908d2b8aff0e | -3.23785 | -45.38306 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73198065-8073-32e4-b4fd-56fdc8b1d6a0 | -2.40389 | -48.93227 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31863368-65af-37f6-9458-09a5af7b04d7 | -3.87935 | -52.39349 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fc59436-2568-3e68-8467-f678a4661ec6 | -3.10941 | -45.96793 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d3c0e9-6567-31c5-9b9b-95cad505ff6d | -3.23645 | -46.52514 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f61e848-13cd-3a99-9024-c25dd0c1a785 | -2.3653 | -46.73976 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 675daa87-c208-3d2d-a0b5-dc6385554496 | -2.25279 | -53.7434 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2d9b1001-03c5-301c-8a04-61d12c3f5f28 | -3.23885 | -46.305 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 961de68a-5d4c-316f-9833-efd2f2f97284 | -1.41998 | -51.1027 | 2024-11-11 04:18:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6d4ac4c-540a-3c40-a2d3-4f4bd4a65c2c | -3.87695 | -52.39074 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79c90554-84a5-3cf2-b2fa-3702a0f32dbb | -2.36034 | -46.7941 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 662566e2-6c3c-34d5-a45a-d4b79bf995a7 | -3.5225 | -53.50271 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 387352d6-d02b-3f50-bf26-347c523c1973 | -2.09767 | -46.52014 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29351e8a-4b85-3e14-b5ca-05d71becac53 | -3.96198 | -46.70224 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f56605a-69bc-35c7-a7fb-57a9ddd8f727 | -3.68383 | -45.23892 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24b4395e-866c-37ee-b962-8e4f57ab7dd3 | -3.10655 | -45.96363 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbd6f6ae-dbc1-34fc-848f-a941ba89699f | -3.11859 | -45.9771 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12122e59-64d8-3fcb-8595-8b03c4714e11 | -2.47089 | -50.39878 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b6aeaed-8c82-3051-8acf-90af2eff5886 | -2.98661 | -46.98365 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 44ac85ae-5e3b-3456-a933-d647fcc599fc | -2.37937 | -50.33252 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ea2a4f8-5184-3cf1-862c-b4911f701caa | -3.59318 | -44.55124 | 2024-11-11 04:18:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7913850-2ff1-3fac-ad22-a8f94a6230e2 | -2.91877 | -45.63355 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de29f3bb-195d-38cb-84d8-5780f0b9c975 | -0.88988 | -51.78696 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cea00285-dc44-3044-9568-36db737c276b | -2.38385 | -50.32616 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f97232a-effc-36c7-80b9-354e11db732f | -5.27128 | -45.73027 | 2024-11-11 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c2e90f4-cfc3-38ae-882a-ea251299949a | -2.22837 | -53.66829 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 23b23b05-3016-3f77-ad8d-4f7db98acc1a | -3.11011 | -45.28558 | 2024-11-11 04:18:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c52d832-e673-3bf3-bca1-0404f02e731e | -2.36709 | -48.57171 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a25e883-dfeb-38d3-bd75-4f1d5d82d84b | -2.54566 | -46.30862 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de9e1d0f-827a-38a5-9623-97043c8b371e | -2.18662 | -46.38894 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a37dceeb-52ff-3e16-a10e-a12bea2d2094 | -3.24124 | -45.3836 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8c683e30-3a58-30da-b73d-7676d2d79fcc | -4.13163 | -38.70562 | 2024-11-11 04:18:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e626bcf5-6c9e-3edf-b2e2-c0ef470918a9 | -2.9943 | -49.52023 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b814b5ed-d3e4-3105-9b14-bb72aa9edd5e | -1.61622 | -52.39331 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bc29f07-31fd-37c4-9ea1-bdb55c62450b | -2.30835 | -49.11558 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9f19604-65ee-3a45-a4d5-4fbdb3832224 | -1.65778 | -52.6402 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4859bfb5-c0e1-311a-81c4-e16ea2c07450 | -1.56326 | -53.42196 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dee3f02-e64e-3ec1-9b03-4df14c367193 | -2.26421 | -53.74535 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8be1b1a2-331b-303d-a8ff-3bdc6726cb8e | -2.32048 | -47.43112 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
