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
| f04cfde1-30b0-3ed9-8908-52a341b28521 | -20.27121 | -46.6922 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 455cc93d-3fac-3ce0-bb08-02020c2b25c0 | -20.27229 | -46.68927 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f96b65fd-a81f-3a63-a070-153f215d9a45 | -24.00919 | -49.0511 | 2025-08-22 03:36:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15b3a828-df4d-39e4-91c2-c0cc1afb2a77 | -24.01038 | -49.04619 | 2025-08-22 03:36:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97c0837f-ae19-3bf9-b77c-01dd90f175e9 | -12.0027 | -44.6618 | 2025-08-22 03:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 0ca66b38-3457-38f3-9824-9f0d90fd355a | -12.0027 | -44.6618 | 2025-08-22 03:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 1d75b426-c0ab-3173-9204-d9400579b8d3 | -7.46128 | -44.45105 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d215fc55-d062-3477-b59e-4245ac0bdfe3 | -3.38507 | -47.61029 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7460add-4757-3e44-a4dd-4bdb3bd15c23 | -4.42476 | -47.75526 | 2025-08-22 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e80f7b9c-ed01-3f6a-9afc-dda7baa40799 | -6.07436 | -44.1329 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 444a7e9d-407e-3f82-994f-0619d1d65eb2 | -3.36439 | -43.36801 | 2025-08-22 03:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48e04850-e854-3ff3-8b05-b316005bb8dc | -6.0326 | -44.3573 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c594a11-294d-3a00-a6df-02d7a6117dfb | -6.28924 | -43.69881 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 366d9ac3-d181-3b71-b21e-d43c621b8bab | -5.42905 | -46.36004 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 806d73cd-5e7d-3b7e-b4a3-f2182c9ec120 | -3.38573 | -47.60638 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2863691f-4c6d-394b-bc1f-69116149e79b | -4.40546 | -48.94843 | 2025-08-22 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66278d6c-fed0-3cc6-a058-8d30bc416c53 | -7.24712 | -44.70048 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976d407e-595a-31fb-9640-c2b72fb27d08 | -5.38355 | -41.22052 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32fb6505-400c-3c55-9a53-f802cbd34c61 | -4.39993 | -44.09079 | 2025-08-22 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b793d1f1-bc3c-3875-854e-f99f7ce0016f | -6.77062 | -44.32671 | 2025-08-22 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 719b2079-21e5-3a4b-ab66-097fd5501a52 | -6.43247 | -44.51969 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fb9d6eb-9f16-3ae7-957f-02e6c86b58cb | -7.46988 | -44.45262 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49ec8843-fe77-353b-8f28-b54f8a3230db | -7.51528 | -44.97055 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2febe98f-5fcd-3b44-aa90-8a288a93eb01 | -7.6376 | -45.24243 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0edd6881-82fb-3b21-bfa7-b82483299b7c | -2.46652 | -47.77217 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39ac7175-17d0-3b7a-9a41-8b8f03ed9e0a | -4.59132 | -37.81333 | 2025-08-22 03:55:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c461c6cb-5ff3-30f4-a1d8-4f6512b51a34 | -2.47401 | -47.77384 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6d5dc70b-32a4-3b61-9720-1cbcdaccfd65 | -6.03573 | -42.83452 | 2025-08-22 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ed1c140e-9d5b-30f2-ac31-7091d6b4db7c | -6.29125 | -43.8908 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa7c5804-0a27-34ce-9a0d-b312d0bcc7d0 | -2.45838 | -47.74945 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd050c7d-3bc6-3bdf-8c46-a06c7d0b45ac | -5.96816 | -52.22197 | 2025-08-22 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e064f8f-380c-3c54-b723-b6d4348c605f | -5.79518 | -45.0755 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc4c0637-c42f-32f9-889f-67a44da3262f | -6.33503 | -38.9801 | 2025-08-22 03:55:00 | NPP-375D | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c71e624f-7ca6-3d52-ac62-1e034b5b5a4d | -7.63307 | -45.24164 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c9365b51-25cb-3984-9523-0787ba2eb873 | -6.49971 | -42.97489 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1537c680-37b0-3f0a-ab18-d27b8275f2bd | -5.4195 | -42.37288 | 2025-08-22 03:55:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 079562bb-5472-344e-af24-479d70a3c423 | -4.72296 | -44.34212 | 2025-08-22 03:55:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9929684b-5155-30ec-96d7-7f1611fcb936 | -6.43393 | -44.51097 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c62ce1bb-3a42-333f-87cc-d9ce63f31eae | -6.11215 | -44.39065 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47f8a398-6200-3674-9ca7-9b257a0611a1 | -6.29974 | -43.89207 | 2025-08-22 03:55:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab4a6e32-5804-3810-a8a0-6c37da084b2b | -5.9757 | -52.2258 | 2025-08-22 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d959d4b8-f4cc-382a-85a8-0b808f167d23 | -7.14219 | -44.17606 | 2025-08-22 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 871900c7-345e-3808-a34d-6e982c9340b9 | -6.94759 | -44.55654 | 2025-08-22 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80489fbc-a5a8-3169-9f68-7b2b08c23819 | -7.63676 | -45.24718 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a9113c10-3d38-3e11-b739-2aa8c583e8da | -7.65575 | -45.24542 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ac478247-fd26-353f-a0b6-00fd5e1f12bf | -7.50712 | -44.96459 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aa568d5-b895-37c4-87e9-68693cbff62f | -5.88209 | -42.40892 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6a1c8f91-911e-31e6-9721-4ef48772d4cb | -5.07045 | -37.71523 | 2025-08-22 03:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07988719-97dd-3e68-be94-304c2a8f5c74 | -2.25771 | -47.85054 | 2025-08-22 03:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d72ec53d-1e1b-335d-ae32-e71943a94944 | -6.53512 | -45.4555 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 754e1f5a-87e6-3b58-a7c3-25a403e65cc5 | -7.14899 | -44.66837 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddd47b7d-e33d-3309-af12-01f0317aef4b | -5.52587 | -46.42068 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a37a8eb-f9d9-3c46-8732-e8825129742f | -6.94898 | -44.54836 | 2025-08-22 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6e35252-3a41-37f6-95c5-85712f6f08c2 | -4.40627 | -48.94371 | 2025-08-22 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb2cf2dc-d9ab-3a9a-bfe9-479a5d1b6362 | -6.49071 | -43.446 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f92d0770-d440-36db-9b33-2022be9561f7 | -6.36995 | -43.24887 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c25ad5ca-31f4-35bf-92ae-6c6e470c3e3f | -7.15078 | -43.22961 | 2025-08-22 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1fb27df3-cb6a-3d01-9524-3930c8fe96a4 | -2.46954 | -47.76437 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 93dee7c7-01f2-3702-b4f5-97449b750097 | -4.14029 | -46.45059 | 2025-08-22 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d566639-bbb5-38b0-a5e8-a6c4358e8a73 | -5.48628 | -42.1623 | 2025-08-22 03:55:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 41b080cf-c08c-393a-b2db-94c0f900ad9b | -3.98306 | -42.52821 | 2025-08-22 03:55:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4730f2f3-0e7d-3e0c-b09f-bd7ccaa84357 | -2.91427 | -48.30264 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee17b552-ca12-3668-a019-fb1f5abb04e1 | -3.81731 | -41.55167 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3287ade8-16f5-3f59-8c95-2f66cc825215 | -6.49277 | -42.85796 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd646f9d-499e-3b96-adf0-cc3dc8608133 | -6.49828 | -42.97303 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad3d33dc-ea31-3ac8-9ea4-762416bbc5b7 | -3.81654 | -41.55401 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a215ceb2-5434-38ee-897b-b427bd931fdb | -6.05252 | -43.99942 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3ee10da-970a-3e47-b3b3-57be6d1c5223 | -6.94248 | -44.56009 | 2025-08-22 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bb15d09-b5f7-3949-bbf3-8d1911e30dd9 | -6.07863 | -43.45277 | 2025-08-22 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe9f982a-4fe6-35b0-873e-2f0f31d5c4fa | -3.23703 | -46.78658 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4efe2e3d-b591-38b3-9e53-0b54dfa6ed43 | -7.94258 | -42.66182 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4e78e595-5f67-30d4-8ab5-a40225fd71dc | -7.2552 | -44.70621 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46dad93b-1a8d-3225-84db-3b0dc02152a6 | -6.50064 | -43.43686 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38f23c58-c12d-35e1-a0a7-9235b0defb42 | -2.46723 | -47.768 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54874724-afb3-385a-98b0-7934d6b5f182 | -6.04502 | -44.36394 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c2566ac-b6c7-32db-8927-900744ce7913 | -6.07865 | -44.13373 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e31820ed-1d2d-3857-b48a-70d6dc6801a5 | -6.03995 | -44.36733 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb2099fa-8d2c-3194-8b65-b5569306cf9b | -7.03906 | -44.62816 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec572ebe-f9bc-309c-ba3e-3bbe0931dcc3 | -6.04431 | -44.36822 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 172b28b9-67c5-387a-a24d-888cc64aee9a | -6.29905 | -43.89616 | 2025-08-22 03:55:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f11ced70-3273-35d4-a1a8-7d5406ab3c66 | -6.49488 | -43.09966 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96b4be18-041a-3715-948e-7bf36b404ffe | -3.26625 | -46.91534 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b42e5c2b-428d-3ee0-907c-075de010ad1a | -5.52536 | -46.42363 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8353e7a-6960-3e4c-b856-f294d28cbde0 | -5.37586 | -41.22216 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bc156f5a-156c-34e4-a106-c1fe981ddf75 | -6.43123 | -44.67795 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c7b09b7-8b8d-386e-b5c7-5a3af9460cbb | -5.1667 | -35.80644 | 2025-08-22 03:55:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9cb537e3-e69b-3c39-a1a8-978c3db4eed1 | -6.70983 | -43.20579 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5e18fc4-9d53-32d9-b23d-40e0bcf75573 | -7.6413 | -45.24793 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9eb6416b-93a0-3613-9169-6860d4522ada | -6.20363 | -43.56547 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d9063a2-cba9-3ad8-8c08-93538c5a29e4 | -7.27165 | -43.66849 | 2025-08-22 03:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6e13302-3f15-3838-8fe2-8c0c63e3784f | -4.31228 | -48.09774 | 2025-08-22 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45dc2112-574b-301d-9107-3da2d96c6e29 | -6.42388 | -44.66757 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 525a0604-b701-3078-85f2-6fb5d1264f57 | -6.37342 | -43.25301 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4df014fc-52ce-3f90-b150-458ff2766027 | -7.17098 | -44.67201 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41e2818b-94bc-3852-b9dd-9c3dce6985ea | -6.49592 | -43.11779 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af9651ce-be04-3394-b209-7a44b0de1e44 | -0.74788 | -47.75463 | 2025-08-22 03:55:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a06e934-1c2f-3984-87d3-a8b5febb99c9 | -6.04052 | -44.36104 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc14c315-2c89-389a-9a5d-32c1dd1aa0c0 | -5.37532 | -36.75937 | 2025-08-22 03:55:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23a3158d-1cf1-3ead-8404-fb626b5b84a9 | -7.15416 | -44.66454 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe49185b-4e3f-3205-8a8d-c2fb1555aa00 | -3.98043 | -43.24256 | 2025-08-22 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README12.md)
