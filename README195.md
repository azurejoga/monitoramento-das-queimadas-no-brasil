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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76dcef01-cce5-303f-8b93-3fe12e8182f9 | -10.6276 | -53.856 | 2026-10-07 16:37:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0234bdc0-205e-3542-9231-27dd3f05a7c0 | -9.81187 | -44.78333 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8d32ecef-009b-3a13-976f-2786a3bff355 | -9.93496 | -46.80138 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 1e2f4b82-bb16-385c-a03b-add95c7d09b7 | -17.52337 | -45.46345 | 2026-10-07 16:37:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a51ab4f5-05c1-350f-95cb-452f29505643 | -3.84854 | -40.63231 | 2026-10-07 16:37:00 | NPP-375 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 40.4 |
| 8edeccfb-ee94-387d-b5dc-ca39eb0f34cb | -7.21466 | -44.29822 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 36cae788-69d4-3446-8df8-93a3889aa2c8 | -4.38365 | -41.84385 | 2026-10-07 16:37:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| dc74d5e4-827c-30d8-a0a8-c05cef33e782 | -7.20488 | -55.1134 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f9854b77-dc70-390a-8a96-f321fcce1890 | -9.24119 | -45.66438 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 54ca5be9-8a10-3a89-b80a-886e1a486e29 | -3.9202 | -44.13552 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11e5d3b5-a503-3baa-a1a0-b41868767f7c | -8.07077 | -45.59048 | 2026-10-07 16:37:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3c58e442-6d54-3ea4-8574-80c2f03ac282 | -11.34505 | -51.87914 | 2026-10-07 16:37:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d94f52bf-f45c-30c8-b7a2-e3b5bd17025d | -9.96183 | -43.49268 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 822dd4b8-b021-3829-9fe9-88980b46baa0 | -5.711 | -37.71497 | 2026-10-07 16:37:00 | NPP-375 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 81ed8b93-133a-366a-971c-a87f59ede59f | -8.32548 | -51.30941 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| a4e83f16-a0bc-3f6d-8a19-33fcecf4ec71 | -6.46698 | -52.80812 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e84da154-4612-3174-bd97-04695fda835f | -7.65497 | -35.43283 | 2026-10-07 16:37:00 | NPP-375 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f170bd07-0489-3519-9d6b-8419d8e0f3b8 | -8.26526 | -54.70798 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d78bba9f-0cfd-3217-916a-d353b612aa62 | -6.29124 | -44.91279 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 03f54836-29d1-3fb1-ae68-05b8a590a6f1 | -5.48425 | -45.63636 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 750f814e-5562-3137-aa99-7b63265b2015 | -5.66705 | -43.61637 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd92b463-e143-38d1-9e75-199c1f851b01 | -11.36847 | -46.71645 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 94ff8cdc-d2b2-3afc-a734-da473d6d050c | -3.56067 | -39.1362 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 62939ce7-39bd-34c6-af00-31fc2e81d3a3 | -3.41329 | -40.03774 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 94393a90-d8df-3cf4-9de0-009378fbc937 | -5.49169 | -42.83816 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 60fec8a0-115c-3686-8c03-edc851c3b370 | -4.33148 | -46.64408 | 2026-10-07 16:37:00 | NPP-375 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1e16f573-685a-38f9-8dbb-f4a65f014a37 | -5.96398 | -40.93973 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 7a68a289-5601-3b3a-8f96-de6059eec9c4 | -11.33099 | -46.66613 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 09168f3c-d07c-3a09-b15c-20d18205f6a0 | -11.14109 | -46.1592 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d1b63a89-c154-30c3-ac35-ba4fa0e3bd2b | -8.51294 | -48.17693 | 2026-10-07 16:37:00 | NPP-375 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76a7bcf1-125f-39ed-8bdb-d7eb5f4c4d94 | -3.76858 | -41.77974 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 14b5e072-1de9-33ac-8e97-7314c5059351 | -9.96972 | -43.56673 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 57abc393-4aa2-3eea-8618-b18905f21410 | -8.98686 | -45.94703 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f757af46-4828-3a04-b37b-b134e7285741 | -6.69103 | -48.2043 | 2026-10-07 16:37:00 | NPP-375 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d2af4a61-b05c-323d-92cc-b7149b006ffa | -9.93348 | -46.80502 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1bb6e5c0-1fc9-307f-ac2b-2ebf626d4eaf | -6.36776 | -42.92616 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 47dace65-634f-3786-a590-6ca016d28386 | -3.69476 | -40.85465 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 872e5b8a-90ce-3eff-a58b-2c6af7a4de5a | -6.68345 | -44.96239 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 83753744-c0d2-320d-9890-1bfe5adb0c71 | -14.70695 | -41.26829 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 2329c1ea-141d-3999-bbd5-890500557f9f | -10.86099 | -50.68853 | 2026-10-07 16:37:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| e46f7c43-7f9d-393e-bc34-53ca848ab340 | -5.0384 | -45.29863 | 2026-10-07 16:37:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 38652dee-3c05-3829-852b-d453466f623c | -15.34115 | -41.69697 | 2026-10-07 16:37:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| b9d63189-87f1-33d6-8482-bdc03cb2112e | -3.56086 | -39.13682 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 35.5 |
| e42916ae-a90c-3e9c-9198-265111734ffc | -6.45204 | -44.03883 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| afbee75d-7ec6-3421-a2fc-2d5d446f4c7b | -10.24395 | -53.93218 | 2026-10-07 16:37:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6ebcbc38-6a7d-3847-a14a-81349879f7ec | -7.34633 | -45.28764 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 73cab8e4-d240-37f1-8c10-29ecb6f21852 | -3.29402 | -42.27924 | 2026-10-07 16:37:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6c27c306-77f9-32f0-a317-0d5cbbd539e3 | -7.87201 | -39.90792 | 2026-10-07 16:37:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 26.3 |
| d84c07b1-0e72-3674-aa04-8b20b34267fc | -4.62703 | -48.86047 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| dca5844c-df00-3160-8fba-6e7e2c0abe85 | -7.89411 | -54.7169 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3b65c32a-ce16-355f-ab80-5ba39517d019 | -5.48868 | -41.39981 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8d785365-139e-31ba-ba38-951b5a2137f6 | -6.33017 | -38.86003 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a7818507-ac42-3e99-b4ca-4ad777598efa | -5.13568 | -44.74036 | 2026-10-07 16:37:00 | NPP-375 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 566b2f21-8eeb-3ea1-8724-a01d3bdcf5fd | -5.24665 | -50.91936 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0723ee17-14fb-3950-b532-7fee67591a5a | -11.08802 | -47.6197 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6db3bc91-d90a-3496-af1c-dd4ce431880c | -7.53232 | -45.87822 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ed7fd552-1963-3b48-9838-019f5f147510 | -4.96765 | -45.58855 | 2026-10-07 16:37:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 5e94f7c1-893f-3a6d-8da1-fbc2eefa32ec | -5.25116 | -50.91876 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 81c6f8a3-f7e4-37b3-9070-5a56d4585438 | -7.21006 | -55.11177 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 0fcfe478-11b3-36c1-b641-cc5425c75b6c | -10.94502 | -45.3856 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 27116530-54af-31a8-946a-135725811d7d | -7.82481 | -47.62856 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8bbf14d-d682-389f-8af8-8b425333d745 | -3.76921 | -41.78381 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| 866e1e09-ad23-314c-aabe-f6dfb75bd6f6 | -7.74909 | -54.94775 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 43a99e4f-12ac-3663-935f-af67068a3897 | -3.75245 | -44.97969 | 2026-10-07 16:37:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 322c6f0e-a0df-3116-8008-e1f56521ba48 | -5.61879 | -46.68003 | 2026-10-07 16:37:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cecf25f5-4328-3026-a0cb-82b077c15c2c | -5.37574 | -44.16395 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2175f017-e62d-3749-a9f7-acf9e2d97c2b | -5.27867 | -45.72993 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b89efd1f-f8b6-31e0-afa4-d931af8ddf5d | -5.58505 | -44.25085 | 2026-10-07 16:37:00 | NPP-375 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac7b19ad-8650-325c-a061-9c1d3cad301a | -3.94822 | -41.54335 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| f6213c4b-1d91-3c23-b910-3b6d0e01de18 | -9.44647 | -45.81976 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 77e09f2f-a73f-3fb1-8f33-10c02c19b067 | -5.94946 | -46.36425 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7358fde9-fd66-3607-98ac-b016c37d4f2b | -9.15833 | -45.81417 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9f2f1a62-f5f4-3fa6-9c8a-9569db332ae1 | -3.96273 | -38.68909 | 2026-10-07 16:37:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b412de59-e788-3005-ac64-a17377ce9de9 | -15.46996 | -41.07187 | 2026-10-07 16:37:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5835afff-f10a-37c1-aa13-eb9d28a990dc | -6.44425 | -45.20685 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17cc86dc-e54c-39aa-b331-078ef9eb2916 | -9.9052 | -44.80231 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9151a4ab-6c0e-33ec-8ad5-f9a617b5f4f2 | -7.83845 | -45.50434 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8c5c3c06-7d1f-3128-ac79-6e2073a142a5 | -9.37923 | -49.36288 | 2026-10-07 16:37:00 | NPP-375 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 90dbe0d8-f99a-3e3f-816f-bb4b37512d0b | -5.7376 | -45.16415 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| aed29a15-59f7-3775-b78e-2700694e9270 | -10.4712 | -46.82417 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e5b5ad7-af7a-3765-baba-fa968e0107fc | -6.8375 | -39.55298 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 372b7589-902d-3b48-aa39-dd00c4d4d3a8 | -7.03648 | -52.76174 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f419967-8865-3e6f-a5c2-834d7983cf04 | -4.77245 | -44.08646 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| acae3daa-55a4-3d1e-994d-dddb8d18d8a3 | -9.20468 | -46.70467 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f016c3b2-8137-30d1-8b1a-2588e45159a5 | -6.67215 | -41.76916 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1ad8f400-6fc0-37dc-be77-95b622b4d987 | -6.02079 | -53.5446 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5628466a-a2eb-38a9-aa9d-e88c737e80e7 | -16.72643 | -42.04686 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 672346c8-8706-3029-a941-9372696fd295 | -7.03573 | -45.42405 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 411f47a3-6117-35f7-b0f2-80a4cd7fd393 | -4.31337 | -48.62544 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| f9f9fc6f-46d9-3bfe-9a97-66840842de10 | -5.23975 | -50.918 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0497e52d-03d4-3d28-a18e-35c6bcd409cf | -3.87763 | -44.11805 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 76402728-991e-334c-afd8-e62b1779fa5f | -8.06309 | -55.30221 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 98441a6a-cf14-34f8-aacc-688d167a3a22 | -9.80336 | -48.92134 | 2026-10-07 16:37:00 | NPP-375 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db919b9e-11bd-3f4e-82c1-e8439e6a2557 | -6.17356 | -52.92487 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 519e3185-ff62-378d-9b26-7f3bed375dea | -4.27276 | -43.01561 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0d60362f-4baa-365b-92a8-8c49e827feb0 | -6.81291 | -55.29857 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6982f24f-4c8b-3576-a225-148a39e0ab1a | -6.26858 | -52.95242 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 236328c7-4808-3e13-b3c1-d6e833f5ad73 | -4.85445 | -43.36737 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4a77cde6-b54f-3aee-8ab2-cf7b09ef1c27 | -3.10382 | -42.95057 | 2026-10-07 16:37:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 07979ea0-96f7-3183-b430-174a8aa7ec5c | -6.07687 | -44.39301 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README196.md)
