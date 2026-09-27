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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa8a215c-66d0-3877-9680-2b817ebab5a1 | -4.54657 | -55.53016 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 799f6f2e-9a29-3b58-b8a1-48bbfda4ae0d | -6.77551 | -48.66481 | 2026-09-27 05:27:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb9f63fe-0a12-3a85-8515-e3bee3377ab9 | -3.96405 | -59.34182 | 2026-09-27 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7e6538-c8d4-3b57-b746-528df1b799ca | -3.72796 | -55.95965 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e642c48-de16-3080-86f0-8563545418fd | -3.82931 | -55.91125 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17e5d021-6ae4-352f-9b9f-5cfd616f8dec | -4.28285 | -48.55957 | 2026-09-27 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96ff3bcf-8e85-3bca-aa29-06104ba4af2a | -1.74217 | -55.24595 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3ff2bee-8d69-37af-a3fa-3d2c69c5d886 | -3.72855 | -55.95583 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34233d5b-8750-3f12-b643-e6205d479bbc | -2.47223 | -57.93856 | 2026-09-27 05:27:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee32760e-50f8-3421-ac10-e93e28c6cfcb | -2.96476 | -49.56468 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f468bdd-2722-3d8f-b7dc-98f6696f995a | -2.42517 | -49.31137 | 2026-09-27 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a07cd16-81d6-3e52-b465-21e44f3233d6 | -3.85166 | -52.01363 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85ecef8d-7041-3cae-9a72-b71ac974ea2a | -1.04371 | -53.56721 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c74a99c5-cb2d-33b4-bd96-53ae93e7e2d4 | -4.47736 | -54.86292 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e38062e-161a-3d4c-b975-30b98aeba804 | -4.4766 | -55.42394 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d9f4e49-a987-356e-b210-2bd71d46c71a | -3.30046 | -54.69396 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57dbf774-7fcc-3d29-b70a-1a0096300304 | -3.01526 | -52.4984 | 2026-09-27 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99798a4d-f85b-303e-8c18-e4f75eba2c0d | -4.36112 | -55.27724 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0687ac1f-21a6-30f7-b8d5-1ba15ab16074 | -6.09995 | -57.62278 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7261fa71-50f8-3c19-adf4-b6ddffebab3e | -3.83219 | -55.91256 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43d2abbe-bdaa-3907-8b99-bf741531d3e7 | -3.96084 | -48.12261 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e41070ec-3af9-3b28-8bf1-a970eea7a764 | -1.13871 | -54.0863 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 048f2e06-a15a-3e06-9af0-71133d2c3011 | -3.71839 | -54.66 | 2026-09-27 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 869e76c2-0ad4-312d-88cc-8822a67b3c76 | -2.92089 | -54.16035 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f28b916b-cae8-3b2c-8213-cedf730799d5 | -5.7593 | -45.29301 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fdf54eff-92bd-3f2c-9a26-03910f134e95 | -3.71907 | -54.65557 | 2026-09-27 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2be2ebf-58a8-390a-8e84-81b890f7424d | -3.19531 | -51.03814 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5071156c-b263-34f9-a78d-232eda033cf9 | -2.06493 | -56.87269 | 2026-09-27 05:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa0a0e4c-63d0-3597-a51a-57e1139fb847 | -1.14547 | -54.09182 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fbc18f9-f09d-358e-960c-27bc55acfd01 | -2.61166 | -51.74502 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 043bd9b1-a072-34a2-bf75-5166c43b6eb4 | -3.41901 | -50.42401 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5494cd75-3dcd-3efa-95e3-bd982a84c800 | -3.26731 | -50.14387 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42470cb2-746e-34d4-b599-4d24bfda6c3b | -4.54277 | -54.96542 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b969a921-8381-3844-a934-73b167aa6089 | -3.04089 | -54.69466 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d5863ba-53da-397e-96d2-b9df4ed56ef9 | -1.21771 | -54.55381 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d0c1eb2-d2d3-3a59-97d0-37875a3e7a1c | -2.9171 | -54.15977 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be5f3867-1ddd-3921-9460-f796e08e2e51 | -0.51129 | -49.12629 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f375881-60fa-32d4-84aa-3231f3d174e3 | -3.01285 | -54.20781 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caac5f3c-68c0-3a19-a833-6ac040d86da9 | -2.54079 | -57.54878 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9516b71b-1a6a-3854-bd31-46223b8e4fcf | -2.89308 | -54.18888 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9044f37-4f9a-31e6-bbed-0f9203507c60 | -3.19132 | -51.0327 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7cfd80d-6161-324e-9587-6360b90d9821 | -1.74508 | -55.25048 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 355ca662-24dd-3f42-ad91-14387b72dfb3 | -5.08068 | -56.34733 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b53baf-f0a7-346e-b372-f68a2830e466 | -3.95234 | -56.09092 | 2026-09-27 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a206c2d-71ce-3c4a-b8ba-d939b1c0dd7f | -2.49714 | -56.13946 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42fafcd6-2010-3cd6-aea9-d1d6e8d13a95 | -4.28848 | -48.56055 | 2026-09-27 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46bc40f7-04e3-3c2a-9aa2-df42277c7834 | -3.78733 | -55.87772 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 872affe9-8dcf-371c-be65-66c36e227bb4 | -4.25996 | -51.0544 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea28ebc4-9125-3ae2-9b38-43f719a1c7b3 | -3.94268 | -56.01476 | 2026-09-27 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c8fc0e5-e84f-3192-a2d0-93e5f9ac96fa | -1.21566 | -54.56667 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9e92ae0-d6e8-3ae7-ac02-fa3b57aa837a | -4.53908 | -54.9648 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 729781b9-9741-3b2f-b955-ba6ae827bb3a | -1.04755 | -53.56776 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| af98a995-135c-3a8d-8581-111a29195146 | -6.1368 | -53.05333 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2d2c6bd-e036-3354-ba82-f12e56da79a6 | -1.21179 | -54.54419 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 005db479-4fbb-35cc-b3f2-b541a4cd605f | -6.07767 | -57.80923 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 032cd1f9-3541-3338-aeef-39a4ac881d0b | -3.84043 | -55.909 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbe5f18b-21be-3994-a6b5-098ac1ef1a4e | -3.05901 | -50.33622 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14ede331-da57-3382-99f2-5799fc821cb7 | -2.44917 | -49.22458 | 2026-09-27 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47132dec-0335-30b5-a106-121a36d0413a | -1.84004 | -54.72133 | 2026-09-27 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e08d35a5-188c-3317-b5d5-9a052ab6b220 | -3.22948 | -54.32952 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1495053c-1620-38d8-8e73-7460d5943692 | -2.56463 | -57.52762 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 581c5b10-d6a7-3704-838a-06361feb1146 | -4.51528 | -54.98569 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecb05187-63b4-34ba-b2d4-b4a11921f84c | -2.9928 | -50.47471 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92eb928a-af18-3419-99ad-c36db40f859f | -5.16564 | -56.00563 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6290a8bf-d163-35e5-8392-eec5ab31a3a2 | -3.87341 | -52.28275 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 898c5830-5c3a-3598-b122-e41756c603bd | -4.54449 | -54.97905 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70f63678-882b-3f3b-b1f8-5f0b8d8002b8 | -1.14478 | -54.09623 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 906d4d19-8456-3956-a6b4-3812eba17759 | -3.07923 | -54.4032 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3ff0fab-df73-3720-957e-3ad4e518dd8f | -0.51643 | -49.12711 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 655ab0d9-3068-387a-81da-908f87edcb67 | -3.23086 | -54.32047 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9cabf8d-700d-3448-8ccc-133a0e0fcd4c | -2.90372 | -54.1952 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b7d097b-67ad-3487-a681-c4fcdeb0e3cb | -3.96893 | -50.71405 | 2026-09-27 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc7e041d-d937-3044-bb99-a7fd60f47b8d | -6.13563 | -53.06127 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dbd7f5a-37ac-31ca-b7ef-fdd02c986db6 | -6.086 | -53.51409 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2febf4ad-6a65-3091-9d55-ed3a6ba6fe60 | -3.36271 | -50.46577 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b25515a-7e43-3295-a7c0-1e9137fba909 | -3.86539 | -55.81702 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d9f4fca-00ec-33d0-806e-b3b4335f29c8 | -5.67987 | -50.09694 | 2026-09-27 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 749b86a5-d603-323c-b045-056c30893346 | -2.42565 | -49.30825 | 2026-09-27 05:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e17a16c-cded-399c-854b-4a9c877c504d | -4.52598 | -54.97625 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9aa7b27-7277-3019-83f3-01270c2f28e1 | -4.46413 | -58.34781 | 2026-09-27 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8eb9d6-4a1c-352b-9bc4-c816cc31a111 | -4.54079 | -54.97846 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6859e5d-da70-343d-880a-181f0cf691cc | -3.83341 | -55.90791 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6c4c6a34-dbb1-3679-b1ae-6932aa55a9bf | -3.09779 | -49.3539 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fa14b7b-3566-3465-b588-f126a5b435c3 | -4.7166 | -55.72122 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c44e906c-df37-3ea0-91f5-fa44d27366f2 | -3.18947 | -51.03588 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 885a097d-e990-3bcc-aa32-ca01975cde89 | -6.3636 | -57.47594 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b6d14d8-e1c8-30dd-ab65-82d652078a3f | -4.44383 | -55.03211 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38edfaf-d081-33d7-8319-95e90200bbd9 | -4.14234 | -48.21645 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 820137da-f449-3a87-a0c3-d021080bf89e | -6.06704 | -57.81116 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 862323b8-e85d-3608-ad7e-62901760b8bf | -2.91064 | -59.13601 | 2026-09-27 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b93a751-164c-38d8-88ca-494df80f36d5 | -3.21723 | -53.95905 | 2026-09-27 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24aa5302-0845-3198-b086-3a7a0636fa9e | -4.52902 | -54.98119 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90bdf17d-0f47-324c-b30d-5d1da4fd1b62 | -3.96348 | -59.34534 | 2026-09-27 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e92b2b4-f46a-30bd-9b9b-d037b1e27bee | -3.98123 | -56.13449 | 2026-09-27 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aefae69f-a153-3ffb-b941-6bfaf978bc9f | -6.28261 | -53.37936 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73df6b61-c22f-3e2c-9dcb-8cf5d857599a | -2.66104 | -56.54346 | 2026-09-27 05:27:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c39c7948-ce3e-3ca3-bad9-0c9c49a37f6c | -2.947 | -57.80429 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a574ea0-2506-3773-95e3-1014dd83044c | -3.00612 | -54.20464 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b694b237-2a80-3833-a755-eb2cf52a1654 | -6.05074 | -53.60987 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 814cf6ed-814c-3b35-a4ea-0c50ff9d4c29 | -0.53861 | -49.18598 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
