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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9af3ed0-b1b5-3585-a638-bb0dd5ee946f | -3.76859 | -59.40302 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3597949-c753-3217-b5b0-73d329732cb3 | -3.16022 | -50.59483 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffafc87e-858c-3c15-9eaa-1ba6f47049ef | -3.29409 | -54.05361 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0aa61b5-4977-350c-bd3c-983864c58142 | -6.4677 | -55.48218 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e75a71db-5537-336c-bddc-4534bac08cd2 | -3.29443 | -54.0158 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e811fbdd-446a-3f65-a09f-36835ba727e4 | -3.73646 | -55.48717 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7e9eb27-e16a-37b6-b788-c968471d864c | -3.58328 | -55.60299 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84216e1f-cc63-3fd6-a0cf-b0dd2c666c54 | -3.27322 | -54.04712 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5ba7937-12ec-39ce-b79e-01222b6f6977 | -3.091 | -54.29092 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7daba78-844a-3015-b3e4-ae6208aa1bae | -3.41029 | -58.90797 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55152c18-9664-3a50-afc2-0c247b8dbe47 | -2.87909 | -54.20145 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 78448c21-4671-3338-9acb-ebb506e410ec | -4.54242 | -54.98665 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e59df211-f279-3475-a6fe-45c10ea81722 | -2.71702 | -57.46433 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d90aa908-4f55-38c3-a62c-32b469c575da | -3.43272 | -58.5994 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c704044b-c687-320d-981d-0318fa0b0ec3 | -3.18027 | -50.55036 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b9fe5d2-c19d-3c99-8d0c-c7347174e557 | -3.4818 | -59.58214 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14c08291-6868-3bb1-b8f6-3bd37758445d | -3.84254 | -55.98999 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a7b040d-ce3e-30fa-96b9-968109218617 | -3.70657 | -59.65351 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed234c4f-2f8a-3be0-85d5-2eda003dc961 | -3.70339 | -60.55468 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddf7fca9-5d29-35dd-acdc-7e457b5ad8cd | -3.09236 | -53.93444 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd981da0-8299-389f-b0a5-7161a9e612d4 | -2.93444 | -54.04982 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11d78f70-38ef-3ee7-a078-1c70aa93d36a | -2.21971 | -53.70541 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c74efc1f-ff7e-3fb6-86a5-f25a20c43a66 | -2.99037 | -54.13972 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a80c9e34-919d-32d6-bd30-d02eaaffab6a | -3.06388 | -54.2569 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7dadba2-bd39-3bec-89cc-ffead5843fbb | -2.57113 | -56.17822 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cdba477-2007-379c-8af5-f7019cb402f3 | -3.45529 | -57.86132 | 2026-10-08 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f258fdca-7edb-3ecf-8a8f-ff631fa72136 | -3.51878 | -54.66811 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10b89c25-43de-38f4-b972-41ef83434595 | -3.27553 | -54.06781 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 875afe15-e6b9-3de7-b56d-276ef883e2c3 | -3.04105 | -54.26606 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06584ebb-e762-3e5d-a844-ce1677f138a5 | -3.29616 | -54.04015 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8810c1ed-b96c-3be5-bef2-0db41b668d23 | -3.29288 | -54.08413 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7fc8894-cc36-300b-ac7c-643a05d6dd3c | -3.17943 | -50.55619 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d248e69-256e-3fca-adb1-d50a75297753 | -3.06522 | -54.17477 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 649a6658-b117-35a6-a94c-f82e1355be72 | -7.22425 | -55.09042 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83c1ad57-a5e8-3b04-998f-50dcd3d41651 | -3.08517 | -53.96442 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| a72159e4-1dfd-3715-8bb9-40079721d60f | -2.50898 | -56.33412 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10cc23f6-5abd-34bb-aab7-c5e2dcc3b844 | -6.09087 | -55.72259 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a79f13e-2596-337b-8d28-98741ecf5f45 | -3.86614 | -55.97021 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 676d1268-6117-342e-a229-3e1ce1d7a906 | -4.05744 | -55.32476 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2552852-49c9-3d02-befc-a4dde53f43f4 | -3.28996 | -54.06674 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e28274f-44b2-3095-bb14-0aa0e00adaea | -3.43195 | -58.60439 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db9a04b7-0bd5-313c-9133-a048eb5f61a3 | -3.30738 | -54.69787 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de61987b-2ee4-3b5b-857f-c86fbdd5b3b1 | -6.30239 | -54.7938 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d801f7b1-1c8b-335a-9e8f-6fc93487744c | -3.08863 | -53.94073 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f25c469-8fd6-3432-beeb-f10e5e7f91ff | -2.03767 | -54.48546 | 2026-10-08 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7098fe4f-e082-34e9-bd64-998572558df8 | -2.92604 | -60.9918 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 719c2351-7c64-3a40-b6fd-dacf9e39fa28 | -3.70096 | -58.29153 | 2026-10-08 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91e7cef3-3897-3cfa-87b5-3f98d311dc9a | -3.29461 | -54.05025 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c4f2e05-f580-3951-bf76-34569cff65ef | -3.25857 | -54.6747 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1ae7b63-7be1-398f-b2d2-1738bed02cd3 | -2.86842 | -54.8859 | 2026-10-08 05:42:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 547c38e3-a4ef-3319-99bf-6cb17f7551ff | -3.50176 | -59.27794 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 381a801f-fdf0-3461-9f6d-eb0f9a3379d2 | -2.84933 | -59.11445 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af5c4641-b72d-3b14-8017-161fe0a6d664 | -2.75965 | -54.10347 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 128a9655-94d8-3c61-b61c-ae6356ad246e | -3.09867 | -54.27564 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41316622-3737-3aae-a803-0d7fa9562f65 | -2.49804 | -56.07386 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6d2d6c6b-3ea3-3ccb-81ea-59f8db93975a | -3.31972 | -58.23046 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28e1c51f-9afc-3dd8-b455-ad41e3d3d19d | -6.09588 | -55.72311 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dcd33aa-4bfb-345d-8138-888c0c30146a | -2.94243 | -54.17451 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0006e219-b7ba-31b2-a9f5-5d3800c66ce0 | -3.09988 | -53.77736 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa87d49f-eb46-3cc2-98b3-cde3a2537d48 | -3.16713 | -50.45189 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 48b73445-7738-3214-8253-31ddcb0360de | -3.10173 | -54.18351 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37fd4c41-a306-3f93-9bee-f2bccb12e816 | -1.83148 | -54.93143 | 2026-10-08 05:42:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42ac8ceb-e432-3c12-bba4-134f383805b1 | -2.99917 | -54.08077 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9f90c347-a142-3f6f-a741-87d8452b0077 | -3.66584 | -60.60966 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c998d0a-1c83-3c25-9d80-ced17cfaa2db | -3.11942 | -53.79467 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8212e582-93aa-3bb4-bc65-63931fdadc8a | -3.59697 | -54.67291 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be925f7d-d0a3-3052-81cf-b8c317b56ce9 | -3.0178 | -54.13724 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac602f9c-2a68-348c-8159-0c2a7472eed1 | -2.90551 | -54.0252 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77e7c6ce-dd57-3f0e-9682-c25eafdb249d | -5.33739 | -50.98949 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69e7af43-2c79-36a8-92e8-5ac36fb70b4d | -3.27986 | -54.07516 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1b8834f-608c-335d-94eb-bc04ed5a0d80 | -3.26484 | -54.06629 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48059469-ea98-3189-86d7-3a6d4cfd6f35 | -3.92896 | -50.34075 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| eaa23398-6954-38cd-bac6-1a7aa4b43d39 | -3.54096 | -50.10246 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1212134f-d2e4-30da-917e-aef24ba2a015 | -4.1388 | -54.03199 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 670329ec-bcde-3b74-a329-a556d42cbd93 | -2.22107 | -58.11182 | 2026-10-08 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d426e2e-1a98-3eae-b461-9dae8dad57df | -3.25872 | -54.03459 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e276df0-c580-3a48-86e4-aadd2e95f5f6 | -2.94062 | -54.15119 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0af9ae7-8f1a-388c-be22-fbe0708da2c1 | -3.02953 | -54.09547 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd5cc03a-2111-35c8-be57-58fca93c9d40 | -2.57851 | -56.16037 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d034ef4-3200-32d2-8923-88e79d4ffd90 | -6.48499 | -62.857 | 2026-10-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33ce7721-07af-3e9b-815c-5d3571714fbb | -3.50106 | -59.28251 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52b38bbd-b6b7-338f-b978-9824ed3c2263 | -2.98848 | -54.11606 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| afcf4227-ef17-31f4-9d7a-a1a071673493 | -3.0141 | -54.08981 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6439c2e0-01f3-3170-b9a7-665e78d9ed5f | -3.30181 | -54.70004 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6641b66-95d1-3aa6-bd39-57d50bab652c | -3.54211 | -54.65245 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 678aaadb-8331-3eee-bb1e-8e00d3772224 | -3.70917 | -58.93789 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7ff6647-d4fb-3b11-8bf2-312fee0f58a4 | -2.99966 | -54.07747 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d2fffda8-5159-3ba8-8a78-0656378c0784 | -3.65158 | -60.63168 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c1299f2-50c4-3c62-9aef-8c30059e4a61 | -3.08006 | -54.25646 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17a14644-67ef-3091-9578-98e185519f90 | -2.84702 | -54.12711 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d5edcda-c328-309d-b588-6f12adc31f50 | -6.98525 | -59.1114 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a6b7b3c-42ec-3ff2-9ac9-580f5bff988f | -2.76109 | -54.09376 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ac1de50-5f8f-3536-bd8b-305643006c57 | -4.06563 | -59.84378 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29200826-3ae8-3b08-bdb1-fe089ea31649 | -4.36958 | -54.75393 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a13540a0-5e02-34ad-88e2-9c4c56e66a4f | -3.54681 | -54.65631 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93041eb5-a2ce-3967-864e-9c59691ca4dc | -2.78273 | -56.50788 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac8815b3-9b36-3049-b289-15ee1dd8b106 | -3.04131 | -54.26564 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 171f3a95-5ba8-3499-9d16-ab9901d2f123 | -3.00005 | -54.11116 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb04869d-f00e-377e-ae91-7fcac268deb8 | -3.26036 | -54.66279 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57be0981-afc6-3d47-a6e8-320be1dbc05f | -3.9627 | -56.11244 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README179.md)
