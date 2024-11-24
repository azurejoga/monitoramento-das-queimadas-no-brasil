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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d82a7ce5-b280-31c6-aadf-ef64cd392ad1 | -3.29286 | -45.72832 | 2024-11-24 05:14:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f8facdcf-c76b-375e-b79e-73fb15630d4f | -0.57579 | -51.7234 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 913f45ca-0fdb-39bc-8fb1-1598766c4617 | -2.85243 | -53.99375 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70c85b2b-746d-329f-b944-1fd976b8823f | -3.12423 | -53.10082 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1da6fe62-139f-305f-9472-bfff0cdcbf47 | -2.84575 | -54.01165 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be4c85d0-4113-3f5e-9813-42b7a7ea7bdc | -3.21904 | -53.9337 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 044041ea-f2fa-3abe-b070-55af78f245dc | -1.19153 | -53.68086 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcdde2f7-26eb-347b-972e-4dbe5e0fc818 | -1.13235 | -53.40282 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3a291f9-3a30-3d08-89f4-67640e99fedb | -0.81471 | -52.82806 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea2d965a-33ba-3316-84be-6ff4eb3e64b0 | -2.16752 | -53.77929 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be2b0f2c-f476-3a9e-b068-b382a2870746 | -0.96589 | -51.71526 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d138987b-77b8-3c94-b333-ff52f0027cd1 | -1.14208 | -53.4017 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a91b022-1640-3501-8fac-eb9090eaaaf3 | -2.74578 | -49.12177 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1d1ee6e3-7ec7-3c8d-9522-6c81e88ec9bc | -1.29285 | -51.73183 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 26d1f46b-8dfd-3d72-bdf1-77d33846b690 | -2.91489 | -54.28463 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f464b294-bc56-312d-8eab-0338ea2cebf5 | 0.40628 | -50.85579 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 98b87185-09a2-3eb7-8dd0-fe7ad1becaa6 | -3.28537 | -53.78291 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27e18132-a34f-3b36-832d-e567ffce63b0 | -2.08302 | -49.60874 | 2024-11-24 05:14:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a19f0861-54cd-3b05-b04a-eb9b13ad7662 | -3.56789 | -51.10927 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa6b8553-0836-3ae8-a84c-34153a2ad2f7 | -2.69735 | -48.82716 | 2024-11-24 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b952bb1-ba95-34aa-bc19-a63bad2d1801 | -3.13797 | -52.98289 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a4ce794-2b99-334e-9dc4-2fd08422e863 | -1.24123 | -51.7421 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de72c612-ecef-3256-94df-c083116d55db | -3.19001 | -54.32974 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deacd17f-15f5-3fca-af9a-99897f6c2f66 | -0.25468 | -51.59595 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29fe867f-2c24-3fb5-9960-8383a06c083a | -0.24982 | -51.57065 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30f35062-9bde-344f-b32c-ac435fc8699f | -0.9251 | -51.63863 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30bc7dcc-fe8c-38e3-967f-c3942c498dff | -3.2734 | -50.43913 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc180211-6cce-3c8c-b62d-54ff92b7ad75 | -3.15334 | -50.59077 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2fab401d-21cd-32d6-a9be-5860a01e4139 | -3.27943 | -53.8217 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11a79932-2bd9-3fa4-9a10-a8404ed5ad51 | -2.71108 | -46.26923 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49d782b6-789a-3b2d-83c2-8cfa967bb657 | -1.12295 | -53.57758 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce78de60-8fbd-3f1c-91ab-9ec34317ce54 | -1.76266 | -52.70644 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02db311c-0576-3791-96ed-fbc415896ff8 | -3.06289 | -53.2271 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00e59530-2cbb-321b-b0c1-c1a522d2dd10 | -3.85763 | -50.05095 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96e2a26f-a58a-32c4-993f-a5ad532047c2 | -0.28324 | -51.49722 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3569b0-7142-39bd-aa62-ec515a24ce7d | -3.03218 | -49.44883 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27b2caff-5483-309f-9257-62bf0bd4fee3 | -2.54951 | -54.05464 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e382a9e-db47-3b9a-85b9-9586a2a171f2 | -1.76729 | -52.70351 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2aa4c7cf-eacf-3612-accf-b60cae2a3ddd | -2.77102 | -54.0427 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e7c0db3-0e68-39c2-ae51-7f3ceb130422 | -2.71437 | -46.29059 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11121ebb-67a8-3c5b-9443-e1fe0700c29e | -3.15579 | -49.90281 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d53b472a-ba65-375e-b09c-b0217c7fe50b | -2.86165 | -51.81986 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41185313-1260-357f-b042-4f3ed39a03fc | 1.42999 | -55.92536 | 2024-11-24 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86f32305-4424-3c94-9507-837988279fc0 | -3.42687 | -49.99902 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd919d8d-fbbd-3c52-954c-6dccc2a3a6a7 | -1.05207 | -53.1553 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 039b6524-b677-3a54-93da-4c63b694f374 | -2.99297 | -53.44498 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08dbf6c1-da75-36c7-984d-ce9c0319479e | -1.36867 | -53.83577 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fb66505-8927-31ab-a2b1-cebf0e9f2e70 | -0.98203 | -51.71228 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f9efa18-c459-3132-beb2-7361efb9c873 | -2.92741 | -54.33458 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5c32842-07b0-330d-8a54-f48a55a800f2 | -1.3644 | -52.54767 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c061c6d-f811-35ea-9134-9041e71383d8 | -0.36185 | -50.02188 | 2024-11-24 05:14:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fac5f3d-7b65-3d1d-becd-2ca8558a20aa | -1.47104 | -55.10318 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40007046-7ead-388d-8794-f7ce93616145 | -3.49228 | -52.0077 | 2024-11-24 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81cc41b9-7392-3438-8713-1f5c81e7d610 | -2.17445 | -53.78513 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 082fac68-8803-305d-814f-c3968f23e0fd | -2.1736 | -53.63549 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80db9a31-d475-360a-9e29-8644539e81b3 | -2.7405 | -49.12101 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a86ccfbe-7930-34b9-93b6-488068424f73 | -1.26084 | -51.75752 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e0f4320-8bf5-39e1-801e-6e38787afbbb | -1.6291 | -52.43769 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af34a840-c898-39cb-8d05-49857363f710 | -0.25703 | -51.63714 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38487f40-f8d0-350f-b883-f4a9ecc480aa | -3.26774 | -50.44366 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6861399f-36d2-3ac1-88a3-acbbab26c7d4 | -2.78619 | -54.04504 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4af081e2-c53d-3273-bdb7-aacf3daa347e | -2.22331 | -46.39337 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b39fa94e-49bf-395f-85a6-2f921a91cbbc | -2.80559 | -54.01974 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 894d8455-73ae-39ea-b104-fbb16e482f7a | -2.70802 | -46.28964 | 2024-11-24 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74716089-8262-35dc-928d-60ce283a313d | -3.27829 | -53.01156 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 603d1ac5-8c7d-3232-b4ba-d6a9211fb56a | -0.94539 | -51.65009 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aecc4c1f-6cb6-3e09-9c5b-dd7b2ba075e1 | -3.17154 | -45.30231 | 2024-11-24 05:14:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc476d5f-7b62-3ffa-b205-c2d0dec842c2 | -1.60976 | -52.5917 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b56f0b7-08ed-3822-a89f-2d0bab7802ab | -1.40563 | -54.47543 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 15c4227b-d4bf-3873-a4c3-a4726ee87092 | -1.04758 | -51.743 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c6fecff4-797e-324a-a5fa-f9df2478694f | -3.49161 | -52.00935 | 2024-11-24 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14376ea4-93f2-327f-a946-6105a913e7da | -1.45616 | -54.50972 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b799a3ae-10e6-33ca-b8c5-550e2edad0c6 | -1.74889 | -54.51891 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1572d39e-a715-3299-ac36-f1c7b4973364 | -2.33362 | -55.30526 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012f428b-2fe8-3249-b808-1173e8c6bf31 | -3.28499 | -53.26548 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d35bfcf-a644-3aab-84df-8655ccea0999 | -2.04431 | -49.72854 | 2024-11-24 05:14:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f15b321-3201-3f1b-a465-ac3b51fc23c4 | -3.47125 | -50.01133 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 371a10a2-1260-34bf-b342-32d2b03c02de | -1.75718 | -52.66166 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ffb0d33-b73d-320e-9599-e8bd8fd64c48 | -2.17205 | -53.77522 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a362029a-269d-3119-8226-88544ed7bd4e | -2.32102 | -53.86241 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55b9d595-5664-3df3-91af-c63bde8b13ed | -1.61391 | -55.13691 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 695f904f-4b33-3588-93da-12cfd3bd5921 | -4.08374 | -46.15084 | 2024-11-24 05:14:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75734616-9c70-3ad9-afd0-c871dcf4ad12 | 0.41965 | -50.85369 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf4b9fd8-ba49-392c-9141-68adbcc9b75d | -1.76967 | -52.71481 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73cfc8bc-dda4-35c7-99a5-f4c88b81c988 | -1.62063 | -55.13671 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20798451-b3c1-39ba-a7a5-e36e10c6a448 | -3.22358 | -53.92967 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b3bf44e-f9ea-3ea0-bd65-8b3df4a3f50b | -0.9189 | -51.65012 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecc81b0d-a608-3320-979d-e816ff29dc96 | -3.28971 | -53.85782 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d852b7d9-1079-3a0f-b59f-1dccca2554ef | -2.03908 | -52.09674 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de5d1e3a-026c-342b-9c70-f2dc203de0d0 | -3.00681 | -51.54799 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00b7ae0e-9856-37e5-b9f1-6d5a9a6b7add | -1.29716 | -51.73249 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9cfdf819-06a6-33be-880a-ba22722b3ede | -1.73439 | -52.72762 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe97bc1a-4cec-3700-95b5-823b5e1ab25f | -2.74627 | -49.11858 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 265dbd0d-aefe-3567-b7a6-b6179bb98db6 | -3.26391 | -53.26923 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24b9be23-50cd-361b-bf56-d333a8682e40 | -2.76685 | -54.07026 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e919880-5d46-3d0d-8dab-ee64f3198dfa | -1.61165 | -46.88157 | 2024-11-24 05:14:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fcf9fa6-bab1-3896-a929-4cc81ab0da71 | -3.09311 | -54.55218 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76407ddb-6f05-3652-ad2d-0522d3e96b8e | -0.88615 | -51.71939 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98470f60-b862-3e9c-9b35-2b582179903e | -2.1763 | -53.63298 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 435d1cb4-0ac3-32ae-bdd0-c728e6b0354e | -3.25537 | -53.27147 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README78.md)
