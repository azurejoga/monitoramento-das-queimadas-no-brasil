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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5e14625-4fc6-3c7c-a1c0-e10e9a302c02 | -14.28988 | -41.84686 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c7d5132-e428-31d3-b910-515476de52f2 | -11.64156 | -44.38129 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad5c35ba-9464-3005-ab21-611ebf026bcb | -12.89443 | -44.64829 | 2025-09-24 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67d49304-c9c2-37c3-95c9-ebe850580b89 | -11.41184 | -44.95742 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e00f292a-ddec-3e0e-ab4e-8d8b63c7f503 | -11.51288 | -43.65656 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 248d39f4-1d3a-37b5-9448-8e7e11690008 | -9.58329 | -47.59264 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7dee116-6fa8-300b-be0c-228fd86ac73f | -11.79054 | -40.35693 | 2025-09-24 04:02:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0a09132-d824-3dad-b44c-6fe5d861738a | -11.52492 | -43.67094 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1687fde8-e141-30e9-bee6-998fa1d9bae9 | -12.12359 | -47.92021 | 2025-09-24 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9260c9a7-38ed-354d-971b-9afbf6e40a7a | -10.84431 | -45.41984 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53289b77-258f-3620-8457-ef34d4da052b | -11.63358 | -44.36229 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1aa7b2d-da0c-32a7-9193-a0fbe9293927 | -11.67056 | -44.38638 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58e4c654-c7f4-37dd-aeb0-d3b14e22a8e1 | -12.14159 | -43.31876 | 2025-09-24 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f6e4f82-e568-3f59-b5b8-325c16c94319 | -10.62578 | -49.06018 | 2025-09-24 04:02:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2f879b3-b1c9-3c18-af38-b94a9b3daaf8 | -16.3114 | -42.99237 | 2025-09-24 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2674b5b-a6da-3e11-a305-56d86c89cd33 | -13.61742 | -43.97847 | 2025-09-24 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07767008-53fd-3b4a-bd41-7997a70fb437 | -10.84904 | -45.41551 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d905cc50-63f0-37f3-b1fd-def2b067360e | -9.58284 | -47.56845 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f855de04-1697-3daf-8c59-4dced96136c8 | -11.92999 | -38.333 | 2025-09-24 04:02:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d94aa07f-8ad1-3906-a2be-db4502a1cf11 | -10.85039 | -44.81263 | 2025-09-24 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 523b515c-5581-3c20-b762-deb1b5731371 | -11.62993 | -44.31783 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e712619a-564e-30e4-965d-9b4930f0d061 | -11.81683 | -45.31397 | 2025-09-24 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11bb4ed0-d43c-3d0b-950b-db3837714ade | -14.98883 | -42.23679 | 2025-09-24 04:02:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 33f3837e-5dd7-3890-932f-5be6a9f5c126 | -9.64006 | -48.56461 | 2025-09-24 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f551169e-0ab9-326b-95bf-bebfe313558e | -10.84665 | -44.81199 | 2025-09-24 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6457cbcc-a423-3c48-8dd2-e87e75bd1a55 | -12.31826 | -44.21695 | 2025-09-24 04:02:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edab554d-494e-3f7b-82a7-01b7056e6c8d | -8.9682 | -47.68237 | 2025-09-24 04:02:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0655ecb-f660-3472-b6b8-a4d47b7498c1 | -13.6772 | -43.3915 | 2025-09-24 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7e523c7-e04b-3877-a79a-ed7354b38d74 | -10.33454 | -43.30398 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f91ed369-748e-318d-afc5-8fd8d8409418 | -11.6749 | -44.38275 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2355cce3-5baf-35f1-9df6-003bd6a92909 | -9.57207 | -47.57611 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 266c5bcc-e29e-36d7-9afe-8e27e1260184 | -11.52625 | -43.66295 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ee6c920-090d-36fa-986c-eb7680a4be3c | -10.85292 | -45.4162 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5868fa7f-4faf-3ec1-acd4-d9fee4ad8eb3 | -9.58412 | -47.58795 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93a87860-a964-3654-bdb9-db460dd7dee9 | -9.5642 | -47.54087 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1e383ee-c2b9-3d1c-ae9f-0a87e734f713 | -9.56709 | -47.55103 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3250f029-d7db-301f-a3d0-99eef49a9b85 | -13.96298 | -42.93129 | 2025-09-24 04:02:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3ffe8f9e-7659-36cd-acda-07e074dc9856 | -13.73566 | -43.98606 | 2025-09-24 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e84232db-a573-3154-802f-1ff7890b6710 | -10.45085 | -40.56515 | 2025-09-24 04:02:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1355ccf3-28eb-38d4-95da-86940ec63239 | -12.0574 | -44.82249 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32a69ae1-47f7-3a1b-9383-cb1bad3762d6 | -11.42251 | -44.9402 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7dd79da9-5e61-34ed-a6e2-e22922487bb5 | -11.52692 | -43.65898 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33fb2a37-ab7a-3f49-a05b-ceba5aa2bdb0 | -10.9886 | -44.42817 | 2025-09-24 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec549e4b-4e12-399e-b599-ecee871a5b1c | -11.42703 | -44.93636 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91cad985-f018-32d5-89f5-17c0731cd2cd | -11.01108 | -45.8951 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1b69c4a5-2ef8-3675-8bbf-623111fda960 | -10.84819 | -45.42051 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c2ffb11-dd56-3169-91b8-494bd529992c | -13.28596 | -39.02532 | 2025-09-24 04:02:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dddfce4b-ee99-3022-a62d-4f03045bb3fb | -11.6989 | -44.35451 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24a72c91-cdaf-3420-8561-aaf66799043d | -13.39223 | -44.19322 | 2025-09-24 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca949da4-b7cc-330b-b32b-68d73a0e8386 | -14.85165 | -40.92575 | 2025-09-24 04:02:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 91bd5355-7181-3b50-9e03-d969f26b55cc | -12.08066 | -44.77573 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cb37c7e-ddf9-3e3f-9065-95db50bad5df | -13.735 | -43.98999 | 2025-09-24 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 466a9112-9e82-3b98-9080-85405ff01f0a | -15.80779 | -45.36716 | 2025-09-24 04:02:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92a4fe9e-325d-3caf-b139-bd44a7f5fd9c | -10.84842 | -45.42258 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84f93fb4-a6f1-39c8-8136-b7c95bddb35f | -11.52559 | -43.66695 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a1e8ea2-8171-3747-8a94-b1143f93b007 | -11.62777 | -44.33057 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cac8ce7d-8f34-39d1-a4b9-75eb53b79e9e | -12.8937 | -44.65259 | 2025-09-24 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7b4ec02-c7a5-3f24-9e61-37677aedb2ad | -10.58 | -44.07107 | 2025-09-24 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fa1b61b-ffd9-3f11-b4dc-2a673fca7786 | -11.67128 | -44.38211 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d894a7c-a7d3-3fdb-923a-a255c9b6fc79 | -11.69525 | -44.37581 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb11fa5c-3883-3d6e-bd94-54c4fc60044e | -12.89008 | -44.65196 | 2025-09-24 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5228fa50-8b8a-399f-a2fd-fd258630d42d | -9.55799 | -47.54935 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da974279-e884-3d0a-b17a-0f2d540081b9 | -12.01546 | -47.78998 | 2025-09-24 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc64b302-f0ae-3a76-97d1-3af335637096 | -10.89619 | -43.63566 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5051588b-b611-3b88-b8ec-f5d56f85a945 | -16.51553 | -43.55126 | 2025-09-24 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0cc8ea68-7135-3af3-8af6-0bff0f6aea2b | -11.64008 | -44.34588 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c3ab8e4-9f18-3104-a225-04c112a60ba7 | -9.73544 | -48.65067 | 2025-09-24 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ac437a2-a590-3486-b96d-12a9dd2d0984 | -8.96357 | -47.68149 | 2025-09-24 04:02:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 146d1d30-40ca-3209-bf6e-0ba4544bce30 | -11.66694 | -44.38574 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8ed78d7-baf3-34a2-9409-fe34d94ad6e0 | -22.61267 | -49.01422 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 18430ec9-1b01-362a-8434-d1f599a72304 | -22.36236 | -49.46407 | 2025-09-24 04:04:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b00db43b-f10c-3a75-9e80-418b9f36d9a0 | -20.7054 | -56.74685 | 2025-09-24 04:04:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd91f9ae-9a61-38c6-be9c-13c3233e4e6b | -22.35957 | -46.90143 | 2025-09-24 04:04:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39df8e18-9210-3b7a-8c55-e1d5bb99b0bf | -22.37405 | -49.49206 | 2025-09-24 04:04:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31ac3e35-0d2d-3981-afa5-f860326b3a2f | -20.4497 | -45.24429 | 2025-09-24 04:04:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 392bbacd-32e5-3601-a590-5d7ed5491dcb | -21.0049 | -47.37842 | 2025-09-24 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d2cc6d6f-477c-38d9-8f6c-60bf2672e007 | -22.61195 | -49.01806 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e7383e88-7b3d-31a1-91ca-b8193980ffc4 | -22.3797 | -49.485 | 2025-09-24 04:04:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55440913-7b35-3d94-a812-a02e88a40a86 | -17.95119 | -55.86649 | 2025-09-24 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3c1ad311-9674-3209-b2a0-a064c56c70fd | -22.3764 | -49.47996 | 2025-09-24 04:04:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a1d9c77-3e8f-3fe9-aac6-1e82456ef0da | -22.37814 | -49.49306 | 2025-09-24 04:04:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d48a5a2-67fa-39c6-bff4-87cf52ce8c0d | -17.95256 | -55.86055 | 2025-09-24 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 559f9331-2174-36c2-abc0-b25a1440813a | -22.37482 | -49.48809 | 2025-09-24 04:04:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e911202d-af26-31b7-894a-1f91452f6d85 | -23.10323 | -52.09638 | 2025-09-24 04:04:00 | NOAA-20 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4f4ead09-b136-3978-90d7-ef6bdd761a66 | -18.68571 | -44.60115 | 2025-09-24 04:04:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c7c2446-a624-346a-a0a7-8c6673bbc75f | -19.31308 | -44.4836 | 2025-09-24 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38e79f6e-006a-358f-a2ab-48e957cdc27a | -22.36144 | -46.90386 | 2025-09-24 04:04:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 522e56b1-b272-3358-83cf-70de1caad680 | -22.60726 | -49.02093 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f916a0f8-5ffe-3fc5-9949-374a7e3cb563 | -21.23103 | -46.98372 | 2025-09-24 04:04:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca120096-1e96-333e-a0bc-e4e0ca4ab956 | -18.6823 | -44.60053 | 2025-09-24 04:04:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1b84926-d424-39b4-bd16-1f5927a81f8d | -19.0133 | -51.4097 | 2025-09-24 04:04:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6cacf9d-da69-37c9-8022-de7cb90a0c05 | -22.60798 | -49.01711 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1f1683fb-1827-339d-9385-b901f8bf35d7 | -20.26464 | -50.24921 | 2025-09-24 04:04:00 | NOAA-20 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc6b8e2d-1dc9-3087-ac65-10115985ffc8 | -18.53161 | -46.05262 | 2025-09-24 04:04:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 676ad9e7-edae-3396-8bb2-ad7a82ed9c29 | -17.94604 | -55.85882 | 2025-09-24 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 72cd48b1-9ce1-3db8-9513-d215868f7fa1 | -19.9748 | -44.95576 | 2025-09-24 04:04:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a259af0-5e97-3e23-900c-32e455dd2e3b | -22.61593 | -49.01895 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ebbf717c-a5fa-3be6-bbe0-5c1a0977cbde | -20.08106 | -48.28535 | 2025-09-24 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5493893d-6b1b-3ebd-9756-36f0f9f8d8f2 | -20.30261 | -46.6435 | 2025-09-24 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18febbc6-4a5d-3578-8945-b68af9dbd50d | -20.64557 | -42.57785 | 2025-09-24 04:04:00 | NOAA-20 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
