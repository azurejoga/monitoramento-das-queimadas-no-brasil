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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b306de99-186a-3538-9083-b6c50561f949 | -2.82439 | -54.02488 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7db8accd-dbe1-3aeb-83cf-97c876d07fa1 | -3.29449 | -53.85655 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8776052-1d5b-3b26-b645-94c049ea75ae | -4.2011 | -48.1244 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d822813-6a77-31a6-a365-76f057f4e687 | -2.07381 | -52.28436 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0df932e1-5935-3439-9b23-00d86758dc1a | -2.94097 | -54.07922 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11d86434-ad05-3eb3-abee-6533e4fb5a0f | -3.94298 | -47.98179 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1dd23855-1552-30b4-b003-a9d52d69e198 | -1.07503 | -53.35638 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0928d497-04d7-377d-ab85-da0ec936434d | -2.00806 | -51.17328 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67ca3162-8de4-354a-9a91-3442550e322f | -2.62408 | -54.93422 | 2024-11-25 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c957fbd-b661-33b4-95f0-c8d58002ac2e | -2.9623 | -53.87942 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5294eb4d-b707-32f2-acfa-9967b5a6a5af | -2.82223 | -54.08172 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8659766f-1bdd-3580-8d1c-3d418fdaf21e | -3.02293 | -54.05274 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c058014-c98d-32ed-9455-76b281ef5534 | -2.76311 | -54.07254 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79bcacd1-2ff5-344f-8415-bf3f8f01b71e | -2.89313 | -53.95716 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a24c0b0-b362-3e5d-b7ac-38b49cec3710 | -1.38305 | -52.3272 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0aec36b2-b5bc-33d4-a280-651e7e0a9a05 | -2.80764 | -53.0169 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 098e9d90-47f4-30fa-81c6-e9747df2b60b | -2.58004 | -45.32676 | 2024-11-25 04:55:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28efb30a-af92-371d-9111-73d36b066c77 | -3.23475 | -53.93254 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0cb9a85-097e-3b8c-bc22-3b0551b94deb | -1.11598 | -52.11084 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656fd9f0-35dc-30a2-8f11-ae26ebd78756 | -0.97344 | -51.70804 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 484802e7-fc4d-3014-b2d4-46e4fb64964d | -2.76699 | -54.06956 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7617e4e5-77fe-345f-b73e-75a0ba9b03d5 | -1.28795 | -51.73072 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d426de5-7b6b-39c9-a871-f211dec27b4f | -1.329 | -52.80007 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6edd9699-d737-3fca-bbee-5250a276a30d | -0.87441 | -51.72527 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db3a86fc-7cc4-3229-88ce-9da67682b1fc | 0.39925 | -51.71507 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33cc67aa-d9af-348c-9d22-18f3929b6e7f | -1.72087 | -53.2528 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67c506d7-e711-36ee-997f-912611231d3c | -2.18683 | -53.79704 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c280965a-0de6-370d-83e0-27ec82057e39 | -2.64118 | -46.85455 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93f0dd95-3ea7-3e2d-9b38-46727a6e45ac | -2.45235 | -53.70319 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11303b36-59eb-3cb6-a2b4-3498b77d4ff4 | -1.04237 | -51.74031 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e69fb170-b01f-3f76-89ab-dcc80916d219 | -1.98662 | -53.13525 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e79c0b68-86f2-3a27-a82f-8a45fba1a573 | -1.88557 | -53.3279 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a7db21-24ac-3c42-b943-44cfcb13c3b1 | -2.80221 | -54.07859 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b76509d0-86eb-386c-a3aa-d64a7d94cea7 | -3.54626 | -50.39829 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44bf3ff6-1e31-3ef0-9dac-b4ef263510aa | -2.84326 | -54.01356 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41682d68-9e69-3f94-8270-a56f4be2e1a8 | -1.2745 | -52.69278 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d788706-4d17-371c-8c68-a24d8f34d242 | -2.54627 | -54.30507 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc7fd550-6878-3fa0-8ba6-b355efd382c3 | -2.57854 | -53.9724 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9792da7d-4440-33f6-a7ce-b0ce3f376150 | -3.23179 | -53.63075 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fc241a2-b539-3148-b1ac-66514d684fa6 | -0.27406 | -51.49836 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee046b16-3f4e-3419-a028-a36591f1acb7 | -3.51505 | -53.80992 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c1d59d7-ff45-36fb-94d0-f4a1935a7e55 | -1.73605 | -52.32101 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b655c19-838b-3ac1-aa09-b70f0b24819b | -3.67959 | -54.58298 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e058e7bc-acc1-313d-92f9-7bd2cb462489 | -1.91996 | -53.00155 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9762ba9-90bf-329d-b4e8-e0f7f4bb9251 | -3.85198 | -52.15257 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba0354f0-764f-35e2-8756-d624cd8037ae | -2.90804 | -51.71058 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c473c607-4fe1-3df4-99f7-870fe4800919 | -2.91144 | -51.71111 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 193ce061-eac9-3f65-9462-d418820a358d | -3.06518 | -53.22691 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ed70717-a0df-3588-9fc2-b0f6b6d65696 | -1.05997 | -52.37956 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f3dffe5-3fa9-394c-b011-c95e01d7b699 | -3.51833 | -53.78917 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfe46893-67c6-3f22-a170-87ba992694f2 | -2.84323 | -53.99213 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21aad416-8c23-3912-8297-87aaeab90008 | -2.24582 | -53.61795 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d6eb97c-2e43-33f8-8ef7-bb43194d365c | -3.12278 | -51.29342 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f915b07-677d-3cbc-b8cb-b44eb1abaff8 | -3.80995 | -51.99544 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262c74ca-38c0-3800-8d58-db11b3e72dc8 | -3.25842 | -53.2675 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 621fa39d-f120-3809-8806-bf15a94f7e30 | -1.24237 | -53.39365 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef61eb7-fd7a-3734-9474-8ad4dbd17f0f | -2.71135 | -53.17503 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d232d40e-4c97-3f24-bc5f-f8892df26a44 | -2.97224 | -53.85965 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc633961-90f1-3fb3-b788-3adbfd0866c4 | -1.33318 | -51.40057 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb93449a-892c-3037-acae-f0792dd1e521 | -0.7417 | -51.94899 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66318ee3-6686-319e-9809-e96e7e0607c5 | -1.04573 | -51.74083 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c93a31e-ffd9-30c0-9813-3c8df6e50720 | -3.16877 | -53.64215 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca3a708c-5470-3dd8-b244-2be6df167daf | -1.42937 | -51.11961 | 2024-11-25 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72d830c1-0769-3ab8-bb61-ad3ccbd7f5ea | -1.19545 | -51.96913 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47365973-bd0d-3dfe-80dd-4d92cc0d5e6d | -2.81556 | -54.08068 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3148b07b-bbfd-39ab-a94d-d164e90f07ad | -3.58126 | -52.18434 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c51dafa2-a275-3ca0-8c75-3472d5e4c96b | -0.94098 | -51.7175 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc9d633-b711-3541-a5fc-44cd311c9e68 | -0.36382 | -51.41031 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4783187-fc23-3916-811d-661f6f489d50 | -0.73781 | -51.95197 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33972988-3bb7-3769-998c-f028c36f54c2 | -3.94603 | -47.99015 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0122d987-aa68-3da4-a0ae-4457b8e39da5 | -1.07237 | -53.1792 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f744816a-e8ed-3ff2-ae53-2fbcc3ab460a | -3.28917 | -50.51958 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd532e75-614c-3bef-9028-797197771ba9 | -3.51783 | -53.8139 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20f6df77-f2df-3a24-a324-0f6fd56a7669 | -0.10143 | -51.74265 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a37a626-2122-38f8-833b-e3107dab6398 | -2.8588 | -54.00171 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92c2ce81-730b-3ebb-b35e-3df9c9781937 | -3.49164 | -54.02287 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 308a4437-f999-3cdf-b306-6d7c335d63b2 | -4.24505 | -48.70334 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5012ed7-32d2-329e-98df-ef127ef82559 | -1.15213 | -53.40442 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26f436e9-e1cc-30b5-8126-8709e5c8a9f4 | -3.3193 | -53.29111 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fe64dfb-3c12-3076-aa9d-cd7ecfc85703 | -3.35116 | -50.51128 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6c4a96ce-9fcd-3629-bc74-d92f64e5209a | -3.34462 | -50.50611 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d3bba3b-5524-3037-882c-4a7e976cc3b5 | -2.91554 | -53.21023 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89be77de-fa87-3e76-bace-fc29188dcf54 | -1.34539 | -51.43525 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 95c6b8d6-65ca-3f39-889b-b65703b9d28d | -0.90393 | -51.64648 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5380320b-501a-32a4-b56d-526a5af58403 | -0.81347 | -51.49009 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ae87469-961d-33ac-9eb5-7e00a437d8ac | -2.79598 | -53.00449 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93dd3ec0-1800-3517-a9b4-69f00fc28083 | -1.77304 | -52.73172 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f6aee0bf-348f-3afb-8b5a-b64d2c156ca4 | -2.11466 | -46.56746 | 2024-11-25 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a9e323e-28ca-3dfc-b788-b211cfb8795a | -0.95497 | -51.71605 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f8baab4-33f0-3c51-aa69-8185f842f23e | -1.62817 | -52.443 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37064d03-52f4-3abf-bd5c-02fec3cc6acf | -0.1445 | -51.2964 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d05fd76d-5646-372f-8f8d-12909b7f9b99 | -2.31193 | -53.60335 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f6acd83-5ef1-3761-b512-5e9ee40f815b | -0.98358 | -51.72033 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87032f5b-c738-386f-92bd-ad9324e2fea9 | -3.7748 | -51.90839 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f87a8f9-d7a2-31cd-a024-86a83aeed102 | -2.67254 | -53.03475 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd15e733-81c4-30a6-9558-e5b03d3e2d21 | -1.52405 | -52.05243 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b37d801-27d6-33f1-923b-906ed2bf755c | -3.21292 | -53.8368 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38825a3b-2718-3e40-8973-563464183275 | -1.19507 | -54.2072 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9c032c6-982e-3050-be94-c173eee3f5a7 | -1.10589 | -52.34414 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4cb52ce-4206-39c4-be26-bf933e73b02a | -1.20059 | -51.76072 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README49.md)
