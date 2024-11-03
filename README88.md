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
| b466e0f2-4ce5-3f45-8504-9d51dad15337 | -3.07087 | -54.16847 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44b650e9-7877-369b-9b65-f820972b4d3f | -3.06894 | -54.14536 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a4b5ae5-559f-3121-be9e-d7725217431b | -3.06847 | -54.14853 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6dd5532b-cd6d-351b-8702-3b9719723f8a | -3.068 | -54.15172 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 797d57c3-cfbf-3dfb-a370-4a936dea388f | -3.06753 | -54.15491 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a6a8d68f-951c-3b71-9c6f-0bba6c1ac616 | -3.06706 | -54.1581 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d10e6f13-f4d1-3bbb-9979-cd00230c227f | -3.06658 | -54.1613 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 398d8cc5-061c-3cac-9b2d-a0cdf2b83342 | -3.06611 | -54.16451 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d554498d-bd6b-3ee3-9dd2-3a9a915aef31 | -3.06563 | -54.16775 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0541544-65dc-335e-9412-aec0e3bed02f | -3.06323 | -54.14778 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1b703e8-2dc3-3d88-82b4-c98521f15ef8 | -3.06276 | -54.15099 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0f6937e-92d1-3b61-8721-05b2bedf5278 | -3.06228 | -54.15419 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e999234e-43ff-3c40-bd96-3c37a4298a0c | -3.06181 | -54.1574 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c36d2871-292b-3c91-ad67-00e5897aaa88 | -3.0604 | -54.16699 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11953263-61c0-3c50-ba43-e58c130209da | -3.05799 | -54.14703 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd271dd4-40b2-3592-9fc6-5e5d4022b8ec | -3.05752 | -54.15024 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 632f4be4-53a5-38fc-8f03-6432e584e5cb | -3.05704 | -54.15345 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd439745-5752-3edb-9ebb-12410fe2e405 | -3.05657 | -54.15665 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0e6ee32-da69-361f-a451-75191bc764e6 | -3.05322 | -54.14305 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf4a9a7d-e559-3000-9110-ed1b5d889d29 | -3.05275 | -54.14628 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eaed531-d94b-345d-8c0e-8fe130727d26 | -3.05228 | -54.1495 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64c5c192-a712-3e54-9082-5365a33bbe70 | -3.05181 | -54.15269 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9704a173-710d-31ab-8822-d0638c94c71c | -3.04798 | -54.14233 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa7ed789-6ff3-3aac-bba4-cf5d5c181916 | -3.0475 | -54.14555 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a987539c-f9df-39f5-bae2-3582a8f05b0c | -3.04704 | -54.14875 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e83a3f-94dc-3c53-9bd0-1c8c283f0000 | -3.04657 | -54.15192 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a21e74a-9f1c-341a-9f53-dceb3a6625da | -3.0448 | -54.20037 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc99efc0-c733-3818-980a-05e219e7cde4 | -3.04434 | -54.20355 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65bcc970-56c6-32c1-940b-16b878515967 | -3.04144 | -53.2649 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e67543a-ac44-3041-95f7-8978211bfb79 | -3.04086 | -53.26874 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f4fe22f-730b-3d4d-9998-6f713058db47 | -3.04029 | -53.27252 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f662785c-c0d5-39b2-b6c1-729c19f6862a | -3.03973 | -53.27621 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4f97e32-6a62-3775-a7b9-eada4e33fed0 | -3.03959 | -54.19959 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71e35c23-46f0-3286-bf31-43c14ee9b4ba | -3.03912 | -54.20277 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 457b82af-078b-30ec-98fc-d4165e8915f9 | -3.03866 | -54.20595 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15b93c9e-d0d6-3210-ba2a-70d75d29cc38 | -3.03588 | -53.26414 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54244486-4bd3-38f8-a3d3-6b85b613e848 | -3.03473 | -53.27169 | 2024-11-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6bde3f2-e2de-3724-9b30-ba3c20753d0c | -3.03437 | -54.19883 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c06fe49d-abd9-343b-b0b3-a151701d9fcd | -3.03391 | -54.202 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb5dea5c-bc75-349c-81b0-0d1e3a627df0 | -3.03341 | -54.20134 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0a0ab8e-6ca6-318a-9a87-9b89f55a33a9 | -3.02915 | -54.19807 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edef26ef-b780-3d27-b2e3-52a191865039 | -3.02869 | -54.20124 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0849620c-a895-3f72-aca6-a7f865c239ce | -3.0282 | -54.20059 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fab708d8-8000-3dd2-ae2a-d2e9cb3e3b5b | -3.0278 | -54.49361 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df472d18-46e5-3f6a-8185-0bea4347e146 | -3.02771 | -54.20375 | 2024-11-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01e12329-1ac4-369e-8842-624f7888709a | -3.02737 | -54.4965 | 2024-11-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bcf56be-a710-3b07-8b93-d5557be68629 | -3.02346 | -65.01579 | 2024-11-03 05:33:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2afbaccf-0d54-31c7-b915-d9a444ce26a0 | -3.02003 | -65.01524 | 2024-11-03 05:33:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec7934b5-1150-361c-aea2-a96e15d5275b | -3.01719 | -65.01097 | 2024-11-03 05:33:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f5ff752-d76f-33b7-a909-20886a222269 | -3.01717 | -56.92562 | 2024-11-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e0098da-ef0a-308f-9c22-ec6090b4348d | -3.01654 | -56.92973 | 2024-11-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61ef4da0-78bb-3204-9c9e-e6772e377442 | -3.01591 | -56.93381 | 2024-11-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed2f3000-b654-39db-8af0-6dec2e8a35f7 | -3.01377 | -65.01042 | 2024-11-03 05:33:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81076bd4-d3fe-3da9-af4f-3cbdd301c6f6 | -2.76381 | -57.78789 | 2024-11-03 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a58ffb99-9760-377d-af8b-6924dc981723 | -2.82589 | -57.70815 | 2024-11-03 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c2b15f9-e73b-3dd1-830d-11c163c35170 | -2.82195 | -57.70838 | 2024-11-03 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88e597c7-8b57-355a-b76a-5e09c0adc6f7 | -2.82181 | -57.70752 | 2024-11-03 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e3513ca-4961-3b97-91ac-e52aae606ff1 | -2.59529 | -56.99909 | 2024-11-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3d7a67c-4967-37eb-bda2-5369e360650a | -2.58469 | -57.57209 | 2024-11-03 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be3038a7-ecd3-3ee0-ba19-9aa1c9de2ff4 | -2.58058 | -57.57147 | 2024-11-03 05:33:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5f6f0df-2538-3272-951f-b60f18933de7 | -2.56833 | -57.11653 | 2024-11-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e7419e8-9203-3719-b232-7f8bf9540060 | -2.56772 | -57.12045 | 2024-11-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 852674e1-61d3-3f4c-95d2-ded25365043d | -1.91781 | -61.72876 | 2024-11-03 05:33:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713b53d9-d9db-3036-8d26-385380432702 | -1.91393 | -61.73174 | 2024-11-03 05:33:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cc8b947-803c-3ee9-8c92-53af1dd123f1 | -15.31164 | -59.39859 | 2024-11-03 05:35:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9f9718c-f40c-3d6d-9072-31351a707019 | -15.31069 | -59.39971 | 2024-11-03 05:35:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79218f80-0105-34ce-975d-bb249d2a337a | -13.45299 | -61.38566 | 2024-11-03 05:35:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b458dc-bf8e-332c-9d74-be73325073e3 | -13.37043 | -61.31419 | 2024-11-03 05:35:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2014c134-cc26-34a0-a078-5e672adf822a | -12.20031 | -64.01958 | 2024-11-03 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c6dcc78-2f0e-3d9a-8e9f-1cfbf798cf88 | -12.19697 | -64.01906 | 2024-11-03 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4bce973-9b31-3f52-a5bf-cc97a22fae57 | -11.99435 | -63.52842 | 2024-11-03 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55f2fd23-832e-352d-8d4f-bde30c1ea11f | -11.9938 | -63.53209 | 2024-11-03 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8bc690e-8084-39f7-a34d-d4f71aac2b21 | -11.95113 | -64.07247 | 2024-11-03 05:35:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd355442-f6a3-3ded-892e-3eac10bf0fc1 | -11.28031 | -56.14438 | 2024-11-03 05:35:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cf82f94-a28a-3fb4-9c6c-1f40ca788ef4 | -11.27991 | -56.14753 | 2024-11-03 05:35:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 201a98e4-7a83-3452-b0d1-529fb93e5447 | -1.0441 | -47.9272 | 2024-11-03 05:35:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c6f33d24-0629-3b21-ba06-8561639ad430 | -1.0441 | -47.9055 | 2024-11-03 05:35:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f8a50060-b266-39b1-8427-ef633d4e7003 | -1.2755 | -53.4138 | 2024-11-03 05:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e0bf1e6d-de4a-3fb3-a56d-949bbeaedf12 | -1.2755 | -53.3936 | 2024-11-03 05:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 7295dd9f-1d6d-39ee-b387-c477373e1b1b | -1.2756 | -53.3734 | 2024-11-03 05:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 531074bc-a4ab-385d-b5e1-aab6e62535f1 | -2.5796 | -53.3927 | 2024-11-03 05:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| f901c958-ce51-37e0-8be6-1679fbedcd2a | -2.5797 | -53.3724 | 2024-11-03 05:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 19c1139b-600a-3614-98e4-8310dfd63a6a | -2.7419 | -54.4353 | 2024-11-03 05:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 315693d6-78e0-3a63-aa63-0d8755cc4f90 | -2.7419 | -54.4153 | 2024-11-03 05:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 14efb6b2-635e-3f6a-bd7a-22bf8b65b157 | -2.7602 | -54.4349 | 2024-11-03 05:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 9b66c8dc-9244-37d7-88d5-ed04b6e585a7 | -3.055 | -54.1474 | 2024-11-03 05:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9b135434-ae59-353b-a4dd-bf21b3d38e3b | -3.0734 | -54.167 | 2024-11-03 05:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ca370962-a4a2-38ee-a722-77d3f7ac1fd0 | -3.0734 | -54.147 | 2024-11-03 05:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8a286516-f3b1-3543-856e-62a6823c82cb | -3.1059 | -50.3105 | 2024-11-03 05:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6447dccc-5159-3b8b-a0e2-6ee92fbd7dc0 | -3.106 | -50.2896 | 2024-11-03 05:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 87783680-25b6-3f6e-82a1-849f80dcc94a | -3.1061 | -50.2686 | 2024-11-03 05:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4cf13be0-4c42-3a93-9f3e-c0e264224a37 | -3.1245 | -50.289 | 2024-11-03 05:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a6b9d873-6107-3fea-8ac6-d6e17e0eb747 | -3.1501 | -48.5689 | 2024-11-03 05:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 27ab1d3b-95ad-36b2-a3e1-727e6c3f2bb1 | -3.1983 | -50.2867 | 2024-11-03 05:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 04ef3286-8232-3723-ad5c-3f727015dbc5 | -3.3276 | -50.2825 | 2024-11-03 05:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 86039d1a-50d3-3bdb-a0d9-2d2c7ab2bdbc | -3.9473 | -48.3666 | 2024-11-03 05:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1594eb4f-2479-3d43-9ea8-13f9656af7fd | -3.9474 | -48.3451 | 2024-11-03 05:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 6f6a1193-7a63-3c6e-9f8d-8eb9c808bdc4 | -6.5239 | -41.4929 | 2024-11-03 05:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 67f9cd54-1fdc-3d50-bac8-6b8e92d8c50d | -6.5241 | -41.4688 | 2024-11-03 05:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 10eb5b1f-b019-3b03-ae31-b7e1ba86b26f | -17.28579 | -57.51054 | 2024-11-03 05:37:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README89.md)
