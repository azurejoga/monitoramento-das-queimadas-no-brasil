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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 547d6ce8-a623-3da2-96b3-923ee481f81b | -9.17301 | -45.781 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3af939c3-f121-305d-9405-18805d25e6a5 | -11.38451 | -43.43241 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed5fe221-2e4c-3bae-8dd9-3a605655c0cf | -11.35619 | -47.43091 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34750682-b9e7-3de8-becd-828ffb59fc8a | -11.68515 | -44.52927 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07cf8d07-c6c4-3f8d-92ee-af72a4fd89ea | -8.36658 | -44.15972 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b06837e-cfc4-336f-93d9-f14dc2b85f90 | -13.33012 | -46.80892 | 2026-09-28 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b47b3173-c727-3d76-914d-c1bd3975ebcf | -7.07041 | -41.73977 | 2026-09-28 04:34:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 799af557-3528-3dc7-802b-fa40419d493c | -13.5641 | -46.36201 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07303e1b-6a14-3085-bd00-936151d6f9d1 | -11.44247 | -44.92622 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6fd9ff0-1e66-37b0-b404-5e64c751987b | -6.71161 | -45.59062 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 076bd2b9-c084-3430-afed-c2cee157736d | -8.00429 | -44.97309 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15c763b2-cb27-327e-88cd-5bb9474b1e92 | -10.20887 | -50.00724 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34677099-2387-361b-a4c9-1742bd08a9a4 | -10.20837 | -49.98887 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b407bd01-7f6b-3f23-a149-9801591d650b | -10.40284 | -53.81054 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 167d1d29-8f8a-3930-97fb-f007664b95a9 | -7.87751 | -61.18914 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c6b4988a-e008-3142-93b3-a07f8be2a294 | -10.11658 | -50.19808 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b0ed044-517a-3171-99d1-5810890cb7d7 | -13.10376 | -47.41381 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f64630f9-a106-3030-a456-ff0d9cc5de4b | -12.72455 | -47.27972 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a535e4-25cf-3137-89f1-5df75715a77c | -11.1326 | -47.49533 | 2026-09-28 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5392abbf-e78f-3cf6-b7ef-ccbc5a91bdf0 | -8.2443 | -45.40531 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 331070c4-80ee-3195-82ae-933aee8198e1 | -8.95643 | -44.16352 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a04a073-2cd0-3325-aba9-bc405873ba60 | -6.93135 | -42.86267 | 2026-09-28 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 054f4c3d-ccdc-3f10-ae90-7fc3227be4b7 | -6.99357 | -42.6965 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a762c11-3362-3181-a0e8-b361cad85b9c | -11.69831 | -44.54816 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da00864d-a68b-3415-b641-941b56a0f3ff | -9.92727 | -49.37896 | 2026-09-28 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd872e10-d4cf-3750-9c85-d71ffeb0ba6c | -11.38301 | -43.41193 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 112585e2-1a30-32a1-82e0-410aa461a3eb | -7.88414 | -45.448 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de9441a7-a98e-35a4-b929-9abee35c97d6 | -11.71101 | -44.51355 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76ec45c5-920f-3666-8599-6e5b973a453e | -7.68295 | -44.79228 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a99bacd1-eda1-3fa9-b859-208d2d80922e | -11.13951 | -50.06065 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 028ae080-2bf2-399b-b847-0cda5b1b57b1 | -11.44007 | -44.92387 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e892fd5-c75e-312d-a486-be64f63ffd8c | -10.41383 | -53.81764 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5399cdf8-873b-3423-ae36-b8fee8ce1ab1 | -10.21731 | -49.9757 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68eb8ac9-af3a-3e6e-830a-b932f51047f8 | -11.10751 | -51.32518 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 586bb46c-39bf-38d9-ba3a-3b2cc8b0008a | -9.62532 | -43.96184 | 2026-09-28 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3d080b58-372a-3cd0-a86b-71e619fbd77e | -12.58893 | -51.9544 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96168453-e08f-378a-942d-7d79db3fd662 | -6.76946 | -45.37267 | 2026-09-28 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17c90f89-6279-391d-a366-74e746b1d86e | -12.31416 | -46.40645 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8f302423-8c20-3a11-bed5-39b65e05249b | -12.69833 | -46.97671 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca8c3b3e-9ef7-32cc-8ff6-9e1c3ab5e5a9 | -7.86673 | -61.18892 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cc8aee91-b7f0-375c-89c2-9cbf61d61074 | -8.63557 | -49.47658 | 2026-09-28 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7cc03bc-1b52-38a7-832f-3968cd2233c3 | -11.4446 | -44.9196 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b21fb7f-6a9c-37c8-bdfe-15155be4e2cd | -7.63076 | -45.51926 | 2026-09-28 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 100a1bfd-ffee-3afb-9671-6792fe6f083b | -10.45683 | -45.09385 | 2026-09-28 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2f1dac6-b416-37a5-ba70-b41620c9ec29 | -10.20503 | -49.98833 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea333038-0d1b-32d2-9ec3-c7f9070b77ce | -10.21894 | -49.98692 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f990a0d-13d2-364f-b484-02658a77bd66 | -11.26651 | -43.53614 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd336cd-1348-32b7-a31d-7373c18cb6bd | -10.12972 | -45.13573 | 2026-09-28 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1baaf148-4d17-3bb1-b147-e0116b06f494 | -10.2056 | -49.98477 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06550d36-3b9f-3e63-92cb-22de9002eb5f | -11.78299 | -48.31398 | 2026-09-28 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db75ef59-c348-3056-b5bb-4dfd1d606727 | -9.15436 | -45.64208 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 791d7021-234f-30ab-ad6e-62c7b93d240c | -11.70824 | -44.53401 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b090a04-61e9-3241-a529-00c62acd49b6 | -8.9603 | -44.1641 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 416936a5-1cff-3ee6-a9c7-86b41911a3f8 | -11.70657 | -44.54799 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc5ef0b7-38e4-3525-a125-d3575eae4533 | -11.1024 | -50.67947 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ec1147-0e71-3938-9404-2a0f7801df0d | -7.37896 | -47.01846 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3ec9381-3b97-32f5-9bef-d79d209b453a | -10.81767 | -60.74462 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b9c37ad6-de26-39d2-9d99-a885329eb0ef | -10.2134 | -49.97872 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6733e44a-f49b-34cb-a6f1-053d6cafb723 | -6.74415 | -55.08706 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c65f9a7-bed2-337d-9417-008356c924b0 | -11.13285 | -50.05956 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 13389899-f023-314e-ab64-dcd3813d8550 | -10.22285 | -49.98389 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b6abf89-7ddc-3637-a827-74c9bb2082a0 | -12.57851 | -43.50291 | 2026-09-28 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c66608ec-a731-38e3-9ab8-eb24a56ebaed | -10.0084 | -45.17439 | 2026-09-28 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 443bf8a9-a61f-322e-b9fd-dd9049180bea | -9.94025 | -50.23955 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a7b7db95-68f4-3fe3-8b4a-fe5f805ed1b8 | -13.56833 | -46.35831 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d94d983-90bb-3df9-b2ef-2416f2fe9e35 | -8.01441 | -43.74011 | 2026-09-28 04:34:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a683445d-e9e4-3c7c-8663-35deb3f796c4 | -7.41515 | -42.62663 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eba21f40-894e-3687-a4ed-97f568a8a60d | -8.67268 | -48.96256 | 2026-09-28 04:34:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f44c0202-9309-333c-9edc-158246845a39 | -11.1912 | -44.79441 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| d20726ea-ee75-3990-853d-154d6da27b9f | -7.34286 | -42.07098 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| aaf9699e-c4ed-3aa1-9ac2-f186b3674134 | -9.79458 | -44.82466 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8448e49c-0820-3008-bdf7-0407380ebc99 | -10.41205 | -53.82796 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49c3629c-0bd2-3c08-a807-213c66cc4135 | -10.00902 | -50.12502 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 567f8ba0-b119-3fcb-8d18-d5b117f31970 | -6.94853 | -41.61269 | 2026-09-28 04:34:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 35f8a36b-b500-3ee3-a014-1119be5c36f0 | -7.27942 | -44.31391 | 2026-09-28 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35345917-1765-3a6a-a519-5dce46091f07 | -6.30331 | -56.03381 | 2026-09-28 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5c2f6ec-0f5f-3c8f-a620-ed598caf0af7 | -10.41295 | -53.82278 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 369402a4-0267-32d5-8f9c-cabbcbcf57de | -11.63708 | -43.48101 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4df06c84-ffc3-3cad-8ee4-8cbfc731457e | -11.70016 | -44.53666 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f679b3d6-2768-341b-bd20-c3977758f829 | -7.64733 | -46.59334 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a65e372-641e-349e-80c4-ebcf35260a0d | -9.31765 | -45.37996 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 337a6b72-4fba-326b-b21e-4445a5e2f0af | -10.40502 | -53.8215 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3992a5fd-72f4-376d-89ca-02f8c77497c5 | -12.16525 | -50.39366 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1e9149db-8f4d-3793-a54a-b58cd1de4241 | -6.21934 | -47.43912 | 2026-09-28 04:34:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15b4f953-6048-3b71-ac35-23a429ce38a2 | -9.98596 | -50.14713 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5e55bf87-c505-3763-88f9-55028bd00cb3 | -7.97549 | -45.01711 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb6d4648-bbb6-3e9d-9fb8-ca5c3a02b865 | -10.21391 | -49.99708 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9d02968-5dc1-3936-afe3-c001ff6e3ece | -10.9015 | -50.69121 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0ba2202-6cd8-3066-8ae4-19eb3320e8c4 | -7.0553 | -42.8689 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d85f0d58-ee01-33ff-9d59-abf9652eb5f3 | -9.97975 | -50.16457 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a262dea-c359-3ca8-b512-6b66ebddac95 | -10.12132 | -55.41265 | 2026-09-28 04:34:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7becb6aa-33d0-3b72-9c49-8d6714d9a788 | -13.45401 | -46.32154 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40790080-7b74-346b-914a-2cc1dab3c60d | -11.5468 | -50.51688 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3cb248e2-1325-3dfe-8e8a-c9300747c8b5 | -12.67628 | -46.98109 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ba23f37-2da6-36f9-83d3-a517e2f3db64 | -9.15812 | -45.6169 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dcd5fa9-3fd6-3ac3-bef7-359cc6b354b2 | -7.07547 | -41.73598 | 2026-09-28 04:34:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ccbd20b4-42e4-3034-b9ac-49b7761068b3 | -11.41092 | -47.42038 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c58ed906-399f-3ffc-963b-5a4d0609ba49 | -9.66409 | -48.9113 | 2026-09-28 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b046db1-36ca-3ec3-b262-0b581f4a87b8 | -9.82446 | -44.94403 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56495a2d-118b-3108-b725-359af6249528 | -7.30815 | -44.5957 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README36.md)
