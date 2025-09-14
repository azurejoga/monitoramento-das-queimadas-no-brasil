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
| 6ec34c0a-a374-3ba0-952b-6f981889a79b | -5.20443 | -44.31546 | 2025-09-14 03:49:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f8fbc28-39e2-3c40-8860-9cbd0c428e51 | -6.3312 | -43.95677 | 2025-09-14 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0853cef8-7de4-3635-9ddb-78cc6d7efa14 | -14.46795 | -47.31578 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac54c7cb-1212-3c65-8412-b5b0c00aeb8f | -14.46741 | -47.31853 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6395701c-a65a-385a-8a1b-a630d707b31f | -12.75687 | -47.16169 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbbf6d78-1d68-32ff-aef5-27db4f7b57f5 | -13.90609 | -48.30495 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ec3a64b-f605-378b-8d8f-aa57bfeee81d | -11.62765 | -47.37113 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed57693f-f46b-3e31-8bd5-9571fbd9527a | -13.88497 | -48.29712 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d21174e8-b686-3fa7-a0a4-d9e42d13a592 | -12.72345 | -48.03343 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a318b36-254c-3316-88f8-d62b87ee12ea | -17.35631 | -42.62161 | 2025-09-14 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a88b44f0-a0ca-3b65-aa2c-ca5d0a2885a8 | -14.46295 | -47.31448 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d667923d-ae84-3249-97dc-ce1d3a94701a | -13.28257 | -43.78808 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29774938-26a1-3b78-b60d-134fe160aa89 | -14.20043 | -46.17493 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| dfc79def-a86e-39ed-9831-52325dddbf04 | -11.62283 | -46.59433 | 2025-09-14 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8f0be69-b7a7-3172-b137-fb976f0d04fd | -17.9416 | -45.25937 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d81a032a-c96f-3a86-adb4-ceb99652ca0f | -14.34079 | -46.62049 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 674278ad-3679-3b3a-9ec1-01c27b9259f9 | -13.00752 | -46.74443 | 2025-09-14 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b0cd388-f713-3631-983c-930184a2b18c | -12.78249 | -47.99473 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd11c7e5-b62c-3bc3-828f-875eda03496a | -12.96719 | -48.03844 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98c75f40-9dcc-34df-b9a4-dc259359a0fe | -6.66149 | -43.51543 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a9c59ae-b03f-345f-81f6-77813db16a22 | -17.43762 | -49.22172 | 2025-09-14 03:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a05f2218-ecf2-381b-a3cf-662db6cf65e8 | -17.69543 | -42.55777 | 2025-09-14 03:49:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5b05f58f-018b-3248-ad55-782fd9cac8b7 | -14.40552 | -43.23177 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 476e70d7-3c03-3070-8942-1338c10ef357 | -14.42566 | -47.34327 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e8f00cc-a474-37ef-aae4-fdc777b68d93 | -12.25455 | -46.7911 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bde2cc55-7680-3f9e-ba7b-90308f1b9b5f | -11.14548 | -48.09462 | 2025-09-14 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7957c0fd-270a-3d77-8b02-cf036d93092e | -15.93208 | -49.98085 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e93bc8b7-7926-3e09-81a8-4c279ed0f175 | -14.75918 | -45.27769 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3114affd-9cdd-34fa-ba67-051b02849944 | -11.47903 | -43.60865 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4019dcb2-deef-31e3-a381-e9460918acbd | -11.43731 | -43.55293 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 305fcfc2-a3dc-319a-923d-81f1761c01b7 | -15.43755 | -47.35677 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7951b78-95b2-3856-bfb7-4ba838b7f1b2 | -14.62169 | -52.02993 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb72997b-133a-35f2-a6a6-ff75be5cce89 | -13.00693 | -46.74743 | 2025-09-14 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3ef347d-ab04-3f39-8027-be3a6d57c00a | -14.17802 | -46.1592 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4b7c39b-cc9d-3689-9e75-cd784f396578 | -18.01666 | -46.97131 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e11ec71f-d09a-3759-b90c-9f8021315575 | -11.46413 | -48.69984 | 2025-09-14 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 25112c95-272b-36e3-9506-cd6bfb427d68 | -11.82935 | -46.36943 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e0fc907-8397-3d11-85f0-3c185d21e6ba | -12.7854 | -48.00859 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 655a08d5-5051-3034-8431-e7503748d8ab | -11.45187 | -43.56765 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a670fe8-6b8f-3180-90dc-9e519fc52cce | -12.56479 | -45.65189 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c7d6a93-3cb0-3fc4-8d49-36ac6c652074 | -10.7375 | -46.44246 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d067d13-69d9-3c2b-809f-e426b423f07d | -15.67049 | -49.90499 | 2025-09-14 03:49:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6074d618-c255-3e71-aa51-e846a6c69877 | -17.99095 | -46.95517 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f8f7f18-7e19-31c2-92a0-b0c933c42bb1 | -14.18751 | -46.31824 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a756afe5-9c60-340c-8758-9f4a536cc683 | -11.33329 | -50.83368 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0efbe382-e70e-3a8f-9872-6f0b46aa8ba1 | -14.20432 | -46.33266 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 14dbca0d-2b10-303a-902e-6b62d5094fb5 | -15.63709 | -44.37306 | 2025-09-14 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df59cfbb-2fa8-39a7-a7bd-65d2f3d6ef2d | -12.91675 | -47.95003 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d77111a8-fb00-3260-9216-c9bb03711a25 | -12.78334 | -47.98746 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37d74488-e6ff-3455-8636-91a936305992 | -12.24186 | -46.78691 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7234466-f70e-3739-8ff5-82f6f7caac08 | -6.11463 | -45.93656 | 2025-09-14 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8647cd0b-1d6c-3769-a984-a5246a22f9e6 | -10.3261 | -48.83065 | 2025-09-14 03:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 733255a0-6cac-3682-a328-6e28dedf3318 | -12.93303 | -47.95316 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 559a313d-628b-39c7-b1d5-f6983304abf8 | -18.01886 | -46.96019 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d64c443a-b08b-3f58-9f90-3f2d5abb8add | -14.63305 | -46.36425 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ad4eeae-c611-34ac-b889-7d75020fdba9 | -17.4063 | -49.26282 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 296d8571-766c-37d2-8ae2-dd7266041d92 | -16.65747 | -49.77114 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28c559c5-36de-30f0-b139-6956ea738f5b | -10.76525 | -44.77749 | 2025-09-14 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a49d7d7-cfb2-37b2-8e75-9b353fdfc177 | -11.49663 | -43.70533 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1a29e50-193a-3e91-928e-6f913776daf2 | -18.20651 | -42.57101 | 2025-09-14 03:49:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 106ae213-7e08-3408-a6eb-dbbb66c89f4d | -12.77949 | -48.03831 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d4d29078-5120-3faf-bb89-0c6fdd44ea3e | -12.79849 | -47.97118 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0a93978-c4fd-363f-8aa4-d61d509ca220 | -6.35347 | -46.51455 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62d8bcf1-ba9e-3e5e-933d-8b1c48f21f3f | -5.64495 | -43.89186 | 2025-09-14 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc7e1558-298f-3588-95ac-688c9a71c93c | -16.91612 | -39.43895 | 2025-09-14 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 12062db2-57f0-3ba9-ae25-107a8928ac54 | -14.98599 | -42.23994 | 2025-09-14 03:49:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 394b01d6-ed27-3662-b89e-d6dd88753314 | -17.44609 | -49.23518 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26583de6-678e-3878-b73f-184d11723243 | -11.33451 | -50.82784 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6139cd68-f883-3fca-bf5d-a0c725c7f983 | -10.91621 | -45.58498 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbc56579-4044-3a05-9fc0-432dc8cec629 | -15.7729 | -53.48531 | 2025-09-14 03:49:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3487f650-89d1-3b8f-baf6-6aeca4365dfd | -12.56855 | -45.65789 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe147ac1-5032-3fab-83cc-082468607de0 | -16.08878 | -39.40958 | 2025-09-14 03:49:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eda2f5f8-1c2e-3372-8ba9-8f195ee70e84 | -15.76186 | -52.25856 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad752f99-0721-3913-9f1b-ae3d7ec17c9e | -12.73721 | -48.02111 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df13ae83-c3f4-377d-a9a2-10d8f975ed59 | -11.44425 | -43.56218 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 217010fa-b0dd-3abe-a109-a2f263c38b62 | -10.96851 | -49.57044 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f816e527-5992-3594-8482-94ddba335906 | -14.40924 | -46.39719 | 2025-09-14 03:49:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e95dd17a-d465-3f64-88d4-04ccbb5fd1fe | -17.40486 | -49.26406 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0283654f-3ecc-3c9c-82e4-81ef062d0457 | -10.91516 | -47.1949 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66dcfb19-b386-373d-86ec-62f44ea83b69 | -16.64664 | -49.76635 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7fb64af-111a-3e57-ad04-f61692e18059 | -15.77995 | -53.48719 | 2025-09-14 03:49:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95f7432d-5cc8-3384-a6ba-49726a1fc9d2 | -12.7002 | -48.29999 | 2025-09-14 03:49:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e936bb6c-eb08-3c2c-a1c0-e6dfc235207b | -12.77149 | -48.02148 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ad0d63c0-3a7f-3a16-9d50-94953059fd4c | -10.89901 | -45.46275 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b36ea39-b8c4-3221-9664-b75b9d469f55 | -17.29339 | -46.11786 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee4cec70-833b-3d4f-a1f3-7146520e0775 | -15.1897 | -52.47411 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b1525c6-bc91-34cc-a070-9c5873d61c7e | -10.32006 | -48.82971 | 2025-09-14 03:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae6279ec-52d2-3766-849d-1d3023bb4c1b | -14.43412 | -43.20582 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2650910a-fe4e-365e-a286-00501b542bf4 | -12.76747 | -48.01318 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bf7c6451-3d9a-3d11-8821-ed79083af6d5 | -5.65823 | -42.62724 | 2025-09-14 03:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 267a58f1-5680-3c27-9e72-4dc0c10b06bd | -10.76433 | -44.78249 | 2025-09-14 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e08556a-565f-30e2-8274-4dc521cece56 | -15.93216 | -49.97578 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e58667eb-9313-3f8e-91bd-b0f5f7504fd4 | -12.78094 | -48.03101 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9f660344-5b13-373d-80c0-00ad3954aa53 | -5.67602 | -43.3244 | 2025-09-14 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4204fc35-2279-360b-9651-b1ee251258c3 | -15.84564 | -47.23401 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7db4660-c9cb-3604-952c-ea33f88729eb | -17.6901 | -42.55858 | 2025-09-14 03:49:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3529daeb-56da-3afd-a670-40466eaa3895 | -14.61412 | -46.33228 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dd08597-9dac-3c04-8f0e-4f075d3214f1 | -11.45844 | -48.70332 | 2025-09-14 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10e4d2ad-17b6-3a95-b2e9-7ee7ce96409a | -16.9167 | -39.43535 | 2025-09-14 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7a90361a-eafa-3578-af1d-e6e0c6f0adc2 | -12.96934 | -48.03079 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README16.md)
