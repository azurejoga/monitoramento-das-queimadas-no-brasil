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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f1fe39a-e862-3a71-a15c-c5b44c0b6531 | -10.8022 | -50.6752 | 2025-09-16 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 478c4495-dbf0-306d-9a84-55661a53622e | -10.7201 | -44.7541 | 2025-09-16 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5f8589c6-a113-32dc-b3c7-5116ee3dec04 | -13.2224 | -47.2871 | 2025-09-16 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ed672ac8-f97b-3121-a839-11037878eb87 | -12.7682 | -47.9568 | 2025-09-16 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 670e583d-0ca6-364f-835e-81ea85861639 | -10.7201 | -44.7541 | 2025-09-16 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 0dcb660e-5ef4-364b-93c2-dc3a68a3e799 | -10.802 | -50.6965 | 2025-09-16 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5261003b-1e40-3f62-aff5-496520d949d2 | -10.8022 | -50.6752 | 2025-09-16 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5f55e052-1ba0-3207-af41-4b9f0afc91ac | -17.595 | -46.6882 | 2025-09-16 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0535e4c2-4763-37ae-819d-ed84c1ff9151 | -9.7495 | -55.379 | 2025-09-16 02:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c63cc79d-28d6-3994-9669-b7db5b1c1d86 | -17.5956 | -46.6648 | 2025-09-16 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d0c02610-b2b8-3e8a-9949-bd70f9915cb5 | -17.081 | -45.8162 | 2025-09-16 02:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b9cf5352-c528-30a8-a92e-eff06ddeb001 | -11.1299 | -45.3426 | 2025-09-16 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ec8f6020-7e3f-334c-8aa9-56402ec71ac3 | -10.783 | -50.6985 | 2025-09-16 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| c98fc65d-48b7-31d2-9465-1e522561a5f5 | -13.2031 | -47.29 | 2025-09-16 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 02644471-531d-3328-a33d-1a01b1f2b512 | -7.4503 | -46.1647 | 2025-09-16 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 45318c36-30c6-3b4c-be4d-19b1ed769a8e | -14.8214 | -51.6577 | 2025-09-16 02:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 87f89162-d7c0-3331-9402-eba5a31a65a5 | -10.7833 | -50.6772 | 2025-09-16 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9e82fcac-c734-3ef2-856e-62ddd0dfd8ba | -9.0485 | -44.8477 | 2025-09-16 02:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5f3b092c-0cba-37e6-8bab-f773d7ed185b | -10.7201 | -44.7541 | 2025-09-16 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 9a959732-2658-3e6f-afa1-5a69c3b89c8c | -11.1299 | -45.3426 | 2025-09-16 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 773be219-5b10-32f3-9218-6fc5e5e57fbe | -10.783 | -50.6985 | 2025-09-16 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 2f43be77-0680-3a3a-97fe-590c047046b8 | -9.0488 | -44.8247 | 2025-09-16 02:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 55ed78df-ec06-39e9-8777-dfa8f7a5839c | -12.6164 | -45.7452 | 2025-09-16 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 20988bf6-5d05-3ac4-a165-46a497de4d2f | -10.8022 | -50.6752 | 2025-09-16 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 12486c72-aa60-30c7-b9f9-e2396e0093f1 | -16.0192 | -59.2427 | 2025-09-16 02:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d190ff81-333e-38b1-87ff-307aa4624e50 | -12.7678 | -47.9791 | 2025-09-16 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 860e09aa-19f6-399e-98e1-373d765df6a8 | -9.7495 | -55.379 | 2025-09-16 02:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 6a5bf8d0-ec5f-3ad6-988e-f4ca1ff59e69 | -17.5956 | -46.6648 | 2025-09-16 02:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 250.4 |
| 15c94c88-0655-31b0-a6a7-0b3ef65ce8c1 | -13.2031 | -47.29 | 2025-09-16 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 570aa58b-39e5-344a-8be9-f9a60a315018 | -12.7682 | -47.9568 | 2025-09-16 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 1341f33b-e14e-3d12-9a66-781570c64e4d | -5.7858 | -43.9378 | 2025-09-16 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| e3822d7a-253e-385d-9629-5b1a4ff3899f | -10.7115 | -46.488 | 2025-09-16 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8a4a6cdf-03da-37a5-b5ba-2d2930d86fc5 | -10.7306 | -46.4856 | 2025-09-16 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 195d365c-1478-3b26-b6f3-b33c848b9281 | -14.8214 | -51.6577 | 2025-09-16 02:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 93f1a358-bfc0-36a2-afad-4f4175e98458 | -10.802 | -50.6965 | 2025-09-16 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 200243c4-1aab-3ff3-818a-7e1a070f3690 | -9.0485 | -44.8477 | 2025-09-16 02:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5ffe20be-60ee-3478-9b5f-130bb68874ed | -17.6155 | -46.6607 | 2025-09-16 02:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 4ab49873-0135-3dda-b3b5-ac9e0230c8e8 | -14.9181 | -51.6657 | 2025-09-16 02:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| f557ff86-3801-3cfc-8f9c-4a49c043f3d3 | -9.0674 | -44.8455 | 2025-09-16 02:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 2e242f0e-73f9-3c7f-b200-1a9c584aebe8 | -15.9998 | -59.2446 | 2025-09-16 02:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9391f00e-e8ba-34aa-a0ca-5bd3a53fc747 | -17.595 | -46.6882 | 2025-09-16 02:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| eac32ca2-34e0-3c20-ab8f-1f117a7e4489 | -10.7392 | -44.7515 | 2025-09-16 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 88b7f888-2333-3471-a943-eb82efa69ef0 | -10.7833 | -50.6772 | 2025-09-16 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d39fda6d-91fb-31ed-8df4-edb73c5d9851 | -5.7856 | -43.9609 | 2025-09-16 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 16c451db-2e00-30a1-bbec-c60e68281152 | -9.0485 | -44.8477 | 2025-09-16 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 688d54f2-8a47-33a0-aab4-3503d3e962b1 | -10.8022 | -50.6752 | 2025-09-16 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 254.6 |
| 85851e02-e0af-3df2-a869-39af13a223c9 | -9.0863 | -44.8433 | 2025-09-16 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| f46fe9ff-626e-34f2-88b3-25381fd96e1c | -9.3017 | -65.5959 | 2025-09-16 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e81bf76e-1922-3088-82ff-8c430e772111 | -10.7201 | -44.7541 | 2025-09-16 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 3f461f8b-84d9-3e2b-bbca-2034d65808bc | -3.212 | -47.1357 | 2025-09-16 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e8bdf3f4-1d81-39c8-a437-92d9197e4c1f | -12.7682 | -47.9568 | 2025-09-16 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d78cedd5-64b0-36fc-9c5a-eed2eb6590f3 | -10.7392 | -44.7515 | 2025-09-16 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 2f02fd00-a4a9-3a8d-abe0-cd638bbf5507 | -11.1299 | -45.3426 | 2025-09-16 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a1e721e6-2f54-3235-bc3d-bed8fc8993d9 | -17.595 | -46.6882 | 2025-09-16 02:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 80ee12b8-58c0-3cc5-9366-95e7eda90f81 | -10.7115 | -46.488 | 2025-09-16 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5ba465ae-1042-32dc-a1cc-acbc3f69e6ab | -9.1053 | -44.8412 | 2025-09-16 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 174e0420-a3e6-324f-9026-990ee4cadaa6 | -17.6155 | -46.6607 | 2025-09-16 02:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 446f5d7f-aee7-3536-936e-d516d4392dc5 | -10.7644 | -50.6792 | 2025-09-16 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 72cae2f7-e557-3f3d-8520-3844a44d2aa6 | -10.802 | -50.6965 | 2025-09-16 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 29f18a71-783c-321b-b7e1-f9c4b58f83e1 | -10.7833 | -50.6772 | 2025-09-16 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 387.4 |
| 56065e11-808f-33c8-8de0-246d3451d6f7 | -15.8371 | -53.4741 | 2025-09-16 02:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| bc18e004-f8b1-3b34-a316-9717884a6b0e | -10.783 | -50.6985 | 2025-09-16 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a3bc386f-07cd-305f-a476-bfe0758bc3dd | -9.0488 | -44.8247 | 2025-09-16 02:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 087ce310-03b1-32ab-bcab-8358d3e79bdd | -10.7836 | -50.6559 | 2025-09-16 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a2ea1b69-ab1f-3cb1-b5a1-632d4132e379 | -22.5787 | -44.7284 | 2025-09-16 02:20:00 | GOES-19 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 4b7f32a2-bc3b-3a5b-b51a-414652c81a9c | -15.8176 | -53.4767 | 2025-09-16 02:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 51fa4e2f-e5b0-398d-9296-fd859a278e1e | -17.5956 | -46.6648 | 2025-09-16 02:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 272.3 |
| c431cfd5-fbcd-3289-8d6c-414d840bb887 | -17.5956 | -46.6648 | 2025-09-16 02:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ad453708-c447-316a-87cf-b7cce97f1fb5 | -9.0485 | -44.8477 | 2025-09-16 02:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 212db738-fe26-3ee0-9be6-ba1631e96402 | -10.7205 | -44.731 | 2025-09-16 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3aaac396-fec7-32c0-ac8f-e913ebf7ef31 | -9.3017 | -65.5959 | 2025-09-16 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c82115eb-bfa9-3e06-ada2-2e6d20f10a1b | -10.7201 | -44.7541 | 2025-09-16 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 271.1 |
| ccbc29df-ecf1-3f88-a93a-682f6503484a | -7.1318 | -47.9801 | 2025-09-16 02:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b1ab5bc6-84ca-359c-95d1-8f2613a2701d | -11.1299 | -45.3426 | 2025-09-16 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9e30aa24-61d2-38fc-b700-620421bddf0d | -14.9185 | -51.6442 | 2025-09-16 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| bf7c2fc4-17a2-33e5-9bd1-7e7372f55df4 | -10.7197 | -44.7773 | 2025-09-16 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0228530b-12e7-3756-9623-17b22519f43b | -16.0192 | -59.2427 | 2025-09-16 02:30:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| cc1c7389-ff79-3e11-9c66-89329bd397ec | -22.5787 | -44.7284 | 2025-09-16 02:30:00 | GOES-19 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| d1ff1692-1892-3122-9df8-8bc62c557ea1 | -7.1505 | -47.9786 | 2025-09-16 02:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 7333820b-c91d-3cee-ab35-0a7167343610 | -15.8624 | -59.3779 | 2025-09-16 02:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4efcc8b4-0380-37e4-8d46-d99080f870e0 | -10.7115 | -46.488 | 2025-09-16 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e0d3bc37-8d5c-3236-85b4-72f19e567167 | -9.0863 | -44.8433 | 2025-09-16 02:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 12615883-ab96-3722-92b9-c20f060b046b | -14.9181 | -51.6657 | 2025-09-16 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| dbec068e-262e-33e3-95df-5d66e9e61a64 | -3.212 | -47.1357 | 2025-09-16 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7b8f9348-15f8-35fa-a2f7-8e7efcc42562 | -10.7392 | -44.7515 | 2025-09-16 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8d125565-4359-32db-be32-19b66aad0a47 | -9.1053 | -44.8412 | 2025-09-16 02:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e5d552c2-de96-3ad6-9073-ef8d64b14a3c | -9.3202 | -65.5953 | 2025-09-16 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e21537c9-bc8b-31ec-b4db-2a2afc0923c5 | -10.7115 | -46.488 | 2025-09-16 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9d5e951d-fc25-3f28-9b46-fbbdf0227ba4 | -14.9181 | -51.6657 | 2025-09-16 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9d2b4c25-b705-3551-9274-f0f1349f34e7 | -17.081 | -45.8162 | 2025-09-16 02:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 43063fd4-a91c-3280-9584-92bf367afc7f | -5.7858 | -43.9378 | 2025-09-16 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8e5239a7-f14f-3dec-b26c-76c2bd524e5f | -16.0192 | -59.2427 | 2025-09-16 02:40:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 58bdefe8-29be-357e-b027-b69f9fe17089 | -10.7836 | -50.6559 | 2025-09-16 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 5dc2fd94-04e8-3361-8d27-d01e69f66392 | -10.7205 | -44.731 | 2025-09-16 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c03887ea-0210-39b3-89fd-93a9b2434283 | -7.1318 | -47.9801 | 2025-09-16 02:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 44eab744-de2f-3bfe-a6f3-50fda7bab835 | -10.7306 | -46.4856 | 2025-09-16 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6fe52e02-a5ed-3d70-815f-d8d5fc55d1a4 | -10.7833 | -50.6772 | 2025-09-16 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 0b0ca316-b352-3ce3-b74e-b9d7384d89a5 | -10.7201 | -44.7541 | 2025-09-16 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 203.7 |
| d5cc24a6-fe52-3b41-90ac-721aa06ba3aa | -10.8022 | -50.6752 | 2025-09-16 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 95f11b08-ec99-3714-9d01-7a819f20ff54 | -10.7392 | -44.7515 | 2025-09-16 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |


[Clique aqui para ver as próximas entradas](README5.md)
