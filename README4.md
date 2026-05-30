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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| facb5157-a928-3dce-9c7d-04f8db4769a8 | -10.63765 | -49.72783 | 2026-05-30 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23ce0a71-aed9-3a66-a086-aa9c610f97dd | -11.76392 | -47.06516 | 2026-05-30 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd4ddaf5-0318-32db-8f4d-08fa30f8f258 | -12.00127 | -47.76662 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8e1f996-7e89-388b-8f4e-2d19917d5b47 | -10.78077 | -48.5443 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b784be-8046-3387-9e4a-8f93e88e5b7c | -11.70167 | -44.161 | 2026-05-30 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e996c197-3464-30dc-9742-9ea6434f5394 | -14.25154 | -42.7459 | 2026-05-30 04:04:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf27b437-72b4-3c13-b742-d3b674013c63 | -12.00367 | -45.36117 | 2026-05-30 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 564c209f-b098-3090-880e-33bdbc22cdcf | -10.7797 | -48.55029 | 2026-05-30 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7f03842-9efe-38d4-9516-1565adf95968 | -11.9787 | -47.89316 | 2026-05-30 04:04:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6ba2146-11c6-39b0-813b-bf0dee8dfc1d | -11.53523 | -46.43842 | 2026-05-30 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99ecdb44-306e-3b3a-ae33-fd92d2313c28 | -15.58372 | -46.80735 | 2026-05-30 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17a7b3a6-d2e7-38a3-b0df-6f448e704ccd | -11.59239 | -47.44137 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18a973c6-b68d-3fe9-ae9e-5f3c1eff9374 | -11.76177 | -47.07726 | 2026-05-30 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b48a72d4-ff89-3f2b-9ff8-a3f3edaaf50e | -12.00702 | -45.36019 | 2026-05-30 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7995a089-ab2c-312b-b094-d922bf559083 | -18.37236 | -39.95667 | 2026-05-30 04:04:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae885692-d6cf-3296-8784-a1740f0adbcc | -11.58571 | -47.45342 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| bfe82b19-c99a-3f2a-ba97-1730311e3f0d | -14.25213 | -42.74228 | 2026-05-30 04:04:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b9446ce-57fd-34b4-b113-65336dffc2f8 | -15.58279 | -46.81249 | 2026-05-30 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57429cef-6c66-36a8-95b5-71570787d49b | -11.585 | -47.45739 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 203a4609-c52b-37ab-8e4c-dd4ddc1f677b | -11.89397 | -47.60569 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee35fc61-5f6f-3865-b9a4-8f699a48f779 | -11.60112 | -47.44303 | 2026-05-30 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59beee30-c133-3569-9609-17b0d9af6f46 | -10.63706 | -49.73102 | 2026-05-30 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d575132a-6197-3d30-ac8f-994e4d0f9984 | -21.42204 | -47.06333 | 2026-05-30 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b5e5c10-eb9f-38f2-8c46-3149f9a05005 | -21.8109 | -49.13206 | 2026-05-30 04:06:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4238a3c6-0a88-3fbc-a6f4-6a55a1144b44 | -21.30101 | -48.5848 | 2026-05-30 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 339dcc23-4d43-31f7-afb5-b98890fdbcfb | -21.42308 | -47.06007 | 2026-05-30 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 460042ce-0f87-331a-a968-ea295e691446 | -21.4184 | -47.06258 | 2026-05-30 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01229635-7fbb-3b51-9ad4-5e1130945d4d | -21.61976 | -51.54642 | 2026-05-30 04:06:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5d6f812d-b78d-3793-be50-136ac50a4f18 | -21.29703 | -48.58401 | 2026-05-30 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6fb4da0a-69bd-3567-b4ce-2cf618a7e6f1 | -21.8033 | -49.13112 | 2026-05-30 04:06:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e26e381-546b-3a34-9994-4bf0a5d40a74 | -21.80737 | -49.13202 | 2026-05-30 04:06:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a2e08ac-5de4-3407-bfcd-66e94e18b585 | -21.80684 | -49.13116 | 2026-05-30 04:06:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c71d7f80-13df-3268-81c7-67285816a3ab | -21.42288 | -47.05872 | 2026-05-30 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c327898-c86f-34d3-99bd-10af91c8e077 | -21.41943 | -47.05933 | 2026-05-30 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab1535c-6e12-3b47-9b93-2d59d6c1b09c | -22.38309 | -49.78625 | 2026-05-30 04:06:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79276f0f-c6dd-3563-85e0-3f10aefb5feb | -18.46526 | -54.70584 | 2026-05-30 04:06:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfac3535-b3f0-37dc-8c57-abe9693281d4 | -18.46459 | -54.70741 | 2026-05-30 04:06:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 190b7a1a-b228-346e-81de-da8a157318e4 | -18.4642 | -54.71062 | 2026-05-30 04:06:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a8d72fe-50c8-3f65-af8b-d137c14d0eef | -18.4635 | -54.71219 | 2026-05-30 04:06:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06244367-bcbc-3cb1-82c6-13b44d2aa837 | -10.8379 | -46.921 | 2026-05-30 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 4409a01a-a25d-320f-997b-4e42c23d633d | -10.8566 | -46.941 | 2026-05-30 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 24128880-40b9-304c-bdff-1c136b270420 | -10.8569 | -46.9186 | 2026-05-30 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2a337622-5220-34ef-9121-b1f43f4554e7 | -10.7614 | -46.9529 | 2026-05-30 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4431cd8e-969e-3ab8-a079-0ddbde946451 | -10.8375 | -46.9434 | 2026-05-30 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 705e8f3f-3c43-3675-bea8-74691dab3190 | -10.761 | -46.9753 | 2026-05-30 04:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 293813e8-1614-316a-a8bb-3c6e6521be69 | -8.72706 | -47.83168 | 2026-05-30 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0aee8adc-527d-3f1d-ace7-ac4f789ead17 | -8.40937 | -49.60204 | 2026-05-30 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98bb4818-b0dc-3280-9763-2a176b78e66f | -10.7709 | -46.94922 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b5fe6b1-3d20-30c3-8792-5980669d3451 | -7.84388 | -46.25508 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cb09cbd-4ea2-3f33-84d8-38c61b504bb6 | -8.72762 | -47.82814 | 2026-05-30 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42699576-e992-396b-88d8-1e7731871616 | -10.76428 | -46.99158 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd86bb5a-126c-350c-9584-ab6fea262fb8 | -10.76644 | -46.93402 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6625be2-2f67-38ab-838e-b696c3f5b580 | -9.76555 | -48.7529 | 2026-05-30 04:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b656b164-64b9-30e8-ba6d-812f98754926 | -7.84038 | -46.26178 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 257caeaf-55d8-3fda-9a9a-da826dabcbad | -10.7698 | -46.95629 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 027729f8-2917-3fc2-aae8-362bfda43f0a | -10.76701 | -46.95222 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 150c32a0-883f-3913-93b4-ae57c45f4b5c | -10.76355 | -46.93744 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0f49031-c6d4-3b57-ad2a-2bc950745722 | -10.98039 | -45.09809 | 2026-05-30 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b838d5ac-8580-34f9-b3fa-b6b2ce6bf97f | -10.76699 | -46.93048 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 627640c8-a4db-386e-b55f-74a3893777c4 | -9.3713 | -50.54802 | 2026-05-30 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7edf4d4-b1f1-354c-829f-e18805a6a318 | -8.01887 | -46.58345 | 2026-05-30 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd95b088-7f8e-3b60-a3cc-92dd266cb891 | -8.40517 | -49.60542 | 2026-05-30 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a16de39a-e3c2-33bb-b5d6-bacc872538d7 | -8.38442 | -46.88494 | 2026-05-30 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c29b05e7-8bfb-32d0-8ef3-b93ee26be1ad | -5.94945 | -43.48459 | 2026-05-30 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbb67040-2a30-3465-9cac-f2996512d35c | -10.9839 | -45.09864 | 2026-05-30 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b9865da-5121-3e97-a451-9a93941a14b5 | -7.33998 | -49.85579 | 2026-05-30 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b319a3b-68d4-3c35-a481-8126a605055b | -8.24107 | -46.35731 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70e3bda4-9298-3e43-89c1-fb00cfc06461 | -7.84722 | -46.25561 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b83728d-0c05-385f-aede-30719c900699 | -10.22491 | -48.1361 | 2026-05-30 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81fd9c0f-2991-3640-b482-49403a43d1ed | -9.9245 | -48.00417 | 2026-05-30 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4834f1ba-f83a-3db4-855e-e3478c161ff1 | -9.45469 | -51.82801 | 2026-05-30 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6dae56fc-22a2-3ea6-be4e-2a794cd42f97 | -10.76593 | -46.981 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 757d292b-8932-3bf5-ae39-d03091b35799 | -10.76812 | -46.94515 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 853614e4-47e1-31e6-a095-d481689cce2e | -10.76483 | -46.98805 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d787934c-46f6-3f13-9fae-82df45ec71c5 | -10.76538 | -46.98452 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53b56555-dbd3-3cd1-a6fe-20481b13c45a | -9.9268 | -48.68555 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ebe7a2f-333d-35c8-96dd-dff936dc32c0 | -7.33635 | -49.85518 | 2026-05-30 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89a2423f-773b-3040-b158-5bd5d8c85abe | -9.40136 | -48.45502 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be715357-ffbf-3731-94c9-4218907763e9 | -10.76536 | -46.96281 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b67c147c-2af3-3338-9e56-ec8326d05fb1 | -10.76313 | -46.95522 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3f70b01-2804-392d-8aec-e19026d2bfe0 | -9.40195 | -48.4514 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54790323-5e04-3cde-ad6c-c969b5464559 | -10.76257 | -46.95874 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ec599bff-2f4e-3ca8-a00a-2b9e5820f19a | -8.84142 | -46.71078 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ac35a1f-f90a-3898-b955-7b4d5c6e20ac | -10.05951 | -49.11571 | 2026-05-30 04:36:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b10ea959-cf0e-3e64-a4d5-99fbd1ce38f7 | -8.72649 | -47.83522 | 2026-05-30 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 056bdd94-d4d1-3be6-9f46-8f52eb3bc6e7 | -10.06294 | -49.11629 | 2026-05-30 04:36:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e098e409-038d-3703-a3b2-0445ffb1ce5a | -5.80217 | -45.13298 | 2026-05-30 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 651bdeb7-3665-30ce-9899-0c14539d9945 | -8.40871 | -49.60602 | 2026-05-30 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bdb5877-f8cc-3521-9cfc-843824d0e783 | -10.76591 | -46.95928 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f61d6a0c-932e-3bc2-9c32-fe31856080c1 | -9.36611 | -48.41587 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4af33989-09cd-3067-be3d-b71d5e925621 | -6.99346 | -42.87846 | 2026-05-30 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d4cacd3f-8348-389c-b89e-7d0e625e58b2 | -10.76425 | -46.96987 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 91d9aaf1-b8d4-3da9-87f6-bd1e96d6c2b6 | -9.45075 | -51.82735 | 2026-05-30 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b6e6d375-94f7-3c66-bbba-60333bb5724c | -7.33567 | -49.85935 | 2026-05-30 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd9e0ce6-7787-3079-9ed9-d81b225c1d8c | -6.99279 | -42.88297 | 2026-05-30 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c0ed38f4-2eba-3462-b0bf-a4c54f9b0f35 | -9.86503 | -48.24595 | 2026-05-30 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1b58c7b-cad4-3b7f-bb31-f471fda8a7c1 | -5.94883 | -43.48864 | 2026-05-30 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e868353-6788-3273-ad15-a4190bd1b227 | -9.39857 | -48.45086 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c8dbfe6-ee3e-3902-9f41-63dcb28867ad | -7.84612 | -46.26263 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a50cbc26-de33-39e0-9aff-427de3420833 | -9.36764 | -50.54741 | 2026-05-30 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
