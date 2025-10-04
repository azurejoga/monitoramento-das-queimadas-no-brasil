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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d5f9319-3d18-31d2-94d6-999f75fb8131 | -7.78682 | -42.57912 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8dfaa1f0-0a62-323a-a50c-6f2e65b2d6c6 | -9.34943 | -45.78196 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ac989d9-8107-39b6-ad90-f751294fb1ab | -10.83895 | -41.27497 | 2025-10-04 03:51:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45fc2320-d901-314a-8dcf-f52115c03cbb | -6.17425 | -43.93036 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0ce9930-79fe-3944-9707-0ae07297e316 | -6.36974 | -44.29844 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbc742f9-d2f2-3c19-8043-a4237063e6bd | -9.38552 | -40.45708 | 2025-10-04 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4872e35a-06cb-3424-bb81-94a0f8ab44c2 | -7.71489 | -42.57446 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34f1963f-e519-3dc9-8ae4-53a20489f9bf | -4.60991 | -43.15839 | 2025-10-04 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| afe24d95-a8a9-3884-822a-e61d382f9e2f | -10.84602 | -47.20234 | 2025-10-04 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 830d6577-4d29-3c4b-987e-7fc1e2c0a7a0 | -11.45173 | -43.49997 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0904ca6f-0e7c-3655-9877-9600285b3908 | -8.23131 | -46.79493 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31f722ba-1eeb-3ffe-b477-a00b5cc4152f | -6.16048 | -44.61372 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b106c3c5-72d5-3937-b83c-e4e8dce9030c | -7.04958 | -43.21851 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fec29088-7259-3d4b-a10b-057e4bb6e1bf | -7.75361 | -42.52309 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ddfa58e5-f6f6-3fe5-8669-83ecadeb5a02 | -9.25857 | -45.77692 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 628b246c-e159-35e6-b5a3-2f7219cfd06c | -8.23163 | -46.79411 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4e6fb95-23e1-3369-8623-375f6f2e8e01 | -11.11486 | -47.74588 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecbbe4c5-cd67-3d40-9c9c-f30798ea94e5 | -11.46656 | -45.15244 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c053dd7-42c8-3e00-94f2-40d91417d6aa | -7.33164 | -41.4432 | 2025-10-04 03:51:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 18b49a73-fae1-3644-b59f-3e339534cd77 | -7.00877 | -42.30553 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a45c7d8-e577-3b83-8053-fac89041e07e | -11.05511 | -47.78685 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 886f79a9-77e5-3103-b102-bfe9be4bd7e7 | -6.18074 | -44.28807 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2fb9ba4b-710b-381b-9f6c-25041126f70b | -7.73526 | -42.60549 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e647ec7-7cc4-3319-ba91-c6aaf61cf9a4 | -5.31423 | -45.30358 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63217c34-a720-38f1-802d-15a3ebac820e | -5.84077 | -42.87125 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e495f13-fe16-3fdb-a5fc-a859fc56cd45 | -7.75775 | -42.52381 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c126783c-a956-3954-83ef-fe7e4bdd7942 | -5.19327 | -45.06655 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 66727d8b-044e-335e-b49a-2f16316c1630 | -6.27761 | -44.04044 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3eb4e1e0-70ae-368a-9ec3-eecc3260b640 | -7.04488 | -42.77486 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1a8dc6f9-318f-33ce-9e55-2ac98a08f55e | -8.17733 | -44.14613 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0384baa3-52ef-3baf-bd52-8771e27d1068 | -5.26412 | -37.93201 | 2025-10-04 03:51:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a470e7a9-dea5-375e-aeb7-1b909e07eb74 | -7.73591 | -46.31477 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 925715da-a8d8-3aed-8d3c-6e6cd46e8ee6 | -11.48418 | -44.98389 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4193ec10-0e2a-3250-a9d5-aa18d741e851 | -7.73023 | -42.58484 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 61f1ca8b-2dba-35fd-95c1-337330e4b321 | -10.52973 | -44.51903 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04334122-f02d-33ba-be0f-a54d57d442ea | -5.74291 | -42.91716 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1e1e5bbc-11e2-338f-80c1-76fe840dd556 | -8.97298 | -46.72921 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d089a16-4a55-34a0-a01f-1b80c115bb15 | -9.10828 | -44.40103 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 23218eae-6e87-3f2d-a4b2-ff11649eeff7 | -5.93312 | -43.31443 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47fba3c3-d0e5-3952-a65d-bfa57d52717a | -5.88299 | -44.25825 | 2025-10-04 03:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25e7f43c-a497-33ad-a033-085d6bf48e4e | -7.05048 | -42.76772 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad5b90ea-2789-3a29-bdd6-53980416fd90 | -10.64113 | -49.13768 | 2025-10-04 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 830318d2-bcdb-3147-8f5d-7bb92d54828f | -4.95133 | -45.07 | 2025-10-04 03:51:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f16c3810-4d39-3292-b9d3-5cb63c4e22f8 | -5.87711 | -42.5279 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2d83772-26b9-3e3a-9789-d5dcae12bcf9 | -5.31999 | -45.30124 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab6fda37-7284-3cb4-b92d-eab9c23749b5 | -5.71741 | -42.63993 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1ba7f55d-b7c4-340f-acfc-09289aa18941 | -11.702 | -44.43648 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dee3239-f1b2-30bc-8492-4266912db56a | -6.72794 | -45.97208 | 2025-10-04 03:51:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b989f849-c099-35da-aef2-89bb1e68dba8 | -6.45975 | -44.57538 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cc5e9e0d-5116-3105-b385-0c5b022f79f9 | -7.86899 | -48.21181 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af436471-ed63-373d-8f1c-eb1e8f3fe2b8 | -6.35336 | -43.43472 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a71c913-8897-3286-bbff-c1e144058730 | -6.34383 | -43.44446 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 695f685f-6eec-3673-b366-4469b1be57e3 | -5.24953 | -42.97053 | 2025-10-04 03:51:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d0fd3226-9860-3294-b611-bc66908957d4 | -6.60711 | -44.31306 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10cc49c9-4d48-3c8f-93a4-f7d5a60c9d05 | -7.46864 | -46.85087 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4fe77f34-2fbb-30e6-b91b-aea9a482f56d | -6.66115 | -42.82906 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e3bb46b-5b10-3a25-9726-1a8219fd7239 | -6.07805 | -42.51476 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 1cf71e91-f776-34f0-81bb-865a706e6ab6 | -6.59324 | -44.62775 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4c724d33-6250-36c8-bb04-c9d2605042a7 | -10.02397 | -44.0184 | 2025-10-04 03:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94adbc2c-69e9-32d2-a36f-070d7f335b49 | -6.24628 | -45.35541 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f23bf7ca-bf19-39c2-afe9-8beb182755c8 | -6.24271 | -45.34565 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69c7b66e-5f5b-395d-8b7a-54e593c770d0 | -10.02546 | -44.01634 | 2025-10-04 03:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9af9040e-e8d9-3480-a1a4-260bb5b37459 | -8.19364 | -47.00559 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b67136b-d1f5-3fe2-ab2e-9f1213a1e230 | -10.53509 | -44.51517 | 2025-10-04 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c14499b-7e5c-3c9f-888f-c9396aa40b2e | -5.97918 | -44.15007 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 476c9e35-bfe7-3f81-b865-f182684d52c8 | -9.99142 | -48.27932 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8e6827d-b041-371f-b77d-474145ff6cb1 | -11.42303 | -43.48797 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca0d6d59-041c-3b22-9648-f6b1415ba34d | -4.65768 | -45.79393 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e5acfaa-083c-3e6b-968e-afb18e2322f1 | -6.46571 | -44.58291 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0cdb924-17f6-3407-bcf1-89155f39c45e | -11.46745 | -45.14766 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63bd2d94-d6d3-3f53-81bc-02899ad386f4 | -8.81579 | -44.82382 | 2025-10-04 03:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd1ba807-4221-333b-98c1-a02469bf7922 | -5.98918 | -43.48567 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df84b63b-cb19-3ead-86b9-f2c01dda5b50 | -7.29176 | -38.09573 | 2025-10-04 03:51:00 | NPP-375D | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9413b25a-6305-3065-b719-71c62055c737 | -6.39416 | -43.61224 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5c0a2b6-c070-3ae8-8403-b62e25305a41 | -11.45139 | -45.14082 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 814863cc-024a-3646-b961-d6c222ce65d1 | -11.14862 | -43.37915 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed007bfa-86e0-304c-b214-2ad2e16f05e2 | -11.48036 | -44.97881 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 306916cc-86a8-365c-b330-f531a72f8686 | -11.14517 | -43.37453 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0e12bec-f132-34be-88fa-23cf01672ebd | -7.15353 | -44.21294 | 2025-10-04 03:51:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8dc9961-383d-3dfc-bb68-b83f06ba22fa | -11.47942 | -45.03726 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40c530f2-9ea7-3a88-bbc4-72d47acfd4fa | -9.93783 | -50.23224 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffd82cd9-ebfe-3753-a95e-9600006f904b | -7.70722 | -42.56928 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d09951f6-6097-3250-ab42-519e36b157af | -7.54044 | -42.40622 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 334509c7-4708-32df-96e5-328c95921096 | -7.73088 | -42.58107 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cc95cd22-1299-3c14-9122-ee02902ac21a | -7.3482 | -39.17419 | 2025-10-04 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 873bb183-d6a3-352b-bb95-6b688724f04f | -5.6604 | -42.71484 | 2025-10-04 03:51:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 75562d8b-39fa-30b6-bcc8-96a9962a8e03 | -10.31424 | -50.35177 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e173b68-1719-345b-9463-c22de0da7b46 | -6.66477 | -42.83389 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 010d2347-26f0-31c6-822e-b7b75a22f3f4 | -6.99952 | -44.19882 | 2025-10-04 03:51:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 982292d7-8507-36ea-a1b6-651c5dc60a80 | -5.19889 | -45.06457 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ca71e739-7c94-374d-b91e-0ac1e12f587a | -9.98964 | -48.28163 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 272bec2c-e9d7-34fd-b8c1-fce89f9e5313 | -4.67794 | -45.68475 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cb3c61e-9da0-358e-8350-fee335695a80 | -6.22566 | -42.93397 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d3c8c86-3e19-350a-8851-146e686eab6e | -5.88516 | -44.26628 | 2025-10-04 03:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 086fcc7a-d481-3fb1-9c74-92074c57840c | -11.07567 | -47.88879 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15292ad8-6f2c-3e9a-bfb4-b713dc21359f | -5.33255 | -43.34905 | 2025-10-04 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1d7a9d7-8aac-3bbd-84ba-24b47bbfa010 | -8.22283 | -46.81161 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a575e72a-2a1f-3375-85ba-40a233d750bb | -7.7814 | -42.58592 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6c186f7-ecb3-3625-8d12-f9689f9e7e66 | -9.94527 | -43.57413 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51f1470b-67e2-33d8-9e49-32e997e1d86d | -10.61316 | -49.15119 | 2025-10-04 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
