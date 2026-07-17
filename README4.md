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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c21a7f2-f6c8-36b6-9c84-e2987ba0d8b8 | -5.60433 | -36.86612 | 2026-07-17 03:17:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5c8c7281-3bdc-3589-9f4a-5c8bea820322 | -9.46895 | -40.3169 | 2026-07-17 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.7 |
| c88c4c50-12b8-34ee-a5d0-c21ad00b00c1 | -12.89037 | -42.45707 | 2026-07-17 03:19:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| dbb72191-2e31-37b5-a68d-02dc8a0e4aaf | -20.54424 | -41.27693 | 2026-07-17 03:19:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a7a80d88-3c9e-3312-838f-ade340e13c92 | -20.6395 | -41.41748 | 2026-07-17 03:19:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 038d2a81-adc6-3659-bc17-2350021a467d | -20.54925 | -41.28057 | 2026-07-17 03:19:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e8ef72c7-fd17-3f97-b7a4-0c5af6b47d83 | -12.88892 | -42.46163 | 2026-07-17 03:19:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fec92e5d-ed79-3f4a-b198-ea6ec9619463 | -20.55005 | -41.27697 | 2026-07-17 03:19:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 35bc76bf-10c3-3d53-8960-01cc9d6db34a | -22.4649 | -43.10047 | 2026-07-17 03:19:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 49692ffb-3415-3c4f-9e89-6c98a4a2d907 | -20.54354 | -41.28009 | 2026-07-17 03:19:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d6803b5a-c1dd-39c7-b502-88f307fb30ef | -12.8903 | -42.45502 | 2026-07-17 03:19:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8d727e54-7fd7-30f6-9c57-d90c160d3240 | -12.88894 | -42.46367 | 2026-07-17 03:19:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 47f9182d-92f7-322c-8d6c-0950f6680dc3 | -9.4582 | -64.033 | 2026-07-17 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 92382b9e-8eff-3545-80f3-fb8e565b1986 | -10.8283 | -45.1312 | 2026-07-17 03:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7228e84a-f2c8-3e99-a176-0cd3e0e3fcc3 | -9.4581 | -64.0519 | 2026-07-17 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a622c315-c186-3381-aa77-01bfc1b223bc | -9.4582 | -64.033 | 2026-07-17 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 00dafbda-a637-3875-81eb-6f0298a730e9 | -10.8283 | -45.1312 | 2026-07-17 03:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 7423e7d6-c7c1-30c7-b34b-3b4113dd0aa6 | -9.4581 | -64.0519 | 2026-07-17 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 25e65b1a-85ed-300a-98ae-fed52ccbdb02 | -9.4582 | -64.033 | 2026-07-17 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 169.0 |
| c1f990b6-3b09-3d8e-a300-59a693afa4e7 | -9.4396 | -64.0338 | 2026-07-17 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 13e2088d-cefb-3b7c-b077-835aea7519de | -9.4395 | -64.0526 | 2026-07-17 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4cc7ec9e-70e0-3dfa-942a-9e30a5dd6711 | -9.4582 | -64.033 | 2026-07-17 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 204.7 |
| 84f418b0-2990-3e1c-a764-a288a3708245 | -9.4777 | -40.2867 | 2026-07-17 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 22a71ce2-bd1a-3e72-9945-bae13e8358f3 | -9.4581 | -64.0519 | 2026-07-17 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.3 |
| cd4556ec-189a-30cb-b142-bba29d2e9dab | -9.4766 | -64.0512 | 2026-07-17 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 71361a92-501c-35e0-a74e-3b3f444e65ea | -9.4773 | -40.3116 | 2026-07-17 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 0d08622a-b572-34a4-b0d1-7b48acb3957f | -9.4767 | -64.0323 | 2026-07-17 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| da7a8b5d-7cc0-3b37-98c0-587b9fc58bc6 | -9.4396 | -64.0338 | 2026-07-17 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 63c582c0-9ada-3cd8-8460-3185e046e79d | -5.31637 | -37.53659 | 2026-07-17 04:00:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b68d47dc-ecd6-3e96-84e5-35a21fc5a8d6 | -4.47691 | -40.86644 | 2026-07-17 04:00:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9efb5a5-bd75-334d-955f-778cca201780 | -4.15399 | -43.09711 | 2026-07-17 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff632e03-9a08-3be4-82b5-c3d8f3165ad8 | -5.03548 | -38.13593 | 2026-07-17 04:00:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 03cb4b9e-7a40-3ab9-882c-40518b94dc2b | -4.47032 | -42.30503 | 2026-07-17 04:00:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d2408a3b-19fc-31e9-adee-7e555f70ae77 | -3.49739 | -43.31433 | 2026-07-17 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72db79ca-8e6d-38c5-ae07-94d690128771 | -5.12517 | -38.06858 | 2026-07-17 04:00:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 12ff7df5-6d25-3137-9b85-0898d2662fa4 | -2.7566 | -42.78024 | 2026-07-17 04:00:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7905bf1-ef39-30e9-9ab1-92e9d493f11c | -5.3155 | -37.53962 | 2026-07-17 04:00:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3eeed63e-eb4a-32ea-bedd-5c0d68c6765a | -2.75422 | -42.78138 | 2026-07-17 04:00:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b65fae6a-627d-383f-abe0-c79ac2cb99d2 | -5.12573 | -38.06497 | 2026-07-17 04:00:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1bf3a63a-8d40-3089-babb-85422ab9f6d6 | -0.09184 | -51.28203 | 2026-07-17 04:00:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e12ad55-37ac-36e7-b4e1-7a542e8a7d3e | -5.31579 | -37.54034 | 2026-07-17 04:00:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8baf10b8-fd0c-364d-837e-da86bad006b6 | -3.86303 | -38.48656 | 2026-07-17 04:00:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5950a36b-f0f2-3f5b-aaab-7a38724cbb5c | -10.712 | -48.38922 | 2026-07-17 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f89b906-278d-3c23-b184-d475664852b0 | -10.81736 | -47.39669 | 2026-07-17 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 112ee98c-6394-33d7-9af1-02c011749621 | -7.72982 | -44.55982 | 2026-07-17 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1be4ed79-0555-3453-913a-791bf2c670bd | -10.81705 | -46.53622 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9b8ede4-6e3d-3144-b1a4-993d6432fa68 | -7.91134 | -48.26273 | 2026-07-17 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b045c773-6d35-368a-adb1-381215d5ec71 | -8.50758 | -48.07737 | 2026-07-17 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40903ec0-9308-3ffa-8d13-01dcbbff137d | -8.507 | -48.07915 | 2026-07-17 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 660e68de-392e-3b55-91e0-29eb4e144420 | -5.63575 | -47.09761 | 2026-07-17 04:02:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7ad61ec-ed23-3e36-915d-90fd23272b88 | -10.82187 | -46.53307 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9cbfa114-e451-3213-a048-c5039f884e2a | -10.82083 | -46.57239 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 130bb21d-d28f-31b9-9d52-81bc62c002dc | -9.90825 | -53.36803 | 2026-07-17 04:02:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7de1deae-05c0-3be4-8e6f-094a78708035 | -9.56861 | -48.6677 | 2026-07-17 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 881ab923-f95b-30ed-a583-b0093c845dde | -9.51361 | -47.13628 | 2026-07-17 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cd5d1465-3d58-31f2-9927-a606f98d0dad | -7.29516 | -46.25202 | 2026-07-17 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d892fc51-3bdb-39f2-be88-7e87227325bb | -8.7607 | -43.93828 | 2026-07-17 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a261c736-58a4-33f3-a61f-caf9a039d1de | -7.96285 | -49.65148 | 2026-07-17 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2685eb43-50fa-3f95-b5a2-65c6b1708426 | -10.83824 | -46.57111 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04f1c929-d1c7-3653-a34c-ce816372a943 | -7.91235 | -48.25715 | 2026-07-17 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d5b5952e-3b8c-37e0-a0c9-89744ff5a710 | -9.6996 | -47.69736 | 2026-07-17 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b97e64a4-90dc-3581-b059-4e3512b53974 | -9.51803 | -47.13705 | 2026-07-17 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 82d4bc89-b5c1-324f-9b10-6a5087cf71be | -8.05063 | -46.72389 | 2026-07-17 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bffb0f9f-d677-3e9f-9c45-63fc7d8347c3 | -4.66268 | -43.22046 | 2026-07-17 04:02:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ff4f63c-5688-399e-89f1-3ad258a42993 | -7.73064 | -47.24388 | 2026-07-17 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 431acda0-aad0-302a-8ba3-9ac0182d3757 | -10.82358 | -46.57316 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67fd8f99-d549-3e72-8124-3e08672adc32 | -5.63244 | -47.10028 | 2026-07-17 04:02:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 567545b2-f4e4-3dbd-abec-d90e27b44099 | -9.51284 | -47.14075 | 2026-07-17 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7f150203-32b9-35bc-b455-fc6d66038a5f | -9.47163 | -40.30821 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8f43083-018e-35ba-a291-95ce927cc880 | -7.9145 | -48.26126 | 2026-07-17 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c388ba9-cd63-39e3-ae45-fbfc9a1cf6ef | -9.47493 | -40.30873 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 975011b1-ba9d-346f-953f-7d0f04dc6a6a | -10.47681 | -49.14673 | 2026-07-17 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47896091-3644-302a-b449-d11d01a69dac | -9.47877 | -40.30577 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 574f842b-47b9-3785-8d52-2ac04b6ccf8f | -10.04486 | -51.66348 | 2026-07-17 04:02:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c88ece06-9ba1-344c-af61-70ba069610a1 | -9.56761 | -48.67311 | 2026-07-17 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 31252c3d-ae1f-3dfe-a389-40ff71caf57d | -7.29085 | -46.25126 | 2026-07-17 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a4f0d08-7dca-3701-ab9a-cb7b73880041 | -10.82121 | -46.53695 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae6c1f0-887e-38fe-a9c2-38e4b10e12f2 | -7.29375 | -46.24857 | 2026-07-17 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62515157-1541-3e0d-9da1-d3e039e1c316 | -10.86291 | -46.50432 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa6ad662-af4a-3031-b370-3318efc76ae9 | -10.86224 | -46.50816 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3b5e16c-7a0a-32ea-b646-9d92a43cf996 | -10.82804 | -46.52205 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c95378b6-eb33-3fdc-aa5d-313553454216 | -9.69501 | -47.69663 | 2026-07-17 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 447ed9a0-94a1-3f31-b814-258ce4789338 | -10.83891 | -46.56733 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5450a3a7-5fec-3081-837e-fbaaf1856293 | -10.82984 | -46.52203 | 2026-07-17 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 253aeb77-ea49-37d6-ad69-a94b4651d155 | -9.8578 | -40.29445 | 2026-07-17 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44f2173e-3763-3a18-960b-ad2a782504b3 | -8.51279 | -48.07444 | 2026-07-17 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7795df8a-2c09-345d-9d13-cad91aba6cd3 | -10.8197 | -47.38366 | 2026-07-17 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9292fae0-41a8-3da0-a960-4852bd315fda | -5.79938 | -43.63635 | 2026-07-17 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faa35883-f482-367f-8b8d-e94f32703ba3 | -8.5085 | -48.072 | 2026-07-17 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d1790d9-b33e-3f12-9792-e4e976a9adbd | -5.80386 | -43.63247 | 2026-07-17 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 682145a9-c0c1-3eb3-9050-f78519c57bfc | -10.82238 | -45.13032 | 2026-07-17 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e5f49f0c-7fb2-3071-8bc4-78452b69c7f5 | -7.68454 | -50.59896 | 2026-07-17 04:02:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b40f728-65d6-3407-8cd3-b5c902273687 | -6.01558 | -46.32262 | 2026-07-17 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78ddb864-e509-322a-be18-25683dcb5f54 | -10.39103 | -44.9203 | 2026-07-17 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21ef8e3-0a02-32f5-8fd6-f19936835398 | -7.29807 | -46.2493 | 2026-07-17 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a3ccb64-6e0c-398e-bd2d-1855b8245b7b | -10.82158 | -45.13508 | 2026-07-17 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 7221509e-0a0e-3ddf-a004-355af4a7ab4b | -7.29589 | -46.24784 | 2026-07-17 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c17acde7-9105-3b65-badc-d63c7e5e8d99 | -10.82124 | -47.37508 | 2026-07-17 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a6a6b78-6b1a-3d4f-b23b-c501ff3b29be | -7.96415 | -49.64426 | 2026-07-17 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01763301-505f-3745-8f49-a19a61195208 | -10.03813 | -51.66667 | 2026-07-17 04:02:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
