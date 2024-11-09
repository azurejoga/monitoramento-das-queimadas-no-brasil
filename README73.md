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
| fd16d32c-bd14-39f9-9698-e78b2844589e | -1.18273 | -52.13645 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b41a421-14dc-32b0-b87b-e17b3bc19d57 | -3.23905 | -53.3927 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88afafe5-30e4-35f6-a1ff-f023a4480b46 | -3.91298 | -46.45053 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0dd7eae2-ac8d-3701-b75a-9a89b809574c | -3.23519 | -53.39563 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 223cfc27-11d6-3e5c-b562-b82bed327dd8 | -3.09496 | -51.11292 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a3a1dcb-8893-3fff-b8b4-c6c77538529c | -0.83148 | -53.0581 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04788b5f-b8dc-3e3d-b89d-dea095220c4e | -3.09149 | -51.11239 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe0fdc72-c5e9-3dac-b9b7-1e179d828586 | -3.81396 | -49.85672 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ced39b26-0a7c-31c7-a6fd-f1d73887d4c6 | -1.81031 | -52.27702 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e5da565-c7c1-300d-8b3d-c63d49bbe2b4 | -3.88635 | -50.23665 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b839123-c05a-3eb4-b86c-71fe8f88a7c5 | -4.62836 | -48.91056 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a739f6a9-05bd-35e0-bf0a-4d40a0f7ca5a | -1.51338 | -52.1665 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 650653fd-7dbb-3018-bb15-f54b7649617c | -2.17522 | -50.97325 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b85f7b9e-2939-3116-948e-ef44bda120b1 | -1.66677 | -53.79144 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b10d886c-fa70-3201-ac81-2397e41585ec | -3.11091 | -53.71178 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcf76b0e-2218-384b-9305-a1a92fb3a7a3 | -4.77381 | -48.91486 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0755ce85-1399-3b0b-8588-f7f2632b17a2 | -1.45871 | -53.41739 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b84e5e9-9845-3ab0-abb4-feb1b1b60a74 | 0.50411 | -50.68947 | 2024-11-09 04:55:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a4ee658-6721-3639-afe9-c7d88fcebffe | -4.20726 | -50.62496 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5229498d-453a-3b09-80ac-63a0e2972f41 | -3.81645 | -50.78418 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 170a9a66-3f9f-3fad-bfaf-f4e487ccbef7 | -1.73187 | -52.37132 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f7adf8f-0f26-37ae-9676-b28ae55e3344 | -1.64792 | -55.31679 | 2024-11-09 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a25a5481-8908-328a-ad35-737a55d3feff | -3.08021 | -53.37157 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 156c1dda-9b56-3ded-a43a-9ebc84c40790 | -2.45332 | -47.16546 | 2024-11-09 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a260f2-802c-3cd6-8772-fb277622fd03 | -2.58411 | -51.92356 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f5a0862-ab2b-32c4-beed-810e1122ac42 | -1.41059 | -54.50118 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de4a6c9f-e583-3a74-b966-72a60db988a6 | -2.32792 | -48.57149 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab4cc02e-8d8a-3aa3-85a6-f151f0a111fb | -4.06878 | -50.011 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7daa04fe-b0a4-3e99-a24a-214c3ac47067 | -3.57746 | -50.55273 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dfe3fdc-df56-35c1-b4cd-4604b77114bc | -0.54762 | -51.79147 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df6ef72-901f-3405-8239-7ba14d5af256 | -3.07448 | -50.47802 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66d493dc-b5b5-390f-ad00-1a082c8dbb69 | -2.88123 | -49.39825 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d8ffbdb-adab-38c8-be9d-e9b3f8d421eb | -4.88482 | -48.63858 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09984659-666f-3b68-8861-05f7ade5453e | -3.25425 | -51.12891 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa8ff445-56bc-3ce7-94bf-e7803cadba4b | -2.77225 | -54.72378 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b969113-a9c2-313f-9bac-9941d8da39e9 | -2.83482 | -51.80049 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4015d8cd-96f2-338b-8e0a-ca1ef99f4c18 | -1.22869 | -51.75521 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c815e54e-4ff8-30d1-abca-1c88ab5f40a7 | -2.8758 | -50.4122 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77669c5d-6882-3a70-b44b-6d217a9f491b | -3.55546 | -43.57348 | 2024-11-09 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| afac4f45-a1ab-3c41-8f6c-fb415c059f14 | -3.62158 | -51.54498 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00603780-a792-3e38-9cad-3d60dfaae3f5 | -2.28958 | -50.47089 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed509904-cb7c-3aaa-91ef-9242c40fa7d8 | -2.84331 | -51.81288 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbd2cad6-a65e-3a5c-871a-7923dfb1dfa1 | -3.91561 | -47.95305 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6278b309-87bf-314e-ac7e-3f3201e4fc37 | -1.49396 | -54.39352 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8c8bfd8-6fe1-31a7-aae4-6f69d860d8ed | -2.25549 | -50.53163 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95c40d8e-6663-3989-8781-69456d956a74 | -2.93978 | -51.06288 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 154569bc-4d37-367a-b90e-1ca84881f404 | -4.02012 | -46.18764 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1902b9dd-082d-34dd-8e14-f3a78eaa52dd | -4.08782 | -48.50883 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d76dd171-ae39-387b-895b-7b6baf7c8e87 | -2.4143 | -48.52575 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9262938-05cd-3cfe-8839-e9213a1c18cc | -2.87376 | -51.48173 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf21fd76-1cfc-31e6-9e22-2af16454f5ae | -3.124 | -45.95431 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53ef3237-1b5e-329a-bf40-1c99ce9daa27 | -2.16684 | -48.73147 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16796a10-ce28-39b5-8e53-19d7d807a8c1 | -2.31426 | -53.61536 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c27ab210-4f56-3673-9888-794b457ce52e | -1.38362 | -51.43494 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5149a88-34bb-36cf-9526-799916f81c99 | -2.57058 | -48.18472 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e86c2503-c417-3f47-8908-cdfc95a6a00d | -3.00909 | -53.43464 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57cff305-fffd-368d-82c6-96826eb3683a | -1.33927 | -51.42469 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f0cfe6b-f00b-3fbb-b42c-6efb5510c851 | -1.12363 | -54.21508 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cb6632e-1609-3c9e-96fc-1eca95002a99 | -2.20111 | -51.94456 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63c87bcc-64ca-3c66-a683-da5f8701b294 | 1.08538 | -51.30046 | 2024-11-09 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da70a393-d3d6-3c4b-9447-d9d4b48d0c70 | -3.70489 | -54.34633 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b3e7526-a30d-32c6-a7ae-8cb7477c84c7 | -2.61907 | -51.29982 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e809db96-b462-3be5-91a7-c5f51ec99120 | -2.09962 | -46.21197 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2104cb2f-6865-37e4-bb91-66a421040fcf | -3.74964 | -51.09885 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68afd05f-d875-369f-b42a-0f9d1316dad8 | -3.28519 | -53.68251 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 222ea55e-ce83-3d13-bdd1-ed5c027d87d2 | -2.20954 | -50.73218 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 580365a0-552b-3ba1-9a53-fbeef0134162 | -3.02452 | -51.00937 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e0dc478-746d-3cd4-bf98-af071f4a2409 | -5.13261 | -50.61091 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f9da58c-0339-38ca-9188-dc2f726aa2ed | -1.5495 | -51.8483 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a2cc528-8f17-34fd-9027-f3dd8f86fe0b | -4.06943 | -50.66494 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78f9164c-564d-3699-9ab0-8a9df343c7f1 | -3.19407 | -48.65746 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da210da7-daea-39d6-b31c-a0a91e96200f | -4.14166 | -54.98843 | 2024-11-09 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76625dc5-b6d3-3336-a9b8-0d629236eed1 | -2.56898 | -47.34497 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62f2c355-cb06-3ad2-8dbb-fe6bb567474a | -3.11341 | -51.28985 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 988ad6f4-9a25-3ae5-bc12-1fa4f035776c | -4.43655 | -49.61594 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe4bf0da-da8a-3fca-a745-3c1819da4d6c | -3.35053 | -50.25719 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef66ff40-3e70-3214-a022-cd40bc4984cb | -2.89255 | -49.40003 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f514024-55a0-306c-ae1b-1ccd8732d447 | -3.04345 | -50.36935 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb9fa24b-480b-38ee-8b6d-6a137714ffc7 | -2.82024 | -50.44069 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2372c4ba-ef5b-3d0a-9209-a30e2f527457 | -2.21365 | -50.72885 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79b3dc85-21e7-3e84-aa20-0f7f5924a2ae | -1.35845 | -47.3207 | 2024-11-09 04:55:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84c1f1c7-661d-3bc4-9d8b-3fbab1e0e306 | -3.96117 | -48.13704 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 509850a0-14c7-3c7c-a6e2-1f8c6440813b | -3.52874 | -50.87194 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d83c68b7-e488-32bf-9b35-5cab754ac104 | -0.89058 | -51.77604 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1726dad0-059a-3772-8359-a2ab922df2a0 | -2.91496 | -51.03954 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da3a08e8-dd48-31c5-8f00-f555ec177e6b | -3.28614 | -53.24463 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92dfd7e1-0395-324b-b029-6f9a8e9933ac | -1.51787 | -52.1815 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9013ea75-f06b-3d7c-ad36-f1b3c65bd526 | -3.54889 | -51.53762 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6b1a625-26e9-36d3-8c8a-0093a2f0dd89 | -2.29744 | -49.10665 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06bd3e47-c446-3e41-ad2f-d00e628965bb | -1.54559 | -51.85131 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5dc94a2-9372-34e0-9f6d-481a0f582932 | -2.38615 | -46.78224 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b34790-3cdb-3000-ab35-fe76ecf7aeb0 | -0.22338 | -51.63309 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7a0d66-1ff9-328a-a573-2b3ba7365861 | -1.39951 | -51.59928 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d1f4b8f-3565-3527-9f2a-6b3af6bc7822 | -2.63841 | -46.79274 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b74efbad-d4a8-3d0e-933f-22b89701bce0 | -3.57003 | -53.52591 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5061212f-8593-3050-aecc-c8593e2bc3c1 | -5.68846 | -46.43541 | 2024-11-09 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e254984-b090-3386-9f3d-301459f610ac | -3.88206 | -50.24026 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48405aa6-34ee-3027-b0da-6cc8eb35f300 | -5.31648 | -50.69963 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ec75f96-2b79-3fa9-8b56-f7e16bffdb74 | -2.66335 | -48.49426 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 627932d8-b5f3-359d-b4a2-2def6b81ba6d | -2.25342 | -52.21251 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README74.md)
