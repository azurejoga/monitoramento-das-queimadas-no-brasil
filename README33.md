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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9471e1c8-0a02-3537-a151-5b4faf6c123a | -10.476 | -46.9877 | 2025-08-03 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b8b4fee8-98f8-3208-b8de-34f60732d779 | -12.4584 | -47.0398 | 2025-08-03 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e36d7aac-3959-395a-bb69-949056bbd724 | -11.9399 | -44.9497 | 2025-08-03 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c876df7a-e2d3-31ad-9c86-4d6ab52402d6 | -8.0324 | -43.1022 | 2025-08-03 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 78156df0-b2cb-36e1-9ae0-90272b7b3400 | -4.5497 | -44.2047 | 2025-08-03 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 4523a6f9-19f5-3f9a-a185-c7236f928fb6 | -11.9395 | -44.9729 | 2025-08-03 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3eff8e14-f446-3948-9b4d-25e10a44b34d | -10.476 | -46.9877 | 2025-08-03 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 774d98b2-7b94-3c86-b93e-dd3d166356c8 | -8.0324 | -43.1022 | 2025-08-03 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 19a16166-de3a-3bc4-b0ed-c41834f2209f | -12.689 | -48.1011 | 2025-08-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5361df16-a9e7-3bad-abd5-0b8e9c671990 | -10.4767 | -46.943 | 2025-08-03 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| dfe6cbc4-8c25-3a1d-ab2a-9965ab7f2edc | -10.4764 | -46.9654 | 2025-08-03 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9b96f6e6-d492-3ea1-8c78-81a13e45ccf3 | -11.9395 | -44.9729 | 2025-08-03 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5b66f69d-a0a7-33c5-bb3c-775f62fd1ba6 | -8.0324 | -43.1022 | 2025-08-03 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 31e947e0-09ae-30f7-9daf-3cbc8d78f808 | -10.4724 | -47.2333 | 2025-08-03 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f05f03f2-ccb6-33b0-9f76-c022438f2f52 | -4.5684 | -44.2036 | 2025-08-03 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 0e600bc3-8b7d-3af3-850b-0be9078c3221 | -8.0324 | -43.1022 | 2025-08-03 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 1e7234d8-0e67-3b03-b173-5d30fe1057ab | -12.4588 | -47.0173 | 2025-08-03 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 9934c964-5149-30e4-9ba0-745dfaf666ec | -12.633 | -44.8654 | 2025-08-03 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 08f7f6b5-7efa-31b3-922c-7866596a105e | -8.0324 | -43.1022 | 2025-08-03 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 6a332bcd-69ff-3695-8829-19323a36d474 | -10.476 | -46.9877 | 2025-08-03 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 041423fd-a520-3c95-9b73-1bcbc023473d | -10.4724 | -47.2333 | 2025-08-03 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 66c973d4-cbcb-3645-867f-20ce6c02fa05 | -4.5497 | -44.2047 | 2025-08-03 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 53473047-6ecb-30c6-8fc9-73c5c3df8c60 | -14.1297 | -45.4043 | 2025-08-03 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 00b888eb-2a27-348b-bc63-7f45a78d5a9c | -10.4764 | -46.9654 | 2025-08-03 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 90838981-2cb3-3f68-bcd7-3f29ab791aa8 | -14.1103 | -45.4077 | 2025-08-03 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 193.0 |
| bf975b91-55f6-3a6b-82a4-8591a9db396b | -12.4588 | -47.0173 | 2025-08-03 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| a17d3ab9-3462-38fa-9411-88448a3ef47a | -7.6873 | -45.1272 | 2025-08-03 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| d4810e55-a115-396b-af3b-3b66989c1764 | -14.1297 | -45.4043 | 2025-08-03 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| e5e84868-e0bc-3482-968b-63d35956dcd0 | -11.9395 | -44.9729 | 2025-08-03 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 2f6d5424-999e-339a-812c-3795c6ababfe | -4.5684 | -44.2036 | 2025-08-03 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7bc8574e-921f-3edd-a995-51e8f368c587 | -11.5102 | -44.3401 | 2025-08-03 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 78d7d1b6-efe5-346a-987b-7b33fc8577ef | -12.4588 | -47.0173 | 2025-08-03 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 4b25fffd-0cd3-3a6e-ba6b-a4484a2b4892 | -8.0513 | -43.1001 | 2025-08-03 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 01ef6805-df50-3b12-95f3-935aa42891d9 | -8.0324 | -43.1022 | 2025-08-03 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 72112c9d-bb5f-384a-807a-d5897c4b5ff2 | -7.6876 | -45.1044 | 2025-08-03 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 2d799202-7a7e-3ecf-9973-253bbc4b4db9 | -9.444 | -46.3239 | 2025-08-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 1566cee7-2327-3fbf-9ac3-bf2b109d5bf3 | -14.1103 | -45.4077 | 2025-08-03 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 84c8e5e9-a1fb-3e01-a634-07130bd12d25 | -8.0123 | -43.1984 | 2025-08-03 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 16b3ac6d-212a-3307-b77f-d4f56795fd84 | -6.2066 | -45.0051 | 2025-08-03 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 42625309-0b68-33c7-afe6-eb0564fe9f4f | -10.4764 | -46.9654 | 2025-08-03 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 6c46f6f8-d15e-350c-a024-6c19186bf552 | -11.491 | -44.3429 | 2025-08-03 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a56cee20-f67f-39bd-8e5f-757594198d4e | -9.6601 | -45.7576 | 2025-08-03 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 260847e2-5313-3f8d-8586-74064b6995e9 | -4.5497 | -44.2047 | 2025-08-03 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 89110c89-9b62-326c-b985-4e61f5cca8e1 | -12.4588 | -47.0173 | 2025-08-03 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6e9f1417-f303-31b7-8e20-7212dfb7d167 | -8.0513 | -43.1001 | 2025-08-03 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 8e80b58b-673e-3446-8ada-4311c409a1fa | -8.0324 | -43.1022 | 2025-08-03 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 61833d72-2410-31d5-8f8e-fb9683951237 | -7.6479 | -45.29 | 2025-08-03 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e72fc421-187d-3f4e-9056-f1647d1b2c30 | -10.4724 | -47.2333 | 2025-08-03 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c169bdf7-5716-319f-87ef-9513e41f6a2d | -8.0123 | -43.1984 | 2025-08-03 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| d8e462ca-e92c-3ed3-a227-6b226375428c | -14.1103 | -45.4077 | 2025-08-03 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 83a4413a-794c-3365-a9f0-97db18239bd5 | -14.1297 | -45.4043 | 2025-08-03 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| a1d08042-1deb-37f4-83e5-3c0553e7cea6 | -7.629 | -45.2918 | 2025-08-03 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d19ed7ac-879f-3f3e-b849-55b548be4137 | -11.4919 | -44.2961 | 2025-08-03 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ab61df0b-331b-3cd5-b95d-d0e37b85256f | -10.476 | -46.9877 | 2025-08-03 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 7f5222ff-2f1c-3984-ba8c-48e63335e8b9 | -10.4764 | -46.9654 | 2025-08-03 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 5d42fbba-cdc1-3a4c-8004-dc3784e21e59 | -4.5684 | -44.2036 | 2025-08-03 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6d0c38fb-7bcd-31f4-8009-109d240cb8e3 | -11.5111 | -44.2933 | 2025-08-03 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4952425f-47db-3e0c-8b7e-15a9669931e6 | -12.4588 | -47.0173 | 2025-08-03 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 6c1b17ba-d8d1-38ea-b8b1-4238b7089aac | -6.0886 | -47.7508 | 2025-08-03 14:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 35871564-e6f3-3f2a-9664-d1ecf2d5ba9f | -14.1297 | -45.4043 | 2025-08-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 7c52c5ed-4ea1-3b7a-8833-f363b4499a69 | -8.0123 | -43.1984 | 2025-08-03 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 5b431b6e-c6be-3ed5-a31a-18db9088fd7d | -14.1103 | -45.4077 | 2025-08-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 969e0931-2bfe-32fe-be43-5501cf231340 | -8.0123 | -43.1984 | 2025-08-03 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| c099b2b3-e773-3763-b117-baa4ee5979bf | -7.6873 | -45.1272 | 2025-08-03 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 8eba2693-660e-3039-b08b-94ad49af38e8 | -7.9699 | -45.0997 | 2025-08-03 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ae802b0e-5667-33c9-9adb-5ef865892a2d | -8.0321 | -43.1257 | 2025-08-03 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 334.7 |
| e50979e6-43fb-34c5-958a-735869bf4f75 | -6.0886 | -47.7508 | 2025-08-03 14:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 185af56e-8d83-3399-91b9-3215ef3decf5 | -7.6479 | -45.29 | 2025-08-03 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8e44f609-b348-34d8-aefe-e62cdc5514ff | -7.994 | -43.1534 | 2025-08-03 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 291.9 |
| 763a0cb3-b1c3-32b3-85c1-4a5561049396 | -12.4588 | -47.0173 | 2025-08-03 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 8dd01325-98b7-3ced-975a-b6660b6469b7 | -8.0315 | -43.1728 | 2025-08-03 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| 05ceb047-26e9-393a-968b-d157f4887912 | -8.0318 | -43.1493 | 2025-08-03 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 314.6 |
| d5a310b2-b2c8-3220-9454-f718f81d5d7c | -14.1297 | -45.4043 | 2025-08-03 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| a99340c1-3d30-3e2d-80f2-4f503a29514d | -7.951 | -45.1016 | 2025-08-03 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| dc96426c-0f2a-3bee-83b1-600a62998552 | -8.0132 | -43.1278 | 2025-08-03 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 702.7 |
| b70ccc20-94c9-315d-9f1a-2fc8ecc6cf57 | -10.4764 | -46.9654 | 2025-08-03 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| eeacbabb-4435-34f9-a3c8-f175a958946a | -7.629 | -45.2918 | 2025-08-03 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 75d81eb1-288b-3792-a1cd-38459bc19ac1 | -14.1103 | -45.4077 | 2025-08-03 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |


