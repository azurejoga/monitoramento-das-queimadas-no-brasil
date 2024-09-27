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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f19d57a4-b8e5-3a15-b3a9-7b0812918144 | -9.589 | -50.13972 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 3277b5e1-1204-3fd9-aa60-9a32b8c483ff | -9.58786 | -50.14558 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bb100f18-c7f8-3fea-a660-6be39454d24f | -9.58354 | -50.13254 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2c748eee-33a9-39b5-bce3-e8c208aaa209 | -9.5824 | -50.13834 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8843c58b-9be7-3d28-acb7-fe4452988059 | -9.58125 | -50.1442 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b92b66dc-b478-39fb-8362-43867b6b4ae6 | -9.57464 | -50.14286 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4230b222-b511-3b20-bbc8-3e0cd8b8dee6 | -10.14476 | -50.00539 | 2024-09-27 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f04d3a5c-2019-3741-b963-6ce1cf69372f | -10.14365 | -50.01097 | 2024-09-27 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ed1c5170-a54a-34a9-87a8-760f900b8215 | -10.13716 | -50.00959 | 2024-09-27 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a92bc01a-57d8-34a9-83e9-5d08861c9fb5 | -10.13605 | -50.0152 | 2024-09-27 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e3705ae8-e5b9-3337-9be7-5f92285ef2c1 | -10.13066 | -50.00827 | 2024-09-27 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3858bc72-3613-3577-9192-c8ed2b550c88 | -10.12955 | -50.01385 | 2024-09-27 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66afc032-0ac9-3cc4-b746-f378fdad75f5 | -10.8371 | -44.79715 | 2024-09-27 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 059b6171-b4ef-3955-8cef-bf412eb409f9 | -8.84009 | -45.06712 | 2024-09-27 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97a1070b-47b5-3aa0-85e2-cf928c495912 | -10.84172 | -44.798 | 2024-09-27 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 048945a2-1e4b-3ae8-ad4b-0c4e32c5773e | -10.52473 | -44.87473 | 2024-09-27 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c7813ca-2dee-37f3-8763-ea8d325d3ee0 | -10.06767 | -44.89423 | 2024-09-27 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcf5095e-51a6-3f88-a10b-7dd0652d3c00 | -10.06676 | -44.89918 | 2024-09-27 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eb17eb3-adf9-34f3-9607-6cb1b9b5060d | -10.06544 | -44.8978 | 2024-09-27 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a61e6f4-1824-3170-be5b-9a78d8694cfa | -10.72371 | -45.21288 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebb5d9a8-c042-3622-9e67-8e6d62620e01 | -10.66762 | -45.85883 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c1801f9-5a7c-33b2-b20b-5fc8676b27ac | -10.66749 | -45.85775 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 63345005-d198-3fbc-b67a-7915362961e3 | -10.66375 | -45.85205 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c9c7c3a-5e78-32f9-bc0e-eba0898ebaca | -10.66359 | -45.85089 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41da2860-eeb4-3985-b0e5-7872da471758 | -10.6604 | -45.89722 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a1b5b26-cccf-3ad1-b46d-4a1ed953d41d | -10.65855 | -45.87891 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9b981cb4-41c9-3797-a78d-db27fa4aec6d | -10.65852 | -45.87989 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8d7683b4-dae8-307b-8e91-3ed085d3d1b1 | -10.65752 | -45.88463 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9feb75e4-d4d0-32ed-b4aa-dc4c16ab0a18 | -10.65745 | -45.88561 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2548222a-2d7c-38e1-a496-a04e9b497eb6 | -10.65673 | -45.9169 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b46446b-624f-373d-9435-d5db1819a677 | -10.65648 | -45.89041 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 06a89b89-4c16-3c24-aa95-c11e4688f9b5 | -10.65637 | -45.89138 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b73222d2-05ef-34f6-81e9-0708b8d69426 | -10.65619 | -45.91977 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b3e589-aef7-34cb-9032-3f07acdec541 | -10.65543 | -45.89622 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e7264fd8-3414-3ca6-b17e-7abfbd35bc3d | -10.65528 | -45.89718 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f3c936d1-819d-38df-95e0-4721811ecf17 | -10.65463 | -45.87323 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab29897c-0022-34fc-b0d8-dcedb9db6fe7 | -10.65461 | -45.87223 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 26d579ea-b3c2-32c7-977c-e5965823f6bb | -10.65359 | -45.87788 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 287d2061-b892-3fb0-b30d-b644e0f8ce22 | -10.65356 | -45.87888 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3220fa1e-5388-36b7-9aa2-a8d08d422a29 | -10.65256 | -45.88362 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b2c04165-2dcb-35cc-bef4-0218dcd35bcd | -10.65073 | -45.86659 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5b263963-9da3-315d-8fe7-e0004faacd15 | -10.65067 | -45.86557 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 375690fa-b2d2-341c-9a27-b4d8417d4d5e | -10.64967 | -45.8722 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b20a2be7-2ec7-38b4-91a9-afa7de630a61 | -10.64966 | -45.87118 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 744b3a5a-0ece-3d51-a956-3f9cdbafa30a | -10.6486 | -45.87789 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 521dba7f-2150-3cbd-9c69-53e1ca327aa7 | -10.6485 | -45.96082 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68f1bcc5-5c73-32b1-9a47-4b888b2322f0 | -10.64793 | -45.9638 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8be58b6a-75eb-38d4-a2c7-6745b36d9bf2 | -10.64684 | -45.85998 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 616236b7-af5b-3f9f-98d1-0f00ba5c23f6 | -10.64673 | -45.85895 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d56526e4-6988-3bf6-ae3a-320180a66711 | -10.64407 | -45.9568 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abc6eb27-952f-3e1e-94db-0651815ea9d2 | -10.64307 | -45.96492 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c083436-dcc7-3015-a17e-b21cde100e4a | -10.64253 | -45.96792 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb049906-7fc9-3987-8d05-339eab0d9138 | -10.64239 | -45.96574 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fa41898-c9e0-3c9f-9edb-294e6f8527dd | -10.64199 | -45.97091 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bcbcfdb-23a1-34cf-a521-83c2a4fda502 | -10.64183 | -45.96873 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9251f6e2-2ad6-3ca9-af8a-0787d2677bc4 | -10.63808 | -45.96386 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7714d0d0-7ba5-34b2-8ee6-94565e3658d2 | -10.63797 | -45.96171 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eace6a3b-852b-39d9-b402-9ba6edeb67fb | -10.62325 | -45.98858 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffc1cd79-270c-3912-b68a-286745fcd232 | -10.61772 | -45.99049 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23caa66b-48bd-3e77-8a89-51a14132ef01 | -10.61719 | -45.99342 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 036f55c7-89b4-38d3-b48d-9e6ecefe4809 | -10.41817 | -45.81211 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d32bce6-3004-3952-8baa-17b6ce9b9c9b | -10.41425 | -45.80541 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b17bebb-7ee4-3349-afc3-67861d8d7cd5 | -11.14812 | -45.53656 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fffe0f4c-3e95-36ec-9703-0b603dab54e6 | -11.14427 | -45.55792 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d01b640-c561-3118-9e34-48482ac38ea5 | -11.1433 | -45.53564 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8384fd74-4de0-372d-9511-8628d789e2d1 | -11.13946 | -45.55692 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a7b0d8e-b736-3baf-97b1-f34024e2e469 | -10.82375 | -45.99101 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca8189e0-e61a-38d9-8615-1a45632086f8 | -10.82321 | -45.99393 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 137f8e15-4c52-3723-a919-43de9bc1a660 | -10.82268 | -45.99687 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 873e0ede-885c-37a6-b1a9-31b74a775e3c | -8.92197 | -47.0871 | 2024-09-27 03:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 520a7717-6e26-3703-840c-4fdd7062f052 | -9.01839 | -45.96291 | 2024-09-27 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5016b787-4e70-3661-a310-0b9b73a29492 | -9.01686 | -45.96136 | 2024-09-27 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e738a39-b606-3aec-966c-b881aa24941d | -9.01632 | -45.96438 | 2024-09-27 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25d6d8e2-741b-3d83-97a4-1e4e23f88b4c | -9.55332 | -46.31425 | 2024-09-27 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a36c0ad1-4023-37e5-a0b5-f7676d41de89 | -9.55271 | -46.3176 | 2024-09-27 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a48e974-6a84-36fc-8ea1-835371ff8cdd | -9.5463 | -46.58259 | 2024-09-27 03:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ba805ee-7bd0-3ec5-8333-8f49776629ee | -9.54566 | -46.58597 | 2024-09-27 03:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46ff74e3-75d6-3008-94b4-e30033e3d461 | -10.07026 | -46.05495 | 2024-09-27 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fec13f99-1fe4-3f69-937b-e6f9d5d14800 | -10.06526 | -46.05353 | 2024-09-27 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e936c49-c32a-3f39-abdb-b45f2b5614a2 | -8.88493 | -47.37651 | 2024-09-27 03:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b04a7fd2-56af-3cee-9a03-354446f3b3de | -9.93368 | -47.78519 | 2024-09-27 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00fcb2af-98b6-330b-acc7-78916d9099be | -9.92793 | -47.78432 | 2024-09-27 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fa349a3-4a19-306e-b64d-aa26751750f0 | -10.66851 | -47.92393 | 2024-09-27 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca43acde-884f-3161-80e8-0522d3d2ad63 | -23.59602 | -46.05148 | 2024-09-27 03:51:00 | NOAA-20 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4df2992-a0b5-3713-a01a-aead9dc24870 | -23.58694 | -47.355 | 2024-09-27 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad248664-0337-320e-b83c-6b064b502d82 | -23.5775 | -47.35721 | 2024-09-27 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cb330498-9975-3310-9f33-3a2d8e3d68de | -23.57502 | -47.34722 | 2024-09-27 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7f8fdde7-3557-3b58-bada-56aa92627d65 | -23.57318 | -47.35627 | 2024-09-27 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ab2c9ffb-5194-345d-b972-b52d799c67bd | -23.57224 | -47.36093 | 2024-09-27 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| cd774895-8284-30ce-8169-ff02ba126fcd | -23.57071 | -47.34628 | 2024-09-27 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| e0b3d605-8ace-3091-8553-78d451f2eb17 | -23.5698 | -47.35075 | 2024-09-27 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ef9901cd-be2c-31c5-a6c5-39b0b45dbcf9 | -23.50481 | -47.10818 | 2024-09-27 03:51:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 172367ea-e607-3981-9464-2ea8d743cf47 | -23.41194 | -46.51942 | 2024-09-27 03:51:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 856881a9-cc88-3b3b-97ab-ba30f80d2dfb | -23.41115 | -46.52342 | 2024-09-27 03:51:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5cbd45ed-cee4-3932-a4c4-cbf5a03e0dc2 | -23.40497 | -46.93201 | 2024-09-27 03:51:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e5affb1-871a-3a75-b041-3fac6a1e8599 | -23.40473 | -46.93076 | 2024-09-27 03:51:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 83bb7620-935f-30c3-a2c4-b8a7eb7f9961 | -23.36262 | -46.27817 | 2024-09-27 03:51:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6ea5624f-1fc3-37f1-abe7-2477573c7218 | -23.36188 | -46.28198 | 2024-09-27 03:51:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 05767e2a-fa5f-3983-8ae8-711036004533 | -23.35949 | -46.18604 | 2024-09-27 03:51:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7b5ea15-b553-38e4-94ed-53ad6fca89b8 | -23.3542 | -46.25634 | 2024-09-27 03:51:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README66.md)
