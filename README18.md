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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6368c15-8c03-3ab1-9e51-bd368a956df8 | -9.0832 | -62.6674 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29debbaf-01b3-3eab-8b80-b9185e3439d1 | -6.691 | -58.537102 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6ab2de5-4b4b-364d-a6e1-a277a75f0a5e | -8.8681 | -62.441799 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67a59971-0c28-3815-9640-441fb044d223 | -8.8893 | -62.444698 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 96c08556-3377-3669-a875-86cb01e1485b | -10.4243 | -64.378403 | 2025-08-26 01:32:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bbb62f47-4342-3cfd-af45-0f7698c28011 | -8.8697 | -62.449001 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc73830-8187-30d2-bdc9-834220b01a5d | -6.7084 | -58.5672 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ca4c61e-9643-32f8-b7ed-b8db2152c895 | -6.2435 | -60.023998 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3621bc72-5b57-3111-93bd-02920f9d9f6a | -9.2786 | -56.9086 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f38568c1-f10f-30ef-9c05-5ceafe35e2c9 | -10.3968 | -57.697498 | 2025-08-26 01:32:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a9dce27-d1bf-3ef6-9f99-f55115d1ac63 | -9.1885 | -59.459499 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea9d7754-061d-3aa2-a5a1-b83567d8b6b6 | -6.5768 | -51.120201 | 2025-08-26 01:32:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1493114-5257-382f-9216-a8ecb0d1b2c8 | -7.3567 | -59.661999 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c42180a-75cf-3ea2-b4bc-bbfc8c02e270 | -7.2963 | -59.6684 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df761ca2-656e-331f-8e7a-a23b35af8375 | -6.7046 | -58.550999 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edeef21d-1127-30e6-837b-1c4cc40f5124 | -8.9959 | -65.404099 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee795a8-5f59-363b-8f28-b18621fe07af | -9.2569 | -65.617401 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8987215b-a6ab-305d-9cc8-a219054a68bf | -7.3905 | -64.351601 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df6f8d84-c959-3fa3-b6ca-a621a06ce868 | -9.2439 | -60.9119 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0658aa6a-246b-384a-9e8a-75e604f3972b | -13.4506 | -51.1278 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d1d1c1b-c5af-3bd3-845e-3839b1ab410f | -7.3584 | -59.6693 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04ab524d-edc3-3069-a090-ec3c26303318 | -9.2644 | -56.892601 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f089d150-68f7-3725-a9d1-a08234ea44a3 | -7.4784 | -61.355202 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53cd07f1-0034-33a9-a2de-1f6771e84b91 | -9.1684 | -60.762299 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0a25618-bdbb-392a-bb0f-582b753c33a3 | -11.5491 | -52.119701 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d35fe6d5-16f4-3a19-a153-46f4d88f6664 | -6.8171 | -58.9422 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dcb1a1d1-62ce-363d-a583-b9c2ceb8f6af | -6.2516 | -60.014599 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57036263-2b25-36f6-964c-0ddb01b960f5 | -9.1602 | -60.7714 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bff9c2ed-9d13-336c-8599-c008bc36e4b5 | -9.195 | -59.442902 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 276dc058-e6dd-3a67-b6fb-6f6552a9430c | -8.2424 | -61.450001 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4bb2d02-83a1-3962-9d19-b84a27595108 | -10.8772 | -55.783501 | 2025-08-26 01:32:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e33d4495-6b0c-3b69-ae92-2546fe6d34ad | -9.2742 | -56.890202 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b97e0f8-932b-308c-9224-16095715fa88 | -9.2688 | -56.9109 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea8a5639-399e-3b3a-a04e-ba51809abbf6 | -7.3985 | -64.3414 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29b61b1e-6d44-306f-9b27-614a23b9df04 | -9.8031 | -64.256302 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7fa14b-2b65-359a-866f-946553d49ce7 | -9.2423 | -60.904999 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 965d0b10-fba8-3991-aeb0-64250b83789b | -7.6568 | -61.459301 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 098572b5-d2a1-311b-9bb5-5f57537d8a70 | -6.8207 | -58.957699 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb522caa-847a-35e5-af39-6b7b18ab17b7 | -14.1158 | -53.9837 | 2025-08-26 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8efe2db-0a56-3b75-8cec-6040fdd8722e | -7.4337 | -60.619801 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03c27123-968b-32ea-b369-d5f43bdf5d5d | -10.393 | -57.681099 | 2025-08-26 01:32:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5750035-1b34-3cfe-afda-75ed903460c2 | -8.5491 | -62.626099 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 501915c6-7f93-3cdf-b75e-25bab2580234 | -14.4312 | -56.446999 | 2025-08-26 01:32:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec27af5e-5638-32f9-888a-4ba957180d11 | -11.313 | -55.114601 | 2025-08-26 01:32:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca9319f8-acae-3778-94a1-a6cf5d725af8 | -9.187 | -59.497799 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63dc62ed-89de-3863-a692-47788d991d81 | -9.2267 | -59.6693 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00c48498-dc7c-38a1-b035-144676d17c30 | -8.9882 | -65.415901 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebb1951c-6762-37be-9d86-87e06829d6da | -7.3887 | -64.343498 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb94d93e-ab99-3996-acc1-e9e7eeb163e8 | -6.3079 | -59.856998 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67e293fe-3141-3a71-b24e-81e4e2dc0af5 | -11.5544 | -52.099998 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f45aeacf-9abf-3d5f-86fb-ef1364079f48 | -11.5447 | -52.1026 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07c35423-e08d-35a2-a82c-b9f91acd30f7 | -6.8127 | -58.9678 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9153b2-99d0-3932-acda-9c13bb6a7cae | -7.2946 | -59.661098 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36cece7c-fc8b-3f7d-9497-e629190c11b8 | -11.7037 | -60.1665 | 2025-08-26 01:32:00 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc5d129a-c991-3354-9938-270966936db2 | -9.1691 | -59.509499 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d17f011-57e9-3170-8018-ee4361df6b84 | -5.5296 | -60.1945 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12e38b74-49e2-365c-b0a3-a41a7375511b | -7.48 | -61.362099 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c83ad78-fbfd-33de-bda7-4403dd280ab0 | -9.1937 | -59.526501 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd2e6ad6-f7f5-338a-9d2c-a677f967b207 | -6.7792 | -59.664398 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 447ddccb-3189-314d-a3ba-a34890cfa19c | -9.2454 | -60.918701 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3010efbc-cbf4-37ae-a471-321b79814760 | -6.8305 | -58.955399 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e08a38b3-be5f-33bb-bfd9-6012ffc9ab1c | -8.2538 | -61.4547 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8762ad-6e75-304d-b12a-8f507d9cbca1 | -8.8779 | -62.439602 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd3d8277-1646-3b3c-92c5-8b25f8056f63 | -10.3949 | -57.689301 | 2025-08-26 01:32:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8b2f10b-fcee-3dcf-bd7a-a0bf5f5f5251 | -11.0803 | -49.984798 | 2025-08-26 01:32:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc83f70-2479-329f-8891-a778d5db1247 | -14.445 | -56.461601 | 2025-08-26 01:32:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c03e853c-d21a-3c0e-8715-bda96b0aa3a7 | -9.1595 | -59.557098 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fee9e691-494b-3d49-8b07-40889fb1da7c | -10.1217 | -62.8974 | 2025-08-26 01:32:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f64e91f-2dca-33bd-a492-b776a3b44684 | -6.8225 | -58.9655 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4ae700c-87c4-3159-b022-1ddb212c269e | -8.9784 | -65.417999 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7434e44e-b03a-322f-a17d-a6417793a5cd | -8.8795 | -62.4468 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 330ae609-4747-3668-96d3-d810858f50b8 | -9.6497 | -59.623699 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d95544dd-8ab3-3f8c-ad60-411e663785a7 | -8.7671 | -63.9319 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30912466-d607-390e-8258-0a18b5ccd7e0 | -9.6432 | -59.640301 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eebd5de5-3a89-37f9-b7d6-741d880a0682 | -7.4223 | -60.615101 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01e25a25-f8f2-3e88-87ca-ce639a0a0af3 | -9.0036 | -65.392303 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66a48b4e-7047-3ef7-bee6-d4311abb7273 | -9.1545 | -59.535599 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76a0d3df-8bfd-3196-8753-69942f4196a2 | -7.3807 | -64.353798 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a07700dd-111f-321e-8282-4d955acdf5af | -9.2764 | -56.899399 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| deb2d098-014b-3458-9b6c-c35b1aa024f6 | -14.7565 | -59.7155 | 2025-08-26 01:32:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 610f412c-e1b6-38a9-8a71-2876566914b4 | -9.161 | -59.518902 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63bdcbf3-7080-3bed-8861-ea66544b999b | -6.7182 | -58.564899 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea2c07f-c8b5-3cb8-8d86-d5c7d197458d | -9.8012 | -64.247704 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35ccae28-aa87-3bc3-8158-8708c00cb61c | -11.1396 | -44.7654 | 2025-08-26 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 6fa88b50-5970-3730-91e7-651206986962 | -23.0471 | -50.3872 | 2025-08-26 01:40:00 | GOES-19 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 139.7 |
| 3e7a470a-4746-3844-9cf9-eefcaf0d2b5a | -7.3854 | -64.3475 | 2025-08-26 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 871ec1a9-7e36-3e73-a28a-b13a6f63b8b3 | -11.1583 | -44.7859 | 2025-08-26 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 823b93eb-eaae-336c-ba6a-18bc9cfa753c | -6.8412 | -58.9746 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 06ea2d04-31df-3dbe-bdf1-1eb3cb29cc2c | -6.2275 | -60.018 | 2025-08-26 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 646821c7-25e4-3f4e-96a8-326e37a40382 | -11.1591 | -44.7395 | 2025-08-26 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| d340b91d-bf51-3d41-905b-87968e67fb71 | -6.8229 | -58.956 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 282.7 |
| 883ae302-730b-38f3-afcd-6c413953c27c | -11.2937 | -55.1129 | 2025-08-26 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0707cf23-4495-3f78-b2bf-c4628db0d1b4 | -6.7476 | -62.8664 | 2025-08-26 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a59e7aac-ff04-382c-8167-3fbc2b9338f3 | -7.4224 | -60.6236 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 8fdbc404-82bf-3c6c-8519-1aa7df56bf0d | -8.8363 | -62.451 | 2025-08-26 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 4400732a-ea62-3735-ac12-cd426038e7a7 | -8.9874 | -65.4192 | 2025-08-26 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5eafdfaa-6561-33ed-a91b-2a290763f67d | -8.855 | -62.4313 | 2025-08-26 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 588e7dcd-8770-3fee-8fbb-1a4a90637b3b | -4.9605 | -55.8226 | 2025-08-26 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f4a3245a-e1fb-3b7c-b8b1-065a2ba5f310 | -6.6961 | -58.5546 | 2025-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 6ba90f5f-df3a-3fae-90b4-6c7aecb6081a | -4.9606 | -55.8028 | 2025-08-26 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |


[Clique aqui para ver as próximas entradas](README19.md)
