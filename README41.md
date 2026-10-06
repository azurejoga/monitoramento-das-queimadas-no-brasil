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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f800ad5-606c-3a90-ba47-f30ddb7b0592 | -2.93315 | -54.11098 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f4d9395-be8c-35a1-878d-3e189b613866 | -5.88799 | -43.45512 | 2026-10-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 368c202d-e141-35c1-adc3-61fc95757d93 | -3.15382 | -50.44676 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b66fad5-6182-3ddd-95b8-91b4d6b2a8b5 | -3.09207 | -54.17369 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1def3b33-7b80-30ce-8dd7-6690741d80ae | -3.68912 | -55.95518 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af8189bc-9a55-3c90-97d7-098efb20b2f3 | -3.77633 | -41.59683 | 2026-10-06 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b5387c34-3543-3408-b996-037e5f39b972 | -2.77347 | -54.10957 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43367a46-5c61-312c-b25a-2facd699d296 | -2.98103 | -54.1335 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bfc7dc6e-7c81-399c-82c0-7e68d422087e | -3.87229 | -55.81903 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ebf6f699-c093-3483-87f8-d1a727417708 | -2.88088 | -54.1433 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5679c893-e2db-3c1f-9f6b-4bff16fe62ae | -2.80688 | -54.13586 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a64bf69-000a-37ec-85a3-3c84213b81ca | -3.0761 | -54.24065 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d3e40e90-9e98-39ff-a118-e3d2d1f3589c | -5.40839 | -44.35211 | 2026-10-06 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd428cd3-d327-38a4-aa4d-95705249bcfd | -0.2287 | -48.95692 | 2026-10-06 04:38:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a85d9b4a-981d-3688-9b8f-48ee049b5287 | -2.78235 | -57.66294 | 2026-10-06 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 719c3257-da00-358c-ba05-b4a92b3efe43 | -2.90503 | -54.08033 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ab108a8-1710-303e-a746-d5f899b6dd49 | -3.13006 | -50.3414 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d86b2c4-46ee-3a6c-8c43-37dfbb794644 | -2.55525 | -54.73465 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 233f6d78-27bc-3a2a-918a-5427836c212c | -5.20741 | -48.33861 | 2026-10-06 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 908f1192-04b2-36f0-b773-e73ce4b23341 | 2.15442 | -55.95495 | 2026-10-06 04:38:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bd9fc83-d1e1-3893-bfdd-e21b1e4fe17f | -2.93843 | -54.13583 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 30879c33-f8d9-38a5-b11b-c5e5ad4dc02e | -3.06008 | -54.16838 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e36836d-be0e-3125-9177-4da05dbc861e | -3.0792 | -54.25357 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| ea90a4df-94f2-31e2-bfe2-44dfe8e74fe2 | -3.83744 | -50.30996 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc9a4151-b027-3da5-b677-0da80032114f | -3.0799 | -54.2461 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| fbab7744-466c-3f1c-aed4-8262112d4487 | -3.07075 | -54.24747 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2eb897e2-4a0d-3e59-8f3e-68c4c489e0ea | -2.77724 | -54.0861 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 796f472b-4389-3edd-8c3b-dc27d78144d5 | -4.507 | -43.69772 | 2026-10-06 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2600bb69-6578-3182-9999-2c848f0dc5e5 | -3.15897 | -50.4466 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07525ef1-12ec-342e-9bd2-e27290588d32 | -2.86181 | -54.14502 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 757f31d1-716a-35a8-a225-4dccbfde8812 | -3.278 | -54.18658 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a1700d4-2b47-330a-903e-4417e4229309 | -3.08864 | -53.71513 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5b4e73a8-1a50-396b-85b0-ccc454928acc | -3.49999 | -54.63324 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 32893126-d833-35fb-b27b-b14cc4bd4763 | -2.87707 | -54.13783 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de0cff2f-6432-363c-88d5-9a3e7eab214a | -3.37201 | -58.19656 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c22b075d-dfbc-39de-bd0e-19e2e808ac2a | -3.09101 | -54.18043 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00342e12-dcd6-3cf7-8f7a-de3f15879d10 | -3.12651 | -53.76165 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a7e3979-070f-3894-bb8f-e68af8cd8059 | -3.37722 | -58.20199 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4cd9ec9-9f8f-3293-8c45-f072588f3df8 | -3.84457 | -50.31092 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 127944ca-decb-340c-adb4-5d507c5d5219 | -3.15808 | -50.44324 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 568da5a0-228c-39c7-8afb-2fbb27d0b079 | -2.9955 | -54.13095 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b96db454-4340-319c-af18-d8c15fbd73d4 | -4.33382 | -50.40209 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 63944741-65d1-325a-be1e-7d22754c1237 | -3.22966 | -53.87613 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af329432-159d-322c-9d92-04aefcf811cb | -3.67836 | -55.95653 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75529891-6241-301b-b22a-c4641d58ee0f | -3.87374 | -55.81031 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40432524-dc28-3eeb-85c8-39c059c44886 | -3.15087 | -50.44207 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88c7baa2-1107-3d40-86cb-1d2ea3256d0b | -2.22255 | -53.71641 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0beecac-5f13-33f9-849c-d1871f0558ba | -3.16258 | -50.4472 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30be028a-b1a5-38c0-9cf5-9d130ba0eb6d | -2.87015 | -54.15161 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 289191b8-9cb7-3414-90c4-cf02e768a81b | 2.4609 | -50.84353 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b3842b1b-9d0b-3613-89b8-dc93b4d8396b | -4.33137 | -43.81174 | 2026-10-06 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 980485e8-c351-33af-b268-d84731c641d3 | -5.45789 | -45.52298 | 2026-10-06 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc1707d1-ed6b-36d4-a5cb-3c8f99a96c66 | -3.05931 | -54.17305 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7235d7cb-e858-3b61-9a21-de5de64f8832 | -3.27874 | -54.18205 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 614edc80-018e-3ead-a1bf-da357303a14a | -3.10359 | -53.76237 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 41343390-e5f4-39c2-8f4f-4cbe0bb6e404 | -2.79483 | -54.09544 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3e74d8c-77fb-341a-b3aa-688548d33c23 | -3.38028 | -58.20174 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1af23ff7-aa38-3f97-b577-ed3de6f54a75 | -2.87249 | -54.16626 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 60893130-4c15-3cab-82b6-f228c8d772a7 | -3.10707 | -53.71367 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d375c02-7377-3b69-a35b-d856ac1e5df9 | -4.05854 | -54.04335 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fe7cc10-347e-3799-89f2-bd62206e72fd | -4.05192 | -54.05567 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44b30c67-fec7-353c-8723-af7785ec1609 | -3.05166 | -54.21988 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c45ae35-397d-3b7e-9bbf-9db5572077d0 | -3.00001 | -54.13448 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 162baf72-4153-3b6a-9f3a-eee8ad25fd2c | -3.10264 | -53.71294 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72f87e50-e28a-3544-b060-20f61c2bcc84 | -3.60923 | -54.59826 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61a04a7c-28bf-30f7-a84d-38dca83e404c | -2.94223 | -54.14128 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 174181cc-a98f-3954-bc80-4e4ce6513708 | -4.2673 | -48.62943 | 2026-10-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15e6387c-d47b-3a82-a93e-57babfc20a0c | -3.10778 | -53.70935 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d5d6287-e2d1-35b7-8c30-1870b887b5a1 | -2.77422 | -54.10488 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3212d27f-c8bd-30bc-8426-be7755239da6 | -1.54931 | -46.59472 | 2026-10-06 04:38:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eeb9666-4c36-3ac7-a8c2-9d9020d3a3c0 | -3.07228 | -54.17996 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 148a16b8-cd62-3173-b8af-e3b681498931 | -3.08875 | -54.16599 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8034794f-a12c-3059-b31b-32b19fc147ec | -3.40083 | -50.3282 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1656a8a-ce2b-3cc3-aa45-6a8401e9d143 | -2.98862 | -54.11548 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e0d258e-410c-3b2e-81aa-42a0286d3a52 | -3.07996 | -54.24883 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 02a57822-2da7-3ed3-9ce3-2cded2a37a3a | -2.9369 | -54.14516 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| caa781a5-9de0-3069-8feb-0296acbac5bb | -3.46979 | -50.09864 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27f9ba0a-d12c-34b2-84b9-01687876a5dd | 1.86254 | -55.77319 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc95f37a-7c68-3ba6-9ce4-9933118aa2bc | -3.67586 | -55.94041 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98646821-234a-39ff-bfb9-3337f6c7bf7e | -3.13362 | -53.71807 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60b0c440-64ea-3b27-a43f-ecf1415b3d27 | -5.46826 | -41.24289 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df1ce8e4-cf6c-3a6f-a7d1-84083f06ccb0 | -3.08749 | -54.17297 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c7f0e66-9b61-3176-a68d-7c6a817e7f82 | -4.79287 | -40.04186 | 2026-10-06 04:38:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb54882b-100b-3e3b-94de-e64c517f8e86 | -3.06006 | -54.22611 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e0b43c2a-5a7a-32c3-b58d-c7c7f7e249ea | -2.83671 | -54.06898 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc281a5c-7841-3d65-b769-f4ec98a6b2f0 | -1.76363 | -55.03334 | 2026-10-06 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f984d74b-42f4-3abf-8b58-a731954dce27 | 2.12735 | -50.83847 | 2026-10-06 04:38:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4062a19-70ac-3a86-98ba-983065f68cdb | -2.89811 | -54.12425 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0b4c8dc-bdb6-3f2d-b1ce-608672b360b5 | -4.23516 | -49.98269 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aab9ccc2-be42-3adc-80cf-5efd320034a6 | -4.05336 | -54.047 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 353245fb-aa91-3094-a67a-625cea038806 | -3.27337 | -50.40145 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 69b5a40d-ff1f-3002-ae84-d7745c4c8455 | -3.49227 | -54.62181 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33c6b525-a716-3190-b47e-a9ec502af8ee | -3.95617 | -56.05634 | 2026-10-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d42bdf3-d858-3292-bd41-3e1cb9318244 | -3.10092 | -54.17732 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 665a46a1-da06-358f-b376-32595e34de79 | -3.50082 | -54.62828 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4cedd1b5-8183-32f3-816e-b1919f8f2132 | -2.79026 | -54.09472 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d649a38-4140-3da1-988a-3ffca6ad3e0b | -3.80522 | -51.03429 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 087f1aed-71a8-3062-9b8c-9369d90ad345 | -2.77498 | -54.10018 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ca7dbe64-a362-3577-8b4c-e9b2c4495008 | -2.93238 | -54.11564 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5098a8a3-56b1-31a4-9df1-38c1979c1a43 | -2.97644 | -54.13287 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README42.md)
