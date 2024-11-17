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
| ef9f4704-3e0a-3898-8bfd-0dc6bcc6a2b0 | -8.4525 | -44.1999 | 2024-11-17 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 204.1 |
| e75c5628-102e-3b14-b36f-cb0bdaab3509 | -2.8614 | -46.7306 | 2024-11-17 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5f06598d-b799-3554-9b9f-d3c8c3afdfda | -6.1604 | -35.1544 | 2024-11-17 02:00:00 | GOES-16 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| d202b366-978b-3cfc-b445-41cc34e66888 | -3.5494 | -50.254 | 2024-11-17 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| a95c651c-d069-3196-a33b-a4468f4fec4c | -6.1601 | -35.1817 | 2024-11-17 02:00:00 | GOES-16 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| add525cd-1787-314e-9b12-d15dd7d04fcd | -1.8982 | -46.5588 | 2024-11-17 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f7efce36-47bd-39e7-b164-9bfef9fc6690 | -2.5987 | -47.5705 | 2024-11-17 02:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e9108448-36b8-3449-ab3b-3b4eac3de63c | -2.6595 | -46.2065 | 2024-11-17 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 326dbcb5-f27d-340f-8275-901baed70168 | -8.4528 | -44.1767 | 2024-11-17 02:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e948c9bc-97e4-38c6-b556-eb9b9a204251 | -1.5073 | -47.3996 | 2024-11-17 02:00:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| d0b7f84e-4206-3f30-bb82-15aa54174c15 | -2.678 | -46.2281 | 2024-11-17 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9babb95d-7f05-3a3f-9bb2-18c66174809b | -4.5616 | -47.9925 | 2024-11-17 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7cc596a1-201e-3502-93e2-1eb8c7266117 | -8.4336 | -44.2019 | 2024-11-17 02:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 1ea94b56-a4e3-3bbb-a74b-dc2751382e6f | -1.9167 | -46.5584 | 2024-11-17 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| a46cb623-8bf2-35a9-a8fa-2a2c8ddf5a0d | -1.4888 | -47.3999 | 2024-11-17 02:00:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 299.9 |
| 79e3e3a9-2041-36eb-8da0-367cd36785ea | -1.9166 | -46.5804 | 2024-11-17 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 53f4dc6c-4263-3f2d-95b1-8cff30396af8 | 0.6159 | -51.7881 | 2024-11-17 02:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5afebd7b-1595-3918-b382-ec58d8588d97 | -2.5988 | -47.5488 | 2024-11-17 02:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 525cef06-f654-3124-8e64-cb15c5c6439f | -1.8981 | -46.5808 | 2024-11-17 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6d12dcd5-0eca-3538-80af-70726f4e4fa8 | -3.3359 | -52.7643 | 2024-11-17 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 08f01d1a-36bc-3f5b-bfba-adb932fcc26b | -3.5309 | -50.2547 | 2024-11-17 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 289.1 |
| ed7ed468-7cd1-3621-8a10-497ba9b0ea06 | -2.5802 | -47.571 | 2024-11-17 02:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b270e491-64a3-37b6-9b4a-7f31c82c13f7 | -3.531 | -50.2337 | 2024-11-17 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 6536e1e7-25e5-3436-bd4d-245ab45f1006 | -1.4888 | -47.3781 | 2024-11-17 02:00:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 8e33224c-c2c7-3f05-a5b9-4d23bff9fe79 | -4.4101 | -45.5293 | 2024-11-17 02:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3677a559-23f1-3508-9213-9746c43b8aa2 | -3.793 | -46.052 | 2024-11-17 02:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 96d30b73-321b-3d74-98db-0cdfd91027a4 | -2.6322 | -48.5634 | 2024-11-17 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9a6b7c05-b225-31cb-b834-71a6d632aa8f | -8.4525 | -44.1999 | 2024-11-17 02:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 204.8 |
| bd1979a1-b5d3-3e54-8227-e847ebf207e4 | 0.6159 | -51.7676 | 2024-11-17 02:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 32fabc75-a675-31fa-a7b2-6bcdc4848133 | -1.5074 | -47.3778 | 2024-11-17 02:00:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 23ced442-d794-3061-8e6a-281d461c9094 | -3.5124 | -50.2553 | 2024-11-17 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| ad3baf0a-0669-35a0-9dd2-5576f58dfcbb | -2.678 | -46.2059 | 2024-11-17 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 7c6da741-1c6f-34cf-b292-57710afcc8c4 | -1.4888 | -47.4217 | 2024-11-17 02:00:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| cf23e18d-4e9a-32f7-b1c5-dcbb283ad95b | -4.5614 | -48.0141 | 2024-11-17 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 525b613d-dfc9-3fe5-9654-748cc52430fa | -1.47 | -47.37 | 2024-11-17 02:00:00 | MSG-03 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 586134b6-d2d8-346f-8796-b847fe59186f | -8.45 | -44.22 | 2024-11-17 02:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f089f971-5ba6-3192-b039-157b7932a065 | -1.47 | -47.42 | 2024-11-17 02:00:00 | MSG-03 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2d68ba9-fbc5-32cb-81e0-635ee3fd5b1e | -1.5 | -47.37 | 2024-11-17 02:00:00 | MSG-03 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff4d343-83c9-3d45-af00-a799e4005abc | -1.5 | -47.42 | 2024-11-17 02:00:00 | MSG-03 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54172a69-5510-3eba-9b92-cbe2bf05ec57 | -3.52 | -50.24 | 2024-11-17 02:00:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5de32f-2a6b-335c-8fbb-c31558ab9cfc | -15.8662 | -59.826599 | 2024-11-17 02:07:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17891e16-a0b3-3ab4-9238-f290e69fed11 | -2.5988 | -47.5488 | 2024-11-17 02:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 699ed8dd-db42-3234-8787-d40bc0412a6a | -8.4525 | -44.1999 | 2024-11-17 02:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 62dcbe52-4082-3da5-a766-496f2506b65e | -3.5494 | -50.254 | 2024-11-17 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 5f4f0498-8bc8-38cd-a3a2-1f746473cdb4 | -2.8614 | -46.7306 | 2024-11-17 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 11e592a6-8bf6-3e7d-b741-2f5688c789bc | -1.5073 | -47.3996 | 2024-11-17 02:10:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 237.1 |
| 5cb5e9db-6c19-3f01-9228-8c927b768bbb | -1.4888 | -47.3999 | 2024-11-17 02:10:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 431.4 |
| 107543ae-3533-348a-a761-26af10f4684f | -3.3359 | -52.7847 | 2024-11-17 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 033ea765-9fa9-3289-b4fd-a8aed7519de8 | -3.5309 | -50.2547 | 2024-11-17 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 329.6 |
| d6a89933-e3fe-3c31-8b1c-d478d1233af2 | -1.4888 | -47.4217 | 2024-11-17 02:10:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0f3c6ebb-7fe6-3921-860f-8812534ba73e | -1.4888 | -47.3781 | 2024-11-17 02:10:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 223.1 |
| 731ae3ab-6117-34f0-b960-0a245279a01a | 0.6159 | -51.7676 | 2024-11-17 02:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 96.9 |
| d4156777-ab94-3047-b4ac-c83939b4d3a7 | -3.531 | -50.2337 | 2024-11-17 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 5c230477-39b6-3a39-8e7d-b0ec6714bf0b | -3.5308 | -50.2757 | 2024-11-17 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 42c5f10d-5e5d-3e17-ad5a-431354121772 | -1.5074 | -47.3778 | 2024-11-17 02:10:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| a6f21f66-77c0-3659-8cb6-bfeb54d9536e | -4.5616 | -47.9925 | 2024-11-17 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7c942c8e-38ef-337a-b4b3-037b9480bfc4 | -1.9167 | -46.5584 | 2024-11-17 02:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7f686975-5a26-3f5f-8738-1850636bca02 | -2.678 | -46.2059 | 2024-11-17 02:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 2ce7b8f0-b8e5-37f8-af1d-37496e33ffff | -2.5987 | -47.5705 | 2024-11-17 02:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cf57d988-764f-319a-bd50-2e94ff2cf12d | -2.6595 | -46.2065 | 2024-11-17 02:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ccd06d2b-385d-397f-82a9-7804bf1e8d6d | -2.5802 | -47.571 | 2024-11-17 02:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| eb6d7e81-d29a-353d-8af0-04eb52814128 | -1.9166 | -46.5804 | 2024-11-17 02:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 2022c99d-3e83-378e-89fe-cdde428ad670 | -3.5125 | -50.2343 | 2024-11-17 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9defea90-098b-3d6c-8278-b23a71253527 | -8.4336 | -44.2019 | 2024-11-17 02:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 7a8360b7-34e5-301f-8e7c-b614a4042738 | -3.3359 | -52.7643 | 2024-11-17 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c8a0fcff-4dba-3ba2-a405-c57649cdf441 | -3.5124 | -50.2553 | 2024-11-17 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 171.1 |
| 86761b36-7ae7-3300-a6f1-f0df77f84d19 | -4.5614 | -48.0141 | 2024-11-17 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fddfa5e8-3f43-34f8-aeee-82c21db33eae | -1.9167 | -46.5584 | 2024-11-17 02:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| ad843e84-0407-3873-9fc8-89d7e83eed87 | -4.5614 | -48.0141 | 2024-11-17 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 23036372-ae6b-35fa-be0e-b5ea7ee73531 | -2.2111 | -47.2321 | 2024-11-17 02:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 31c5a9af-34cf-3962-8b0a-1431407bf9c8 | -8.4528 | -44.1767 | 2024-11-17 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 6388b2e3-199b-3ab1-96aa-3e08ad45dbe4 | -1.4888 | -47.3781 | 2024-11-17 02:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| e6440462-9354-35cd-b542-3dc9ed5a0e55 | -3.5308 | -50.2757 | 2024-11-17 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b3af3c3b-9412-3be4-a504-3db7cd026e4e | -3.5309 | -50.2547 | 2024-11-17 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 304.1 |
| c6a945f5-e583-30e6-8055-29ba16e85484 | -2.5988 | -47.5488 | 2024-11-17 02:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| be68c61a-7a9b-34bf-ae46-e28f8372c62d | -3.3359 | -52.7847 | 2024-11-17 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f6c63d43-f74c-398b-9500-156c815081e2 | -2.8615 | -46.7086 | 2024-11-17 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ec29c126-e617-3d7f-9da4-b2d5fd01c47f | -1.5073 | -47.3996 | 2024-11-17 02:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 220.2 |
| 03e2915e-d3a7-31da-883d-9da1dabb633e | -8.4339 | -44.1788 | 2024-11-17 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 66a42bea-a9c7-3b53-9304-0eecc71f214e | -2.8614 | -46.7306 | 2024-11-17 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1f5ed1e9-2844-36c8-89d3-d3f330650cb7 | -3.5494 | -50.254 | 2024-11-17 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 06762e68-beab-3fe4-ab09-64e06e317e4f | -2.678 | -46.2059 | 2024-11-17 02:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7b9d2de6-0262-3c77-90d4-9602296a6eb2 | -4.5616 | -47.9925 | 2024-11-17 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 439eec86-fb2f-3c4e-941c-3db3c4ea546c | -2.6595 | -46.2065 | 2024-11-17 02:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 99b95867-2800-3e17-8081-1bf9ed9acaa7 | -3.531 | -50.2337 | 2024-11-17 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 20988e43-c53b-3ff7-9515-9d4e754459b8 | -8.4525 | -44.1999 | 2024-11-17 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 173.2 |
| a717a6db-45a4-3823-9b25-d5fb0de50d35 | -4.4101 | -45.5293 | 2024-11-17 02:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fcde5a31-239b-3ea7-844a-95f63daa30f0 | -2.6322 | -48.5634 | 2024-11-17 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 775ba548-d0bb-34f4-9776-d02c4cefccdc | 0.6159 | -51.7676 | 2024-11-17 02:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 85.8 |
| beb0c77c-a58d-33c1-af1f-ddc6ac4f8b92 | -2.2111 | -47.2102 | 2024-11-17 02:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| c9ea7dbf-4f94-3978-9cc7-3c1a7961e011 | -1.9166 | -46.5804 | 2024-11-17 02:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 595152a7-9242-3c3d-b0d7-5351ba1c57bc | -1.5074 | -47.3778 | 2024-11-17 02:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ddf50739-e71b-3477-aa13-3dee724dda37 | -2.2296 | -47.2098 | 2024-11-17 02:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| dad75dca-b128-321b-9b90-79ada7bfaa84 | -1.4888 | -47.3999 | 2024-11-17 02:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 209.5 |
| 130182e3-1132-35da-8913-b0567f399047 | -2.5802 | -47.571 | 2024-11-17 02:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4ca64a96-721f-3a91-a9d8-dde1ad66a052 | -3.3359 | -52.7643 | 2024-11-17 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 34fe3ab5-c194-3c5a-92e8-1f7b81bdb7fb | -3.5124 | -50.2553 | 2024-11-17 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| f030ec18-d7ad-3629-b81e-6f9a3a2e18ba | -2.5987 | -47.5705 | 2024-11-17 02:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 16c5a4e2-a552-368a-b7bf-6e12a2fac4aa | -8.4336 | -44.2019 | 2024-11-17 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 208.8 |
| ca606f00-ce77-3aa2-a009-d11084245e15 | -1.8982 | -46.5588 | 2024-11-17 02:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |


[Clique aqui para ver as próximas entradas](README19.md)
