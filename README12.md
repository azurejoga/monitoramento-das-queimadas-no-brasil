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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2879f0b1-448b-363c-847b-4808417a4e2d | -2.322 | -53.882 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa35f34b-ea56-3ddb-bb7a-5e6b7962a83c | -4.2151 | -47.867401 | 2024-11-11 00:51:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca525f9-9cb3-3b1a-bac0-8c0ada285b1e | -3.0545 | -49.526001 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7218a462-328a-3f94-849e-6112c22b3566 | -0.6489 | -51.710701 | 2024-11-11 00:51:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8c91f008-3048-3764-b1a8-fbc12251daf3 | -3.1998 | -50.287998 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 890cce4e-b70d-350b-a830-7f029aa3e3b1 | -3.6897 | -50.622398 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe63ff6-b235-320c-9c94-674a2df6b327 | -1.2263 | -51.754299 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 000f292a-0413-34f4-af98-1389e0fd2645 | -17.597 | -57.5172 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a1a6eff-ef3b-368c-8d8e-2c864929245b | -4.3061 | -48.608601 | 2024-11-11 00:51:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ae8a7a-2e78-30d4-aab7-d568e4106755 | -3.255 | -51.558498 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb2a27c-da91-30f1-9efd-4c9d3afc9d8e | -3.2589 | -53.697498 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9822b8c-f41a-36b2-bb70-217982c31ad0 | -1.2114 | -53.6241 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b27da58-7cdd-310d-9b53-a4eff5c703b6 | -2.7446 | -49.3465 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f39d8a-c17f-3d95-a796-e249fa57b158 | -3.2432 | -46.322102 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df0f83f7-3bf9-34c8-9b8c-b1fb269c70ee | -3.0349 | -49.530499 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90805142-6990-3bc4-a426-d4928173ed47 | -2.1566 | -48.900902 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42afc707-4e80-3f16-8151-13704f089740 | -2.4592 | -50.387199 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e527f594-cbb1-3faf-83cc-ac694af3738a | -3.2309 | -50.288502 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6034bf54-618b-307a-967d-f498a770e9f9 | -3.8909 | -52.3992 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d4487a-1590-3084-8cb3-f8d20e6e2906 | -3.2422 | -53.397202 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7bc183-99d0-3d60-8438-0883580a0cce | -3.6609 | -54.652901 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0a92ba5-826c-317b-ba1c-c01d8bf9001e | -2.2697 | -50.6838 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf3d6ce-ec24-38c5-a10c-3ad841fd32d3 | -2.0656 | -53.301201 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d5f807-8dce-3153-b041-c2ac3200167c | -2.9329 | -52.764702 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a5adbf4-fd5d-3e6f-9ef6-97af4574d868 | -2.3728 | -48.6329 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecfd371d-a371-38c8-95f8-e0d900e55219 | -2.9379 | -49.5126 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 097eb685-2d6c-34da-bf98-20f23fabeaf6 | -2.4723 | -50.3993 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba3d8cd-152e-3d00-9025-9896378ebb9e | -3.2259 | -50.267101 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9693f457-111c-3994-b529-22172d06551c | -3.1196 | -45.9734 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd278bd-9d57-367b-afc1-64fa8dd2931b | -3.0805 | -53.275799 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 313719d4-b1d6-31e8-ad40-7308701edbff | -2.8333 | -54.000801 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8956a7a-cfbd-3c8a-82ad-dc16ca1b35a2 | -1.2098 | -51.772301 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f39d0617-4169-3b2d-a166-18ed78c30bed | -3.116 | -50.148499 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcf99e28-8bc8-3a39-92bb-19fd6c0e140d | -0.9754 | -53.178699 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604f9541-5a76-3640-8d40-dc75cf5db741 | -3.1987 | -49.5252 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a626327-e77d-342f-87d7-8936ce873747 | -17.590099 | -57.478401 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88efe537-70bc-3329-b1da-a3f7002d27ce | -1.2491 | -51.7635 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2145b1c-8eb1-3096-a412-d48183df5f66 | -4.0544 | -49.210999 | 2024-11-11 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc23e4ad-ae0a-3e39-ba26-73a193e963ce | -2.3971 | -53.850101 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6baa1ad2-da20-378d-b03e-691731e3f35f | -2.906 | -49.375 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 615c74c7-9b0b-3307-acee-db54a8b43180 | -2.1253 | -48.8993 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef96d05-0bff-3231-ad8f-4dc6012406c5 | -3.5067 | -55.5653 | 2024-11-11 00:51:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9e09b69-e5ad-3fa4-8409-33d47f3fae68 | -6.1369 | -44.9403 | 2024-11-11 00:51:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53e13171-33eb-3800-88c5-9ab218cbd8ab | -3.262 | -50.423401 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4778ddd4-32c3-329a-be93-53bbd71a59bf | -2.8968 | -49.246601 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4d89c9b-9966-37ef-b9ca-707e99b16d38 | -17.6227 | -57.492298 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65bfa10a-7d38-38e4-8dfb-27fd5abcab2e | -2.9441 | -49.495098 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c01dfc2-bb70-3842-bf1f-df293653e97d | -2.6364 | -49.903801 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c20d452-bfed-3b03-930a-bcfd9883c2f3 | -1.3977 | -52.366402 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5f33df0-65b2-305d-b787-8a0e1cf95fd4 | -1.3354 | -47.7164 | 2024-11-11 00:51:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0aec44-de30-355b-ba22-0ef9b282e070 | -3.2292 | -50.281399 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f465e1-9c58-3421-8fff-a27f29b998dd | -15.3038 | -56.5135 | 2024-11-11 00:51:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9288db0f-88e7-39b1-804e-db8ba63ba898 | -2.7278 | -51.7337 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39c41c8d-bd4f-33e6-909e-e36592eb77e2 | -2.5651 | -54.044601 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07b946d0-55c2-3028-9e3f-083a3a6e88da | -4.1149 | -49.116402 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce52c48-19b2-39c5-ac49-113221ef139a | -2.5482 | -53.9706 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b49a65-5e50-3e69-ad88-654874240a8d | -2.5502 | -54.024502 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6fa2c09-2c7c-3ca9-bb7f-b831eff060d8 | -1.4441 | -51.669701 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 300bb867-713c-3d1a-93e2-efd9d651a0bd | -3.6361 | -50.121799 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb50854e-3194-35f7-9135-5bbaa1ea8772 | -2.1089 | -46.093102 | 2024-11-11 00:51:00 | METOP-C | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38240f7f-564e-38bb-bd8e-e60eca29d395 | -17.606701 | -57.5154 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a0e6e8d-d2ad-3c09-bcfe-c8906ab0c7a8 | -3.3373 | -51.6474 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ad5a7a-8c08-3219-9743-69c008f45037 | -1.7115 | -52.475201 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5388dfb7-2c4c-3434-9024-adf5c9cf4da3 | -3.1329 | -50.445 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07c4099e-de34-310d-8366-3bc6b131a7a1 | -3.0881 | -49.582001 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2e2276e-1cc3-3395-ad79-b2500e889096 | -2.8955 | -54.183701 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92f03bb-6211-3f2b-9236-a3f808d3b652 | -2.2021 | -49.542198 | 2024-11-11 00:51:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2ccca6b-cb82-35b0-a5a4-e05d2cd3a42c | -3.147 | -54.474899 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37aa5c8d-7b64-3a5a-9a14-9d62823e1fe2 | -2.5997 | -48.1908 | 2024-11-11 00:51:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4f919d3-6323-30ef-8968-d5dba8ac180d | -2.8968 | -51.796001 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4af5999-b848-3d6f-bcd7-d003ff8c1cea | -3.0812 | -49.196602 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebdea806-636e-3ab9-ab66-fd014db43c8d | -3.2371 | -45.383801 | 2024-11-11 00:51:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce30a1d-77d6-3684-9245-63b685e65252 | -2.6564 | -46.8032 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c95787a-e941-3821-a49b-6187b901375f | -2.5715 | -54.0275 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3320e561-1b42-3a31-be24-106661c39d16 | -3.0136 | -53.253399 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60d7c7da-cdd7-3509-b4a8-7219a51fd07f | -2.666 | -49.2742 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 731da425-ccf4-36d5-a8ce-28968665cc54 | -3.0927 | -51.077 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7f0e2aa-2c8e-302b-9d01-2d7a5f6f169e | -4.2332 | -45.850498 | 2024-11-11 00:51:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9c44c8e-4d72-33d1-8969-78c303f1ccd0 | -3.1118 | -45.289001 | 2024-11-11 00:51:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1ca7788-0b23-3944-a671-33061f94c37f | -1.3418 | -51.404202 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 353e9fb7-5c0a-3b80-a3c9-6508ff411b15 | -2.5634 | -54.037102 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3b09444-74f5-340a-8728-d811cb1e6ff7 | -2.7296 | -54.133499 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ad5a5c-0679-3825-8177-327c11119d9a | -1.2048 | -53.6404 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b8f7e7-3027-3e81-8c89-f25dea782525 | -2.6441 | -46.794701 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459d5fff-6250-3536-8294-5323d3469b22 | -1.2278 | -51.761101 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f70f59a-99f2-3c26-8580-97db304e255a | -3.2211 | -50.290699 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d217fca-db2c-300e-9f83-17cfc99eab69 | -2.1972 | -48.365601 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f588a1b1-d52a-36c8-a02f-965bd647ea26 | -2.6466 | -46.805401 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab0f8b8-6ed3-32d6-a0f9-3c564d0ffe97 | -0.9008 | -52.448799 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deba4003-5295-37c4-a8a1-514d2c22f819 | -3.4457 | -51.580299 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa050c53-0567-3e9b-838c-aead8560a3e3 | -2.4465 | -53.931301 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71acc994-4e29-35ae-8bdd-8de33afe094b | -3.6575 | -50.214699 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c057b65d-0a4b-3155-bd57-e6f6a0b8daf7 | -1.6693 | -55.177101 | 2024-11-11 00:51:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1b0ea6a-b7da-36fc-8171-4412b17bb41a | -3.0898 | -49.5895 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1fcd15a-cf09-3582-acfb-b3f73fa9b8e8 | -3.2491 | -53.699699 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18b4a419-70b1-368f-91b1-8f580f9f3746 | -2.4609 | -50.394299 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 391cc585-3628-33c6-896f-7b02b8ac5120 | -17.284599 | -57.456402 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9bf9e7bc-c79e-3564-b6e6-08333dbd0358 | -2.4642 | -50.4086 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4126a2a5-8cdd-3347-927e-b007ebf9305b | -2.8773 | -53.967701 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 688f6be1-ce79-38cf-bc48-a1cd18c70f24 | -3.3256 | -49.895 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
