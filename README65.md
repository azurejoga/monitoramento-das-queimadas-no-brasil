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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 129330ab-fd5e-39b6-a448-54c914ac0a31 | -10.31679 | -50.26663 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5028ac61-2864-37e6-b6e1-36cec26d9e4d | -8.43477 | -70.12574 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e0f91cd-5b34-380a-bfdb-485c6dad7f42 | -10.0581 | -59.35785 | 2025-10-06 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a9f1556-897e-3c34-85e7-da9f5b267286 | -8.67586 | -49.46761 | 2025-10-06 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4e40f93-6311-3538-b4e7-5f2eae24ab37 | -10.23089 | -52.70232 | 2025-10-06 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aab11a4f-c275-354a-885a-415bd7301395 | -8.60797 | -54.96558 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f25b081-0653-394d-a280-3d2f827a910d | -8.88182 | -50.89446 | 2025-10-06 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efe2a5af-49e5-3a0b-91b2-2236fae4bef1 | -8.06928 | -54.92381 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 988c77e5-5f9e-3bf2-bdcd-769bf2a54e95 | -9.15207 | -58.30933 | 2025-10-06 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8290041b-aa16-31fb-b7e0-c3bcbbe7497d | -12.40973 | -51.12856 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6427d73a-5b1d-3c2a-b21a-80f5f7bce016 | -8.61189 | -46.27695 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1487c9ce-ce8d-3a93-8b5e-73fab7d7db32 | -10.06288 | -57.89843 | 2025-10-06 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90a2c53e-d922-33a3-b376-961591fd2516 | -9.24984 | -60.27785 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f959b5-af05-37e3-9491-e0f46dbddae1 | -8.15364 | -54.8451 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9958b404-2bbb-35f6-9d9b-09ad5a9acd93 | -8.90083 | -50.67091 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e080b2c0-916e-30cf-9fb8-39007fee1ddd | -9.25719 | -51.80844 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf603509-b364-3f0f-ab6b-0ee8604f8b0d | -8.61045 | -46.28816 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d56e290-8815-3a91-81fc-b51a61c7ed4a | -9.24928 | -60.28138 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257ed239-76f4-3a08-99c8-b919199a9cdb | -9.54639 | -54.59325 | 2025-10-06 05:16:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 150ede7a-d6e2-33c0-8df0-7807c55cc3f6 | -5.64647 | -50.30696 | 2025-10-06 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52eebd9d-cc65-3bce-aaa4-6ca256778cd9 | -10.59971 | -54.36093 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 995a03f0-0378-3270-8a7d-cd536db50b47 | -9.06445 | -54.52976 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7db7bed-0be9-3566-8ef7-e131e5e84b16 | -8.44576 | -70.13232 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c5762d4-94b1-3194-b2e0-68123f97f1fb | -8.56564 | -46.2588 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9527236-5ca6-3345-8cf4-cac4e921a48a | -9.6724 | -49.95845 | 2025-10-06 05:16:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae14cc85-3e1f-377d-afaf-dd068ad77460 | -8.88592 | -47.62329 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f37176a-d1df-332e-9169-953ab14bb2c5 | -9.55944 | -50.78223 | 2025-10-06 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5bcc691-9155-3de6-b64b-8c685b68d294 | -10.80358 | -48.81998 | 2025-10-06 05:16:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7af52815-3535-355c-91b4-35ba8a1ce97d | -7.35584 | -64.65694 | 2025-10-06 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af08f231-a8a1-3636-96e1-e0537b501f73 | -9.07826 | -59.02298 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78a63c44-6c0b-3d77-b091-e222854bb42b | -8.62895 | -46.31657 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6a8331b5-9d0e-378b-8baa-ef1e2e926372 | -9.61881 | -57.20201 | 2025-10-06 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85995fe3-8737-3003-a253-bc41ee1532e8 | -11.44192 | -55.04398 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a320e7e3-0bc2-3a91-840a-7f824a39e49f | -8.62614 | -46.32744 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 03072ce4-2207-3bdc-993a-5d31b0a5dc9c | -8.61956 | -54.96723 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5762e607-0c29-31d4-ba02-2031f7bfec2f | -7.3552 | -64.66076 | 2025-10-06 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 633a72e6-1ab0-3d65-afb5-4aa194f66559 | -10.46281 | -57.49969 | 2025-10-06 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 859b0b5a-eab9-350a-ac56-e2ec5f1ec533 | -10.45611 | -51.24691 | 2025-10-06 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fee188d3-1e75-34c9-bef0-fe0542b4c834 | -9.54688 | -54.58978 | 2025-10-06 05:16:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b777600-d1b0-3665-afa2-3ea02b91e917 | -12.38292 | -51.08479 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22e4c741-96a4-3868-9853-9406bf9d30be | -10.30593 | -50.2652 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61370f3c-7775-3455-8f52-458de3514064 | -9.96922 | -48.75009 | 2025-10-06 05:16:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b57396d2-23ff-34bf-a98d-e4c363c3babb | -10.96662 | -60.69858 | 2025-10-06 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad1c65b6-0d41-339d-a442-f531bb231a70 | -9.26755 | -51.8045 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52dae126-ada2-37d2-8315-171ff869ac5e | -8.54467 | -46.26001 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1d4f433-5b83-351e-89e9-96668beed449 | -10.80848 | -48.82964 | 2025-10-06 05:16:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ee6f7ec-cdd0-397c-9cb0-b248f47f7934 | -10.75303 | -49.70119 | 2025-10-06 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b0f22c8-17d6-39e5-b945-eb9a46744330 | -8.83205 | -62.37204 | 2025-10-06 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89aac3fc-ec9c-3ed3-96ae-c301a4686807 | -8.90285 | -50.60805 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c47fecb2-61ef-3e36-b8b6-8267ffca7d64 | -10.42595 | -50.34881 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8c34e66-a9ac-393d-bef9-cfb60927111f | -9.27728 | -51.8012 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef42085b-f44d-3d34-8d45-849860aa0527 | -8.62136 | -54.99468 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d201182a-dad3-38c9-bd93-774dfe4341e9 | -5.33353 | -47.28516 | 2025-10-06 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 7551f3c7-7c79-3578-a22c-d3417629cf21 | -8.61757 | -46.29652 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 642c9399-5826-38e7-9943-64fa61c55989 | -9.26694 | -51.80518 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c745d29-7cf9-300c-a982-4da347b5faf2 | -11.01022 | -50.68001 | 2025-10-06 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1836bbb-1856-3a35-8f7a-68e95c4fc29a | -8.63045 | -54.62519 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83cf1eeb-de05-3d64-812b-df594a3479aa | -7.57243 | -63.39195 | 2025-10-06 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb733aba-4099-3fdd-b188-419e2282df5c | -8.6275 | -46.32827 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b99891e-5dcb-38b4-b4de-8542e0ff511b | -12.41136 | -51.11542 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90c2a7f0-fb9d-3d37-9d82-dd05082a0883 | -10.36747 | -51.18472 | 2025-10-06 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a61ce195-ce2f-3ac5-83f7-6c086c479834 | -6.52558 | -55.03012 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1214e479-884f-33d6-ba12-55af7d281141 | -11.91991 | -46.641 | 2025-10-06 05:16:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96ee37b8-b021-308f-bd39-aaa56d7ba85a | -8.60726 | -54.97038 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 022bd719-d0ff-3ecc-b98f-2300f04dfdb9 | -9.33679 | -54.51982 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47bfd2df-154a-365a-8d97-f341c1396dce | -7.99881 | -45.48232 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 595329e2-1263-3293-8896-d62a26610bad | -12.25212 | -49.21789 | 2025-10-06 05:16:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f59b734-5e02-3793-b881-ab767bd4edf5 | -8.16652 | -55.06915 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed9f3504-e4ce-3569-b6e4-8e2a283c7b5b | -8.61006 | -54.96351 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbd2aa05-159f-3366-a648-fb37d0f5e120 | -12.25529 | -49.2159 | 2025-10-06 05:16:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be08d0ec-44d1-313a-b490-a68b087def0c | -10.37425 | -48.14799 | 2025-10-06 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13593747-c99f-3727-b098-1d20f08b30fe | -10.80903 | -48.8252 | 2025-10-06 05:16:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 879cf61f-b93e-3c6e-886f-14f5e322b002 | -8.62216 | -46.31548 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| def6c1f8-253f-39ff-9c29-ac8e8a6d0295 | -7.9917 | -45.48158 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f8e374b8-1ca1-3bbb-b0d2-98e3f98609f9 | -5.62766 | -51.09066 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6112f1c6-b001-373f-a3c5-e430c06ae99d | -8.61779 | -54.96462 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e4bd31a-0e21-3a12-8e50-d35ddae86699 | -6.54947 | -47.85538 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8ab25f37-18ec-3e0f-b7b3-9b14c6480ff0 | -12.57122 | -48.14318 | 2025-10-06 05:16:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 78c6362d-bd97-3bcd-ace5-f373bb36b80a | -11.02159 | -46.54083 | 2025-10-06 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2022c756-c0c5-3812-98e7-17efba91d1b6 | -7.57787 | -63.38297 | 2025-10-06 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92228aa3-4abc-33f7-8b83-07096fae3e8d | -11.00401 | -50.68604 | 2025-10-06 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc7078cb-ef9b-3a0f-a871-b06e8e1de05f | -8.61682 | -46.30263 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1330b86d-04d3-3a7f-8ae7-9b49e43e6784 | -11.50017 | -54.46832 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e6e3745-782a-3799-8ea1-635ff243f753 | -10.59558 | -54.36037 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e261cb9-6374-3788-8ca5-074622c1da2c | -10.32361 | -50.27159 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3973fd3-4028-3871-8161-469b68e7f392 | -11.91922 | -46.6475 | 2025-10-06 05:16:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d12e82ff-1cc3-3a97-956b-9b06e0595e5b | -8.90123 | -50.66785 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 180935d0-d2f4-377f-9727-ae3e3178da29 | -11.06498 | -47.91807 | 2025-10-06 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3466938-a383-3a0e-a951-f859167b425d | -9.22811 | -51.84163 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35d7bf53-55d7-363b-b13d-b4bf04efa9e5 | -8.62205 | -54.98989 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| affe6df3-094a-36a3-82cb-2801709d7321 | -11.40316 | -55.08912 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a37141d-bd42-3a4a-9008-99738bfb280a | -11.50483 | -54.46515 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88943acf-8f79-3279-b6c5-edfa093be8dc | -8.61256 | -54.96132 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 343ef37b-50d1-3e5b-9c19-453cd22b1a98 | -10.37553 | -48.14968 | 2025-10-06 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c414645-6af7-324d-95d2-24b9412cb040 | -9.31207 | -59.67411 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d63c3a6-bc25-377b-9fe8-c56397bb4d79 | -9.98034 | -55.28661 | 2025-10-06 05:16:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39a66595-88ad-367c-a532-a71a1aabc947 | -5.33293 | -47.28947 | 2025-10-06 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f7fabbd9-cf63-3e5b-92ff-929697fb98a2 | -8.62977 | -54.99094 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d886638-967e-37d8-a152-15559b5f66a1 | -10.59609 | -54.35675 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8ee8084-7aa0-34e0-80d0-c6cb66ccc58b | -9.27659 | -51.80635 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README66.md)
