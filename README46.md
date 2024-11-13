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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e372bd08-e76c-3b4c-a631-337eb7f3f9b5 | -1.25393 | -55.69079 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eadb1bf0-ec6b-3c69-9abe-15a85c6600bb | -2.45948 | -53.69546 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c5b536d-ed5c-31ec-b6e5-34cf0198327b | -1.89195 | -54.62 | 2024-11-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e63a333-0e37-3b80-b3e3-93237b425110 | -0.28192 | -51.66754 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6269e46-f799-3c80-bccf-d99a8917e77f | -1.64044 | -52.5339 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3c94db6-c52d-3330-a62a-253b883c6296 | -2.37036 | -53.85993 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecd8daf9-7fee-3ed7-a96d-00854781a3e5 | -2.11832 | -50.68791 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dbcc9d1-0639-31f5-9453-dc9d475f5840 | -2.24106 | -53.74452 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 887d1cd7-b3ed-32d3-98ed-9e49d72c4827 | -6.9458 | -52.86265 | 2024-11-13 05:22:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2740b57-bef5-344d-b697-1eb529d62572 | -2.83263 | -57.09992 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd20906a-3d8a-3ebe-bd86-ee5833f7dba7 | -3.76542 | -54.65573 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26237f10-ffd2-3c27-9394-301925255178 | -3.66525 | -54.65926 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0467e3f7-62fc-394a-bb87-00147bc58632 | -3.2375 | -50.67171 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b4de8ab-159d-3bf2-9754-3cecedd396bc | -3.21652 | -50.38697 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 969c9b4c-12bb-377a-9129-10942f440f61 | -3.52204 | -54.48046 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0b67cda-be96-3653-908e-4278eccbb3e4 | -3.52149 | -54.48416 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99d9ce46-6d65-3e71-8628-af52287f1529 | -2.93364 | -54.45766 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 719f586b-fb38-375e-91bd-c072f5967398 | -3.35111 | -48.95239 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8a3e962d-c6ab-336c-ad61-4fe859c6f3f7 | -3.31228 | -54.91386 | 2024-11-13 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36976fa7-0391-3c54-bea1-f31d9b6733c8 | -2.66371 | -54.08068 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b5a9354-de1b-3cae-9612-7286ddc8a4d8 | -3.02685 | -50.97445 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c6588e9-9441-3c23-ac80-905ac65e5555 | -3.66933 | -54.65984 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdd33449-d488-3733-8af6-9547050b5d47 | -10.73407 | -49.52 | 2024-11-13 05:22:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 37cda500-f9ff-3bd6-95ae-194a4be22fb3 | -4.16279 | -59.90802 | 2024-11-13 05:22:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d47407b-c16c-39f1-967a-37b4af9d6df2 | -2.37244 | -55.7612 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88751b7a-3fde-36f6-b092-21042f4b5390 | -2.99714 | -51.03058 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae94e3d6-2b42-3898-82e3-8768af112a05 | -3.53384 | -54.48613 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aba64405-2d2b-35b0-b833-d1fa25df371b | -3.15213 | -53.2454 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d07c5192-5ac6-327f-aa98-c612446f2d7b | -2.62121 | -54.27388 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04433fd4-17fe-3b21-821b-e4d0fa3c306b | -3.27256 | -48.75208 | 2024-11-13 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84d76127-6d8e-31f4-a5b6-baf2f107b809 | -3.25042 | -50.30993 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95f503e3-e34c-3dc9-8617-fffdc62f4e94 | -2.99574 | -51.03989 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7a6e2ddc-e029-3fd0-9fe9-afcfb13703ff | -2.98271 | -54.59325 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2eb9697-01d7-3ff8-84ab-e5f387c5af5b | -4.42672 | -45.95307 | 2024-11-13 05:22:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4a21b19-bcbf-3bec-bcfb-4823da6fb9ee | -3.34275 | -48.95469 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 84d78160-90c0-3c3f-a953-152574e7ae67 | -3.98091 | -56.2426 | 2024-11-13 05:22:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e517809-154c-3405-93ee-7a246dbe0973 | -2.6679 | -54.08127 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95c65729-1870-3128-a5ba-55ba223e5b72 | -3.52917 | -54.48916 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1f135ee-5b8b-3ba0-b04a-461e611a3aeb | -3.25948 | -50.39682 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90ce80cc-af62-32a2-8b94-3429d6b965ce | -3.73173 | -54.43213 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7c3b418-f0bf-3a9d-abc4-a3cd6a3f149f | -3.87982 | -51.1734 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc404f8c-cd80-3fa4-a342-17bb7ae5bcb2 | -3.25405 | -50.39603 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0fc5f52-f649-3955-992f-c8eaa09fc6ee | -3.06797 | -50.33377 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f4090763-5470-3b48-8457-bb444b11df58 | -3.10628 | -54.29584 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b2b6dd2-8afe-3120-b6d4-2acf7f97a155 | -2.8977 | -53.0528 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0529520d-91d2-3b3e-85f0-48beb64a5339 | -2.77095 | -54.73036 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dae475d4-dd36-323e-b625-a4ef2fb82845 | -3.25848 | -54.52864 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb82fd42-12a1-3b15-b7cc-a26a06e93606 | -3.22539 | -50.67991 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4a16ffc-af80-36b5-a226-84362d5e23b5 | -3.62437 | -54.11374 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8784264e-b585-320e-8fe7-c9f47f2a353e | -3.67341 | -54.66045 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93a0dc0b-200a-38ee-a96c-bc6c4ffa2044 | -3.05114 | -50.33472 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c4327ccb-9d23-325c-88da-66eec4a7819c | -3.20096 | -59.69733 | 2024-11-13 05:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44912792-b8d8-3de2-b177-a8928b20698d | -3.50322 | -54.68946 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e21916c3-7309-3be6-8626-cf6d4c43dee7 | -4.66051 | -47.43456 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 50044d27-01c1-3a99-a977-4781310fb555 | -3.85598 | -49.11716 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d27ac123-0f08-3715-87fc-185ed1a1e9e1 | -3.66169 | -54.65521 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e569cb66-c741-3a8c-93e2-8aa68d34744f | -4.7815 | -50.55402 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67f2266a-72a7-3753-a6aa-8ff63886f83b | -3.30021 | -51.59422 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb11a3e8-2114-353d-8745-c738f18ca68c | -3.81895 | -51.26028 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bde63f1c-c67a-3fdf-8e74-71170584e3d8 | -3.14944 | -53.24757 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0e6c1b5-3d58-35fb-8c48-068f9e88c1d7 | -3.81808 | -51.26618 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b93be9d-70a6-3f29-b94a-6c57d779d900 | -3.29537 | -51.59282 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f53a91bc-aa7a-37de-9688-c15ff189f9ad | -2.992 | -51.34133 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22df7b2c-830f-381a-97d4-17c813f3f040 | -3.70671 | -53.75173 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68de3a8b-0126-37a0-b649-d8ffd0a835a4 | -3.23799 | -50.66838 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e5f77d6-d064-379a-9a6a-b9edfc2237c9 | -3.53273 | -54.49347 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0a7f0d53-92a3-36ed-8ce5-69130737e7c1 | -2.59626 | -54.24372 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 844bf88c-3af1-3f89-87d8-cbe55b1b127e | -3.05556 | -50.34257 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1615a8b6-0d3e-30dd-a17a-b36f3a22a31e | -2.86824 | -54.20829 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f182c5ab-c334-3271-84a0-d1007983b4ce | -2.7153 | -57.34261 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 427bbadc-f663-3268-ac9d-38d5a5fa5897 | -3.17325 | -50.4542 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee9d3563-470a-370d-aff7-525343f7defb | -4.21703 | -46.4528 | 2024-11-13 05:22:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8231f9c-5ffb-3075-8a90-dbdb7a3fdd33 | -2.74404 | -58.18504 | 2024-11-13 05:22:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89d8a803-dd44-365e-89af-f7f67492df40 | -4.77601 | -50.55314 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d16aa84c-d1e8-3ac8-9064-d97a14ea7453 | -3.76652 | -54.64856 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1540127-875f-36ff-8462-d4a7e68750a3 | -3.25012 | -50.39666 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21821127-8446-3007-b128-14327dedc79d | -3.34205 | -54.18714 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c85d6496-6516-36e0-a266-b6ef21a8a443 | -3.62367 | -54.79499 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e0a6a8c-5263-32c3-9b56-9837f4db1db6 | -2.99246 | -51.33831 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77cba25-caa3-328f-96a4-d344f4af2767 | -3.10573 | -54.29953 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8feed7de-3516-3a65-a409-a156156cb177 | -3.86485 | -49.1205 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| faf08e33-59cb-3e51-a2dc-969bd8dfd9bf | -3.66578 | -54.65576 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74116c08-c8d6-395d-8ab4-ee75b45c0af6 | -3.73588 | -54.43274 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e36ed74-384f-3676-a16f-902084ddaeaa | -3.70598 | -53.75242 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca0b47a9-e710-3bdc-9269-1a8d2b4dd8c3 | -4.33416 | -50.4274 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45b7a63a-3b67-38e8-bf9d-fff33a8815e9 | -3.16836 | -50.44987 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c3335474-e262-34e8-a86c-151e401b35ef | -3.73116 | -54.43597 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fc5abfe-a1e9-3441-a84b-37265c431316 | -2.99195 | -51.02978 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8262de45-ff56-359b-90cc-a1e1be2a4298 | -3.49975 | -50.84442 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76c5fbb2-0168-3abf-a433-f67e7fb6239c | -3.14553 | -54.48185 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcff2a67-759b-3535-9b63-26422a5c6b5b | -3.31123 | -54.91221 | 2024-11-13 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30c7b5b0-061e-3c24-895e-013cb9dfbcde | -3.85664 | -49.11272 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8296223-8a2d-361c-bccb-2d654732f225 | -3.15907 | -50.58708 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 77182b2f-64a1-3ffb-b379-2e1608f80bf1 | -2.99667 | -51.03369 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 919e5a34-08b5-32c3-8d62-07ad31b5b99b | -2.89073 | -54.17322 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7c70738-eddb-36be-a5f5-7df04dd89b4e | -3.98176 | -56.08126 | 2024-11-13 05:22:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4465b002-93ed-39a4-ab86-54991421aac5 | -3.34565 | -54.19176 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ca357ce-42f1-3625-8c7c-7459702904b4 | -3.71105 | -53.75234 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03be30ea-abfb-3c4e-8794-088fa327d5c7 | -4.66417 | -47.42574 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 028de46f-db05-33ca-9205-470e079b70b7 | -3.04517 | -50.32738 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README47.md)
