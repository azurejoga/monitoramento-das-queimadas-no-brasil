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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36995355-8e96-39b8-8315-c1fae0939e3c | -21.30454 | -47.60789 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8179c10e-e32e-3e8f-88a7-3195f91fbff2 | -21.30389 | -47.61469 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94f14fc2-3134-3f7a-acd1-8e6eda431da1 | -21.30321 | -47.62178 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac3f9264-cec7-377f-8175-c07dba73d99f | -21.3029 | -47.62502 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23bcf90a-deae-320b-86c0-6d051aca92a6 | -21.29903 | -47.6078 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f7e0f71-bc2d-3610-bafb-116d813a3abe | -21.29872 | -47.6111 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3532f774-e889-3373-87e6-0c8c8dfaaf0c | -21.29809 | -47.61765 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33fda35e-073e-3077-9862-6a3aa8f86db7 | -21.29778 | -47.62088 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57e8175f-e46b-3b17-90db-f0875726f08d | -21.29747 | -47.62417 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4579ee6d-59d1-37d9-bb38-3cf61860bdc8 | -21.2926 | -47.61739 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efa7d86c-e3ab-3adb-a2a5-e1218aabb25a | -21.29229 | -47.62061 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1c1aa4a-310a-3548-b9d9-846c283b8e43 | -20.80446 | -49.25199 | 2024-10-04 04:59:00 | NOAA-20 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f0e25e6b-304d-38cb-9600-ef9fb09e0dab | -20.63327 | -48.75615 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0731f4a5-f38d-367d-bd68-ccfc785e8aff | -21.57362 | -48.48673 | 2024-10-04 04:59:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d08f3595-a247-3f2c-935a-bfe32cd6a9cc | -21.80774 | -48.75723 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d8d8304-516c-34b0-866d-1cc6d9fe981c | -21.80742 | -48.76049 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3ad3c99-71d7-3032-ae60-d4be8bf6f798 | -21.80462 | -48.75988 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60934cf5-eae9-3a26-a2e5-4506cafb7a92 | -21.80426 | -48.76316 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7281335-6c5f-329d-b699-34d37aff2f72 | -21.8022 | -48.78255 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39c4c63f-c61a-32d2-a8ab-e50c0b759a70 | -21.80006 | -48.78269 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf0fdf9c-cd10-39a1-b0a5-6bef51e085a3 | -21.79677 | -48.78506 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42ec7362-4ab4-33b5-8c56-18bc0fbb7559 | -21.79497 | -48.78206 | 2024-10-04 04:59:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfe046dc-3637-37f1-8c34-1e960e63596a | -21.39514 | -48.88544 | 2024-10-04 04:59:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15a87b8e-121b-3492-bd93-76504158eb29 | -21.39482 | -48.8886 | 2024-10-04 04:59:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fcf2b65-e8df-37c6-9108-eb5d273d97a7 | -21.35027 | -48.88323 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02ffbcba-f706-3931-a23a-ee1d4736aa46 | -21.34994 | -48.88625 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc79a5eb-7771-3843-b8a8-792c38ce5ece | -21.34521 | -48.88277 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 66cefdd1-fb57-312d-b5a6-464efa199274 | -21.3449 | -48.88577 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c2cab26-dcea-3e7b-af97-23baebd109cf | -21.33986 | -48.88523 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80478fc4-c36f-3c52-8ac8-277752f16bf4 | -21.33774 | -48.80906 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c37a582-45e4-3b46-b129-b3d992a66561 | -21.333 | -48.80542 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 73ea29e9-2917-3f80-8a41-ff03ef02a404 | -21.33267 | -48.80855 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 10cb6d3e-2f66-3087-868b-43fb55c61dd9 | -21.33234 | -48.8117 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c697ef3f-99da-3c2f-9cce-ab43d6122afb | -21.33178 | -48.8653 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c81f46e6-3817-3320-86ca-9fdd432d2099 | -21.33144 | -48.8685 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 698713c6-5e93-3974-be2f-36a27ab7fedc | -21.33076 | -48.87488 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5f8a6c6-654b-3f5a-b43f-097ce8b8ddca | -21.32761 | -48.80804 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5f2b3e4a-79cb-3932-a4cc-b597622bc7be | -21.32728 | -48.81116 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 22c36d7a-6b02-3085-a0a3-017a118cf2be | -21.32506 | -48.88054 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aa7cf06-f4ad-3a16-a20d-6a21d474be52 | -21.32475 | -48.88355 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 238b7dd5-9c87-3efe-99a2-0037181223f3 | -21.32171 | -48.86403 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59090248-6153-3c8f-b955-804293d503a6 | -21.31667 | -48.86346 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 368b2239-f01a-3221-8a18-ee49ae382551 | -21.31469 | -48.88229 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29c5acb0-a706-34f7-a4da-1c4b1910334b | -21.31437 | -48.88527 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5eb8faeb-44e2-3b3c-901f-bbd491e102eb | -21.31375 | -48.89122 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f27ac31-9953-30fd-bf2e-58af1a96359d | -21.31097 | -48.86911 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cbc4ee9-fd7f-3859-947c-74b7055cb3fe | -21.31065 | -48.87226 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dcebe55-e531-3e1a-896e-c9bcfe12ceba | -21.30966 | -48.88164 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b930030d-5862-362a-9cea-d29a42b24b74 | -21.30935 | -48.88461 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71a92602-73cf-34b9-a464-a77bf8c217f2 | -21.30904 | -48.88758 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 491b0ec6-81f9-308d-b354-3c74ca8dce4f | -21.30872 | -48.89059 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb28ae00-6e39-3e2a-a051-48f222997641 | -21.30369 | -48.89 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c33e9cba-2847-32a2-85f7-6df8cda756c6 | -21.29897 | -48.88647 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d798c60-ab35-3b34-b30b-932236639982 | -21.29865 | -48.88955 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21e716a3-5e18-3263-8084-ff2537a0db60 | -21.29832 | -48.89268 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13f78876-bd31-3c25-b2a7-a804b8837971 | -21.29393 | -48.88597 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc0b1b55-db87-3d57-983c-97c61614b1eb | -21.2936 | -48.88907 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac4bcda7-aba8-3caf-b124-9a5174511e08 | -21.29328 | -48.8922 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5a866c28-bdb3-3d9a-8335-c043d445a6e0 | -22.37754 | -49.04046 | 2024-10-04 04:59:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf3f5df-7172-367d-8c92-2a733bf5bc2e | -22.37722 | -49.04355 | 2024-10-04 04:59:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41e316a7-fe3e-3f90-b63a-cda0d176e1e2 | -22.37218 | -49.04287 | 2024-10-04 04:59:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 701a4b18-9a66-3cba-a5b2-89d2d200eba6 | -22.37187 | -49.04593 | 2024-10-04 04:59:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fc24433-0bd9-307c-9c18-697247c684e8 | -22.37155 | -49.04898 | 2024-10-04 04:59:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a20243e1-c702-3a80-8af0-b4a62999fa22 | -22.34761 | -49.23096 | 2024-10-04 04:59:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8f70578-815c-3bb6-8d8c-d075d9435ed8 | -22.28782 | -49.79559 | 2024-10-04 04:59:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64b460f3-00d1-3447-a31a-809ec9538515 | -22.23457 | -49.70696 | 2024-10-04 04:59:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 5a377e13-383f-3438-8642-a535232488f4 | -22.23418 | -49.70309 | 2024-10-04 04:59:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0c9be99a-b9e5-3160-89f3-9d7f441b872f | -22.2336 | -49.7087 | 2024-10-04 04:59:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ce086452-137a-300e-a1d7-ff888a2da696 | -21.35831 | -48.89677 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12614296-7b8e-3b85-8731-2254754e341c | -21.354 | -48.89585 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5e8d7df4-743c-3c6a-b8a9-f6292888b5c9 | -21.35368 | -48.89885 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd7abb05-4531-3e7b-acb1-9b0f4a259852 | -21.35336 | -48.90184 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8016d6e1-cb20-3ff0-a354-44c7b7e449c2 | -21.35327 | -48.89627 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9950418-e27c-327c-93a5-c24cc164bf4c | -21.35297 | -48.89928 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cc0f1fa-b7ab-3bf1-80f7-005a92aa8e5b | -21.35267 | -48.90229 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4aec3069-33b2-39a9-a991-15c02068791c | -21.34831 | -48.90137 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e794426d-e5ee-30aa-b820-344e4de99988 | -21.34798 | -48.90445 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 24d5f98a-a064-37b0-8712-1afb1b32e286 | -21.3436 | -48.89782 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82c7d81b-3e8a-3f19-ac0e-a4fade71dc38 | -21.34327 | -48.90092 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b20b5b8-8ea7-3fca-8976-78a7f769cfa5 | -21.33823 | -48.90047 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd4f2473-94bb-38a1-8d73-ce24586208f8 | -21.3379 | -48.90353 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6cb4db14-b273-3374-b8f5-226ae3feb447 | -21.33208 | -48.91033 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14c53da9-6ca9-32a7-9f85-bd1f9267c351 | -21.32707 | -48.90967 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d37654-8557-31c2-a71e-0db3b634ec0e | -21.31701 | -48.90849 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bffa6e0-998d-3ca0-9234-a09722081cf3 | -21.31279 | -48.90026 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d58505bf-25b0-379b-bcbd-703a806f4787 | -21.31247 | -48.90334 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d52b962-5b4a-391c-b906-4e71a865d4d0 | -21.31198 | -48.90801 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c766049-7edf-3ab5-bde7-c77f4cfa2f8b | -21.30808 | -48.89668 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6144bd58-0f52-3a55-bb55-239b3466cc6f | -21.30743 | -48.90294 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fde7ce20-cc8c-377d-a41e-d7ab0d77d291 | -21.30694 | -48.90757 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dea25d2-767a-3d0c-be6e-acd596a31fd4 | -21.3019 | -48.90707 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3a8bc9ac-44ea-3238-bdf0-a935635f70ad | -21.30128 | -48.91305 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9ad68196-66f1-342c-b22a-50512e94a4fd | -21.29767 | -48.89889 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10b7db07-df17-36cd-9a7c-8eef28ae1bc2 | -21.29688 | -48.90648 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e7de9a31-75e7-3cf2-90fd-37f627752dbe | -21.29626 | -48.91241 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9f3f5465-4278-36dd-bf75-9499b39e95c6 | -21.29564 | -48.91831 | 2024-10-04 04:59:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 041cb7da-e549-312e-934a-56c61d5b9ccb | -21.29296 | -48.89532 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3c31e365-d0f8-32bd-92c0-d6025f2aa42c | -21.29264 | -48.89837 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 115eea01-a0cc-3f23-be13-42ead67ada7d | -21.29233 | -48.90137 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 52a07d9c-413e-320e-ad5d-7b096f9a5568 | -19.65673 | -56.46803 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |


[Clique aqui para ver as próximas entradas](README173.md)
