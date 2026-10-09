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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2d28ffc-5f46-3bb8-8272-c03abaa7ad8b | 3.5577 | -51.28252 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f2f7b3-1c03-372d-8003-54aab154a712 | -2.04825 | -54.29714 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60591167-c487-3fb4-bccc-fe540bd5f9e3 | -2.75899 | -54.09356 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aade79e8-ed9c-3dda-979c-acd99e03c282 | -2.98698 | -48.91691 | 2026-10-09 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36483740-4cd2-35c6-83cd-728190ea5030 | -2.74538 | -54.11124 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f943bbd-2ed3-3573-a246-6ab3cb12ccd2 | -1.82799 | -54.99337 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 744ca508-fd2d-31eb-ab53-affd5859abee | -3.1549 | -50.59398 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d2130d5-e13f-3809-8f4a-7188a21ad41e | -2.63505 | -51.70187 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 821f70a9-8467-3a54-a5f0-9d99e5f54ea6 | -3.17446 | -50.44708 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9c8d6e3-08fc-30e2-9527-54f41dd1fd39 | -2.74166 | -54.13452 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4667bc32-9963-38e4-87b6-03c2793b229e | -2.50834 | -56.15939 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea09b54a-e6ff-37b1-a145-58900ef4f49a | -2.7802 | -54.07315 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b9cd818-3a0f-3c54-907a-e4293903a5cf | -2.76126 | -54.10188 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48755787-068d-3f93-8ba3-c25f7e8b8980 | -3.38232 | -50.41249 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bae83802-fbc0-3657-8f4e-937de8286b6c | -3.26019 | -50.40903 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0449332-036d-3548-a49e-bc169bb9dafc | -2.22035 | -53.69807 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ba67b0a-70fc-344d-a8fb-1b17049aed1c | -1.53607 | -54.53755 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec12ed71-cff1-3ea1-893e-22917ca99227 | -1.44992 | -54.77136 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa08ba08-7718-3d2b-a29c-0903781fba06 | -3.15546 | -50.59043 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc75d9e1-a1ef-38a4-92a0-d3a36b3f3279 | -2.73486 | -54.10956 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e52285b-6fc8-391c-8aef-9e9f4aec2c71 | -2.83275 | -49.51415 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 608acc5e-012e-3b11-b817-788b454f664c | -2.80039 | -54.0833 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6c23d84-a38a-3da8-b963-44e32984aee3 | -2.48407 | -56.13538 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aebf8be-eb1d-39b1-9388-9e29cf11bef4 | -3.36375 | -50.48363 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1daa86a4-9334-3341-8229-2883f9b514da | -0.04793 | -50.82426 | 2026-10-09 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa86dc02-1adc-3db1-9295-a325b90cd99e | -1.75854 | -55.28118 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3201ec5a-d3b0-323f-8d7c-2c1fa15a6807 | -2.8467 | -54.13034 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3fdc615-d1a5-31cd-8ec3-e55340ac59bf | 2.76879 | -60.00553 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c306cac2-d64e-3853-9450-10a6dbd14596 | -2.66176 | -52.57794 | 2026-10-09 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4bb7153-b5bd-3d55-90aa-b578c245a5eb | -3.16319 | -50.45271 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd736d80-5188-3cc8-b15e-c02ca08b8f76 | -2.73362 | -54.11732 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54431246-6842-3aa2-995c-4c1aa4b4ed5e | -1.62482 | -55.12629 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4278761-45e1-3701-acd5-969b94b70189 | -2.47191 | -56.06291 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a224cd75-8609-3ef0-8b51-cfdc81fc9b17 | -2.095 | -50.4084 | 2026-10-09 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc03f997-c320-3f4f-a74a-8a72171c2d5b | -2.4788 | -56.0941 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1705b382-2691-3855-856e-3168df8186f9 | -3.34408 | -50.41068 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6163eb5d-c354-340b-bd40-6e6ed1a94f88 | -2.78532 | -51.6722 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cf4ab21-f5d1-363a-b9b6-d13124f88c2d | -2.46947 | -56.07764 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b31a6f5e-41c7-333f-8bde-926e2fbdf2c4 | -2.59149 | -47.35489 | 2026-10-09 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d183eae4-1b7e-326c-ba2c-7de02c194045 | -3.16894 | -50.59253 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 693fad5e-6bf0-3c90-8a16-a9ba4517f243 | -3.39535 | -50.21848 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8449bb91-a975-3319-81b1-e92de7329813 | -2.34564 | -50.7931 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e4f5c2d-0310-3817-8974-ae995cd55f07 | 0.53265 | -50.89896 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37a0e64d-ffcd-3597-9c89-ae9ad97d8c50 | -1.77421 | -55.02048 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab3f135d-4d07-3bb3-845b-3f7c78babc1b | -1.43899 | -49.58769 | 2026-10-09 05:01:00 | NPP-375D | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11f3bdb6-6dc4-3e1d-af60-4b1c97cf60b5 | 0.52878 | -50.89603 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba8c9321-a6d5-3163-b1cb-ef0ee58b90a9 | -3.18689 | -50.54426 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5c82e8d-6e43-347b-a691-ab3452846208 | -1.21513 | -55.64395 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e94353f9-439e-3f55-b910-3a25e7bf4676 | -3.26643 | -50.39158 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 555835d5-d7bd-31a6-8891-ed1172536398 | 0.99046 | -50.02858 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c70b3b20-dd97-3f4b-9a1a-9d07b046c986 | -3.38854 | -50.21741 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5b33b37-6b08-39ef-a90b-84771fb9577a | -2.74724 | -54.09961 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a86a4e1-4f37-3c71-89d2-59ef4b6b501e | -3.20285 | -50.82593 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 44ec3940-a61d-344e-aeda-fedda2d6eb95 | -3.16164 | -50.59504 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d998f5da-8619-3945-9093-ea3eb8d3868a | -2.83334 | -49.51035 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5cbd5b2-ea84-3766-a33c-dc46e5df199b | -3.18354 | -50.58752 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13742c8e-e18d-39e4-b2f5-596d013113b8 | -2.51152 | -56.13976 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b91677c6-dfff-3015-939b-e35d09cb5454 | -4.08246 | -44.11988 | 2026-10-09 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02106156-84e3-3ede-a92d-5b378a019448 | -3.26076 | -50.40543 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99723e7e-1d28-3c2a-89b0-7e2c9c6ca186 | -1.42497 | -54.62309 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c8bf3d0-8963-3b34-bc33-45b739dcb513 | -2.51147 | -56.16494 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecbd1ece-f985-31e6-ba0b-c64256e64384 | 0.94246 | -50.20045 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ec2d355-07eb-3036-9934-411a641ab819 | -2.79976 | -54.08716 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 826db809-361d-3351-95f1-b76739f0cdd9 | 0.5393 | -50.89792 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40d487f9-3b1e-3811-97f5-aed9d196aced | -3.32438 | -50.1813 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 664d1820-6fe5-3249-8958-92acda2c43fe | -1.48229 | -54.52143 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 084b06fc-315c-3549-8e5c-68613ba99201 | -3.03428 | -42.1081 | 2026-10-09 05:01:00 | NPP-375D | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb1401b5-ec50-3fc7-9687-9362dac916b6 | -1.32974 | -47.95725 | 2026-10-09 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69eb6030-c6a6-36f1-b837-5f81829cf596 | 3.73106 | -51.62745 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66e725f7-90e9-35d4-bc79-09537bf60dfd | -2.73899 | -54.10624 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f563bf60-8bc3-3a1d-90eb-149af04f44a8 | -2.47178 | -56.06606 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daeca806-1990-3267-a71c-574934809423 | -2.34236 | -48.86928 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc59a39b-c36e-3578-9a10-4c531691aae1 | -1.90694 | -58.24663 | 2026-10-09 05:01:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f7433af-0123-3101-b515-16d0cc3957b9 | -3.25285 | -50.41158 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f5254d-0c13-3450-b53d-25b1df9929ed | -2.48128 | -55.7578 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8bfda08-6f74-3659-8f06-7e4c262cbf3b | -0.40276 | -51.78337 | 2026-10-09 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 582fb398-45eb-3ea0-bbe5-b1dcad73442b | -2.08153 | -46.57305 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 420812ed-6269-310e-94dc-c35589093b72 | -1.15398 | -54.22445 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb5dcfa1-303f-37fa-b309-425a25c0822e | -3.19364 | -50.54531 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe237f3c-cf45-3552-8388-5d0a6413d906 | -3.20713 | -50.54741 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2ae5df7-8060-3e07-bf1f-b099baf79e45 | 3.73052 | -51.64594 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742b53fe-870f-397c-9d83-45790b8c29e5 | -1.55085 | -54.56108 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4290db09-116c-35b9-9183-4fd198c46859 | 0.44621 | -60.5342 | 2026-10-09 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b531c495-6b6b-3c56-a1b8-1fb5c5796520 | 3.74294 | -51.61134 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba4e058b-bed5-370e-88af-2733bd39f5a8 | -2.75301 | -54.1085 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2c130eb7-b928-3d4d-a6a6-6122b1fccfe4 | -2.65841 | -52.57741 | 2026-10-09 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0c4ea64-af22-3fd0-b893-62a62cefe056 | -3.03374 | -42.11176 | 2026-10-09 05:01:00 | NPP-375D | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 950a5ae0-2f9f-3be1-964f-a58dbc9f2a41 | -2.75013 | -54.10406 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cf8ce4a7-013b-32aa-9abe-2a4d9f478b60 | -3.3469 | -50.41481 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7b0a9ac2-2c83-3565-9390-83e50ad2a87b | 0.92806 | -50.25233 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 669d9798-0f3e-32f0-be46-d7fa20b276b8 | -0.99899 | -47.6578 | 2026-10-09 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d5071c7-6d9b-302a-8c5d-6e38b950494d | -2.99055 | -48.91747 | 2026-10-09 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39b504ec-4df7-3ce0-9880-5f2112787b8e | 2.76931 | -60.00909 | 2026-10-09 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5049f3d-9eef-3935-913e-49b63a053047 | -3.39593 | -50.21483 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb70380-a5df-351e-a8ba-7f7b38e0db9e | -2.78597 | -54.08201 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10736f1d-a5e3-3d65-a551-0ebe66d7474b | 2.41892 | -50.82147 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 77dfceea-ca0b-3414-bbed-716e8e5b0d38 | -2.99871 | -50.29836 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24e50e62-3da0-38dc-9505-0186ab53b0a8 | -2.78809 | -51.67618 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 455ba3ca-b7e7-35e5-b713-9abf210d91c5 | -1.5279 | -54.51927 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33e81d9e-0de7-3b8b-b5af-f0c954ec30ac | -3.2506 | -50.40385 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README124.md)
