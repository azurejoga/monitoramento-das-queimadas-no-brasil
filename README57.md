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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea50b751-2ffd-3460-ad03-e7acc9e39c7c | -6.08256 | -57.70935 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 594898f3-e82d-3000-9de6-1d42566ccb70 | -3.16862 | -58.64756 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 45cca515-beba-3aff-83f9-2dcc559682b7 | -3.09774 | -61.15049 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba613ccc-88ea-322a-be7a-e3bebd7d10b2 | -3.38012 | -61.32125 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d6adf69-5075-3039-9866-9098a2d6b01a | -5.08376 | -56.25035 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b618c309-f9bf-39d1-800e-3b444a3507eb | -2.89528 | -50.42849 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e7570320-aa86-377f-80be-859cb8fba4d2 | -6.32553 | -60.01876 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d31a7ef-d5f8-389f-8733-a164bdc1c1b9 | -6.31208 | -55.27926 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ecf2f63-ae97-3fae-91cf-332f3923bd40 | -2.89124 | -50.43312 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6b115632-af61-3a83-8c06-029a39661330 | -6.29489 | -55.28988 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e82e17db-d050-393a-9332-35b27921fee7 | -3.18306 | -61.12094 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13062268-c471-3e76-8d77-999521c8b811 | -3.75766 | -51.1527 | 2026-09-14 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 87ffc9dd-0bb8-37e8-860d-00f765434dac | -4.12028 | -60.68215 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| fcef7d23-95b5-3b17-b34d-b3fa9d618825 | -2.8954 | -50.45167 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 933acb11-4004-3d0c-81b5-ec49665689df | -3.16986 | -61.20641 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f536107-3f2e-3c5d-9968-d8d20317440b | -6.6 | -58.86267 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f132702-3b59-3a00-9e4a-f4c4ee6f4398 | -4.11676 | -60.68161 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8add8d1f-ca3c-3ebf-afae-98d5b3389150 | -3.94471 | -59.3415 | 2026-09-14 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79be0e48-47ff-31c7-83f0-0786e4ecde35 | -6.29689 | -59.95432 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 970d5171-b718-3a25-afb4-7952ebc6b699 | -6.38081 | -55.25555 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34c7c331-daa9-3129-8ce3-1b664142a0ad | -3.17219 | -61.1231 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2336e272-9731-352f-9457-95b98fc7a505 | -3.11333 | -61.14072 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc637c4b-caf8-33d2-99ba-309b08d76680 | -6.58543 | -58.84967 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cc7f2ff-5377-3327-9d05-00bb0c2ed08e | -3.04123 | -61.2441 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28b24b5c-076c-3a63-a776-95a40313fbe0 | -2.90639 | -50.40014 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bcd2e0c6-b732-3f78-80a9-cc1246038341 | -3.72757 | -61.75357 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63244f67-8648-3e2f-bf8a-47d9084f4436 | -2.92051 | -50.4197 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5cd5496-9e42-33e3-a99e-deabfb811a9c | -6.11405 | -57.67566 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ff7a3d84-cb03-3c06-8a3c-963926fdae0e | -4.13086 | -60.68377 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b8b84b07-97b0-36e3-9fad-53ffab953cfc | -4.54078 | -54.93479 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c8880df-4dbd-3137-9577-ea4d3939dd82 | -3.74556 | -61.74895 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c85df898-713c-35a7-9848-09a33b75ac7a | -7.86667 | -54.7178 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f19b041-d5c3-3f9e-b35b-1b85d55e386a | -3.71448 | -59.29934 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa2975dd-172e-3aab-a15a-36113388480e | -3.31098 | -59.35603 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e9b6cbb-f3a8-3a72-b983-3ba9fadfbcf7 | -6.13788 | -59.88097 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71da4fce-7107-313f-af02-9c633a46627d | -6.58947 | -58.85027 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7db19f98-c51c-3b90-81e2-57b7032e8f8a | -2.8939 | -50.39212 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68fe2773-cec9-3474-8a19-0fad79a7f2ee | -3.53188 | -59.06963 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99b56abb-6aca-3a8a-90bb-6ca8263f8eb1 | -6.59141 | -58.86501 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6502086b-ed52-3f9d-837b-56820d4cdf45 | -3.745 | -61.75256 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68017a10-fe78-34df-a3b2-08c860873066 | -3.1679 | -58.65244 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d92c21a2-a939-3039-af7e-1bf05aa3ee37 | -2.9332 | -50.3794 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce8dfcca-ebdb-3030-8bc1-e03106d1dae7 | -6.10597 | -57.67027 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7c43b2df-dfca-345f-93ae-e92e38707da8 | -2.89039 | -50.43903 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de3cfe48-dcbf-311b-a6f2-25b966023056 | -6.2914 | -59.93961 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6b971396-4098-3657-affa-4f326deb7b16 | -6.59649 | -58.85855 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b273efc-d267-3801-86fe-6c047cd9cbcd | -2.70724 | -57.54436 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31afa7b4-0f49-3cd4-ba51-d0b8f2069989 | -6.31124 | -59.96108 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84d0c56a-f764-3c99-820e-2bc6870c3024 | -7.86621 | -54.72126 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e36afdb3-5593-3470-ba34-c3cad0fdca70 | -6.31974 | -59.98106 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fe5c45cc-367e-3e1d-8e66-29fad35baf81 | -2.8872 | -50.39112 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce9268a5-bd4e-339c-a98b-42b282959dc5 | -3.19832 | -61.36482 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d76fd3a-8a55-3d6f-81fb-9356efb787c0 | -3.83111 | -59.6563 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 473f57cf-54f5-311a-968f-fe80c367c2eb | -6.11094 | -57.66666 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3803b4e-dd3e-3e75-b74c-63795df434e1 | -2.67838 | -57.56698 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 146317bf-845f-3c93-94bb-17ecbd080677 | -6.91671 | -55.63629 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61dfc466-bc4f-3cb1-bb05-d97b2f2c243d | -3.54223 | -53.98471 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a030d8d-1292-3ec2-a83c-03d3df832647 | -6.29152 | -55.27643 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c6ae5ac-597e-30e4-b771-00dad3223d5b | -4.34836 | -54.77983 | 2026-09-14 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b30ec7c1-034c-3711-b127-56bd515d5ee3 | -6.64853 | -58.81839 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13bc7aba-5b0c-320d-ad8c-5c0248b99928 | -3.554 | -58.64627 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93617bcf-afab-30af-8989-d698d43457fc | -4.36667 | -55.03555 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fac9fd03-691d-34fd-b072-f184211d054c | -2.91552 | -50.40686 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7cdf756a-1004-3fb7-a6ac-2360aa16a6ee | -4.38843 | -55.20681 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b92f3991-98e7-36c5-bb3c-1555bbbe21ac | -6.31668 | -59.97591 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3274a0d0-edd0-3473-81b9-858a445993cc | -3.11676 | -61.14124 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56b5419a-20cf-38b2-b8b0-2e3bc6c1cfeb | -6.31737 | -59.97134 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb79a6a1-7d3b-3a4b-8a42-87fb36cc95dc | -6.85352 | -55.56956 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7de46833-74f5-3423-bffa-736aa0a053e3 | -3.17138 | -58.65117 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6a638021-a819-36e2-b988-e587ac3eb132 | -3.116 | -53.94803 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b371ebb9-f86d-31bc-a218-04b17a375b14 | -5.805 | -52.1135 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4075c2d7-5478-34ed-8e4e-48b66ae67805 | -3.53687 | -53.98377 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e594571-98fd-32b7-ad0c-10d1493665ff | -6.65995 | -58.88195 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec6dceac-8585-3860-966c-4ec23de25f97 | -6.28972 | -55.2894 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb3135cd-3c45-36ac-8a7e-bc47f41e805c | -2.88948 | -50.42159 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0d9db4c2-87af-3435-97cc-b63d2997c283 | -2.63703 | -54.75156 | 2026-09-14 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1a68fa3-a8a6-3cd2-b70a-71835b041ee2 | -6.30092 | -55.28418 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5499029c-8aa5-375a-b96c-f043e5505f88 | -4.77976 | -56.15119 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26176ccc-d24d-3680-934e-88f06671fbfd | -2.903 | -50.39875 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 863a1387-edc0-32ed-be1a-ae38df90ee04 | -6.28165 | -55.27203 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf72be04-670a-3efe-aa47-bf5007528cca | -2.74626 | -57.62344 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 827c2c67-619b-3a81-bcbd-97546807ad74 | -7.87116 | -54.72583 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9d1e573-4dbd-3e8c-8227-f2ba5af2b6e9 | -2.90057 | -50.36796 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a47f0c96-42b2-3352-bb07-e38403bb0821 | -6.28595 | -55.27884 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ec6711f-729e-3a44-85bd-dbfc41db85da | -6.1097 | -57.67506 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7dd25066-0302-3403-9712-3117e3c06ddf | -2.67693 | -57.56383 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2958e287-a6fe-36fa-8a2c-a1e4bc912375 | -6.59193 | -58.86148 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd36aced-138e-30d6-8cee-c4df3598246d | -6.67694 | -58.70811 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e28f9aab-90c1-31ea-b367-41e7b676f65c | -3.7178 | -58.86608 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59c47cd9-d8bd-3a98-9535-a5a14d4dcb4b | -6.31123 | -55.28534 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1022ad93-832c-3f19-9ed0-010be5a355ec | -3.52876 | -59.06436 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5f2d3e3-f0d3-3451-9bf2-629b648c0269 | -6.15248 | -57.69646 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c39b35b-a037-3e77-960b-b7f35e7f2302 | -6.07336 | -57.86254 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d71475b-3cec-38bf-b36a-9682fa2f42da | -2.70957 | -57.614 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd7d9954-2ee2-3982-a16d-6dfcf2d87b3c | -3.37671 | -61.32074 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c931b5b-da86-3773-a5fc-3a216c84ff76 | -2.90123 | -50.45856 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1059e14a-7a83-38eb-afd2-0ab2527fdca6 | -4.13805 | -54.01076 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ebf0125-c695-388a-aa53-be87bd9055f3 | -2.67635 | -57.56759 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5ca093b-365f-3e32-b710-720ccf2ed6b7 | -2.9014 | -50.36212 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0975ce02-72e3-39f1-9ed4-25a0a857b59a | -6.08677 | -57.86061 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README58.md)
