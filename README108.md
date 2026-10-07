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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc128f99-9fd1-35fe-9991-942d01c1aa91 | 2.43502 | -50.8499 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b51b92b9-e0a3-359a-bca3-b6bdea321846 | -3.44013 | -56.93657 | 2026-10-07 05:40:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51c1a496-95ce-38c1-9042-66e6d99ff2ea | -3.28947 | -54.03057 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1ad43920-28f8-335b-a1b4-9f2dcabae863 | -3.96996 | -55.81974 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9b92ee2-cbd6-33e8-934e-ebe05037bc09 | -2.90226 | -54.01664 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69dc8fd2-ed7b-3748-a91e-8f11a547cf12 | -3.22871 | -53.88673 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5c1206e-510a-3eb4-8b0a-3da99c2ece49 | -4.07237 | -54.04453 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7f11c52-8bd2-32de-ae64-2c6f0f7a12e5 | -3.17792 | -50.56221 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1cbeba4b-5b54-3754-85ef-720b00de2a28 | -3.56674 | -59.50163 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c830916-1307-3563-90eb-1e445a9742a9 | -3.29494 | -54.03308 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7913e060-72e0-3602-ab19-3cf61ca706da | -3.56721 | -57.80355 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ff8e96-5b36-34f1-8518-eda3c4b81d37 | -3.09383 | -53.71928 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9511b9c8-fc04-31f9-9f74-911667a6ba9b | -3.5013 | -51.6845 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77d30537-242e-3d22-8349-1304c37e47b1 | -3.18454 | -50.55878 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2136c994-7f40-39e2-a80b-3077c710b2c6 | -3.17492 | -58.64032 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 929465fe-a351-3fb1-bd15-030cae6271ed | -4.15745 | -55.15433 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f516d02-e96d-370a-8bd2-f6d72836e713 | -2.79113 | -57.66576 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e79d294-599a-33d0-a256-917baf5f4566 | -3.04543 | -53.9066 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e282e1f-61f0-3459-9a71-1b994b544b9b | -4.45189 | -47.92677 | 2026-10-07 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a7d4045e-39d7-3f59-bdf6-833316d78fd7 | -3.50509 | -54.65635 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9c37bf8-2a1c-37c4-8841-a4a04d77270e | -3.29569 | -54.02804 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 412fbf27-a5fa-346d-97f8-98cb978dfd4d | -2.42807 | -56.53378 | 2026-10-07 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2136f56-9fbd-3fcc-a009-79b6dc6c3679 | -3.28471 | -54.03673 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0778cd40-8dfd-38fd-afdf-af7dfe73513c | -4.11058 | -54.01863 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d7d1a0f-7b1e-3d4c-a852-5475e0d42c1d | -3.2927 | -54.04819 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4381f53-6ad9-3bc1-bb48-15b00f04b304 | 1.71248 | -55.62012 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc7b3366-b237-3d2c-b104-9e383569a4b5 | -3.28005 | -54.05989 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ae72879-38f2-3c57-93ae-5dde223af883 | -3.37873 | -58.19598 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9bd8624-ab0a-3c40-9ff0-d8d2bc1877b4 | -3.67187 | -59.63148 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14666667-4c7f-3e5b-922a-b9a240f7fba1 | -3.50521 | -51.69637 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37f6e3a7-0a70-3b1f-b2ed-879aacd454c6 | -3.53929 | -50.09063 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 313213ff-e2e7-3692-bea3-853daba343ab | 3.21775 | -61.05206 | 2026-10-07 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ccc7a65-58f9-32ab-9f93-434d7b658364 | -3.47675 | -54.62854 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa9783b8-af00-304c-b076-c1b7ee8309d8 | -3.49771 | -54.64305 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b331eedd-96fd-3e02-83e0-162c03b53864 | -3.51317 | -54.66451 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2331318b-6237-3fc7-be5d-54f183b39b8d | -3.74237 | -51.22378 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a94c1aa1-8419-3ada-b75a-1ff5e8a81019 | -3.27395 | -50.7927 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b2b20d1-e151-3d2b-a769-b5573c6e2cdb | -3.54099 | -59.46334 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 975f71a8-e188-3c6e-96d7-938c27c425c6 | -3.27206 | -54.01776 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2f4b9fe-3666-359a-8c7b-19c7d4b9fd03 | -3.08759 | -54.30316 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f8cb220-0228-3227-bbdc-11494b577dad | -2.77053 | -54.08026 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2d021988-e44e-369e-b35b-1a1c9cf9ab97 | -3.30041 | -53.86618 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85e9fda1-9ed7-3b8d-b699-d4efe5fb7837 | -3.34671 | -59.48008 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1664271c-dfe2-380c-9c38-da8c8bb5558f | -2.99265 | -51.05639 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7fde2a10-7739-3fa6-ad06-bedd61ff3335 | -4.3005 | -50.78529 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1a8caa3-785d-3639-9c55-3797ef7c52fa | -2.92865 | -54.13766 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39e89af8-bd0d-34ac-b873-e39fcd9b520c | -2.7896 | -51.67223 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5edc51c-b6b0-35e3-8f2c-11c8449dd6d9 | 2.4401 | -50.83201 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d332d6a2-fe1a-3c12-9ac4-7b6893510250 | -3.51987 | -58.75858 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea894da-10fc-3bbc-ab8a-7afa0621d9a1 | -3.38171 | -58.20072 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 134858c1-62cb-319f-acf4-e3dc9342eb36 | -3.55012 | -59.49524 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5df3f345-a5fb-3152-961b-874d411a81f3 | -3.51339 | -54.63152 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc69cdf4-4b1b-3030-af2b-16515026185d | -3.54385 | -59.46759 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4cbe4c0e-be8c-3007-9192-4918dfe34f09 | -3.50075 | -51.68814 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de777f23-df80-3ace-baaa-945ad83ba602 | -1.29584 | -54.56388 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7eb067a-aed3-3e14-8ea1-b98139eba570 | -3.68011 | -55.94131 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f482a3-2419-37e0-b912-e1c0cbf4e4be | -4.15368 | -55.14926 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bac3b81f-17c0-32dc-9261-540a2e633694 | 1.70312 | -55.63681 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c0410d-9a58-387b-9b12-923b9d29b86d | -4.12084 | -50.81293 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c4fa5c7-dee5-30bd-abfb-413af7a81b8c | -2.99326 | -51.05239 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92da14b1-7cc1-3375-91c7-81e15dcc01d9 | -3.10132 | -54.18204 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 784131d3-38e9-3166-88e3-6cbd759d14ca | -3.0207 | -53.87684 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e315fcc-7346-35d9-a2e4-fd2b97f63d19 | -3.09817 | -51.37831 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58f6cb3c-4745-323d-a4d9-09e015808241 | -3.54617 | -50.0868 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b44781bd-20c1-3edb-b950-d76c8d34d807 | -3.28121 | -53.83143 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38048ac7-b7c1-39b9-9560-5fedc91a67e9 | -3.11281 | -53.78343 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c5ca4395-9f63-341d-843b-1f2ffb17a568 | -3.07383 | -54.23737 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6dfaafd-ec8d-3b36-9b50-666f8c96e068 | -3.5794 | -54.31335 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26d236c3-99ae-3574-aa30-12731c7a2f3e | -3.50411 | -54.66286 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87547c79-5897-392f-9d7f-705c93878185 | -3.76513 | -59.32062 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b412127-d697-3d1e-bb95-5ea3753382b5 | -3.09091 | -57.6479 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eca7923-9f75-3dfe-9db5-611c7cb19d8c | -3.10069 | -53.76562 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| faecc03c-5bfa-37b3-8c2e-e536deeddd63 | -3.28769 | -54.0166 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0f9cddb-6576-3a46-beac-24cc2279c20c | -3.07631 | -54.25243 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef64b3f4-48fc-3a4b-bdc4-7c8e861f0a9a | -2.78508 | -57.65587 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ad2ebb4-3dd2-3cdf-b332-2ba4efc6faf9 | 1.89917 | -55.71005 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcf4843b-3e14-33f7-b0e6-bae52e58287c | -3.98588 | -56.21879 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93c20086-2c3f-3540-91be-ccaa3bb0cea3 | -3.63634 | -58.94038 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c73a4df8-880e-362f-9756-7067691fd3b9 | -3.51271 | -54.63614 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ba505ea-7afc-304c-b3fe-291d4735ac6f | -3.27128 | -54.02277 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec33b090-d657-31cf-9b13-441452b8aa95 | -3.08901 | -53.71854 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acd1615e-7d38-3122-a39c-5b4c9d32c6af | -3.97171 | -56.06095 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 663d14cb-58fc-3a85-b7d0-bec64aaa90e7 | 1.79984 | -55.53438 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcf6e5d2-69d1-3e3e-ab93-881fed8bf5cf | -1.76967 | -55.03376 | 2026-10-07 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62ee7039-af55-36e5-ba41-bde6d95b135d | -3.56381 | -54.48161 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d633924b-3870-34e8-b224-d86aa0c55847 | -4.08189 | -54.88667 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1bd0506a-c32d-3867-aea6-7bb48ba34608 | -1.28323 | -54.55746 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42cac2f6-90d5-390a-9b1b-3363ca59a5b0 | -1.6148 | -55.11442 | 2026-10-07 05:40:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c14841e8-7763-35d2-b0a6-093c3b22ac02 | -3.43539 | -59.62543 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6e98ff1-36fb-38fa-9dac-dd20c546d730 | -3.68201 | -55.95697 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4568331-099a-3e56-a885-36cca7e262d9 | 1.87188 | -55.73936 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c57fe44b-a9f0-3bd9-b1f8-f60e6949db92 | -4.16188 | -55.15509 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75bb2762-9fc6-39b3-8388-3e658557d5f8 | -3.55588 | -59.48091 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e850c52b-72ed-3104-b2eb-0e908a918b9c | -3.16906 | -58.63129 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 853424b0-6fff-3503-b53c-674e78fe0e57 | -3.00721 | -54.12479 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e14d0adb-c70b-390e-97c1-b395be89d44c | -3.06831 | -54.14702 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fd40894-5b52-355f-a9ad-d41d8c569393 | -3.10746 | -53.75869 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db144d8f-e7cd-3fdb-b5a2-b3be50ed7dd6 | -2.76687 | -54.10447 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 37b9f726-628d-3c9d-bcca-67502c6b1c81 | -2.44129 | -58.01752 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e39adcb-bcd8-3a2e-a0db-d6b5b4dfcec5 | -3.99375 | -56.24989 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README109.md)
