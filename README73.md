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
| d86ec2d4-1f16-3bdb-8b9e-1cfb26ae6ecc | -2.73828 | -54.1155 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5a5dbf8-b5eb-36ca-a7ed-c863932f208c | -3.27954 | -48.79935 | 2024-11-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 323666b6-4436-39ea-8f0c-ae2c1819dbc7 | -2.37137 | -53.8345 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c139fbaf-643a-3bec-b80b-efe1dfe99d1a | -3.31774 | -54.0823 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53e7cb25-8e07-37d5-a1a2-6c2782b5a704 | -3.46267 | -52.72817 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01192113-8e9c-38c8-b3c3-d7bf2aae6218 | -3.51207 | -53.79856 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4920e3a8-6998-34eb-a9ee-09efaa3fcbbd | -3.26747 | -50.62475 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cc37a93-b7b7-3e62-9624-312004d1caf3 | -2.75921 | -54.06895 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212a1a61-be59-3290-a19c-ca98615d911d | -4.10363 | -48.48954 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a311106-87e6-37cf-83a3-57dafd9f12a9 | -2.62699 | -51.92538 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d213c36-742d-310f-969e-60f887751f3d | -3.07219 | -53.28933 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea1c0db7-cdc2-3368-9d26-5a4643611160 | -2.84751 | -54.00499 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d09fe1-fa3c-3919-8162-17ef0c310f07 | -2.85544 | -51.58627 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a631885-65ad-331c-90ef-0e0ceab37a42 | -3.37908 | -52.45748 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5afd28be-42d9-3f72-931a-bab5ca92daa8 | -3.06889 | -53.28881 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7e45939-94fb-3876-a7d7-2a08f22d5fcf | -6.12079 | -42.51815 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 584ac6e1-b466-3c8a-9244-80aa1f43a348 | -2.95581 | -51.41306 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8bc16ad-85eb-3ff6-9732-33c57943b69b | -3.21604 | -53.84319 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3432245a-af2e-3621-9421-c1a94bcacd57 | -3.91043 | -52.40242 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe30e581-8d6d-3a67-af45-be4fb12d6232 | -2.91337 | -53.06704 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e50a33c0-7fb4-38d1-b8c0-11f37788d732 | -3.16154 | -50.58503 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5005c078-c7d4-301e-a0da-6eeb63f4121c | -3.04863 | -54.40728 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a74cc39-7291-3049-8595-7777c8848541 | -4.24864 | -46.11155 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| db44ce55-1042-38ee-8c59-e75f512f72e5 | -3.27975 | -50.25836 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f84cb72-3b81-3bfc-a1dd-1ee2b0b04235 | -6.3189 | -49.67528 | 2024-11-21 04:55:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db120726-1e15-3634-8721-8ec2e2d4895a | -4.83997 | -49.3537 | 2024-11-21 04:55:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdf2f11d-e309-3d51-bbe9-b1a2b94f744a | -2.60169 | -54.01234 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75a433a1-8848-3b9d-9c71-07e450650b6a | -3.10487 | -53.75169 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f216624d-ae65-3f38-9b58-0c0d0cf11a17 | -3.90772 | -45.09154 | 2024-11-21 04:55:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 890f84d2-1efb-3568-924b-2b571ed7209e | -5.29602 | -50.57108 | 2024-11-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6de2d0d-fb57-349b-a5a1-cd8719c5d2b0 | -2.46394 | -53.9379 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 672c0e83-c870-37f6-bff5-2a728995ade6 | -3.05599 | -51.33297 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a24008b1-3e4c-332f-9f8d-f39a295a82ec | -3.63954 | -51.45425 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 585ebc49-73ab-3fb5-96a1-366ef6f0c19d | -3.77239 | -50.70486 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 965b35c5-8b1c-3222-bc59-07aaa4f420db | -4.04741 | -54.45307 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1be4da84-980d-3392-9e7e-38700840966f | -3.10319 | -53.74085 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 207179cd-9346-301d-8d92-56bef9ef8178 | -3.29297 | -53.85204 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 27a131ae-b626-34c2-bf28-b8591bb1147f | -3.08086 | -54.54918 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60b7e3e9-c26e-3f22-b244-9292b324a28b | -2.91722 | -53.06411 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c6d12ea-e02a-3ee4-8aad-c9ce1ca76210 | -2.9429 | -49.44346 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6391c7d-4a5d-3752-89bc-dc1367221a63 | -2.54085 | -53.98832 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d930ace-2042-3210-89ff-69ddd1eb86b4 | -3.2232 | -53.84077 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58ba9bc6-b0d6-38fc-9e6a-a867189c27e5 | -2.94279 | -54.80059 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f661fb5b-6548-36f4-938f-c51db7c1a1bd | -2.99404 | -51.46064 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4a6b676-eb45-3651-a6ba-eb16a73caa34 | -3.10505 | -50.20016 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec952926-1c37-3f5a-9bd8-e744d6f569ed | -3.18144 | -54.3209 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bd9e600-dd5e-3f04-a51b-718da2e9b116 | -3.43523 | -50.36184 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca16c053-6c87-37ff-86fa-5be3549f2ade | -8.58529 | -50.97933 | 2024-11-21 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfe9ab3a-d8a7-35cf-bb8f-c15ea75c3bf9 | -3.50768 | -53.80492 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 057cf6df-21aa-3a4a-84af-b14e89d057ba | -3.78404 | -54.52996 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef74da43-3ff5-3bab-adf1-1df225fdff27 | -3.51813 | -53.80305 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad68735d-5e16-3dd3-9d4e-54305cc8d7b2 | -5.24255 | -42.63732 | 2024-11-21 04:55:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f45e7fe-ab48-37f4-8c13-55799aa43fa9 | -3.32804 | -50.25731 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a75d276-cbbc-3015-b12d-93344dc25b2a | -2.76143 | -54.07642 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eae747cb-309c-3c9a-8472-ec15f4fd6ae5 | -3.38296 | -52.45448 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d7ec5283-d792-373b-9d15-1418e2e5c5d2 | -3.84089 | -50.01484 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa71ea3b-3ebb-347f-bdd7-2cd5e42ee241 | -2.81661 | -54.02855 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62d08f6f-fa2d-3463-8e27-d81383b5325a | -3.41878 | -50.25295 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a882907-1e1f-3437-93cf-dedff57978b6 | -3.37073 | -50.72966 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9539431c-71d4-38d2-a3bb-62e670b49cf0 | -4.09448 | -54.04864 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c7687f3-c1a2-3213-aa6e-5eafd1ab1513 | -2.76624 | -52.59814 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6781a418-97d9-33f8-a951-bf4a8cab2744 | -2.57244 | -54.08971 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25fd504d-30df-36d7-85bb-fc02c0153898 | -3.57233 | -54.68416 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c82e6908-235f-34e9-b444-3c47093b3934 | -6.93645 | -42.82685 | 2024-11-21 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3191f05e-5a84-335d-bcda-fab969153ee7 | -3.01757 | -53.42154 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95756227-8997-3b33-a70a-ca1822bd64af | -2.85204 | -51.58575 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23136f61-2216-3523-8e6b-0ee57068432a | -2.76797 | -54.03481 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| febbb825-2047-3159-8550-0dc3f67b731c | -3.35064 | -50.18339 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5818c6cc-36c0-3a0a-8e66-9ddc3c7a3faf | -4.10281 | -50.7432 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 827e00e3-e6f7-318e-a42a-c606e0289111 | -2.78698 | -52.87805 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6f7f1dc-c213-32b2-92f2-90d2a739fbaa | -2.28014 | -53.74602 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc8c3c00-20fb-35d8-92a2-d545c276bdeb | -2.81107 | -54.02058 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a7ee0a0-91b9-3213-b7eb-0a694eb54407 | -2.87774 | -53.9424 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b891f91-a1f6-35d5-8b48-ec7d19105366 | -2.84364 | -54.00794 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47828c36-7f13-3a1e-8b2c-a896a199db59 | -6.8214 | -46.77692 | 2024-11-21 04:55:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| acc98a51-c883-386e-8493-e95b6307a78d | -3.05641 | -54.40133 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 878ce745-cfaf-3f8e-86b1-e25b5ed130a1 | -4.38729 | -47.77803 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaee2d22-b19d-3217-af75-1d130ac27748 | -2.76421 | -54.0804 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16303488-f797-3c93-80bc-94bbda2fe1c2 | -3.09729 | -53.2158 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b9fb5ad5-0103-37f8-9a82-9ee57626b3f0 | -4.21372 | -48.72264 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73572fc5-b3fa-3cb1-bd41-74aa9bba549e | -2.65708 | -54.0709 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d605de8c-6edf-3075-b4ed-77cc83d9e2aa | -2.83045 | -54.04847 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14baaa1b-f27d-3d4f-8540-98f47e5775ce | -2.87814 | -52.44818 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e81f1dca-7d97-35aa-94fc-6e2f7a67ef1b | -8.58465 | -50.98376 | 2024-11-21 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 558aedb9-91aa-3ac3-b2c7-11c7937e9824 | -3.66345 | -51.57234 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2773d69a-69f7-32a9-91da-6ecefab389aa | -2.67465 | -51.88524 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56654293-08a9-3412-803d-c19270a9b380 | -3.08141 | -54.54565 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9399c4e2-0141-3bec-8946-93a7271334b0 | -3.05864 | -54.40883 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5e0f9e7-d7ef-31c2-bdc6-325d073f3989 | -2.84633 | -53.96936 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7e523e5-4f9b-3769-8293-037c81adffc9 | -2.61889 | -54.05416 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c28e6900-97f9-39b7-a3f2-99fa2e0fd161 | -3.90939 | -53.82224 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c37b9614-06de-3113-8b0f-945d000562f5 | -3.31941 | -54.09321 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 000ad285-1961-3922-98eb-339527bb92ef | -3.27145 | -53.83811 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31ab0a92-1181-34b2-9304-71d691dfecf9 | -2.58734 | -54.03857 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9808d214-ed0f-3131-ae77-b1edc8f949bd | -3.48103 | -50.31236 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdd5c095-a393-33a7-adbf-3e71990efac8 | -2.61734 | -51.81031 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca832bf1-a299-3b47-bbd1-72368d0c4870 | -3.51868 | -53.79961 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21b5a010-89f1-3fcc-a60f-9b1579b29674 | -7.9475 | -50.01153 | 2024-11-21 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fedde87e-c529-364e-8de3-954275df2009 | -3.28336 | -50.25896 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 968b5261-f35c-316d-a366-09dcd5b87650 | -4.41215 | -42.14349 | 2024-11-21 04:55:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README74.md)
