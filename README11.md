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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac5876eb-2be3-3b2e-a50b-3233221c3ded | -10.6659 | -42.3112 | 2026-05-21 13:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| e0b54660-5a0a-3591-97f3-ab4744f23de6 | -9.95 | -52.4602 | 2026-05-21 13:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7daa5696-5fd8-36ac-ae20-e5dc97d8d1d5 | -11.1267 | -46.7048 | 2026-05-21 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| dc6e6096-c818-3bd5-9f3d-89c4958b4489 | -11.127 | -46.6823 | 2026-05-21 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 317.8 |
| c139f8ed-8f33-3c1b-9a0d-beae97b4e60c | -11.1425 | -48.1263 | 2026-05-21 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 6a01938a-fc19-33eb-bcfc-d1e2db4730a6 | -9.95 | -52.4602 | 2026-05-21 13:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| bbe1b368-1a0c-3e44-ab5b-e6655cd96429 | -10.6663 | -42.2871 | 2026-05-21 13:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 4e023696-bf4d-3f1e-867a-ec2652d9e73e | -11.1428 | -48.1043 | 2026-05-21 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 2209b31e-6d95-3b61-9191-4263763506c6 | -11.2743 | -49.4642 | 2026-05-21 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| dc275c07-2240-36cc-8e4f-c8ff1c9e020d | -12.6011 | -44.521 | 2026-05-21 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 4a3aa89e-10d9-3f46-9c69-f0818a8968b1 | -11.2746 | -49.4426 | 2026-05-21 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 659aeb6d-b1de-3d74-9d74-0e6b395b1084 | -11.127 | -46.6823 | 2026-05-21 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 462.5 |
| 3d637083-fc31-3d05-b22a-b8ba85403102 | -11.1267 | -46.7048 | 2026-05-21 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 2be0b31b-72ed-3da4-a009-51b79b9f9b34 | -11.2743 | -49.4642 | 2026-05-21 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 53f9d01d-d3f5-382d-9a96-823e23420787 | -10.6663 | -42.2871 | 2026-05-21 13:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 133.9 |
| a13e17f1-630e-3516-a1e0-deacfc70c39a | -11.2746 | -49.4426 | 2026-05-21 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| cd60f951-abc9-3c19-a067-0e5d750ccaad | -11.1428 | -48.1043 | 2026-05-21 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 0330864b-ec8a-38b5-979d-e7a2ff68f0c1 | -9.95 | -52.4602 | 2026-05-21 13:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f2c52ef7-4768-33b4-b5c1-58e6c36871c7 | -11.1425 | -48.1263 | 2026-05-21 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| c75afb38-5afb-31c0-9fb3-2a7cf8b7c7d9 | -11.1428 | -48.1043 | 2026-05-21 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 31c1b012-48bb-3de5-84a2-2c16ec197160 | -12.6011 | -44.521 | 2026-05-21 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9bd0ae37-8f5d-38b5-b78c-9537570ce61f | -11.2743 | -49.4642 | 2026-05-21 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 86fdf8d5-d3d0-3782-9839-6269305e3033 | -10.6663 | -42.2871 | 2026-05-21 13:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 104.7 |
| a2175cd0-7f28-393c-9355-c3f667f226bd | -9.95 | -52.4602 | 2026-05-21 13:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 20bdb039-220e-3ceb-b55d-ac3dff7aaf24 | -11.2746 | -49.4426 | 2026-05-21 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| df9188bb-1072-39a4-bddc-8ef755b51aa8 | -11.1425 | -48.1263 | 2026-05-21 13:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 9aefcd30-0b69-369e-86a1-c6c9502d4467 | -11.9741 | -47.3762 | 2026-05-21 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 329aee1a-23f9-3f9e-ab28-20f07c0889d4 | -10.5479 | -49.9114 | 2026-05-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 34d258b8-93db-3705-a260-46c6072740ef | -11.2746 | -49.4426 | 2026-05-21 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c8322e9e-b0b0-3919-b1e6-a11dfee4414c | -10.6663 | -42.2871 | 2026-05-21 13:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 150.7 |
| e5e3ec61-4af2-3e61-a093-4c6b3727045e | -11.1425 | -48.1263 | 2026-05-21 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| bcfb4c8c-5b72-384c-83c3-2b6397f53f95 | -11.127 | -46.6823 | 2026-05-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 318.4 |
| 4bbd01a9-2fe8-375f-8051-99cfaa68024d | -12.6011 | -44.521 | 2026-05-21 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 44aa44c7-34c7-3bb8-aead-a1b8baf2d94c | -12.424 | -47.9159 | 2026-05-21 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 079f7312-81f6-3963-8aa3-9bb7bf58de3c | -11.2743 | -49.4642 | 2026-05-21 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4c1b1686-34db-3847-95f1-ddfe6bc6f8fb | -9.95 | -52.4602 | 2026-05-21 13:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 31da7fbc-f0ef-3ef0-a491-92f3552353ed | -11.1428 | -48.1043 | 2026-05-21 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 60258893-85ee-3469-83e8-77a1263db13b | -10.666 | -48.249 | 2026-05-21 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 38628cbc-9352-32f3-a03d-d27f1d379b45 | -11.2743 | -49.4642 | 2026-05-21 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8aa2b44d-622e-3bfb-ac9c-123e36336087 | -10.6659 | -42.3112 | 2026-05-21 14:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 82d42d2a-2274-3cae-826b-a24a8b3ca92b | -11.9741 | -47.3762 | 2026-05-21 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| d28002b8-aa61-3ce4-a865-751975be2930 | -10.6663 | -42.2871 | 2026-05-21 14:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 174.1 |
| 2056f774-a33b-302f-a1dc-3caee4d1d622 | -11.127 | -46.6823 | 2026-05-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 4e4efa7d-b02d-3ea3-9430-aa7f658e7a18 | -19.7799 | -54.0749 | 2026-05-21 14:00:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a724a4e2-ab59-30f9-8ff6-1908047a0290 | -10.666 | -48.249 | 2026-05-21 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3a7305a3-0ed7-3f9e-ba34-2de277a36e4f | -12.424 | -47.9159 | 2026-05-21 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 58c544ed-a7c4-392c-9a42-99bf3788c50a | -11.1428 | -48.1043 | 2026-05-21 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 98abbb66-313f-358d-9bba-cb1985af740f | -11.1425 | -48.1263 | 2026-05-21 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ceff72e6-27b8-3d5e-bc5e-b1d66a6c2b72 | -11.2746 | -49.4426 | 2026-05-21 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 99d4defa-64a6-3979-89e0-3b522915d5ed | -9.95 | -52.4602 | 2026-05-21 14:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5b68d9c4-8368-3c83-a95a-b9905b54484a | -11.4534 | -52.9212 | 2026-05-21 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 53c1f635-9f3a-3b30-884b-9f39a899a348 | -12.424 | -47.9159 | 2026-05-21 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1ed154ed-36ff-34da-b9e6-52ce962fc251 | -12.6011 | -44.521 | 2026-05-21 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c562a7fa-f6f5-370a-b654-92ecef0c6751 | -10.6663 | -42.2871 | 2026-05-21 14:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 102.6 |
| addf0920-aa61-3061-8a3f-59739017849b | -11.2743 | -49.4642 | 2026-05-21 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 711593b6-33ff-390d-b59a-4f8ef94aa1ac | -10.666 | -48.249 | 2026-05-21 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 28afbf2b-a8e5-3bdd-9016-2f67df6ae3dc | -11.1428 | -48.1043 | 2026-05-21 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 83844d8b-ecd6-3cc6-bbbb-8c15b8dae6ad | -10.4988 | -49.3567 | 2026-05-21 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a0e8cde5-b72c-386f-8a52-66cdf99900b9 | -19.7799 | -54.0749 | 2026-05-21 14:10:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 69913cef-7c3b-3b17-9179-a94e4d73856e | -11.127 | -46.6823 | 2026-05-21 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6ffd5d34-9986-3214-ab8a-c5cd6bded132 | -11.9741 | -47.3762 | 2026-05-21 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 80d490e0-1781-36d4-9590-31846e4dbaf2 | -19.7597 | -54.0782 | 2026-05-21 14:10:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 5bcda836-9f50-3420-9994-7904bdb26bbd | -11.1425 | -48.1263 | 2026-05-21 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 78174d10-83c1-3490-9adb-c4410e94b39b | -10.4798 | -49.3587 | 2026-05-21 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 9fc9aab9-ea67-30dd-9613-48f23b6e8f50 | -10.666 | -48.249 | 2026-05-21 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 9251514a-b04d-3dcc-9b77-bf5e1482d789 | -11.1267 | -46.7048 | 2026-05-21 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 369.9 |
| 87124446-300b-3cc7-8d1d-15ff6024c392 | -12.6011 | -44.521 | 2026-05-21 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 604171d0-8c77-37ad-abc9-6ae31a41e4f4 | -10.6659 | -42.3112 | 2026-05-21 14:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 7fc365b1-967b-3549-8a49-31d8a5bdd461 | -10.6663 | -42.2871 | 2026-05-21 14:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 184.4 |
| 150a5143-8e8a-38e3-8a28-e92a261de906 | -19.7799 | -54.0749 | 2026-05-21 14:20:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 17a812dc-d225-3d5a-930e-629980c3ee77 | -11.1425 | -48.1263 | 2026-05-21 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 282e57d5-daab-3436-832d-966774724970 | -11.4534 | -52.9212 | 2026-05-21 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c59d6dd0-54eb-379a-be12-4fcd613fb9d5 | -9.95 | -52.4602 | 2026-05-21 14:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 50072f8a-ce67-3566-beab-b28dd0ae6127 | -11.1428 | -48.1043 | 2026-05-21 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| e02ff927-5693-38f9-b9a3-48dcc38e4053 | -11.1428 | -48.1043 | 2026-05-21 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6c4a55e1-9ea9-3bd6-a141-4546bf816095 | -11.1425 | -48.1263 | 2026-05-21 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a24eeb15-cd41-35e5-9d57-b8de83ffe2c6 | -10.6659 | -42.3112 | 2026-05-21 14:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| a7a58f5e-231f-30cd-a675-3cd320fc786c | -10.4988 | -49.3567 | 2026-05-21 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 44179988-63dc-3a68-90f8-b0bb87d60afd | -12.6011 | -44.521 | 2026-05-21 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c7ea00c1-1e51-3cd7-9ab4-725f0b1ad862 | -9.95 | -52.4602 | 2026-05-21 14:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 84c99519-3fa6-3477-8786-fca5ab5f8d22 | -10.666 | -48.249 | 2026-05-21 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 79c593b7-3ab6-3a7f-b01f-757076ad5c2a | -11.1425 | -48.1263 | 2026-05-21 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a5bbdb2e-a13c-371e-b200-8f30f62504e9 | -10.4988 | -49.3567 | 2026-05-21 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8f823fb8-bec3-3bb6-bb5f-c045041b6993 | -10.6663 | -42.2871 | 2026-05-21 14:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 4b1ae32c-eaa0-37db-801e-ee6d2ee48608 | -11.1428 | -48.1043 | 2026-05-21 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 50659e7e-633a-3fdc-9cf6-c1155fd26b7f | -10.4798 | -49.3587 | 2026-05-21 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 763179da-4f79-322c-b9e6-00423e363233 | -10.666 | -48.249 | 2026-05-21 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4f33b891-2110-3458-beac-3c622071e5eb | -12.6011 | -44.521 | 2026-05-21 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| bb5440e2-9abb-3c9e-a3f2-e2b9e5586724 | -11.9741 | -47.3762 | 2026-05-21 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fdac13dc-70c6-3a31-9a14-8986c0d9fea7 | -10.4988 | -49.3567 | 2026-05-21 14:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f45079b0-6eef-3aed-9c3f-739b70a68d42 | -9.7368 | -47.029 | 2026-05-21 14:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 55a3eee7-2118-36eb-bcc7-3892e70f124d | -11.1428 | -48.1043 | 2026-05-21 14:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 767cff95-9fc4-36c9-baff-c2c08c9890b1 | -12.6011 | -44.521 | 2026-05-21 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| f9927054-5573-38ff-8a2a-e15b276cc67c | -10.666 | -48.249 | 2026-05-21 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 9cc7dccf-dafe-3d28-afac-4907cd2c2c0b | -11.1425 | -48.1263 | 2026-05-21 15:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| dd845963-a373-3154-a5f5-04d9ba8e25fc | -10.4988 | -49.3567 | 2026-05-21 15:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ab4ebbeb-41f1-3594-850f-ff2fba0208d9 | -10.4798 | -49.3587 | 2026-05-21 15:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7f206734-82e4-3419-b98a-6b47b3c39686 | -10.666 | -48.249 | 2026-05-21 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 523847ad-7c95-3f27-a312-fa025eef9abc | -11.1428 | -48.1043 | 2026-05-21 15:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e9c7cfae-b6bf-3562-88ff-ebf8330a30a7 | -10.6663 | -42.2871 | 2026-05-21 15:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 117.5 |


[Clique aqui para ver as próximas entradas](README12.md)
