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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37de0c37-4fd1-34fb-99c6-47a6728b60ca | -13.06807 | -46.33499 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08c4c890-ce8b-3408-98eb-242a88e3539e | -13.06992 | -46.31651 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c37bebcb-9fe0-3785-863b-dd64d0e72d94 | -8.69009 | -47.20433 | 2025-08-27 03:38:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cda9096d-ee8b-3101-baf9-b14cf2775b01 | -10.31622 | -46.76619 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26dd4e79-8bfe-3cf9-a61e-8b8e56a327c8 | -13.50864 | -46.86648 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bd3769d-352a-36a7-8974-ef05a69ea9af | -12.7493 | -48.07588 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b6d529a8-5f00-3528-a218-89bd739ed310 | -13.50629 | -46.8839 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d20a12f3-9ea2-3b69-9915-e2d27cc2df13 | -11.74932 | -49.08462 | 2025-08-27 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9247fcd-5611-32f0-b831-d31e034affb1 | -11.82026 | -46.7944 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef139580-9307-3062-99bf-86ee240670aa | -9.94956 | -46.37539 | 2025-08-27 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d9ec5db-c121-3b7f-9824-a6a277f41737 | -11.91889 | -46.74613 | 2025-08-27 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09740b54-c662-34e4-8418-ec2802bab1bf | -15.79439 | -41.47205 | 2025-08-27 03:38:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b0b1f2bd-bc23-3ad5-b64d-73c8b2448b1d | -14.12893 | -45.41017 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80e249cd-d013-3cc4-ac0d-37d52ea0c2d1 | -13.49742 | -46.86613 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e980388-20e7-3b61-a29f-3e564dfb82a3 | -13.17483 | -45.29558 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 09b78697-0c8e-361c-9494-a8ebf3ea889e | -11.24555 | -44.98794 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a697e429-abcc-360a-8b6b-2f8775bf6c49 | -11.15319 | -44.78383 | 2025-08-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e627230-a33c-3c32-882c-8cf3b538a786 | -13.06897 | -46.33042 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d401279e-d039-3743-8b35-029bf83d5268 | -8.25716 | -45.11998 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 533cd8fe-e416-3ade-a6c3-e507d6500144 | -11.7693 | -48.98826 | 2025-08-27 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 576ed56b-9b5b-3d27-b478-08b307c10bb9 | -13.18157 | -44.04094 | 2025-08-27 03:38:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0f0f9e4-3409-3832-ad0e-2f6e9804c590 | -11.15247 | -44.7876 | 2025-08-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f83bdeca-b652-3d78-ac6f-48001489ceae | -8.29722 | -46.33165 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0549fd60-b96d-3eae-b12e-bbf331e03bd2 | -13.53456 | -46.89933 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27e8a6a8-faa7-3af0-be8e-4158f454452d | -13.50273 | -46.86462 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cc8f54d-69bd-34e0-95d7-53a4707d9c77 | -11.10773 | -44.75242 | 2025-08-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 619bbcae-e123-39ba-9e63-5d6baf8de80d | -12.90506 | -44.66313 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 997b2403-f0e6-3c6c-b5ca-a4ed058d82f0 | -11.74638 | -49.08362 | 2025-08-27 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 211cb705-8505-34cc-9db8-e4a84e21c80a | -12.57255 | -43.78926 | 2025-08-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35385774-bdd7-31e8-9ec4-fbea53b48d50 | -13.07098 | -46.3114 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6e1101c-f832-3dc6-bd68-94c6ff5c17d4 | -13.51232 | -46.88515 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e73666b-b2ba-3bda-bd7f-5a85bcda9e27 | -13.06898 | -46.3211 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d5c7b5c-4ac5-30fd-a19d-f7e403feebc9 | -12.74824 | -48.08091 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dac949d0-73db-3221-b7e7-11c07a590e0e | -10.31823 | -46.78923 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be5a892d-c6cf-3a49-b7f4-9a32d1c249a2 | -14.12335 | -45.40532 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8423045-9c80-3b5b-ae92-63704b53c518 | -9.30337 | -48.2788 | 2025-08-27 03:38:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81c35ea0-b94f-3ac3-b081-929998a352d8 | -12.76022 | -48.18762 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 453f7d81-89ba-3658-ab0b-d763f218714b | -10.77274 | -46.38042 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a9fcbd6-4372-3f73-8422-0a088d4bbd74 | -9.0144 | -40.33974 | 2025-08-27 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9805313-f3cd-3509-8087-d327a212df2c | -10.12088 | -47.43486 | 2025-08-27 03:38:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd98d00e-e182-3de3-94d8-b8b7cf55be05 | -8.25804 | -45.1153 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 908383dc-d8bc-3192-815a-c9a24480a3f5 | -14.12966 | -45.40655 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cf7bea3-3f9a-3a06-b479-71282188c066 | -13.18473 | -44.04126 | 2025-08-27 03:38:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 734e850b-8504-3b28-837f-5a48cfc5b188 | -10.78569 | -46.37947 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece8ca33-dec3-32dd-a9af-60dd5116e9f9 | -12.76681 | -48.1772 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 09ce6d42-b36e-3f24-8a5c-9ae3111c443a | -9.19818 | -46.74102 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fdb8a9ab-733f-3897-85c1-44a816cb0772 | -12.74449 | -48.19697 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 72b3f438-e240-39ea-91f8-eccaafe0a055 | -9.31468 | -40.21313 | 2025-08-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 9f07df0c-c29e-330a-9a63-15af8881543f | -8.48245 | -43.65437 | 2025-08-27 03:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49c0889e-dbd8-3b1e-83ee-976c8cd01400 | -11.32636 | -43.29355 | 2025-08-27 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de631316-3e18-3c89-a2f3-affee2c99489 | -9.49965 | -40.32615 | 2025-08-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c48e47da-5f40-3b8f-85b9-ab4073b50337 | -13.17007 | -45.29078 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 76a213c9-91ce-36f0-8eea-97a3801ca4ac | -13.17657 | -45.28841 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 809b22d1-f7ba-36ba-b38b-564e8302ee11 | -13.17558 | -45.29184 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 23bcb145-0341-3a92-a489-342f05555726 | -11.82864 | -46.81664 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ebb24fc-a6df-3e2a-a984-7ea4a99606a2 | -13.17585 | -45.29214 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aaa9e7c5-762a-3a43-9a25-c62230adfc80 | -12.76375 | -48.19141 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 05fc8167-2ae1-3838-9691-044719565b38 | -13.39802 | -46.88429 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47d234e0-a5af-3e6b-a8e7-44f4e1357110 | -11.45801 | -47.31792 | 2025-08-27 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ab5e91a-a7bf-3b59-9152-bae220e59ed9 | -13.51084 | -46.88676 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64391af5-3c89-3780-a8c7-7045d6f7214a | -13.65204 | -45.70602 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa43f18-9437-3381-b1a3-4b4e4b543def | -13.64159 | -45.70008 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 963627f9-74ae-3c71-85ac-4ffe8cf00e2e | -13.50653 | -46.87697 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5bd70de1-7e39-3e8c-ab0b-aca9865e0d81 | -8.29582 | -46.3299 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c14125bf-656e-3002-bf0e-6382bff86603 | -12.76523 | -48.18455 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eaf7d4df-3bf5-3b32-9f94-81dd1bb201de | -15.78941 | -43.34623 | 2025-08-27 03:38:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 178d23f3-1e5d-3ab1-9795-9aed9d08f00a | -13.46423 | -46.99427 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ddb43642-a3d1-3f71-9334-88cdb25c933c | -13.18662 | -44.04206 | 2025-08-27 03:38:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89953aaf-4333-37d7-9701-f847a40ce04b | -9.17335 | -40.59776 | 2025-08-27 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 92b20935-6661-30b8-a13c-bdc65a90ec6f | -13.07171 | -46.31661 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| be2849ec-5118-398a-b5e9-5821789666b3 | -12.75477 | -48.08241 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| adf604d4-d94f-3096-bee8-f10fd57c591d | -8.45777 | -43.66794 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e29e6e11-f158-3fc2-a3dd-f6b4135a37f5 | -8.27509 | -45.12251 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec2c89f9-7469-3f08-b9a1-184577d9369d | -13.62648 | -48.19793 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99553f06-a261-3242-b7b5-a6eb617c7ccd | -12.68333 | -44.40699 | 2025-08-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96326df4-815b-344c-88c9-09deb3d64e50 | -9.31113 | -40.20847 | 2025-08-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8389992-a47c-3c3b-b91d-2ed10e3b5693 | -13.63797 | -45.70014 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25fecb34-2259-3606-bdb5-50f239555d9b | -11.1361 | -46.3413 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 572b73c0-e109-3d6e-88af-8b7144393288 | -10.77961 | -46.38177 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbd56a97-af3b-3c5e-97f9-5d8392234914 | -13.53944 | -46.90619 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b6f9def-6c37-3239-93e5-fefce9ca0403 | -10.78259 | -47.06054 | 2025-08-27 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e541af3-5e4a-3e0e-aa2e-1314666eed4c | -10.78145 | -47.05893 | 2025-08-27 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0de42325-f791-3423-b996-4e3900520e62 | -11.07952 | -44.7839 | 2025-08-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd96ea18-e22f-3785-a2e0-d11f080b2245 | -13.5033 | -46.86809 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af35ae73-8efb-3534-b107-49f1150a0cce | -11.82145 | -46.82032 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86dee7bf-086d-335d-bbf7-22abeb441580 | -8.26314 | -45.12078 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cea71707-cb11-330e-9315-13ea405010bb | -8.45588 | -43.67838 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af4ae912-efa8-3c35-ab94-24ba5478206f | -11.13701 | -46.33656 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9664323d-cc14-39ab-9872-7ca643ffb1bb | -14.76463 | -47.92718 | 2025-08-27 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ed5cf43-ace1-33dd-a9c0-6ee6b45a3411 | -13.42066 | -46.86623 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4ef26cd-692a-36a2-844d-6fd27806bb80 | -11.8153 | -46.81887 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13d052f9-74fa-3914-bfad-882ef92fa7bf | -13.62418 | -48.20855 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 324dc745-81c9-3cc7-9a5e-c6be8fa038fa | -13.07394 | -46.32677 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 624e1167-e9d7-39d8-9df9-fa2af270c5c4 | -13.06306 | -46.32939 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b5fb5bc-4de5-3cd9-8ef7-e8c0668c067a | -9.31534 | -40.20919 | 2025-08-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 4926bc4e-7eb7-3213-83cc-c124e64b34f2 | -14.12809 | -45.41008 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c7cd51e-73a7-3b56-b444-ed3f4d99cfe8 | -13.43201 | -46.99518 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 430c9471-5f03-31d5-b122-09e1f5a5d426 | -8.4584 | -43.66446 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad709008-58d7-30b7-9ebd-699816ffc215 | -8.90098 | -47.32878 | 2025-08-27 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 818f3745-8b02-3522-923f-c4ddde2da7f1 | -7.88745 | -45.87045 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README21.md)
