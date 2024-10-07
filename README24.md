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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3375f1c-0274-3b25-8454-6f2683513906 | -2.2174 | -53.708599 | 2024-10-07 01:24:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 074f96e9-3346-32d3-9f6e-fafe64018e5f | -2.7585 | -57.6464 | 2024-10-07 01:24:45 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e9a10ff-dd55-3d47-ae1a-8cc51633e905 | -1.1271 | -53.623001 | 2024-10-07 01:24:57 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc1166c-696a-3135-b5f7-78ba0f0cb84b | -1.0326 | -53.5261 | 2024-10-07 01:24:58 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf8ff407-e72e-3ee6-8753-e07a9a21649b | -1.035 | -53.5364 | 2024-10-07 01:24:58 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e93af8-4475-3d19-aa41-51bc74296d00 | -1.0239 | -53.710098 | 2024-10-07 01:24:59 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3eb99d4-a8a4-30e8-9f72-aea1936d09ab | -1.0262 | -53.7202 | 2024-10-07 01:24:59 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b57a8704-eda6-3e4e-9f74-ebef8d8221fe | -1.0285 | -53.730202 | 2024-10-07 01:24:59 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caaa9045-e537-3740-913d-b5f106d20447 | -1.0365 | -53.7389 | 2024-10-07 01:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 22037f2c-067a-367f-9a2d-8ac355218d67 | -1.0365 | -53.7187 | 2024-10-07 01:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 0c1424fd-eba4-379e-b253-c1ba382465a0 | -2.2113 | -53.7029 | 2024-10-07 01:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c9c5a948-8e61-3c36-ab59-c9840ff73090 | -2.2297 | -53.7026 | 2024-10-07 01:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 983093d6-78e6-3de8-a6a2-21041e3be661 | -2.8569 | -52.9197 | 2024-10-07 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| a0688eaa-71e4-3731-82dd-4686b4d1ef23 | -2.857 | -52.8993 | 2024-10-07 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 7444003c-a931-301a-90f9-b0e7590cb224 | -2.8753 | -52.9192 | 2024-10-07 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 197.4 |
| 713a95fd-71b6-3441-a140-4ced7e66e374 | -2.8754 | -52.8989 | 2024-10-07 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 234.8 |
| deab1808-6520-3d3e-9edd-81270257fc6e | -2.8937 | -52.8984 | 2024-10-07 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 151bdb37-6bcd-3db3-a4f5-cf8a3419a858 | -3.5381 | -65.0229 | 2024-10-07 01:25:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| f12db7d2-1634-342d-8f92-80f318e77743 | -4.2728 | -43.7601 | 2024-10-07 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f7b01759-9d86-35c2-b432-8880c381799f | -4.2729 | -43.737 | 2024-10-07 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 6629c9e5-2c0f-309f-8ce1-358e56e0f081 | -4.2914 | -43.7591 | 2024-10-07 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 1b7b1080-3b2d-31f3-92bc-c55271a18037 | -4.2916 | -43.736 | 2024-10-07 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8579928e-78c9-358a-990f-3fd94716527c | -5.3153 | -44.2479 | 2024-10-07 01:25:36 | GOES-16 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0fb95762-0e86-3a48-8cd5-e288fd093b55 | -5.3155 | -44.2249 | 2024-10-07 01:25:36 | GOES-16 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 16d15713-5fce-3ad0-b1af-a6db27085c03 | -9.5152 | -40.331 | 2024-10-07 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 56fd90d6-af2f-375f-afdf-39287c9097ef | -9.5343 | -40.3282 | 2024-10-07 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.1 |
| ba5d974b-d6d5-3a83-a43f-8562a46f4ada | -10.4506 | -63.1393 | 2024-10-07 01:26:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d7fc7209-c685-3960-88c5-8ed0e08fd45c | -10.4508 | -63.1203 | 2024-10-07 01:26:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d30b34fe-da28-381a-a78f-82987fceb218 | -10.4693 | -63.1384 | 2024-10-07 01:26:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9877c56d-6cea-312a-b861-160140686d78 | -10.8754 | -63.9169 | 2024-10-07 01:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5e05e267-d765-3049-8fb0-6700f6f613ab | -10.8755 | -63.8979 | 2024-10-07 01:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c4c62641-dc74-319d-8136-5cb0972f7423 | -11.2583 | -60.3885 | 2024-10-07 01:26:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8e8cef8c-421f-3acd-8a90-910b2a091b15 | -11.2657 | -51.3898 | 2024-10-07 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2a90c1b9-1558-30b1-981c-52ff4fc2bf99 | -11.2844 | -51.409 | 2024-10-07 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f0f7f51b-556a-322a-a4cf-85517f13ddc5 | -11.2847 | -51.3878 | 2024-10-07 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 0b48e202-56af-3fa5-86f9-49868f6b4f83 | -11.3037 | -51.3858 | 2024-10-07 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0b45ce21-ed16-31c1-ba9d-01a4ce5eb9b3 | -12.0585 | -63.7841 | 2024-10-07 01:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| fe93b1ad-e4e5-34ac-bf50-ff16c9f6ec86 | -13.5719 | -50.3223 | 2024-10-07 01:26:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 63b8c91f-5dca-3b8f-be66-9aa7e71aae14 | -13.5723 | -50.3006 | 2024-10-07 01:26:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 198.7 |
| cbfbd597-1059-3529-9200-4af21bf356a1 | -13.5911 | -50.3197 | 2024-10-07 01:26:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 199.7 |
| c7fdf5cc-79a1-3a17-a562-4b5d7c58a140 | -13.5915 | -50.298 | 2024-10-07 01:26:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 265.0 |
| b4f13f03-3cd5-369e-b1c4-8372f4b2829b | -13.5919 | -50.2763 | 2024-10-07 01:26:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ef3188a0-6a2c-3f35-9968-89ba905c44b6 | -13.6108 | -50.2954 | 2024-10-07 01:26:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 991c5734-797f-3319-9fcc-23302dedf5f3 | -16.992 | -56.721 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| a1f5831d-573c-36b4-8b02-79b60ecaa7c3 | -17.0116 | -56.7186 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 28977db0-081e-3690-bed0-a69a7a51f5e9 | -17.012 | -56.698 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 44f66572-4638-3b7d-aced-220bba58ee5c | -17.0685 | -56.8352 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.2 |
| 2d77b324-e958-3937-a76c-296a176880c0 | -17.0688 | -56.8145 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.2 |
| a7f2d79d-5b62-3f4d-8301-8527ba337d60 | -17.0881 | -56.8328 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 206.3 |
| 49621f6c-c43f-344e-ba05-ee6e3872ae13 | -17.0885 | -56.8122 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| bf1f676e-c947-3242-9d3c-7e463e5d891e | -17.1078 | -56.8304 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 157.9 |
| e74c0dea-95c0-3fac-9a75-d6e368683f67 | -17.1274 | -56.828 | 2024-10-07 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 7c529354-957b-303a-a0fb-3b42169d72e9 | -17.1786 | -53.9213 | 2024-10-07 01:26:42 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| ddcb0352-a291-34fd-896f-1777fc36bf14 | -17.1581 | -57.3582 | 2024-10-07 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.6 |
| 289b0f31-3b73-3dfa-8d8f-5c9ee39b47d5 | -17.1584 | -57.3377 | 2024-10-07 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 2cfe0a34-5847-3800-aa8d-f0be8d0c82a5 | -17.6274 | -53.1309 | 2024-10-07 01:26:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0e0385dc-98db-3c66-a50c-2e617d5f2687 | -17.6279 | -53.1094 | 2024-10-07 01:26:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 450.4 |
| 58925241-0f1d-3837-8298-0783351ab9fc | -17.6283 | -53.088 | 2024-10-07 01:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 203.9 |
| f47bf14e-f849-3a1c-a23d-2aa28ff8967c | -17.6477 | -53.1064 | 2024-10-07 01:26:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 605acf78-7a5a-314e-bb07-6f3f6a64014d | -17.6481 | -53.0849 | 2024-10-07 01:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 28b4761f-9dbb-3805-91dc-5441202666dc | -17.6679 | -53.0819 | 2024-10-07 01:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 263d5458-1a1e-3fb7-806f-5adf6bff2c81 | -18.4518 | -53.5165 | 2024-10-07 01:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 5dca0e08-a418-3489-93be-b024593ae05e | -18.4718 | -53.5134 | 2024-10-07 01:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| fec661f8-4929-3871-a082-120f84e69445 | -18.4722 | -53.4919 | 2024-10-07 01:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e19e43fd-886d-36a8-a617-2d7e8255926f | -18.6391 | -57.2578 | 2024-10-07 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 33723133-5751-3d19-b5ed-26d6464b8cc3 | -18.659 | -57.2552 | 2024-10-07 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 9587cb3a-45cc-3cb9-a9f8-e166b7e79f2c | -18.8686 | -54.5617 | 2024-10-07 01:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1ab38ca4-fb88-34b8-9edd-d60f51e3f8c8 | -19.8112 | -42.36 | 2024-10-07 01:26:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 32597d34-0c66-3c4b-b62d-ec20e811f5f9 | -19.831 | -42.3796 | 2024-10-07 01:26:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| c46087af-7372-3416-828f-dc57ed502a56 | -19.8318 | -42.3542 | 2024-10-07 01:26:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 159.1 |
| a421f46f-e40a-3576-b3a4-e9c17c012b9c | -19.883 | -42.6663 | 2024-10-07 01:26:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| 66189043-b165-38f1-a336-8935d113d823 | -19.8838 | -42.641 | 2024-10-07 01:26:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.9 |
| 5c36ad80-95c3-32ab-8f1c-78e58b8a118d | -20.1019 | -49.0791 | 2024-10-07 01:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2d4216bf-0953-3479-a138-a26049b43d5d | -20.1026 | -49.0562 | 2024-10-07 01:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 6e345f72-2141-3cfb-8c8c-ca8e15114f06 | -20.1223 | -49.0748 | 2024-10-07 01:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 92f43d81-2af6-337e-96df-0f9a7ee2738d | -20.1229 | -49.0518 | 2024-10-07 01:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 412.8 |
| 87aa05fc-a8bc-3c88-8f4a-bf085e07205d | -20.1236 | -49.0288 | 2024-10-07 01:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 17c4b534-4529-3004-b197-8bd60436cceb | -20.1433 | -49.0474 | 2024-10-07 01:26:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 8d76f1ca-5f6a-332f-bcf9-af6706661975 | -20.4449 | -47.6875 | 2024-10-07 01:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 20d07595-42a0-3d62-86e9-0ba928577aa8 | -20.4456 | -47.664 | 2024-10-07 01:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 7515f075-4aaa-3205-ba17-8385ceaaf1d7 | -20.4655 | -47.6827 | 2024-10-07 01:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 443.3 |
| 77505885-e818-3dfc-bcdc-a774b1610b12 | -20.4661 | -47.6592 | 2024-10-07 01:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 1012.6 |
| 14eb9b00-44c1-3835-a7ae-e44ce3d0ab74 | -20.4668 | -47.6357 | 2024-10-07 01:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 8b3c1d55-13e4-319d-a875-6f6231d3bd9f | -20.4866 | -47.6544 | 2024-10-07 01:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 842ac33d-1b13-36e8-bf94-2d0e77831dd9 | -20.606 | -48.4858 | 2024-10-07 01:27:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 306.6 |
| 487e62ad-07d8-3b45-a458-eba9d70a994f | -20.5855 | -48.4904 | 2024-10-07 01:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 550970f1-3385-396c-8fdf-1d36aeef5110 | -20.6053 | -48.509 | 2024-10-07 01:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b9ff2adb-e9b3-3b9f-a41d-a397e49f70e4 | -21.0712 | -47.2331 | 2024-10-07 01:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 56dfe3da-2485-399c-9132-9c136680a7d8 | -21.0919 | -47.228 | 2024-10-07 01:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 167d86a6-bcc1-39ae-80b6-9f62e52e7410 | -21.605 | -47.9485 | 2024-10-07 01:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 70f1cb66-40d1-3a08-97c3-45ed083f3b57 | -21.5843 | -47.9536 | 2024-10-07 01:27:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 82cc5444-ab92-3963-a00b-5b8a21cb8fbc | -21.6529 | -47.7255 | 2024-10-07 01:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d75a82c6-8131-39c3-a501-92a856c5d768 | -22.1974 | -48.1778 | 2024-10-07 01:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9df7522e-796f-3146-bcef-f52446edc7d8 | -22.2183 | -48.1726 | 2024-10-07 01:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9cd9dbab-2bbf-3f29-88bb-5b8b16426b02 | -20.0709 | -54.53439 | 2024-10-07 01:28:00 | TERRA_M-M | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9f236ccf-89e2-32f5-9720-f7f1ac56742a | -20.10856 | -49.05177 | 2024-10-07 01:28:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ca168220-ce6a-390d-95b7-828f6f693b7c | -20.11999 | -49.0494 | 2024-10-07 01:28:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 325.4 |
| 392be418-bd8a-314b-a94b-93a8b7b910e9 | -20.12281 | -49.06568 | 2024-10-07 01:28:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 389.2 |
| 05a1c9d1-a720-3eac-8fc8-a0864491cc39 | -20.26471 | -56.53061 | 2024-10-07 01:28:00 | TERRA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| bc42bd53-d7f6-34dc-b26e-50886e5e498e | -20.44211 | -47.66607 | 2024-10-07 01:28:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 23.2 |


[Clique aqui para ver as próximas entradas](README25.md)
