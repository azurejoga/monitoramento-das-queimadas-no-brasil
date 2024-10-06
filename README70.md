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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f699df5d-e8f4-3e0f-b7ef-42d43029ccca | -10.80736 | -44.76928 | 2024-10-06 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd794d79-1e61-3224-9b84-2f180dbc08f1 | -10.62044 | -45.18689 | 2024-10-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fae6df9-8a3f-3e5a-9b0c-a2609e9cf4e9 | -10.61713 | -45.18637 | 2024-10-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0059e48-ea16-39d3-b904-113a2424652e | -10.61382 | -45.18584 | 2024-10-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0efc95e-7b39-323c-9d63-74f05395fa79 | -10.61327 | -45.18935 | 2024-10-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd9757ca-1b40-366c-9528-a3a3487f7c67 | -10.46299 | -45.12929 | 2024-10-06 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61e6eb3b-bf5d-38c8-8e4f-470bbe815056 | -10.27185 | -45.48216 | 2024-10-06 04:19:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e650d2f-6e54-36f3-8cbc-eac0094c3aa6 | -10.27131 | -45.48565 | 2024-10-06 04:19:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 143ea236-4487-3c9d-935a-24888a02a1de | -10.15011 | -45.19815 | 2024-10-06 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1ad68cd-bb64-3187-9676-e2d873177cf2 | -10.1468 | -45.19763 | 2024-10-06 04:19:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 504dfd36-af7c-34fb-9229-eeac82f59fd3 | -10.14295 | -45.2006 | 2024-10-06 04:19:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91db4dc3-ffc9-300e-89d4-bc12f325cb64 | -10.14241 | -45.20409 | 2024-10-06 04:19:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3094f8aa-c5fb-3ee1-a140-19caf0126d5e | -11.6705 | -45.24581 | 2024-10-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36347d64-df55-341d-a45c-fb8fced326d4 | -11.66722 | -45.267 | 2024-10-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9191bece-c893-3350-b07c-88a43dfcd244 | -11.66664 | -45.24883 | 2024-10-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 949d06d9-a139-38f7-a486-ca7c92ea1044 | -11.66445 | -45.26298 | 2024-10-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a4af248-587b-3be7-8df6-16c381f89ea0 | -11.6639 | -45.26651 | 2024-10-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c915f88e-47c0-3bed-9329-e40ed8827597 | -11.33519 | -45.54525 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9c16e0c-c02c-3607-b60b-ba0eeb75942a | -11.1528 | -45.03706 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52d71712-7650-3904-88f5-f9311d5709ee | -11.15003 | -45.033 | 2024-10-06 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c352aa79-c273-34b8-9211-0313d131cae6 | -12.07394 | -45.59893 | 2024-10-06 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c837974d-1768-3e94-aa91-a7f9b5123ff0 | -12.74629 | -45.85894 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2db10962-8700-348d-b08c-66c3610251d7 | -12.5112 | -45.29575 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7975b5b-60d7-3365-8f45-71168d28c0ca | -12.51065 | -45.2993 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9191cf34-80bb-3335-baa0-c2fb4dbe6ebb | -12.50747 | -45.29923 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17c6c308-ee0f-33ed-9f3c-9c23db72f6d9 | -12.7444 | -45.45681 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6376e6ee-12b7-3a8b-bd77-c8b09cb7cc36 | -12.50802 | -45.29568 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 253c330f-653d-3144-aad3-072d07e748fc | -13.09823 | -46.38578 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0493ee3-82e6-3a8c-8417-615762b60666 | -13.09719 | -46.3494 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 204278ef-1886-3b40-80c2-a021594f4c1a | -13.09493 | -46.38523 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df7fa9e9-88af-3b5b-a49c-67d8547bf10a | -13.09443 | -46.34533 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3e28b10-76a9-34cb-a911-713c32c0da4c | -13.09437 | -46.38876 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6289369e-16a5-3e9c-b2b1-464756dc43e6 | -13.09273 | -46.37764 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f3ca5d4-9c94-3e82-928b-339afc4b69a7 | -13.21929 | -45.54713 | 2024-10-06 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 692a6c24-30fb-3d11-b0aa-3c66940e3a10 | -12.5036 | -45.30225 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a2b7c05-aadb-39b5-950b-58ea57ed49a8 | -12.50083 | -45.29817 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eece443-3649-3290-8c00-67a82344a859 | -13.09552 | -46.36 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70a637d2-a96a-3eb2-9fe1-b4cb83c3eb1b | -13.09548 | -46.38171 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e42acec-bdd1-3860-ba91-23ddda688a60 | -13.09496 | -46.36353 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c175cda-e830-3933-8758-a19ff23688a4 | -13.09388 | -46.34887 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6e6029c-5cde-3aa0-af87-c3deb14a0f60 | -13.09116 | -46.32306 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5174fbee-cf56-3f45-be60-639ea3f32261 | -13.09994 | -46.35348 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5fdf658-e59b-3138-b77b-a4dc51aab528 | -13.0983 | -46.34232 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 902c1386-fa10-3764-b0a5-fa59e65edf20 | -13.09771 | -46.3676 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adc529a6-b550-3fef-9dae-717bbb472050 | -13.09712 | -46.39283 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a5dd845-4079-367a-a648-71220a3444f5 | -13.0966 | -46.37466 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fec29ed-eb58-3bb5-bea4-a163c727fd14 | -13.09499 | -46.34178 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fde72694-4b84-37e9-bca2-1583515a31b5 | -13.09332 | -46.35239 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b8c54a5-88f5-305f-85ac-05ae4fc0efac | -13.0906 | -46.32659 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af17aecf-28c5-3d85-aece-43800d7b8e7f | -13.1005 | -46.3932 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f619575-4a5b-3bef-a7ea-b053dac56df2 | -13.09994 | -46.39672 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba6d737c-471f-3b3e-a739-90541bcc6e10 | -13.09774 | -46.34587 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbf255e4-3a62-31d3-a649-100ba71a3c67 | -13.09663 | -46.35294 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bff267f5-4b60-319f-a5e0-42d72a10d503 | -13.09329 | -46.37411 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84784e9e-be32-33dd-a6f0-19ecad40b115 | -14.20478 | -46.45494 | 2024-10-06 04:19:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6466fa8-af9a-342e-9290-74c17cf73376 | -14.20423 | -46.45848 | 2024-10-06 04:19:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 297149e3-be23-3d70-811c-6626ddcaf77d | -14.20147 | -46.45439 | 2024-10-06 04:19:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a765112f-5392-3d00-8898-c9d3d9ad7cd2 | -14.20092 | -46.45793 | 2024-10-06 04:19:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6759639-f6ea-3e33-b551-e083b4739ee7 | -14.08993 | -45.51374 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15972105-542d-3a26-bf9e-3388246e336c | -14.08937 | -45.51732 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31c2ee6d-0dd1-3ea8-94c4-758d97788733 | -14.08881 | -45.49886 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51cd3ea1-1bbb-3004-a28f-82557f721c0a | -14.08825 | -45.50245 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 783e662a-1585-38ae-a972-c155c22ab27f | -14.0877 | -45.50603 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0310e669-5cbb-3e2f-aeef-79c752e3125c | -14.08715 | -45.50961 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a74a2e4-856d-3c6e-978c-f315f92afafe | -14.08605 | -45.51678 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1260114-5aed-3d26-87be-dc23f5a9d4ed | -14.08603 | -45.49473 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7622494-1992-39ba-838e-91c54b4c33ff | -14.08548 | -45.49832 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64234af-05e8-39d8-9d65-06ce96cfa42c | -14.08329 | -45.5347 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc771c1b-b190-31ae-b4a2-da9857c3e881 | -14.08325 | -45.4906 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efead52f-c168-3924-aa2d-55e738961290 | -14.08163 | -45.54546 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a231190-7bee-3a23-a813-4f5f26210c90 | -14.08051 | -45.53058 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1503bde4-25c0-3768-bf10-fe2d7bb1badb | -14.08047 | -45.48647 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6a0a86b-33fe-3c6b-979d-bc5588652c98 | -14.07992 | -45.49006 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 617ad2c4-dde5-3ea0-a51d-578ae73fa739 | -14.07714 | -45.48593 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e60d684-58f3-31f7-88fd-4bc40979d711 | -14.07382 | -45.48539 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31fc3191-8889-3480-adfb-73153b20f6fa | -14.07104 | -45.48126 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea133693-3dcc-3fd9-bfac-184796e5d43a | -14.06771 | -45.48072 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c46ba42-a88b-352f-bf58-cac33df2a32a | -14.06438 | -45.48018 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32fa1ceb-168c-353d-82a9-efc9daadc08a | -14.06222 | -45.53865 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21ac331f-46ff-3933-860f-367813982c57 | -14.05945 | -45.55663 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aba4f791-016b-340b-9c82-70a80b3b6db1 | -16.52511 | -47.03309 | 2024-10-06 04:19:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e46a48ea-c4e1-3ca2-9b24-79a9f93ed292 | -15.90085 | -46.87793 | 2024-10-06 04:19:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 177e0bb9-da9b-3aae-ad99-5a9939cc42b5 | -16.52237 | -47.02895 | 2024-10-06 04:19:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f95f3a38-3798-3925-b755-e27066f6153e | -16.37601 | -46.87999 | 2024-10-06 04:19:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d5e9c1c-d52a-3308-ba3b-c8fdd2d9ce82 | -16.77661 | -46.61854 | 2024-10-06 04:19:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd23763d-ed0b-3f39-9862-3d4642669ccb | -16.65963 | -46.67302 | 2024-10-06 04:19:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 814e1d47-1239-3bbd-acbd-a3adb7387451 | -3.37256 | -45.53778 | 2024-10-06 04:19:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 546441f1-79b0-3bc8-932a-5982edbdfb1a | -3.36918 | -45.53724 | 2024-10-06 04:19:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f068be26-d071-3834-b5d7-405e8a0aa78b | -4.87136 | -45.77154 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1be1b52-64b7-3ecd-b4c8-8ee535e810d1 | -4.86798 | -45.77103 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 643675d1-ff3d-313a-8e73-0d83cce4f757 | -4.86673 | -45.95302 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e37ea4fc-6825-3ef9-9966-ab7862602621 | -4.86261 | -45.84805 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a645bdbb-53dc-31dc-94b8-d129c8c72df1 | -4.85866 | -45.85112 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3929685e-b232-381f-8ebe-01f9742904a0 | -4.84081 | -45.81105 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98c06c1e-4c2d-37ba-98f7-2217ef54d8ce | -4.8329 | -45.81717 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7d94c9f-e0db-30c2-8034-8195ec4c3657 | -4.82952 | -45.81663 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec887099-afe2-3a67-95e9-78c6309f1de0 | -4.57835 | -46.06919 | 2024-10-06 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f24fc2b-10a5-3b88-98ad-c1b9e9a6a8ab | -4.57776 | -46.07284 | 2024-10-06 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd5cdf9d-2872-37e7-bd66-8a782d4de15a | -4.57494 | -46.06865 | 2024-10-06 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78fc9022-039c-3091-81dc-4a8f1c658fa1 | -4.13157 | -46.09892 | 2024-10-06 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README71.md)
