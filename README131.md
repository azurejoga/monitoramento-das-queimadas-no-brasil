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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e219c766-46cb-3674-a03c-1a08f0f52eec | -1.5163 | -52.2106 | 2024-11-10 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 776bcb23-dbc5-31f2-a2de-b5b20afc9eee | -3.9955 | -46.3981 | 2024-11-10 14:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2538ebf2-6c05-3e8c-82ad-44522bef8b34 | -3.9953 | -46.4203 | 2024-11-10 14:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 27666c65-1071-3e38-8445-f0bace2f8995 | -6.2377 | -45.6809 | 2024-11-10 14:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e954dd11-f771-3908-be50-c46ea64f4d29 | -2.4377 | -45.991 | 2024-11-10 14:00:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0aafbd84-eaf2-374a-8f79-8aee404d4907 | -4.1244 | -43.6064 | 2024-11-10 14:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cfa631f5-dc91-30b7-80d9-3f6abf7f1818 | -5.2848 | -43.4179 | 2024-11-10 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6512b832-8152-354b-afb6-d895aca513f8 | -8.4421 | -39.5053 | 2024-11-10 14:00:00 | GOES-16 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 98.8 |
| d8fa31ea-6ec1-3dd7-888f-d876be40f442 | -5.9101 | -42.6676 | 2024-11-10 14:00:00 | GOES-16 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| d735f651-e8b9-354e-8e71-c48d775c9ec2 | -4.3979 | -41.8987 | 2024-11-10 14:00:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| a0fc1da5-c4a6-3ed6-a7e1-0acecc4dd173 | -3.9486 | -48.1291 | 2024-11-10 14:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 88292608-e57d-30a6-86d6-84b9b77d7a04 | -4.0915 | -49.111 | 2024-11-10 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| e0586f4a-dce5-361a-b0b0-2c961c64121e | -5.4689 | -41.656 | 2024-11-10 14:00:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 3b3c2ef3-9a8e-3579-b4b5-1e0016900a20 | -3.8876 | -49.1407 | 2024-11-10 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 87e5e374-63b8-3219-b076-2d9afc693b3f | -2.418 | -46.3024 | 2024-11-10 14:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 99050459-b57b-3ac1-a56f-82bbd1fc121a | -8.84 | -47.7 | 2024-11-10 14:00:00 | MSG-03 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d1413bf-4ef1-3724-997a-64be156b9afc | -8.42 | -44.12 | 2024-11-10 14:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a363cec-302d-3642-89ef-aa8499e6246a | -4.1 | -43.95 | 2024-11-10 14:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 177b2403-8424-3ce7-8644-dbb39ce3f0f2 | -1.5 | -54.31 | 2024-11-10 14:00:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fee09c1-b7f8-3c0c-bbf2-86f9663c6e13 | -4.07 | -43.91 | 2024-11-10 14:00:00 | MSG-03 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a9a75e4-1313-361a-907a-76215f20509c | -4.07 | -43.95 | 2024-11-10 14:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5a13fe4-a372-3115-8fb3-39465b9de3c6 | -5.57 | -43.97 | 2024-11-10 14:00:00 | MSG-03 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cceda46e-d241-3062-a05e-5e24d617307c | -4.45 | -44.62 | 2024-11-10 14:00:00 | MSG-03 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff911d56-48fa-38f5-82d4-137ccbfbfef6 | -4.1 | -43.91 | 2024-11-10 14:00:00 | MSG-03 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1176ca7-a11e-344a-afa8-7fbda5a2c8db | -8.39 | -44.12 | 2024-11-10 14:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| add896cd-5918-3ab8-ba15-2326963facaa | -6.14 | -38.89 | 2024-11-10 14:00:00 | MSG-03 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3ff8ac5d-2f8b-36e8-8176-14109929b486 | -5.57 | -43.92 | 2024-11-10 14:00:00 | MSG-03 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69d148da-01bb-38e3-8abf-50b397b59028 | -6.11 | -38.89 | 2024-11-10 14:00:00 | MSG-03 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 424258ce-e1bf-353a-aaea-fa9b8bbae79b | -3.14 | -50.42 | 2024-11-10 14:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91e1eda8-e046-31d1-acd5-b0b995a01681 | -8.39 | -44.16 | 2024-11-10 14:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a263d79-4a82-3471-9af5-8cff8e26caf2 | -2.6388 | -46.7597 | 2024-11-10 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 259ec368-4e1b-30fa-a5c1-d2b66e86fbe1 | -2.0477 | -46.1125 | 2024-11-10 14:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c5cd29fc-9e16-3ab7-b875-e8bf1e76ee48 | -2.3076 | -46.0391 | 2024-11-10 14:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a73e31f7-710a-3400-80e3-9a22fc74076a | -4.3724 | -48.5844 | 2024-11-10 14:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fe68734b-afe4-30ec-b92c-831f5c40b5e7 | -2.0664 | -46.0899 | 2024-11-10 14:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 7700c91a-2f06-3c76-b640-1e059cbd91a6 | -2.0769 | -48.8129 | 2024-11-10 14:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 44af62ef-b794-3476-b8a6-476f30d18fb9 | -2.326 | -46.0831 | 2024-11-10 14:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4218cdab-deb9-38f6-bb6c-bebd12f77205 | -2.3792 | -46.8112 | 2024-11-10 14:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 65ea3216-8311-3c3e-8d18-9b535e4b33b0 | -5.7346 | -43.3849 | 2024-11-10 14:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 95554bdf-a9be-3b38-9b7f-0f8a2c32a43d | -8.3775 | -44.1617 | 2024-11-10 14:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 29e7d07d-f6e6-36fb-83e7-e11d65d0999a | -3.9485 | -48.1508 | 2024-11-10 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| fa94d341-45a4-3bc6-94d4-2d6419ca1068 | -0.4503 | -52.0355 | 2024-11-10 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 59.4 |
| aaa9b12c-6fef-331a-aa15-244fe5e5bb5b | -5.7287 | -41.9942 | 2024-11-10 14:10:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| b2d7a066-fbb3-3ac7-81d7-9732bc60f665 | -5.1314 | -41.6096 | 2024-11-10 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 233c7b8f-287d-3203-a74b-53cea2f41122 | -3.2244 | -53.0524 | 2024-11-10 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 745073e4-5897-3844-91dc-9b400567de58 | -4.0915 | -42.9329 | 2024-11-10 14:10:00 | GOES-16 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e8df3514-81d9-322a-8383-bbf160bc3bde | -2.1021 | -46.532 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 1ea93c09-6a71-37a7-a0dc-dd4ee3f31f36 | -4.3979 | -41.8987 | 2024-11-10 14:10:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| f5c7f692-2757-356d-96c1-facd6d55682d | -6.2564 | -45.6795 | 2024-11-10 14:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ca9126c0-6619-3fb9-91d7-4dab4f8004c3 | -5.7659 | -42.0389 | 2024-11-10 14:10:00 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 237abb28-2e7c-3330-a7ab-65ac7f985083 | -8.3778 | -44.1386 | 2024-11-10 14:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 223.9 |
| ed1afb27-bc9a-35f9-a396-654e037141dc | -5.1128 | -41.587 | 2024-11-10 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| c53155d1-8cc4-3321-8d42-a8d898b0f681 | -4.1565 | -44.4099 | 2024-11-10 14:10:00 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8152da5a-4f28-38f0-9a71-57e81078063e | -5.5795 | -41.8868 | 2024-11-10 14:10:00 | GOES-16 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 053ffb7d-ff17-30e3-961a-a9e451b7aee4 | -2.4191 | -45.9915 | 2024-11-10 14:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 345f680a-60a0-3d9d-b47b-a7cd207be3b9 | -2.2502 | -46.5723 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 09c65fe5-db0b-3273-849e-e6349431bd88 | -6.1366 | -42.5544 | 2024-11-10 14:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 9fac9c61-06ed-381e-a470-8b51bd417f37 | -5.7789 | -42.6546 | 2024-11-10 14:10:00 | GOES-16 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 9fc9b2ee-f85d-319c-8e67-0b1f6624f33e | -2.5119 | -45.9888 | 2024-11-10 14:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 12bac5df-12d7-38eb-8a09-416da02fd903 | -5.2483 | -48.0857 | 2024-11-10 14:10:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e102eb9b-7cd9-3fce-8a4e-76d27365015b | -2.1023 | -46.4657 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 3adfa6e7-4f20-30eb-aef7-ac25d3270215 | -1.718 | -52.4736 | 2024-11-10 14:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8ed497fb-9505-3ae2-b84b-149c98fee09d | -6.3772 | -44.7868 | 2024-11-10 14:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a276589b-9388-325b-9403-11e647bbc210 | -5.9919 | -45.9906 | 2024-11-10 14:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 6ba3dc42-25f8-3be9-8c77-606eb1b0d395 | -4.1244 | -43.6064 | 2024-11-10 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0958dba4-db5b-3911-b7f3-4befc3310823 | -5.2418 | -41.8649 | 2024-11-10 14:10:00 | GOES-16 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| bba2d54d-2bdd-3c5c-a398-34144f46f7e8 | -6.1363 | -42.578 | 2024-11-10 14:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 235.9 |
| 375be270-ce1c-3c03-98c9-3c770c21f00e | -1.9726 | -46.4467 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 09eaacbb-dda8-343a-a0e6-783f7e174992 | -2.931 | -52.7753 | 2024-11-10 14:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ece26bbc-d098-38ca-b729-65627dadb047 | -3.5954 | -44.7792 | 2024-11-10 14:10:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d1eb15ba-da9f-3fea-a593-c37d078c9a08 | -6.3689 | -45.6483 | 2024-11-10 14:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 152f643b-10bc-3dd3-ad49-6f25a26d5c39 | -2.0842 | -46.3334 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3ae57cf2-9d59-369e-9a68-f72d153d027d | -2.2619 | -48.7445 | 2024-11-10 14:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ada2d213-ea64-3c9b-8325-e75ec6e5e788 | -5.7661 | -42.0151 | 2024-11-10 14:10:00 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| b478928d-d199-32f9-b47b-2aab1dd94d04 | -1.5163 | -52.2106 | 2024-11-10 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b1201998-0c39-396e-bfd5-bd9bdd57a28e | -2.9168 | -46.7948 | 2024-11-10 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 68bae88b-571c-3157-9e4f-127c14bf9f13 | -5.4544 | -43.2893 | 2024-11-10 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5e99af1e-1b96-3f7d-adab-141f19603d11 | -1.6923 | -47.3963 | 2024-11-10 14:10:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 872af399-2a80-3f36-a556-46d50dabd8be | -5.7146 | -43.5261 | 2024-11-10 14:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6d7b8030-249a-3940-a872-454483b8905c | -3.2243 | -53.0727 | 2024-11-10 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 833fe4a1-8fcb-37c1-a3aa-56baecaee103 | -5.7473 | -42.0166 | 2024-11-10 14:10:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 8fcbdf11-200d-3f45-bb4a-3ccf8c1ddb5d | -4.0915 | -49.111 | 2024-11-10 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 8c94c4c1-c55a-3d69-b5f8-771df9170910 | -4.0913 | -49.1323 | 2024-11-10 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ef499c98-f2ef-3b36-8ce0-50e762eb3e06 | -3.5589 | -44.6445 | 2024-11-10 14:10:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 0c68b940-0e2e-3289-9e34-5650596ac702 | -2.0768 | -48.8342 | 2024-11-10 14:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 485b7a3f-f510-34a7-94f3-3b2f4b85d3de | -2.5118 | -46.011 | 2024-11-10 14:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6d636128-4ab0-32ff-97fd-0912cb987591 | -5.2848 | -43.4179 | 2024-11-10 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| bac00806-e50c-395c-a809-bc211e9eb893 | -2.0292 | -46.113 | 2024-11-10 14:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a68ed294-c8e2-35de-83c1-1f16d95aed1b | -2.4192 | -45.9692 | 2024-11-10 14:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 65bb91e3-4864-30eb-be21-cf4b7fbbbfb5 | -5.2485 | -48.0641 | 2024-11-10 14:10:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 507e9256-0536-3425-b4dd-7205b3eb9742 | -1.9911 | -46.4463 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| ab4b84d2-2933-30ac-927a-b8c658bd22c0 | -5.4359 | -43.2673 | 2024-11-10 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9011a467-ac06-3d79-ab69-680496d2cbbb | -6.1361 | -42.6017 | 2024-11-10 14:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| dd12b630-1183-3c6c-a843-0d31918c126a | -4.1099 | -49.1315 | 2024-11-10 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 198.8 |
| 0ca9f1c5-3447-3f3b-9a5b-8809bf091e09 | -2.4365 | -46.3019 | 2024-11-10 14:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| da14e30f-7c29-3ec0-a956-013f192b980b | -4.1057 | -43.6074 | 2024-11-10 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ae4917c8-c6bd-3a59-b9d4-ef8233392a6d | -17.293 | -57.5062 | 2024-11-10 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| f1a6e255-57b8-3d6b-ad93-feed46585d28 | -6.2377 | -45.6809 | 2024-11-10 14:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3026d059-48a2-3ee5-ae23-a4276d3aa0a8 | -2.4365 | -46.3241 | 2024-11-10 14:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 62d20947-22ec-3885-962c-cefa9f75ec62 | -2.6387 | -46.7817 | 2024-11-10 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |


[Clique aqui para ver as próximas entradas](README132.md)
