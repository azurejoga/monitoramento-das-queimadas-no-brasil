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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 575fca1f-6679-3e53-a63c-832af2d159f6 | -1.5757 | -53.86378 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1de4a84-c809-3afd-870d-860ea0c9221a | -2.97726 | -53.28806 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d0cb037-dd2d-3ad4-951f-b7cac321d2db | -1.59822 | -47.32618 | 2024-12-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 108a58a5-ed21-31a2-a6f5-94dabdba686f | -3.42148 | -50.18139 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff68193d-e9d0-3674-8462-2dcbae9c420d | -1.67125 | -53.77477 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ab0c91b2-08f3-314f-8985-acadc943a933 | -3.98434 | -46.63813 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db9c234e-fb59-3729-9557-08a279ae0284 | -2.62743 | -54.21227 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4845b213-8f60-3295-a541-c9b4b6a7d27c | -2.98758 | -45.5687 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5278d2b-50e5-3612-9be4-d8610f8ef7a8 | 0.93632 | -50.74035 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06db0711-0a4a-3b53-83e4-f499a793cb2d | -2.90247 | -51.58202 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c47072da-546e-3ee0-830f-899e73714f0e | -3.97585 | -46.53606 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e450df4-3da2-37c0-a67c-57f2a6554a7b | -2.65177 | -46.58098 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a11a5445-ec7e-3404-97fd-9c85769dbf99 | -2.6305 | -54.22886 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf334816-ea30-39cf-ab7e-88888109bc03 | -3.21423 | -53.1213 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8f4a2407-cbea-3fd5-b1d5-8dabc2ce4bcf | -3.61491 | -50.1909 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd09f13d-e187-39c3-8c35-248b1ff53191 | -1.80164 | -46.63426 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebf1c565-fde2-326e-ab2e-777e06ffff5b | 1.25099 | -50.6804 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 01ff676b-490f-3c36-a586-f491e1ecab87 | -1.92065 | -52.66188 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1183eeac-0e41-3188-89ba-2a92283f4222 | -2.66589 | -46.25481 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2253ffe7-7ec2-392b-b735-314c1e3b17aa | -3.78995 | -48.09048 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a660f674-edd1-3b20-a6dd-08dd20736c5b | -1.19485 | -51.75284 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42c87f01-220b-3ac2-b38c-2150fd02b422 | -3.02844 | -51.54017 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dbd8ad0-6e5a-3cfa-a28b-2319523c68df | -2.12237 | -46.55677 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4218497c-7a33-356f-b70f-bc0189041eca | -2.73839 | -54.97523 | 2024-12-01 04:21:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 51044703-7424-3a7e-88bf-5e8e3b4595f1 | -1.70455 | -52.43819 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 074fd9db-35a3-3fc3-955a-b1282a24eae5 | -4.22879 | -43.01566 | 2024-12-01 04:21:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95d71b7e-c0a5-3389-ba3b-3c09be53bdf5 | -3.54409 | -50.17532 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42c181b5-b831-319f-94c9-0fb2047326fb | -0.84555 | -48.52527 | 2024-12-01 04:21:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29571210-df34-31f4-80ad-17e8714e9716 | -1.64568 | -55.06575 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ac04187-56ac-382d-86f4-7e8d60104276 | -2.51765 | -51.8354 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 416bb0b8-7b6e-3637-a556-7b3e5c6c3884 | -3.46628 | -50.27462 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2283e023-f98e-3663-89d2-fdfb02fff778 | -2.625 | -46.95244 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff43a97-fe4a-39de-9c8f-fe363addc1fc | -2.68078 | -46.60134 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4603149d-09e0-3bac-ad8b-abe9d27e036b | -2.80893 | -53.06144 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 718909ea-7811-364b-8141-ccb286585353 | -1.64419 | -53.87079 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20aeae83-760f-30a7-98c6-f23b3800f635 | -1.73219 | -46.66098 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 264803c4-99a4-38bf-8e94-22a371eb12a5 | -3.26751 | -45.128 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c00b80b2-25a4-32c5-b973-09bb1cc3a696 | -3.5262 | -50.47878 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d845633-e9e4-383f-ba4e-dd26d513dccb | -4.05006 | -46.115 | 2024-12-01 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a60bead-77ea-3a99-ad56-901449e79ce2 | -3.12335 | -51.79463 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ce0d1c49-ac35-311f-a4ef-524a8a1a29f0 | -1.43221 | -53.39586 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cbb9580-23b3-3618-8a2f-e9368e5966bd | -4.5413 | -45.69869 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aa3f9a37-8e60-3cdf-b804-a6fcd148a583 | -2.67543 | -46.61245 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3914ed0e-9da0-31db-85ef-bc2219c1acea | -3.03712 | -51.47646 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ff11337-ce12-34c2-8daf-98247c0c9515 | -3.1393 | -45.98895 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caa71c36-bc9c-32cf-99aa-1a6074d2af9e | -2.63663 | -46.12738 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dd13d19-47fe-3695-a1d3-bd495eed8763 | -4.21705 | -47.71743 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de411c91-dbe5-34a2-ad4f-60a0b5be9599 | -2.99039 | -45.5728 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 632f2caa-cea7-37e4-b494-051005f58a06 | -4.5307 | -45.70064 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f797c64-a7c2-3bd2-9a72-37d2405b8251 | -3.89681 | -46.6833 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07014d5b-345f-3c27-9123-320f317ce9fb | -1.14567 | -53.66769 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77d44bdc-b594-34e4-8039-4906e27863ba | -4.5514 | -43.30579 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 1727b46f-dfec-398d-a5c3-7c112681594f | -2.59975 | -46.07186 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3f63dc-bbc7-3bf4-9e2e-f32e1a63da8f | -3.07361 | -50.98686 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 78e11763-46d2-3792-be91-09b520f3b03e | -1.72173 | -52.62444 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2b7db13-10eb-3ac0-8c14-2383b4a741c3 | -3.54091 | -50.44246 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd3815c9-1185-32d8-8b7c-63525fef0e75 | -1.45569 | -48.20292 | 2024-12-01 04:21:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caf78b31-d636-3521-9c95-2ec3f72f674e | -3.28528 | -50.63084 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a009944a-b06b-3dd6-83ca-6eb2ff9da201 | -2.64007 | -46.1279 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1254922-e0ce-3878-88c4-59424949e3bb | -4.03958 | -46.9296 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5ae60883-5140-3d6b-b24b-3c26bd13a26c | -1.51997 | -45.90732 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be27f2ab-4c25-32e3-8ed4-54e43d17fd02 | -3.85916 | -46.54115 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d328a01c-30b1-31a7-a9f5-6c6d5d1f3bfb | -2.12488 | -46.41874 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c8f77fe-77a0-3b1b-906e-6cef982d5aef | -3.1719 | -46.31644 | 2024-12-01 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4f8d66d-096b-31c6-8469-d66afc621190 | -3.12661 | -53.09629 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75dd6ad5-94a6-3f47-bf8b-22c785d2f45a | -4.17226 | -46.55882 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce9a25ca-836f-3ba9-b235-3e399c2d1569 | -2.6647 | -46.12786 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88f5ab6f-b2f3-347c-9e01-142f2db89ba9 | -1.26409 | -54.55542 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee113ec5-d69b-31e8-8a5f-57e7c964bcfe | -3.45622 | -44.92265 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02491708-6689-363e-bda2-56e4f166c2d3 | -2.29042 | -45.60775 | 2024-12-01 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 73b5b5de-96ee-34c6-8737-48ce41c808e5 | -2.9887 | -45.58355 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 5c5362e1-7d9f-3180-922a-47d94db0801d | -1.19396 | -51.75839 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b1cd115-db55-3fa8-881d-34b0a1bef6b1 | -3.94751 | -41.49144 | 2024-12-01 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d054250-747e-3ac4-8771-02c91ca9d24f | -1.07713 | -53.6285 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c26bd444-556a-370d-bcea-4014fbc41858 | 1.25124 | -50.67826 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 457f1a6a-3c59-3634-9ade-0e813e7e0df0 | -2.62371 | -46.96054 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5be0c082-6627-3eae-ab5d-3317264e5502 | -2.56331 | -46.32795 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d84e3cc1-ae4d-30e8-903a-d08fa1eaccca | 0.97541 | -50.12202 | 2024-12-01 04:21:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee21024e-b90d-3a56-bad4-3e1bea6ad015 | -2.03094 | -48.73404 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08b94adb-54c3-3827-86ed-71a469899dc5 | 1.14828 | -55.98849 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 75ada6a4-62be-38f4-9da1-97138e53336f | -3.8557 | -46.54067 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 83a87212-76d3-3ea9-bbfc-d8bdae11ca8e | -1.72223 | -52.491 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2da27924-b583-34e9-9463-0587aaf42792 | -1.18722 | -51.76872 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17216ea0-9e0d-3a99-8e45-153e650d0b19 | -0.59733 | -51.69386 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ad3f286-5957-3268-92f4-594689ddc4bf | -3.32883 | -50.1926 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 07b6faaf-4ba2-3e5e-b5f2-b0e1093cf24f | -3.93579 | -47.97602 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e9de8de-67d9-3e5b-aa69-e87de4532152 | -4.5542 | -43.30984 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 1dd5d13c-cd95-3ab2-ba56-48500f545348 | -3.05242 | -51.05936 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 76fa7779-edd4-3737-9a92-0d13c4d483d7 | -1.14547 | -48.33269 | 2024-12-01 04:21:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9786a74-9a05-3dfe-8d85-abf8d9340369 | -3.44161 | -52.04136 | 2024-12-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb395f8d-903a-33b9-997e-34f0dc834a00 | -3.11972 | -53.81033 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7dd99251-b7ab-3147-8a28-f05a0a8064bb | -3.81372 | -46.67803 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d1565b7-bd93-3b52-b962-4d1ec2926b88 | -3.69703 | -47.12072 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8783570f-9b35-3ef0-832b-b22076c74b69 | -4.44538 | -45.35976 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75548d3f-2901-3cf6-aaac-6198c314d1ab | -3.47193 | -50.26712 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a8065b28-91da-3ee0-8e83-12ce954ca04c | -3.60155 | -50.37977 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64c21727-f0d0-3bb2-97f5-b3eb7263ea7c | -4.10612 | -46.11238 | 2024-12-01 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d58de86b-f1a5-3bdd-a816-8c12bcdbcb7b | -0.60229 | -51.69461 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e4b3b99-3a2c-3b5d-90d2-d917794973c7 | -2.84117 | -49.88119 | 2024-12-01 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9cb893c5-008a-3213-b9ec-e6dd1f3b0a6c | -1.15015 | -53.67572 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
