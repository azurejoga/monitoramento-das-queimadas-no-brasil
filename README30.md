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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43dde5dc-2b56-3c71-bc4e-b67e4577d380 | -7.95715 | -46.71732 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9516434-1609-38e5-815a-58892f0cd9ba | -13.3449 | -47.66716 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d95ac041-d4ee-3268-ab43-45f472ae0def | -8.05211 | -45.17629 | 2025-10-30 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7e2c12b-2294-3e70-8e8b-77f98bd70f6c | -12.39574 | -46.8241 | 2025-10-30 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5df27111-cc91-3cee-8d83-cf65d63daba7 | -13.30368 | -47.69837 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 285044d4-ca59-30c3-ac2a-d853f21f1d91 | -7.95932 | -46.731 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f814af2-904c-3f8d-8b42-09846d1be33e | -10.90078 | -47.99833 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fdb4a69f-61af-3a20-8e3a-8fdbcd5900db | -11.15653 | -43.48129 | 2025-10-30 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e77d211-7953-35c2-9142-7f69d5c30ba1 | -10.42248 | -45.05118 | 2025-10-30 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 896a5bb4-be3c-3237-9f81-1a264cbcd0d2 | -10.61519 | -47.8895 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec1898fa-012c-3165-b8a1-0b6b7f4f617b | -12.4885 | -50.60662 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22b9c174-c725-36b6-8a9c-58b3ae072363 | -13.87341 | -43.55877 | 2025-10-30 04:06:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0404eb2-75c9-3d7a-a06f-bd072ae3210a | -9.88681 | -47.44382 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5190d157-2397-3441-807e-4dc72b401262 | -12.75108 | -43.4297 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 429c3eae-05a4-3f0e-85a3-8e97c25229fa | -8.32359 | -47.92202 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d9972f58-3596-3dfa-8ade-30ec33bfd71c | -9.80572 | -47.58216 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bc3ce4b-9e90-35ca-b712-bb47527ba622 | -10.88233 | -45.0781 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5d809f7f-3065-3b1a-984f-0ddb391122de | -13.32842 | -47.68461 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a1dd118-6a96-3af2-b944-073a70310505 | -10.27468 | -44.57993 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beeeceb4-11cd-3a4f-948d-b6ba20864668 | -13.36004 | -43.08726 | 2025-10-30 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d0d09051-4c48-3ff9-a2f4-e7305bc69254 | -13.41452 | -47.37701 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 133a5961-958d-31a4-af02-89ce51433d99 | -10.23262 | -47.6372 | 2025-10-30 04:06:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e936d1f-02cf-3651-9c1c-a661f25e0202 | -14.57039 | -40.72189 | 2025-10-30 04:06:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df1e3ac4-0405-3629-a7fb-d52ddc039e07 | -11.55612 | -44.68952 | 2025-10-30 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d555651d-da0f-35ee-bdc5-a9770cc10a3c | -11.16241 | -48.34624 | 2025-10-30 04:06:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 418031af-437e-3f38-89f6-a59f4c5bf992 | -14.69144 | -43.15175 | 2025-10-30 04:06:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d07de4e2-84ef-3647-90ba-d3a6f0194874 | -13.56688 | -47.32523 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3d65072-2891-372e-89ae-c76c1c48c87d | -13.61019 | -48.40974 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7258ad6f-b394-35f3-befd-6ec93920ad59 | -8.0538 | -45.16621 | 2025-10-30 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57cec2d3-2911-3b93-8565-729af86496ba | -8.32836 | -47.92282 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 210e9873-73d6-31a8-bda4-d278b461638b | -14.23209 | -44.31879 | 2025-10-30 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b2fdf08-c825-3d58-a036-ac96a5a5fc9e | -12.50692 | -50.56896 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 97c86c47-92ea-3f4d-a3ea-70e94dc0072b | -11.35953 | -42.25647 | 2025-10-30 04:06:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1ee53b37-dbfa-37b2-836d-f9393e9f98da | -10.45375 | -44.31753 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0c0470d-65f9-3cb3-9747-365d0b96edf2 | -14.129 | -44.07286 | 2025-10-30 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff172e8b-9d60-3133-bf58-38a1e0f6bfae | -13.03015 | -47.0318 | 2025-10-30 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5108dcb8-3826-37d5-871f-99f4ad2b5499 | -12.49348 | -50.56324 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3dedf688-de36-3ca1-9c18-2517cedd77fd | -13.32702 | -47.69233 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 196e9a6d-4bf5-3f74-a2ac-3824499c305d | -11.32894 | -47.96959 | 2025-10-30 04:06:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62e2077e-0262-3134-a711-da68bd4304df | -12.03059 | -44.80576 | 2025-10-30 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6607be12-a776-3a02-9f0a-368fc2db3b3c | -9.84767 | -47.6884 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b2b370-cd71-31c9-8248-bfc044ec876b | -11.84599 | -47.92337 | 2025-10-30 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2da3680a-c2d6-329a-bd4e-54fa83de0e7c | -13.32737 | -47.44904 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba777f36-e0ce-354b-b946-3874cff4aa5c | -13.4054 | -47.37946 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1fa6c88-4049-3705-a8f7-443aff727197 | -11.55537 | -44.69392 | 2025-10-30 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaedfd72-b352-3fff-9e19-21a2fb047665 | -10.85253 | -47.87545 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50549b0a-8154-3034-9028-a2faac14acfa | -8.31471 | -45.37001 | 2025-10-30 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9709526f-225f-3c56-86cc-2b60556a97d3 | -12.52271 | -50.57218 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eea1e521-cc09-34ed-a258-d5ee5ae503ef | -14.39137 | -43.71935 | 2025-10-30 04:06:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12848fa8-b946-34f2-bc08-0b806e1bee9c | -12.47787 | -50.58765 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a45cbbf-a428-3692-b840-8818095bd7ca | -10.08987 | -36.24402 | 2025-10-30 04:06:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 528bd4cf-0d97-3d89-9e78-fe922a3c6992 | -8.15341 | -44.80941 | 2025-10-30 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99302a76-8a41-3b57-a112-b99ed53f1149 | -7.95412 | -46.73467 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a037cdad-5d28-3411-90d0-c7e6e87088cd | -13.16427 | -48.45283 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c66fb5d0-fd7b-334f-a80c-2488b6b454a5 | -10.35644 | -48.70431 | 2025-10-30 04:06:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a91d175-e7cb-34f6-830f-3f15700ce40a | -7.88116 | -46.74174 | 2025-10-30 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9e4624d-fc23-3faf-bed6-9cdc0a5ce569 | -13.27776 | -43.11886 | 2025-10-30 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2c9c41e-7054-35c2-b474-7d012aee8a5e | -12.47978 | -50.57767 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a638854c-e80f-37b6-a209-ab4ccf379880 | -10.8565 | -47.61741 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ba3e91-5428-3d1e-91f9-3c7231e16d31 | -11.38893 | -46.04043 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 396a4e9b-74c5-3645-8cd6-9061b863bf49 | -13.47515 | -42.50658 | 2025-10-30 04:06:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7a1406a4-cc9d-3629-89dd-7fc04409e824 | -12.30247 | -50.2626 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 39fe1016-ceda-3892-9e87-cf9face53ea8 | -9.91162 | -44.91572 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f09bd80-6925-30c6-ab1b-7ee92d4165c0 | -10.7665 | -47.88375 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f10b55b0-e706-306a-ac48-d776375453b9 | -12.91284 | -43.19265 | 2025-10-30 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e4b87aa-4a7e-337a-bf7c-f9445a491003 | -12.17565 | -47.75265 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97a89b52-5286-35ba-ad0a-5ffe9a794c49 | -13.59957 | -42.51231 | 2025-10-30 04:06:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 207b5a37-48d4-376d-9080-eee9f1ea6b6f | -12.49159 | -50.5732 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5ac8dc56-4af0-367a-a5e1-b4fea764abbf | -11.53185 | -44.96593 | 2025-10-30 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52bf1aa8-12ef-3085-90ed-23e1ad44f50f | -12.03133 | -44.80133 | 2025-10-30 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1adc151f-a490-3aeb-a9b7-98c91e476b80 | -8.29092 | -49.32002 | 2025-10-30 04:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f0f60f1-8cf5-383e-a8b6-80028679832e | -9.23547 | -45.56226 | 2025-10-30 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3e2992c-c2a0-3935-8c3b-f33fd90d33ab | -12.47723 | -50.59098 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5268729-419b-3dbb-be14-ab5a600c384b | -11.96411 | -43.28797 | 2025-10-30 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cf9d1da-2dd9-379c-854f-5709a6ef57f0 | -10.75329 | -44.74262 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8b9fc98-5dc4-3da6-9f7c-6f79c6c08a80 | -11.33347 | -47.97047 | 2025-10-30 04:06:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d109a3ea-0b43-37ff-b91a-49c4ff96f278 | -13.34996 | -47.66368 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| badb72b7-47e0-3f50-bfe6-7bdf5b47fb9d | -9.89358 | -44.88348 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b145fea-ef5a-36b4-ab5a-8e92f2024842 | -13.52686 | -44.34599 | 2025-10-30 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d42b7408-066d-39d7-b91e-8212b97cff70 | -10.27545 | -44.5754 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65f63942-7e86-3693-84bb-211689545edf | -12.37162 | -50.1521 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9222ebc-a29f-3919-98e8-b2372838c8ce | -13.2716 | -47.75155 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aad7c341-6eca-3531-bb3b-e70c6ab050c7 | -10.23365 | -47.63438 | 2025-10-30 04:06:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 903f3bec-102c-309e-88e8-bd5f09f875de | -10.98424 | -50.21525 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 294cb4c8-75c1-3f43-b492-2812e740ac45 | -12.36757 | -50.15105 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad4e8581-7f38-3f28-9821-7c1c12d0fe6a | -9.49699 | -40.37309 | 2025-10-30 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ccb059f1-35ed-37ef-adf7-ef8b350ae839 | -10.27318 | -48.05921 | 2025-10-30 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49193dd8-a19b-39b3-8155-2fea6147cc78 | -9.29344 | -48.42207 | 2025-10-30 04:06:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3f14845-883f-3d23-99a8-6e674eccf619 | -12.75452 | -43.43029 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8144e8f3-cfb7-3a86-9da0-f512df867783 | -12.91927 | -45.04597 | 2025-10-30 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c52e3e7d-6b43-3498-a794-0582c1119b05 | -13.45721 | -44.07017 | 2025-10-30 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76685f16-2ebb-3697-b80a-c84483159151 | -10.9277 | -50.204 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54ac2eec-28cf-34a6-86a1-9af8a2fd650c | -9.82236 | -47.69797 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6ab18863-efc2-3594-92dd-2a3c1b4db437 | -12.48695 | -50.5688 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 895d04a3-2d65-3105-9653-501d03ff5396 | -11.03758 | -47.8393 | 2025-10-30 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c686c12f-c229-3d26-8348-5af8b1503333 | -14.71592 | -42.44777 | 2025-10-30 04:06:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8296da6a-debd-35e3-8923-1beb5270df07 | -13.03484 | -48.46713 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 021e724c-9507-348a-ac21-3c84308e7f36 | -9.90642 | -44.90016 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7d3b8af-677c-3e59-b236-18352e13cdf0 | -11.71829 | -41.65991 | 2025-10-30 04:06:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c52739e-4c99-301e-80d6-ce7bc4ce83c6 | -12.66783 | -47.3413 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README31.md)
