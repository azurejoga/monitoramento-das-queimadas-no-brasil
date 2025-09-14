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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc9093d4-a609-33cb-912d-a9db96d47374 | -12.9294 | -54.7333 | 2025-09-14 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| cf59e84e-b2d8-3f1b-af0a-e1e527926304 | -11.2924 | -50.8356 | 2025-09-14 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9326fb5c-c253-3a84-99f1-11680b488a1e | -11.3117 | -50.8122 | 2025-09-14 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c7e0a968-1197-335e-9f5f-78ba9f3e943a | -22.7275 | -49.9098 | 2025-09-14 02:40:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5f67c601-23c5-3f97-9b17-15d6af9f2450 | -3.5995 | -47.5142 | 2025-09-14 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 274bd680-2798-3b38-bf9d-a55dbbf69e7f | -12.7863 | -48.0209 | 2025-09-14 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5359421f-ab58-3829-9f08-57fc202277a9 | -10.769 | -46.4583 | 2025-09-14 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 45b4b237-a926-34c5-a39e-1f32215a8442 | -3.581 | -47.5149 | 2025-09-14 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 06138c33-47f0-33d5-ae8b-eb65a9baa268 | -13.9278 | -44.8576 | 2025-09-14 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5ba9c83a-0c43-3adc-a7af-3230fe159c05 | -11.3114 | -50.8335 | 2025-09-14 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c754c445-38a5-332e-9b07-54fbf09b4756 | -13.9283 | -44.8341 | 2025-09-14 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 511a09b6-b935-37bd-84e0-3f82a412de9b | -10.7687 | -46.4808 | 2025-09-14 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f56eacb4-edfe-326c-a185-ad9cc3b2cdf9 | -11.2924 | -50.8356 | 2025-09-14 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e5043465-f6de-3bb1-b545-2705512b5b81 | -12.7675 | -48.0013 | 2025-09-14 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| acf8f7bc-8a63-3b79-b604-2161aa1db941 | -22.7282 | -49.8866 | 2025-09-14 02:40:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5c707842-ed96-39ac-b4dc-b39451749183 | -12.9294 | -54.7333 | 2025-09-14 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 45cfd85f-07f8-3ae9-af33-31739541ce5c | -11.2927 | -50.8143 | 2025-09-14 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 0662048e-fecb-33a3-875e-3e0d0837b6d5 | -3.5994 | -47.5359 | 2025-09-14 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 690ac2df-33f2-318b-a93c-f71e05f397d1 | -3.5995 | -47.5142 | 2025-09-14 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| aceb6468-5c3e-3992-951e-4274552acc13 | -22.7492 | -49.8817 | 2025-09-14 02:50:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9bcab712-410b-369d-8fef-bc80eae52dff | -11.4569 | -48.7026 | 2025-09-14 02:50:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 60c51747-54a7-3851-aba8-8a020b467904 | -11.3117 | -50.8122 | 2025-09-14 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b5855208-dd8d-335b-ac78-8f2b27414a32 | -21.3821 | -48.5382 | 2025-09-14 02:50:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 117.6 |
| e0c9d07a-7573-3d11-a7f5-ff7a0b09bc35 | -11.3114 | -50.8335 | 2025-09-14 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4dce25cd-63bc-3750-9c5f-a86a82447e95 | -12.9294 | -54.7333 | 2025-09-14 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9510ffba-0370-3fbd-be5c-316d62657364 | -22.7275 | -49.9098 | 2025-09-14 02:50:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 3207d854-4615-31f5-88ae-62b2c4c95845 | -21.3814 | -48.5616 | 2025-09-14 02:50:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| f63d5959-856a-38fe-99e9-335232a499ca | -22.7282 | -49.8866 | 2025-09-14 02:50:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 7fbaae52-0a33-3b87-859f-c5bf9992aa22 | -11.3304 | -50.8314 | 2025-09-14 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8a261069-fa0f-305a-a434-ed84c5d778c8 | -11.2924 | -50.8356 | 2025-09-14 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 85132eb1-93cf-3bda-8f8c-ede1bcd8d553 | -5.66431 | -37.22421 | 2025-09-14 02:58:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 579de861-9d1e-3d35-8a9d-5a18804eb71a | -5.6655 | -37.21779 | 2025-09-14 02:58:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 860ed887-594c-3ef5-8110-a6b80df68ccb | -5.66468 | -37.21655 | 2025-09-14 02:58:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bcc8c539-5d8b-30d6-93e1-841a5368f443 | -5.66353 | -37.22295 | 2025-09-14 02:58:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| da8349f1-dfdb-3933-8bcf-d0cf52cf895e | -3.5995 | -47.5142 | 2025-09-14 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| b9a849fe-0f60-31e8-b72f-f4d14ee2f1d4 | -22.7492 | -49.8817 | 2025-09-14 03:00:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 36252d96-8c97-3109-ac74-75af0ec3f996 | -22.7275 | -49.9098 | 2025-09-14 03:00:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 9eb0ec3b-9e21-3833-943c-05d51cadd47f | -11.3114 | -50.8335 | 2025-09-14 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 75abfd2d-755b-3750-b9d2-a52d2eadbbf4 | -11.2885 | -51.1122 | 2025-09-14 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 6bac8b01-2594-3f37-821d-392f13a56fdd | -11.3075 | -51.1101 | 2025-09-14 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c4e94e04-167a-32cc-b540-cf697332fb7e | -11.2695 | -51.1142 | 2025-09-14 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 55eff61c-b73d-3b77-88b3-243b02f11f93 | -22.7282 | -49.8866 | 2025-09-14 03:00:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 597f7bd4-ecd9-3410-8609-70855383c6e5 | -11.4569 | -48.7026 | 2025-09-14 03:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 1b80c056-d9f4-386c-8152-cc5f29c725e8 | -9.625 | -40.6122 | 2025-09-14 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 685b2b4e-c159-3428-9aef-dd9d5783a1f6 | -12.7863 | -48.0209 | 2025-09-14 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 74f99079-2bbb-3736-8fe9-b628d540303d | -11.8291 | -50.4977 | 2025-09-14 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0f825390-0a15-330d-99db-d43c3cdbf3d3 | -22.7275 | -49.9098 | 2025-09-14 03:10:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 375e65ac-b5ca-3393-aac1-55d6b96c3059 | -12.7867 | -47.9986 | 2025-09-14 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d61001ec-09af-3baa-9b36-2aebc69bdbbc | -11.2885 | -51.1122 | 2025-09-14 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 5681ba98-e881-35a6-9182-4fea2d2955d7 | -10.7687 | -46.4808 | 2025-09-14 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b8ddc738-ffb7-3654-ad46-6ff28bebac6f | -11.8481 | -50.4955 | 2025-09-14 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 3e1922d0-5fe4-3461-b097-4dcefdc32728 | -22.7282 | -49.8866 | 2025-09-14 03:10:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 45873167-1025-32ed-89f4-b9d70dc30fb4 | -11.3259 | -51.1505 | 2025-09-14 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| a9e5bdad-ebec-3575-a83e-55c913bf750f | -11.2888 | -51.0909 | 2025-09-14 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 36e02527-6519-3093-b0a1-1d321ea670ba | -12.7863 | -48.0209 | 2025-09-14 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 78e658d3-3cd4-36d2-9820-2d18b7254d00 | -11.3494 | -50.8294 | 2025-09-14 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 60161dea-b016-3c9a-89b4-1a5b8071b070 | -11.3259 | -51.1505 | 2025-09-14 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7fc922af-7fe4-3116-9d9f-673acb3249dc | -22.7492 | -49.8817 | 2025-09-14 03:20:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 8f9024a6-7829-38f7-90c2-464a419540e9 | -11.2885 | -51.1122 | 2025-09-14 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| c662e08e-7878-31e2-b66f-d17f79b401b4 | -11.4569 | -48.7026 | 2025-09-14 03:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 87089211-aa97-365e-8fb3-7cabf5640f1c | -9.625 | -40.6122 | 2025-09-14 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 58745541-1724-3347-851b-e1fa1026de64 | -12.7675 | -48.0013 | 2025-09-14 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 68a327b2-9243-3c7b-abd3-bfbae1253441 | -22.7282 | -49.8866 | 2025-09-14 03:20:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3e492970-9b37-300d-b46b-a75401e757ca | -12.7867 | -47.9986 | 2025-09-14 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f557166e-1fcf-301c-a5f5-ef3c9f4f202e | -11.3304 | -50.8314 | 2025-09-14 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| ac121b03-3ba6-3377-bc56-3903fc5b37ec | -5.0616 | -40.47173 | 2025-09-14 03:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 50c5f047-2391-360f-a3a3-56a3d9ddb41b | -5.73196 | -43.19961 | 2025-09-14 03:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b699efa5-41ae-3e6a-9322-2e88290eeb93 | -7.37588 | -44.35284 | 2025-09-14 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 635320f4-82dc-3304-9651-d34321e9fa4b | -6.32851 | -43.87228 | 2025-09-14 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 479a342b-798a-345a-b6cb-feafb3e00634 | -6.17691 | -41.1652 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53c03f6e-616d-320f-8464-65eb5c79c130 | -6.42521 | -42.61568 | 2025-09-14 03:25:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 740ac3ea-3a47-3868-83a7-25de21ed098f | -7.06688 | -38.54314 | 2025-09-14 03:25:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 854781da-30a5-3c4c-8950-30b2a66151bc | -6.98757 | -44.54559 | 2025-09-14 03:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3355ed4-0f9b-3a72-82d3-5ec3c9b47c00 | -6.17708 | -41.17641 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39b9e9fc-7303-3251-b254-6d5957763899 | -5.39921 | -40.34585 | 2025-09-14 03:25:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e2241bf5-264c-3122-82c6-c932de0ed97b | -8.61817 | -40.19617 | 2025-09-14 03:25:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cdf37cd2-233b-3b61-bcf9-cbc12ac0109f | -8.61755 | -40.19954 | 2025-09-14 03:25:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b02d68b4-a88e-3e1e-b951-eb0cf08cf34c | -6.28255 | -39.68757 | 2025-09-14 03:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7b3d8a5d-d1ad-38fd-beff-cb793e0b0238 | -7.38152 | -44.36142 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 591d5a55-5b3a-3218-9ec9-57069c74bf97 | -5.79416 | -43.89172 | 2025-09-14 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a663fae7-ad70-31db-a3d0-32181e0c6adb | -6.17868 | -41.16765 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62697a03-decc-3ea6-9ae2-0400bf1ed308 | -6.33069 | -43.87418 | 2025-09-14 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bf39cc70-5f9c-3bf9-98cd-b6845de1e650 | -5.73093 | -43.20517 | 2025-09-14 03:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2061f8e5-4b88-3c52-9b48-33c95e5a2390 | -8.50427 | -44.73146 | 2025-09-14 03:25:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab8b1fa4-ad90-3e5c-b69b-17a8627261c2 | -9.62658 | -40.6179 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| e65562e8-639d-3427-98ad-e9dd4e7d19c4 | -5.66268 | -37.21238 | 2025-09-14 03:25:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92aae4c1-680b-3442-b643-8c16d508a6c0 | -8.49857 | -44.72295 | 2025-09-14 03:25:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd1465ac-8ee4-3d8c-916d-d9e9e7a11010 | -7.72397 | -44.85582 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0fcbf44a-6cc7-3821-aa55-3d7b99232d51 | -6.52834 | -39.51096 | 2025-09-14 03:25:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f70f409-9d10-3d04-8c5c-09be8b4fdff0 | -5.78928 | -43.89483 | 2025-09-14 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3908dfe-d8af-3544-86ea-2ae792bf7bba | -7.72239 | -44.8638 | 2025-09-14 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f80bde2-0156-3b4d-bc45-a8e9db355c75 | -6.17789 | -41.17202 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8eb5d74d-7604-3c95-b340-754798097a71 | -6.17948 | -41.1633 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4b2f5dc-08be-3109-97f9-8c009f7d5009 | -7.37186 | -44.35231 | 2025-09-14 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d2d22b2-ca43-3473-93fa-62907dd2f8ef | -6.17843 | -41.15654 | 2025-09-14 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df55cbc1-beb7-3a94-b3fd-71041cd933b2 | -6.33414 | -43.88069 | 2025-09-14 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 20887216-be62-3fc1-8f30-effdcca47fe9 | -6.33759 | -43.87592 | 2025-09-14 03:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ad4851e7-f5a4-30ee-8386-7cd8cc8d0f60 | -8.14007 | -43.6682 | 2025-09-14 03:25:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60df03af-2cc6-39c6-a662-d888269979cf | -9.43331 | -40.30835 | 2025-09-14 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1a0c7860-d622-3558-a82a-9f09005fa05b | -8.49476 | -44.72052 | 2025-09-14 03:25:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README7.md)
