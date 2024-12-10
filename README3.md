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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0783dac7-8b71-3cc6-886e-0423f76276f8 | -3.0969 | -54.077801 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c72ec5-fdb6-30a6-b668-933e06eef294 | -3.1015 | -53.735401 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92add89c-d492-3c73-9f8d-b8da384147f3 | -3.1032 | -53.245201 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 329c1140-5e43-3b6e-b9a2-237474c5a002 | -11.3694 | -43.892899 | 2024-12-10 00:51:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e96f8ccb-1c4f-3a44-8ca8-0d20f47d657f | -13.3797 | -52.5611 | 2024-12-10 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50aa1f3d-121f-32f9-9bf3-913838c94ce2 | -4.836 | -47.312698 | 2024-12-10 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96108682-a57f-3fab-b1c6-18fa53659f8c | -3.1293 | -54.0392 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67588bf9-4270-3324-9fc8-b1faf48cb2a7 | -13.3285 | -52.417599 | 2024-12-10 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56120b4f-8f49-3200-bace-dbba914569ef | -2.82 | -53.042801 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7d5636c-a6c1-343d-a88f-b2a54a692826 | -2.8184 | -53.035801 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 247536ed-897b-30be-8bb2-167dfad42cd3 | -3.0884 | -54.040401 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65a89ea7-1cfd-31fd-9bf1-7360c7c6f9bf | -14.2798 | -57.450298 | 2024-12-10 00:51:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5cbdab6-8dc2-37c4-97a8-4e705dd461fe | -4.1261 | -50.4174 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9371698-e390-31ec-896d-eb3592a3f3ba | -5.381 | -43.072701 | 2024-12-10 00:51:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b9b8c4b-4883-305e-ba16-e8c76f78dbce | -12.8545 | -51.933498 | 2024-12-10 00:51:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c97460b4-9c37-3053-951e-675a896858b7 | -13.9433 | -44.337399 | 2024-12-10 00:51:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68092156-cd74-3252-b9be-e1ae57939631 | -3.0009 | -52.8419 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a53f4236-25cd-33be-a765-8e6ecf9b58ba | -3.0952 | -54.070301 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae143c3-9008-3c6c-ab68-bce9efe5e8cd | -2.3574 | -53.862 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1beb229f-6b90-36ed-b27a-dd9dbea78ea9 | -13.3268 | -52.4095 | 2024-12-10 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f03fdcc-0fde-30f9-bf46-cba1508d6cca | -3.3402 | -53.244701 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1c07495-f31a-3eff-8e72-78b0b84d20ec | -3.1277 | -54.0317 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9dfa76-a077-3ae7-ad51-93b40a5af1b7 | -2.8253 | -52.9757 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed523522-54c1-31a5-8108-d89775ee27db | -3.0935 | -54.062801 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6681bf-fa4a-3147-adfa-09ec4bf5e151 | -10.5098 | -44.932301 | 2024-12-10 00:51:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 43948801-9e0f-3888-8214-c298ab2ae687 | 2.4367 | -60.632999 | 2024-12-10 00:51:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5c058ea4-52d3-3cb8-8a31-5fc7335bee3e | -2.4823 | -47.6045 | 2024-12-10 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63773215-6a67-3f1d-8c95-1fa6e49e6d2f | -3.5227 | -50.977901 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31528e7b-da69-37cb-b9e3-0c1f80bfa6ef | -4.2829 | -46.673599 | 2024-12-10 00:51:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dddc7b92-2c22-3eb8-95e9-ee85d132e79f | -11.5309 | -56.426701 | 2024-12-10 00:51:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9705388f-f216-35a1-8656-767d12e75eeb | -2.2214 | -53.717701 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f53c6f-133d-3141-a27e-c4dfca2b3478 | -5.7711 | -47.865299 | 2024-12-10 00:51:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d2302602-9cb1-3064-b8a8-1306123b83df | -4.038 | -50.7966 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bdc8553-e5ce-327a-bda2-c6754b76f5e1 | -14.8366 | -43.147099 | 2024-12-10 00:51:00 | METOP-C | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 472276fa-b11a-31ba-b96b-2c6a5ccde592 | -4.1908 | -48.562901 | 2024-12-10 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a2e73c-598a-32c4-ae3b-755ec11c708b | -3.5088 | -54.6684 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c679f56-4ffb-3fc9-9f01-716ca233330c | -3.0625 | -54.243801 | 2024-12-10 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 893b6a2c-3c9b-3168-8571-5cff30b3660a | -2.9942 | -52.858002 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f4f5dcd-41bc-3f64-8d63-c67c7e005654 | -4.0396 | -50.803501 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4bde25-6aeb-3fb8-97f4-962e5c682f6b | -11.0621 | -45.372398 | 2024-12-10 00:51:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca47b798-93d8-305f-b387-f4f078c6bd8d | -3.8745 | -50.355499 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af5cd101-6853-3cd6-b73a-320246c9faed | -3.0527 | -54.245998 | 2024-12-10 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0577824-23c0-3662-94ec-ed1ca19834e2 | -3.3162 | -51.471298 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4fa60a-cd38-3fcb-98a4-c71e988736d9 | -2.7886 | -52.860001 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a53aaa6e-32c2-3be7-b538-09b50c50edf6 | -3.688 | -54.3232 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 846611b1-e1c5-3114-b7cd-b9fd03c2613c | -5.928 | -48.050098 | 2024-12-10 00:51:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 556e5016-804c-337a-ac9f-47f5490a0f71 | -10.445 | -44.8787 | 2024-12-10 00:51:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee6f7ee0-9d3f-3380-94d1-58f92091747a | -3.2771 | -51.076599 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c008f937-ef1a-35c2-b9bc-88c6ba109657 | -2.2198 | -53.710602 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab4aebdb-2e9a-38e1-8d6a-80baa662a900 | -12.3688 | -54.1707 | 2024-12-10 00:51:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95a4c71a-95c4-369b-9220-f3f7a090fbf2 | -2.8171 | -52.984901 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3981eee2-aeb3-39af-8551-3dd04bebd8d2 | -17.470699 | -47.8596 | 2024-12-10 00:51:00 | METOP-C | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77e53b25-46a7-38ff-9417-8bd6cf5d062a | -2.4747 | -47.616299 | 2024-12-10 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970ccb6d-ce32-30cc-81df-5f98ea3a25d6 | -6.9087 | -47.830799 | 2024-12-10 00:51:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9eda521f-1693-35c1-8233-07d060d80934 | -3.8375 | -52.351398 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5d1963-2328-379e-a692-2182fc8b820c | -13.1101 | -43.324699 | 2024-12-10 00:51:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 51093e6c-dbbd-369a-b642-b37c51deade7 | -4.2853 | -46.683998 | 2024-12-10 00:51:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bb7f925-865d-3dee-b373-cd5924159344 | -15.2581 | -53.566898 | 2024-12-10 00:51:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2cf1d1-64e7-3178-b618-0afb3e20e285 | -17.464001 | -47.018501 | 2024-12-10 00:51:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9538d7f6-c80b-301f-ad75-a396e172918e | -1.6921 | -52.980801 | 2024-12-10 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e59df09f-d91d-3e75-a94c-ca9158a5e0c2 | -3.0756 | -54.074699 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26ff4c6f-3473-3f6b-b916-ce2bf75d9817 | -13.0285 | -57.207901 | 2024-12-10 00:51:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 595ea130-a26c-3138-9b3f-a53a34257082 | -3.3759 | -51.191799 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4c9fd93-0791-351c-9a26-5c7619f6c590 | -3.8124 | -52.241699 | 2024-12-10 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 421fac7e-78fc-3b5b-93c1-1368ebaced8e | -2.783 | -53.242199 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e6f9c9-81dc-3afe-b8c3-0ebc3be35c1e | -12.3766 | -54.158901 | 2024-12-10 00:51:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfbe1c33-0541-3fd5-a779-a01fc9c202c3 | -3.0411 | -54.240601 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce67848-28f4-3663-ab08-7512b8b61260 | -3.0786 | -54.042599 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4279921-04d3-32c1-87f7-2af725f5f7d0 | -10.3819 | -52.001099 | 2024-12-10 00:51:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aeafc159-aa4f-3a7b-9f1b-e3d453895a53 | -3.5356 | -51.572701 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74fb841d-5dc0-303f-80f3-a8e2885e7c84 | -3.1148 | -54.066002 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85f9f6cc-a023-3c3e-8c29-90635bd92afb | -7.6052 | -46.6329 | 2024-12-10 00:51:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f09fc64a-607d-3d8a-bebc-277ae6739d12 | -2.96 | -53.114399 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5261850d-7882-3d46-8f8e-a7ea0ff5b692 | -3.8395 | -50.651402 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebbe7e20-d4de-3f73-b8cd-45e60ac93008 | -4.5429 | -50.211899 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0149087-db29-39c6-ada8-4629171fd4de | -4.4523 | -50.579201 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 256570ad-e2d9-3778-945c-7598db9960f8 | -3.5281 | -53.935398 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb141897-bd01-3f51-a5d3-2a03a6f7c68e | -6.8433 | -44.377998 | 2024-12-10 00:51:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 223189c9-fcda-351f-987a-18538ec6f5df | -6.9146 | -43.494202 | 2024-12-10 00:51:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 86ccd6f4-6998-33e5-aa5f-0c42aa4aa3b9 | -13.325 | -52.401299 | 2024-12-10 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b37760a-6181-32f4-bd9f-64ef53106b42 | -3.105 | -54.068199 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7caac475-d750-3f0e-ac5b-19af5497b1e9 | -11.5363 | -56.452999 | 2024-12-10 00:51:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36dd3805-9c72-35ae-b3ee-e5175636bc09 | -3.5336 | -54.5961 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a07f8366-1ad0-33d9-b377-46ac98c7df53 | -2.7984 | -52.8578 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99647d21-1d3e-38f4-a700-7cd0d199af02 | -15.2678 | -53.564899 | 2024-12-10 00:51:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce02c544-3015-369d-b4db-2b4d2687f41b | -2.8314 | -53.047501 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f6ba3f-fc08-3074-b904-050f81d76289 | -4.6079 | -48.493099 | 2024-12-10 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8205c6-d094-3351-a59e-a4538c1a9ff8 | -7.9828 | -50.679798 | 2024-12-10 00:51:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e113e750-7211-3966-92b4-5d90b5487bdf | -2.2231 | -53.724899 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3fbb96-0831-3631-b5c0-4d38cc3d1f03 | -12.8592 | -58.2024 | 2024-12-10 00:51:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09715ec9-8831-3696-9b8b-883bc137cd61 | -3.5763 | -53.0144 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71e0c962-37db-3de1-933d-d065d9cf6ee2 | -3.5209 | -52.184601 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 441cc926-9fe3-31ea-a88f-7319f093f536 | -3.8761 | -50.362598 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9655bab8-022c-322d-80e8-d0145260f7d8 | -3.5338 | -54.688099 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41709d23-e069-3ecc-b984-3d93a396278d | -5.9202 | -48.060699 | 2024-12-10 00:51:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1b50f7-c8a6-35f7-a1ed-b0bf07aa978e | -3.8644 | -54.785198 | 2024-12-10 00:51:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9a73d96-429f-3e51-a33c-fefa7c769f2c | -3.7872 | -50.961899 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f594ad1b-3180-3e7d-b8b7-119dcc0cd8f4 | -12.3745 | -54.1492 | 2024-12-10 00:51:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c08e511-b26e-39a0-b37e-ad3eddd61c32 | -3.1165 | -54.073502 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a3ac0f-2a38-3bfc-a7d9-e4264b2d8acb | -2.925 | -52.960899 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
