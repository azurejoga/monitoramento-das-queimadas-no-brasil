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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69da98fa-7486-3349-9514-e000b4dc984d | -2.86757 | -50.71611 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42d5647f-ebc9-3014-8df5-feea0d93895a | -2.87426 | -50.71416 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca9bb79e-233d-36ec-bf7c-fedbb04a6798 | -5.32091 | -48.18126 | 2025-10-23 04:36:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bb06b6cd-a917-3d52-bd22-bf1aac2f0366 | -2.87495 | -50.70977 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 920639f9-eb58-3fa8-abac-2eb3062f4d3d | -8.87238 | -47.96992 | 2025-10-23 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c406ec71-b482-35b8-80e3-753696ae4219 | -6.60436 | -44.21522 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb9913ad-feae-311b-ba71-511c34298c25 | -6.7883 | -45.44801 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c76a6824-c171-33d5-a4ce-a83ae6f0e0fa | -2.87797 | -50.71475 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2026210-5875-38cb-aeec-4552e2d8338b | -7.06557 | -44.09668 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c57716c-38f6-39b9-a89b-4d7cae190202 | -4.63663 | -42.52995 | 2025-10-23 04:36:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e76384f-6d4e-3872-8b5a-cc50f6de812d | -2.80623 | -50.27029 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb25c27b-d1c2-311b-ae57-9b410c925889 | -7.63691 | -42.20527 | 2025-10-23 04:36:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ebdf2513-0129-3f29-b843-5db2a6bdd742 | -6.7337 | -44.15207 | 2025-10-23 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3118904d-6b8e-3888-8367-0ea833735b81 | -2.87572 | -50.7129 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e29c82e-3a3e-3f82-804b-c4a48ac86982 | -7.62513 | -42.19538 | 2025-10-23 04:36:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 470ecb13-243a-3b4a-b123-6ca238a1c1cc | -2.89868 | -49.39777 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ced084e-0f2d-34a6-a8d0-e9eaccacc9a5 | -5.47202 | -47.13871 | 2025-10-23 04:36:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f101bf81-623c-36b7-a7a8-ebd005ccb3f6 | -2.86196 | -50.74376 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d2b91db-a3f4-3fa5-99d1-8d65a8ebe957 | -6.53606 | -44.36306 | 2025-10-23 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ffa7425-01be-3b5f-a371-fb835ed85c1d | -4.27653 | -48.19136 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a54908ab-ea97-3b8c-864f-58651beb952b | -3.0261 | -49.48018 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| cabdfd1a-8b8f-38eb-a6f9-14045553f36b | -2.72715 | -49.56624 | 2025-10-23 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c91b0f8-a006-353b-bef2-893a2246ac62 | -3.2176 | -46.8036 | 2025-10-23 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c384e28-002a-3e4f-ae92-05f1de7d3842 | -6.78597 | -45.43959 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d782d8a-a298-3b15-813e-403b8d363f7e | -7.84071 | -45.38892 | 2025-10-23 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f12d4d4-351d-3bde-b927-fe6de15612ac | -3.02671 | -49.47636 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6750cefb-3ca2-326a-a176-5f1a2da4e124 | -7.27759 | -49.99321 | 2025-10-23 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0850ff3f-4015-378e-9575-e42d1f86a930 | -3.16173 | -48.60794 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3cdc0dc-ab0e-396a-80b1-187d75928400 | -5.2565 | -50.80768 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ac5313e-4ad8-3af4-8c3f-a5f132e49858 | -3.8023 | -52.14492 | 2025-10-23 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 834c93f6-f018-36a7-8504-e75a3bae573b | -3.15433 | -50.16958 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd9cd4ba-dcdd-326a-950f-3d6b99a39034 | -8.87571 | -47.97046 | 2025-10-23 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccdcb234-14ef-376c-bbda-976ba045e620 | -3.94869 | -46.97168 | 2025-10-23 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15551a20-85d5-3ff8-9fb2-4e44ebdf7594 | -3.76478 | -48.9212 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e66bb070-939c-3ce0-92e6-1d64ab4441cd | -3.80177 | -48.99391 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96311e23-d67e-391d-8638-1a816b040694 | -2.9298 | -48.04416 | 2025-10-23 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f16767be-7e41-33eb-bad4-6f8221e04278 | -2.89761 | -49.17314 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c147dc99-038d-3c50-a7ab-eb1fe2acda1f | -2.80853 | -50.27923 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3c6429e-9245-3b39-a6b0-cdb440b16ab5 | -6.01372 | -43.3249 | 2025-10-23 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2954d698-7fd2-3fd3-9efe-17756acfb1b3 | -3.22176 | -49.36551 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 601996a2-f294-3972-be33-a3a7c9a5cc4d | -8.35398 | -46.18304 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71097ed9-4cbd-36a7-ac1a-5b8fe408bdaa | -3.48301 | -50.07302 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 192acd2c-12d2-3aca-9543-47bc81dfc36e | -5.91273 | -43.30842 | 2025-10-23 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55fcbb1c-437c-344f-ac84-a2d42dc10f75 | -3.38061 | -50.27384 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca530118-fa90-33ab-8829-f6d6236cf21b | -3.22766 | -49.35093 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de6d219f-fb03-3542-8471-b8d7df9525b0 | -2.90706 | -48.97979 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9725451-d47b-37ad-bc60-5cd812b9301e | -6.80917 | -44.00891 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eed3577-4b57-3c91-ac1d-3e088c708bf6 | -3.41739 | -51.43603 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61ca5a42-cc3d-3f58-9c32-8b3175d45a72 | -9.2336 | -45.60536 | 2025-10-23 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aaaf6727-b6e4-396b-b25e-20bfffd8304b | -6.81296 | -44.0095 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e3f49ed-ac7e-3506-9ec8-635b3eae3509 | -4.63972 | -49.54176 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8947a40b-636d-371a-ae40-3d06b389ea9b | -2.81202 | -49.13272 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d96c3fa-0bcb-35fb-a371-00b1025aaa04 | -6.30437 | -41.8857 | 2025-10-23 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4c0b5821-7268-3975-bf7c-a56d7a60406f | -8.20099 | -46.98932 | 2025-10-23 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 776a32d2-62c2-3352-b785-0f1c19cd6d1b | -6.23688 | -49.36496 | 2025-10-23 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd3f512a-1af5-3e29-9aa3-ff19499aeaca | -7.06916 | -45.21438 | 2025-10-23 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b7372b1-30de-3b6a-9e55-ec781b6d5aa3 | -5.63638 | -50.03066 | 2025-10-23 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fb76aeb-e9a1-3ee7-830a-339298f0f8fe | -6.80917 | -44.00892 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65177c3a-3b97-3414-9904-22f07f6759b4 | -2.81313 | -54.38064 | 2025-10-23 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8a35438-21ba-3bb3-95f6-719f00787bd6 | -4.32912 | -46.79234 | 2025-10-23 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 508439f6-10cf-3341-8db1-82c83393c848 | -2.87201 | -50.71231 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c992f218-2837-3639-a91a-11c58438e1ee | -6.28588 | -47.0111 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88c7408c-5b4b-33aa-b2f3-acfdb8c04632 | -4.37562 | -50.35147 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aac667b-b815-3802-8481-af5de3084a42 | -9.23718 | -45.60596 | 2025-10-23 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc4a4d40-de26-3c5a-bb61-c74545f51a20 | -3.12144 | -49.1039 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ce27d79-5b10-3f52-b17f-f3de8827e58e | -7.27184 | -46.16553 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6a7e190-168b-36fc-9154-de02d760f8b4 | -3.4723 | -50.07138 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c964c67a-a449-30cb-9899-4d7bcd43d58e | -5.32146 | -48.17777 | 2025-10-23 04:36:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 59512b9b-6c0a-3aa3-b470-3b1620d0ebe1 | -5.68472 | -38.59721 | 2025-10-23 04:36:00 | NPP-375D | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b811ec9-fac0-35ab-af55-c92d60dca998 | -2.98213 | -53.99899 | 2025-10-23 04:36:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc7d519e-4589-371e-a482-36cffe5d9062 | -2.85451 | -50.74257 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa46fe93-30db-3aba-8591-9c89a27f33e0 | -3.1122 | -51.20897 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6eba392-4ac2-3db7-9400-c3df356c0906 | -6.32318 | -43.63211 | 2025-10-23 04:36:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45d3437d-d8e1-3ef7-b9d2-c5d83e0b14c1 | -6.85677 | -46.29683 | 2025-10-23 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 1e020fa9-685d-3153-8eac-9eabb67424f2 | -4.37854 | -50.35611 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d4df86-f278-3c7b-ac16-0d9301685cb2 | -7.88417 | -43.55113 | 2025-10-23 04:36:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75be167b-0f33-34b0-beb0-3fe291847661 | -6.27919 | -47.01004 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b20e7eab-e495-3af5-9de4-1a358ddecaed | -3.21428 | -46.80308 | 2025-10-23 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6a45e7e-4e75-3bb9-8653-2619bdeac3d6 | -6.96588 | -44.0132 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6542a3a9-3e9a-3763-9186-decb3afef9ed | -3.64793 | -48.97411 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f278ab99-48ac-34bc-811d-49e936a33e92 | -7.00229 | -46.99896 | 2025-10-23 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94909cd2-a29a-3d2b-b4d0-fd7f3a2c84cf | -2.89821 | -49.16938 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e74bf99c-bae5-3eae-b9a3-aa33966e0333 | -2.81142 | -49.13645 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 525ca834-bd33-3180-9112-4ca506cf301c | -3.24524 | -48.762 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20dafd6a-f2fb-31fa-8a5b-2e7aa1513776 | -7.79288 | -44.00025 | 2025-10-23 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd1b89d1-7ef5-379b-8168-da3ef4b59b13 | -2.85963 | -50.73436 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 580d82b9-fd8a-3921-b188-a14c5f4293f1 | -2.8084 | -54.37989 | 2025-10-23 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4a92b39-8f13-3201-ad71-733841b17e05 | -5.88514 | -46.28761 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d218928a-4c68-3358-8cb1-a3b600ca903a | -3.83083 | -51.29973 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c35052-da55-32fd-882d-852f711d1381 | -6.94143 | -44.46175 | 2025-10-23 04:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0c7bf75-cdd7-3551-bc1c-831c261ded13 | -4.89264 | -39.80864 | 2025-10-23 04:36:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ab2a7492-ec69-38d7-811b-dbd2c89ee158 | -7.82512 | -45.38394 | 2025-10-23 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6beebe88-e1b8-3e88-a5d2-de92fcf9bd4d | -3.39737 | -51.50424 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d703f0c-aaeb-3be6-bbce-b41121c07e09 | -7.64109 | -42.17685 | 2025-10-23 04:36:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa0a79c6-e7d4-375e-a9c7-714e2c75b42e | -6.45428 | -52.82694 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fc91053-6f64-3749-b491-3e35526928e2 | -7.68613 | -42.23984 | 2025-10-23 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f017a2c2-d518-36e5-92a0-75df53b92290 | -5.61629 | -41.12542 | 2025-10-23 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa0ef401-04ed-3bc9-ac98-6c68bfe7d398 | -3.40199 | -51.5001 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 797d8715-d49c-330b-ae66-8837d3b21004 | -3.70124 | -49.56428 | 2025-10-23 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 549e2438-2643-39f0-a0b4-ecc794a503e6 | -3.8063 | -52.14556 | 2025-10-23 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
