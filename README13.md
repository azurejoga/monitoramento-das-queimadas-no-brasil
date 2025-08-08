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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08d2b972-909f-3124-848b-8aa7a6a03d37 | -7.18748 | -44.3882 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b990449-a0fe-350a-8504-6bca938d18f2 | -9.47454 | -57.84631 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 487df5d8-80ad-39af-84a8-66335745986a | -7.26765 | -44.31898 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 582ca226-e21f-39ef-9752-e3962422ce2d | -7.89488 | -45.34232 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66e9a26d-7acc-3135-9ee8-38b2c18b7398 | -7.38375 | -44.65394 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d28da298-0701-32c7-b25a-cdfe677b2c90 | -7.2328 | -44.47956 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 026666e3-fc0d-349d-911d-3cfa31fd2699 | -11.46012 | -47.31225 | 2025-08-08 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c45ecfb7-9a78-3e7b-8e48-c4d49d4d7e5b | -9.70835 | -61.29428 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cc56f55-cea1-3c57-a6d6-47fce1ac94b9 | -9.0667 | -45.05539 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b985924-b7b4-3aae-a57c-058af043eee5 | -8.20934 | -45.06105 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fe4250d-464f-380e-830d-d6d69e5d2e21 | -9.47442 | -57.84911 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1d3cb1-d1db-3848-a997-cae6a0e683df | -8.21344 | -45.05988 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6940f20-54df-3d3a-81b6-4797b316fd3c | -9.8712 | -49.96294 | 2025-08-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6274c57a-d85e-3ce3-9e50-c7503a65b0f5 | -12.72426 | -46.37664 | 2025-08-08 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0650524e-0907-32b5-8f8a-6a2eb47c9f2b | -12.52634 | -47.13834 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af819f5d-6f61-3b62-9f86-bfc5794ba248 | -10.62687 | -44.76048 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 5bac4a5a-d341-3f49-acfd-0e5d01e148cb | -12.58073 | -47.16943 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49a8743a-749d-39ee-a4d9-03cdda84461b | -7.24695 | -44.66648 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| baafa5bf-a605-31ba-bf5d-099ab5e5d9f5 | -7.91681 | -45.53655 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eeb4c3df-2321-3b60-849d-943e00434cc7 | -7.90797 | -45.35281 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b973fafa-225d-397a-8307-37b008018e4a | -8.05303 | -46.34375 | 2025-08-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5238fa40-57ce-3055-83f8-bfc03ac10c5b | -12.57532 | -43.79435 | 2025-08-08 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4de45328-bc49-3fbf-9086-15c080b2b582 | -12.49396 | -47.49759 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3391f21b-b552-3941-a2d8-80eae896533b | -8.33058 | -46.57253 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52e1ab57-23a0-38a7-a6fd-b1e52e1a5cf9 | -12.57316 | -47.14843 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b08558e-111a-37cc-89dc-30bc5e673cd4 | -9.93861 | -60.51113 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ab31ddc-187c-3e60-b1da-dee5bc07a779 | -8.92495 | -60.73477 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e26c7ae-3a84-36d9-83be-9d3e2b351443 | -11.7505 | -47.50145 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d44f165-080c-3a16-8b21-b73346c867bf | -9.70615 | -61.30535 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4b7f05f3-c52f-3ba5-aeda-c26c2b6217d7 | -11.0276 | -45.06412 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac539c07-000a-3e42-8a13-269c7023475b | -12.53385 | -47.13554 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f88338b5-5bc4-3c9a-9664-9b0bcb124c1f | -7.86709 | -43.86253 | 2025-08-08 04:34:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efdc38c0-5b77-3d0f-befc-1c7caed90f56 | -7.25128 | -44.66272 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 85d673e7-56bc-34ab-92dc-b31bb368f039 | -9.06604 | -45.05987 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 901ad580-56a2-36f2-b3ea-e364bc9ee45e | -10.42404 | -48.57237 | 2025-08-08 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df33d18d-99e0-3c91-82f2-c1467ed8f7d9 | -12.53731 | -47.13607 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ceb8419-41b3-3b49-bc48-9564b1eb0d1b | -12.48285 | -46.91623 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e1713de-9dba-35cf-937a-2a498ae40951 | -7.40967 | -47.13823 | 2025-08-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b201442a-13a6-36ff-b98e-b7e3587f6446 | -7.25372 | -44.59538 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e2913f62-5a39-3718-814c-e9836827903d | -12.09423 | -44.73113 | 2025-08-08 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e978c6c7-77f4-3991-bf52-8c6d52931aaf | -12.54078 | -47.13661 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 047adf30-93dd-3b4b-8e99-09e75700cc90 | -12.524 | -47.10617 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b853b350-5449-34ba-8e22-56bb2bbb0c0b | -8.9239 | -60.7401 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76d3f6c6-ab70-36d3-acc5-9085be44ebf5 | -9.9256 | -60.48538 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66bb6e4d-2570-358e-b43e-c6909e676665 | -12.54425 | -47.13715 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20af7189-f1d5-342e-9a1e-17b2c1029ef7 | -8.90727 | -60.54162 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1dae59f4-bdd3-394a-a6d9-b6a4d05330e2 | -6.82121 | -48.64658 | 2025-08-08 04:34:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31ba5472-0b11-3779-94d6-4371d47e35f2 | -12.57082 | -47.1492 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3622ff5-f0e0-30fc-a9b9-ef110ace2c3a | -9.0604 | -45.07251 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9af4c4f-6fe6-39a3-bfa4-5b246ded3030 | -11.19205 | -51.43328 | 2025-08-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32919f8d-4844-331e-8206-2dad7930a2f1 | -9.94126 | -60.5038 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdef0301-deab-39c3-9254-b5394104066f | -7.10276 | -44.22798 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 676942b8-3882-3f90-8cdd-f9654995939b | -7.70217 | -45.51969 | 2025-08-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9535b841-bfe4-38db-8d1d-35f26facbc01 | -10.63 | -44.76582 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 423d25f3-afd3-34ee-bf94-947b9e570340 | -10.5882 | -45.24831 | 2025-08-08 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1f4159f-f201-3457-a2df-d5608d8a3c2d | -7.40632 | -47.13772 | 2025-08-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe6e17f6-4eec-3b62-baf1-6fcae75346b3 | -8.93028 | -60.74124 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b8e9de9-3094-3b18-93cd-b482153668df | -7.10653 | -44.22849 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecc7eeff-30ef-3e16-bcbc-c35454c513c9 | -11.74466 | -45.02308 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5c544ab-7a5c-362d-983a-ea27dfc8d076 | -7.92717 | -44.81769 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c9941d5-16f4-3462-a0ec-70aba210ae7b | -7.06086 | -55.41633 | 2025-08-08 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cccaf21e-638b-313c-8f49-5f987b5c33cc | -8.92923 | -60.74659 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0506cf3e-a614-3a5c-8f4d-116f7babd8ab | -9.93695 | -60.49288 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cca8f01-4a0a-358c-9cfa-be034149d388 | -8.52324 | -43.30914 | 2025-08-08 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cbe04a4a-2ace-3c79-9765-d83e246c780a | -7.72337 | -45.52138 | 2025-08-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96e7273b-234e-34e5-8ed6-b40f8ecf8be1 | -5.81281 | -59.2306 | 2025-08-08 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 82505db8-e40f-33b1-87c7-5aee5865a149 | -9.70185 | -61.29305 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e55f02a-b841-339c-b293-d31e066abc1f | -7.25815 | -44.33149 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04779bf7-2219-30c9-b258-d587e3f959e3 | -12.31002 | -50.01201 | 2025-08-08 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b43923c-118b-3a51-8b4a-1bf8a390f2de | -12.57783 | -47.16502 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8991557c-8007-3889-8ca8-5203da2c6b9b | -7.93146 | -45.31829 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06785d56-75b5-338d-a327-bee4ee428054 | -12.89697 | -43.77727 | 2025-08-08 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 966ab240-6bf8-3b90-9498-be4f5c815dd6 | -12.70511 | -46.38231 | 2025-08-08 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc5e18a8-d27c-37be-be73-82f930adc649 | -10.53054 | -42.5489 | 2025-08-08 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25f2eaa1-fe79-340e-a8d5-081efcc7e4ba | -7.89549 | -45.3382 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ce0a00b-b486-3ff7-8e84-57db7b083dd8 | -7.2476 | -44.66214 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78c1e4cc-b19b-3521-a888-5553c7dde532 | -12.30726 | -50.00792 | 2025-08-08 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1257d1ab-1e83-3ccd-9007-92fdc3a58ffc | -10.62618 | -44.76525 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| db721704-5a37-3fa7-a4d7-ad3cae30d904 | -8.93125 | -46.74671 | 2025-08-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e08a63a-b581-3a8c-9e81-c9c951a35d9a | -8.99035 | -45.68283 | 2025-08-08 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5507a58c-0fca-3b1b-8896-12f5ccf2d2cd | -8.93466 | -46.74724 | 2025-08-08 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39d8ee5b-46e5-3b3b-9bb7-51ad337ef7d2 | -7.58926 | -44.90548 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5160d9a4-4f73-3b3e-998f-82e219867d14 | -9.87512 | -49.95992 | 2025-08-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c26af70-71b2-3ec5-93c6-e08730a60cd8 | -9.71342 | -62.41057 | 2025-08-08 04:34:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc411f56-0699-3930-86ef-d56f3a4e5b2e | -11.02692 | -45.06881 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f304c85f-2aab-321d-9b62-e0b0f5a95e24 | -7.92098 | -45.53303 | 2025-08-08 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bcf5b65-7219-36d0-b0f2-c9c861b2e354 | -8.11148 | -47.43532 | 2025-08-08 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83d1a816-ebb5-321d-9409-632877b2616d | -9.47383 | -57.85241 | 2025-08-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 655d8ecd-7760-3840-a274-9a71e198bfb8 | -11.02294 | -45.07109 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0063fd74-c3c6-3988-86aa-00e26581ab2c | -10.63376 | -44.75851 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 51abd1e3-acb2-3bfd-9f14-20b207b4d398 | -12.55521 | -47.13497 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a48d1dfc-998a-3b52-b169-a81047cea481 | -11.78645 | -47.52146 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f24f1f7-9e46-37ba-b6ea-77903935b821 | -12.57896 | -47.15727 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8caba59b-43d1-3c11-a4e6-d020574079cd | -10.43385 | -44.34932 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b9f5471-5012-3b22-adbe-8dd2215c8b57 | -12.58363 | -47.17385 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 93d7239d-545e-3880-81d5-ac43266ad006 | -11.75094 | -44.95086 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 292800aa-f917-33a3-b1cf-60b6ee20e3d2 | -10.83218 | -49.37659 | 2025-08-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cc320d8-3dc2-3e82-82fc-04ea5b04836f | -8.2087 | -45.06529 | 2025-08-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7965c42-118b-393d-bd36-5a78c16c226f | -11.02671 | -45.07167 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3025640b-d29c-3211-a57a-b92029bb7801 | -7.89897 | -45.36405 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README14.md)
