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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 862eae9b-ce84-358e-924c-056eefee646d | -4.54794 | -48.51202 | 2026-10-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 753b0711-3e1f-31d1-8973-a982e131c6b2 | 2.4641 | -50.83778 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 765d5b7b-d3c1-3248-915b-ec93ced8387c | -2.32354 | -57.98906 | 2026-10-06 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| acfdcc34-191f-3010-b605-1444651e85ec | -3.09892 | -53.70796 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b738d05-705b-3405-9138-d71ba5fdad58 | -1.08501 | -54.1201 | 2026-10-06 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd43692c-f461-3bb4-9450-bdca50d5b171 | -2.86715 | -54.14107 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d423995-c42f-3370-b77c-be0a7b4e7c28 | -3.93757 | -42.99052 | 2026-10-06 04:38:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cfbc1129-c7fa-32a0-bf8f-d5432194939f | -2.95592 | -54.11498 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81a60634-bab1-3107-9066-ac31b695bbc4 | -2.79476 | -54.0938 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d837e5a7-031b-3a16-9d78-128cd3f81e62 | -2.46488 | -44.18244 | 2026-10-06 04:38:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac64cf95-8fb9-3f87-a0fe-e4ee054c8d3d | -3.05624 | -54.22065 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 89ca0992-b1ed-3d26-9964-6a102be52ad2 | -2.78028 | -57.67525 | 2026-10-06 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56147f68-ea4c-3597-b932-7951f96f4dac | -3.06998 | -54.25222 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5b474e11-ab88-350b-913c-1db95ef94f49 | -2.91491 | -54.10798 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76e5cb34-1d50-3484-b8f4-d3ab3502a2b8 | 1.86749 | -55.7687 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8be518a8-3b12-380c-a6eb-51b46643d96c | -3.22447 | -53.87983 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30fcde98-2dff-370c-b646-eafc289aa299 | -2.88801 | -54.15645 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 394ead6e-cea9-3176-8167-96ba95f6bf0c | -3.84175 | -50.98861 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eded33f7-de29-3719-a2ee-d7a78996491b | -2.87826 | -54.1306 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06610909-0c56-3616-b591-16982f4b2e6e | -3.11763 | -53.76018 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2723b865-171c-3ac0-ba5c-82d550010b11 | -2.79237 | -54.13827 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70633fb5-a8a5-3d4e-b3cc-a8776b75c129 | -3.08935 | -53.71087 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5fce307e-6adc-382a-9634-140a345ed66d | -2.93161 | -54.12029 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f05694-306b-3cbb-9b6f-e4316869c869 | -2.93387 | -54.13505 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0592bf24-993a-3077-8e6d-7feb646e0466 | -3.06312 | -54.14978 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 837174a2-2ff2-3c86-a354-b4180a6fe9b7 | -5.06893 | -46.10856 | 2026-10-06 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 437d2ee8-9cad-3e70-9940-cd97e0c18e0f | -5.97095 | -41.36557 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4b89031a-6b44-34e7-82c8-42c726311be5 | 1.7867 | -55.57064 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1defa512-c14d-31bb-96fe-5718f30e374a | -5.88223 | -43.46217 | 2026-10-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65dd09bb-a000-34bf-b91f-368d19073bea | -3.07368 | -54.25491 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f94cac70-75aa-3fd4-b56d-b1603c94563b | -1.62907 | -55.1315 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c529029-75cc-3339-a613-56ba2d66e6a2 | -4.45564 | -47.91751 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 63aca139-fd1b-3cc8-87d6-612ce8d558c3 | -3.07613 | -54.24336 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2fc9d991-3bac-3af7-847a-55a4032464c2 | -4.10908 | -49.3981 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ce39563e-c4e8-3f87-8333-b5993f7b83fd | -3.27996 | -50.01777 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3d54c97-452e-3ec6-b75c-ac4ce3abc974 | -3.67146 | -55.95155 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b086fe1b-ea66-3fa3-99cb-ee6ffa5c2e25 | -2.95364 | -54.15766 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9c2d538-a63a-36ee-85cf-4d2d269863fc | -3.68858 | -55.95831 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60aff227-9274-32c5-8fd5-81875d3f18ef | -3.67009 | -54.54844 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b342386-c185-3abb-ae14-37e902cf85f9 | -3.04935 | -54.234 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2c387ec-bc93-3ee6-9d76-9f15535ffa48 | -3.10059 | -53.7529 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8237728e-ff6d-30e7-909d-6deb492183ad | -2.56004 | -54.73547 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b12e9986-569e-389e-bc25-e59a2d468fcc | -2.06881 | -56.86221 | 2026-10-06 04:38:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cbde3987-5a74-3670-8af5-da431851a407 | -2.1349 | -56.70092 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb1bd45b-d7a2-3672-822f-d3004864570a | -3.05854 | -54.20654 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 434e3f3a-c96e-3e37-a8b4-489908beac91 | -3.01886 | -54.19033 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d05de092-82bc-3520-a76c-2498d5fa9391 | -1.50708 | -54.81042 | 2026-10-06 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1522195e-180b-3743-90b4-e4f934303cf9 | -3.6743 | -55.94954 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fed74f67-c6f5-3389-b08f-e6d5d8c32b36 | -4.14086 | -46.83527 | 2026-10-06 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcc5464f-5601-3d6e-b554-8668ca80f9bb | -3.01946 | -53.89553 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| c4f8ee5c-0be8-3e2a-ba3a-fd8189a9ce5d | -1.61497 | -55.12341 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc3c9453-339f-305c-a493-add0afc15659 | -3.98486 | -55.82101 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1acbf28e-405a-3345-9f24-22a89f91ef14 | -3.84258 | -50.32306 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f29271da-9eac-30ae-ad21-134cfba3a1cb | -3.09811 | -54.16529 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 511f90a2-3e85-3a68-b64e-2edc0d1ae52b | -3.09132 | -54.1783 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c17a2e73-6ba9-3b9a-9455-4892411461bc | -2.93007 | -54.12961 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14cf634e-5ac1-3417-acf7-9b6dd2f5a52c | -2.12941 | -56.69988 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba8f618a-9384-3a07-9f4f-ad87f98f6766 | -3.08069 | -54.24139 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6b15734-f99c-35b3-85d9-182ca81b8468 | -3.08896 | -54.16388 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eef30f3c-5f8f-3ed5-99c8-7d4ebae8301d | -2.9331 | -54.13972 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a96aed90-c47e-3ba2-9889-2f05b9f1b980 | -3.27385 | -50.40857 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a402669-7f36-33d2-b59b-b29fc4aaed7d | -2.04728 | -56.88828 | 2026-10-06 04:38:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c337fe1c-c314-32aa-8f9c-ef1e389e3f53 | -2.91568 | -54.10334 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5be4c48e-55f0-36d0-abdf-79069a403519 | -3.09163 | -53.72451 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8aa118ea-51e4-3f52-8296-ef4813816fb2 | -2.94374 | -54.1607 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ed4bd1ff-88b7-30bd-8189-ce19c5e6896f | -2.98937 | -54.11082 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ff20a90-ff74-3f96-ad68-90220063430f | 0.8234 | -51.61617 | 2026-10-06 04:38:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59c3ccb3-35df-3ee3-84c3-23d9193f9b80 | -4.35547 | -47.77774 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72d6caf2-be89-328c-bd94-83b10997eea8 | -4.05781 | -54.04777 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b47cdafb-6623-34e3-b1fe-631d2db9666b | -2.85723 | -54.14426 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4f53bd7-6b6b-3b77-8c44-c5ec16d4e2b0 | -4.07792 | -48.96116 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b25f8323-62d5-3573-991d-b3e378355208 | -3.23412 | -53.87687 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21309af0-7569-3583-aae1-add40c33e41d | -2.98302 | -48.5872 | 2026-10-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6562fcd6-3a46-3fa0-9620-2cc5e5887cbe | -2.94458 | -54.07006 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1aa9f2f-10fb-33a9-915b-8aaaeba56781 | -3.33281 | -53.38985 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72e0154c-e480-3657-8a4c-38dd37e5ea89 | -3.68045 | -55.94432 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc3127b8-c53a-3179-a9a9-2a316fb8cf37 | -3.8718 | -55.82196 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6ff7988a-ba47-378f-93d6-826430e3bc89 | -3.05691 | -54.24549 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a7db8fcd-9789-30c8-a4b7-4a8647e85cbd | -5.43565 | -43.44614 | 2026-10-06 04:38:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ae1f02d4-64fc-3b65-bb10-6c9cc592a408 | -5.66717 | -42.58079 | 2026-10-06 04:38:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cc0b009-a187-37bf-bb82-298501a89830 | -3.89701 | -49.71503 | 2026-10-06 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74eec74f-af42-3e32-91bc-f9ef6d7f4507 | -3.0976 | -53.74343 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 348251de-e47a-3065-a8c5-716c6ecbd01c | -3.92436 | -55.44568 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c60a095-ed7a-3a95-b9b2-e9ec328867c8 | -2.99093 | -54.13021 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9886541c-3b3c-383e-b631-98426b02920a | -2.92628 | -54.12418 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2660acf3-65f8-375f-bb0f-9aed60487c6b | -3.00797 | -50.47176 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 689f1793-5325-3d3d-93e9-957b5a6b7245 | -5.08925 | -46.04464 | 2026-10-06 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7791dd-d32d-33b8-9c8e-e77caa0e3a0d | -2.95746 | -54.10555 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 441c5cec-36ae-3998-84a6-d07303aae7e9 | -2.77955 | -54.10094 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 834bedae-b8b5-3887-9c91-34525a1e8f2e | -2.13429 | -56.70452 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e624bc7-0f91-3a8f-896a-94877fffc6f5 | -3.09714 | -54.17192 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ef1855c2-6a0f-3353-92b9-177da3c79a84 | -2.997 | -54.12162 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5e85af3-bc5f-31fd-bc7a-63e48ffb28d9 | -2.88776 | -54.15905 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 291d0b1c-8f7e-354a-92fb-e6e1ae169ac2 | -3.10576 | -53.74923 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b8306af-1b7f-3b43-add8-eba2d530665d | -2.57157 | -47.45704 | 2026-10-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d55b2e5-0403-3317-adc2-6643a2081faa | -2.94759 | -54.10865 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1222b36b-e34b-347d-a6b3-80d27fd41611 | -5.67071 | -42.58508 | 2026-10-06 04:38:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7552809b-23f1-3e70-9f56-d0dfde569a89 | -3.38245 | -58.20742 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1b917fe1-31b2-3dcd-99fc-3def8a788ade | -3.09833 | -53.73904 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb3533d6-4fdb-36ae-9c57-ed88834fc457 | -2.78325 | -51.67149 | 2026-10-06 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README41.md)
