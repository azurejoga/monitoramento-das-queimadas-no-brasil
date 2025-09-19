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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa317525-44ea-3565-951c-0f40ed99932f | -19.91695 | -44.14993 | 2025-09-19 03:36:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73b08dd9-804d-3edd-8f25-4b940e3c3a40 | -16.51886 | -43.54736 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13fe92cd-56a4-3141-a6df-61e2aa4c2ef7 | -19.59557 | -42.10149 | 2025-09-19 03:36:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| 8e960316-d5da-387d-a574-35d363ec6970 | -17.22033 | -45.95379 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ab4fc30c-dd2a-3719-82e7-4a98f4f0bbdb | -22.03809 | -45.59548 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 36746dfb-c213-3891-83aa-2ed58e11b6ff | -22.33741 | -46.77329 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d26a3aa0-405e-3c1f-b37d-1b7bb05c4942 | -22.3497 | -46.74596 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ad381bb6-e63a-3699-b792-8835eedda3c2 | -23.63653 | -47.22096 | 2025-09-19 03:38:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38acdfef-c1b5-3077-9bac-513b6432804c | -22.3337 | -46.76353 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75810b63-b104-3bf6-a017-5f62fd1b5713 | -22.344 | -46.77063 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 200f3329-9a62-3a3a-8e32-1c30fd850630 | -23.67507 | -51.73162 | 2025-09-19 03:38:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4b8549a6-f4fe-3ecb-88db-505f5a0620a7 | -22.34035 | -46.76059 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bae83bf4-d850-3fdb-a17c-8e826cca1d02 | -22.35059 | -46.74211 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4f738903-f107-3da7-8ae4-36e0706da345 | -23.67707 | -51.72408 | 2025-09-19 03:38:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6705dfd5-c014-3f1d-bb6f-14db0cc9d437 | -23.67833 | -51.72364 | 2025-09-19 03:38:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 69d5fd48-ba18-396c-84fc-ac4442aef03a | -22.33938 | -46.76477 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e7cc4f9-788b-3400-8c9c-788debfad677 | -25.68676 | -49.90622 | 2025-09-19 03:38:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 59a3778d-4b15-3a4e-8aa1-b163a9f5c110 | -23.67624 | -51.73132 | 2025-09-19 03:38:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1ddab017-2f62-38df-a937-33e89b90c774 | -25.68979 | -49.90247 | 2025-09-19 03:38:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79886b32-46af-351f-bbc3-bf9e31372192 | -23.38801 | -47.14434 | 2025-09-19 03:38:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0563f5d5-dff4-3aa4-bc53-67d90177ffbb | -25.68816 | -49.9007 | 2025-09-19 03:38:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f761a5c5-ae03-304f-b700-547e60f07819 | -22.3384 | -46.769 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d723118-c231-349c-b008-100d035e2717 | -22.34129 | -46.75653 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3cc82bb2-876b-3677-9990-d51f762435a1 | -23.38711 | -47.14824 | 2025-09-19 03:38:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e44fea3-ddb2-35a7-9953-6a1a8613095a | -22.93384 | -46.95959 | 2025-09-19 03:38:00 | NPP-375D | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f79a9e58-ef79-35aa-8a13-f9a02d1d249c | -25.68358 | -49.90051 | 2025-09-19 03:38:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7ce3183b-1e4e-3658-a21f-4ef53b34a9f4 | -22.345 | -46.76633 | 2025-09-19 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34528f70-e5b0-3d1d-ae44-de356c0f8a21 | -23.64138 | -47.22232 | 2025-09-19 03:38:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 68a46b95-8c7f-3079-ab2a-dc5706a43ba9 | -23.64214 | -47.22253 | 2025-09-19 03:38:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cfb2cd6c-d7a2-3a63-8720-cecbfeadb91b | -10.2982 | -50.2158 | 2025-09-19 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 51a08ded-43db-3f88-9f3d-306ccdfed468 | -8.1381 | -46.771 | 2025-09-19 03:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ac50dd53-d711-30a7-add8-192cfa904619 | -11.2147 | -49.6441 | 2025-09-19 03:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 5a54298a-0dc7-35db-b555-eb0aa74d018a | -12.8777 | -50.5422 | 2025-09-19 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 737913be-792a-333f-a717-de5bec16c83b | -11.215 | -49.6224 | 2025-09-19 03:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| a80801ab-39ea-3f88-8dda-1314a8391f3b | -10.3168 | -50.2352 | 2025-09-19 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 324759c5-1520-3897-9830-eb28317f988b | -10.3171 | -50.2138 | 2025-09-19 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3f30d0b4-2c4e-3a3a-a8ab-d7a4adb82c3f | -12.8969 | -50.5398 | 2025-09-19 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a1a82184-11e2-3f23-9d77-3f5a9c6ad7bb | -10.2979 | -50.2372 | 2025-09-19 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 65f5f4b1-7b60-35d8-8abc-498eb4039654 | -17.2363 | -45.9476 | 2025-09-19 03:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 4a77ccd5-971c-38e1-a644-75be84db0ca0 | -7.5705 | -45.4786 | 2025-09-19 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| cb545ee0-87eb-3821-b712-a5e6188317c8 | -14.2666 | -51.3479 | 2025-09-19 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e2162597-0d98-342f-afc7-98706cf07525 | -12.8969 | -50.5398 | 2025-09-19 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| c23b3c1b-8550-3234-b024-3a8130a1939c | -10.279 | -50.2391 | 2025-09-19 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 369cf098-bcde-310e-bab9-ebff93bc89b7 | -10.3171 | -50.2138 | 2025-09-19 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4af1b79e-0a4e-33d7-8f32-033e07ca3ed6 | -10.2982 | -50.2158 | 2025-09-19 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 28241ffd-2926-3ae0-b16b-4267a6ee9820 | -6.5631 | -51.1126 | 2025-09-19 03:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 37d7fa37-8fe0-3579-981b-824a9ddcf1f1 | -10.2979 | -50.2372 | 2025-09-19 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 694de8cc-3d9c-3b2e-9bd9-ec90dbfa5ca1 | -10.3168 | -50.2352 | 2025-09-19 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 38800bfb-d470-3238-83b9-bc521b8128e2 | -12.8777 | -50.5422 | 2025-09-19 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f5502833-1305-3218-a1ac-6a5af1590d74 | -11.2147 | -49.6441 | 2025-09-19 03:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 186.3 |
| ca2e11f1-6a3d-3a80-96f3-91a142525367 | -11.215 | -49.6224 | 2025-09-19 03:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| dfc86340-64e9-37af-baa8-877038fe86e3 | -3.58703 | -42.86221 | 2025-09-19 03:51:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f154e29e-390a-3b5e-8263-dfdb3e02fb53 | -2.94326 | -49.34493 | 2025-09-19 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1365a1d7-cb92-335c-8250-08045a892a6d | -2.94614 | -49.34346 | 2025-09-19 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee0b1119-af2f-3bff-b7a1-c7ddf66956b7 | -4.35519 | -38.45137 | 2025-09-19 03:51:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 92687e75-9af3-3a2c-a909-3ccf57be8d43 | -3.89509 | -40.83434 | 2025-09-19 03:51:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f1c1425-3383-3650-81f6-a019f775af29 | -3.4126 | -42.98744 | 2025-09-19 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 178fe62c-066b-35bf-8380-bba5f94d2111 | -3.40497 | -42.98238 | 2025-09-19 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca83700c-77b7-30bd-b649-15a80376fa40 | -4.5381 | -38.60454 | 2025-09-19 03:51:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47a5a68b-e9fd-3815-8ef8-2fdc1cd88a0e | -1.75952 | -48.0531 | 2025-09-19 03:51:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b60d4e34-19aa-3d63-b072-93f1f118c10c | -3.98875 | -43.23264 | 2025-09-19 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 295d868b-47cc-34c2-8747-00ac238911fe | -3.15498 | -43.26606 | 2025-09-19 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91b337b2-c04a-304c-9289-6f0495c108be | -3.4102 | -43.00223 | 2025-09-19 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b807278-5efd-31f3-8088-2f2d97ecaa1b | -4.66449 | -37.65461 | 2025-09-19 03:51:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a19cbf8-b56c-3e0a-b155-92bcde4f2461 | -3.85642 | -40.35061 | 2025-09-19 03:51:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c31e15d-730a-37c8-b496-489cbbf404ca | -1.75611 | -48.05484 | 2025-09-19 03:51:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9053a01b-8336-36ae-b589-48fc67de1c0f | -3.4108 | -42.99852 | 2025-09-19 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f5968ce-bcef-3bb6-bf37-3031b1ee07f5 | -2.94528 | -49.34845 | 2025-09-19 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4cd28a41-2674-3528-85e0-2602ea664aa4 | -3.85705 | -40.34666 | 2025-09-19 03:51:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c4ecc75-62eb-3bbf-9ec8-ae098b4f2d05 | -3.41612 | -42.99181 | 2025-09-19 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6121fc33-3445-3ba4-b200-e9dba1da94d6 | -3.40909 | -42.98307 | 2025-09-19 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 932312d4-4be1-3012-a358-d3d3a0b5cb4c | -3.1514 | -43.2615 | 2025-09-19 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a70f00df-6dd9-302a-8bc9-5f12e58a8524 | -3.4096 | -43.00594 | 2025-09-19 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8944f48b-9647-3fef-96c2-69a10c489998 | -1.75882 | -48.05745 | 2025-09-19 03:51:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92a048de-abdc-3c8a-9907-a10c556fd247 | -2.26236 | -47.84549 | 2025-09-19 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8ec29cf8-11bf-33c5-82e9-9652b65f7ccd | -3.15561 | -43.2622 | 2025-09-19 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d3b1f1f-1149-319d-b7c3-7305a6c08d42 | -1.75686 | -48.0504 | 2025-09-19 03:51:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f36f16b9-2b21-3a8b-853c-95232dc86bd8 | -7.84855 | -45.63204 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c214b3bf-f7bd-3692-95cb-a8393350ea32 | -8.21357 | -45.80593 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96194243-c922-3b44-9383-be91f676aca4 | -8.06691 | -44.08989 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 51ef4608-9d13-3d8e-a344-46a536e69da1 | -7.55841 | -44.74809 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a8c1f61-0144-3f3a-950b-a3e99aba63fb | -5.77422 | -45.9745 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31b5a2a0-e12a-3719-b3b7-c86ebe8c3d7d | -7.55279 | -44.78084 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2b1875f-38de-3e5b-b061-b362fe213f3c | -7.63391 | -39.23997 | 2025-09-19 03:53:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e3d5e72-24b3-39d8-a10f-87749f8cbc92 | -5.976 | -43.79778 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24120061-cbbc-3008-a523-d262c223074c | -10.1026 | -40.9291 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2722256-61eb-3949-82e9-5b4624df5968 | -5.81914 | -45.90543 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9572d52-f7e0-3211-8118-b08ab452eb20 | -5.98141 | -44.14898 | 2025-09-19 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d580e4d-d25e-392f-82ca-090da05f871c | -6.90825 | -44.77302 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6ca2354b-5d1c-3f1c-8c91-fcb7e7316ca4 | -9.14081 | -44.85622 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c463c46-3097-3d5a-b9b7-b34fd52b7c02 | -9.15788 | -44.88407 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a918254-1951-3fcf-8b28-9146e7c57815 | -7.71038 | -44.39315 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa7f388d-d051-301f-806b-a9654166d187 | -6.7561 | -46.00304 | 2025-09-19 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3daa23c0-ddb9-3216-80f3-57768aabe8a3 | -8.37822 | -44.67711 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56643357-d263-3fdf-b49c-4d36b1bcad23 | -6.92935 | -44.75518 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dad73158-ac6c-3955-af70-e49f9e930c54 | -9.18614 | -45.31659 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3503844d-e4e5-360e-8760-008a4282b43c | -9.14666 | -44.64701 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91743db5-2a9d-3fe2-97e4-6f0964426a7b | -5.735 | -45.27686 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 432fa885-fc37-312d-b856-a6c3461446ec | -5.77514 | -45.96904 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77a46c8a-2551-3a94-ae39-cd3363854baf | -6.00919 | -43.70177 | 2025-09-19 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README10.md)
