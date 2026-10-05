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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 664b5d0a-1688-3fc0-8661-ba7a483766eb | -6.7708 | -39.03013 | 2026-10-05 16:37:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1764a126-fb36-31b5-af4e-598081c8b660 | -9.76582 | -44.80156 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c91c1bda-4f5d-3822-9918-4a3efb26e257 | -12.75076 | -40.03772 | 2026-10-05 16:37:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fe7c6715-7f5c-3b48-9c38-9087eaf914fd | -9.86284 | -38.90225 | 2026-10-05 16:37:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 446f5145-7129-3353-906e-6fcb33dd9b4c | -8.54895 | -54.57967 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 45a3f32b-8eb6-30d6-9acb-d660557452cd | -9.87479 | -44.84619 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a8a118fa-0dc5-3142-bd30-efbe4841639a | -10.66084 | -50.72533 | 2026-10-05 16:37:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f17ef779-a6d9-3bc2-85d5-357e810d5132 | -11.93078 | -46.81901 | 2026-10-05 16:37:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 63ce07bb-aae1-3af1-97e9-a994277b82f4 | -7.14796 | -46.43506 | 2026-10-05 16:37:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57debbc8-5f3b-3900-b7dc-d1716b9daed6 | -9.9699 | -45.60276 | 2026-10-05 16:37:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bed9f4f2-2ad2-30fd-b719-1baa37c4992a | -13.59578 | -40.71582 | 2026-10-05 16:37:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5d10c35c-338b-3e90-956c-7a86418b71c8 | -11.6793 | -43.63448 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d5d266e4-af24-30ff-bc93-c7aa27e6eab3 | -9.96933 | -45.59917 | 2026-10-05 16:37:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 75d87009-dc60-3bc5-8b61-28512ef8215a | -11.82811 | -43.54489 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b9e4afc3-34d0-3281-807f-63f5ea3bd0a9 | -12.25443 | -39.33969 | 2026-10-05 16:37:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| d4a0ea1b-a1db-3f9b-9941-a158b4edb319 | -10.94883 | -45.42501 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1d00fc04-cecc-3813-899c-0f2fb23ac613 | -11.22671 | -44.85077 | 2026-10-05 16:37:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddcc169f-0dd0-3f6f-b836-390d9991373b | -12.81288 | -43.30814 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| eac7a5cd-0855-35f7-bdfc-50fb6be27236 | -11.09504 | -41.26202 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f4a443ad-0c92-374b-bdf9-8c28b5655f22 | -12.9064 | -40.0788 | 2026-10-05 16:37:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3ee4f7c5-10d6-31cb-985e-ed9604780206 | -6.71131 | -45.55354 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1172b77b-7e04-3682-891d-509cd2fd0e4a | -11.24249 | -45.25906 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cffb6905-8ab4-320a-97fb-4ed653f4feff | -6.68783 | -45.22469 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c7d7643e-1b54-3bf4-ad72-0fffe355efd6 | -8.84651 | -37.74227 | 2026-10-05 16:37:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 94346caf-9cc4-3451-a4a3-6a448d5b9dd0 | -8.59209 | -45.66291 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 67d18529-f98e-38b5-b631-f8d794661ecf | -7.0251 | -43.4377 | 2026-10-05 16:37:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c0e6d705-1a61-3658-a202-026e0bedb9f2 | -9.40259 | -40.31892 | 2026-10-05 16:37:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 6e5ccfb7-8ddc-3ff9-8229-b53571a02f1c | -10.39676 | -47.5281 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d73c1e37-b36d-35e7-9b53-0f2cdb585175 | -10.96328 | -45.42984 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 194b5ed2-6b4a-33a6-bd30-08442165abb5 | -6.70289 | -45.23021 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 890b1d95-88fd-3c28-95b8-1ef852ebcd62 | -6.70848 | -45.5578 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4937df0b-7982-38ce-a6b9-ef07227afc38 | -8.52674 | -39.54571 | 2026-10-05 16:37:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 3de7d67d-073a-39e8-9bd5-f2d81b7f7956 | -8.65344 | -54.55022 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f95572e1-dbc7-37c5-b913-ddfb9738a659 | -11.7935 | -43.5331 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c479da7-eda6-39e9-8fbc-8b76e3349899 | -14.078 | -43.76938 | 2026-10-05 16:37:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 38b76059-67da-30d3-ba8a-25a2c232e13b | -11.71404 | -43.42481 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 96e75515-cdc8-3e0e-a183-09ba66ea0f51 | -6.61846 | -41.76924 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e08e4c66-ccb9-3d86-95f7-6dd00d9c9de5 | -18.58631 | -41.27771 | 2026-10-05 16:37:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1cff4694-d414-3739-8915-c218a7be46db | -10.97608 | -45.44606 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| aa88e806-3270-3e75-9ac0-d13ac5dea758 | -12.26322 | -40.68122 | 2026-10-05 16:37:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a2a2c1e1-f69e-3cf7-9bfc-b2ed35cd4064 | -6.69777 | -45.24283 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c1b42a33-ae50-3676-95da-a34d1aca1dfb | -6.59945 | -41.57782 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 4b6e4464-07c8-3007-b892-9b0291f61916 | -10.74939 | -45.29967 | 2026-10-05 16:37:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c88ec3dc-584d-3efe-b165-2e8b958f4a9b | -10.33627 | -39.49236 | 2026-10-05 16:37:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 80e3eff5-5104-3677-8b9c-195e67ed9aaa | -9.03473 | -45.17207 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 2a8ab7e6-c5c3-33d7-9f99-2a8d2accda42 | -13.16257 | -43.09554 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 971c9ed7-bdaf-3109-a8bc-f6a698183ec7 | -10.39396 | -47.53217 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35644806-558c-3c84-95c7-b0290391d943 | -6.70575 | -45.22582 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 60240662-0bab-380d-a6b0-68b3b794ff90 | -6.59742 | -41.56574 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 389077f5-8909-3207-9567-4c8550fb1934 | -8.3489 | -44.74234 | 2026-10-05 16:37:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb292e16-ed30-3ba9-ae9e-b2a04017bf5b | -11.24527 | -45.25491 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c0d357c-50f6-324c-b0c2-d2070fd4cb62 | -8.55476 | -54.58096 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f6156d02-510d-30bb-a90d-00ab81b5d20d | -6.60529 | -41.56031 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| ec3ca173-358c-359f-91f2-57824a7be784 | -11.67262 | -43.66034 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8b09d29f-5d41-34bb-9281-2c9535ccabdc | -13.32553 | -39.06973 | 2026-10-05 16:37:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 0ea9392c-f5dc-34cc-b5ab-2f670e008ea9 | -6.69415 | -45.21971 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 49339a3c-8f52-3c2d-bd51-7af9b52e82a6 | -7.79321 | -45.49147 | 2026-10-05 16:37:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| f1d26c35-c173-3f7f-8009-b093a9f9c9d3 | -6.71072 | -45.54978 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe23b32b-ac4d-388a-b00d-68416f936f79 | -6.37796 | -43.63671 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 01c6d92c-9e73-3d5d-8550-5057c75b90d2 | -6.92886 | -43.67936 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| d14a0e71-2296-37da-863a-50382854dd48 | -10.39782 | -47.53521 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6ed3f538-bdff-3f56-bd5f-821c5d847248 | -9.02793 | -45.17319 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 281.5 |
| ab781313-6bbe-33bc-83fb-4f4b9b14d2a2 | -13.02234 | -41.04765 | 2026-10-05 16:37:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 56a7d814-ccd9-3031-89be-dbb5943056f8 | -11.68733 | -43.66191 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2482d8a4-40bd-3fea-bef0-8856edeeea8f | -11.80554 | -47.36588 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7bc6aad9-47a7-3ea0-9745-b271b1f9bd9b | -9.76522 | -44.79779 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8e38a7c-1789-3591-878c-22ba88701d29 | -7.0304 | -42.85628 | 2026-10-05 16:37:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 115d59a6-bbcb-30f5-9838-aa08520abb7f | -12.80714 | -43.31748 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 191.5 |
| ccbe5a98-d388-3d40-85d4-5e3c3516ccc0 | -8.27267 | -39.07476 | 2026-10-05 16:37:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 36.5 |
| d7128036-3685-314f-b8ee-7d279b14bf41 | -11.27482 | -45.22433 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bed8ca12-113f-318b-9a53-ded743e79523 | -6.73184 | -44.92764 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 08349ff0-db93-31f5-a466-6a53d888d2d8 | -6.60305 | -41.57308 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 8970a4f8-231f-325c-ad3c-5b78de0b0885 | -11.68189 | -43.65057 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a974726-a6ed-361d-9ecb-c6380ed3d3bb | -8.53707 | -54.59381 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e3d170ba-b5f8-3d92-9b13-f0343cddc29b | -6.68437 | -45.22525 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d12bdb43-b911-36ee-b45b-a64bd15cfaa9 | -8.53298 | -54.59962 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| bc65d92c-829e-3367-a7c8-599923aea16d | -9.94466 | -45.50756 | 2026-10-05 16:37:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b3b18e10-1a9f-30a2-8045-8f987455d25b | -11.31154 | -41.18145 | 2026-10-05 16:37:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3cc900f7-ac36-3d2a-b520-ba62f2f0278d | -7.88304 | -44.19009 | 2026-10-05 16:37:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d297ad6c-b5ef-3e58-b35f-8da45cd28315 | -8.6623 | -54.54401 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 176bee40-f702-34ae-abcb-52f5329d5681 | -8.03038 | -46.97699 | 2026-10-05 16:37:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e2b7fd57-8d86-3539-8c1b-ed29701b5dda | -8.5398 | -54.57769 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ea73cb8d-f1d5-31cb-b952-097911e1b84c | -8.53611 | -54.59186 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fb789d91-9fd4-3aed-b57b-eef4232003a0 | -10.9733 | -45.42818 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e2f2331-9b20-3ef6-8b8f-c7bf1c42b3e8 | -6.42569 | -43.71725 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6d57982e-7d03-3387-b7eb-cbcae8299dc7 | -11.80834 | -47.36179 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32d5718b-041e-3b7f-bab2-c5292d336f96 | -7.55386 | -46.72906 | 2026-10-05 16:37:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 89f8359d-da16-376b-a1ba-f6b3eb162640 | -8.52588 | -54.58799 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 382e2693-3114-3a3b-a083-bdefc1412196 | -11.68282 | -43.63393 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e0f14890-25b2-3572-b6ba-1acf1dd516a7 | -6.49782 | -44.16499 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b134ef0e-3f92-3548-bc6b-49c4fad9ab9d | -11.63435 | -43.62523 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 4aadd06f-586f-32cc-a1b5-a79c15258b8f | -9.03801 | -45.1487 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b0422499-4a46-3781-9c16-a8cbe93685c8 | -6.95475 | -43.21692 | 2026-10-05 16:37:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 02e3c0b3-9769-30e0-a5ed-e3dce1425a88 | -10.97385 | -45.43175 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cdbf4491-c5e6-3af6-badf-8d7aa62f67c5 | -11.09052 | -41.25851 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fd6d2f36-5a18-3960-b176-4b877b5b9542 | -10.74996 | -45.30329 | 2026-10-05 16:37:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8ad5c483-dd6c-3f9d-a402-67c037c0c53b | -8.22824 | -54.69481 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6f43cda8-8008-3ce3-a985-48a8df80581b | -11.09037 | -41.25904 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| eb811b65-6e50-3a02-9a69-502893c88ec1 | -11.62863 | -43.63452 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| efdae188-0925-33db-b593-43eea3765dc1 | -6.68905 | -45.23243 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README84.md)
