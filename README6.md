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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc9241a2-2c82-311a-afb7-5e89fb047425 | -5.7927 | -45.12203 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b2f95387-f313-3737-8137-aff740b8cb29 | -5.95663 | -43.4881 | 2026-05-26 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47bd7aae-95b4-3811-808c-3059a70061e7 | -6.72713 | -44.36911 | 2026-05-26 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94de42db-02b1-392c-a3ef-048f57bf7852 | -7.01236 | -44.99182 | 2026-05-26 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 336007a9-3fbf-3c8c-8d40-b8bddddc7cfe | -8.61232 | -45.02934 | 2026-05-26 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7889d1a9-65c6-385e-bdef-62454bcbf073 | -5.79209 | -45.12566 | 2026-05-26 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba24d63a-9f91-3359-91b9-73ef9c9c23dd | -7.13369 | -44.05975 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0d66d40-6515-38fc-90c2-6575d32e19a2 | -7.13667 | -44.06487 | 2026-05-26 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b42881ad-6530-3667-a16f-2d518cf8169b | -7.57441 | -50.18076 | 2026-05-26 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1bd5cec-d8f0-39fd-ba41-5f979329f34c | -8.55611 | -45.98642 | 2026-05-26 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aea74454-6e87-3e09-926f-88e5809aedcc | -14.25042 | -45.8282 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37841ba9-129d-329e-b13b-b5f23b57fd34 | -9.37124 | -45.46393 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 768b8af4-6a0e-330b-b1d9-b5dbea75afc4 | -9.67596 | -47.0499 | 2026-05-26 04:12:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b979402b-8db3-3619-b8d4-42fbf469ef8f | -12.44651 | -47.88419 | 2026-05-26 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56ee65f3-698b-3545-a4f1-ea37d0c48125 | -12.69901 | -44.95922 | 2026-05-26 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79edb29c-febd-3aa1-b6d9-3127bd5decca | -12.46298 | -54.45593 | 2026-05-26 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc4a2940-c04e-33c4-96c6-027899482f00 | -9.36556 | -45.47321 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2047e6ce-d0ca-3ceb-97b3-f569ce1c4e51 | -9.36739 | -45.47193 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 28c8107f-80f2-3598-93b8-61604fd22d22 | -12.03991 | -47.33704 | 2026-05-26 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0b86e27-5e42-35ea-8158-99ee45b9275b | -9.29918 | -45.49093 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e697d7-6355-3729-92c8-cbd094c064b6 | -8.98634 | -46.82159 | 2026-05-26 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71e93d96-a2fb-37d4-9f46-bb90500217d4 | -11.36335 | -52.96183 | 2026-05-26 04:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ac5c6d81-69d4-358c-9156-7f9d9f5dddfe | -10.60323 | -44.32437 | 2026-05-26 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 12768b18-2765-3cce-91ae-8d423344320f | -9.29338 | -48.58147 | 2026-05-26 04:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 932677ad-1e4f-33a2-8db2-5615dc4ce759 | -10.60032 | -44.31948 | 2026-05-26 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a2782890-9ca9-3a44-bd19-1fe6ef84a598 | -11.78827 | -46.47403 | 2026-05-26 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f054d79-23dd-3bef-a106-a764e25ec39a | -12.14145 | -43.58596 | 2026-05-26 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e33142dd-5640-32b6-ab16-1ed78843a44d | -13.28246 | -48.86277 | 2026-05-26 04:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe68c26c-a6ba-3e8b-bfdc-42512c7523a8 | -9.35473 | -45.47484 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e14476c-0cac-3248-9e7d-108094161be0 | -11.21445 | -53.82992 | 2026-05-26 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9f8c0ee-3d8c-32e2-926e-7d5a25a597d6 | -9.44768 | -50.8473 | 2026-05-26 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ad0818ca-fbf7-3fb0-808d-9cc3ae077565 | -11.17608 | -46.83617 | 2026-05-26 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9303c966-b153-34bd-b6e5-e68f561cacd9 | -9.35286 | -45.47614 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 52dbf217-fdc2-317c-9c26-4025ca49771e | -14.16315 | -45.44185 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d6c9b9c-b2f0-3b78-8154-d966e73576cd | -8.98562 | -46.82576 | 2026-05-26 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1285cc70-4545-37be-8bd5-826eef5e72e8 | -14.16238 | -45.44624 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebbdcf37-2fb8-33db-abb9-2f10c9d573ad | -12.45637 | -54.45446 | 2026-05-26 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b874cd8e-e6ca-34ad-9af4-f227a7f066a8 | -14.03916 | -46.3479 | 2026-05-26 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff385310-3788-3db0-bb28-e97e3fe54d56 | -14.04215 | -46.35358 | 2026-05-26 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 692e273b-6416-3bb5-b03e-690a7b42dc37 | -12.23132 | -46.60473 | 2026-05-26 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e94289b-ceae-3dce-8980-1f6571431865 | -12.0471 | -45.27544 | 2026-05-26 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d0c73fd-b41e-3cf8-beb5-696aac7f6deb | -9.37217 | -45.46764 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a1d678f-cbd1-35b2-a644-658472be3773 | -12.45887 | -46.52103 | 2026-05-26 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f460e198-7305-3d42-990c-7793d953af6d | -12.69975 | -44.96062 | 2026-05-26 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c269099d-e0cd-32c2-8c3e-b6fb0a693613 | -14.24667 | -45.82755 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2566830-3605-3299-a2b8-9ec68dd4c384 | -10.63527 | -48.32687 | 2026-05-26 04:12:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fed7b55-1d2e-32fc-8975-b34369bf967e | -10.60757 | -44.32076 | 2026-05-26 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 603584f7-5bdb-3531-a1c2-1ea4f15c0528 | -12.67318 | -43.09324 | 2026-05-26 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 163439ca-96f2-3efd-8111-d6bf27645002 | -11.78735 | -46.47716 | 2026-05-26 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6c73b83-d586-3973-8d52-190921bc9a71 | -11.22095 | -53.83141 | 2026-05-26 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1fc50e9-ff37-3f4e-aced-53ce0e5603c6 | -9.36823 | -45.46692 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d7606dd-18f6-3716-b5e4-3c07e9346df3 | -9.36162 | -45.47251 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dae89e59-27ca-36cd-83bb-27918b121a71 | -11.36433 | -52.95699 | 2026-05-26 04:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 673393b0-265b-3d02-b559-7c49c6399a08 | -10.91996 | -54.12313 | 2026-05-26 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0787c109-5e07-3ff0-87b5-4d9bb5be8cd6 | -9.35079 | -45.47414 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b055a6b9-1dea-3986-ae7a-ce823dd53087 | -9.35952 | -45.47052 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64e8037b-67a2-3a3e-8343-70d381d21ced | -9.29129 | -45.4895 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a751c53a-0de1-3666-8072-0685e8bf39a0 | -14.25417 | -45.82887 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e374d7d-e005-3077-bd38-d24872382e0f | -13.28157 | -48.86758 | 2026-05-26 04:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 359e95f4-6d51-35bb-af16-00a2c1a92bea | -10.92121 | -54.11703 | 2026-05-26 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25c07430-493c-37ef-92ce-f08a050a3515 | -14.24588 | -45.83213 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96fa22c6-8ffe-3994-a121-7cba6b57e2ea | -11.96859 | -46.79137 | 2026-05-26 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 98220076-5f63-31a4-9ac2-c4a54eb51a15 | -9.29523 | -45.49021 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 974d65e3-2744-3900-b26e-8b2b580d4c3d | -11.97084 | -47.37833 | 2026-05-26 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4020ef83-fd06-3a0f-b290-82478c57f270 | -9.3568 | -45.47683 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 284bbc80-1000-384b-967c-d1a8a12f183c | -9.36643 | -45.46821 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e11113a-ee7e-3a63-a3bc-848f1fff4e81 | -12.23068 | -46.60835 | 2026-05-26 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1a4b963-52a9-3862-bf94-2d50235dc7e4 | -8.97925 | -47.98396 | 2026-05-26 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be1c0312-44c9-3c56-8fbc-8b1a1138448b | -8.97456 | -47.98318 | 2026-05-26 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0be1fde1-8b70-3e70-b73e-6609e0455e71 | -14.16682 | -45.44252 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 983f3c21-423e-398b-a627-de141858df6a | -9.30691 | -48.58968 | 2026-05-26 04:12:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13eebe79-d87e-30b6-a406-15a181cd455e | -10.62972 | -48.33091 | 2026-05-26 04:12:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99c56e1f-6358-3636-ac39-14cd3b52e1a4 | -11.17692 | -46.83535 | 2026-05-26 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9113695-4713-38d2-b05c-b2e01e07bf3f | -9.30305 | -48.58334 | 2026-05-26 04:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3438cf64-0866-33bf-b44e-52f787eab863 | -11.61411 | -47.90284 | 2026-05-26 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d58928a6-4024-3eae-9504-15d0335e188d | -8.99067 | -46.82234 | 2026-05-26 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deb96552-de01-38d7-8043-eef7f92a6018 | -11.78763 | -46.47773 | 2026-05-26 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48afb8a3-5686-31e1-bddb-56e63f510087 | -9.30208 | -48.58872 | 2026-05-26 04:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff8fdf09-2e13-3a67-ab67-963cc29719c2 | -9.3625 | -45.4675 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e1b4f65-6db4-3f37-8e9b-b58e9b5527e3 | -9.35768 | -45.47181 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d8adb098-2051-3217-acb1-a25ad9b296cd | -9.37037 | -45.46891 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ed2f174-f385-3786-8f72-52bf88ba5272 | -10.88312 | -51.21413 | 2026-05-26 04:12:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d37dd942-9478-39ed-98ec-e1ed9c6c77cb | -10.60395 | -44.32012 | 2026-05-26 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2920e00-68bf-3add-995f-f05ef0797529 | -15.78007 | -43.85598 | 2026-05-26 04:12:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b8d59e97-6173-3596-b267-c658450e5090 | -11.35911 | -52.95092 | 2026-05-26 04:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7a06865a-5cfb-32c2-9a6e-7b34b1b8df4f | -10.5996 | -44.32374 | 2026-05-26 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0e677b77-d6c9-3f0d-99ff-b749cb3ac0a3 | -9.46503 | -46.11372 | 2026-05-26 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b39c032c-c26f-35db-800c-332bc8884973 | -14.15301 | -45.35599 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a48b02b8-ad82-3e21-a51c-eab92b01d93b | -11.35717 | -52.96054 | 2026-05-26 04:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 43afa3fb-1011-3614-a13c-a4f41a7bef2b | -12.46179 | -54.46157 | 2026-05-26 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db78d8ed-758a-3471-894f-c61fb69a5f99 | -8.97836 | -47.98896 | 2026-05-26 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb131a4c-7985-3f1f-a846-974cdd69bb4d | -9.34994 | -45.47918 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0cc76340-3985-3fff-bd28-e273e3d17f77 | -11.35619 | -52.96541 | 2026-05-26 04:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e95ca290-d656-31cb-aec7-282c68e18ebf | -9.30225 | -45.49671 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54b0e20b-3504-3f7e-96e8-81d45ec18d4e | -9.37517 | -45.46465 | 2026-05-26 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1815f61b-5648-3186-af87-4a01e41008e3 | -10.63436 | -48.33184 | 2026-05-26 04:12:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9454d593-9d5d-3c17-a162-64ca81e2bfdd | -12.44856 | -54.45865 | 2026-05-26 04:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c199d976-0dee-33fd-b31e-986c18f1a28f | -11.73858 | -54.81429 | 2026-05-26 04:12:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77dec913-05a4-3fe4-bb0d-1738227b2d1b | -14.15734 | -45.4317 | 2026-05-26 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01f7a10a-ee44-3441-b265-9c89900091e7 | -11.73993 | -54.80786 | 2026-05-26 04:12:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README7.md)
