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
| 7f3dd599-4d6e-315a-849c-2b42299e9208 | -9.3041 | -48.5965 | 2026-05-08 00:16:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0434f445-1def-3551-8915-24256d66032f | -5.7858 | -45.113899 | 2026-05-08 00:16:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fcfaf8d-f365-3047-a14b-019113d8fc86 | -10.0294 | -51.665001 | 2026-05-08 00:16:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3128a452-6504-3909-9fb0-1fe1a80e7815 | -11.1233 | -45.114201 | 2026-05-08 00:16:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c313fdc-b272-3e5d-8a4b-9b2fb96d30b2 | -6.3181 | -44.641998 | 2026-05-08 00:16:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccd21674-5f46-31b3-9fbc-72766a747829 | -21.691999 | -48.399399 | 2026-05-08 00:16:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e0e03ca3-c439-34a4-9916-7111dec59e07 | -5.7778 | -45.123798 | 2026-05-08 00:16:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28663342-fcfc-37ca-95ad-6945275ebc07 | -11.6299 | -47.888901 | 2026-05-08 00:16:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 671525dc-c3b8-3877-8799-f939ff7d56d5 | -8.7033 | -49.081501 | 2026-05-08 00:16:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a77da51a-1877-3268-b98e-7c7928cbe4b2 | -8.6838 | -49.085499 | 2026-05-08 00:16:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae65e6fa-1e8d-3cc5-9c5e-7e9007b23ea5 | -9.4066 | -50.673599 | 2026-05-08 00:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d798065f-2f36-3d7e-b962-4dcbd373c0e7 | -9.4106 | -50.693199 | 2026-05-08 00:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccbf5394-b74f-36a7-b68a-9c1bb8e076c2 | -8.6966 | -49.098301 | 2026-05-08 00:16:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8644dbf-7ace-368b-8234-4f4fbcde23c4 | -9.3109 | -48.580502 | 2026-05-08 00:16:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8666113e-e16f-3800-bc6c-fa7a72f8f50e | -5.7795 | -45.131599 | 2026-05-08 00:16:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed0c2b46-fe56-3e68-8677-5b9387ec0d82 | -9.2885 | -48.570499 | 2026-05-08 00:16:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78464c9c-4221-38e3-9628-c4b07e5cf7c3 | -11.1291 | -45.141399 | 2026-05-08 00:16:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27de2a83-5367-33e9-b261-f9a9bb3a22f4 | -8.6869 | -49.1003 | 2026-05-08 00:16:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1ad0657-93ed-3ae8-9c9d-381f15316d41 | -5.776 | -45.116001 | 2026-05-08 00:16:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0064ddc-d607-35e5-82ba-f01b14b88286 | -11.8114 | -47.332001 | 2026-05-08 00:16:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| febc8d46-bac0-345b-bb03-c7acd2082b5d | -18.080099 | -50.3964 | 2026-05-08 00:16:00 | METOP-C | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d9cbbbb-be81-39e2-bcbb-1c845e3442cc | -21.6954 | -48.420601 | 2026-05-08 00:16:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 127f8c84-794d-3449-96a7-7ca556cfac18 | -11.795 | -47.102699 | 2026-05-08 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 809df887-98aa-369c-b98a-58e7a7819a9e | -5.7876 | -45.1217 | 2026-05-08 00:16:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b3ff071-3561-391c-a21a-c746625ab7da | -13.3546 | -43.087399 | 2026-05-08 00:16:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d75284bd-a2b0-3acd-aea5-5a6e573d79aa | -11.8237 | -47.342602 | 2026-05-08 00:16:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e53ea43e-6ec9-3b1a-b50e-d8ba05eca76c | -6.8949 | -42.857899 | 2026-05-08 00:16:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b2ec4bd-10ea-3ffb-8761-315253bf87de | -9.5609 | -44.5742 | 2026-05-08 00:16:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51a5452f-08d4-3c00-b977-dd1f70905bb1 | -11.8048 | -47.1007 | 2026-05-08 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d75468d8-a190-3fe0-bed4-7747f087f67b | -12.8535 | -43.763302 | 2026-05-08 00:16:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d500e418-7bcd-3409-be93-9f162d8c8b2f | -8.6935 | -49.0835 | 2026-05-08 00:16:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83b3be15-058f-3253-b82c-c5ba0a3adfc5 | -21.375799 | -48.5434 | 2026-05-08 00:16:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ea8cda9-a00e-3ccb-b530-68a58d3bf630 | -9.5626 | -44.582401 | 2026-05-08 00:16:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75b2f75d-882c-3345-a0e3-c44d0ccba71a | -5.78541 | -45.11617 | 2026-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 90798fdc-f85c-3de5-b42b-37a81894edc9 | -5.77639 | -45.13182 | 2026-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 6945c450-3bc0-3c22-a3fa-9efe8e14ba41 | -5.78849 | -45.12448 | 2026-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 0ca250f2-f821-3946-995c-4ebec0b8331e | -5.78744 | -45.13035 | 2026-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| ccb31719-0875-39e8-a0fc-70ebd099523f | -5.77956 | -45.14 | 2026-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fe628c26-5025-38df-8540-549c54fd2b49 | -5.77744 | -45.12596 | 2026-05-08 00:16:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 8337029c-be62-30f5-908d-2aa8d36492ae | -9.4071 | -50.6847 | 2026-05-08 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| eee3708a-61d5-375f-b343-af1f8592e879 | -21.715 | -48.4126 | 2026-05-08 01:00:00 | GOES-19 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7508b313-5159-366b-8429-d0e78e317026 | -20.7192 | -55.160099 | 2026-05-08 01:24:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 21c54c06-b203-3794-b933-d8a611c6d69d | -16.151699 | -58.469101 | 2026-05-08 01:24:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1dd21806-29e1-345c-91f4-3696587fa652 | -16.1555 | -58.4837 | 2026-05-08 01:24:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 309d49eb-b156-3473-a7af-799910418558 | -21.8457 | -50.3402 | 2026-05-08 01:50:00 | GOES-19 | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| cd6d5696-2d24-332f-a6eb-0569038a7ae6 | -21.8451 | -50.3631 | 2026-05-08 01:50:00 | GOES-19 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| f9cf28ec-3a08-39d1-9997-5864befdb1fd | -16.160101 | -58.4921 | 2026-05-08 01:55:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71a0fcef-7b13-3e2f-94ac-f064f3ec08a1 | -21.8531 | -50.346401 | 2026-05-08 01:55:00 | METOP-C | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f3f39ea-ab10-3b6d-9fa8-2789566f4e66 | -8.78769 | -44.83755 | 2026-05-08 03:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4373dfe7-e9ad-3aaf-86d7-35810d7e7a4f | -8.78608 | -44.84574 | 2026-05-08 03:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d99b9eb3-29ee-3f50-9f12-700f56335317 | -14.13 | -45.34351 | 2026-05-08 03:28:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd391404-9560-389f-a242-49d09b288fd1 | -15.6141 | -46.52098 | 2026-05-08 03:28:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e0551087-9b6a-3630-a34b-48442a214295 | -11.94331 | -43.3796 | 2026-05-08 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e91037c-b6c5-3468-87a3-4ceba1ae77a2 | -12.84803 | -43.76368 | 2026-05-08 03:28:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48075242-16ef-3357-9ecb-421d6d09d1de | -14.13665 | -45.34503 | 2026-05-08 03:28:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27b996cf-460a-35ae-b754-de8cb7e3a3c8 | -14.13536 | -45.38313 | 2026-05-08 03:28:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 220397f6-5f39-3e13-a093-26a6c3bd6909 | -15.6156 | -46.51432 | 2026-05-08 03:28:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 493776e5-e75d-307d-97ad-8b7d143cd9ad | -12.85424 | -43.765 | 2026-05-08 03:28:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1baa227b-22b1-3caa-930c-696c23c95a79 | -15.60726 | -46.51903 | 2026-05-08 03:28:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c00f4ae8-f5aa-3c1e-b24f-2e945d4734d0 | -12.85527 | -43.76003 | 2026-05-08 03:28:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7af40e21-7920-3de9-bb9a-ae3e4684dd21 | -11.76703 | -43.65154 | 2026-05-08 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c3f7003-f229-3f33-97b4-a5470c49b42b | -12.86251 | -43.75637 | 2026-05-08 03:28:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cbf0df3-4239-3ae1-8711-ade0cfc097ef | -14.13407 | -45.38911 | 2026-05-08 03:28:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93a72cc8-920a-390f-afb8-e085f15d2e77 | -12.86148 | -43.76134 | 2026-05-08 03:28:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d59b9b45-2905-320b-ac47-44cdd4e81834 | -21.43047 | -47.06519 | 2026-05-08 03:30:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25c05378-3af2-314a-8bc4-6c5b8e865d1a | -20.22058 | -46.8343 | 2026-05-08 03:30:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bdf47c1-c22f-308c-8b64-96f56f1223df | -21.6992 | -48.41539 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5635bfd2-d653-3aba-8a2c-80ef6572d95f | -21.70655 | -48.41588 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 548f6ee6-bcb7-344f-bec7-18508921d4bd | -20.21424 | -46.8361 | 2026-05-08 03:30:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc353b64-2de5-36ff-8a39-fc1eb07ae317 | -20.22215 | -46.82779 | 2026-05-08 03:30:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb3881ad-8aca-3505-928f-5000121650b3 | -21.70497 | -48.42221 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 171b43f2-1907-3d7a-a678-3fc775deb65a | -21.69822 | -48.42014 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77286fe4-17dd-3ed6-8f3f-974b8f0a5c46 | -21.70436 | -48.42369 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cbf9608-3eda-323d-bbcf-5d60c7317492 | -21.69978 | -48.41384 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0efbefb-b584-3dd1-a5a8-e291823afe89 | -21.70597 | -48.41739 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62e7d310-1264-3b23-94f5-6f1aeab07565 | -20.00311 | -44.21407 | 2026-05-08 03:30:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eef83f95-557f-3a73-9344-e18fd6a8aad3 | -20.2223 | -46.83092 | 2026-05-08 03:30:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 209d6480-f9ea-3161-b358-1389414e39a2 | -20.21881 | -46.84158 | 2026-05-08 03:30:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89acbf86-5913-39de-8795-92757c887cd8 | -21.03416 | -48.9458 | 2026-05-08 03:30:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2be68922-3e7d-3abb-a6b8-9dbd408fe276 | -21.42414 | -47.06331 | 2026-05-08 03:30:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45ef8b85-d14c-3652-b893-304f96b68ab1 | -21.6976 | -48.42167 | 2026-05-08 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5f4f292-7145-31b3-a89b-dde99fd9454d | -27.94609 | -51.06702 | 2026-05-08 03:32:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b4215a72-5552-3c8e-9e6b-bbece521846e | -7.33717 | -49.78918 | 2026-05-08 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83c72972-130a-38fc-9a25-d05f460513f7 | -6.66269 | -47.54604 | 2026-05-08 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78c31781-0318-328d-9b31-a8466d735c62 | -5.7308 | -43.23763 | 2026-05-08 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d93534da-30b1-3e96-b77a-d6006704eb88 | -6.25551 | -42.5778 | 2026-05-08 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 365a5bed-74f8-3948-928f-ad125fdddea3 | -6.02412 | -44.22477 | 2026-05-08 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7344b95-114b-3295-aaeb-e4a68ca197d5 | -7.45773 | -43.28801 | 2026-05-08 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f204571e-3235-3191-a55a-dac3bfe90de3 | -7.29168 | -49.62809 | 2026-05-08 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74eaf1a2-7853-3031-a800-cc39213a730c | -6.31249 | -44.63967 | 2026-05-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 835d49f9-be58-3cbc-b731-b719392a99f4 | -6.31985 | -44.63706 | 2026-05-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d92e2215-cb47-39d1-8c66-79b0b9a54273 | -7.34043 | -49.78808 | 2026-05-08 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0d8db29-4e2e-3ace-ae16-1a973daf8967 | -6.32266 | -44.64124 | 2026-05-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7114b685-91c8-30e9-9259-54d34922e1b1 | -5.72749 | -43.23711 | 2026-05-08 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb43ca1f-085e-33df-8644-996640a6e966 | -6.31588 | -44.64019 | 2026-05-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fc69af8-0558-3454-9597-03fa38e2ed3f | -6.89196 | -42.85848 | 2026-05-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 30aeddf7-c7ba-32e2-ab96-d1eaabb05b36 | -6.77198 | -46.82034 | 2026-05-08 04:14:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dca2361b-2a6f-376c-969c-6e4edcc05bd7 | -6.31927 | -44.64071 | 2026-05-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d99bf6d-8611-349d-8945-ad936a7d5719 | -14.17692 | -52.8807 | 2026-05-08 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e42ce996-d1d6-3ac8-8965-f2523fe3f84c | -12.40236 | -46.75936 | 2026-05-08 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
