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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0d09ded-8c79-33c7-aaa1-bb3c9f67a07a | -11.3442 | -43.9906 | 2026-09-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| d90f37fa-8c4d-3c14-91e8-cbc097ea8b67 | -14.1542 | -45.1675 | 2026-09-18 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 281.9 |
| 971921bd-5cc6-3faa-9dba-62a787aceca8 | -11.4541 | -51.4754 | 2026-09-18 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 0866b661-5fa1-309b-b3fe-457cb9d13f7c | -12.5341 | -47.0964 | 2026-09-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 110a2f84-5422-3c34-bf25-e3e85ed48b74 | -9.699 | -54.8176 | 2026-09-18 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 185fedcd-c4dd-3b45-a8ca-94f0478524ad | -9.6988 | -54.8379 | 2026-09-18 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b741599f-dffd-3898-a9f8-91b777edace1 | -8.5425 | -44.5363 | 2026-09-18 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 279c39ae-b522-300d-a379-3369bcf6d37f | -9.9768 | -50.2694 | 2026-09-18 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| cf0b726c-f0a2-3177-86d8-5a6174d936c4 | -6.3287 | -55.2677 | 2026-09-18 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ff40a69e-7099-3d33-aae0-9a7bfe885a80 | -12.998 | -46.9381 | 2026-09-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8b23e5d1-0aed-3141-a6b9-8c71b423f5af | -11.8556 | -50.0006 | 2026-09-18 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 5fab6197-2d8a-32e5-8b56-e39d68c75a75 | -10.6187 | -50.268 | 2026-09-18 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e3a073a4-fac8-3916-bca5-1551b8888c36 | -10.6755 | -50.262 | 2026-09-18 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 78a62941-603f-30f4-a4b5-b1ae923415e7 | -7.8038 | -44.8193 | 2026-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 477fad24-fe5b-36e9-9b49-454530a1466f | -11.3838 | -47.2982 | 2026-09-18 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 97db6b51-0627-3f6e-986c-f4da2e2f2cee | -4.5587 | -42.9523 | 2026-09-18 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 268.6 |
| a434d35f-1757-3be5-8a63-422604b32b75 | -12.1527 | -46.9933 | 2026-09-18 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c6a61d2f-fb1b-3b69-a066-1bb13b520ab3 | -12.5688 | -50.7308 | 2026-09-18 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8ad363a1-7aab-31e5-b812-8414a3cbdd83 | -12.1723 | -46.968 | 2026-09-18 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9424f376-76db-3487-8e2e-62242db09c9e | -9.8313 | -48.4073 | 2026-09-18 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| aa099bf9-4985-3040-8994-2895e94683b5 | -9.8316 | -48.3854 | 2026-09-18 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d1a82755-5343-3a88-a571-da3178ede7b8 | -2.4814 | -49.4208 | 2026-09-18 14:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8c14b1e2-53ff-3f5f-ae20-f9bae6dca828 | -15.6752 | -52.7339 | 2026-09-18 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 205720b4-eec3-3c11-9739-01f52ae7e2f0 | -11.8934 | -47.6322 | 2026-09-18 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 169.6 |
| c1e91034-165d-3611-8b2e-3881eeff813d | -11.3437 | -44.0141 | 2026-09-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 247.8 |
| e52388f2-f0bd-39f8-bd94-e98ba458a312 | -11.2787 | -43.3643 | 2026-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 47d8272e-4904-3508-865a-4c12b4854474 | -14.4668 | -53.1889 | 2026-09-18 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| deb194a3-662a-3c90-aa24-9038dba1ed67 | -13.4303 | -51.9036 | 2026-09-18 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 34e0e1ee-8c3f-3096-8ed9-61b950f36886 | -11.2783 | -43.388 | 2026-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 8c4f82d2-8471-3c29-be70-c37bca8a39fe | -6.3516 | -41.7494 | 2026-09-18 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 6424c1a2-fbbc-3eb1-a5c1-c12009509176 | -11.8359 | -50.046 | 2026-09-18 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8547b272-e417-3ad3-b4f4-ecc54942f75c | -6.4076 | -47.5319 | 2026-09-18 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 91e550bd-5406-3c34-be6f-463127c7b339 | -12.6427 | -50.893 | 2026-09-18 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 72fd74db-c10c-3768-97dd-5d4f74669a4d | -12.6235 | -50.8953 | 2026-09-18 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 2168b879-130a-334f-8626-5d6b35bf3512 | -14.1737 | -45.1641 | 2026-09-18 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 16e51d41-4065-3060-a84a-0fec0cf97609 | -10.6189 | -50.2466 | 2026-09-18 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 7aa69eae-545d-3f07-80f4-a8179778fec6 | -11.0643 | -48.2678 | 2026-09-18 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| dc230ff9-64b4-3d64-8996-d9acee4fb894 | -14.1732 | -45.1875 | 2026-09-18 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e2c920e7-7c4e-3a3a-8ff4-831b27ea2058 | -6.0196 | -51.7893 | 2026-09-18 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1269bfd3-72aa-3d43-8fbf-a9622bdd9fb4 | -7.8027 | -44.9108 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 364ab9e6-56c6-3cd3-b7e4-b8422d015684 | -13.4303 | -51.9036 | 2026-09-18 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| ef20c7aa-0343-3e90-917c-861ec2f66d3e | -11.3835 | -47.3206 | 2026-09-18 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f44b928e-17e3-3309-85e6-15eb614fa72b | -14.1732 | -45.1875 | 2026-09-18 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| d8f916c3-210f-3a8f-a830-e7466a33ecaa | -14.1542 | -45.1675 | 2026-09-18 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 11b5a98f-6b80-3342-a175-8b43fb73ce56 | -6.745 | -45.483 | 2026-09-18 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9f66eb3b-ad41-30ce-8683-e18b08877d47 | -8.5989 | -44.5531 | 2026-09-18 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 374cccc6-997e-340a-a781-92ded4e0f73d | -11.3617 | -44.0817 | 2026-09-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| d1438600-093c-3599-a37c-ae00904444c5 | -6.0168 | -52.182 | 2026-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4d8c2e97-ef9c-3028-806c-28a1ad2ba90c | -8.5422 | -44.5593 | 2026-09-18 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 47.7 |
| e6e2f619-6258-3e49-aac8-dbdaf510965f | -15.5923 | -56.5559 | 2026-09-18 14:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c1d0c7d4-5463-3840-b4d3-6922fe35dc14 | -14.1737 | -45.1641 | 2026-09-18 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 181.9 |
| d44d4ee5-1165-3650-a5d4-3a95edfe7d4d | -9.5695 | -45.4729 | 2026-09-18 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e20c054f-79e3-339d-b1a5-6c4806cc9762 | -10.6944 | -50.26 | 2026-09-18 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 240.3 |
| f8a23b88-fbf5-31b9-9bf0-bf619e9bcf4a | -12.4168 | -50.685 | 2026-09-18 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5aeac458-fca2-31d3-8b89-0d3aed7d3e57 | -15.6557 | -52.7366 | 2026-09-18 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a42a4b64-a29f-303b-a4b1-102c124bfd40 | -11.3437 | -44.0141 | 2026-09-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 273.4 |
| 1062bd32-cb69-3782-b629-b2acbb01a44e | -11.3838 | -47.2982 | 2026-09-18 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b2b10990-dfbf-3187-8422-be8236293361 | -11.8166 | -48.8331 | 2026-09-18 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 91f4c6a8-4ecb-3dfb-9a5e-f95cfff89836 | -13.6341 | -46.9304 | 2026-09-18 14:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4f8af123-a3f2-30b5-9801-243e6f0239cb | -7.8038 | -44.8193 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 64639e47-326a-3211-9722-1095a49d91dc | -9.8316 | -48.3854 | 2026-09-18 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 73e3d4cd-fa8b-3d37-9f87-179aded6ca44 | -11.3442 | -43.9906 | 2026-09-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 3ddbf5a8-978c-35a8-8c77-8544db5f9e83 | -7.8036 | -44.8422 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 248.7 |
| 9063ea82-58b3-30eb-905e-120f26164d96 | -11.2971 | -43.4088 | 2026-09-18 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| a7dae058-680c-3502-bbec-c16ebdfc88ea | -11.3446 | -43.9671 | 2026-09-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 6f394683-5fa2-3059-8c80-7cf31b584bb4 | -15.6752 | -52.7339 | 2026-09-18 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9b66aff1-8ec7-31ab-bbce-9436d2b79470 | -4.5961 | -42.95 | 2026-09-18 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 244.4 |
| 0bea438e-ab1f-3c7e-b3c7-2e1d64101114 | -14.4668 | -53.1889 | 2026-09-18 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d47aceda-5691-31fa-9321-6838d01e1e1c | -11.9898 | -49.9413 | 2026-09-18 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| fc7462e5-da71-3bc7-bea3-e8376991126f | -12.998 | -46.9381 | 2026-09-18 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 710c574f-c9d2-335d-bd9f-5bb8fb0d107e | -2.0952 | -56.4083 | 2026-09-18 14:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d6373f70-d8d6-3a2d-9439-b6f18ad08536 | -12.3954 | -48.4727 | 2026-09-18 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| de0ff319-5715-3294-b5cf-662f3073102e | -10.3307 | -45.3112 | 2026-09-18 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 33685b17-6281-3423-803b-50648a275bfe | -6.3102 | -55.2686 | 2026-09-18 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| e02f5ed8-e0c2-32d0-8219-60851b870abf | -11.083 | -48.2875 | 2026-09-18 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a975cf7b-f00f-38b6-b093-8eaf0322580b | -9.9768 | -50.2694 | 2026-09-18 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| a33198d8-233b-3b7d-a328-dfe8ba53d68c | -10.126 | -46.2899 | 2026-09-18 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 786370d5-effb-353d-9114-a18b1c798abe | -14.1547 | -45.1442 | 2026-09-18 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 595502b3-9912-3d56-bf5d-b394cf7db7ff | -11.8359 | -50.046 | 2026-09-18 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cfa53ca9-f196-38bd-b068-98ec664c940e | -3.6635 | -42.6505 | 2026-09-18 14:30:00 | GOES-19 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 35ba1d9a-0cb2-3005-bd4a-7a66fc2d3aa4 | -14.8026 | -48.5622 | 2026-09-18 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| cb390392-62d5-374b-aa4d-327b7d7f5c05 | -2.4814 | -49.4208 | 2026-09-18 14:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 0c9d5f41-ccbc-365e-b64c-33d6ae5ccc44 | -12.1256 | -44.246 | 2026-09-18 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 41b5d4d4-dd7a-3b89-aad7-1bbe763bb82e | -7.0063 | -42.166 | 2026-09-18 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| a66cbc24-beef-38e3-b7b6-d48d9accaee8 | -10.6755 | -50.262 | 2026-09-18 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 56710758-5827-3e9a-8938-2459b874d56d | -12.1448 | -44.243 | 2026-09-18 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1ddb315d-69ae-3477-8329-f1aa9ba5b66c | -11.4541 | -51.4754 | 2026-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 859e07dc-8574-3184-b4da-311515c57531 | -10.6189 | -50.2466 | 2026-09-18 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bcb54284-4ee7-306c-a80f-5fb415c3fe5b | -11.6423 | -51.5819 | 2026-09-18 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3bb508ea-76c6-38d1-8b4f-14da2ccd7102 | -11.8307 | -46.8131 | 2026-09-18 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| bdefebf1-9232-365f-a7d2-dcd7242ca463 | -7.841 | -44.8614 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 24c8b75b-9f1e-3f0b-8089-5c80d49fe4ce | -8.6646 | -45.3013 | 2026-09-18 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1ba57d94-a165-3d18-a228-b9e0081b3058 | -12.0902 | -50.8521 | 2026-09-18 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 371649ce-1bdd-3e76-9720-e3ed48d77f21 | -11.8937 | -47.6099 | 2026-09-18 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| aa0dd7b9-a20c-359b-8900-e45ee34a2c29 | -3.7516 | -54.6494 | 2026-09-18 14:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| f4cf36ce-925b-3cdf-ab48-e7ba72d0dfe2 | -9.9956 | -50.2675 | 2026-09-18 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 19a54f4a-ca52-3d50-9416-e0b2a431b3d5 | -12.5153 | -47.0766 | 2026-09-18 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f3b5fabd-c2c5-3378-9e51-b768c4e0f4e4 | -13.4694 | -51.8563 | 2026-09-18 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7092f783-6712-3f95-9df0-8b42aeb1a2ea | -11.2975 | -43.3851 | 2026-09-18 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 264.8 |
| 4fd083ad-7d7a-30e7-9e63-c9fbd773bdca | -7.3564 | -44.4726 | 2026-09-18 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |


[Clique aqui para ver as próximas entradas](README102.md)
