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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b09a81e0-9678-3d3f-b527-2cf8e9b7d739 | -6.24808 | -55.48191 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae8aca68-38c7-304d-acde-e58a75b72dea | -6.08095 | -57.89445 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e32dc083-3948-3235-aee9-64e9ecc21a31 | -3.24287 | -60.81165 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 312141c0-eaa2-3841-aa51-08657934714a | -5.25328 | -55.90005 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 799c28e8-a3d0-33c7-bc2c-e057c9e9ea76 | -4.15035 | -60.69831 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 882593ab-5def-34e1-96a3-4b7a5c44b003 | -6.15206 | -57.78209 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1bbb5f99-dbbc-3afe-9154-474024d3fd02 | -5.24473 | -55.90378 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a1481940-bfb2-36be-9c58-bb3320937291 | -5.87526 | -57.77965 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79ca6185-861e-31d9-91e2-51feb1e41f22 | -6.93277 | -55.64021 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5270af5-42ce-39e1-b135-02225b53110f | -6.26514 | -55.42198 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d877015e-c3c1-3386-bcf0-88694c1e5e18 | -5.94504 | -57.69865 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4d56294-c894-35ff-8998-60ecef5293f6 | -3.86639 | -49.10839 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5bdd3d0-7b72-32a4-b710-77f3e875dd89 | -6.08885 | -57.91146 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893092c9-1e63-38ec-97cd-9cb09a97eafc | -5.87599 | -52.15104 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9a213be-31fb-3bc2-82bc-7d83c0a0c746 | -2.84828 | -61.97921 | 2026-08-31 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7a73ac1-a913-3c95-abf4-5aaa24187cbf | -3.61755 | -60.54229 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cf3d2d6-e7c4-37cd-a243-ef0c33298152 | -3.62485 | -60.55389 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72c51181-7b3d-3a53-a262-4b740f8b1892 | -5.25645 | -55.90551 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ad73b38a-c3b7-3dd3-a465-55db2cc99983 | -6.78184 | -55.67949 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc48c7b0-47ea-3d87-9f38-4acb10fd8965 | -7.00022 | -55.88125 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5ea2011-1a8e-3997-8797-03f64493a7b4 | -3.76786 | -59.33559 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 336ecf87-b0db-358f-88e4-11757f4d0c89 | -3.62707 | -60.56136 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa5bcbe9-9cc7-3d94-90f9-b54a1d5fddf4 | -3.8862 | -59.40023 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac557e7c-77f2-3808-988c-7526c064bba3 | -5.35271 | -56.67067 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a41d73-72dc-389c-a844-f6d67d778dc5 | 0.98873 | -59.87497 | 2026-08-31 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc68de6b-2302-3dc6-a6e4-848825bba09c | -4.15756 | -60.69588 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec1e22a3-87b2-3780-b199-40ea7f4e2a98 | -2.94331 | -60.90153 | 2026-08-31 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20ec25b8-da02-3fcd-b0f9-bd8110b0463d | -6.87942 | -56.50576 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d456c93-3335-332a-ad5d-dc78e873aa88 | -6.78722 | -55.61426 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1eb45c-05a0-3c07-bab6-e16c7c9eb9e3 | -6.08925 | -57.72346 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 072054e1-dbd8-3b92-bcf2-0b251bbd004a | -3.63095 | -60.5584 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89e63c63-5238-3715-8180-2eb2291725e5 | -3.62263 | -60.54642 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90a45502-c742-380c-8a7c-28cf1dc6cbb4 | -5.87588 | -57.77563 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d073ecff-325d-34e6-9757-f6e90c4dbfaf | -6.22803 | -55.61971 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73aa51c9-306f-3813-968f-b3d8fda5b412 | -3.86941 | -49.0924 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7aaa820-af9c-3437-ac86-d88395c9962f | -6.9363 | -55.64444 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 427b1b4c-4f0c-39ef-9b44-7b9dfd7616ba | -4.8556 | -55.83675 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 14896b88-a584-386b-874d-0a51df769e6d | -6.41445 | -58.23086 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ba12766-00a9-39f3-9468-2a0b06567fcb | -3.46247 | -51.89254 | 2026-08-31 05:33:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5aa61f4-a9b9-3e89-a2db-5afee90119b9 | -3.97339 | -55.65044 | 2026-08-31 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b247b4e4-03b9-381d-b32d-1f9101bc7e6f | -5.88607 | -57.75687 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3489af5d-42f4-31c5-8a69-ba504c9e3527 | -6.02728 | -57.74693 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89f66f5d-5804-30f0-8740-e86d0f5f2b83 | -5.89669 | -57.75314 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8673e64d-869b-3cb4-baec-bd93eebfee1f | -6.12244 | -57.67451 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 859e7700-d0ab-31d3-b314-2182d0f35f2d | -6.24777 | -55.43074 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85f2ac28-6c11-37a2-aa53-7c56141b9f20 | 0.1453 | -60.40024 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df26351-c34a-389b-be4b-7f8e485d9ec6 | -7.28886 | -52.36833 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e27b13f-8437-3e0f-a68c-0deb2dd9b7f6 | -5.24937 | -55.89946 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d4c2c4cc-e950-3dbf-b03e-3b3d431aadc5 | -6.60618 | -58.59623 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 89189429-b9f2-3e53-8e9d-8ac53b66daec | -6.61882 | -58.6059 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f69254f-9156-364a-97c4-a2c9e997c128 | -4.96194 | -56.27202 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c795e58e-fde8-3b4b-934d-a52b7eda9350 | -6.25646 | -55.42422 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb7f5819-1bbb-307e-a669-1185f505b0ec | -5.25086 | -55.88956 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4faa9804-3f30-38a8-bd08-2ff99a89b405 | -5.95946 | -57.676 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0cab3cf-ae9f-31d1-a971-04ba36e15187 | -1.62592 | -55.16807 | 2026-08-31 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f71b11a-89d1-36fb-a657-87477ad376e1 | -5.24584 | -59.7274 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1afb016-751f-353f-8ebb-803f3fea4ed0 | -5.25254 | -55.90498 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| efe99cdd-221d-3306-bca2-c3e444bc39cd | -6.12394 | -57.6783 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 372e4f42-046e-3ea6-957f-8181f4019dda | -5.89738 | -57.75439 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9616d09-d94e-3250-95be-68b221b2f8b2 | -5.32037 | -55.85411 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 984529db-db61-3f6f-a0db-e8478f1980b1 | -5.88839 | -57.76535 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a8d765d-c300-3967-848d-1de62791f0a7 | -5.9666 | -57.6771 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9895c684-cab1-3a6d-847f-19b0ad37157e | -1.59252 | -54.40249 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b1740849-b60c-3c4c-8607-a22e5a3f03c7 | -5.94689 | -57.68651 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1c6d940-aa97-37d5-9fc5-dea42c3f575b | -1.59141 | -54.40968 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 728b8ad2-5280-3519-aced-db282713db9f | -6.12641 | -57.696 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ff6fb9f-f990-37a6-b111-5e1f9229d6df | -6.01911 | -57.66862 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 435c0c2a-a2af-3372-8d16-6fb0ca165303 | -4.15423 | -60.69535 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b7e0cbb-d027-3971-a447-01befc6162c1 | -5.9708 | -57.67353 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34426c63-013d-37b7-990b-fa61d9bd009a | -1.39927 | -60.33206 | 2026-08-31 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 247cc498-0ac7-3bf3-89d0-c8623f81f9a6 | -6.22575 | -55.4935 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f2147a2-ac38-36be-a38f-04e9a50a380b | -6.77896 | -55.64241 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf6ef1e6-6493-38d9-b6d3-204895076bff | -2.98074 | -60.92553 | 2026-08-31 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e50fba52-c0f6-34fd-941b-82c69039cc02 | -5.97249 | -57.68634 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 006daf1a-9ba7-3ad0-8ec9-78253d329757 | -6.72785 | -58.70602 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87b4fee9-9ae2-36b3-aeef-66f8dcfcfe3d | -4.96302 | -55.84104 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86c0ef39-a5a9-32ad-8b22-8e456ca8d2fe | -6.92108 | -55.7189 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fbd2fc3f-27e3-37af-9de2-fd0587b3007f | -6.02103 | -57.6674 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2acdefc9-bc17-3070-9216-2d7d357e28b8 | -6.77543 | -55.63816 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17cd403a-8477-3682-84ac-80b11e42cccc | -5.95465 | -57.68352 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7acd4da5-8914-3a05-8b1d-e5543df75823 | -2.9813 | -60.92201 | 2026-08-31 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d5e3981-f8cd-35c8-8d1a-fe46f26ade33 | -6.1218 | -57.6786 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 92c09502-4261-3844-b267-1b50a34aaedf | -3.11416 | -61.23028 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9acb7497-5373-3043-ab7a-c77235f59906 | -4.96694 | -55.84155 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 835f6c9e-b902-3f70-930e-b46fe8df695b | -5.94141 | -61.33309 | 2026-08-31 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 062fe199-496d-322e-a4b3-3960f70c59f9 | -6.11927 | -57.69487 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1674215-5ae1-3d62-8946-3a0d62721770 | -4.28678 | -59.94699 | 2026-08-31 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1d408d7-878d-3818-b580-6a20f86a788e | -5.97017 | -57.67764 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b663c0f-54bb-3b1b-9246-b87251a256d9 | -5.89608 | -57.75722 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6265b28b-4697-3c5b-a039-945f1cb18afa | -6.77137 | -55.63754 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| df90c5e0-d3e4-3035-aa06-3803a8ee1783 | -5.96303 | -57.67656 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79d00426-e81e-36a5-aa3b-ca7580c8f433 | -7.06152 | -52.72065 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e45369ff-cd41-3165-bed2-ee5b52c58eac | -5.25571 | -55.91047 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 89222bab-0683-31aa-b7de-7f43b0ba55e9 | -6.25006 | -53.67764 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 619642d6-2b67-3425-8d36-c693e946dc23 | -2.66267 | -59.36897 | 2026-08-31 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ca20ff6-7a87-3f65-a923-5f7257bc5e4a | -6.75996 | -56.34044 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aaba8887-a27b-38d4-a9e6-83ddd5de8868 | -6.93384 | -55.63301 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| febb6836-08fa-3113-9005-6747ccacae7d | -1.60071 | -54.40362 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 458b0372-97ed-3f86-a031-f1c4a6975ae1 | -6.73976 | -56.34273 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 815a0203-37cb-396a-b3ff-8cc823ea9d4b | -6.75608 | -56.33986 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README59.md)
