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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a113938b-b9e0-3b61-8352-fb1d5c11d060 | -7.55899 | -41.84918 | 2026-09-15 04:32:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1d959f90-48a1-3cb3-aa8d-e824e72d194e | -6.15538 | -55.71368 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 328ab316-4192-3f0c-9dbe-4bdd18a4d566 | -7.44266 | -45.48386 | 2026-09-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ace6a5e8-e1a9-3252-9530-c5a83b4f746f | -7.11402 | -42.09303 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 561ae04d-7530-3812-b8ad-f2a4a9ca6954 | -7.96379 | -43.98156 | 2026-09-15 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 129827e9-7c19-382e-be82-41b1ce412206 | -3.04478 | -51.27189 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 720b2bda-455f-30a6-af74-1d3f445a8f48 | -5.3527 | -55.89428 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca5c044a-8666-3fe8-bb14-a5aaed96abe8 | -3.63917 | -58.61571 | 2026-09-15 04:32:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39a898be-8787-3baa-88ba-24f6058711c2 | -7.01702 | -44.61675 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 957b9ab1-14c4-30f8-a1a3-9e40d7ac6dfa | -3.07553 | -50.57207 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57de14c9-a91e-37c4-877e-3a26e8236de6 | -7.25235 | -46.15705 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c561291-7520-340d-97b1-e583269242c2 | -3.25799 | -54.29012 | 2026-09-15 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7634b953-cf2d-313c-8706-ae1d204a96b1 | -3.07619 | -51.07669 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 210d3711-6501-3431-8c0c-5acfcdf6475f | -6.05399 | -52.1848 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 02a1b2cf-d51b-3441-b1c6-a2dccba7d3cd | -7.21751 | -46.14087 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 554ae686-b6df-3ecb-b309-3b671f011646 | -7.23853 | -46.15846 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f5bca0c-8ab7-3062-a3de-736b6139d18a | -2.91187 | -50.39713 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3eb08b7-ea7a-35f7-bc8d-dfaed3bcca40 | -5.73655 | -43.28006 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2a804fd-d69a-3433-ae09-f002cb094c12 | -6.18722 | -44.01971 | 2026-09-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dab60d2e-63b1-30a4-8a5e-3011b6109388 | -5.81074 | -53.80022 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6586750-3c5e-3c5c-a46f-24f5888413c0 | -5.74077 | -43.27649 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fcddb49-ab0a-3c07-b21d-f7149d62b956 | -3.42367 | -58.228 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5325f80-ab14-35cc-bd4b-d23599949c29 | -2.68991 | -57.5267 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85144644-4e54-3889-8fe2-4ef19a1de349 | -7.09157 | -43.54028 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c57d43d5-94ec-3a34-b668-fdd71450ec81 | -3.3764 | -50.77058 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a56c65b-c009-309b-8991-b829fd45d0a5 | -14.68608 | -48.00641 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7469e51-7ed1-3d77-89a3-54d3d77b58fe | -13.47824 | -48.04445 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62bcfa60-c9de-3477-8113-bff9d9579737 | -14.22367 | -47.42559 | 2026-09-15 04:34:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d441623c-76f7-3d5e-a420-e08e49670d39 | -11.26886 | -54.12828 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 337bab95-1b24-32d3-8ec2-52edce2203a9 | -15.49971 | -48.55375 | 2026-09-15 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04febade-e50d-3a89-99bf-f3d738b8a1f1 | -14.20256 | -47.4296 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d780587-f03b-3140-926d-160dabd911bb | -11.11012 | -50.917 | 2026-09-15 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b340c4b4-e144-3136-b295-a85310a9d9a4 | -9.01385 | -49.55653 | 2026-09-15 04:34:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a491a059-70cc-3f39-a314-95fdfd660f69 | -11.92156 | -49.73751 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c434b35-4e51-3285-99e4-df728c06a407 | -9.45524 | -56.71213 | 2026-09-15 04:34:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6794824d-7b49-375c-b045-3bd92e1f2133 | -10.89853 | -51.54402 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eec5e6ac-df74-3702-9285-85014017987c | -11.25021 | -43.45398 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e81c3fd-3454-3092-b626-6095e6e98f09 | -11.88746 | -43.82624 | 2026-09-15 04:34:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f6ca7ed1-0d60-3abb-9836-5bd5897d31d4 | -11.8124 | -46.58229 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68c185b7-6c42-3da1-b14d-6bfb68df453d | -13.55327 | -43.53033 | 2026-09-15 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 490bad39-71ed-3ce3-b881-9f1b891ae760 | -10.66722 | -54.1567 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d33df27c-8d14-3898-a67d-bfaf5eac61fd | -12.37076 | -47.98216 | 2026-09-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34c42a78-8b34-39c0-9618-cca8b3b057fa | -11.81854 | -46.58697 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a606422-dcfc-33e2-a4da-79065bece09b | -10.5805 | -47.74749 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5032c98-013e-3019-8f0f-5d235dba5cc9 | -14.86015 | -49.94564 | 2026-09-15 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c692b91-a3f6-3213-907b-8804d8fb72da | -13.58049 | -47.91239 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a8f761d-8b37-3749-85cc-9639c65af6c9 | -8.40738 | -54.73093 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4045cfa-f441-3cb9-b65a-87c203d6279b | -10.75322 | -44.82052 | 2026-09-15 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17ae066c-c495-3e1a-9cce-09b9e5318735 | -9.8754 | -47.80175 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63e2c481-eb2b-3049-95cf-3cc594fdc96d | -9.28777 | -50.31051 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af5c19b0-8127-370c-a2de-5099f657d2a9 | -14.67621 | -48.00466 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9756deb4-2536-34b5-955e-90dcdce86f64 | -9.41998 | -50.10211 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3bf54919-0c4f-30ae-a4be-941fe329dfac | -9.36133 | -50.18939 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c5bbe1-26f8-3202-b998-4bfa3cdbd0dc | -10.94497 | -54.09127 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e6929b1-a37c-35bb-9ba7-bcd91153fb14 | -11.92093 | -49.74129 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64c3640c-cd62-3390-8215-d6b899ed5572 | -10.679 | -54.16832 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf37d793-6be0-310c-a514-0dfd1ae95594 | -10.06546 | -45.48642 | 2026-09-15 04:34:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4840844b-99c3-36ef-a41b-54db3162ba67 | -8.65631 | -49.13161 | 2026-09-15 04:34:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db2e9b6a-d34c-393b-83ae-0a7e0de58ec2 | -9.84873 | -48.34544 | 2026-09-15 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad74a11f-a297-38a3-8cf0-3072f14b3aa0 | -14.8519 | -48.13963 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c73c356-3f9f-388a-aa1a-59f80e2b626c | -14.67234 | -48.00766 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d55cb14b-d3d9-397a-bcd8-6da3e4fe9eab | -9.78769 | -48.15622 | 2026-09-15 04:34:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56126e50-4c8c-3a4c-987e-af9de950c75b | -12.49467 | -41.42131 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2bd5cd30-0806-3404-9fa6-c5cd86b50a58 | -8.79073 | -45.89432 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac9cdbe7-59fa-3a85-92f6-e096f4f9154b | -9.54252 | -45.42664 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e044f99f-c221-31eb-97e3-1101d7b22483 | -10.23015 | -56.26293 | 2026-09-15 04:34:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b730c207-91d4-33b2-bce1-3c2da7176ee9 | -14.66959 | -48.00356 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c44f540f-8810-3c20-bab0-fc541c4c0be0 | -10.89933 | -51.53938 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19d801eb-043b-3976-8739-9a0a8c028555 | -8.4817 | -44.57606 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6638f3ab-346a-3555-b808-ab682d172520 | -14.86292 | -49.94991 | 2026-09-15 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dceeb5e5-d443-3d21-bfce-d53453f93c76 | -9.41573 | -50.1056 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 5143378d-875e-36e5-af9d-e6d4583fb492 | -10.98714 | -48.32728 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 434dae2c-3cc9-3c65-953b-17320b884d13 | -11.23431 | -43.45646 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfe1b7fe-272d-3a0d-9f03-077d5eecd4c7 | -10.98818 | -48.34209 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d254c90-5229-32b8-a50c-35b16c61bfe1 | -10.67408 | -54.14413 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17766af2-d51f-3888-9b98-4e5a02fdab94 | -14.21259 | -47.38694 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc112aa3-a107-3acf-8595-9e000dc914cc | -10.9915 | -48.34264 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb51481-b26e-3ca2-bf28-daba148366b4 | -10.67488 | -54.13963 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24f1985d-577b-37dd-a372-42512efd00c6 | -12.11982 | -57.19298 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 574804e7-ccc1-3cc8-b66c-0024c3d4ec5d | -9.25797 | -59.64032 | 2026-09-15 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93368f7a-c951-3e45-8d06-6d61358c702a | -6.87804 | -59.64377 | 2026-09-15 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba47e1b0-30d5-3163-bfde-5ee22859b1c5 | -10.88264 | -51.546 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56b6ddc3-712d-3dd6-8c85-d59379604a6b | -10.70446 | -47.50239 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb801648-d971-3e68-a55b-b057f3082506 | -14.38398 | -47.26181 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aea9e31-b133-3386-8893-d2e121d4c13a | -11.92295 | -48.25591 | 2026-09-15 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ab5fbf-1941-3f76-90a5-9e97b1a2c230 | -8.46599 | -50.77249 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57ce6f3d-909f-3492-88c6-87e0b33e0cfb | -9.68952 | -58.17841 | 2026-09-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c8ab043-2372-355d-a30b-aa4aff7c2f32 | -10.43825 | -42.73973 | 2026-09-15 04:34:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 677184b0-e32d-31cf-8f55-2b4e3601609c | -9.84818 | -48.3489 | 2026-09-15 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9f7f8c7-c9a1-3620-abe5-93c19f817a81 | -11.88878 | -43.81705 | 2026-09-15 04:34:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b537781f-227d-3519-aaf1-02e76b3e3498 | -10.57831 | -47.73996 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b022e838-63da-324c-a066-775ded196984 | -9.35775 | -50.18878 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da204426-b9b5-3c7c-aa43-c6c88583247b | -9.41506 | -50.10969 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42bea21b-658c-353c-8d25-9b46693813c6 | -8.80843 | -50.48899 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f4b5cda-7dd7-35e5-9548-dc385861a68c | -10.98381 | -48.32673 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac91c87e-1ace-3975-b02d-f86502fddfa2 | -13.25753 | -51.28293 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4804e45b-093e-314c-b195-2256b87c3bba | -8.79242 | -45.90553 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fd2332e4-104b-3e3e-aef9-e482d15f9897 | -13.58987 | -47.91756 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d7bc577-e25a-35bd-944e-ae2e3cb33297 | -11.17704 | -42.804 | 2026-09-15 04:34:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 481cf1d7-c583-3e6a-a064-047c80e82062 | -11.33021 | -46.78107 | 2026-09-15 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README42.md)
