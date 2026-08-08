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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3754d878-698f-38fa-9834-2bbf34819db5 | -8.163 | -55.4266 | 2026-08-08 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ffd3a4bf-bab8-332d-9516-ada5c5e1ca4c | -11.2851 | -55.862 | 2026-08-08 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 3198b420-50ee-3cc7-a1a1-6403e2e1f4f0 | -4.2634 | -48.2016 | 2026-08-08 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9fb63926-9a81-3ce5-9246-d4fce926c814 | -4.2635 | -48.1799 | 2026-08-08 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| beba6494-e84d-3be6-af97-1d6efa070300 | -3.9671 | -48.1283 | 2026-08-08 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a753a330-bed3-31be-9e3d-e866c539bbf7 | -11.2662 | -55.8635 | 2026-08-08 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 54af6efe-314e-3531-b7df-8714410938f5 | -14.3617 | -54.9701 | 2026-08-08 00:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 21e54b17-ec63-3368-b2d9-77cc2778b2e9 | -8.1631 | -55.4066 | 2026-08-08 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8a0cb0d9-4fa3-389a-9787-d3b7c0faaf02 | -11.0334 | -44.2696 | 2026-08-08 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 2f0387fd-dc97-3b5c-bef1-486a84cd6b6c | -4.2635 | -48.1799 | 2026-08-08 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9f0933ca-46e7-3dde-b23f-410f2783a392 | -11.0526 | -44.2668 | 2026-08-08 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| c72ea185-2a42-3a6f-94c8-04ba56faef83 | -4.2634 | -48.2016 | 2026-08-08 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e91c6eb7-db88-33c6-ab60-171a6a4d4f09 | -3.9671 | -48.1283 | 2026-08-08 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5ca0c589-85e5-34b7-89f1-889c9fe34ab9 | -11.2851 | -55.862 | 2026-08-08 00:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 474b26e2-3ab5-3e76-8dbe-62adf571a086 | -11.2662 | -55.8635 | 2026-08-08 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 32eb9bfe-7504-3331-b65c-9855daca0b3a | -10.2662 | -45.7979 | 2026-08-08 00:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d8dccd4b-8f97-3171-96ab-9437c30158a0 | -11.0334 | -44.2696 | 2026-08-08 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 497ede7d-6af5-3b43-984d-9b8c83391333 | -11.7167 | -50.117001 | 2026-08-08 00:12:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0426a591-a67f-34ff-9897-f45190c229a7 | -5.4283 | -43.432499 | 2026-08-08 00:12:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9aa6e432-8cac-3a3f-91c9-e1e8e83decc7 | -12.5394 | -46.948799 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f82d3365-c627-36ba-9b2c-52b570f4f9fb | -10.2669 | -45.804501 | 2026-08-08 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed9114ee-b4bf-3518-9825-8670dd64c220 | -7.3595 | -45.373001 | 2026-08-08 00:12:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9966a9dc-7c00-3869-8ed5-d37116f3a8ef | -3.9484 | -48.124199 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596af2fe-15ae-3315-bdf3-582d36b5f329 | -9.3834 | -40.3279 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed170131-e9dd-356d-8422-b95e3c92e9ec | -2.7636 | -49.464401 | 2026-08-08 00:12:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 580983ca-c660-3df1-8c68-871540653d0b | -9.6259 | -40.578098 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 33f29fa4-8c50-3f5d-911d-c50bc3981497 | -14.4149 | -45.6549 | 2026-08-08 00:12:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c32b3e2f-82e3-3b34-9961-a48d80cc8278 | -6.9881 | -42.9062 | 2026-08-08 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71e1ec31-3c63-3149-a6c2-ccd600e66fa8 | -12.5422 | -46.962799 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 526f0580-b45f-39c6-909f-3db2b3427983 | -12.5366 | -46.934799 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca7e97b-4964-3ed2-a21c-bcde478fcc0b | -12.5533 | -46.916901 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5ffb084-cd20-330e-9516-57b2d4c15a52 | -3.9553 | -48.109798 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a06ee2f-55a2-308f-9bc7-2fb456ee0e8a | -9.372 | -40.323101 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 13ce678f-aaa4-3090-b59a-e6553bfd1755 | -3.0492 | -39.923302 | 2026-08-08 00:12:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| af861c4d-6886-3551-8fca-351156b20710 | -6.9173 | -42.407799 | 2026-08-08 00:12:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5174340-6963-3dc1-a743-96bf1bd8dcd0 | -9.6275 | -40.584999 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 230c29e7-5985-3672-a959-afd0d58f7631 | -6.7136 | -48.105598 | 2026-08-08 00:12:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 822115e3-f314-3c3a-8ec6-6fb11e4f20f3 | -8.1161 | -45.884701 | 2026-08-08 00:12:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0cc59ae-750e-3ba0-b8ff-73e86d7d79fa | -6.9768 | -41.4869 | 2026-08-08 00:12:00 | METOP-C | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72415656-e9ae-316d-a929-28164747d893 | -4.4542 | -47.912601 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb0c86c-58be-3096-97d7-54261890beaa | -9.3802 | -40.313999 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| afba0ae9-5328-37f3-a430-cbe8490728a4 | -6.9098 | -41.964001 | 2026-08-08 00:12:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a934740c-7509-363e-a225-3acd4b0613fe | -9.3704 | -40.3162 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 06c2d399-8b1c-32db-bc87-ab3c10da99b0 | -11.0357 | -44.268002 | 2026-08-08 00:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e18f521-c68f-33ba-9089-642895cdd842 | -12.5492 | -46.9468 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 544ebd8a-099b-3d8f-8dc0-51ad2da89176 | -6.9188 | -42.414799 | 2026-08-08 00:12:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18fd5708-4f85-37af-a49c-6e00c7b9f578 | -14.4173 | -45.667198 | 2026-08-08 00:12:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3ba5e8-6ef5-308f-a246-c360bd08d4b3 | -20.055599 | -40.886398 | 2026-08-08 00:12:00 | METOP-C | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 606396ca-fb16-3926-b507-c540388405bb | -4.4515 | -47.900398 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 495b4be8-ddcb-322d-8c0d-bec3e51da7ae | -4.648 | -43.124599 | 2026-08-08 00:12:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d03630e4-8bad-37e1-8268-8239ea57bb86 | -13.9569 | -41.869301 | 2026-08-08 00:12:00 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7a9a583f-d668-3c52-b061-1204acebaeba | -13.9471 | -41.871399 | 2026-08-08 00:12:00 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e53aecf1-e5d2-37fb-9356-7b81ad28dca0 | -20.368 | -41.164001 | 2026-08-08 00:12:00 | METOP-C | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16e9830f-854d-3606-b49a-74419d8dc43c | -11.7113 | -50.141399 | 2026-08-08 00:12:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 629aee42-6897-360b-98eb-905473e915b1 | -4.3824 | -43.361698 | 2026-08-08 00:12:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 325f2b62-d920-32ee-991d-a08b08c1b0c6 | -18.334299 | -43.919201 | 2026-08-08 00:12:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3227ef9-2931-3c1d-8c1a-d12f5943c9e1 | -9.4728 | -40.358501 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6d5e7298-5c31-3b18-984f-3eb82edeb5d3 | -6.9113 | -41.970901 | 2026-08-08 00:12:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99e38210-cb4d-337f-b7bf-dc9114a09f4e | -4.2566 | -48.175701 | 2026-08-08 00:12:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b45757d-508d-3cf8-9b49-824eabe2eba1 | -7.3497 | -45.375099 | 2026-08-08 00:12:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bba0b66-c729-37ae-a7d2-f379ed23cb28 | -6.946 | -41.941502 | 2026-08-08 00:12:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1c9f834c-6d5c-30aa-a3ac-cc8ba66bff3d | -5.5203 | -45.779301 | 2026-08-08 00:12:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d900735d-8acf-35de-9970-1aef64c0c034 | -7.1822 | -42.3489 | 2026-08-08 00:12:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cfa8dc9e-9fdf-3e50-82e3-d55fb58b3139 | -7.3616 | -45.382401 | 2026-08-08 00:12:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 398c12aa-e800-32f6-b567-79b2609965fe | -9.3818 | -40.3209 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1c0c5972-7b08-3f01-81cc-4ba9df958105 | -6.9082 | -41.9571 | 2026-08-08 00:12:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f652a00e-dea8-3301-8cca-107b09ce92f9 | -6.9204 | -42.421799 | 2026-08-08 00:12:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0c005f53-c916-315d-a9c7-bf4668b5fb24 | -7.1552 | -44.070999 | 2026-08-08 00:12:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80882ffa-526f-31ca-9150-42cebc5081aa | -13.7028 | -43.8615 | 2026-08-08 00:12:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2850c4e6-02bb-30ec-80da-c4b6b24b06b0 | -12.3519 | -48.1996 | 2026-08-08 00:12:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 812fa4fe-2176-303b-90a4-5029ee5feae2 | -6.9865 | -42.898998 | 2026-08-08 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a50c0d98-25ee-3c25-86e6-bfddc290819e | -11.0396 | -44.286098 | 2026-08-08 00:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bcddf2bf-8c23-3b5a-91c5-27f2fb5ae8a5 | -13.3911 | -41.345798 | 2026-08-08 00:12:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5ee50dec-8d2c-3f51-b052-c77cdb9e7096 | -11.1513 | -45.9333 | 2026-08-08 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47a9c40e-91c8-318c-8008-186a198abeae | -11.8868 | -40.963799 | 2026-08-08 00:12:00 | METOP-C | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5b071485-35dd-3e4e-b81c-44b605d7a1c6 | -20.358299 | -41.166199 | 2026-08-08 00:12:00 | METOP-C | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1d80bde-8686-3823-abb5-f4042d0fee4d | -8.1183 | -45.894901 | 2026-08-08 00:12:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b65f805-0b46-3764-8f4b-796687c6a23a | -9.629 | -40.5919 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 74df1600-b174-3330-854f-c1fa1e8ea73c | -12.5297 | -46.950699 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb974091-a7c4-3e52-ae9d-f7c39db86a09 | -7.0393 | -45.549801 | 2026-08-08 00:12:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75820f56-4995-33c9-8cc7-0e63e5324401 | -16.142 | -43.551498 | 2026-08-08 00:12:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 108b12b5-d234-3bb1-a3f3-7ec87484c9e5 | -6.9897 | -42.913399 | 2026-08-08 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f63d9b4c-a963-35dc-9dec-0238feaef934 | -7.0372 | -45.540401 | 2026-08-08 00:12:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12e4c3e4-4627-3f58-b834-cc3272853b5b | -10.2692 | -45.8153 | 2026-08-08 00:12:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43f94270-61e8-33e5-b7fe-1350fa5b57bf | -11.7958 | -40.925301 | 2026-08-08 00:12:00 | METOP-C | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aef95afd-8805-3517-ad02-5547b379ee2b | -11.707 | -50.1189 | 2026-08-08 00:12:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04692aa1-183e-377e-ad04-5b91bd96cdc6 | -4.161 | -48.7617 | 2026-08-08 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c3f345-3722-31f4-8017-99f2c8f7f9a4 | -4.4569 | -47.924801 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f59d610d-daea-3922-bf73-a7abb9e5a00e | -3.9679 | -48.119999 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d64ed33-3fab-3a76-ba98-191b94a52a55 | -6.7165 | -48.119202 | 2026-08-08 00:12:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1dcb11-6cc7-38a3-82b8-eba59d97b9ae | -6.9752 | -41.48 | 2026-08-08 00:12:00 | METOP-C | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19197557-2f09-362a-9c84-33b8016a46a8 | -15.9208 | -43.517799 | 2026-08-08 00:12:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9f93ae5c-31c0-3c81-9052-f3ea0b9447f3 | -9.4744 | -40.365398 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 463d2c4b-00fe-3392-936f-f04b594e607a | -12.5436 | -46.9189 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1887cae0-29de-3c00-aadd-af2e267c91b6 | -6.918 | -41.954899 | 2026-08-08 00:12:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bd838e7c-391f-3239-8594-5abb81f45159 | -4.2719 | -48.198898 | 2026-08-08 00:12:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2081d4a6-e9fc-3a1d-ab11-43df94d5dafd | -4.2691 | -48.186199 | 2026-08-08 00:12:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42cf2cfc-dc80-301f-8357-881e5df8a0eb | -11.7943 | -40.918301 | 2026-08-08 00:12:00 | METOP-C | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f5872852-4fac-3dc1-a51e-68192f63c940 | -16.1401 | -43.541801 | 2026-08-08 00:12:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 60976ca1-daf2-3327-bcdf-481d6b0374bc | -4.2593 | -48.188301 | 2026-08-08 00:12:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
