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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74907810-8cc8-33e4-8757-a158dc491f85 | -11.72636 | -52.94719 | 2024-10-04 04:34:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe4be54a-75b7-37ae-8c64-68b06057f5d8 | -11.72339 | -52.94191 | 2024-10-04 04:34:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b69e366-9fa9-3b40-b246-366972399d0a | -11.72259 | -52.94652 | 2024-10-04 04:34:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 757b0aac-346c-3d68-aaa0-02d28d92714b | -11.07715 | -52.53424 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4bfa67-c0aa-3b12-852a-f064a14f099e | -11.07344 | -52.5336 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca0aea35-e374-379d-a0b9-c383c920ce15 | -11.07048 | -52.52842 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b38be108-3268-3780-abb4-2ea0ac81fb2e | -11.05492 | -52.50725 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b5b75c3-5d7d-31a8-89b8-8012901fa27d | -11.05121 | -52.50661 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ced59c-b9ef-3cb3-b581-71b5df40f43d | -11.03634 | -52.50407 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51c8d663-b660-3b09-b8cc-0ebe7afb3592 | -11.03263 | -52.50343 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7669ded7-94d4-3145-9a56-31f452f1a0c1 | -12.70067 | -54.10495 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c622b1f-4ee6-33b5-a3d2-37553a474eb8 | -12.69669 | -54.10422 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21bdee04-1ce5-31d1-8901-a385c4bf4551 | -12.66627 | -54.08036 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23cbfbcd-4552-30cc-894d-c1b8612b400c | -12.66372 | -54.08189 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f633a7f2-5162-37cc-be41-b72e152373fb | -12.66285 | -54.05273 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f5e5342-eab2-3561-a90e-dd4e52105429 | -12.6623 | -54.07961 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d392785-d888-3bf0-900f-6d44b5bd91f1 | -12.65923 | -54.07364 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4a59ee5-aeb0-3df1-83d3-7b7a20431bda | -12.65888 | -54.05201 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a890e83e-e6f6-3cbf-874f-9b6f8b313c48 | -12.65832 | -54.0789 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 697a6d26-fe3c-3eaf-a348-5831200e5e5c | -12.65798 | -54.05722 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1698f189-fc70-3a63-955d-f84e5d2ae2c9 | -12.65526 | -54.07292 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c50b960-b448-3708-a14a-f9841209e2c4 | -12.65401 | -54.0565 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a2d21b4-92ab-3a82-8629-1dc588275e21 | -12.33648 | -54.09214 | 2024-10-04 04:34:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89fff248-5745-323b-90bf-413d338aeb82 | -12.33588 | -54.0906 | 2024-10-04 04:34:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141e79ce-a00f-3b9e-a570-187ae9fbed28 | -12.31988 | -54.08769 | 2024-10-04 04:34:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1393060e-5817-3c76-a44c-c13e48d6ea32 | -12.31896 | -54.09296 | 2024-10-04 04:34:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8dddfd74-52fb-3169-8128-c42b97e3ae8e | -12.31496 | -54.09224 | 2024-10-04 04:34:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c41a2e5a-f2f9-35ae-956d-637da75292c4 | -12.61469 | -53.49836 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c952987-b761-31ed-8bf1-31218cdfb92a | -12.61302 | -53.14886 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b5caacd-d98c-35f9-9040-5ddb70ec66f9 | -12.61256 | -53.15107 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fdbb3eb3-b08e-3921-abe8-c34aa9d3f963 | -12.61223 | -53.15349 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f9d5cf5-92ba-347a-a550-648c4c5f31a8 | -12.61084 | -53.49767 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30404e28-34c5-3e46-bf55-818ef0188d4c | -12.60846 | -53.15282 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc9a2c3f-c9ee-3d93-90b5-9c04119c4c7e | -12.607 | -53.49697 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27702c48-451c-34b4-987d-55216dc7de2b | -12.59811 | -53.12246 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 373ef003-2095-39fa-8e90-9759666ace0d | -12.59732 | -53.12709 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c2df358d-c6a4-3d8a-9c5d-61df39b1d8b5 | -12.59653 | -53.13171 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a859542f-584b-3830-a6cb-99c387e84447 | -12.59514 | -53.11714 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 07b4907c-b742-3733-94e3-493ef0e9e190 | -12.59434 | -53.12179 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 96e0f790-870c-34b5-b2bc-5888dd5c9582 | -12.59355 | -53.12642 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c8f5e9fe-e804-3184-9a78-f0946db6c5d0 | -12.59277 | -53.13104 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6e48fd16-8bdd-3931-b52b-f61663b54fd2 | -12.59198 | -53.13564 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf2c3f21-d29f-3ff1-940e-266e1a35bf0a | -12.59138 | -53.11647 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1fab2b41-e9e2-3a6c-94d2-ea9530490cdf | -12.5912 | -53.14023 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d43749af-3ce6-3fca-a6a3-05ce73c2555b | -12.59058 | -53.12113 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0c91e6ad-62a0-377e-9aa2-9c70b2e839a2 | -12.58979 | -53.12576 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dcb33cb6-8bf6-334a-8ec5-1614178a4205 | -12.589 | -53.13038 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8c7e09c9-b4bb-3930-9395-e198ea3c894c | -12.58822 | -53.13496 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1478df3-3e1d-3617-943c-a18f4cf877d2 | -12.58682 | -53.12046 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1827a7fd-7232-3329-bb65-ff24fcf94b80 | -12.58603 | -53.12509 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 71b14d6d-7ddf-30a1-b850-e02eb2c56562 | -12.58523 | -53.12971 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 95364e8c-d4d5-3844-a28a-0d33a77c203c | -12.58385 | -53.11513 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 89c9b6dc-c396-34d8-8973-99b8788cf84f | -12.58306 | -53.11978 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5977943a-d9f2-34ab-8b87-88999b6ad7a0 | -12.58226 | -53.12442 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b624e51c-a4d3-3fe7-bf91-efd0d76f4760 | -12.58009 | -53.11445 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9eb56e8-a79e-382b-a513-354760c597c9 | -12.57929 | -53.11911 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1b89f41-a2ed-330a-9050-6e63e5e48a28 | -12.5785 | -53.12374 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 141fdf29-9c8d-3e9b-b24f-a0fb9313fb35 | -12.57771 | -53.12837 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47f9cd89-2b61-3a1b-b100-47473e5cf244 | -12.57633 | -53.11378 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 81dc9bed-5376-3007-a2e3-2c50d878027d | -12.57553 | -53.11843 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a616ee66-e787-3dee-aa0f-cb6db4888114 | -12.57474 | -53.12307 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 231b7555-3ee8-3f05-9793-a8f8343ed036 | -12.57394 | -53.1277 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6e4faed-9e39-3b33-b66d-c00d1125759c | -12.57315 | -53.13229 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1dbffc5d-ec31-3c39-a658-e1e50a98347b | -12.57097 | -53.12241 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78112622-5498-3861-93b9-94675eb3af7c | -12.5686 | -53.13622 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3882691f-ed40-369b-a5d0-1f50ccbd8792 | -12.56483 | -53.13557 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 543c4eba-8f62-3047-b204-a6f1afad73d4 | -12.55649 | -53.13884 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77cc57b5-9950-38b0-bd72-8ab44f6ab548 | -12.5557 | -53.14342 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e9fce18-b1c9-38bd-9781-73cb7ecc646c | -12.55273 | -53.13818 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5821006-c0e9-38a4-a1d5-785368d31f03 | -12.54984 | -53.47433 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e8f4599-7d74-3f71-9fff-a5217aafeef7 | -12.54896 | -53.1375 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e333c2f3-763a-359c-a77a-0eef0008e0bb | -12.54682 | -53.4688 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98738607-59f7-33b0-b307-e534a3bda786 | -12.54599 | -53.47364 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b37faea-b878-3709-80d8-5ee18fb99c41 | -12.54519 | -53.13681 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f2bc125-e58d-3db1-ad83-8ae226164f56 | -12.54143 | -53.13611 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a38ce4b7-a3cc-325f-9692-2855fbfc64ec | -12.5136 | -53.14329 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d0df8f9-9a1c-391c-a412-be96bf67d962 | -12.51345 | -53.14059 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52dd6047-5e49-3473-83e3-5b1106e41b99 | -12.51139 | -53.13341 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0c1ad35-04d8-3ab5-8b25-9ade43405d58 | -12.51061 | -53.13801 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9373b5db-e6b1-3ece-af58-41aa19673a5d | -12.51049 | -53.13534 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 305ee7e9-d2b9-365a-b2cb-39297d1157e1 | -12.50968 | -53.13995 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88da27e8-5221-3ba3-bd9a-a00a3739bdaa | -12.50605 | -53.14199 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 565d6bc2-d344-3782-8274-50c3cc58a229 | -12.5059 | -53.13931 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11137a28-7b3a-32a0-972e-f021c6a61a36 | -12.50306 | -53.13671 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7cad224-9e89-3e58-a814-48c82ca4de1a | -12.50228 | -53.14133 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d61a894e-939e-3588-bc12-74f4aeeac01f | -12.49773 | -53.14525 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c925cd78-e86f-3a21-84cf-68cf200e3e1d | -12.49096 | -53.13932 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 756bb962-5915-3b05-a422-af0c49d5f330 | -12.48841 | -53.17722 | 2024-10-04 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e13f2d72-239f-3c11-9235-48c4d41acd05 | -14.79642 | -53.90125 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69324222-4141-3393-bcfe-62b6587de846 | -14.79261 | -53.90057 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3735a25-e138-3418-8c7a-4cd1acbe043c | -14.79177 | -53.90533 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 025ab664-964a-3409-a401-3356318ce222 | -14.78795 | -53.90464 | 2024-10-04 04:34:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a28e89d-8656-3b7e-92dc-d0616961bab2 | -14.62937 | -54.29983 | 2024-10-04 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9f2f635-7ee2-3324-af50-6b7f6006d890 | -15.77796 | -54.20546 | 2024-10-04 04:34:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fa36861-2423-33d2-aede-110cad846aac | -15.223 | -53.76867 | 2024-10-04 04:34:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9e099cc-e532-3bef-92ef-677a1b02d62b | -15.22225 | -53.77057 | 2024-10-04 04:34:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fe39f27-7f75-33c1-bef7-d33453f43e20 | -15.21924 | -53.76797 | 2024-10-04 04:34:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84e4f0e6-383f-3c75-862c-f9af1e621027 | -15.79161 | -54.20513 | 2024-10-04 04:34:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f2a187f-9a49-3731-a04b-e44dbdde80e1 | -15.79023 | -54.20295 | 2024-10-04 04:34:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5ce8ddb-a025-3ad8-b25d-faf41860c89f | -15.7878 | -54.20436 | 2024-10-04 04:34:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README125.md)
