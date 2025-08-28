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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7fc407e-158d-3aaf-bad4-825215dc438c | -5.4147 | -41.15039 | 2025-08-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 03477ffb-299b-3688-b01a-7da878c65880 | -3.78713 | -45.03765 | 2025-08-28 04:06:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 30c45bf8-84de-3c40-86f1-169c44a15a99 | -7.43684 | -42.04824 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74dc0493-ea3b-3011-8735-b7401599c306 | -7.62818 | -42.70417 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 12cb9c74-9060-30bb-b31c-9b317fe4bc4c | -5.90059 | -43.39762 | 2025-08-28 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a61126a9-53d4-346f-b59d-ff402dc31260 | -7.08007 | -44.30744 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 084b8083-5ddc-3197-8ae7-cbfa280eecf8 | -7.08509 | -43.64182 | 2025-08-28 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab9a8546-f717-320f-b60a-ac75dad1d908 | -6.16704 | -44.39862 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5123333-39a6-3d8a-ac88-0b3056823bbc | -6.97219 | -44.10175 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bad5cc47-07ec-3157-a08e-58189138e06d | -7.42521 | -40.08425 | 2025-08-28 04:06:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c4f3d95e-8971-3315-b474-32c31ca457bd | -6.1819 | -44.06198 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b605c31-edea-3491-b1bd-f99be3f38bee | -6.32617 | -43.75621 | 2025-08-28 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47dc9192-c3db-3fd8-b682-7f641369e515 | -4.79646 | -47.25755 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4d459ca-46ec-3768-ad5d-a1b6c3f8fccb | -6.86731 | -43.62256 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f4967a8-a875-3a5e-926b-0acfbdfd9212 | -6.38046 | -43.24643 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 076ba712-31de-3a03-8ec8-99117c47f567 | -6.94714 | -44.10189 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6556ae7-5c7b-30dc-b113-17fa93e2ccf2 | -6.57517 | -47.38069 | 2025-08-28 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e5913e3-ee03-3f31-848c-2e4c31798365 | -6.87872 | -43.61657 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 52fdd7e5-b7f4-3d34-a799-fcd442abf96e | -7.40675 | -44.05939 | 2025-08-28 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 932a9ddf-e358-30f5-9d4b-41bf2078cc93 | -7.62545 | -42.6785 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 492cfd7f-fca1-35e7-ad48-01054f391411 | -6.49547 | -47.18924 | 2025-08-28 04:06:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fbb3e67-ef68-3a52-bfb9-b3c81978365e | -7.1304 | -43.68721 | 2025-08-28 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e5b186c-8135-3202-8ba1-bae59afbaf4e | -6.178 | -44.17443 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fc8462e-4e95-31b3-9cd7-71c2515f2b11 | -6.80481 | -44.3527 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba195733-fb7f-3ac9-8418-ca97851660b5 | -4.63865 | -41.39861 | 2025-08-28 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 539edae7-d3b4-30ed-ac2d-0ed501daf108 | -4.55978 | -44.00951 | 2025-08-28 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 728d6841-9a64-319d-bd56-7994b54f04e3 | -6.81152 | -44.99752 | 2025-08-28 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0ac36bd-4854-32ba-b830-b6dfa45db7ce | -6.87312 | -43.60815 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5bdc9d3-52d3-336c-a5fc-9f26fbd01575 | -6.22265 | -43.35666 | 2025-08-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00b82114-5b09-3cae-94c2-cdb99b9510ff | -6.07111 | -44.00809 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79139a4c-1d3c-33e1-b2bb-6087a99b9364 | -6.44 | -42.42077 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 593087b8-7224-31fc-8e1a-fe656a315618 | -6.301 | -42.5027 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cadfdb50-871c-38c8-ba8d-2c221088c0e1 | -6.30465 | -42.80136 | 2025-08-28 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ebe7ee8-7f07-3bbf-83d4-d5644e76cb45 | -6.6906 | -44.40814 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b11f744e-82e6-3aa9-9b09-a4165eaaa194 | -5.01013 | -42.97851 | 2025-08-28 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 60e69030-92f0-3b47-9702-3aaf8df2ff8c | -6.86627 | -43.60706 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90e16616-9319-335d-a171-8774f2b4f34c | -6.86805 | -43.50836 | 2025-08-28 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fceda1c-dd45-3818-b0d8-58dfdba7be14 | -7.55548 | -42.0061 | 2025-08-28 04:06:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb506e8d-b85c-327e-b444-4032664fe89d | -6.44253 | -44.57366 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2771ecec-ca12-34cb-889d-4d2ca87628fe | -3.73205 | -40.27334 | 2025-08-28 04:06:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9beb902c-1f28-3458-89eb-ec7e4dbbfaf8 | -6.98644 | -44.12426 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeaa58df-737b-3490-ac2f-35315b33b713 | -6.15162 | -44.04925 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 789459f3-7743-3013-a66f-baf67a30ca20 | -6.15897 | -44.38083 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae969f1-780f-38a1-84ac-c1ccf1f6c835 | -6.88055 | -43.60537 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7023be3e-c455-3c92-b5e5-561a4a1b69c7 | -6.22606 | -43.35719 | 2025-08-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfae0aad-7d0a-32fe-a6cf-912539b5a633 | -7.05935 | -44.36885 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9b70b76-0f94-3b68-b9e0-5e67b4275cad | -5.6827 | -40.97995 | 2025-08-28 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| babdec4c-e928-365a-b331-d51504f06554 | -6.12817 | -44.41288 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab0b922c-4d29-3d52-9807-b2f5d7ae4ea6 | -6.65489 | -44.38227 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4bbd34f-3ae7-309c-ba8e-c31f9f6b1907 | -6.49641 | -44.39978 | 2025-08-28 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97280406-4167-32bb-95a8-62d531e66a7f | -6.08222 | -44.00602 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82b99407-9b08-3713-ac69-3aabc9cd30cb | -6.86568 | -43.6108 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85dc0c71-7ba1-3111-9031-db17873c6346 | -4.79577 | -47.26165 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3c161b60-479c-3754-82e9-3b65a4a9c7de | -7.15599 | -39.42238 | 2025-08-28 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 72d3eca2-8f99-3a13-8acf-3e60ac0be78b | -5.5352 | -36.84657 | 2025-08-28 04:06:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46806c0e-718e-324f-8a8d-46619276b68f | -6.88686 | -44.42651 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc9c89b-9806-3648-aa23-67ac600c09b5 | -6.88267 | -44.42992 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edd8cf56-0086-3356-92f8-bdcc6d0293fb | -5.41524 | -41.14694 | 2025-08-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e5bdbfdb-a11f-339f-8fce-31265b26ecff | -7.38758 | -39.69039 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 42.7 |
| c5376242-f8b6-31d8-8a42-927bc9511f37 | -7.40192 | -39.68874 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 28506228-e73d-3e04-b2aa-954c5986fbee | -2.91993 | -48.31033 | 2025-08-28 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d14c73b2-c36e-3d1a-a767-06067d2db7e4 | -5.89984 | -45.56494 | 2025-08-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de7a2322-a472-3337-a394-390233066a1a | -7.63711 | -42.66957 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 855b7b6b-3f28-30dc-b473-244931541602 | -6.96933 | -44.09733 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cea7aed2-db1e-37e8-9fb6-7b10348c8fc7 | -7.00749 | -44.3765 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 060d3b9c-e1bc-3927-9f59-2838b1cc4911 | -6.19112 | -44.16034 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee6506f5-cdb5-3181-a5b2-5ca2820cc00b | -4.29005 | -40.9381 | 2025-08-28 04:06:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c28e6d0f-7f5f-3f87-bd12-83b56397c290 | -7.17667 | -44.87248 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75732ea3-409e-3895-9651-6b2bc4713dd9 | -6.86612 | -43.63003 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f672ece9-6aa9-38e1-b203-7b5bc7d6a49b | -6.86329 | -43.62575 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 506e226b-4a95-37cf-9fdd-569a787d7702 | -6.38796 | -45.59063 | 2025-08-28 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a80e967-fd41-35c5-a0a6-10f8f767d34a | -4.87739 | -44.96021 | 2025-08-28 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac68d2a0-6781-37a9-bda5-0e5704895034 | -2.44489 | -47.32779 | 2025-08-28 04:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d925d64d-40c9-3f7c-a1e0-f0b61392c288 | -3.75876 | -54.82505 | 2025-08-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8760bfaa-f1f5-3627-93d4-e8d87a6f430a | -7.66319 | -42.65581 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69c6036e-ca12-31a9-a04c-586a116f14d7 | -6.87407 | -43.6235 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12709689-0335-38c8-bc8b-819ee2d1122b | -7.2431 | -39.18089 | 2025-08-28 04:06:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 54205922-43b1-32d9-bfda-61125c342f5c | -6.80575 | -44.32477 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b957ba6c-bf0d-3d6d-b09f-351eb6aa67e7 | -3.27574 | -43.52657 | 2025-08-28 04:06:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c83fb711-0efe-365d-8067-a7bfe03ead14 | -3.73259 | -40.26987 | 2025-08-28 04:06:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5184b959-6ebc-344d-abcc-712e151a99d1 | -7.42472 | -42.06052 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4144fc70-d8ed-319f-a750-478beaaccfed | -6.81247 | -44.35009 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90500c87-338e-3f6a-a676-83873993246b | -7.63322 | -42.67254 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47a2fed9-d0e3-3e78-a51c-9d57e7fb3f29 | -7.01559 | -43.87725 | 2025-08-28 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d9e0ea1-cbee-3d6a-b488-d164a2bb435f | -7.42858 | -42.05758 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20c226f5-4125-3c03-b586-ea73d73c54db | -3.75484 | -54.82373 | 2025-08-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 94f4fe71-aab4-356f-b735-4d77b4905499 | -6.71725 | -43.09185 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db70f373-c0cd-3116-b461-aab22944dda5 | -6.52293 | -42.99039 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d4611aa-3011-3b7f-bf3b-7164b4b01868 | -7.3847 | -39.68609 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6577e0fc-4a3f-36e5-afdc-c65f24a2b029 | -6.87014 | -43.62683 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8c4068ab-7023-3a5d-acd3-4db3be34aa5f | -6.88852 | -44.39428 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d35ccb07-339a-32ab-8432-aaea0c76c585 | -5.20559 | -44.31935 | 2025-08-28 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a5e3382-44e0-39e5-958c-844ebd7e8df3 | -6.18602 | -44.01472 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0a060aa-1168-3b4f-8cf5-f105e5b97f89 | -6.4522 | -42.42992 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a1ebb8d-cb1b-303e-9cf5-91014f0fafe4 | -7.39503 | -39.68768 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 18216eb2-9f76-39a0-bb27-6b06e777dc86 | -6.88336 | -43.60965 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c9a63238-27e2-3b28-8bc5-4d08ded66a48 | -7.3979 | -39.69199 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 32e06c41-90c5-381c-96d6-5c47b3bbdf85 | -6.87994 | -43.60911 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9f183a2c-8e5e-3beb-8e9c-6e8ab6987fe1 | -6.22206 | -43.36032 | 2025-08-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d91a3c83-7f6a-3e7e-9d6b-f6464457c596 | -6.48868 | -47.48187 | 2025-08-28 04:06:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README31.md)
