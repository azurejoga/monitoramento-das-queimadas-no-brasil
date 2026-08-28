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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c57f588-f921-38a1-b049-959a90bd2f62 | -9.9102 | -60.4287 | 2026-08-28 21:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 0da48ff9-56a2-354d-ab24-955a1f471d11 | -6.7247 | -60.0189 | 2026-08-28 21:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 36849308-4647-3c57-ba04-5e736b4f5eac | -5.6085 | -44.9583 | 2026-08-28 21:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 51572275-3605-3162-994a-633c4c3a52dd | -12.7599 | -44.2844 | 2026-08-28 21:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 67e0ea90-7fd6-3dab-bd1c-d073336e7674 | -7.5478 | -61.3056 | 2026-08-28 21:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 8fab455a-7550-3680-bb1b-ac3fa8f00340 | -5.7233 | -44.6541 | 2026-08-28 21:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 7284fab3-5e33-3496-9019-9e8c74262e8f | -9.929 | -60.4084 | 2026-08-28 21:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| fe34ddd0-07c8-3ed8-a74d-3ce35a68eb51 | -5.3992 | -43.1766 | 2026-08-28 21:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| fc68e85d-6287-3c84-8748-a86cd3578cda | -6.8572 | -59.3986 | 2026-08-28 21:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| c8002cf0-6e9c-35ef-be69-b1724001ff12 | -11.0443 | -57.2222 | 2026-08-28 21:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 301.8 |
| c25796a4-8b25-35f2-a64c-98d853a633b0 | -12.7802 | -44.2341 | 2026-08-28 21:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| c482bcd6-54ac-34b7-865c-2fde20ab9638 | -4.5694 | -44.0657 | 2026-08-28 21:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 194.1 |
| c19bb621-d382-3cbb-ac8c-8cf1705c1832 | -11.0441 | -57.2421 | 2026-08-28 21:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| a0d27af9-dc39-3a4d-b391-e5e017067c4a | -14.4856 | -58.5074 | 2026-08-28 21:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ea28b968-b327-3c07-96db-1eadd6b8f0a5 | -6.7514 | -55.6654 | 2026-08-28 21:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 160.7 |
| d2efda03-ded3-3a43-91f3-421866849cc6 | -6.3279 | -44.0797 | 2026-08-28 21:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| a61bcc5c-ba13-3322-a59e-467631d408f7 | 0.1367 | -60.393 | 2026-08-28 21:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 4126b84e-0187-3f55-ba2a-21d56a68667a | 0.1549 | -60.393 | 2026-08-28 21:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a9679d72-fef4-3ab1-acc7-cacbc6e6729f | -6.0122 | -45.8099 | 2026-08-28 21:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a19efb87-79b8-3c9f-93f3-66507bed06c8 | -9.9288 | -60.4277 | 2026-08-28 21:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 498.3 |
| 33b1090d-cb45-35a4-a8e0-69b4c38641cf | -5.9078 | -57.77 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| aa885155-4e85-3c18-be91-d3ad51797f05 | -4.5507 | -44.0668 | 2026-08-28 21:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 134a85e5-db12-30c6-b290-a326c1e7a731 | -6.7699 | -55.6644 | 2026-08-28 21:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 326.8 |
| ce833c07-1918-37cb-8490-0146d2f79988 | -5.4179 | -43.1752 | 2026-08-28 21:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3ea7d86b-eda0-3227-b367-2a63c03a27d7 | 0.1367 | -60.412 | 2026-08-28 21:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 2dcb3471-df5c-3b45-8854-01353a7d9035 | -12.7797 | -44.2576 | 2026-08-28 21:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| bc819666-174c-3f72-b017-a8af0afac1c2 | -5.871 | -57.7715 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| aca8efce-47d3-347c-b04e-2275c559bdd2 | -6.77 | -55.6445 | 2026-08-28 21:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| c7a297b6-3017-37b3-9b5d-781702431feb | -9.1926 | -56.9742 | 2026-08-28 21:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 3ad07db7-9ce4-355a-85c1-cf224cef6e5a | -4.0574 | -56.2865 | 2026-08-28 21:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 73fcf3e5-23a7-37bb-90fd-e0f2b68b4e87 | -5.3117 | -47.0558 | 2026-08-28 21:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 074d3733-3b43-34a8-975f-d56044a9aae8 | -12.43 | -43.4182 | 2026-08-28 21:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 49bb061a-36c6-33e6-8871-42dbe82174a1 | -5.5491 | -45.3474 | 2026-08-28 21:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f40f503b-d2b7-3c5f-8a27-33b0ddf87fcc | -4.5507 | -44.0668 | 2026-08-28 21:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 26f89bc6-4075-3347-b655-0535898cda6d | -8.0113 | -48.0161 | 2026-08-28 21:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e5c4493a-8c33-388b-9dba-3328a79e4a88 | -9.9475 | -60.4267 | 2026-08-28 21:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 188.0 |
| d26f4e0f-4560-3dff-8ca7-2c301e2051b2 | -6.8572 | -59.3986 | 2026-08-28 21:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e2804a90-b310-311d-bc9d-ba369654f260 | -4.5695 | -44.0427 | 2026-08-28 21:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| b17a060c-e1d3-3605-ae5b-2abd63f7329e | -4.282 | -48.2007 | 2026-08-28 21:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0ba443c3-e6d9-3610-bf20-b2e1492ce01d | -9.9288 | -60.4277 | 2026-08-28 21:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 248.2 |
| ad4a6a3f-54db-3e43-a7ed-510b07a2efc8 | -8.6012 | -70.2192 | 2026-08-28 21:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a9ffa913-6179-3206-8325-9068fa513156 | -17.4354 | -40.1643 | 2026-08-28 21:50:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| cd69281b-3c20-3340-8092-101349d8e76e | -5.6273 | -44.9343 | 2026-08-28 21:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 169.9 |
| d9121a24-294e-39a7-84d6-3bdf1906895e | -6.3467 | -44.0782 | 2026-08-28 21:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 5ffd4959-8198-37f4-911a-7c105c30b4a8 | -7.5478 | -61.3056 | 2026-08-28 21:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 8588f0d3-0955-3ef0-a5bf-8a156d0ea0b1 | -19.0152 | -47.4288 | 2026-08-28 21:50:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 809e6d1c-f65f-35d1-a704-4405d30fe087 | -9.9474 | -60.446 | 2026-08-28 21:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| da4b410f-704b-3353-82c8-b9fc5f2cf4e0 | -2.7119 | -47.043 | 2026-08-28 21:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1c132bc9-4fd9-3ddb-95c8-2d4b7fac5f6e | -5.5493 | -45.3248 | 2026-08-28 21:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 4be96f6a-f6e3-3dcf-aa07-cd395752711b | -5.6086 | -44.9356 | 2026-08-28 21:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ccccc8a0-64ad-3d72-9121-661c4a78f617 | -6.8757 | -59.3978 | 2026-08-28 21:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 228985e5-0221-3de3-a2ed-28f0cc2c68a7 | 0.1367 | -60.393 | 2026-08-28 21:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 55fe9e49-0008-3540-aea3-9b18aab2f322 | -5.4179 | -43.1752 | 2026-08-28 21:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 719ee027-bb48-3fea-8404-cab285662de6 | -5.4177 | -43.1986 | 2026-08-28 21:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 846f3398-c256-345d-b5a0-ebc126c58048 | -5.6272 | -44.957 | 2026-08-28 21:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e1e74f4c-5583-3d94-b9f7-316d010c62bc | -9.8739 | -60.2955 | 2026-08-28 21:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| c7387365-51c6-3733-b8ca-515df7d9382a | -12.7792 | -44.2812 | 2026-08-28 21:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f9e58e4a-c5f0-3f04-96a1-2a3e598d46f4 | -12.7603 | -44.2608 | 2026-08-28 21:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 5c7ce636-cd77-3211-b182-4e8ce3618f74 | -4.5694 | -44.0657 | 2026-08-28 21:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 209.0 |
| d1aa56d0-aba1-3a40-a882-013d1967f78c | -12.4305 | -43.3944 | 2026-08-28 21:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 88c6a88f-7ae4-3322-bfb7-c2c3530f945a | -17.4555 | -40.1588 | 2026-08-28 21:50:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 125.3 |
| 3188dec1-8aef-3318-b270-8319fe92fdd6 | -6.7247 | -60.0189 | 2026-08-28 21:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d793aab5-abd0-371f-a960-2c70346e1e9d | -6.0122 | -45.8099 | 2026-08-28 21:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 984821f7-3828-30ec-8d43-b6f459b70a3e | -5.5678 | -45.3461 | 2026-08-28 21:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| ce236cb5-ea3f-3a45-95d5-b552bfcff9a2 | -5.5962 | -44.2052 | 2026-08-28 21:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7ca5fe9d-14d8-3923-b4ec-7e48b13fcb48 | -5.5964 | -44.1822 | 2026-08-28 21:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 5ee643d3-bc3e-3d21-b5e1-4c7e2c3fc2e7 | -6.3465 | -44.1013 | 2026-08-28 21:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 51ee1543-31ac-36f4-a55b-ccad4dc05346 | -12.4494 | -43.415 | 2026-08-28 21:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 6dae4f61-4f86-3a83-8d60-8730a73386ea | -5.742 | -44.6528 | 2026-08-28 21:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9c93c791-e9e8-3761-8e8f-6d2d73261aa6 | -7.5662 | -61.3049 | 2026-08-28 21:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 1e7e2315-ada2-3b16-a6d7-198def3a3c2e | -9.929 | -60.4084 | 2026-08-28 21:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 9de23c4c-fbb3-34ba-a85a-5b4b58fd031e | 0.1367 | -60.412 | 2026-08-28 21:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 4840b2e9-b8e8-352e-9718-d9a82425f3b1 | -9.9287 | -60.447 | 2026-08-28 21:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| b0717910-51de-3f9d-a65c-ea2165ba7390 | -9.2644 | -45.6444 | 2026-08-28 21:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 95f2afff-804d-351a-ac27-4bace6c19eeb | -12.7797 | -44.2576 | 2026-08-28 21:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| bbf6261b-da16-3d3c-aa27-7da21665a864 | 0.1549 | -60.412 | 2026-08-28 21:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fcdf3e7b-ef50-3ac7-aa21-0d5e9d29aea2 | -15.4952 | -43.7291 | 2026-08-28 21:50:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 89ab73b6-0030-36ab-b4b1-5468006aab82 | 0.1549 | -60.393 | 2026-08-28 21:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6e1ab9da-b3dc-399a-b2b5-e7910001f803 | -2.7304 | -47.0424 | 2026-08-28 21:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2ca06963-739b-3a04-9cfd-3d580549d916 | -5.3453 | -45.1576 | 2026-08-28 21:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 1e1d3b04-5d63-3645-a02f-50b8d20c86cb | -5.5491 | -45.3474 | 2026-08-28 22:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8d71b50e-6d93-3f33-9076-3bf2adc21d19 | -5.568 | -45.3235 | 2026-08-28 22:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cfa4a969-65a1-30c5-a7af-46a4635529f2 | -3.7013 | -39.5792 | 2026-08-28 22:00:00 | GOES-19 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 745ff581-59ba-347f-958a-cb08d6bbb987 | -4.5694 | -44.0657 | 2026-08-28 22:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| e40f6e16-846f-30e7-9033-5ca5d7ce246e | -7.5478 | -61.3056 | 2026-08-28 22:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| aa59808a-e386-30ca-9604-a4b6bdfe5ad1 | -6.3467 | -44.0782 | 2026-08-28 22:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 54eebf70-a578-394b-a533-8aaaa8adf454 | -4.5507 | -44.0668 | 2026-08-28 22:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4182ba99-b0ad-3714-a50a-e74182be22e3 | -2.5042 | -48.1366 | 2026-08-28 22:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 54954435-e898-3e39-9e1b-5cf3d07f157b | -5.5962 | -44.2052 | 2026-08-28 22:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 50389eeb-e787-34bf-b339-441fc22ca6d0 | -5.5678 | -45.3461 | 2026-08-28 22:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 2a8ae0fd-f056-3694-8987-e1f7e73d8cfe | -2.7304 | -47.0424 | 2026-08-28 22:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 17e3441f-a71a-30a9-bdeb-9ca6a8f7c1a2 | -4.282 | -48.2007 | 2026-08-28 22:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8e3c9ced-a4d9-3099-a492-a1ead0e22efa | -12.7797 | -44.2576 | 2026-08-28 22:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 4dc5dee4-b71b-3b6d-8052-5e3e8bc222c7 | -6.3279 | -44.0797 | 2026-08-28 22:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6f1a59a0-883f-3fbc-9e16-9fdd410f5701 | -6.3465 | -44.1013 | 2026-08-28 22:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 7a0cbdd4-9c5e-3445-8c51-cb2342d7b81c | -13.3521 | -43.6633 | 2026-08-28 22:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 80b9062d-b121-3170-9c9a-ba4edce20531 | -12.7603 | -44.2608 | 2026-08-28 22:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 4f935e14-fc79-3f0a-ba4e-2e25920c0c94 | -19.0152 | -47.4288 | 2026-08-28 22:00:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e44eb5ad-dc5f-39d1-9435-5b99f1cb3fb6 | -7.5662 | -61.3049 | 2026-08-28 22:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 136.2 |
| c27895f0-2e65-3528-bd4b-ff43fbd04fcf | -8.4911 | -50.4046 | 2026-08-28 22:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |


[Clique aqui para ver as próximas entradas](README189.md)
