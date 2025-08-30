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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af883198-c76f-334f-9b7a-2194c6c5c697 | -11.39805 | -63.24974 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51b9ad58-a235-3f0f-8eb0-611f7f4b313c | -14.50528 | -52.05021 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 420019a9-e90b-3444-8796-83a0c8e48834 | -14.50807 | -52.05436 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08bac8db-7fa5-3ade-a47a-3eab0be3762a | -13.53214 | -46.94947 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ffb34acf-5efb-34c2-a1cc-08697b385577 | -12.66034 | -48.18478 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f06fee5-f80f-3853-b955-28b916373fcd | -14.22982 | -48.07207 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6262438-77db-3c5f-84b4-58c69e561b5d | -13.36128 | -46.8797 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31cf84e7-e0ab-37bf-ad76-3fd6d7d46c85 | -14.32153 | -53.09057 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81fe559e-a3fe-39e7-8fe8-ce586cc9c66a | -13.55972 | -46.93507 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55d96240-35ea-3d0b-a6f0-ee5c4ffcc0ee | -13.35442 | -46.86727 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4f3ceec-eba4-3c9c-b9a4-d25e7e5b3499 | -13.39287 | -47.00009 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b9cf2ae0-a278-348a-bd07-d8623776c962 | -12.6238 | -57.0058 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 131edfb8-aadf-38b4-8bdc-649aadcf304b | -13.40302 | -46.956 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a655a2ac-b1d4-34ac-a60c-cd2cb205e2f4 | -15.22152 | -53.81326 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff478105-2e8e-3d2b-84a5-4593aad29e5c | -12.83049 | -48.08805 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54b778cc-ab67-3fbb-9481-1c60b6f88a6d | -14.00384 | -44.56208 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e69d5383-cdb2-3018-8c58-90f9dbf8e6f3 | -12.92085 | -56.98299 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 902c2708-fe9a-395e-aa94-43f8b6c4e357 | -14.50372 | -52.99255 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d025d94-bb18-3080-b5a1-307dbaa67143 | -13.36944 | -47.00542 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27b84bd6-ac85-3f82-949b-cc33e3daceb7 | -13.68302 | -46.91401 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a4acabd-f5c3-35dc-bb75-58901bb88fd9 | -14.56105 | -52.00009 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32d591bf-2926-3672-9526-74d56f6167af | -16.5837 | -54.65402 | 2025-08-30 04:51:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b310074f-c73b-32e6-bd30-b1172717622c | -13.39238 | -47.00379 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8557cb8-b08f-3b6e-9250-e8798c2bfcbd | -13.37422 | -47.01275 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38087dd5-317d-3777-8319-c7039e91ff30 | -9.73093 | -64.91526 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbfcf374-da37-3ecb-8731-0df65571cd4d | -14.23373 | -48.07281 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9487d1d-0eb0-3643-b000-70352402fc36 | -13.46861 | -46.94368 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 906a3b9e-7abd-3a64-a7ce-d44be4866c76 | -14.02029 | -44.55456 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 83eb05d5-941c-30ee-9b44-e33d96afd3d3 | -13.372 | -46.99744 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cff8916a-1b4f-3008-8201-1857fd083702 | -14.49469 | -52.05217 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c04cadeb-420d-3ac3-aff7-43655f9e28de | -14.45658 | -48.45358 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eeafd622-b75a-32e7-8b94-64ebf0813983 | -14.6247 | -48.07374 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ca67d078-a121-35e5-8a96-155e743fec34 | -13.37888 | -47.00954 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bf7ac646-244b-3a69-a2ee-3b9cdc1313cf | -13.36315 | -47.02013 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feec0e62-9a65-3e83-9846-383619a81b3a | -12.92475 | -56.98369 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ab4f4c4-9b97-38e7-bb48-d35b834ee278 | -13.3872 | -47.01074 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88e67d30-98a5-3c88-aaf7-c7e61175ba80 | -14.00831 | -44.57038 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1ee7d2d-af3a-3b37-8e31-844fb2644ffb | -13.67861 | -46.88348 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88b315c7-02a5-37ac-a5e0-d7bb1e049501 | -13.96633 | -46.33985 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4591bb30-fa7a-3c72-9c93-bb862f139f7a | -15.31253 | -49.61498 | 2025-08-30 04:51:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cef4c583-381b-39fc-8a00-f091412cd058 | -14.50751 | -52.05796 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bf20b2d-03d7-39a4-8f77-de329d5d1b09 | -12.94354 | -46.1437 | 2025-08-30 04:51:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cc0566f-a072-3aeb-afc8-139b8ca9cd79 | -13.9669 | -46.3356 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d1103d9-ef1f-3310-b87c-9b9844bb3c4d | -13.41245 | -46.94917 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99a208ac-f6e2-3807-8a22-17d4735cdc9b | -13.3895 | -46.96169 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7315716e-5382-39d9-9875-498f54dc7af3 | -13.19775 | -45.28667 | 2025-08-30 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a97e2aaf-1754-355a-b46a-0d464a5a7b5c | -13.36854 | -47.02362 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcb51c7d-9c3e-316e-a6a8-97f28f5c13c9 | -14.51037 | -52.99366 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d62a023a-0f50-3b4c-b19c-e6bcc15675aa | -13.51106 | -46.94759 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fceb6f2c-8c14-3ad5-b3e5-c7446580531b | -13.56969 | -46.92466 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 171518f2-2440-396f-9632-74c29b183c54 | -13.57656 | -46.90577 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2db1ece-6383-3fb2-9beb-2e50de6e402d | -12.63165 | -57.0072 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b2bc3b1e-6e8f-3b25-b13b-31db60200fd9 | -13.51057 | -46.95126 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00d74f49-f570-3d48-9ee4-92b119b773cf | -13.40021 | -47.00869 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65953eb7-4702-3d80-98ce-dec50040e30b | -13.36904 | -47.01981 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2770bcda-d25b-33d6-85ab-6f657f9ed4f6 | -13.38832 | -47.03411 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21926b43-3953-33d8-9e69-0e29e4e89340 | -14.53316 | -52.00295 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ada21273-ccc3-36ed-ae6d-229a676e42b0 | -9.67272 | -65.02816 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b259e3d-4fe9-3e13-8219-1f6fae9f5926 | -12.42529 | -63.91802 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b9996f8-3b32-3089-9a74-5e598ff9e1f5 | -10.83797 | -61.46454 | 2025-08-30 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56ec21a7-e8d7-3b9d-aeba-877b84d5b8e2 | -17.91927 | -46.84109 | 2025-08-30 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cbab987-b983-3a2e-9947-1265214171cf | -10.74574 | -59.81752 | 2025-08-30 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 191fae8f-117e-331c-8eaa-49c404f614f4 | -12.7068 | -48.14492 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d6e7e8b-bf2c-3f41-b478-ae6952e4d976 | -14.0422 | -44.49895 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60d5461c-9938-34d8-a9f5-7a81f945e052 | -14.59445 | -54.5491 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e97ad304-272d-3cc7-8647-4938cd127c9a | -15.18882 | -53.7816 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 366ab708-7e31-3043-90ec-feccd78a6116 | -15.10538 | -48.18781 | 2025-08-30 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af041733-6c6f-36a6-ac4e-abd5c17ddfd2 | -11.39714 | -63.25425 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5a851db-ac3d-38b4-a673-8ea151981e2f | -18.41698 | -51.97258 | 2025-08-30 04:51:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7968633f-7e95-3e59-b9a5-09255cdb6d79 | -13.45622 | -46.97186 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a21bea8b-2e14-38d5-98ea-5bbe74ca8ff0 | -13.01364 | -48.72312 | 2025-08-30 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47c979c4-d076-30b2-99c8-b8f34534023a | -13.6443 | -48.15962 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7769f9c1-6339-3f49-a9f7-5a0534adc15d | -13.67883 | -46.9133 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceafd2fc-a1bb-3b97-ab61-3351b6aa4f90 | -12.43041 | -63.92414 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30d8923d-ed5a-3bc3-858f-fa91d3c91ac2 | -13.47114 | -46.95622 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f58edff6-8d0c-3cb6-b857-f938798f3b9d | -14.01872 | -44.56388 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2d4dc21b-2800-3722-85b7-f810f1dc32bf | -13.36879 | -51.75407 | 2025-08-30 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 354e0ba6-9f7e-384a-98d6-65e885acbb42 | -14.45958 | -52.02476 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 169da177-6848-36e4-8d45-a7f2534bc4c9 | -14.00069 | -44.59188 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 486d3694-9469-3e24-99ae-243819aa95ed | -12.43163 | -63.92231 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8459b81-4db2-3289-8aaf-d542c08fecf4 | -15.02109 | -59.91417 | 2025-08-30 04:51:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02d31b0b-93f4-3e0f-8ce1-ae1f38db9fdb | -12.92658 | -48.11159 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01482556-f34b-358d-98bb-6220a4eeffc4 | -14.59569 | -54.54154 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a18ca53-1ccb-3414-a663-c78c28c50474 | -16.53422 | -55.03742 | 2025-08-30 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 081fd439-2757-33cd-b7c1-2224bb37d46c | -13.62834 | -48.19556 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1d6bcb-fb4e-3884-89c6-e0f08c640735 | -13.36967 | -46.88084 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 390b82e4-28e2-3030-8d38-22ce1c7ad427 | -13.36178 | -46.87606 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8103068-a598-3872-82c2-b1724a627bd7 | -9.78948 | -64.24448 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 297a3467-3d25-34d2-97e8-ff9068648fa0 | -11.39296 | -63.24405 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61fb36f6-0b1a-3420-91de-5220cf75ee74 | -14.50361 | -52.06103 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acd3e67e-3942-3ae1-8887-601173efbb0e | -13.37838 | -47.01334 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f38894b2-4ea2-3391-abfb-892ef6dc96e2 | -13.39006 | -46.95744 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f084b8a2-3686-3727-bd6e-9e7ea5379836 | -13.38125 | -46.95968 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 615b4a4a-56d3-3222-b2cc-0ac48a5cf5c2 | -13.50431 | -46.83693 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc5ff751-e868-3543-80f2-5108f685efe3 | -13.35158 | -54.39032 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5eeb9f5-2c68-33ee-8a18-269c06901ba7 | -18.91407 | -56.25077 | 2025-08-30 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 26acde57-0b21-311a-8701-f16dae33a965 | -12.84991 | -48.17295 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d6208a2-a14a-354a-b496-dbea49e54944 | -22.84642 | -47.49575 | 2025-08-30 04:53:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 13830c4d-adea-3c3f-bbc7-1d732af95b93 | -20.47593 | -53.67638 | 2025-08-30 04:53:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4cacb18-00ab-3803-8a40-0e19d2c705a1 | -22.1926 | -54.84102 | 2025-08-30 04:53:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README61.md)
