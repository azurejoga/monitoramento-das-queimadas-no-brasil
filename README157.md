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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1295dc8-ccfe-3a37-967d-598f357ada4f | -11.84793 | -43.53993 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 3b6f96bb-a409-35cd-8c0a-7c5e9ef841e9 | -11.1495 | -47.29607 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d6b6b1f2-cf96-3751-bace-e1375d3a9522 | -8.91297 | -47.25774 | 2026-10-07 16:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 005cc4c3-2c89-322b-b356-e80fbbc69697 | -11.22947 | -45.27564 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2524edf5-88b0-389c-bb58-88fbda1404bc | -11.83789 | -43.5332 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c18d2005-ded2-37db-aa68-22b3f5dc8a87 | -9.37036 | -50.65662 | 2026-10-07 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 06e41918-cf9f-3ad3-a61a-f2d4e4bddc99 | -11.62341 | -43.64168 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a394b291-83e0-322a-8a21-43c284898bf2 | -10.07589 | -45.98197 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 7729dd25-33b3-3013-b420-a58e41cfde25 | -8.96216 | -47.55561 | 2026-10-07 16:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8c25818d-e638-332e-9c55-e950ff873838 | -11.10947 | -45.69512 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3654a85b-0bb4-3602-8173-74f8d5ab1e18 | -13.64164 | -39.69303 | 2026-10-07 16:01:00 | NOAA-21 | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a31c2a00-f77b-3048-b372-d5d41ea94964 | -11.33211 | -46.66573 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fc473b3e-1a81-3ed7-b5cd-a71ec20eb9bc | -8.81311 | -47.92209 | 2026-10-07 16:01:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 416b914b-4fe3-319f-94cf-6b91082747e6 | -9.9275 | -45.74242 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d00b8de3-c77d-3a09-9ed7-009f1cb74123 | -7.82801 | -34.845 | 2026-10-07 16:01:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8109c3cc-1bbc-3e2e-944b-099d4589d7dd | -12.50196 | -38.68573 | 2026-10-07 16:01:00 | NOAA-21 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 26ace4fe-e761-3f1a-ab10-cfd6ff93d18c | -12.20352 | -44.65303 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f84f1624-50d0-3920-be63-4897fffda9c4 | -7.64017 | -37.56657 | 2026-10-07 16:01:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a6572897-702a-39ff-808b-1b0c24886c46 | -12.2235 | -44.73513 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| a45fc044-806e-3035-85b1-567777ee87d0 | -10.57301 | -47.28344 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8cb2b87a-7e18-3b11-92c2-efbdeaf95b95 | -10.87851 | -47.60227 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 5c8ca835-d03f-35f0-92a1-a5ec096a160d | -12.17918 | -44.75832 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 15ac6951-01dd-34dd-8681-9955725e3d54 | -9.15792 | -37.69499 | 2026-10-07 16:01:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ea0f55ca-36c9-3a0a-9fb1-02226436ac96 | -9.82237 | -47.47775 | 2026-10-07 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1fd90542-6dff-3cd2-a441-a2cd244f56ad | -11.61738 | -43.66549 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 38b33332-76eb-3d48-8242-57ac56bb10e8 | -11.15471 | -46.18332 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7c71e02c-92dd-3fca-8a69-9b93ea4e6f02 | -11.84151 | -43.56019 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5dc624e0-e910-3a6c-874d-53abd709cfd0 | -11.43621 | -45.57401 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f294e589-c862-3b09-b059-5117c34a0a64 | -13.59138 | -43.16917 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 5fa3aa96-f683-3fda-a445-65fa4507758c | -13.4459 | -43.45245 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7e85dd94-4114-32f9-83c2-4d0032bd4660 | -9.86675 | -46.31102 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b6e6edb6-44db-3bd3-9800-1af07ffc778c | -10.12593 | -46.85329 | 2026-10-07 16:01:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70d87ce4-d353-398f-a8f6-6248b752462c | -9.42559 | -46.33183 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4aac9746-5441-37e7-9792-ea9b4369738f | -11.00134 | -45.48307 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 7c02fa45-b6dd-391f-8d71-3dd868ffb176 | -9.38393 | -45.92256 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 22b9bbcf-faed-30f0-9c24-5dd4bbcb9087 | -13.32069 | -38.97809 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bb29f437-c597-3368-9e54-392b5b357951 | -10.97608 | -45.40693 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4f7217d3-5596-38ea-8d09-8c9acb168882 | -11.10121 | -47.58793 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 947650ff-ff4a-362f-8ab4-ec700a31d5a7 | -12.17146 | -44.73674 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cd16efbb-a520-3cf2-ac85-23bb7b2c02d2 | -8.91067 | -44.5508 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a09450f-f68d-324a-b68a-e07502526dbc | -10.34455 | -46.24001 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 230d1529-8913-319e-8b35-2b4233807818 | -11.0141 | -47.97755 | 2026-10-07 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c2378c51-c5f8-3dfc-a0c7-d067de397f8d | -11.08856 | -45.6538 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 98841cb0-5929-3e0a-8f4e-cec4dbc81ed7 | -11.64108 | -43.67079 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| cf512559-4cd0-3378-8f63-cd7fb007b30d | -12.16585 | -44.73175 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ff929d06-cbcb-34cf-abb0-f532dd7a4468 | -11.85046 | -43.55869 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 73bb0370-f537-34d2-ac55-66469c738cb9 | -11.83704 | -47.36752 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 122aee9b-7bcb-352d-a67a-ed11939086d3 | -10.27304 | -47.03806 | 2026-10-07 16:01:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79d5235b-0aba-3b25-8ae0-346e3392bd83 | -9.45683 | -44.61376 | 2026-10-07 16:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8f81dae1-b7ad-34b1-8d94-ba376409bb98 | -11.08779 | -45.64766 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| de7dc8e2-5ed9-3741-8e66-7e94e4be3215 | -9.14027 | -45.09734 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8dc70af9-2b2c-3823-8058-cf17147a9040 | -9.40016 | -45.88749 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 85197091-c982-32fd-9869-0b3f04a46030 | -11.62699 | -43.66861 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c98d31c5-6128-32ed-a04f-6b91eedcdd52 | -13.37309 | -43.87103 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| c7f5938a-c7ba-32e9-a1df-6ac4ed086d10 | -8.63885 | -44.89199 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7f3f30f1-4848-3e58-8bf5-ba4bbba0081c | -11.84308 | -43.55601 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0e390257-6c35-35c9-8649-da462fda24eb | -8.59074 | -45.6787 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 26ad3347-bceb-3311-9f03-6d4df5d12e1e | -10.99472 | -45.47176 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c572e60c-9ae3-34f9-9c3e-e3451e586e3a | -9.42036 | -46.33265 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 842a4a4f-5efb-3988-a2c0-21b68a88dff3 | -12.26496 | -44.43714 | 2026-10-07 16:01:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7c98f6b5-809b-3948-aec5-12de14780285 | -10.78823 | -46.53819 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2abf77ef-33d7-3235-a56f-07a004a01782 | -11.38717 | -46.70229 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 635355c2-2a17-3bb2-9300-0f7baaa0a8ee | -11.64685 | -43.67945 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a808c034-a735-3536-91ad-793f7d964d7c | -14.75501 | -49.25357 | 2026-10-07 16:01:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 50a1a112-e13b-33df-82fb-d19b8124ffca | -9.21564 | -46.68844 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 519e4bfa-2151-375f-9db7-02f0f511153d | -11.36731 | -46.72332 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35aca63b-714f-3410-a529-4e260e62f32d | -9.99504 | -46.02039 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 71574638-98f2-3157-827b-8726f92c886a | -9.91222 | -44.80608 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 824f1679-8432-3268-9901-6c938729d541 | -7.36627 | -34.81556 | 2026-10-07 16:01:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| e2041847-b75c-3712-a109-68768bca33e2 | -9.95619 | -45.9645 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| d8a24ffb-5982-37ce-8caf-feb8972bbf37 | -10.46027 | -46.83235 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 1555fc1c-23a0-3fb1-b7b7-0221325708b6 | -11.06326 | -43.17189 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f5d94703-7bb7-35c1-8870-6d8f03f00999 | -8.78616 | -47.57729 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d4fbbdc2-d425-3502-848a-2151d441db64 | -12.22472 | -44.7248 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ead807cd-a7e3-30c8-af7d-fd1bf6577170 | -9.9163 | -44.80021 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 9d080501-077c-3219-8c8a-1dbbebd30431 | -9.12649 | -45.10243 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 421.5 |
| a28adda8-cead-3ea9-884a-fae7ebf1eebc | -9.38465 | -45.92822 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c40ee20d-24b3-39ba-ae9b-b901cfcdc32d | -9.6415 | -46.09713 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 926ba20f-f1ab-3b90-a7dd-b7e37f6b0f76 | -11.84087 | -43.55543 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 7e45e926-4ee4-371b-b309-197b86aee00a | -9.8629 | -46.07225 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7e065363-5dd1-3cb8-898c-210bc1c7f7ae | -9.53602 | -46.85708 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2419900c-b653-3c03-961c-4e9f301e083e | -9.40049 | -47.33307 | 2026-10-07 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 028c6d4a-3792-31fa-b000-1259d3971fb5 | -9.77816 | -45.92042 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0d9d8d6-343c-3a9a-8e47-3fa4048323db | -11.76814 | -47.73615 | 2026-10-07 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 328f7138-5de0-37a1-a2dc-9407137704a4 | -10.24656 | -44.64062 | 2026-10-07 16:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6c3e4cae-eae0-3b56-b6ce-e4f6bc1dbd7d | -11.23125 | -45.24906 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 559c0997-894a-3556-8a83-c3b6d4df97c4 | -11.33809 | -46.6688 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d4d1813d-7a68-356c-99c6-a0bfa5f6a258 | -12.2145 | -44.70225 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3c4ddc19-82fe-38fb-a369-9db189e49ad0 | -8.80036 | -49.00964 | 2026-10-07 16:01:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f02b159c-b813-38f6-ba37-488d1df2d937 | -9.15156 | -45.82188 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 680791ea-f32a-3795-a6fe-8bfb0e592650 | -9.93141 | -45.73277 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a0cf9913-00c0-31b3-a18d-6ad8f0f8408d | -12.83122 | -45.5689 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2e3c975c-311d-3981-a65e-fe1de380031e | -9.0286 | -37.33424 | 2026-10-07 16:01:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 0b9ace19-ae02-39b5-bf3a-ecfbc9fb3c82 | -11.38367 | -46.67507 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9c07d86b-b6a6-303d-91a2-d54815301cd6 | -13.24613 | -47.00029 | 2026-10-07 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 68808c0a-2a80-3df7-9ef6-bb75ccaf6b9d | -8.58657 | -45.67585 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bea4bb72-99fa-32b4-ac6b-318ac0fdcc49 | -12.20357 | -48.4228 | 2026-10-07 16:01:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 7f663fd5-bdeb-30f8-af5e-50bf2ae3a71c | -9.38429 | -45.92538 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf784931-271c-33db-ae58-71f8c5f3ba47 | -11.23347 | -44.87191 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 264438ed-56f5-3c27-9e8b-28d8ae531b68 | -11.01349 | -47.97264 | 2026-10-07 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README158.md)
