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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36442aba-4075-32f7-8efa-068ce7d92062 | -4.7621 | -43.2667 | 2025-09-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 97eb5d51-5419-3534-b735-ddb849335c55 | -4.7434 | -43.2679 | 2025-09-26 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 567908ab-0814-3e43-941b-55e17368a29f | -16.0023 | -49.01 | 2025-09-26 00:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 083288ab-f562-3a95-b476-1f364cfb8b28 | -16.0018 | -49.0323 | 2025-09-26 00:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 35f65e73-b18b-32b3-9312-86a49594889e | -11.2217 | -45.559 | 2025-09-26 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| cfb50085-1c98-3689-9a79-8d00ca8b7adc | -15.5871 | -42.3997 | 2025-09-26 00:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| cae30618-9015-3bc0-8a89-663661d195c7 | -5.7579 | -44.9704 | 2025-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e564e3d1-7e21-3c46-a1cc-244f3c145f00 | -15.9273 | -57.4972 | 2025-09-26 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 51af4642-0baf-3663-a75b-e37d36e9d272 | -5.7581 | -44.9477 | 2025-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 8c0a41a1-891e-301a-bc97-b4e292249b53 | -22.4425 | -50.4347 | 2025-09-26 00:00:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 7c799ec8-8b34-392e-958b-f8ff129ecf98 | -5.4562 | -43.0788 | 2025-09-26 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 694eafc3-75cd-3709-ad7c-5ac8fa2fb30a | -12.7382 | -43.4375 | 2025-09-26 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 29d10fa9-deb7-36e9-aec0-62c719325b76 | -5.4752 | -43.054 | 2025-09-26 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 95318441-6c86-360f-9053-e0830b546844 | -5.4565 | -43.0554 | 2025-09-26 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8a63f89a-4486-36d9-8a27-fe9850abe045 | -17.1939 | -56.3661 | 2025-09-26 00:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 714df3c2-f439-3997-80c5-9b896d4a7d2f | -5.7205 | -44.9731 | 2025-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 477dfb3f-4689-3edb-b573-d57a2b2982ab | -3.703 | -49.0413 | 2025-09-26 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 5fff5d92-ee4a-38b1-968c-2dfb02a8daad | -13.8544 | -45.5908 | 2025-09-26 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2e0c6463-64ff-39a6-beda-c8f92a23a66d | -5.7394 | -44.949 | 2025-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 240b6e7f-495c-3d58-bbab-adc284c7a5ab | -11.2408 | -45.5563 | 2025-09-26 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 26c40415-68bb-3fcc-840b-691284a84287 | -7.0541 | -46.3997 | 2025-09-26 00:00:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| f11730a3-ece9-3603-aec3-4e0c2249dcf7 | -12.7377 | -43.4614 | 2025-09-26 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| af5759c9-c8b6-331f-a55d-dead488dee90 | -5.7392 | -44.9718 | 2025-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 203.7 |
| c7786f60-f0cf-3ced-82ec-bde6e7e7a7ef | -3.6845 | -49.0421 | 2025-09-26 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| be6fc379-58a4-3a8e-9cd4-01642d417241 | -13.8539 | -45.614 | 2025-09-26 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c00b6e97-b552-3199-bcb5-7abf6efa754e | -7.0539 | -46.422 | 2025-09-26 00:00:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| ec2fadcc-71cb-3029-8578-cff01b31e825 | -17.1743 | -56.3685 | 2025-09-26 00:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 3de843d1-79e6-3f17-9427-2e2cc44b5695 | -11.0131 | -44.3424 | 2025-09-26 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 43b0ea4d-0cd1-3ea5-a03e-b520fa4d57d0 | -6.5946 | -41.9187 | 2025-09-26 00:00:00 | GOES-19 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| c98d01f0-8ea6-3735-ba71-a523438e41d7 | -5.739 | -44.9945 | 2025-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 62bbef04-1f2e-3fcb-813d-cc73afc5a966 | -5.6553 | -43.8782 | 2025-09-26 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| d5e3f7c7-ebc4-3a6b-a259-68a6b1c118dd | -11.2408 | -45.5563 | 2025-09-26 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 1a1533a7-d677-383a-9c22-1025533e810c | -16.0018 | -49.0323 | 2025-09-26 00:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 78e2f7a1-f6ca-36aa-b4a7-53d48f461202 | -3.45 | -44.1238 | 2025-09-26 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 8acf02c2-3fd1-3a7c-9408-6fe29a83f67f | -17.1743 | -56.3685 | 2025-09-26 00:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 5e190f85-6cf8-3e76-9673-005c75123e8b | -12.5577 | -45.8 | 2025-09-26 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| fa41c706-a319-3f2a-8bfa-3bd333e61eb1 | -10.0062 | -44.1766 | 2025-09-26 00:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 6d63adfc-7fd6-33cb-917f-6ba084e3cfdd | -3.534 | -59.2128 | 2025-09-26 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2d89ba64-128e-3ea0-a3da-9e839d3ac8fe | -16.0023 | -49.01 | 2025-09-26 00:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 937ff392-b55f-371e-8f7f-1fb1f9d1e0f6 | -13.6877 | -44.2899 | 2025-09-26 00:10:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 8b3ded48-e2de-352d-be39-51520c765841 | -3.703 | -49.0413 | 2025-09-26 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 78b02225-1a89-35f2-b333-a201be3cd5e4 | -11.4425 | -44.9303 | 2025-09-26 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 807dfc2e-0b22-3022-8eef-3e1b259373e9 | -5.4752 | -43.054 | 2025-09-26 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| b90299df-1488-3631-96f7-1dcc81f0efa4 | -13.8539 | -45.614 | 2025-09-26 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1bec32ef-11a2-354f-ac06-6f5c14940598 | -11.0131 | -44.3424 | 2025-09-26 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4616e53b-6d74-3262-8389-6b905ec259ac | -6.5946 | -41.9187 | 2025-09-26 00:10:00 | GOES-19 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 008294ce-7a79-3321-b5ed-2bc4b1c23d26 | -17.1939 | -56.3661 | 2025-09-26 00:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 4253cd8d-a558-37c4-aa44-837a3b971e12 | -12.7377 | -43.4614 | 2025-09-26 00:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 477b345b-64c5-3483-949b-e2ec1d443942 | -22.4425 | -50.4347 | 2025-09-26 00:10:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 60.0 |
| dd857026-8877-375c-b9c3-d36d9a032753 | -12.7382 | -43.4375 | 2025-09-26 00:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e82fed13-6f54-38a0-83e4-321dcf16e9e8 | -3.6845 | -49.0421 | 2025-09-26 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 279eb4c2-f9a3-3ebb-9912-206d922358b6 | -3.534 | -59.1937 | 2025-09-26 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8ad50d11-5f85-348a-ae7c-5c8157b6bd0a | -12.5573 | -45.8229 | 2025-09-26 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 967c978e-48f1-36b5-9660-619d6923b5d3 | -5.4565 | -43.0554 | 2025-09-26 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 80eb9cf4-c6b5-3658-8620-a12d070450e2 | -9.9048 | -45.8646 | 2025-09-26 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 76ebe558-14c5-3616-91f0-c477108b4516 | -13.6877 | -44.2899 | 2025-09-26 00:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| af999778-0b7e-32af-b28a-bf34e9e3fc70 | -9.9238 | -45.8624 | 2025-09-26 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| fc6c245a-135d-3313-9384-6a01a595695a | -10.0062 | -44.1766 | 2025-09-26 00:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 68034b07-7163-32e6-a2d3-02d15bfa9214 | -16.0023 | -49.01 | 2025-09-26 00:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0be692fd-0213-35ee-9ad3-2309f910a4fd | -12.5573 | -45.8229 | 2025-09-26 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 85d31e47-1cde-32d4-ad48-f139a9c5c59e | -11.0131 | -44.3424 | 2025-09-26 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| cca96726-441c-3fa9-861d-c4d36f23e6b8 | -12.5577 | -45.8 | 2025-09-26 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e385a0c8-10b7-370c-a3aa-9377924b599e | -12.5765 | -45.82 | 2025-09-26 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 0dd85468-5ecb-35c2-87e8-656eddfbcc57 | -13.8539 | -45.614 | 2025-09-26 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2d377e7b-126d-3231-9952-b64f157ddbc5 | -9.6922 | -48.9438 | 2025-09-26 00:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1689b1de-f1b1-346f-ba7e-951e7f36ac9a | -6.5946 | -41.9187 | 2025-09-26 00:20:00 | GOES-19 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| bfbf094b-3572-3d65-901e-6080cd9950af | -3.6845 | -49.0421 | 2025-09-26 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7cc66753-5897-3eae-a12a-4bf74550dbbb | -7.0541 | -46.3997 | 2025-09-26 00:20:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 66d33858-8e6a-31b0-9f27-e5981d803963 | -11.2408 | -45.5563 | 2025-09-26 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7845be41-d03c-3e1e-9d93-695f451dacb3 | -11.4425 | -44.9303 | 2025-09-26 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 003c6192-043e-35b6-b91d-c040acf8a1b6 | -17.1743 | -56.3685 | 2025-09-26 00:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 9b36e435-aa87-3701-988d-bcc8fb8262aa | -17.1939 | -56.3661 | 2025-09-26 00:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 6944fc64-b4c0-3dae-8f1f-0dd7b6e699dc | -3.703 | -49.0413 | 2025-09-26 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 2853c675-0523-36cd-bbca-d174e0b9871e | -16.0018 | -49.0323 | 2025-09-26 00:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9d35af76-4466-3fe5-b55e-cabd5d3a0435 | -13.6877 | -44.2899 | 2025-09-26 00:30:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 67f0ca8a-c44e-32dc-b128-0abadb5b5843 | -17.1939 | -56.3661 | 2025-09-26 00:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 80f0b4a7-7581-3643-8b71-6470c3af15d7 | -9.6922 | -48.9438 | 2025-09-26 00:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| dc33d960-ceb1-3aab-ab08-28bacd3e3ad7 | -12.5577 | -45.8 | 2025-09-26 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1ec8dd0e-d5f6-3dc8-9a88-5b3482784ad7 | -16.0018 | -49.0323 | 2025-09-26 00:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4bc24484-9ced-3ff5-ae76-b094220f91a3 | -17.1743 | -56.3685 | 2025-09-26 00:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 89bce32f-501b-364a-b16c-b3d23f366def | -9.8728 | -46.7683 | 2025-09-26 00:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 92329486-a15a-3a28-9b26-0e4b63f4306a | -11.0131 | -44.3424 | 2025-09-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| fd2df344-2670-3150-9d5e-1f1343dc8ddf | -13.8539 | -45.614 | 2025-09-26 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d8db1c99-ea12-3d12-9c3e-6da914b2a19c | -11.2408 | -45.5563 | 2025-09-26 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f5c4a04b-6850-3166-a5b4-b4d695ac0f31 | -12.5573 | -45.8229 | 2025-09-26 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 10a228b5-d956-32fe-9e78-f49fe0cae77a | -12.5765 | -45.82 | 2025-09-26 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| cff1936d-7c02-3578-8fcb-955fb6664a36 | -22.4425 | -50.4347 | 2025-09-26 00:30:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1c069a3c-2ebb-3b34-987f-d7bfea9bc4bc | -3.703 | -49.0413 | 2025-09-26 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 19d818a9-d80f-3d26-afd4-3f8cd8907d41 | -22.4431 | -50.4117 | 2025-09-26 00:30:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 115.0 |
| df7f3f46-305b-33ff-916d-70714e2f2eba | -12.5568 | -45.8459 | 2025-09-26 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| d32a2e82-e482-3659-85e3-ecbb87a0a280 | -12.5761 | -45.843 | 2025-09-26 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 8956cb26-e708-3152-aedd-c081bd1a4413 | -12.538 | -45.8259 | 2025-09-26 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| d840c93d-5155-3737-84dc-32311a6d6471 | -3.6845 | -49.0421 | 2025-09-26 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 20c7676f-30a6-35fe-9a79-1d14fa11b459 | -17.1743 | -56.3685 | 2025-09-26 00:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| b8e56fb5-f0dc-3f48-8a10-f3ecf1032a0e | -12.7382 | -43.4375 | 2025-09-26 00:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 568497e9-19dd-3168-afe6-840d15e47827 | -12.5765 | -45.82 | 2025-09-26 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c77b6664-9258-3314-8840-61844705579e | -11.2603 | -45.5308 | 2025-09-26 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| a2039810-74ef-3214-a3df-99015b32e747 | -5.4565 | -43.0554 | 2025-09-26 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 13235ac6-27ce-358c-8ac0-1cf3ca1a5d43 | -13.8539 | -45.614 | 2025-09-26 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d6cea269-c425-3be2-b287-9eadd3b7c62b | -6.5946 | -41.9187 | 2025-09-26 00:40:00 | GOES-19 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |


[Clique aqui para ver as próximas entradas](README2.md)
