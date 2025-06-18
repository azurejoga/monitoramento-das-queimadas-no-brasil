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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ba75a39-81ef-3b50-a8dc-52e84a8a6a15 | -6.96762 | -44.14178 | 2025-06-18 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 683a5afa-42f3-3b9c-a6de-1809c330b856 | -7.23794 | -43.10548 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5056ac21-7699-378f-8189-49dd301b44a8 | -4.86824 | -37.586 | 2025-06-18 03:47:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 821b6a25-0a11-3f31-be28-5556b49c9294 | -5.90267 | -43.45375 | 2025-06-18 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 689afceb-aaaa-3eb0-a472-12c3155cee13 | -4.55787 | -38.46095 | 2025-06-18 03:47:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1b7cee7b-3779-334c-97be-0c354b39d490 | -4.55822 | -48.00603 | 2025-06-18 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29f63397-45ca-3890-b1a8-2045629a4cee | -6.12028 | -42.51392 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0bb2f35-2d75-3cad-88a3-fa5c054e7bd2 | -6.12962 | -42.53566 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9a8bbc48-bac8-3822-b9a1-f98df6ea31b3 | -4.55203 | -48.01239 | 2025-06-18 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22ce3ec5-749a-3d20-92b7-f10782588a5a | -3.77827 | -41.6687 | 2025-06-18 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe3a0c75-4006-3a05-92c8-4be24d6cba44 | -6.04037 | -44.04924 | 2025-06-18 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a3c85fbd-95f1-3d2a-8251-b6fed48611bc | -6.31911 | -43.74586 | 2025-06-18 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b5ca6af-82ef-36b7-a5bf-b0b7dfe440db | -6.67269 | -43.18518 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d6b44ede-6864-3eed-b37c-b4715d625644 | -6.11656 | -45.94047 | 2025-06-18 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d215ab48-dbe4-3f9e-9b3d-4fcdc3a2bccf | -4.81669 | -46.82635 | 2025-06-18 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc74853a-2508-37ee-9fc1-c0836757f83d | -4.94947 | -37.63115 | 2025-06-18 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11cb6195-6c16-3bdd-a4d8-462ea932bd48 | -6.03487 | -44.05332 | 2025-06-18 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a6b613a-0ab7-3289-aa6a-4a775d8a6d05 | -7.23862 | -43.10143 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d7ff447e-82c0-3262-b152-e1a7f0edcfd2 | -7.14779 | -43.29552 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05247833-f56b-3e72-b133-c8df6919817d | -6.37377 | -43.75467 | 2025-06-18 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fa65c8d4-d400-3235-b856-6246ac523946 | -6.23891 | -43.36779 | 2025-06-18 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8316d3a1-46bf-35f1-9a91-3757d0565dae | -7.23365 | -43.10474 | 2025-06-18 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2cb83038-2da2-30bd-a4df-aa398bf5d535 | -6.12606 | -42.5311 | 2025-06-18 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fd3399bd-0dde-3712-bfbc-f489148a05b8 | -6.67637 | -43.21666 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5cdcbb18-55ef-349a-9b8d-5cda73a07634 | -5.06224 | -43.25006 | 2025-06-18 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d02fad25-a386-3b83-bc0b-0583abff1224 | -6.23951 | -43.36966 | 2025-06-18 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78c9d21a-a20b-35b0-9805-c06ebd7f2f19 | -6.4188 | -44.80123 | 2025-06-18 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b57fdd2-2ac2-3ec6-bd9c-9dca82f9a2eb | -6.68747 | -43.68664 | 2025-06-18 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 64247ed2-6346-3782-9f48-149d0afbaa31 | -5.90873 | -43.44539 | 2025-06-18 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 375979cd-1a39-3829-b1a4-03d02d998271 | -4.81095 | -46.82539 | 2025-06-18 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4a16b1a-4c07-3ad6-9d9f-1ce7095f202e | -5.91069 | -43.44741 | 2025-06-18 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 28765375-9e29-3339-ae4f-86c7ebb61eb3 | -6.65891 | -43.18726 | 2025-06-18 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7ba9f2c9-0d50-32ed-abb7-0202a64dd1a8 | -6.41636 | -44.80256 | 2025-06-18 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b26be5d-a03c-39cb-9ebd-d7ed08aff5d9 | -6.36216 | -43.6576 | 2025-06-18 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b207d28-aa78-3bcf-ac6a-6b704e38928e | -8.32943 | -46.23298 | 2025-06-18 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43029638-adaa-304c-b33c-f8301e183a03 | -7.80883 | -46.57395 | 2025-06-18 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3115ac24-4679-3c42-8bd4-27ae1b58dd7d | -9.27041 | -50.04515 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f1aed70-9911-39fb-a7a6-cbabba0c22c1 | -9.84331 | -44.7051 | 2025-06-18 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a534ee88-8bff-3ad7-bc25-f25561dc807e | -11.90914 | -44.18263 | 2025-06-18 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c305a04-d49e-33d2-bffa-577171bac7ad | -9.86063 | -47.88988 | 2025-06-18 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55256cf0-9484-3b86-bffc-6e1235880557 | -12.23575 | -44.20776 | 2025-06-18 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f2a7517-9c17-3a88-ac0c-1c65e24aca6c | -11.58179 | -44.84288 | 2025-06-18 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e53c7be-2152-315d-b9a5-5e9b8794ce1f | -9.1498 | -48.97436 | 2025-06-18 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e43e64ac-a93a-366f-b614-22039c68ba1b | -7.2536 | -44.6414 | 2025-06-18 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bc82699f-3b56-336c-bc85-d85fd783af9d | -10.66032 | -49.36302 | 2025-06-18 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ca240809-719c-3797-9501-2d379bab63d4 | -9.15001 | -48.97392 | 2025-06-18 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a78bb5d-0d04-392c-a2f7-24c7baab41a0 | -7.48659 | -49.58155 | 2025-06-18 03:49:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0b54ec2-dfd5-3b57-b05a-6542b079f078 | -9.27151 | -50.03957 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fca1f8c-405b-3032-a941-6a08b6294fa6 | -8.72095 | -49.03029 | 2025-06-18 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 688889f7-7942-39b0-9be6-b13030381584 | -9.82127 | -47.15633 | 2025-06-18 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8192bd9-6962-3c45-8c99-42c96c472fda | -12.13965 | -47.42239 | 2025-06-18 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ad5cbec-d5c2-3885-99e5-6764c2a27ff1 | -14.19871 | -45.51442 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 585374b3-421e-3d41-9152-dfa3dc1549cb | -9.14363 | -48.97345 | 2025-06-18 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53fef217-7f1d-3b76-aca6-6d73d9d8bf98 | -11.66696 | -44.62274 | 2025-06-18 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00fc02dd-0d2f-391c-b9bf-4f0ae526e2ee | -11.9106 | -44.17447 | 2025-06-18 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c35a539-c7eb-3ace-80a0-cde2c0ba13dc | -12.2098 | -49.6515 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5c35f17-70b0-367d-b443-52fca81a9fb4 | -9.15475 | -49.63884 | 2025-06-18 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d188b7dc-b7e1-3472-8456-af736e2724d2 | -7.80944 | -46.57053 | 2025-06-18 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eab2a4fa-7435-3751-978a-3f79ae052230 | -7.3057 | -44.39861 | 2025-06-18 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6bf8625-22cd-3d7f-a9c6-6d6975518fdd | -8.60036 | -48.05565 | 2025-06-18 03:49:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43c6c361-2861-3e4b-b0ba-ae4ccc3e9c23 | -12.20886 | -49.65617 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f5085b6-36d4-3ec2-83c1-8a34782cb154 | -11.66695 | -44.62102 | 2025-06-18 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cfe65ab-61e8-3092-ad98-5fd97c3fb27a | -14.19956 | -45.50982 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d236060-eb5d-31ff-b211-ef57c767e8a3 | -10.66033 | -49.36324 | 2025-06-18 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d316293a-f8e5-3816-ada9-1383e766ffcf | -9.26501 | -50.03833 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84733b0d-5042-34c7-aa3f-2f2a8d82e41e | -2.87337 | -40.02153 | 2025-06-18 03:49:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8eb62b94-b54d-3941-89a9-2a3abda90c39 | -11.79499 | -43.79362 | 2025-06-18 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a97d07d6-bbec-3735-9eb0-7943b498c1e4 | -11.34021 | -45.21285 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5201a6da-feb6-3711-bb25-1ee1fcf60c0f | -8.72712 | -49.03149 | 2025-06-18 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ce54ad6e-0e60-3a30-aa60-0813f3ad573e | -11.55428 | -47.61332 | 2025-06-18 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ddd93cc-acd7-3394-bc80-4cc827c26b18 | -9.41614 | -48.43747 | 2025-06-18 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50745d07-5529-3725-80d2-c657eb8fd7ed | -9.84415 | -44.70039 | 2025-06-18 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0109fbea-cddb-33fa-88ae-45aa70489055 | -11.55499 | -47.60969 | 2025-06-18 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a4151aa-80f1-39b1-8141-a59987e761b7 | -10.65936 | -49.36804 | 2025-06-18 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 429a9996-c8a9-3ce7-be1e-6ff9f6a16853 | -9.26531 | -50.03964 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20e25917-8644-3e53-8487-092849cd4cb9 | -7.53968 | -45.65379 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ebabc753-f35c-31f8-8e95-9902bb772c0b | -7.2804 | -50.0042 | 2025-06-18 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd76415b-5768-3a03-8715-d12dd31ec2a8 | -3.46045 | -40.71864 | 2025-06-18 03:49:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28c0de1b-23fa-3cfa-bf28-fb61bce96b4e | -9.14385 | -48.97302 | 2025-06-18 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 134279d0-43f2-318b-a448-1608a8c0df05 | -9.25774 | -50.04396 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ab98b99-cd70-3cb5-a290-90e3669761ad | -10.65327 | -49.36667 | 2025-06-18 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecc22f06-e884-3cc9-a559-ddfc3eb5976e | -7.54529 | -45.65163 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f3a0d3c-9451-3526-be74-6ce1d67c510f | -7.54422 | -45.65769 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 98961274-c3a3-30e0-b777-1e0fda5503de | -14.19423 | -45.51357 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48ee1e92-2527-3fe3-8572-82f2eba527cf | -10.65939 | -49.36782 | 2025-06-18 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| f9ac87ca-f66d-3f87-ae5c-f70abbcb2f24 | -7.60765 | -45.55863 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c2826b3-21ee-30fc-b955-22e2858a549d | -12.23647 | -44.20369 | 2025-06-18 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79b1c24c-cfcb-35d7-97ee-294533709a5d | -10.98589 | -45.10591 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21052190-4a88-35e1-9841-0cf91043a6c7 | -7.54743 | -45.63943 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a49aaccc-b79e-360f-8831-4c2eac94ae58 | -11.55744 | -47.61381 | 2025-06-18 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd7fcb8-db97-36bc-9286-99b31a511de9 | -9.20201 | -49.67758 | 2025-06-18 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d50b9f1f-413f-3a8c-8898-d0448748ba37 | -13.37515 | -40.05607 | 2025-06-18 03:49:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cdfbc8d3-e5c5-385a-a429-5a3ab46d78e3 | -7.28151 | -49.9983 | 2025-06-18 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a70bce1b-d4b7-396f-8cfc-2b2551d8881c | -9.88704 | -47.81049 | 2025-06-18 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c943f67b-6542-3279-9b21-5e0a685a97bf | -9.2574 | -50.04266 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3a15c19-02c5-33ed-9485-e1a3f1c1f584 | -9.88472 | -47.8097 | 2025-06-18 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a25a0b6-86d6-3e93-90df-1fa4d0de0ffd | -7.54582 | -45.6486 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 481b438f-339e-3efa-8187-5fe103ebfd07 | -14.00387 | -46.18591 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4d25dc2-c957-36da-b816-eedd07d656b5 | -8.59956 | -48.05992 | 2025-06-18 03:49:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e42a4e0c-9b42-3c31-91bf-df466fbd8df9 | -7.08118 | -44.38616 | 2025-06-18 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README8.md)
