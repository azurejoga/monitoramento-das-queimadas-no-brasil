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
| f51bd7f2-426d-3e3c-8101-53c7d667b3c3 | -6.7194 | -44.3231 | 2025-07-17 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 6b58c15d-61a7-3fea-a9f3-57cc5174fdf5 | -6.7192 | -44.3461 | 2025-07-17 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 8ec16743-66ae-3e54-a50d-d2c558db689a | -5.6754 | -43.7147 | 2025-07-17 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 21ee12a0-ef00-3dd1-98e5-d4022123286c | -3.3958 | -47.4785 | 2025-07-17 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c5d209d3-1f2d-370a-85f7-3f2cad8c9c1f | -11.1125 | -48.8531 | 2025-07-17 00:00:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3b28230e-e46e-397d-9cfb-0a5d3692316a | -8.1078 | -43.1175 | 2025-07-17 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| cadd88a7-5bfa-38e2-accd-c35e6169b19b | -3.3957 | -47.5003 | 2025-07-17 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4986c17b-11e1-3019-8723-2fd768eec68b | -5.6379 | -43.7175 | 2025-07-17 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 345d92c2-8697-3905-849c-0d2aa169a50b | -11.1121 | -48.875 | 2025-07-17 00:00:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d02f38df-a023-3de9-be3f-4e641c027c97 | -11.9568 | -48.4203 | 2025-07-17 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6e9d40e1-d79b-34bf-b962-60d237ce4d0a | -8.0886 | -43.1431 | 2025-07-17 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.0 |
| 85c803b6-0216-37dd-8367-33f21dae6360 | -8.1075 | -43.1411 | 2025-07-17 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 324.3 |
| 0b5db6e1-23c1-3fa8-bcd6-75fab7f6c451 | -6.6304 | -49.7382 | 2025-07-17 00:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 517499a2-f91e-326e-b79a-97db6aa9409f | -5.6567 | -43.7161 | 2025-07-17 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 36ce0efb-9d97-3059-a5bc-232e122b70be | -9.2449 | -48.5546 | 2025-07-17 00:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 412.1 |
| 6bad6e77-96cb-365f-983b-0d76a7b273e8 | -3.3772 | -47.4792 | 2025-07-17 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 8317c1a9-329d-3ff9-acd3-b264b0750592 | -11.9376 | -48.4228 | 2025-07-17 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8dd85147-48e4-358b-9096-e139d25dbc09 | -5.6565 | -43.7393 | 2025-07-17 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ed7bfbdb-21cf-34cb-b93c-425024960b6b | -22.3989 | -49.7795 | 2025-07-17 00:00:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| d204d4b4-bcb3-303c-8b11-d3fb0e82cb22 | -8.1072 | -43.1646 | 2025-07-17 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.5 |
| 024b554b-f55f-3538-a2f6-c8500bca44e8 | -9.2447 | -48.5764 | 2025-07-17 00:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 8166def2-e749-3455-ac58-3f62ed79d19f | -6.7382 | -44.3215 | 2025-07-17 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| b406a527-96da-3b24-a988-65e2c8bbf9ec | -12.6929 | -46.8029 | 2025-07-17 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e0c77eea-ff29-381b-b8f7-255485819764 | -9.2258 | -48.5782 | 2025-07-17 00:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| ab9f495b-d041-31fa-b72e-df0a7f9fcd53 | -12.427 | -50.0387 | 2025-07-17 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 76881a4c-f09d-31a7-ae03-61c953058f00 | -5.6569 | -43.6929 | 2025-07-17 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9cfdaf92-2177-3692-a086-92ff2a8ef702 | -8.0883 | -43.1667 | 2025-07-17 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| e38de460-89d8-3e11-8f4a-ab1c9df15efd | -6.7006 | -44.3247 | 2025-07-17 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 72fec054-83ad-3ec0-80af-5e44cd118652 | -8.1264 | -43.139 | 2025-07-17 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| cc266212-1853-3d86-8d67-495520dcb38b | -9.2261 | -48.5565 | 2025-07-17 00:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| ef614303-5ef1-3539-85da-60b98f4116f5 | -5.6569 | -43.6929 | 2025-07-17 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 258c7720-e05e-3cb5-b12c-dad86023367b | -20.1928 | -48.716 | 2025-07-17 00:10:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b260fddb-1cbf-3be7-8ad8-7e02bda8a6d6 | -6.7192 | -44.3461 | 2025-07-17 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| bbea23ae-bf76-3f5d-9b68-5540c53e0734 | -5.6754 | -43.7147 | 2025-07-17 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 8df4c4f3-a534-3482-ab21-bababbe9aded | -11.9568 | -48.4203 | 2025-07-17 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 64ac1320-d2df-34ea-8635-01638a3f94c8 | -8.1264 | -43.139 | 2025-07-17 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 0dabc322-84be-3d75-a079-12176b5f545f | -9.2447 | -48.5764 | 2025-07-17 00:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 191.6 |
| b022d00a-8733-3a37-98e0-8c33cb02958d | -11.1121 | -48.875 | 2025-07-17 00:10:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 1230d82d-05ad-3170-b6d4-037cd4f67374 | -8.1075 | -43.1411 | 2025-07-17 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 346.2 |
| 02f35037-3533-3895-96f2-83a4c514057d | -9.2449 | -48.5546 | 2025-07-17 00:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 322.3 |
| 88ff95f2-db84-3267-8e8b-70719a03eca6 | -11.9376 | -48.4228 | 2025-07-17 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 14a2e18f-2421-3eb7-a4fc-7ab38305a12c | -22.3989 | -49.7795 | 2025-07-17 00:10:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| 93fdef7a-9478-3765-8b6e-f489915eadd5 | -5.6379 | -43.7175 | 2025-07-17 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| c2e0aa98-3e69-31b0-ae90-ebcee421aae3 | -8.1072 | -43.1646 | 2025-07-17 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 1692a865-f0df-3841-976f-c63d631dfca2 | -5.6567 | -43.7161 | 2025-07-17 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 319.6 |
| 0e94209d-54f3-3e1e-b1da-f17d050b3caa | -3.3957 | -47.5003 | 2025-07-17 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ce4e0b5a-9921-3338-be70-9c8330c89be0 | -6.7382 | -44.3215 | 2025-07-17 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 63401a08-9016-32fc-85ca-674f4c40100d | -11.1125 | -48.8531 | 2025-07-17 00:10:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5666c090-3061-35a0-884b-dcf2d4b66dd4 | -3.3772 | -47.4792 | 2025-07-17 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 6ec189d2-1730-3144-8e63-69efb50d1281 | -20.1724 | -48.7205 | 2025-07-17 00:10:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 58c4b7ca-8e5e-3649-bd3f-82e04c7838a8 | -3.3958 | -47.4785 | 2025-07-17 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d92fdd7f-9a94-32fc-983b-cd0fa4f8ff19 | -12.427 | -50.0387 | 2025-07-17 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 708b8e3e-d1d5-37f1-8c85-36dd4ba6a0cc | -8.5387 | -47.8588 | 2025-07-17 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f5fabb1d-30d3-3065-8857-676d51b05445 | -6.7194 | -44.3231 | 2025-07-17 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 5b07d883-858e-35ed-8239-f1bba8655644 | -8.0886 | -43.1431 | 2025-07-17 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 1c0189c4-26cd-383b-968c-95cb3c31948f | -9.2261 | -48.5565 | 2025-07-17 00:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2badcfa8-9618-3856-88ca-173380a7e0f4 | -8.1075 | -43.1411 | 2025-07-17 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 327.4 |
| 557d41e1-3066-3c29-aa2a-1d7c7a81f943 | -6.7006 | -44.3247 | 2025-07-17 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 8437353a-3745-3e55-a201-20f5fc8d08c3 | -3.3772 | -47.4792 | 2025-07-17 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 12e65108-0015-3e55-905a-3d9685eea925 | -12.427 | -50.0387 | 2025-07-17 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 93e62e19-1457-3085-8174-9a1b9998f428 | -5.6569 | -43.6929 | 2025-07-17 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 743dd6d7-a12d-3b86-96f1-8aa16efa34f1 | -5.5241 | -43.8878 | 2025-07-17 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7ce0ee32-a8d9-3c7c-99a0-8123d41a00a7 | -14.0377 | -51.2072 | 2025-07-17 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2648480d-3229-3cd2-8ddc-099340b47f1e | -9.2449 | -48.5546 | 2025-07-17 00:20:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 5b913c4b-c991-33d5-ae9d-40e717322585 | -20.1928 | -48.716 | 2025-07-17 00:20:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 1c35cdad-c77e-3a1e-99c6-b2214173670d | -11.9376 | -48.4228 | 2025-07-17 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2a326f87-48e8-3ced-b98a-f34729db6cd0 | -3.3957 | -47.5003 | 2025-07-17 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| f881aed2-09ef-303f-8eb2-ca8f314fc90e | -20.1724 | -48.7205 | 2025-07-17 00:20:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 95.1 |
| c81b435e-0351-3414-8da9-1493150a689a | -6.7194 | -44.3231 | 2025-07-17 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 97bb265f-cc9d-3165-a2ba-bdd8ea84d465 | -5.6754 | -43.7147 | 2025-07-17 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 21bc307a-d0aa-3828-b60d-bcda4314feca | -6.7382 | -44.3215 | 2025-07-17 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d004f42f-028a-3cac-ac65-fb4a2a58dd8f | -3.3958 | -47.4785 | 2025-07-17 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| b4d792d9-1241-39f6-94b3-e06b2d8f3081 | -8.1072 | -43.1646 | 2025-07-17 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 29ffebff-0212-3825-9f53-79a3d36d1f6b | -5.6565 | -43.7393 | 2025-07-17 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e4cbd0b1-8e53-35e3-9df6-ffe478490a25 | -11.1121 | -48.875 | 2025-07-17 00:20:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 63bda313-5ca8-3a55-9469-39094f859cd7 | -22.3989 | -49.7795 | 2025-07-17 00:20:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| fa711ee7-b47c-3c84-978e-85519e0a672a | -8.0886 | -43.1431 | 2025-07-17 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a0b755dc-9626-3958-ae12-3ff5130b43eb | -5.6567 | -43.7161 | 2025-07-17 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 352.4 |
| 1dfdf4b6-0e98-3eaf-baa0-660fda4240bc | -9.2261 | -48.5565 | 2025-07-17 00:20:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 343a9485-877a-3c4e-99f8-fa4a8c27f142 | -11.1125 | -48.8531 | 2025-07-17 00:20:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 4006ffde-c22d-311a-a178-1d52910a76ca | -14.0373 | -51.2287 | 2025-07-17 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bf115437-3fcf-33ac-9720-ffbf772a6b28 | -9.2447 | -48.5764 | 2025-07-17 00:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| b1ebc6a7-ecac-31ac-9c1b-6c3a5bca673b | -12.4701 | -46.899799 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88c47d74-3a2a-3882-a0fd-92d5dce4ca7e | -5.5342 | -43.886299 | 2025-07-17 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99abb4cf-f666-3672-9410-febe7e01d5bb | -8.8786 | -44.7878 | 2025-07-17 00:21:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3e81f7d6-8a30-3a00-a74b-d9d226f009e0 | -12.9909 | -44.856499 | 2025-07-17 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8e1d501-cb61-3912-88e5-776e74e1191c | -3.0184 | -49.417702 | 2025-07-17 00:21:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6eb3a4a-3545-3006-a6d4-9674ef77850b | -3.3797 | -47.466099 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 486d04a7-0c8b-37ac-8334-846e31d46a0f | -7.0839 | -49.145 | 2025-07-17 00:21:00 | METOP-C | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d84f4dc3-87ee-3a9f-a2f6-ce599f266041 | -6.7237 | -44.3134 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f253d6a0-ae11-3a91-bf45-a20a3c8130ac | -4.3001 | -48.086102 | 2025-07-17 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb4b5be5-f3be-3065-a43f-83ed7dabf7d8 | -6.8447 | -44.758099 | 2025-07-17 00:21:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d05b162b-67c3-31de-a650-34de758efd2e | -7.1519 | -46.085999 | 2025-07-17 00:21:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30b5b759-b48d-3191-b00e-f5ad49139d64 | -14.0142 | -51.176201 | 2025-07-17 00:21:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c3159fce-c362-3ce5-a070-0b0b6242cbec | -5.5213 | -43.874802 | 2025-07-17 00:21:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea2c1d99-fa0c-34c2-b8d7-df8735570334 | -6.6269 | -49.723301 | 2025-07-17 00:21:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35a050a9-d41a-36ae-aa86-6eb0c47a8908 | -11.9356 | -48.411999 | 2025-07-17 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa5b35e2-e092-3edc-ad59-d3fc2367b799 | -11.1117 | -48.859501 | 2025-07-17 00:21:00 | METOP-C | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8abae72f-1cef-36de-b5fd-4ea2384f278f | -7.2081 | -45.322701 | 2025-07-17 00:21:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 653880f0-dfc2-3abe-b6bb-a0b59159aad7 | -8.0956 | -43.137699 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
