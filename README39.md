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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca222e69-36bc-3732-a1e6-b12031cc9784 | -2.4983 | -56.1371 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31b96390-0e38-32ae-b76d-a7c9dc91d365 | -5.7051 | -53.4865 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cde6c6ef-2f6b-3595-8765-940b80305538 | -3.842 | -55.991299 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33ba8c5c-ccd8-3115-a4a1-41309145d02f | -5.097 | -49.701599 | 2026-10-08 00:48:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc53589-f048-3a0d-a74e-e6f89371c923 | -1.4711 | -54.655899 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2b05845-55f6-33cf-88e7-17feae1ad9a9 | -2.789 | -51.679699 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d63ef06a-5758-371d-a6fa-576810bbbceb | -3.145 | -54.092201 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc63280d-2518-35ca-8aec-ff213ca428c9 | -6.2319 | -52.855499 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47baacf1-7530-390b-950a-806aa3ba5fa5 | -6.9924 | -59.123402 | 2026-10-08 00:48:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44a1957d-a008-38ef-aefd-285e7ea581bf | -6.5709 | -53.0354 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d4cff8b-be1e-35b2-b498-6fa861a0da70 | -10.3072 | -46.614498 | 2026-10-08 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbff9660-fe47-357c-8bca-0cbb99f0764a | -6.6295 | -43.7188 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ef2a70a-bd58-30f9-b841-71afe1e90ddb | -3.0516 | -53.907902 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf7aa093-586f-3785-b02e-b6e2490ada4a | -6.6428 | -43.731201 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b44b51f-b06c-3fef-b681-492ad88d555c | -3.1765 | -50.452301 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc683bca-3603-31af-b83c-16ab6667f1a0 | -6.9485 | -45.277699 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 370db10a-485c-34a1-a2fb-30b2d491ea30 | -3.1209 | -53.760399 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0600a5d-83bd-3807-8bc4-c453e7f62ec2 | -6.1111 | -51.733002 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfeff2a2-8c59-3320-bdf8-e33b73417139 | -4.058 | -59.8522 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eec86b72-9ed9-3a50-96b7-14e63f9173e1 | -3.0474 | -51.233799 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8d19b1b-1081-3465-a817-5931a5e90e4f | -3.0954 | -54.190899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee23e3a-bc06-31ce-aee6-8e049f86108f | -3.0273 | -53.936798 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 776aa8c3-e469-376f-9ffe-37627dabba3a | -3.2672 | -51.068802 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b42cee8-97f9-3b37-ac04-382ac629d45b | -11.0045 | -45.435699 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58fdee5d-811f-30b2-ba7f-9bc920700f0d | 1.7428 | -55.603001 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd32cc1e-8482-3f65-96de-90522e39cf15 | -5.0498 | -49.7654 | 2026-10-08 00:48:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24a51bc6-0eb2-3215-bf17-091fc5b47a7c | -5.8935 | -53.500702 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81598acd-41bd-3f72-ad99-33e8d6fad69a | -3.1467 | -54.0998 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f03b5bc-aabd-303e-a996-60f10071ef07 | -2.9276 | -54.132401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d8f1cd5-c041-37c6-9c89-f236a51bf2e9 | -2.9898 | -54.134499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb83ed29-f72c-3505-9308-2149917d427b | -3.1098 | -54.163799 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc5e17e6-bdae-389c-bd08-c1d618a36162 | -6.0394 | -51.7346 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cbd30f7-a6b0-33de-9a00-f8bb905d990a | -2.9893 | -54.087002 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88e704fd-c12a-3edc-98c5-a9eb990acc9f | -5.8721 | -50.1078 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c0de76f-8d2d-35af-9f73-9f779c596bd2 | -6.1229 | -53.056702 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f11131a8-9033-305a-a637-d1fdf1bc2a04 | -3.7352 | -54.651798 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5b1c52-78d5-3297-95be-5dd2766ce4d7 | -6.5121 | -55.400398 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0a0c847-8f97-39cf-a95e-ecc11ebd37fa | -3.002 | -54.052502 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68fb8f54-5b23-3a80-a6c3-b5b870d7a328 | -3.1213 | -54.169201 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5e98a8b-8780-374d-a21b-2a5d8ebc43f8 | -3.5049 | -54.634701 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924a7dff-bdd9-3cc9-9dfd-3aacfaab71af | -11.7727 | -46.778198 | 2026-10-08 00:48:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed07b0a2-0f00-3547-a5ab-0ae42675b5f6 | -3.0146 | -54.153 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e5ce554-34fc-3db3-a0e9-17666dae282e | -4.2842 | -50.781799 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a239af6-a672-32ec-a39c-79cd74a9c7b7 | -3.059 | -54.167099 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7da8368-a558-3c9b-9968-bb65f906416d | -8.3825 | -46.3004 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 907da9db-ef6b-3985-843c-249a53899543 | -4.4639 | -47.9198 | 2026-10-08 00:48:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbfed54f-d7c6-324c-9c07-70aaf90f2b9f | -5.8367 | -47.3978 | 2026-10-08 00:48:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6892a3c9-f3ea-37b0-826d-f4a996edcc4b | -3.3492 | -54.174999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b162f08b-6aab-3236-ab87-bf91d5d8f784 | -6.1681 | -52.664501 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf0df2b7-df43-38e0-8158-7517a1561cac | -2.7748 | -54.095001 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f76ab7d5-fd45-3f26-975c-76b08f8e1120 | -2.768 | -54.064999 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1efd3f7-f528-3609-af74-4806bd4acc2e | -6.8929 | -43.701099 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 58819923-927e-37d5-971c-ba72d07d8231 | -2.9322 | -54.107601 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddacd68-4848-32c8-9916-c24740252034 | -3.5551 | -54.6745 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4071f048-dd5a-3e6e-a35d-0c3a851292d4 | -2.5753 | -56.159698 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc420007-0c5c-3e64-826b-b7abc46cf523 | -3.1944 | -50.5741 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e3553d-3651-3b1e-9e0e-bbe197e2a756 | -4.3516 | -43.782902 | 2026-10-08 00:48:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4eeb96-4662-39b2-94c3-58fc694abf1c | -2.7514 | -54.037201 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7600113-3c9e-3c15-a62d-c162d83d5744 | -2.5068 | -56.174702 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f45bbdd4-cd93-3ad9-ba91-236c5f670b98 | -3.295 | -54.027199 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca274f1-7d36-33ad-a845-7d4d7ea1fdb3 | -2.8938 | -54.029202 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54ecb4c1-f9ca-3929-9e19-89ccba7f4a6e | -2.8544 | -49.551399 | 2026-10-08 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7a38723-23ed-39f2-a3c2-16d1c545c558 | -3.2545 | -54.664799 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b208801-c497-366a-a1f0-8ce91e8cb0de | -3.5264 | -54.6385 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88c0ec4c-33a3-3723-98fd-fade3a0d3a32 | -3.6954 | -54.203499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce41682-e92b-3827-83da-a2b73501f32c | -5.697 | -53.4963 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608bb8cc-4589-3394-8603-87a6cb48544c | -6.1503 | -47.939098 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 650d11be-31f4-39c3-b91d-f6970bb3524c | -2.4933 | -56.069698 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10b974a2-64b0-3102-93e9-213600e25f53 | -3.1798 | -50.4664 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23c86ec5-8475-34f5-bc28-b77328ddd2d0 | -1.8266 | -55.039799 | 2026-10-08 00:48:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d862fbe-4d98-3f7f-8422-599acf836a8e | 1.3285 | -50.9053 | 2026-10-08 00:48:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fce3552e-b282-32b6-8ea3-0864ea547dbc | -3.1065 | -54.285099 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caaa2187-6f77-3dac-9414-e58ed89b69ce | -6.2202 | -55.657501 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6581fabf-30de-3e66-b057-00bd781e5fbc | -3.1356 | -54.367901 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c593df2-b1c7-3583-b49f-14943eb9cbed | -9.595 | -47.791302 | 2026-10-08 00:48:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac89a6f1-9006-3eb4-b9c9-9bcc754e5c4b | -4.1143 | -59.876801 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c655e941-c033-3c18-b413-98b97eff9a11 | -3.2581 | -54.680801 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9c30918-b83c-3046-9288-fe8a1feb1ba8 | -3.3041 | -49.1343 | 2026-10-08 00:48:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caf07d18-6bd5-3d61-a872-02b2918ec8bd | -4.067 | -51.047699 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aae035f0-9492-3dee-85c3-839e879a6a8d | -3.2741 | -54.071499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 967ad15b-0f47-360d-a9dd-528919a61141 | -3.0337 | -54.236801 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e39eab76-1bfa-3d92-baa2-848f4183c382 | -3.0153 | -54.065399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fafff6bd-8b46-33eb-9e0c-92706a37d6ac | -6.7303 | -55.134602 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8128040f-cd68-335b-96d4-00b3e1ed912f | -8.0783 | -55.298901 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6491e68-4a8b-39cc-b078-c607d216a0c5 | -2.844 | -59.120899 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da4384bf-7196-35b9-80c2-5d6547376422 | -7.2168 | -55.1082 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19049ef3-0b32-31d7-896b-de0215352a50 | -5.7004 | -53.511398 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b7b715-16b5-3bf3-a038-30e093f54654 | -6.2368 | -52.877399 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff82c9e-6268-3a1b-a7e0-1b9ece1386fa | -3.1558 | -54.728802 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d3b4de4-a1c5-3801-a87f-6d2facf3cced | -3.1231 | -54.1768 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59c85c85-bccc-3302-ba3e-84ac37056cc5 | -3.098 | -53.750099 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04dd8afd-daf9-379e-921e-be61909c6d05 | -2.9535 | -54.110802 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aacd7e7-a64e-3fb3-8616-979688f3e020 | -2.3599 | -48.887501 | 2026-10-08 00:48:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca92811-4978-3156-b255-b0cd1b4ac864 | -3.2955 | -54.074799 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dbbb7e9-38ca-3e09-87e5-251a424a75be | -4.0638 | -51.034 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c95cc3d8-a320-35ef-bfb6-79de3feebc2a | -6.1654 | -39.468102 | 2026-10-08 00:48:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ea9b0d9f-b70d-3322-85e4-943f2d4bd88d | -3.7185 | -54.2146 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86df7500-4def-3f36-87db-5d744e46a575 | -4.5655 | -54.959099 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fee3df3-7fb4-35b6-8ac8-4b1d3af4c43b | -2.9773 | -54.034302 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56304810-b948-3f66-bd7f-f7b66fd9a688 | -6.3491 | -43.333302 | 2026-10-08 00:48:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README40.md)
