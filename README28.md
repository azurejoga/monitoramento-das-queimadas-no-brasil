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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7df604c1-8321-37a9-ac89-4b5c7089cd1d | -5.29935 | -56.01289 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 847171dc-f419-3350-9e17-2b01dfe7f4a9 | -3.03651 | -59.36481 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 482c5ba6-16e7-3258-bc86-31045735fc4e | -3.08102 | -61.18548 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99f42884-d1d2-358e-8a9d-1de117f283bc | -3.08211 | -61.17858 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8041a39-c4bc-376e-91d8-6836527f9763 | -3.39946 | -61.31371 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ef9e47e-831e-3c68-bee9-008a02c2d305 | -1.96486 | -54.05743 | 2026-09-05 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06bd02c4-6cf6-3846-8808-01765eb0c24d | -4.12684 | -56.33775 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79bb2eee-0e2a-304a-a011-3fa770ca8039 | -4.67561 | -55.63348 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1df3e0b4-1a08-3814-8e35-0460e719d145 | -3.0885 | -59.38356 | 2026-09-05 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4af2f9ec-9fbe-37b0-83d5-8afb5ced3f33 | -3.17235 | -61.14318 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1470f83a-5541-3056-985b-6b673c8c1f5c | -5.29504 | -56.01228 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 024930dd-221f-3a85-a3d6-0451f0e5173e | -4.10439 | -60.66029 | 2026-09-05 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57870d2c-4679-3db2-a05b-e62d94bf312b | -5.08027 | -56.29246 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2c32ef3-c034-3c3d-984e-704440bf53bd | -5.3461 | -56.03482 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5c7d87df-3a5f-3e6b-83a1-c1fb3d1c33e6 | -5.16738 | -56.05632 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c05c2005-4394-3a91-92ab-7474e7871112 | -3.23125 | -50.57448 | 2026-09-05 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b2bbd9b-a866-384e-b3a4-9106eee472b6 | -5.35101 | -56.03137 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4421a936-625a-3eba-88f6-37d1e508bd87 | -5.28523 | -56.01899 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89afe76c-8b4b-346d-be06-289e716cba68 | -5.85354 | -52.05541 | 2026-09-05 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1a7856b-be2f-3b84-8717-7e241356c356 | -5.07606 | -56.29183 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f578b534-5b37-3345-be86-4a5f5735c4df | -1.17989 | -53.82489 | 2026-09-05 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e40682b-dde0-30a1-8766-e6d167f69e76 | -1.18462 | -53.82542 | 2026-09-05 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 007756bc-cf29-398b-9bff-cd5b68c5aa83 | -5.17494 | -60.28507 | 2026-09-05 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc0c702c-8922-3e66-ab60-51613000cc3e | -4.90732 | -55.81881 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c50444a-7491-33a4-a90f-e3d0bd989666 | -3.3818 | -61.33925 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d813cfd-dba8-31ab-a007-350b224bec4b | -5.33379 | -56.02883 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dead1d74-f3e1-363f-a87a-26652f8e977d | -3.14886 | -60.64832 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dad967d-2de4-368a-9846-48be890957e5 | -5.85571 | -52.04013 | 2026-09-05 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9674d7e-4c53-3d2c-b855-f268458ac04a | -3.14328 | -60.64029 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 415c4e90-fdc4-3dd6-b123-8742aba3435a | -1.77457 | -56.24531 | 2026-09-05 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1314c59c-9c59-313f-87ac-40cacfb2aea6 | 2.44885 | -60.75739 | 2026-09-05 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65460aa0-627b-3e56-baa4-e82cf6ce9e4b | -5.29688 | -56.00006 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 129ed77b-1f49-3598-a1d2-0e6dafc8e61e | -4.91423 | -55.8026 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11b1b061-07d2-31ab-a2a4-6c50f080c037 | -3.14383 | -60.63678 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46a63bba-0858-35cf-9f9c-7c0664174c39 | -4.16221 | -49.70107 | 2026-09-05 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dd63a19-35eb-3739-a547-58430147165f | -3.38289 | -61.33235 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3743dd2a-eba5-3cb5-a797-b308d028e046 | -4.66684 | -55.63228 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| feb408ad-f7df-3755-adaa-ceea1b51cfaa | -5.30305 | -56.01755 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4007c19-9a3d-3c46-aaad-572cb94f3ab7 | -2.76624 | -49.4767 | 2026-09-05 05:40:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eaaed6c-9c63-38c2-bde2-0efa92b097b9 | -3.17732 | -61.13334 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ded0a787-2955-3980-9b93-9d8d33617f9e | -1.96272 | -54.06063 | 2026-09-05 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b075f017-0bcb-35be-92df-b759f195e333 | 0.95959 | -60.64837 | 2026-09-05 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be0e9204-c76d-3481-ab70-fab566e21e96 | -1.66898 | -55.50647 | 2026-09-05 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5d51c84-5255-31b5-ae2e-2914a7409846 | -5.29135 | -56.00757 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae7fb49-04db-3654-ad1f-ed52074c32bc | -3.62386 | -54.60511 | 2026-09-05 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1642368b-8821-3633-ad39-8d5ce86bfc74 | -5.30674 | -56.02224 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6fc5527-1920-327b-8c83-53c5df2792b3 | -3.77582 | -61.75822 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c06b1ab-aae6-375c-b54b-33047a6adc58 | -5.25088 | -59.97938 | 2026-09-05 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c92706-95ce-3e60-a923-c68fc9826ad1 | -5.30243 | -56.0216 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f36801e2-4b40-3410-a22b-7c51b9190c5f | -3.8309 | -60.76875 | 2026-09-05 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab319320-729f-3c07-b64b-5e4e3065c1eb | -5.3246 | -56.03155 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2050461e-6373-33c2-bdd8-e9bf4f7df5d0 | -4.91487 | -55.79838 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 830c94e5-5a27-33f6-8b1f-aeeb55e56193 | -4.2942 | -59.95651 | 2026-09-05 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21fab493-f016-3e01-bee9-e53b03ed7555 | -3.14551 | -60.6478 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64a76efe-7d1f-3089-aba6-14da7f885cb3 | -3.29779 | -57.88462 | 2026-09-05 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98f5cd3e-4c36-3ca3-8ae4-d11c629580a9 | -3.75867 | -61.75906 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9133f8fa-e9c0-3920-ac8b-63045449cb72 | -3.22972 | -50.57259 | 2026-09-05 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa8a3d9e-3d8d-34e0-8d34-09d18506f223 | -5.31596 | -56.01946 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87250d27-e477-3e86-8c47-c387c3f96d65 | -5.29565 | -56.00821 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d468b2-da08-3135-8b1b-0a7df53ef5b4 | -5.29383 | -56.02031 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f57d848-bd10-34c0-b475-bdd5666d5e56 | -5.34982 | -56.03946 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 374cce1d-787b-340a-9369-7e6da0289b61 | -5.31227 | -56.01478 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d321a1c-a75d-3e4d-b0d7-c7191d2029e5 | -3.93044 | -59.34258 | 2026-09-05 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2f77f24-45cc-3d5b-a221-98e1596f1949 | -1.18389 | -53.83011 | 2026-09-05 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ebe9cb25-5a54-3a25-849a-5c325c7b96f0 | -5.29813 | -56.02097 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8ad1568-35f2-3a7b-a397-677618b8287a | -3.09763 | -61.18809 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 566d76dd-b612-33bd-9bc9-6894208a833c | -3.38567 | -61.33632 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8b2cd7-9366-3088-bb05-3a6412e82fa1 | -1.7751 | -56.24185 | 2026-09-05 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 36290534-8301-34d1-9505-37a6014ac069 | -3.39227 | -61.31612 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e3e3a2c-f129-3d4a-bf34-b26a9ffc6072 | -3.76199 | -61.75957 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09fd0ce9-7e41-354c-ab14-5f84710d44f9 | -3.76254 | -61.75613 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02c30aee-655f-362f-93b5-c8b3e5281970 | -3.77527 | -61.76167 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 719aa206-8517-3650-87b3-f008f05b14d8 | -3.7775 | -61.7691 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 896f5444-ad1b-337f-8406-014ebbdc7695 | -3.4388 | -52.81367 | 2026-09-05 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 785ea3c5-5aa8-35ea-9103-61a5d28c3ff3 | -1.27724 | -60.33142 | 2026-09-05 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52733c85-1d22-3438-a035-de7be448be09 | -4.2757 | -54.7739 | 2026-09-05 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16a202eb-235d-30a8-9a0b-86ff6ca6c925 | -3.12309 | -57.69431 | 2026-09-05 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54f3ef94-8e9e-350d-8511-6081e5eabd67 | -3.827 | -60.77172 | 2026-09-05 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a8f44599-1a84-3172-9559-b97f28e05b3f | -5.31165 | -56.01884 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b7a7748-c904-3e3f-bd2a-93a13f854706 | -5.3289 | -56.03223 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9ae8f77-01da-320d-850e-162dd9c35008 | -3.39559 | -61.31664 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bab99e74-55b4-3aa2-bd98-44ee23af9ad0 | -3.16848 | -61.14612 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d3d2c06-e0c7-3673-842f-92c29b83fd4e | -5.21462 | -60.03103 | 2026-09-05 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9a64c07-f539-3339-a6d8-1b6f670cab36 | -3.27686 | -57.87243 | 2026-09-05 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3312e057-2954-30be-a131-c7fa0cd495f9 | -5.3522 | -56.02326 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3a479c64-97d1-30a0-9aa3-6deaefd6ba16 | -4.66561 | -55.64057 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76b3f5fb-1437-3109-a55b-a0621cde949d | -5.3375 | -56.03354 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5744fa89-1650-3fff-a68a-c5961a197114 | -5.31904 | -56.02816 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 701713ed-a9c0-3d73-b0d1-9419d22be244 | -3.07972 | -61.08612 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0c6406c-e35a-31e9-a5e9-705ba893038d | -3.13994 | -60.63976 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c491b1ee-0a26-367c-853a-34a1ba788f0b | -3.52423 | -64.67816 | 2026-09-05 05:40:00 | NPP-375D | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f749e0d-6952-355a-903c-6bca4e8e3203 | -4.36302 | -47.77508 | 2026-09-05 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52b7129e-96ae-3e7a-b9ab-9b1a5fb009d3 | -2.91432 | -60.9996 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8d5b3f8-0ab6-30d6-b7ed-0325e0aef8f4 | -3.76476 | -61.76355 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb4d95c0-f841-34ba-b5a1-a65df2992998 | -3.0341 | -61.24535 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0907c685-e635-3c9e-a9e3-71d68418e1da | -3.43898 | -52.81372 | 2026-09-05 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87fd0afc-946e-3eec-aa6d-4a638f585afc | -5.34299 | -56.02607 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8e723748-e241-3a8d-992f-6a115c542091 | -5.31965 | -56.02412 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb452b4f-9dbe-3054-a1cd-b3552048fc7d | -5.25432 | -59.97993 | 2026-09-05 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a009371a-2b66-333b-9029-3d207061e41d | -3.42132 | -58.30907 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README29.md)
