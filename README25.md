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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ce58bba-b75f-3689-8040-a2e6839d83b1 | -3.31423 | -53.84841 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6308ef5-7d0b-3c8a-865b-b292afc03760 | -1.62996 | -55.1306 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 009e0d93-6bf8-36e0-bd77-f93c08266652 | -3.32142 | -53.85218 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0984d88d-d871-3510-b0cc-cd7a34b35f7b | -6.85693 | -41.63963 | 2026-10-05 04:38:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 876e7aeb-2cfb-3404-8d53-59ae160a186f | -3.12348 | -53.71792 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54ca777c-3a17-39c1-a994-4800d0252293 | -2.95711 | -54.14731 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b74fd700-75aa-3d89-8ddb-978ef1c1591f | -3.12853 | -53.71878 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 313552a6-d6f2-3180-9f00-c2eb60c2dae9 | -3.37765 | -54.10643 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3742168-006f-3a5f-90bb-48b0023d5281 | -3.71361 | -50.66097 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d8d1690-f977-3a79-b8f4-21643e34a41a | -2.48897 | -56.10695 | 2026-10-05 04:38:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1c0b3d5-3607-3281-baca-00714b1ff5ca | -3.11126 | -53.761 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b9667106-2ce2-30d0-816c-7d48242c9ad1 | -3.85964 | -55.81951 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa46a377-f6be-3918-ab9a-82d9828ecde2 | -3.22901 | -53.87321 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 496d9632-3aff-3f22-bdad-3226fe1b2c6f | -3.12005 | -53.72683 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e02ec642-d40a-3d1f-b6ab-209489fbe088 | -1.33526 | -54.22581 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9700d7f0-da43-3deb-9c05-fdc2caebd5df | -2.80938 | -54.10049 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72a10b48-36c1-3ee8-8bf6-5b61442abfeb | -4.44246 | -54.96513 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e6c208b-b20d-3db6-8c9b-cdc26cc6e160 | -4.07773 | -48.96191 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8293e3fb-e4cc-3389-99ef-e47c2aad3553 | -3.07216 | -54.16338 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fe9f71ab-ad10-3f5a-898f-244a476419e0 | -3.07684 | -54.16739 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8470573a-4d10-3d82-8145-57c757c56c4b | -2.22385 | -53.71509 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2ec329c-9827-32ba-99d9-fbcad940ea99 | -3.27383 | -50.40456 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5b49af75-0df7-34e8-9409-98b2e8f034e0 | -3.07787 | -54.19302 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc0cb720-5e09-3f11-abf0-10efa1c91bac | -2.98538 | -54.10674 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6012f6ac-f153-3471-b427-17b139930dab | -1.33338 | -54.22615 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3274e3a5-c615-33a1-9dd9-e54eeb023395 | -2.22434 | -53.71209 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3020c01e-db4f-372e-a54b-fa5a3851b0cc | -2.93993 | -54.08717 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a1b71d7-36eb-31ae-99e9-8f1b30efe554 | -4.28353 | -50.27791 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2891555d-0571-3fcd-8377-f989a4b33d42 | -2.25232 | -51.93706 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1676fc74-4a05-3678-977e-a6c3ed85c1c1 | -1.97239 | -48.91692 | 2026-10-05 04:38:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3312c845-06da-301c-be63-6dcc107230f3 | -3.11871 | -53.74721 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa1421f-6a09-360e-ba67-8c27cce7f317 | -2.99148 | -51.04381 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cdba4346-eab0-3e98-be70-72b957da2580 | -3.04639 | -54.22018 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 651955bd-018f-3b1e-bafb-9ef302c036db | -3.84597 | -50.31115 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 356b99de-21e3-347b-9d59-8261698adb9e | -2.79792 | -54.10502 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 679f10e7-7dbd-303a-ba13-e2139dc75cae | -6.89944 | -43.68324 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 562d72c9-8ba5-3e10-93ab-5b2be20e1e60 | -2.94336 | -54.19657 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49df392d-91cc-3fb2-bb76-3b40ff6bb664 | -7.32997 | -44.36694 | 2026-10-05 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77ba28cf-cf39-3c6a-b27b-e1d76d1b055a | -4.04189 | -50.75819 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1cbd51c-f025-3c47-8082-e9e74cc235aa | -3.12916 | -53.73439 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fc9cb7e-5946-376e-a64e-6ad99e62bcfd | -3.86743 | -55.80864 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70d6e264-e75d-3265-aa5c-620fa3409dc1 | -2.79428 | -54.09472 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8477255f-e781-383c-85c3-f4e408cab0af | -3.11604 | -53.73171 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14537a61-80ec-3ba6-a6c8-bf7aaf17c962 | -3.61398 | -54.60117 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7431ba80-6e17-396f-b0cc-dd3a7d95f222 | -6.89175 | -43.6861 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95c8de1a-a5ed-35a4-92d4-818a5684ea66 | -1.55146 | -54.79898 | 2026-10-05 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52728311-1a02-3224-93c1-c0d20958f763 | -2.82036 | -54.13152 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8755090-3505-31a5-bab9-fb912e904c47 | -2.82088 | -54.12834 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a494ce30-d76f-3fd2-9ae4-59abe63b2fe4 | -6.91774 | -43.67664 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d4cbc3c-72f9-341f-93d0-4098b6b962ce | -3.12253 | -53.72377 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c18bb1-8f16-3bb4-833e-1c15555b1302 | -2.8261 | -54.12922 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66a9117c-1143-30ad-9af0-965d849158dc | -3.30472 | -53.85848 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea0f0dc5-67b2-3e05-ac61-e75d80f54d0b | -3.08521 | -54.18135 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| f37df35e-9bb7-321a-8f93-89ea272ecb13 | -6.65207 | -43.76849 | 2026-10-05 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ff300e1-6446-3f3a-a844-07f926930779 | -3.51337 | -54.60871 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70310809-a9c0-3fa9-a6f1-1e9b17577b73 | -3.12012 | -53.75691 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f330cab-ed19-3dce-aace-89ddf4451991 | -3.10593 | -53.73 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be0bc3f5-9b8b-3ffb-b78a-7cd12843e7e6 | -3.65694 | -55.50706 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7009718-73de-3b74-8132-be5680cd128b | -3.05517 | -54.17002 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ee3ebcb-574c-35ad-911c-ce49756fcc9d | -2.94282 | -54.20083 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d761746-024a-3e4c-84a1-a3e848791c9b | -2.99162 | -54.10142 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 655460e9-b16c-32b6-b98a-e0e313cf5530 | -3.10545 | -53.73291 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc02f345-743d-3c40-b216-02892a29df2d | -3.31831 | -53.85516 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0b451f2-47fc-3674-8ceb-cdc25582817c | -4.10922 | -50.80623 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf94bb11-686f-3991-9390-3cab212c2bba | -1.24839 | -55.88364 | 2026-10-05 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec41d98f-bd39-35d6-852f-f0dbfe1e165d | -7.89708 | -44.19651 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bef568e-a4de-3b66-8cae-951e0795d318 | -3.123 | -53.72084 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17f7bafb-6587-3450-838d-12c056cb1207 | -3.10039 | -53.73205 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a39ac68-5d2c-3d0c-bd9a-3cd4b1a5c2d7 | -3.06071 | -54.16768 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f31ea904-8c3b-3b3e-8a4c-329b43d5d70c | -7.32651 | -44.36641 | 2026-10-05 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdc57bd3-8949-3836-b1de-28efff63e7eb | -3.13213 | -53.71689 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 89ea624e-d63b-30a6-b0d7-a153161191ff | -3.11986 | -53.7083 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6e5d505e-af82-3300-9092-87cd5e7df5a8 | -1.74238 | -55.24013 | 2026-10-05 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b20b4a2-01f6-314e-9778-7fbe3901ed6a | -6.90545 | -43.66787 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70c88c2a-0c13-3791-b65d-5397c318f91a | -2.94315 | -54.13288 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe8dd31c-bcd3-3c7f-81f5-95336a570b73 | -6.05556 | -53.48027 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0863d5e6-d3f7-31b7-97e9-4d383097140c | -3.30013 | -53.85466 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de3689f0-13e1-32f3-b0aa-db948ce43a01 | -3.15608 | -50.43972 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 972bb3ef-50ba-3a32-b104-1ffa0df059b5 | -3.2924 | -53.83817 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a7aa7be-ddcd-3464-bee6-8a3ccb9deb98 | -3.27038 | -50.40043 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 247fb33d-5545-3b60-adb8-bd6bb57adf85 | -2.69408 | -49.03631 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 23e40293-d9df-3ab8-a84f-901e63f2456d | -2.81981 | -54.10222 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21c27b1a-53c4-32bb-97b3-8d48bf742500 | -6.00006 | -53.51487 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ec1e955-750f-3699-b7b7-8e323375479f | -3.10955 | -53.73963 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a595422-d195-30e6-ae42-3aa00cccd171 | -3.58901 | -54.31269 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d48aa727-9c35-3c90-885e-514c78d7d233 | -3.80741 | -50.85379 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e5ce0e0-bd12-32a4-9bbb-4cfa2d29d8d3 | -3.7055 | -50.65955 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01d1b60e-0e6e-3ca1-ba72-65c0a0239732 | -3.50858 | -54.60453 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6a9cfdd-addb-3238-850c-9fe8c07592c4 | -2.88844 | -54.13965 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5ee1817-8526-3488-b314-e7195f1ef61f | -6.19968 | -52.79536 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 387773a2-fdc7-33df-96c1-3ef4bb9067de | -7.88601 | -44.19868 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40d42a56-e9da-3867-930b-d1819862fd28 | -2.95244 | -54.1432 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b3ee4053-c0f4-3f6b-b616-8f21fdf1e9da | -3.13718 | -53.71775 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 01a0301f-17c3-3569-ab7b-054fd84a9b7f | -6.3363 | -42.54247 | 2026-10-05 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 02824984-6469-36e1-94e4-d1284a00e1df | -3.50582 | -54.60741 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 483fda35-926a-3a32-a5eb-e5df8af1bd0d | -3.33525 | -53.39472 | 2026-10-05 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0fadc55b-6778-3d9d-9bb1-e1e62c55bb75 | -3.09798 | -53.74677 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f478183-9bea-35c3-a2f3-3625b32e3787 | -6.90837 | -43.67239 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa4eafd0-44ee-380c-886d-fce4085ee953 | -3.32389 | -53.85305 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0c297c5-440f-3b9b-83e0-3f7d9cf13de4 | -2.81511 | -54.09822 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
