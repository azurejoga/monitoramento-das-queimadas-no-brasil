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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88f8495c-60c6-3fbb-bea0-f37c3165bee7 | -4.2058 | -48.5491 | 2024-11-09 05:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 29830a60-bcce-377f-bd63-8a82ac4795df | -4.2486 | -47.5729 | 2024-11-09 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| f5149dca-f0b6-3334-946b-abb70b495add | -3.9854 | -48.1708 | 2024-11-09 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 88e8cdf7-df8c-3095-b565-6c9e824aa354 | -3.5819 | -47.3403 | 2024-11-09 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c28466a7-ca1d-3c09-872b-9ec7a802c780 | -3.6004 | -47.3395 | 2024-11-09 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 37869f7e-2082-3f7e-913a-ef40a47fe202 | -1.5163 | -52.1901 | 2024-11-09 05:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e584ad46-908d-3c1e-8f00-767bb0da45f6 | -11.1068 | -43.3428 | 2024-11-09 05:20:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 71.5 |
| cb931e8d-72d1-3e26-93d1-293979463bd4 | -2.81546 | -52.96109 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc753410-9ff2-36a4-bf56-6ee03f2aa1cd | -3.23959 | -50.27796 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65ab062f-fab1-337a-990a-2726089d1aa9 | -2.69282 | -51.69979 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9df16373-57cd-3a90-b6a1-78a6c7db5fe0 | -3.12318 | -50.15207 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b6676cc-7ec7-33fa-a869-1c03daf75b24 | -2.24501 | -53.6703 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a915be26-af2f-37e9-88e3-ce1fb6c0c15e | -3.73858 | -50.44946 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef9549e2-bacb-3ccb-95ed-e1170c5f169e | -3.23408 | -50.2772 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49d97941-272e-36c3-8a13-c0523fa07027 | -0.39228 | -51.94304 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70be897d-681f-3512-ab42-043e44e22b83 | -1.69473 | -51.92105 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c81edf5d-dd16-3cd6-9615-0bb144d6ff69 | -3.58939 | -50.27407 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce5a7fab-93e4-3144-82a1-e1c745c8731f | -3.24242 | -50.45612 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df06a0a-106f-342a-ac00-575083002582 | -1.14555 | -53.65109 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0de96ac4-ac94-38f3-af6d-863fbb45cd6a | -3.03575 | -50.36602 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea48b711-c247-3349-8fc7-ad9181f4aafe | -1.62212 | -52.54289 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 257977d2-b537-3a1f-91a7-41ddf405ff5a | -2.45767 | -53.69289 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f8c7ac7d-2d9c-388a-abf2-1b5009e68e80 | -1.52623 | -52.19007 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eb772c6e-5837-321f-b8bf-47faf1dd2055 | -3.17351 | -53.85565 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ad82326-fe9c-3fae-822c-afb3a023e282 | -3.79019 | -51.82587 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8117e2f-0f08-3537-874c-2d6f65dd9b3b | -2.3594 | -54.7507 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9aed8b6d-ed03-3638-852f-1a553babbfce | -2.87998 | -51.47502 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 128f5727-7b8d-3edb-b0b8-70ca173d9cbe | -3.81235 | -50.78594 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1afb868-54ae-35a3-add7-8bb0fb8f1205 | -3.02746 | -51.01217 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06657039-930f-370b-9828-cd4159ee8370 | -3.64149 | -50.18797 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb0ad3d3-63d5-3626-a72c-278e8e4e5cc4 | -1.52547 | -52.19502 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 17493457-0ca5-3672-a790-a3e9dc52bbad | -3.07769 | -50.57022 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6f858544-e2d8-3895-bdf3-011eafae14e0 | -2.81744 | -57.12681 | 2024-11-09 05:20:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80d67ac1-ae79-34f2-a9c2-ed9275c0a9dd | -3.04615 | -50.37114 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59fc4bf6-e048-35ac-a811-af001cc84b44 | -1.53837 | -54.29951 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25e70429-887b-37bc-b016-7665e401bdc1 | -2.45827 | -53.68888 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 98c5056f-9757-3b45-b3fa-2e9f4fb3eb59 | -3.78562 | -51.82237 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 610efa9f-08f1-30a7-9892-3ac0e27918c6 | -1.52153 | -52.18935 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6f1e8f1d-561d-34c2-830f-beaecebb594b | -2.3971 | -53.8681 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09dccd8c-5e91-36a9-8f0c-1599ae94e363 | -3.89331 | -50.08504 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c16492f1-9154-3500-8827-a340642c6c06 | -3.02697 | -53.26132 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09a6a3af-177a-35af-bdb5-e3638dc95080 | -4.20938 | -48.55519 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45537377-8df5-3693-9d8e-8716de382ccb | -3.58479 | -50.2703 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33189567-f9e2-372e-87cf-546247b84d31 | -3.75303 | -52.1038 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4d94ef-adc8-3930-bc1e-0eef81b2e3b0 | -2.75184 | -59.4269 | 2024-11-09 05:20:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70a92a9c-af62-3cb0-a818-d7cb7460d0f8 | -3.17284 | -51.2632 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c3a797d-a040-3e06-a939-6f5619a83f70 | -3.017 | -51.04612 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 493c5d6d-85b2-3d5e-a6db-d576b5c4a84e | -0.04099 | -50.78546 | 2024-11-09 05:20:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0af65a4c-f6d5-3d57-ac31-7a7dcf734451 | -2.99731 | -49.23916 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0768a1d7-e819-343e-8bf2-913225f4eea6 | -2.45278 | -53.69619 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7608d9d-a66b-3f10-b773-4a1cb2534f75 | -2.98181 | -50.3067 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd5f5005-eb19-37fe-81ca-90dad959c182 | -3.16224 | -54.48852 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 417b7a91-c12a-3a35-b8a8-9901ce4e848b | -3.53093 | -50.87085 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4d26a333-442c-3299-8ce2-5e07c600a7e7 | 0.62791 | -60.08947 | 2024-11-09 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35f87ed2-c7fd-35f4-99ba-3d0c8e4ba0b5 | -1.31836 | -55.88333 | 2024-11-09 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adf53028-ff3d-3ae6-927d-2119689869a9 | -4.2496 | -48.54134 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f061f767-788f-3afc-8036-f1b61eb167d2 | -2.41012 | -48.52224 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0ab49c69-689f-380d-94da-b742898bdb23 | -2.81965 | -52.93341 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90253ceb-e7fe-3b1a-9e47-18c39c03004e | -2.40132 | -50.31051 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 358ef833-6de0-334a-97e5-55b0e595c056 | -3.26052 | -46.31441 | 2024-11-09 05:20:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6477ed84-2b0a-3a1b-b88e-6d69a8145f56 | -1.38014 | -52.20483 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f9abb3-5c2c-3ab0-9de6-669cee4f48b7 | -2.92051 | -51.0432 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2548619e-764b-3c51-9c4e-4f52a324abea | -2.97739 | -50.29881 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e22c0897-f1ca-313c-924e-380ac70dd2fb | -2.23782 | -53.77582 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 409f14bf-f2be-385e-a521-ea9ed1900ab2 | -3.28298 | -51.52209 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8266ef7f-6b4e-34c4-9bdd-e9934e967786 | -2.56665 | -54.1691 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 349f2e40-4c6d-397d-a62e-79df03d013e6 | -1.22094 | -56.17252 | 2024-11-09 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebc80773-5659-3cf1-9333-57cf920d64d9 | -3.40664 | -50.01695 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 373bd54c-e8e1-32d1-a51f-92cb6e07bfc4 | -3.26756 | -46.31546 | 2024-11-09 05:20:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 649c74c7-6907-3215-8787-318038fda1aa | -3.35428 | -50.26608 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a7b6822-015e-3db0-8e18-a7caf8800ec0 | -2.98928 | -51.46104 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bafa9b4d-a889-34f1-a459-d59e81ce83ff | -3.83198 | -50.04966 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaf805e1-a92a-3a5b-a882-af6f12f96dce | -2.15957 | -53.69527 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c7d467-94c0-3afd-9567-bf055b729073 | -3.58496 | -47.34962 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| dc7dc06b-0054-3bee-8b36-671c0404efd9 | -4.29897 | -50.74592 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 788480fb-7140-3118-a138-02fda27ead50 | -1.32053 | -54.63983 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff94e5c5-a71e-3fb8-be1b-c65f0f7dd191 | -3.2365 | -50.45871 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7110212-affc-3540-be82-0c35c493930f | -3.64874 | -50.76118 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd8b89d4-b28a-3394-a652-18f26c742428 | -3.81961 | -49.85917 | 2024-11-09 05:20:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97aa3f04-0d7f-39cc-ac75-50265f70b1b5 | -2.79938 | -52.94437 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3d80826-aaf9-39bb-a1c2-30c6e7d5769f | -3.03062 | -51.53033 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43e285ed-8a85-3f02-92ec-c2796771c06f | -4.2154 | -48.68951 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f674281f-47dc-33aa-9e2a-9cd5e3e569c0 | -3.477 | -50.80524 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1495e60-79aa-38a1-9c97-919a1e6502bb | -1.15836 | -51.99828 | 2024-11-09 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d81a636-8bd5-3cf3-9239-7859a76bf489 | -3.21759 | -50.3876 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4600ddf7-0202-3759-86ae-d4a270a08413 | -3.90001 | -50.30695 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98d7a565-9ace-3156-b82b-39e887a02acc | -3.04463 | -50.38163 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e185bf27-e7ab-32a9-8690-81e71a4f1779 | -2.88087 | -51.47334 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cad88a7d-6445-3dfd-8e14-2a42316cf6a4 | -2.08205 | -54.69392 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 708c6de9-6df6-3a23-98bd-0c8f76778324 | -2.92599 | -49.35602 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91102c47-5f64-35a9-ae6a-7225c6ba8e5c | -0.18954 | -60.76617 | 2024-11-09 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3330135-6f5c-3d3b-b1a0-def83ad7575d | -3.61161 | -48.92242 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 003bdc19-22dd-3b84-ba03-04bb60e18987 | -3.02915 | -54.20506 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58f3e7fa-dcd2-35ba-8b92-a92574a493de | -4.22293 | -50.645 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f188d35d-a4a4-3905-9465-55425f8fc72c | -3.23699 | -50.45531 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ac12e7f-a873-3e4c-a910-840ad09b9aee | -3.03452 | -53.27162 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f5126f6-d8d6-329d-9f1c-a3a44a00a4d8 | -4.37954 | -48.58524 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc2b42fd-3a13-3ab9-90b7-f5c3d1f8c250 | -3.92558 | -50.24683 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03dfb801-cfd6-3c3a-9d45-d847846d68e0 | -4.5405 | -48.64716 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a36723e8-c4bd-3a49-ab77-b7dc6863fca5 | -3.25679 | -51.13375 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README102.md)
