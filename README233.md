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

## Dados Diários - Página 233

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d44a7fa-4e8c-34cb-b9d1-db5db1ddbf1b | -2.76504 | -54.08615 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9985b2bb-b078-36e6-bffc-9fa32bcc57c4 | 1.65251 | -51.05351 | 2026-10-07 16:39:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 32608ff2-2959-3b7d-9cdd-2a6bd1f28155 | -3.03783 | -58.02026 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e40f7621-d434-3775-85fa-8db1ccc358cf | -2.94414 | -54.16559 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2be71d38-a786-34d2-91bb-1178a966c1ff | -2.794 | -54.09583 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d668eeae-770e-3dda-8816-3f67278969a8 | 0.7002 | -54.54117 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ea91ec9d-e979-304d-9185-93fe24bb9923 | -1.78818 | -55.02179 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea1e7347-0164-3589-b86a-4ad62bd1ed62 | -2.77397 | -54.10929 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| db960f77-af10-3c4e-8b65-455f02765070 | -3.18277 | -50.57036 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6a135c69-b062-3d9d-a466-ce7722b84f55 | -2.79268 | -54.12385 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ff4eb094-ce8c-3726-8103-5dd5bfbdcf9d | -2.62476 | -43.68975 | 2026-10-07 16:39:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f84af7df-95f7-37f9-a55f-da720e2f2b36 | -3.11404 | -54.17087 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8bab1ffd-9270-3203-81e7-dcf53a7c5f42 | -3.54252 | -54.65621 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 41ce2b1b-ae11-3ce1-b9b5-d98810bb96a8 | -3.11304 | -54.16415 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b64caaae-1473-3024-9a45-f41609948804 | -3.16936 | -57.86182 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4506aae-df52-33c9-b6fd-b74c44a1c8da | -3.29696 | -54.07687 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b1dabd7-655d-3e7d-8e3c-eb2d2fed05dc | -2.78849 | -51.67345 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9cb60f1e-dbf7-3ac1-a459-2618150388cc | 1.34399 | -56.13414 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b79bcec3-3fe3-331c-a974-edd4e5905bce | -1.59524 | -48.74226 | 2026-10-07 16:39:00 | NPP-375 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44a54b96-2c0f-32c9-869e-823226f2d92b | 0.69942 | -51.4338 | 2026-10-07 16:39:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 241405c6-3a78-3c85-8398-74d0dfd0cc74 | -2.78922 | -51.67491 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb1a8042-9476-3189-97bf-e6b9bb6504f3 | -3.66573 | -57.09038 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ecac9e6e-d96d-3af4-a3cb-d5494537e148 | -3.02876 | -54.23756 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b147022-a49f-3584-b92a-a7320a26cc5e | -3.04317 | -53.91366 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2301f830-4e14-38f1-a983-aa9bc23d0ab7 | -3.35701 | -53.53619 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0a40dc0-5be6-3639-a17f-74ff681783da | -2.92809 | -53.92865 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec7c9faf-774d-3bb2-b5c6-f89b4f4b833e | -1.83631 | -54.93763 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| dcd5ee01-8f2a-332c-8224-b5732889e281 | -4.15613 | -55.15349 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cddab6c8-3451-34f1-aac4-68ad27a5c2f4 | -3.8498 | -55.98684 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bfea01db-6a87-3923-a00a-ed8d3df86fb0 | -3.02838 | -57.48865 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5f0a32c0-cf9c-350c-82c2-570875d4fd76 | -2.99364 | -51.05022 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 89113f86-cfe7-31b4-8b06-81348ad8964f | -2.55689 | -56.43399 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 789fbd7b-b91b-307d-b1e1-56e381753d4d | -3.13025 | -53.70235 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cc2a5558-9529-328e-ae60-995a7cb79d28 | 1.75926 | -55.5691 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 78b75126-d718-3dfd-8ee1-8e3b22ffffc9 | -3.10241 | -53.764 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| b2fa4068-ec4a-31e3-9efb-0e6045a96830 | -2.40392 | -51.30559 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5c58422-6d7c-35d7-94e6-71e88b8a225d | -3.30035 | -54.06222 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7074863c-8a23-3a26-8e45-b41acda57b0d | -2.49316 | -56.05993 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 013faf04-288a-3d69-bc44-d472fe7e280b | -3.47904 | -54.63106 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 491ce388-c695-39d2-898e-4491a10eef3d | -4.06509 | -55.32515 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5c2afa88-5f79-3868-9980-919a7a42c864 | -4.77065 | -55.71951 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 00c7ac4b-6de5-32ab-91bf-2b7a24c20cdf | -2.94468 | -54.16914 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4df8aa87-1f8d-3bd9-814d-f56d74e99ef0 | -3.44583 | -51.08512 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ca3a3da1-0235-3195-bebc-57364beb706c | 1.75431 | -55.59526 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4253672f-0289-3686-ad8d-b6b8ec646d87 | 1.76308 | -55.58093 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| afdf9885-00e5-399d-88e5-8957476851c7 | 1.76229 | -55.58142 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1309a05a-ba12-35e6-acf7-466f7930f7f4 | -3.29784 | -54.04512 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 161.7 |
| c2ea4d45-d4c1-3902-9c18-a414d730fbeb | -2.66355 | -54.3128 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6420019c-f0eb-3fdf-9814-300ab2912dc3 | -1.13308 | -49.23165 | 2026-10-07 16:39:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 97edcc55-1051-3d64-a3b1-beb4ed9426d4 | -2.84723 | -54.07123 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb72fde5-04b1-3fb5-955d-86d72c0406d1 | -3.27175 | -54.0558 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 36b9a19f-9144-362b-9449-a8ded9fea04d | -1.99659 | -54.09683 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5de0493e-1ccd-36da-9b9c-3f43b99723a6 | -1.63045 | -55.41555 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed085c91-2e00-349d-9f39-0328a540b175 | -3.29977 | -53.87218 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 9061eac3-e816-38a4-a556-90ca939bd510 | -3.00886 | -54.1413 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dad99a57-84e1-36f8-a9af-88fed617bb2b | -2.78862 | -54.09666 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ad8c7e31-3e5c-310f-8f70-7feb7e8a1b7b | -3.07716 | -54.26185 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a908942e-e586-39b6-8d8b-c45920156ffc | -3.68093 | -55.94239 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e54c3db-ac79-329b-854a-a3cafa90378e | -3.74296 | -51.2133 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 6637eaff-60eb-388f-980e-95b9c19bc57f | -1.24814 | -55.70225 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e5a4d579-979b-3b8a-9ff8-7e357a43b6a6 | -2.80416 | -52.08918 | 2026-10-07 16:39:00 | NPP-375 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 2b894303-3f25-3197-8403-dbcc59e988e2 | -1.79998 | -44.88163 | 2026-10-07 16:39:00 | NPP-375 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b565d5a-8194-32f5-ab43-45c3da81e75b | 2.71605 | -51.36583 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 465be32d-8ecc-37e2-83f2-3150cd2e993f | -3.49377 | -54.61355 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aeab81f9-404a-37bb-9fa2-8d69e80ff1c2 | -2.06826 | -50.82755 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10a20244-00c2-3a3f-a5e1-233505bf0781 | -3.49876 | -54.64765 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7cf3bff9-49b2-3f2c-93c6-9d2397246d77 | -1.28315 | -55.84888 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 86c2659f-954a-3fd6-b344-51ece3d00aa0 | -3.12722 | -43.83892 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| b3fe3c83-b580-3fd2-a3c1-5e2cebcaef75 | -3.29283 | -54.01097 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 12f48a96-8495-3423-aa46-d45fd0429662 | -1.82406 | -55.08681 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 331990e2-7597-3dff-9e83-cd6f84b3f53f | -2.77093 | -54.08874 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f46cdc85-a5aa-3b41-af31-9de5ae2687a3 | -1.74456 | -57.18245 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ea367bf1-163b-3313-97be-fc7b75fb5166 | -2.93439 | -53.93448 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3145b77a-db96-3695-88ec-16c5a8bec3f7 | -1.46681 | -54.76447 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 55c515ef-dcbf-3ea6-8eb2-53e722fbfedc | -3.51171 | -58.59796 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 04bc9433-af60-30c7-b285-d6c42f66b67d | -1.11436 | -52.27775 | 2026-10-07 16:39:00 | NPP-375 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 75b1ac44-d46a-367f-ae04-97278d7203ff | -1.71247 | -55.44909 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 57076db2-7bf6-3c2d-961e-46f547bbd4b5 | -1.83534 | -55.04598 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fefbc73b-c51b-3e3d-b16d-2e2533d960f7 | -2.46084 | -46.01654 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 575e79a3-472e-338f-86dd-286078eccf97 | -3.02568 | -53.90596 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 82cbeedf-3233-3277-9a98-55aec82615e2 | -1.21093 | -49.03387 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8c2c093c-d3de-3066-9be9-acacf430c55c | -3.27959 | -54.03368 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0e539d8-51b5-3d79-93f6-e5d252a68317 | -4.16008 | -54.02957 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fb72ca4e-0a2b-3da0-b74a-8159fb492ec1 | -2.49304 | -56.10339 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ce3e8a3a-23ab-382c-9806-41242d532e7a | -3.05332 | -54.14197 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 64508fbf-33e0-3256-ba80-c62dafa814fa | -3.09083 | -53.72787 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 26364d45-aefc-3ae9-a487-b69b0b28a60b | -3.84765 | -55.97922 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e7cc4159-b8ba-3f88-b013-092d92fa0b7c | -3.53834 | -54.64203 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3f7066ce-fe7d-3f39-a432-cbbb6ebda6d8 | 1.71285 | -55.6104 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cf2f36ec-228c-35c7-9104-db83406daead | -1.24671 | -55.69896 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f66a34e8-3b76-3a36-8ab0-545185e76797 | -3.51893 | -58.59703 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 265e8d83-36d6-37fa-a49c-d43914db7a22 | -3.62124 | -54.6019 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4263338f-59e3-3a0f-a189-b2252c4f1b19 | -3.03056 | -54.51682 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9553a95b-e799-3170-a929-77a608795c23 | -3.83529 | -55.97417 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e18b1d32-b323-3bc0-a730-f8d45752b23a | -2.89427 | -54.16574 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b88b80b4-995b-3318-8c9b-45824952f817 | 1.63287 | -55.78494 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddbaca25-3027-39bd-aff4-172cfbc4b4a4 | 1.75868 | -55.57275 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6ae422fc-7d2a-3a69-9649-cdb92ae0c35e | -3.04296 | -54.14687 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 97e176a0-87a3-30f0-b651-6235045b0536 | -3.06328 | -54.20762 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8afa7967-0120-32be-a094-9fc282a88eec | -2.11026 | -45.67403 | 2026-10-07 16:39:00 | NPP-375 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README234.md)
