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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09f78f67-b5f6-3282-92d9-302f420994dd | -2.769 | -48.592201 | 2025-08-20 00:14:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec3740e0-205c-36be-b412-b1da58f795e9 | -5.4928 | -42.1698 | 2025-08-20 00:14:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aca6167e-7bac-385d-b41e-6609381f0ddd | -7.6528 | -45.2617 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 745f5bea-9e50-388a-82a6-9488e2561fae | -7.8136 | -46.8857 | 2025-08-20 00:14:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61e83f7f-cc2c-3211-8ba9-69a166a1e3b7 | -5.1112 | -43.160801 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d56c01d0-7f0e-3ba7-a170-bd908168fbf1 | -19.1129 | -46.607601 | 2025-08-20 00:14:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0451a2-b91e-3da7-9f00-71065d31c0ac | -4.4281 | -47.755798 | 2025-08-20 00:14:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1733f33-f5d7-3485-a6fb-7602a36f0156 | -8.7913 | -45.490501 | 2025-08-20 00:14:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dea3d4d5-065b-39e0-8a82-4ba17cd96bd2 | -5.9825 | -44.139198 | 2025-08-20 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61713b87-7697-3b8a-92be-d4b084077b04 | -5.9775 | -43.616199 | 2025-08-20 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30c60125-05f3-3e25-a2fa-e0f4e86cd9c4 | -7.1239 | -44.639198 | 2025-08-20 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9578a2bf-128f-330b-bec8-7f2e65eec06b | -12.9534 | -46.155701 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09bd1801-f64d-365b-975a-39608a7428a2 | -11.0965 | -44.817501 | 2025-08-20 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c30c0e63-5aeb-3d31-bc00-a006e70862ca | -4.6021 | -43.325001 | 2025-08-20 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aba6d21d-d380-35d9-9ec4-8d25b30c1b2f | -8.8926 | -47.336399 | 2025-08-20 00:14:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dee41dc4-b442-3b73-ad10-80c40cf1209e | -8.8013 | -45.4422 | 2025-08-20 00:14:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67288b5e-0039-3625-a8f6-edce5d7caff1 | -21.725 | -46.4967 | 2025-08-20 00:14:00 | METOP-C | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8593091-0fb5-366b-8c4e-33935e3b1b05 | -8.0278 | -47.688099 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62d4d183-40ba-3a29-b60b-23a5149b240b | -10.3155 | -46.675201 | 2025-08-20 00:14:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6420930-3049-3685-9961-e89ee6592e07 | -13.395 | -46.370499 | 2025-08-20 00:14:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 56e6b31a-68bb-3282-b1d3-853b1efe2f7d | -13.577 | -47.0186 | 2025-08-20 00:14:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f5efe5f0-22d0-3dd6-9127-40ca59a095e0 | -7.6388 | -45.291 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f558f744-64f2-3fd7-8b1f-a4f0fe8e0ae7 | -20.3281 | -51.728401 | 2025-08-20 00:14:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2ad6c568-147a-3bc5-8874-50130524f16b | -2.9079 | -48.297901 | 2025-08-20 00:14:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaaf7803-6e3d-3fb3-bc2b-3e4f94184353 | -7.5949 | -44.3988 | 2025-08-20 00:14:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f2ec4af-58f3-39d1-98c2-1aae6ce0b636 | -7.643 | -45.263901 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44d426d9-2847-3959-bf79-c76542d4ce04 | -5.7898 | -43.6063 | 2025-08-20 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e58eae39-e461-3548-acc0-ff55a37f476c | -13.0253 | -46.806099 | 2025-08-20 00:14:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fdd67c7e-7206-3212-a034-687e361ddbd9 | -7.0263 | -44.294399 | 2025-08-20 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31029003-b705-3a90-bbbc-83b898d7e75a | -7.022 | -44.597 | 2025-08-20 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b182c77a-fa6d-3016-b2b6-428d163c1c39 | -7.2339 | -44.256401 | 2025-08-20 00:14:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7637cb08-5cc1-3a12-a221-3bf57c835e1c | -4.9212 | -43.232201 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 085b2978-a052-3f7b-bd4f-8c8fc9a065b6 | -5.1154 | -43.2248 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88425028-da4e-31aa-a5df-ebf3a0718c71 | -7.2432 | -50.174 | 2025-08-20 00:14:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa3be41-069a-3f57-876c-90615dd54201 | -22.716499 | -42.142502 | 2025-08-20 00:14:00 | METOP-C | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b00dde9-39ec-3cee-b1ab-570e987cfc90 | -7.0237 | -44.604698 | 2025-08-20 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62bea5f0-aadb-3876-b0ca-48cc00db4d73 | -12.6653 | -44.9697 | 2025-08-20 00:14:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6abc0ca-02a7-3596-b1de-c35e4cbcfc57 | -5.6543 | -43.372799 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd5d269d-26ba-3fba-b6c9-b0f9a9e10c44 | -9.5224 | -42.9375 | 2025-08-20 00:14:00 | METOP-C | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db17831a-2e07-3272-982c-0be1e39f1dfc | -12.9937 | -45.217899 | 2025-08-20 00:14:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05b6f81b-e31e-3336-8cbc-664b9f476356 | -7.6253 | -45.276501 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04fece10-1ff2-3b49-a1d5-e21808063873 | -15.5519 | -42.299 | 2025-08-20 00:14:00 | METOP-C | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb659b5b-2074-3d8e-b623-584c94c3138b | -14.9447 | -47.000301 | 2025-08-20 00:14:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0af803f2-215f-35fc-922e-d62f7027f462 | -4.9129 | -43.2411 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64c20d5a-1a45-3395-af53-5fef177e7432 | -4.9098 | -43.227402 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23bbbe9e-b0c5-3761-9c2f-29b7889f7316 | -6.8595 | -43.598202 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 08836bfa-455e-3d5e-aa13-3b0d98300379 | -4.4183 | -47.7579 | 2025-08-20 00:14:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d57e49a-3877-33fa-9e7a-4decd07921fe | -4.3088 | -48.094898 | 2025-08-20 00:14:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91bf4f44-18a9-3713-a8a3-c80b9dbe9133 | -4.9145 | -43.248001 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9391eb0c-6e9d-3ca4-8cc0-e3811c92d346 | -15.5502 | -42.291401 | 2025-08-20 00:14:00 | METOP-C | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f664b3ae-fb3f-39d5-9b84-7d3a3a638fe3 | -6.5697 | -51.115299 | 2025-08-20 00:14:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec8aa325-c9d4-3251-ae40-6f8939986d11 | -20.332701 | -51.693199 | 2025-08-20 00:14:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fb5db044-6b5a-3b6f-81ea-425455dd3682 | -4.9227 | -43.238998 | 2025-08-20 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e109118c-439d-37c8-8d4f-30eabcc75187 | -6.964 | -42.876598 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 68d9398c-d2b6-35fe-bbb3-4be2bc80d074 | -9.9216 | -49.2817 | 2025-08-20 00:14:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d677fdca-4c20-383b-830f-4df7733b281c | -12.9798 | -45.2006 | 2025-08-20 00:14:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1952152-b5b3-3f3e-83f9-d38651b0ddec | -7.6332 | -45.265999 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57fff248-da04-38cd-afe0-a5d404453421 | -6.8709 | -43.6031 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a972119-8bd7-3c79-a009-c5f77d6d138f | -3.7367 | -48.930401 | 2025-08-20 00:14:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdc0216d-1fd4-3bdd-bc2e-9dbdd344c024 | -5.7933 | -43.894699 | 2025-08-20 00:14:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da53501c-6a2c-3ecb-9f47-8e0dbd9a8cbb | -13.5939 | -47.001801 | 2025-08-20 00:14:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54db2ddb-e954-3131-aff7-4bb40e92bfbf | -21.5016 | -45.460999 | 2025-08-20 00:14:00 | METOP-C | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a28d96c5-a832-36d3-86e5-c60f23483368 | -11.7419 | -48.1996 | 2025-08-20 00:14:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab6c0216-5569-30c3-8ef2-eb84274fe4d3 | -4.9191 | -42.097198 | 2025-08-20 00:14:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8e317c3-3b1d-311d-a434-15e7ffdefd50 | -7.1464 | -44.601799 | 2025-08-20 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f5994dd-6e66-3c98-8bc8-b569f4bb2fb0 | -7.7949 | -45.161201 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b38be0c4-87c1-3d8e-bcb0-29c9cbcc0bdf | -5.793 | -43.620399 | 2025-08-20 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e63ac7d-6d86-3c32-a94d-03fc44c39bc8 | -8.035 | -47.6744 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1e42df5-1387-3ae6-907f-5e1827f6a071 | -6.8544 | -43.621601 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 621f34c8-2833-3fd4-966e-33ee87ee5e09 | -7.6547 | -45.2701 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6bf0055c-2e2c-3e71-9fdb-d88af5623eb7 | -6.9558 | -42.8857 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d0ac58b-a6cd-34f7-b419-918fb1271bae | -12.6634 | -44.9604 | 2025-08-20 00:14:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49c36c76-dac9-311b-8762-a746dbe1cf44 | -5.7914 | -43.6133 | 2025-08-20 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f664f54-6666-3819-9c0f-ba814663c99a | -20.4823 | -42.258099 | 2025-08-20 00:14:00 | METOP-C | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71cea00e-8834-3ec1-acc4-2d87981fa9f2 | -5.9871 | -42.8423 | 2025-08-20 00:14:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 14b43bb2-e335-3177-9fdc-e677f3aad76e | -4.4258 | -47.745399 | 2025-08-20 00:14:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b1efbcf-1eeb-33cc-856f-61fd66a85796 | -6.6233 | -43.875801 | 2025-08-20 00:14:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0db36fee-5262-3241-b78f-0338fb58ca4c | -8.1412 | -49.515499 | 2025-08-20 00:14:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3e97af6-9ebc-3849-bca6-0dba6cd0cfd6 | -6.625 | -43.882999 | 2025-08-20 00:14:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a6702bd-0ad0-3796-aaf1-1445aef46879 | -6.8528 | -43.614498 | 2025-08-20 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cfafc6d2-6bdf-3035-893c-6cd6349a0248 | -7.6351 | -45.274399 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c11740f6-4468-3c51-b3b2-6ecc4755b287 | -7.1482 | -44.609501 | 2025-08-20 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea4e825d-17e9-39b3-9fd9-6d6e3c6d0fb2 | -8.302 | -46.3517 | 2025-08-20 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 021ce9ef-a4f2-38de-b4fc-c76ddd12a0e9 | -5.6445 | -43.375 | 2025-08-20 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7bf39e2-8568-3b1c-8df5-3de630f88e69 | -20.521999 | -44.277599 | 2025-08-20 00:14:00 | METOP-C | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6d0c459-1886-33a2-ac4b-4ba02cf4ca85 | -7.6449 | -45.272301 | 2025-08-20 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 42fad8c0-9e39-3cf4-b64b-9bb3302345b2 | -3.2262 | -46.794601 | 2025-08-20 00:14:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ff3c079-c096-34c7-a359-e69af6d50c36 | -14.1636 | -45.292301 | 2025-08-20 00:14:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9936646-29be-37bc-9f4b-278e1bdea672 | -7.5834 | -44.393299 | 2025-08-20 00:14:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27e29063-abcd-34a1-99a8-2ff3889b304e | -3.8158 | -41.5634 | 2025-08-20 00:14:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c87359e9-d836-3168-ad89-4668df379988 | -3.9837 | -42.516399 | 2025-08-20 00:14:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93097081-4123-3c9e-9a5d-a96c7981dca2 | -6.9624 | -42.869701 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f45b192-5938-3824-8ce0-3bbdd338c12b | -6.6152 | -43.885201 | 2025-08-20 00:14:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5a6aeeb-a5d4-3ff6-a735-eb815045450c | -3.236 | -46.7925 | 2025-08-20 00:14:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ad5fc1d-35e2-358c-8d51-f1f34239f2be | -6.9542 | -42.878799 | 2025-08-20 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d70780e5-be66-3e93-830e-05a74b99beb6 | -8.0325 | -47.662701 | 2025-08-20 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e802c0e-039b-3cbe-8ad7-f9d1ae8f5959 | -11.4679 | -47.307701 | 2025-08-20 00:14:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed05998c-9b5d-352c-a42a-8d72bb575e47 | -5.483 | -42.172001 | 2025-08-20 00:14:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 29a1119d-cdf5-30ec-bd60-c57a781552db | -3.238 | -46.8013 | 2025-08-20 00:14:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e487fac7-c9b7-37a3-ae7b-21ffeb1eff5d | -4.6037 | -43.331902 | 2025-08-20 00:14:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
