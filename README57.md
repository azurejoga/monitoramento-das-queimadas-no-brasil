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
| 5547cabf-a1e1-3b94-af5f-8047a542347e | -8.0681 | -49.6951 | 2025-08-25 05:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c4feaefe-2056-3569-813a-8c8967c560ba | -9.0416 | -65.7163 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 97c211c7-1dbe-3e39-a30a-93dba8b12249 | -6.8413 | -58.9552 | 2025-08-25 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c130ef34-a92b-364e-a5ba-c8128cd0ee00 | -9.0061 | -65.3813 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 9b9a49a8-c76a-3c28-a4e1-0f7eb806807b | -8.9875 | -65.4006 | 2025-08-25 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6a5d9ba5-386c-39f1-acd6-a20030dbfcad | -6.8229 | -58.956 | 2025-08-25 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a156110d-b973-3ed0-a44c-1cd170409d12 | -5.1181 | -43.1964 | 2025-08-25 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1fe3da17-b3e9-332b-b77c-d1a866e5ef8c | -5.10618 | -43.21652 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e9db1fcc-de5c-392e-97d2-735ae91b9011 | -5.10753 | -43.21409 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c3148f10-d85f-34cb-b7c9-0a5408c13b9c | -5.65377 | -45.14467 | 2025-08-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c594e69-4de6-3698-949a-e2269b9d0a8f | -2.82662 | -59.23433 | 2025-08-25 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc070292-e8b5-3304-a64f-0fb43e1e0d96 | -3.83849 | -55.97309 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b77875c5-2976-3fc3-9fd2-7f3eab8d7e45 | -4.049 | -56.31738 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b247d40-b4db-3557-9296-7ac704bc1d39 | -2.26273 | -47.85454 | 2025-08-25 05:01:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b29dbf-152e-31c4-8415-9df191981089 | -3.58624 | -49.42677 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e34e46cd-c248-312c-bbd6-5223bffa0a29 | -3.83904 | -55.96961 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c77b9af-8e5a-380d-aec7-08d33a864418 | -5.10772 | -43.20537 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| fa467088-fe63-39a2-8e69-94fdd20b349e | -5.6532 | -45.14886 | 2025-08-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54fd9975-46ff-35b3-8341-15fbe7fcf45c | -3.43587 | -49.05105 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d0aed2e2-dd92-32d5-bdd9-56b0b771d607 | -5.11353 | -43.21179 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cb4b8f82-3bcc-3b23-b65a-b55186ab7adf | -3.93439 | -55.75388 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fae6db9-4666-3894-81d5-8cdb50cafa1c | -5.29895 | -45.2703 | 2025-08-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 82566e64-4dd2-385b-9d5a-7a3c7b4e2b1d | -3.42717 | -49.04976 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e5b5030-fb58-36f2-b2dd-47ef5c195f8b | -5.10092 | -43.21347 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 2f337080-14e3-3f27-8b3d-c0a3f6c9a80d | -5.10172 | -43.20793 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 1d8d1653-0a33-351b-b2de-d5e95cced1dd | -5.29953 | -45.2663 | 2025-08-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 684d98f3-fe65-3b71-9736-439b80bb0f1d | -2.88911 | -57.32547 | 2025-08-25 05:01:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77958b12-abe7-3d2e-8fba-53aef87acc22 | -3.82502 | -54.11477 | 2025-08-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cbb1919-04a3-332f-a425-ce367942fa77 | 3.83555 | -60.90863 | 2025-08-25 05:01:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b3254b3a-ab1b-3341-b398-0c4f353d6e27 | -5.65487 | -45.14327 | 2025-08-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81e9583b-c013-3480-aace-122ee74ca6fb | -3.59049 | -49.42741 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e906c8d-193a-30c4-a65f-0966e16906f9 | -3.93715 | -55.75787 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c7b7833-d119-31eb-9fed-a66ebb3d822e | -3.73275 | -48.93066 | 2025-08-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53381b76-a138-3e9c-8721-0c1dc828ccb2 | -5.65427 | -45.14742 | 2025-08-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b9b4874-3a1e-36e5-9998-e2a52fbd953a | -3.79441 | -51.18798 | 2025-08-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7327164-9cc8-313b-9c9f-78d44ef895b8 | -4.30934 | -48.09914 | 2025-08-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09f4190b-7b3c-32d0-895a-2f2f31f3c9e8 | -5.10695 | -43.21099 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 87e869e6-b2f7-347d-8cb0-759e681ee4a3 | 1.03271 | -51.18967 | 2025-08-25 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eed5be1d-46a9-3988-8d24-ab429ffd9506 | -3.43152 | -49.0504 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b17a0baa-aa7e-39cd-878b-d873e17d85be | -3.9377 | -55.75441 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13cc3754-6096-3cc9-a71b-8b0c07410b3f | -3.45776 | -43.34696 | 2025-08-25 05:01:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc867658-66b7-3b3a-a740-752a00f111b3 | -3.21353 | -50.58777 | 2025-08-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c61877a6-d2ed-3c75-aa99-319abce9b245 | 1.10439 | -60.47673 | 2025-08-25 05:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6b4fad2-5570-3f7c-bf7f-c438ffbff0f6 | -3.7982 | -51.18858 | 2025-08-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e546755f-78ce-3e08-9857-1858f5513409 | -3.82837 | -54.11526 | 2025-08-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b6caa9-165e-3ea3-a7d2-ec549978f468 | -3.59722 | -47.52731 | 2025-08-25 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d28df738-ede9-3128-89af-ee9a4b21e4c0 | -5.93974 | -44.14142 | 2025-08-25 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b0f639f-8876-33ff-89cc-e05765c0781c | -5.10033 | -43.21038 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1d0c2f6f-5811-3ad2-a7ad-e928172b42cb | -5.10834 | -43.2085 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 464e87a3-e8ea-3b1b-958f-d9ea6934e854 | -5.79614 | -45.39967 | 2025-08-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de7a4c75-8ec3-3d39-96ee-e0e32fc645e3 | -3.43649 | -49.04691 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fa498620-b8d8-37b5-9d34-55522784c3a9 | -3.93384 | -55.75734 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a70afd61-f484-384d-95a0-f24c875c1d5a | -3.4585 | -43.34176 | 2025-08-25 05:01:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4de1246b-9072-33e9-a9f6-abfc1da4496b | -3.44084 | -49.04756 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b1a74be2-85ef-31f7-86f4-2dd549765e8a | -4.28949 | -48.26656 | 2025-08-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89e0acae-1f46-3bcc-9908-d98801e23694 | -4.06346 | -56.31244 | 2025-08-25 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e420300-7505-37fb-ba59-d23e41f515ea | 1.02978 | -51.19432 | 2025-08-25 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b433ab92-082c-3075-ad1f-f2711dd1a1f7 | -5.10916 | -43.20289 | 2025-08-25 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2ac73b3b-ac24-3d43-8173-6c49a551af97 | -3.45607 | -43.34523 | 2025-08-25 05:01:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6135b176-5c61-33ef-8c6d-f8f11de808b6 | -3.69762 | -49.54671 | 2025-08-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd1ef1a7-73fd-3f69-bef8-f01ae551a866 | -10.42204 | -64.44265 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fc5c418b-f590-3926-942b-7c7a60ed803e | -4.96613 | -55.825 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc2abcca-a15a-36d8-998a-8ae47b2f26b8 | -8.89825 | -62.44667 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba7053c4-5449-3a4d-adb1-7f895ff4394e | -6.89118 | -47.9296 | 2025-08-25 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 83d77e04-831b-3966-a06d-8beabbf4b4f5 | -12.7492 | -48.10838 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e10319da-4de1-38de-bebc-a6f9496a4b0a | -8.65835 | -68.67513 | 2025-08-25 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48cb2c5b-8ee8-31b6-8cb6-1545b50ca72b | -6.91638 | -63.00264 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c873457b-8713-31b1-869f-166bbae6b35a | -10.39538 | -57.68375 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31d93bf2-4be5-3364-8482-398c821119a8 | -8.63729 | -62.6479 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa4cd420-79b2-3608-bbe6-66704367ffff | -8.88898 | -62.44921 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efe18aa5-0ffd-3a0c-9367-5dc44477783a | -8.77483 | -63.96153 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 756830a7-3ee1-3fdd-9200-1ba3084009eb | -8.8733 | -62.3877 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90e48504-5e18-3b09-a2f8-e6d698cadbac | -8.99616 | -65.39664 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eb253c5-b902-3e96-bdb6-b43d9e8f057b | -9.21191 | -60.92733 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3d67c81-6c17-30e9-ba0a-287eee61d4c6 | -5.4229 | -60.17714 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90a24b94-000f-381c-acfe-3fd75070aa7a | -12.74606 | -48.13448 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6902a606-0447-3548-ac74-01f36a6e09f0 | -12.74061 | -48.14306 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ecf48f9-33d7-3579-85a0-bd2d6fde88b8 | -6.79074 | -58.62943 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c2e1847-bad8-3cd0-82dc-d1974f7db88e | -8.06923 | -49.68167 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fef3984c-81c7-35d0-8005-1b30eb0bd780 | -7.78798 | -61.57548 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68652709-a456-3a72-989b-3770110f03fb | -9.06402 | -65.73269 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6cc198f-ec9a-351a-a9a7-0f0b3e5877a7 | -9.20805 | -60.92662 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ac26e7c-6e21-3368-937d-60f1a0b1bb11 | -6.2476 | -58.07045 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ba42d1-2672-391f-9e0d-a853b8348aba | -9.16885 | -60.82272 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ad7405a-930e-3d02-8678-403e2e3b5cb3 | -9.20141 | -60.79377 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb1ac9a4-026f-3736-86c1-12e76abffd2a | -6.3221 | -47.65859 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 067fe5d1-4ca2-3144-bcd4-908fdf04ffbe | -8.11841 | -62.88312 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 467bcb04-3112-31f4-a8ec-f612db878efc | -9.26337 | -59.77008 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d8350b74-afc8-3e34-913b-e36c43a19831 | -11.18264 | -55.0245 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b5677d9-43dc-3f58-adf9-fe8652ef3ee6 | -12.9585 | -46.33577 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 402916b6-3cea-32a1-9b55-c969cac95499 | -8.06792 | -49.65856 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a26389f-345f-3db9-9a5a-283e820ad77d | -7.92553 | -45.8949 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bde45a3e-5f2c-3284-8b9f-b2e962be73d5 | -6.74777 | -50.96357 | 2025-08-25 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 078d5e91-e86e-3f91-a07e-551bab3300df | -8.87327 | -62.46325 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c94c5687-276f-36f7-9d67-10af9556adb4 | -11.17753 | -55.03521 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58bd1a5c-083d-35f3-866a-6f1624777f25 | -5.43153 | -60.17352 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0efd5406-35e1-3927-a414-967c2ea2a151 | -8.90249 | -62.42224 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92ece605-e9dc-3879-a4db-008862654204 | -8.9189 | -62.42928 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2d7a75b-2302-3bef-99ce-0870c0644b58 | -8.9182 | -62.43335 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52383804-63c1-33b2-8d52-7f618a471b8f | -6.91366 | -62.99517 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README58.md)
