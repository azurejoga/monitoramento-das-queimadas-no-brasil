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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee7ec66-6c0b-3ded-8cd0-e0c2a680b246 | -4.82076 | -42.91904 | 2026-09-08 04:44:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69514b0f-ebca-3ed1-a583-604ac6afcb9d | -4.74317 | -48.13765 | 2026-09-08 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a4c84d1-bb3e-33ca-ba28-7ee428f61774 | -4.70325 | -49.15448 | 2026-09-08 04:44:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f26de22-a624-3dbc-8fa2-3df9d4f39262 | -4.03783 | -50.88565 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9437b35-089f-39a9-b449-f4d883bb22c7 | -3.54552 | -48.17695 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 0cb93019-fbc4-3ba8-8356-70ff299fd45a | -3.2527 | -50.82451 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87bbd646-1d4e-3745-9ee9-3320c1054915 | -6.6148 | -44.72245 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2d45570-60a5-3733-8c7c-be3611b9d0c1 | -3.71464 | -51.13882 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03355fd7-2784-3b27-bc6c-62f7cce8ed7c | -4.10634 | -49.06474 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fe179209-42b8-3f3c-bc01-21c2772379a8 | -4.97776 | -50.63951 | 2026-09-08 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a2d1153-1efc-3bba-b711-b973d0b51ee7 | -6.64815 | -51.48968 | 2026-09-08 04:44:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53b2294-10a0-3975-af22-bfebbbb6fac9 | -2.87189 | -50.44322 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7a67655-0a18-38aa-bdfd-6b0c8ae9dde1 | -2.97633 | -49.2692 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 662971a3-0057-3035-9d41-67a4d2962e46 | -3.55166 | -48.18151 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 9a797418-e4f8-36ca-9551-c03932354d97 | -4.16515 | -55.84972 | 2026-09-08 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f3c3e5a-712d-38ea-bd99-758704d0d0c3 | -4.7252 | -48.84261 | 2026-09-08 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b074a6-5cbc-3a94-b540-5ae21d78b55c | -2.88224 | -50.44369 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e55ccb0-b6fb-3974-9ef0-57f8fb62e414 | -4.03556 | -50.87634 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a0d26ef-9c1b-32a4-8f34-181ea4eefd53 | -4.34667 | -47.58452 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 472a0fa6-5495-3ce0-b8b3-58e022bbe0a9 | -2.63105 | -46.77214 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b46ab56e-b082-3b81-b2ef-b03befac6399 | -1.19994 | -55.74265 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b0764ce-dc36-3745-9f31-c0e2a30a4fb7 | -4.07876 | -48.95236 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0204b510-e119-3814-8d06-0124ac55600d | -6.61182 | -44.71749 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65713204-a1bc-3228-8d4e-cfe3e3787a9e | -2.95874 | -48.70575 | 2026-09-08 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be10240a-005c-3494-ac19-413fd81cedda | -7.61289 | -47.28928 | 2026-09-08 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a0e3f84-ecda-3c9f-97be-caff74a53034 | -2.88521 | -50.44851 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45d653f9-e972-39e1-bec8-9cda5a280a6a | -2.84239 | -53.99161 | 2026-09-08 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49f60448-33f0-3dd2-957f-3ba40aa50cd3 | -7.60954 | -47.28876 | 2026-09-08 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cf8a36d-399e-3c20-be24-4c9585d20721 | -2.84158 | -53.99362 | 2026-09-08 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b14e31a6-02b2-3c3f-91bf-7e1ac07efc24 | -1.20102 | -55.73604 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0459f26-e081-36e8-a450-3df4f2b22d4a | -2.8668 | -41.74299 | 2026-09-08 04:44:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9030507b-fb6a-3611-b666-3afb6e755c8b | -7.37389 | -47.76154 | 2026-09-08 04:44:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4d622b51-09cb-3e21-a376-202f96427894 | -5.75479 | -49.11222 | 2026-09-08 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 174410e9-939e-3be1-9bee-5641f9de4bc8 | -4.34003 | -47.58347 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8138752-0469-39b8-953b-22f432e6f9ee | -3.54775 | -48.18451 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| dda0741d-77cc-3beb-b4e6-c9d619e8715a | -4.50059 | -42.55349 | 2026-09-08 04:44:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 586db167-c56f-3cc4-910f-868a0ce46fd2 | -4.3447 | -55.22704 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a778f0-3042-3e2c-869d-e9e375563396 | -4.03485 | -50.88068 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38704fa2-67d5-3680-b5f3-3e9ebdabdfc8 | -4.93373 | -42.87354 | 2026-09-08 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 36702514-bf33-3b1b-8ad1-c60a116c1ac4 | -2.8307 | -48.65294 | 2026-09-08 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa8592be-1793-3c76-b4fa-58d27709c895 | -4.43079 | -55.10329 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f173c98-f962-3957-ac65-9e917463c952 | -3.24247 | -47.25013 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 83d842b2-fa42-340c-a7a1-288e0a3b8b37 | -2.48078 | -49.4049 | 2026-09-08 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e7e128e-2692-3d98-9195-528163c9aa2a | -3.01701 | -51.34719 | 2026-09-08 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed0f7835-9523-3a96-a6e1-6d78e80737b9 | -7.37143 | -47.02209 | 2026-09-08 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f7d6e28-a28b-3c06-9843-c5548b70e2ae | -6.19271 | -46.45833 | 2026-09-08 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c18a39b-0572-3f14-80b3-060f2c0cb813 | -3.0651 | -49.52142 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4ad25ef-c762-3412-9e9b-42314e00e12c | -3.33361 | -44.59141 | 2026-09-08 04:44:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f105a83-7594-3a1b-b431-78f68de67789 | -1.86984 | -47.98237 | 2026-09-08 04:44:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2290b17e-53a9-3b81-a58d-08308c3b5fde | -1.20419 | -55.75012 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32474c1e-2371-38ac-8669-2466717ee6be | -2.60623 | -51.21338 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b01acc8-fd02-379d-a8a8-a4469e7f2129 | -4.34375 | -55.23246 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28e88c18-a534-374b-953d-555b53a835f7 | -2.03288 | -48.57681 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0170182-37c3-302d-8acb-80f82309f998 | -2.87946 | -50.46069 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02d7749b-c713-3931-8de0-3eab62f5147b | -2.87921 | -50.44442 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd787e9b-fb35-3e7c-b9da-20eabff6145c | -4.03995 | -50.87262 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ddc75bf-ec9b-3748-8b32-823b35010b68 | -1.09948 | -48.05822 | 2026-09-08 04:44:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c4e849f-386b-3971-b030-d1aa1f2bb4d3 | -2.74067 | -51.37642 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87f1cb43-c96b-308c-9f43-bbe006953b94 | -7.66915 | -46.0494 | 2026-09-08 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df8da5cb-1845-3225-a64a-a2051850f5fd | -4.70267 | -49.15813 | 2026-09-08 04:44:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df03dc3-624b-3025-a74c-421d2ab6a80d | -3.93512 | -48.42988 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86e6235a-f370-3832-b035-d75598da03b6 | -6.33208 | -43.35011 | 2026-09-08 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d8b91b28-9490-3fd8-bac8-131b3ae0e7fd | -7.54317 | -45.00908 | 2026-09-08 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 68af1e11-87ae-34c0-ac3c-cdfecc414792 | -2.63438 | -46.77266 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15751e68-c1c5-3efc-98d4-e4659964fca6 | -5.13906 | -55.97201 | 2026-09-08 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8370c86e-d164-3632-9240-529202d5ad63 | -3.54496 | -48.18047 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 9e8ec5fd-f469-3e37-94d1-2fcd58d318ef | -3.45531 | -59.51362 | 2026-09-08 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e26281c2-bb53-349a-89f2-3d3d386498b9 | -8.27751 | -46.37927 | 2026-09-08 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f6c1f6b-49a2-3ac8-a591-d8266a4ece0a | -3.92707 | -49.05121 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c18d426-f3a6-32bf-b99a-19d86778a934 | -4.11315 | -49.06583 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12c5593d-91e7-3657-80e7-9f94f58df5b3 | -4.03925 | -50.87695 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26a04ed6-3400-3317-b8be-616ba3add487 | -7.61233 | -47.29282 | 2026-09-08 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fbd962b-0568-3981-a02b-79933dcb96ff | -3.15984 | -50.82457 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f5c8fbd-af40-3034-b2f5-6f9a3147cfee | -4.34155 | -55.23055 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 121d2ec2-acbb-3a85-89fd-420c496dcc6d | -0.93691 | -47.19116 | 2026-09-08 04:44:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29177a57-5c17-3286-b117-733cd1e8d255 | -3.69555 | -58.94475 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e11f14f1-bbd8-3c35-9d67-0bb05e34a9ee | -5.94086 | -51.70241 | 2026-09-08 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 366b747e-6539-3f13-b9d6-d1b87d2c5172 | -3.54719 | -48.18803 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 0f0e6c01-44ed-39f2-bb2a-190a9fb1c9b1 | -4.47981 | -48.19256 | 2026-09-08 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ff97260-2fe2-3997-8579-af40867ae193 | -5.37137 | -56.02137 | 2026-09-08 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebdb766f-e433-3087-9087-e0d84907d398 | -2.30497 | -48.57861 | 2026-09-08 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a489de-0285-34a4-87a9-d0bb89ad89e9 | -4.27618 | -48.65892 | 2026-09-08 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bb1dd84-5a14-32f8-ac63-1518d14af8e8 | -3.38403 | -50.45758 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c681f29d-9c3c-3dd9-a269-33824586ed01 | -4.7795 | -44.40011 | 2026-09-08 04:44:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5acd19c-e8a6-3adf-9296-60dc2c8dacb3 | -3.06921 | -49.51814 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2a6057f-cadf-3a2e-86bd-a4a880434250 | -4.48036 | -48.18908 | 2026-09-08 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33216bbd-a101-315d-80cf-be99103d9aa5 | -4.93153 | -42.87568 | 2026-09-08 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e34d79e-36a1-30d5-bc05-8a80d2cb0181 | -13.3982 | -44.14406 | 2026-09-08 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b008696b-ad83-31c3-add1-9cfe181c2f41 | -11.27572 | -45.69689 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74eb3667-d761-3083-9e9c-091e731f2e4e | -9.71482 | -43.45841 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15f5ba94-4dc3-37c0-adec-cd1d2025bf5f | -13.26129 | -61.71446 | 2026-09-08 04:46:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf32be9f-69e0-353c-8ef5-f61fad40c867 | -9.50813 | -41.991 | 2026-09-08 04:46:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb7dcafd-7ab0-312b-902b-d3c1684899be | -9.72914 | -43.4752 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01becde0-0e18-3ca6-9297-7cbd6b801fd9 | -9.71122 | -43.45429 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc7a9f85-e26b-33d2-9fb6-735c20c14491 | -9.71021 | -43.46147 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d88026c4-bbd3-3436-af82-6e1ddc58513b | -9.74549 | -43.47759 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f5ce417-4160-3f4e-9ec0-fb302f7d08fa | -11.36254 | -45.73941 | 2026-09-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22d18067-5d28-3190-9ca3-b0a655734a2d | -9.73827 | -43.49887 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf7de7fd-f3bc-3187-8c8a-8e8605432784 | -9.7703 | -43.42146 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 922f964b-043d-3a07-903f-ab5a9884acb6 | -9.71379 | -43.46564 | 2026-09-08 04:46:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README16.md)
