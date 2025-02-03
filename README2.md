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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 850b34cd-246f-3e62-a935-e348cfe78968 | 4.43208 | -60.72502 | 2025-02-03 02:06:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| cdae2e20-2c84-3653-8d73-9d264479b00a | 1.9419 | -60.3827 | 2025-02-03 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| daf594ea-a56a-3a87-8079-fe2a84a31553 | -7.87935 | -35.20795 | 2025-02-03 03:06:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95c20df4-47a4-3526-9435-5d2ebb885f6d | -7.87728 | -35.21124 | 2025-02-03 03:06:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42e44504-0ac1-3ff6-9264-dd1c0e9adb2f | -7.87877 | -35.21123 | 2025-02-03 03:06:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6eb70a0c-66f5-323a-8d7b-64b5260c4d80 | -7.87788 | -35.20797 | 2025-02-03 03:06:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 48fc6670-83f6-3a59-a1cb-48dfaa1cacbb | -7.395 | -35.23506 | 2025-02-03 03:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 55c6874c-2e48-3891-b618-f6e81dc0e6d6 | -7.39432 | -35.23919 | 2025-02-03 03:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 52806293-b8f4-387a-8a29-db7db810291a | -7.79965 | -37.9208 | 2025-02-03 03:27:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c6a02e78-3ef3-3d18-a151-16d00daba1c7 | -6.22491 | -35.4869 | 2025-02-03 03:27:00 | NOAA-20 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b03e74a-e2c0-3d04-9457-5d28241fb6be | -7.84291 | -35.20058 | 2025-02-03 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c60ff249-ebe4-3be1-a788-ff6040dab583 | -7.84357 | -35.19658 | 2025-02-03 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3df13056-6517-3851-8512-a7229be85281 | -6.66061 | -35.20682 | 2025-02-03 03:27:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2679d699-c7de-3786-8c89-2ae1cf7f1928 | -7.22511 | -35.78716 | 2025-02-03 03:27:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 48b1e371-af74-302b-adcb-f280256105ec | -6.22512 | -35.48835 | 2025-02-03 03:27:00 | NOAA-20 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb886809-bf72-3072-b6b7-76045376c91b | -6.3906 | -37.3963 | 2025-02-03 03:27:00 | NOAA-20 | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2aa8b192-a369-305d-bcf9-80acdfa501db | -7.45876 | -35.15828 | 2025-02-03 03:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 76914cef-4c88-34cb-8bcc-909645af32d3 | -7.2295 | -35.78341 | 2025-02-03 03:27:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20249536-ccc4-3f77-b959-e13ced1d804c | -5.25363 | -36.18747 | 2025-02-03 03:27:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 037a2a5f-6e2d-36a0-8882-45706d362252 | -7.03909 | -44.39738 | 2025-02-03 03:27:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a48e45f-2efa-3736-a180-079a1be93acc | -7.84002 | -35.19601 | 2025-02-03 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1bb6831f-ab9a-38be-b8c4-02d052ea0616 | -7.83936 | -35.20003 | 2025-02-03 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f746a344-932a-3961-952d-24b1b0273828 | -7.87415 | -35.21002 | 2025-02-03 03:27:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1e64df44-14a1-3ab8-b860-6ad8ab93e576 | -15.72413 | -41.7962 | 2025-02-03 03:29:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 23bc7c5e-84a4-3647-8975-e462aceba567 | -16.26388 | -40.06101 | 2025-02-03 03:29:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4782bdb1-8bbf-3611-8686-a148e2c73ba9 | -16.26803 | -40.06182 | 2025-02-03 03:29:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 28609e46-43bd-3327-8a90-7f2b4389a81e | -19.20637 | -39.71258 | 2025-02-03 03:32:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f1ea2ebb-1c34-32a7-82e5-e88a36666b29 | -21.65809 | -41.32595 | 2025-02-03 03:32:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 96ab7ae1-a3fa-3452-84cf-9fa8fa2caa5d | -20.19049 | -40.81291 | 2025-02-03 03:32:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1ad08933-46c2-3f5b-bb08-ea927e0019d2 | -18.04014 | -39.92694 | 2025-02-03 03:32:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 434653c6-b92a-3edb-a396-7e7bded37d5c | -19.20595 | -39.71018 | 2025-02-03 03:32:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 747a4626-d838-348e-b80a-b5cc4b5f3780 | -17.65703 | -40.74592 | 2025-02-03 03:32:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f802bd26-7147-329c-a89a-8befe228aa5e | -22.90245 | -43.75254 | 2025-02-03 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 32915435-9aba-32f5-bbd0-2db37595b41c | -19.83701 | -40.08036 | 2025-02-03 03:32:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 849aae29-1202-3d28-ba7b-55ee03a256dd | -29.62739 | -51.9745 | 2025-02-03 03:34:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dc0d4c33-5b9e-3211-8975-139c28de03f5 | -29.62903 | -51.96855 | 2025-02-03 03:34:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f312d4e1-91c1-39c8-a873-728e34803351 | -7.04136 | -44.39616 | 2025-02-03 04:21:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4792fdde-d5ed-301a-b5e5-18aff94b3ca1 | -7.67105 | -46.10432 | 2025-02-03 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e564f2ca-b0c7-3c05-9d81-130e69341f8b | -7.04466 | -44.39668 | 2025-02-03 04:21:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0d2865c-8bc3-394b-b0fd-a85dfd279626 | -7.68452 | -42.98964 | 2025-02-03 04:21:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 355cd4c4-e2f9-346b-a44e-bbd5f1f020a8 | -7.68397 | -42.99332 | 2025-02-03 04:21:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d28d8cb4-29ab-3ceb-b41c-342780397829 | -7.68793 | -42.99017 | 2025-02-03 04:21:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4c6d5dc3-ded8-3f71-837d-ba6fd34bcdab | -22.6756 | -42.85289 | 2025-02-03 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 52c2974d-d2a9-3fcb-877e-1e0319fa1606 | -22.67968 | -42.85345 | 2025-02-03 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 53db6b71-48b4-39f1-a071-c378152272fc | -22.67513 | -42.85677 | 2025-02-03 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 45cf301a-6c9d-3898-abde-498e36a0f94a | -29.52624 | -50.63869 | 2025-02-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e8f0da8a-fd3a-3f58-985b-d9265d0f7a98 | -28.58623 | -49.44287 | 2025-02-03 04:25:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d2196670-6b1a-393c-b9f3-aa51d80b9b1d | -19.59468 | -55.30786 | 2025-02-03 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9eb4b07c-cfe1-3fa6-a760-fa036eebbe79 | -30.19132 | -55.26997 | 2025-02-03 04:25:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 9d6b4cef-69b4-3c3a-b94b-c4bec32ba532 | -29.74489 | -51.18434 | 2025-02-03 04:25:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 89f9dab7-d7c8-3a43-af3c-280349961122 | -30.15092 | -52.02565 | 2025-02-03 04:25:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5e83f8a8-0245-3bc4-aef6-4d8bae6dfd0c | -19.83987 | -40.08252 | 2025-02-03 04:25:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 49df2652-94e8-3281-94c9-f3709dd61684 | -29.63214 | -51.96731 | 2025-02-03 04:25:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 99e785c5-d520-31c6-b14b-6d9a2af99f10 | -29.62877 | -51.96657 | 2025-02-03 04:25:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 46d1c7ce-7ce2-30c8-b96c-007366729770 | 0.728 | -59.41231 | 2025-02-03 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0bd356f6-26d5-3b3d-8aca-0ff49903caef | 4.43095 | -60.72656 | 2025-02-03 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee46d4ea-00c4-3cde-bfa2-62b3b56a9bcd | 0.72237 | -59.41317 | 2025-02-03 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| df08fa2d-bc08-3f00-8320-ac1bc3c6ef3e | 2.88414 | -61.5774 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93dd15a9-d1e8-3c6e-94e8-7c1edbc92f77 | 4.43234 | -60.73626 | 2025-02-03 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 186ef7e9-f8fe-3fd5-b9e7-6f7e31b21639 | 2.88665 | -61.57154 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d2ed8c7-38f1-3621-b598-92a31db7592f | 4.43812 | -60.73061 | 2025-02-03 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8806563-7cfc-3547-a298-746e973eb6b3 | 2.8908 | -61.57644 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b999beff-88e2-3bb3-bd7a-bd13251d4b31 | 2.88748 | -61.57737 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d435da8-8ed7-340c-b710-e8fa0d847eaf | 4.10685 | -59.90096 | 2025-02-03 04:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c932f7d-5136-31f7-b9be-9d4e7228aabc | 2.88828 | -61.58298 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 810709f2-7672-3fd5-b7ed-1374d522a9bc | 4.11231 | -59.89569 | 2025-02-03 04:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7217eb8c-edb0-3304-9c26-865730d96e94 | 2.88498 | -61.58304 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29d8abbd-d8ed-3fe8-b38a-ed75ef618610 | 0.72297 | -59.41702 | 2025-02-03 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e6f48582-16b7-3efe-b22f-27947b2b95f9 | 2.88994 | -61.57069 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9fd6d651-3d4c-325c-bcef-65cb3a0e21c3 | 4.44468 | -60.73044 | 2025-02-03 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54fc078f-874a-31e4-941d-33c9428d718d | 2.89331 | -61.5706 | 2025-02-03 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4df42d5f-c968-3682-acfc-a023215471ab | -7.68388 | -42.98849 | 2025-02-03 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c0cd5d40-0e9d-3239-b1e7-26f5863e8bb2 | -7.68694 | -42.99166 | 2025-02-03 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a72435e5-9b77-38ac-9795-33b7cd3e42ab | -7.68182 | -42.99088 | 2025-02-03 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d96d9755-33b3-3ffb-b235-ebc7520f8f2d | -10.53239 | -44.92265 | 2025-02-03 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03acd0c9-51ba-340d-9733-63931793a9af | -7.68349 | -42.99141 | 2025-02-03 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f71824ca-3f22-3ed3-bdd5-28ed76bebfd1 | -7.68223 | -42.98797 | 2025-02-03 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d365cd04-e3ba-3223-a952-b54afe8096f3 | -7.68736 | -42.98873 | 2025-02-03 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 99b0bd5d-ff58-3552-a5d2-626f8096d978 | -22.20667 | -53.41151 | 2025-02-03 04:50:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 74282ee2-b912-325c-b25b-14222c0b78ec | -19.02394 | -57.62057 | 2025-02-03 04:50:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ca713da0-72b6-3af5-bf4a-c95040e05f63 | -22.0188 | -57.12081 | 2025-02-03 04:50:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ca87b6b-8c3a-3c12-a9e4-2fab636268cd | -29.62774 | -51.96804 | 2025-02-03 04:53:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 884c6109-9cdd-3b45-9326-7c833d4c18e8 | -30.19111 | -55.26698 | 2025-02-03 04:53:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 4d388d47-d7ae-37b1-b4cc-800a3850a0b2 | -28.58353 | -49.44304 | 2025-02-03 04:53:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4c92da56-982e-3baf-9428-1df2cfe2a184 | -30.19051 | -55.27116 | 2025-02-03 04:53:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 981522a0-bdf9-3415-b66a-7d333f12d76a | -29.63134 | -51.96973 | 2025-02-03 04:53:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 415cf742-7952-3be0-8840-d44f701d14ca | -29.94524 | -51.19414 | 2025-02-03 04:53:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| e18e3d26-36b0-340c-807e-9278b41974dd | -29.62745 | -51.96912 | 2025-02-03 04:53:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 9e54ffc4-1421-3921-af22-d812667e52dd | -7.67864 | -42.98932 | 2025-02-03 05:01:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 84281cd2-1170-31ae-a37e-ab2e09db8728 | 4.43604 | -60.73467 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1fa5c8d-660e-394f-a8e3-6fbfcc25da77 | 4.47038 | -60.76245 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74f8cb24-6019-3233-a166-a3e763b50fa6 | 2.88229 | -61.58099 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 212429bd-0ba0-332f-b289-170e87d5afe0 | 2.88293 | -61.58519 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 476d177a-41e0-3fc6-a74b-7b74e5724659 | 4.10924 | -59.89296 | 2025-02-03 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 591393f7-4603-3cff-ae2e-fc7c69e21cf3 | 4.1137 | -59.89564 | 2025-02-03 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| becdc368-25fd-38ab-a3e1-f319b4fba26e | 4.11321 | -59.89232 | 2025-02-03 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77601362-12ae-3cf4-9ab6-d5274a36c700 | 2.89042 | -61.57546 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b9d9b2a-7dd8-3449-922a-f58af7c4c142 | 4.454 | -60.76896 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abf9613b-c603-3ede-b2f4-cb0c5b20ad7a | 4.11022 | -59.8996 | 2025-02-03 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85f52930-19b1-3b26-92c1-226b0885d486 | 2.88914 | -61.56698 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README3.md)
