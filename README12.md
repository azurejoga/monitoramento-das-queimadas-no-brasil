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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a1838d7-80ca-3531-9930-7e7b2d8042e8 | -3.6314 | -58.944 | 2026-10-06 01:29:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a64aa28-fd45-3dcb-8ef3-a4b43fa84066 | -3.4923 | -54.621799 | 2026-10-06 01:29:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2b6f1f-4057-3ff1-8f73-ed67f062576c | -3.0903 | -54.187 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 441f8346-dfcc-32d0-8e00-7b081418b9f9 | -9.5508 | -64.825203 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f45c5e4-df07-321d-a02a-dda08b212fed | -3.5828 | -54.3153 | 2026-10-06 01:29:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4929cb5e-5a9f-3a4a-9c7d-077ace652ad6 | -9.1073 | -68.309402 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce39a055-d69d-33e3-aab6-828f834530d1 | -3.6919 | -59.6451 | 2026-10-06 01:29:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 116bfb59-04c3-3832-bd2f-23ace7a2515b | 2.7998 | -60.632 | 2026-10-06 01:29:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d37c5c91-3d6d-3dc6-b02f-23722039f1d9 | -8.3514 | -62.831501 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ef2240fd-9536-3e4c-90b2-2c64499edc34 | -3.0458 | -54.215302 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 948d2bbd-e63b-3936-be47-1af4503b8418 | -3.5443 | -59.4986 | 2026-10-06 01:29:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6dc8a94-e6b2-31c6-a87d-a9ecc7be77af | -9.7234 | -65.102798 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 255a233f-0cad-3ec9-a9ad-4d97408af1c8 | -3.5425 | -59.490799 | 2026-10-06 01:29:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a51939f-f71a-30ab-9ad6-1f6c85f0d4b5 | -2.7761 | -57.6693 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad32e6f5-69a8-3fa0-9c03-a800cd9a2e9e | 2.0138 | -61.097599 | 2026-10-06 01:29:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 533d099c-28b1-340e-98ad-05effcb5f6f9 | 3.571 | -61.315601 | 2026-10-06 01:29:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| baeb5645-d03f-3110-8fb7-f0da581dad4e | -9.4925 | -64.039497 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a26084ec-46dd-38b3-9bf6-fad80958cb2b | -2.7808 | -57.689301 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20aa0a05-33d4-333d-8a64-58634e2990f7 | -14.9235 | -59.3979 | 2026-10-06 01:29:00 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 898056b5-84d3-306a-8131-ae8326745443 | -3.1143 | -53.776001 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77f7e814-1e4a-3337-87c4-5c49f6e8d71a | -3.6813 | -55.969299 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db6ddf50-65b4-316a-913a-e7d4c19c3620 | -3.2771 | -54.196098 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0fc45c-b604-37ff-b136-d540ae9f468c | -8.9761 | -65.435501 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91fae836-0de9-366e-8963-38b85fb905f1 | -3.0692 | -54.227501 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef778dbb-d6eb-365a-97d0-5dee9f779b81 | -3.111 | -53.719398 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb98399-09bc-3694-bf63-12b0d748a5b1 | -9.1445 | -65.409599 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf9eb2ca-ee80-345f-b660-b4ebe23eadb5 | -3.0969 | -53.703499 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27214c85-393a-3de9-a8a9-bf6a258ce3c4 | -3.5155 | -54.632702 | 2026-10-06 01:29:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7ca8ff4-7afc-397b-bda2-85d1ef991c06 | -9.4939 | -63.9519 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3984e4e1-f009-30ec-97ed-5fe3564eca6c | -9.5433 | -65.693298 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87f1a628-d876-36a5-9e8d-c8c914bc9e85 | -9.3429 | -64.7174 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 97a4b973-50df-3662-a648-f962a71cf15f | -3.0676 | -54.263199 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac4df05-5605-36ca-aadd-d9eaea25cd85 | -14.9121 | -59.3932 | 2026-10-06 01:29:00 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1dfc437-fcc2-3c1c-a038-d03180f1956e | -2.7761 | -54.116699 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ef3c0d-0dda-3fe8-9d20-5201bf369889 | -9.7116 | -65.095299 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0dda02e1-7345-3327-917b-c0352dd5afc6 | -3.006 | -54.135101 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff82994-34de-306d-81ad-7bceb24c3eba | -8.9782 | -65.445297 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc2af2a-276d-3cfe-903d-e7a77cb0825b | -3.6313 | -55.286499 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 665b2027-01ba-318d-8215-0423946d760b | -8.8499 | -66.800102 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53aed19a-3808-36cc-aafb-8cbf022a8dfc | -2.8661 | -54.150002 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7c74b44-f25b-38d2-b4fe-4a72f6ed1b16 | -9.4657 | -64.339302 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77f71088-f06f-316a-8ec7-d92fd82a0eed | -3.0821 | -54.153099 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e261439a-3d19-393e-a254-d427fd91a868 | -3.5303 | -59.393902 | 2026-10-06 01:29:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3147416b-112d-3f4b-aa46-5e5d1f02b54c | -3.6754 | -55.944401 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b743d6a5-3467-3b3c-9719-3541d7deb980 | -3.0724 | -54.155399 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b92dc22-0525-3a22-98cd-badf4d102f64 | -3.11 | -53.757999 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb014e0e-46f7-323e-b284-09e11c5cdb8d | -3.6783 | -55.956902 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8da59695-c960-318b-8f32-a6fff2c08fae | -3.0765 | -54.172401 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c33defc-1b7d-38cb-8b12-db9782f9d127 | -8.9684 | -65.447403 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e377425d-1745-3625-9191-5af78c5e237c | -3.0959 | -54.167801 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7aed810-291c-3b8b-84a6-5b5f391d780e | -14.8735 | -57.566299 | 2026-10-06 01:29:00 | METOP-C | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfbd4bb-22a4-3752-a292-8998d59440fe | -3.0773 | -54.260899 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007bd81d-50b0-320a-b2bb-508585957166 | -3.0918 | -54.150799 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17047594-84d9-38f4-a290-ca7d9074582f | -12.8797 | -62.153 | 2026-10-06 01:29:00 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b27f579-4002-3617-8fd1-ea4053d3aba2 | -12.135 | -63.167702 | 2026-10-06 01:29:00 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 018697d5-fa01-3d09-b9b4-c82bbc560d45 | -9.1159 | -67.719299 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfb1373b-f79a-302d-ad40-f4ec4f203d79 | -3.0709 | -54.191502 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b28b309-81ab-30fd-bb58-7a3646715a55 | -9.0168 | -65.719597 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72aeac08-6a1e-3b35-a609-45a0d26f9e53 | -3.1063 | -59.168201 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a29e6bea-f3ef-33ac-8e29-46734f4a7154 | -8.5165 | -67.008301 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3d7719-3bdb-364b-85a0-16cc981724a5 | -2.9437 | -54.131699 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50d4d5ea-6e40-3608-9bde-58b8a07efaf9 | -3.0806 | -54.189301 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c736a450-edd4-389c-b8cb-1b794099c22a | -3.1096 | -54.1824 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47247caf-7d49-32f6-afad-1ba4b55b641e | -4.4604 | -54.971901 | 2026-10-06 01:29:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50996dde-0b3b-3696-9d55-b2f1ab6872a1 | -2.9243 | -54.136299 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee58dea7-4d20-3746-9bc4-678c993af6e7 | -3.087 | -54.258598 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71deca4e-16d4-3454-914d-1820ec4a1728 | 3.5578 | -61.3288 | 2026-10-06 01:29:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1a220c-5880-371c-847f-42e87643d4fc | -2.9881 | -54.103199 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b729f934-a021-3478-90b7-5a73cb31229c | -2.8619 | -54.1329 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b40ed0e-a6f0-30b7-9315-ca3e7da80ce5 | -3.3739 | -58.196701 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd4da9bf-95a3-344b-84ab-31a5f9bdd373 | -3.7117 | -58.934399 | 2026-10-06 01:29:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39cb44f8-8537-35eb-ac4e-316f422ea56a | -9.7213 | -65.093201 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36672795-2248-3234-afea-7908b186df13 | -2.8855 | -54.1455 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0b5c3a6-2f5f-3c2c-a798-b2da27dff4f1 | -3.3319 | -59.4725 | 2026-10-06 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb9c56e1-d51e-34d7-82c1-30f29538b468 | -14.9105 | -59.386101 | 2026-10-06 01:29:00 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66dc32c4-537e-39f6-9cb4-32e094aa48dc | -9.7137 | -65.104897 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 558a979c-a982-3528-ad73-1074667f298d | -3.0627 | -54.1577 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179281bb-2411-3ce2-9577-29b965b34268 | -2.1361 | -56.698299 | 2026-10-06 01:29:00 | METOP-C | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7cb287d-9efe-360b-af08-3efa7d891be6 | -9.5488 | -64.816002 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f87fb921-d2e6-37ef-b7c7-c5a6d0f1b2b7 | -3.222 | -53.882401 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dad78397-ac1f-3a19-9ef3-d7e934f84b84 | -2.8799 | -54.164902 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba554f59-7080-337c-b797-e1b7e8544547 | -3.3781 | -58.214901 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c664bf7d-50de-3946-85d8-573127b4fecc | -12.6139 | -60.9034 | 2026-10-06 01:29:00 | METOP-C | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| adf93650-2bdb-3af4-aa7c-7b23013f1541 | -2.7835 | -57.657101 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa84167a-adfb-34a7-8d9d-52c8c5c41a9d | -3.0292 | -53.890598 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec26be2e-069d-3f24-aaac-8bfdf657c4e8 | -2.9825 | -54.122601 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdca5351-6f17-3132-a62f-b99b38c53dd1 | 3.5808 | -61.317799 | 2026-10-06 01:29:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6527bb18-36d4-34d9-a47f-87df1491c268 | -2.7785 | -57.679298 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0b9c460-c1be-365a-93ba-155f7583903a | -4.457 | -54.957699 | 2026-10-06 01:29:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bed6366-1807-3db6-935a-f7f33663d559 | -3.3258 | -59.490501 | 2026-10-06 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec202337-9cc5-3aa5-b96b-8af5db982623 | -3.7097 | -58.926102 | 2026-10-06 01:29:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15d10c25-b492-3646-9c51-58aa7d0939e9 | -9.4809 | -64.033302 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e83a32c-924b-30c1-9791-7c53bbcca019 | -9.1104 | -68.3246 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2eb5878-ee80-35ef-bf4f-53704ca9fedc | -2.8037 | -54.146599 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9a24c6-8bbf-3ad2-926f-ca692eb09e5f | -3.1013 | -53.721699 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3d685fb-798c-38e7-b585-a22c5f6df275 | -3.0999 | -54.1847 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9efe7cc-f9b3-3bc1-97ea-1540b0fd3f8f | -3.5523 | -59.488602 | 2026-10-06 01:29:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab3b26b-f3ad-3637-a865-f1779407b93e | -3.691 | -55.966999 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e8bb11-9e1d-3a4b-a0ee-2bbc28604078 | -12.1333 | -63.1595 | 2026-10-06 01:29:00 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2674ccb5-bb54-37b7-bc66-3bb4f949edfe | -3.0595 | -54.229801 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
