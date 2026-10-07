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

## Dados Diários - Página 198

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52c852fd-f078-390b-a0f4-14e8e338a426 | -7.17105 | -43.76797 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bff083cd-c121-37b1-9b23-6600012ee291 | -8.98151 | -48.94046 | 2026-10-07 16:37:00 | NPP-375 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 24d60525-3805-31df-813e-41546998a193 | -10.40621 | -47.5301 | 2026-10-07 16:37:00 | NPP-375 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84882b4b-89e4-38da-ab51-bceab29cba7b | -6.44203 | -52.66887 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2b45071f-aa3d-3e0b-b588-d07523003380 | -6.64978 | -47.91275 | 2026-10-07 16:37:00 | NPP-375 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e0982fe9-0683-38d1-abb3-5e11abe4a9e1 | -8.59556 | -45.6776 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.8 |
| f0d86953-2844-329f-951f-8871d7e0f24a | -6.84138 | -39.55228 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| afddc610-8067-3530-93c4-d33db6db99bd | -5.89206 | -51.54215 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c19095a7-770b-3efb-ab84-9b03d40e963d | -7.30476 | -43.97781 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee4ed91c-370d-3de0-b531-2a620c2a4b8f | -3.03003 | -41.09224 | 2026-10-07 16:37:00 | NPP-375 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c2ce7e91-94e0-3e86-8453-5a360298b6ae | -7.20542 | -55.11742 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3c5cba8f-fd54-37e5-b5fb-2e5fdff9e25f | -14.93281 | -41.09945 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5cc7d2a0-7d3b-3d75-b626-f9442ef1e23d | -8.82861 | -38.38913 | 2026-10-07 16:37:00 | NPP-375 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| bdd3d39b-67de-3a09-aa3b-515b0519460e | -5.69148 | -53.47488 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a6d47916-f91f-3c2c-b2fa-aa9b0f63a3f9 | -6.22575 | -46.00051 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2d5986de-6fa0-3680-8772-5ed2481a65e0 | -8.20963 | -38.07136 | 2026-10-07 16:37:00 | NPP-375 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 31a248e3-bbce-336b-ac72-f3eac2e605c3 | -10.12493 | -46.84731 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 55fa5f15-ce8f-3f26-8a22-cfb8124c7556 | -5.87175 | -57.66969 | 2026-10-07 16:37:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 276a71a9-6054-3b13-96cc-6332eb91c329 | -9.02145 | -51.42375 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5a45f706-8db3-3df0-beb8-f6380f36af34 | -7.0193 | -47.5113 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d69254a2-003e-329f-ae07-a4877580cd04 | -5.88659 | -51.19532 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e164c24-819e-3387-a9af-5e26f9cc0529 | -8.74152 | -44.20387 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ef338697-a584-353c-b8c8-4ad6075b0ef8 | -5.68171 | -53.48368 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 76ea0e12-6a68-324a-9499-6ca45b0990b6 | -3.01458 | -39.83234 | 2026-10-07 16:37:00 | NPP-375 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9d621565-5c48-358c-9cc6-3a931c9b6060 | -6.17461 | -44.0374 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| b3422328-69df-3969-9d8b-f880c7a01477 | -7.17634 | -43.71387 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7959f787-1fff-370d-9d17-43b700c636e3 | -3.86925 | -44.12999 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8990e73c-e039-370e-ae7e-4e3870f64f67 | -9.98591 | -46.01374 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3a1c6f4e-aaa8-3004-ac13-41caeab8e308 | -16.41671 | -50.49054 | 2026-10-07 16:37:00 | NPP-375 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3f42dfdf-4dbf-3566-a84a-84ab98b8b8fd | -9.91591 | -44.80442 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e453e2c7-0649-387a-90d1-0b1b51d4d540 | -6.84883 | -45.52672 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1cf68e1-0b20-31cd-a46a-df4e2c86a190 | -6.21025 | -52.84047 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1b93a0b-ceba-363f-a8da-38b06ba46159 | -3.57336 | -43.0955 | 2026-10-07 16:37:00 | NPP-375 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| c883912e-8756-37f3-be5c-e765b401936d | -9.26269 | -45.64151 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9b1ba63e-03a9-33c4-9c7f-6b6d94c290d6 | -17.01856 | -45.91359 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 15ec2543-86d0-3b7c-83b0-b8306ca2554a | -3.94949 | -41.54767 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 542fbb8b-7643-35fa-8064-176e869939a5 | -5.78157 | -52.35885 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| eccd4750-8e72-36f9-ad78-3f9088a51263 | -11.38024 | -46.69175 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 7b163673-2fb0-3f3e-8969-7461df554346 | -9.94326 | -43.54932 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 12b19d9b-61ee-3b11-95eb-9945b88110af | -14.7019 | -41.25794 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2400e4fe-8934-32ba-9de9-b6ffd41e096d | -7.59948 | -47.02085 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 10c6ae96-1bf2-3620-ab8e-16e8afc6c149 | -16.06103 | -39.86099 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| c33529dc-3fbf-3d5a-aa93-e6158b4f9720 | -5.96101 | -40.94448 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| a69079e8-4984-3aaf-a3e0-d7152a9f0ac8 | -6.46111 | -52.88017 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35b3aef6-70d4-3c81-8906-93438523d6a7 | -3.43654 | -42.381 | 2026-10-07 16:37:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 27.0 |
| afc9508d-b9bc-388d-a63b-d28fb70923dc | -7.39766 | -55.20805 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 97cd68b0-1820-30e4-a5dc-e74cebff2238 | -4.05718 | -42.22247 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 466ed672-c019-38bc-8ddb-920f483b81ec | -7.76677 | -46.6592 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5db651e9-2cec-3fb3-ab6a-dfa780071d6e | -4.67866 | -43.71984 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c034dd63-7b76-3163-b99c-f1f42ec106bf | -5.47872 | -41.22096 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 4e4f30d6-d9d4-36fa-83c1-a7f3a9c36e39 | -15.51108 | -42.70189 | 2026-10-07 16:37:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5343fdc5-a96b-354a-bdfd-494c8d850914 | -6.4353 | -38.13663 | 2026-10-07 16:37:00 | NPP-375 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 20107190-04a4-3423-93e3-57b7b8a0f912 | -4.84476 | -40.41058 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fde271c5-901d-3aa2-bed4-bc59d83f08a5 | -15.92002 | -40.02309 | 2026-10-07 16:37:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 072a005a-0b91-3f8b-8464-2796ec78bbd9 | -7.97329 | -36.73497 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DO TIGRE | PARAÍBA | Brasil | 2514107 | 25 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cbc784a3-14f5-3f32-affa-2a607e68c81f | -8.77872 | -47.57667 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 45de5938-206c-3b0f-8513-ea69da208884 | -10.36071 | -40.11052 | 2026-10-07 16:37:00 | NPP-375 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 83540bbf-c602-3b3d-94fb-1e278416bc65 | -6.63821 | -50.06417 | 2026-10-07 16:37:00 | NPP-375 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b93267cc-feaa-3fe2-923f-90ab0c17f2a4 | -4.68281 | -40.82879 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 35.8 |
| 3eed2079-6731-3b59-9837-01352c2bfc04 | -11.09951 | -47.58744 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 66a25a9b-4f99-3bf6-9771-3bbdbc542f13 | -15.3899 | -41.70366 | 2026-10-07 16:37:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.9 |
| 8ae50fa3-a9d1-36e6-9fa1-a58ba4d44fd8 | -4.51468 | -42.88449 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7f453585-ca19-3af7-8448-83e0faf311fe | -3.51259 | -41.94686 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bf543b65-8207-3593-ab98-681bfd079d9d | -3.77091 | -41.77112 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| e6a61461-15f1-37d4-b907-7c935c1cf488 | -10.63998 | -53.85872 | 2026-10-07 16:37:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 06be3c24-2ae2-343f-90eb-f918ed5339c3 | -7.03627 | -45.42768 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d73696f-724c-35a9-8eec-278bd98a57fd | -9.37895 | -45.92198 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 47b7edf8-12ea-31ad-b6a9-762d6618b858 | -16.05914 | -39.84945 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| b4d0e439-601a-34d1-8815-e91415707557 | -9.82364 | -47.47806 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bcee5215-381c-3313-aaef-9398e47f8d50 | -5.52107 | -45.5832 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8222974-d001-332d-af2b-c9c6eb44c481 | -14.73447 | -40.84483 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9ac95e76-c278-36e2-bca5-f33703eafada | -8.99305 | -35.25893 | 2026-10-07 16:37:00 | NPP-375 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fab664e4-b8a4-37b4-a2ce-daff0d6e3825 | -17.0224 | -45.91304 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6f457217-8012-3d0c-a1fb-260a6909d9be | -5.72394 | -41.72287 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 40.4 |
| 4bbe9848-3cb8-3059-ae98-91b7ae403517 | -7.87786 | -54.98475 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 5254156b-dbfd-38ad-bd25-fddaa62f100b | -6.44856 | -37.63358 | 2026-10-07 16:37:00 | NPP-375 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 317be0a7-32ab-32d8-bfbf-fea0bc0d1300 | -7.42154 | -47.37635 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 12562a64-4578-3764-89cc-9a85562ecca8 | -8.00697 | -47.18719 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e06c4702-ea41-3add-b906-3c79d067f3ee | -8.78252 | -47.57611 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3844653a-72f1-3d16-ba70-7a520cd1cf11 | -5.74818 | -45.16618 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| ad34fe23-85a5-33a7-a2ff-27a02131ac6a | -7.03548 | -45.42822 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1982b38-1ca6-38b0-8e5a-f12a158f68a0 | -5.76818 | -38.56112 | 2026-10-07 16:37:00 | NPP-375 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 9b394384-4256-391b-baa4-6d5d3fd99a30 | -6.15693 | -51.7288 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a84601c3-500f-312f-9627-167c5c77840d | -3.77508 | -41.78727 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e0b928c1-0dcd-3b0e-a0ec-a27a7ff68418 | -9.91745 | -46.79839 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 3d4daf60-e090-3875-9743-57c3cfc137d6 | -8.19469 | -46.33479 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c0bbdec9-13ae-3b26-9bc3-6d8279de9db8 | -6.69359 | -48.20626 | 2026-10-07 16:37:00 | NPP-375 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 52730505-a1d4-38ba-8940-dece44b1c0b3 | -11.32168 | -47.58062 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 968e39d4-d212-3435-a67d-c7f2537d6d85 | -6.22508 | -52.83253 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c593e27d-2e13-3643-9eeb-2c2f320ac909 | -3.70485 | -44.88865 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 19dbc526-62ad-30a6-b59d-ae822b9139e3 | -9.94273 | -43.54582 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b2cd15ba-f25d-3720-9ee5-74de1b620495 | -4.57006 | -40.72197 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 0d579ddd-a688-3ab9-900e-735719fc6002 | -9.96472 | -45.96749 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e7c7e4b3-3c07-3d86-90ec-90d2021da5e5 | -15.6356 | -41.69529 | 2026-10-07 16:37:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 75928199-2012-3f7e-9a1f-525f90496593 | -5.48034 | -45.63328 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 728e57a5-ab46-3339-9f89-c0bcac44cb54 | -3.40227 | -43.99692 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31977abf-ed96-3c09-8609-45bb668dd01f | -10.62656 | -53.84758 | 2026-10-07 16:37:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ecac35e3-84b2-37c3-97c2-0c90684eb80f | -3.29888 | -39.51264 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ef3be165-80dd-3817-b80a-796208e3385e | -4.98918 | -45.63973 | 2026-10-07 16:37:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00486839-d142-348e-b155-742c4ab0228a | -6.30431 | -53.02509 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README199.md)
