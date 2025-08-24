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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a1712d8-ca12-3ffd-8da3-abad632999ed | -20.36339 | -46.73687 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6018f4be-6972-3248-9cd8-688bec3165d8 | -23.40255 | -51.99994 | 2025-08-24 05:04:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85de1380-87ae-3e6f-bfc5-42a7c666e75a | -24.77888 | -50.12111 | 2025-08-24 05:04:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 44f3a8a0-dd7d-3b82-bdf0-b327573bc1b0 | -22.01192 | -44.99781 | 2025-08-24 05:04:00 | NPP-375D | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ede19b4b-67fd-3d99-a1dc-b127cf5c93be | -21.41495 | -47.61387 | 2025-08-24 05:04:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71fa5bbf-562b-3da5-a537-58f0f8aa1f6a | -23.10594 | -49.97871 | 2025-08-24 05:04:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a46094f8-7bfc-3b32-9174-946d3876cb77 | -20.3611 | -51.69068 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b527c898-8721-3c03-95d1-10d8406ef3c1 | -20.3518 | -51.69752 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 53005349-94ff-359e-a2f5-95c1758ab580 | -20.34251 | -51.70431 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8369ee3a-5d30-3140-a1b9-e779fffe86a9 | -22.14421 | -43.65901 | 2025-08-24 05:04:00 | NPP-375D | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a14ed41f-f563-356f-9e57-7024a852f481 | -20.35744 | -51.6862 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a067b4d0-c1bb-367a-9831-63d36decb569 | -20.35686 | -46.74461 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c10bdf05-80bd-3634-895d-bb708b7db0f3 | -23.30622 | -45.53556 | 2025-08-24 05:04:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| bb6e169f-f0c1-38e4-9ab9-b1c5ee9ae00f | -20.08377 | -46.10742 | 2025-08-24 05:04:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9804acc4-cfcc-3423-85cd-a10a830182ec | -20.34863 | -51.68909 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9e0bbb9d-9bb6-37cd-baa0-1aeeced201a0 | -23.31331 | -45.52675 | 2025-08-24 05:04:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3800d734-47b0-3fb4-8c44-269fc8436398 | -23.35915 | -46.9326 | 2025-08-24 05:04:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ead240d1-9fa9-31e5-af89-f227a94557c8 | -22.90266 | -47.72593 | 2025-08-24 05:04:00 | NPP-375D | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06b79c22-c239-3bd9-91f4-5252f67b1bf1 | -21.90004 | -48.83199 | 2025-08-24 05:04:00 | NPP-375D | ITAJU | SÃO PAULO | Brasil | 3522000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bd1407b1-97f7-3ca8-a79a-c50e520f7753 | -20.35328 | -51.68567 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b773a678-c57f-3d10-9e8e-eff02fa8f735 | -21.72942 | -46.8173 | 2025-08-24 05:04:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 988b48f6-8723-3cc8-a82a-1a37206dd65f | -23.13457 | -47.03488 | 2025-08-24 05:04:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 462f8ac5-fa8d-3d58-9c58-52ba2d7bd3ec | -20.35229 | -51.69357 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b1683a56-8013-3e17-8475-8293dea468fb | -20.34665 | -51.70487 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dc8870b1-a11b-3524-9285-d463e8f32cd8 | -21.40911 | -47.61694 | 2025-08-24 05:04:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdcda678-1ae4-3bc9-a02e-245c0e79ea51 | -23.51208 | -47.25949 | 2025-08-24 05:04:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6151bfcf-098b-38a1-9ef1-3e193d994bee | -23.3707 | -46.86554 | 2025-08-24 05:04:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 80eb2088-e1f5-3e5c-9f5a-32db12b0215a | -23.32406 | -47.84676 | 2025-08-24 05:04:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| fac51f37-925d-3165-94d5-6d6723161089 | -20.34764 | -51.69702 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3f0a6754-6eca-3476-85f4-8d90fda2766c | -23.50635 | -47.25872 | 2025-08-24 05:04:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e2b395cf-5909-3763-bed3-f79de746c5a0 | -23.12936 | -47.0335 | 2025-08-24 05:04:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b10cdb02-ab82-333f-9706-19594d168a7c | -21.32472 | -48.67277 | 2025-08-24 05:04:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf4e1e61-b6b6-3076-b480-15935d7c9e58 | -20.34349 | -51.69646 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2fd5441c-2813-3374-84f1-55759442306d | -22.95308 | -45.13197 | 2025-08-24 05:04:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| be23520c-cfc5-38dd-bf49-63d85a74a208 | -22.71939 | -46.97971 | 2025-08-24 05:04:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48a6e792-8c3a-3417-b591-9ea8dab095de | -20.0842 | -46.10281 | 2025-08-24 05:04:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c0c1436-ebc7-3204-961f-4d801005dcc5 | -22.14228 | -43.65382 | 2025-08-24 05:04:00 | NPP-375D | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 39233905-4635-3737-a274-89a4952684b1 | -20.12252 | -45.36192 | 2025-08-24 05:04:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a5e5836a-4d69-3c6c-8525-a7d503ee4667 | -24.25171 | -50.23547 | 2025-08-24 05:04:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8925a186-bc8f-3d73-b40c-06bed19b1b21 | -20.93896 | -46.82389 | 2025-08-24 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c29b03e0-fbbe-3035-976a-02b62a164dc7 | -25.14896 | -49.54232 | 2025-08-24 05:04:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 526b2fbe-31b2-3363-b3f6-1c5004055bef | -23.62901 | -50.55963 | 2025-08-24 05:04:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| c400982b-02d1-3e7c-9401-138adf4c2340 | -20.35279 | -51.68961 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 37049bfe-92b6-33e7-bed9-ce094ec4f625 | -22.73201 | -46.96902 | 2025-08-24 05:04:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0c255b82-7dc4-3559-a0d7-c7d7bc3baa27 | -20.34813 | -51.69306 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aa8398ec-499d-31fc-baef-c3f2720e80c5 | -20.11999 | -45.36474 | 2025-08-24 05:04:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e8bb4d77-f312-3756-a84c-e0affa84bf37 | -23.47465 | -46.81134 | 2025-08-24 05:04:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 31c23f1b-178d-3745-ba7b-2f7ee21cc890 | -22.94707 | -45.12923 | 2025-08-24 05:04:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4bf3e251-eba2-3b0c-bced-a0bd6c653694 | -21.72394 | -46.81334 | 2025-08-24 05:04:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1b9fa2cb-7cfc-338b-b159-49d69219c3dd | -23.51276 | -47.25673 | 2025-08-24 05:04:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c3c1d736-60fd-3919-a056-d5d606c27417 | -19.6538 | -48.48851 | 2025-08-24 05:04:00 | NPP-375D | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e303ca5-82b9-3b46-bf4f-3118aed94e5e | -23.2892 | -47.63845 | 2025-08-24 05:04:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1a9e0776-4270-3b87-af98-964c4c6455cc | -20.34399 | -51.69249 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a174b9e6-0a19-3840-8229-fd74b44878d2 | -20.35764 | -46.73655 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7a22de5-bcf9-3337-992a-27a29cd7b3e2 | -9.0232 | -65.6982 | 2025-08-24 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| db54ea26-da2d-3896-a61f-c4590e9fe2cf | -20.3599 | -51.68 | 2025-08-24 05:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 3a794ca5-9106-3919-9af7-8b072fe18f81 | -17.6176 | -44.298 | 2025-08-24 05:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7e98c0d3-01ef-3701-9071-a90e7a556b33 | -9.0231 | -65.7169 | 2025-08-24 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1276a72b-304e-30ff-a19e-f4c276a78495 | -9.1535 | -59.4834 | 2025-08-24 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 73240541-814f-30c2-ab33-7a0f4ffe2c21 | -11.5437 | -51.8454 | 2025-08-24 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 47e8c71d-7fa7-3959-91ac-70dc62f3c859 | -16.797 | -51.3419 | 2025-08-24 05:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f6eae1a6-92c1-379f-888c-c7f7ee58c799 | -9.1536 | -59.464 | 2025-08-24 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 69f5eca6-52a8-3811-9727-65b0f28e9670 | -20.3396 | -51.6839 | 2025-08-24 05:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 39ab8949-97f1-3605-b0b8-0d4ba2559fc8 | -9.1722 | -59.4629 | 2025-08-24 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 49dc3592-ad4e-3f6d-8341-ef31387ebcc4 | -11.5434 | -51.8665 | 2025-08-24 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 60dfe5f1-949e-3dcf-9ccf-b0101adb12f5 | -9.1721 | -59.4823 | 2025-08-24 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 037b5a6d-a568-3791-a125-9bdbe59e462c | -20.3594 | -51.7023 | 2025-08-24 05:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1fa27317-c8ad-3dd1-8162-567411c302ec | -4.9605 | -55.8226 | 2025-08-24 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 81aa227f-3d80-3562-a2a9-4d10fe8d828e | -10.60492 | -44.30956 | 2025-08-24 05:18:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 1ab6a9d0-14f9-3a91-99ed-1118e4807a4f | -7.69718 | -42.12662 | 2025-08-24 05:18:00 | AQUA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| ad2dede9-3f95-3ef4-86a1-7c0774bf55ec | -7.01915 | -44.62932 | 2025-08-24 05:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| a477f803-a47a-30f2-880c-b3b48df8878b | -6.19377 | -42.98401 | 2025-08-24 05:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 87feaece-04be-3b39-be33-c04e72b06008 | -10.60217 | -44.32591 | 2025-08-24 05:18:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 19126daa-dedf-3274-8913-227e3031e963 | -7.01709 | -44.63631 | 2025-08-24 05:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| a71cad64-7fbc-31ba-a789-8e89643a1486 | -20.3599 | -51.68 | 2025-08-24 05:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 116.6 |
| a5acc93f-6345-3291-9d8f-c0c69e183d70 | -20.3396 | -51.6839 | 2025-08-24 05:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 9e675fa4-da75-3e69-836d-9ee17c210bef | -9.0232 | -65.6982 | 2025-08-24 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c9e701f4-d545-3798-b116-f70e0d09568a | -16.797 | -51.3419 | 2025-08-24 05:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 21f6ded9-2d05-3332-a278-df3d0db99852 | -20.3594 | -51.7023 | 2025-08-24 05:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 54.0 |
| b9b1b10b-f3ca-3daf-a43e-eaa3b18f9229 | -9.1536 | -59.464 | 2025-08-24 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| fcf71bee-30b9-39ef-8ccd-6610d1e2489f | -9.1535 | -59.4834 | 2025-08-24 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1f736759-c595-3289-abee-4991ed7a5b64 | -17.6176 | -44.298 | 2025-08-24 05:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 42db8feb-da9a-319e-bb50-3b9ad42546ca | -4.9605 | -55.8226 | 2025-08-24 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a223a3cf-146d-3f85-93b4-97e730fef5f0 | -9.1721 | -59.4823 | 2025-08-24 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 13e1f580-97cc-378b-b670-f62a3f915df8 | -9.0231 | -65.7169 | 2025-08-24 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7ab9ffc3-0596-3c90-8dce-7ca7f71cb632 | -11.5434 | -51.8665 | 2025-08-24 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 7a3d4774-a915-3c05-a92d-801e8ab70e79 | -9.1722 | -59.4629 | 2025-08-24 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8cb45943-9077-306a-ae65-17a1a98ce083 | -11.5437 | -51.8454 | 2025-08-24 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1ad35067-aa88-386b-b121-c11f4c60f743 | -2.26349 | -47.85887 | 2025-08-24 05:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 154805f4-fa84-3997-9f56-3facdec624ca | -16.79027 | -51.35434 | 2025-08-24 05:21:00 | AQUA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 84edc9a1-479b-345d-b380-01fdfb4421dd | -2.26428 | -47.85362 | 2025-08-24 05:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9575df77-40d5-3da4-b194-859a32ace3e6 | -2.2552 | -47.85434 | 2025-08-24 05:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f5875e2-90b0-3fd3-9c80-5e2e6c7ab39d | -14.80662 | -47.90969 | 2025-08-24 05:21:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| de5d1744-c69d-3e89-bf85-4b014b24e106 | -17.59964 | -44.3014 | 2025-08-24 05:21:00 | AQUA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| f047c947-3544-3333-9643-b311cd85d390 | -17.6081 | -44.29681 | 2025-08-24 05:21:00 | AQUA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 57d61f7e-89af-3211-8476-ccdf8bfc7f4f | -19.63231 | -43.19046 | 2025-08-24 05:21:00 | AQUA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a9227ea8-2ee6-3e97-bda7-8305503b26bd | -17.60177 | -44.28862 | 2025-08-24 05:21:00 | AQUA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d13e1f33-103a-3594-bf8c-bb04aab14adf | -13.04899 | -45.2247 | 2025-08-24 05:21:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| eb341093-3fc2-3d81-a77d-197a5509b586 | -12.734 | -48.11815 | 2025-08-24 05:21:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 0e911b90-9fe6-32ab-80a8-20e9f2d28725 | -19.62472 | -43.17828 | 2025-08-24 05:21:00 | AQUA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |


[Clique aqui para ver as próximas entradas](README71.md)
