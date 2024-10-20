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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec072d19-e0af-395e-875e-266ebe7b3ef7 | -4.71728 | -56.14094 | 2024-10-20 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d44d45-1d66-3ac4-8e95-fd521a4562fc | -4.71699 | -56.14079 | 2024-10-20 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fb40071-2094-3edd-9a40-5dfe8f24a23f | -4.71672 | -56.14429 | 2024-10-20 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 635f6522-7d84-38d3-9a20-757f1a7336ab | -4.71641 | -56.14411 | 2024-10-20 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f5f8446-1368-3454-b8b1-317ccc2eccd7 | -4.27893 | -55.60193 | 2024-10-20 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c365575-8e9b-3b4e-b15e-6af36417f7ee | -4.27842 | -55.60486 | 2024-10-20 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420ceb3d-7cee-3137-b87b-232e52582e8a | -17.87023 | -39.79567 | 2024-10-20 04:34:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e26107f-2c05-384b-ae92-c134355cb507 | -17.86445 | -39.79508 | 2024-10-20 04:34:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ef7a26e-cba9-3ad7-b73d-7e06982c5865 | -14.23978 | -39.36907 | 2024-10-20 04:34:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f8f6601b-f400-3aa9-b370-cbe66fdfede8 | -15.07775 | -48.9458 | 2024-10-20 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4734e5e2-4e98-3fae-9453-3ebed218719e | -11.8174 | -57.36944 | 2024-10-20 04:34:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b5edc7a-0cbe-38f8-ba35-f618e17f1ff1 | -11.81675 | -57.36444 | 2024-10-20 04:34:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9609f648-a129-308f-90d7-e24ac0dd18d8 | -11.81564 | -57.37022 | 2024-10-20 04:34:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c797ea4f-fb4e-3ff4-88a6-a79a11c3c08c | -12.38874 | -57.63945 | 2024-10-20 04:34:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4544f9b9-6316-39dc-ab8f-bd0440ebee6d | -12.38819 | -57.64237 | 2024-10-20 04:34:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cdb8d7c-2a5b-3911-8138-b8d375edb8c8 | -12.3837 | -57.63843 | 2024-10-20 04:34:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad59542a-a8cb-304d-993a-e0ab651d3b49 | -14.28236 | -60.12502 | 2024-10-20 04:34:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83631f45-98fc-33f1-bb06-fbd572ee6c59 | -12.28255 | -61.53292 | 2024-10-20 04:34:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b87abc4-9be9-3cad-9583-9b8ffe326128 | -12.27608 | -61.5317 | 2024-10-20 04:34:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfbbcf38-83ae-3a66-8b70-e5087bbfd71f | -12.07561 | -47.98708 | 2024-10-20 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd4c7b6c-c691-392b-ab3c-91a754078217 | -12.07505 | -47.99069 | 2024-10-20 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c052482f-d451-3cec-85ed-b21ff7acf240 | -11.95485 | -48.06771 | 2024-10-20 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 278abb81-20a1-3e9f-9211-3530ca2e804d | -11.9543 | -48.0713 | 2024-10-20 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2ce924e-af34-3ddf-bfc9-db69a17e4b06 | -11.84275 | -48.09427 | 2024-10-20 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43e53376-5738-3923-9289-8e053d4e7a78 | -11.8394 | -48.09373 | 2024-10-20 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28881ab3-3933-3953-92ca-dbfa0a7c1a12 | -11.14614 | -54.6013 | 2024-10-20 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0994083f-e70c-31cb-afb0-86d671b2dacc | -12.40716 | -55.00831 | 2024-10-20 04:34:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c28d57a6-0ff4-38b3-9826-b8087e416b28 | -12.40293 | -55.00751 | 2024-10-20 04:34:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 932e9987-1fb2-3aa5-bad7-a2011d53c4b8 | -15.96349 | -54.95885 | 2024-10-20 04:34:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f41a35fa-6bd8-3d4b-97df-8132be324914 | -15.96129 | -54.95441 | 2024-10-20 04:34:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbd234a9-4c9c-3294-9e37-c86f76516cb1 | -15.652 | -55.98364 | 2024-10-20 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25cba31d-6a41-358a-9ff5-a4e127bce949 | -15.65018 | -55.98029 | 2024-10-20 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2102966e-acf6-38b9-be55-58eb17f65b64 | -15.56389 | -55.76477 | 2024-10-20 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76cb71d8-1f96-3975-9123-b262b37a5cd5 | -17.20667 | -57.50618 | 2024-10-20 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e97d639e-88fa-3174-98b2-b1d892034a3d | -17.01655 | -57.46581 | 2024-10-20 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 177f000a-cc12-386d-a3c5-07abd930f7d2 | -16.99882 | -57.51679 | 2024-10-20 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b35a6a31-8df1-3842-a77f-4f6645ba5172 | -16.99516 | -57.51087 | 2024-10-20 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ba155f19-1cd0-3628-8c02-d04a48486e51 | -11.81846 | -57.36366 | 2024-10-20 04:34:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 299dbffa-41ae-3fef-a02f-d21bdee81338 | -2.7773 | -49.3067 | 2024-10-20 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 49c848d2-6e0b-35e9-97a8-2893dd90f1c6 | -2.7958 | -49.3062 | 2024-10-20 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3e4cf360-99b1-370a-87cd-ee0a711d0552 | -3.0478 | -51.0226 | 2024-10-20 04:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e50ae633-855f-3d04-b6b6-832bf6c09ab5 | -4.1985 | -46.6318 | 2024-10-20 04:35:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 3735f82e-b355-3ede-9238-9c1a0d05245d | -4.8758 | -48.2145 | 2024-10-20 04:35:34 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2c68c633-a98e-3339-8c18-2646c3ea1099 | -21.67051 | -57.84156 | 2024-10-20 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 89a9a91f-742d-30f9-b8b9-09e39d6ec518 | -19.58818 | -56.53436 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d3b71e7f-bcb2-344f-87be-d275d99f2a8d | -19.58405 | -56.53349 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 188ced4c-614e-30be-b4a4-25955f78cded | -19.5583 | -56.6224 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 55068b0d-9c50-3545-8bf6-aafaf08bd5d7 | -19.55744 | -56.62371 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 26292961-1474-3b75-b83d-ea8ff7c3bc08 | -19.55492 | -56.61755 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5603b014-7d48-3a32-8bed-3103b5f22276 | -19.55415 | -56.62151 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2a8ed262-321a-3971-82a7-b02b5eaef213 | -18.29604 | -56.17207 | 2024-10-20 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 31a67d8a-d781-3812-842b-d79938190097 | -18.27763 | -56.08782 | 2024-10-20 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 17c0416a-f9c9-3c17-a19b-759f647b5a84 | -18.27426 | -56.08312 | 2024-10-20 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dd97fcd0-13b8-37c9-b838-f35ca62f511a | -18.27353 | -56.08698 | 2024-10-20 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 175dcd78-e465-3f5c-aee9-7415080c58dc | -18.18483 | -56.30116 | 2024-10-20 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 739290a7-a0fa-3a64-adfc-e3bf41a93d18 | -19.55404 | -56.61885 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 748a6b80-6300-3906-a901-071af04033df | -19.5533 | -56.62282 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2f5bf336-c6df-3660-a251-c7a4c5afa185 | -19.55077 | -56.61666 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b132d563-b248-38dd-8feb-ae9204b4f387 | -19.55001 | -56.62063 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| abb33091-ec28-32a8-8d42-a1a922c13cc9 | -19.54989 | -56.61796 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 955d8efa-6ec5-3f33-bbff-a02190f856a3 | -19.54915 | -56.62193 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8e7ee251-a3f3-36f5-bc59-2cabe7a78c14 | -19.54846 | -56.62857 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fa355f00-2bc9-3dc3-a600-d9137ec2dd07 | -19.54841 | -56.6259 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 75f21835-149d-39e4-8265-25d106afd50c | -19.54769 | -56.63254 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 26d300c1-4c9b-3678-86c4-9adcb4acfb52 | -19.54766 | -56.62988 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 03c4f64e-02e3-370b-b0c5-823dd578e60c | -19.54692 | -56.63387 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fb6f6f9b-6838-3c9e-a804-b648cb693b62 | -19.54617 | -56.63786 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| efa6c1aa-3b4f-3758-b784-cb9c07ed2859 | -19.54615 | -56.64049 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2e1bc802-68c3-34a2-b90e-94d06ed91e32 | -19.54543 | -56.64184 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c8827df9-6181-33de-87b3-25ac28c68e1a | -19.545 | -56.62104 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 138dd6e1-d36e-3daa-a1bd-f9431bcbe31b | -19.54426 | -56.62502 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ca6d6352-179c-3757-8cf2-80aa5c5563f6 | -19.54351 | -56.62899 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6af2d50a-249f-3bf0-998d-862fdc2cdcc1 | -19.54277 | -56.63298 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 089044e9-7846-3513-8e68-4563c5c88dcb | -19.54202 | -56.63697 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d89a95fa-3f0b-378a-a83b-752225120ea6 | -19.54127 | -56.64095 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 898311fc-542a-3377-b181-2d1490f9138e | -19.54085 | -56.62015 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0d28d72f-c6e0-391c-a09d-b6003adca7e5 | -19.54011 | -56.62413 | 2024-10-20 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7ded7907-b56d-3947-95d6-d8529b5fc231 | -30.52181 | -52.74201 | 2024-10-20 04:38:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 862a42c5-d902-3b24-beeb-87b4582e7cf6 | -30.15122 | -52.02433 | 2024-10-20 04:38:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| ce145639-2f53-3429-aff3-7aeeef3825a8 | -29.95223 | -51.61518 | 2024-10-20 04:38:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 8723c466-368c-3fc0-9667-880d218e3905 | -29.86724 | -51.16496 | 2024-10-20 04:38:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 37723f0a-4916-316c-bb7d-0892c722ecc2 | -29.86378 | -51.16434 | 2024-10-20 04:38:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 698d57ec-04b4-3bf3-b7b0-7a9627538aab | -29.81576 | -51.17764 | 2024-10-20 04:38:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 45fe0590-7490-34e3-8f33-52fda509f041 | -29.6813 | -51.19397 | 2024-10-20 04:38:00 | NPP-375D | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 0a94800e-0899-31a0-844f-807921d3e4d6 | -29.67954 | -51.19543 | 2024-10-20 04:38:00 | NPP-375D | ESTÂNCIA VELHA | RIO GRANDE DO SUL | Brasil | 4307609 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| be7b2f46-e86d-3188-965b-104e95c69bb0 | -29.42181 | -53.99704 | 2024-10-20 04:38:00 | NPP-375D | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 1e78095e-e319-3df3-895b-4930fd675b60 | -1.165 | -53.6571 | 2024-10-20 04:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| cf235df5-0341-3cdd-8cd0-95c47119468b | -2.2994 | -48.5722 | 2024-10-20 04:45:17 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6a884f79-2d19-38ba-8218-07c5c823a359 | -2.7773 | -49.3067 | 2024-10-20 04:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ac30e433-1925-3910-b838-d34b07d65171 | -2.7958 | -49.3062 | 2024-10-20 04:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 73c822a7-6df1-3fdd-a74c-64fe09d05222 | -4.1985 | -46.6318 | 2024-10-20 04:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ee10c9d4-c6c7-3eb9-9967-f2754fd4f0bc | -7.3638 | -72.8628 | 2024-10-20 04:45:46 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 105608a3-fdac-35f5-84d5-af39c7ed7a84 | -1.95154 | -45.58844 | 2024-10-20 04:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6de943cc-47f6-31c9-9fa8-e0e327c96c9d | -2.17358 | -46.85568 | 2024-10-20 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 807e71d2-0177-3bdc-9ef5-8ae636db311e | -1.97526 | -48.6862 | 2024-10-20 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5b4ae0a-984d-3c65-8935-f3eb3ce63f6c | -1.50427 | -47.21641 | 2024-10-20 04:53:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c09de14e-f251-39c7-8fab-924502840dc7 | -1.41213 | -48.38388 | 2024-10-20 04:53:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d81a150-966d-3ffc-ac7b-19072443c6ee | -1.12395 | -47.26628 | 2024-10-20 04:53:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80c95878-afe4-3a0d-b8b9-9e06f7c94ffe | -1.12033 | -47.26171 | 2024-10-20 04:53:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2172bbcd-93e4-3367-b475-7c6d429c4301 | -1.11972 | -47.26564 | 2024-10-20 04:53:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README41.md)
