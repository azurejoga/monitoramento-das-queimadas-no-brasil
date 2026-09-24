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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cd0e243-4484-32b1-bb4e-0cf272a67f62 | -8.27622 | -54.77181 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ec257e4-9f38-3f5c-954e-f093d945367f | -3.85885 | -58.8898 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a83a703e-13b9-3c86-b441-5c2c92215b3f | -2.55811 | -54.72971 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9bccefe-a26b-34bb-9478-988a57bee7d0 | -6.10176 | -59.88325 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94a2e159-190a-3190-bf92-4f66a36e545f | -2.83238 | -60.22886 | 2026-09-24 05:04:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5a4d83e-02be-3d8e-9c66-45f12b6f2a45 | -6.33268 | -59.96089 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dbb01b0-6e99-37e8-a667-b3c1c423e227 | -3.68353 | -60.56746 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a98ee7d-df7f-3778-ab3f-107202bf7f12 | -4.44925 | -55.03526 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86484023-02f1-3753-834c-343e98ba846f | -4.01955 | -52.07124 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5616e76d-4d06-30e8-8373-51ccee4fe505 | -5.86861 | -60.16128 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09243f5c-143f-32f0-a6ef-1b18172088a9 | -5.84319 | -49.87796 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e3cd942-fd49-31f4-bbce-d258380e9aa8 | -1.63573 | -54.90833 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78c20a29-a635-38bc-a72f-1f763294763b | -6.61434 | -59.9328 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dfb43654-b126-3104-813b-8b9df5461453 | -7.33009 | -55.59245 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 982bfb3e-f516-34f0-bde8-9c809a93efe3 | -5.42356 | -60.25279 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87a1d369-d52d-3b87-90f2-fd0f668aa932 | -4.41443 | -55.12397 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bac9970-f9e4-3163-b304-e0f474fb1835 | -5.49776 | -49.03 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f565995-3a95-3feb-8880-d95954ed52dd | -3.06121 | -49.5757 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a91a45f-0e75-370f-a69b-f08378b22f69 | -9.75269 | -48.34743 | 2026-09-24 05:04:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 592e3910-f1b9-3cbf-9028-a3b02b15e57d | -2.79694 | -49.58202 | 2026-09-24 05:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67593a96-abb9-359e-b6f4-e8a545345156 | -3.4551 | -50.07528 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 536e52c1-6b92-3d7d-9031-e689c7f6512b | -3.96522 | -59.35707 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e53f6d2f-f46a-3e89-b4b3-8d43bad623e0 | -1.22009 | -54.56048 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e68ce771-f484-3694-a884-1f20254e51d8 | -6.63984 | -59.93327 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c451180-6230-35a1-b704-e39365e51c31 | -8.89976 | -46.81924 | 2026-09-24 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94945e00-f7f2-3b9e-8b13-007fc3e1ed40 | -8.91447 | -50.89117 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f08a610d-e1a8-3dce-9795-0eb7059d324d | -8.09192 | -54.99112 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca46ef9c-34ce-3708-9f92-95c2abaa2a7d | -6.67365 | -50.94704 | 2026-09-24 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d3587c-b5e5-3bde-a993-5a849b7ca976 | -4.55622 | -54.93997 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1204c921-14ff-3e93-a4a9-61a92c679019 | -4.30178 | -49.12637 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44c7201b-ebf4-3a22-a2f8-1821386d75a8 | -6.64046 | -59.92949 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f0a2ef9-49f0-3849-b32b-0015e23b62da | -4.56622 | -54.94158 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 928f5546-d795-3200-a5f8-3c048df390e0 | -7.67406 | -45.47845 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56b3a46b-69a0-3976-8bad-756b576025f1 | -8.45979 | -48.69628 | 2026-09-24 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ff36a90d-3922-3078-bc40-93032d0e7858 | -5.76846 | -45.10102 | 2026-09-24 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e3d8b411-5293-3514-ac24-0413fe8f2494 | -6.02683 | -53.89548 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4afeb548-be24-3ccc-a82a-01698fbf70ec | -9.26303 | -46.25054 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e140c19d-e376-3f8e-ba2b-e0d7b8ed18fc | -8.12882 | -54.82269 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68615184-49a3-37b5-a58f-ae5714521475 | -6.44581 | -59.9586 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f7a0a3a7-96c0-3041-8697-1e326529fd0c | -6.47073 | -59.96321 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368ff1fb-b63f-38e1-a8bd-123088b6696c | -6.10525 | -57.67192 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0509b31e-bd03-3931-b3ce-4bb808a76a20 | -3.95816 | -59.34814 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 330206d9-431a-3c83-8ad9-2e7492d3c3c2 | -3.06425 | -54.38897 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c73f7779-7df3-39a6-9bcb-11a242d01da6 | -8.78438 | -45.83973 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d346e7c-9635-33eb-bede-b9fc97c90c06 | -5.9979 | -57.68619 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54a15682-813e-3b19-9a49-a541a36850ab | -6.19506 | -57.78611 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4651cf9e-4635-31f8-a06c-e4956a19007b | -3.0389 | -50.43681 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0936733f-1786-3dea-8731-05c8c0a12460 | -2.89608 | -54.09978 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 31c7a2ff-7d29-3d9d-944a-475c111b2782 | -2.8282 | -46.70972 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd1c08c2-ea5c-3b9d-891d-14cece71aa4e | -3.45297 | -50.07756 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| aa34cb68-5ae4-3ba8-a78f-abcdcffc43b0 | -3.91805 | -59.66747 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b3c3fca-79a6-37b9-9dd7-bc5f90a84273 | -7.19545 | -47.45506 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 62764610-717d-3116-9f4a-6dc6480a2f0c | -6.18408 | -57.78426 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6332494e-98bb-3a72-a135-19a5f7d6dc97 | -6.24196 | -60.03263 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc9d7eb8-7b4d-3723-a21b-1726658aa76c | -8.28726 | -54.78781 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 109e4ad8-aa17-3b50-b04b-420d3a25a794 | -6.6137 | -59.93665 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f3202eb1-00ef-3c09-bfb0-787430995cf2 | -8.90053 | -46.81347 | 2026-09-24 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a42f2cef-dafa-3936-8d16-92fb983e64eb | -5.40763 | -60.21636 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6cdf61b7-0cfb-3f45-8ca8-7581ed4ff3f7 | -5.22735 | -49.2284 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b3669516-36af-3184-94ef-535bded2c47a | -7.51478 | -61.4842 | 2026-09-24 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58280211-0e80-3b35-a815-46d142b826da | -10.08635 | -46.04327 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47104edb-ea09-3593-bfb9-22a28035f751 | -8.14727 | -46.82331 | 2026-09-24 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9e33b74-db29-32b4-b2ef-f4970f99212d | -5.33417 | -48.98449 | 2026-09-24 05:04:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a97ebea9-57de-3d64-afd9-2199d1f793e5 | -1.27818 | -57.04087 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00977917-856f-3ca7-8138-1bc582d405df | -3.4207 | -54.00628 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a63bbf0-e563-3a95-a412-477e5b1f42b2 | -7.6723 | -45.47521 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624efe59-8d1b-366d-b136-4180c60fefef | -4.06522 | -56.225 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c8dbcf0-f699-35a5-8d1a-28c6229a6002 | -1.21784 | -54.55289 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9a051cfb-05a1-3519-98d2-09f1d0344cdb | -7.57142 | -57.66129 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf6959b7-c3b6-33ae-903e-a2a88abc1902 | -9.25281 | -47.34846 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 644de2f8-78fc-3a9c-b388-e2ff94c2664f | -6.45792 | -59.98809 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8cdd1a3-299e-3c30-b990-45cd3317c9a3 | -2.63377 | -51.69983 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e4e8b8b-8352-3956-9740-8235b235bea3 | -6.07313 | -57.79858 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e256ebac-efcb-3b21-a607-1349da39717b | -5.99962 | -57.72147 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f0e13be-2ce4-3b8e-b357-e7ccabb4b6aa | -3.70483 | -54.2063 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f6152b0-ddc4-3a84-873b-fb47a5e3459a | -9.26221 | -46.2566 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbccccef-d9be-33c3-ae81-194fbf509500 | -1.27963 | -57.03195 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89f22966-1ec1-388f-948d-9ddf8be11ce4 | -2.64252 | -54.68893 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 743c7db4-f7fe-3115-867f-f27bb7c0d05c | -7.51559 | -61.47955 | 2026-09-24 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7b411c6-34e8-3578-a23f-01daffc6e67b | -6.12484 | -57.75847 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34b99d7f-b307-3926-aa5e-c562423018ab | -5.40541 | -60.21679 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a73c6597-e1c3-3536-9cca-f2b7f4f66fd6 | -4.65834 | -54.47101 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13be54bb-f098-356a-8795-c980554d767b | -3.40638 | -61.29223 | 2026-09-24 05:04:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcf236b7-d128-3f4a-9564-94f6433ad188 | -3.67747 | -60.57593 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c86b918-456f-3fa9-a2a4-48e00c5e4b09 | -3.71532 | -54.20439 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ef7492a-c6a6-3075-9c0d-4e92e2979a11 | -8.27567 | -54.77529 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b79f5a1f-68d6-387f-8560-edbfb4b54bca | -5.7743 | -56.52178 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1ea5892-128b-3711-a8bb-8d61ca19657a | -6.6102 | -59.9321 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fdc32508-099b-37b3-8dfa-af9b31fcfa74 | -3.70428 | -54.20975 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98909899-f9a2-3cff-a6e6-9cdf209a6abe | -6.4243 | -43.48173 | 2026-09-24 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd8d0787-524d-34c5-96b6-54135c6cb53e | -6.18828 | -53.47094 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da8c83d4-e7f0-392b-bf75-84cf6d2efb63 | -4.06173 | -56.22446 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8f06cb8-b7cf-373f-b5e2-133028d3f6aa | -6.11154 | -59.88469 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 833624ee-d1eb-32c7-a514-7f8af81777fa | -6.33395 | -49.86821 | 2026-09-24 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bb930a1-213f-3f8c-b8ce-a71016deeef0 | -3.56299 | -54.22292 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cef4271f-de15-343b-b5a8-0ae90c47c1fe | -9.53053 | -46.49136 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc6304a2-827f-3197-97f9-e44280c2ff11 | -6.90162 | -57.61221 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea74fdc7-13d0-354a-aa49-62cb54a6d46b | -6.88311 | -55.56085 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 794a2fce-c2c3-3019-8ed6-d7a9f4b2ac1b | -1.6302 | -54.87788 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f48ea1a-f752-39df-84f5-1f606d5abb9b | -6.45753 | -54.99257 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README74.md)
