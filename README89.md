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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 607f53eb-e813-31ce-bbb6-154998507e58 | -3.3859 | -50.33501 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 196edc46-4b45-3421-9e8d-cb4e5aad86c4 | -2.1444 | -46.48582 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a8b0d4f-9c36-389f-894a-b874513bdf2d | -2.97035 | -52.11425 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c2a787-5d43-3d65-a6f5-73c94df1900e | -2.98479 | -53.35885 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6a1e91-e9aa-3ec9-9b43-d1326dd2a825 | -2.61528 | -53.98311 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ef2e54f-f6f9-37e5-aa24-cfdd0cbcd5f3 | -1.39453 | -53.63686 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d04bbd0-6980-3c34-a602-0799e5106418 | -3.7708 | -51.67862 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16242738-4209-36a7-8eaf-dc4b9a3315c1 | -3.11398 | -53.99256 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11dbf79f-b54a-398a-800b-233f1d1096f6 | -2.03224 | -52.07773 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c55661b-5754-3213-bc25-9e3cc689c2f2 | 0.09194 | -49.93081 | 2024-11-30 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb130a62-7247-3b6c-9afb-3a2ac851341c | -2.18573 | -47.14837 | 2024-11-30 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e81878a-4ba8-3e23-b017-e58a3d3854a7 | -1.79088 | -52.73885 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a408ff8-9b63-36f4-8d8f-e8976e4cf2d4 | -1.134 | -53.80754 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49dcb605-b813-35a6-ba4e-b2bd2661e583 | -2.53773 | -47.3637 | 2024-11-30 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1368c74b-f31c-331e-bc7d-72be0fe9eb10 | -2.76233 | -54.04229 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbb8b1c6-aaad-317a-855f-a3b713f347bb | -2.79923 | -54.0371 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4feaa92-4d98-3f1d-aa31-957d21604c58 | -2.53502 | -54.04595 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1b0db44-1f64-3a8b-ba4d-ede8848d6246 | -1.18173 | -53.41621 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e475244-2bd8-3cd6-95de-69879fb4ed50 | -1.70672 | -52.45376 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c4b6c1c-ba1d-3b85-986c-4f80cefb44c2 | -2.7231 | -54.16129 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e4cdcb5-e2ea-3700-a0b7-f80e5373a680 | -3.25544 | -53.86599 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ac0176c-4900-3e2a-93fb-55980d1a3907 | -2.84877 | -54.02683 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37111b89-b00d-3528-9075-ed27d0e3fcb6 | -0.98289 | -53.67383 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6afe61f5-fbdf-3249-934a-47fa0962baa2 | -3.34873 | -46.29738 | 2024-11-30 05:01:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dc850ea-b24e-30a7-a00d-c13b45d7a7c3 | -1.16465 | -53.56887 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8969554a-ea31-3f45-ae07-5947e9b462ce | -3.03959 | -51.78051 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69d17844-7f6d-3c48-ab1f-6c91a897019b | -2.26087 | -50.35537 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 450a06fc-a3c3-3814-89a0-9dfc820fe6e8 | -1.45416 | -52.61579 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef45b55-cf61-3290-acf7-6fcfe9ff720b | -1.70548 | -52.76743 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0ec84b4-efb7-3d51-98f8-c8755a416c05 | -1.75798 | -53.64248 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a4e7b9-fd08-3d73-bce8-53c5a09aa14c | -2.80078 | -53.04202 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e5639fb-3360-3da2-b2aa-6204f89c01cf | -2.83655 | -54.03928 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02c29ea3-e389-372b-bacb-703acf4cda78 | -0.76229 | -52.45895 | 2024-11-30 05:01:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4059d45b-07a3-3ca8-99d3-128231a107ed | -4.67809 | -48.15126 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cfc7803-6973-3451-a2d4-8395ecea96e1 | -3.71189 | -47.14852 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d440aa62-2e42-3a15-9487-0645f2a5d39a | -1.1329 | -53.81453 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 360f0c04-8e57-3d9d-92b9-3863e7c4ca47 | -1.9513 | -53.34134 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 083b82b8-ba40-3c57-b1d8-fbb334f9a435 | -3.11083 | -53.26971 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9abe113b-8a10-3045-8f1d-971ffef40c6f | -2.83634 | -49.8868 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db05f4dc-4068-3b96-bca4-10570ce4bf45 | -2.87269 | -54.00541 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26b3f1dd-3294-3853-a96f-89513aede29e | -1.04413 | -51.73556 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6afea3e9-2b16-33f1-a9d4-5e9b58a0fd1a | -2.29701 | -50.68633 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f84f11bf-c429-38c6-aae8-fc40edb27198 | -1.64538 | -53.86887 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 67fa7954-18c1-35df-ba7e-0c9ee489a1a6 | -2.06526 | -51.18837 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 877d128e-e42a-347b-b072-5f4f5149a0c0 | -3.09349 | -50.34658 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8be72bdf-d56d-3be7-ad43-f508eb34bf6c | -3.24106 | -53.64164 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d12d929d-5fd8-37f5-95c7-d7b5b282b282 | -3.85756 | -50.12051 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c883ad1-09fa-3f3a-8394-2e9e9c3cd726 | -2.97341 | -53.88038 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9c63c31-a2b8-3039-9c23-3e83a3e3417e | 1.67361 | -50.66714 | 2024-11-30 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7f2f4db-8baf-3ab7-82cd-2337c85dacc7 | -1.17054 | -51.94012 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 196649b0-8860-3a54-8ec8-ecef04eb2b13 | -2.00972 | -51.19065 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b49e8ed0-b8a4-3bf3-b873-8e43acfce5dc | -3.20537 | -53.37706 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba37894c-43b0-368c-a8af-35c9eb1c18ca | -3.24778 | -53.42092 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1778706d-412f-3728-8691-ea867f1dde82 | -0.9648 | -51.6466 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2de3746-9314-35b9-bb26-8c899a728d5b | -3.35961 | -51.54304 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 727ffd5e-6877-3b2b-8b1a-3d542197ea1e | -1.00213 | -53.69822 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8819c15b-b515-35cf-bab3-2af1d7bf740f | -1.48918 | -54.45433 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdbe321b-8a12-356f-a1c2-21c19cd2f15d | -2.58661 | -54.0788 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 200ce091-7ae8-39dc-879c-9a02f54a65e3 | -3.12489 | -46.0482 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aea2e52-b178-3791-aaa0-f9c80c252154 | -3.22446 | -54.17467 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0343f64e-f50b-3cea-bd5a-fadd071dc446 | -2.64154 | -49.91217 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed709a2e-00b9-3d05-886f-a19223bc0924 | -1.74408 | -47.35312 | 2024-11-30 05:01:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f10b3167-930b-35ec-a036-e3d6eb98a197 | -3.06915 | -54.41111 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d41a800a-9f1f-364e-ba7c-1d8576c494e5 | -3.14767 | -53.84211 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b98c6db-c7d3-3f92-9984-c80a9a41c302 | -2.72344 | -52.98124 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a10b22b-5f75-394a-9359-823cfd067dd7 | -3.83143 | -46.46922 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9face3d0-47ad-37b1-805f-bb512fdf174b | -2.7496 | -54.07971 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ea09f81-2b5d-34b3-be4e-7265d1ea285e | -1.30044 | -55.74061 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43ced23a-5f13-3281-ab41-b4c12873723b | -1.24216 | -53.36027 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2317ea42-5d2e-3ba6-804e-24a344ec7ccf | -2.94099 | -51.00899 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32ea2946-1ba2-39a0-ad52-98667dac76b8 | -3.10673 | -53.80642 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b8ff144-0c30-3a8a-b778-fd55c2ef55a3 | -3.79725 | -48.96704 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8922900-2dc5-3c37-bc97-4eba5fabf1a4 | -1.92096 | -52.65908 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 747f05f3-21e7-3c70-9911-05db14fe2859 | -0.22805 | -53.13168 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40df81a3-e7e1-3911-b5e7-651d743ba31e | -3.09244 | -51.40819 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 97d7e52c-fcca-364e-8f24-010893566a3d | -1.60174 | -53.82639 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6901101-15bf-3e89-b866-7890e30e42fb | -1.19934 | -51.75354 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9de9f580-edde-3beb-93b5-7a4d4d333724 | -2.7586 | -54.13115 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f74ea48b-4dbd-3ab7-ab88-0ade231d440b | -2.29555 | -51.98528 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cefb132-fe37-367b-b19f-0b6f96cabfd5 | -2.96438 | -48.03752 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c20647fa-d072-334a-af37-47c320a1f1b7 | -2.57963 | -53.67466 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9c6dd15-8f0c-3e9d-82a6-ff9d8745e394 | -2.59666 | -46.5672 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57f6a4f-9f0a-33aa-801a-298d24efd852 | -1.71818 | -52.68572 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b64a3d-6948-3c31-84bb-d7083900a218 | -1.26822 | -51.82555 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2192c420-44c8-3423-8436-404b919c5742 | -1.37614 | -53.64487 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3133af2-96bf-3538-8879-a57ee951c79f | -1.5325 | -51.61568 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f96c8ff-994c-3d4c-920d-9446203d5d7c | -3.14085 | -53.72086 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0401615-6a21-33fa-883d-5473607e23c3 | -3.30827 | -50.3785 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| def28f2f-d308-34cf-a1f1-3f4eacf83db1 | -3.58297 | -53.28398 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73521a95-9e9c-31ff-8c98-95a0d54490c6 | -3.01228 | -53.22865 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aee95a17-4ede-3ad5-a53b-19ae6f838b4c | -1.49972 | -54.94649 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ba8ebbb-8950-3614-8f89-75823348ecc0 | -1.15052 | -51.70217 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65a85521-5354-35ea-aaab-fa3b0cace690 | -2.71664 | -46.1271 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cefe2134-38d5-3116-9b58-0295bdad3163 | -3.81415 | -46.54272 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ae3b3df-03eb-37ef-8b20-7986f2172aab | -3.3529 | -49.75798 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 889ac584-63b7-331f-bf9c-8c1d24cc008b | -3.18937 | -54.33351 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cd48d73-23ea-3801-91ff-8f3accea7048 | -3.55354 | -53.54094 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 084c661a-60a2-3528-8731-2d7ee0b62dd2 | -2.6309 | -53.99265 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1caf90ce-e3ab-3ee1-8b62-b0a6bf5a19aa | -3.73964 | -51.83122 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb0f1e65-600f-3446-83aa-2c2beabcf5c3 | -1.04976 | -53.18532 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README90.md)
