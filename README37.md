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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3a43c12-4bf8-376b-bb7c-e8f63b6e79e1 | -7.86558 | -45.22422 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cd91adc-dac2-3112-9809-4cbc27f6ed7a | -6.64409 | -44.25513 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e29a496-3849-3bb7-87d2-5d14ee6a0a01 | -2.52866 | -44.21812 | 2025-08-31 04:27:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff21260f-3dc2-3dab-891f-592b28295648 | -8.30024 | -44.91747 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 692a3690-01f4-34e7-9280-e642f7155824 | -6.64009 | -44.25825 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a933a657-c465-3516-a148-c037f7bd6038 | -6.17316 | -43.32246 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8c6b56fb-4f9e-33cd-9026-16338ef36c5b | -4.91469 | -42.08954 | 2025-08-31 04:27:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 930f35ff-d884-3e18-a1c9-9652b341ee92 | -9.25781 | -47.06273 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f812122-4e0b-3ac1-8efe-260fce8d1de3 | -6.17198 | -44.13197 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa5c07ee-9787-3c53-af96-013013941daa | -3.51309 | -47.20613 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af90cae8-3dc3-3c0d-b11e-e42cf7f4b756 | -6.81079 | -44.31114 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d7e9d22-a290-347d-bd4e-ac9920871617 | -5.80446 | -43.87255 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2a159467-f5b3-3605-9479-e3dba039219f | -6.11632 | -43.32332 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c49e1c99-d837-35c2-b0c4-3b19fc55d0a8 | -6.15303 | -44.14051 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64b6c2b8-bc2e-345d-a179-8bff338442bf | -8.56364 | -51.30843 | 2025-08-31 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5296f57d-3421-363c-bbe9-10f1f78dafbb | -6.53581 | -44.44112 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd360d8-4aea-33e6-a42b-d2fe13638279 | -7.09707 | -44.57795 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b4ee03c-1a29-3e73-b179-d06971550f30 | -6.53817 | -44.5844 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0842ae82-03c6-30bd-bd03-95f2640a1343 | -6.9503 | -45.69522 | 2025-08-31 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0aa484c-c9f2-30fb-a393-b38ce64fe2aa | -6.21581 | -51.4677 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed49fc60-e5bb-34c4-ae8a-059525fa4f33 | -8.33086 | -47.42099 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29d90235-c054-3d0b-bfb4-4b6a39cd121c | -6.48671 | -43.55996 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a47b76f-01b8-375f-a9e3-da4cd3492b9b | -9.25004 | -47.06866 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fb4b64e-8c7b-3849-b735-d73ba0722388 | -8.54587 | -45.80792 | 2025-08-31 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff565e2f-db24-37db-9914-589aef74993a | -6.27755 | -43.53831 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ff09bdc-3fbb-33f2-be2a-c1c2f2432541 | -6.25226 | -43.3706 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87cdb9e9-a437-3aa9-9d26-7f08f1e00eb5 | -7.71642 | -50.28228 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ddafc207-0e9e-38c7-b974-438f8c45c824 | -6.18262 | -43.56857 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c8d8720-880b-3694-a503-d2231fbce787 | -4.55609 | -50.47877 | 2025-08-31 04:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac7c4caa-a5ce-3a2a-b933-f9ea84fc3a08 | -6.18224 | -44.20241 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2cda600-a427-30e7-977c-2c814b468924 | -6.94374 | -44.05573 | 2025-08-31 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ff8d20b-e3c1-37f1-b98d-5020e54b239b | -7.39346 | -45.92939 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c66c2b1e-f8d8-344d-b559-2db6bb866237 | -5.69515 | -45.9543 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91a58ed5-a6db-331f-b713-6b85783d89d0 | -7.20899 | -45.42602 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 269ae024-14c6-3965-9695-c28d235edc20 | -7.5816 | -42.71911 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ce5f9b4-484e-3ed8-8cd7-6da821052944 | -6.37315 | -43.547 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56471151-639b-33d0-ac96-b8a5b30eb4fb | -5.6525 | -43.64305 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 42569518-9ddf-3383-b7b7-14455e8e38ae | -5.71252 | -47.43114 | 2025-08-31 04:27:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 193f1884-abd0-3ad8-928c-02e54445c3f2 | -7.72312 | -50.2649 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ac7099d-6a0d-3472-ba79-cbd2d9e1e437 | -6.93144 | -44.70348 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8d6f14f-4fe0-3f83-81ed-544243b6ee43 | -3.20872 | -52.25434 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85fdebd3-5b3f-3222-bebf-83be0a38e8a4 | -3.5948 | -47.52517 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0044060e-9d6c-3179-b817-f8a48ecd1eb1 | -6.57707 | -43.6975 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 487e49e9-b144-3ed3-80d9-d579e7da9103 | -8.49504 | -44.74206 | 2025-08-31 04:27:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08d951e9-2c51-36b2-a1a3-42b4973e5eb4 | -6.19646 | -42.75402 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3cca3870-fd0c-3bb8-8e6d-8b4abbc9cbe1 | -8.73266 | -50.38143 | 2025-08-31 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c79ec536-e0f3-32d7-a8be-df613f39233a | -6.53949 | -42.96945 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10e74f57-9b2b-3fa1-a215-72895ecf4b4b | -5.79449 | -42.55975 | 2025-08-31 04:27:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1a31244a-68b5-3d6c-b98f-23e68c9bb6b6 | -3.21698 | -46.82982 | 2025-08-31 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f503c2d9-88a6-35bf-9f41-84d499de932e | -3.81748 | -41.57091 | 2025-08-31 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50bc0bb0-ff2e-373e-82fd-508b2691f31a | -9.25836 | -47.05923 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 928cf8c9-e4a6-3f56-8549-89e07504c94e | -5.83288 | -44.83548 | 2025-08-31 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca394141-6188-3661-8347-8475ef6be93d | -6.22144 | -44.98678 | 2025-08-31 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57a78d22-a93a-3dd2-b7bb-5f4159c7f8e7 | -4.2717 | -48.63704 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 692198d2-e813-3793-bc72-3a244264b822 | -6.60946 | -53.12859 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5ed5ef8-6100-330e-b278-b8d430e82e93 | -6.97051 | -40.94304 | 2025-08-31 04:27:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 404e31de-d9c0-30a9-a64a-399b2a9c6237 | -7.64346 | -42.72158 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e2e63bf9-d8bc-370b-8801-82de90152b58 | -7.10287 | -44.31165 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d33c806d-dad9-3acc-9de3-0e4f2862caf7 | -8.29968 | -44.92117 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e1fefc1-6a9a-3119-a16f-386a3f09de6d | -5.80911 | -43.86551 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b3f6338-2b7b-3a22-8328-8da953aecd86 | -6.49791 | -43.55769 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bc7fcf2-af61-3fee-bfdf-b416d5754474 | -7.96633 | -46.41674 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71077f88-0fd4-314d-af02-1a7d22003cfb | -8.85131 | -45.73149 | 2025-08-31 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6af77f18-6df6-385b-8342-d6db499b0bdc | -5.73759 | -45.38069 | 2025-08-31 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6fb504a-623c-30b2-b2a1-056dc85c817b | -5.6946 | -45.95776 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33a37227-c18d-399d-ac62-f586f9146c20 | -4.30484 | -48.09681 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67f35e20-1579-387d-9694-9322c33ddf1a | -5.14282 | -45.03292 | 2025-08-31 04:27:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b616fa3f-e6f7-3ec8-aef6-9a383d48f519 | -9.26022 | -43.4079 | 2025-08-31 04:27:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dcf88676-e439-3562-98b5-e0e9033e6258 | -7.33094 | -44.09281 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa8ab2a-4047-30bb-ad60-41f545700be4 | -7.37286 | -43.39088 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1e3d730-58bb-3454-8680-2cc42c653918 | -6.25879 | -43.3756 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e853cf8-182f-3586-86b6-7faae5d9e7cb | -7.21381 | -45.43023 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cab60cc-edf8-333b-83ff-a21aa034eb9a | -7.71043 | -50.27188 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a305d9f-79fc-399c-b2c3-73375caf5f59 | -6.21651 | -42.7701 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa9a4fef-5d5d-38bb-a5b4-911844094b1f | -4.91354 | -42.09152 | 2025-08-31 04:27:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f7dfe13-095c-3803-82ba-832d6c62148b | -7.11256 | -44.43222 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0284c552-8038-30a8-9c84-2a232f1dc323 | -7.71572 | -50.31003 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3206db5c-538b-3248-b0a5-f0299113d717 | -6.33532 | -53.43139 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e55befad-4919-3da2-8c11-da517a579b7e | -6.22605 | -42.41005 | 2025-08-31 04:27:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f7a0c22-32f0-30c6-b926-768830604509 | -7.78074 | -45.46001 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83a9c3b9-9dec-3de2-ad16-a852ce2680f0 | -7.09942 | -44.31114 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91f7cd4e-ba85-3206-a7da-9e3d4c7062b1 | -6.6179 | -43.73869 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8b9c4400-6281-30f8-8e04-5d5b958ff951 | -5.47869 | -44.39786 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eff100d5-8124-3195-910d-3242fae20a41 | -6.94675 | -44.31191 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f81e5ad-d11b-3e93-b37d-bc439f43c604 | -8.17339 | -45.04149 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fce0b34-1efe-35d3-9c67-2349efe4f690 | -3.21979 | -46.83393 | 2025-08-31 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c4c796-684a-383e-bb94-4ce3b8d6b8fd | -6.51025 | -45.41475 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 738be6ce-20bf-3350-91f7-3a03b3db6544 | -5.84005 | -41.25644 | 2025-08-31 04:27:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6cf5cb3b-b69d-3a6d-9ae9-88aeb7822e02 | -3.51367 | -47.20249 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c183e3-d381-3f30-83c9-71ff53a6d197 | -7.37881 | -43.40025 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b916d93-1c4b-33ad-97bf-47462ab9054e | -7.20677 | -45.44018 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 772f08cb-d073-3372-aee6-6a5ff44d6d97 | -7.40164 | -43.39535 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 089db51f-5f66-3dfd-91b9-dcd3cd86aeb2 | -6.51448 | -43.54417 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e5150ef-8122-32d4-a41c-f2490d5f4689 | -8.12242 | -45.00772 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d362f4-476c-372a-8dc6-af25896a87b7 | -8.86924 | -45.74881 | 2025-08-31 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97b8f919-d16d-3200-b1ac-ce35e42b5386 | -3.59255 | -47.51714 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b623ab7f-d249-3b10-a696-8d35c9723a67 | -7.15021 | -45.14 | 2025-08-31 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d585e07-dffa-3957-93d1-58eeba5565de | -4.69232 | -48.24427 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb3bf0df-209c-34ef-8093-b7fcf517214d | -6.3131 | -43.51901 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dddacb96-c9be-3955-9902-3dafb93d52de | -6.58965 | -43.63908 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
