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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b117a4b-ea40-3f6a-8d7b-dbf3ea59bc7a | -3.2835 | -53.868 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22c7a89a-3f0d-3b17-862c-9f3c6d6b5c59 | -2.7658 | -54.080502 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1753bb87-eddf-3d5a-936a-ad953fc7852b | -3.5434 | -59.479401 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 224f00b1-0cad-34b8-95c0-7489b6b3c743 | -5.9953 | -53.509499 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 119585bf-77dd-3291-b92c-99107209d67d | -1.5092 | -54.840401 | 2026-10-07 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 441c0cb0-8ff6-35b0-8edf-41627558a550 | -3.4908 | -54.625401 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d92bbde6-7208-3e79-bef4-68aa40e07c7e | -6.2181 | -52.7915 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8692c862-6bd7-3a4e-b95b-db9c831637c2 | -6.4408 | -55.020699 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3be9974e-f343-34ec-a647-2e80ad730a99 | -3.0046 | -57.749401 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 651251fb-c2eb-3a4a-8bd8-58e5c1067b98 | -2.961 | -54.1213 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b255b88-0a79-3f8e-8747-ccf74017ccca | 0.9424 | -60.404499 | 2026-10-07 01:09:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f09643d0-b6db-3a06-8428-346e8d454bda | -17.441099 | -43.653099 | 2026-10-07 01:09:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7928c8dc-6e81-3171-858c-9caea788e7a7 | -3.1657 | -58.6339 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f12a2335-b97f-3fc2-a8f0-30f8f9ebef6c | -3.8887 | -59.322102 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb663661-264b-3c0a-9774-96c403256f6b | -4.1365 | -54.917801 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2be90083-11dc-3222-b28a-0bbd227065a0 | -3.4879 | -59.597698 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e858cf5f-a617-314d-a792-99fe255d4495 | -3.6855 | -55.955299 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e76403fb-64c4-3133-9863-a3d5a85863be | -2.8682 | -54.210098 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f205a80-2d85-3f1b-82fd-0f1edf429d6e | -2.8827 | -54.139198 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beaa00a9-b931-37e1-9890-80ae1694c535 | -3.3037 | -54.043301 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f6eda4-8b70-393c-b89e-7aa60a856e8a | -3.6061 | -55.478298 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7991150-c9ca-3674-9253-c2970a591ba0 | -11.7255 | -43.644299 | 2026-10-07 01:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c13301f-9530-3b35-8f40-1bf91d0aacb2 | -3.5308 | -54.6642 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b403cf12-def1-3ded-9196-9a6c9549f55d | -3.2995 | -54.069599 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55717366-ed8f-3ab8-bda5-7e0491f9d493 | -3.5353 | -54.639301 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baff7c9a-78a1-30af-b588-f06492ed0667 | -8.2911 | -50.291698 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eabc7336-7c04-34d4-8093-79030527b163 | -3.9734 | -55.8172 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb1e7f8f-a602-33e1-81aa-d7d1d0a806d3 | -2.5272 | -58.095299 | 2026-10-07 01:09:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb5aed6b-6487-3df3-886e-7553eb91a734 | -4.3754 | -54.7472 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8a55189-0ac2-3a9c-8cd2-e9ebab9f9a23 | -2.8516 | -59.109001 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a927ee67-e181-3032-a8a8-45917b01b8a8 | -9.7997 | -48.915901 | 2026-10-07 01:09:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1442dd3f-46b8-31c7-a266-a4c36eba2024 | -3.2766 | -54.015499 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e64ef8-4db1-3e61-9ded-9a5250d933b1 | 4.1501 | -61.250401 | 2026-10-07 01:09:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| effad782-6aab-3f33-b8db-bf19652b0d9c | -2.0535 | -56.886101 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85a9816f-055b-3d32-a000-49bd7adda465 | -3.5175 | -54.651199 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2176e0-e47e-3211-a8aa-dc0e986ae21b | -2.6032 | -57.572498 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a7da2cf-0651-32fd-8d08-b8c8a0b923a9 | -2.9717 | -54.2117 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e71bf29f-0a2d-3918-955f-32f575e21598 | -3.2845 | -54.005199 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49dd331a-168b-3c65-b1cc-cdd43fcb48ef | -3.0268 | -54.1824 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855e14cf-b442-301b-8711-37590ffe3aa2 | -2.715 | -57.4757 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 401a6215-4af9-3053-9128-a16cfd84e1c3 | -3.5354 | -59.4893 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99db7027-5334-334d-b707-0a808f153659 | -3.1155 | -53.766899 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9cd5353-1175-3ab9-8d70-697418fd1847 | -3.6253 | -55.2934 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a832d89-417f-3ad1-a967-782b729edd3f | -3.0952 | -57.6497 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23b58b54-b7a0-3c37-9215-107516823e7b | -3.5042 | -54.638401 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 782ba4b5-1b8f-34d6-a978-1c4f96f56c04 | -3.031 | -53.890999 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0246b3a1-0eff-3714-8fc1-3011315744c2 | -3.4979 | -54.655701 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a28c3551-a07d-39f3-b4ea-f849a58f6ac8 | -3.3014 | -54.077702 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab36144-6f77-386f-bb06-2a3238e7997d | -3.0659 | -54.1735 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3ece51-5708-3c09-886a-3609c96f7ea8 | -3.0876 | -54.3106 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7658d75e-5f12-3884-ba5e-3c4d29e03a86 | -2.9744 | -56.629398 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f192a27b-e1d0-364f-b075-7c66c1884024 | -2.9731 | -54.084599 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b17dd20-91b9-3d8d-a0a3-4be104279e75 | -3.0525 | -59.901199 | 2026-10-07 01:09:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e353906b-55cf-35c5-816c-a92fd64f1b9b | -2.993 | -51.056 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee632502-d297-3a1f-bb9e-03ed397a2b8e | -2.9624 | -54.171799 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9f80c53-5f70-3d6e-8082-65d0f1d60069 | -3.2301 | -54.302898 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b79d95d-9a0c-3568-b1b2-f492b3fc2e38 | -1.2931 | -54.575199 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6199e39d-6915-379d-911c-7c36fc03efa2 | -12.1788 | -44.744598 | 2026-10-07 01:09:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eeebb43b-d4ac-33f6-a01d-20240c012ac9 | -4.9217 | -55.858398 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d74602b9-c4c7-3a28-8583-9dfb76520ae6 | -3.4803 | -50.079399 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69181147-ff27-3442-95de-51ad6cf1eac0 | -3.2285 | -53.8979 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10a55c1e-ba9b-3ab1-8438-56b00d18362b | -3.0453 | -54.262001 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceb05a1c-7247-3bf9-9c43-f0021d3ac98f | -3.4365 | -56.934502 | 2026-10-07 01:09:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc123c47-cc80-3f23-9d4c-7033d4a374d7 | -1.7938 | -57.102001 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebf4e41a-cb7c-338a-b3b2-6cb5bec8958b | -4.002 | -56.254299 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3a500fc-c032-3eb0-892d-c3f372057b30 | 4.1483 | -61.258099 | 2026-10-07 01:09:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa81a8d-ff76-34df-a8f4-a8e6717823fe | -13.6437 | -44.431099 | 2026-10-07 01:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 195ce4f4-cb74-35b8-8b68-2482c3cd43df | -3.5067 | -59.9529 | 2026-10-07 01:09:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20b2dcb6-8e84-3880-90f0-4d539e9f867e | -14.3767 | -55.048199 | 2026-10-07 01:09:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f64cc41-d2d1-3818-b97b-6385a691e86d | -3.2856 | -53.832802 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b57466e-78c0-3daa-b158-46dab167cde7 | -2.993 | -54.037399 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d4d93bf-de51-3749-80ab-869fbaa6282a | -12.1884 | -44.741901 | 2026-10-07 01:09:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d5ee374-722d-384c-8823-8048e221eda1 | -4.7626 | -55.660801 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aec26e70-37ac-38fb-86ca-ff7de9293689 | -11.0605 | -49.580601 | 2026-10-07 01:09:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a202988-5c47-300d-982c-9d5199e9fa6d | -3.5532 | -59.4772 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae949e7b-5e88-31b6-9bbb-67475654fa7d | -3.8904 | -59.3297 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3da98056-2a02-35ed-9dfc-470f3f9f9672 | -5.6827 | -53.497002 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f31c61a-a2ed-313e-be92-a9b296ce53be | -4.1331 | -54.903198 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3659124e-d54d-36ab-940d-e89f14aa0083 | -3.5916 | -54.570599 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b191d56-1525-3317-a9fc-6587ddd68023 | -8.9168 | -49.979698 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba8158d3-0aed-359b-8548-03448167666a | -3.4835 | -55.438599 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3727103-552a-315a-92a7-e579344c5cf2 | -3.5371 | -54.646801 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96c30b78-fe3f-3128-9de6-3082adc8b0ca | -2.4897 | -58.0672 | 2026-10-07 01:09:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cf2b15b-726e-3aca-85f2-4104188dde62 | -2.9465 | -54.1922 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a14e4ae6-c57b-3652-921a-325a94115d83 | -2.1097 | -52.066299 | 2026-10-07 01:09:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d85de2b8-97a4-3ded-aeea-b735f187a0e4 | -2.7677 | -54.0886 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2dc416a-2225-3d89-a908-1c7b8cbdbb74 | -11.7994 | -46.707298 | 2026-10-07 01:09:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3428d553-3b2b-395b-93a6-90e6e69c0e61 | -3.0837 | -54.160999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6d49463-48fc-3673-a059-ed8b459951ba | -3.732 | -51.221401 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef0f939-34d5-36d1-95fd-f8596a8154d7 | -5.9848 | -55.368698 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03532885-8a85-3d01-bdc2-04185faebf45 | -1.4734 | -54.775101 | 2026-10-07 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb7a8887-d52c-3c41-8b52-95364b378eb6 | -4.2686 | -54.864601 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f39065c-582e-325c-ad87-60a5154b0862 | -3.2203 | -54.305099 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 744f1602-181d-369f-b67f-abf3a56f665b | -10.9899 | -45.431801 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bfd86a7d-54fd-30dc-9118-a6ffcf11ae9f | -3.2819 | -54.0821 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ffa3b6c-20e5-3658-b552-0463419c1688 | -6.2151 | -52.691299 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff2634f-9cba-368b-9a9a-cf46fb80e090 | -3.6073 | -55.305 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd547de-631d-3fdb-bfcc-c112a0fc8a28 | -2.9889 | -54.063999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8cb6117-d6ab-3fd4-8fa1-c69d4df5dd9c | -3.1014 | -54.148499 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 068ab1b4-b929-3fac-8ce7-f1e53589bbb0 | -10.9995 | -45.429199 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README21.md)
