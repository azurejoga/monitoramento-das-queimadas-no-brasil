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
| e2296d18-927a-3d15-8396-d5fe2b5ee647 | -12.83069 | -44.36219 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d4a3b3c-8ba1-3a69-9e69-5b6d84372fb5 | -14.87353 | -54.53678 | 2026-06-27 04:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 69bb3732-5a00-35e0-90a4-6183808c4df4 | -12.51896 | -48.3037 | 2026-06-27 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49affda3-a452-3678-beaa-4728975adb03 | -13.87313 | -47.16273 | 2026-06-27 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33fd7ce8-9707-3492-a01b-95416381d7c2 | -14.87234 | -54.54234 | 2026-06-27 04:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 47d8124d-8cd6-365d-9f7a-641669c2bbe8 | -12.83355 | -44.36687 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4da9a66f-e160-33f0-8f0d-b9453d85c77e | -12.51449 | -48.30277 | 2026-06-27 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db26eceb-1523-3baf-b75b-995432401f66 | -12.43363 | -49.5788 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8e13a4a-0698-377c-ae80-20ea7efe9b9c | -10.54073 | -53.71378 | 2026-06-27 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a0e659b-3141-3884-9991-f723a5f55a33 | -12.44876 | -49.58871 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19674d62-f270-336f-bcdb-b85ab6ec888a | -13.43946 | -47.86631 | 2026-06-27 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 255a1cdd-a3c1-3798-8c7a-4d71a2fc7965 | -12.83273 | -44.34999 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9082e2de-1e0e-379f-a40a-aff8b11fd248 | -13.64462 | -55.2984 | 2026-06-27 04:14:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77cc19ae-fbaa-3219-b4d1-e3aee256c0fe | -14.87873 | -54.54363 | 2026-06-27 04:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afc1b1fa-db4a-3cd9-9f08-e11e6aadf736 | -13.24941 | -54.40878 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dcbf8f76-2fb2-3173-85c0-2e0398669293 | -12.82783 | -44.35751 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f9eaee3-4cb7-3d8d-a49e-88be364f14a9 | -17.83556 | -50.96772 | 2026-06-27 04:14:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a0a9f8a-8bd6-3692-807d-8a62bbc31a64 | -12.82143 | -44.35218 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e72bc66c-51fb-32d9-ab14-22a3c6765748 | -13.64391 | -55.2978 | 2026-06-27 04:14:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ebc5d2c-57b3-3a87-bc37-4cefbfa0f25e | -12.82701 | -44.34064 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 982f415f-2813-33b8-9506-ef94b9864d21 | -13.08876 | -48.17262 | 2026-06-27 04:14:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1bac327-63b9-3fb7-876a-187b8aebc238 | -12.44493 | -49.58226 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 441a150c-363d-359f-b7cc-810e287b5629 | -11.78405 | -46.47282 | 2026-06-27 04:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87484963-a12e-31e3-abed-7eb3dce8765e | -13.8723 | -50.4036 | 2026-06-27 04:14:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffbd23d8-6c54-3465-9823-f1925e8824d6 | -14.70088 | -46.14686 | 2026-06-27 04:14:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8f21e6a-7439-3632-9ab1-db6d34168dcb | -12.82565 | -44.34876 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| fa0fd5ff-fb11-375a-91bd-5f3eb5e7aab9 | -12.4424 | -49.58616 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94256ba5-a1fb-3ab1-af08-e0edca70438a | -14.86831 | -54.53002 | 2026-06-27 04:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c3a74f7a-38c7-332c-af2c-f350decdeb15 | -14.70084 | -46.1536 | 2026-06-27 04:14:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a34abca8-4cc2-3682-ba7d-7bf3c9491dcf | -12.83491 | -44.35873 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f878e0a-0149-3334-849b-bca25b89a092 | -12.8334 | -44.34594 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e72c126b-ad11-3f22-b007-ede42ce812fe | -12.4375 | -49.58524 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9744ebb6-ff69-3665-97d5-21667febf6f3 | -16.44886 | -45.01608 | 2026-06-27 04:14:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5cce765-f237-3610-85fa-f2dde8f256ed | -13.86784 | -50.39962 | 2026-06-27 04:14:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dffd68bc-9389-39b8-9b73-463442c9cb63 | -13.0852 | -48.16724 | 2026-06-27 04:14:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 667d7bad-e7fc-3238-83cf-15b6f0001da6 | -12.82633 | -44.3447 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| af2e256a-c8f3-3ba0-be8d-a972e042c071 | -12.83137 | -44.35813 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaaaec03-1f1a-3756-8f10-4583ca6c768e | -13.87402 | -47.16395 | 2026-06-27 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4783de17-90f7-3142-a85d-183ed71b8269 | -13.65724 | -53.94321 | 2026-06-27 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4483d61-13de-3d8d-bcac-e5b1a75005e5 | -13.02861 | -49.94435 | 2026-06-27 04:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d989011e-6634-3462-b28e-d66c7dada821 | -13.24292 | -54.40726 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fd194e70-fdaa-39b7-872b-6386729a3c3f | -13.93097 | -47.33303 | 2026-06-27 04:14:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8bb8a50-f099-32de-9357-d84a355795df | -12.82361 | -44.36092 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faf83c23-aa58-3b16-ae70-5402c7e5ea91 | -13.84056 | -47.13948 | 2026-06-27 04:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 186d3305-dab2-32b7-8777-2bfd56846583 | -14.85007 | -48.14313 | 2026-06-27 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51c4614f-b02b-3e69-b440-ab955c0b2f80 | -12.82075 | -44.35624 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 910aef50-a601-34a6-95f7-5cf547664b7a | -12.82919 | -44.34938 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 06557139-eb76-33b8-818b-b26a580e85f4 | -12.83408 | -44.34188 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 888ff5a2-168a-3d08-92b4-1414b7e738d2 | -12.83287 | -44.37093 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3582a895-4c72-32df-8705-e268cb3a4f88 | -13.66351 | -53.94469 | 2026-06-27 04:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 39abb12b-9fbb-3889-840e-08258fcc6192 | -11.04681 | -52.467 | 2026-06-27 04:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 731c33fd-1fef-3d89-9f05-19478889cbc1 | -12.44983 | -49.58317 | 2026-06-27 04:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b5235ff-fb62-328b-9439-879a23c8126a | -12.82429 | -44.35687 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56163dbc-935a-33d8-b3b8-9480d54a75ba | -12.83054 | -44.34126 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 17b2eaa9-8394-39ac-947f-0cc7b10a32ea | -11.04773 | -52.4624 | 2026-06-27 04:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdb84c55-a9ae-32ca-ad4f-0e5d862c70e2 | -13.26115 | -54.41761 | 2026-06-27 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c742613-6548-35e0-9876-0b88c5b74790 | -12.83913 | -44.35528 | 2026-06-27 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a25de4e-bf6c-3082-907e-409c201bef63 | -13.08436 | -48.17176 | 2026-06-27 04:14:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eec37254-c0fd-37b6-919e-95f76f4a5d5d | -14.86715 | -54.53542 | 2026-06-27 04:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d8484307-52ab-3f7b-b35d-b5878e40e21e | -22.97146 | -52.6966 | 2026-06-27 04:17:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bba062c1-9209-3fb6-ba77-b2ebfacd8b59 | -27.63909 | -52.1381 | 2026-06-27 04:19:00 | NPP-375D | GAURAMA | RIO GRANDE DO SUL | Brasil | 4308706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b06b42ce-04d9-3a94-8888-6eb50be04307 | -27.64006 | -52.13348 | 2026-06-27 04:19:00 | NPP-375D | GAURAMA | RIO GRANDE DO SUL | Brasil | 4308706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f6682358-b187-3af7-8dfe-c3583e7d4d90 | -27.67605 | -49.6951 | 2026-06-27 04:19:00 | NPP-375D | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3267d083-16bd-318a-823e-f192c0cd9f99 | -12.4462 | -58.5023 | 2026-06-27 04:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 2aa8ffa8-e10f-36a0-92cf-ed4d93cd4bef | -12.6236 | -57.8926 | 2026-06-27 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 883ca990-a951-3c32-8f38-3226694afac3 | -12.4654 | -58.481 | 2026-06-27 04:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9705c3a0-024d-36b8-a9a2-f4afa10ca0ab | -12.4464 | -58.4825 | 2026-06-27 04:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| b7961676-fb3c-30b7-8186-239b87ff99f7 | -12.4651 | -58.5009 | 2026-06-27 04:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 838a1964-9a63-38e4-a9f1-a682f34cc2a5 | -12.6046 | -57.8942 | 2026-06-27 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| fdf0a307-f227-3974-8217-fdf28af53242 | -5.77228 | -45.06388 | 2026-06-27 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f383ccc7-6c10-38ac-a44b-95ee11ad92f4 | -5.1311 | -42.88074 | 2026-06-27 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 510baeba-5101-3b9b-8b85-0816688e6a25 | -7.73723 | -44.1776 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f68a194e-151a-3e3c-9b22-9ee0d780e32f | -3.50708 | -48.03374 | 2026-06-27 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f3b5c5c-260e-32bb-bbdd-10cb98e94d95 | -7.74072 | -44.17811 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c43e237c-392c-3ffd-8442-babda387e337 | -7.29771 | -49.62115 | 2026-06-27 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 979c4c9e-6c34-3d17-9805-451b9bd1d2e9 | -3.51403 | -48.03481 | 2026-06-27 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef53e9cb-fc79-3721-834e-b9daa721e1aa | -8.49438 | -44.73916 | 2026-06-27 04:29:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28689e4c-32c0-370f-8ce2-5f0590b1497e | -6.97609 | -42.8922 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 868ae61d-f5dd-3e5c-8f0f-cb7e6ff06be7 | -7.62466 | -47.29956 | 2026-06-27 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c82813d9-9dde-397a-ada9-f0f8bca2a0db | -4.14122 | -43.65236 | 2026-06-27 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01746905-8039-3946-a95a-b674c8ddf247 | -5.55325 | -45.79162 | 2026-06-27 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0391521e-ccf6-3202-8fce-2c1693d8d5dd | -7.73663 | -44.18149 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 804fdd2f-c98c-3c7f-94b0-4f13236466d2 | -4.13777 | -43.65183 | 2026-06-27 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f01c556-9a42-38bb-b656-687c8a169916 | -6.9737 | -42.88282 | 2026-06-27 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ea67fad1-b76a-301e-9407-aa07b5397588 | -7.74361 | -44.18253 | 2026-06-27 04:29:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 329b7124-f52f-3dc7-bcf8-7d99f48e5006 | -7.49229 | -43.38746 | 2026-06-27 04:29:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 79fe270e-0cee-36d0-b5bb-96b9d151a54e | -3.86494 | -42.96829 | 2026-06-27 04:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 407d8b40-0280-3fd2-83e2-f94038e3162a | -4.14023 | -43.65158 | 2026-06-27 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61d941b8-c2e7-323c-b619-55acd986eea1 | -7.74914 | -44.62057 | 2026-06-27 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e479bfa2-83ea-3246-bb73-6f7c9845b84a | -3.86911 | -42.96483 | 2026-06-27 04:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ab10ce16-4414-3fa4-88e7-5cee53f19f12 | -8.21742 | -47.11964 | 2026-06-27 04:29:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eaae1af-a3fd-34ea-ba8d-a90de6e4e309 | -5.60115 | -46.66894 | 2026-06-27 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b3a7dd6-2ba2-3685-80f7-e0f34f165201 | -6.90504 | -43.68561 | 2026-06-27 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 685c3a81-9e9f-3808-a552-510926320c96 | -7.49591 | -43.38801 | 2026-06-27 04:29:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e74a128b-4fa9-3f45-ab8a-bcd88d3c53bd | -3.87265 | -42.96538 | 2026-06-27 04:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8fc4731e-f8c3-3e5f-a0f5-0156ade11279 | -4.14368 | -43.65212 | 2026-06-27 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac69540a-14e1-34b7-a395-392f3fe7de46 | -7.49717 | -43.37966 | 2026-06-27 04:29:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa077599-53dc-3b99-8e99-e1267b774f3b | -5.77563 | -45.06441 | 2026-06-27 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 475c3dbc-543e-335a-b407-7baa0cb9528a | -5.77842 | -45.06848 | 2026-06-27 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 796035c2-770c-3710-8ad5-d10688724445 | -4.34818 | -47.15575 | 2026-06-27 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README12.md)
