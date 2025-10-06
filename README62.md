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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d7cc363-6bd0-3ab3-8cd1-2b3f5fcde0fe | -3.53762 | -52.80457 | 2025-10-06 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 180b8cc6-e9b5-31e1-91fc-676113609d01 | -3.57037 | -52.6985 | 2025-10-06 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2dc921-d298-347f-854f-75022cca3e31 | -4.31357 | -50.54769 | 2025-10-06 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a66f1e4c-3473-3656-808e-81393712d033 | -2.7846 | -54.41301 | 2025-10-06 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5676f12c-658f-3266-92c1-7b58c177f864 | -1.12049 | -53.0523 | 2025-10-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d084ab10-e8a1-3592-a44b-a168322fba1a | -4.25287 | -48.57222 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07bd2ca5-d7ce-37a1-9b70-a83df3d65d40 | -4.76917 | -46.60852 | 2025-10-06 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 041084f3-005d-340f-bd86-92c1acfe53a5 | -3.28979 | -52.54952 | 2025-10-06 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a33badb8-29b7-3709-92cc-d3a134886274 | -2.92792 | -54.21158 | 2025-10-06 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1b4659a-9659-316f-bf81-071a459ccb00 | -2.69676 | -54.76632 | 2025-10-06 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccacd4e3-7946-35a9-93e3-918d4e0af30c | -4.31127 | -48.23993 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbd74d4f-3ed1-3a22-970f-3caf1b2308b4 | -4.22733 | -46.76347 | 2025-10-06 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33aa87c2-1670-3372-9ea7-d6b3d74ee859 | -2.59158 | -48.12611 | 2025-10-06 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 336b467c-7290-3b90-a091-991d607d13b1 | -2.24544 | -47.87125 | 2025-10-06 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d4e73e7-6efb-300a-b0ba-db4b804deef5 | -1.11974 | -53.05719 | 2025-10-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f79ee72-e4bd-3007-a076-9a3e7c223e47 | -1.1244 | -53.0529 | 2025-10-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a459034-e202-3c1a-9c70-fab3bced765a | -3.8391 | -51.7392 | 2025-10-06 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b17987cf-a100-3f0d-8413-05427389de38 | -2.20171 | -56.9184 | 2025-10-06 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3923771d-3d86-3aeb-87cc-83179ba5f7aa | -1.62978 | -54.45494 | 2025-10-06 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83178656-bfac-389e-9972-4bab982dce7f | -2.20504 | -56.91892 | 2025-10-06 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0d6c526-f4d8-3720-aa9b-554b67cd7e6f | -3.85514 | -52.32537 | 2025-10-06 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0e1c508-bf64-3e7d-8c89-4d96e537f500 | -21.3916 | -45.07729 | 2025-10-06 05:16:00 | AQUA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.8 |
| 70d80329-b5b7-3b4a-ab8e-8ecad55a1078 | -21.3943 | -45.08321 | 2025-10-06 05:16:00 | AQUA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 98477e1c-5935-3eaa-83a1-e2895d18c0ee | -23.39252 | -45.38392 | 2025-10-06 05:16:00 | AQUA_M-M | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 3671afa6-a169-3f27-b516-8985ebc4fc1b | -20.35787 | -46.46751 | 2025-10-06 05:16:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 435df0b0-a2ee-37f8-ab4f-a6292f9d7d42 | -22.36236 | -44.20781 | 2025-10-06 05:16:00 | AQUA_M-M | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 88fb15ef-5354-3409-86ab-0f15f55d515d | -21.39811 | -45.06341 | 2025-10-06 05:16:00 | AQUA_M-M | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 7fe6c9f3-181a-33ec-bb4e-94623f8c8475 | -7.71526 | -46.25816 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09036388-b049-3cb9-b8d2-6aece0a79c8b | -8.423 | -70.12339 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b4ddf7e-8db9-30cb-8e89-d7b4c03bcfda | -8.51995 | -46.33124 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1c15ba9-e06a-3587-8694-62610aeacf10 | -8.42807 | -70.1289 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac177113-ab21-3831-80af-0476ff08e9bc | -9.33179 | -54.52633 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b68dbd4f-5eee-33fe-8457-87110868ebaa | -9.96319 | -48.74987 | 2025-10-06 05:16:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cc15477-e87f-387d-a05b-37a54e775e46 | -9.39526 | -61.43849 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eff84fa-1a5d-3954-96e1-ecbb65df2a65 | -8.52248 | -46.32725 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 619604ff-6bb2-3d21-a133-bf4f91008e36 | -9.32927 | -54.51511 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecd7ccbd-916b-34d5-8782-326c8a34e3ff | -8.52087 | -46.34025 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d5084f1-6670-34dc-b706-8f2bc3577873 | -8.61608 | -46.30864 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21fe4342-2459-3e5f-8387-cc7ea09972b3 | -9.33278 | -54.51925 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dffbc8ab-5da4-3008-b91a-a79389ae2cda | -7.95628 | -55.29263 | 2025-10-06 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87543e59-8352-3b4b-a86a-5c3322341e0e | -8.61111 | -54.97097 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 871095a3-18ff-3a6e-8bad-13fd0617029e | -11.07127 | -47.9195 | 2025-10-06 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e70283f-3d15-3940-883d-9e31ce0fafa1 | -8.44737 | -70.12365 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 052ffe3f-1623-364b-9b8f-9db41a42e6e8 | -11.91993 | -46.64763 | 2025-10-06 05:16:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47130832-0805-3cdf-a790-56f10a1707c8 | -8.61365 | -46.27192 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 53d62ec7-6831-356d-91e3-9d36768933c0 | -12.57182 | -48.13797 | 2025-10-06 05:16:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7372339f-10a3-36f2-8c11-837bbafd1d25 | -8.62087 | -46.31472 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc27a70c-0e2e-310b-ac03-e4a901d3e188 | -10.67162 | -48.47512 | 2025-10-06 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be83f149-c5b0-3252-991c-6b58138e075b | -10.32176 | -50.27084 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 51a46228-a976-3646-a343-8f15f3879dff | -8.61462 | -54.95921 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97bb4206-8f17-3467-b942-020e5f29c51a | -11.43695 | -55.05046 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e94217a9-2365-340e-9384-c8627ee1dc2a | -8.48036 | -54.69373 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7395a9e-4833-3930-883a-e0f8ceb1d207 | -10.80958 | -48.82082 | 2025-10-06 05:16:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12558955-ce64-3e31-b636-910940aa6968 | -9.48024 | -66.62765 | 2025-10-06 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca4de9b4-1819-3756-8a60-2730fce875ac | -11.06759 | -47.9162 | 2025-10-06 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98f0c68d-eb39-3a22-9119-3d3b2f47b645 | -5.64277 | -45.95807 | 2025-10-06 05:16:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e5e3aec-e71c-3b0e-9b19-1573d3dad60b | -8.63372 | -46.32231 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 51551911-d440-3196-8c32-3025b42adfac | -12.25581 | -49.21138 | 2025-10-06 05:16:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f1009d2-443d-38b5-a6ed-c68064cc7018 | -7.24746 | -59.53921 | 2025-10-06 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c447e5bf-09cb-3ea0-833a-3f3441c87084 | -11.02808 | -46.5467 | 2025-10-06 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f922964-a5bf-3cf2-9514-b53347a77a9e | -8.62692 | -46.3214 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 572b8869-535a-3525-9c2b-a502b7ed7cb1 | -8.62147 | -46.32113 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ae3478ca-9ccd-3782-b581-4c839fd41af5 | -9.61534 | -57.20147 | 2025-10-06 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 758d50c8-0b19-34ac-89e8-a85393cb7590 | -8.62765 | -46.31581 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ecbc78e4-440a-3470-8a2d-2ecd092aa20f | -8.62414 | -54.97536 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bb3145c-a51a-3ef5-864d-89d319a334d8 | -11.02115 | -46.54598 | 2025-10-06 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d740969-d8b7-3b2f-8281-9960c4418d2b | -8.62533 | -46.33368 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc219b81-2695-33c0-bba3-d98a157a4a82 | -11.50586 | -54.45751 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e3d5a61-67a9-30e4-af0b-46f0f8915e5a | -11.15813 | -47.93293 | 2025-10-06 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ace2ad65-5e0f-3e02-adb1-b6b0788d5e54 | -9.02336 | -50.59327 | 2025-10-06 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99d20029-d479-3388-8502-85de0a3e993c | -9.15014 | -59.53785 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68e5b6b2-c967-3177-a06e-e10822020801 | -11.38191 | -54.34788 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 692f1bb8-81c8-341a-a494-37fec51865fc | -10.43336 | -50.36052 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 096467e5-8d16-39ff-862f-f05e582bae5d | -9.39867 | -61.43907 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 114d027c-652f-3731-a39c-69e75c1b15a7 | -11.50068 | -54.46453 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c78c241-7fa9-37b3-bf28-b61eec74b507 | -10.36922 | -48.14955 | 2025-10-06 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df35648c-1a8d-33e9-9750-0ce2c42e60c8 | -12.26432 | -49.18972 | 2025-10-06 05:16:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e26a7ec7-2b4b-3eaa-be79-ebd108b745d6 | -9.32666 | -54.52151 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8abc1683-534e-324f-9009-6fa55496dea0 | -11.31876 | -54.34298 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084d698a-d2cf-3fb4-8bb3-969dc1225c33 | -8.44657 | -70.12796 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05c2cbf7-1301-35a7-b4dd-a6e60c2b56ec | -11.14335 | -47.16606 | 2025-10-06 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a15ffbe-7ff5-35ee-b41d-7de8b616b973 | -8.55298 | -46.24907 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 785d0fdd-241d-3c15-a22b-24a83a4ccd55 | -10.42841 | -50.35635 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 061caf4c-cc2d-3003-9251-83a30ebf0634 | -11.0277 | -46.5483 | 2025-10-06 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b9c422e6-b619-3e93-8824-7a02a6edf870 | -9.23578 | -51.82147 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c62aabe-b1b8-33a4-9ad2-cbb96d3c0bce | -11.15755 | -47.93796 | 2025-10-06 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19811645-8abe-3798-9926-fbd3e0bf33dc | -11.15118 | -47.93713 | 2025-10-06 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 907a402e-0d40-3863-b56a-07a46d9a1784 | -10.46223 | -57.50355 | 2025-10-06 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6d52ec8-66b6-30bd-84bb-b596557e502c | -10.9363 | -54.2683 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a0b4a98-b27c-3fc3-a988-56fc1994c4c4 | -8.61561 | -46.30183 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78fc95cf-4ea0-34d2-b7d1-c1d1d859736d | -9.39807 | -61.4428 | 2025-10-06 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 814bd941-4296-3d9a-9eb8-455a083e8869 | -11.42194 | -55.07067 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93957ae7-0a31-383d-b7b7-5f0fdbfc5929 | -9.34382 | -54.52802 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3bef070-6b69-3828-99b9-071d5e6bc3e3 | -11.45951 | -51.52811 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 245738f3-c08c-3932-a5af-69f6313725fd | -8.62097 | -54.96996 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee575286-4ca1-3426-9fc4-9b8f104dc82e | -10.31588 | -51.46172 | 2025-10-06 05:16:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e05b4ddc-ff43-39b3-af15-377c9d21aae7 | -10.04641 | -49.206 | 2025-10-06 05:16:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96fcbdda-e46f-3354-b4c5-aa64faf73f77 | -8.61335 | -46.26556 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65298f59-7bc4-3f2b-a248-3fd6e84a0d23 | -11.51417 | -54.45866 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a58bae33-7405-3a1e-aebe-c930b9fcdcb3 | -9.31793 | -46.01659 | 2025-10-06 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README63.md)
