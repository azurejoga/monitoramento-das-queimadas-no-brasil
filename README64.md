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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae98bed7-b259-3313-ac15-1d2efccbb564 | -4.18933 | -49.40521 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c9c8d6-eee7-3075-a7c1-0ec19b8513e1 | -4.18655 | -49.40121 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b909c926-4123-37a1-b7bf-6582465880ec | -4.186 | -49.40469 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c89aeaf6-a684-361d-829e-6bf52534c95a | -4.18498 | -50.66385 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5e69d6cf-bc2b-3c20-96de-98d722620d65 | -5.8735 | -49.90599 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4789a758-e1f3-31d8-98db-5e73d260abb0 | -5.795 | -50.16343 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01a5cf89-97d2-3274-acd1-cd080e957dbd | -5.7894 | -50.17699 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13fd95a1-f768-32b6-9480-a6568d5606f2 | -5.67851 | -49.95784 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f68622-81cf-3578-99a8-8b0804418d53 | -5.57664 | -51.05103 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17e7f8f2-5d68-3b79-83f7-2659863f8edd | -5.5552 | -50.43902 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01c93274-5159-3ee4-8fac-e56b3b662a8f | -5.5211 | -49.80069 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4e9326-8c19-3c8b-828f-1d2a6209f56e | -5.36181 | -50.93036 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ebf6d6a-d1ae-3047-8f2c-e9cabbae3f3c | -5.35838 | -50.92982 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17250f65-3aa6-3c8e-90c6-be794b61d78a | -5.30798 | -50.56627 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f1f33fc-3389-39f7-999b-eab6f6909dfd | -5.29683 | -50.98463 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d46d33f2-d9aa-3445-a1ce-10ee93591b9f | -5.21637 | -49.99662 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd407027-6dc7-3bd5-aece-87a3f31a8a09 | -5.1801 | -50.07396 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0a2ba88-15f5-32a8-8682-99c316e775ec | -5.11264 | -50.71795 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e53f949d-40e4-3e89-a9dc-120682f6c712 | -5.11228 | -50.72122 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fb8e5d1-8dd9-3f07-bb34-4511b623f9e6 | -5.1109 | -50.72894 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6d5888b-e1c7-32c6-b98a-de7f01ed8a28 | -5.10865 | -50.72107 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7009760-537e-38ec-982b-67814bc25504 | -5.06547 | -50.44647 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b129f71b-fbf4-37aa-9501-110409a96b67 | -5.06489 | -50.45005 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d37dc64e-4893-3807-a24f-4a20386c1908 | -5.79834 | -50.16396 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c58b06c9-4bf4-310b-93d4-0a0b5bd05eb8 | -5.75413 | -50.22579 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a8eff45-3175-3261-aa3c-74f6ba48fc8b | -5.75407 | -49.8265 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21b1c97b-3b97-347f-be50-223bcc6c1eac | -5.67629 | -49.95031 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97377dc9-1001-3f95-8afa-01c173412e03 | -5.65888 | -50.0808 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da3c3259-8147-3bc8-bd40-8aa9b81d5a28 | -5.47648 | -50.14624 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61e25d18-7d67-3495-8e61-cd7e99d29036 | -6.41868 | -50.78881 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 304155c7-ab04-35db-b3c7-4f367171d50d | -6.41588 | -50.78461 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f49b3b-395e-30dc-ac39-7f041015370c | -6.41531 | -50.7882 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef007a7d-daf9-333d-b29d-8400ad4eacbf | -6.41471 | -50.79187 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a01664e-80a3-300e-a3d5-381eea9b5e3a | -6.41193 | -50.78761 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0b3a5e2-5dfe-3f9f-a782-b687324112c8 | -6.41134 | -50.79129 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a90fd3d5-bf28-3ef2-b2cd-93be8659202d | -6.22663 | -50.87428 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45674dc6-5169-396e-83ef-286896c0c78a | -6.22265 | -50.87734 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f56b330c-25f9-31d3-bb0a-a252efdffa16 | -6.21304 | -50.87213 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd0646d2-c30a-3a36-a4c7-3d634567e65d | -6.17508 | -50.86984 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ae49d94-b1a0-3eb9-b3ff-e7afc765f55d | -6.17449 | -50.87347 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 633ed6e4-1897-324f-bdc3-0849036ee54f | -6.1711 | -50.87293 | 2024-10-25 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7597779e-d447-38ca-9de8-08ee15bb1fb4 | -6.10764 | -51.11456 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfcb84e2-63e1-3a63-a899-c7e29359eaa2 | -6.1042 | -51.1141 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb395961-12b8-36e3-b03d-17cc096eef21 | -5.926 | -51.04831 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5041de6-8fa8-3cfd-8ce6-20d8caf68e47 | -5.3046 | -50.56572 | 2024-10-25 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 201af64d-7f00-3237-8cf2-7c8d6dbebdf2 | -5.25844 | -50.87648 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38598f66-81cb-34ad-8684-a0930eb11089 | -5.11287 | -50.71756 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 420fdf4d-0f45-31ff-b4ff-84717897c1e0 | -5.11206 | -50.7216 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ae7094f-47c4-3f95-855b-140dc5cf51f2 | -5.11169 | -50.72488 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96498e7d-7d51-3522-a745-342375509c9d | -5.11148 | -50.72527 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e2ea1c3-837f-338b-9b13-9d39a2aa03ee | -5.1111 | -50.72854 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0363c1a1-3a0b-318c-8013-100336f7fd21 | -5.10923 | -50.71741 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be96a663-0755-3e24-a306-93bdce30186f | -5.10807 | -50.72474 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e89ea9d8-edc5-39d5-8c0d-757e59e9bd59 | -5.0084 | -50.84456 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e47eb743-a925-3771-b646-2a262a217be5 | -7.81175 | -50.22876 | 2024-10-25 04:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28b617ed-475f-3ca2-83ae-1d8401306327 | -6.89635 | -50.32755 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdd3e82d-405e-3e25-ad75-0c63bd404964 | -6.68462 | -49.97373 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d37d6cef-0454-34fe-bc2c-ff0b04fc62ec | -6.68407 | -49.97721 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f75358f1-0d9a-30f7-abd6-f22298335a2a | -6.68351 | -49.98071 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9c9a2f67-e75a-3085-93c1-03e548dc9eda | -6.68129 | -49.97321 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ddeb44d4-1982-3284-b8a9-e8ca2b7c5425 | -6.68074 | -49.9767 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab76ddac-6c90-3584-ba51-8196a2ab0aea | -7.56697 | -50.70624 | 2024-10-25 04:38:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 797ea88d-48f9-3d62-8345-b20c45d8b448 | -7.4485 | -50.78999 | 2024-10-25 04:38:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bd41d23-5ec5-3507-b200-90c800100b08 | -7.44571 | -50.78589 | 2024-10-25 04:38:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8500ec39-3a30-31b1-ab7d-d14d41bfbc50 | -7.44514 | -50.78946 | 2024-10-25 04:38:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23cf5f6f-5142-37cd-86f2-3003f929d9c9 | -7.44234 | -50.78535 | 2024-10-25 04:38:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 746f1ad8-d60f-3f9a-a5f3-ae7696a08b73 | -7.02994 | -50.48238 | 2024-10-25 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef6d3f47-728e-399d-af10-9eb1493552f6 | -6.8182 | -50.86314 | 2024-10-25 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 322a33b6-91ce-381f-884a-de5325c1b225 | -6.81481 | -50.86265 | 2024-10-25 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 58ab05a8-f920-37de-801b-08566b22cdbf | -6.81085 | -50.86572 | 2024-10-25 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 050fdc83-4481-31c0-a2a2-e2715f854d4e | -6.80632 | -50.87239 | 2024-10-25 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a50fea04-4c97-372d-9ce2-8120ee912e1a | -6.80575 | -50.876 | 2024-10-25 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8339fd97-a834-3d13-90f8-739b45cfcbfb | -6.53431 | -51.13261 | 2024-10-25 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d17829e-1301-3cd4-9f33-a13d14a38412 | -6.43602 | -51.28429 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcf8e253-deff-3305-8967-fa77c0b630bd | -8.17893 | -50.15427 | 2024-10-25 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f55d80ff-4b2a-33a3-b392-15d1c4ba2758 | -9.35987 | -50.64191 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ca5bf01-9bcc-3a3b-9289-5ba1b3a40aae | -9.2549 | -50.68666 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f59921-e796-3bb1-937c-108adc205832 | -9.25434 | -50.69019 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd8c7a8b-64b5-3376-acd6-ed2f1f3ef2fb | -9.251 | -50.68966 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7796cf41-fd8c-3770-a138-e2266f123871 | -8.89873 | -50.58957 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee425890-8e38-38ed-9962-2713173ae31e | -8.1756 | -50.15373 | 2024-10-25 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac03be91-574f-3ad7-95c8-4e2e3efa6ab0 | -9.36043 | -50.63839 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b7af377-67b2-3276-bcf2-eae0ab4ed0f5 | -9.25156 | -50.68613 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f0c84b2-8c7d-3f4b-b719-535844218642 | -9.18261 | -50.54522 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9aa353d-7049-3078-b054-837192062d9b | -8.60764 | -50.90626 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e482e452-7b43-3aed-95d6-ed13365577cb | -9.55215 | -51.68133 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 321e9d99-ea0f-3b35-8205-0931976a558f | -2.24098 | -50.45663 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 556a1f78-a352-3a37-b6ff-d4c9d8e6cad6 | -2.23423 | -50.67645 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63ca2a75-f80b-3672-bde8-48a38b339b72 | -2.23075 | -50.6759 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04464726-24dd-334a-b95d-bf2992236e0b | -2.22813 | -50.71469 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57d03ede-0330-33b3-8c96-5e54abd54ac6 | -2.22465 | -50.71413 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ee4f8af-e73e-3b4d-95d3-8977557747c4 | -2.20909 | -50.83401 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abcf2904-bec0-33de-9e26-809da74c6d69 | -2.20739 | -50.62151 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 968e0dfa-70ec-38c3-b248-2daacafccf91 | -2.20494 | -50.63672 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e477b2ad-7d99-3fb4-807d-1b422621846b | -2.18864 | -50.50698 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56507021-69da-3c5a-9eca-aac706e43045 | -2.18232 | -50.50212 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85f39812-ab67-3a9c-be46-4542fc96a09d | -2.14546 | -50.66735 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb4d7e26-daec-3a5c-b4b6-05ba5f3d6ffe | -2.13032 | -50.83065 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 637be5c8-3cdd-38e8-b2d4-e8b57d42ab0c | -2.11116 | -50.88341 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe782609-c001-3109-b130-5c7cd7f1d00e | -3.63647 | -51.24786 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README65.md)
