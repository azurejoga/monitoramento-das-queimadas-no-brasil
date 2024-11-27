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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbe5313b-151c-31af-a531-f2a54388ee3e | -3.27879 | -48.75787 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f3e54ec-bbdb-3dd6-af34-c87d3d77930f | -3.07106 | -50.94559 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c8b4bbb-b734-31f7-a960-0715607cf174 | -5.5829 | -43.15345 | 2024-11-27 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8d3e8aad-da63-32a1-b78d-00ec06e95443 | -4.72596 | -46.57095 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dcb4ad0-536b-3664-9edd-2b4ee6543d27 | -4.18524 | -48.63067 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73d813e3-cbe2-36c4-a04d-779578c46845 | -3.28958 | -50.61535 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd5c575c-d526-3124-aa73-6ad9cfd131f3 | -2.93522 | -48.01746 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 422ebabb-a0b9-3ff5-a9b0-b8ccb566d1f9 | -2.99942 | -51.45937 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efbdff53-b9bf-3201-9299-24507fec3648 | -0.30415 | -51.7583 | 2024-11-27 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fd6bd27-64c7-3404-905c-bb6812b72f0d | -1.2672 | -51.6307 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce0ec27d-2aa2-37e2-9170-c04cbfe23a0d | -3.89717 | -45.62342 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a86199a-cfa9-3b91-86e1-ca4e42733c61 | -2.61074 | -54.24724 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2859ead-8c15-3cb6-a97f-3387430d0141 | -3.9627 | -46.90964 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2272e8c-afd8-304b-8611-7de080e7d2ae | 1.95437 | -60.85787 | 2024-11-27 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3df8bc9e-f9e5-364c-9e67-a7fd71fe1d43 | -2.79917 | -53.04376 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20338af8-0cfe-3ae5-a7c4-06f874932960 | -5.20416 | -40.63681 | 2024-11-27 04:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6717c28e-6b79-3e0e-8e1f-f174c31beb46 | -2.83301 | -46.83744 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0a7eb266-432f-3b18-b3ce-1e192b788fb4 | -1.69885 | -52.76548 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1991478-6968-320f-a786-7272d41ef079 | -2.60699 | -54.27068 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 307d009c-dfb7-3f7d-a700-05834860f6d7 | -3.11235 | -53.26114 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9bb28f4-9992-30da-b21d-7e5f690ce58d | -1.65566 | -52.51516 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be2e1e7-f613-35d9-882a-80969bb5c61d | -1.18358 | -51.97965 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2294afb-a7ad-3880-9711-1318df35c58c | -3.05592 | -53.68768 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f72f5c1-90c5-3e6d-bbcd-ba8c4ba36620 | -2.24805 | -53.6332 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a283b7dd-161b-3cad-b92d-87cf2b574eff | -1.12309 | -53.734 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c094e07-a0be-3a8d-8846-ebd448391e8d | -1.11195 | -53.3871 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74c531c9-f622-305d-8e14-511c0c8a61eb | -2.87725 | -51.58607 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a12d54b-4d04-3d82-97ad-ba09e6706c5b | -2.80374 | -54.13142 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3387d5d5-749c-3747-bad7-b0a26b1a8b55 | -2.89707 | -54.177 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4f06df5-9b9d-3b7f-a448-2e872073e97b | -2.94005 | -54.79954 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5802cd7d-d53b-378a-a348-354f0ec9ef7f | -3.7206 | -50.18611 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be722670-56b7-316c-9ac7-d41b68db256d | -2.97266 | -51.44045 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de350af0-8140-32e8-b68a-62364c44f7e0 | -3.1544 | -49.24699 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7efd0e09-d3eb-3118-afe2-3e3c0f95a9bc | -4.2365 | -50.01616 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e67f199-1343-3e0e-8ee7-b3e2db8dc066 | -3.09213 | -53.24962 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b391e2c8-f41c-3ef3-b418-a4193a387f55 | -3.45801 | -50.83997 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b08e65-f566-37a6-94e9-bbe57e096310 | -1.96798 | -53.13967 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d845680-b076-3be9-9095-2f3450c3209c | -3.59511 | -50.3569 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f05a014e-af22-342d-84c4-77464f27a84c | -3.32676 | -53.72587 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a1680f4-d925-3b2d-b570-3043a115256f | -2.81613 | -46.8262 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30faf354-d20c-39aa-922c-b7c8b2637907 | -1.90032 | -50.59211 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfd17626-4c38-3e52-bcb0-35257bf7b441 | -2.7216 | -48.60289 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8e9ea0e-6bc1-318c-bbff-f1de06414b77 | -2.69958 | -45.66102 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef9231a1-4cfa-32fa-b1b0-e7b44ff66eb1 | -2.80659 | -53.02015 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab2a615a-32cf-3f23-bca4-47183bb406c3 | -1.50958 | -47.27041 | 2024-11-27 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ecd6781-60fc-3184-a595-bf82ca64e42f | -3.19705 | -51.26611 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b6ec874-da6c-3828-a3e0-69c0ded0dd10 | -3.9426 | -46.89339 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 050e703d-f4ec-35e4-8a06-cc860391baab | 0.94613 | -50.74301 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ecc411e-a5e5-344a-9adc-60fdecb75c28 | -2.8224 | -46.80985 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 903313fa-0626-3af1-b2c7-32c69389760e | -3.2495 | -53.41578 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c10ba4ec-57c8-3ce2-af4b-c7c03c29c3fa | -2.43897 | -53.89167 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5892ed9-88a8-3ce4-b4c4-9ad1543d2aa8 | -3.9766 | -49.94051 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 399c8b02-a559-378b-9c5f-eb5c20c86531 | -2.26394 | -50.46122 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ba44300-aec6-326b-a2ea-4c6dafef6931 | -3.3834 | -50.10519 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bc55b9a-1234-3d3c-9b0b-6ec87c0d9cbf | -3.68329 | -50.22963 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecb51138-c587-3017-be94-92e3498f1ca6 | -3.33039 | -50.05468 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef99a0cb-d7d0-3138-bc9f-434a9619475c | -4.28056 | -48.60343 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50c2787f-d884-35c6-a2dd-cd35e63bf4aa | -1.6342 | -52.4917 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d64d634f-7ef5-3dab-b672-8919eb73f71a | -2.84492 | -49.40206 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26c95f30-2825-3499-aae3-66f8bc5595fc | -4.11413 | -48.52545 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29321d09-f769-314e-921d-12d75ca010f1 | -1.79632 | -52.74797 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d343bd48-eb50-3000-a157-c909477a4fa0 | -2.93392 | -48.63473 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 123c50e6-7230-3f17-91ab-e8f109f81508 | -4.21551 | -50.88472 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7c3d18e8-ea61-3017-ad6e-3c0795de9078 | -3.10648 | -53.25186 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ebfaf812-4ed4-3d1e-8bb8-1110401ad739 | -2.85874 | -51.27842 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1bee72d-1ae8-36ab-ab38-b96780c60209 | -3.46794 | -50.25957 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e589365-18a4-37f1-98d8-93d96761129a | -3.10942 | -53.2565 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e6267d29-cfcb-3b75-8a20-ad3d1b916087 | -3.10354 | -53.24722 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d8feede-ca34-3cc9-87f4-7ba1c5e01e43 | -3.6772 | -47.21451 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb9b504b-7f2a-3f61-b133-5ba071a94020 | -3.5885 | -50.35588 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecd60458-f723-39c0-9d71-0ec0efcba5f0 | -2.87616 | -51.76655 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0070abb7-1add-3611-86f2-3fec9a0713e5 | -3.63192 | -50.1443 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78d93e79-5bd0-3c9d-88cd-0d554e2ff85b | -1.51507 | -46.07695 | 2024-11-27 04:42:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd277f1a-79e9-3a10-9f61-6186253ee9a8 | -4.13551 | -43.80577 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 987952d2-fc65-3360-aff1-014b07d7af3a | -2.66561 | -51.72322 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a19a54e5-e611-3025-ab23-16d84b2af7e5 | -2.94639 | -51.43274 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 854252d4-8396-3bd2-990a-674c40d41b51 | -2.93865 | -49.12712 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95e58edc-d305-3bc8-8cf8-0c531b6025c1 | -4.143 | -50.41798 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64edbaf0-979c-3c03-84af-f9c5305ed2d4 | -2.80187 | -52.91304 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b6d77783-ac62-39e0-896e-b4f2873ad1c6 | -3.78015 | -46.6845 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03f606f5-bb45-32f1-b18a-5706940f0351 | -2.24875 | -53.62884 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 137654dc-493a-363b-b99f-a3b0a604a900 | -1.38026 | -53.62828 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a735858-bce4-31d7-b445-380e5d6c1874 | -3.1117 | -53.26525 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3cb34c8-068c-367b-bd09-59f94063f718 | -3.15873 | -50.58424 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83d9f28b-a20a-3e15-a786-0e50d09d6555 | -1.7398 | -52.71444 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd733f52-b89f-3fb2-bd1d-33d8a54e2c95 | -3.45856 | -50.83651 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a1f76b1-33d3-3e0b-9bc8-b7fa780d06d7 | -2.95237 | -48.33575 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c92193f7-528d-326e-be00-478f171a90fd | -3.03542 | -48.50213 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4191d3f8-b5c6-35cd-9731-d329d80b7527 | -4.24415 | -48.59018 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9445808-4dd7-33d3-84fc-ffae4d83058e | -4.28617 | -48.20179 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6873c0d0-5d8c-3b54-b26a-7d1580afb57a | -4.951 | -47.80336 | 2024-11-27 04:42:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3bce066-bde4-30a4-8832-f92ef9c619f9 | -3.77432 | -52.40268 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20656dec-dbf4-38b3-af0f-2d9bdbc7cc22 | -1.53632 | -51.19547 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85c34e8c-e095-38d8-834c-8e4f2d701eee | -3.23036 | -50.19394 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a324203-50c5-3aa1-832d-124147823d5c | -1.62679 | -51.99352 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72ca79c5-c5cb-3687-9d9f-6608789645b0 | -3.04629 | -47.88617 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3e33a56-0ceb-3e6c-892e-cc22665db9f8 | -1.6298 | -52.72242 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92078d21-70a7-3ccb-923d-e9c8a1ca22d6 | -4.72149 | -46.57489 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b6dbb8f-f334-3de5-a79c-61a7a8b92fa6 | -4.02047 | -53.81431 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe0e898-b579-3aca-8ac1-8de04179075a | 0.97529 | -50.12499 | 2024-11-27 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README56.md)
