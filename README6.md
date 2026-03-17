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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76307b2f-e31a-38c0-a6b8-6db4b9d18053 | 0.90865 | -60.30245 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62c833eb-c0f9-3733-bd5e-2f764dd9169b | 3.72635 | -61.28875 | 2026-03-17 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8b6b29e-996d-3362-ab02-a5d789825a89 | 3.13477 | -60.73389 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f9bc50f-9bdd-3170-8b78-801fdff0310b | 3.15208 | -60.73214 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 703ea8ff-e8de-3b13-8563-5951ee13ff7b | 3.12825 | -60.74667 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f5d0602b-50fb-3f71-b727-81592c0ac766 | 2.79085 | -60.7171 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6272d816-316b-39cd-bb0c-526c33464649 | 3.19511 | -60.12708 | 2026-03-17 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb5cda13-1f55-3e5e-95ba-45af2b29785b | 0.83916 | -60.33949 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7d84e4c-3ff4-3622-8134-ed40d162df3b | 2.85452 | -60.73449 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42156c11-18d5-3215-9358-a8336e4118c2 | 3.14664 | -60.72523 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8345281e-0f99-3dca-be1d-2b6ba6ed1208 | 3.08604 | -60.77686 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afd28b62-533d-3d8e-a518-65a1975887d8 | 3.1407 | -60.71732 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74ba8f4e-37b2-3875-b685-02f60e501bf3 | 0.88199 | -59.46208 | 2026-03-17 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8da21b4-1a2f-3b21-b81f-ec7b7a90de3b | 3.12051 | -60.75182 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 04effcec-0e4d-37cb-9fce-2a86f4f11457 | 3.13701 | -60.71899 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89e4b8d1-3f5d-3b61-ab27-8ee09d52f369 | 3.08187 | -60.77754 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51af84e8-8ada-38f3-961c-43afc1b7585d | 3.14252 | -60.72871 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc36dbc2-15ca-31a3-a321-67f56eac292e | 3.13121 | -60.73838 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bbaf2c20-f8d3-3039-8890-6e8c18116b01 | 0.83541 | -60.34456 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9aaf6f3e-a7f3-38be-9b87-72262332b067 | 3.08897 | -60.7686 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d557cfe-2ab3-32d7-9360-0d7d50bc4544 | 3.1253 | -60.75494 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9aabf1f-b02b-3fa1-b5c2-5b2c70b0b78d | 3.78649 | -61.31849 | 2026-03-17 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaf342a8-5aac-36f6-996e-0d9572263479 | 1.32879 | -60.6992 | 2026-03-17 05:57:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd7df71e-b62f-3964-bd3e-0b1ac4e174b0 | 3.12886 | -60.75046 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c5be0bf-20a8-3484-8306-f8a84e4a2549 | 3.08542 | -60.77308 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9515cfa3-aa22-3c6f-baf9-2ac9497d18a8 | 3.19213 | -60.13609 | 2026-03-17 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47897f12-8b6a-3879-b265-8da65d26a047 | 3.78564 | -61.31339 | 2026-03-17 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e43f41c1-d115-3c30-9bbb-cf2c9370b78e | 3.13537 | -60.73484 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8a889fa-244c-3ad6-8fc8-752ac859419d | 3.19076 | -60.1278 | 2026-03-17 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a324b19-bcb4-3896-af3c-05bd7254af70 | 3.78467 | -61.32054 | 2026-03-17 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a052a821-7837-35e2-b215-50c21a1e874c | 3.12703 | -60.73906 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 08bed37b-d235-3a72-ac28-d06cff20d54a | 0.83774 | -60.33076 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c0696cb-42f8-36c5-a110-5d5ca30706fa | 3.14192 | -60.72492 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70149bfa-d0a2-3746-a756-2465fffd34fd | 3.12407 | -60.74733 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 59afd7af-afb1-3281-9b9f-833a81e29d35 | 3.12346 | -60.74354 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c6b5c4fb-239b-308d-929b-5103a2606db8 | 1.00736 | -60.23244 | 2026-03-17 05:57:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e15c4cae-33a9-3c20-8fe3-94c7c3fae05f | 3.12469 | -60.75114 | 2026-03-17 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1dcc708b-0823-3e51-84b6-58de79347096 | 0.90627 | -60.30179 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffef1d69-7bda-33d9-850e-910868b1e759 | 0.8347 | -60.3402 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f9d05df-fbf5-3c24-89b3-0658a1c01901 | 0.83329 | -60.33148 | 2026-03-17 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bd736ca-15e4-3a8a-9943-e989d399dbc5 | -16.44873 | -58.17531 | 2026-03-17 06:03:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5f3d440d-287c-3998-9e5d-b0dcebe89c5a | -16.44816 | -58.1811 | 2026-03-17 06:03:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bdc588be-85be-399e-bee2-9c3f555023d3 | 3.19302 | -60.13623 | 2026-03-17 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fe56033-ae8c-398c-a83f-e0d3e966c816 | 1.33311 | -60.70615 | 2026-03-17 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 376bc349-d63a-3d07-b7bc-e0dd8bf775ee | 3.12545 | -60.74172 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5b5dd40a-3ac9-3b4e-aa63-f46a77448990 | 3.12082 | -60.75344 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a8d840c4-0ddf-3640-a3e5-0ac49658d854 | 3.13098 | -60.7353 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5d1cce85-a5f1-3807-b068-1e754f424fa0 | 3.13166 | -60.73379 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1731188c-26d0-3cd4-a6f9-f045fe0f5419 | 3.78867 | -61.32172 | 2026-03-17 06:20:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0c006a8-3c30-3908-9bcb-c2b4d16c3384 | 1.33217 | -60.70051 | 2026-03-17 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77974685-e440-3661-bf29-9cd9a94eb7b7 | 3.08412 | -60.77053 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2849167-08af-3154-83b7-221746701fd5 | 3.13625 | -60.72212 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1411077-65a6-3770-a2dd-84b2a9d27482 | 2.74136 | -60.43935 | 2026-03-17 06:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9852b9-94d9-350e-95cf-cef6a25ec2c0 | 3.14176 | -60.71579 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df325704-ace7-3bc7-9642-b3b01269d34d | 3.14268 | -60.72107 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2acdb638-b645-3229-84e4-baf4e46b3b1e | 3.12634 | -60.74704 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c5d2c8d0-db89-3264-b1f4-7a6cc67674a0 | 0.83939 | -60.33698 | 2026-03-17 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d990707a-5ae7-339f-972a-9709b1515ff6 | 3.13259 | -60.73913 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8dc432b9-2f49-3e17-af55-b5776edb2c68 | 3.19199 | -60.13044 | 2026-03-17 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6cd79935-653b-3f6f-8c74-e43fbfa8642f | 3.17978 | -60.1213 | 2026-03-17 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 994f6954-2a46-3af5-8a13-8047edd3aa81 | 3.12456 | -60.7364 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ec1d2e1d-bbf6-3abd-9e38-45206bdc2cc7 | 3.1445 | -60.73163 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41238bcc-9663-37d8-bbf7-63979982c04c | 3.12253 | -60.75718 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 52ec3c15-ca9d-371e-b059-3079d51baf91 | 3.12617 | -60.7402 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c2ea4441-69a2-3396-b2e4-7cebb90affc4 | 2.7396 | -60.43699 | 2026-03-17 06:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7754b212-0789-320c-bada-145c35cba610 | 3.1216 | -60.75187 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7a1fe7c7-2345-3b6c-b216-996f3e2f09d6 | 3.08503 | -60.77586 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dac0170d-abcc-3ca2-939f-053052bb8d34 | 3.12723 | -60.75234 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6e778120-23c7-3263-9357-385ede1b4c59 | 0.83838 | -60.33085 | 2026-03-17 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10a474ac-a983-37ce-b682-b34e14b07fb0 | 2.74618 | -60.43593 | 2026-03-17 06:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e81e7c-f9d6-3a73-a9ca-dbe4a0fd7c01 | 0.9113 | -60.29929 | 2026-03-17 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b16e947-5452-3698-87a9-270bdd993d9a | 3.14359 | -60.72635 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc23575e-3506-3b16-9632-be9bcf9d98a5 | 2.74041 | -60.4337 | 2026-03-17 06:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afc52bfd-c388-396e-8791-21dbb608166f | 3.13533 | -60.71684 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e8a2d10-9ec7-31f0-94db-fd3e689c6a0e | 0.83259 | -60.3381 | 2026-03-17 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 90faa101-fcc5-306a-aabb-0e4222732090 | 3.78786 | -61.31702 | 2026-03-17 06:20:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeb31523-22d1-399f-a448-58ededee4219 | 2.74793 | -60.43826 | 2026-03-17 06:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bf8ed42-09a4-3a90-b3e2-7491eea14749 | 3.1951 | -60.13082 | 2026-03-17 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41e036a2-bd1c-3254-95b1-efcf6cf32f33 | 3.1961 | -60.13667 | 2026-03-17 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e36a7d8-bb4c-3d83-a2d0-0b55a6aec0be | 3.09053 | -60.76942 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 249d4b07-5a1e-335b-8adf-69ae99912347 | 3.12068 | -60.74655 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bc31e7c7-43b9-300d-9aa2-8555e398346f | 3.13008 | -60.72993 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 84756e06-734f-30a5-a941-9ac4211b4bfe | 3.12802 | -60.7508 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7dcd82ac-0529-320c-9d5c-2b719d805507 | 0.8404 | -60.34312 | 2026-03-17 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0bb04ac2-0082-3656-b4ba-0e3effb76fd4 | 3.78704 | -61.31233 | 2026-03-17 06:20:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c569e6eb-c718-38eb-8b77-0f4dc6bdaef4 | 3.11992 | -60.7481 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e85dbe87-3f2b-3ee6-b379-ba713c7b6ead | 3.12346 | -60.76248 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c050ab63-10ee-3650-aca7-508b254eadbe | 3.15093 | -60.73056 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0af3fa5e-a245-3f16-8fdb-15f43b97446c | 3.1226 | -60.76408 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c76e7130-9349-36e4-99a4-398780522201 | 3.12171 | -60.75877 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 209abab8-b1fb-32a5-9461-b21a42183a87 | 3.1271 | -60.7455 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 08341eb4-a8bd-32c3-8a1b-48b6df6e7aa8 | 3.11704 | -60.76353 | 2026-03-17 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e06512d2-a097-302d-a729-08bd1a85657d | 3.1941 | -60.12496 | 2026-03-17 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 530a3a12-3b04-3a96-b7ee-d326a51113dd | 0.90447 | -60.3003 | 2026-03-17 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9fa373a-6e18-3bfc-a6be-92666b9a4562 | 3.18644 | -60.12023 | 2026-03-17 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33949b18-c10e-3d39-b82e-1d0a1e9d216c | 3.1147 | -60.75283 | 2026-03-17 07:16:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6aa43fad-42e1-389c-9859-3a18eea8e93f | 3.12221 | -60.74264 | 2026-03-17 07:16:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b9105def-1f43-3dcd-815d-86b2ee270c5d | 3.13105 | -60.74134 | 2026-03-17 07:16:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bdd6b08b-f23c-3e98-ae03-90dba79cba4a | 3.11604 | -60.76173 | 2026-03-17 07:16:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c6c7bec7-39d3-3bbf-ba65-07b22f2b27d0 | 2.74068 | -60.42691 | 2026-03-17 07:16:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README7.md)
