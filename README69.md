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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64e3ec73-0001-3f53-8dfa-7fa1f8317dbe | -20.81418 | -42.29673 | 2024-10-02 03:55:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 64eada7e-14fc-3e06-b75c-f56dc5cbba7b | -20.81358 | -42.30046 | 2024-10-02 03:55:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56e68a9c-32af-3990-854a-78d8c0f971eb | -20.81086 | -42.29611 | 2024-10-02 03:55:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 932a8d5e-4493-366a-936e-33f1350d2026 | -20.81026 | -42.29985 | 2024-10-02 03:55:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5abd5232-5c14-3e1a-90ac-dde05f2a7291 | -20.33552 | -42.14734 | 2024-10-02 03:55:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 24de7368-a000-30ba-8a34-5d6bfba9d06a | -20.33161 | -42.15042 | 2024-10-02 03:55:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dd6e6e6c-6c76-370c-bc38-5ba7a8ef8a34 | -19.89498 | -42.32438 | 2024-10-02 03:55:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0f100941-d975-37e5-a298-59c89a663d5c | -19.89164 | -42.32378 | 2024-10-02 03:55:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 43b45d53-a8f7-3c06-97a9-c125094ba164 | -19.87114 | -42.3511 | 2024-10-02 03:55:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cd2bdefc-3fff-35ed-941f-85f75906563a | -19.86841 | -42.34678 | 2024-10-02 03:55:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 19d6a235-bc8b-3b9c-83ea-5f6501534220 | -19.83414 | -42.09269 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 508b49ae-b714-3ac6-ab75-62aa8858c6af | -19.76676 | -42.0049 | 2024-10-02 03:55:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ecacc6b-c906-3273-8df9-1f694d66cec3 | -19.76284 | -42.00801 | 2024-10-02 03:55:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef9f88a9-40ce-3cbd-bebe-a3bdbf2b2038 | -19.71896 | -42.42766 | 2024-10-02 03:55:00 | NOAA-20 | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ac7a8727-0a2e-302f-9df5-2eb18075f783 | -19.68343 | -42.4135 | 2024-10-02 03:55:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad5a92f8-12d1-33d0-8dad-2a3eed33488d | -19.90971 | -43.16793 | 2024-10-02 03:55:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6072cfa4-8e58-3d69-820d-e3f3639160b3 | -19.89406 | -43.15687 | 2024-10-02 03:55:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 586e8cb1-df27-3ce3-a450-acf1b2079236 | -19.89067 | -43.15625 | 2024-10-02 03:55:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b2d61ad2-2df1-39f1-aeea-d229e0443893 | -19.8839 | -43.15492 | 2024-10-02 03:55:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d10858a7-7851-362b-bffe-d16810f52c94 | -19.88052 | -43.15422 | 2024-10-02 03:55:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e8f64b2d-6803-3fdf-a857-46d88c21cca5 | -19.87923 | -43.16188 | 2024-10-02 03:55:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ea48b304-9f9f-3a94-9595-b64558942b1d | -19.87521 | -43.16504 | 2024-10-02 03:55:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cdfc2fd1-9953-3c52-b1a9-98c2a950aac7 | -19.86781 | -43.16744 | 2024-10-02 03:55:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 52eb3738-df22-34f4-88a4-4cbc24df2bd6 | -19.78247 | -43.1725 | 2024-10-02 03:55:00 | NOAA-20 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f87ea23b-9e3b-3ca2-903f-78347db110f8 | -19.77905 | -43.17199 | 2024-10-02 03:55:00 | NOAA-20 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9bfea5f5-ed0a-3d3f-90fd-e969de761cab | -19.67894 | -42.93242 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 98a47120-ad4d-3a39-a4fc-e6d5d83fce0b | -19.67217 | -42.93127 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de4beb7a-d3f7-38db-a11e-ff29fb94a57c | -19.58385 | -42.6315 | 2024-10-02 03:55:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 50e10327-9243-3c5c-a1bd-ea22717a0a0c | -19.51249 | -42.8751 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 6dd029a7-3ebe-3590-8646-e47bfda67cdc | -19.50912 | -42.87444 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 82f32187-76e6-3017-aae4-7c71f4b3cbdb | -19.50851 | -42.87815 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2de90380-3210-328c-8bcb-49cc33776b1b | -19.50514 | -42.87748 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 329483aa-74d4-334b-9789-76191845bbd0 | -19.44328 | -43.05978 | 2024-10-02 03:55:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80114e24-528f-3ff0-a723-aa588a656923 | -19.44054 | -43.05533 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 67434149-5b61-3019-98da-7b9c98b3fa11 | -19.43989 | -43.05919 | 2024-10-02 03:55:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b0cd2c02-4d90-390f-8eee-c427d69b426a | -19.43649 | -43.0586 | 2024-10-02 03:55:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ccffecfb-64ca-3ccb-b829-6901de03c469 | -21.62604 | -43.46864 | 2024-10-02 03:55:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 849bcff2-5216-38bf-9472-0adfba76da99 | -21.62565 | -42.8084 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d134dc2-fb82-3eff-851e-4803f2a684b8 | -21.6196 | -42.80332 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a00ca9b1-7325-32c7-852f-3d9cd3dbc1c3 | -21.61898 | -42.80718 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 0305c08d-1330-3c2c-89fb-01fe0fccc989 | -21.61835 | -42.81107 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 10052842-568e-325e-9004-651927078b64 | -21.61626 | -42.80278 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0cd9954-e07e-36eb-a53e-d3e5d1eb8cd2 | -21.61589 | -42.82621 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2682bdf6-dd6e-30f6-9b8f-6efb9845dc62 | -21.61563 | -42.80661 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c2d6a24e-d049-3e62-8e14-9de89808126a | -21.61229 | -42.80605 | 2024-10-02 03:55:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5240b9fc-9a41-3ddc-9af1-4783038668ef | -21.52559 | -42.62825 | 2024-10-02 03:55:00 | NOAA-20 | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 19a2840b-f8b0-307a-8aa2-fe2f842ee75e | -21.52226 | -42.62764 | 2024-10-02 03:55:00 | NOAA-20 | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0c944985-7dc6-347b-b216-9fad8be7f84d | -21.28664 | -43.02269 | 2024-10-02 03:55:00 | NOAA-20 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4f002234-1a1c-3a6c-b5fe-b6683da40a3f | -21.00284 | -42.60265 | 2024-10-02 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c8ca6f18-21f3-35be-98bd-df6af0e38ad3 | -20.97284 | -43.30066 | 2024-10-02 03:55:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 441d3388-974e-3d3d-9111-5694163b2b73 | -14.75607 | -42.41984 | 2024-10-02 03:55:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e238213-d6f2-32a7-9717-583141bf56ec | -14.75541 | -42.42379 | 2024-10-02 03:55:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 29176541-430c-3ed5-967a-ae579177e016 | -14.39589 | -43.27498 | 2024-10-02 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a973d1a4-690d-3430-9a8a-761169a1943e | -14.39516 | -43.27922 | 2024-10-02 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 13c2ac58-79c8-3ec6-9e49-f821d23e2657 | -14.42933 | -43.4488 | 2024-10-02 03:55:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e110e67a-828c-362e-9836-d55aaecff7af | -14.33329 | -43.5498 | 2024-10-02 03:55:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c33edeb-e60b-3075-9d4e-5196705ece0c | -15.55461 | -43.01798 | 2024-10-02 03:55:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 434b97a9-5f1a-3e7a-9b19-ab038759557b | -15.44725 | -43.62263 | 2024-10-02 03:55:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d74f648-a69d-3b7a-a4b7-74a4892e2347 | -15.4004 | -43.04942 | 2024-10-02 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b7558723-4d26-35fe-8b98-b12077e394ed | -15.40017 | -43.05064 | 2024-10-02 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4f9d379-5514-3cad-86bc-011147110cf0 | -15.3997 | -43.05353 | 2024-10-02 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c7ba39fc-7b02-31e7-90ab-61a852eca99e | -15.66241 | -43.92019 | 2024-10-02 03:55:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83dfa012-f2e3-3f1f-bcb2-7de550828105 | -15.448 | -43.61832 | 2024-10-02 03:55:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa59c6ac-d812-3f3c-ad5a-06cffb589456 | -15.20103 | -43.85136 | 2024-10-02 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67d62ecc-07a7-3133-8702-156f2c55547f | -17.9194 | -44.33342 | 2024-10-02 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c66715d-bf8c-3a85-9eeb-d73fb46c9180 | -17.09357 | -43.80619 | 2024-10-02 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 813f23fe-38a0-374d-91a4-c16f17965998 | -16.67935 | -43.884 | 2024-10-02 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38263099-2d6b-3270-8cf4-1d2f7b16ccce | -17.92056 | -43.44746 | 2024-10-02 03:55:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb54b22b-3fe9-3e05-a89a-4ae24853ce75 | -17.63334 | -43.25568 | 2024-10-02 03:55:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5414da99-939d-3031-a04a-7672f415e71a | -17.28195 | -43.19086 | 2024-10-02 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 878dda13-f9e7-3085-a86e-1066625c1e67 | -19.43718 | -44.34014 | 2024-10-02 03:55:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eed651c-4452-37cf-a071-12ab168ccac0 | -19.2933 | -44.42249 | 2024-10-02 03:55:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b3e6363-8965-3ee3-bded-7bc7dbff82e9 | -19.26088 | -43.76421 | 2024-10-02 03:55:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7cf017d-270d-3412-a0ca-35da4df76492 | -19.25739 | -43.7636 | 2024-10-02 03:55:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd335049-2ab8-3969-bf1a-3de2acb9a1fb | -18.77447 | -44.64213 | 2024-10-02 03:55:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b87bbbb5-02c5-3398-9ff1-23e8fd474d59 | -18.60888 | -44.47155 | 2024-10-02 03:55:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfa113be-4274-3a08-b850-0485d8124ef2 | -18.38658 | -44.01521 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9833dc4e-b9f7-3a0c-a156-9b1a03a910c8 | -18.38583 | -44.01962 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afa83fd8-3d6b-30ac-8c4e-6b58ad992f37 | -18.38383 | -44.00983 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 318aadde-7650-33b6-8ed8-6d6a2a71e467 | -18.38305 | -44.01439 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8feb4182-e415-3367-a5d7-26a03548625a | -18.38086 | -44.02728 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1fafec5-5419-30b8-8834-15475ae05a60 | -18.35802 | -44.03215 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 894bc58c-fc52-32df-9f96-d0b4afb2f06b | -18.35447 | -44.03148 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dc7265b-4d9f-3135-a04b-ca1d3bd38fc1 | -18.35321 | -44.01744 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebfdec70-1bdb-375c-8778-9fd63a7af5b8 | -18.35243 | -44.02197 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0e121edd-c412-369a-912d-9694bc2f5d3f | -18.35167 | -44.02642 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 13a71e8e-aa22-356e-ad45-f7fea0c932d3 | -18.35092 | -44.03079 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3b64bfd-0e5a-3c9e-a1e8-55f1888630d3 | -18.3489 | -44.02122 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddca30f3-2525-3e9e-815c-6a011d16d087 | -18.34813 | -44.02567 | 2024-10-02 03:55:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b30cb61-2984-3106-84dd-94821bc959a1 | -18.20463 | -43.95059 | 2024-10-02 03:55:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a96d90d2-be04-30af-a562-67a9a62cbbc4 | -18.20391 | -43.95473 | 2024-10-02 03:55:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f6630c3-10b2-34e3-89ab-c140aab865fe | -19.24849 | -43.36276 | 2024-10-02 03:55:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a8b3c3e-6681-34b1-bef7-4e40ebcfe437 | -19.24784 | -43.36662 | 2024-10-02 03:55:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 993b7a78-10b2-316c-969c-113920fcd07e | -19.24719 | -43.37049 | 2024-10-02 03:55:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df8561d6-c0b8-3baa-933e-efb3dc9963f0 | -19.2462 | -43.33425 | 2024-10-02 03:55:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a948bf3-3a87-3faa-862e-a0f7acfa0a15 | -18.85662 | -43.55879 | 2024-10-02 03:55:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 989c2623-511f-3e52-8a0d-02570cd0d03c | -18.85348 | -43.43048 | 2024-10-02 03:55:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f6c7e954-42cb-31f1-808f-5a7cb4aaba8c | -18.85036 | -43.55356 | 2024-10-02 03:55:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 808fd3ea-9a1a-331f-9b9c-dce7f5bed9d9 | -18.33228 | -43.25128 | 2024-10-02 03:55:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9bbbd5c7-985a-3057-9416-75761a6f843a | -18.33162 | -43.25518 | 2024-10-02 03:55:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README70.md)
