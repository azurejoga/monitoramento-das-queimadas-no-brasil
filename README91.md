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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08626297-d7a9-3189-afe5-355a2efd4076 | -3.09644 | -53.74091 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dd35df0-5e20-32ca-8cf3-20fce0a62649 | -2.92869 | -54.1162 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a970b10-3d99-3c48-bdf0-cae1c50bdbaa | -2.99711 | -54.17945 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e30f32d8-a77e-3148-a366-62d8631c1de3 | -7.22516 | -55.08861 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff6c92a0-97a6-33be-8e79-bc8787475e41 | -2.79429 | -54.08709 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 471328d5-8a9e-3122-a5ef-e65931eec3d5 | -7.0005 | -59.1129 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d689181-49e4-3200-8362-592ff82a6f7d | -4.12203 | -59.87826 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 54fc70ae-0a45-3a4a-858a-0281d24b50ac | -3.01941 | -53.89785 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3154c695-2d39-3c12-8e94-d47e4b63f5e7 | -7.87844 | -54.99539 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2429e5e5-56c1-3a11-8543-4922a8c10c76 | -2.97983 | -54.05072 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2332025c-33ac-3ab7-acd4-f4f13f5b8107 | -11.21826 | -44.87079 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d02c033-81ee-3529-83d8-11581be5444c | -3.52105 | -54.66851 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0197e342-d363-3125-acbe-686fb68776b6 | -5.9676 | -55.34357 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86748abe-2705-32eb-987e-4ae4bcdffd29 | -4.45017 | -54.9738 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 114ab421-31fb-3a15-8779-1f4b7f52b98f | -3.10994 | -53.77313 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 420b68b9-7d8e-3728-824c-ef792e07525e | -6.47002 | -55.47792 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7705ef81-e8d9-34cc-8f14-33e55216d7ef | -4.29895 | -54.80572 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 70f4be4c-bd31-313b-aa14-946b0f5ce2ca | -3.17619 | -53.8303 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3fe10ba-2bb9-392c-b784-feceb560ede5 | -4.29833 | -50.78441 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db2922df-9220-3d72-a1bd-af5226ce596c | -2.89634 | -56.67646 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2dbdad9-9f79-3c3d-bac7-9588eec54992 | -4.30762 | -60.94606 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4804a68-7e93-3186-a725-573826218a02 | -3.43604 | -56.94086 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb80a171-bcd9-38a3-86c4-aed36bd5cfcf | -3.16201 | -54.73077 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62580ed2-d303-3ed0-acdf-7af39251025c | -3.07424 | -54.25777 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb1f58b0-36a9-3ce0-aa89-56b19bbf6c48 | -2.46162 | -56.06682 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23649253-beaf-3d93-a89f-48950163cdb0 | -10.42954 | -47.27113 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e936a674-f7f2-3731-ab8b-50a016bdf265 | -4.07087 | -51.04079 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e17d94d-fc62-3e53-86e3-81037d116772 | -3.3093 | -54.03165 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0ee5228-69cb-3d60-914c-9e5f4f74629b | -6.85088 | -55.78287 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86407e23-0a1b-3081-8a3f-785f47526e5e | -3.27564 | -54.03219 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8615f17-5e03-3bee-b1fe-74d361dfc9d6 | -3.06399 | -59.26673 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82902d47-d9d3-38df-ab18-6218bdfe99bd | -3.18395 | -58.65843 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0113bc2-41fe-309d-889d-fcbd69d5f75c | -3.4799 | -59.45995 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4778890-87b6-3772-8b0d-b6c9ff870d88 | -3.74782 | -51.21581 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a08e7fd2-cc43-3564-bf1c-50d49652cf27 | -11.06878 | -49.53853 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 184f1578-c728-370f-aaf0-7e874ccba163 | -4.28864 | -49.0864 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc181b5c-3028-33de-a936-1ae5f4ccf572 | -5.96835 | -55.36304 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c34d996-3f7e-3b8a-94b7-f2a1543703d2 | -7.18574 | -52.61698 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c6c2de3-b4f4-33db-b5e8-0d0526dcdda2 | -2.88132 | -54.19942 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f0932516-5c02-39fe-8fff-663e62973dc5 | -3.47149 | -59.57801 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b1f16f2-c873-38d0-96a0-4256033ad359 | -10.29006 | -47.99472 | 2026-10-08 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d21bd571-7293-386a-aa7e-a7cf5e8e55d4 | -2.77085 | -54.1151 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cce19809-6f2c-3a20-ab4e-04c5f9c08bab | -8.38315 | -46.2907 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a88b798-251d-3c8e-95d5-721b8bd396b8 | -6.2929 | -56.03823 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66679109-c708-3a67-8758-7d6f44c43139 | -4.10724 | -54.40974 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bce8604c-2e5e-3cc3-8545-cb57a24dfa0a | -3.70171 | -50.65879 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd1e4b01-00fe-337c-b27f-c01127e412e0 | -3.55228 | -59.47906 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fe7e03a-4cbb-3199-a4ee-3d7405941673 | -5.70423 | -53.49339 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 640f42ce-a448-359e-a314-ac4699da6382 | -3.08575 | -54.30529 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b00ae470-6f3c-320b-8f64-a6a436d2532b | -3.16744 | -54.74609 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5770da93-7b36-3b34-916f-3c2d177a7f43 | -11.00953 | -47.96497 | 2026-10-08 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4ce209f-c6c5-3bb1-8bd0-05c14961b7b0 | -3.10043 | -54.18924 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 292e5562-ef58-3c2c-8752-38316d5e5a18 | -5.76892 | -42.05342 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ef224ff-b312-302e-9ad7-8a72d6a5646a | -2.83559 | -54.12878 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6adce826-56d6-3619-9d32-9f240a2874b1 | -3.35221 | -50.48101 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 25a26113-ed3b-3e9f-b1d4-4d44b9da026c | -7.30427 | -46.19056 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e3e8ce5-2d72-3055-9ed0-6da0d86a0af4 | -3.603 | -54.56844 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ee33fee4-8964-3d6b-b1ba-0ec911556195 | -8.60209 | -45.64119 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa45a209-ad81-3c96-9d96-ef7a46fa2116 | -5.95235 | -55.34107 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 894f3526-02bc-3158-bd94-d26c067572ea | -7.21944 | -55.12386 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bc40c18-b892-3f02-891f-7361d1b6b333 | -3.44182 | -56.93301 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b16dfdbd-65a2-349e-afb7-7a923847d825 | -3.23065 | -54.37601 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c9dc38b-59bf-37e1-bbb4-75e022a4fd27 | -3.53755 | -59.50297 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f49f17a-51a9-3723-b15c-79c373bec486 | -11.71037 | -43.66138 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 388fde67-65b4-3973-825e-4d4d5c329479 | -5.73379 | -45.1601 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 466802b4-f874-331b-bacf-1bc7bc439663 | -10.08329 | -55.15998 | 2026-10-08 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84816dc6-0bf9-3f79-9cd4-47952c3d2b04 | -2.61551 | -56.48492 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b89fe1da-3392-306b-8c6f-5f15a27c9b9a | -5.72645 | -45.15076 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 31a588db-dc4c-308d-a5cf-8e5724283c33 | -2.99675 | -54.13402 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59f9a301-acd7-3cea-a73c-0b53f4fa6949 | -8.08576 | -55.29081 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 492e4df5-5758-342a-a45d-1cc7d8fab417 | -5.23001 | -50.89952 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c037d042-c8f2-33ba-8aba-ab8cd78357a7 | -6.43544 | -60.05591 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 332532f4-e271-3250-9d01-4d0cad14fc7e | -3.29747 | -53.86938 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 925799c5-f955-3c6f-8443-0db013012424 | -8.72629 | -45.16443 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 74b6857f-d1af-310f-9d95-e724ada3efe2 | -3.84929 | -58.89541 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e578749f-c1a6-3c42-9390-fe6cd6668264 | -4.07012 | -59.83844 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e9eee54-3aae-3cb8-b507-a3265ee0f52f | -3.36157 | -58.18872 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aef7474-13e1-331e-8bce-25978ce9d69b | -10.4222 | -47.26551 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4fb35a49-14ee-32c4-8bab-9369aa5df74c | -7.86225 | -45.4013 | 2026-10-08 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c656ede5-6a1a-3929-9d75-c8387d0e80c3 | -2.93195 | -54.1438 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47d6a194-703c-38ae-b807-5dc8be458d00 | -7.8974 | -54.721 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1d4b7dd-1042-3d29-a3d0-5e43311769e3 | -5.2976 | -60.10705 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a73bda6a-217e-3503-a72d-b11a77a72762 | -3.2224 | -54.29839 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 233fd396-ff72-3db2-9495-cf755b5e00bd | -3.42994 | -58.60294 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc05a83c-bcd9-3d8c-a8c9-bb85e2f72768 | -4.92595 | -55.85706 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32a33b1-ea0b-3abf-98a6-9833e7278f6a | -3.51952 | -54.65408 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f04d629-aa3d-3075-b2c7-a6c39e47a1f3 | -4.46316 | -54.89479 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0ee95ed-c38f-329e-8c3c-77b3de0351e4 | -6.34771 | -43.34255 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03ba2f45-e3fb-3daf-8f0d-404216c629bb | -3.10493 | -54.28077 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| edee6aff-87d3-3f9b-bcd0-852c1d604535 | -6.99071 | -59.1078 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af3d085f-1da7-38a9-9e12-1f1559ee69a0 | -3.05766 | -54.21872 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7be0989-4cda-3c0d-a1c4-38b6c32e257d | -5.03317 | -50.01903 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61873061-8fea-310d-9a9a-ef87d73d70cb | -3.34669 | -50.47313 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8f7185a-646d-350f-a9df-2565c60ecd4d | -3.36317 | -50.47567 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f29393e6-aaca-3ab5-ae93-2118b50d0b9c | -3.52029 | -54.67311 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e7d755e-791a-34a8-a8ae-08176d6961f2 | -3.28522 | -54.04108 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f69d2916-87ce-3851-bc82-996511fb6dcd | -2.98846 | -54.11474 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ca7b0279-4937-3f6a-b734-abdf2e0d0d76 | -4.09592 | -53.99375 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b39d007e-e213-39e2-989f-bb036f15bc45 | -3.31035 | -53.85841 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c616b893-c2bd-3592-9b1f-eff235365cb9 | -3.47027 | -59.58178 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README92.md)
