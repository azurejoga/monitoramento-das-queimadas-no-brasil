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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba818819-3ea9-3790-b67b-bd70ba8d68ec | -14.18152 | -45.15186 | 2026-09-17 05:18:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| faa9efda-4df0-3be3-921f-7a2f7ef1c664 | -11.32415 | -46.77563 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57128b95-9e37-33d5-bec3-c99a3db72c23 | -15.64171 | -52.73122 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0b68e77-574c-3ec6-b6fd-3de8fd1af57d | -9.28686 | -60.62466 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0edae55e-d7bf-330e-a582-5dba0b2cd921 | -9.88723 | -57.79429 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f40d801c-1e63-39eb-8e74-fd3e8dd4e12c | -12.11493 | -57.19654 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5f8059a-2ba5-34c3-a8a8-2b59b223c52a | -10.39381 | -58.30767 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 688b3621-593b-3035-b065-2cf4b52c753b | -9.10164 | -60.95437 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aeca9a0-8d99-33d2-9c15-516a911bdc79 | -12.37648 | -48.46544 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ba98ff3-f75c-3b9b-8d75-48b37ebe3158 | -9.25025 | -60.79072 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0f915f4-b81e-3d22-920f-8a379c9da385 | -11.57036 | -46.88216 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb064659-b481-3968-8979-866827cac884 | -11.21561 | -42.82734 | 2026-09-17 05:18:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 109491b5-6da3-324a-8066-901745d405db | -12.44446 | -50.81402 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c28056b-214f-39ee-a7e9-d827203351f6 | -10.77175 | -46.20515 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28478da0-8403-39bf-b331-0c2271967ae6 | -12.43505 | -50.81712 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| abefeaed-ecf4-3b5c-add9-46a30ca77bf9 | -11.53003 | -46.86902 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aec8d692-3cf8-30c0-9f43-15786e2a9ab9 | -10.83213 | -46.15269 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 96b357fb-0d03-3482-baa6-14774ce65bac | -12.51814 | -50.6874 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a01f8cc-4ced-3dd3-95f9-80ac67d8ad13 | -12.75377 | -52.84244 | 2026-09-17 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a29c8fa-ad6f-3420-9a6b-5e2868538789 | -15.49121 | -53.79269 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ece68de6-ec42-3975-a410-888d43587369 | -14.8239 | -59.54834 | 2026-09-17 05:18:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d100ab78-f689-3370-95c9-61165782b4f1 | -11.13634 | -49.03952 | 2026-09-17 05:18:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a5b969b-68ad-3daa-9519-9957f60ff2b9 | -12.14104 | -57.1827 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 820e2dd2-3eab-3897-8af7-473b521e5379 | -12.44221 | -48.48673 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33500c0e-9645-37fd-8db0-ba39c7dae515 | -12.11105 | -57.19952 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d8de5bb-7ebe-33ef-83bc-da1ccfb2457a | -12.45829 | -50.81153 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2fee754-c33d-36f4-ba1a-330e83a07a7b | -15.64627 | -52.72816 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d01011e1-9f3b-3366-a365-a787e8bd1249 | -11.80988 | -58.17345 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 02bbb990-4b08-3888-9cd5-21dfbbff6d4c | -11.59414 | -46.87682 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec1e38d1-1e63-3549-b938-bf9a2e968994 | -12.44237 | -50.79597 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db4da0a8-2aca-37f1-9c4a-e7047714cec5 | -14.18214 | -45.14603 | 2026-09-17 05:18:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b879c1d8-a024-382b-a1ea-ccb7c7f2cc23 | -10.59442 | -59.41669 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87e3b0ae-d824-35bf-acc9-2165781bfa4c | -12.14205 | -48.2559 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfbb358b-8eb1-3b15-9990-0d58098cbfaa | -10.66057 | -58.7642 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ae8d1be-dc80-32d3-9adb-e64b81f2e464 | -11.32505 | -46.77776 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6303c8b2-977b-3760-99fd-773970f1771e | -12.43795 | -50.79536 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6c7adb7-bf7f-3a63-bfa1-c75813ad2d20 | -10.79199 | -46.18638 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a1d9e60-f396-3bd4-b0b7-dbcb535d4cd1 | -14.86555 | -59.50925 | 2026-09-17 05:18:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42998daf-6689-33fa-be3e-1eeaca242515 | -13.75296 | -48.81165 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b71f04fd-42b4-331d-95fc-ff2a8e4e4983 | -10.78504 | -46.19429 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b72d5c1f-3c9d-377a-ba44-9f23446bf46d | -8.65387 | -66.59299 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3f63e6e-361a-3f48-b0be-78c408d8219d | -9.10701 | -65.93124 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 601c3437-a58a-37a7-86b6-6cc388828ce5 | -15.46829 | -52.88343 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a6ad5aa-9ea8-3dd0-aeb9-ead0a3b5fc39 | -9.69796 | -58.18228 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ba47556-efe9-38aa-8478-8c5a3e3034d8 | -12.4268 | -50.81153 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff7c0c6b-e81a-30cf-aff7-5f6ad79fd4a3 | -10.6612 | -58.76043 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cda4d41-fcc0-369c-83fa-bafd2d507b95 | -10.82678 | -46.14746 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 66669356-75bc-3ed2-b464-42157b0909e8 | -9.10274 | -60.97303 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d13a5bf-81d8-3349-8826-3df0751fea39 | -12.43702 | -48.48622 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf3697f5-78e6-32e3-89f3-c189ee78050c | -8.87766 | -62.397 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a84a0d-b76b-354d-b4b4-d8522580243c | -12.43389 | -50.82581 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| fb0071a0-dc8b-3fb7-afac-36c1de487749 | -13.58263 | -45.47651 | 2026-09-17 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e6b7d23-08be-3c13-84bc-d05d0361f363 | -12.43273 | -50.83449 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 90cbf172-4768-364e-946f-e3457cb0d25d | -11.531 | -46.8733 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8763af23-4f28-32d0-b796-058448fb12a7 | -9.06943 | -61.00324 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e029af71-edb4-3e73-b183-3a8356d712ec | -11.57181 | -46.87038 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ccbbef4-c063-33df-822c-9efa0275b202 | -12.45858 | -50.84255 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7df7ac23-29fa-360c-bf11-0c1d311caed9 | -12.40083 | -48.48125 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a11cfd8a-c955-3a38-98ff-a397ae640744 | -12.14248 | -61.16475 | 2026-09-17 05:18:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b5a4228-b1d0-3e55-9007-599f7c074d72 | -12.44919 | -50.84564 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7b3bcdbe-953a-3512-866b-98cb106bde5c | -12.44329 | -50.82271 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5d4b219e-f3f2-3012-81f9-a7b3c9dbfc2c | -12.45036 | -50.83698 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af9d7d1c-d963-35fa-8230-3b75f8e29b72 | -9.09773 | -60.95367 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925a19b3-d884-35d6-922d-9cf8a840855e | -12.44504 | -50.80967 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45c0658e-52d3-3b57-b359-e69d4b523222 | -11.04889 | -48.27816 | 2026-09-17 05:18:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d02bc27c-ab9e-3587-89a1-54ea73fd1d01 | -12.42665 | -48.48501 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e23d9e45-6915-3d45-94a9-2ad4cd92ca85 | -9.09408 | -60.97667 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9775b9ca-253e-3e20-8424-5c55f34fc31b | -21.45713 | -48.6791 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 123a33d0-9366-340c-828f-a2b501f8ecee | -17.48927 | -49.49907 | 2026-09-17 05:21:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e313240-fee3-3160-8824-92a4223a524e | -16.30859 | -53.84655 | 2026-09-17 05:21:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c771601-e44b-350d-898d-0cfc34840df8 | -18.0289 | -50.94245 | 2026-09-17 05:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 757657bc-aa79-34f2-a7fd-efbc6755bfd4 | -21.44583 | -56.99698 | 2026-09-17 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54e6be6e-6f35-34b9-835b-aa85f418fc63 | -21.46249 | -48.68379 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 463a50fd-8175-32bd-99c0-193c654709d4 | -21.45751 | -48.67493 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d64014f-132a-3a53-935f-31985ad7e2ce | -15.29814 | -59.25927 | 2026-09-17 05:21:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2d9363b-860f-3f14-8ae4-7afff03c8e2d | -15.83616 | -56.19678 | 2026-09-17 05:21:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 79bd10d1-7e6c-3345-b564-1c7228996bc4 | -21.46285 | -48.6798 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c5e1d5ab-069e-3cd5-afe6-ed8a86777c8e | -18.11708 | -51.69527 | 2026-09-17 05:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc64418-4884-38e6-9735-549b98553fd6 | -18.02896 | -50.94468 | 2026-09-17 05:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 06854efc-fd66-3a42-a0fa-a33347133a79 | -21.46246 | -48.67841 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 817fd0dc-c5d2-37f3-b81e-ee03b3e65e43 | -18.02826 | -50.94767 | 2026-09-17 05:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a640927d-52d2-3fcd-98f3-7de54f30252f | -16.30796 | -53.85112 | 2026-09-17 05:21:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54354d51-336c-35b8-938d-74e119dd0389 | -21.46323 | -48.67561 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcc60d2c-7c07-38ef-9622-6cd2d6ef8a12 | -18.02762 | -50.95291 | 2026-09-17 05:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0578d739-706e-39d7-a856-72565dc2cab4 | -15.60978 | -56.54414 | 2026-09-17 05:21:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bee29814-93d6-3f9c-97ca-442e80e0333b | -17.77267 | -46.47782 | 2026-09-17 05:21:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2cf70303-71e7-32a4-9274-741dcc670ae3 | -15.83902 | -56.20116 | 2026-09-17 05:21:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 53632ee2-d1de-3f68-8216-1b07c3fa0566 | -17.77619 | -46.47857 | 2026-09-17 05:21:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0753197c-9a40-3de2-8193-d0d12c6416c9 | -21.45674 | -48.67772 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c97be48-d10f-3ad4-b73a-a370c9993b60 | -21.46207 | -48.68244 | 2026-09-17 05:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9eff5d8e-3f5f-30e4-9e16-ec1396e5974f | -17.7699 | -46.47787 | 2026-09-17 05:21:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78c0bbb2-d523-3717-8418-0f8aa76e4c05 | -17.49443 | -49.49978 | 2026-09-17 05:21:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d26998ff-b9af-3cb3-8fa8-01597f03f9dc | -18.02836 | -50.9499 | 2026-09-17 05:21:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d155bc50-fd9b-366a-a75b-6e720d2ecc33 | -15.84015 | -56.19351 | 2026-09-17 05:21:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 52a7e2f7-2fcb-3d87-a13d-32b2faafd799 | -18.12262 | -51.72465 | 2026-09-17 05:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ca03c36-c1fc-3b01-bb76-bbd2a8b9bc3e | -28.02675 | -54.41306 | 2026-09-17 05:23:00 | NPP-375D | GIRUÁ | RIO GRANDE DO SUL | Brasil | 4309001 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 19fda52b-4f74-3421-bf9f-5c869a1e665d | -3.2825 | -57.91446 | 2026-09-17 05:33:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 869681e4-e35b-30a5-ac82-0f8b9e34e0ad | -2.95638 | -50.32233 | 2026-09-17 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ffe625f-2804-3ddc-98ff-70a461becc41 | -1.81846 | -54.93541 | 2026-09-17 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2c0a6d-088f-3cbb-a81e-fdfa7406ea02 | -3.33215 | -59.82446 | 2026-09-17 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README72.md)
