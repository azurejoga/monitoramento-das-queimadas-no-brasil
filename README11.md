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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eacf7e8a-0963-3983-9894-96e9130203f3 | -9.35327 | -50.73898 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 889940af-25ae-397d-88a8-525d0c372d8d | -10.66691 | -49.71508 | 2025-11-20 04:33:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c6c63d9c-b063-3f14-a955-29eb38c4cc9a | -10.52904 | -47.5858 | 2025-11-20 04:33:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d42cb2aa-3685-3041-bc1b-00c1c5f0ef86 | -10.36157 | -48.90225 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9fb8dc06-705f-3612-9e28-3c63e1da67e6 | -8.45225 | -47.93325 | 2025-11-20 04:33:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f387c3ba-a2d5-3096-bf90-255db98f1bd5 | -8.61055 | -48.6522 | 2025-11-20 04:33:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59632fcb-b02b-3bf3-a636-59020faa9e8f | -14.49814 | -47.97848 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e67b904c-1312-3371-a71c-9c5b8b71ecc1 | -11.25794 | -48.49354 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ee6fea0c-3913-3d4e-a9d2-098537f747ab | -10.02176 | -48.12465 | 2025-11-20 04:33:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfb1d047-b113-3700-9748-5610a251985a | -12.80759 | -47.55994 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c033ed0-a247-3c27-b116-8bdc9378384c | -12.94555 | -47.71384 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 026d7889-5461-3c60-9422-7864dacb6b2c | -11.41475 | -48.44665 | 2025-11-20 04:33:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39353963-afec-3215-94b2-1919e6f7d51a | -13.92489 | -47.4817 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41ec0be4-a3a4-3254-98c7-9aea90396b25 | -9.39683 | -50.6833 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c2b16af-15b1-3886-b57d-74b6ac830500 | -10.36818 | -48.90332 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8148434-13b8-3d03-8626-82d6b51435d6 | -15.05717 | -48.30579 | 2025-11-20 04:33:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01e4a06f-5d60-3eda-acfc-4d7f87457acc | -10.48814 | -49.36725 | 2025-11-20 04:33:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61255610-6a98-34f4-9a25-750f52fcb463 | -14.94667 | -47.33253 | 2025-11-20 04:33:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d0c5299-3345-3aff-9dc7-fcf3c91c2aad | -13.8218 | -46.57628 | 2025-11-20 04:33:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d41e260e-608e-3502-9094-6f3d2e08044a | -12.87384 | -54.74284 | 2025-11-20 04:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c24a9408-3275-35fb-a5cf-ca0215d6855d | -11.49977 | -48.55407 | 2025-11-20 04:33:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c676da34-2c78-3957-8897-4e1e8da35d17 | -11.26402 | -48.49812 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 756eae25-2f69-306c-ad67-4004d0b1572e | -10.10498 | -49.5944 | 2025-11-20 04:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a966e999-0157-3e2f-a52d-f977e2da68cb | -14.62813 | -46.54122 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d7c6e112-15bc-3ae0-8d95-5d9d20678cfb | -10.35772 | -48.9052 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fd23de63-80c7-3343-a670-d68a2bebfdf2 | -12.78953 | -48.90556 | 2025-11-20 04:33:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 349bd935-f9c7-3ef7-81bc-8c71c59ba497 | -11.4153 | -48.44312 | 2025-11-20 04:33:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ea8cce4-8cf0-3e46-a312-427acbf4dbdb | -13.27217 | -47.33561 | 2025-11-20 04:33:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac385403-f1b1-3ac3-87ac-5ce03cba56cb | -9.05412 | -48.83398 | 2025-11-20 04:33:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73ed7955-331d-3d03-aa31-b543b06202f5 | -12.50489 | -49.86851 | 2025-11-20 04:33:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9402b1b1-9e05-3f20-b6e6-0b965170a4ea | -13.93916 | -47.45667 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3795d79-5cff-3f79-85d1-ce970ee9ea8d | -12.42947 | -47.88 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6501412b-f433-3378-9dcf-4d159b445383 | -10.38082 | -49.92736 | 2025-11-20 04:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45fc1fb1-4100-3035-9f3b-4857435e25b5 | -11.5026 | -48.23225 | 2025-11-20 04:33:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ce247bf-e10e-3763-9af7-1e22d08118fe | -10.54194 | -47.9901 | 2025-11-20 04:33:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f76a004d-4c47-3422-8c6e-98b9b90ff083 | -12.48145 | -49.78111 | 2025-11-20 04:33:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 940e8478-6421-386b-888e-fc6c55e05f7e | -10.38692 | -49.93204 | 2025-11-20 04:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6336c6e8-d7cc-3c35-a966-97ad09d722db | -14.85594 | -52.85368 | 2025-11-20 04:33:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9c4aa22-8c3a-3534-8be5-004e5124024d | -12.15049 | -46.50527 | 2025-11-20 04:33:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01c2b03d-0b89-35d5-8751-0bc1e10e02dc | -15.75083 | -47.78347 | 2025-11-20 04:33:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83cf798f-df4d-3b97-84cf-6a4c2ab42bca | -15.42866 | -48.07076 | 2025-11-20 04:33:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d55f59be-be24-3aca-919f-c8aa4c9274f1 | -10.35882 | -48.89823 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 19b8269c-1de7-350f-953c-4edb1a00fefe | -12.8745 | -54.73909 | 2025-11-20 04:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96caf0d4-0ed1-3cdc-868d-0ddad3dd8e8b | -13.51406 | -47.91537 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e58c2f91-594a-3ec0-bdc2-36954d8ab804 | -15.78816 | -43.35909 | 2025-11-20 04:33:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e38be64a-1d90-3358-b93f-20363b7e8ae7 | -10.36047 | -48.90923 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43ed7f79-f467-3f29-9429-fee60ed2665f | -10.10166 | -49.59385 | 2025-11-20 04:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 142e2cd1-ad7a-3774-a45e-4e373947ada4 | -12.80812 | -47.55981 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8290acf5-96c6-3905-8007-f017c071383c | -10.02344 | -48.13573 | 2025-11-20 04:33:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a2b9977-4dc4-30d1-958e-466e7b001abd | -9.96824 | -54.57574 | 2025-11-20 04:33:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe832069-0680-37ea-8080-cd8cd5653e84 | -10.88871 | -54.14159 | 2025-11-20 04:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 054ce946-3756-3377-9b06-3bf454ba6935 | -10.36763 | -48.9068 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe29fe47-b578-37a3-9d4b-9eaaa740b86e | -13.81932 | -46.57698 | 2025-11-20 04:33:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cb2ff89-7ce8-3256-b850-57efc61cc8ba | -13.92944 | -47.47475 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe2c618c-458a-3615-9738-cd4fb6b9aa10 | -10.79183 | -47.97486 | 2025-11-20 04:33:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92c261b1-208a-3076-8a29-bb06ce29017f | -14.63174 | -46.54177 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0faf1527-6c2a-38b4-b445-4e2eac4f9e99 | -12.67715 | -46.77645 | 2025-11-20 04:33:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c04acc77-c4db-3c5f-aa12-172f71ff92d0 | -11.26678 | -48.50219 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4056bccf-46c4-3122-bfbd-1334e08aee21 | -10.79517 | -47.97536 | 2025-11-20 04:33:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45ec1daf-3cd1-3eab-90ff-c67d78a8857e | -8.45501 | -47.93725 | 2025-11-20 04:33:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0532390-16a7-3bb5-ad19-a69dee239429 | -14.3382 | -48.08458 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d1dbea5-6d80-3d32-8e46-08993a5454c3 | -14.63957 | -46.53871 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b76f68c-20f8-34c2-970b-d235a285448a | -10.36377 | -48.90976 | 2025-11-20 04:33:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ed19037-aed1-3b0d-aeaa-e2fa1cdd0934 | -13.7943 | -48.88607 | 2025-11-20 04:33:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cebfa501-ea4a-3dfe-8258-8f263b78b5f5 | -13.93974 | -47.45276 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9f9591e-b504-3951-bcf8-acb2deb65736 | -13.16818 | -48.30056 | 2025-11-20 04:33:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b5bb7fb3-fa30-367b-9e89-0cbbe58b49cb | -14.74522 | -51.1338 | 2025-11-20 04:33:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c93a6f7b-8d47-39db-ac85-dbcf3aa22e9e | -14.94898 | -47.34115 | 2025-11-20 04:33:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 618e2bf2-fc7e-3208-b7a7-12706f6aa8be | -13.93858 | -47.46061 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0a8b1f7-0cda-3157-990b-7e4da2305862 | -10.91753 | -48.67326 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6ff78ec-9450-3832-8eec-c166c2e0264e | -14.66352 | -46.5263 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d6531ea-3a93-3043-a62c-cf88ac69f1dc | -10.73025 | -49.68189 | 2025-11-20 04:33:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a916d96d-da91-3537-aa41-a18f403485b8 | -12.48899 | -48.39204 | 2025-11-20 04:33:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99ff0b6d-2a6d-3e19-83a7-88415046e6db | -12.61838 | -48.87129 | 2025-11-20 04:33:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c218df6-b2f6-3978-90a5-6e04a03f89ac | -11.26125 | -48.49407 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a39284e-fa7f-3b24-8169-e5d2243fb2ae | -13.19834 | -47.94356 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00252be3-34b2-3c0b-b5a5-62585556eaa4 | -11.96553 | -46.55737 | 2025-11-20 04:33:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99a338b6-90b1-37c8-8a96-1f25677b488d | -14.52674 | -48.62217 | 2025-11-20 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b680d067-d378-37c0-836a-c97c9ebffdcb | -14.87308 | -52.88259 | 2025-11-20 04:33:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2ca749e-2ce5-3fc9-b3bf-4e0f359bffe5 | -10.02453 | -48.1287 | 2025-11-20 04:33:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f6906bd-8eb8-30e2-9874-9b8da62766cb | -14.95017 | -47.33306 | 2025-11-20 04:33:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2c5f414-1edf-3d53-9926-7837f61d5912 | -15.88808 | -43.4535 | 2025-11-20 04:33:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 213fad95-1f00-34bf-be99-8ca1b6de18d9 | -13.87453 | -47.39874 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11243a92-be2c-37f2-9f18-eb96315ebd65 | -11.65819 | -49.6165 | 2025-11-20 04:33:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 339f3dca-013f-37ad-aa3c-c00f40439f92 | -12.89748 | -54.72811 | 2025-11-20 04:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08f48933-2e6f-3bd6-b5c6-11c0a7ef4349 | -12.94104 | -47.72074 | 2025-11-20 04:33:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ebaa3d2-ca34-39dd-9b5c-35070b2d819b | -13.51191 | -47.92311 | 2025-11-20 04:33:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa9da0ee-b3a7-30e7-9e95-2e6cb4729d54 | -10.83646 | -56.95827 | 2025-11-20 04:33:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 8e1c463e-220c-3db1-97ed-0bc886c214e3 | -9.01652 | -48.66387 | 2025-11-20 04:33:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78bad584-821f-3990-bb2f-ab6271b16f30 | -15.40402 | -49.27364 | 2025-11-20 04:33:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1058c0b-cd5a-3e88-a277-fa09b07431f7 | -9.70743 | -49.9361 | 2025-11-20 04:33:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76068677-e7c6-38a3-a4ab-538b23e4dcde | -10.84134 | -56.95924 | 2025-11-20 04:33:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 0aed4f99-22e8-3515-9291-39b71d2a16dc | -10.33799 | -47.77228 | 2025-11-20 04:33:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e806dbe6-19dd-3f8a-9c49-82af6f24bc19 | -9.35266 | -50.74276 | 2025-11-20 04:33:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e2bbe75-d804-3854-bd61-df753b994864 | -14.88535 | -49.57385 | 2025-11-20 04:33:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ec8cc34-685c-3195-81ee-23a346c30892 | -11.25848 | -48.49002 | 2025-11-20 04:33:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8fe2a2b1-f820-38f0-82de-b84567fd2f25 | -14.63287 | -46.50813 | 2025-11-20 04:33:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04436fde-6280-3c5d-a664-0edd33e8d33b | -10.5414 | -47.99363 | 2025-11-20 04:33:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a46c825-b845-3a52-984c-6b9529b80a39 | -14.51289 | -47.35984 | 2025-11-20 04:33:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67f50e09-b9e2-3dc4-9188-21900d1ecaff | -12.88338 | -50.15708 | 2025-11-20 04:33:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README12.md)
