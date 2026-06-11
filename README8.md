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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3977bc9a-190a-3a3e-9495-597d51faae69 | -12.0903 | -48.4111 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b830c116-7252-30d9-82a8-9fe5828eb1d0 | -12.02481 | -47.8025 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8230636-376c-3532-959b-96a49f4726fa | -10.84335 | -46.78717 | 2026-06-11 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d1ff7a7e-66e5-3f05-ad63-20e4fb31902e | -12.14388 | -48.46028 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df597727-3264-3560-a4c6-e19fbfaed318 | -12.03473 | -47.80412 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af19c628-5977-3096-b93d-425ea0bc56de | -13.26583 | -45.57492 | 2026-06-11 04:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea11696c-72ab-342e-81f5-e0b8dcfd93ba | -10.98791 | -46.75256 | 2026-06-11 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d663fda7-7753-31ed-a64e-d6b5a888734d | -14.62454 | -48.00874 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c680342-e039-358c-8700-1373fedd0b7c | -12.03487 | -41.38525 | 2026-06-11 04:32:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9101a08d-1c73-380c-b341-4b98faea7fca | -12.01196 | -49.27293 | 2026-06-11 04:32:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 22bbdee5-5e7d-3e42-977c-3208a72121a4 | -10.90005 | -49.35516 | 2026-06-11 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7411b7a0-e935-30de-8478-cac4624a9e89 | -14.37921 | -47.92797 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02cf0ddd-328b-3f6a-a3f0-78b1c06eac23 | -12.86585 | -44.37199 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 644935a6-78a8-33d2-b3b3-45b47f4b2264 | -12.85188 | -44.36547 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ce1e961-79c4-30f0-9567-f0386fd7e87f | -14.6444 | -48.01188 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48162029-0035-3c47-94b2-42b00b5c0c1b | -12.05514 | -45.29262 | 2026-06-11 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a140f492-bf29-38bd-a8e4-019067541875 | -14.64108 | -48.01148 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb946250-4f1c-3a55-96db-2881f8c35c4f | -12.37072 | -47.89129 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7dcd8acc-0e0a-3d2e-9ecb-10dde1cfb484 | -13.54434 | -47.81656 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a9b614f-fa25-3c04-902e-e8c89a14a981 | -12.3641 | -47.8902 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faa6beae-d789-3b84-b3f9-d3608a369d07 | -14.63065 | -47.99153 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90e4126e-8f43-32c4-ba20-b0a6aae76fce | -11.98548 | -47.38504 | 2026-06-11 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8506024d-87ff-3484-9783-4745fec33012 | -11.79941 | -48.79787 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a39db865-ec73-3646-82bf-f916020b6c42 | -12.01535 | -49.27351 | 2026-06-11 04:32:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0475548a-21b5-3877-b407-1b040d556abc | -12.86157 | -44.37578 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdf4b1c7-5d25-3333-97a2-653e3f07cfb9 | -12.31054 | -47.90666 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1aa3ef82-5732-3f51-b1ce-953a1d623abb | -11.81066 | -48.79231 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c7149ad-e447-3041-b132-fb35ab10ab5e | -11.87023 | -47.10312 | 2026-06-11 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7587779e-41a0-36e0-bb5d-51bf2f3f19b4 | -13.54764 | -47.8171 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55529233-51c6-398c-960b-217f21589723 | -12.14835 | -48.4537 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8558b7f-eac0-3845-9110-91937c0a7297 | -11.10702 | -49.10069 | 2026-06-11 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 080cddfa-85dd-33e6-bc74-d8e76760f920 | -12.03238 | -41.38278 | 2026-06-11 04:32:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4752aead-a26a-32fe-8c11-ea1bc1f97021 | -12.85855 | -44.3709 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bbb3fdf0-52f6-38ea-b093-0ea5aefb8500 | -12.36741 | -47.89075 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 324441e3-32e5-3a7a-9263-7768691937a7 | -12.03142 | -47.80358 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe1dd11-0496-375d-bfce-1ac322a4403e | -11.30771 | -47.33268 | 2026-06-11 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21cd5367-cb22-318e-b222-70a96d63dcb2 | -11.58147 | -47.44947 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b284d26e-efae-3859-b46d-0ab30361370d | -14.6422 | -48.00437 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be203d93-8f00-3644-bc3e-72861fedf859 | -12.14502 | -48.45315 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 906bdf72-5e03-37f8-b59d-b4e8c9cb964b | -12.85981 | -44.36222 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0443668b-dc96-372f-be65-95a5e0cf4c10 | -12.30723 | -47.90611 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44021d1d-bdce-332f-a1e2-17cb03b73d96 | -11.94247 | -46.74831 | 2026-06-11 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3af8ea4a-86e3-3947-ac31-dcb4831f71e6 | -15.18173 | -43.85079 | 2026-06-11 04:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e686fea5-1387-3f32-a4d8-18d18d5961d3 | -10.84667 | -46.7877 | 2026-06-11 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fe724184-135e-3496-84bc-308bd7cd8f22 | -10.8439 | -46.78365 | 2026-06-11 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad9c97b7-2c9e-3162-97f7-9a40c4438111 | -11.58202 | -47.44596 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68eca161-088c-3658-a262-d44f13a5ecdf | -11.80277 | -48.79843 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f60cd5cc-b102-3836-a31b-dc3a9329c320 | -10.87679 | -49.53944 | 2026-06-11 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28134a73-5924-389c-a5aa-fb505842553c | -12.77976 | -46.81947 | 2026-06-11 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a44d2aab-751a-38e8-bb53-188367ead5b6 | -11.98272 | -47.381 | 2026-06-11 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e95a019-1f6b-3a28-aae0-6415e08113e5 | -12.1495 | -48.44657 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bbb7a8a-d4d6-3fd8-b652-7ed71fe5238a | -13.36884 | -43.20278 | 2026-06-11 04:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c61ed52-a9d6-3a39-9f71-0832bcffdc1b | -12.85792 | -44.37523 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c1956df3-ae89-38e4-8ff7-68a455d7def7 | -15.96641 | -41.66187 | 2026-06-11 04:32:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d0157d4-229d-3054-8725-843cac73c52e | -11.31046 | -47.33672 | 2026-06-11 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7c665e5-1250-38ff-bd84-d206658b1ccd | -12.36685 | -47.89426 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ba9f0c4f-d4fa-3e67-9c17-5854635ac12c | -12.0696 | -45.29084 | 2026-06-11 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31fba421-7e44-3b94-90e9-478b83e7addd | -12.8549 | -44.37035 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| cc930b63-5375-3876-a727-bde46c09b095 | -12.05167 | -45.29208 | 2026-06-11 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17dca3f6-948a-3a64-98e6-811b77fbd07c | -12.1433 | -48.46384 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f38156fa-1002-32ca-8723-587139b790b8 | -12.05861 | -45.29316 | 2026-06-11 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4e522cf-0b75-3a63-97cb-20772f66c19a | -12.86283 | -44.36711 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a05acdea-9012-3322-93d7-1a8771e707dd | -12.08972 | -48.41466 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7276607c-24b5-3b85-b164-0743b67701c7 | -14.63777 | -48.01093 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37391f94-ca4a-3b62-ad46-9dd40b90cb77 | -11.5786 | -47.44511 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3aa9885f-23fc-3cab-85fb-12f940af9dda | -12.78094 | -46.30402 | 2026-06-11 04:32:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c6fdcb7-626b-35cc-a3ad-dfac3cdf2af6 | -15.17786 | -43.85022 | 2026-06-11 04:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c893f4a-dcb4-348a-865f-8d251143be3b | -12.06612 | -45.29033 | 2026-06-11 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ad3dbd8-9f72-3b86-add3-702556048d65 | -12.8622 | -44.37144 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29d88f14-71eb-3e5b-b23f-41209500b294 | -11.57804 | -47.44861 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c860374-0184-333e-bb65-1f85cd70ff9e | -11.8 | -48.79425 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 133a8973-f6b0-36b4-a0ae-f36049d14f30 | -11.98217 | -47.38451 | 2026-06-11 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 116704a8-3763-3026-a79b-8b437d8bf79a | -12.30667 | -47.90964 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 572d5f39-0823-3881-aa6b-3512efcf2e4f | -11.97831 | -47.38749 | 2026-06-11 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14b4ec7f-04ef-3b2e-988c-59a380a7eb73 | -11.87409 | -47.10013 | 2026-06-11 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ff9a2c3-5f88-3864-97b7-298d3207ca27 | -12.06207 | -45.29369 | 2026-06-11 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9e4aa75-b38e-35b1-903f-47b888768dc1 | -11.79804 | -48.79381 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cc91b83-f0ff-3869-9e0a-f3f69f151e9a | -12.7792 | -46.82305 | 2026-06-11 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2ab1132-368a-38d4-af7d-f8beeee21d40 | -13.53939 | -47.80488 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f58d6d8-7e47-3160-9256-c1bd8077553e | -14.63009 | -47.99508 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f8ca932-1716-33f0-b21c-0876fdbee8e1 | -11.81125 | -48.78868 | 2026-06-11 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81043df6-4251-3c77-b684-b62ab3b2acb3 | -12.77866 | -46.82661 | 2026-06-11 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04412add-81b8-3691-8600-76115de85d00 | -13.55151 | -47.81411 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daa7a8ad-1a45-3780-b251-16add2b335d0 | -13.53553 | -47.80787 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f163bd4-c115-3306-9a75-33fdbe6e7c9a | -11.84461 | -46.63425 | 2026-06-11 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f982a977-2a45-3dda-baa8-6cb6996fd862 | -13.36491 | -43.20221 | 2026-06-11 04:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ba23b6a9-65dd-3c10-b9e0-38758f4bf9e0 | -12.74865 | -49.89174 | 2026-06-11 04:32:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54fe9578-08a1-3957-a42b-5512b68f7901 | -11.84127 | -46.63372 | 2026-06-11 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa8c2c41-1154-37a8-82c6-035f6ff3c82b | -12.30336 | -47.90909 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a0e44e9-4af1-3749-b788-4e3829a667a9 | -13.5482 | -47.81358 | 2026-06-11 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5f8681e-4317-3cc6-8101-d8d2eec978ef | -14.64826 | -48.00887 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c42c1707-e14d-394a-a11b-5d13fb75fdd3 | -11.10824 | -49.0933 | 2026-06-11 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| accb39e7-4a1f-34ac-ae8b-9eb8c8e6bf6f | -11.10763 | -49.097 | 2026-06-11 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 137f1720-e4ab-3d05-ae7e-1c0ed1a96025 | -12.02811 | -47.80304 | 2026-06-11 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71f11cc7-f64d-373a-a6ae-1db338c1219b | -11.38606 | -47.20159 | 2026-06-11 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70caaceb-38cc-382f-99cf-027640e60060 | -14.6251 | -48.00518 | 2026-06-11 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bec427b-01bd-3749-9370-4f7265c88b2c | -13.36933 | -42.42231 | 2026-06-11 04:32:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf3f6877-ec4c-3ac7-9d7a-65103a2de500 | -14.72063 | -43.12305 | 2026-06-11 04:32:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fe8771e5-7b0f-3969-8c4d-086f3d253a3f | -12.30392 | -47.90557 | 2026-06-11 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c72aa1a3-26a7-36c8-8cdf-08d582c9dafb | -12.85553 | -44.36602 | 2026-06-11 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |


[Clique aqui para ver as próximas entradas](README9.md)
