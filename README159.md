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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 736e81a5-8a29-3910-8ec4-3d62cfc52b2c | -12.37871 | -41.96004 | 2026-09-21 16:01:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| d6f547c3-1fcd-307b-ab69-b6ba5624847c | -12.47286 | -44.67992 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bd4e45f6-20b5-3911-b9c8-7e110e23a5fd | -8.77562 | -44.29908 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 0db31983-6753-3ff7-97d6-e688ae6e7914 | -7.39654 | -34.94973 | 2026-09-21 16:01:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| b808f389-f7b2-39dd-a226-99a0cd485b87 | -12.43615 | -47.06336 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 5fb848ef-5b60-34fa-b962-40c72dbfe2d9 | -9.57351 | -45.4314 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 329b6a09-ad1e-321a-8b46-e31f9f4ec785 | -10.73301 | -50.78632 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 31d0353c-ba2c-3ae9-bbcf-15c4f7a172ba | -10.28165 | -50.23576 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 900c6873-f386-3d3e-8b2c-98a0d54a5a90 | -12.54028 | -50.0312 | 2026-09-21 16:01:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d6b8e343-74bb-3a95-9b9d-a0ea47f6c3df | -8.76106 | -45.85559 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4fde60f2-6cfb-3fac-9ad8-3f4c33404f26 | -11.15333 | -42.82888 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 1ef180c1-b9e4-31be-9fbf-a9cbfddfc1f2 | -12.81047 | -44.23491 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bb747fe8-55d2-366c-a952-f1f428048e7d | -11.9513 | -46.50451 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 87d8d328-a43d-3f45-a67d-99baeb3f6e80 | -10.55842 | -46.56068 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 51120bc3-8571-369a-aee8-2330a39e86ba | -12.80645 | -44.20331 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 20fb9851-006d-31be-93c9-20451ea25e40 | -9.39388 | -48.32836 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| aad55eb5-77df-3723-aeff-bd0a5d5ebb60 | -11.10451 | -48.30419 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| edb42943-af42-3d5a-aa26-c1ab871b8b09 | -8.69609 | -45.43773 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e0eef01f-a182-3108-b854-92aae77a1863 | -13.90787 | -45.49372 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7dcbab4-236c-39f7-86f0-222b01253039 | -9.53967 | -47.94626 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b0360d97-0143-34d8-9d04-13ee65740b0c | -12.44719 | -47.05791 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 37047d51-58fa-3439-9ebf-37456900bd99 | -9.45396 | -45.41306 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 39a4f481-8579-3bdb-b972-3ca5b6cded08 | -7.41415 | -34.80922 | 2026-09-21 16:01:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 36884cd1-d254-34ea-9eaa-b7ff12f9cb4d | -11.39754 | -47.28843 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 830f4fc2-0deb-309d-9040-e35d0c9a996f | -13.90312 | -48.57219 | 2026-09-21 16:01:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cc0b0540-0816-3cdf-b2c9-c62dd62fb424 | -9.58374 | -45.47856 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bd27852c-2e37-3778-b005-32e715df5df7 | -10.57829 | -46.5275 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 00febc96-6025-3989-b665-74613224018b | -9.45352 | -45.38659 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| f8896424-1b06-3a34-ae88-6c98a0907fa0 | -12.29827 | -50.66592 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7fead1cb-0fed-3f07-9e3e-9ebdb632ec12 | -11.47574 | -47.63969 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 21d6b43e-7e8b-3608-a3ec-8012a55a120a | -11.44074 | -45.34551 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1a73b642-2af5-3288-8009-2faf7b5daa3a | -11.67376 | -43.4572 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 7964041b-93b0-3a92-88d4-9227766be09f | -9.18516 | -46.4963 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 46f5af45-9690-398a-a815-d2875c884692 | -12.84629 | -44.20802 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d709db9-9d3c-3f30-98d7-f08e19464c44 | -10.08388 | -50.28774 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 033a394b-1b89-35ef-94a1-20ef873f8f53 | -8.94942 | -49.05117 | 2026-09-21 16:01:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a04f27b8-e6a1-3887-9531-dfe3308227f3 | -13.55135 | -44.89379 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bebc7a1d-8f42-3cd8-b439-b3c200e0a67e | -11.85994 | -46.85898 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 50b236dc-786c-3d72-8d9f-33b0023119f3 | -10.61913 | -50.59875 | 2026-09-21 16:01:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7c2d8460-4e6a-3372-a3fc-47726dbbad72 | -10.13427 | -45.93402 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 19dacb92-da76-352a-a2b6-5f1783544180 | -12.266 | -50.14898 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 404c8d73-100c-3d74-9002-836133272ea2 | -11.67764 | -43.45212 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 64a0643e-0a1a-343a-ae47-9703c5883064 | -12.10811 | -47.05176 | 2026-09-21 16:01:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ad72f63-bae9-3949-abe0-8c7a3c6cfff1 | -9.16204 | -50.01273 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 9402dbd4-cc1d-3dc2-9f44-a51397724c1b | -8.82751 | -37.41489 | 2026-09-21 16:01:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4ba5fda4-8c8a-327c-ac0b-8ae94cb6dab6 | -12.45215 | -47.06305 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b436e909-8335-3729-a064-f5daafbab2af | -10.26051 | -45.49522 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2d47a38b-c5ed-3438-879f-768da36827d7 | -8.84456 | -44.92868 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0da46296-14d8-38b5-9cb3-c1b9ea2fae8e | -10.8639 | -50.16212 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| eb891817-85e0-35a3-a3a5-24785f8fc490 | -9.2756 | -46.20291 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 99e09879-1ecb-3eb5-adc1-ebfbd2780d30 | -12.73787 | -40.98514 | 2026-09-21 16:01:00 | NOAA-21 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7a50adec-ac4b-3256-b1bf-167eea6d95e2 | -11.46343 | -47.63672 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a8928409-6375-3d27-ac0d-c23fe590939d | -9.54127 | -47.95879 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| fe32de43-e5c4-3a8c-b2fd-f1b1833cd095 | -11.43038 | -45.3857 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 55a4733c-dcc1-3516-83b6-d2cc178b4bd5 | -11.93348 | -46.50025 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e45bfd0e-cd29-3d71-a42e-bc902a8b3052 | -10.74866 | -46.3357 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4e679bb4-8086-391d-92c4-f68812e4a846 | -9.03497 | -49.82601 | 2026-09-21 16:01:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f6208379-7dc3-3af3-af82-8fbccfcf9ea2 | -14.87474 | -49.21345 | 2026-09-21 16:01:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d281e3c0-96f3-3b89-b936-776be32269fc | -12.54142 | -50.03845 | 2026-09-21 16:01:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 54362654-6a11-3b9d-bcea-c2acdd58ad36 | -10.0968 | -48.44016 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d259553f-ab4e-37a9-95b4-0a592a8f1d0b | -9.95896 | -45.72878 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 91a3e075-45aa-30d4-847c-35a233285862 | -10.66982 | -50.71611 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| be0da295-94cc-3ed5-b45e-a6e6069754c9 | -11.62673 | -45.3675 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 518af2d0-1661-38a8-8e72-7aaf1bcb319b | -9.88848 | -48.42257 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 60e7933d-e2ab-3459-ad18-f053309bab02 | -12.05454 | -50.07781 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| c5803b7c-a716-3369-83bd-0926d31a6702 | -12.43291 | -47.03492 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 016e24be-2fd8-3382-b614-b72d79c97a19 | -12.41913 | -47.01601 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 542235cc-f291-3258-9cdb-8c1d0d1d1d08 | -12.44689 | -47.06779 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a1956309-5eff-3e3e-a527-340b538ddb13 | -11.15306 | -42.82906 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 9df82ab9-08a3-394d-b4f2-7874a653c7af | -13.43578 | -43.82489 | 2026-09-21 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 80a9dfbd-32fe-3db5-b4e1-b4cba862e62a | -10.8139 | -50.14839 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| eadc8fa7-a83c-3470-ad9c-636cbbeec2d5 | -11.66552 | -43.45319 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1728d6ea-4617-306c-b3cc-7a554ced1f45 | -10.72593 | -50.78701 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 452a63a8-8c50-31fd-ac7b-0e6bbb83114d | -12.42188 | -47.04034 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9795b929-2058-3ac1-a0d8-e08c8b04ae82 | -10.96153 | -50.58526 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 735b347f-900d-3d66-9755-5f7b66e1c9c7 | -9.87656 | -48.47636 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 4d366903-a03c-3353-9b33-2daad132a346 | -11.92715 | -49.80415 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ed8a4f41-9fb7-3dcc-ba30-81a9d518944f | -12.04714 | -50.06986 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 2f4527a9-0f35-3f68-b750-08e7fd6526e1 | -10.81339 | -50.15678 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 0b25536f-6701-3ada-b3fb-3edfe3983a53 | -10.72434 | -50.77325 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| ab343745-e53b-30bf-b8ce-f7b998fe4c09 | -10.38579 | -48.91695 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 89b61878-a41f-3a22-843d-2313643a8633 | -11.09875 | -48.30803 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c4f3de9a-5a34-3067-92f5-fe78597586ba | -12.20423 | -42.23765 | 2026-09-21 16:01:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2e7b53d4-97ad-3e47-9fec-d2f3100e44f0 | -8.45528 | -45.08938 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85e508af-121e-3db6-9cf1-a079c1ecbc7d | -9.27601 | -46.20611 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7bdf38e4-542d-3878-8eb1-c75546298858 | -8.58894 | -44.54705 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 025a8ff6-9a27-31a8-bcfb-247e118b0a46 | -10.01902 | -45.21025 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 086b8ea2-7827-3a3e-96b3-a1b81ab4e1ce | -10.08606 | -50.28994 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f748a890-e094-3f3b-9106-0114c33b2730 | -8.69872 | -45.43906 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 2d4aa898-2934-3d97-a779-fc8c0085ce2a | -12.34778 | -42.21997 | 2026-09-21 16:01:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fc464b46-7807-35dd-a590-8b13cd640602 | -13.4274 | -46.32547 | 2026-09-21 16:01:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 41d57d47-4960-31a1-839e-892b1ee3cdd4 | -10.74965 | -46.31712 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 64690612-0bd2-3494-a941-5030a117cc79 | -10.4368 | -47.50581 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c33919e0-d963-3243-953d-5a4992bc7936 | -13.02755 | -46.97554 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 71e4d560-1cda-3790-91b5-111f58c9f3ed | -11.67808 | -43.4202 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ff58443c-218f-321a-99cf-f9050b37ecd0 | -13.02855 | -50.59771 | 2026-09-21 16:01:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f26be152-4a6d-30b8-9d44-d47020b724fc | -12.41995 | -47.03796 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 087a6be6-3319-3ed2-bd4a-172bd8fe2705 | -10.16204 | -45.56165 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| de15b1c9-b705-3446-a6c6-fb032408c476 | -12.45342 | -47.06135 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35cb97c7-851b-3d36-b41c-51c91caf1cfa | -13.43512 | -43.8198 | 2026-09-21 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |


[Clique aqui para ver as próximas entradas](README160.md)
