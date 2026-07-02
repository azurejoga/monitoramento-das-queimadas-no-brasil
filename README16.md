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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6a9a0a3-14d6-3ad4-982a-b8dade8188ea | -3.51657 | -48.03902 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2514ca1-a8bc-3810-a115-3a189aa032a3 | -6.922 | -43.71642 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8447c5a6-b166-3ab5-a842-c99012c67fe4 | -6.93122 | -43.71954 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f24a001-3c01-39de-be60-50401f724d18 | -5.81444 | -43.79746 | 2026-07-02 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e06c3ac2-a7c4-3bd1-aefc-29023a48eff8 | -3.50329 | -48.03693 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1e5b24d-858b-33aa-b2a2-38abb6343c40 | -6.92512 | -43.72181 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d5e7c83a-a636-3fd3-8301-9b9dcd3d6a8f | -6.92736 | -43.71896 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65dd53fb-07f3-3813-a836-4b9f2e57b4c9 | -4.28497 | -48.35686 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ec4ce9f-fa0c-3617-80b7-70eb0d3555e6 | -3.47499 | -39.57755 | 2026-07-02 04:36:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 44ff031e-7463-38da-a47f-5246b2a8d1e9 | -6.48549 | -43.72834 | 2026-07-02 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a629f760-935e-3a9c-ac3a-a436d51803cb | -5.78727 | -45.04944 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7de8cda-26b9-3e04-a2d6-387066456d8c | -3.66946 | -48.97751 | 2026-07-02 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab47468b-d2fd-3f2b-aa72-5378054683fc | -3.51048 | -48.0345 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f81e29c0-46d4-3fc7-90d1-0e5050ade582 | -3.87197 | -42.96623 | 2026-07-02 04:36:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bad1747-119e-3e14-a3a0-646495903f83 | -7.00529 | -42.78025 | 2026-07-02 04:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12a25e5c-fbf7-3a5f-a57e-8b78e95d89a1 | -2.4326 | -47.03057 | 2026-07-02 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d531536-9ce0-3586-92d6-e9d0112a990d | -5.34701 | -45.18348 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2fa4bd89-208d-3ff7-aede-ceae20bf4a1d | -4.25917 | -48.53972 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ee05893-f6f6-31ba-82b7-691d282123a4 | -5.12519 | -49.32904 | 2026-07-02 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3feb5fc3-a50c-3d74-b740-a3e094f6d7b4 | -4.28441 | -48.36034 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d65c662d-657d-3269-a0a3-3ec44898a5f4 | -4.00601 | -48.05944 | 2026-07-02 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4b3c9a0b-4f5d-3edd-9753-205a0ce08133 | -5.79265 | -45.03798 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d92ba6da-900d-3b5f-a2ed-00a5dabb4894 | -5.47093 | -45.41879 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1057ae1a-3d37-3594-9794-cb0714196b96 | -4.00933 | -48.05995 | 2026-07-02 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 94722e44-e646-3703-925c-08ff6d9dfd80 | -9.17969 | -49.6685 | 2026-07-02 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43dc2d8c-4161-3193-9757-c478cb809dbb | -11.85231 | -48.23969 | 2026-07-02 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa41a6f7-51ca-3020-9d4f-38893b1d9721 | -12.76499 | -44.52846 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6bab24f4-2e0e-3d08-a214-b257ce139a30 | -11.17125 | -49.5228 | 2026-07-02 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be059f92-06ed-3c61-b0ed-cdd6af428799 | -10.12399 | -52.10044 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da6532b4-dcbc-323a-8cdd-f159773d3471 | -10.80038 | -48.56155 | 2026-07-02 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2220e588-2689-3cbf-99df-5ab4dcc0d190 | -12.51521 | -48.27826 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01733bb1-a823-3ade-a5a2-781e05d65bd5 | -10.12541 | -52.09194 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f72f51fc-7bd8-3221-b919-a7b69ff66a30 | -9.02059 | -59.53574 | 2026-07-02 04:38:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4fa8515-3b80-37d2-a78f-d63c86a944d2 | -12.75804 | -44.49019 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f70c85a7-0d3b-386d-8440-45fbb3ba7831 | -12.50853 | -48.27718 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d32ee7c-4b90-3011-bc5a-53b98106b8a0 | -12.85029 | -44.3546 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 63fb7623-88e2-3899-a862-1c24f213e17c | -9.20471 | -45.31849 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 926ad44e-3e38-3662-8a07-d4d46da23212 | -12.76262 | -44.48639 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4731393b-c49e-3f94-bea9-72db35de371b | -10.37715 | -46.6693 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331ea4a9-c4fd-3596-be38-aa936344eda4 | -9.18858 | -58.05167 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4152dcf2-3015-3fa9-8478-184acf1dc7b7 | -12.14458 | -45.81584 | 2026-07-02 04:38:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0627734-0a9e-370c-a429-1e503761c0ea | -10.37275 | -46.7042 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| dfc5b2a7-8332-343f-84e7-fd1391b6f7e1 | -9.20108 | -45.31796 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b535a76d-40d4-32a3-9169-43c8a7b37f74 | -12.76101 | -44.5279 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 73b3b3c3-d4aa-39a0-8e22-3e6015ea2f48 | -9.18795 | -58.05508 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df42da89-d04e-3ec7-8143-8d61fc22cad2 | -10.79983 | -48.56506 | 2026-07-02 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b9e8d8d-87db-3c55-8dfc-074539415ab4 | -10.37258 | -46.69991 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4cf704c6-7b4a-3121-8c85-0cb047abafe5 | -10.25077 | -48.14653 | 2026-07-02 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9fea828-b76f-3cce-a6cd-ff9e2a774d9f | -9.74412 | -49.03186 | 2026-07-02 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9eb8d5e-b885-3775-b6a7-03b8d121f0fc | -12.45402 | -46.52343 | 2026-07-02 04:38:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6436afa8-bd6e-3d42-b4a6-7c0d31d2da72 | -12.77857 | -44.48867 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f70e0c1b-3ff2-349c-8443-9b9c09d0a238 | -7.91247 | -47.30946 | 2026-07-02 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89c91105-a162-3196-89b3-0f9ce02fe3d3 | -9.157 | -47.23164 | 2026-07-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d01b6655-02e0-3a13-ad45-be25c309bcf8 | -12.92154 | -49.47797 | 2026-07-02 04:38:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9487361e-2bad-3da7-9512-23904e256ba4 | -9.82299 | -46.42715 | 2026-07-02 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79860c98-3a6e-3f2b-bb46-2cb53b70213a | -12.50797 | -48.28078 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcf7675c-f845-380d-bf06-4f7a0f1b23f3 | -8.49702 | -47.19639 | 2026-07-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fda012c9-f33a-3c4f-a03e-0ddc9d657068 | -10.36989 | -46.69983 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4af0a05f-d9ce-3de7-a4cc-f1e4b582494e | -7.90843 | -48.24459 | 2026-07-02 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae8ef320-20d5-33c5-a528-24541c118533 | -10.46933 | -46.5743 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa3eac89-8de4-33bc-994d-9c9d1b03496c | -12.52044 | -48.28285 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b771566-5685-367d-9101-fb33c9d856fe | -11.85509 | -48.24379 | 2026-07-02 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1f9eb103-6d9b-3b51-bb7f-26295f282427 | -11.14969 | -49.53009 | 2026-07-02 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ddd77b32-0184-316a-aeb0-21dd8d1bedac | -12.51131 | -48.28131 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 920dd895-e042-3a83-9043-9061ed3ca3ad | -11.42075 | -56.0609 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bed56a52-a24e-336c-b2d8-30cd080b95bb | -7.09948 | -46.51315 | 2026-07-02 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca87eb80-58f1-3bb1-ab5f-3444afbf44af | -9.60512 | -56.92481 | 2026-07-02 04:38:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6d1d16b-6e01-3045-9e33-c453e47ce513 | -12.7631 | -44.48289 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 88db476b-a8db-3ea4-a671-196fdc297ed9 | -10.37224 | -46.6845 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 683b908d-45d6-3561-b010-d316301bf622 | -12.74498 | -44.48131 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cd83d453-d6e2-328b-b4b3-b798bf25c4de | -11.3624 | -55.42485 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37b98cde-dc87-3a1d-ac9c-2d152044c181 | -8.71259 | -48.338 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29fb0a4d-2529-3a22-afbc-5784d33ad0a3 | -12.76928 | -44.49714 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b537c1c9-87dd-3d59-83cf-fafe37de5470 | -12.75007 | -44.48902 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 113bb1a4-2773-3ee6-9526-d02f0f882fef | -8.49982 | -47.2005 | 2026-07-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a5b688b-2345-3d18-9e63-9d80089486e1 | -10.37889 | -46.68127 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c6419244-fbee-33ef-ba47-052b53f1ebe9 | -11.53902 | -47.4554 | 2026-07-02 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a8c6db3-03ef-3b53-9537-3a272e8f8c7e | -12.85884 | -44.35218 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d6950995-3210-3601-9203-49889278ca21 | -11.90082 | -55.52658 | 2026-07-02 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dde9cfa1-1e2c-33a7-a796-bb387fbd67ef | -12.77059 | -44.48752 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9fe6a6f-af77-3e05-9f19-38a3fc794c0e | -10.12761 | -52.10106 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6926fbfe-dc8c-33ac-b321-77525b483238 | -12.51466 | -48.28185 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 480f32ac-def0-3a54-bafc-0455fe844f2a | -12.52268 | -48.29058 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d067df9-719b-3573-b43e-fac9c8b6a664 | -12.76091 | -44.48361 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e1a31095-41bb-3483-9539-0e63765abd17 | -10.77842 | -53.53833 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2b504b1-e141-3b47-b6a2-482f26a9a39a | -9.1902 | -45.31635 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6d31792-31c9-3a28-8669-90c4f634734f | -12.61925 | -44.65855 | 2026-07-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b1c8cd-a115-3163-b2b7-0875787eba5a | -12.75911 | -44.48231 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 24229dd9-e302-3da3-a77d-b58201c129a0 | -11.36162 | -55.42915 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41175a4a-34c7-324c-889a-ca6ac0e94bae | -11.41739 | -56.05834 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4fdd484d-38c5-32dc-a4c8-fa2b3a94880e | -10.3751 | -46.68887 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4c4eefef-0192-3c20-901d-cb112d9ba25c | -10.37157 | -46.71187 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 497ce5a3-e21b-3e7d-838b-7710fa9312b4 | -12.76529 | -44.49657 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 76a1a7d6-7c99-32f1-9aaa-49786c047473 | -9.20061 | -58.04681 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21ab03d1-a8ae-37dd-ab87-1f14c0e28d70 | -7.95167 | -49.27378 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67a5b9b2-2b47-31cc-b48c-84c47351cd0b | -10.37832 | -46.6851 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 66b46b0b-88f9-3e99-95c6-f184959cffb5 | -10.36182 | -46.70641 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4242f30-8047-3621-a7c8-c4811a910d7a | -10.6954 | -49.60747 | 2026-07-02 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3eaa6db-c021-3387-9ab7-bfd5c0e986ff | -11.36674 | -55.42572 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac0284cb-0e37-3a4c-bb74-6a3c868287ce | -12.84626 | -44.35402 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |


[Clique aqui para ver as próximas entradas](README17.md)
