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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9929a88-dd23-3de1-b3fa-f19e7d2ae134 | -3.23963 | -50.31988 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 51b96948-9b4d-364c-b427-853c8c27bc8c | -1.8405 | -52.08063 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| be0cd124-4b81-3849-80ff-725dce2829a2 | -3.89428 | -51.91695 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aa85ea7a-768b-3fea-bb16-075ed9bd08d4 | -1.48084 | -54.40084 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5dd13c4a-643b-3b4b-8288-1a117782ee16 | -3.04179 | -49.53445 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 877266a2-7e5d-3c29-9a1a-0aacd9c7a5a4 | -2.66038 | -49.39477 | 2024-11-10 01:19:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e44c7297-1375-3113-aff9-a13e2b164b6e | -4.88064 | -48.59377 | 2024-11-10 01:19:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a40f86b0-a777-31fa-8c78-c3f0762fc731 | -3.38952 | -51.4622 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a3abfbf2-dea3-3c31-89bf-1066cbef6268 | -1.14618 | -53.6597 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3f88e0b9-6dc3-32a6-bc1c-a1a274890f1e | -1.15634 | -53.79044 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3ca386f6-1006-34a2-851d-c11c8473934a | -1.66331 | -51.91163 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 079d220e-6e1d-35e7-8bd8-2b650de64a58 | -3.82497 | -53.77039 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7f9281e6-0c4d-3e50-8f61-183ed86191a1 | -2.6232 | -54.40305 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 96fc837e-2cf8-3eca-9037-e433dbb24bc6 | 1.57699 | -56.0707 | 2024-11-10 01:19:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 32cd6dce-636c-37cd-9e0d-407b4bae13c9 | -3.16567 | -45.0847 | 2024-11-10 01:19:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 082e7051-c396-3934-ac5e-de1e0e9215ce | -1.70099 | -52.17568 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 276c2987-5b15-36a3-b8a3-7cd5f55cf910 | -3.20286 | -49.46418 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f981232c-1560-39c4-ab2b-c14b4999616a | -2.6044 | -49.81947 | 2024-11-10 01:19:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bacc65a5-2fb2-3b0f-8d59-84052b3fc39a | -1.42091 | -54.7617 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 68357329-1216-39ab-9f91-1ade725e9d8c | -2.65256 | -49.3903 | 2024-11-10 01:19:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| d0a22486-d6c6-3771-b38d-59862b76d66e | -1.28301 | -53.71184 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 6563915f-abe5-3f57-ada2-f3b74ab154f6 | -2.66068 | -49.90241 | 2024-11-10 01:19:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 0f5ed7ee-7afe-3b9a-ab83-e08e657e73b6 | -3.30242 | -50.12584 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 86e27f33-c2d6-36c0-aeee-fdc044131ea6 | -3.01833 | -53.27011 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| cca546d6-3035-3a1c-bdb3-889bf60282c3 | -2.93123 | -52.78248 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 42755cb5-f3db-3baa-bfaa-6f3488170f0f | -2.97336 | -53.8728 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7145a321-2908-3576-bda5-26a73ddf0f23 | -3.27592 | -53.66505 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d69f6331-396d-30d6-a9ab-21a49ce9c97e | -4.10908 | -45.70672 | 2024-11-10 01:19:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 45a1bc1a-fbf0-3b6a-9d4c-9bec006d6a61 | -3.57939 | -45.82585 | 2024-11-10 01:19:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 5ca19847-c634-3aa0-9548-afad413166e8 | -3.1696 | -49.10276 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 42bd1653-d1a8-392f-8fd0-28b0dc9d3392 | -2.98971 | -51.4594 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f336a1b0-22de-331e-9980-f7e248a001e7 | -2.31447 | -50.68185 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 724592dd-85dc-3a5f-87bd-b657717869d5 | -1.52854 | -55.00132 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ff834e9b-8d9a-3612-b6e1-b882f13290cf | -1.20645 | -53.62156 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6218f384-61b8-317e-a349-777423077d48 | -5.05566 | -44.25362 | 2024-11-10 01:19:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 2ee1b5cb-4b1c-32fa-a317-f3866028c8c1 | -3.70141 | -47.64502 | 2024-11-10 01:19:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 80bc7b43-0ef7-32d7-878f-b0f44a72f598 | -5.31981 | -45.05173 | 2024-11-10 01:19:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 54fe536e-0fc0-3c84-82cb-0748705c25df | -3.09879 | -53.32103 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d321ccc5-f9ab-3c8e-a839-5510f861200e | -1.38702 | -54.64897 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b66365e3-24e1-3a30-8810-d39677d93b60 | -2.76329 | -49.34975 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 69ad42f7-6a77-3340-9574-517f7c524422 | -3.85205 | -54.22468 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f5f8326f-d45c-3d51-8259-64dd2a47241b | -2.96308 | -53.86494 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d0cdb823-e8a1-3327-9f6e-78baf3e0cc42 | -2.09564 | -48.82378 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 9b7a749e-7443-3790-ad9a-a239e3d43aeb | -3.87449 | -50.25688 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9f651ff4-2f54-37db-9e26-e4a8b6bae6c5 | -2.9254 | -49.49525 | 2024-11-10 01:19:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a098bb14-1897-36d1-b885-a6c3aab9b66c | -2.66098 | -48.47804 | 2024-11-10 01:19:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 7af52ae1-08e7-3c7f-98b5-48acdaed3723 | -3.40851 | -50.30394 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 8fedde85-6fda-3e98-8bdd-6085f30ae786 | -2.6967 | -51.69592 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 24566226-8ff6-3b55-a4c2-e48836914260 | -3.90407 | -51.91553 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a053af84-fe5b-3a3a-b146-bae3adb6a149 | -1.25297 | -51.76356 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f3e48b85-8a87-34d2-82a9-873233d90c7b | -2.56658 | -50.6898 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7f68ed2d-0c1b-3c9e-a53f-d12b8056cff7 | -3.24799 | -53.40298 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| c4be7e43-dc4e-3e1a-a0e7-0f4fd20b0f7e | -3.3912 | -51.47402 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d78ecb15-2b7d-3191-b95f-4dbb7df662b9 | -2.21171 | -48.37691 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 35e1c5ec-21cf-3515-8c19-0e72ced98ee4 | -5.81711 | -44.12157 | 2024-11-10 01:19:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ca47d2f8-ba17-3897-8eff-d5d11363883c | -2.08356 | -48.83195 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 892c47a7-8373-3a89-8e3b-f33dbb709db2 | -3.23746 | -53.06335 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 404c2db8-0789-3970-852a-7aaf64c523ba | -1.87352 | -48.45768 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 8e380236-4b13-3821-8968-440aff35dc71 | -1.72234 | -52.46514 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bcf358e0-6827-3d35-a06e-56d82467415c | -1.34714 | -54.63332 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 6c6f6cac-8753-3802-afa8-1d0f0fbc6444 | -1.52731 | -54.9925 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 960b5600-6131-3e37-a039-3ca01ae302a5 | -1.54106 | -54.30344 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5ac0a5f1-a0b2-341d-a4eb-8ef3b01506de | -1.6177 | -52.53628 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 509a036e-8ae6-3808-ae12-9fd030734211 | -3.80765 | -51.66715 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8f1e3dcd-3da0-3843-8e6f-c7c2498fa73b | -2.29936 | -48.51371 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 17a8750a-e160-3dd3-b804-a7a08ab543ce | -3.21759 | -53.05639 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ba439939-3aca-39b0-ac2f-876c41916f4c | -2.42552 | -50.50003 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5fa6b627-0a56-326b-b6e2-bbcd62d89ddc | -2.78406 | -53.96766 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| d97aaaaa-1fbc-3d12-a735-2460921f6d2e | -2.4235 | -53.89412 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 619dddb0-6c11-336b-81de-3366953b2d73 | 0.62232 | -60.08895 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 17636514-8a4d-34f7-9b18-4a1da2b48653 | -3.13122 | -50.4501 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 301.9 |
| 9b846683-2095-3c84-ba14-6e92157929ae | -4.67658 | -45.1287 | 2024-11-10 01:19:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ae1a7929-cfbe-3ca9-bc85-17c1f06f3be3 | -1.39762 | -54.99602 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ce989f2b-31b3-3ad7-8008-4cdb8d1bfedf | -3.30926 | -50.09436 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 90a8ddf1-458a-36c5-8734-430b51c6b40e | -5.24835 | -48.07429 | 2024-11-10 01:19:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| cde6a6c3-4756-309e-9d3c-67fef6d4f3ef | -4.37794 | -48.57299 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b9574750-b6f0-3d70-a5ba-abd626fb9a53 | -3.54683 | -49.98558 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 1fc79f35-e9fe-3ea8-937e-c2b1d7cbaa57 | -2.47412 | -48.45453 | 2024-11-10 01:19:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| d619bfcb-a898-3b4b-bde3-9232762de19a | -3.30573 | -50.14611 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 19982695-38dc-3765-8651-9c68d55fcb28 | -2.31545 | -48.53253 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| aeb761e7-6362-37f3-a18c-713f4277e41e | -2.94237 | -49.1488 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| ac64b54e-f0b8-349c-8ad3-df05331af6e1 | -2.23545 | -53.66845 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03299569-731c-3707-935d-6db427107e1f | -1.8761 | -54.19455 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0d9c29e1-c475-3879-b0dc-ba4df19ba142 | -3.23345 | -50.44368 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b1da82fa-6130-323d-b032-a6b99605efb1 | -4.15973 | -45.75917 | 2024-11-10 01:19:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 2d62cc86-6d85-3470-b0db-fa50796ceb5f | -3.1126 | -45.32546 | 2024-11-10 01:19:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 49014059-1cc2-3670-a0cd-685082dc7075 | -3.03592 | -49.54105 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e84d2c2d-136f-3c6f-b1dc-9b063802d4d0 | -3.22958 | -53.0744 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| df12cae9-ebe7-3b8b-93a1-febca64a37ae | -3.89456 | -51.20433 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 865b8724-8312-39b8-8fc6-2fe8662dc65b | -2.2672 | -47.0556 | 2024-11-10 01:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 769e46b6-3ff5-3a1d-8402-ca2e48bc49ba | -2.931 | -52.7753 | 2024-11-10 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c0e4234f-9151-36a5-9140-1b081d0d6dac | -8.3967 | -44.1365 | 2024-11-10 01:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| f500d093-e43f-309c-b9b5-c48df2630aa1 | -3.2168 | -50.2861 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 195.7 |
| fb0b7109-3723-3f5a-afce-4fa56b44d38a | -2.7772 | -49.3492 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1fb56612-0ce2-365a-838f-d6c56c919aa8 | -4.6922 | -45.153 | 2024-11-10 01:20:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| fbe6fdba-2160-3e5a-b731-d8d7bdb6aa0a | -3.0911 | -49.4034 | 2024-11-10 01:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 391d56a5-1982-3371-9274-adef698532f3 | -3.2353 | -50.2645 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 36feef64-acdd-3862-ada1-0fc542b6f3bc | 2.8552 | -60.0853 | 2024-11-10 01:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 5b58212a-1262-354c-b20f-c518aa055fe1 | -17.313 | -57.4834 | 2024-11-10 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 69959a8e-bca1-3296-a957-5eefb9c8d073 | -3.2352 | -50.3065 | 2024-11-10 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |


[Clique aqui para ver as próximas entradas](README15.md)
