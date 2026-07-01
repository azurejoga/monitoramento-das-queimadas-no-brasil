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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dfaae09-9cfd-3c13-a180-b8ad04bfa7b2 | -10.80956 | -49.34051 | 2026-07-01 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f76c5eaf-d6f5-3adf-8813-d45850255fb9 | -12.8437 | -44.34673 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 4649c8c1-7a03-3e4f-9686-fd1a8b90a432 | -11.90109 | -57.38735 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 920a59d1-b7ea-3417-a5dc-17400a316beb | -9.88332 | -50.39708 | 2026-07-01 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e7705a40-790a-3401-9010-a898a5536fe9 | -11.43492 | -56.06439 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 78d3f453-8fa9-3e80-b912-3b0a5652e2c5 | -10.67434 | -54.52517 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 769394be-75b5-3366-86fd-ed06ceea9296 | -11.4187 | -56.06748 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b2ad08d4-449f-3f9e-9b0d-e74f53257fef | -11.42933 | -56.06639 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0ba419c2-f23a-34a8-b1b8-f02ec74c4948 | -10.43783 | -49.5793 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffce0cc0-5ee4-3a00-b1e6-d87cf22dd524 | -9.02803 | -59.53644 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6657d373-c04d-3ea7-b26f-5dedf08da9f6 | -9.17512 | -58.06791 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18756b61-5184-3364-abf9-510338ab6017 | -8.60139 | -48.0084 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7962c4b-1a68-303e-bc49-46a89c929b26 | -10.44066 | -49.58372 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11791274-1ae2-3f33-928b-6d06301dc1d3 | -9.02316 | -59.53559 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfea0355-6ec8-33fe-a619-0d7559083022 | -9.88763 | -50.39351 | 2026-07-01 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85e25649-d757-30ed-a58e-842045927946 | -10.66429 | -54.52823 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18e0d7ff-abfe-39a2-8531-70e01142ecdf | -10.83831 | -54.0377 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55d03b41-155a-3743-ab63-2d153a2f023c | -10.76092 | -42.1077 | 2026-07-01 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 84340526-998a-3952-a7fa-4ad27e861483 | -11.42659 | -56.05345 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14a33371-866e-3040-a4e2-dbe7c2ee673f | -11.42099 | -56.05551 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| e3316bd3-ee95-3de7-ac72-f07a478c7c08 | -11.4385 | -55.90954 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0041571-879a-3cbe-999b-56aa588d0302 | -9.33171 | -58.01701 | 2026-07-01 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8457e2db-9734-388e-8c26-b4938cd701ea | -12.83565 | -44.35006 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 611c1081-bb53-3ad7-969d-4c97fba526b9 | -10.67059 | -54.51966 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d4734bc7-e32b-3e80-b527-a4a3af39922a | -11.56341 | -52.80573 | 2026-07-01 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83350140-1b78-3310-a173-b9dfed7d4bd0 | -10.78442 | -53.55513 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb1c0e86-a7e4-3d95-8b2a-d45fdc027cc2 | -11.54696 | -47.45204 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8f1e6b80-8c99-3061-b4b6-e28261cd7a9c | -7.73916 | -45.91605 | 2026-07-01 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26d010aa-3586-3e65-93b0-ac32e50ede9c | -11.42488 | -56.06241 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| c4bd7a9b-4809-3d78-b07e-fcb2531c0e55 | -9.69541 | -47.69244 | 2026-07-01 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69a8c951-08c3-3599-90a0-cad89b5f53de | -11.04359 | -56.92449 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37b78d81-2f34-396e-a82f-2e13580e948d | -12.41625 | -58.40477 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c973456-14b3-3b6b-9659-71b01e2ea7cc | -10.92207 | -43.05928 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 593b5e80-4c03-330b-9fbc-2cdca7a84105 | -10.92668 | -43.05491 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 49ea8759-9e61-3f4a-9ef3-06cdc905ed96 | -10.66257 | -54.53768 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4b49aaa-8388-3c07-9198-b4298438188d | -8.9872 | -45.71862 | 2026-07-01 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fc6d127-ea76-3d33-b850-f57af05c3503 | -11.9072 | -57.38485 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71f8b484-d214-306a-a78c-58d13257e94a | -12.21449 | -56.56208 | 2026-07-01 04:38:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c3f82a0-3797-303a-a21e-6de26a0d2806 | -12.1499 | -57.22493 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ff730bf-cd85-3f18-a7c5-0caf59ff9e3a | -13.48197 | -47.87437 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 127dd43f-3023-374b-9a5f-12d3fe7cade3 | -11.79001 | -56.99985 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d70f50f-c505-3add-9dd9-6abb1862db5f | -12.44388 | -46.9216 | 2026-07-01 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a61cc74d-396e-3fa5-90ca-9412710e43bd | -10.83352 | -48.76226 | 2026-07-01 04:38:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0c7a16a-9dd2-32ba-a83e-c4e6922a35ed | -12.4187 | -58.39246 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c00d2219-419c-3d86-b640-3e4810549886 | -13.72069 | -47.88451 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5210111c-e697-3885-bd74-296df1243be6 | -9.60302 | -56.92741 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 007f19d1-04b4-3291-a7f7-57c24f8c2db9 | -11.9148 | -43.39167 | 2026-07-01 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 926d7443-a7d4-31cf-af18-501ef4c8bc1b | -11.50138 | -54.50107 | 2026-07-01 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a9e453d-addb-3ab1-9ee5-07add1bab7f9 | -11.4906 | -49.8738 | 2026-07-01 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9f78b8c-20ff-3c34-afb0-773064c04b63 | -12.21904 | -56.56607 | 2026-07-01 04:38:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7930cf74-32f3-3a49-bff3-b2528cb21e2a | -11.79532 | -57.00087 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a8b9528-c5de-34e4-ae20-c11ab94e6f2b | -11.53873 | -46.65779 | 2026-07-01 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8be8483b-8223-3d26-9da7-208abfc0a1e4 | -11.78468 | -56.99889 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b56b517d-8859-3c1b-9b86-efab54b602c9 | -9.60437 | -56.92015 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa7a82ce-01c4-3554-b6e6-5509b5506159 | -11.54209 | -46.65832 | 2026-07-01 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4c78b56-f679-39f4-bf32-ea5a307e7d2d | -8.12772 | -47.88469 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3007690-a85b-391f-8f29-9fe7aea7d5e6 | -7.29105 | -46.25246 | 2026-07-01 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75e9fd49-e613-30e7-aebc-b3a9570ed522 | -11.53255 | -47.45692 | 2026-07-01 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36a83204-2da6-3a96-b887-9b6dd294e76f | -11.5464 | -47.45556 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7bd567a6-552f-388f-b66d-4dd6ef4c2457 | -8.12101 | -47.88361 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ffa44bc-fd4b-35d3-9bfe-ad15e504202a | -12.41293 | -58.39144 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4d060c6e-2f97-3e86-b6ea-bc667d05bf57 | -12.41707 | -58.40067 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cffa932c-6093-320f-9d2f-251a132f22cf | -7.28772 | -46.25193 | 2026-07-01 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f10e0c4-9d3a-31c5-bc6f-378014009cb7 | -13.72401 | -47.88506 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31cf680e-daab-3e71-8906-7a9a2d6e9ee6 | -10.43656 | -49.58697 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa420545-2c27-3da7-a83d-c51545514a57 | -10.37983 | -49.58532 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a2d8bec2-1cf4-324a-ad9a-5aaf58182b42 | -10.66599 | -54.51881 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 23b33982-54d9-35cc-8fe2-ad30f7a8c978 | -8.69192 | -50.70224 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1acc6c1c-e079-3049-b33d-23733f920a1c | -8.80483 | -47.48009 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0382dd32-32ed-3d8e-8aab-7191da8b55aa | -10.66889 | -54.52902 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7efdd77b-e226-3ebe-945a-94eec62c731c | -9.89054 | -50.39831 | 2026-07-01 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85234b40-0e11-3392-8df5-a91c2e5e181b | -11.30523 | -51.39769 | 2026-07-01 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 771875e5-148c-33c3-9f01-945cd905e0ea | -11.41813 | -56.07047 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 69032188-e864-33f6-b232-fa60627ab88d | -11.91808 | -57.38692 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6563d29-1612-3320-8984-7b8b863d5a1a | -8.69268 | -50.69776 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11fd41e6-ce81-3e96-b864-81a04838d646 | -8.12437 | -47.88415 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fcac779-6fb1-3e79-97b0-b11b8bf81d52 | -10.92597 | -43.05986 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7e854c84-6a99-3ec0-940b-ba43e181258e | -10.75932 | -53.54644 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09ba5ca0-ff0c-3dbf-93c5-368f40ef36eb | -9.69105 | -56.10015 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8199893d-bc3a-35ba-938e-81a10058211f | -12.84741 | -44.34729 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 55375cc9-3925-3bab-a099-3e10ded6807b | -10.97481 | -49.67488 | 2026-07-01 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d148e1-5315-3d44-8367-b2c4cd558ab3 | -9.68586 | -56.09917 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0a50aee-6073-3ea8-8cbe-8939be8f6192 | -14.0462 | -46.33101 | 2026-07-01 04:38:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c614a6c-9405-3c32-a9f0-386441b6ae76 | -10.66514 | -54.52354 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 593bcad3-6b07-334d-8021-165454453cb5 | -9.28218 | -48.76369 | 2026-07-01 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfcdbbe2-2172-3342-9ace-95e8372e855d | -8.59688 | -48.01496 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20db4455-4b1c-379c-8764-326ac6042d06 | -10.66631 | -54.54333 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb92d002-1603-31b0-8055-4aca475fc12a | -10.79697 | -53.5429 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 997e6b68-2a7c-34e2-8162-d93c90036000 | -9.20729 | -45.33167 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0de35bd-16a9-3cad-b8b1-9fcc220a581d | -8.50458 | -50.42746 | 2026-07-01 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5942c972-5463-3bd5-b79f-6aacf0322377 | -9.19759 | -45.32635 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e53af3d-4e89-3bff-8411-00dec2007832 | -12.76342 | -44.49408 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 2971dca7-129c-37b6-b990-6c2fa9e0d2a0 | -10.12226 | -52.08929 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4342d5eb-0c95-3f05-8905-5df4dc17352c | -12.41131 | -58.39959 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c2a391a-ebc8-39d9-84dd-3e3b96c58d04 | -11.53975 | -47.45448 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af3ce68c-fa56-3c5f-a2e0-304609c615af | -13.47865 | -47.87383 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af99c765-5465-318a-8b67-699f02e7d1ac | -11.42316 | -56.07142 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ec75cd7-c64b-3031-9e18-4321f997cb11 | -9.97536 | -48.24157 | 2026-07-01 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0aa0b0bd-ed67-3def-a608-b59111c586d0 | -10.66343 | -54.53295 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 438a47f1-e854-3fe0-880a-90ba61f1ed95 | -10.67894 | -54.52602 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |


[Clique aqui para ver as próximas entradas](README19.md)
