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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2390fc17-b5ec-3017-aa62-bdd8ef4594bc | -10.8097 | -43.951 | 2025-10-14 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 7e23b25f-5d5e-37bd-941c-3992bf387dc3 | -11.525 | -43.516 | 2025-10-14 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e8cc4cb4-b726-32c2-bed8-8de3265a1e0f | 1.8768 | -55.7029 | 2025-10-14 12:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 2ad7151d-cf3c-38cc-acaa-6dbe159b52e0 | -11.2862 | -44.0226 | 2025-10-14 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f27e2807-688b-3903-aaf6-5d739c14a53e | -10.8285 | -43.9717 | 2025-10-14 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2261a145-4059-3c99-9e1f-f83cbd2bf9ea | -11.5062 | -43.4952 | 2025-10-14 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 35cc6117-6d22-338f-97dd-60caaff3472f | 1.8768 | -55.7029 | 2025-10-14 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5cdd4a6f-68fe-3825-b0ae-303fdbd735a2 | -11.4389 | -44.0468 | 2025-10-14 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 41d77e17-ed73-3d90-b499-cea5608df174 | -11.525 | -43.516 | 2025-10-14 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 0ae7a394-2303-3d02-9fff-a8aa01226b5a | -11.5058 | -43.5189 | 2025-10-14 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e63cd36a-edd1-38f2-af62-106985e91576 | -11.5255 | -43.4922 | 2025-10-14 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 74da9f17-29b8-3f2a-a4fa-62ff84365983 | -12.9188 | -47.0626 | 2025-10-14 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a3e39ea2-1802-32b1-82b5-63324e98e96a | -10.8093 | -43.9744 | 2025-10-14 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| be2f2fe4-64b6-3dc5-b1d1-dd39058f66f9 | -10.8097 | -43.951 | 2025-10-14 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| c054bd69-538d-305a-a864-823a2a3d16aa | -10.8093 | -43.9744 | 2025-10-14 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 196.3 |
| f4725e40-4c1a-3219-8014-8c9ed23b5ece | -10.8285 | -43.9717 | 2025-10-14 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 361.5 |
| 5b5d8cdf-476a-384c-849a-e509ac55304d | -10.8097 | -43.951 | 2025-10-14 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 249.8 |
| 81ad59cb-d8c5-3952-ab8f-4debe9d47ef6 | -11.3817 | -44.0319 | 2025-10-14 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ed08265f-f81a-3ef9-a652-531c1c3e156c | -12.9188 | -47.0626 | 2025-10-14 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 35d7c2b6-8abe-3448-98d4-6120223d2fb0 | -10.8281 | -43.9952 | 2025-10-14 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 7c8a2694-7ca4-3063-a8cf-b76918330315 | -11.3821 | -44.0084 | 2025-10-14 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1de62ebe-8421-3cbb-99e5-0ad1afd87a8a | -11.4389 | -44.0468 | 2025-10-14 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 164.1 |
| a52efff3-a48a-307b-b633-10c0d132f11a | -11.5062 | -43.4952 | 2025-10-14 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a316bdb3-0c31-30d3-99d7-0bdbb6227702 | 1.8768 | -55.7029 | 2025-10-14 13:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e710c5e0-7cbd-34bd-9226-29fff78f4834 | -11.5255 | -43.4922 | 2025-10-14 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 099ba5f5-9512-35a3-86c2-d6fae0df00cc | -11.5058 | -43.5189 | 2025-10-14 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 0a53a373-aa5d-34d4-96f3-fb70218d2fda | -11.2862 | -44.0226 | 2025-10-14 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f0fab40a-2d53-38cd-a27a-9556bcf21593 | -11.525 | -43.516 | 2025-10-14 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f18062c0-168a-3797-9f04-69f495a5faf4 | -12.34 | -47.2362 | 2025-10-14 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e0b3caea-b097-3645-a138-6d85c00f8edc | -12.9192 | -47.04 | 2025-10-14 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 385e43f9-f6bc-3b69-9046-5b80b6187e43 | -11.2862 | -44.0226 | 2025-10-14 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| df6fb6e1-0c30-31e3-ac23-4725918758fa | -12.9188 | -47.0626 | 2025-10-14 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| bf4cef4f-1ece-364b-bbd6-e6297a420b30 | -10.8097 | -43.951 | 2025-10-14 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 248.7 |
| 8d5ad275-3d23-3004-8950-ce8f0c649e13 | -10.8531 | -47.1648 | 2025-10-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c572f94f-8e79-3bb3-bcd5-465164688f3f | -12.8995 | -47.0655 | 2025-10-14 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 94a041d7-98c0-3c44-9d4e-3baf6fa85e1d | -11.5062 | -43.4952 | 2025-10-14 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c7ee7ea1-8743-34fe-abf6-bdc5f45e0506 | -11.5058 | -43.5189 | 2025-10-14 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 234c1069-dc64-34af-b935-0601693d21a1 | -13.8122 | -45.7595 | 2025-10-14 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| c282d49b-e30e-3f3a-8002-0613cc4ce988 | -13.094 | -46.9461 | 2025-10-14 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 0423e299-5116-32d8-95aa-18158685459c | -11.4389 | -44.0468 | 2025-10-14 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ec61e3b9-c31f-3563-b2a8-bf40214ae230 | 1.8768 | -55.7029 | 2025-10-14 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 099886da-235e-3915-990b-b1117053a9bc | -12.7299 | -45.8422 | 2025-10-14 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 72e5c27b-47ce-3d89-9b3d-7d737bdd2764 | -10.8093 | -43.9744 | 2025-10-14 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 39b6649c-2f7f-3924-8934-59de52c50eeb | 1.8765 | -55.8805 | 2025-10-14 13:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 32107ec3-d8ba-349c-be88-c0a3c79506a9 | -11.525 | -43.516 | 2025-10-14 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 47c19b5a-36f2-3443-81d5-fea5046a2a52 | 1.8768 | -55.6832 | 2025-10-14 13:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c9ac9bdc-05e0-3283-9133-bb559a9d3719 | -10.8097 | -43.951 | 2025-10-14 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 1693241d-ab60-39e2-9be5-7a26f18911dd | -11.3817 | -44.0319 | 2025-10-14 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4ad002a0-aa7d-3dde-8c26-89382c7b1a2b | -10.8093 | -43.9744 | 2025-10-14 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| a63cb5ae-10aa-3a54-9d9c-b36ba6fd8fd8 | -11.2862 | -44.0226 | 2025-10-14 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 856be674-d551-36ff-bea4-f14d7ead320b | -12.8995 | -47.0655 | 2025-10-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| e6a3bf42-68ff-31d0-b3bd-9a0076581202 | 1.8768 | -55.7029 | 2025-10-14 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| bda8bf2a-9f79-327a-98af-9621c76ae427 | -12.0118 | -45.2161 | 2025-10-14 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 333ae572-a6f1-340e-82da-e28f58da1694 | -11.3625 | -44.0347 | 2025-10-14 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6652b053-b729-3592-97dc-99b056976521 | -11.3629 | -44.0112 | 2025-10-14 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 40878eb6-dd4f-327a-b9b0-ee1e2aec73b6 | -12.9188 | -47.0626 | 2025-10-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| e2cbcba6-c606-36b7-a30e-cad7d9ea4e32 | -13.094 | -46.9461 | 2025-10-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| fff929a7-2b74-3e19-a80b-eb9e4072b61f | -12.7299 | -45.8422 | 2025-10-14 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2e210331-020a-3ae2-ba96-de0ac23b47f5 | -10.8281 | -43.9952 | 2025-10-14 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 29d7197b-6b70-3551-97d1-a617e2332171 | 1.7667 | -55.8031 | 2025-10-14 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| cebebd0d-0f3c-3119-9ff9-8c5fac5e0f31 | -13.094 | -46.9461 | 2025-10-14 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| ad549912-b0d1-3189-bde6-2f3715a7390f | 1.7851 | -55.7831 | 2025-10-14 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 711bc274-49f2-3482-aa61-b2e6ff42a1f6 | -11.4389 | -44.0468 | 2025-10-14 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 0ae0b106-5f43-3161-8fd8-bea7bf55eb3b | -10.8281 | -43.9952 | 2025-10-14 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1ab04b30-1ca4-3c95-ac04-225f3d9bd844 | -12.7492 | -45.8393 | 2025-10-14 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| fd77113b-f5f0-3134-91d9-3b7478891002 | -11.487 | -43.4981 | 2025-10-14 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0d63c57b-7dc5-3d8e-94be-a33b7c116a91 | -12.9192 | -47.04 | 2025-10-14 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 484f008f-34b3-38d6-b9d3-a8e3ddd70136 | -10.8097 | -43.951 | 2025-10-14 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| c124b96c-70eb-3a0c-b700-e40630d31d24 | -11.2862 | -44.0226 | 2025-10-14 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 503cb7fe-bde1-3a5e-815e-d65c8feec0c8 | -12.34 | -47.2362 | 2025-10-14 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 1356959b-89ed-3be9-b629-3ead9167a1a8 | -11.3629 | -44.0112 | 2025-10-14 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0fc34431-0eeb-3b24-b00e-9797e84327e9 | -11.3054 | -44.0198 | 2025-10-14 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d6aaf2c4-f5ed-33c2-bbd0-a4eae33744ab | -12.7111 | -45.8223 | 2025-10-14 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c63aabf4-913e-37cc-9d96-c3658d0606b5 | 1.8768 | -55.7029 | 2025-10-14 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ed5e5e04-ee6f-3bd4-8d80-22a00b1491a4 | -10.1524 | -44.552 | 2025-10-14 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| fcc03305-f5fa-3333-8382-37fffb50e9cd | -12.9188 | -47.0626 | 2025-10-14 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| a088bede-80fa-33fb-b5f4-b1af1f35b6c6 | 1.8768 | -55.7029 | 2025-10-14 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 8eaecdf0-3e32-3c85-8f69-7f5c514b7822 | -11.5058 | -43.5189 | 2025-10-14 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 2143a705-d573-3cc4-bfb7-b899c4e491ec | -3.3812 | -43.039 | 2025-10-14 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| aea67d90-14c2-3c2f-98d3-8a01cd3da3d2 | -12.34 | -47.2362 | 2025-10-14 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 71b994bc-0b35-3a0b-b3f8-827183e19632 | -13.094 | -46.9461 | 2025-10-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 144.5 |
| fe59eeb2-dd49-35b9-bb90-8e6f88cfaa45 | -12.8995 | -47.0655 | 2025-10-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 3d3df65a-951f-38d9-8b3d-00e54483d493 | 1.7851 | -55.7831 | 2025-10-14 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2aa2106d-d49d-3dda-935e-8e9ef2ad511e | -11.5255 | -43.4922 | 2025-10-14 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 5d9e3bd2-9ada-31b8-a3b8-407f35925ac4 | 1.8768 | -55.6832 | 2025-10-14 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d5766c53-5ca7-34bd-bf77-31742d463042 | -12.9192 | -47.04 | 2025-10-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f4365b4b-8ea0-3b93-9b72-e51fc25e4010 | -10.1524 | -44.552 | 2025-10-14 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| d6f813fd-2fbf-3328-b4ba-cc30b1bad1f7 | -11.4393 | -44.0233 | 2025-10-14 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4181c156-5383-3896-88c5-eace7500b6e8 | -11.525 | -43.516 | 2025-10-14 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 271d8055-9496-3ef6-977d-97b4cb45d35d | 1.7667 | -55.7833 | 2025-10-14 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ca35ac9f-14d0-33fa-934b-29495b628382 | -11.7809 | -46.3687 | 2025-10-14 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 116a62c6-116b-3332-9a49-88ef510d57d0 | -11.9211 | -44.9293 | 2025-10-14 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 8bef8101-7695-3392-8201-49e3451a29f6 | -10.8097 | -43.951 | 2025-10-14 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| cddd12da-97b1-37e3-a83c-c7f96ccc38d5 | -13.0747 | -46.949 | 2025-10-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 4e089ccc-f9a6-3feb-807e-e2646e80686d | 1.7667 | -55.8031 | 2025-10-14 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 989bf8b9-b42c-37fe-8313-e72035d8b3fa | -12.938 | -47.0597 | 2025-10-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 75f4fcbc-7b51-3eab-b2ef-029d463846c5 | -12.7111 | -45.8223 | 2025-10-14 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d48b9dec-9756-3ece-a6eb-64078ff117b2 | -12.7492 | -45.8393 | 2025-10-14 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 57f15ee7-9aa0-3835-aa00-84785f72739e | -11.7813 | -46.346 | 2025-10-14 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1f0c733a-0762-33ea-a699-6ac2b2fe8353 | -12.9188 | -47.0626 | 2025-10-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |


[Clique aqui para ver as próximas entradas](README42.md)
