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
| c8517079-65b1-329e-a306-e7a03512560b | -14.7199 | -45.9942 | 2025-10-07 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4f4753ed-5ae1-3f58-9697-d4b3d503b89d | -22.1621 | -49.3737 | 2025-10-07 01:00:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 83.2 |
| eecc2e28-9da3-339a-85dd-877f372fdb1c | -6.2421 | -43.2743 | 2025-10-07 01:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 82cada10-a5b2-32ed-8eb5-baae0b193b02 | -18.1176 | -53.3548 | 2025-10-07 01:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 9d1942c0-c1d0-36f2-895d-f4e59ac3b88b | -10.8731 | -51.0289 | 2025-10-07 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 396d56a9-4107-3b14-9f93-88489a1cc015 | -8.2077 | -44.1568 | 2025-10-07 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| c3abcec3-87b9-3a3b-aadd-818373fb3305 | -5.494 | -43.0526 | 2025-10-07 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| cf119b4c-b046-3562-b811-443f336d868b | -22.1822 | -49.3921 | 2025-10-07 01:00:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b585cc64-654c-3a30-924b-c240c5b80b1f | -11.7645 | -45.1143 | 2025-10-07 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7ba383a8-eb70-343f-a043-dff4407f2c59 | -11.7641 | -45.1375 | 2025-10-07 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 7eb99175-05eb-3b3a-88ff-893efa542180 | -8.2068 | -44.2263 | 2025-10-07 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| a1712e03-c113-3661-91be-f23888d13dec | -8.6319 | -44.9169 | 2025-10-07 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 5b018f43-db2c-3d2d-a273-a0b1d2abd5c6 | -8.6127 | -44.9418 | 2025-10-07 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c5fe48ae-6e5f-37f2-8457-77f14f7762de | -22.0285 | -49.7042 | 2025-10-07 01:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| 59add95a-3233-3bbc-8130-2ac9661b40d2 | -4.6873 | -45.8504 | 2025-10-07 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 98.5 |
| a468f526-6a4c-3354-acdf-e6cbc03852fd | -4.4445 | -43.2397 | 2025-10-07 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e5a988e1-3d95-39bb-92c1-7ea657eb755e | -11.7837 | -45.1115 | 2025-10-07 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 295d01e2-80e8-3bdc-9ae9-253357a930ef | -8.6521 | -46.274 | 2025-10-07 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 195.2 |
| ce2a4e97-c405-34bb-b25a-fc5d3c8a1a76 | -10.2693 | -44.3745 | 2025-10-07 01:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5678610f-d065-3a5a-bf0d-c0aeef9411fb | -18.0977 | -53.3579 | 2025-10-07 01:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b4315c65-f63e-3182-b55b-e219d4152339 | -11.7833 | -45.1347 | 2025-10-07 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 7c4ccf5a-d6c8-3e38-84a7-a31ff499fd24 | -18.157 | -53.37 | 2025-10-07 01:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 87cc73ad-e695-378f-9a72-42f759b695c5 | -8.613 | -44.9189 | 2025-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 3234bcd3-918b-3842-8c1a-af9c26682e8e | -12.9103 | -54.7352 | 2025-10-07 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7071524c-d55d-3543-8512-d8d8aa0730dd | -4.4633 | -43.2152 | 2025-10-07 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 086982d5-ebb8-35ff-9226-db220de16c63 | -18.1176 | -53.3548 | 2025-10-07 01:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 2978f6c9-e92d-31c7-ad1b-ecf0700bac29 | -4.6873 | -45.8504 | 2025-10-07 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 9d475c57-9ae5-3ef9-9d26-00e0fe204cd4 | -4.4446 | -43.2164 | 2025-10-07 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| f6c3c58c-26ee-378b-8edb-7c656d7e6a30 | -8.8717 | -46.7878 | 2025-10-07 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| abee0a69-a987-3934-8435-84e2f7478e39 | -14.922 | -51.4507 | 2025-10-07 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b5569179-e1bb-3e14-a715-679b7cac3a8f | -18.1769 | -53.3669 | 2025-10-07 01:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2d8fea86-e29e-3854-8c3c-a6996a306fa3 | -22.1829 | -49.3688 | 2025-10-07 01:10:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9c970884-c775-37be-a044-b452bdde2bf0 | -4.6504 | -43.2038 | 2025-10-07 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 69f5c14c-5858-35f5-8071-5b6963586562 | -6.454 | -44.5978 | 2025-10-07 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| dfab1635-a889-39df-bb47-f74769c07435 | -5.5125 | -43.0747 | 2025-10-07 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 1761dba1-af08-3b18-8d78-7c6895b00b00 | -11.7833 | -45.1347 | 2025-10-07 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 926218f7-b567-3035-b221-1dce9424a11c | -22.0077 | -49.709 | 2025-10-07 01:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 203.4 |
| 26e27a45-2c3a-39da-89bc-fd2829c7769f | -14.7394 | -45.9907 | 2025-10-07 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 545bc8a6-da0e-3e60-b72c-e7642d89e511 | -5.4937 | -43.0761 | 2025-10-07 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5055cfd6-c630-3e6d-8596-9563b29e5c9f | -8.6316 | -44.9398 | 2025-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 068453ab-9fac-3651-8c42-f044d5373200 | -22.1621 | -49.3737 | 2025-10-07 01:10:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4a0cb4a5-d048-36e9-b7bf-1b663bc3dfc9 | -23.0614 | -49.8998 | 2025-10-07 01:10:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 2f8fd18b-3c42-3d1c-9488-fa92e3e45e70 | -8.6319 | -44.9169 | 2025-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 5f17dfd3-5daa-3eda-8d0f-6187bc577634 | -22.0071 | -49.7321 | 2025-10-07 01:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 249.4 |
| 572d2b72-59e1-313f-a5ef-b6d91ee77124 | -4.4445 | -43.2397 | 2025-10-07 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| cd91485b-8bac-39f3-90a2-e6bd75a221df | -22.1822 | -49.3921 | 2025-10-07 01:10:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 44b593c3-03e5-35fd-acba-c0daa50c7795 | -11.7837 | -45.1115 | 2025-10-07 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| edc98734-eb63-3ae3-bbe0-f7fa001934c0 | -22.0279 | -49.7274 | 2025-10-07 01:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.0 |
| 1d0834bb-1eae-3c5f-8ca0-c38c920a4832 | -21.4993 | -46.005 | 2025-10-07 01:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| 9381da67-b83e-3b33-9643-9d05466dd66d | -8.6127 | -44.9418 | 2025-10-07 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| a94fbc0f-c989-3fb8-8128-eb8030b0a451 | -4.6505 | -43.1805 | 2025-10-07 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 62a463f7-299a-38e2-b6d7-040712b22584 | -21.4986 | -46.0292 | 2025-10-07 01:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.9 |
| c9f5f5da-b5e9-37c1-8052-9c440785eb6c | -6.2421 | -43.2743 | 2025-10-07 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0c0b8a39-afff-3e81-a8a8-e402af8ec729 | -8.501 | -46.3117 | 2025-10-07 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0ca55c65-ea8e-3e7e-8a16-e0f8790cf3c9 | -14.9216 | -51.4722 | 2025-10-07 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3a20ac6d-40ec-336c-86fa-a3dbe8267460 | -4.6875 | -45.828 | 2025-10-07 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 9dead6d4-4b9d-39a3-bfc3-a2844f4261b0 | -22.0285 | -49.7042 | 2025-10-07 01:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.6 |
| c866eaed-a030-38e7-b6ab-494d56b1ae4a | -8.6521 | -46.274 | 2025-10-07 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 801a8136-2818-3778-82ce-89257dbbb088 | -14.9026 | -51.4534 | 2025-10-07 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ed8e71af-22f6-328a-983e-185447ef4a19 | -6.4543 | -44.5749 | 2025-10-07 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| c7d6627c-6766-3506-b97a-73b5d472ca33 | -8.5007 | -46.3342 | 2025-10-07 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 61239263-1e87-3707-a7c6-43e7583d3b4b | -23.0607 | -49.9231 | 2025-10-07 01:10:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.4 |
| 947f78ca-ff30-304b-920b-300d54a9643f | -8.174 | -50.3035 | 2025-10-07 01:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 36b38246-fd25-3165-88fc-709cee4077a3 | -8.6519 | -46.2964 | 2025-10-07 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c0101710-ea55-3e86-ad87-87a1977ee644 | -14.7389 | -46.0138 | 2025-10-07 01:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6a82b585-d2de-3d74-9c59-97d29353d876 | -18.157 | -53.37 | 2025-10-07 01:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8a1d1b1f-6c02-3f09-aa4a-2322f4957b02 | -6.4543 | -44.5749 | 2025-10-07 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| e112e841-683a-337e-a8a7-b58e6d9c80ef | -22.0071 | -49.7321 | 2025-10-07 01:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 296.0 |
| 188e7ece-ddad-3986-b297-990512b0a7f7 | -8.1927 | -50.3019 | 2025-10-07 01:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 00e21ff9-b495-3583-b5df-5cce51b06997 | -11.7401 | -43.2928 | 2025-10-07 01:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 44.7 |
| d2c20766-f1f0-33fa-98f4-9d7eb405cd02 | -14.8835 | -51.4346 | 2025-10-07 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e2c3c334-e095-3ee5-b17a-2853f0239334 | -22.0285 | -49.7042 | 2025-10-07 01:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.7 |
| ae197d39-0d33-36a8-8d03-70e283732e3a | -18.1769 | -53.3669 | 2025-10-07 01:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f33cd69b-c2bf-3af2-befb-342307a25a40 | -4.4446 | -43.2164 | 2025-10-07 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| a0c98247-194e-335b-b3a8-bed4ec7ecd0c | -8.6127 | -44.9418 | 2025-10-07 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 970a7e67-559f-3e51-baf9-992180f39a2d | -4.6504 | -43.2038 | 2025-10-07 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ab65d8a2-862d-3e15-be6c-8b18662198d7 | -5.5125 | -43.0747 | 2025-10-07 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| dc76d46e-c78d-31f6-936c-3509ae73b7f2 | -8.174 | -50.3035 | 2025-10-07 01:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a43da8f6-caaf-35f3-a227-a2ce1b1dea4a | -4.6875 | -45.828 | 2025-10-07 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a05ef755-a767-3409-9e8e-d05b27e251fc | -18.1176 | -53.3548 | 2025-10-07 01:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 34a232bf-e03b-3dbb-a997-e1dca83e6ba9 | -6.2421 | -43.2743 | 2025-10-07 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ac742c07-a6af-36be-b365-7d74d45dd1fa | -21.4993 | -46.005 | 2025-10-07 01:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| 179f1157-ea3a-3c1b-b1cf-674074914e0d | -8.6521 | -46.274 | 2025-10-07 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 09ad7418-4dd1-3c3a-84ce-9f06b96ec075 | -8.501 | -46.3117 | 2025-10-07 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f0ebf791-37e8-3561-bfe4-ce32ef5fc4f4 | -5.4937 | -43.0761 | 2025-10-07 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 58a1b289-45fd-3852-a457-a4c40c77a8d3 | -8.613 | -44.9189 | 2025-10-07 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 1395da58-f7cc-3f84-a31d-038b1dd76b6d | -18.157 | -53.37 | 2025-10-07 01:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a4c49f2b-5141-3fda-b331-c322ea57201e | -22.1621 | -49.3737 | 2025-10-07 01:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 292adcb1-824c-3445-88dd-5b8a0c188543 | -4.6505 | -43.1805 | 2025-10-07 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e0a6d134-4ca0-3f28-8962-86a12c4b8875 | -21.5332 | -45.5856 | 2025-10-07 01:20:00 | GOES-19 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |
| 716bd171-1f5d-3662-957c-03d2a368deb7 | -4.6873 | -45.8504 | 2025-10-07 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3f6c3f61-a2e4-3bcf-83c0-f6696f428bc1 | -22.1829 | -49.3688 | 2025-10-07 01:20:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 61e25f66-28ad-3b00-b882-7a565a244b84 | -21.5124 | -45.5912 | 2025-10-07 01:20:00 | GOES-19 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| babc9e5d-0540-388e-8359-c4b2739343fa | -11.7833 | -45.1347 | 2025-10-07 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8b053841-c09c-3284-855b-ecfe8f44c399 | -14.7389 | -46.0138 | 2025-10-07 01:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 89f3a9a1-d899-3651-a12e-40fecf1d1930 | -4.4445 | -43.2397 | 2025-10-07 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 06a3c2bf-6042-3449-beef-f2a30bc8fce6 | -6.2609 | -43.2727 | 2025-10-07 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 03c28c29-ee84-365d-a1f3-251c33ff3835 | -17.555 | -40.1835 | 2025-10-07 01:20:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 69e35a05-48fb-39e4-a9bb-8339b9f30e45 | -11.7641 | -45.1375 | 2025-10-07 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e84ec85b-facc-3196-a548-de7c4f36af18 | -22.0077 | -49.709 | 2025-10-07 01:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 211.5 |


[Clique aqui para ver as próximas entradas](README13.md)
