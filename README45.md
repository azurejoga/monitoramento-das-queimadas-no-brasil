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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0bd3422-a474-35f3-bd54-c18133c527ac | -10.7214 | -51.0657 | 2024-09-27 02:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ac0a5b32-cbc3-330f-ae56-7fce4cc95633 | -10.7211 | -51.0869 | 2024-09-27 02:56:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 80e88d2d-e88a-36a2-8614-95eeae6ee98c | -10.9456 | -54.2471 | 2024-09-27 02:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3934345e-41e7-39cb-ae21-85b0933a45a2 | -10.9453 | -54.2676 | 2024-09-27 02:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 60ae34cd-384c-3e04-814e-71f1f607035c | -10.9267 | -54.2488 | 2024-09-27 02:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 2aee622e-11dc-3f15-86f7-d44402ad877b | -10.9264 | -54.2692 | 2024-09-27 02:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| afc843dc-2964-3779-bc7f-565184fdbad5 | -11.2223 | -54.7735 | 2024-09-27 02:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 50870a60-5673-3da9-94e1-1e5e85587235 | -11.2034 | -54.7752 | 2024-09-27 02:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 1dc0de39-20b0-3909-a50c-01fb9979757a | -11.2538 | -47.0918 | 2024-09-27 02:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a58f2ecd-7f27-3080-93a6-a8fc692cb41a | -11.2534 | -47.1142 | 2024-09-27 02:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 561.2 |
| cbffe4bf-d49d-30cf-8dc9-734b7a4b65fb | -11.2531 | -47.1366 | 2024-09-27 02:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 665dc679-9aa1-3329-a073-b45b7ac6cea6 | -11.2412 | -54.7719 | 2024-09-27 02:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| edb00af7-e9ec-3f4f-8bb7-51ba68d007c0 | -11.2343 | -47.1166 | 2024-09-27 02:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 01d2abe0-9584-3de3-8e77-a2010afb2378 | -11.234 | -47.139 | 2024-09-27 02:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3737619a-5698-3540-9661-ebebc46bb6b3 | -12.1668 | -50.8218 | 2024-09-27 02:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 394.7 |
| 35f06725-ab8a-3ce8-b3ec-4da777f5a650 | -12.1672 | -50.8004 | 2024-09-27 02:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 225.5 |
| ff61d842-dbeb-3ce3-8b8f-25028c95dc8f | -12.1856 | -50.8409 | 2024-09-27 02:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 08b63363-49e9-3bb0-88d2-b83e5eb5fe3e | -12.1859 | -50.8195 | 2024-09-27 02:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 168.4 |
| dd4c359d-4b40-3dcd-9096-590199a34a9b | -12.1863 | -50.7981 | 2024-09-27 02:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 29ef0b86-8f36-3f63-97a5-94a34c1e6bf7 | -12.6824 | -54.6968 | 2024-09-27 02:56:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c4bb1935-7277-3d39-8d6c-55bc58d524d0 | -12.844 | -54.0215 | 2024-09-27 02:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 229a4412-4c45-3f13-9a90-b89f3332ee3f | -12.8628 | -54.0402 | 2024-09-27 02:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 538c804b-fede-3266-8ef3-b8498fee25b3 | -12.8631 | -54.0195 | 2024-09-27 02:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 12bc74a8-9d6b-3a9f-bac3-ac104f723090 | -12.8634 | -53.9988 | 2024-09-27 02:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b0b6a258-31b9-3ca2-8f2d-a0ad1c30968e | -16.7325 | -55.8445 | 2024-09-27 02:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 8b05c7d9-4fe7-3f8f-b408-b5fe6ce04d37 | -16.893 | -58.0417 | 2024-09-27 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| b3abfdff-117c-36ef-b241-fa44314a0f4b | -16.8933 | -58.0213 | 2024-09-27 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 7590ab2c-a2f5-3e34-9051-7f57a8b1667f | -19.3977 | -42.5753 | 2024-09-27 02:56:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| b4da9d0d-acd5-30b6-a3dd-aff948d85d2a | -19.6342 | -42.8103 | 2024-09-27 02:56:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| e8b0debf-7f24-3c15-adf7-90dcd41fdc59 | -19.6136 | -42.8159 | 2024-09-27 02:56:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| 53111acf-149c-34f7-be00-47cca95e15a0 | -20.1828 | -43.5049 | 2024-09-27 02:56:57 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 147.1 |
| 378c1cdc-ff09-3f8a-aa26-3ef1fa02eab7 | -20.182 | -43.5299 | 2024-09-27 02:56:57 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.0 |
| 79f366cb-6b63-3bcc-96e5-7d3d728b1880 | -21.0865 | -48.8381 | 2024-09-27 02:57:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 75c582bf-9876-362b-b39e-436c4aea71aa | -22.7433 | -44.8035 | 2024-09-27 02:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| 18ce4984-014e-3c08-944b-85f63b2d4820 | -22.7442 | -44.7785 | 2024-09-27 02:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.8 |
| d2d0a168-4e58-3ea1-a2ad-9beafb6700ba | -22.7645 | -44.7973 | 2024-09-27 02:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| ffa1e1b4-45e9-3fc6-bcfc-2279fd502272 | -6.73715 | -35.11681 | 2024-09-27 02:58:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 2940c45b-adea-361d-a66f-871340a7ecb5 | -18.1729 | -39.82306 | 2024-09-27 03:02:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 3ee90cd4-ce1f-3add-83d5-14f596145826 | -18.17238 | -39.82725 | 2024-09-27 03:02:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e9179d27-c2e0-3347-932b-19c5f18fb89f | -17.06893 | -41.14593 | 2024-09-27 03:02:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 32fc9a49-fae1-3761-8e07-9532425763bd | -17.06738 | -41.15256 | 2024-09-27 03:02:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 675b13c6-4bf6-3827-9989-6f2552750db8 | -17.06558 | -41.14456 | 2024-09-27 03:02:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3a142f67-cec2-3809-9662-e2fff7602866 | -17.06404 | -41.15098 | 2024-09-27 03:02:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 08138b9e-0a3e-3085-a1ab-1d0a59395533 | -16.76124 | -39.32138 | 2024-09-27 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2287d27e-68ce-3295-bdcb-1aa73b325583 | -16.76108 | -39.32239 | 2024-09-27 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7348cfef-eb41-3589-bbd1-c210c76920d6 | -21.74261 | -41.37175 | 2024-09-27 03:02:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d492cfa2-3313-34f6-ad58-bf8fd90561ed | -20.98007 | -42.40599 | 2024-09-27 03:02:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a707b835-4c6c-3a08-9f8e-f6350672ae33 | -20.77312 | -41.85133 | 2024-09-27 03:02:00 | NOAA-21 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6d8a0993-569f-33ee-965d-00ebd80472ea | -20.77135 | -41.85846 | 2024-09-27 03:02:00 | NOAA-21 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 632abcd6-7e84-323d-abca-24d344741b95 | -20.61366 | -41.24068 | 2024-09-27 03:02:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fad46324-cac4-38e5-a9f9-a8ec26c16b2c | -20.59664 | -41.24063 | 2024-09-27 03:02:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| b088370f-51cf-3bfc-9c18-5cd9ad808579 | -20.59517 | -41.24667 | 2024-09-27 03:02:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 300bf15e-84f2-3a16-8514-3f370c8d31e2 | -20.59224 | -41.22971 | 2024-09-27 03:02:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 7aa403f9-d380-3eb2-86c6-45cf64b5dd17 | -20.59098 | -41.23487 | 2024-09-27 03:02:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 52fa865f-903e-3b71-ba0c-57c0e92166db | -20.51859 | -41.97025 | 2024-09-27 03:02:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 05dba1fc-158a-3fac-84f4-78aaff06e9c1 | -20.46602 | -42.15118 | 2024-09-27 03:02:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 21bb0268-5528-316b-8228-dffc73cdf663 | -20.46371 | -42.16042 | 2024-09-27 03:02:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b605bb6b-d0d7-38a7-898e-a424ee3cabff | -20.436 | -42.01391 | 2024-09-27 03:02:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 09751fee-adc9-3205-b8be-ab75476096ca | -20.4338 | -42.01413 | 2024-09-27 03:02:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a64678d4-457f-3c12-a1b1-51e75a54aa21 | -20.42897 | -42.01245 | 2024-09-27 03:02:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8411d723-1d2e-32b0-831b-2b4b856b95bd | -20.42847 | -42.00597 | 2024-09-27 03:02:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cec9fd9e-59e0-34c8-94b4-cdf7792d7a6b | -20.42654 | -42.01358 | 2024-09-27 03:02:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3c3129cf-cec0-396a-a213-5075fc9081c5 | -20.41052 | -41.87917 | 2024-09-27 03:02:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 955fe2d3-c584-33f9-94a3-7b3f81a742d1 | -20.40778 | -41.89019 | 2024-09-27 03:02:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 1c4694ac-560a-3d2d-ad24-190e6b801a45 | -20.30696 | -41.14645 | 2024-09-27 03:02:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 93e83782-c651-3503-920b-308d5ef2d7f7 | -20.30553 | -41.15238 | 2024-09-27 03:02:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c4ae5000-e451-3b1f-af2f-ce9fd916ceb6 | -20.27889 | -41.32902 | 2024-09-27 03:02:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ca9f500a-1c2f-356c-90db-566fd2465abc | -20.27725 | -41.32822 | 2024-09-27 03:02:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b8b53d99-2724-3359-819f-5b83bc6ca4a6 | -20.27212 | -41.3275 | 2024-09-27 03:02:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 12e8f115-e8aa-3960-82a7-fba593dff19e | -19.86941 | -42.17051 | 2024-09-27 03:02:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9824ebd9-0f8c-3022-b1d1-3964624de92e | -19.86591 | -42.16776 | 2024-09-27 03:02:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e378026a-0cdb-3194-a4fc-30705e88e8be | -19.16192 | -41.38934 | 2024-09-27 03:02:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 8960a607-feac-3cde-b21a-7653e7bb94fd | -19.16187 | -41.38595 | 2024-09-27 03:02:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f93c33e0-e2bb-31fc-9d80-fca6d7fc07ed | -19.16022 | -41.39263 | 2024-09-27 03:02:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ab0784a5-3a22-3069-90a8-8b69e68cc097 | -19.1567 | -41.3807 | 2024-09-27 03:02:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 6d2d4acd-6dc1-3cea-a21e-7d195ac6f27d | -19.15511 | -41.38732 | 2024-09-27 03:02:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| cf144d60-2b57-3f57-80fa-f2c6462871ab | -19.15346 | -41.39412 | 2024-09-27 03:02:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 63fe6be6-8e59-34fd-8217-48a62d92b8ea | -19.14991 | -41.3786 | 2024-09-27 03:02:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b0968101-e70a-3627-9c3b-de85d6cd81c2 | -18.17367 | -39.82153 | 2024-09-27 03:02:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 9117ca38-f41a-33bb-bf48-7c63001bc0b2 | -22.67628 | -42.85625 | 2024-09-27 03:04:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| e19c8273-409a-321a-9d4e-f858bd2b7b0c | -22.67441 | -42.86343 | 2024-09-27 03:04:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| e12a38b7-484d-3e00-acae-00124ea89223 | -12.19 | -50.81 | 2024-09-27 03:04:15 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0028a878-e6a7-328e-a2cb-3f03d2e875d8 | -12.15 | -50.8 | 2024-09-27 03:04:15 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23c07bb2-1b74-3d49-9c0a-9b5f644abbf9 | -11.25 | -47.14 | 2024-09-27 03:04:21 | MSG-03 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1e0070d-04dd-307b-9955-0fdb36c15599 | -11.25 | -47.09 | 2024-09-27 03:04:21 | MSG-03 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98b179bf-3bd2-3fd0-8489-f2c428bab2d8 | -9.6 | -50.13 | 2024-09-27 03:04:31 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3a9d3a2-81c5-3fe1-a3b5-eafde4ffbc6c | -2.358 | -47.5989 | 2024-09-27 03:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| a4966767-d980-3031-8bf8-da732e1a824b | -2.3579 | -47.6206 | 2024-09-27 03:05:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 71b41839-3139-3dde-a6d8-95b51afcf7a7 | -2.8611 | -51.6699 | 2024-09-27 03:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 320bde6e-2584-3152-80eb-de02303e80a2 | -3.0107 | -51.0652 | 2024-09-27 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 27e6a5f2-5b36-38a4-9fad-e3cb964cd598 | -2.9339 | -57.8562 | 2024-09-27 03:05:23 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| f5d5410e-3e7a-364d-84f3-c0dd70209742 | -2.9156 | -57.8565 | 2024-09-27 03:05:23 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 62d1ebf8-378c-3a44-8845-3f5cfe3f1232 | -2.8795 | -51.6695 | 2024-09-27 03:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4bbfce62-27f2-3ce9-be26-2298efb265d1 | -3.2321 | -46.7836 | 2024-09-27 03:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 85a10ce5-6c27-3043-8454-32b173dadf2c | -3.2136 | -46.7843 | 2024-09-27 03:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 5be438d0-d7b3-3ea3-adec-e4c4e85b4f56 | -6.253 | -62.4671 | 2024-09-27 03:05:42 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 626506e8-2a75-34ab-867a-e828c96afd73 | -6.8199 | -63.1651 | 2024-09-27 03:05:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| cf56dc69-c615-32a9-a95b-0e21b2b16edc | -7.8156 | -54.7252 | 2024-09-27 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 629a0cf1-7df7-398e-93ae-7571866dc84e | -8.1579 | -61.2809 | 2024-09-27 03:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d599e102-e687-3af5-bbe8-9cdc1fc7c598 | -8.1394 | -61.2817 | 2024-09-27 03:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |


[Clique aqui para ver as próximas entradas](README46.md)
