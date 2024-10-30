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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2802812b-9230-3136-a144-e340ef6ee619 | -1.4265 | -49.22262 | 2024-10-30 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 890d61cc-b5c4-3501-b67c-01be7c0ffbb4 | -3.60615 | -49.86123 | 2024-10-30 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ccd11a0-99ea-3923-92ea-5a0c84401130 | -3.5697 | -50.03331 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26586de8-b635-33ec-89b7-16e01de05440 | -3.56904 | -50.03738 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65f5327a-1d8e-39d4-b6c5-249a68541816 | -3.56474 | -50.03667 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 152680d3-e7f6-365a-9e35-20c06bbb6ba4 | -3.55801 | -50.30407 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e68d0fd-a37c-33fa-ac16-d6d4dc571cad | -3.55363 | -50.30336 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 040518e1-6ac4-303d-9fcf-c00cc819f222 | -3.51203 | -50.47553 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6e5efcc-4493-35b6-b948-bf1da5af75e1 | -3.51118 | -50.28466 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc803e60-f37a-357f-bce4-c12c7d7d2b08 | -3.51065 | -50.47832 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d004d6c3-da8b-3d37-ab10-f3c432694ca4 | -3.39266 | -49.75885 | 2024-10-30 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39627ca1-7532-38a3-9b0d-f714404b78dd | -3.36471 | -50.16179 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a21e80ad-adaa-3078-b87f-b00fd767ce5a | -3.3559 | -50.26879 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44d1f45b-bf7a-34b7-8788-b59bb35565dc | -3.29357 | -50.23437 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e102b230-bc7f-316f-a1f4-8bfaaffc5ed9 | -3.29289 | -50.23854 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dae7676b-45f0-318b-aa9e-795058724741 | -3.28478 | -50.23313 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec2fc672-1ff7-304f-b59e-dfffa805109c | -3.2659 | -50.34859 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 765b0d82-6713-3310-905e-97f63d4bd7a1 | -3.26518 | -50.35295 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4881a9a3-c833-3540-bbae-8a17a3908ced | -3.26076 | -50.35224 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f8e0f1b-7878-351e-8cb4-99d829bf30cb | -3.26005 | -50.35656 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a8828bd-099f-3d79-8520-d9a38e9d5e10 | -3.25563 | -50.35584 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f764fbd4-7274-3f24-9dd5-90d0488505c9 | -3.25264 | -50.34649 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6294573-0680-391a-8879-33e8bbaa810b | -3.25192 | -50.35081 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e852c314-bc94-3700-b053-0cd7e670d993 | -3.23586 | -50.58838 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6b16bd9-72da-3310-8c23-cfe08ad6d5d9 | -3.23137 | -50.58765 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 84fe5a61-1e43-31a9-b45c-3946072d5f74 | -3.22761 | -50.58243 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55f181dc-e8f9-352c-9046-86cc06d047f5 | -3.22687 | -50.58694 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a549829-60fa-3889-9514-bd3f846fe549 | -3.22467 | -50.18536 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b87ce1b-f747-39a7-b5b7-c9954a94ba4a | -3.22031 | -50.18459 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62ca7400-6ca5-37e1-8005-346bf08e71f7 | -3.18338 | -50.38597 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1892d3e6-f3ea-3ae7-a551-fa4da41c9972 | -3.18268 | -50.39032 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 090da8f3-786a-396e-84d7-97e6416fc1a8 | -3.17894 | -50.38527 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1567a972-ca72-3464-a75f-460b7cd08549 | -3.17824 | -50.38963 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c57d173d-ee73-34bf-a27e-a041e6a3f278 | -3.17753 | -50.394 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8792eaa5-b294-30e1-903d-2a63ad893034 | -3.17667 | -50.58355 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f92188b9-20fa-3eb5-93a9-129a22335021 | -3.17217 | -50.58283 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cd7e6252-49b2-39ef-977e-c8acd59d2001 | -3.17141 | -50.58735 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 62faeba1-509f-3071-8958-3b922c97dd4f | -3.16915 | -50.5888 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba1bc43b-efc2-30d6-ae4e-007be4922b43 | -3.16691 | -50.58664 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc64d387-4ffe-3aca-9dce-90a17e863db7 | -2.65848 | -49.83908 | 2024-10-30 04:19:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a86fc7d-1039-39cc-9495-abc7995e464a | -2.65841 | -49.25755 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54e96440-4ed2-35df-a33a-a560ff1aa46a | -2.62367 | -50.07719 | 2024-10-30 04:19:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aefe722b-a624-3d7a-a761-15f91e313831 | -2.5968 | -49.33636 | 2024-10-30 04:19:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 883c732c-9185-35ca-9e56-a49380759e8f | -2.56106 | -49.45266 | 2024-10-30 04:19:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b58b8403-7787-30c3-adea-0f7ec558b763 | -2.52375 | -49.08745 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3a6a6718-f14a-32ae-b43c-ffa5e6e9a3b3 | -2.52317 | -49.09111 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9744f035-6148-3f29-8ce4-7df20e8ae847 | -2.52258 | -49.09477 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3f7c210-215b-36ba-8965-6e91ffce3c9e | -2.51437 | -49.09344 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 904cd9d5-840d-35b0-a0b9-8340ba9fb0e2 | -2.49404 | -49.30104 | 2024-10-30 04:19:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dcda62c-2609-3f89-9a4c-3952e86fd8a5 | -2.47107 | -49.39151 | 2024-10-30 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f0d508c-dc9f-3695-88a9-1cf245688e8c | -2.45536 | -48.91314 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7ef0dfa-fe4f-3b15-90bf-d0d172646754 | -2.38857 | -48.93956 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a3f17b2-9cdd-3454-bd6a-a8c7105be6a5 | -2.38765 | -49.18055 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22d50b6b-bcf1-34b8-9e74-e5ff7eb29aac | -2.36173 | -50.32283 | 2024-10-30 04:19:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e6f9dfec-66c5-3710-98de-32a6c2d3c54f | -2.361 | -50.32724 | 2024-10-30 04:19:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4bedd849-fde2-3a1e-8706-9c9048a6872b | -2.31158 | -49.11052 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d65ccf5f-ac4e-309f-b97e-c15c14f36865 | -2.31099 | -49.11424 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3ea1484-e4d2-3e71-9bcb-81c4c4925497 | -2.45712 | -49.16038 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad150c9c-c750-34aa-a4b8-906ac8b1b629 | -2.45299 | -49.15975 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f558b3a1-6c6f-34ac-a2d2-971ce365a450 | -2.38824 | -49.17683 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7349278-85ce-3cb9-861a-e628918e4c71 | -2.38799 | -48.94315 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bafb40a-ca2d-3a18-af81-0414f51ca3ba | -2.37442 | -49.02675 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 782485e3-4fd6-34f4-bd86-244de4882445 | -2.36428 | -49.08918 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e385b44-389a-3f3b-9b31-ed66a4e15a23 | -2.36016 | -49.08855 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d81ebc2-6a16-3d9e-bfbd-df0d7574f10f | -3.52311 | -49.23231 | 2024-10-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 972eab3f-a6d6-3452-a812-c13e43d33052 | -2.83466 | -49.2317 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ea74afb-a202-3605-af27-7b63ac5efeaa | -2.81109 | -49.2204 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 211332c0-ed65-3a77-b593-6a5b366abf55 | -2.80757 | -49.21604 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6cc2db09-36aa-3d69-8810-15bc49357cb8 | -2.79753 | -49.22581 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20d511d9-a650-39cd-9711-89c27a523830 | -2.63188 | -49.08929 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ef7fe45-4c15-393b-b5e6-90b5b69e9c97 | -2.52727 | -49.09177 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9190c58f-bc07-3855-8f21-ca6a5c926351 | -2.52669 | -49.09544 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2768027f-ecbf-385b-a900-57176ebbd997 | -2.51906 | -49.09044 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5d0a9a3e-1bd7-3fd3-8f6c-70b27f6689fa | -2.51848 | -49.0941 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2038f73-c10e-3df3-8081-bef0236cfb74 | -2.51139 | -49.19178 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d1135f0-0821-380b-b28c-334e8f629118 | -3.06967 | -50.50459 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae3d58ea-28d0-37d7-99ef-c43e95b08aed | -3.05197 | -50.41535 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85ec3adf-e217-325b-872e-60b9d44f89cb | -3.04825 | -50.41014 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7da1d6d-8140-3d83-af95-8e00b27f9cc5 | -3.04752 | -50.41459 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7453348d-8a55-3de7-a19d-829617dcba2b | -3.04679 | -50.41907 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f0d5fd9-cefb-3d3d-b3d1-c59f266cfe86 | -3.03715 | -50.42212 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc30cea0-8ef6-3673-b7c9-22f1503e9e6e | -3.02319 | -50.45145 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d08fbc29-89e6-33c7-a304-ac61383e24a8 | -3.00377 | -49.58603 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0a313f11-b239-351c-bbfe-4e5dbcc223c5 | -3.00316 | -49.58989 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f14df56-4a37-3c51-808b-e494c4f8a4fd | -2.97769 | -50.47664 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d762ed97-0adc-33e2-bb02-edeef62fe210 | -2.97488 | -50.47776 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4638ebb4-4fa9-328a-914d-3baf5b3c1a2e | -2.9673 | -49.54432 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 999321a9-cef8-3359-b49d-c9b61f3b7df6 | -2.89257 | -49.46883 | 2024-10-30 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ff4ec41-c18b-38e5-9655-fd2919475be7 | -2.85907 | -49.46352 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49704737-1f17-3b68-ab7a-ac6558dc4127 | -2.85739 | -49.44745 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 827ee7b9-c579-32ab-84b5-335f2bfef8de | -2.8376 | -49.23979 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6fa144cd-f014-3fb5-aa4a-4118dc47395a | -2.83701 | -49.24351 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4f572fef-0845-3986-b3c1-696a6359d36a | -2.83289 | -49.24286 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a3561f21-7973-3d77-8ce1-091d00d7a0a6 | -2.83053 | -49.23105 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d32a17d9-9346-32e6-b8e1-c3fd02ca4115 | -2.82994 | -49.23478 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| be4ec478-f0b9-33f8-8e0f-6d41920a0914 | -2.82935 | -49.23849 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e7b7d2fd-f5ba-37a7-a01e-9d095c804ebc | -2.82522 | -49.23783 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2080c9d9-393f-3bb0-afe6-b52a27dfdb83 | -2.80697 | -49.21973 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6cbbd81-db9f-3fe7-9f1d-5ba613d21cf6 | -2.79401 | -49.22145 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b8f1558-b751-3593-9a2f-99a65ba4fbc2 | -2.79068 | -49.4811 | 2024-10-30 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README43.md)
