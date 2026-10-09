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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8e0014d-68fb-3446-9423-737db20888f3 | -3.7425 | -59.42196 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67260817-ba7f-31f9-905c-2832f6b08257 | -2.13458 | -54.46578 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2521921c-05df-372f-bf5c-0a7fd66a2796 | -3.77346 | -58.58665 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff066209-66ea-3d77-81cb-12fd3673e972 | -3.12346 | -54.17777 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bd689c25-316b-3848-9a6e-e3dd84a5b1b0 | -3.09113 | -54.28807 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b192744-8fb3-3cc5-b26f-be5eea0b743a | -2.83601 | -54.13662 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91b4730d-3fc6-38ee-96b0-5159793d60bd | -9.08459 | -59.48054 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bc3df3b-e604-3c4a-8ec1-ff2808b9d8c4 | -6.08359 | -62.51247 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50c14b32-f4f1-30e8-bf06-127f82b17a43 | -2.99513 | -54.18014 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ede32e70-0120-3555-a6f9-315e2d693f3f | -4.64064 | -50.96098 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3608371e-5820-3389-8bde-74ac2b988db0 | -2.93628 | -57.64911 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51f0240d-41ad-31a2-b8d3-285389541566 | -1.18716 | -54.18442 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 116d4f59-4f1c-341f-9088-96d75c8a933f | -3.0168 | -54.06248 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0cd595e-4d59-3e51-a89c-bdd22098edd0 | -4.3577 | -55.22942 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a86a0843-cdfa-342a-8ee2-dea27a62520f | -2.48638 | -56.13711 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 506336c3-0f67-3c82-8046-7d87d67516c0 | -3.78338 | -58.58821 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6270d12d-1645-35bb-ae9d-a6d58b73b3b6 | -2.63271 | -57.72194 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5a044d2-664c-3c49-80c2-13a847f3ab54 | -2.42908 | -55.98975 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53c810c2-0892-3299-bbee-b26f0a704ba0 | -2.50165 | -58.07912 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fbb5ea1-7261-33c2-b141-6cb69061cce4 | -3.51888 | -59.22552 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec777e55-c37d-3c2d-b0e9-174f2069103c | -4.93782 | -49.21859 | 2026-10-09 05:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 978e3d61-8189-362e-bcda-fbb5b35f5684 | -4.27054 | -55.71434 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ffd382-a4ab-36b3-a670-230391206034 | -3.69788 | -53.67282 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22d67d3e-254c-344c-a183-ebe79e236e05 | -3.4814 | -50.08921 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d63333d-a77a-38d1-b17a-cdfef2c42d10 | -3.01439 | -54.0523 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca2a88d8-6792-3ccd-a336-8b2cef90e17e | -3.00649 | -54.10473 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be3a3e55-fea9-3c36-a182-f08665d15976 | -3.05733 | -53.92548 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf01275-7527-343c-af85-764d6f804539 | -3.56927 | -54.67494 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f68200b-494d-3356-89ca-be2922928fbc | -4.5403 | -54.98672 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc31a7c6-b94b-315a-b320-27e5a7211bc4 | -3.08593 | -54.29677 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2416cb0d-6bfd-362c-a216-8b483e575d1d | -3.07223 | -54.28786 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68e777ef-c23d-3b4c-8bb3-5d41696d087d | -2.55332 | -58.03085 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5991306-2d4f-3925-92b9-f81fa11e51c3 | -1.50106 | -57.7453 | 2026-10-09 05:23:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4b6aa99-7cce-37ec-b597-03359b57e2f8 | -3.20331 | -58.00282 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23696704-445f-3132-8797-9b1d03e08e21 | -3.54767 | -55.5242 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fca29d55-bbe5-3b17-98db-b0e72c74fc1e | -2.97689 | -54.05413 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2007cec-8aa0-3832-a326-4120eb20f591 | -3.7369 | -59.47848 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d4c0b90-934f-3111-ba13-1d8bdfa11df8 | -1.15049 | -54.22421 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9899547-5620-3a71-8a27-80196850c995 | -3.01177 | -54.09584 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91694d60-beeb-3c8b-8f09-a216415d1cbf | -9.2968 | -60.53789 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde710e2-07ca-38e7-94ac-0319667aac6d | -3.57641 | -59.0781 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55f5c2f9-7635-33a1-bef1-d21cce56ec8e | -3.91251 | -55.89645 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8b99f33-8522-3a2c-becb-11b521806b1a | -3.04532 | -54.15917 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec1de042-f451-378d-b75d-0d5a1a5b6415 | -3.05954 | -54.21918 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8595e15-4eb3-3493-8004-5ccd64f0ae17 | -4.29223 | -54.80772 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5a88b54-7507-3573-a679-7e5b37608380 | -1.25669 | -55.75599 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac1fe3fd-9b76-39f1-94eb-892b01dcfdba | -3.57461 | -61.6105 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56c5e8fb-e457-3cee-bc79-6d765512e95e | -2.50249 | -56.1242 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a52cac58-fdea-3077-add5-0276c482cc2a | -8.54028 | -46.91434 | 2026-10-09 05:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66572f7f-49f2-382c-83bd-e54c0cb22948 | -3.02462 | -54.05164 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0decfd1-a791-391e-bba4-6e7eba4d5941 | -4.10492 | -54.02388 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3de70d62-be62-34c3-a1ec-536e1118177c | -3.74413 | -59.47603 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 565f4af4-2bc3-37ce-a614-8c53cbee6e3b | -8.76596 | -61.38362 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bf21c5d-6823-352b-9acf-9421e0efdf2c | -4.11131 | -54.6265 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 36e0209d-30e7-3211-b5c0-a8d03ff02857 | -3.67188 | -55.53266 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6231c6c-1125-338b-8588-1a64502d7b18 | -7.90473 | -54.71302 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d080e248-13cb-333a-842a-733804738232 | -3.09933 | -53.93689 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4bd98ab-bf76-3f63-b592-ee9024c45232 | -3.306 | -53.71281 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| afd33eba-c3e7-3c85-b9b0-74b7ba290c87 | -3.01558 | -54.10875 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe82ef01-78c3-32b3-9722-92342075cd91 | -2.62995 | -57.71796 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf38bd8a-319a-35e6-91ba-406f825c3194 | -3.04092 | -54.26378 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7052e6ee-80cf-382f-8e1d-c9ee5d6aa7ca | -3.02403 | -59.21879 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69f7822d-b3bd-3fb3-916b-732d52cc3507 | -1.20157 | -55.68676 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| feeb19b0-5906-3c1e-b191-7ea58844fb0d | -3.49247 | -50.49327 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| deaee4c2-2dc8-3237-ba10-930a002ec19e | -3.69841 | -53.66939 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6f420c1-b067-334a-83aa-bcc151707fbe | -4.52368 | -54.86181 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f619c8ba-bd4a-3663-8b01-09df32a8c595 | -2.77988 | -56.99899 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 238dd3eb-bd7d-38ff-93dc-1135ba2ba15b | 1.69348 | -55.61093 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6bd6e73-53f2-31b8-a44d-f2b729fc255d | -3.05418 | -53.91999 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28cb3c80-b29b-38b5-af9e-79aeb34a2dd0 | -3.08815 | -54.28563 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba9af933-31e7-3c3f-8aa0-5e6eb97dc9b0 | -2.56773 | -56.18042 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b5943cc-198d-35d1-bae3-f09e7b27a895 | -2.07581 | -56.87996 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 499f9d43-8b71-31ff-97db-33eeb076741b | -3.59012 | -54.67068 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4572b9a3-a4f0-3585-9925-9454909883bf | -3.38275 | -58.22192 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 011a0eca-06f3-3f68-82c4-7f8f4c7412b7 | -3.09321 | -53.95078 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de7fe7ec-fdad-3216-a779-b7d10eabfada | -8.7046 | -62.41961 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97769810-9221-32bd-82e5-02b612895cb7 | -2.8444 | -57.478 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbbdff8a-9b42-3da6-8bab-e42d22b0c68a | -3.29425 | -54.00037 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab0d55c4-587c-31e2-8557-9751382de35f | -3.18984 | -58.64577 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f66ba1d8-09d9-39a9-8e0c-2354caad88bd | -11.87662 | -47.38096 | 2026-10-09 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8defddc0-aeaa-349d-a7fc-84ced2f729c2 | -3.75846 | -58.51029 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89ad1653-5c4e-3d17-ac0a-e13f8c0f5c95 | -1.34184 | -55.46322 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 017a5bfd-aa84-33fc-b386-0701c1922ccd | -3.00097 | -54.10166 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17d1613c-876d-3d8b-a7a2-a12ef3f705e1 | -9.2101 | -57.72495 | 2026-10-09 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c341bc90-d495-35aa-9b57-51fbaf7f777b | -2.39436 | -57.89686 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4f730d4b-db92-36a1-ab9d-cec098c564dd | -3.05544 | -57.51831 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a48e46fd-399a-3f61-a252-399ed9cc452c | -1.33012 | -56.40201 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8ef22d4-47a0-3f25-8ee7-80fe9998f1b7 | -3.55428 | -59.43142 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 468db91b-8cd9-3c52-8a89-0b63abcb0a3d | -3.1719 | -50.44511 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37ae0364-69bd-3256-9776-d86c35e453e3 | -2.879 | -57.66857 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd7f1430-513e-349e-97fe-8185c2a174a7 | -3.89726 | -58.96301 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeb25d25-6fc9-3c14-8d7c-b4c8cec5a81f | -1.12832 | -57.2877 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00de8b80-a246-3e50-b6c7-ea1bb729d220 | -3.7218 | -54.21742 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d518d69-6f38-39e9-8bf3-9e20158f68d6 | -2.47084 | -56.06207 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3fc4091-83d6-31cb-917d-4a37fb00aab9 | -11.25688 | -46.27827 | 2026-10-09 05:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 682fd4e5-2518-3e32-85cf-915e45e79c99 | -9.00667 | -45.94513 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61fb2483-1a4d-3142-8cc1-8b34edd7b211 | -2.49406 | -58.08163 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5b791f90-debb-33f8-9f9a-a17f28122ec8 | -3.22914 | -54.29693 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa009eb7-26bb-3d29-b4cd-184fea2f65f9 | -2.85682 | -59.26371 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f42f1d6-f05e-364e-af50-3c89f1e09e1a | -3.35321 | -59.47915 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README191.md)
