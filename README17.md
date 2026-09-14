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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e728df-89c5-3e04-98ad-dbd5f9dd6d82 | -6.41995 | -41.55587 | 2026-09-14 04:32:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3be2ac8-0a22-3d24-b978-9fb375afa815 | -2.6178 | -54.72508 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c36838fe-bc08-3836-bb05-a9f2e48f6c58 | -9.42355 | -50.12326 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e501e2b8-8c4e-3226-a164-f5e9e5219c6e | -9.42046 | -50.1175 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1d7f6972-1573-3f40-b788-fbe1e16e28ac | -3.88359 | -41.04298 | 2026-09-14 04:32:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6bf711ae-2ae0-31ee-9a98-e28066f0d972 | -2.88803 | -50.41113 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e89ee31a-5da5-3397-93d3-5bcba57c53be | -5.0874 | -56.25505 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8058c6a-7cf5-3218-8a0f-fea9a0bf84b4 | -6.79122 | -58.79305 | 2026-09-14 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9b0ebda-adf2-33fe-b524-10388bd1b7ff | -2.6711 | -57.54356 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 200889de-6f2d-36d9-9205-1f9220529ce0 | -7.13054 | -42.09469 | 2026-09-14 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c8f403d7-0343-3b82-b71b-624f3243a5b4 | -3.37724 | -50.7673 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 585c8aef-53f5-3317-b322-961fbe448dbf | -4.13134 | -54.01412 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b01fa2cb-9ba9-3318-8939-622eba0a1dab | -9.33305 | -44.36884 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 373418e2-bc4c-3935-ab06-09ea726bf7b9 | -7.09324 | -41.80199 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5680fdd9-b7f9-3bae-a809-4fc8dba6e435 | -2.88285 | -50.41477 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e57347d9-6ff1-3a41-a8f2-5d2e6d3d08de | -2.91771 | -50.43745 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 5379e1ad-08bf-3c9b-b393-fa38b6554f4f | -7.10488 | -55.63587 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf11d6b9-1a44-3dbc-b185-fb149da20536 | -4.34709 | -48.96809 | 2026-09-14 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 921e9f74-dc09-351f-a3a0-3869b7f723cd | -6.32985 | -44.18004 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09c003b8-ce01-36d0-b67e-3d4df9679079 | -9.41215 | -50.14229 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e149fe65-9c28-3946-93b1-135ee4cc7ba2 | -2.93783 | -50.4271 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 42b8ea11-af7c-3481-8496-1d01135a3e0f | -3.04776 | -51.25863 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff8dc884-5e5a-311f-ad42-f966cae2eaa8 | -5.01938 | -41.95704 | 2026-09-14 04:32:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| feb7b2b5-30e9-3581-aaf9-ff31a50f568d | -9.44592 | -47.85685 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29bf5e86-d56b-3344-bd11-33dd76cd754a | -2.61439 | -54.75272 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 579a0953-0be7-3d8e-acf6-35ef0cb758dc | -6.10721 | -57.66764 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a11e5ffd-a204-3ee2-b4bd-736f34cd3262 | -6.42058 | -41.55169 | 2026-09-14 04:32:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ff425f0-46e3-3996-8c42-6ec934fead7d | -2.91026 | -50.45435 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a711cb6a-4b85-3fdd-8ce8-7f470bde6f42 | -8.56987 | -44.47461 | 2026-09-14 04:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 470600ef-aaa1-355b-97da-1f8e7a4d74b9 | -2.61276 | -54.7554 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4787c3f3-4703-3d18-8311-2057e827a595 | -4.13698 | -54.01485 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e41dee93-749d-3b0a-bed4-bcbc4560b1cf | -2.93998 | -50.38685 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43507162-e0ff-39e4-abe0-70365cff7a9f | -2.89769 | -50.40819 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2827e6d-1fce-391d-b805-83592512b730 | -7.42348 | -41.92844 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 505bca22-a8e6-3769-a1ab-62ab7d63c962 | -2.82536 | -49.23404 | 2026-09-14 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f80f5b46-f4a4-321d-b022-bc361519a4d0 | -9.44241 | -47.8563 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4be06f24-213d-3720-9fc2-494d51a3711c | -7.15548 | -42.09847 | 2026-09-14 04:32:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4391fa7d-06d4-37a8-bfc1-469e128f3f0b | -9.1405 | -51.58303 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667f7885-8420-398a-9573-b5de6da657c3 | -7.10897 | -41.79586 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 67f00941-c116-38eb-b773-88704f1f1bce | -7.96437 | -43.98475 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d88bc521-def2-34d9-8dda-270882dd6d57 | -6.33401 | -43.36596 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cd8d15b-1c96-30a6-b535-e60aa62f1ed4 | -9.12157 | -51.58821 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a01927b-1bb2-3349-8f32-b909d814d1ba | -6.29058 | -55.27826 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ea7d0ae-f043-3d50-bc4d-f89799066f33 | -2.90805 | -50.40084 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 41b0b4d9-a1fb-3c1f-a21c-53a2c950ea71 | -2.9252 | -50.4082 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 05a2e0db-37f0-328b-ba15-d45da9cfba66 | -2.67456 | -57.56543 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b43bbb23-8f15-37c2-a064-7750bffdf5a4 | -6.85026 | -55.57014 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fc1f916-4e37-3802-a211-2b8dfd8e9f97 | -6.66377 | -54.98386 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2d6023d-3bec-3c0d-85ff-99309d6331a8 | -9.49369 | -45.48043 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e5ecf8f-7d36-3301-a34c-0fe9eebe4844 | -2.89123 | -50.44795 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ff47578-8a28-3890-b68e-42dc599369d7 | -2.911 | -50.44994 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 5c4ae92a-949b-3296-8124-76a16174e739 | -2.70067 | -57.54176 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6421e0ed-8a8f-36a3-bb12-0178ad4ed0b4 | -8.5393 | -54.69358 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 899f9309-7300-3ae0-ad96-751dfbde830d | -8.53735 | -54.70399 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f43cf53-12bd-3300-82d6-2f4e632fc853 | -2.88516 | -50.42875 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 680b1973-e84b-3381-998e-f9b6f1d9464a | -7.78683 | -46.66268 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 240dc64e-2b06-330d-be32-ff5c78077943 | -9.3743 | -50.17253 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b85eb4bb-2581-3614-9f9b-43bdcb370e98 | -2.95189 | -50.39784 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1b3c8a1-4feb-3226-9ddb-14cd105a2b89 | -3.22472 | -50.59123 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 424fb556-9289-3bdc-9dea-89935726efbf | -7.07338 | -43.55283 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8979600b-135e-39e2-9b8d-448362faf76b | -8.54149 | -54.71189 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05dd74c9-0c29-33c7-b04b-d6bf15cc6376 | -9.41303 | -50.13718 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17794a1f-5bba-3e8e-a746-6c168a7bd773 | -2.91696 | -50.41465 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 59997b3b-e6a2-3df4-b278-42760b3e7496 | -2.92024 | -50.43913 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ee029173-e2fb-34d0-a4c8-45284c441198 | -3.53776 | -53.98562 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e6d39f29-d2ed-36d0-bec5-92158f28dbda | -3.25 | -44.63472 | 2026-09-14 04:32:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aef91f18-ee5b-3b65-901d-231d58a02d34 | -3.85874 | -51.97753 | 2026-09-14 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0ead09c-b3c2-375a-8cde-43344ca8867f | -2.60676 | -54.75434 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ae47e589-ae7c-3400-8368-b940f61e2b5a | -2.9549 | -50.40731 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31397625-49e9-3878-92ee-d7e0e5aab0d3 | -7.31311 | -45.30203 | 2026-09-14 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8a10cc9-5673-322a-a9c1-e1c72c92f760 | -2.91322 | -50.39717 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 35c3c0b9-0512-3b73-a438-5a0fd85f5b07 | -6.34579 | -44.10028 | 2026-09-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd4e0aa6-f535-3ba0-9c6a-fc7a62580797 | -10.29937 | -45.30417 | 2026-09-14 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 339a22c0-cc73-36cd-a268-4db0790bea3f | -8.80862 | -46.58768 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 70c2a229-f6a5-3f55-98cf-6827897d7bff | -2.8925 | -50.41185 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2334026b-de64-311c-a3ae-efd5f2028e52 | -2.87693 | -50.42286 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 102a7eb2-616e-3211-ad99-26cf79b8d9d8 | -2.91252 | -50.40157 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ad1f3ec4-eb4c-3250-ac46-07367d965188 | -9.44331 | -50.12673 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e73636e5-b865-30a9-bad3-64c5b48558a8 | -2.95417 | -50.41167 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51723e43-b422-36f8-8087-6e2018942c94 | -2.4922 | -49.10897 | 2026-09-14 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 933ff265-671f-3dd8-b96f-c476b3debe97 | -6.59633 | -58.85224 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4aaf488a-e448-355e-9ffb-555f4cdc7e1a | -9.43936 | -50.12605 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 352e35fd-581b-3bb2-9c17-6247cbfd2275 | -5.81512 | -53.80772 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36c9ce8c-d21b-3785-81be-299486e65b6c | -5.80977 | -53.80669 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18936d49-d29e-3a69-ba3d-0ffb96c5402a | -2.966 | -50.3956 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84d96b72-9ca6-388f-bd22-6441470a170c | -2.91647 | -50.43399 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 444f21eb-6fa9-3aa0-b4e7-c45ba4af671e | -2.93409 | -50.42199 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 66804a16-2f1a-39f4-bacb-b35f1cd0f1a9 | -2.91993 | -50.39706 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c75f168a-98a3-31ef-b58c-95336d697f29 | -6.58919 | -58.85619 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bfac1ee-56cf-3344-b1f7-ce3080f83e73 | -9.45271 | -40.39241 | 2026-09-14 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.2 |
| 1ac0a7d8-3d97-3603-84ea-5cfe5cc0649c | -8.39095 | -46.29902 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0efece72-ade0-32b1-abc4-3184819439ef | -6.59359 | -58.86697 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 06fd3c38-f3fc-34b6-a7aa-8608f3087387 | -4.59511 | -47.17393 | 2026-09-14 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e35e570-5093-3297-b5b0-6f3b236bf7c8 | -2.92365 | -50.40219 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d6e6f2cc-9a6f-3207-aff7-720e6fc28bc7 | -6.69392 | -43.1425 | 2026-09-14 04:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2a32e83-143a-391c-9268-d8ed5931c4a8 | -2.91769 | -50.39789 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 7a1c1a19-7bb3-3b59-b197-24ec8a41d4eb | -2.89715 | -50.43981 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| fcc0ca54-42e6-330a-a8f0-dfad7337251c | -2.89697 | -50.41258 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 85959505-97a6-3ab9-b4b5-473aed99ce8d | -9.36556 | -50.12885 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebd24641-7a85-3cc9-b1ea-160e30236f2a | -2.90802 | -50.4676 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
