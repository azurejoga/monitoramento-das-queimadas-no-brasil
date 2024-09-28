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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 302ff61a-34cd-3894-96c9-9d8b4711eadb | -17.1136 | -56.204201 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f60f2e5-87bf-3e97-bd35-b08bd833f03a | -17.1157 | -56.214802 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85f33df0-04e9-3c19-9ec2-3e12461d5d2a | -17.1017 | -56.195599 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a188bf32-c468-3a62-9dff-d48619afa1f8 | -17.1038 | -56.2062 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a84a3ba5-a90d-3dd7-a55e-0baf96b1e16d | -17.1059 | -56.216801 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4f64131-c731-352d-a9ee-e68a35989b89 | -17.091999 | -56.197701 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c529b83-339b-3396-ae7c-09be8d719d2d | -17.094101 | -56.208302 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 30578f89-10aa-3e4c-9d31-95cb779c9173 | -17.057699 | -56.128101 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91f44915-ee15-3092-b8a8-ff294e2e5335 | -17.059799 | -56.138599 | 2024-09-28 01:06:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5448a2a-7fb3-3019-a466-0596ecfa354f | -17.0459 | -56.119801 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| da1b12a2-e61e-3804-aac7-6d7e1285f25f | -17.047899 | -56.130199 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58382a23-5388-3690-b816-dc88b302814f | -17.034 | -56.111401 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a2166b4e-4882-3dd1-a31c-cd0dc2bc2e82 | -17.0361 | -56.121799 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b07e6215-81ad-3eb4-971b-03549829b3f5 | -17.086901 | -56.377102 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd7957eb-c2be-3e0f-9063-3d3d8d5a61d6 | -17.0222 | -56.103001 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09a62e00-2945-350a-8147-beb76a658f0c | -17.0103 | -56.0947 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75a97224-3820-3d15-bca0-e0850b5aa73c | -17.0124 | -56.105099 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c68e654-9fc7-3db5-a8df-2e90e61c0f7a | -16.9984 | -56.086399 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e393dc74-72b1-3f9f-944a-3a76fa7531e1 | -17.0005 | -56.096802 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d82c306c-a783-32f8-887b-3a8e357550b2 | -17.0026 | -56.107201 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e2ec832-7c65-37be-af59-6da1ce51cb05 | -17.0109 | -56.148899 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3c9724c-b9c0-3eec-bc31-9f4e3445caba | -17.013 | -56.159401 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a044404-d712-3b75-8392-c52a342ad94d | -17.0151 | -56.169899 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18c3eb8e-c0c3-331b-902a-c1595fa34cde | -16.988701 | -56.088402 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e2c7e03-d992-37bc-ba11-035c3f74f266 | -16.990801 | -56.098801 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9eea298e-af6f-3b94-8001-4184a1e2b470 | -16.992901 | -56.1092 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bed5e017-e333-3df6-9406-a87fb9434db5 | -16.9949 | -56.119598 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35d3b8ab-34d1-3df7-8275-e57c94ff78c1 | -16.997 | -56.130001 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51082ebc-b884-3adf-b7da-a0d6cf35c5e0 | -16.9991 | -56.140499 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2cd2e7a5-d812-3743-8f39-afea4b69d1e8 | -17.0012 | -56.150902 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b30bc2f-0c73-3617-9451-593d888cef66 | -17.0033 | -56.1614 | 2024-09-28 01:06:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8fcd6805-cfa8-359c-87e8-df89c3e247dd | -16.981001 | -56.1008 | 2024-09-28 01:06:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 250351ef-0877-3ed6-b6fe-2ae15e0501f7 | -16.983101 | -56.111198 | 2024-09-28 01:06:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4164ae7-be61-3c27-ad43-4624778379c3 | -16.7397 | -55.813 | 2024-09-28 01:06:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90c0883e-eaaa-34fe-b20b-ac95552566d6 | -16.741699 | -55.823002 | 2024-09-28 01:06:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57a31f61-e631-307e-a39e-2541ca646cbd | -16.7437 | -55.832901 | 2024-09-28 01:06:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f66ae057-dc81-302e-af58-bbd4d8bf7f66 | -16.731899 | -55.825001 | 2024-09-28 01:06:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9811ea77-c799-3e41-b8b3-cf48a2d00b64 | -16.7339 | -55.834999 | 2024-09-28 01:06:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 49fa884b-1ac1-3646-b7a0-59956f9fa8ba | -16.7124 | -55.829201 | 2024-09-28 01:06:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 302a3d5a-1733-3e15-a1ed-6186458e9ccf | -13.375 | -42.032101 | 2024-09-28 01:06:56 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 588a6363-f3d7-340f-ba99-ebca335c08f6 | -13.3654 | -42.034801 | 2024-09-28 01:06:56 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b2deb865-559f-32f7-8f33-83502e02d625 | -13.3401 | -42.017601 | 2024-09-28 01:06:57 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f1909446-b575-3172-bfbd-d714a86b4696 | -13.3463 | -42.040199 | 2024-09-28 01:06:57 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 22dabcfb-a13d-356f-86f9-dd81c615a064 | -13.3305 | -42.020401 | 2024-09-28 01:06:57 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6c1c0156-847a-316c-b84b-73dcef624cf6 | -13.3367 | -42.042999 | 2024-09-28 01:06:57 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 83b37e92-7479-3daa-b80b-e284e46ebcb6 | -16.9126 | -57.9842 | 2024-09-28 01:06:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1fcfe382-07a1-3c4d-9945-643a56faa300 | -16.900299 | -57.972599 | 2024-09-28 01:06:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 364e4384-b341-31fa-acf2-2dbc5ff88038 | -16.902901 | -57.986198 | 2024-09-28 01:06:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c85e683-7705-3ece-8fd0-88184e3b62b7 | -16.4781 | -57.363602 | 2024-09-28 01:07:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c75bfeb3-fd06-3266-8a69-568ecf814ce4 | -16.480499 | -57.375801 | 2024-09-28 01:07:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aff6fbe8-0cc7-38cb-8856-90fb0cf857ef | -16.4683 | -57.365601 | 2024-09-28 01:07:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82feaf1e-4aa8-379b-a10f-30069cc4706a | -16.470699 | -57.3778 | 2024-09-28 01:07:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 456abfde-1775-3555-bee5-88a360ee2b72 | -15.0348 | -51.2215 | 2024-09-28 01:07:06 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1f6fbc8-0a34-37f9-aca6-5b9364fbaf86 | -15.4822 | -53.376202 | 2024-09-28 01:07:07 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0979f62d-099d-3c10-8f32-271c83c8439e | -15.4838 | -53.383701 | 2024-09-28 01:07:07 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f49ebbb-9bd0-3e6e-bec8-82c3791eb02f | -14.9706 | -51.4384 | 2024-09-28 01:07:08 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bba8ef0f-cde2-329e-af95-dddb670158fd | -14.8696 | -51.4473 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9afb62eb-3c84-3954-9ee0-a1ea626d522e | -14.8712 | -51.454399 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef1ac8f5-2031-3708-8923-fe549e759dca | -14.8486 | -51.400101 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0ee265-3690-3942-b852-fde1868675ec | -14.8502 | -51.4072 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc80edb2-cc07-378c-85d1-c64ce7c6174a | -14.8518 | -51.414299 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1cbf7a2-8bf8-3c67-8f52-bcbce0105078 | -14.8775 | -51.5275 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3f21090-3216-3368-bbce-4f70d917ce8a | -14.879 | -51.5345 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 799edecb-fcb4-33cb-9a94-2d9137866e39 | -14.8806 | -51.541599 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8efd0664-a53b-3319-839e-3eff29417685 | -14.8372 | -51.395302 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 804bf6e3-ed60-32d2-8a91-9887a36ed8ed | -14.8388 | -51.402401 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3a251cd-7253-3082-a263-e254e57a9512 | -14.8404 | -51.4095 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7284bcb-8437-30af-a37f-04ad0cb28bb0 | -14.842 | -51.416599 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a00e1bbb-0d10-3e41-b838-1d12fb6f91a4 | -14.8274 | -51.397598 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56b23bdf-0658-3724-8206-b15c1a61614b | -14.829 | -51.404701 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cb290ca-4771-352a-a02a-fe0fdd7a35f3 | -14.8306 | -51.4118 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7c753ce-c8a2-3855-b04b-c44835e20012 | -14.8322 | -51.4189 | 2024-09-28 01:07:10 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f2533df2-3d37-3e99-bf26-d19ccfb78955 | -15.926 | -57.191601 | 2024-09-28 01:07:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55487d5b-936b-3c08-a377-46f33d8ec6d7 | -12.9898 | -44.7201 | 2024-09-28 01:07:14 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71ece2a5-995c-376d-b2d4-cf3b0218b8b0 | -12.9937 | -44.735199 | 2024-09-28 01:07:14 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 900d7768-7652-3435-b2fd-a618590ee470 | -12.9976 | -44.750301 | 2024-09-28 01:07:14 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34675323-84ce-3120-a652-9f8fad45ebf2 | -15.8294 | -57.371201 | 2024-09-28 01:07:15 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82bdb261-d099-333d-ae08-ae639223d5df | -15.8317 | -57.383099 | 2024-09-28 01:07:15 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fca37997-780e-39c1-8df3-ca6c29f26719 | -15.8341 | -57.3951 | 2024-09-28 01:07:15 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f410fa5-4f35-3df1-b612-56115ac881d5 | -15.8365 | -57.407101 | 2024-09-28 01:07:15 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f78c86ad-52c9-311c-bdcd-745852bc3677 | -13.2679 | -46.3008 | 2024-09-28 01:07:16 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50810046-4d3a-3acf-a4ff-7b104651e263 | -13.2709 | -46.312698 | 2024-09-28 01:07:16 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 31232cd3-fb92-3b26-b80d-5b21aad77485 | -13.2738 | -46.324501 | 2024-09-28 01:07:16 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4c20a3dd-4859-33b5-8388-f57355eac332 | -13.2581 | -46.303299 | 2024-09-28 01:07:16 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8302e25f-e3f4-3f9d-ade0-201c8620102c | -13.2611 | -46.315201 | 2024-09-28 01:07:16 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 098cf5f6-f85c-3afe-8760-6dc31f6d5e99 | -13.2641 | -46.327 | 2024-09-28 01:07:16 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f522ff1-75a6-3bec-ace0-bd4052a6fd5b | -13.2484 | -46.305801 | 2024-09-28 01:07:16 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5035e39-701b-30c6-8734-aa0f45055421 | -13.2514 | -46.317699 | 2024-09-28 01:07:16 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2f0971-8b98-3890-8a23-19d4ec6cbb13 | -13.2544 | -46.329498 | 2024-09-28 01:07:16 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63a5ab36-2a4c-3e54-a7d4-b9c4578d0c04 | -15.6264 | -57.475201 | 2024-09-28 01:07:18 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d1c2485-ac07-3231-b4f8-1799f93de82f | -15.6166 | -57.4772 | 2024-09-28 01:07:18 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 572ed010-aa86-3467-a880-cb79960f8c8b | -15.6069 | -57.479301 | 2024-09-28 01:07:19 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2bf51ee-4804-3daa-94c4-62fb4e652253 | -15.5873 | -57.483299 | 2024-09-28 01:07:19 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92b829af-b875-3fe7-a8eb-b0dc1267e7eb | -15.5897 | -57.4953 | 2024-09-28 01:07:19 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8184a9-9330-30dd-b799-ae64fa3789ff | -15.5752 | -57.473202 | 2024-09-28 01:07:19 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cb6fb77-90c9-3562-bd38-e2c213155864 | -15.5776 | -57.485298 | 2024-09-28 01:07:19 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56d5aeb0-a632-3fd6-bd2b-faf812e0b54a | -14.7726 | -53.845501 | 2024-09-28 01:07:20 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15a91000-67c7-3854-b5f7-7fc31def60ae | -14.7742 | -53.8531 | 2024-09-28 01:07:20 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecea776c-f081-3a4b-a3a2-cee5cc2e97e9 | -14.7759 | -53.860699 | 2024-09-28 01:07:20 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57a34ea4-7251-3411-94c9-ed7ce9c57497 | -13.4746 | -48.5728 | 2024-09-28 01:07:21 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
