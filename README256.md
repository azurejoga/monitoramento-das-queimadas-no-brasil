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

## Dados Diários - Página 256

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7d88d79-bbd8-305c-a9ce-421743dcbeda | -4.286 | -50.7707 | 2026-10-07 19:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8766c740-98d6-3611-be6a-fedb9f2c6ce0 | -6.895 | -43.7066 | 2026-10-07 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 564428e9-bb99-366a-a007-02a743687a59 | -3.2085 | -57.87 | 2026-10-07 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 35b5cf29-b6eb-3636-bb4a-df33d9fa2c00 | 1.7121 | -55.6063 | 2026-10-07 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 20b3990c-68a5-3522-b211-318dba4bd86d | -3.891 | -52.2147 | 2026-10-07 19:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 06baf7c7-7eb4-375a-adc5-be8ec0aaba1c | -9.9409 | -43.4835 | 2026-10-07 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 427783d7-6234-30a4-81ed-44d97976c535 | -3.5684 | -54.4946 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 6f169106-b831-38dd-b6ce-5e0bb0c7cd06 | -4.2657 | -54.8729 | 2026-10-07 19:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 108fdf22-254d-39e3-be43-25217c71ca92 | -5.2461 | -48.3887 | 2026-10-07 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3ab448df-de78-3b1f-9137-1f7cfae1e84c | -7.5756 | -46.7112 | 2026-10-07 19:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| cae0f549-4b53-3645-b9cb-d66e16412c07 | -9.0591 | -65.9396 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 568fe16d-43c2-3910-9160-8b4b683b1c99 | -3.1697 | -58.6437 | 2026-10-07 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 4ce2fa45-77f6-3bd7-b6d0-056e0f0db79f | -5.372 | -44.1751 | 2026-10-07 19:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 379da146-f779-3894-b3f7-27626e7b581e | -6.1482 | -51.9477 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cfcb43a7-705b-37d0-9877-e01716ae43ca | -3.6049 | -54.5736 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f985f52f-e07a-3061-8e0a-ac7db8fe160a | -8.2184 | -46.3396 | 2026-10-07 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 295.0 |
| db98b887-27ec-38b0-92ad-f29934bf0046 | -3.1788 | -50.5388 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3545cfba-d8fd-32d7-bef3-6124d51e814d | -8.537 | -66.9764 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 6f5c2841-b16d-3685-9249-20e9c8ae7d0f | -3.4762 | -50.0883 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 233.8 |
| e546b190-63f3-371d-80c5-e9c8808f6fe4 | -5.9584 | -43.5072 | 2026-10-07 19:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 18df6cbd-7e16-3a22-98d1-263584b05557 | -4.2859 | -50.7916 | 2026-10-07 19:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e013337e-735f-3ef3-a495-78c2c7e7f1ee | -5.4835 | -44.2592 | 2026-10-07 19:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 4bb7ccbc-f02f-34d2-a6d2-a286dd23ca19 | -9.96 | -43.481 | 2026-10-07 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 6bdb5eab-2cec-33b1-8b7d-65a53da003ae | -4.1367 | -54.917 | 2026-10-07 19:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| cf0f815e-46db-36d5-87b0-642585ffe2b6 | -3.55 | -54.4952 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9b659dcb-ae49-32f7-aa5b-85ce1531f044 | -3.8627 | -50.4106 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a0f3bc3d-92ba-3322-88ba-cd12cd974e25 | 1.712 | -55.6459 | 2026-10-07 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d08c22e0-4b85-3f3a-983f-532a0d4bd03e | -3.3452 | -50.4707 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3671f572-5c55-357b-943d-b9865eaa8550 | -3.2137 | -42.953 | 2026-10-07 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 049b89f2-a002-35bd-87cb-1e7abf6a4dd9 | -6.1429 | -47.9432 | 2026-10-07 19:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 7a0a7eb9-3fa5-3511-b116-2b065ce096d5 | -3.531 | -54.6757 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| db21e8a6-e190-3d95-97e0-773d74239639 | -13.3865 | -43.8708 | 2026-10-07 19:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 4683ab94-e111-3dfe-b5f8-5bbe538298d5 | -3.8973 | -44.1255 | 2026-10-07 19:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| f5f48ccb-4662-3a3f-9f74-3552fec108a5 | -9.507 | -70.4439 | 2026-10-07 19:10:00 | GOES-19 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 98485c38-ad6f-336b-8d94-fd65537c3fe6 | -4.3045 | -50.77 | 2026-10-07 19:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 1cb0c876-4f19-33d2-97cf-26e529608a7e | -5.7489 | -53.4641 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| a1b6533c-f261-3141-a91f-bcf4f0192d9c | -3.3134 | -53.8592 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |
| d16a831d-b33b-3ede-8b56-8ee4461b5120 | -11.2333 | -44.8678 | 2026-10-07 19:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| f5b1ff84-6ca8-31e7-9d63-a51de854d086 | -6.1298 | -51.9281 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 83310ed0-f18e-34c5-bbfc-fab28b368ffe | -5.051 | -49.7677 | 2026-10-07 19:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 346307eb-4e6a-3aa8-acc3-697de5aa7671 | -3.6786 | -54.5115 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 552e8bdf-2777-3dce-b9ac-52c27e5b3087 | -2.6859 | -49.0539 | 2026-10-07 19:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d6928e85-1c94-3d0b-aaef-7621f9985b5c | -2.9327 | -58.3204 | 2026-10-07 19:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 8ce8cd6e-c6a3-3735-b2b0-3b4828c45380 | -3.2136 | -42.9764 | 2026-10-07 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 16f9b9bf-dfa9-35e2-9a8b-e8cc4dde699b | -5.9644 | -40.9627 | 2026-10-07 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 174.6 |
| f202e39f-43e8-3c2f-a2c9-49fce32c4add | -3.7166 | -54.2297 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| eb32146f-087c-31d2-9579-2feb21b35a01 | -5.8205 | -53.8255 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| d874ba5a-be5c-3c35-a559-b7389c9e8fc3 | -5.4771 | -42.8427 | 2026-10-07 19:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 214.4 |
| ec3180a9-9b78-3344-bd5e-41010fa93426 | -13.3671 | -43.8742 | 2026-10-07 19:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 5dfe9a33-b6c4-3c8c-a27f-055b26604cd2 | -3.7872 | -50.7483 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| dec06bb6-aa05-30b0-bec1-c63864150e3f | -6.1244 | -47.9227 | 2026-10-07 19:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7092f478-90b6-38b1-b2cd-57e74140f118 | 1.8768 | -55.7227 | 2026-10-07 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 81e52f6a-7f01-3b3b-8d15-99ab620ecb1c | -4.1574 | -44.2726 | 2026-10-07 19:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b20215c3-f3a6-3d9e-85d0-285451716aa7 | -9.1015 | -45.1164 | 2026-10-07 19:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2a010df5-cc44-3348-be18-063289b0548f | -11.6369 | -43.6876 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 76224495-2a8f-33e2-84c7-53ec2c711638 | -6.6599 | -52.9675 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| a722776b-24b1-3876-b7e5-c7366a72c384 | -7.8789 | -72.3492 | 2026-10-07 19:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 94.4 |
| f9282751-976a-341c-b5f0-c0a84a62ce70 | -7.6767 | -72.3142 | 2026-10-07 19:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 0827a87f-5671-311b-a805-2e97dd630051 | 1.6937 | -55.6263 | 2026-10-07 19:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 82c7c0c3-46b3-371c-a689-2f28c1883fef | -6.1431 | -47.9214 | 2026-10-07 19:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 57fca691-3db6-3bec-abce-a253e197af8a | -6.1617 | -52.6471 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 4f15f8a0-05f6-37aa-aa7e-b908a26378b9 | -4.0486 | -54.0384 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 463319a3-9b18-3361-a951-3c577bc84631 | -6.8764 | -43.685 | 2026-10-07 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 6cb44d4f-1e8b-3bb4-94e9-cef6ead17360 | -9.0592 | -65.9209 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 5e1d4509-d8a2-32f7-a327-bb24cfa68be6 | -6.6784 | -52.9664 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 2f34397d-4bff-382b-aae9-bbeeaa96bd3e | -10.4727 | -47.211 | 2026-10-07 19:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| e06c0d9c-4d6d-394e-876b-d4e19810d03e | -5.8204 | -53.8457 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 4e2440e6-d906-3a59-8211-622a0894a369 | -4.1406 | -54.0353 | 2026-10-07 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9850be3d-1f07-3d5f-84fc-392e1beafb57 | -5.6748 | -53.4879 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 0ac0eabe-eece-3e4f-85bb-e12b8b3d5234 | -5.7189 | -45.1547 | 2026-10-07 19:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 84d6904a-2063-3d61-bd28-9b81f1ba300d | -3.195 | -42.9772 | 2026-10-07 19:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 75e4ed90-c60a-3986-ab03-4d9552f381f9 | -8.9772 | -45.9249 | 2026-10-07 19:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 03ee04ae-b517-35fc-8c3f-f87f5b37d1f9 | -3.6612 | -54.2715 | 2026-10-07 19:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3f1917e1-ac12-3a0b-bbb0-f80f75e15931 | -7.1827 | -52.6078 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 3c968164-409c-3fd9-b999-258cba44a514 | -3.73 | -55.486 | 2026-10-07 19:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 95c7d583-e179-3339-b374-e645587b157b | -9.3566 | -65.7436 | 2026-10-07 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 67f30205-097e-30cb-9e74-55600e5bf949 | -3.2267 | -57.889 | 2026-10-07 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c0bdb453-df3b-31cf-a254-379612b55c16 | -6.8952 | -43.6833 | 2026-10-07 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 386.2 |
| 1f21edb7-13b3-346e-96a1-99f76e5df564 | -5.9412 | -45.3874 | 2026-10-07 19:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| de0a441b-1bf9-3fe6-8e26-d2ea3b375cb6 | -1.1094 | -54.1601 | 2026-10-07 19:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 4d19d628-fd39-33de-8abb-09ab9a4e7308 | -10.9938 | -45.4985 | 2026-10-07 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 895f59a2-5bc8-342e-9fca-80660b2ea36d | -6.6753 | -44.9674 | 2026-10-07 19:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| f28de60d-694a-3ec8-88d5-a6d2bf8cb42b | -3.2957 | -49.1202 | 2026-10-07 19:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2411f097-71f6-3ed1-bfc2-421bb722bbd0 | -3.4761 | -50.1094 | 2026-10-07 19:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 879a97bb-bce1-31fb-ade4-fc1f8d1b0684 | -7.5758 | -46.6889 | 2026-10-07 19:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d0baec13-7143-3d97-a466-f23277422f16 | -5.7659 | -42.0389 | 2026-10-07 19:10:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 0d9e3c82-c17c-3c72-bbac-499233cc8e4c | -3.1787 | -50.5597 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| 0a49da09-99be-34b4-9843-ccd58c0e0689 | -7.4697 | -42.8315 | 2026-10-07 19:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 164.0 |
| 81c55922-d15f-3a6c-8606-b4991e40ad33 | -3.7654 | -44.3611 | 2026-10-07 19:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 95f80860-1bbc-38f8-881e-21924fd90f51 | -7.4886 | -42.8295 | 2026-10-07 19:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 497ee67b-15e0-3046-94ce-98e9d3baf06b | -3.3637 | -50.4701 | 2026-10-07 19:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 9fefe994-85d6-329e-9927-819c8d243741 | -5.9647 | -40.9383 | 2026-10-07 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 198.0 |
| 37460596-880c-34e4-b980-439563b2cab2 | -7.6583 | -72.3144 | 2026-10-07 19:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 93651e26-a753-3d02-8e7d-7d505ce2bc1c | -6.0447 | -53.49 | 2026-10-07 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 35ab2506-a311-33c8-ac54-a6c40f28c9ad | -4.2744 | -46.3846 | 2026-10-07 19:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| b97459b5-f727-3a12-8c12-852620ba55fd | -9.9398 | -43.5542 | 2026-10-07 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 23fddc09-4e5b-3ac7-8288-5d4b138d50c5 | -11.8503 | -43.5598 | 2026-10-07 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 34b41dd2-1ce2-381c-b0cb-c002d5dbad8b | -6.1217 | -53.0584 | 2026-10-07 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 8da2579d-796e-3ced-91eb-b180a99cee73 | -3.1102 | -54.146 | 2026-10-07 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 4338c078-500b-30ea-81de-2e052d829f64 | -5.4958 | -42.8413 | 2026-10-07 19:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 212.7 |


[Clique aqui para ver as próximas entradas](README257.md)
