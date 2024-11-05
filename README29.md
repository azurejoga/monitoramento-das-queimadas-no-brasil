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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 454c4764-e857-3f5f-8da2-acb732fa897c | -4.91145 | -44.36551 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01efd131-fbdf-3dfe-ac42-78c233eed7e6 | -5.92921 | -43.64883 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4873218-8f8c-3567-b069-562b9f8c98e1 | -4.4049 | -43.11711 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91f89bee-cb1a-37b5-b32f-ab69b7740533 | -5.06372 | -44.24147 | 2024-11-05 04:55:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c87e72f1-9f03-36f8-acff-7468c9232191 | -4.38596 | -43.12305 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 411e5477-ba00-38a1-bda9-a70e699575b3 | -3.30608 | -47.01071 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ec923e3-ecda-3410-8541-69461c668ff1 | -2.7834 | -48.72114 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be5cc74f-b3d0-3c2a-aa6b-7c867649aced | -2.13939 | -51.01092 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a191e70c-b83c-3a14-a9b4-dbafffd5ccfb | -6.1052 | -43.95816 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73fee232-cfc1-3831-92c7-fb7ae4d97952 | -3.10069 | -50.29525 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1de4de99-87bd-3827-911d-2045dad5b38d | -2.81615 | -52.93841 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 303ca392-76a2-38fa-b033-1b8a87d88cc7 | -2.82 | -52.93547 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07a76238-f960-34fd-9ac6-569135ce57a2 | -3.76452 | -51.9597 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88b14c59-a705-3069-95cf-c80d9ad3df64 | -2.96362 | -51.27575 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffa0acf3-b642-3fb9-b6ea-8267d79205f2 | -4.90196 | -46.72241 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 722e730e-0ae0-3927-9ba2-9d95f5543166 | -3.70055 | -47.6208 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8674332-c88c-3b5b-9d06-c473f3869a25 | -2.18 | -48.85977 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ae8bdf87-e76e-3ad3-be8b-5bacc2358ceb | -5.00147 | -46.89796 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 042aaf99-56b7-3ac4-96af-428088b15d4e | -5.44461 | -48.21265 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11ee9c16-3884-39b5-952f-ccf4695280b3 | -3.11609 | -51.10843 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 103203a3-7ab7-35c8-b17c-7aea6541e473 | -2.57563 | -51.33689 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43fe0f3d-39ab-3447-8626-3feef638a72b | -2.45219 | -48.86749 | 2024-11-05 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2128163-cfa4-312c-bab9-aca32d813d7c | -2.12846 | -50.82939 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32aee763-d309-34e4-948c-bc615b125c42 | -4.49965 | -45.65273 | 2024-11-05 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5630b2b8-05a1-3146-912b-38a6464ace86 | -2.99719 | -51.21909 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8772fea6-abe7-3d28-a143-685854965077 | -4.3497 | -45.90353 | 2024-11-05 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df87fa93-628a-302b-8a81-ca604f981480 | -3.47639 | -50.38589 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a004e3c5-4faf-38c3-9101-0a6c3050e959 | -4.78073 | -48.90847 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98290033-bf15-32c1-b783-8d4210cfe45b | -3.55635 | -47.37741 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 48bf7480-e6df-3daf-b3ba-caa143fc3380 | -2.71342 | -52.96442 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b60c94-fa34-3e66-84cf-f9f088eac9b3 | -4.0198 | -51.02233 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8012f6c2-af79-3e6e-b57b-8aadbc5e1432 | -2.92108 | -48.06008 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d1b79b3-0138-33ec-b349-b032b569034f | -4.60213 | -45.83253 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54ac44f8-4ea6-3fef-bd39-c91ac3ab5cb4 | -2.28268 | -50.67369 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 440b9030-18d7-316a-8e95-b7329373ddab | -5.12114 | -45.15616 | 2024-11-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b914ea0-6843-384b-b594-a6adfe7ab1b7 | -5.93619 | -43.64146 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f01ccc9b-786f-3890-bd53-3758382d8d0a | -3.97284 | -48.39464 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccef8111-3ae9-3692-b486-e50d7032d146 | -2.6463 | -48.57249 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 019d8997-c57d-35c9-8576-7e7a3ba34fa5 | -3.56243 | -45.24553 | 2024-11-05 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63440bb2-251c-3c9e-bbdd-bdb0bc0bd950 | -5.30448 | -46.25195 | 2024-11-05 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5c44b5d-d92f-3deb-94b5-372cd775f3b1 | -3.09128 | -48.14194 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f9c52c6-b2a0-38f8-9e42-317a45379bd0 | -2.91696 | -48.05944 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e8d2be1-0118-3a25-8557-730433d5526c | -6.30339 | -42.0405 | 2024-11-05 04:55:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9626f481-1718-3e09-a5ed-966893bc244f | -3.54701 | -47.38018 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 5dd9526d-cb34-34c6-b18f-95da50197cd8 | -3.9952 | -49.9439 | 2024-11-05 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b195ae-e54f-3d50-95d4-dcd9e1384a02 | -3.04121 | -53.28037 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 144a7c13-cc41-3c43-afd6-daafb4225550 | -2.87252 | -51.38952 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 376dda60-8831-3969-aa13-3c35361b8cf2 | -3.12653 | -51.11 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df972efe-5979-31fb-8fee-bc9c67d57515 | -3.34212 | -50.25679 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64cd8de-b143-3588-8307-7d8739dae355 | -2.59795 | -51.30604 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b875a481-dc82-38d9-9d38-7a3919e43ef6 | -3.10133 | -50.29108 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e475120-04b9-36c8-b42d-e73876b8fd91 | -3.97078 | -49.0355 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa3cd85b-e060-3c33-a229-5eaa92dbba18 | -3.5418 | -51.47691 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63bb14a7-6189-3b07-8f3d-f4b200da30eb | -2.89828 | -48.59564 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2382f1b-c0a7-37d2-8715-777c37da7706 | -2.78556 | -51.61057 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5a7cbe8-83c9-38a7-9a2e-c2702b1ce420 | -3.08648 | -54.50056 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c68712db-6c99-31ff-9824-0233f0637936 | -2.88292 | -48.62708 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c904c02-73cd-3172-a925-e7df8179021f | -4.26483 | -50.60656 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 266753fd-f085-3ead-a876-561eab7e7ea9 | -2.90906 | -49.42324 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98bde68d-1e87-3e3f-9bf2-346ea6e1f124 | -3.09071 | -50.26384 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 253cb69b-21cf-36b2-8b54-83a7119bdfcf | -3.96629 | -48.15871 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2afb9958-afe0-3007-b175-443f8d4f5803 | -5.42031 | -48.14489 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7804f4fd-55fc-39f2-b48d-5b96356e5af8 | -2.80212 | -51.48126 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52d6fd7e-3355-3d7e-80e0-61adea7b00c0 | -2.40096 | -50.31152 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6752222f-359c-3d29-994d-b518e024d4d0 | -3.87416 | -52.31817 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d255eec-fa5d-3472-bf61-df4358c16841 | -2.95139 | -48.62109 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70e0bc99-0807-30b3-a32a-5223d06508b0 | -5.12173 | -45.15671 | 2024-11-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30359054-cc10-3bd8-a4a5-793d63a2de5a | -2.88977 | -49.26837 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85802d83-425c-33f8-8c3f-e29ceb555325 | -2.71615 | -47.7328 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51113d81-28ba-3439-98ef-67931872685d | -2.19164 | -50.85877 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0149879-23b8-37e3-bd55-e7a0bc853636 | -3.552 | -47.37663 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 02368b8d-6f80-3513-b707-4efd2b3d49ed | -4.89259 | -46.7077 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbca0b73-9ea2-3e0e-b4e8-37445c23b608 | -1.3831 | -55.42806 | 2024-11-05 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df00fdba-5e0d-315a-b345-2e675858ea7c | -4.26568 | -50.7203 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74c1b45b-b3ec-34ac-a246-cc837d477b11 | -2.61168 | -51.30817 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a73e570-26bf-3052-a29e-2eb2f273b4f2 | -3.47856 | -50.38761 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 420b7543-9347-3afb-afe9-eb67324c1ef8 | -3.41722 | -50.30573 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a530b6c-feb0-3da3-9a41-993f10542960 | -4.22442 | -50.63008 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8df316c8-5ef0-3e12-b44b-114180d99b00 | -3.96685 | -48.15499 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b86c6da-6095-37da-9402-87c0321666b1 | -3.034 | -53.26166 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01bd2e7a-6bf9-3e57-9dc5-0ffa7be08d8b | -3.73539 | -44.54771 | 2024-11-05 04:55:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39b2edc3-d3cb-3594-b77e-96eb07664e36 | -5.37368 | -46.45116 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb10ea9f-cc00-33d2-ac46-f67afded27c5 | -3.56384 | -52.6964 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80584a4a-7184-398e-9d60-eb3650fe8a22 | -3.10412 | -50.2488 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e435e9b-b254-3de9-82e3-a6a2f22c9de9 | -6.2892 | -46.12124 | 2024-11-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b848e0f-fc73-3472-8f1f-4fbce48b1565 | -6.5202 | -45.92859 | 2024-11-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d10061e-a26c-32cd-8c98-045c81d4da73 | -2.92107 | -49.34468 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0441c0d3-b5ea-39b4-8500-90029e19c222 | -3.5445 | -53.038 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 344505b4-b0f7-31d8-9b75-9fe2b6b69f61 | -3.97396 | -49.04105 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35da46e3-332f-3609-a2e1-7044ee2b5757 | -2.82118 | -48.55218 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d77e1e1-f9b1-3fcd-8027-8cb0efab0514 | -2.57906 | -51.33746 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e46335f5-34f1-3002-bd4a-dd682a292ac2 | -4.35183 | -45.90543 | 2024-11-05 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe483640-1b22-3d74-9a7d-fe74a9175695 | -3.54203 | -47.3837 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e816ba1f-8e69-3b71-a372-f4e95a82f484 | -2.97426 | -53.2734 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13351e8b-730a-3745-a841-3cc4236f955a | -2.77819 | -51.61316 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c4d6da7-5aa6-3d64-8963-ea812ccf5e65 | -2.83116 | -48.3502 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8212884-a132-37ba-ba79-235e14ca2cb0 | -2.84339 | -48.46001 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a311842f-a14f-3d4f-9be8-823a4eff4936 | -3.29512 | -50.02921 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b558f5fb-63d7-3565-b3eb-a040e6420c07 | -2.82607 | -52.93996 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ed21df4-4c81-36fb-b0ef-85324f0b8d49 | -3.09007 | -50.26801 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
