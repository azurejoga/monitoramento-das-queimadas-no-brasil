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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 893db5b8-fa40-3d55-a945-60b6c0883dc8 | -8.5198 | -46.3098 | 2025-10-07 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e47e5dd0-2113-31b4-a226-2a712d39823a | -14.7394 | -45.9907 | 2025-10-07 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b3c19a74-47c2-39b0-a57f-dd3178540395 | -11.7837 | -45.1115 | 2025-10-07 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 83f7cea8-4344-30b0-96ba-e588c03e8166 | -22.0279 | -49.7274 | 2025-10-07 01:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 155.5 |
| 967c98d8-c889-3f9e-829d-d76c2ee0cbd6 | -11.7645 | -45.1143 | 2025-10-07 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 611a000c-b3c7-3d83-8e88-325fee30e728 | -9.1978 | -47.8161 | 2025-10-07 01:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4ca3a906-3bce-3868-9ee8-9b69f30b56e2 | -5.494 | -43.0526 | 2025-10-07 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 5bc04faa-caa3-348a-8a3a-3e924dad41f3 | -22.0285 | -49.7042 | 2025-10-07 01:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| cec8a6a2-5cfe-3989-8910-a7a61edb791c | -22.1614 | -49.3969 | 2025-10-07 01:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 86272816-57d1-3401-9633-aa8343c76e27 | -18.157 | -53.37 | 2025-10-07 01:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9cecc16e-8673-3742-81d1-fc246490adf2 | -6.4543 | -44.5749 | 2025-10-07 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 350822f4-4b9a-33e9-9528-1d40b0eafc56 | -22.0071 | -49.7321 | 2025-10-07 01:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 265.4 |
| ad80f782-d16e-3d51-8d23-36e487b8d668 | -8.501 | -46.3117 | 2025-10-07 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1c21236a-667d-337f-8cd3-885eb35d4272 | -6.2421 | -43.2743 | 2025-10-07 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 809e073c-25d8-3a67-b351-0156ecc54992 | -8.174 | -50.3035 | 2025-10-07 01:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d97ea86f-83f3-3340-a955-12c7b3b9a22f | -5.5125 | -43.0747 | 2025-10-07 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4ee9e7d4-c89a-3275-a6ce-4b0f746f0b19 | -14.7389 | -46.0138 | 2025-10-07 01:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 751ff0da-a207-3bf7-9c8a-3e0797ef14f2 | -6.454 | -44.5978 | 2025-10-07 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3a0119c3-17da-3acc-bb37-c9b048145a57 | -14.903 | -51.4319 | 2025-10-07 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e5ace574-7282-3288-ab8d-140d6a8b5070 | -14.9216 | -51.4722 | 2025-10-07 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9d7dfd40-18da-350f-af95-e0adb098a81d | -4.6875 | -45.828 | 2025-10-07 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 7f1bf6be-ae55-3d0a-93cc-13aca46a7cb0 | -18.1176 | -53.3548 | 2025-10-07 01:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 889e5190-d42f-3ace-be37-66d4f64fe458 | -6.2609 | -43.2727 | 2025-10-07 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 02d86a27-a208-3105-b7ba-14c9b5110ff2 | -22.1822 | -49.3921 | 2025-10-07 01:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 744211de-5d67-3eba-a598-721a1fac46e5 | -4.6504 | -43.2038 | 2025-10-07 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 20de49af-6031-3bea-8680-ab035659020c | -4.6873 | -45.8504 | 2025-10-07 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 027203d9-494a-3ecd-bd8a-f7436a1b23f4 | -14.7394 | -45.9907 | 2025-10-07 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 60cf579a-930e-302e-81ca-37856497ab46 | -22.0077 | -49.709 | 2025-10-07 01:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 176.3 |
| 754af0d5-f97b-39bd-aa62-7f2038efd298 | -22.0279 | -49.7274 | 2025-10-07 01:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.4 |
| 3dfbffc9-3083-3183-b1a2-bc4adc1c7517 | -4.4445 | -43.2397 | 2025-10-07 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f2dca56b-49b9-377b-bd61-28d4b56f1a60 | -22.1621 | -49.3737 | 2025-10-07 01:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 142.6 |
| cadceab2-8042-3e0c-b825-8bac8971b848 | -5.4937 | -43.0761 | 2025-10-07 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| e58a60d6-bbbe-3e6b-ab58-c9759334db57 | -8.2071 | -44.2032 | 2025-10-07 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| d63146a4-9fba-36d6-90d3-4cb2c2dec549 | -12.9103 | -54.7352 | 2025-10-07 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e6595669-1ce1-3231-afe9-bd972f15b283 | -14.9026 | -51.4534 | 2025-10-07 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9502bd10-b32f-31e0-ad3d-de63b334490c | -22.1829 | -49.3688 | 2025-10-07 01:30:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 131.3 |
| f4d93548-ce06-36c7-a8ef-9323b20b8f08 | -4.4446 | -43.2164 | 2025-10-07 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b21a7493-f172-32e1-ad0f-8f335327e36c | -5.5127 | -43.0512 | 2025-10-07 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f436f468-c48b-3e09-a63a-3eae4b345fe2 | -4.6505 | -43.1805 | 2025-10-07 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 5e399173-767c-3427-9099-1979514d44e7 | -6.8703 | -46.0574 | 2025-10-07 01:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| db558241-f541-3744-9879-9f18b30148e8 | -14.922 | -51.4507 | 2025-10-07 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9450f9ba-a0ba-30f2-ac64-1f47734accf4 | -14.922 | -51.4507 | 2025-10-07 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 4102a1ec-7d09-3ac6-b770-3dfdf77b8912 | -22.0279 | -49.7274 | 2025-10-07 01:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.8 |
| ffb2d2c6-6121-3609-84bc-3ec73470701f | -22.0077 | -49.709 | 2025-10-07 01:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 164.4 |
| c83195b7-caf3-330d-869b-29fb71516aa7 | -6.2421 | -43.2743 | 2025-10-07 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f568e9fc-518d-3697-a6ed-418861054332 | -4.4446 | -43.2164 | 2025-10-07 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d3ca579a-22fc-3fd1-b65d-ef41bef17cca | -22.1621 | -49.3737 | 2025-10-07 01:40:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 48ba01bb-6267-33f4-b7f7-417ffcb421ca | -6.2609 | -43.2727 | 2025-10-07 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 13b2be7e-01ea-3260-8323-ab1617d4dc48 | -14.7389 | -46.0138 | 2025-10-07 01:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 150.6 |
| ad110ced-07d3-3d53-b18b-35056e326383 | -4.6873 | -45.8504 | 2025-10-07 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 91cd1187-0498-3e8d-b6ad-5dd82c8b0bcf | -6.454 | -44.5978 | 2025-10-07 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 241f0771-dd6a-372e-b6c9-2b12cb59b30f | -8.6521 | -46.274 | 2025-10-07 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 6c151b98-5904-3670-9d5d-dfd90c97b28f | -22.0071 | -49.7321 | 2025-10-07 01:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 201.4 |
| c8705d2a-813d-383d-a7ed-aafc9cd8bcb8 | -14.7585 | -46.0104 | 2025-10-07 01:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8058bc7c-170c-3d04-adf5-92516d9b4a65 | -4.6875 | -45.828 | 2025-10-07 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 5c487678-40e0-342d-bc95-6a03e907d190 | -14.7394 | -45.9907 | 2025-10-07 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| d4930993-4c23-39a6-b195-c5dcea99d15e | -4.6505 | -43.1805 | 2025-10-07 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ec456eca-133d-338d-8c40-1ab45d633663 | -8.613 | -44.9189 | 2025-10-07 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 0695d110-5885-3a48-be19-c7a9f4ad1a48 | -22.1829 | -49.3688 | 2025-10-07 01:40:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8b9a8de0-e79d-3cb5-85cb-f92e45fed5ec | -5.4937 | -43.0761 | 2025-10-07 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 37f3c958-5130-3197-b37c-8c5e50cf7c1f | -22.0285 | -49.7042 | 2025-10-07 01:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| a3cdabd7-f331-35bb-890d-74287fb0a05d | -14.9026 | -51.4534 | 2025-10-07 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ce5b3816-c258-3674-b81d-84d4191e4b2b | -10.8728 | -51.0501 | 2025-10-07 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| fc6678c2-30cd-348f-8e2b-6e3b6b00a235 | -5.494 | -43.0526 | 2025-10-07 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 69e731e7-8df3-3b9d-8fd3-dfde2bb30d9f | -6.4543 | -44.5749 | 2025-10-07 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 89df3adb-b320-37f9-a6ba-88316e4ef0a5 | -6.8703 | -46.0574 | 2025-10-07 01:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 7a8bb565-8a42-35b4-910e-abebd1f0c1ac | -14.903 | -51.4319 | 2025-10-07 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 43b6bdf3-bc4a-32d9-aaef-bcc1ebd33bb0 | -18.157 | -53.37 | 2025-10-07 01:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cb2b669b-6d37-30ee-a92f-f1a6e27039ab | -5.5125 | -43.0747 | 2025-10-07 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4756fc29-fa05-3d85-99d9-da783e8e8bee | -4.4445 | -43.2397 | 2025-10-07 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 88eda6e7-b9ea-33b3-bf07-7d62a082e642 | -4.6504 | -43.2038 | 2025-10-07 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| fdb3066c-8500-3c20-9fd0-03dc67597dd3 | -4.4633 | -43.2152 | 2025-10-07 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c2722391-6663-3c68-a0be-58a07aa05e78 | -6.4543 | -44.5749 | 2025-10-07 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 1ea91858-4a99-3987-9360-701fbed6973d | -18.157 | -53.37 | 2025-10-07 01:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d0d6623b-a3e7-31b7-a920-92696d94c420 | -14.7585 | -46.0104 | 2025-10-07 01:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 8e807d89-671e-3101-83bc-706637a3b1d6 | -22.1621 | -49.3737 | 2025-10-07 01:50:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 430ac651-1174-3379-9368-895376a8d99c | -14.7389 | -46.0138 | 2025-10-07 01:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| c43e5c05-c108-3925-93a3-a2d9faed997c | -6.2609 | -43.2727 | 2025-10-07 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a8ef5c0f-2d08-3154-85b0-a84df885f50f | -4.6873 | -45.8504 | 2025-10-07 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 155.6 |
| feb66d65-6394-3b9c-b8f3-656c63bdedb7 | -17.8157 | -40.1897 | 2025-10-07 01:50:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 4e8c1aef-f29a-3a21-a5c1-e825d4c4765b | -4.6504 | -43.2038 | 2025-10-07 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5b66c58f-17f2-3158-878f-732fd1543b10 | -4.6875 | -45.828 | 2025-10-07 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 53e07423-f96a-3b3a-808d-77add18bb694 | -22.0279 | -49.7274 | 2025-10-07 01:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.5 |
| d1fd8e21-bf57-3431-98b6-593056897623 | -6.454 | -44.5978 | 2025-10-07 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| cb636d7a-f8e1-3563-800e-dfa68f228866 | -4.4446 | -43.2164 | 2025-10-07 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 15f82667-336a-3a8f-8e63-ef6a8d9eeace | -22.0071 | -49.7321 | 2025-10-07 01:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 241.3 |
| ed660690-867f-3edb-8f3f-8394d9ea97ac | -4.706 | -45.8493 | 2025-10-07 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 2f048f81-7703-3564-9583-28d2848a3959 | -22.0077 | -49.709 | 2025-10-07 01:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 191.1 |
| 7611095c-fd6a-3474-826b-3566ebefe932 | -4.6505 | -43.1805 | 2025-10-07 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 1d173cf8-1c7a-392b-93d1-2058a48f3b44 | -18.1176 | -53.3548 | 2025-10-07 01:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 0f57082b-df52-354b-84f8-4a6864634119 | -10.8731 | -51.0289 | 2025-10-07 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2bb7345a-b89c-3213-92ee-a12d55e9ab6e | -14.759 | -45.9872 | 2025-10-07 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a9ceb8f7-7182-389b-8365-454b84d8ba2d | -14.7394 | -45.9907 | 2025-10-07 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 38dce516-9cdc-31d0-82fa-c8f50a49645e | -10.8728 | -51.0501 | 2025-10-07 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 89fc0e9b-db21-31ca-b687-ac574a9454f6 | -22.1829 | -49.3688 | 2025-10-07 01:50:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7b37d80f-eb47-3cab-8291-5cf438096bb3 | -8.8906 | -46.7859 | 2025-10-07 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 16d5ae0a-6fe3-3b8b-a73e-94a5596882f4 | -6.2421 | -43.2743 | 2025-10-07 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f3c8ca11-4f00-39bd-99c2-3f10934b72bc | -22.0285 | -49.7042 | 2025-10-07 01:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| d2db854a-ffdc-3b9d-9274-daf341763119 | -18.1769 | -53.3669 | 2025-10-07 01:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 59.8 |
| cdd90ee0-926b-3bc6-987b-ad964ef7ae5f | -14.758 | -46.0335 | 2025-10-07 01:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |


[Clique aqui para ver as próximas entradas](README14.md)
