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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b52aa165-229c-3140-9c62-98efd1fbcde9 | -3.54327 | -50.08778 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae6a2399-642d-399a-b18c-a56180277ead | -2.78771 | -51.67723 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 45d89d16-3147-32e9-aeb9-9c11e535de39 | -2.91343 | -54.09938 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69e7def2-e96b-39d6-add5-fb0f96107506 | -3.15139 | -50.44677 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd172f0f-7545-3a3f-8862-65505a9b36f8 | -3.17337 | -50.43581 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43afad77-e142-3d0c-b7f9-a73962ee377e | -7.09381 | -45.57412 | 2026-10-07 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee10cbb6-72bb-3fcb-bb0c-ee1ca5e93657 | -3.48094 | -50.08563 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c7b1fd58-2833-3964-b3ec-d55574ee008f | -3.43885 | -56.94032 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3c4a173-6527-3a29-8e34-c679b073a1c4 | -2.93573 | -54.13156 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc62bf73-b08a-3e5d-b5e8-d3e20c0b7a4b | -5.99747 | -53.50396 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e7a6f7ae-c82a-3e6e-9391-1d50daef8c13 | -2.84066 | -54.21722 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b87ac859-7758-30e7-9f3a-25c44058141a | -3.29451 | -54.05708 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a1b10403-699d-304e-b6b4-6607e18b1ced | -3.03599 | -53.92284 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48f7745d-a869-33d5-a18a-6e8343a0a5f4 | -2.7712 | -54.09498 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1ac29351-4753-3450-97df-23588c25997b | -2.94857 | -54.20151 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0b64761-98e3-316a-8cd3-7efa19a4f6eb | -3.12244 | -53.76461 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f85c5ace-aca5-310a-9a48-b9f794a45c6f | -2.83069 | -54.12926 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1233362-c44b-3dfc-a442-5bec28c56af4 | -3.5645 | -54.48626 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8049f41-6b2b-33c5-b31e-5b8a15087638 | -3.99386 | -56.24777 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b62f4cd6-f8ae-3064-8544-d3bbcd91874e | -2.75533 | -57.66057 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6a72bfd-5e8b-3848-bea3-e43762da6a35 | -3.18879 | -50.56919 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c88658a0-71bd-3748-b14b-25740bc661fb | -6.00383 | -53.50902 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c87066b-af4d-35ac-891d-41c431e0ade6 | -2.87383 | -54.20092 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63c07e3e-7a1d-3791-8193-127fd3762f13 | -3.16358 | -50.60485 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 883d37ac-5349-38fc-90ea-ed92685ea243 | -3.53843 | -58.64804 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32e6b959-74ae-37b0-8f91-30d8e660260d | -3.76743 | -59.31847 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd49ab84-2eb1-33cb-9436-2c375fd9dc2b | -3.49877 | -59.27184 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fdac08f-d1a4-36b8-a0e1-4686f5d6de03 | -3.04188 | -54.25875 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a2c48ea-4535-3117-a44b-946823e72ea4 | -8.2494 | -47.98948 | 2026-10-07 05:04:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7e20ad0-0121-38d7-9b35-3cf40945193e | -2.88397 | -54.09126 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ad03a52-c9cd-3cba-9b2c-e5e43dfac64a | -3.071 | -54.24543 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 739165e8-328d-3f3b-add7-1b76f1c5ef56 | -2.87862 | -54.14788 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e482d164-585d-34e8-9e04-8cfe39142463 | -1.47802 | -54.7747 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37f98a26-a2b7-3120-b4d9-eb38132045d4 | -3.50126 | -54.6296 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34175a29-e582-3433-8cd4-51e22f69bc73 | -2.9812 | -54.03391 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0279f1f1-0f1d-34bd-afda-4feef9620bf3 | -3.07046 | -54.24892 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c05f0ede-0b51-3096-8532-62182e057e48 | -4.13022 | -54.26126 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b51f5a5-fca8-394a-8e54-b1b35e0d7645 | -3.27221 | -54.04642 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6bfa9f32-9917-3f25-97ea-cfbff542ea3a | -6.20984 | -52.69442 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0c8c671-9d98-380b-8c64-50cc8eceee7a | -2.4962 | -56.83506 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0e43710-f559-3b72-8441-b062441d84b3 | -7.18854 | -55.11176 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d0fe845-fb09-36f2-b836-53a943ba3d49 | -3.24426 | -57.86586 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6de4825c-8bee-32e9-af95-d7cb99d0cfdb | -3.23751 | -50.17843 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e5e4b07-2e27-3233-8bf1-f579b50c052c | -3.1792 | -50.55587 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c1d31c98-849e-38d3-8cbb-d769ab859f08 | -3.09901 | -54.17446 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14bfa527-f17b-3b35-b00f-dc7370d903de | -5.17902 | -46.2714 | 2026-10-07 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d36401e6-2e33-3e65-85e0-dba79a8c1894 | -3.08173 | -54.15378 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70fb980e-9215-376d-94f3-609e6de51d4a | -2.76454 | -54.09396 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 346aeb47-4197-3de4-975c-199b0670c803 | -1.97457 | -56.06005 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a8840ac-1353-3671-8e4e-b102bb3b467b | -3.97638 | -56.05691 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3642d93-9f03-37f6-a26d-cc21d4f4665c | -5.57442 | -48.98814 | 2026-10-07 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d89a69-f809-37fd-bbb2-5b5510eabb21 | -3.29939 | -54.06491 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d214cc31-323d-3f9e-ad26-7dbe8e7b5c39 | -3.27381 | -54.01408 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baeaabd9-fc6b-3cae-b37f-733b954ed31e | -3.05223 | -54.38878 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec34f33c-db6d-348d-8a3f-ce269406969a | -4.45043 | -54.97953 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9742baa5-b419-3e2d-a96c-292563cd0c91 | -2.77291 | -54.10601 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 7fac2570-0b63-3811-b5ed-1a9bdb030c03 | -3.28948 | -54.04546 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77068303-9482-3d64-bf94-26ef32687a0f | -1.80757 | -53.75188 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c74efec6-391e-3518-8f52-50373930b9a1 | -3.08106 | -54.26846 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ef3bfab-f028-3f49-b917-bde51231f254 | -5.96373 | -55.3573 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff666045-65f9-3786-b3ba-aa862cd30226 | -3.10289 | -54.17146 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 063842d7-d69c-38bc-9a6d-f58ec7a62a52 | -8.70827 | -45.20513 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9d24112b-ad0a-3f9a-84a7-2c0bff648fc7 | -3.52065 | -54.65743 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 67e3ba1a-84bc-305b-8e90-8685b6c1d3db | -4.36988 | -54.75374 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fa04d8ec-6097-36b0-9406-0e0441125907 | -3.46816 | -50.08737 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51528828-19b4-3998-8606-7097720018cc | -2.48811 | -58.06166 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16bbf44b-4885-36d0-9d4b-c01d64e81bf2 | -1.10757 | -54.16108 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fd56600-0c81-32ba-898e-ae59971aad4b | -3.6174 | -55.28167 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1aece6d7-543b-3b1e-9503-48240bff67f1 | -2.98571 | -54.04904 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9424e05e-409a-3346-a407-2c2e8bff015e | -6.02814 | -55.35666 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2895d9c0-3665-38cc-a480-9c9d2e2a9a42 | -3.06515 | -54.17283 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2414974b-90c4-3255-999e-9e51a12648d1 | -2.96225 | -54.15696 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e6cd86-c549-3b50-9130-8237a50c5642 | -3.08949 | -54.30194 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df45560a-0f5e-3ebb-a62b-7ba416963357 | -3.47039 | -49.93757 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de5e3ae0-1db1-3b55-83e9-da72b399f6ab | -3.80351 | -51.9928 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39fde46c-204a-3c57-b823-143abcb707ab | -6.08076 | -53.8842 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94d86841-ef52-3018-8043-b748dba773f1 | -3.58422 | -54.31411 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1d5ac85-d869-318f-b8f5-46ce17f6e26b | 0.4419 | -60.5329 | 2026-10-07 05:04:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8273c15-102d-3dcd-bb65-986c738d6b5e | -1.0993 | -54.12444 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed039ed0-4f5f-3bdb-ab97-3ec013f75e0c | -3.28558 | -54.04849 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fea61270-3de5-39df-b721-6ea31e0440ed | -3.29555 | -59.49965 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67c73722-fcca-393f-9801-852d71a5b7b1 | -5.23699 | -50.91351 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87ff3ee0-4037-3edc-8ac5-0d9efe7e39a4 | -4.06135 | -59.82811 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b682eea7-1000-378a-9f94-ed7591bd5e8c | -1.09592 | -54.10271 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6176fe6b-0b4c-3b58-95d7-a46f09db1164 | -3.05642 | -54.20737 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d5c091b-74f8-3e3c-930e-bfed6aecc779 | 0.66324 | -59.56451 | 2026-10-07 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adee07bb-7ba3-36d5-93e3-45f2351d3848 | -3.51126 | -54.65242 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 177abb62-0bca-3e7f-bf5c-6ba21c9fd0c6 | -3.07227 | -54.14876 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29138210-bcea-3310-94f0-75f5a4c95028 | -3.967 | -56.0519 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14741d36-49da-3a2c-8b38-a9eeafddd824 | -2.80282 | -54.08908 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56a56984-109f-3759-88dc-1e3b84ce1cd1 | -1.8039 | -57.10707 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| df5d6197-2ab4-3d67-a305-344bfe89b468 | -3.27771 | -54.01105 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85315a7b-16b7-34ce-8d34-acb2ee18ae5b | -3.52889 | -54.64807 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f62d42a2-e277-3428-84f2-3867e6bf4211 | -3.61799 | -54.60133 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2114fc41-20c8-3632-a65d-b87b6c91148c | -2.8035 | -54.12867 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a520838a-9320-3aea-8a4a-af10c6009668 | -5.95766 | -55.35281 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7095fc6d-1f3b-3183-b5ea-39ba2a93472f | -2.52706 | -58.09263 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecff3e1a-d82d-33e5-9fc9-9ba6aac6ec02 | -6.87501 | -43.67763 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15a97de7-9581-37e4-a94d-aba96f5c186f | -3.00624 | -53.87096 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 238fd48c-853a-3a5a-90eb-9a76f5f39fbd | -2.30629 | -57.08375 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README69.md)
