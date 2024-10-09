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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b28bde70-f844-3586-b23b-ce743145c16a | -22.14926 | -48.12631 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b242cb00-bc0b-3c58-9170-46acd3026f8f | -22.14888 | -48.08689 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35ffd012-dbb3-3040-aacb-3bac091ae28c | -22.14862 | -48.13014 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4cfc2c5-9150-33b4-8706-648f9defb8c7 | -22.14844 | -48.1104 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0b6eb86-80f6-3167-bd39-cf12ef9380f8 | -22.14799 | -48.13397 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5aba7c2b-988f-399a-89f4-ba8297c74e36 | -22.14572 | -48.10596 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7151cc04-98c0-3497-8d0c-64ba0d3882e3 | -22.14553 | -48.08624 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d35eb5e3-dd4d-36fc-a03b-0994858546c4 | -22.14509 | -48.10978 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38d9f75c-908b-34e8-abd5-2067499bfb4c | -22.14446 | -48.11361 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e5af464-7f77-3347-98ab-589fa41e0fb0 | -22.14382 | -48.11743 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7532645-0427-348e-a0b2-5ac9f75ca010 | -22.14319 | -48.12126 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2311540-295e-3065-9294-31fdbb0a8c43 | -22.14238 | -48.10531 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e830b97d-0925-3db1-b760-a4cb9e8db025 | -22.14048 | -48.1168 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16e3320f-5e41-301a-b920-f105fa056dd0 | -22.13984 | -48.12064 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5fa8ca0-0c27-324f-99b4-b77051167c6b | -22.13904 | -48.10466 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 660251e2-d1af-349d-8c13-4deaab392e28 | -22.13713 | -48.11617 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3a09029e-0baa-3c3e-b921-6a769bedb7d2 | -22.13649 | -48.12001 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c177b7e4-5c17-3f38-9e8c-9278d49031f6 | -22.13586 | -48.12385 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9426877b-6e95-324d-bdc1-5ae00caa687c | -22.13488 | -48.08812 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 408e5fac-ee90-33ab-8fcd-4f1ae74cde46 | -22.13425 | -48.09192 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cd87b61-9b52-3121-8a8f-0035fefc287b | -22.13315 | -48.11937 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70c62bd1-4590-3af4-b648-d56b4fad8cfd | -22.13251 | -48.12321 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68fe2581-0926-3871-bce3-f1226dcb15d3 | -22.13091 | -48.09129 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9086704d-d96a-3598-b665-256853d03222 | -22.1298 | -48.11873 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 917f7a26-eb78-3e10-9613-8a75ac990d0c | -22.12917 | -48.12257 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f25d9fac-e4d0-33fe-82aa-5f12986ac6f7 | -22.12853 | -48.1264 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2b31e9e-f12a-37b3-bcf9-e4e33cd40d0a | -22.12693 | -48.09446 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2d3ea42-61a9-3200-8875-6c677dbe4dbf | -22.12646 | -48.11809 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bb58bd6-5700-375f-b28c-d295feb3f3b7 | -22.1263 | -48.09829 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b77cb92-bb8f-38d4-8f1c-2e0c575ad5d7 | -22.12582 | -48.12193 | 2024-10-09 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2fc02b3-bf21-3635-bce3-2fdeaaff0fb4 | -21.58662 | -47.96029 | 2024-10-09 04:17:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d4e1db9-6e4d-3ffd-bb76-35144fc69d0a | -21.58218 | -47.88977 | 2024-10-09 04:17:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 46ab115d-800f-372e-b83b-8e740bb82dca | -21.58094 | -47.89735 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45af2ac4-2556-3e8c-a3c9-abeb8355b075 | -21.57908 | -47.90871 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9843cdc5-c30c-3404-b859-0c72b42fc18c | -21.57822 | -47.89293 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a70cc520-f64d-3e86-819b-d70f3f95e2f6 | -21.5107 | -48.07239 | 2024-10-09 04:17:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bf6d0c0-1840-34ab-a5cc-584d672b5456 | -21.47877 | -48.09788 | 2024-10-09 04:17:00 | NOAA-21 | MOTUCA | SÃO PAULO | Brasil | 3532058 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5ea15eb-b634-391f-9543-4a088d215e45 | -21.6605 | -47.72079 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 45594eeb-a6a8-34f3-95f8-eeab6d850e6a | -21.67775 | -47.72023 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 590e05f8-6456-38e0-aba1-21099efd8fe5 | -21.67713 | -47.72398 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d104e5d-9325-3f01-8a56-39084d81c999 | -21.67652 | -47.72775 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a81fc162-8bfe-33ee-8b7c-3a91114318a6 | -21.67442 | -47.71958 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7cb3a4a-319c-3936-ab52-a3f9c50cad71 | -21.67381 | -47.72334 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 504c27fa-4883-3578-a4f9-9552d6200241 | -21.67319 | -47.72711 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1e11c23-cae2-34c6-b852-d0f21027afdf | -21.67257 | -47.73087 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f4fb023-586e-32e9-9dae-8a620c73a5ea | -21.67109 | -47.71894 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 167f6334-4a42-354f-b434-9bb22dc2b251 | -21.67048 | -47.72269 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 1525f63c-7b18-3d24-b4c8-351ae1dcba85 | -21.66986 | -47.72647 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 174.5 |
| f6fedc94-4dd3-3ade-a1f2-3117ff1ea088 | -21.66925 | -47.73023 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e52ccc09-5a09-30fd-9dbf-a5a0cfc8ea83 | -21.66777 | -47.7183 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 52.2 |
| b32a95f0-4ba8-3535-8725-7feb9205cacd | -21.66715 | -47.72206 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 4e80b557-7364-3f57-a28c-273693d60045 | -21.66653 | -47.72583 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 05bec472-9805-3848-a79f-8c1352d7ef9f | -21.66592 | -47.7296 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0ea8339-1545-3e53-9f97-c36c5504ed8e | -21.66531 | -47.73336 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48a168ff-9a9c-3152-96f0-5ea9a3d051a1 | -21.66383 | -47.72142 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.0 |
| bb14e931-81a0-3d4a-9b7b-8c30685ba141 | -21.66321 | -47.7252 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 2afc0d5e-eb65-3ab1-91ac-eb83a0351b00 | -21.66259 | -47.72897 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b1926fb-da70-3309-84f5-8e10f18c2e9e | -21.66197 | -47.73273 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31dd4fdb-914d-3dfa-b06b-a01c4a074440 | -21.65988 | -47.72456 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.0 |
| bed46964-d66e-351c-8e5d-417ae9eeaa6b | -21.65926 | -47.72833 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8714bd4-2437-3fb3-a105-f5b7280c6f1f | -21.65865 | -47.7321 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cd6b8dd-e124-3bbe-a2f9-ae05809b070d | -21.65717 | -47.72016 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 6ebe3627-9af0-30d7-abc1-90f5233ebe52 | -21.65656 | -47.72392 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| e0c01d7d-cbc4-3a95-a79f-f34387423be0 | -21.65594 | -47.7277 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3d9360d-dc0e-3e5a-8930-58066afc6d5f | -21.65532 | -47.73146 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87ccb112-1bc7-3386-bc48-c647830ab754 | -21.6547 | -47.73524 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d07898db-af27-3010-b9ce-39d5c4485a04 | -21.65385 | -47.71953 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 895a0690-9fca-3b1f-8c8a-01a1092d832b | -21.65323 | -47.72329 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 6c6dfe15-aebd-3277-9461-8ef702989d32 | -21.65261 | -47.72705 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52466de6-c038-340b-86f3-bc635492bad5 | -21.65199 | -47.73082 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dc31a24-605a-3fb1-9125-005050d481e6 | -21.65052 | -47.7189 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62609e0d-5245-35d1-898d-69ab6d77fd90 | -21.6499 | -47.72266 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55cf8821-023f-335e-a262-88ac33e76a7f | -21.64928 | -47.72642 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73ccdee9-10a8-3e0e-9de9-2226ff58891a | -21.64867 | -47.73019 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1342b26-8dcc-39a3-88c8-88cfed70c6d2 | -21.64719 | -47.71827 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73dd1d9f-a4cd-30a4-9595-551ba46a5b2d | -21.64657 | -47.72202 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c15cb1d-b9b1-3b64-b31d-7a7c054386b0 | -21.64596 | -47.72579 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8b1cf04-dd16-36d7-8b73-689af368931b | -21.64534 | -47.72955 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8bcfa0c-fb54-360d-8127-13ad2a0b38d8 | -21.64386 | -47.71766 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12014599-cede-37a0-bb3e-26aca1e63eb8 | -21.64324 | -47.72141 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a25dc12e-4846-32bc-a839-068b41388852 | -21.64263 | -47.72517 | 2024-10-09 04:17:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc44091b-d6b7-32f1-abc2-a0d12a3e57a4 | -21.09166 | -47.21787 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 206edfea-a914-399e-ab93-bfbd61fe8709 | -21.08954 | -47.20988 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faeff1e2-e8af-3445-83db-2ca6aab38ebe | -21.08836 | -47.21722 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 103c5999-c576-305d-928e-2875d40c7e8f | -21.08623 | -47.20928 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee8979cc-e34b-3bb2-a189-9990c62a9b09 | -21.08564 | -47.21294 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 184d96dc-5829-3911-8f8a-818cd443be63 | -21.08505 | -47.21662 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06610f56-e19b-373e-9b35-348708f955a2 | -21.08232 | -47.21238 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c221cb8-7ee9-3b10-b601-6af53771ec2f | -21.08173 | -47.21605 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb663861-8c26-36b7-928b-411267f80ed1 | -21.08114 | -47.21972 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebfea0c3-27a2-3421-b89b-146e5bd1282d | -21.07841 | -47.21548 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7041e741-5cca-3dba-af84-79eee0e2b664 | -21.07782 | -47.21915 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bbf41658-37e1-38fc-a40f-69eaf96aba57 | -21.07508 | -47.21492 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 89283963-cc11-3b47-a0df-93657ba36263 | -21.07449 | -47.2186 | 2024-10-09 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 066e0aca-cf9b-3acf-bd86-a3ec4ed0b8cc | -21.5827 | -46.97865 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9ed98b3a-3a93-3c01-900d-8246bfe9b40b | -21.57161 | -46.98425 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01512518-3745-362c-ac6d-cff648c5d48a | -21.56052 | -46.98985 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dff34886-d45c-3215-a133-f213872227f5 | -21.55956 | -46.97447 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5c5659b-869a-3459-a1e9-13649f2a65b8 | -21.55839 | -46.98185 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a8a8c2f-d34c-3ca6-b4c6-b71e6d7e0e20 | -21.5578 | -46.98555 | 2024-10-09 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README91.md)
