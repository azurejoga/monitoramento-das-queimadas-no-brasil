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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3860a8f4-4e3a-39e0-a4d0-41649cef5c99 | -20.59424 | -42.02068 | 2024-09-28 03:32:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c83860a5-5c83-3acb-b073-8ec3b540a74e | -20.51477 | -41.96271 | 2024-09-28 03:32:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 26a200fa-2528-3e6d-961e-e6d594fc2d75 | -20.51383 | -41.96747 | 2024-09-28 03:32:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 149cd55e-a1d6-3110-85bf-8cabdff3bfa3 | -20.51196 | -41.9769 | 2024-09-28 03:32:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06fa8034-fa11-3771-99fe-693a03f90b7d | -20.50765 | -41.97558 | 2024-09-28 03:32:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06be1291-f17a-33b9-8043-60b17f16ba25 | -20.50331 | -41.97439 | 2024-09-28 03:32:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 66c73401-a354-3a65-877b-57960e06fd5f | -20.4382 | -42.00702 | 2024-09-28 03:32:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 95b4f3b3-0ca2-3a39-a523-3762a5d7a8bb | -20.4338 | -42.00609 | 2024-09-28 03:32:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7fc9cf75-ea1f-3025-8d51-9c081a75e484 | -20.43014 | -42.00139 | 2024-09-28 03:32:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4ad94ddd-2dfd-35eb-8654-9580e156f051 | -20.30547 | -41.45145 | 2024-09-28 03:32:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9793da92-4d74-3e7e-885f-0f8c4eb15e80 | -20.29087 | -41.43533 | 2024-09-28 03:32:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4e0ece81-bf0a-3e61-a3b4-1ffe06eaaeee | -20.0838 | -41.68164 | 2024-09-28 03:32:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 224da00e-4407-3829-83eb-d00fde251530 | -20.08289 | -41.68618 | 2024-09-28 03:32:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| af0f278d-4f44-32ec-93ef-09ab6c23daec | -20.08266 | -41.68492 | 2024-09-28 03:32:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fc57a7ff-acee-3419-ac5a-629a6c8f09bd | -19.93541 | -41.78834 | 2024-09-28 03:32:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c8d81fc8-7224-33d9-972b-ee0d38ef3a83 | -19.52167 | -41.55512 | 2024-09-28 03:32:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a357b78d-b134-3a17-b05a-42f00da57141 | -22.3048 | -41.88179 | 2024-09-28 03:32:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 711579b4-e9d3-3fbc-95b1-95febf01b4e7 | -21.29543 | -41.9264 | 2024-09-28 03:32:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7937d371-369c-34ad-9ef2-e0e62ae23308 | -21.29354 | -41.93597 | 2024-09-28 03:32:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ccabd248-4cce-3c02-ab32-102a76d52752 | -21.21402 | -42.08528 | 2024-09-28 03:32:00 | NOAA-20 | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34b2bf06-be3d-3670-b7cd-8d28cb96d2f4 | -21.21361 | -42.08681 | 2024-09-28 03:32:00 | NOAA-20 | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3349104d-0a33-3c08-9670-cb851f20081e | -18.824 | -43.18166 | 2024-09-28 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f7d92f83-d4ab-39c8-a6c5-decee7237015 | -18.5204 | -43.02641 | 2024-09-28 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f6fc9ae2-9b0e-3d5f-b750-74d27f3f110c | -18.51855 | -43.02514 | 2024-09-28 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 3aea06d3-d5b0-3ca4-a6ae-2ad2b26b8c40 | -18.51745 | -43.03069 | 2024-09-28 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 3b610793-2ae2-32f6-9421-6231b372ed98 | -18.51546 | -43.02573 | 2024-09-28 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.9 |
| 03676ae9-c498-34a0-b1c8-4bb3a8dcc150 | -18.51362 | -43.02443 | 2024-09-28 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| b0949ebb-5eb9-3058-90e9-cdbc8f092cc9 | -18.49473 | -42.86611 | 2024-09-28 03:32:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| aa280293-3db9-31b9-bfd1-65fe083f1d63 | -18.35863 | -42.75833 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 325cdd1b-6ea9-3863-98be-e138e0755057 | -18.3576 | -42.76357 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b9795f55-8d9d-3a0a-bc70-273e4c8fa35a | -18.35711 | -42.75918 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| bafc5f0d-8466-3e4f-94bd-2d1f8932d57f | -18.35601 | -42.76459 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ffdc2cfe-2d2f-31a8-9dd7-d7686236d382 | -19.4285 | -42.50985 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e08b4f3f-2c61-3316-bcd9-0e7e6aa57cfb | -19.42489 | -42.50376 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0345f3e1-34ee-31b4-bc61-39dfa7cfd196 | -19.42388 | -42.50883 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1530cb8c-4488-359f-b496-3abe9ed2fd3c | -19.40716 | -42.9823 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b73e8b9-ed76-39be-817c-49c67de2a11a | -19.40618 | -42.57269 | 2024-09-28 03:32:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ff26b3d-ee1b-3e71-aeff-d752cb6e1c5d | -19.40156 | -42.57155 | 2024-09-28 03:32:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 641645d3-3fec-3290-8f7a-eac580302258 | -19.40147 | -42.9857 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 738ec760-ecb5-32e7-9116-f66121d8c265 | -19.39774 | -42.98326 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f6c6832d-6fbe-3a2f-bfba-932fe93bb3e5 | -19.3968 | -42.98416 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0a7f54b2-b504-38aa-8694-33a9fbf99512 | -19.39561 | -42.98989 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8a6960c7-9583-3169-b52f-0b54b849bdc3 | -19.39534 | -42.99538 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bdcce335-516e-3659-92ff-b22114f729d2 | -19.39421 | -42.9967 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8f0f0e39-7920-3a87-8be3-ab559dc1255d | -19.39223 | -42.59362 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ea554203-b59d-3e0d-99d5-d4d8ccdbdce7 | -19.39166 | -43.27888 | 2024-09-28 03:32:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 54d6a218-00e9-3e60-9510-716c48fb8ada | -19.39052 | -42.99453 | 2024-09-28 03:32:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ca5786a9-fa2b-3d93-8f7f-37f761e12e63 | -19.3905 | -43.28452 | 2024-09-28 03:32:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 463cc591-a19a-3be5-aee2-400b88ff7a37 | -19.39033 | -42.57903 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 98448577-80a1-3721-b186-4d600ae54540 | -19.38946 | -42.58333 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 13f7f62d-a191-3313-a587-865c67964759 | -19.38767 | -42.59216 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e33ed500-9fb7-310b-b556-ebfd6f6255a2 | -19.3867 | -42.59694 | 2024-09-28 03:32:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1c21c414-57ad-35ae-b05b-da335260305c | -19.38565 | -42.60208 | 2024-09-28 03:32:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 034abb74-8f9e-3647-981d-9a492ff3b6a5 | -19.38112 | -42.60044 | 2024-09-28 03:32:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 21b30cab-e40b-3b95-b808-b81ed789cda0 | -19.37758 | -42.59393 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f019a941-66d4-3f21-9ce3-f376fe51fef3 | -19.37649 | -42.59929 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bf225356-2f62-3a14-b790-b54629e9340c | -19.37565 | -42.59266 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8d5d5fc4-5a8f-3ca7-be1a-65d66f93ea2c | -19.37462 | -42.59793 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f21641a6-fa2e-38ed-9793-ec4049f78da6 | -19.37285 | -42.59327 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 197c7c58-b852-3a9d-aad6-46c0debf62b5 | -19.37177 | -42.59859 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f5508192-421f-3821-87be-8e7e5f05c9a3 | -19.36989 | -42.59729 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6ff257ce-5c8c-37ec-a36d-8b23986bc979 | -19.36823 | -42.56827 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| abf3373f-9ba9-39b4-9b83-be54c41e278e | -19.36731 | -42.57275 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8b217f18-347c-3d30-83e3-bb463ac63643 | -19.36612 | -42.56718 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 7141292a-26bb-3c38-bf74-d4950f0d17ac | -19.36523 | -42.57168 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 75f6f35d-2022-3d1f-b0d3-1e364d08b561 | -19.36513 | -42.5968 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5f213a1c-5423-339d-af3d-3f47e4cd2f9f | -19.36348 | -42.56771 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 2fa67283-c6cc-35e2-8f27-d7b91b2ba6d2 | -19.36328 | -42.5925 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3f83bf7a-3079-3df4-85dc-88f66679a71b | -19.36327 | -42.58161 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a0cfc89-f627-38d3-ae16-d35085832257 | -19.36252 | -42.57241 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 8360d80f-16d2-351d-b718-befda3d6ebaa | -19.36233 | -42.58636 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c4a60ddc-9d45-3cad-9ab2-8ec6a0d7ebcd | -19.36227 | -42.59742 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 10e3d21b-4de1-331e-87dc-11c246f0d595 | -19.3615 | -42.57742 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4ff7ab28-089c-39fc-80a0-d5ac8ea82848 | -19.36141 | -42.56643 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f900d749-1c11-311e-b978-099532260b9b | -19.36053 | -42.58216 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4cf5dcd6-89e7-3dab-880c-86fe55ab1406 | -19.3605 | -42.57103 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 488af34d-95f3-36fc-9aaa-1909b8666360 | -19.36043 | -42.59601 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e1aa67cc-b233-366e-9d75-06ecc8ef9b36 | -19.35954 | -42.57593 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 0acd9c6a-f288-312d-a82d-1812e33024ad | -19.35787 | -42.57141 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 5655107c-579e-3ddd-97d0-afa302b95026 | -19.35585 | -42.57 | 2024-09-28 03:32:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 75f6e1fa-253b-315b-818b-647b09e2fe13 | -19.27581 | -42.7263 | 2024-09-28 03:32:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fdfd0914-b45c-3702-8a71-521d88f90e3c | -18.70319 | -42.08242 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 26853b7b-b649-379a-afc2-fedd264d4479 | -18.70319 | -42.07956 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b919ea0d-3109-3ad9-aad2-bb6132b8f101 | -18.70229 | -42.08403 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 00044781-19ba-3be2-9005-d2e2282f955c | -18.69949 | -42.07699 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 08739722-eaf1-38f8-ae43-02b98ce9aebd | -18.69863 | -42.07856 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c7a8862f-a1ff-31aa-bf95-7acb808c7d1d | -18.69861 | -42.08154 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 51a58e6a-43f5-321d-95a0-cd6deac396a1 | -18.69768 | -42.08326 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0938d0d7-42f8-3b4c-b985-97799ad00a90 | -18.69669 | -42.09145 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 6a73645d-8f4a-35f1-b232-56b143870f71 | -18.69669 | -42.08821 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1b26a9e7-c98d-35ce-b2b6-a70d9d4f6608 | -18.69569 | -42.09661 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 144ae191-27b3-340c-9424-cc39b8075d90 | -18.69567 | -42.09329 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| b6267bf2-0e03-3a2d-bf05-d3f1beac4c99 | -18.69492 | -42.07602 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e1b3dbad-75fd-3cb9-839e-e70638c98512 | -18.69404 | -42.0777 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 7ab9f638-9f6f-3c57-af8b-d6f5bce19f1e | -18.69401 | -42.08071 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c422e6c1-9da3-39bf-b30a-d01a4003b295 | -18.69205 | -42.09085 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0fd59234-de69-3254-8673-cf0d84826ae5 | -18.691 | -42.09276 | 2024-09-28 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 9e3d9e4e-8c84-31a2-b7e1-a17f726ee07d | -18.50437 | -42.22293 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c27d2138-e1a9-3cb4-a580-4c6450b30834 | -18.4941 | -42.22605 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5dd19d1-3374-389e-a551-8c9bf21ffd9d | -18.48689 | -42.21386 | 2024-09-28 03:32:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |


[Clique aqui para ver as próximas entradas](README33.md)
