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
| 3f140a9e-026c-39c9-9f61-76f48b24d496 | -1.2723 | -55.7494 | 2026-10-10 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0d0e1b3c-964a-34c0-9ac6-75a4e5cf055c | -3.2577 | -54.0217 | 2026-10-10 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| bb1a4834-5e0f-381f-b0ee-c1b3792d4da7 | -9.2976 | -47.3871 | 2026-10-10 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fe30cdca-71ec-3f52-998d-584d14b7a834 | -6.9319 | -59.2412 | 2026-10-10 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8e52c9e0-adaa-38c0-8cca-dada6d8c9b76 | -6.4567 | -55.4809 | 2026-10-10 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7dac493f-778e-3453-9527-d2bc55313b4a | -13.3666 | -43.8979 | 2026-10-10 00:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| f06ce2f6-e785-31af-8371-bc900c996ee3 | -6.441 | -55.0624 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e2ce95f0-3c13-38e8-9cac-bc812e76dfaf | -12.3066 | -63.3701 | 2026-10-10 00:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 180.6 |
| e1c3fcc5-4582-3965-9578-1639a76cf12c | -4.4507 | -47.9112 | 2026-10-10 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 84941c2a-5ef2-3ddc-9330-fcf06c6492af | -7.535 | -45.3006 | 2026-10-10 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| b83e9d1c-1d3d-3d29-9de3-060faea3d13e | -3.5808 | -51.4832 | 2026-10-10 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c6bf6c11-5111-376c-b847-d2fcb7d1aee1 | -7.923 | -63.7123 | 2026-10-10 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d8cdcbc0-a980-3508-b10d-5977c1c93068 | -7.9084 | -54.7396 | 2026-10-10 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 19a4e058-a081-366f-ba8e-c0145157c75b | -13.3865 | -43.8708 | 2026-10-10 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 882182e5-9ab4-3159-926a-3bac6047f0e9 | -3.6907 | -47.815 | 2026-10-10 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ce45e276-5320-38d8-9356-58b6650cccaf | -3.6048 | -54.5936 | 2026-10-10 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3dc2aae8-441a-3d18-b1b7-436ff948df4d | -12.859 | -44.1504 | 2026-10-10 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b7d62120-f709-3671-8e78-01d734d78061 | -4.5929 | -55.7168 | 2026-10-10 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 44a97773-be49-3d8d-a720-97514c90b938 | -12.2877 | -63.3711 | 2026-10-10 00:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 798a509b-8f02-3aaa-ada1-cf155bbfc699 | -8.9964 | -45.9002 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 47f5c8c9-32dd-33c3-92b5-22f1e88faa28 | -22.0694 | -49.0021 | 2026-10-10 00:30:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 7c3cf970-b95d-3100-97ba-53d2a162fba4 | -12.8585 | -44.174 | 2026-10-10 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 67d84751-7ef3-3616-bffc-2372641a9dd3 | -14.4726 | -43.956 | 2026-10-10 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 222.2 |
| bb7b4a59-587b-3c6b-b64b-de7b718b4bb0 | -7.535 | -45.3006 | 2026-10-10 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 6a182447-145a-3e22-9df2-b8d64bc538c4 | -6.441 | -55.0624 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 276de1ab-8e22-39fd-8e12-26674d43e552 | -3.9911 | -59.3752 | 2026-10-10 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 59b7c0fd-df94-344a-883f-7c5985e9ac9c | -3.8749 | -55.9961 | 2026-10-10 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d14af182-3376-3d84-ae5b-db11ee94fcd5 | -9.0159 | -45.853 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 0983f488-0be9-32ac-a47e-d54644f147f7 | -8.9583 | -45.9269 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ee52700c-9ad3-3974-90d3-0ef13664bcb5 | -6.4567 | -55.4809 | 2026-10-10 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| fb12efa6-4200-3830-875d-1ecdc5ef4950 | -3.0375 | -53.8865 | 2026-10-10 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3fba6716-0fdf-336a-8f1b-f137d2489cd7 | -7.9086 | -54.7194 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e51c248d-df71-3566-93f0-61d96a2208aa | -3.8574 | -55.7794 | 2026-10-10 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c90d554f-e361-371d-bc40-57ab0d3e4e14 | -3.1101 | -54.1661 | 2026-10-10 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2ff4055a-72cd-3d93-ac89-f6a6604ec9b6 | -7.4975 | -55.0055 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| de98946e-60ca-38c5-bebb-9d6ecea267fd | -4.4344 | -47.5421 | 2026-10-10 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f6664cda-7235-32fe-9ede-58b28cb11963 | -13.386 | -43.8945 | 2026-10-10 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 6c2683c5-6305-3708-bc19-843ee0116815 | -8.997 | -45.855 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b9269d8d-dbec-3904-ab00-745e7c1e5d5f | -5.7565 | -45.1293 | 2026-10-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c5bd55b3-7dec-3ffe-866b-b869bcb2d8e7 | -3.7494 | -60.6014 | 2026-10-10 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 232.9 |
| b39ce8c5-8df2-3a99-843b-927368184acb | -3.9912 | -59.356 | 2026-10-10 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ab58f78e-e56b-30ae-a3cc-f97fe3cc2d6c | -3.9729 | -59.3564 | 2026-10-10 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1f316d2e-6434-3019-9819-cbe4873767ad | -7.0228 | -47.661 | 2026-10-10 00:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 16582723-0977-3494-9c77-95e3c3dcb5af | -6.8808 | -45.041 | 2026-10-10 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e18cc299-939f-3bdb-b0c2-3e1d8d1d3cfb | -6.4566 | -55.5008 | 2026-10-10 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 13cee550-8f09-3d6c-ac23-c0a49a5db2c1 | -7.5159 | -45.3251 | 2026-10-10 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 665b809e-8a0c-373d-b0e9-f09a69c1b1bb | -6.9318 | -59.2605 | 2026-10-10 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e11d5cdb-e9ea-3d1f-91a0-0babdb3bd632 | -3.2203 | -49.4417 | 2026-10-10 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4da1e4a7-6b45-3f45-98d9-f421a83bcb42 | -8.9584 | -47.3778 | 2026-10-10 00:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 154ea768-5afc-355c-8857-d6b72f656696 | -5.0876 | -60.2263 | 2026-10-10 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2ec7bdc0-0536-3670-b1d9-1eea8c232e2f | -7.927 | -54.7384 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1b98ef17-de04-3c07-9c24-1407dcade8af | -12.2152 | -57.1488 | 2026-10-10 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a543709a-e63a-3b8c-94aa-0597b4a1bbb5 | -7.2011 | -52.6272 | 2026-10-10 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| abc8270e-6864-3987-b3d5-6754eea24a33 | -3.2571 | -54.1824 | 2026-10-10 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 93014616-5356-308d-9b06-9fa0271bb3d2 | -3.7495 | -60.5824 | 2026-10-10 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 715923f3-0bfa-3243-b6d9-5a11833ae10a | -12.3064 | -63.3893 | 2026-10-10 00:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a2808e2c-15ad-3664-b0aa-20ad9efd1f9c | -8.9967 | -45.8776 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 364.0 |
| eb57755c-032c-3af4-a420-48a1ee26888f | -3.2736 | -54.7025 | 2026-10-10 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 203f97a2-70ae-34d2-9c00-81d86236cf9d | -7.9272 | -54.7182 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d7bdd38f-ed5a-3566-8483-2c17b632d789 | -14.4731 | -43.9322 | 2026-10-10 00:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 3bd61eca-91b0-351e-81ad-34ac8273ba29 | -7.2009 | -52.6477 | 2026-10-10 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| acc731fd-4b3f-32fc-803c-c5b9dce59b35 | -4.3582 | -54.77 | 2026-10-10 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d548f1f0-cc11-3265-aa18-f182c7ff5d5c | -3.7494 | -60.6204 | 2026-10-10 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c3b5a603-d2d7-3af0-a1a9-3fc842ae5969 | -7.5162 | -54.9844 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 84806014-cade-3ab4-8c51-9817003d7b68 | -9.809 | -64.4526 | 2026-10-10 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 68676cd5-5567-36c2-98ae-1ec1ddcb874b | -9.8091 | -64.4338 | 2026-10-10 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6f5c78f7-034f-35e7-9e88-9cbb77bcd3f0 | -12.2156 | -57.1087 | 2026-10-10 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6c96f6c4-8427-31d7-905f-bf459d4dd546 | -3.1285 | -54.1657 | 2026-10-10 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a0c147e2-1c3a-3960-9551-bd657059df97 | -6.633 | -59.9457 | 2026-10-10 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| e9558905-e64c-3b1e-aad6-b412734ca582 | -8.537 | -66.9764 | 2026-10-10 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 705d7324-df4f-35ee-9685-b028a09021b6 | -6.4411 | -55.0424 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 9e11d9f1-4845-3c07-8208-65085809bdad | -4.4507 | -47.9112 | 2026-10-10 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9694fdf6-cb8d-3ad4-8a6c-9f635532222d | -10.6013 | -60.4669 | 2026-10-10 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0bae1f68-1480-32f9-ae04-d7d265bdb500 | -11.0933 | -44.1209 | 2026-10-10 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 957b3f60-b89e-3344-87eb-9cfb96f0bf88 | -22.0701 | -48.9788 | 2026-10-10 00:30:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d5e71b7c-ae34-3040-80b4-a00f1887e25f | -13.3666 | -43.8979 | 2026-10-10 00:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 660393e3-72c4-324b-bc18-8fd901e1ce68 | -3.2204 | -49.4205 | 2026-10-10 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d80bbf78-b930-3c24-af9c-1e6e6203c885 | -3.1114 | -53.7839 | 2026-10-10 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ee0681c5-78bf-3845-bbbd-5e284cbab034 | -4.5929 | -55.7366 | 2026-10-10 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 606a66e4-19a0-36b4-bb0f-1b1b0a821837 | -3.5307 | -54.7356 | 2026-10-10 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e5636d00-902b-304c-9740-b281237667c0 | -7.0225 | -47.6829 | 2026-10-10 00:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ec018249-2009-3548-b6a4-ba60c2461831 | -6.4595 | -55.0615 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c8089ae6-2eb6-309c-b6fa-90867e500f98 | -3.2577 | -54.0217 | 2026-10-10 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0ac97eb8-ee3d-32a3-aad2-22f7fb21a2e6 | -3.2737 | -54.6826 | 2026-10-10 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f5480b7d-045e-3bd9-812f-031d1517c23f | -12.2343 | -57.1271 | 2026-10-10 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c0825e3e-6bd4-3a34-b688-bb7557084c10 | -1.2723 | -55.7494 | 2026-10-10 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1ffad4c9-c476-3e46-ba5b-88dafd3efa4e | -12.3066 | -63.3701 | 2026-10-10 00:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 784974f4-211e-3925-8df7-b4e4e14cc054 | -8.958 | -45.9495 | 2026-10-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 20dda308-2339-3966-83a6-be44297c8b20 | -3.2553 | -54.683 | 2026-10-10 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 925b6b62-813c-3048-bfce-a26f45c36c0f | -3.8391 | -55.7799 | 2026-10-10 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| e984139a-194c-3f06-81aa-57ec152cee9f | -7.9084 | -54.7396 | 2026-10-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7e317565-0c73-3aaf-831c-45e2c4cdc453 | -10.6012 | -60.4863 | 2026-10-10 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2810387f-5eab-38bf-ad8c-63b408568bed | -1.6225 | -54.4348 | 2026-10-10 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c1f0e003-e3ea-3280-924d-06b2d58bf58d | -11.0741 | -44.1237 | 2026-10-10 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 36db5028-7168-3b73-8c12-e7ac7e593cb6 | -13.3865 | -43.8708 | 2026-10-10 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 747a9aba-10eb-3a5b-a56a-ab6811717e26 | -5.7059 | -49.05 | 2026-10-10 00:30:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 4b67eb03-92f1-3016-80a1-bab43d699ab4 | -6.6145 | -59.9464 | 2026-10-10 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 66d7c97e-aa58-3eaf-b927-45f2f320843a | -7.923 | -63.7123 | 2026-10-10 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 24fec9be-da70-3348-bceb-cd643dec7f85 | -4.4506 | -47.9329 | 2026-10-10 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 40bad63e-2894-3430-8bca-b304cc2ac47a | -8.6883 | -62.4002 | 2026-10-10 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |


[Clique aqui para ver as próximas entradas](README12.md)
