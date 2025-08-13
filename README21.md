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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 411d25cb-89e9-3208-be00-83bf9b7b4af6 | -12.58623 | -47.00284 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3e83534-e799-3e76-8b53-da8248157349 | -9.194 | -59.65745 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 55a39f6d-6135-3c85-9a32-da14b5b85d80 | -9.82856 | -60.76375 | 2025-08-13 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ea0081f-96cd-370e-bba0-50660d10dab4 | -9.77418 | -48.36777 | 2025-08-13 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6d0c59a-9b8c-3a5b-b0b9-096b56d18105 | -6.10489 | -59.92859 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ed4e006-d52f-3d14-b6c4-e24fc34f3e28 | -12.58254 | -46.97424 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 009a07ee-3d27-3418-9779-5d297b865d68 | -9.3882 | -61.53326 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bdfcaed-b406-3e6d-ae03-b74501b90a7c | -16.30776 | -52.9225 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ab61179a-259e-304e-8eef-50be472d6d2a | -17.05069 | -51.79695 | 2025-08-13 04:42:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5360077-1063-38de-9261-ff1244205c14 | -17.66543 | -46.6821 | 2025-08-13 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7697de9-f41d-38c7-84db-f1143352f051 | -14.01348 | -52.06046 | 2025-08-13 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32702c89-1e30-3fda-aec7-638fb6084c6c | -12.36229 | -59.84238 | 2025-08-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2df18544-0d84-3892-87aa-7c3418d61fe0 | -13.51538 | -48.18499 | 2025-08-13 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 167261b0-29bc-3f76-bb5e-04b2609fb3f9 | -16.3919 | -50.88787 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f7684c3-6a9e-34ce-9d82-004e801d6008 | -16.29915 | -52.91695 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfa460b6-319c-32d3-b4d2-1dcef7db99a4 | -16.26925 | -47.87759 | 2025-08-13 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d8c6114-59c8-33c6-bdc3-917f4a96a1d9 | -16.39969 | -50.88166 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 37b0d210-ef0d-3dd0-a69c-2302d9056044 | -13.88315 | -45.57364 | 2025-08-13 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5e65410-6957-3f0a-ac5b-8aa63260827c | -16.3129 | -52.912 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9eeb7ee-614f-3571-826d-6a78a657ce1a | -15.60636 | -48.24228 | 2025-08-13 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3733c279-8008-315e-811b-c108196f3d85 | -14.61065 | -51.33533 | 2025-08-13 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 954a89b6-240b-39a8-a682-e09dab3e53f7 | -16.28973 | -52.91154 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9847c7ae-8bf4-3dc6-8ca3-ba9f3b0c9eca | -12.3654 | -59.84332 | 2025-08-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4cb8fc6-4e55-34bd-bcdb-f661c87c773f | -16.30523 | -52.92179 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60e5b357-cbb3-307a-8627-3384624fddc7 | -16.31624 | -52.91256 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f51bfe1-bc88-3df4-b965-aa72b31bc7cd | -14.00238 | -52.06595 | 2025-08-13 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 878c0770-7feb-3acf-b3cd-bdcbdf1b8e3f | -13.54263 | -47.62806 | 2025-08-13 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c853847b-549a-3373-9175-68f29b1ab029 | -16.39913 | -50.88536 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8118580f-2cd9-3db7-b53f-f331e4883ea1 | -16.3117 | -52.91936 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a7666d4d-7b94-3f8b-b7a0-a9df7dae39d1 | -16.29385 | -48.01261 | 2025-08-13 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55d8a02b-2da3-3b59-beb6-820d4fabfe0d | -18.53838 | -46.05724 | 2025-08-13 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 32.2 |
| e41461af-b635-3450-9f67-597e6376a54b | -16.36196 | -50.60836 | 2025-08-13 04:42:00 | NOAA-21 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b9d9939-cb3a-3f66-8f58-97fdaf064f53 | -16.36807 | -46.8796 | 2025-08-13 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68ece441-4a20-3c8e-bfb4-b4e9ee7d361e | -18.91574 | -48.22419 | 2025-08-13 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67ce9676-3eb4-3153-b8b9-ad7747d868fa | -16.51244 | -47.84985 | 2025-08-13 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1eb5719-1907-38e5-90e1-d8b77c9d4bae | -16.7389 | -49.35566 | 2025-08-13 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d71ebcbc-b01a-3522-901b-deb9918e7ed3 | -15.09734 | -51.35299 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cacf613-d7ee-3111-b3ab-20e972afe295 | -15.08685 | -51.35492 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd91a099-5c7e-30cc-881a-cd9d5e777e93 | -16.91225 | -48.14998 | 2025-08-13 04:42:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7594f21d-5774-30ed-bfe4-af7f1718a5a5 | -15.09292 | -51.35957 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c2941d4-8a59-3cd2-af7c-0439f06aaa47 | -15.09403 | -51.35244 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2d77211-a813-3251-b2a0-5457e3966350 | -16.9112 | -48.14776 | 2025-08-13 04:42:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d777ce15-552a-3f22-a1d6-2f7b05bda473 | -13.53216 | -47.6222 | 2025-08-13 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6d330ef-d51e-37ba-be9f-1cecaed1a4ba | -16.73967 | -49.35442 | 2025-08-13 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35a8919d-1605-3f3d-bce0-be487b8a38e5 | -16.68469 | -46.64335 | 2025-08-13 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e65a630f-de53-3feb-a4da-7a4efc51e742 | -17.05125 | -51.79335 | 2025-08-13 04:42:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d76a7096-d7d7-3db9-bf4b-d42325e9b270 | -15.55904 | -43.15629 | 2025-08-13 04:42:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e446834-0d08-33f7-9933-caa2b450887f | -13.88001 | -45.56513 | 2025-08-13 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d999b45e-445e-3dac-ac6b-44c0251c6dd3 | -18.92019 | -48.21994 | 2025-08-13 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 273f7a1b-ef94-3949-a50b-4f294a639db6 | -16.30641 | -52.91441 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44295113-ee91-3f7e-9683-b19a37756317 | -18.05463 | -47.94042 | 2025-08-13 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d10a7b4-3428-38df-9070-64777a114369 | -15.09348 | -51.356 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aec1b3e-126d-35e4-aada-55f4b99b427a | -15.5594 | -43.15317 | 2025-08-13 04:42:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d91cc108-2999-3843-b9e0-4433ecc306f4 | -15.09016 | -51.35546 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b361a94a-17c3-3798-8891-6c8d92cab613 | -16.30836 | -52.91881 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ad7a62ef-13d3-3849-a211-79e215f808fa | -12.36745 | -59.84324 | 2025-08-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17563ce2-af64-30b5-b016-819fe3fe131c | -14.12333 | -44.31331 | 2025-08-13 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b749fa2b-f6a9-3c17-8112-149b1a993cf3 | -14.11813 | -44.31752 | 2025-08-13 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc88e879-77c0-3e7f-ad19-db438818f0f8 | -15.70803 | -56.39806 | 2025-08-13 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73f02b0b-b006-35fc-8f3b-16084172a104 | -16.508 | -47.85408 | 2025-08-13 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbc6a9f7-b3f8-3a6d-9737-e3891650aa94 | -16.30307 | -52.91383 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27d85a3e-ccd0-38fa-b6f4-ccbb83e17759 | -16.29974 | -52.91325 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9bdaa50-f95a-3f8b-a9f7-c7a39a6cec0e | -16.40246 | -50.88596 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1171d2a-bc9d-391b-ab54-ffb20038e662 | -16.31564 | -52.91624 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 71614aae-635a-3006-aff8-8d5f4fb3cd9c | -18.54272 | -46.05781 | 2025-08-13 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 5e1155c6-8c79-3ef9-8951-03ca9dea5023 | -16.38967 | -50.90253 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98c86ee4-d97f-3fc1-9587-ca10a37c4d00 | -15.70836 | -56.40109 | 2025-08-13 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0879499e-b679-33d0-a19b-cad17104acd3 | -16.51228 | -47.85163 | 2025-08-13 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6599eca4-f65d-3749-b18c-5b385effa6c7 | -18.53892 | -46.05285 | 2025-08-13 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 96e37894-de90-317c-bb28-cd51d548eb54 | -18.05399 | -47.94527 | 2025-08-13 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67acfa04-1f0a-36b8-ae68-2e2052cdb990 | -19.08257 | -48.15237 | 2025-08-13 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59b37810-85d5-35b5-998a-16532c5e80cf | -13.53154 | -47.62666 | 2025-08-13 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ce5b8dc-274c-3bb2-9a33-0ecb7cb06f19 | -16.31444 | -52.92363 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60d963d4-9989-3725-bab3-612df532512f | -13.54201 | -47.6325 | 2025-08-13 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac5144de-5a11-3be0-9be6-d0d9fa450f21 | -18.65696 | -46.8336 | 2025-08-13 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c0ea276-153d-331d-972a-16923bc6a1d4 | -19.45282 | -45.30791 | 2025-08-13 04:42:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1d72eff-cede-38cd-a614-4fb7ed382db1 | -16.59981 | -47.03488 | 2025-08-13 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a027f64e-6330-3a5d-9629-08ee2197f9ed | -17.65672 | -46.68473 | 2025-08-13 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b4fe1ff-24fa-3b8b-b4e8-68a5ca39ece1 | -15.08961 | -51.35902 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 974709c3-df0c-3816-a00a-8f5668139c7f | -15.85881 | -49.41635 | 2025-08-13 04:42:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54476647-a290-322e-9773-9bbabea8d5f7 | -16.39857 | -50.88905 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 462f64de-80e0-3a26-a95c-73b03d6ebb83 | -14.49138 | -53.27862 | 2025-08-13 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2e46a1a-0f02-3ced-83da-448e25a5cfe1 | -16.59584 | -47.03432 | 2025-08-13 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a133fb64-1fe8-340f-8666-30ef385f19f9 | -16.2964 | -52.91267 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ece3b0a-6724-345a-b9db-34ebf676b6cd | -18.05784 | -51.29921 | 2025-08-13 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c572340e-1866-3a43-9d7a-2b357dac3b53 | -16.36761 | -46.88309 | 2025-08-13 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f24dc98b-60de-38b9-b74a-638241a68f2b | -16.30956 | -52.91145 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23516cb7-ec3c-3813-a122-4ae2d5bc21f3 | -18.88067 | -48.31297 | 2025-08-13 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75d3308f-75dd-39ec-87a7-7c0b70be52e8 | -18.9263 | -46.78842 | 2025-08-13 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9730fd55-c423-34d3-b38b-af6251abdfa5 | -16.40135 | -50.89328 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd703577-b082-39d9-ab39-50b8c7093387 | -18.91954 | -48.2248 | 2025-08-13 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fa2a578-9a01-30ba-b338-490dce5b76cb | -18.53458 | -46.05225 | 2025-08-13 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25a06c35-3d6c-3e1c-935e-83ee90338005 | -15.55398 | -43.15566 | 2025-08-13 04:42:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30728c16-8f9b-3126-b037-eda4f49922a3 | -15.09679 | -51.35655 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ca780d8-4ff5-3236-974f-37b67f2a1c1d | -14.12272 | -44.31811 | 2025-08-13 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68e7d3fd-f2ad-3374-bdef-800556396142 | -15.15274 | -53.5116 | 2025-08-13 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eb6cc9e-2797-3486-8d5c-0573c253e539 | -18.54326 | -46.05342 | 2025-08-13 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a52e6628-7baa-3505-8053-a0a664c05525 | -13.65053 | -49.00241 | 2025-08-13 04:42:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bf07f4a-0549-3dd5-ae2a-6d7a926f7fc7 | -15.09072 | -51.35189 | 2025-08-13 04:42:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0bda1cc-d6ca-3270-925a-e2b11db26514 | -16.31504 | -52.91993 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README22.md)
