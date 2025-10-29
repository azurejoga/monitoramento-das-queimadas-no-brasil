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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6d81406-8aca-35ea-bc3d-c21b44fd71da | -5.90273 | -37.82929 | 2025-10-29 03:04:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24200c5e-bea2-32f0-a5f0-81f09d359abd | -13.81825 | -41.69893 | 2025-10-29 03:06:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7624591b-9c10-382d-890d-748315c75c35 | -16.6296 | -42.21991 | 2025-10-29 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc965114-385d-3b36-811c-fac2a5afd093 | -13.81119 | -41.69707 | 2025-10-29 03:06:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7ec248d-acd7-3ebe-8833-927ef3811b7b | -16.62794 | -42.22703 | 2025-10-29 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a16e3be-31b1-3511-8345-91b6b408ece2 | -13.81552 | -41.69938 | 2025-10-29 03:06:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 3b636882-0fe4-33a0-9683-9953139bb6e8 | -20.99955 | -42.8026 | 2025-10-29 03:08:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a7505d58-e6f8-3033-a980-0ff022763393 | -19.33126 | -43.05352 | 2025-10-29 03:08:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 49df1295-0355-383c-9d1b-588515f26675 | -20.99541 | -42.80608 | 2025-10-29 03:08:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5b8d45b6-3fd2-3576-a723-00dd9a9df6b0 | -18.88873 | -43.3586 | 2025-10-29 03:08:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d45c1dc9-3639-323b-8918-01340b4b23b5 | -19.32946 | -43.05243 | 2025-10-29 03:08:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 779cca44-4b29-38c6-9652-25dcb98917ed | -19.98181 | -41.06952 | 2025-10-29 03:08:00 | NOAA-20 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8c097595-ec90-3a34-ae6a-7fe4c00e9c36 | -19.3279 | -43.05879 | 2025-10-29 03:08:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3f60d648-6f30-31ca-8383-b87554caba61 | -18.88691 | -43.36612 | 2025-10-29 03:08:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f802be8a-b632-3823-ad0a-fb9f1706199b | -19.33502 | -43.05975 | 2025-10-29 03:08:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d1f4e919-569f-3ab7-b57a-7ca1b704a366 | -19.32967 | -43.06017 | 2025-10-29 03:08:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f89edf2a-b6cd-3556-9f78-7088fdd65987 | -19.98063 | -41.07451 | 2025-10-29 03:08:00 | NOAA-20 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fd94d718-2a04-310d-b731-eb0fea8c8d6a | -20.99697 | -42.79958 | 2025-10-29 03:08:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 343e2588-c9cf-3bd5-a96e-b0e32137dfc1 | -19.4214 | -48.0566 | 2025-10-29 03:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 60e1fabf-68a1-30d4-830f-38b136ea501b | -15.1202 | -43.8294 | 2025-10-29 03:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 547836c3-e100-395c-8ccd-6eb00817235e | -12.0032 | -46.7892 | 2025-10-29 03:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8f7ec5e2-05e5-39ae-bc65-c8683168ee1e | -15.0809 | -43.8372 | 2025-10-29 03:10:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 63.1 |
| d42e6b06-fcf2-3beb-9a4e-1a4e17d7d072 | -10.6509 | -47.9869 | 2025-10-29 03:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9fd475f7-8c24-37ea-9ff3-ca16a8e8c042 | -15.1 | -43.8573 | 2025-10-29 03:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| aa52d0d9-ef65-3593-b2bc-fd36d656d62c | -9.943 | -47.1614 | 2025-10-29 03:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1bf43d99-3e91-385d-98f5-0ef008ef0814 | -4.1972 | -50.0819 | 2025-10-29 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9a2487f1-5d6f-382c-a6ab-8912f68b238f | -15.1006 | -43.8333 | 2025-10-29 03:10:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 176.2 |
| b54eae03-380a-397f-bc97-ff95e14ce00a | -4.4804 | -43.447 | 2025-10-29 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2af28595-b443-3857-aa09-2209d371803b | -4.2157 | -50.0812 | 2025-10-29 03:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| e120e94d-a014-33a9-9180-2a58c48cb40f | -6.2939 | -41.8744 | 2025-10-29 03:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| daa2abf4-ec45-37cc-81dc-b3da90c83254 | -10.6506 | -48.009 | 2025-10-29 03:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 34e596ef-d2d3-370b-9bdc-171f1ca4d28f | -18.94 | -45.0429 | 2025-10-29 03:10:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 072ef833-3319-3155-a03c-82724480afd8 | -18.94 | -45.0429 | 2025-10-29 03:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 86.9 |
| be30fcef-0461-317a-93d0-94981ab8a4e9 | -10.6509 | -47.9869 | 2025-10-29 03:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| dfd77b8a-da2f-399c-b406-367c11d93596 | -12.0032 | -46.7892 | 2025-10-29 03:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e0920767-510b-31f2-a643-60262b72740c | -4.4804 | -43.447 | 2025-10-29 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 48f5ea5c-38b7-38b1-8aec-739bc4cf169e | -10.6506 | -48.009 | 2025-10-29 03:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0e3dc28b-f64e-38a6-8eed-7ca957373e4f | -13.6422 | -46.5205 | 2025-10-29 03:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4b9ca832-511b-3537-bd36-0d9305854ff5 | -15.1006 | -43.8333 | 2025-10-29 03:20:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 3f36e493-4b56-343a-984b-ddc9b23e9292 | -15.1 | -43.8573 | 2025-10-29 03:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0af5f9a8-0296-3ed2-a173-24f5f6425f46 | -6.2939 | -41.8744 | 2025-10-29 03:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 2299d53e-b6b4-3561-9d7f-ade60eeb39a0 | -18.9197 | -45.0478 | 2025-10-29 03:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e11af9e7-27b7-32be-9a9b-e38868a055f7 | -10.6506 | -48.009 | 2025-10-29 03:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b104aca2-d4da-3300-9fe4-1ec02a32be83 | -18.94 | -45.0429 | 2025-10-29 03:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b76c0697-44d2-3be8-b283-70d5255276c1 | -4.2157 | -50.0812 | 2025-10-29 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 626818e8-9d29-3280-90a0-edaa1e6d42ba | -4.4804 | -43.447 | 2025-10-29 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c1203b5d-7e71-396d-9aca-e3c919db8bbd | -6.2939 | -41.8744 | 2025-10-29 03:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| b7807d74-c939-3f72-86e5-a2f010a95c53 | -15.1006 | -43.8333 | 2025-10-29 03:30:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 49815fe8-9990-3113-8c60-6926388bb8c3 | -12.0032 | -46.7892 | 2025-10-29 03:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e04e8bad-77ca-34ae-b855-03c6bfa84503 | -6.3127 | -41.8727 | 2025-10-29 03:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 71a4fadb-852a-3d30-a170-d896d51e1a65 | -4.1972 | -50.0819 | 2025-10-29 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 658209a1-9aac-3892-8913-8dd544342819 | -19.4417 | -48.0522 | 2025-10-29 03:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3f16319a-5484-3d7b-8f3f-864da5401369 | -19.4214 | -48.0566 | 2025-10-29 03:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a2c48652-7e18-3d77-8a21-3057a8c6f078 | -7.8037 | -46.4458 | 2025-10-29 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c0b993e9-3315-3629-959c-1a54fa875403 | -19.4208 | -48.0797 | 2025-10-29 03:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 20188de4-6a3b-3e52-9a02-f598373c3a12 | -15.1006 | -43.8333 | 2025-10-29 03:40:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 118.7 |
| b5028cc8-1373-31b3-824f-3f2ae7b2d9c8 | -18.94 | -45.0429 | 2025-10-29 03:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 3ea76fd2-2a02-3c60-bb1b-9758cfc7630d | -18.9197 | -45.0478 | 2025-10-29 03:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 37dea82b-a067-3bc8-9c69-676b6799c283 | -4.4804 | -43.447 | 2025-10-29 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 82af6c8b-5470-36d1-90a4-0db075d1d3ef | -4.2157 | -50.0812 | 2025-10-29 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4ca8f3d9-a5af-397b-b0f7-12d61d497a08 | -12.0032 | -46.7892 | 2025-10-29 03:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 341a8703-5803-33d9-a4da-f1d7b9f9533a | -18.9197 | -45.0478 | 2025-10-29 03:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d25b4821-bbe2-3108-b02c-c9d55f84fbc5 | -7.8035 | -46.4681 | 2025-10-29 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 698a744f-eeee-3383-9310-154f8a8b962c | -7.8037 | -46.4458 | 2025-10-29 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| da75a169-8b2c-3c37-bc50-9fcdfe7599ef | -4.2157 | -50.0812 | 2025-10-29 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| fc88cb74-b64d-3a22-8b46-f5d05911b3da | -15.1006 | -43.8333 | 2025-10-29 03:50:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 056815e1-4834-3f1e-993f-a395d19c9760 | -4.1972 | -50.0819 | 2025-10-29 03:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 62c2ffcd-408f-3d2c-b615-c4131d5f519b | -12.1958 | -46.717 | 2025-10-29 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a73fe199-8bf9-37f4-b9ed-7e157e69e88a | -12.7021 | -46.303 | 2025-10-29 03:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| fe0601ec-d8a1-325f-8596-53096477a2cf | -18.94 | -45.0429 | 2025-10-29 03:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f6105d1e-eeab-3e14-9b84-cb761d5813d4 | -10.6506 | -48.009 | 2025-10-29 03:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 383e261b-e653-3941-b204-5ac0afd778d0 | -7.7847 | -46.4698 | 2025-10-29 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 01e55e60-5379-3990-949a-ecea15cb4f9a | -6.1249 | -41.8414 | 2025-10-29 03:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 32d0c307-5f6c-36af-821e-c093f6a748d9 | -18.9204 | -45.0237 | 2025-10-29 03:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| dd91cbcd-07b1-3f2f-a30f-0eec3d697c2d | -12.0032 | -46.7892 | 2025-10-29 03:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 116d2960-381a-30fc-840c-1c4524d0ec7b | -2.91085 | -40.3468 | 2025-10-29 03:51:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 85055beb-4759-34b3-ab78-022160ebad02 | -2.90852 | -40.3426 | 2025-10-29 03:51:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 1f21c9f6-dfd8-36f5-bbd2-ba635a80165f | -0.86492 | -47.31133 | 2025-10-29 03:51:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d44732a-5cd9-37e4-8d44-d465081d729c | -1.49228 | -47.81156 | 2025-10-29 03:51:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b4edb0c5-1143-34b1-a4c2-85843f3d39ce | -2.9073 | -40.34624 | 2025-10-29 03:51:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 940ef526-d0eb-3c70-96b4-b3c325c5290a | -1.49407 | -47.81292 | 2025-10-29 03:51:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2f0fa083-46cb-39fe-b9be-fe30b5b255c6 | -1.49476 | -47.80863 | 2025-10-29 03:51:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9694a26a-37b6-3d67-b841-171b0b3cbabd | -1.49299 | -47.80725 | 2025-10-29 03:51:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5c9773ec-8c31-3761-bea0-cc4b3982478f | -2.90788 | -40.34663 | 2025-10-29 03:51:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 0036c3e0-46fe-326f-a639-de89545d7d1c | -1.49544 | -47.80433 | 2025-10-29 03:51:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 451ca475-0c59-3795-897a-4ff9ea91d8ba | -5.33484 | -45.42816 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0b7d94b-93b0-3130-b0b3-712696935653 | -7.89133 | -45.68738 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52a695b1-95dd-373f-a72f-b9660977f186 | -6.11234 | -41.71296 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ccf3ec8f-1761-3c01-b15a-c345c2f1a98d | -4.0868 | -46.93235 | 2025-10-29 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 843d199c-5a45-3cff-a385-b1386b617b6d | -7.8956 | -45.68548 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b526fd36-4261-3ea5-8886-b6a75960223e | -6.98959 | -46.23515 | 2025-10-29 03:53:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e9d6d6c-e2e5-3bcb-aac9-7778d23ff8f3 | -8.00414 | -46.21045 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d7a4d52f-d18a-3fb7-bc83-ba780add88ff | -7.74955 | -44.71619 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c587f862-40b3-376c-b112-a7e3dcfdebed | -7.43288 | -41.85579 | 2025-10-29 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| db90007c-a9ef-38aa-828f-bb69b65abb91 | -7.79021 | -46.47065 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59f7d64f-72dc-304a-9aab-d4b7d1efdd07 | -7.40884 | -47.17459 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 772ff1ce-5d98-3df8-a809-302ad7534994 | -7.70236 | -46.90562 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17f68cce-5bc3-32ce-b7b7-2b99e7f65927 | -3.46095 | -43.35344 | 2025-10-29 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89203171-8b1d-3a41-969f-ee286a27c5a9 | -7.43777 | -45.1246 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0e6cd0e-1100-3bf2-8ff8-bca1c2e82d6a | -5.33971 | -45.54852 | 2025-10-29 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README6.md)
