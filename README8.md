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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 292f1560-dfb1-3f93-babc-f22abb463c96 | -4.64275 | -50.93703 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 82487fd1-8cdb-34a9-bd79-c5b9dc3ae5cf | -4.63389 | -50.95256 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d5176056-18cd-3728-9dca-b7e2d8d92990 | -4.63182 | -50.93859 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 61850c03-4d11-38bc-9ea8-7930451faf31 | -4.42306 | -50.53921 | 2024-10-19 01:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f4477646-2b0b-338d-9024-05b47c762e16 | -4.41174 | -50.54082 | 2024-10-19 01:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 4a3805b1-7110-3690-a905-c0f03a3b1733 | -4.40952 | -50.52571 | 2024-10-19 01:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| b11fa106-9dd1-3f91-8851-5b9239157573 | -4.32579 | -50.81495 | 2024-10-19 01:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| aafbb744-39e6-364a-9449-dc6c8f8d2737 | -4.24888 | -50.99144 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 509b819a-7aea-30bf-8c3d-7edc1c713807 | -4.24717 | -50.99804 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2160377c-0417-34bb-8c49-cf5108e1c446 | -4.24679 | -50.97746 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 51382f39-f97f-314d-a1c9-73df73dd5d9b | -4.24521 | -50.98425 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 05473025-cf81-3f4a-a302-dc07d33e066b | -4.1741 | -53.56066 | 2024-10-19 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e736c7f-8e41-3589-a7de-a5a5c233fc3d | -4.16758 | -51.23909 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 82cc8a82-6e32-302d-8d79-12d50a576e2d | -4.16565 | -51.22567 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a03fa816-602c-3b76-8a8f-cd9b09c3471d | -4.16379 | -51.0389 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cd19e59d-fe5e-3d40-a5a2-7a3d55b62be9 | -4.14463 | -56.10227 | 2024-10-19 01:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c2b6b02c-aeb4-394f-ab33-c1fe47227170 | -4.0761 | -51.14206 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3706deef-2515-3871-b56f-b63ecd8203f2 | -4.07524 | -50.98679 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4b5ba895-f12d-3910-8e2a-97fd152ce2a0 | -4.07359 | -51.14876 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4f0d6431-5369-337f-942f-556992a024b9 | -4.07167 | -51.13531 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| dc82c94e-e6bd-3ad6-9e76-d646d9333089 | -3.99643 | -60.39851 | 2024-10-19 01:24:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1b6195fe-3364-3c9f-9531-7b4cfb4f65bb | -3.99507 | -60.39297 | 2024-10-19 01:24:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 91e53f3f-ce21-3490-92d1-150b8ce7852b | -3.82929 | -50.64874 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b5249e63-44d1-33f6-a691-b144374220de | -3.81487 | -51.19122 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a25a3b79-cc61-3526-8c12-961f448a8986 | -3.80841 | -51.20027 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5dcd7ec1-99ab-38d9-9672-b00bdeab47be | -3.8064 | -51.18683 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d796778-a579-3552-bad2-c4c7b78c2d51 | -3.80399 | -51.19266 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e3142b2c-3152-36ef-b7de-86a13b582d45 | -3.78228 | -51.34805 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 77640db5-ed42-30a5-b95b-77d8dc4ab494 | -3.75707 | -53.39995 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 13a7fdce-0366-3b80-9e8a-0158ef698ae1 | -3.75341 | -52.05987 | 2024-10-19 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3a6d904-94c2-391a-9c8a-282247a3066a | -3.73732 | -51.3407 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ec9f5104-de64-33f5-bb3c-84010c0fffa3 | -3.73306 | -52.13582 | 2024-10-19 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b07854c4-d669-35de-b06f-9bb735c6bb02 | -3.72524 | -51.25978 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fb253c51-f13b-3d16-b06e-9c5673b7d681 | -3.71562 | -51.12074 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 76c8f384-a5f6-3665-a633-c7b8d90996ac | -3.71355 | -51.10685 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| cdb9806e-2a40-3bd8-994d-d89567f40963 | -3.7118 | -51.11364 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| eace3826-718b-3dfd-a024-9634614dfdd6 | -3.70759 | -49.84059 | 2024-10-19 01:24:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 34aa2ce0-f0e5-3d04-bc19-1e66fde10bb9 | -3.70615 | -51.60641 | 2024-10-19 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e25b604d-5197-38b4-a2e2-929424028a4c | -3.70494 | -49.82312 | 2024-10-19 01:24:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b73561c7-abd6-33c9-bb9c-013dd6fdd2a9 | -3.70088 | -49.83008 | 2024-10-19 01:24:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0aeed370-874e-303a-8eb5-416eace6c774 | -3.68652 | -54.21465 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f8a5e69c-2b2e-38c6-b23a-c43e5ae4306a | -3.63122 | -54.67511 | 2024-10-19 01:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a0a909c-4137-364d-bf66-6dce86838c06 | -3.60815 | -52.12406 | 2024-10-19 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a85ac767-042f-315d-a1ad-391464d4c611 | -3.60302 | -50.59277 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 68bf9a10-c056-3798-8fda-d0093323e552 | -3.60079 | -50.57736 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1814e448-84aa-30cb-aef9-d7813e6a99db | -3.58523 | -48.94807 | 2024-10-19 01:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5d92029d-0096-39c5-8b15-3342662131ae | -3.54343 | -53.02071 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| faf57247-3aa3-316e-be58-fb214a1ea326 | -3.46601 | -50.36254 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| fd5d0e2a-3dce-3366-aa12-0f8fda2a1dc8 | -3.44961 | -50.33212 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 16de1371-8a63-3cca-9a02-503650991bb0 | -3.43982 | -50.1832 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3cbd231b-4d91-33b2-bdd5-8a8a647a2f35 | -3.43749 | -54.14863 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 97e41e08-fa37-3ab8-8b58-74e37fd10a61 | -3.43485 | -54.12999 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d974b488-f8c7-3940-a603-5448662d3d9c | -3.43353 | -54.12066 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7068e3e8-762f-3bf5-9881-915f232efe0a | -3.43283 | -50.21797 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| a4690a1d-283b-327f-b2d2-ac4545c03d17 | -3.43041 | -50.2015 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 8e6a36bc-bada-3015-b110-ed6b643eaec3 | -3.42842 | -54.14997 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 208ec579-ee37-3ed5-a12b-e6645a5f3fe0 | -3.42103 | -50.21983 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 937edb02-6eb1-3adc-9025-2e226697b4e6 | -3.39823 | -54.06829 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c6dd57b2-cf05-3959-b947-11f1a23a782b | -3.38391 | -50.34838 | 2024-10-19 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 635e5bce-35ed-3ca5-b507-384becf02e97 | -3.31598 | -52.85936 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 016c3374-772c-3be6-ba07-183f8e408bfc | -3.31401 | -52.86559 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c408063f-7a97-3be0-a3ba-fa4d41d104d7 | -3.3125 | -52.8548 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 56f9b8d5-9787-3828-99b5-789e24c8e35c | -3.28078 | -50.66475 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 636fb826-4df6-304f-831a-4796943ab444 | -3.28072 | -50.67378 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f7d5c684-c228-38e5-bcf7-e379194584bc | -3.27845 | -50.65855 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 44a55930-53a0-384d-ab45-ed7653b231f1 | -3.27625 | -46.23434 | 2024-10-19 01:24:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 2f8108cc-32d8-316c-8583-3d84360146aa | -3.26752 | -54.18508 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2d819bec-3574-3382-a816-713ec71a5ba2 | -3.2662 | -54.17573 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 35382c7a-a6f9-3f0d-ad75-153e1a6bf92f | -3.25712 | -54.17705 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c456a959-4914-3c78-962b-cb5586951d82 | -3.23874 | -50.85535 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 15696953-04e6-3028-a285-c8ed13839b93 | -3.1884 | -51.29156 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a0285ad9-fa64-3dfb-9750-982c3590db4f | -3.18624 | -51.29831 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d752997b-6c7c-3f88-bf0c-91da51c2f527 | -3.15559 | -51.31702 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9dc2f2c9-f841-3685-8b4f-76f1fea75db4 | -3.15062 | -51.35951 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a8aa25d2-7a90-337c-8de2-efef16a9736f | -3.12266 | -53.74601 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 42bef490-eee7-3510-8f8a-5dfa8c6c78c8 | -3.08691 | -51.22812 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f7c91fc3-9911-3c18-8269-cd6de877a892 | -3.08484 | -51.21416 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| c713b57b-c5ea-3a29-b8d2-13d549be63c9 | -3.08343 | -51.22017 | 2024-10-19 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| d4b6e730-8674-3f15-a107-00a48b37f83a | -3.06245 | -50.36409 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8a032573-2c35-3549-b0fb-03aaba6c6547 | -3.06129 | -53.24354 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ae43a60a-67d7-30d7-b4d4-7856c9f85134 | -3.06058 | -59.19068 | 2024-10-19 01:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 6093a1cc-903d-3bf0-817e-2bcc6ea9aa76 | -3.0522 | -49.41838 | 2024-10-19 01:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| ef1d85c3-c6d7-3065-8501-72c23e81c91e | -2.99823 | -45.61481 | 2024-10-19 01:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| bbad3fb8-5748-3d7a-8735-d935a59f9825 | -2.99555 | -45.62021 | 2024-10-19 01:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| f74363bc-c104-3335-bb9c-4060964091c8 | -2.99055 | -51.04472 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 9909bc0e-8067-3ab8-8681-e0fb67f0a70f | -2.98843 | -51.03021 | 2024-10-19 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| e56d5190-59d9-3b7a-9ed0-56bb80c32754 | -2.98634 | -52.85415 | 2024-10-19 01:24:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 4ea38489-aa5d-3102-8294-123f3631af19 | -2.98479 | -52.84325 | 2024-10-19 01:24:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3a4cdfd9-e482-325b-a930-49d56959c641 | -2.97658 | -52.85555 | 2024-10-19 01:24:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 34dae672-ee63-3dce-9d46-aaad58127f2d | -2.97503 | -52.84474 | 2024-10-19 01:24:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6ea4757e-44c8-37e6-81d7-3ea132eb0b4e | -2.95523 | -52.91422 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| afc6b7b4-a24b-32e2-8616-6ebacbfe09a2 | -2.95365 | -52.90332 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3a3315c9-203a-3eb9-af36-d3a0507de69f | -2.95333 | -52.92014 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 025f5b60-0d63-3efb-b42b-86bc56f0caf4 | -2.95183 | -52.90936 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 0532485a-e9dd-3901-baa1-07e9d57fafb2 | -2.95123 | -53.70288 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f9faa9f-5701-34cf-86f4-dbe3564317bb | -2.94933 | -54.15376 | 2024-10-19 01:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| acfd5075-5047-3845-84d5-1678f251d703 | -2.94799 | -54.14435 | 2024-10-19 01:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 252ccb1a-082e-37ce-8ba8-596319a153a5 | -2.88922 | -53.98442 | 2024-10-19 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b703ea07-ebf4-39aa-87f6-453db1f9c312 | -2.86651 | -48.2547 | 2024-10-19 01:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| f9e60421-0a6c-3e3a-8bcf-a870ac28a953 | -2.85971 | -53.32686 | 2024-10-19 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README9.md)
