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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbbf112b-2edf-306a-87ed-14b1b9e193f1 | -13.269 | -47.58446 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c54752c8-86b3-3504-befc-0d5b50711423 | -18.51236 | -43.90888 | 2025-10-07 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d456123c-f255-356e-a5cb-614a44059ec7 | -17.5657 | -46.07715 | 2025-10-07 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0424ddd-a3a8-3c0e-b3e4-d3b5e476b26b | -11.60888 | -43.11138 | 2025-10-07 04:38:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 721b29ef-f3a4-367b-89a4-866bd0bc188b | -13.22717 | -47.81376 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8c6e2aa-3207-3960-a2b8-926d4377daa0 | -10.99696 | -49.58173 | 2025-10-07 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36f12294-6d36-3fb3-a3e2-9afec8c5f716 | -12.90501 | -54.73377 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5ebdf2a-2fe5-3366-a8cf-498073a18d21 | -12.72395 | -47.93632 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60aed979-7bc8-359e-b046-9be5a42f29a8 | -12.94592 | -46.78722 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca40d4c9-853a-3405-9608-77be9e2ec7c9 | -15.60701 | -47.29115 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f0fd225-fcd0-34f1-92b6-0e73dcccb7fb | -12.24767 | -49.20182 | 2025-10-07 04:38:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1a3f024-3fc3-3053-8cb7-74893b585e8b | -14.75827 | -46.05363 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b74a53c0-fc85-332f-914c-5bf756aaca80 | -13.37496 | -48.0565 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92d9437-d84a-385f-9f19-c4aff162162f | -10.42011 | -51.63541 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28211482-ee24-3cd2-aeb6-3ab7053c1b86 | -13.70617 | -48.07677 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c29a7c9b-05eb-332e-92ab-53c116479973 | -15.03742 | -56.03425 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5eb2b4d-1457-3492-9cdc-217090e169a2 | -16.45978 | -49.06148 | 2025-10-07 04:38:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbfbd5fb-c78d-3790-ae2f-8e850dad7d5c | -13.22231 | -48.45932 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47d60616-0c7d-3117-bfe0-ba766c02632a | -12.9485 | -54.72678 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60cb9575-eb2f-3cd5-84a6-40c5528d7f4e | -15.7949 | -46.25012 | 2025-10-07 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b563be1-bb22-3323-b506-b2befbd7b317 | -16.29354 | -50.98282 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8453311-4f93-3a20-8062-745b01748598 | -15.17074 | -45.73522 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6bfa625-2d11-3741-af18-6a093d3f08b7 | -13.33258 | -48.03476 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8d6edb6-0c64-3fec-ac71-536db8432519 | -11.2297 | -47.76941 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad65c883-4c24-3254-b87a-7daeda13b6a2 | -12.401 | -51.13642 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36072478-9300-3dca-ae59-8c098bde50e0 | -15.20507 | -56.80907 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb5e8a28-2b9f-3a7e-a25d-919e438d50f4 | -13.08058 | -47.88258 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e476460a-d801-37e2-872a-b5af1f581d40 | -11.49943 | -44.97312 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecb9837b-8cf7-3dda-b11c-eebf89b2aaf9 | -12.31264 | -55.11062 | 2025-10-07 04:38:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9efb8859-c2c0-3cf6-990f-81f45c22771b | -11.22129 | -47.7792 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87d0bee5-7657-3b2a-82f3-267cd44c307a | -10.45136 | -50.41003 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 848a93bd-f2e1-3c9d-8d6c-46db266d0151 | -10.37741 | -50.30381 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aed3d64d-df87-397b-919e-3ecbed25fd7e | -15.59032 | -52.55067 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c7cdea4-8c0e-3d7f-a030-3c5ee0fe1253 | -11.88584 | -44.95259 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79e7d9a3-ad48-3eca-99dc-5577a9ec2d17 | -10.4383 | -50.33984 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5fda3c0-31ec-341e-8be0-5f2c7d3414eb | -14.71419 | -48.34772 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef264cb9-aa8c-3e5b-b200-a4307a22b508 | -11.71805 | -44.31466 | 2025-10-07 04:38:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e46ebc6-e2f0-378e-bc83-501c73ad1ecb | -10.67678 | -54.6952 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a617cc34-3aa9-3872-8eb6-5214ac4e9a43 | -12.1801 | -47.77426 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0968b08e-3d80-3250-80e5-590df88a78bc | -13.31281 | -48.0504 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea6f0a99-2de6-38e7-8dc5-3562fab4af21 | -14.75467 | -46.02501 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a90d554-d1e1-3021-9eec-20b8cc55f223 | -12.32417 | -47.85994 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0571d0a-c8a6-30d8-85d8-3edd96485a0d | -13.26724 | -47.59601 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b9c1a45-3a49-3631-9e95-36b378a930d3 | -10.61542 | -48.70378 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5030386e-47d3-3181-b458-17fb3b17643b | -15.60347 | -47.29058 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 49f8ea17-36c1-36c2-9abd-627da24d3170 | -13.24122 | -47.24948 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fddf204-a512-3024-b6dd-84f931ec5d51 | -15.91068 | -47.79692 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d7c6614-ec1c-3a23-ba1d-4f7ccddfc771 | -18.56635 | -44.18524 | 2025-10-07 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 376ea656-d15b-3e2f-86fe-a4583f71eb3d | -13.709 | -48.08103 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 707427f6-1f0e-364f-b3b7-696de10b4956 | -12.21547 | -44.25209 | 2025-10-07 04:38:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd996676-8389-3dce-828f-ff7aece10e52 | -16.01995 | -51.03679 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71679e22-e7b1-30eb-99f1-2d444c50f060 | -12.38784 | -51.08765 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cda133c2-c43d-3f8d-896e-59da04bcf62f | -11.22688 | -47.7653 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d739028-9835-371a-92eb-be59ba5595c3 | -15.16983 | -52.76808 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0b9ceb3-e717-3aa8-95b5-850c31993d82 | -13.39588 | -47.59743 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 376a278c-b4d7-3273-aa93-7da5f0585c8a | -10.39277 | -50.29838 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ade72603-172e-3de4-a028-9395c9651fbf | -11.7431 | -51.49683 | 2025-10-07 04:38:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5352f430-4cc2-3159-b518-3facddad9fdf | -15.99957 | -50.83556 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9ce693b-03e1-341f-9ffb-7c863faa9b16 | -11.9477 | -46.43979 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f81dc0f0-bf62-3c62-aad4-201707c0ef0f | -13.6779 | -47.33508 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a625d07-a9c0-3bc0-9f62-18481cb66d7f | -16.10799 | -48.94234 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26b1d1e0-fea6-35ac-8008-0b4188b89bc6 | -12.54161 | -48.14444 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7fb3cc0-a31d-3091-9a42-2f9f4d785bc9 | -15.61623 | -52.54702 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3872ef49-d522-3a78-a984-d6be7043b43b | -11.09963 | -47.20398 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92f294f-d6ec-3500-8546-f0236aefcc37 | -13.63947 | -48.71378 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17731aa0-0fd4-3dab-a63e-458d0322f978 | -13.24304 | -48.45882 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc3c986c-6873-397a-a4ee-a49db4f7c6e3 | -15.3771 | -47.99651 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f45ffb45-7c73-3a51-979b-b1c5cb1cc33a | -13.00896 | -51.02893 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bcd98d75-e3dc-387c-bf34-98aada6c9074 | -14.90262 | -51.52028 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c41297b-13ad-33bb-86d7-e33e46bad0d0 | -13.2545 | -47.79497 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8e0f96b-6592-367a-a8a1-0af4b0539ac1 | -18.0176 | -44.96877 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db942510-a586-3d61-b77d-9d9b5b62314c | -12.66341 | -45.02652 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 252c1350-a0d1-336f-adfc-05fdb5e45fb7 | -10.79163 | -48.59103 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16134e6d-2700-35fb-bf71-81d39794e424 | -13.5056 | -43.67153 | 2025-10-07 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 4a0a03a8-50ab-309f-827d-598dc7465f77 | -13.3239 | -47.77141 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9260d9c-5ea0-3442-a90e-165664ec967c | -13.96936 | -53.89513 | 2025-10-07 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ad26ff34-18a0-35c1-bb64-c5a37b5c8f72 | -14.76653 | -46.02221 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 169be563-902c-39dd-9f81-d0d54177961c | -15.5021 | -47.92828 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beb4a565-4733-382a-851f-07d1d0fa81e6 | -13.01978 | -43.54605 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 190299d8-05a7-3367-8b85-0133b128278e | -12.76597 | -50.48681 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4ff9f2c-4831-3257-a5b7-f60e759ab43d | -15.61702 | -52.56376 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ad72036-db73-359b-a322-0f70cbcf9ce6 | -11.68593 | -45.27521 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d818c5d-e1b4-325c-8aba-b0853cbb210c | -15.37509 | -47.30869 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6368d3e5-62cc-36ee-bf2e-a5f07a1dd945 | -17.71851 | -40.24989 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e8aba4f2-2c38-336a-8be4-189e4f52da26 | -11.94853 | -51.4781 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64430f61-cbda-379a-ade8-515f9c9283d5 | -15.55394 | -46.82608 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 626e9e5c-13e1-36b7-94d1-ef971bf30084 | -10.79884 | -48.58858 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcd7d68b-dffb-3d1f-8b33-61c060909d1f | -11.79801 | -45.05756 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8148f72d-c858-3918-ae91-14e117695143 | -16.01606 | -50.97607 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ac70e9c-b959-3305-990f-6b1e1b66ddfc | -12.37729 | -51.10909 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f1c0625-3a81-35c7-b8c2-d513d1c2904a | -13.52181 | -48.62148 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 876fcbf1-859d-336a-8ad8-07703e5a620c | -15.60444 | -52.5741 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| eeba586a-335f-34d2-9587-26b1ccd4830b | -14.61792 | -52.49048 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50249ded-5e1d-3819-918c-11a3b28c4652 | -13.64476 | -47.28586 | 2025-10-07 04:38:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 523a982e-95ef-356d-8a62-b879ae60ec8f | -11.77926 | -48.91578 | 2025-10-07 04:38:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c653506-7163-340c-bc64-c684b82a0a47 | -11.10077 | -47.1964 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86190848-0215-39b5-a75f-10509c530e7a | -10.42491 | -50.31501 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 06b8f4c0-d246-3fae-8880-cd65a9cc2698 | -10.74699 | -50.481 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bcc2159e-e0ba-3666-98a7-23a123a04116 | -17.02825 | -43.45404 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 785fa23a-e023-349e-96c0-4b7b2f296af4 | -12.41331 | -50.26486 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README68.md)
