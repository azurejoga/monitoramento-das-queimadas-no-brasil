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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db3856d1-5a56-3197-a825-2cdda387da42 | -4.46607 | -50.97502 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f6fc68e-bbd4-3054-ba0e-5a9cc78634b0 | -4.2677 | -49.97661 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dcb0441-b053-39f5-8003-20df51d1469a | -4.81535 | -49.2828 | 2026-10-04 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e3679df-7809-3281-9689-6ec3a44585d4 | -3.13245 | -53.72367 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8ec38cad-47fd-3f58-8c75-b055f7f604f9 | -5.99868 | -53.52343 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7882fbd2-b0c1-3d6d-b8dc-14c68cf1a2ad | -3.30146 | -53.83355 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f13a3a3c-6866-33ed-b3d4-56b9f416de29 | -4.39132 | -45.99301 | 2026-10-04 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5466b80-81c6-30a4-bc4c-eee20414ee7c | -3.08433 | -49.54572 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84e212af-7d22-3457-864b-7eb98ecb8ad0 | -2.82217 | -54.12616 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 515f9117-d9a6-3c95-aeda-66cd53052859 | -2.80213 | -54.10708 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 801c3744-79ca-39dc-ac53-f78d7d14c30f | -4.28671 | -48.56814 | 2026-10-04 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1fc0ec5-724c-3964-a717-3d2682cf8b3c | -2.90655 | -54.12536 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e36bec8-0fd6-3041-9a82-d1ee62f9edd2 | -5.99952 | -53.63971 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a07b478d-a870-33fc-b8f6-042af4043c4c | -4.26883 | -46.37081 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 678ae577-11a1-3138-b1da-f22bc1b3fe76 | -3.2079 | -50.74426 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac9b483d-169c-3990-b5b0-78caa59317be | -3.29413 | -53.84354 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45a5ba6f-92a1-361f-a4bc-846900ca2f51 | -5.99661 | -53.52527 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26f81074-9809-3350-b509-9782d0c79202 | -4.20344 | -53.46722 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 038ef022-8128-374b-974d-78768be9ff4c | -2.90169 | -54.0854 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e66a0e5-9e90-3510-b4be-386a105b9350 | -3.08676 | -49.53889 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce7a418f-b028-32cf-810f-f6b9098d24cd | -4.29819 | -50.26793 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 221a9434-e255-33ed-940e-acf3a6cb7cfd | -4.1042 | -42.50107 | 2026-10-04 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 13d66628-8ac2-3bf6-8fd0-76c1a937b388 | -4.30145 | -50.54278 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2581505d-4ba8-33de-b157-40343382cc5c | -3.19072 | -54.08269 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce6443bd-a527-39a4-b91b-7bcab2dbeede | -2.75354 | -51.5588 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68b687bd-55e9-3649-88bb-e91461e9dd68 | -2.81086 | -54.1243 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9701dbd9-9c99-3903-ae01-dd851be223f3 | -5.54348 | -49.76139 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bcacc15f-c619-3304-a313-941414bb65a5 | -1.35238 | -56.09288 | 2026-10-04 04:19:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| da20d614-c740-3c4a-bda9-744e3e446aa5 | -1.10014 | -54.11006 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adbccb93-9c4f-3d90-abdd-dc23546577f9 | -2.80471 | -54.09172 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46bedd58-5313-35d5-aed3-89b18809b01d | -3.19509 | -54.10139 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b47145ec-1c85-3652-baf9-6d893f5714ce | -2.68799 | -54.64343 | 2026-10-04 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7e01a851-5f14-3045-8a08-fa3a3d23cf42 | -4.2946 | -50.26332 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c821ee2d-73ca-3553-aa4f-1866777b6dfc | -5.22665 | -48.4067 | 2026-10-04 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17e3daf4-64d9-36ae-9656-0c57b90e9b3d | -2.8126 | -46.78281 | 2026-10-04 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcf32ed0-ffe7-3687-8b55-a01b018d8fd9 | -3.47216 | -50.09042 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9b575049-e990-3e50-9d1d-2040a816db0f | -3.11473 | -50.28571 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42b5b0fa-3a02-3a07-8318-6e73c18b521c | -6.08042 | -53.48018 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63b68479-4ced-39de-8da3-0e1d5833397a | -2.56002 | -54.72785 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62a5d995-930a-3cbf-936b-ff180135e2cf | -4.27923 | -50.277 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| c7fb28fc-0f19-36ef-9b6e-a3ef9cf99214 | -2.25669 | -51.88689 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 34ff263d-e33c-3cfd-83c9-9f228ed84b05 | -2.9059 | -54.12924 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6278e380-5019-3b31-af76-99c036fea80a | -5.28337 | -42.63504 | 2026-10-04 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88137ae6-58c6-353e-b317-81de6c43bd4d | -2.25468 | -51.88468 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 70725d40-0478-3542-853d-9cd3b4617096 | -4.27224 | -46.37135 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9fe9429-339b-3a9e-a019-f974575abaa0 | -3.70933 | -50.65617 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4443b23-5983-3a2f-9da8-af3e94d39795 | -3.11616 | -53.75418 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7788db13-0915-30f3-9525-c9dfd208d2e7 | -5.86566 | -55.70894 | 2026-10-04 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6cb4d99-e31f-391a-a50a-65cf008be573 | -4.28706 | -50.28241 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec96a691-ed0b-345a-bae7-782b05b0c923 | -4.13384 | -46.82276 | 2026-10-04 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8f8935c-780f-3d40-ab63-455e4fcf5f6f | -4.15503 | -47.53731 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95665d74-5b0c-3ae9-a553-1b3ff3de7031 | -2.82538 | -54.10687 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7887ffa-98a1-330b-be59-430f86c4d2d3 | -6.2808 | -53.15275 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0719dc29-86f3-3bbe-9170-95cb51367bc2 | -4.27542 | -49.98171 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fac6711-70be-38a0-a108-fdf5d68eb53f | -2.96241 | -54.10304 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a97168da-8140-381f-90b8-8731ff7546c1 | -2.58537 | -51.86179 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c330b10-5e04-3424-885e-218496568322 | -7.99819 | -44.49031 | 2026-10-04 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7df2d6a0-bb38-3722-a540-3643cfd2b92c | -2.92796 | -54.10137 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1458a598-768b-3e69-a39b-c21f9568ae98 | -3.50526 | -52.96116 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82c9952f-c5f4-3cff-a8e6-b53cde18c1bc | -6.89824 | -43.68414 | 2026-10-04 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 414781ff-8346-3837-993e-4aaab4618c04 | -1.4841 | -49.47638 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd978d72-e88a-3cc2-9eef-fda38c37d2f8 | -1.85787 | -47.97538 | 2026-10-04 04:19:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f421e0d-759e-39a0-85c8-61b90204f421 | -1.41318 | -49.26991 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c04e499-157d-3ae1-80e4-e64b468979d9 | -5.36236 | -44.94675 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed2d6d4-986b-3479-842e-136bdb39f680 | -4.29394 | -50.26726 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cb868720-3f89-3da4-95e3-50a0b92de53d | -2.99022 | -51.04771 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03d5994f-0c64-369c-a407-35edbd84c1c9 | -3.04649 | -54.21057 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 544523e9-496f-311b-a3dd-c4b36c6cf7ba | -7.27886 | -49.25283 | 2026-10-04 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa61c37a-5c6c-37fa-badb-3c65b8522e7a | -1.18158 | -47.61082 | 2026-10-04 04:19:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b64b8035-8262-3c87-8c4b-61527bd3a3cb | -4.43151 | -43.11663 | 2026-10-04 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 761e87d3-8370-3e5e-8dc0-e129940f8177 | -3.51806 | -54.60604 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cab46726-0616-3a47-992c-4b15d5786629 | -2.81343 | -54.10891 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 62b0e292-048c-397c-a8ac-a31f729756d7 | -3.01249 | -50.46951 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 70a360be-4fd5-35b0-983d-93094a1eade0 | -3.70863 | -50.66043 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bfda26ab-af1f-3445-8368-f5845468b447 | -5.34591 | -44.83073 | 2026-10-04 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4204673-01e2-3bd4-aac3-111bcb9637dc | -3.05349 | -54.16819 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 985ce2fc-d205-3c04-a7e0-e2028c6777f8 | -5.57925 | -45.40572 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b39398f2-2ea4-3b9d-a4b9-0bd02589f0e0 | -2.81407 | -54.10505 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bbd1f5b2-54b7-3a90-8d00-91bdf000c685 | -3.30025 | -53.84079 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66bbd325-b906-3441-905a-353bc5c85a2c | -1.15836 | -49.25428 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22bab749-e79d-3b63-85f8-f1d35f6b0950 | -3.07617 | -49.55238 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc8f88ca-adda-3062-8acf-82e9dba66ced | -6.71177 | -45.97235 | 2026-10-04 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d7af278-6dea-394a-846c-4ed0e242c303 | -3.30636 | -53.83806 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad4ba3a2-8213-342d-af3f-dc3387c6724e | -3.20502 | -50.7514 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 54778abf-661f-3e54-9b1a-2b0e32bd1533 | -2.22281 | -53.70915 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d930a1a2-fc00-308e-9d2f-fc5492023aab | -3.1901 | -54.08629 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa833adf-7449-3bda-b4e8-fc0c6f58d462 | -0.49744 | -49.10276 | 2026-10-04 04:19:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cdc5fbe-1dc3-3dd5-984c-88ecdbdb4d85 | -2.91025 | -54.13793 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcdb07a4-cbc8-3803-9f04-390c92b5b36b | -3.07098 | -51.27418 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10b9595b-afa1-3978-9e06-9cf6945d7641 | -4.28348 | -50.2777 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| cabf4835-41fa-38de-82b3-4868ba1b097d | -3.1166 | -53.71742 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 103dcfca-7501-399b-8d5f-61f89f378447 | -2.81151 | -54.12043 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 793223c9-3eff-3354-948a-f2857b31dc4d | -2.3642 | -50.6039 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e36eeb4d-fbd1-3ca8-8e63-03b5bf96153a | -6.71234 | -45.96882 | 2026-10-04 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f28e0ac-4340-3c77-988a-2275df2182bc | -2.69516 | -49.03356 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 06410e3b-19c8-33a5-af25-a3ee446ca834 | -2.25516 | -51.92625 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30b7855e-bf56-327e-98cc-514a520a4d39 | -4.18268 | -44.2642 | 2026-10-04 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0dd1267-0cd6-3c4e-abc6-be194d654a0f | -3.04522 | -54.21829 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c23a02bf-ddc1-3a90-a326-044240118310 | -1.90869 | -47.01664 | 2026-10-04 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c23f0bce-c414-3bb0-b359-6620b9e595cd | -3.12402 | -53.74071 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
