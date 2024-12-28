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
| b6eac500-5c27-32d1-8f85-957fa1c1a66a | -22.59338 | -54.92507 | 2024-12-28 04:44:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c6076bf7-bc1f-3cb6-82b6-8ef46a1699c8 | -30.46144 | -56.39509 | 2024-12-28 04:46:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 0b6ff1bb-d90b-3c9d-960a-37623fd48e71 | -30.60845 | -53.69293 | 2024-12-28 04:46:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 136143be-6412-38c2-8304-84ff5bc31756 | -2.22406 | -50.45875 | 2024-12-28 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e80fb1c5-3783-3fa4-b4f8-c84a7e0aa621 | -2.62884 | -48.0887 | 2024-12-28 04:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53be2912-0ba4-3d00-a61f-27df1d7d4a27 | -1.641 | -45.86831 | 2024-12-28 04:59:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d26ae285-3ce1-3f3a-a53b-169fdcc563c4 | -1.42726 | -53.70395 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b3e3c62-00bd-3aaf-a608-1a75d22d92a1 | 0.92878 | -50.77991 | 2024-12-28 04:59:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea73af4a-adc4-39df-9553-6357b44cfdd1 | 3.50991 | -60.67551 | 2024-12-28 04:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1efc967b-b2fe-3d9d-b72a-2aeb0d76e224 | -1.71185 | -52.424 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60133dad-13d5-3442-ac59-7f70ba51f038 | 3.50686 | -60.67351 | 2024-12-28 04:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dfa7018-97b9-371e-a154-6207de455bbb | -1.52315 | -53.87261 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86bfe509-9f51-3b6c-89e9-ba8bea614c43 | -1.71074 | -52.40827 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbdf5aa8-dd1b-3c0c-ad84-fc4f126ae6c1 | -1.71303 | -52.4164 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d803f97-bf9c-311e-92eb-74d51957af30 | -1.76171 | -45.84992 | 2024-12-28 04:59:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938e3077-441d-3b7b-b91d-815d2c471285 | -1.71244 | -52.4202 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1fcdb66-35ff-30fe-aad3-9936daf76ee2 | 3.51153 | -60.67279 | 2024-12-28 04:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9472c9f7-636d-37ea-992a-ab7f48299b05 | -0.12204 | -51.52617 | 2024-12-28 04:59:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 282efc83-9d19-306e-bacf-db9a2869b436 | 3.62804 | -60.03822 | 2024-12-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2fa45f6-4634-3b90-b9fb-0f3b18f265da | -2.28746 | -45.59472 | 2024-12-28 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b06d909c-87c9-3923-b4e4-2f00a1d9ecd8 | -2.29046 | -45.57428 | 2024-12-28 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10961b59-196f-31aa-b014-8b4e711019eb | -1.63339 | -52.54741 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f809ebf7-dba5-3cf7-8b23-8573dabf56e0 | -1.70779 | -52.42727 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7c43163-376c-32b2-8aa4-e989c38e12fb | 3.9624 | -60.56397 | 2024-12-28 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282e6b22-629b-305c-8144-2a2261e99940 | 3.51078 | -60.66791 | 2024-12-28 04:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d8d37a6-7531-361d-97c9-66163b0396f4 | 3.25337 | -60.7066 | 2024-12-28 04:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b155c64-e02f-3827-a343-48147e83d90b | -1.64622 | -45.86909 | 2024-12-28 04:59:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb4b8378-4182-379b-a1ae-eea739d291b6 | -1.45704 | -53.55795 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bee08a79-5e6d-3073-a1e4-093b1567ab06 | -2.29097 | -45.57084 | 2024-12-28 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdc99727-2609-3d08-99f5-35db5180b9e2 | -2.28207 | -45.59393 | 2024-12-28 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83f1d827-efdb-35c7-9968-aa72bf8cb867 | -1.70897 | -52.41967 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce0d89d-c165-3282-b1e0-421e877c1e48 | -1.19046 | -53.58845 | 2024-12-28 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cded4c95-0f35-3cd0-94c5-7996562917f5 | 1.62833 | -60.3395 | 2024-12-28 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9720d466-543b-35f5-b88e-7f7a1386de1d | -1.4422 | -53.67405 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d953f6d-1523-31fa-b25e-56ef426a7a0b | 1.63341 | -60.34309 | 2024-12-28 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49f3fb48-37ec-3eb5-a49d-3d3dc3686454 | -1.70956 | -52.41587 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14256fa7-67e8-3743-b247-598ad6070515 | -1.42393 | -53.70343 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d486399c-a289-3311-88d7-936631ebeead | 4.17618 | -60.0811 | 2024-12-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c095d92c-7353-3b3f-ae1d-701ad7b8695a | -1.6328 | -52.55116 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4440e6a-eafe-30e0-b959-e44717b6eded | 3.96168 | -60.55907 | 2024-12-28 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e69d8e7-6290-3eb6-ac1f-787a91490abf | -1.70838 | -52.42347 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cf9ccc6-bf10-394e-9b05-f092f5934a97 | -1.64703 | -53.19492 | 2024-12-28 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40e3e936-c13d-3bad-bfb6-5559aaa83fa6 | -1.25483 | -53.48336 | 2024-12-28 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ab4b793-2409-3d99-8ea7-83c64a3b1b3e | -2.28451 | -45.59507 | 2024-12-28 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7cf20a9-a1f2-3593-a546-8692f313947d | -1.56758 | -53.52483 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 224b87d8-04c0-304f-b70b-15ca05fec776 | 3.5092 | -60.6706 | 2024-12-28 04:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c707e2b0-051c-3114-bf70-ef416232fda2 | -1.15172 | -53.60047 | 2024-12-28 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 619c3a20-e9dd-3513-97b5-9b1477f3e2b9 | -1.64366 | -53.1944 | 2024-12-28 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 215baa96-e02f-3505-8a3f-1e541e6dad1f | -1.55416 | -53.50111 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfaa96a3-ea85-39e5-abbb-e36b688eab8e | -1.65096 | -45.87308 | 2024-12-28 04:59:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 989fa780-45ec-3b7d-8c15-957f6366ae84 | -2.2882 | -45.57124 | 2024-12-28 04:59:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 36320497-12cf-3a49-8d49-e0b54533ac2b | 3.62951 | -60.03536 | 2024-12-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89ac9861-4a2a-3937-ae0c-45694226230c | -1.71015 | -52.41207 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7581b607-b1d4-3f68-93da-709c4a2b50ec | -1.35341 | -53.67835 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783d2e79-25e0-356c-bff2-44fbacdadf0f | 3.6274 | -60.03379 | 2024-12-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a62bec2-1646-3dd6-9762-7cf016103ab1 | -1.15228 | -53.59695 | 2024-12-28 04:59:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e9268f2-6714-3d7c-9120-029e3341a670 | -1.38554 | -53.53979 | 2024-12-28 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 994339d9-52d9-3c35-baa4-57632d4c2229 | -1.12553 | -54.13269 | 2024-12-28 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84a239e1-aa7e-3117-a0a0-47111a4fc774 | -1.59334 | -54.13832 | 2024-12-28 04:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd4547ab-e8fb-3b91-85e0-f522e6af9b3b | 0.93242 | -50.77935 | 2024-12-28 04:59:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39bb1955-3a19-3c4c-acda-6a31ede74349 | 3.63187 | -60.03307 | 2024-12-28 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fec771c-e8a0-38fb-8cbf-72ca7f8aec0b | -1.70728 | -52.40773 | 2024-12-28 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b67d38c9-177a-3ef8-b88f-73bdb492fee4 | -3.7595 | -47.22197 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ccebcce-7859-3d4d-bda8-fb546d8b8740 | -5.90451 | -43.4873 | 2024-12-28 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b15e159-92a5-3fdd-ba5f-7f19d9c8a9d8 | -1.92824 | -53.34736 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86a8a487-7f9a-39cc-87d0-ed82eb67da18 | -4.73829 | -44.6486 | 2024-12-28 05:01:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ca9963d-d7e7-3fc5-8dd2-f9278b09ed9b | -2.26225 | -53.87952 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f845d30-7edc-3f37-830e-cfb85539ecd5 | -4.03648 | -47.0518 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 29339395-a0b1-3dac-9293-f957af7fd984 | -2.48212 | -54.16712 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a506cc8-0184-33b4-b8c8-056421d60225 | -1.94171 | -53.34944 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e4228d9-338a-335f-ac0c-59a6b817189f | -2.90325 | -54.49179 | 2024-12-28 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46706ce6-f6c9-34f5-b5b0-adce08c6f2fc | -6.1183 | -43.95454 | 2024-12-28 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5840c9ac-d944-3ae8-a070-3fe1859c210d | -3.93354 | -46.9852 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b601cab5-bb81-307e-b597-f257d35493b0 | -1.94564 | -53.34639 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62fc4a2d-8e21-3623-b7cb-8b62ef527214 | -3.20579 | -53.94652 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbd8b53d-bd02-3503-8b55-36a740cebbdd | -3.93855 | -46.98597 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10279c9a-c5a6-307f-85d1-8ea6f9ea533e | -2.37445 | -53.87929 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e74b2cb-8802-3b25-a49b-e536daf768bf | -2.21322 | -53.65269 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 458d6068-d381-3671-8c92-ec11cd2cd768 | -4.07659 | -47.09124 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4f86bff0-d233-3970-a580-fb6b9d3d81bf | -3.92893 | -46.98169 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ea90517-bc2e-30fb-9abe-495b139033a3 | -3.15246 | -53.89885 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdcfa59b-7bf7-398c-a58d-170db6d3d4ca | -4.11593 | -46.72151 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a6609fc-77ae-3f75-b64f-0ebd6b631fa2 | -2.91436 | -54.0094 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c862f3e-340d-3144-ac1a-daa36f39ee48 | -4.0373 | -47.0462 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d71dd620-1a1e-368c-9260-f9fe6c441d4c | -1.82296 | -53.84377 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a92bf1e-f08f-3a97-acf9-cd2b4d23f0ff | -5.64029 | -43.71803 | 2024-12-28 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e0af4b8-182d-3784-8dfc-bdf3e102f825 | -2.41642 | -54.21725 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe60d697-610b-3291-822b-0b0d8acb6ffe | -2.37391 | -53.88278 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e16cc12-4605-3c3d-88e1-afe2f4b68884 | -3.94044 | -46.75887 | 2024-12-28 05:01:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c23c692d-3624-32f6-8ab9-f6614dfe4768 | -3.98122 | -47.1171 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb017651-a054-3f72-b040-32f81d01915d | -4.50374 | -44.23697 | 2024-12-28 05:01:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75cf7010-d7d5-3ef9-81af-6aa248a87884 | -3.57037 | -50.67707 | 2024-12-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e48f53-e10e-3ec1-b640-de77ce44dd93 | -4.04067 | -47.05809 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 517b1f18-09c3-3baf-bd8c-eda4e0f920ea | -2.69461 | -51.84959 | 2024-12-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4988d7ca-cc08-3411-a7ba-01853663bb50 | -2.49136 | -54.17246 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7399c7c8-ec10-3aa7-82f9-02618e23653b | -3.18979 | -46.12831 | 2024-12-28 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 559152d8-fc8a-3d3b-82ea-679148766d68 | -5.63957 | -43.72309 | 2024-12-28 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceb1fd6d-f4ea-3f92-b6e2-e825c92aa1e6 | -1.95232 | -54.10264 | 2024-12-28 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 584f0e7f-5ba9-3656-b4bc-f8f0dee26525 | -3.81686 | -46.06272 | 2024-12-28 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cb59d54-b36d-3685-8576-03d96717ddc0 | -3.53686 | -53.80204 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README21.md)
