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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee85a5ff-4e07-312d-816d-c6d878c12c17 | -9.86439 | -38.02056 | 2025-06-07 03:55:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a815279d-a493-3f51-b4fc-02d0d4ecaa37 | -13.07639 | -49.23817 | 2025-06-07 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f21a945-61fc-343f-a7c7-e75354b24486 | -12.32669 | -52.4843 | 2025-06-07 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be40937d-d030-3cee-970a-d133b954cd1e | -6.95237 | -42.89578 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 18aa0b2c-2d50-3dde-b3cf-0f9506024c94 | -8.45622 | -46.48599 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18a0741c-d511-3982-8b03-e1ca6f836743 | -9.07469 | -47.14797 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a8e00fb-01f8-3a1c-b0b3-adb3f519f875 | -7.72446 | -44.16219 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 60801f70-3f66-3063-8ea0-a88b21e0212d | -9.33181 | -48.51933 | 2025-06-07 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3f197f1-ba82-39c0-97f4-22003063115d | -9.39966 | -48.43978 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad6195e9-4463-349f-bd05-024347c9a205 | -9.07076 | -47.14147 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d583936-cf9c-32ad-817b-606375567cb5 | -10.46732 | -47.95207 | 2025-06-07 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b956bf1b-2a75-30e3-bd3a-9c80f2345026 | -8.45533 | -46.49122 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06ef216b-ba46-397d-8ae3-5d20cbe57403 | -6.23603 | -48.55788 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3929ea02-5407-3344-a678-f76db5c6e42f | -6.94742 | -42.80667 | 2025-06-07 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b607be2a-b831-3f94-86ea-bcee0b1c6d27 | -7.72507 | -44.15855 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f647fc3-cfeb-321d-bd43-26dcd4b302ba | -8.32463 | -46.20031 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7502eab6-f471-30df-b587-f4ce680dbd7e | -7.86398 | -47.90043 | 2025-06-07 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3133583-0df9-380a-981d-45604cf77180 | -8.72382 | -47.90543 | 2025-06-07 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7c7be5d-11b2-3ba7-b21a-7d5e8ee85291 | -7.73431 | -44.17919 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 406dcc2b-4d79-316d-a9b3-41bfccdb1139 | -9.06977 | -47.14707 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebd40971-c5b9-367a-8249-b17a95b8c9fe | -7.21116 | -43.11139 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16c21906-5cd4-326f-8902-f88cb25f4b90 | -10.87562 | -49.55163 | 2025-06-07 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24bc38f9-5ed3-3f0e-9e98-6f55a60f62f8 | -11.77637 | -47.40072 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6963e99e-5ec2-3ee2-8f86-48c707c338ac | -9.40095 | -48.43294 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a546248d-37e2-34f3-ac66-ede21cdaac29 | -11.33469 | -44.85417 | 2025-06-07 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c2f9d2f-b9a1-30d0-a2d6-57f8a122f232 | -6.28602 | -48.50714 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ad90840-8342-3576-a765-a0942ea6fdd9 | -9.50735 | -40.36826 | 2025-06-07 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a1dd2bd3-0c71-3420-9f7f-003eac6f3f4a | -10.46411 | -47.95026 | 2025-06-07 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 486dfd8f-d5b4-3ff0-82ae-724263d03d3f | -11.81513 | -44.26266 | 2025-06-07 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4d12ee3a-2511-398f-9f92-4f8509a9d7ad | -12.41865 | -43.81291 | 2025-06-07 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63eac52a-ff07-3c33-aefd-968701c83acb | -9.55575 | -47.77325 | 2025-06-07 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d820301f-2c5a-3009-b43c-84af017002ab | -6.96539 | -42.91269 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 464e520e-af47-33ea-8b62-1b3dc5c896cd | -6.96461 | -42.91748 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59f20c5a-fbb2-3f8e-a92e-4af6fe4fe1ab | -8.44795 | -46.48115 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52bd367c-9cb9-3912-ae46-eabc8d5d102b | -6.94614 | -42.90965 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a51cca4-d714-3859-bc35-37c643e0c937 | -12.28538 | -50.10025 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e719fe9d-3cd7-364d-a5af-b4d1c34d2bf1 | -12.27197 | -44.60545 | 2025-06-07 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73ba35c8-b30a-3f68-b61c-cbbc69abe685 | -13.53126 | -40.68972 | 2025-06-07 03:55:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 00b6211c-661c-3693-9d00-598afd2595e5 | -12.2782 | -50.10697 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 444b9ffe-c24d-3c46-a2ae-d615d20d6262 | -7.67782 | -46.09295 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50017219-049d-3136-9cbc-3218b9df0b25 | -8.45147 | -46.48513 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 822cae68-6620-37a5-a320-f2c8e024ddb5 | -10.89709 | -42.24331 | 2025-06-07 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22ceafd8-6cbe-31ae-8c45-a5071d810ba7 | -6.94999 | -42.91026 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40766252-3561-3e6b-a93d-463d530a69d6 | -6.94821 | -42.80193 | 2025-06-07 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9dfc9ecb-4868-3f00-b147-5477f0bcea3d | -7.72321 | -44.16962 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9eb8e885-17a7-3d43-b608-50f6aacaea3a | -7.73082 | -44.17474 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| be98e0ad-0e05-37dc-8fc5-c61b0254274e | -12.33435 | -52.48001 | 2025-06-07 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bce0a615-6cf2-3793-9659-a4ad3273b4e7 | -7.72795 | -44.16658 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7efadf36-a3f8-34e4-a8d1-d54d24077bae | -7.20645 | -43.11566 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c5a153ce-c72e-3946-8eb1-cd415d7fb4ea | -7.73268 | -44.16367 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6cf2d3e4-61cd-3cf3-989c-e445c6d3f079 | -8.87541 | -50.18928 | 2025-06-07 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b46236dd-a4b0-3912-8963-b5d1307a9bfe | -7.72607 | -44.17779 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 943b3cc1-34a0-31d2-985a-3e383d3b9107 | -7.72544 | -44.18154 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c1f26f5-2e29-3504-97e2-650d984c963d | -6.24166 | -48.55906 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04e26e79-0d0d-397b-af31-f12b510e595d | -7.86451 | -47.90308 | 2025-06-07 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e74c8f3-39c5-3576-a539-c00936cf1453 | -8.21249 | -48.98257 | 2025-06-07 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea6cfd6a-d3ce-35cf-a360-192cc0e07b1e | -6.23826 | -48.54557 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b816f9-d3b8-3180-94ee-f2f77d689a8f | -7.22281 | -43.11325 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ea2a77c-9189-35d4-8a68-4b0cabf7d54f | -9.40155 | -48.44001 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1577f069-ed16-39d0-9779-23b78ef5628d | -6.95848 | -42.90667 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 85493ae7-c4ef-31e6-9a17-2cc7481072d3 | -6.95927 | -42.90186 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 01d2eafd-313e-3c8a-99d3-753863413f8c | -7.21504 | -43.11201 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e2cba227-8ff1-3ba5-97c3-f8ff7813ff5e | -13.06915 | -49.24722 | 2025-06-07 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecfce639-ce29-3648-87f5-32c4154a85c7 | -12.77879 | -48.72361 | 2025-06-07 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c39a58b0-7c78-3c77-92c0-4513b3e0e7f4 | -6.95077 | -42.90548 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1c74622-1932-34a0-820e-0e4fbdcae7e5 | -7.73678 | -44.16445 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 27c89f90-7cc6-3e37-aa05-a177a99b731c | -11.78212 | -47.39639 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d1216465-a674-3717-9975-b4b80711984b | -14.70482 | -40.97336 | 2025-06-07 03:55:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b3d33202-ee27-3fd5-931d-c966d4bdda2a | -11.81426 | -44.26766 | 2025-06-07 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bf99be3e-cc2b-32f2-8ef5-22ef6c4799a8 | -9.40437 | -48.4441 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7a9c20f4-d7d7-3de5-b343-2a63b359ef33 | -12.77939 | -48.72045 | 2025-06-07 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2238db6d-8b54-3600-b05c-8ab82e2fa639 | -11.81815 | -44.26833 | 2025-06-07 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 723107f1-9d2f-31a1-b2a2-7c7cc8f40f24 | -9.40216 | -48.43657 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6147f406-e8a8-316d-868e-82f84688e754 | -10.24526 | -48.46743 | 2025-06-07 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e67070fb-81e1-3dc7-9527-e5d6a8ffb928 | -9.06375 | -47.90918 | 2025-06-07 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2de6573-2e97-393c-9b37-2aca65940e89 | -6.23963 | -48.55679 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6bb13df-a5fd-3e26-ad08-4edf6024282b | -11.78014 | -47.40697 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2ca17baa-5d66-363f-b5da-eeae15a16aab | -12.27471 | -44.59 | 2025-06-07 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a36ebe1a-efc5-30b4-a3be-99ffdc21bdbf | -9.05708 | -40.07655 | 2025-06-07 03:55:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0f60aa77-200c-39e1-b4aa-a0aa640609c2 | -9.07783 | -47.14033 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ea0f04a9-b612-3bcf-ba8e-f8dd8cbcff7c | -11.78687 | -47.39736 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 28d9ec97-401f-39be-b5fa-e8c53ee324c8 | -9.06319 | -47.91238 | 2025-06-07 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68a4e24b-35b4-381d-b434-cabf98b9feff | -6.95305 | -42.91567 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bda70cb0-4282-3ba5-8646-afd37a07dc78 | -8.20934 | -48.98527 | 2025-06-07 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1a970e1-53b1-36d1-8b05-9294d2cf7b7e | -14.13376 | -44.54132 | 2025-06-07 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 436c6a62-8597-342e-8bfe-cde0336bae7f | -9.12558 | -46.88742 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5729abb1-0a69-3f3b-9c23-1c97c5f7b85e | -6.59847 | -43.89814 | 2025-06-07 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a42d7e0-a0dc-3c21-be71-2ea5dc64f4a5 | -7.18149 | -42.82597 | 2025-06-07 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a736e19-5f37-3698-971d-4f9bbf8a5f17 | -7.72956 | -44.18223 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6bebc5a4-e0a1-3fb1-a8df-51d082449ad4 | -9.40629 | -48.43387 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c53eb88-2395-3468-ae36-e3eda59851cf | -6.23753 | -48.5496 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574aeb83-1577-3af9-aec8-5494362bf1db | -7.72857 | -44.16289 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a5db2281-d8a7-392a-822e-fb1bac1a7ed4 | -8.45557 | -46.4933 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ca6b130-2283-3b99-b046-237cbcfb74bc | -8.20685 | -48.98159 | 2025-06-07 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94d9e53d-6dbd-3446-b4aa-2f5c7886a28d | -8.87627 | -50.18476 | 2025-06-07 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cefb7d06-75cc-3ace-9f0f-c382fde8cb25 | -9.39902 | -48.44321 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec450010-6901-3c1d-9c54-2912008f024d | -12.9624 | -46.76559 | 2025-06-07 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c24215db-0363-30c4-8efa-616aac009068 | -12.33552 | -52.47439 | 2025-06-07 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54c3d023-908a-3bcc-b1e6-61555ba6c58b | -13.0639 | -49.24613 | 2025-06-07 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28049411-1288-359a-9ebc-14dedd74b404 | -9.40093 | -48.44345 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README9.md)
