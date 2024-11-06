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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfc2dfaa-4e62-3a62-9c71-64effb882b6e | 3.34876 | -51.2892 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a0a6bf9-985e-3971-a153-780341fe8f60 | 3.50492 | -51.24683 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6c64b80-69b1-329e-9efb-bf17bf09d656 | -3.68765 | -51.36876 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24e86ff6-54ab-3459-b6fb-3cdeaa92c7dd | -3.68101 | -50.1648 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a459d624-47f0-3c19-822d-72fe0831c89b | -2.44756 | -49.02672 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5dddbdcb-a5a7-3f4c-b0c3-b22f2ecc6c35 | -2.99546 | -54.09451 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c15b582-ae65-3f99-b180-5826d28c7ae7 | -3.04157 | -53.27818 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f60da952-55ee-3105-8d28-b9619e8556df | -6.3226 | -39.51445 | 2024-11-06 04:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 816bad45-c2de-3467-8026-04e4d60e3e65 | -3.48431 | -48.245 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0918d2c5-b4b3-34d5-ad2c-44f93b4004a6 | -3.16472 | -50.20867 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 20f5c875-8c7d-3759-8610-83b82d850704 | -2.628 | -49.17548 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d53710f1-6781-3940-9881-37dbd5c15106 | -2.84183 | -51.35419 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c262e258-1d83-3341-8129-0d3dc70a734a | -4.17797 | -46.58441 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1c900eb-55e4-30b9-b4f5-61b263d2ac24 | -3.99539 | -49.94273 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 700aca50-9451-3a06-95a9-d00284ab0b99 | -2.42977 | -48.85825 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb038661-c416-3c96-8719-b0caeec41f64 | -2.67187 | -51.82723 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6dd0831e-fd17-3d34-9a1f-036a2c5bd0f2 | -3.03453 | -53.27198 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8ecfc090-f4a4-3686-b84e-765f36efdf5c | -3.51394 | -53.14474 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a234ac81-9e6b-3d96-9f9e-ca7d783ae565 | -2.83586 | -51.80529 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6ba70f4-09b3-3704-b15f-7420543e5913 | -2.64058 | -49.11734 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 021a690c-c9c5-3c3b-b386-a04b2acc1153 | -2.64592 | -48.56549 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1990cf25-c42b-3fc1-b5ab-d3a4b921de3b | -5.14429 | -47.70235 | 2024-11-06 04:36:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c028e410-5cbe-3144-a625-59b12e9303b0 | -3.72301 | -51.39425 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d25abaf-8686-335e-a62a-eb494da64688 | -3.15369 | -46.4992 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2119e32a-0397-332c-9543-06b9262b2184 | -3.51941 | -51.67205 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f427ccf2-755d-369c-97ca-e18bc7082667 | -3.16752 | -50.21278 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 1884394c-aff1-373c-8c31-c030235c8087 | -3.09766 | -50.2607 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd8c2f84-ace9-34d3-8636-cc0177552301 | -2.45138 | -50.39595 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9305c4df-96ec-389f-84dd-c5fdb736313c | -3.16614 | -53.07529 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea222fa5-7591-3fff-9fbd-63598c47c28d | -2.87306 | -49.32338 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcd280c1-db40-3ede-a8c1-3ec5a46efe80 | -2.8649 | -49.39668 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40a47d69-f4c1-3b44-910f-c720acf0768c | -2.51926 | -49.19737 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 086bb142-349b-32fd-935d-e1f9eed459e2 | -3.68415 | -51.36819 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5cdf57-6b1a-309f-8c0f-6fd61f0c7645 | -2.88531 | -49.37499 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ed02b6a-c426-3a13-9b02-dad85603c256 | -2.62007 | -51.91801 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73aefa66-f4e0-3951-97a5-379c28cf115b | -2.30719 | -48.9027 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f422d010-24d3-3bea-8d13-1171fe973c11 | -3.51956 | -51.66677 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| beee6b06-278e-3d9e-a01b-4fddf6ceffc0 | -2.61032 | -51.30702 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60661b65-e539-3fd2-b8ea-0feda10d9ca4 | -3.05807 | -50.5076 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1f2cd46-90f8-33da-a483-ea55bd5fddb1 | -3.00372 | -54.09584 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b5ee893-4089-378d-b9c6-f3a249ac42d4 | -4.55765 | -48.00525 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c3182d98-67ca-3969-9add-d6547e9885f0 | -2.81988 | -52.93405 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2b54bb3e-ee6f-3479-8af8-0e48a1ef1c64 | -2.84797 | -51.79873 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cc91f99-1c2f-3f79-bc1b-0094dfa05496 | -5.71518 | -43.81448 | 2024-11-06 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c269ac9-c794-3b33-b8f5-b7008adcbe00 | -2.31467 | -49.09426 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc022122-ba3d-3258-b416-20629cd03333 | -2.84531 | -51.76865 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e64996a6-c396-36a5-a7cb-a77a2baf6168 | -4.05946 | -46.94134 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c43a244f-3a6c-3a94-ac0d-0854c378c973 | -3.06966 | -47.7681 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6d306bef-0ee3-3baa-a194-d23cdd1d5b87 | -2.9173 | -51.03909 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 322ac0bc-3bf6-34b0-8a97-6995aabc139a | -3.32333 | -51.62579 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39521f55-d7f3-3a97-8bdf-1744abbf9fe9 | -3.1809 | -50.59465 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a4ed006-47b9-3c73-b7ef-90c52aeed990 | -4.34806 | -48.63169 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d8d0bf3-98da-3fcd-bc1b-db654f47b725 | -3.22556 | -54.86149 | 2024-11-06 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46e8189-110c-3de0-b577-a95363835b1e | -2.80816 | -51.49586 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 594b6663-c6f9-3c3a-adf7-0b2bf5ed24c5 | -4.33106 | -39.36337 | 2024-11-06 04:36:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b37d356a-b0ce-3e83-a7f1-92c242407db9 | -2.80171 | -51.49072 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ff0225f-01cf-325a-873c-261c705ebc00 | -3.79932 | -44.03354 | 2024-11-06 04:36:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6661a3d1-720f-3afc-8615-796f5b1eb0d2 | -2.65199 | -48.56995 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da3ea6ae-f9a5-3f6b-bf49-6d1e10d4d79d | -2.95466 | -53.7239 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c521433-c75a-3871-afa4-fd700f6c2ac6 | -2.51585 | -49.13315 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8dfd237-f994-3165-8327-14689a81eada | -2.80834 | -52.9323 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a64ddf7b-36bd-34e7-b0a5-0a19a43c730d | -2.82219 | -52.91971 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 341025be-aad1-3665-b877-27832587d2a2 | -3.3643 | -51.57478 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f30183d9-e35f-3e34-a85d-8693ad7b9b41 | -3.10144 | -50.30197 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bd836fa-5ae4-3af4-b725-6b8f81064e8f | -4.07788 | -48.31651 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2580c1a4-32c2-38d5-b7b3-4b84e4282326 | -2.85399 | -49.48753 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58579ed9-ba56-3297-b3f2-fe7de2e6f910 | -2.82449 | -52.90548 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ae1c123f-5119-3a32-a742-dabff4a9a952 | -3.20135 | -51.03473 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9437ae0c-7f27-3336-95cd-4c226d01bcfe | -2.52076 | -49.10211 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e47aec35-8aa1-3b29-88b4-4330d5a4c4d6 | -2.52523 | -49.13815 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b467e69-492b-36a2-8e36-f7dcc550de39 | -2.71449 | -48.7344 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb8459a6-ed0c-394b-a3a6-59ae472eb847 | -2.90936 | -48.59583 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 977fdaf7-3597-3beb-b8c7-1c1b62768152 | -2.17979 | -48.37266 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8154be0d-8375-3198-882c-50d304bd55cc | -4.12576 | -43.5749 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 72b7523e-00b9-3502-a737-d15ffba1b4ef | -2.83983 | -52.90791 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| f419ad18-df59-3f43-9f11-edf0f32155d5 | -2.67913 | -46.71531 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f86c8e98-c3a7-3674-ab70-52d3f3585ede | -3.45128 | -50.37177 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a4529439-06c4-3034-958e-7d2cc3160b98 | -2.4407 | -49.17762 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cabe7b88-ce19-3e89-a227-128c243d45ac | -3.85576 | -52.27029 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9b013bb-528a-3a66-8b0a-f2419e15d209 | -4.63602 | -45.06788 | 2024-11-06 04:36:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcd6dba9-7a94-3365-b136-0c595f121629 | -5.91233 | -42.90778 | 2024-11-06 04:36:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 27189c36-155d-3c0e-8845-f3d6e2536b8f | -3.79799 | -49.98347 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c5ed2e4-5ea0-3d7f-bfc4-b0a6ad10786f | -4.07125 | -48.31548 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d6d1b85-56a0-3646-85ea-0079f5b433f1 | -2.46231 | -53.98882 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74e0e6b8-5074-3a0e-937c-328e69f56794 | -3.54589 | -47.38894 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 30dd032b-5a65-374f-9f21-41e4c309b15e | -4.69622 | -45.64993 | 2024-11-06 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd54d49e-02e7-3644-bfd6-998deead6395 | -3.64134 | -50.14072 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bce0a0a8-95e1-394e-bb55-7dc7051fd86c | -4.24366 | -46.88447 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e5245cc-39c0-3f33-8dce-cf49dd68768b | -4.27684 | -50.7158 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4f897f6-9ef2-39a4-8fb4-cd7372eebd20 | -1.33155 | -47.32779 | 2024-11-06 04:36:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 182525aa-f23f-31e2-aa6c-7717c7fd501f | -3.55036 | -47.38232 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 03fea1d9-c4b2-331a-875b-967b7b5fef0d | -2.82758 | -52.91072 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e8ff1501-52d5-3ab4-a8f8-1ba1394efd77 | -2.85721 | -48.4541 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dff8d4da-bb1b-3480-b995-64074eb69727 | -4.06003 | -46.93761 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b6e69d5-bcc9-38e7-ada9-5bd5283ef8f4 | -2.66377 | -48.64557 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1513d60-ee5f-3dfe-970e-e4a9d99423fc | -3.85436 | -52.1379 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14680a38-a5c2-357f-893c-7024e8ed23ce | -4.07179 | -48.31201 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ced23d85-8fbe-3c35-bf14-80f4fab3608b | -3.02826 | -53.2609 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1641062a-1118-36cd-9548-4af8fcb27705 | -4.29996 | -50.74567 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf2b13a1-f3be-3b83-ba15-cd73a1e32b7a | -3.02442 | -51.00369 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README31.md)
