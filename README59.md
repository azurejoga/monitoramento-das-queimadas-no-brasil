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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64e2ae37-1e6b-3feb-a7cf-ad38d585c4dd | -6.095 | -47.0048 | 2025-10-26 14:00:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 855cd951-78df-3090-89a6-edec3979dae2 | -4.8935 | -43.2115 | 2025-10-26 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 4748af44-69ba-3ab6-ba77-03568b6b2e18 | -4.4618 | -43.4248 | 2025-10-26 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 4df0744e-53ec-367b-8c78-560246f165dd | -3.9166 | -44.0097 | 2025-10-26 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| d527f0fe-fdfe-3655-98e8-1b58a2c44bad | -14.9235 | -52.454 | 2025-10-26 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9e09458b-ea54-3336-9113-73ddf96cb83f | -7.2379 | -44.9868 | 2025-10-26 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1a82f1b5-8060-386b-899b-6cecef4b6c74 | -3.9168 | -43.9867 | 2025-10-26 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e6e47347-12ad-3505-b69c-b77456cade3a | -17.4317 | -46.8608 | 2025-10-26 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 145.0 |
| b818c23b-7427-3eda-b14a-821193c7d4ef | -3.8575 | -44.5393 | 2025-10-26 14:00:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4fb41827-333e-3d84-b795-00b359827b75 | -6.2567 | -41.8298 | 2025-10-26 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| e1e027e5-9f14-3ed9-b6aa-797ef9ec5dc8 | -3.0148 | -41.6851 | 2025-10-26 14:00:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 7747df1e-e939-3e2d-9fd3-9939031135f7 | -11.1419 | -55.1869 | 2025-10-26 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ee3b4841-9bba-3c5d-b46a-eee08c7e95b5 | -4.3239 | -41.7839 | 2025-10-26 14:00:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| fd6ac002-8428-35c8-9858-ff8f816da660 | -6.3864 | -45.7819 | 2025-10-26 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 863f1c24-4648-3612-81dc-71cb2574e58b | -3.6533 | -41.2464 | 2025-10-26 14:00:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 93.1 |
| a3c3cb4b-5462-398a-829e-02904cf6ada9 | -5.4676 | -37.8278 | 2025-10-26 14:00:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 207.3 |
| 3faba230-5f04-3c3c-a6d5-3b7a60c6e746 | -5.014 | -37.8416 | 2025-10-26 14:00:00 | GOES-19 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 5a91d51f-3f57-3314-876c-37cf3501e7b1 | -4.8931 | -43.2582 | 2025-10-26 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| bc8c84a6-6b89-3ab1-9f64-6bfa2bca4967 | -13.6249 | -48.4323 | 2025-10-26 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 4f5175ca-84d6-3767-9e91-5e4bad8d49c9 | -14.6031 | -53.1087 | 2025-10-26 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 169.4 |
| b57cccef-a4c5-35d6-9263-c9ce2367c7f7 | -6.1735 | -42.6221 | 2025-10-26 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 460aed76-4368-3368-ba5e-5faa3f94be29 | -3.7661 | -47.5727 | 2025-10-26 14:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 599db24a-469d-319c-a86c-9b3530cffb74 | -13.547 | -49.5434 | 2025-10-26 14:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 4bf9aa53-97ae-3387-9ef5-e77db0a71073 | -16.1901 | -45.0841 | 2025-10-26 14:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 147.1 |
| f9aa1bd2-3464-3aac-94ff-927eeeb078ea | -17.4311 | -46.884 | 2025-10-26 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 0f51bec3-6444-35e1-a5fd-2f132f6bc404 | -13.3262 | -47.9207 | 2025-10-26 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| a62a913c-4242-30bf-9bdd-62631ddcf78e | -7.2382 | -44.964 | 2025-10-26 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 499c5bc2-7568-31fe-9f06-c5d5c500b4ce | -12.2977 | -47.4658 | 2025-10-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 978a6eed-6d12-37a9-b7b8-969482f9202d | -14.374 | -51.8252 | 2025-10-26 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 046f1228-e2b8-36dd-928d-443f5b7e93de | -3.7896 | -43.4153 | 2025-10-26 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 280627ff-565b-341a-84f8-5387acb43b9e | -13.2586 | -54.3902 | 2025-10-26 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| df16e62d-0250-3436-88a5-f08c477b9f3b | -13.8953 | -48.4141 | 2025-10-26 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 19155dc8-dcb5-35c0-860a-b485f9eb0a44 | -13.3266 | -47.8984 | 2025-10-26 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 983302dc-145f-3c4e-9c23-45066af5d086 | -7.257 | -44.9623 | 2025-10-26 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6099a33c-1680-374d-ad85-b56a80ba2a95 | -13.0315 | -47.2033 | 2025-10-26 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| f0d1720b-7161-34f9-b383-3b4d86ff7278 | -4.8933 | -43.2349 | 2025-10-26 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 270.5 |
| a4901414-962d-3a87-ab8d-6711ce5c9eed | -6.2567 | -41.8298 | 2025-10-26 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 41502fb5-bdd5-3a28-8513-4a9a66b1ab8e | -13.6249 | -48.4323 | 2025-10-26 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 124ff23b-c4dc-3345-96f0-59e805f8b5f9 | -13.2482 | -47.9768 | 2025-10-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 3f413825-5d43-33ee-bbc3-5d63cdb0ad44 | -12.3169 | -47.4631 | 2025-10-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 18a8e2b4-c7a7-3ce0-b581-f9158449e241 | -6.4053 | -45.758 | 2025-10-26 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b9ac3730-ba5f-3a6f-b3bf-64aefd6014bf | -13.0315 | -47.2033 | 2025-10-26 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 2e3fe707-2443-3ba6-9bc2-a300cc8c6977 | -2.9961 | -41.6859 | 2025-10-26 14:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 2c8a15f6-f66c-3fd0-968c-2af7cd6dbdff | -5.4676 | -37.8278 | 2025-10-26 14:10:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 220.9 |
| 414431cf-8086-30c0-87ba-53c19c564ec8 | -13.8945 | -48.4586 | 2025-10-26 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6e96e2ce-ae22-37f0-95ab-d5ba9f3912b1 | -12.3634 | -48.1016 | 2025-10-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 85758305-71f3-320a-afb3-6722dc8515ce | -3.6531 | -41.2705 | 2025-10-26 14:10:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 587f4a4f-fa7c-3caf-a1fc-8f39c8717123 | -13.2586 | -54.3902 | 2025-10-26 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 17dd009a-93df-30c4-abe3-0678fd814af2 | -3.0148 | -41.6851 | 2025-10-26 14:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 545b68a7-eff3-3c11-a9ac-e627620b063c | -2.8994 | -42.3552 | 2025-10-26 14:10:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3ca3b539-9db3-303b-bb29-f6d1252ffa5f | -13.3262 | -47.9207 | 2025-10-26 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8cd6a16b-d0a9-35f8-8145-64af367ad315 | -4.912 | -43.2337 | 2025-10-26 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 18585fad-ac19-38cc-9764-90b1ac21e860 | -6.3864 | -45.7819 | 2025-10-26 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 187.5 |
| db46ba26-23eb-3276-8491-bb54a2878c9c | -6.5414 | -41.6117 | 2025-10-26 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 914541dd-c44c-3d60-a364-d42b643bce41 | -11.327 | -53.9254 | 2025-10-26 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 2881c07e-8c55-3a3b-8be9-56546f4d62ef | -13.8949 | -48.4364 | 2025-10-26 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 16cb94da-68db-35f4-a0f1-d89d808fde12 | -6.1683 | -43.14 | 2025-10-26 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 2389e8d5-25c7-30f6-bbb9-adec4c5cdcc9 | -4.3239 | -41.7839 | 2025-10-26 14:10:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 93dc2fe6-e467-3cf9-94b9-22b35c58ad46 | -17.4317 | -46.8608 | 2025-10-26 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 11af9560-d4e8-3993-9368-489dc67dbb9f | -3.9166 | -44.0097 | 2025-10-26 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b5fa47bb-a650-3113-8f06-a7d2025b176e | -5.7039 | -49.3066 | 2025-10-26 14:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 56368f72-bfed-33f0-ac5f-032e2fd6b12b | -13.547 | -49.5434 | 2025-10-26 14:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5ecf60e8-87f9-3984-8f08-05ee99e03fbf | -12.3165 | -47.4855 | 2025-10-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d27d24fb-03df-3e77-adfd-d8c4f5a99dea | -5.014 | -37.8416 | 2025-10-26 14:10:00 | GOES-19 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 122.2 |
| d1f56ed5-3f2c-3aa5-85b1-1a567637136f | -5.8342 | -40.8036 | 2025-10-26 14:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 33e1f385-80ca-39bb-967c-d6b869aa8e0a | -6.1735 | -42.6221 | 2025-10-26 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| dea231bb-3609-33d7-8d7c-518e32140ea1 | -14.2978 | -51.7713 | 2025-10-26 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 21d545ca-1ea6-3b24-9f8f-ea63bc1cd937 | -4.8931 | -43.2582 | 2025-10-26 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c0e4d651-f1ca-355d-9abc-d95ee462ce74 | -13.2777 | -54.3882 | 2025-10-26 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 68dce0aa-7a51-3905-94f4-6fe7e9c4b6c3 | -5.5909 | -47.0825 | 2025-10-26 14:10:00 | GOES-19 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b4b69ee4-b1ef-3277-9a58-b54e225e459a | -6.4051 | -45.7805 | 2025-10-26 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 98040d18-8118-3ca4-a833-d5d7c1a331c7 | -7.8138 | -43.9894 | 2025-10-26 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d52d3ee2-dee0-3411-a650-6e95d8fa0422 | -7.1581 | -45.4253 | 2025-10-26 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| f6b8a35d-e2b8-3c34-8f4f-f8766fceda6e | -13.9341 | -48.4083 | 2025-10-26 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 6a882fd1-27ec-36ed-83b4-f644485d46d6 | -5.834 | -40.828 | 2025-10-26 14:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 94da2434-8f7e-3ae1-a1e2-f76c0dc4e845 | -4.3424 | -41.8067 | 2025-10-26 14:10:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 685de7f6-71cc-3200-8382-2e950a31c1a7 | -7.2379 | -44.9868 | 2025-10-26 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4bad42f8-76ce-3881-a231-a11dec781711 | -11.1419 | -55.1869 | 2025-10-26 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7ec11204-b396-309b-b549-d9ee134ec791 | -8.1609 | -43.3935 | 2025-10-26 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| 5b920f9f-9c88-3435-832e-9b3f895a7940 | -7.7971 | -45.3893 | 2025-10-26 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 279e3ece-25b5-3034-b96e-fc62a20942da | -4.8935 | -43.2115 | 2025-10-26 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| e1642ee4-ded7-3954-a8c7-f0fadd03c0d0 | -3.6091 | -49.3431 | 2025-10-26 14:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 98da7bcf-4c20-3d96-9360-60c794f59677 | -4.8933 | -43.2349 | 2025-10-26 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 243.3 |
| c1cd7156-c730-361b-846d-4ba5bf0ba86f | -4.3237 | -41.8078 | 2025-10-26 14:10:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| f33ee58a-2c2c-3a88-9441-09bc2f279002 | -3.7898 | -43.3921 | 2025-10-26 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c08d54e8-3f64-3358-b7c6-716d649b1b67 | -7.4113 | -44.6051 | 2025-10-26 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.1 |
| dd18e643-1921-33b0-ae28-6e1189539630 | -3.7896 | -43.4153 | 2025-10-26 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9a1a6326-69d5-309a-b892-828f580c7f74 | -6.3866 | -45.7594 | 2025-10-26 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 09acbf1f-81c2-31fc-940f-41d246f127fe | -12.363 | -48.1238 | 2025-10-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 1a33c68a-32f3-3e5d-b903-b6818dc2098a | -5.5908 | -47.1045 | 2025-10-26 14:10:00 | GOES-19 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 55f81e08-620a-3e39-9ef7-8f40ad4cbfb6 | -6.9108 | -43.9834 | 2025-10-26 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0fd8b049-7818-3b88-9c0b-b326a82cbcde | -6.5062 | -45.0041 | 2025-10-26 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b006fa6e-31a7-3f05-963d-be5a9cdace7f | -3.7024 | -42.3892 | 2025-10-26 14:10:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 2d4f2127-57a8-32ec-b4b4-fbf9ee5f40c9 | -16.1901 | -45.0841 | 2025-10-26 14:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 4a81507f-cb15-3ac4-adc5-88a308d51f18 | -12.2977 | -47.4658 | 2025-10-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fe84c0fd-c7b7-3638-bd38-66f738ea5a80 | -17.4311 | -46.884 | 2025-10-26 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 2b1efa90-a5a1-3f92-88a2-0721498d3469 | -15.2649 | -50.7535 | 2025-10-26 14:10:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 39a81f8b-6b52-39b8-ae7a-3c8b874ec2b3 | -13.3266 | -47.8984 | 2025-10-26 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 25323db3-32b6-3556-86c9-57e170f437f0 | -6.2118 | -42.5479 | 2025-10-26 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 250e1ec0-1cc1-3168-b7b8-58f500555987 | -15.2649 | -50.7535 | 2025-10-26 14:20:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |


[Clique aqui para ver as próximas entradas](README60.md)
