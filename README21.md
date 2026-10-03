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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be9f7a6f-0dbd-3641-bd1e-609c9ac7dd4d | -3.1033 | -50.30152 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41e52c1b-a231-3763-91f3-3b2457a82254 | -2.92403 | -54.10169 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 032231a4-9424-30af-ada3-d1bd9f2effd9 | -2.04948 | -56.86669 | 2026-10-03 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e334cae-ee62-348c-b07f-8353a1c618d8 | -2.57887 | -49.99783 | 2026-10-03 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2734407d-0bfe-387c-adeb-892f28579b1b | -2.97629 | -53.26823 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbb12104-9b64-3713-96b5-96d35e823949 | -3.00549 | -53.88161 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32d7f6cb-be85-3f7d-bb67-d470f0c433e7 | -3.25008 | -54.51306 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 004d5466-66f3-316e-b940-a9e060b6aa5f | -3.13675 | -53.74268 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 123903ac-83a1-3f88-8af7-0ac6b02faf42 | -3.27279 | -50.08499 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 782a631c-3ffb-37bd-a595-18197957b268 | 1.78802 | -55.61383 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c4ca493f-e5e7-37f7-b73c-bd7154c331d1 | -3.21195 | -50.91061 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8f654d3-8368-33a1-ab84-84f2bf0c3070 | -3.22114 | -54.30737 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd841000-f489-30c9-aa38-84eca4316537 | -3.1908 | -54.10409 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09f6a45b-711f-3b86-8b81-93a440ed5f5b | -3.76496 | -52.29412 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da1fe677-4d95-3502-a583-da7e78eecb68 | -3.17345 | -54.08274 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64715bf3-36c8-3204-8d28-4647702ed9b8 | -3.13785 | -53.73584 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8adfc556-d705-37c1-a586-eb4840a13219 | 1.73178 | -50.80267 | 2026-10-03 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef0b1ad3-4f42-3a1c-b4c6-b28540e8b51c | -2.98406 | -50.48902 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd5b02b4-4b6b-3b36-96ab-ebfcd42e1f3c | -3.07652 | -51.2756 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a509aa66-168c-3c15-b29b-756cc08e196c | -3.01007 | -53.87875 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e38891ac-a259-3bbd-87b8-ab26d588531a | -2.97243 | -53.26758 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d249e1b8-acf5-3d85-9def-b9fb314daab0 | -4.0574 | -51.11627 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e9d5ec3-f6f5-3878-839a-7d73ce6daddc | -1.26007 | -54.5562 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebf4b351-06ed-3984-a9b9-b7abd07442ba | -3.12371 | -53.74764 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 72df979f-7fdc-3341-b9e1-320db9a1848d | -3.22344 | -54.31213 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c53d0ad-3998-38b7-816e-2514f1dc0e84 | -2.93157 | -54.1561 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bdb460e-948b-323e-b4b4-74d31adae183 | -2.88965 | -54.13358 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 170be6f9-374d-30d9-b720-6701aba0f947 | -3.05925 | -54.16842 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eba11fca-cc07-3d86-84ab-deb7ef52a635 | -2.29045 | -47.88029 | 2026-10-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b33c2b13-37d2-39a1-9433-8313e8f846cc | -3.30017 | -50.3251 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb30317c-5809-3d9e-bd41-938f31f4df76 | -1.96497 | -48.37338 | 2026-10-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f07f798-b712-302e-9921-fd82c0af0cc8 | -3.0072 | -50.47409 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac2a88b-059a-364c-aca8-e7ff00b94477 | -3.14182 | -53.73647 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9c7ab7a-26db-3259-95a9-61637e1b2c25 | -3.06605 | -49.36502 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff30febf-f73a-332f-ba58-2047f6831133 | 1.95602 | -55.7784 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91a3bb6c-b811-39d4-9c72-c7b0d1a191bf | -3.17577 | -54.09406 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a14ce077-a01d-366e-a9aa-8d33c6652caa | -2.25638 | -51.93767 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbed19e0-5e58-31e1-bf95-06584cd17679 | 1.96234 | -50.88647 | 2026-10-03 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6cb6396-c098-35d0-96f7-91ba6ece5cef | -2.88348 | -51.03213 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef8ebe1-c0f0-3a64-8115-d854a98c3439 | -1.24875 | -55.87907 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08207181-7733-34be-9e76-bc939feb9162 | 1.92479 | -55.80586 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0cd72dd6-38da-38bd-ab84-a76e862f04f6 | -3.00951 | -53.88224 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1235d41a-c830-3ea9-a062-c17f5cbe5c44 | -3.29418 | -53.8452 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b902bbe-7173-30ef-9730-9a43f0301a9e | -4.74283 | -43.27196 | 2026-10-03 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d14e68c-0da0-3adc-a760-291ed0f4b75e | -2.88288 | -51.03589 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cce68b2a-b4c2-341e-bbd8-467f1108552d | -3.17288 | -54.08627 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27a9f19b-2471-3903-aff6-a9270c105b93 | -2.17401 | -49.75816 | 2026-10-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc6534c3-d31f-355a-aead-4695ba341497 | -3.35426 | -43.38758 | 2026-10-03 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 294a024d-d186-3f2e-b08d-709b64ce4ff7 | -4.18536 | -48.66801 | 2026-10-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 136e7ae9-1442-3d84-82bc-3badd7a2d0a0 | 1.78315 | -55.61459 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5b35e8ec-44b6-3693-91c3-b25638c865b1 | -4.05179 | -51.08507 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53e2d4c6-6ad3-3fc1-a348-0035745dae48 | -4.73855 | -43.27127 | 2026-10-03 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dcd73314-196d-3b90-a24a-18329e557214 | -3.12602 | -53.75853 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b9ef785-cefe-3244-94af-cb21c28e889a | -2.91702 | -54.09317 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c7d37bf-d705-3b2d-b9aa-5df56a65d133 | -2.15443 | -47.74839 | 2026-10-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3ca4ed6-fe50-30ec-830e-ef9c717bdd75 | -2.86094 | -51.02145 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 056409c5-749f-3ce2-add1-e0d76565b004 | -3.1226 | -53.75448 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72ce02d5-dc7a-3d7d-a64d-d36577e00d09 | -5.18919 | -39.74224 | 2026-10-03 04:38:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26afa1bb-93d9-3509-85b6-3a29fd35e65f | 1.73535 | -50.80213 | 2026-10-03 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25438ad0-b4b9-3759-a858-e95968c7f4da | 1.79449 | -55.59087 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b173021-d26c-32e0-a050-3f89207cccbc | -3.1031 | -51.28751 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d74f6a67-b944-3bd3-9d56-3f0b950b2676 | 1.75027 | -50.80404 | 2026-10-03 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2bd5987-188a-39e6-bdc3-54c4eb3e07cc | -2.89491 | -54.15318 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bdebd19-4156-350c-9ee9-a08ca970f137 | -3.13619 | -53.74609 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5312eec2-5777-3910-932e-64c2cb509e6a | -3.22939 | -54.30857 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fc1160b-ebfd-3c85-8c32-a3ebe6d801d9 | -2.89199 | -54.11896 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ae788f3-f3f8-3ad0-8809-dcda5f6972b2 | 1.92069 | -55.81223 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01cfe960-63b1-372d-bbb3-a8e3d6e28be3 | -2.96938 | -53.26203 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74cf88f3-7d87-3b14-bde3-3d792b26b539 | -3.16999 | -54.0785 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 540cb7f5-085e-3e47-97ef-7f92b57923b3 | -2.25409 | -51.92877 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d4107af-0873-3764-ac8c-6fa4b17ec58d | -1.22085 | -54.53785 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb5dba0a-10c8-34f7-8350-12c4c4a21e82 | -2.89316 | -54.13789 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c459271-2ce2-32d2-831d-64601eeb4430 | -2.86438 | -51.02198 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5feb1388-851b-3d79-9bed-e54353237419 | -2.15389 | -47.75188 | 2026-10-03 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7801b02e-cc59-30f7-b3fc-e6eb9256ac84 | -3.01064 | -53.87529 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbb550a0-c4cf-3cba-b435-893e53b85333 | -3.28039 | -53.82904 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1c8f1a5-eb2e-38da-a720-8d7be120cf43 | -2.91677 | -46.72543 | 2026-10-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f278d147-88b6-39c4-b1f1-349f977ae63c | -2.82864 | -46.7051 | 2026-10-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 774c1ec5-8632-3297-9995-8e47564f3c21 | -2.89257 | -54.11532 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bf7e033-b23b-3c4d-9916-fc8b3979a649 | -2.78138 | -48.65899 | 2026-10-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 310c49ab-5eb9-35ac-b065-a9d829e4ae53 | -2.87284 | -50.31677 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fb63280-1f8e-3263-87bc-add1ff0af9a5 | -3.17866 | -54.07636 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2eee8a6-59f1-3228-aa0a-303ab121aaf0 | -1.27235 | -54.56238 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a168a429-576b-3f91-84e5-c1e86b092efb | -3.06551 | -49.36847 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 428910ed-d10d-317d-8cdd-9878ea9b3f43 | -4.05683 | -51.11993 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f47aad4-51da-3468-a186-aba1b2908453 | -3.14127 | -53.73988 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf331950-6d64-30fa-a7c1-20ef4f046110 | -0.36849 | -52.02033 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8d8e689c-1ba2-355f-a908-b78016096f9f | -3.1265 | -53.73053 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d4f3ff68-b793-3481-ae8d-b7b4c19526f4 | -3.22468 | -54.31165 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99a4c71f-f8e9-3986-b910-83cdbef4c44b | -4.05398 | -51.11571 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaef03bd-dbb3-3465-aa5c-ef16d3900b14 | -3.21213 | -53.94721 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32a2218b-0813-3a28-94bc-b86de9297039 | -3.1161 | -50.2779 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8df24ab8-f4d5-33d1-a9aa-6ba319b95e67 | -3.12595 | -53.73395 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1069b589-0a53-3339-927b-f6a599695755 | -3.17057 | -54.07491 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba69a90b-3f18-35f4-ae94-62b8ce3a5962 | -1.44513 | -48.91279 | 2026-10-03 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e493a8be-def6-3121-aebd-65a53cabbf8f | -1.41373 | -48.89741 | 2026-10-03 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3584b757-76c1-339d-9238-db65468784f5 | -5.1897 | -39.73866 | 2026-10-03 04:38:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1fc27231-bc96-31bb-b9ba-cd5023a29f01 | -3.09817 | -51.09596 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6404a99-7927-3205-9bf4-4b1783a7ee79 | -3.27167 | -50.02718 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d67a1a6d-e0a5-34ab-815e-714405955fdb | -2.93647 | -54.10087 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
