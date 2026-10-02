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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba47c7c3-97e9-33f4-a905-dadfc5127872 | -11.71619 | -43.42671 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 56abeede-6069-3da9-b9f4-fb3cbcc1f5ae | -11.38635 | -43.35928 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d1895cd3-56f2-3db8-a162-352c8d7f12c9 | -11.70461 | -43.61842 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b55b73c4-c236-3cae-b7a6-4c095d94e43a | -11.47324 | -43.41124 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b3334174-a70e-3d82-a0a6-f48ff528c6db | -8.56542 | -44.13141 | 2026-10-02 15:54:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4de54533-5bbb-3462-81b4-61ca097b2992 | -11.6946 | -43.62 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aa09084b-1a26-3ff3-b6bf-5824083782ca | -9.84896 | -44.8314 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b80e803c-29c6-3108-aece-1384f0843ba7 | -10.65977 | -40.47437 | 2026-10-02 15:54:00 | NOAA-21 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 600b8c04-bf0f-3ff9-958b-22e3f8c4e07c | -12.52234 | -41.60169 | 2026-10-02 15:54:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c58a39e6-4a39-377d-94a1-1afcf8f1fc34 | -11.70928 | -43.61498 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ea9f031b-486c-30b6-8b20-4ab5cb258dec | -11.4717 | -43.51501 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 596af51a-db11-384f-8abb-3b3cfb5cabb1 | -11.80482 | -43.56421 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d5016f0a-9997-3708-b566-75dab4043e6d | -11.697 | -43.59909 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dba7a5da-c37d-3654-8492-d049b0f4eaf8 | -7.48412 | -42.80297 | 2026-10-02 15:54:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 654439f8-5407-32d4-83e1-8f0c5b546ff0 | -11.25978 | -43.5265 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8608954f-ac7d-3fa7-865f-46088a40f917 | -11.46405 | -43.40532 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 46f5db3f-65ee-39d8-bfb7-3fe206658b22 | -11.47052 | -43.42876 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1528d48a-8fbf-3d6a-b4fd-c151f29ae312 | -13.34394 | -43.84427 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 00637ac9-b5f2-3fbb-aa6c-5aa3fa740956 | -11.46335 | -43.39966 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 6ab6ee93-093b-3047-a7bf-9b61c9288e0b | -11.65489 | -43.54861 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9571551a-beb9-3e6f-a0bc-2ecc80693380 | -11.75617 | -43.54324 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 924fd45d-4642-316c-bf03-774a6652a319 | -13.35668 | -43.85424 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 3f1cd82d-bebc-38dd-b322-d853fe32306d | -12.78755 | -45.13389 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| cad3cd3d-ac1c-3e5a-bfed-bd555d93e993 | -11.71948 | -43.61708 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 2561ca0a-ad62-381e-a4ee-52b1e4a99096 | -8.57751 | -36.12062 | 2026-10-02 15:54:00 | NOAA-21 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9de10096-39e6-31d9-b63d-52d2cbcbf8f8 | -12.49912 | -44.14178 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0d1fd854-caf5-3d13-a58e-57a01bad8684 | -11.76117 | -43.5426 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c7928a44-d90f-316a-9400-cfb2ddd09e58 | -10.9215 | -43.84032 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eeaee10e-19ac-33f4-a3a0-bf17baf8b3ca | -11.7124 | -43.59977 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| af4018d7-6d1d-30da-b465-c8bb48f50af1 | -9.80876 | -44.80554 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92558777-0366-3111-b9f4-4b73adab7e63 | -13.34075 | -43.86132 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6065b4a-8b58-3a03-a0e2-ad05e6f333f0 | -11.25264 | -43.51875 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 1a912dfc-2af5-3561-8290-3350a61b1609 | -12.58595 | -42.11045 | 2026-10-02 15:54:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 8088299a-c5e1-37a0-8437-6055cc6ea088 | -11.74817 | -43.44009 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f91a823f-6bc9-3d95-b50b-bce82f246e87 | -11.31774 | -44.26851 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| c2fe9263-688f-3a86-b26a-b9b85b792ede | -11.43078 | -43.39353 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4c173dd9-9308-30de-ae8b-2b46a970c534 | -9.87396 | -45.47849 | 2026-10-02 15:54:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 48ae181b-25ac-3f7c-962c-524405e8316e | -8.58599 | -36.08739 | 2026-10-02 15:54:00 | NOAA-21 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e577656c-a069-3f96-ae99-6bc0643d5117 | -9.46299 | -35.84056 | 2026-10-02 15:54:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 37ef600c-97c2-3439-85b6-0b09b9770151 | -13.26999 | -43.41685 | 2026-10-02 15:54:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 60be1359-adca-3026-bae9-d41d606cf21c | -9.9424 | -43.46242 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 181795cb-5501-3ed1-8df4-5902b2c9d859 | -11.78578 | -43.57594 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d5869fba-870b-30a8-b744-c1d1dac3fad3 | -10.95123 | -42.37011 | 2026-10-02 15:54:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f562e259-2ec2-3ba4-bb86-e7c0de74dc20 | -12.52279 | -41.59976 | 2026-10-02 15:54:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 636726fd-7f93-3dd9-a0f9-7247d768a6d4 | -12.26424 | -42.15007 | 2026-10-02 15:54:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 80aa33d7-21c1-3bb9-9e35-d79152132d86 | -11.59841 | -43.54377 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ca860b59-b0c3-339e-a285-742716b9f6e0 | -11.78807 | -43.55396 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 3fc12411-2f06-380e-8193-3af94ee162e6 | -12.20776 | -42.11243 | 2026-10-02 15:54:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 659dcf21-61cb-308f-8aa8-838e50c63dd2 | -11.41213 | -44.89093 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| e0d616eb-76f9-37ef-a937-3ddab709d814 | -11.25667 | -44.2465 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 80109638-a7bc-3fa4-9bad-234297feb11d | -11.45272 | -43.40794 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 60beb4f5-be63-317e-9971-15cb20320c98 | -11.4626 | -43.40672 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e207470a-a6cd-3c93-a5c0-da4957f5f6bd | -13.34957 | -43.8469 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 7753cc06-1a32-353b-9f60-ebaef0d1191d | -9.95143 | -43.45612 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f643f9bf-5976-3375-bee7-46f2493277a7 | -11.47893 | -43.41625 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 354.0 |
| 269fa332-fa90-3b4a-962b-ee11028ed374 | -12.86515 | -42.75371 | 2026-10-02 15:54:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 83.9 |
| a7ac843e-d53e-38d7-9ef7-e3438646bebe | -12.77148 | -45.14345 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 30c9c9ab-2070-36d8-aeb9-a1bc1c24acea | -11.71985 | -43.62011 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3ced22ab-8502-3466-b51e-8b26e53526e6 | -11.47621 | -43.43379 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 104df0c0-f5d4-321d-8e11-222c34bc6b10 | -11.15638 | -44.59937 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f5c901be-3bf0-3776-88c8-2630129a2aab | -11.8488 | -44.74685 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d1bbe852-5840-3f76-90fa-9045daaa243b | -13.36229 | -43.8569 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 425d2d60-3e6c-311e-b2b8-843b56e19995 | -11.70381 | -43.61421 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0af74a29-bce5-338c-be03-8592ef8f358c | -11.67915 | -43.49524 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2485f397-9059-3a15-9663-f225e6f207f2 | -13.34508 | -43.84572 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| aa539135-683b-3d6b-89b9-6fdff64f2b3c | -12.51525 | -44.14256 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c1e690cb-24b4-31ea-846e-cc5d891ffaa9 | -8.12173 | -44.79643 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 888ac085-444a-31c5-a1de-09bfdc9670a3 | -11.45693 | -43.40171 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9176c70d-b91f-3498-a414-357bcb0cf345 | -11.63912 | -42.93051 | 2026-10-02 15:54:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 36d715ad-3d4d-3acb-a7e7-8d0749030122 | -11.66365 | -43.61769 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0a187f1-451e-38ff-9f6e-fc623d0971ae | -7.07426 | -42.28961 | 2026-10-02 15:54:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3569ea91-1cef-3dc6-bb4a-5d5c2eeaa852 | -12.36434 | -41.66011 | 2026-10-02 15:54:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a91993cf-f4fb-32fc-bcda-434e11360a8f | -11.81061 | -43.56995 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7d71deb5-873e-38fc-bf9a-e1b62b171cec | -11.65074 | -43.59628 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 74a1fcc0-817d-32ef-9469-3ba458f4b18d | -11.45347 | -43.40092 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 4a03bbd6-75de-34df-9e58-a1a35dbabf4a | -11.73072 | -43.58411 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| a2696eb7-b09f-3ce5-8dd3-bff803ef2839 | -11.69422 | -43.61705 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 008902eb-fd4b-37ec-9cfe-7cd92f7d416a | -10.89728 | -43.85176 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1fc06b54-cd76-30db-a65c-0eb74657a0f0 | -11.66903 | -43.61982 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 181a3714-dc9f-36ad-b6df-5e035cd3f63c | -11.61069 | -44.1314 | 2026-10-02 15:54:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2588df66-1539-3684-99f7-f6e5cb132986 | -11.26901 | -43.51952 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 56d52c74-cb75-37bc-947a-d63c811f4945 | -11.73326 | -43.44201 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8ee9115a-df79-3707-8c1d-fb0545894f0b | -11.4747 | -43.53802 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 680f7e51-cdd6-36cf-9944-cbcd6420f2da | -11.13912 | -44.59128 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fda68494-58f0-3fcb-844e-b86c9290acb5 | -7.36645 | -44.64184 | 2026-10-02 15:54:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cb79d15c-fc46-335f-8eab-577d361715a0 | -11.3125 | -44.26912 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 077cd195-5729-3bea-b8a7-5a58615897d8 | -11.7297 | -43.57588 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 049a0547-50d6-3ba8-99ef-3aa10c6de1b9 | -11.74359 | -43.52414 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 10433975-c481-35b9-a0a6-37210e7c7694 | -10.3124 | -44.64624 | 2026-10-02 15:54:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b140c528-e57e-3930-b90a-472c8dad6aab | -7.95572 | -37.47569 | 2026-10-02 15:54:00 | NOAA-21 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4f0c34d8-8211-3e25-b451-1160db9d8a39 | -11.71194 | -43.43304 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 28d268bc-714b-3140-a942-55e0c639ea81 | -11.28197 | -43.54974 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d6bb3253-daa3-381a-acf1-55f28d56b38e | -11.28396 | -44.25299 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a77e26a5-3dce-3c22-b31c-fc3b45b5e9b2 | -11.65526 | -43.55151 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65a646f6-b0e7-35b3-be21-d3082ddbb4f5 | -7.88909 | -37.50462 | 2026-10-02 15:54:00 | NOAA-21 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a1d8a5e6-1844-3de7-9024-cf4025204b22 | -11.27922 | -43.56731 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 92ef518f-ffdf-3422-a8c2-2e1d087985a1 | -12.02493 | -38.1282 | 2026-10-02 15:54:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 34fea025-0cf7-3874-9e4c-241215fb17b6 | -11.71537 | -43.62253 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ee7299fd-82d0-3a0a-8600-af2fdf8930cf | -11.37107 | -43.37502 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c6cfe3be-7f21-334f-ab38-c1ff8353239a | -11.63277 | -43.57489 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README103.md)
