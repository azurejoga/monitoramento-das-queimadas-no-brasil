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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee5dd57c-8251-3a7f-b816-88af4d2d98f3 | -3.93666 | -52.18486 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ae26bf6-1918-37db-b89a-f9a7925c01a2 | -3.13318 | -54.36488 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e399bb6b-2f1c-3b69-adc8-db4344b469fe | -3.21917 | -53.88515 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebbc4c60-2cd3-37d8-a316-70480e8f9b5f | -3.47803 | -59.46553 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7bd9035-7554-39b6-ba42-2338487d2eba | -3.5104 | -59.94963 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8dcc2cc-031c-30be-80b1-217264a406e8 | -3.09303 | -53.72451 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 881ff020-026f-36fe-8f00-b91c2d3e2a05 | -3.62337 | -55.27915 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d695e7f0-4018-3632-8328-a5d4e2bc8b23 | -2.94124 | -54.14951 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1c98d638-378f-30d6-ac43-52609dfce6e6 | -2.60178 | -59.37862 | 2026-10-07 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99967110-9b20-39d2-b1ca-701858307d4f | -2.94592 | -54.1502 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2b88e6f-7030-3580-b5c4-193c66d79d42 | -3.12924 | -53.70604 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5c619c4-6a83-301a-a8c9-4e2798aa0c58 | -1.8036 | -57.10035 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf899976-0a33-3651-b838-cb0517603fe4 | -1.29276 | -54.55445 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d9895e-d756-381b-b9a8-ef538c0efa92 | -3.56388 | -59.49738 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c476085-60bc-3cce-9909-2245848ad5ff | -3.47886 | -55.42928 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 340f3874-7cfc-321f-abb0-7f786467c82b | -3.09487 | -53.7382 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccf5bdd3-41f9-3858-8360-3788bf29f9fd | -3.27692 | -54.18641 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f83c86e5-39fc-3cff-a801-70dd1f7a5be3 | -3.52956 | -54.64825 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d61e274-0044-3b1e-aa00-ae01716cbf6f | 1.03428 | -59.45031 | 2026-10-07 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1116b9d7-c0de-3988-a019-baeefc8d59e4 | -2.10777 | -52.06167 | 2026-10-07 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f4048a8-de47-33c8-aefe-cc9b678a1ee2 | -3.12519 | -53.70001 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58007cdd-0863-3908-9ead-9f87b05a9ad0 | 1.73284 | -55.59632 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b9b453e-85a8-3ae5-8b62-60217fc4733b | 1.6409 | -55.79514 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a055d033-83c1-3d9d-a30a-378af0bf9174 | -3.27457 | -50.78852 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67c3d8b0-db46-3ed7-ab59-91b24070aafb | -3.6184 | -55.28255 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 34b9203a-5d1b-3054-93cc-fbe9a8d4576a | 2.5515 | -60.01094 | 2026-10-07 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c26eddd-de2c-3403-84dc-621277f025ef | -3.17581 | -50.43746 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f17b4cdc-d3a1-37da-9d37-c3de71e773fc | -3.70779 | -51.13624 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40bab8a8-91e2-3506-ac37-f298ab5848bf | -4.30712 | -50.78177 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66d07412-f422-3199-a4b3-6f000a3c16c6 | -2.20865 | -56.92116 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e73dab53-b5c5-37ef-9de6-294bf146ab4b | -3.28238 | -54.04493 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 44b73845-e128-339b-bb1b-0ca3307c753d | -3.3012 | -53.86105 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5097c8f8-0fc2-3df4-9cf3-21a2ad16495b | -3.87093 | -55.81646 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 322329c5-a07d-38d7-b5fc-09aa943d03b2 | -2.92793 | -54.14252 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88a08162-1687-397d-bb72-81c703025010 | -3.10105 | -53.76821 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acbc5519-713c-3f78-bf11-ba103d8f3992 | -3.02624 | -53.87248 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d908a3d-d236-3dae-bba2-f39826e81553 | -3.52341 | -58.75913 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae9e04f9-b8db-3784-8b0f-f79f2b3ae645 | -3.2879 | -54.04061 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21c292c3-25cf-3181-a660-d0e31b0ee452 | -2.82462 | -54.13322 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c39c7af-e93e-3e5f-95bc-6bb4edb3eff5 | -3.05353 | -54.14983 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5129c318-416e-3992-85b9-d43a73611517 | -5.01852 | -50.94215 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb6e9436-2624-3759-bc71-974dfdd3dc71 | -3.5132 | -54.63419 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a10424d3-ef07-3262-aa1d-6ab6dc496957 | -3.11066 | -53.76974 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1502becb-51d8-3b32-8582-5ab1e4a719cd | -2.55236 | -57.38992 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c972a9f1-72aa-328f-80dd-8a17a242130e | -3.12688 | -53.69752 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d640c743-a692-3a71-9e52-dc02bb4ed45b | -1.28767 | -54.55806 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b14a1105-fef2-387b-b270-d5aec3b79454 | 2.44094 | -50.85234 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0efbb7ff-b0b6-3f0a-8cdc-774499b3f318 | -2.87355 | -54.14252 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0820ec2-e84c-3b24-8f4d-2ffe557d5d7a | -3.35104 | -54.17242 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42cba615-d1b4-3a13-850c-d1a2f5829349 | -2.99539 | -54.10792 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4c59df9-f71b-3f02-bba4-305be3c2eb73 | -3.54753 | -50.0908 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e65afd2-e2fe-3d03-bcf1-f2ecc0f648f3 | -3.39356 | -59.51767 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3ef1f001-1663-3175-9bf3-7f8ba7166273 | -2.88115 | -54.12395 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b414016-8928-337f-957d-24f5dd74cd02 | -2.93621 | -54.11885 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a6754db-10a6-38ea-a05c-b9ecb72f71cc | 1.73365 | -55.60133 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14553e15-2fc5-387a-b310-2b811afca833 | -3.27852 | -54.06968 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2bc8560b-96ea-3c88-b759-e2a49268a115 | -3.09905 | -54.29028 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 26c5dfbe-6285-3660-be6c-0aa94e85f667 | -3.5381 | -59.48195 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35a3fab6-0a86-3648-bae1-dfa7446d1a44 | -3.67479 | -55.94818 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c02b21ad-1430-3aec-b60f-0d9c38a5002c | -3.28028 | -54.06668 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 439f64db-faaa-32a1-8e26-0776223004b0 | -3.47086 | -49.93555 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82234201-7b5d-324a-a99f-f931cbcf343e | -3.20732 | -53.87153 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d975d2e-a384-3e15-ae22-663183830430 | -3.27235 | -50.42327 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41dae2ac-e233-3beb-aea5-1c719a100977 | -3.28868 | -54.03558 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5b4189a7-fbc8-39bc-8715-a6e274d62375 | -2.59771 | -57.54576 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b1f84f8-284d-3113-95e5-e940cfb3fe3a | -3.03436 | -53.91529 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36b3489a-a191-32d1-be06-4b545a557ede | -4.24555 | -50.73016 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff29a62e-b8c4-32a6-8670-bffb8a8a0a9d | -2.10195 | -52.06408 | 2026-10-07 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0732d24-2adc-301a-8b1c-f645b843bbd7 | -2.99252 | -51.05612 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d390dd8-2f07-3c5b-8aec-6e542b212d31 | -2.88583 | -54.12467 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46ac5a3b-48d3-3847-bb67-4a2b6b9f84c0 | -3.30066 | -53.8625 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31027142-70c6-38d1-b1cc-f2b5985e6253 | 0.66739 | -59.56494 | 2026-10-07 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d220b341-a670-30c8-856b-cbb29467a1e6 | 1.81841 | -55.53487 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e604f8b9-b8f3-37a5-9536-d295b5d91746 | -3.85897 | -55.98348 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43220423-d49e-374e-88be-17759cf2dd1a | -3.13913 | -51.02716 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 557b9482-88bf-340a-aa9d-e87a390c7542 | -3.13852 | -51.03126 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee5b4229-7a73-3e28-aa87-923647d29407 | 0.72461 | -51.37318 | 2026-10-07 05:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ee4db8-1430-3c4a-aef6-33ce6c181ed0 | -3.27687 | -54.04921 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| cdb47155-b4ec-3938-8f73-8038e775f358 | -5.01314 | -50.93714 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2c3571-3dbf-31c5-8e34-a3d37d07ddb2 | -3.50632 | -51.68908 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0ca7e1a-f5ad-3f8a-9745-6c95a8fffa57 | -2.86817 | -54.14653 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fbd0c8c-445f-3bbd-b0e7-2cdaf8538174 | -3.28024 | -50.41663 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e4cdd9d-8537-324f-8698-123d431ab7f0 | -2.87214 | -54.15182 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1525f258-9b2b-318f-9a6d-5be3e875fccb | -3.28796 | -54.04752 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fd65908c-6c7b-3c7c-ac4e-506a02c5361b | -3.41375 | -58.91193 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d060546e-2752-3ae4-928a-e5f486364397 | -1.28558 | -56.98457 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a90b39ed-fd82-373a-b275-11c37827126a | -3.03912 | -54.25791 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78ed5f55-4858-319e-b4ec-866c7decf58c | -3.1059 | -54.27665 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18f831c4-0365-3d35-b7ca-34266e6a2bae | -3.86201 | -55.9917 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d215938-143f-3af6-b973-b58a0620b17f | -3.63654 | -59.5427 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09b34c0b-c2cb-34c3-a73f-e6eee81075e3 | -3.22818 | -54.30103 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ca78f80-232f-3eaf-a6c1-4c34826a877b | -1.79982 | -57.09976 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1d1ebe1-c718-3d03-bcba-051295f620c5 | -3.10025 | -53.74161 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17c2cfe1-d130-3003-aaab-2a0b383ff886 | -3.01115 | -54.1304 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8ddb27f-ba3d-3e81-b863-2ec6e70aac46 | -3.29372 | -54.07382 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5e4b063a-acfc-36c3-a172-2b3ba53d86de | -3.50687 | -51.68541 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 791bb3c9-21f7-3dab-a450-c92dc0b5e9c3 | -3.28974 | -54.0681 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4cca8ab4-e856-3f78-a582-4df1e3e47323 | -9.14193 | -65.29684 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32b03797-5457-3183-8ab0-4271845fe634 | -6.44491 | -55.01663 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3ce0e85-d58a-3491-91c4-e44fd73f267d | -5.67708 | -53.49382 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README111.md)
