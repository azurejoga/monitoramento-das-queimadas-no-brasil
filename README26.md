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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93f2af62-7e89-3202-a48c-ccc883951ba5 | -17.1048 | -48.99377 | 2025-09-08 03:42:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7a9d975-e6a7-388d-8072-aeea27e63b80 | -16.90976 | -45.82737 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e2e4a0f-503f-31be-8eb8-b9bad48865b2 | -16.91279 | -45.83987 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34e87391-947c-3e94-ab36-20e6e6644f5e | -18.02645 | -47.12317 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 99598345-3f88-3fd7-9cf4-51a15dbd13da | -17.83971 | -44.24652 | 2025-09-08 03:42:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce7d24be-76c8-3d8e-b945-4f775e15e919 | -18.96062 | -46.79499 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ed5ffd4-1001-3014-9999-16fe4545bf34 | -16.93649 | -45.78088 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b8f9cb6-fa7e-38e0-aebc-056dc410aef2 | -18.03033 | -47.10659 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28c207b5-ba2a-3306-9404-a26c55462ade | -17.59155 | -44.53431 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd416591-0ce1-3ee5-8aa1-4c6651c8e871 | -17.64448 | -44.78385 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f76433e-0b2f-3a47-af45-ba66372b3329 | -17.65353 | -44.18287 | 2025-09-08 03:42:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 947fbec5-48dc-3dc8-b07d-9ebdd0552320 | -18.35678 | -43.92384 | 2025-09-08 03:42:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a976b96-3825-3da2-8deb-25345c79e1e0 | -16.54069 | -45.10631 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09fece99-2112-30af-b3e5-e84bf17328d3 | -19.86837 | -46.14908 | 2025-09-08 03:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 178f5a5a-e544-3cdd-a914-508ee0ee86bb | -18.1429 | -43.39971 | 2025-09-08 03:42:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c77cf4c8-d186-397a-a7b8-53bf0968d916 | -19.51888 | -47.88414 | 2025-09-08 03:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af2fd0dc-1355-32a3-ba93-d163ce20050b | -19.36391 | -44.51134 | 2025-09-08 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4397fc39-1ad5-3a09-a2d1-9c593dd23fd9 | -17.61927 | -44.83131 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0b02d11-6714-356f-a974-1c7ab2005290 | -17.24244 | -46.69419 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1532fc4e-ae57-3d5b-8f58-87fb9590026d | -18.24799 | -46.63407 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10ae3400-acaa-3e98-a66a-8020cccdd7ae | -18.0246 | -47.10376 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c96d624-f11a-32ab-9b46-1bfc26766d25 | -17.24083 | -46.6951 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6afef77-3cc1-3dde-be4f-2c6d05c7d33b | -16.93571 | -45.78459 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a633b2fe-5bcb-33dc-8e84-7f6053106236 | -21.74527 | -46.56401 | 2025-09-08 03:42:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 06356cd4-6431-30d7-959f-8f9bca98d559 | -16.89409 | -45.76394 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a1cef00-3ca6-3f9e-823b-f2d605100c4f | -17.59134 | -44.53376 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34311e39-318e-3b64-aa04-8fff2b72b316 | -16.53164 | -45.09739 | 2025-09-08 03:42:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1412fa0-37eb-3253-a004-8dc0299d9f58 | -16.90841 | -45.83203 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdd5f67e-9d0a-3b49-9fcb-3bdec9efed20 | -18.95571 | -46.79768 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed03feac-0a45-3187-8634-4dc83ef35921 | -19.45364 | -47.88454 | 2025-09-08 03:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d4524dc-4fc8-3300-b3af-80e9f381632c | -18.95979 | -47.34017 | 2025-09-08 03:42:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d0de469-491b-3694-9c3d-e779fe5a689e | -17.44281 | -50.22879 | 2025-09-08 03:42:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f868cfe3-9391-353e-ac9f-4ce76c083f02 | -17.91767 | -42.61342 | 2025-09-08 03:42:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84b366c5-1244-3079-898b-9aa9b3d2d2eb | -17.9934 | -42.59635 | 2025-09-08 03:42:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 104128e5-0986-387a-95fa-774e44749b60 | -19.87269 | -46.14958 | 2025-09-08 03:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38ff9285-2034-3b48-8f1e-23e2a36d4955 | -19.92269 | -46.1716 | 2025-09-08 03:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 187e9ba4-0bf3-3ea2-b65f-c5cbd903dcc6 | -17.23517 | -46.6937 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2df186e7-b6ae-3634-9f9f-2ce7d10f753c | -15.96751 | -48.11206 | 2025-09-08 03:42:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22117932-f869-3073-b6b9-2c336495c0fd | -16.54976 | -45.11514 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d49f3572-9b06-3a15-b609-4b445bb97a05 | -17.6433 | -44.78978 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79fd2e4b-c3ed-3132-b5df-1876fd54501e | -19.53536 | -47.89277 | 2025-09-08 03:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e71f7855-980c-3264-be13-36b8bb7136a1 | -16.91282 | -45.81041 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db74f740-20ac-33fe-9924-896934877628 | -16.89439 | -45.79304 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2bd9165-3554-3abe-a719-ff5ceb298202 | -16.89435 | -45.79016 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51140a93-30ed-3d15-b0a5-902f5e3e89e8 | -16.89518 | -45.78934 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da3929c4-1718-3d23-bcc1-bad2aad93210 | -16.28766 | -49.55247 | 2025-09-08 03:42:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5aee690d-f14c-39cf-a1f9-39b35c73e24f | -18.14229 | -43.40134 | 2025-09-08 03:42:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d20ab920-e6fb-3a02-9e37-c2b3cbd43502 | -18.02889 | -47.1118 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ac7e8cf-6fff-354f-b17b-4543b341d707 | -18.0221 | -47.11657 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f7c9b2d-322a-394b-a055-aec259fc9a40 | -19.38039 | -44.50355 | 2025-09-08 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ee80481-8bd8-36fe-8b6f-bae850b633db | -18.35767 | -43.92564 | 2025-09-08 03:42:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eff6854f-744a-39a0-83fe-2263513f3864 | -16.90046 | -45.76446 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac10159c-517d-3816-b05a-9dd058166fcc | -20.90663 | -44.24983 | 2025-09-08 03:42:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5919d2c6-c89f-3103-b521-4232ed0c1718 | -16.90991 | -45.82468 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1359f35-6f24-3bcd-935d-8e8a61f315e9 | -18.10828 | -44.50399 | 2025-09-08 03:42:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e532ad8d-0745-32e1-a84d-f125764c51d7 | -18.96192 | -46.79575 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38b9ac5a-9393-336a-962e-efb2b5ee895b | -20.92863 | -45.26953 | 2025-09-08 03:42:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 58e400d9-d03b-3d37-88ea-e9186b0e10c7 | -18.56727 | -43.61584 | 2025-09-08 03:42:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b21e65c6-e24b-319f-b5db-ac29e9672da3 | -17.95889 | -42.77381 | 2025-09-08 03:42:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ef7dafc-ce9c-36e5-a54e-420978f518e1 | -17.61864 | -44.83442 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a81aab3-9856-3347-b828-df573d89cb20 | -16.29453 | -49.55376 | 2025-09-08 03:42:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 079b3086-1057-3a04-a835-c193c359a044 | -19.20978 | -43.73372 | 2025-09-08 03:42:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b477f526-8ca8-3f2d-b2ee-3a247fda3a70 | -18.03966 | -47.09156 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a1df804-92b0-3650-aff8-778bc12ea6dc | -19.39825 | -44.51336 | 2025-09-08 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4444b2a-78bd-312d-a8d9-efd547fb486e | -21.22162 | -44.02219 | 2025-09-08 03:42:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9721b239-1b31-3d79-b1df-9a21904a9993 | -18.02383 | -47.10737 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9473d374-1b6c-356b-8df1-f6e56a5b4bad | -18.02439 | -47.10623 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf994ea1-027a-3c84-bf4a-6639f159dad6 | -21.64329 | -45.3684 | 2025-09-08 03:42:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 331c9b13-12c4-323c-8827-cc2c2eaba0d7 | -19.52954 | -47.89136 | 2025-09-08 03:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4074b7c6-5038-367e-9364-457148c2c7af | -18.95924 | -47.3423 | 2025-09-08 03:42:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c45331f-efc6-3ff7-9238-ef5dd4cf7c99 | -17.16362 | -49.02948 | 2025-09-08 03:42:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d6a56ce-b131-31c9-b725-337de615ae7a | -17.66703 | -44.19048 | 2025-09-08 03:42:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d501f699-5ab0-3c2e-b600-fbed941295b5 | -16.89947 | -45.76519 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb2329e6-0108-38bb-8500-74d57218f9ea | -18.40687 | -43.89864 | 2025-09-08 03:42:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 257a520b-cd9a-34c0-9367-c518aaac63be | -19.62334 | -43.95789 | 2025-09-08 03:42:00 | NPP-375D | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58308ab8-a906-3303-8992-b43245aca36a | -18.03969 | -47.08934 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23d2fe51-ccee-3e0c-bccc-156aa60d9baf | -17.53992 | -43.74071 | 2025-09-08 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7e83dfe0-d94d-3c09-9e71-e1f2e29a71cd | -16.93725 | -45.77725 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d40eec4-927a-39ac-beea-6b5fce48f809 | -16.53752 | -45.09526 | 2025-09-08 03:42:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d8e27e0-e067-3ade-a7d0-31f2113202d4 | -18.96071 | -47.33601 | 2025-09-08 03:42:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b05c605b-9409-3b5e-9f49-4d29e96fbe0d | -16.28846 | -49.55038 | 2025-09-08 03:42:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0319f213-9a39-333d-8ce7-d86703dee314 | -17.26354 | -46.70008 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3b13bf7-ddb2-3f21-8491-28e388b163a4 | -18.4317 | -48.79018 | 2025-09-08 03:42:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5ee600b2-7d1a-3cda-8b4f-2903c6e2fd4f | -21.22065 | -44.027 | 2025-09-08 03:42:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9752d11-1eb8-3a3c-be5f-d2d769499524 | -19.64074 | -46.58056 | 2025-09-08 03:42:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 30489c37-0082-3508-91cd-061821e1aa5e | -19.5305 | -47.88706 | 2025-09-08 03:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 782eab4e-c42c-3ff3-aa2a-7b30fd6cd6db | -16.29531 | -49.55175 | 2025-09-08 03:42:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07682e51-8a05-3c22-972b-cad12b6c72aa | -19.69845 | -49.28819 | 2025-09-08 03:42:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bb9dc29-f973-3a1f-9a0e-1fd447b0b73b | -16.55043 | -45.1119 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f0d28ff-adc2-3a66-9d8d-2a1d7f6738a2 | -17.59011 | -44.53997 | 2025-09-08 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62a2dfbc-5e5f-3398-8932-4c7f68a1e645 | -18.24247 | -46.63267 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f07b77a-fd6b-3f41-b3d0-d53017c14bee | -17.53658 | -43.73727 | 2025-09-08 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c979fe5f-ce28-39fe-bcb5-35fadc60a8bb | -16.91356 | -45.80675 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb2d121f-efa3-3335-8c89-aae0508e6de8 | -19.3569 | -44.52131 | 2025-09-08 03:42:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23fe0b8b-2645-36c1-94f0-edfbfc6c2d26 | -18.04451 | -47.09678 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 668ae646-f111-371f-8e38-82af21cfa1a3 | -18.96013 | -47.33816 | 2025-09-08 03:42:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 187b20a3-8d42-3954-9826-bead5357d647 | -16.91196 | -45.84381 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9463544f-05fc-30dc-b099-7ffa86bb143a | -18.04461 | -47.09437 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02ce95b1-a8b8-3526-9ec2-ca019f4276eb | -18.24137 | -46.62171 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 020d5f29-2675-3b66-b5d1-edd7e51d825b | -18.35216 | -43.92265 | 2025-09-08 03:42:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README27.md)
