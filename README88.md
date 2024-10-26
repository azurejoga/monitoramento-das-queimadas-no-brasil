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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 002fafee-41b6-31f2-92c4-f40d1667f99e | -17.94458 | -57.55607 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 2e6b539f-d112-3a79-be95-6c53c9feb456 | -17.94385 | -57.54931 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 8ea1b1b6-4517-3743-8955-a688465c2b45 | -17.94377 | -57.56078 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ee4c195a-7e3b-3586-9c25-e9f6d140a592 | -17.94312 | -57.55339 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| fd66acf8-2b24-31ca-83be-4da58fdd96eb | -17.94237 | -57.5469 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 98377ab9-3c11-315e-a65c-70327adf6e47 | -17.9423 | -57.55793 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 36350f28-5c13-353f-bae8-a4e1f34bf6a0 | -17.94166 | -57.55097 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 3c6b1224-5222-330e-a2f7-d5371d52bb1a | -17.94145 | -57.56263 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3437e704-9641-34e1-9a38-37b5a4ac739b | -17.94011 | -57.55979 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9ad9514e-84e7-3f86-9f54-d4aec0a56e8f | -17.93928 | -57.56458 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 931e300e-d00a-30f8-839b-1fb600b92b08 | -17.93796 | -57.55027 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a47bf02c-6e23-3407-aebb-293c80f75b4a | -17.93723 | -57.55438 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 2820ead2-1398-34ef-9e3c-af4f6a64d7c0 | -17.93576 | -57.54106 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 02b6d7bd-8ee1-3d89-94c2-71b962109392 | -17.93499 | -57.54542 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 35785818-eed7-3a3f-b5ee-5debb51f61ed | -17.93132 | -57.54455 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b0cd7479-0b04-3a2d-9f14-86ddf185cc6e | -17.93028 | -57.57231 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 28e29b4a-8680-3a04-9d7a-85983fda63f9 | -17.86761 | -57.58029 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 151234cc-5be7-3f25-81bc-95148b87bfdf | -17.86681 | -57.58483 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6a2befb8-be7a-3a9f-9b18-54053b4e3afa | -17.85686 | -57.59758 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 1c4552fc-e29b-35a9-b76a-24602a4d9e3b | -17.84305 | -57.61034 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4c5730f8-ff8a-3004-a50d-42d30ab7fb81 | -17.84191 | -57.55267 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 826a7b0b-e40e-3e1d-b1b5-f1921dbedd9e | -17.84043 | -57.55044 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 09159c12-473c-32ef-9216-66a264373249 | -17.83963 | -57.55504 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 202ece6f-de97-3ce5-96c7-4534ebbd8405 | -17.83818 | -57.55208 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 3ac4ca90-0190-39f9-b3b9-0cd7e85a6b98 | -17.83671 | -57.5498 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 6d604896-c941-3b01-af14-ab9a06525101 | -17.83479 | -57.61356 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 7b8b89ff-17b6-3b7c-b091-e75b2a9e872c | -17.81461 | -57.58858 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 33b8a652-223a-3a4f-90f5-42166c0cb3f4 | -17.81136 | -57.60715 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| f81eaf62-025b-354a-8c54-0f0b7f7264bc | -17.8145 | -57.54548 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5e6d282f-52b4-32c5-b875-5bd921dd63c7 | -17.79814 | -57.59497 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 29f5390d-c711-39d2-9ae5-5708700c1811 | -17.79443 | -57.59425 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5ead1f92-e7c6-3ca7-b277-4716eafd2b7b | -17.78618 | -57.59743 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| d937b487-fcd1-3ddd-ad53-55039ebe5fb6 | -17.78247 | -57.5967 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f3dcb2ad-a5ca-3c90-850d-e2e8263125b5 | -17.74168 | -57.54564 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c1ecffeb-fa83-3524-b048-8004eceec03f | -17.73549 | -57.55879 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2f7bced6-704d-3b1b-8c1b-60d10a602aa1 | -17.73382 | -57.56806 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 99cf7bf1-9721-36fa-9334-60c72c18cadd | -17.73282 | -57.56559 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 53f04b87-a553-3802-bcf3-94ac42a9cd0f | -17.73132 | -57.58196 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5264ffe2-726e-38f1-b0b4-5b0eff48b6a5 | -16.93638 | -57.7164 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8087616b-3b8a-3c9d-b35b-e70f58bbfa31 | -16.91543 | -57.6577 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ad08ec04-ac56-3f14-ac97-6d05f7e52a11 | -16.91459 | -57.66249 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ea02a3e4-4b4f-3399-9e42-ba1d80d79242 | -16.90704 | -57.66102 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 053492de-1ffe-3b4f-9b09-69b8d345c9e1 | -16.88562 | -57.67174 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f3b75b76-63af-3ee5-a0d3-897d2a0c14e9 | -16.88476 | -57.67654 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4f921ff0-fe77-3048-91ba-d72ac2324976 | -16.88184 | -57.67101 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cd4fe45d-48fa-3dcd-80c2-79cac4ac69ef | -16.88099 | -57.6758 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 00a99653-7b06-3c36-8ccb-4691f92dc303 | -17.26623 | -57.2619 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8cde57fd-d5fd-3215-bf5b-cac003636b47 | -17.25888 | -57.26049 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bcb59b4f-5e26-3b57-874d-251644c1e854 | -17.23675 | -57.1973 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8d860250-5355-3738-8b32-6c20bbd33550 | -17.23386 | -57.19209 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d30e1ea4-ab04-3363-90f4-931003b740b2 | -17.23308 | -57.19659 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 188aa861-36d8-3f9c-bfbd-09e43652e1ba | -17.23152 | -57.20561 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 08c59aa0-a027-38f9-b778-782f4f2eb107 | -17.22707 | -57.20942 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 66b83234-9cf5-3103-b42c-35a8d4f29e0a | -17.22551 | -57.21844 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0225dd6e-a047-3251-9e9b-685b936d291d | -17.2208 | -57.24556 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e1ec228d-b78c-39fb-b222-00c104074bc0 | -17.22027 | -57.22677 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a9ae47c3-54d1-3dcb-abf4-90e2e51aa126 | -17.21948 | -57.23129 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 236a9c81-ab5c-3fd4-a6c7-f53d9b1a1afe | -17.2187 | -57.23581 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a689f697-f988-3a73-98df-eee8994fc9b5 | -17.21581 | -57.23059 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c1576d35-f614-30a4-b06a-10cfb78a3041 | -17.21424 | -57.23964 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 55487b45-858a-389e-a663-af77e64cf372 | -17.21108 | -57.25776 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ee5df517-97d4-33e3-a7a6-2d78c6512c7c | -17.20503 | -57.27066 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2234c25c-15c9-36bf-8b90-637d8669a356 | -17.20424 | -57.27521 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ce52c52a-30bd-33cd-b656-796b4ec988bf | -17.20056 | -57.2745 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 27b9f6b6-245c-3a93-b41b-6b43212fd542 | -17.19977 | -57.27905 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7d351f76-e403-30ef-a7ce-a8c23a9b64c0 | -17.18793 | -57.28147 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5cf00ebb-fc3d-35b8-9d2b-9a1037a31004 | -17.18713 | -57.28601 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b528d90-ff37-30a4-8b9f-99e64a2aa157 | -17.03593 | -57.52666 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| da7409aa-e4c0-349d-9549-5ddc66f2f1b7 | -17.0322 | -57.52594 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f1248f09-6eeb-341e-b40c-8cad98cf0bf1 | -17.03137 | -57.53064 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 4544ce5d-d4bb-3671-a112-899cb75ebd53 | -17.02763 | -57.52992 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 1741e8d5-3739-3fbd-a5a7-31b0e9bf58a6 | -17.02389 | -57.52919 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 17882a35-a07c-32a4-867c-cb5d43f3fc1a | -16.9892 | -57.34681 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7d162813-a979-3848-9f0f-f7241cb069a2 | -16.94016 | -57.71713 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1799432c-d82f-3f07-8e5e-468a8d535dbd | -16.9401 | -57.71458 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| afcd259e-4c43-3019-b560-f90b3bc65f62 | -16.93635 | -57.53894 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2c2856f5-2a53-3c12-82db-29ff9183e067 | -16.93632 | -57.71386 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7b50d9b0-5d14-3516-9d77-0bd23d287a81 | -16.9326 | -57.53822 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1447a0f6-7a97-3e7d-a6b2-9ac3c1393c11 | -16.93177 | -57.54294 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d21501fb-22a4-36a1-9277-e09d93c5130d | -16.92969 | -57.53279 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d2067006-ecce-3385-bf3e-7b19cf6985b6 | -16.92886 | -57.5375 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 51b4d9e6-2a07-3623-8076-7b2c6a5afaa7 | -16.92844 | -57.51793 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6ae439fa-d129-31d1-80c1-f7811d7cef3a | -16.92761 | -57.52264 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e401dd99-d3d5-3442-933a-c8f4888298ab | -16.92677 | -57.52735 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 01f97f4b-dac6-3d33-92e7-3f5dda1cf7db | -16.92594 | -57.53206 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dd146561-4e0c-3fef-9d89-01ebf222b742 | -16.92511 | -57.53677 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3074c703-ce8e-3d63-baf2-b4597c217ad8 | -16.92469 | -57.51722 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2d583733-a2bc-329b-ba18-6f091ac94d8b | -16.92386 | -57.52192 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 7b8e842d-1882-33fb-875e-071911cb20d6 | -16.92303 | -57.52662 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 82761cbc-dc70-3580-9b4a-5aba540eb41e | -16.9222 | -57.53133 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0962da26-fc3e-3ea7-a031-597f42a1868a | -16.92137 | -57.53605 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3c2f223f-88fa-304f-8eb3-4cb2a9b20a9a | -16.91082 | -57.66175 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7f817c81-cf40-3a8f-b525-31b8d89bb996 | -16.90682 | -57.50891 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| c7c8be59-e6df-3aed-a8d9-4e1fc9da7d13 | -16.90598 | -57.5136 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 911510d3-27bc-3ee5-9cab-539a9ba7bc60 | -16.90308 | -57.50818 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 13afb18e-61aa-3110-8dcc-06b3b2ea36bf | -16.90224 | -57.51288 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b2b00aa6-a734-39e7-b3f9-13107e481e8c | -16.89933 | -57.50747 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1930a14f-cc39-3c67-be7d-a9093743acb8 | -16.86038 | -57.68175 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 37306e7f-ab15-3a90-9c16-fe1bcd98ab33 | -18.15313 | -57.32764 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 30102c02-18b5-3256-8064-e0ee4d182899 | -18.15235 | -57.33212 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README89.md)
