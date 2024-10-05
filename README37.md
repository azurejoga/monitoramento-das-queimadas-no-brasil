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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a19d6e9d-f9f4-314b-967c-eec7e49f4dfe | -13.1245 | -46.352 | 2024-10-05 03:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5f0ec3d3-7e62-3c17-ac98-c52f9cc8a550 | -13.3978 | -61.9376 | 2024-10-05 03:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 267.3 |
| 20d4c3b0-b35d-3116-a3d5-dea172073aa9 | -13.3976 | -61.957 | 2024-10-05 03:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 500.3 |
| 46bf4230-7fb3-36da-b75b-f0e377060e92 | -13.3786 | -61.9582 | 2024-10-05 03:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 84.7 |
| b0ff14b8-5143-3316-a282-34ecee35b302 | -13.6328 | -51.2604 | 2024-10-05 03:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2ac7ff4d-7d78-38f7-93cd-b7dec69eba94 | -15.5791 | -57.4532 | 2024-10-05 03:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0c2e9020-bde0-30a9-bc24-78833e66822b | -15.5597 | -57.4553 | 2024-10-05 03:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b010d1c1-bcac-3212-9707-a2bb83c8458d | -16.5745 | -57.16 | 2024-10-05 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 2a08c39f-5c2a-328f-b1c1-9184847bd461 | -16.5544 | -57.2032 | 2024-10-05 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 188ad7a9-8ea6-33ff-823c-c5c21bdcc156 | -16.554 | -57.2237 | 2024-10-05 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.7 |
| 1f5c5d33-a576-3ecb-b4a8-48a9b6a23b77 | -16.5742 | -57.1805 | 2024-10-05 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| b42552b7-cfe4-3c07-9668-a8bddbf9bad1 | -16.6871 | -57.4536 | 2024-10-05 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 1128d702-6b5e-3275-a219-c7fef0e0f11f | -16.7644 | -57.5061 | 2024-10-05 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 2a1116c1-b0c6-3ae0-95f8-fd41a9a47496 | -16.7647 | -57.4856 | 2024-10-05 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.3 |
| 4446b5d9-ca67-3061-bc05-b50459d660ba | -16.765 | -57.4652 | 2024-10-05 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 06004c5f-4a22-3fc8-b6e2-11c6c931c39d | -16.7843 | -57.4834 | 2024-10-05 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| d8e783c9-8c5c-3fa2-bf3e-853e7921f69e | -17.1085 | -56.7892 | 2024-10-05 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| ba4ca827-d420-3242-b09c-fcc470b49d9a | -17.1178 | -57.4244 | 2024-10-05 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 128004bb-b48f-33a2-91c1-3d9dc87e2910 | -17.1182 | -57.4039 | 2024-10-05 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 35cac032-4af9-323d-ab81-521aab99e185 | -17.1185 | -57.3834 | 2024-10-05 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| fa246b47-640c-3d34-8a35-5ffa40d33e94 | -17.1375 | -57.4221 | 2024-10-05 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 36a5e8f7-57e8-3cde-a580-35f6195102bd | -17.1378 | -57.4016 | 2024-10-05 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 169.6 |
| b435955c-e4b4-3cb5-a366-b62c0d54f741 | -18.5062 | -52.8193 | 2024-10-05 03:16:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| cc71081b-6fd3-3a36-ac05-e682850cfc68 | -18.5058 | -52.841 | 2024-10-05 03:16:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 291.5 |
| 38d47eb5-21f0-3e4d-8a67-1c282a7b0fdc | -18.5053 | -52.8626 | 2024-10-05 03:16:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 841a3f15-4f46-33fc-947a-37c5610c5ea8 | -18.4862 | -52.8226 | 2024-10-05 03:16:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 67af952a-628e-361d-a870-72920f0ef580 | -18.4858 | -52.8442 | 2024-10-05 03:16:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 94104b9f-42f9-3226-ac0b-ebe80970cb7a | -18.4853 | -52.8659 | 2024-10-05 03:16:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| aa248224-bdae-3097-b3f4-3340b34a5350 | -18.8816 | -43.5785 | 2024-10-05 03:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 2d66dd13-de73-32d7-9b90-1dcaa924b11c | -18.8809 | -43.6032 | 2024-10-05 03:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.7 |
| 9660130f-0cb5-3c4d-b4fa-150064b281b6 | -18.6981 | -57.2915 | 2024-10-05 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 840ced38-501f-3e17-bc1a-e4e110b42a01 | -18.6785 | -57.2734 | 2024-10-05 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.0 |
| 07082844-63d5-324c-b671-6b4890acc84f | -18.6782 | -57.2941 | 2024-10-05 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 41fffc15-561c-3ee8-8b8c-b408285bf42d | -18.6586 | -57.2759 | 2024-10-05 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 2422491f-f1f8-334e-83fe-92ce246b012e | -20.9385 | -49.0098 | 2024-10-05 03:17:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| 88118ed5-d4ce-3a8c-8cf1-d3b86fd5180e | -2.9014 | -50.7142 | 2024-10-05 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 89ae071c-9be7-3cfd-b5ca-659df8a87069 | -4.0794 | -47.9502 | 2024-10-05 03:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 77d361df-8b49-38f2-9698-195656b4335a | -5.8214 | -44.1426 | 2024-10-05 03:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1a9f0ae7-186a-30f9-9dfd-b0f12b222cf6 | -5.8216 | -44.1196 | 2024-10-05 03:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| c40b1c0d-104d-3dfa-99f0-a0f74f5ad008 | -6.9514 | -59.0666 | 2024-10-05 03:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| eb70e0ea-445e-32c8-9126-885a12f68c34 | -7.5193 | -63.2558 | 2024-10-05 03:25:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fc51bfd9-81af-3242-a93c-09d277ac5b44 | -8.7652 | -44.8335 | 2024-10-05 03:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 212.2 |
| e43822a7-d8ea-3927-93e1-bb27e0940ba2 | -8.7655 | -44.8106 | 2024-10-05 03:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 291.1 |
| f4ae907f-4be5-3342-b568-346e977492ea | -8.7841 | -44.8315 | 2024-10-05 03:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 285c4174-0596-33c7-bfbe-a9ba8de9da1b | -8.7844 | -44.8085 | 2024-10-05 03:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| b852e50c-b890-3533-805e-8cdf8c553b19 | -8.7772 | -49.955 | 2024-10-05 03:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 84f41a15-e13d-3b86-bf1c-06f2e30ffbe4 | -8.7957 | -49.9747 | 2024-10-05 03:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ba59c823-acd9-3896-ac77-670a4105b6a4 | -8.7959 | -49.9533 | 2024-10-05 03:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0b80ace2-5bae-3bde-8da3-aacc6f683a2d | -8.9851 | -49.8297 | 2024-10-05 03:25:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 96fda6a2-3c33-37f3-ad1e-c25197753b06 | -8.9853 | -49.8083 | 2024-10-05 03:25:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 15b78183-719d-3c92-9d4d-8fc5f5daab64 | -9.1759 | -61.5794 | 2024-10-05 03:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5712ec05-1219-3e38-85e0-31cf7624db31 | -9.9505 | -44.0908 | 2024-10-05 03:26:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 3f76206e-40a0-326e-9d96-c69b6cf3564d | -10.2569 | -36.3362 | 2024-10-05 03:26:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| cf5ab071-9a14-366a-b7d4-149e991bedcc | -10.2762 | -36.3327 | 2024-10-05 03:26:03 | GOES-16 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| a874bee4-0bcf-3e3f-93ee-7455baf81fd3 | -10.294 | -50.536 | 2024-10-05 03:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6ddb4d70-6a2e-333b-877a-0d18048bfc92 | -10.2942 | -50.5147 | 2024-10-05 03:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 88bf9d54-239b-35ba-9683-52a8dcafc304 | -10.3129 | -50.5341 | 2024-10-05 03:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 4245ca0d-71d3-3593-90ea-5e4cb2e82fe5 | -10.3131 | -50.5128 | 2024-10-05 03:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 38af119c-811b-3d9c-9ce2-eeb892e5b9db | -11.1155 | -54.2319 | 2024-10-05 03:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f7ddc278-29ba-39f9-927e-0052d96933f9 | -12.7819 | -50.5543 | 2024-10-05 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 78fab3d8-8f48-311b-9241-728d2c8961f3 | -12.7822 | -50.5328 | 2024-10-05 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d8661dc4-b7d2-37e8-b6eb-ed3df3b44b36 | -12.8007 | -50.5734 | 2024-10-05 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 0c74900a-bf51-3fa7-96a6-cb1d4430b492 | -12.801 | -50.5519 | 2024-10-05 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 24652c8d-18a1-3189-9e7d-5cfc8f0ca96d | -12.8198 | -50.571 | 2024-10-05 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 87ed7613-e24a-3421-bc57-71c41a440096 | -12.8202 | -50.5495 | 2024-10-05 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 227.3 |
| d7bbbf16-65ee-3220-9ef6-606c8b83b8dc | -13.1047 | -46.3778 | 2024-10-05 03:26:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b898d02b-90c8-3b4c-b25b-06d16f970e82 | -13.1052 | -46.355 | 2024-10-05 03:26:19 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 166.4 |
| fe378469-2eab-3b29-8c87-36554f7c343d | -13.1245 | -46.352 | 2024-10-05 03:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ece3edcd-4bd6-3597-a5e8-9b011e8fa38d | -15.5791 | -57.4532 | 2024-10-05 03:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d9d0839e-4365-3d6d-8f4f-03cb4997d6d8 | -16.5345 | -57.2259 | 2024-10-05 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 0b697658-4385-37d3-9773-c1d5cc95d4e4 | -16.554 | -57.2237 | 2024-10-05 03:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.5 |
| bf320028-aeb2-3c26-85a0-5c317de2bc59 | -16.5544 | -57.2032 | 2024-10-05 03:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 429396d2-17bc-3994-8acc-7d8c066385b6 | -16.5742 | -57.1805 | 2024-10-05 03:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 76ba70d0-178a-3ad0-9983-68f28b205eff | -16.6598 | -55.5219 | 2024-10-05 03:26:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 679b5949-c8e4-38b4-8e2f-f1c81badde9f | -16.6871 | -57.4536 | 2024-10-05 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 40786202-d7de-36c4-9e76-7e3d8fd125ae | -16.7452 | -57.4878 | 2024-10-05 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 6ea7052e-7815-34ce-a359-318e876878c5 | -16.7644 | -57.5061 | 2024-10-05 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| fa23ffb2-5de6-3792-96ce-9efc76b1473f | -16.7647 | -57.4856 | 2024-10-05 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.3 |
| c5e6f0c5-5c14-3745-88fe-73a75acd3f94 | -16.7843 | -57.4834 | 2024-10-05 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| f49e4800-fed8-332f-80dd-e3a6cda3cb0e | -17.0888 | -56.7915 | 2024-10-05 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 06f6a228-abcc-378f-b46d-338362c86cb7 | -17.0892 | -56.7709 | 2024-10-05 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| bdb52344-220e-32dc-8ebd-758b1964272c | -17.1178 | -57.4244 | 2024-10-05 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 6e51305c-bc3e-3be7-a05f-b5209a91777e | -17.1182 | -57.4039 | 2024-10-05 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 144.0 |
| d7bd1472-f753-3f94-be09-4d6c0cda73fe | -17.1375 | -57.4221 | 2024-10-05 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.7 |
| bd611ea7-51ef-34cb-802f-e6a0eea33043 | -17.1378 | -57.4016 | 2024-10-05 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.4 |
| 1ccbb997-e3ec-3099-b5d0-795f3512c67d | -17.1381 | -57.381 | 2024-10-05 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 81946efb-4b62-3f6f-bf15-11e433886acd | -17.1574 | -57.3993 | 2024-10-05 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 827d13e1-7d78-3db2-8aa2-aaa3872256ca | -17.6911 | -43.7978 | 2024-10-05 03:26:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 65c74a68-bf35-316b-9ccd-a67db75aee37 | -17.7112 | -43.793 | 2024-10-05 03:26:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 259.3 |
| 97bc6a40-90e7-35a6-a5c9-29f988e6a345 | -17.7119 | -43.7686 | 2024-10-05 03:26:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8f95cc59-592b-3ec6-9b2a-71f3fddc1bd8 | -18.4858 | -52.8442 | 2024-10-05 03:26:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 2c2b4b1a-3bb9-33c2-8a32-e8598f867146 | -18.5053 | -52.8626 | 2024-10-05 03:26:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| feda9adf-e802-3971-a6f3-33ac719319c7 | -18.5058 | -52.841 | 2024-10-05 03:26:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 386.8 |
| a66b009a-3dfd-30d3-91e5-27b17956e287 | -18.8606 | -43.6084 | 2024-10-05 03:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.5 |
| deb872bc-ee43-3ff9-a9b2-7caad1fb493e | -18.8809 | -43.6032 | 2024-10-05 03:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.7 |
| 96705143-7712-3011-9192-18750fd81441 | -18.8816 | -43.5785 | 2024-10-05 03:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| 096bca9f-8dc3-3c58-b1a7-3ea00b42fa4f | -18.6582 | -57.2967 | 2024-10-05 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.9 |
| ef561fb8-bf96-3cda-bb2a-f8df0b9b7dcc | -18.6586 | -57.2759 | 2024-10-05 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 29f71185-d63d-3bb1-9a19-31f44371ef2a | -18.6782 | -57.2941 | 2024-10-05 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| b830807e-5475-30d3-b9d6-e24df69687c4 | -18.6785 | -57.2734 | 2024-10-05 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.0 |


[Clique aqui para ver as próximas entradas](README38.md)
