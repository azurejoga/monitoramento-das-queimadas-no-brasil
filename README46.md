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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caf238dc-4101-39ed-a3d4-85ef08a6d93f | -12.28538 | -44.1077 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1f49307-8c9d-3ca8-8f85-f113fd86d67f | -13.35255 | -47.30583 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a308bf7-03b5-32fe-8176-50aeba3ea109 | -11.76892 | -47.56122 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0368eb5a-98ca-3f65-84e8-068dd5c781b6 | -12.58213 | -41.28908 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b4ecd886-242f-3af6-97f0-d5495bf40743 | -11.44303 | -46.64119 | 2025-09-29 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1084ad6-ade8-327c-8dd0-046a734838f9 | -11.69125 | -44.31202 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe63ca63-9592-3106-83d0-ff64940eefaa | -13.81254 | -48.01702 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcc59536-ee73-34b1-b27d-e745043f877b | -13.62152 | -47.3421 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a49d4c9e-80e8-3a3e-9c62-21d146efff45 | -12.99862 | -49.44625 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 666119c0-2f10-3d33-b89f-6fc0995129eb | -15.46019 | -44.18366 | 2025-09-29 04:08:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71cd0401-48b5-3554-9b21-a490c849ced5 | -14.72129 | -45.70673 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a839c04-5180-3b83-ba1b-ebde86eb0543 | -11.61921 | -44.41063 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a309e49a-8f61-36e3-bbed-9b7ab39602ea | -15.22029 | -50.09767 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 80e9298e-614b-39d3-a63e-b766b59edfc0 | -10.8087 | -46.66887 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f564bb47-0f58-32dd-a403-5a05b3d0e389 | -11.91905 | -44.7622 | 2025-09-29 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24876bb9-43ed-3f0b-9604-58436ad28466 | -9.27775 | -45.73531 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 428402b9-c1cf-3d4a-b94e-a84817598b38 | -15.42828 | -48.24468 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30a6279d-50ff-391a-9804-8a1df9884f49 | -12.17341 | -43.55822 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fa0a36d-dd36-3acc-ba18-6fcf20c964f2 | -8.71799 | -47.97945 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16629bc8-cbcc-3699-938c-21fbbd58e5e2 | -14.77307 | -40.08981 | 2025-09-29 04:08:00 | NOAA-20 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e36050fe-9ef2-3ba9-ae89-1e03c82b0103 | -15.08689 | -48.32539 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b47e731b-ba4c-330a-b84c-5418b117eafa | -13.58032 | -48.10173 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de0ba4e1-5179-398f-86d2-749cfa59123b | -11.69239 | -44.47681 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac9d9bd6-d6fa-3073-bab4-1a358f716756 | -12.85166 | -46.96671 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8bf21b2c-5e3d-325f-a494-b982cefa8d8f | -12.84693 | -46.88245 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62aabe9a-cfe4-3e70-bfc7-c5a541525c76 | -15.28373 | -49.5045 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d5e96cc-73f6-3c9f-b06b-0208bf618fe8 | -12.58157 | -41.29277 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c1047aee-6c33-3020-b481-832b3ff70579 | -13.80723 | -47.90777 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fab25c36-229a-3c27-a216-05db276559b7 | -15.27186 | -40.01512 | 2025-09-29 04:08:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5661e574-7aed-3c7f-add0-1c58f657d790 | -11.81054 | -51.80733 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf830a40-4dff-37ad-b63f-d2e230437438 | -14.78592 | -45.69326 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 492ad6b3-6be0-3a15-93be-af8867642baf | -9.45942 | -45.499 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28babf32-2411-3760-8136-c1994066b466 | -13.42102 | -48.20156 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbbf9194-c453-388a-8891-7ff1502b9c15 | -12.77091 | -46.84988 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f658a9c-7fd0-3a0c-bbb4-582966fe49f1 | -12.65351 | -46.92167 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a681118a-9976-3bc2-898e-472fefab296a | -11.99056 | -46.59496 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9367d972-cab9-36fb-a25a-dd7587286343 | -15.52141 | -47.92611 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f79a31bb-bc84-3038-be6d-f2e14bdb64ff | -14.52404 | -48.40244 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a81fc938-dfe7-3e66-a9d4-b6346d790dec | -11.83404 | -51.7963 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 46f82d9f-678c-33af-81be-4b1b8acfe1df | -11.82423 | -51.79084 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0d4b3312-48fe-3ecc-a037-1037f6814159 | -16.79949 | -42.16085 | 2025-09-29 04:08:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0879ad3d-9a56-3afd-a68b-00313f126162 | -15.19381 | -48.47144 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d616187d-0a2b-3e92-ad31-55dd32abb9a6 | -12.79539 | -47.74727 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57411b47-031c-3e12-88ac-bde96643e57c | -9.05335 | -46.71019 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| afa225b4-9789-36d5-8d57-122ffb1f6258 | -15.33853 | -47.90803 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb4685e9-7192-3e99-92ee-7686395e31fe | -15.49179 | -45.87845 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bed8e32d-618f-3e5f-be31-b849ede31950 | -9.77043 | -46.19995 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d336672-5ba8-36d7-a586-11e706c2e5bb | -8.78195 | -44.94627 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d3b3652-4850-3763-9fa2-e59e33abae67 | -14.575 | -48.23467 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae9afa08-6ade-3bd3-a4a8-95c5cc57439e | -11.36643 | -44.94456 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0b7735c-3a1f-3224-b7f4-2369318d5cf3 | -15.18927 | -50.09259 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8234ee6c-f66f-3165-bc42-417ffe86b0ff | -10.62336 | -48.53366 | 2025-09-29 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 772006d3-5ec5-3b46-b256-1a728ff85380 | -15.05398 | -42.33894 | 2025-09-29 04:08:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3cbb0048-2cf4-3937-82a1-ba6f419f0772 | -11.81018 | -48.23345 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 477859b7-abfd-32f3-91bb-6087adca428c | -12.2832 | -44.09985 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c4df4bd-53fd-3577-8d34-cd6501fa423b | -11.69786 | -44.44313 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6874467c-1c47-3726-a062-fae38fee8a74 | -12.69855 | -46.88521 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08af97dd-b22c-3bde-b145-c0841cc2fb68 | -15.16082 | -46.41359 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 673b8d17-1813-3815-ba21-51e5650ea397 | -14.76895 | -48.18639 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d06b152a-e697-3007-a496-61b572cff280 | -12.96731 | -46.86106 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f26117a5-fccc-3ec5-a90f-00851f9f8201 | -13.60447 | -48.06911 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe5f44f5-2d73-375c-8c79-3d7f1c4f9739 | -12.00941 | -47.78976 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2055a03a-aa64-3599-8820-88afad667ec7 | -12.96347 | -45.17527 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8965056e-2a95-3a98-9504-7ff8b2694e11 | -15.49055 | -45.8748 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaa94116-4af5-33ed-acc2-ddd9c3114ea8 | -10.40343 | -48.15626 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a2a2f14-6741-3286-aee2-1b540eef0005 | -9.95171 | -43.59504 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a178f64-0391-3c66-aa59-9b68bd6c6178 | -9.07424 | -47.60521 | 2025-09-29 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b30467d5-e963-33fe-98d3-34d38c4d3ed6 | -13.38383 | -48.15404 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9d580e61-0763-3a0e-be28-f88162162cfa | -10.60117 | -46.29263 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bba63334-056f-3112-af8f-630be41a2c7b | -13.61617 | -47.31193 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5408dce4-ffac-3872-8b33-42f75bf0c9ff | -13.60548 | -48.06348 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc68c7db-38a8-38e6-9c7f-5ccb0e1a38e4 | -14.49412 | -48.54348 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17c3f20a-a0c5-3ef1-9d2f-e2b544e3ac6a | -15.81234 | -46.03989 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afc96a27-069b-3f7c-932b-8988f16810d3 | -11.45026 | -47.28896 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81788606-b629-3fc5-8328-f15c4224ba0f | -15.28498 | -49.51739 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 98b2274e-7a95-3912-8ee7-95c0a7c71fbc | -11.69506 | -44.43882 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20aa0e42-7186-363c-b2d2-8f6b68d48b8f | -11.4472 | -47.28315 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1f568d4-ce38-3de0-8714-69e45297fb17 | -11.6194 | -52.86463 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8008e04c-a358-3b9e-9eb5-fa8de07374a3 | -15.6157 | -46.25513 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72cf7123-18cf-3cf9-8c94-d8f5a002cb5f | -10.39835 | -48.16053 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3ca9b82c-99b7-3f80-aa29-c9af9b9769ab | -10.22549 | -43.03212 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| baeb550a-d668-3c0b-8a8f-9db521136452 | -15.53856 | -47.8739 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92b313d4-7ff8-3759-aa96-f9b5a0283855 | -15.49525 | -45.8791 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4456ddf2-caf0-3471-8012-99fef5d87fff | -15.03111 | -46.97519 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b605929c-3304-34cb-9ce5-3d607dc82cf9 | -15.70688 | -47.79934 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cffd4189-5f1d-322a-8635-fc9585c90ff7 | -9.38588 | -47.61287 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5909d496-564f-35ca-ae16-4545017eef7e | -14.83873 | -45.5696 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52382156-32bd-3363-b97a-81c7d4908dda | -13.02638 | -49.44131 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5863b389-2f8f-3d10-97bf-cda6bb629e16 | -8.88328 | -47.62878 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d58e591-f16b-3f79-9d1a-6f053846a55c | -11.81885 | -51.79195 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c861ba72-1ffe-36c9-b773-61f9c82bd077 | -15.79563 | -45.39031 | 2025-09-29 04:08:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86007d4b-c97f-3f34-bad9-fd033dcb16ca | -12.17284 | -43.56178 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6dc6b96-fbbf-364e-898b-01bdbca8a101 | -14.5843 | -48.27406 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5685d6f-52fd-37a5-a086-2971912c5d4e | -13.63391 | -47.33874 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e199c8-1b1f-37fd-ad07-47bb4268c558 | -15.28724 | -49.50934 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 71f5ea35-6bd0-3c19-9da9-e53aa2d25dab | -12.85382 | -45.18102 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93cd69bd-60cd-3585-afb5-51e50a836134 | -13.42401 | -46.54234 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c49c0782-9c25-3a5e-9d4c-079e58bce51b | -15.53816 | -47.38798 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abad198f-47aa-3f7f-b2a2-0c2a373bdb65 | -13.58131 | -48.10608 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 495ada81-0bac-3af7-bf57-be61be1735ce | -11.8099 | -51.81074 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
