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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2d899f3-d9a2-3d43-ab00-e99f52997742 | -9.70237 | -64.5376 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a99e34ac-0354-394b-9505-00df187aeb94 | -6.97067 | -71.74628 | 2025-09-01 06:14:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a738eda-8a35-3212-8a15-246cc6f0f67c | -8.698 | -62.41648 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da0faf22-0636-3821-9629-573ee2f93dae | -9.07883 | -65.42879 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f6891b1-b277-31e5-b960-537bcd21d692 | -10.08757 | -68.46523 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b352e71-cc20-3f13-a759-6d398fc0b9bb | -8.23622 | -72.81312 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1d2cbdc-efee-3237-8070-51a34d3bcfc4 | -8.66115 | -62.92887 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f0c7e12-c4ab-3622-a18e-f39409386b4f | -7.27827 | -60.65027 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74a59a00-2302-3635-bfc4-6e11795d4117 | -9.07726 | -65.4286 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af8dc1ed-a1b5-3baa-bf92-33971ec517b1 | -8.09258 | -70.21751 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 593afcfe-49b8-3557-a0e8-8bdbd510ffb3 | -7.0645 | -63.05695 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df341430-e56f-3bf0-b55b-20a507e8abca | -8.66473 | -62.92289 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89e32caa-547a-3f2e-bc86-10999fbe51fa | -8.09561 | -70.22237 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78820bf5-8960-324c-b9c8-d0a834c83099 | -8.44387 | -70.14005 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbf43fae-5994-385c-8b03-3969ef3b7c55 | -8.75845 | -61.43188 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c9ac0e5-a0db-3b99-b3ab-b3d60be4c8a5 | -8.7657 | -61.42719 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcb0859b-66b5-361a-a42a-a0c8aff1e2e5 | -8.24567 | -72.81821 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ec4e499-84bc-3f9c-93af-f5a24379f898 | -8.64355 | -62.83196 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 231b6320-438c-307c-8518-57c98f3a3cd2 | -8.64919 | -62.92746 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5abfbaa0-562d-3718-8c70-71c7e1ebba45 | -7.88393 | -72.87333 | 2025-09-01 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 202952e3-1e2f-381c-b79d-53e2011293cf | -9.28091 | -67.64759 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6e63842-3420-308b-8144-752a9d4a4af4 | -9.07218 | -65.42786 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9800d5d9-de03-3a8d-9cd3-faaa0919900b | -8.87502 | -71.39575 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33884816-7801-3324-9cc1-5e2b78cfc5a2 | -9.08156 | -65.43529 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbb1a1cd-ac74-3ce6-8422-c76abbd8603f | -8.4156 | -70.72665 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adf89301-9263-3392-b889-78c7a8e9815f | -12.43994 | -63.92855 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f22d3cf-239c-3832-8808-a826de41adbe | -7.58974 | -61.63065 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8eca2660-10d1-35f9-a24b-0a8d5f787665 | -7.08519 | -63.03481 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 850a1572-6dfd-3ff9-ab49-04141ccc19a5 | -9.13838 | -65.8536 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f854e51c-dc4b-32e4-af9a-fa2b509ee0fa | -9.95886 | -66.87077 | 2025-09-01 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2637f20-c16c-38aa-9ed0-b85d9421b115 | -9.8832 | -65.02045 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50bf54d3-139f-3865-97ac-3314ee0f339f | -9.84195 | -65.05477 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cba42d3-3ac6-36f3-88bc-14790e297107 | -8.96774 | -65.97475 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d11d0bb2-f122-3b53-942b-fd4db9002445 | -7.68092 | -61.08266 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8fa8131-041e-3d16-9510-bf9e9ec060d4 | -9.0695 | -65.42136 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b36abfd-bddb-32e8-8216-6bb63170b89b | -7.60593 | -70.2011 | 2025-09-01 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3eb6d03-0274-3b11-bdd8-165b4c094e1e | -8.84316 | -64.15619 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dadf5906-5141-3717-886a-cc2ecefded64 | -8.23106 | -72.75805 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65129968-9e8f-32af-8c07-653bff572d8f | -9.024 | -70.66114 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79ea2075-2e47-3df1-8450-1f1e97655065 | -8.75776 | -61.43742 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bd1408b-3443-351c-857b-151b589eab3c | -7.46168 | -70.14135 | 2025-09-01 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 213e6797-c287-35a7-a0f7-8df46bda253a | -8.24512 | -72.82173 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6fb1232-8054-3e2f-80c5-36bd01603a96 | -7.81179 | -71.95132 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 200a117f-114f-332c-93bd-3a1e81e9df3b | -9.064 | -65.42365 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 624d7af2-0559-3ddd-948c-fa6d2e7585ec | -8.6677 | -62.92532 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8da2c2d4-9082-33f3-964f-46f40b7bfa9e | -8.7314 | -62.39357 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15b310e1-29cd-3053-8a9f-df36e9aff4f7 | -8.75485 | -62.40693 | 2025-09-01 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91357881-8900-3386-9967-b6ddb818f1c3 | -10.5937 | -44.331 | 2025-09-01 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ff6d82cd-a504-3e84-bbeb-29ac0fc90b60 | -12.8625 | -48.0545 | 2025-09-01 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6586a056-04a0-3bff-ad9b-ae47880d589b | -11.0568 | -45.146 | 2025-09-01 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 298.7 |
| 37357944-b26d-39e5-be34-ee275d542c29 | -11.0454 | -47.029 | 2025-09-01 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1e6ef46f-beb0-31cb-8b99-00b04bf60093 | -11.0461 | -46.9842 | 2025-09-01 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 8634c9f2-80ce-36bd-a321-f1bb7fe5036c | -11.0572 | -45.123 | 2025-09-01 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f9b22553-800e-3e7e-8822-5ea9bd177e31 | -15.7116 | -48.8809 | 2025-09-01 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 96f693ff-ff57-325a-b7fe-884cf32422ca | -10.6131 | -44.3051 | 2025-09-01 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 79233c42-c47f-3bdb-aa66-311bd1799bdf | -11.0373 | -45.1717 | 2025-09-01 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ee343f4a-ee64-3912-b053-f1b4eba028b0 | -10.6128 | -44.3284 | 2025-09-01 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| ea370c05-f157-3ea6-b8e6-7c6171bce5d9 | -15.7289 | -48.9892 | 2025-09-01 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 5639d15e-1742-31ce-b85b-e4ea18e1ce6a | -15.5862 | -48.3435 | 2025-09-01 06:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1f69b3ca-8a0d-33b0-8df7-86a96e9feace | -11.0565 | -45.1691 | 2025-09-01 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 768b8ca5-8c64-3fe5-91c1-13937d4b8581 | -11.0457 | -47.0066 | 2025-09-01 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| b8a1465a-2c34-3de7-b52c-c1318320e93a | -7.076 | -44.3376 | 2025-09-01 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bd3a6fb3-dfc1-316c-9637-bc765c82a2f8 | -15.7112 | -48.9032 | 2025-09-01 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 74afe993-56f5-3cf4-8564-05fa9b75ae98 | -7.0948 | -44.3358 | 2025-09-01 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 36078513-14ed-3afa-8db4-5f929605a76f | -11.0381 | -45.1256 | 2025-09-01 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 555c87ff-bc03-3673-a9d0-4b4f1c994496 | -11.0377 | -45.1487 | 2025-09-01 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 9c22f33f-c395-3d78-941a-f2ac2ae8f155 | -15.6058 | -48.3402 | 2025-09-01 06:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 67230f34-2850-39ea-8a34-f4df67c452d1 | -11.0648 | -47.0042 | 2025-09-01 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2e54d482-4615-3e68-abc1-65a3cd9d8d7d | -7.0948 | -44.3358 | 2025-09-01 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0d53370c-ff1f-3c8f-b210-dd0c8594e1c5 | -11.0572 | -45.123 | 2025-09-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 52e2008b-3435-35bc-bdae-70a26c0f7025 | -7.0946 | -44.3589 | 2025-09-01 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a3a4b82d-d228-3c79-84f0-688ecd6e4ba7 | -15.7112 | -48.9032 | 2025-09-01 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 7cef2bb4-67fa-3c78-8c2b-e86ca32570dc | -19.966 | -50.4197 | 2025-09-01 06:30:00 | GOES-19 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| 082821bd-551b-3c0b-b50d-caefa42571cb | -15.5857 | -48.366 | 2025-09-01 06:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 821bb6ce-ed41-3e2d-bc28-0902cc3f3c30 | -15.7116 | -48.8809 | 2025-09-01 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 1c606a4c-3449-3933-bf0c-cc9f15970d80 | -10.5937 | -44.331 | 2025-09-01 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7bab9762-bb70-341c-943e-08bfb98bb06b | -7.076 | -44.3376 | 2025-09-01 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7bb496f2-bd3e-34e0-acdd-840e9c828667 | -15.5867 | -48.321 | 2025-09-01 06:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ec8c5ab1-9037-3828-98e1-97c242fdd1b5 | -11.0377 | -45.1487 | 2025-09-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 319.9 |
| ce0c56fa-6f15-3a15-918e-d0cb16128a7f | -10.6131 | -44.3051 | 2025-09-01 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f2c56b8b-29d5-3dd5-af72-ca83baf2dd29 | -10.6128 | -44.3284 | 2025-09-01 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 63f0e5ce-6a17-36ce-94b4-4bd272c1c12a | -11.0568 | -45.146 | 2025-09-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 274.7 |
| e11860aa-34b7-378c-86f9-718c90f45db5 | -15.6058 | -48.3402 | 2025-09-01 06:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a8016406-00dd-3cef-a256-9c6dbd18ffc9 | -10.0434 | -48.0998 | 2025-09-01 06:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| ad41b563-26d3-39b4-bc3d-c8a477ecc19a | -12.8625 | -48.0545 | 2025-09-01 06:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0a6b9006-0525-3cee-a271-470808a97c2b | -15.7289 | -48.9892 | 2025-09-01 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 63c8647f-63aa-3ac7-87bb-bac63627c505 | -11.0381 | -45.1256 | 2025-09-01 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ba163b15-0c54-34c8-86df-bf53e9cd8f68 | -15.5862 | -48.3435 | 2025-09-01 06:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 2df7064b-27ba-33a2-b0ec-3715f5b45fc9 | -14.4153 | -51.6703 | 2025-09-01 06:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ee551201-047e-325b-b079-00ac1e93df48 | -11.0568 | -45.146 | 2025-09-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 278.2 |
| d12a7352-f892-33f4-a374-d5e7ff1cb252 | -15.5857 | -48.366 | 2025-09-01 06:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 73b4f422-f12f-34ee-9d02-05e0710ead21 | -7.0946 | -44.3589 | 2025-09-01 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 5f0e4023-48e6-3909-b822-f19c88b026bf | -15.7289 | -48.9892 | 2025-09-01 06:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e894a519-2fd2-30de-a942-964fea1fccd4 | -7.0757 | -44.3606 | 2025-09-01 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1ffcfb68-4cd1-364d-aa1a-1ad85702e36e | -15.6058 | -48.3402 | 2025-09-01 06:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 06f9d457-d8b3-3ab2-9558-9f9833c9b2f1 | -7.076 | -44.3376 | 2025-09-01 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 612286d5-1952-385f-843d-a785b65e3b4b | -12.9197 | -56.9471 | 2025-09-01 06:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ac694774-d135-385a-b18c-e42fde1f111f | -12.9194 | -56.9672 | 2025-09-01 06:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 66255d3b-e961-3da6-8664-d238bf6fac15 | -11.0381 | -45.1256 | 2025-09-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| ce0269ae-a643-37f7-b680-4dcb10bfc170 | -11.0377 | -45.1487 | 2025-09-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.0 |


[Clique aqui para ver as próximas entradas](README97.md)
