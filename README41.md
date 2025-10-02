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
| 7b77ee2c-b3bc-3765-ad6e-4e8ec8eb35b8 | -15.2955 | -45.08362 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea2b6409-fdd9-3791-8873-2b140cd53b30 | -18.13073 | -39.65218 | 2025-10-02 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce8094e5-b579-36cf-b5fe-5dc04b3a2ffb | -14.6502 | -48.15256 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8fc43dd-66e0-35f9-be2c-93a9ec1ae934 | -14.32596 | -45.87883 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2915cd95-4c46-3065-918f-9b78aad266b2 | -13.16074 | -47.82173 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5998c73a-4e6b-3830-b9b5-606b999d51c4 | -19.56171 | -43.16997 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5a0b33e-2b7a-34dc-b968-acf0a86c71ab | -14.67021 | -48.1167 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d37be5a-3d7e-3505-a01d-57894f97b956 | -13.30842 | -47.19397 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b46c614-454d-32bd-8014-7dd51bf329bf | -14.21494 | -46.09157 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3efa7b71-f855-3172-81e9-7323fba09366 | -14.65617 | -48.26434 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7f16467-7841-36f6-bbb4-538dd470279e | -13.78183 | -48.05109 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71db7d1a-eae7-3b13-be1a-7ca90bbb2e67 | -13.1695 | -47.82254 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 23de00ce-7d6d-33a0-a285-cfb933d5ff27 | -17.56202 | -44.80167 | 2025-10-02 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9c3062a-7e2c-3606-aaf3-715d4111e3cf | -14.33555 | -47.12729 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac62d71a-e226-355f-a913-e99b9ec1da75 | -17.01683 | -49.14968 | 2025-10-02 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dddb0b7d-da84-31cf-b1b0-8d7f82caa3d3 | -14.42405 | -46.12048 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9631c2f3-5a4f-3326-8a98-542d4481a9cb | -17.68267 | -44.43526 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5082223e-9de3-3ded-b6ab-9545f703d38b | -13.22143 | -48.43779 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ab1ee83-18d5-3063-a52c-62198f5e6b03 | -19.95523 | -43.65069 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8519e1ef-cb39-330b-a4b4-d58de4528e73 | -14.89444 | -48.32446 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8372ae6e-61d7-3ee9-b1c5-c9f225e50791 | -14.48348 | -48.41101 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d2ce42b-13b3-361d-b6c0-95b341412899 | -14.87715 | -48.12959 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2f5e315-6d8e-3848-92e1-5545fe85ca56 | -13.31929 | -47.20463 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1d90caff-fbf9-3631-a8ee-d019f9e2ba5a | -16.01004 | -50.91174 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc7145fa-f60f-31cf-b296-5216b8cde0cb | -16.01509 | -50.91263 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 391a10d6-817f-310f-bda7-b58e35ef872d | -13.37711 | -47.28827 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11703c27-a1b4-39e4-a4e1-78e40731dee1 | -12.49533 | -50.25663 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9fccca1-272d-3de4-8ea2-e1545d2d0894 | -20.11485 | -44.39016 | 2025-10-02 04:04:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2372d74a-a391-3a1a-8de2-85681260343f | -18.5056 | -44.04726 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91e55d1f-6bcd-3ea9-8ec3-153b5c04e8f9 | -18.31322 | -44.03167 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43977725-65a2-3233-a277-0a6e30305989 | -13.37132 | -47.28328 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5b8f699-e429-36bf-8dd8-ff0231fb562f | -14.3254 | -44.5029 | 2025-10-02 04:04:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 712311d8-9973-3723-8efa-cbb1dd63a9a4 | -16.37048 | -47.06776 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cee7bafd-49cd-33b2-b7fb-5e313a4130a6 | -14.27605 | -45.94219 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 791d0149-0144-3c4f-b042-7742c29887cc | -20.21779 | -44.1788 | 2025-10-02 04:04:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 70e86d31-d9dc-3be5-b4e4-aac667d240a3 | -17.55223 | -44.48008 | 2025-10-02 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 545f0fd6-09ac-386b-b0e1-41a4c678460b | -17.17558 | -47.0201 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6055be78-3368-39eb-9f42-b103f596b431 | -19.70876 | -44.43761 | 2025-10-02 04:04:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3022d350-b989-37a3-b659-5629aa5ae910 | -12.57521 | -49.89901 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37775bef-1a82-3f06-a254-8ba4978e6132 | -15.34799 | -47.09166 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df6bada4-9241-3e98-99fc-69f24893fba6 | -13.13295 | -47.41638 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 621e4d95-ad5a-37b5-905f-7d127f35a525 | -13.3112 | -46.99466 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f354b0d-519b-3b08-b185-93d1271a0df7 | -14.31285 | -45.99856 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 800d39fb-2b1a-3ff0-aea4-f8274dd03348 | -15.64324 | -46.25564 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 882b38fc-dd7a-3d68-9f5e-892b936accd3 | -18.65861 | -43.69004 | 2025-10-02 04:04:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 927209ed-702e-3919-a116-499baef2102f | -13.36765 | -46.34516 | 2025-10-02 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4203a344-9a21-3950-b76a-5b8884fd800a | -14.92249 | -47.22427 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fc0260b-e6c5-316d-861e-79deb50872ac | -15.34158 | -46.2643 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ecdae93-2ab3-34fa-8d96-bf1e0de39b6c | -13.06065 | -47.06075 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 050cdb70-a938-3f02-80a0-bbe66ec951de | -14.16633 | -46.12249 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1564b06-56d2-30ef-810f-6f5d7b9b51cc | -14.41137 | -46.1033 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc235bea-3b65-3f7f-a5c5-b8e104205e4d | -18.99808 | -43.00945 | 2025-10-02 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dbb75c6a-6f65-3916-86cd-655f7b78de69 | -14.39866 | -46.08641 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ab7bddf-7daf-3494-af0a-310cfaf3723b | -14.98416 | -46.90839 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa55a30b-8200-3541-8df5-0365a3f6d553 | -14.89718 | -48.09318 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 21f92ada-50d5-36df-a361-e8f06c2b89e9 | -19.85506 | -44.08331 | 2025-10-02 04:04:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 845ff1f5-c671-3594-9461-a291d7af3d8c | -20.73586 | -46.03151 | 2025-10-02 04:04:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e252e65a-1f35-3c1e-83df-21f91561aa1e | -19.371 | -41.75272 | 2025-10-02 04:04:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 718272fa-a68d-31c9-bc63-94da28c3e1b3 | -15.46647 | -45.87873 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab59373e-efaf-304c-a202-c5a41e4b4611 | -15.2062 | -48.00267 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa88797c-560c-3fac-86ef-a2b45e04f2e3 | -15.39468 | -44.97331 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 817e4744-0c28-34d5-8e8a-d4a35f162f92 | -15.549 | -48.17856 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac3761dc-2cf4-3ccd-87d4-75801b0a0a5c | -13.68485 | -48.06627 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c312f94b-646e-3dc9-a5d0-a7c382d44e98 | -12.49739 | -50.26251 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc9f752b-507b-3913-99f3-9dac7885bd46 | -13.29439 | -47.24774 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1e99dbe-b457-3541-8053-3518a0b9a181 | -12.57131 | -49.89376 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35ed4e64-54a3-30c8-909e-c791940dd6a9 | -14.22104 | -44.92968 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50c2e44d-7ce0-3670-8508-8f0ebebab78d | -14.91229 | -47.22997 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87c587d8-db9f-369a-b568-32530d3ea5fd | -13.18179 | -47.83911 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 43c61460-6cf3-37f5-8a37-839655233735 | -13.23742 | -47.34109 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a871ff87-9543-3e3a-b6ea-26976b0a1444 | -15.76208 | -43.67335 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16a647db-09d6-3e10-88bb-6df9babab4cd | -19.42078 | -46.80853 | 2025-10-02 04:04:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d4e6e0e-3b1d-3170-bb71-1b8391fd5646 | -16.00501 | -50.91078 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b46de7b-a4a8-3cea-921b-922386ee0a24 | -15.78351 | -43.71149 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b114494c-acc4-3c9c-ab54-bbb0a175f35b | -15.25826 | -49.27229 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 90ce42f6-2dc9-3e77-af54-1c49531735e9 | -18.47035 | -43.07803 | 2025-10-02 04:04:00 | NOAA-21 | MATERLÂNDIA | MINAS GERAIS | Brasil | 3140605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08ab3992-a0a7-31f3-ad4e-37a3992874ef | -15.99408 | -50.91319 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 634f6c12-33fa-39e2-8da5-013b5b203c88 | -15.21668 | -47.1711 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 030af309-a8c2-3c8d-8fba-3d639a1f8245 | -13.39937 | -47.77929 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 269a3f42-aaf3-3fa7-a358-7d83916f7712 | -13.14995 | -47.78254 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30fd02a6-9759-3b63-bca6-e2e5c3d8496e | -17.16612 | -47.02851 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c9a448ea-ab5e-3159-ad9f-2f2d2de77ad2 | -20.12632 | -46.35436 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a7786cd-164b-3256-b6f8-3a33f5d10e72 | -14.42487 | -46.11572 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 53d9262d-644e-3138-8819-624246972ff1 | -15.27988 | -49.30695 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 453eb3b2-a602-3dc0-9ff1-365a96b77db0 | -20.21447 | -44.17822 | 2025-10-02 04:04:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7dc6f2b5-799b-3129-9dc6-3375ba59d7bd | -13.38591 | -46.95059 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cdfde94-a823-3d57-8b03-a51423c48593 | -14.47284 | -48.4442 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29f5d909-4e62-32b8-9519-30436dfac861 | -19.56444 | -43.17418 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0acdd8c3-a002-3d2b-8bb1-60e6c1f68c4a | -15.18462 | -46.42265 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d17d2eda-ba86-3853-9e28-21511458ad40 | -13.24777 | -47.33128 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8947eb8f-0a80-363e-baec-dd0401f80e45 | -13.30696 | -47.84854 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 32e8e758-2095-3d7c-b781-dc7e984c4e23 | -13.75727 | -47.96441 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfbfbaf5-02f9-340c-be10-68ce127cf139 | -14.22292 | -46.11356 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35499f30-6ca4-3cd6-b69b-57d82a041782 | -14.59936 | -48.32266 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19808ff0-1cc0-32da-b05c-57bbeb470eff | -15.46198 | -45.88267 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 778bfc3c-1db7-32a5-9dd3-394b242bf91b | -12.59022 | -49.90189 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f65fa70-061c-3f80-8109-20bb9ea0dc5b | -15.94595 | -43.34116 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 309f3b1c-559a-3685-bfca-922edbf0bbe8 | -13.4218 | -47.79194 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d7992928-1ed5-314e-8323-960ce4ba8840 | -14.59523 | -46.712 | 2025-10-02 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8b1d0ab-e971-3b25-b74d-7e8171e6d9ee | -15.554 | -48.17524 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README42.md)
