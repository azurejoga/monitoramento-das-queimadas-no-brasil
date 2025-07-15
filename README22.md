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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a9bfe0c-a622-3421-8b86-0b375a1f3eed | -22.3966 | -49.80291 | 2025-07-15 04:36:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5e1985ad-3c57-3c45-a34d-5ad7f78fc6c4 | -19.28348 | -49.38988 | 2025-07-15 04:36:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd89e442-532c-3b69-b8b6-64d8efa692e1 | -22.90012 | -43.75094 | 2025-07-15 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fd77225d-7e30-3d46-9fca-28e9c3fba238 | -18.65505 | -55.71914 | 2025-07-15 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 829bbee5-f46d-3285-a785-c2a1a57f01ac | -22.67458 | -42.85391 | 2025-07-15 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8494b8a2-b48d-3eba-861c-6ad2dafbe70c | -20.39429 | -46.53566 | 2025-07-15 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d39f8f4d-13b8-31d8-a9f6-05db6e07b9e9 | -20.30984 | -45.58307 | 2025-07-15 04:36:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9542024c-0b1c-3308-8d47-3dbf703b3bc3 | -21.25051 | -51.65731 | 2025-07-15 04:36:00 | NOAA-20 | SÃO JOÃO DO PAU D'ALHO | SÃO PAULO | Brasil | 3549300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4ef8afc1-6f23-32da-bbc4-1415c96b8c50 | -22.39718 | -49.79893 | 2025-07-15 04:36:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d3639bfa-4f12-32db-ac43-7834cd8f5465 | -21.86141 | -56.74941 | 2025-07-15 04:36:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 311b6f66-5e30-31eb-89ee-40e2c3cea8b5 | -22.51385 | -47.01469 | 2025-07-15 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f26bf45-2e25-39d9-8322-6379f1bad237 | -20.39041 | -46.53493 | 2025-07-15 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4244bcd-8a82-3f5b-af1c-48ef245f7750 | -23.06145 | -51.07684 | 2025-07-15 04:36:00 | NOAA-20 | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b3fa795a-27e8-3618-89ab-372096a26772 | -25.24981 | -49.92624 | 2025-07-15 04:38:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dfd2cd2c-d410-31c4-8ab6-15343c7b22fd | -28.16776 | -49.3583 | 2025-07-15 04:38:00 | NOAA-20 | GRÃO PARÁ | SANTA CATARINA | Brasil | 4206108 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 49f1bd05-0a83-3224-aa73-e8464988b43a | -27.08946 | -50.51265 | 2025-07-15 04:38:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6a0dada3-1c8b-3225-b44e-3fee855b39cd | -25.63002 | -51.96093 | 2025-07-15 04:38:00 | NOAA-20 | CANDÓI | PARANÁ | Brasil | 4104428 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b77cee9c-b63b-3071-80f7-2b2fd68ce038 | -28.12482 | -54.93863 | 2025-07-15 04:38:00 | NOAA-20 | ROQUE GONZALES | RIO GRANDE DO SUL | Brasil | 4316303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b558501c-8dc9-3e5c-8b07-3ba1da8002b8 | -25.19209 | -49.32892 | 2025-07-15 04:38:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bd92a1d7-e0c4-3528-8840-98bdf91d99e3 | -28.58414 | -49.44259 | 2025-07-15 04:38:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83d2befd-0be5-3e0f-8db6-e82fd5dfd47b | -28.60098 | -55.40381 | 2025-07-15 04:38:00 | NOAA-20 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 426d6e85-9563-349d-be17-efe16e0011ee | -28.1282 | -54.93935 | 2025-07-15 04:38:00 | NOAA-20 | ROQUE GONZALES | RIO GRANDE DO SUL | Brasil | 4316303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 183cfd83-8054-3414-a66c-8bfa1497ab15 | -10.5776 | -49.1316 | 2025-07-15 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b740835e-a816-3e3d-9928-bddbd053e6ca | -11.4397 | -45.0923 | 2025-07-15 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 0cc85e8f-d5e8-3a42-962e-4d8cebd4fb60 | -11.4393 | -45.1154 | 2025-07-15 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9f96adf7-9f4b-3631-ba3a-21367b86322d | -11.4588 | -45.0895 | 2025-07-15 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 223.3 |
| ac66bc57-5050-34f3-8c18-d01962ac2a2a | -11.4584 | -45.1126 | 2025-07-15 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a09145cb-40ce-3e31-b9e7-44856ba7ee84 | -11.4389 | -45.1385 | 2025-07-15 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 2a51503c-e2f2-3a7b-a591-3ae5a2845098 | -11.4393 | -45.1154 | 2025-07-15 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 342b1eea-eaf8-3cac-8d46-8bce83d7842f | -11.4588 | -45.0895 | 2025-07-15 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 6b29b37f-f38a-31d4-80ed-014fdd15b6b6 | -11.4397 | -45.0923 | 2025-07-15 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 969b7e58-a7da-312f-b329-e40c67a19f70 | -11.4584 | -45.1126 | 2025-07-15 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 915373ab-71c6-3c68-817d-4ea54dd2bae8 | -11.478 | -45.0868 | 2025-07-15 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9f6b4e02-5331-38e3-867b-ebe3a95e8218 | -10.5586 | -49.1337 | 2025-07-15 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ea74dce6-2047-3a36-8000-abff57c36809 | -5.3741 | -43.9216 | 2025-07-15 04:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 78aa7ecd-6ec0-33a3-bc67-f7935cfe70a9 | -11.4588 | -45.0895 | 2025-07-15 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 1bc8ca45-524b-3a75-b74d-43633e766827 | -11.4592 | -45.0664 | 2025-07-15 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c779fb1d-b0ad-3231-928b-515031f83189 | -11.4393 | -45.1154 | 2025-07-15 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ad8321aa-c605-3a1e-bbf2-c51fe1f861e9 | -10.5776 | -49.1316 | 2025-07-15 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4db4817c-c76b-3796-8129-38d2fd1ee244 | -11.4584 | -45.1126 | 2025-07-15 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 44a444b7-ff78-3fc8-bd50-11c167f92a9a | -10.5586 | -49.1337 | 2025-07-15 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 73c546ae-4830-39ff-8469-2a161ce3c34a | -11.4389 | -45.1385 | 2025-07-15 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2dc9e41e-e6c2-30ea-8cf9-e6561079608e | -11.4397 | -45.0923 | 2025-07-15 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 408e6148-c2a7-3628-bc17-0fac9a3a2dee | -11.4389 | -45.1385 | 2025-07-15 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c916d0df-90d0-3bf5-9fbd-aa7f2b6971c2 | -11.4584 | -45.1126 | 2025-07-15 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b3481a1d-9fa4-3fcd-96cf-288517f9aa2a | -11.4588 | -45.0895 | 2025-07-15 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 207.0 |
| cee181aa-9cf5-342e-baea-f9f86c07c8f0 | -11.4397 | -45.0923 | 2025-07-15 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 338ed11d-8f0b-3198-b9a4-47e69be6611a | -11.4393 | -45.1154 | 2025-07-15 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7630cb2b-cf93-3c89-8e62-2933cde4e8c0 | -10.5776 | -49.1316 | 2025-07-15 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 58e0034a-e9ba-38ff-a1af-776c002b17dd | -11.4588 | -45.0895 | 2025-07-15 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 515263d9-b507-3525-97bd-a68cda7c3944 | -11.4584 | -45.1126 | 2025-07-15 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| a575d1b5-2c22-37fd-b709-5afd01a1ccfe | -11.4397 | -45.0923 | 2025-07-15 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 85ca146f-0243-308a-835a-617d0a4fd4a5 | -11.4393 | -45.1154 | 2025-07-15 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 30bf8881-d800-3210-8397-8ca6aee9faa4 | -10.5776 | -49.1316 | 2025-07-15 05:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 56cad3a4-b3ea-358c-9b89-09e2a017a782 | -9.29132 | -63.72257 | 2025-07-15 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da2f1511-af54-3d12-8118-b3bf862adf29 | -4.27007 | -48.18333 | 2025-07-15 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 34d72e56-8f93-34b2-b4ea-56d8f3fed2c4 | -9.42794 | -59.16972 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9a9f484-5e56-35ee-b77c-118a3ed76035 | -10.49913 | -53.57669 | 2025-07-15 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c487cea-3429-3aac-8791-3ccc97dfc394 | -7.40736 | -72.59903 | 2025-07-15 05:23:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b040ecc-9066-312f-8d9f-b45673c852d5 | -9.30174 | -63.72428 | 2025-07-15 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf833f9f-d791-30b1-97ef-0c568a88b815 | -9.29479 | -63.72314 | 2025-07-15 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eb4d202-555b-3ff8-83e7-bc89a79e5bbd | -10.06116 | -59.11275 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 962515f5-0ddf-3827-b590-3d28e224c0cc | -10.57296 | -49.142 | 2025-07-15 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f5ee1364-0bc7-3a88-bf9e-2b97ae46fe46 | -10.89514 | -49.21145 | 2025-07-15 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 99b174d9-2a4c-3ae4-b973-ea8d932d648f | -10.28137 | -60.53646 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00880bb3-87ba-3e55-bf81-ada81b9015d7 | -8.38295 | -51.07681 | 2025-07-15 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ead811b7-9718-3b21-a3ed-7eb74e686072 | -10.87751 | -54.05481 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9774413-27cd-397f-889e-90be0a58e1a6 | -9.02499 | -61.23306 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e25055eb-48b4-3267-ad0f-dd5038615336 | -10.56574 | -49.14664 | 2025-07-15 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d1026e88-9304-3dd1-ad61-138c6fcdd384 | -9.02248 | -59.53946 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80193a58-0b36-3202-967b-3a767999538c | -10.96257 | -49.25185 | 2025-07-15 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fba3168c-4c9f-301e-8147-24dc4adc0936 | -10.28063 | -47.61652 | 2025-07-15 05:23:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03937c1b-dad1-3808-bc42-a569b42a757e | -3.22032 | -48.97108 | 2025-07-15 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9afce114-a118-31ff-8203-feb42e6bccbd | -3.38535 | -47.49495 | 2025-07-15 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b2cfe31c-af7a-372e-a95c-9330e128d2e7 | -3.38286 | -47.46522 | 2025-07-15 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7dba1b57-bc52-3b47-bcda-2f9381d6bebb | -10.87683 | -54.06015 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1482402-2df1-3a69-b203-ee45d398fd2c | -2.92617 | -48.23854 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b24269cb-a76b-3848-a6d0-3665c8eec544 | -9.3513 | -58.83403 | 2025-07-15 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dab3c3c-b4b1-3f9d-870b-002a851b95cd | -10.86732 | -54.05845 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73e2fc46-ecf8-3e3c-8166-ed21bb225313 | -9.30111 | -63.72814 | 2025-07-15 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42c176b8-8906-392b-99ba-8837fb8742f9 | -8.69298 | -64.11912 | 2025-07-15 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b807829f-298c-3b92-8d0b-1bf38816d200 | -10.05768 | -59.11221 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72855b84-d122-3f37-8bf8-ccd44726e122 | -4.68413 | -48.8693 | 2025-07-15 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5638ea28-4c34-3fca-a9dd-2dced0c543e5 | -7.40204 | -72.59306 | 2025-07-15 05:23:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8627883f-7631-3807-ac62-4799a50af574 | -10.56709 | -49.13507 | 2025-07-15 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 28511cfc-ef50-36b0-8012-9b680c78ea4d | -3.21605 | -48.97097 | 2025-07-15 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6612598f-a8c5-371d-9972-820b0b86095b | -2.91503 | -48.24485 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a66e00fe-3bfd-304f-bf06-a96a399f6e22 | -10.87211 | -54.05911 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8232a0f8-ade9-34f9-acb9-12b231efab9f | -10.88315 | -54.04977 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2bb9374-8a96-3460-a091-9488018ce7ca | -9.667 | -63.44276 | 2025-07-15 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c4e1958-8465-3656-be88-ee8482bfc8a9 | -8.61004 | -47.43732 | 2025-07-15 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7e91064-3662-3c78-afef-5782057b1dd3 | -10.05885 | -59.10445 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea7f991b-67fa-33ae-a82e-45e98703fe01 | -9.01852 | -59.54263 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05d3ce71-aaa9-3958-a999-f17c08f68077 | -10.57228 | -49.14789 | 2025-07-15 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| b634b1a4-d23c-3cd5-b6d0-700993948bde | -9.62339 | -49.02201 | 2025-07-15 05:23:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e18533b4-24f9-3076-a093-2ef260f8a1b3 | -4.01312 | -49.47001 | 2025-07-15 05:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0c1851b-c985-3b3c-89dd-39eea629e251 | -4.26913 | -48.18325 | 2025-07-15 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fac5cc01-be84-325a-b42d-e155968be22d | -8.38344 | -51.0729 | 2025-07-15 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df3967bf-de7f-37ac-8195-8543753cbdbe | -9.01758 | -59.54304 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0821d44a-bad8-3252-b4fb-1e21686be2de | -9.61683 | -49.02126 | 2025-07-15 05:23:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
