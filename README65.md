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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0726f54a-d651-30b4-adb4-207c6ef328f0 | -7.47821 | -42.85015 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73f5b385-e0bd-36cb-a5a8-ac49898db072 | -11.72059 | -43.63961 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 257e9651-44f9-3ce6-8cc3-dfd52242db6f | -10.28889 | -46.61259 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dad379bd-f7a3-3e63-bd2a-5017de29314b | -11.3139 | -44.83406 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| f7b030f3-cff9-3553-a815-ddccab4dfbcc | -11.99455 | -43.47629 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 320241cd-80ab-3cc1-922c-c847a1904ec4 | -7.33984 | -45.30812 | 2026-10-09 03:45:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62858cf6-da12-36c4-91c0-372f9ad8f16c | -11.65667 | -43.68427 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90cff1b9-b08c-3a10-a008-94ca49aee03a | -11.41636 | -47.58957 | 2026-10-09 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 305ee49f-dbfa-348a-9bf5-67dd3b7ce6f1 | -9.0344 | -44.38816 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 650ab255-91c9-3f87-85d0-fc6c13d792ee | -10.32229 | -46.60863 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0e768aa3-8c8f-3ce8-aaa6-41e49599e799 | -13.35157 | -39.26953 | 2026-10-09 03:45:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce91fa53-1c8f-3a0f-8d07-a157dce2d205 | -8.72792 | -45.1632 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a09233c7-854d-3f89-84fd-352ed83eec9a | -13.49793 | -44.37677 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0682f3e0-c812-3561-9aa2-d0de8f683fe9 | -8.90401 | -45.22154 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 4a6e2c84-c467-3cbe-a7fa-dd3e6d08fac3 | -10.86884 | -44.81066 | 2026-10-09 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15fb9739-272c-34cd-8a0e-f0026a4d154b | -11.83917 | -43.58699 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5df942c-df8d-3e3a-80e7-96f6967bf24a | -11.0674 | -44.08717 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6968313-c590-38ee-8ae0-70c1b91feff5 | -12.0051 | -43.4753 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd007eb8-1cef-3850-924e-d09394de85a1 | -8.97713 | -45.90942 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a819031a-a009-3aa4-92c5-cda0eff098b5 | -8.72876 | -45.1588 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6732e239-2e0e-3f96-a77d-9400745db062 | -11.58873 | -43.65242 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bb1d7ed-774c-3efd-8731-b12aa5a63f19 | -9.01213 | -44.38342 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f0740c4-17e2-3dac-a8f1-3d61be2cc9d5 | -11.01272 | -45.43128 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 90bcc3a0-d592-3334-ba23-82a5851412f6 | -11.76745 | -43.53082 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 911852a3-c866-34c1-a6e6-655c88c12830 | -11.60698 | -43.69523 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc80f7c5-cdce-3036-8e87-7e3a88a3e081 | -12.01617 | -43.44389 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fd6623c-2688-37f0-8de4-408643557045 | -11.77406 | -45.55803 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed37124d-a05a-39f8-ad29-0a52b8cabc34 | -11.84923 | -43.53424 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7633b8c8-f36b-3a4d-8b84-ea6a45538abc | -11.6097 | -43.70881 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f25dbb04-357b-3001-a935-b53636503f59 | -7.50581 | -45.76694 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db00c2b5-d5b4-3772-9b76-7b715ea25af2 | -8.74298 | -45.14824 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7063a1f3-6eb1-3fc4-a617-32999b338433 | -7.39983 | -44.7498 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e18597cd-c057-304a-98a0-6b8d3c0ac4b6 | -10.58011 | -46.29372 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cab352ba-6f0f-397d-a76d-95193f0d4534 | -14.22104 | -41.66741 | 2026-10-09 03:45:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ccca2afa-3f17-30d1-8caf-2995a599cba9 | -10.90484 | -45.52666 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fae2974e-b0b3-3479-9e55-aabca4534baf | -11.71614 | -43.63535 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a64e49c8-7b6f-3360-a78a-047bc974e02b | -14.05036 | -43.83342 | 2026-10-09 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3a2912c-a5d0-3750-ad8e-d204e9341edd | -11.74705 | -43.63892 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d74e82fb-f84a-32fc-a1a2-12d9c97b97f6 | -6.96091 | -45.27475 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 38ba35d1-4119-3450-b0ed-bfca1654bc87 | -11.99564 | -43.47052 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 059e54a4-4638-3653-93bc-e85920ac1e56 | -10.89682 | -45.53192 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ac7e137-aa23-36dc-824f-f13db73927cf | -12.81556 | -44.64509 | 2026-10-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3766afb-5cfb-3052-b144-738bc994c5a4 | -7.31124 | -43.98274 | 2026-10-09 03:45:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a31a27bd-cc51-3969-9c4c-e63e2b782b60 | -11.21777 | -45.24108 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 310d0a13-4aa9-3441-b863-9993d8754bb7 | -7.50751 | -45.77168 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2f9daf1e-e9e6-36c2-b870-9261a1a2762e | -8.96378 | -45.91694 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4784070-ac2c-3982-a696-17495844ad21 | -8.90076 | -45.23908 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2941b56b-ce69-37b8-9bbf-94e30c2b83a3 | -11.6127 | -43.6099 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc6bd7de-1802-378b-a4ea-01bf1a2c9328 | -12.63361 | -40.9051 | 2026-10-09 03:45:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c971cf77-6ef5-3df0-a840-057fd64c3042 | -11.76749 | -44.95817 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69fd6f24-b059-3a3b-acf1-caf4abbbb550 | -8.84348 | -45.42625 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6faf534-f429-3688-a3fb-a12d2029f6db | -11.07046 | -44.01185 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a511d47-9f45-3f45-b2f8-45bf89b2c0f7 | -13.81792 | -39.90978 | 2026-10-09 03:45:00 | NOAA-20 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 21b156a6-2c44-3ddf-9273-465e87bcbe88 | -9.29303 | -47.44239 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 61f91595-d066-33db-9b0c-8b30b90f1865 | -9.9125 | -44.79128 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92834b96-930c-31b0-99b1-e0b872eadc97 | -13.35075 | -43.97027 | 2026-10-09 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c79bfe1a-f469-3099-9e5e-abc3ad99023e | -13.2624 | -44.00118 | 2026-10-09 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdc6beea-9a1c-3695-872a-4ec95e1f4fa0 | -11.84192 | -43.60008 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1eb63fc-fe53-3f05-8257-860d6a2839ee | -10.59334 | -46.41531 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99d8e52d-6bf0-3827-8199-99b172ffb0be | -11.07676 | -44.08837 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b816124-9c1b-353d-b814-7ae6ee62c1e1 | -8.9083 | -45.23139 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 392f6943-6b0d-335c-88cf-86e5e9246d62 | -12.0351 | -43.4532 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41c27792-2dd3-3c7d-8001-61175be130a4 | -11.46456 | -43.38566 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 863dac89-0c50-38ab-89db-e7b7b7d08208 | -11.76263 | -44.95369 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33537ab0-c508-309a-8e85-dc80ec8aadf4 | -9.3028 | -47.4636 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b897f775-e2d1-382e-b4d3-912944e94725 | -13.63455 | -44.42527 | 2026-10-09 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe82eea5-d7e9-3872-9373-56f4b090c82f | -11.62218 | -43.69887 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd62ed83-fa38-3bf3-b667-afd633bb283f | -11.29738 | -44.83047 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4396726a-222d-300b-9b4b-910661813f39 | -12.02555 | -43.449 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a5c7ef6-3fc7-30da-b828-ca4206c4b4dd | -11.06542 | -44.0619 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa0af537-cc8a-3042-b970-76f1f21636d6 | -8.73547 | -45.15567 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e6b2cae-e68c-3b50-af12-0247b660f825 | -9.86763 | -44.87268 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ce45439-323e-3593-afcd-5133446fe0a6 | -11.86159 | -43.60685 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa504f0d-e43c-36df-a057-f28ca016a21d | -12.00914 | -43.48134 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73be86fb-1444-3262-8d62-ec749694c8c0 | -8.97764 | -45.91117 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a816fd7-c20b-3fc1-866b-89c55296c92c | -11.99798 | -43.48558 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 316ed74f-6e5b-3340-a191-6c4c8a42b2d5 | -11.99148 | -43.49252 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6927a474-baec-3652-8440-f2056b6b4321 | -12.00892 | -43.45494 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2899919-5988-3adf-9d52-8a76a131eab7 | -8.73294 | -45.169 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e184bd4c-1b2d-3654-bd09-f0311608d815 | -11.27384 | -45.19456 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddfdd823-96b3-380c-9144-83fc1db973b0 | -6.87618 | -45.89959 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d02adaa2-c64b-30f4-b1ac-5112f9394055 | -11.08875 | -43.99776 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7abf52c2-2d0f-302a-a4f1-e1b60b8d34c3 | -11.85431 | -43.58999 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a22e162-f9e2-36d7-b3f8-74fa081b875a | -11.23677 | -44.87587 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39d67734-1b04-34cf-8b8b-caecb6e60ed6 | -8.97857 | -45.90623 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c1237c3-2b83-3345-9f85-ae22773242ec | -13.25719 | -42.2564 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f1c8a7a-bd4e-3b9c-8ce6-071107485c2a | -11.1784 | -45.32139 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 331709e0-a165-3410-961b-77b7042ada16 | -11.00859 | -45.42156 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| af4781a7-717f-35e1-b9a4-1efcad8ee91f | -12.00341 | -43.45675 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3dfb0e8-9b71-31bb-9285-c13531cc8ef1 | -13.11912 | -46.33164 | 2026-10-09 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b639c0d-839b-3ca1-98d8-130d04359842 | -11.72118 | -43.63653 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e309457-d468-3b18-b3d8-12dd40211269 | -7.51113 | -45.77299 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46ff31c4-18ca-3b04-9629-a20f8f2f7134 | -11.63792 | -43.69961 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3ad70f2-3b6d-390d-adac-50517bfe94dd | -11.00699 | -45.42991 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b842614b-5fdb-3eac-8ac4-fc86ef8d857d | -11.6263 | -43.59379 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa3209d5-1fad-3104-a5c7-58f7e77621f8 | -11.25244 | -45.25474 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07ddc159-24ab-3b0b-a8cd-7b3415868613 | -9.40423 | -35.55703 | 2026-10-09 03:45:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| baddd872-d3ef-3a1d-964c-6071d1353bd5 | -12.00781 | -43.46088 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73d93ca4-2428-3859-b59d-730555893870 | -14.08117 | -43.78048 | 2026-10-09 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daffd844-db6b-3f2b-85c7-75e691e83c66 | -11.09098 | -44.04289 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README66.md)
