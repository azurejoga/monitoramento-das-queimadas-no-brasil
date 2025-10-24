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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 507fa249-c76c-3329-af86-8f1ad9d6d6c0 | -3.1306 | -49.51738 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c61bef4-ede5-3328-a368-22b0db73497d | -5.96796 | -44.12919 | 2025-10-24 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43225132-a67c-3353-8b76-f4079951f9d7 | -12.07583 | -46.43745 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e00e0740-cfb7-38e6-b7cb-25107cb1954c | -6.07119 | -42.15019 | 2025-10-24 04:17:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3535f7ce-00d7-3fb7-a909-a902c4ffbe66 | -4.46163 | -43.23632 | 2025-10-24 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9127a8dc-bbae-3900-943d-b5d8c1575f34 | -5.48236 | -48.86856 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a81459a4-9d97-39a1-a977-e69f5efc8b03 | -9.85584 | -48.27644 | 2025-10-24 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 43082d56-1a44-3c35-b649-25d5c2a51b30 | -4.82211 | -48.6799 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58708dce-72fa-3839-b93f-8c44d8945e38 | -3.13373 | -50.62336 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a099da46-0c1d-3fc6-9159-a2f2e262d92a | -10.54748 | -44.85784 | 2025-10-24 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba76874e-ed14-3e26-b470-37704c538cf9 | -9.85969 | -48.27716 | 2025-10-24 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96def244-89e6-34be-83c1-22d050c2fe7f | -12.07054 | -46.40517 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1df0239-638b-3107-96b5-5276b8147e6f | -10.87373 | -45.08261 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| facd6e5a-2f96-3c0c-8fdd-95f7287b6a89 | -6.84532 | -41.55106 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 38df137b-4b7f-334e-b890-38860ae8b508 | -2.8715 | -50.72046 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db312a2c-1116-3b78-aee6-b6c2a26cd92b | -5.62442 | -46.42859 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcb3a518-4f3f-3e4c-96e8-ec244bd89539 | -4.18357 | -46.23107 | 2025-10-24 04:17:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f802f7d7-fc1e-3dfe-8e54-0ed04ecda3ef | -11.01182 | -47.90463 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2c3cf0b-de99-3847-b39c-25b29ee742f4 | -12.02845 | -46.53134 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 43fe7f76-f488-362f-b6a5-82d44b0eec7f | -3.13876 | -50.6242 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5fa87508-e6de-39b0-a645-9c0b458d2c0e | -12.07272 | -46.41338 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2a4c86c-bdca-3836-8602-5ee4d8e6eed9 | -3.80608 | -40.83678 | 2025-10-24 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1e16e98-e65c-3a6e-af94-a839c5b39018 | -2.42507 | -49.28109 | 2025-10-24 04:17:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92b6d376-e0f2-346a-80ec-cb1409e04f8f | -3.25433 | -52.91275 | 2025-10-24 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cac27f4-a897-3a1d-ab41-7bbab52848ea | -5.43138 | -40.90311 | 2025-10-24 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 099af2a1-bd1f-38ab-a25c-f9536b20a4db | -4.61119 | -46.59466 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2af26ea-678f-3417-a546-ec3910e36f88 | -0.6227 | -47.666 | 2025-10-24 04:17:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 345bf349-5846-3387-9a71-182c2fafc88e | -5.43486 | -40.88043 | 2025-10-24 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 058ed465-fa23-3a35-898d-2ebbaa76fe1e | -11.36241 | -45.9489 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6219b8e6-ad9a-3cb0-98ab-73ab32748e32 | -9.26934 | -46.46667 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5359c33a-220a-35df-afda-e32933c4acba | -2.80141 | -54.38213 | 2025-10-24 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6843e5f5-596b-36d0-bdd2-4b7d40d85182 | -6.11393 | -41.74542 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0290eaa9-b24e-3b79-9ca4-d2d5d01172f9 | -9.55623 | -46.69756 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f6c466a-1fe1-3022-adbd-93ee14aa3ccf | -3.13469 | -50.61761 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a5de42f-cbc0-35ed-8d48-a7063443ae0d | -2.81237 | -49.14146 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ff7ef8d-2b59-36f0-8bd9-e8eabaccaa9a | -12.25251 | -47.46325 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 537fe1f5-a89c-3dd6-bc6e-2459a1f45a6a | -9.59777 | -46.90229 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eda2d2c7-bfcd-3311-884b-782d99edc3fe | -4.27338 | -40.70299 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5419aa9b-82fb-36bb-961f-44c363ff1f92 | -4.05602 | -46.74985 | 2025-10-24 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69953909-7faa-3a2d-a322-0585c620106b | -10.87302 | -44.41098 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4986202-b479-3dea-8fb3-3bc6d2cae088 | -3.21752 | -46.80617 | 2025-10-24 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 535a9489-ecf0-398c-a2ba-f7771bc0555c | -3.08839 | -49.2565 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 269c9fbc-b8cc-3954-a7c6-070113d10209 | -11.00893 | -47.89919 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a73ac22-83fc-3448-af52-ddb6be198c32 | -11.4637 | -43.70462 | 2025-10-24 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89626cfd-9db8-3d7c-93dc-87e918e6fa21 | -1.55115 | -55.41463 | 2025-10-24 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 491572cf-f898-3c82-b435-b770ef5e52e5 | -11.36643 | -45.94574 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a41c569f-3b59-3bcb-9308-7974c7294fae | -3.48853 | -50.04985 | 2025-10-24 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74fd8d5f-54bb-3d7c-a3f4-1f2422a76d9b | -10.881 | -45.08015 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5d38846-bcb2-3469-bc5f-820678c38553 | -11.3522 | -45.94715 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58aef693-70e3-33bc-a5bc-92eb2da869a6 | -11.33347 | -49.08413 | 2025-10-24 04:17:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3febf07b-180b-32eb-98b9-96c2fe50a50c | -12.17734 | -46.56432 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3323129e-e35c-3ad1-8caa-8f167e598fec | -5.40651 | -46.41375 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40ac0b54-d032-305a-9c4e-eac9e30c300b | -10.02647 | -47.08524 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86873ac4-71d7-3740-8f34-aeb78e017e68 | -3.47858 | -50.08046 | 2025-10-24 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e98d9869-05af-3c0b-8fda-f53e344139c9 | -3.60149 | -48.98938 | 2025-10-24 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad7f3d07-f849-39e0-af60-f2cf111a94bd | -9.23261 | -51.83239 | 2025-10-24 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2270722a-f620-37cc-86a0-eb4b34e5bd46 | -12.31298 | -47.26994 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a02ee8e-caad-3e89-b5aa-295dce7b36e1 | -9.60495 | -46.90355 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9bcbd96f-00e8-3a06-a71a-b1f5f50acf24 | -5.22298 | -48.00699 | 2025-10-24 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0162f56-8c02-3bff-8162-3644923fbca2 | -5.45294 | -45.40957 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 059f8ccf-941f-3455-9c7b-d71e9ebecf15 | -10.11481 | -47.73919 | 2025-10-24 04:17:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01a5f55b-96d0-313f-b12e-b7ef54065ce7 | -12.15625 | -47.02121 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdcd33a5-2c14-39ee-a375-5b8641d7a53d | -4.37574 | -50.35534 | 2025-10-24 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bf253d7-866b-3627-a38c-7455b18420b0 | -9.30681 | -45.20378 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b1ce657-12c1-3685-a8e9-f72632c51fea | -3.81716 | -44.08403 | 2025-10-24 04:17:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33014e3e-e154-3a31-9e00-fb412bf4b4c9 | -11.1441 | -44.94028 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 081e34f2-9c43-3139-aa81-a8b5598ec8a3 | 0.36327 | -50.93636 | 2025-10-24 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1786f41d-1029-3448-9aeb-f4ea0ddcaea8 | -4.38135 | -43.29808 | 2025-10-24 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4b177b6-2c2b-3d4b-b6da-4b7025b884e5 | -12.15829 | -47.00906 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e125b67-6e04-3ff8-a4aa-7564be7256e7 | -13.18807 | -47.75148 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6debfd5e-7bdd-3dc3-80f0-5f4555ec44f5 | -14.25348 | -44.08974 | 2025-10-24 04:19:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fee2c96-15bb-368a-97bc-651673407999 | -6.79954 | -45.43236 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ecb10f9-8604-3f9f-aa45-cb8d1fc78686 | -7.62344 | -41.84499 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3defd78-3c33-3607-a323-bba39197b431 | -6.81677 | -45.32629 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75785abe-be22-3d3e-82af-688afc672269 | -7.63441 | -42.20194 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8143edf-3ad4-3842-aa54-d36906cbf40d | -7.62967 | -41.8497 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 697a734a-016d-32c1-91a6-515dcac2c041 | -12.81084 | -50.95509 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0dc9fa2-cc75-3350-86a1-a1edb91ab1c4 | -13.18733 | -48.48934 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5ad04be-32d8-3b6b-9be0-90754ac82232 | -14.54203 | -48.02419 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0df1114a-86ab-382f-956a-8a65d16e8199 | -6.78041 | -45.48418 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 291a6b64-6620-3cb7-bc4b-3b0f62bb0d00 | -6.76811 | -45.49392 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d4fe5b7-1d0b-3d59-9745-ac979ce864ee | -14.46291 | -47.91734 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54696980-bdc8-35b4-8a54-22ceffcfe1a1 | -14.5137 | -48.34648 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03f62d8a-e880-33e8-b145-a126bba38f31 | -6.88869 | -43.61412 | 2025-10-24 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5c61a306-c5da-3249-bd78-81721ed87535 | -7.62854 | -41.85699 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eea6d548-1535-32c8-86ee-eeb2513e2430 | -16.47688 | -46.47553 | 2025-10-24 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2237d850-943d-3873-b1ab-b7805b17f1cd | -6.27722 | -47.01296 | 2025-10-24 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 656b3e65-f61d-3a5d-aae9-563bbfe272a2 | -15.03075 | -48.01503 | 2025-10-24 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 664d7137-58a5-393a-a79b-024ab967db2f | -15.22873 | -47.9131 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27502896-51aa-309f-b0b8-4df075d99789 | -8.64943 | -44.79514 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52d31712-1cfc-319b-9e3e-eb773eba75cb | -14.74833 | -46.61342 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eeec9ab-b669-3d99-99f8-cb3d66c39741 | -12.81239 | -50.94654 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| be2a2090-f499-386b-a29d-f1f03a1eccd7 | -7.44947 | -47.26194 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77989f45-7665-3c20-a5b0-d62bc7bc65f4 | -7.55582 | -47.36694 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d51b7a3d-9837-386e-a431-8b8a59bab26d | -15.60011 | -48.04692 | 2025-10-24 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8b6f182-b654-388a-b70f-c9d000e31da1 | -7.78484 | -45.40983 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c619ea38-5159-3192-9596-50ec378f42f8 | -15.44656 | -48.57351 | 2025-10-24 04:19:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fea89f5-e06e-36fb-898d-7ef6b7b71e2e | -12.67426 | -48.63249 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32f2d5f5-2b59-3f57-a78b-23458f892994 | -6.79449 | -46.46791 | 2025-10-24 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2180512e-4535-323a-b2b0-e71e2cc4097d | -6.77096 | -45.49832 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
