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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8abd78fc-10e2-351a-9e8b-2f0caaaee410 | -11.8221 | -45.1059 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 77863f7c-e60c-3bd9-a7b4-a5bad08513c7 | -8.4821 | -46.3136 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| dcd1e0e9-41d0-39c0-bb7c-3bfab11246a2 | -13.0939 | -47.9992 | 2025-10-07 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 288767e9-d5c1-346f-920b-ad6890e2e690 | -15.8091 | -43.7597 | 2025-10-07 13:30:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c44de426-4ffb-3279-a50f-dbb8cdebfc6b | -17.9778 | -45.0057 | 2025-10-07 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 973d43bf-08ca-39b1-9e5b-526e35898b17 | -8.9759 | -47.4864 | 2025-10-07 13:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a032aed0-aec0-3d94-84fa-df75256247a2 | -12.891 | -54.7577 | 2025-10-07 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 937.7 |
| ba2cbaf6-7560-35fa-b507-255c5d72d7ec | -11.0451 | -50.9047 | 2025-10-07 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3661e242-4d9f-36a2-9c87-2784eedc49e9 | -11.1644 | -54.8804 | 2025-10-07 13:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 262.5 |
| c6608a23-b85c-339c-89f2-2e14b9d7d51a | -15.6198 | -52.5715 | 2025-10-07 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 7623119c-1252-3ef0-b53d-47d9013844e9 | -7.7014 | -42.4043 | 2025-10-07 13:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 16090d4f-7439-391c-a491-8c2eff99e16a | -11.6859 | -46.3366 | 2025-10-07 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 18ebe3cd-1175-39c3-a65c-7bb1b3018b20 | -8.4522 | -47.2288 | 2025-10-07 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 53329f9f-8722-3727-9021-db48a14aaeab | -8.5393 | -46.2631 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| dd136d95-20f5-3824-b168-a82b74201c50 | -8.0946 | -47.2844 | 2025-10-07 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 483015bb-4dc2-3ce3-abd1-00bffe752747 | -8.8429 | -46.0969 | 2025-10-07 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 73b9609e-bf71-3c78-9c7b-3102e719daeb | -8.1618 | -43.323 | 2025-10-07 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 9ead2459-7f25-3ccb-85c6-3a5c463d62a3 | -14.7092 | -48.3766 | 2025-10-07 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 78a530ce-dfe7-3058-ab37-b244d0263656 | -14.5057 | -46.9242 | 2025-10-07 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e35d5858-08d1-3322-a922-90b327be5ee3 | -11.2433 | -50.2859 | 2025-10-07 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 899abeef-dbdd-33c7-b711-8ffa6d7d69cb | -11.0262 | -50.9067 | 2025-10-07 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 89a101f1-a74a-356b-8406-54bf03853404 | -18.9846 | -47.8282 | 2025-10-07 13:30:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 71a5560d-bb87-32b4-8b89-7bc459280a12 | -15.3742 | -47.2973 | 2025-10-07 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| d7eee1a5-6821-3dd0-b00f-a946efb06c2e | -8.5207 | -46.2425 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 485f8524-b830-3f7c-a009-6fef9240565d | -7.7885 | -44.5228 | 2025-10-07 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| fe4629c9-7120-3ccb-bd52-bba78d013b6d | -9.1528 | -49.9425 | 2025-10-07 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 1e84ef70-717c-35f4-8a1f-b10f313a7b98 | -11.8029 | -45.1087 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 61528664-e774-3eb0-9caa-b447d5c75f83 | -14.8641 | -51.4373 | 2025-10-07 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 695b5fd5-e38a-3600-a3b9-10343b5240f1 | -11.9515 | -46.4579 | 2025-10-07 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 96c0cb44-ea02-3d6c-940e-fc7ad6313fc8 | -10.9109 | -47.1129 | 2025-10-07 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 4c339091-e542-3c4b-81ae-59b173a5e5cf | -11.7837 | -45.1115 | 2025-10-07 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 15239c5f-1c0e-30f7-833a-0c40a56cbc6f | -8.9121 | -46.5829 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 0693674c-f181-3bb4-bcf5-6e6afea2ebb6 | -10.8919 | -47.1153 | 2025-10-07 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 3281776a-d163-34d6-8df6-2ae75113376b | -10.4245 | -45.3907 | 2025-10-07 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 231.5 |
| b8d705c7-4457-39b6-84fc-1c0021aa0705 | -8.8986 | -47.6483 | 2025-10-07 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 16efe96d-5da9-3d3d-bd5e-f11be9f8d548 | -18.2862 | -45.4348 | 2025-10-07 13:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 12df427e-b274-3fee-8569-461c941a7965 | -8.6521 | -46.274 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 4e91117c-2a35-395c-8272-9f47863d6a92 | -11.6855 | -46.3593 | 2025-10-07 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c163cc72-6e83-331d-8964-abf4395a2770 | -12.9619 | -46.808 | 2025-10-07 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9b38e40d-0439-3787-9daf-dc8f74d082be | -8.5007 | -46.3342 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 363c772b-fda5-3ce5-b744-5152250a332c | -12.4669 | -45.5155 | 2025-10-07 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 59818fd9-8dba-39e5-a386-cd2b28dba08e | -8.1882 | -44.2052 | 2025-10-07 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 27cb90d5-fa20-32c3-a166-f12a18e2de1e | -12.9103 | -54.7352 | 2025-10-07 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 368.7 |
| fa639d51-7b15-38d7-a647-13d6f58b7ee1 | -7.9011 | -47.8072 | 2025-10-07 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 197.4 |
| a04bfbe9-be65-388d-a786-ed191a7c2e78 | -8.921 | -47.3595 | 2025-10-07 13:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ddc4d9a6-b8e6-31f4-b2c4-5d181047624c | -13.7932 | -45.7396 | 2025-10-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 93084133-0a96-3d65-b0e4-32355ffc0f2e | -13.2658 | -48.0632 | 2025-10-07 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| eede3c1a-3555-3135-aef0-33cb55689bc0 | -7.7743 | -42.6103 | 2025-10-07 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| a6039f1b-b3b5-3738-b321-ecf0737e2d69 | -13.2426 | -47.2391 | 2025-10-07 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 84071605-5f2b-3696-8e0e-650989c331f8 | -13.7927 | -45.7627 | 2025-10-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 4331af20-7293-31a8-bef5-ec4c21a4bed4 | -11.9963 | -47.1944 | 2025-10-07 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 83077f18-72e3-3d85-abdc-f3c91c51ca8d | -10.1569 | -45.493 | 2025-10-07 13:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 47bf2368-ed37-3497-be18-0587376c04e9 | -8.8618 | -46.0949 | 2025-10-07 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| bc206e89-237b-35a8-8875-cdb4b0b94864 | -8.8794 | -47.6722 | 2025-10-07 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c32befab-4604-3dc3-b6e2-6d729fc88af2 | -8.0866 | -44.791 | 2025-10-07 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a86fc47d-8e33-35be-82d5-64178eba208c | -9.1525 | -49.9639 | 2025-10-07 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| f2f3facb-8b8c-3206-bb44-6a9ccf5ca8b1 | -18.2856 | -45.4587 | 2025-10-07 13:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| aa41ac40-1d66-35b4-8630-893177a3cd63 | -8.4824 | -46.2912 | 2025-10-07 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 9159e825-cf70-3b86-949a-67b246f5142e | -11.9519 | -46.4352 | 2025-10-07 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 7f36bef8-202b-3b8c-ad90-20e7870a06a5 | -11.7221 | -45.3508 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 3b886ae3-87a8-3c02-b767-0f5e70f3df68 | -10.9113 | -47.0906 | 2025-10-07 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 3a9c601b-f054-3f1a-a7b7-77ffb3c58d67 | -12.9103 | -54.7352 | 2025-10-07 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 1191413f-10e3-3af6-968f-fba1ccf5a032 | -7.6935 | -46.2324 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d9babbd9-dcc8-3bad-9493-12694175c4fb | -14.8645 | -51.4158 | 2025-10-07 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 689e91d5-c824-3bc8-80b6-7fbb49b14fcd | -8.9121 | -46.5829 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| bb82aad5-9ebb-380e-9b8d-b021eb625410 | -8.613 | -44.9189 | 2025-10-07 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9e59b274-2866-3ef3-a917-8caeaac5915b | -9.1789 | -47.818 | 2025-10-07 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 4372f64d-7985-3634-9a4c-5c97b06172d1 | -11.9963 | -47.1944 | 2025-10-07 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0c2b666d-1ad9-306d-b190-013c7f9abd98 | -14.8641 | -51.4373 | 2025-10-07 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ad21cb2d-54b4-34b0-97a9-5832fd6cc86a | -13.2426 | -47.2391 | 2025-10-07 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 67e797e6-cd64-34e4-83e8-efc3f751aec8 | -9.1525 | -49.9639 | 2025-10-07 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a80bfc03-c245-3445-87e2-b53cdb26eb03 | -11.6855 | -46.3593 | 2025-10-07 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 91d29a55-037b-3b8b-8665-a5ed443e976f | -13.2229 | -51.6957 | 2025-10-07 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 23408d46-1eb7-316e-aa61-882c53f5aa40 | -11.7837 | -45.1115 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7432209c-071b-3e11-8825-4a32741f7681 | -8.1882 | -44.2052 | 2025-10-07 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 8871fc7b-6fac-37ab-a795-ad65a1a9403e | -9.1975 | -47.8381 | 2025-10-07 13:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9944b3b1-f73b-31a8-8768-a8fc2cf43eee | -13.2623 | -47.2136 | 2025-10-07 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f7ffd912-b6f5-30e4-8de6-d21ec041fc00 | -8.8794 | -47.6722 | 2025-10-07 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 25c459a8-bfde-3e41-9047-5bfd32d7f2b8 | -8.2159 | -49.875 | 2025-10-07 13:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c53c509b-b299-3193-9122-42acf819d249 | -10.2129 | -54.1262 | 2025-10-07 13:40:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9940b097-5d17-3166-a214-cd053c7aeafd | -11.7833 | -45.1347 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| e3301610-6403-30de-8c39-77cb0d473ffc | -11.8029 | -45.1087 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 623d0020-cedf-3de4-b0d3-b30b39987791 | -11.8025 | -45.1318 | 2025-10-07 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 83de0e9c-1bf3-3dcf-97c8-47d897d1e02c | -12.4916 | -54.7364 | 2025-10-07 13:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e39dfa89-5898-30de-9c16-1f7751681cdb | -8.6397 | -47.2769 | 2025-10-07 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 25c52f82-9a4a-3df7-b4d1-de5e163b91eb | -8.6798 | -47.0738 | 2025-10-07 13:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| bec91c18-6839-3cf5-80f8-ad5e9f72cfd6 | -15.6003 | -52.5742 | 2025-10-07 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| aa244beb-8ad1-3aa4-b141-ff5e639e3a3b | -8.8717 | -46.7878 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 31e9b840-0f0a-3d17-9436-d5a00e7c7171 | -12.3158 | -45.3776 | 2025-10-07 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e13dcf4b-d249-31be-b570-1194e009e6e1 | -18.018 | -44.9965 | 2025-10-07 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 64b5265b-746d-3151-8c05-3d18f5f902f3 | -8.1804 | -43.3445 | 2025-10-07 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 223.3 |
| 31f48caf-0f66-3ebc-803e-7f8b232eccd5 | -12.3351 | -45.3746 | 2025-10-07 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| abba6dd6-e875-31ff-a01e-f4b9d083033d | -15.6202 | -52.5501 | 2025-10-07 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0863f155-b520-39e6-9eb9-2cc7a155bebc | -8.4821 | -46.3136 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5a65504b-929f-3f06-a4dc-5bceb45f6796 | -10.4283 | -50.3732 | 2025-10-07 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 11e3aacc-744c-39b2-be7d-c78dd5251f12 | -8.1615 | -43.3465 | 2025-10-07 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 89ec5a12-309b-3b54-88ec-ae2c4c58bf8d | -15.1553 | -45.7067 | 2025-10-07 13:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 3be36289-ac2f-3862-899e-ff927ad59a95 | -10.428 | -50.3946 | 2025-10-07 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| c6b51b7b-ab30-37b8-b8de-d00a24f155d3 | -11.487 | -43.4981 | 2025-10-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| b03dad0b-db9a-31b2-8ce0-a60512334b09 | -8.6521 | -46.274 | 2025-10-07 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |


[Clique aqui para ver as próximas entradas](README123.md)
