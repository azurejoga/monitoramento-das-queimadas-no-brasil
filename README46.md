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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc654f9e-34ef-329f-a921-be9b2f131cea | -4.15948 | -46.24947 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c6abacd-3605-3a8e-9746-24bb20c11207 | -5.07217 | -45.51097 | 2024-11-14 05:01:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 131718a5-24ce-3c95-aed7-3c159cdb7c05 | -4.77779 | -45.73415 | 2024-11-14 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9ac2167-7f9d-37f5-b39c-c9ac9fcb166d | -2.64711 | -46.17933 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27664ce9-ecd8-3229-a92e-fb8335ce8f07 | -2.36523 | -48.84491 | 2024-11-14 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d05adcb-bc52-3a3e-bef8-87a15aa6d908 | -1.24568 | -51.78138 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44a1c0ea-d66a-3875-8005-d372db83b97a | -2.66913 | -46.98867 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc81342c-854f-3dc2-9b08-cc956f0f1220 | -4.03005 | -46.54717 | 2024-11-14 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45b17ef8-b3b2-36f7-b5c4-2a40205c7f2f | 0.00306 | -51.12679 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b28827ae-491f-3e39-88bb-368082d67cc2 | -0.19294 | -51.50199 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31e1c707-74aa-35ca-8093-0dd4d1acce66 | -2.63562 | -46.17732 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef9523cc-8928-3c21-b876-bee23f34d0dc | -1.45267 | -52.25755 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8ecf8c0-ba13-3c93-b32e-c15c8b34e21f | -1.22681 | -51.74636 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a008eb74-b7d7-3879-b8fb-2f295393e198 | -2.72269 | -53.19788 | 2024-11-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d65b1db-88d3-3d09-a72e-159e744d03d7 | -3.48024 | -50.26299 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 17bdad3f-34d9-300c-ba96-300510fede66 | -5.56435 | -45.36274 | 2024-11-14 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bef7cd2-72f6-38df-990f-b0b5d6ea40a8 | -1.21553 | -51.74869 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd64d783-f3fc-3788-9862-0fcce4e8b827 | -0.19232 | -51.50598 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 582e7533-b37e-30b7-a9c2-9642df2b215d | -2.11944 | -50.68858 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92b810cc-308a-3231-ad13-2db8e9b35a95 | -3.40758 | -50.31424 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99504fb6-779e-30cb-9912-787f54d16a1c | -2.4055 | -45.34043 | 2024-11-14 05:01:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 254135a3-2610-3e64-a1d5-021fc49a8df1 | -1.22406 | -51.78663 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2259dd64-88ef-33ba-887a-0c4c1223875e | -2.63611 | -46.17419 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a2395ba-4aea-3bf5-9a1f-baedc4419c48 | -3.46927 | -50.30813 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 076be722-8caa-37ae-8669-bf0f7c96137c | -0.20715 | -51.50418 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1032903-f018-3996-904f-b73f13197367 | -1.21971 | -51.74527 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 221ec34b-3a1a-3789-bdaa-c35def2e14ca | -3.71558 | -50.60502 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| e2b15226-9fc3-37c3-9d6a-7146408ccc1f | -0.20236 | -51.51161 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c5d4a74-20cc-3c18-a615-e3b432ecbf4f | -2.32525 | -51.2799 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 4118ccb7-f0a0-377f-bc3d-a1151e05565c | 0.44304 | -50.94027 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fea5485-889b-3342-af4b-8e48c715724b | -1.34046 | -46.5646 | 2024-11-14 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d4fac64-d358-3a70-9512-5db1a2e41a23 | -3.13214 | -51.12362 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25881d8b-e4a1-362f-8aaf-281bf898e4c9 | -1.60429 | -52.4894 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7aa18e92-b17b-3d47-a2ee-eaa9827b19a6 | -1.61136 | -52.23795 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a3bb81-474d-3436-9003-a638b351d4ac | -1.21177 | -51.77254 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e9a9409-4ef6-3f67-aae0-5a90a20a4cee | -3.7473 | -50.44796 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cb1353a-a15d-30c5-a03e-ef2bea7e53d9 | -1.41101 | -52.38711 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4be230f1-fa09-3944-9af6-cd848cb7ed17 | -2.6433 | -46.16921 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fd5a6c4-de9c-35f7-a007-5060025328d2 | -1.57289 | -52.02227 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afa176af-7481-3450-9cc7-769685acd6f8 | -2.08616 | -46.62459 | 2024-11-14 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6ca3472-7323-3a1c-bdf7-377119ce821a | -1.22469 | -51.78266 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40444d46-9ba5-3782-84d3-146bb1d7395b | -2.64422 | -46.16294 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b3aef8f-e7fe-3a15-bf0f-5fef4f3662b6 | -3.49694 | -50.83356 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecf91894-5dd2-35e2-8d10-362e34dd7b0c | -2.63514 | -46.18045 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b0cefe-ceb7-375f-8611-c5f13d909bac | -1.33201 | -51.41296 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3714da7d-7008-35fd-9a14-301699d7822c | -1.39475 | -51.12976 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59cc4ef1-9d90-35db-ac44-7f1b55403cda | -3.52965 | -50.79991 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6f9d78f-475e-3f8b-8645-16cc15c544b5 | -3.16371 | -50.45101 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66dcba68-8e3d-3dee-afbd-c199e67d0f1b | -1.2523 | -51.76202 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28845d39-3c5c-33d9-b93d-5a49c94e16a3 | -1.33675 | -48.32804 | 2024-11-14 05:01:00 | NPP-375D | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f12947cc-1b95-3ac2-a881-6803f360c62f | -3.49933 | -50.84361 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87f05285-f9fc-3b32-8632-2a41c66a86b7 | 0.31212 | -50.76866 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0922cf6-e2d2-3bde-a3d5-f7b2269f42dc | -2.42486 | -46.27209 | 2024-11-14 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d23bb266-f33a-318c-8267-38e68b780824 | -4.15466 | -46.24551 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57126bfb-a5f2-3908-bc9a-bbdff59398a1 | -3.13328 | -48.08648 | 2024-11-14 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e5ca334-b5ef-3b85-90ad-39da5faf9d14 | -3.74015 | -50.44184 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 81e82711-4760-3ced-899e-df289901b76b | -0.95063 | -51.64077 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 740dcf9f-79d5-33be-8f57-b75f674eb13f | -4.9416 | -44.96112 | 2024-11-14 05:01:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1ac437f2-7b8c-3f1e-930f-9c4803980da8 | -3.8105 | -47.79791 | 2024-11-14 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c52b3326-8c77-3aa7-a8d3-0bfe2dc65be6 | -5.85797 | -46.42226 | 2024-11-14 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4fdba18f-ef48-393d-9d92-f619053153e9 | -1.21468 | -51.77706 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8af5977-53c9-3fe3-ba84-3946664f27d2 | -1.0496 | -51.74458 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| affdb294-6823-3a18-8a09-0cfc3a64823a | -1.85509 | -47.82839 | 2024-11-14 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceaeeebb-f85f-38ee-8705-3caf96e5bd5b | -1.38412 | -51.56254 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94d834a4-0bb1-3e77-bc82-08b3e27461d1 | -1.70842 | -47.89957 | 2024-11-14 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 332e5004-2b77-3dd6-909b-af22570944f5 | -2.92535 | -48.07082 | 2024-11-14 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c9e25f5-a755-3dd8-93ed-d05cf4252158 | -6.26898 | -44.54779 | 2024-11-14 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3718801-314d-3368-938b-17ed04502320 | -2.11272 | -50.85557 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f1b3368-ba43-39a8-b373-f084343bc30a | -1.412 | -53.47695 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d540bce-53ee-3386-a17c-0edc59f0d856 | -2.05712 | -52.05686 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a9063b6-daaa-3564-a790-6c8b72ec205b | -5.54651 | -44.32457 | 2024-11-14 05:01:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e58e66e2-ccc8-3ec0-9ccd-8d796b72bf0c | -4.52094 | -46.47995 | 2024-11-14 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c6510f5-ac6c-3b9c-9be3-8162d762aec0 | -1.63524 | -53.27194 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c1c3accd-a0ea-3f2a-9e7e-c03ad9cd4156 | -0.93768 | -51.7244 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a04af0d-893b-3d6c-8502-713ed0b25a3e | -4.42616 | -49.68167 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7fb3349-14db-31fa-b250-c3c36406d215 | -1.13835 | -51.68895 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44d55a6d-4054-3ef8-a4d3-f74346582948 | -4.34823 | -49.68548 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5e85f2f-ba94-3cf1-bc94-bd0b622fb8d2 | -4.79586 | -43.66226 | 2024-11-14 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fefe173-d48c-390d-9c3c-90703c1f0cf1 | -2.96822 | -50.50221 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f1de5ef-5333-3356-a9d5-7431c284fb24 | -1.35575 | -53.07846 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 395537ef-598d-38e8-bcbd-646a5f533d87 | -2.3531 | -51.9865 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d7255ff-7c11-36c4-adae-edbae2cee6a1 | -0.19037 | -51.50309 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d599ddd-09a5-3645-a0a1-733d7cf6846a | -1.40122 | -52.38174 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c17d3c-6cb4-32eb-91d0-50c3a3daa400 | -4.14357 | -43.84885 | 2024-11-14 05:01:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52e62602-d5d3-3a6b-8604-d54717581958 | -1.63125 | -52.52045 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50d68f49-bbed-3df3-9a66-3431d176e1ad | -1.40209 | -51.1309 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e398d438-6638-3341-ac7a-30ca40cbcfe4 | -2.88921 | -50.41865 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76fdb48e-6b68-35bb-a024-fb8213324fc1 | -2.24238 | -51.43029 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bb85146-6a62-32c2-896d-514bebe91f18 | -2.89621 | -51.68757 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33d7e3e5-d528-372e-a37e-af210b273b6f | -1.6103 | -52.40543 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f726912-8f2c-3c94-a1fe-d320ebdfc60b | -2.31478 | -50.69512 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c0f0761-fcdc-3788-9a3c-6673518c4fe4 | -2.11493 | -50.69259 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58959469-e249-34fa-91b2-b3ca5ad4f972 | -2.63672 | -46.17783 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe6998ad-7aee-36d5-a58f-b553bbc7f94d | -1.23036 | -51.74691 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 512b26c3-90be-3077-940c-91046318fd71 | -1.35408 | -53.08923 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79047b93-2d31-3a8e-9277-bb7fee94a1f4 | -3.05159 | -45.52626 | 2024-11-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d9ca254-1203-3c92-9bb2-7a05952edb9c | -1.21406 | -51.78103 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98f7a728-3b03-39dc-8d56-f7d917469da8 | -1.67329 | -52.56085 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6e0bc71-6de5-3f7d-98b4-d687b0c41785 | -1.66984 | -52.56032 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db431464-8a73-347a-9c21-3311d8f6fe8c | -3.31669 | -51.1017 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README47.md)
