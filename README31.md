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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c312f98f-3cca-3d76-968f-9141d4de8b5f | -3.48276 | -50.59006 | 2026-09-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1169a76b-bb04-3185-80fd-7590ee763ed8 | -1.44525 | -54.22412 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98a4ad84-47b2-340d-a5b2-e9f72574436e | -1.96631 | -46.40788 | 2026-09-01 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88b85298-a5ba-3719-b04d-38616eda948f | -4.21138 | -48.60566 | 2026-09-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f71f1b44-270e-3e30-9f03-75f0b2571e44 | 2.24298 | -50.74591 | 2026-09-01 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08c3ab03-ad0e-321b-ab7a-7a53b28a827b | -1.59041 | -50.43807 | 2026-09-01 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c9b9559-f50f-31dd-9caa-d1f8efa1474c | -1.95803 | -48.11694 | 2026-09-01 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9542ca25-aa49-3d14-95e2-b8b6b1722985 | -3.97744 | -43.11 | 2026-09-01 04:38:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d91c7b8a-eee8-37ae-9bfb-119b8e810377 | -1.46943 | -54.20831 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69a7ce4f-20ee-3be4-afdb-3d2a3d4b948c | -6.9552 | -55.635 | 2026-09-01 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| ec40307d-e236-3156-9c58-e8293f67bd84 | -10.3577 | -49.9957 | 2026-09-01 04:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4b638826-17c9-3466-aa6d-6e0ce6ad7310 | -8.2603 | -54.9186 | 2026-09-01 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 38a75151-b38d-336d-bce6-beeb8300ec86 | -8.279 | -54.9174 | 2026-09-01 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| cd7f0f21-705a-37f3-91d3-6478978e46ca | -8.2788 | -54.9376 | 2026-09-01 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6951f4f8-aec2-3d08-adc6-80b08fd091d0 | -7.571 | -60.4643 | 2026-09-01 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| f4e01886-bac1-3858-b9ff-cdf174aca1b6 | -7.3488 | -60.5691 | 2026-09-01 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 209392cb-ae69-337c-be30-254fdb39a5d8 | -7.64523 | -46.71328 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e745627c-3492-3489-b65d-d399f12a336f | -6.25591 | -55.4272 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67364d99-17df-37f9-b2d7-d7afc8d53630 | -6.13297 | -55.64626 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0c220f5c-e1d3-30f5-bbfc-c4d88c5a2988 | -11.26773 | -50.56754 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7da85c5-c264-3eda-95cb-a9aba788624e | -10.35152 | -50.00856 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cb46c49a-2e71-347f-94cc-e5296d008a7d | -11.49178 | -45.0962 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09735125-99c9-33e6-b696-4b1f1bf14d60 | -7.05847 | -52.71828 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24c387ff-6837-3282-9bd0-1d80f55bd08f | -8.84839 | -47.082 | 2026-09-01 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5320eb22-19b6-3439-a845-5f6d10d8731a | -11.26941 | -50.57858 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fc833890-a3e0-3b62-b4b0-fc1546d48e06 | -6.96186 | -55.64481 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1959749f-d8dd-330e-ae9d-5a411d30c9e8 | -7.29897 | -60.57794 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7ae9052-18fa-3251-9969-a219beeb1964 | -8.79041 | -62.48404 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f54e7e20-7085-308c-8643-f5ea956940f0 | -8.27559 | -54.92564 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ce730673-a541-3443-953c-9ca065049f6d | -6.18403 | -57.7356 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5ded7859-03ac-3fdb-9066-fb26dfb7aa66 | -8.81334 | -62.50462 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8de8c01e-a0bd-3ebe-bc52-2cc3edfa9d2a | -6.185 | -57.73001 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2f28787b-13c2-3b0d-ba78-dc5f73ecf652 | -11.20456 | -45.11152 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e69ae555-0252-3c08-bc1e-a568cc53e6a1 | -10.32621 | -50.03995 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8153b33-230f-3582-9b64-413de37d95ed | -4.75927 | -50.6669 | 2026-09-01 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| debade0e-aff9-3a83-8145-c823a8f7c9c4 | -6.60157 | -58.5971 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f76c4e32-50d6-3923-ad24-80598bb410d5 | -11.49127 | -45.10009 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d273db5-e9f3-3fb4-9c24-7d267714cb2d | -8.71234 | -52.36429 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 824abfe6-ddc2-36ab-9bca-56cad2844436 | -11.68533 | -47.15236 | 2026-09-01 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44e97ebf-be7d-36bc-88a7-19e037c74121 | -7.34685 | -60.58229 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6ab704b8-ef64-3350-8355-4b1e14b77151 | -5.89061 | -52.15422 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6cf694c-029f-3ea6-9fb2-9c297c47ff73 | -7.34297 | -60.5938 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78d7d373-4377-3449-8504-30825cee0876 | -6.94482 | -55.64185 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0a745c4-d087-359f-a810-9a7dd3c26fa6 | -11.90956 | -45.06323 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5806d0f6-c317-375e-8142-64b60ba6ab34 | -3.51167 | -56.31884 | 2026-09-01 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c25f3545-6673-3c31-b3a0-8fc17c021a17 | -7.5583 | -60.46927 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9413effc-527c-3ee6-b0b1-f99d74b56ff7 | -9.83448 | -47.8294 | 2026-09-01 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfb5ee91-7bb0-3589-9e24-765c6d9a1dd8 | -9.67133 | -48.31687 | 2026-09-01 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db68b39a-175f-3507-a890-43c5356acfc1 | -11.06815 | -51.53367 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7a8061f-b642-3a07-be2e-6fef5b3cfabb | -8.5879 | -54.7708 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3622246-3e4b-30e6-b35d-b547faa399f7 | -6.12407 | -53.55051 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25b2fc2c-022c-3734-9309-206d2e0602a3 | -6.81101 | -43.52974 | 2026-09-01 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4bf83709-e6a7-33d7-8cdb-677d7f623940 | -6.18902 | -57.73642 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17736bd9-d8d4-332f-94ea-04ac4ccd228f | -10.32267 | -49.95321 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1daafc0-7906-38d8-83db-33f6b183a84e | -4.85906 | -55.83273 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae8e5f1b-53e7-37fa-ae9d-4cdf65b00574 | -11.48254 | -45.09222 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c093451-49b2-3510-af8b-83b4ff493810 | -6.25147 | -55.47992 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af8c740e-da2f-3fbf-8b2d-aa27a9d9494f | -11.72236 | -47.65018 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d5e2686-7609-36bc-9c0c-dcf62f88abf4 | -8.12563 | -54.96437 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4956aa9-20ab-33a3-afbf-66238340eca2 | -5.25388 | -55.9006 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f64f07d-b6fb-319e-98c0-1bed32e65a71 | -11.07092 | -51.53777 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5efb6260-889c-3ac4-9536-567c419b09ad | -7.04305 | -59.22451 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b15cb59-6ae5-374d-8ac0-181bf74c111c | -11.67675 | -47.5977 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 963fbdbf-6abd-37fd-8d20-ecc7548f70a1 | -10.3293 | -49.95425 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b865cb8-9261-3585-b938-6afe37f7b270 | -10.74914 | -54.06356 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3629443-3b82-32dd-b2f8-2a565005455c | -9.16322 | -59.54103 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6003517d-deb8-310d-bcd6-60962d5150be | -5.53863 | -46.59785 | 2026-09-01 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39c5464f-479c-3133-86cc-e135d60a9460 | -11.22785 | -51.27686 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1c5ce26-f862-3043-bfab-b6bdf4a82b18 | -8.79146 | -62.47858 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a01abceb-01a0-35fa-8576-85c6a190a82d | -12.07084 | -44.98658 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3940d674-256d-38ca-bb99-03bb75513636 | -7.08503 | -45.65705 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b619afd-ab4d-3512-b984-e8b28764777d | -10.21112 | -50.32254 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f84d3a6-cc94-3368-963b-34e709cb68cc | -7.35722 | -60.58266 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 40ca92ed-dba6-39b3-a081-40024a734663 | -6.20578 | -42.51762 | 2026-09-01 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d145c43a-7854-3dc5-ac5c-d895a0680fd6 | -6.74285 | -55.45045 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8127cbc-a57c-3b99-b0eb-361bc4ceb6b0 | -7.63379 | -55.28689 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62f3940e-23b7-3c0e-be6f-4f8d1ad4ace5 | -11.52361 | -46.9277 | 2026-09-01 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6148863c-3b00-369b-b37d-fe6900ac0ee8 | -11.26057 | -50.56999 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0dbacab-ca48-3194-87b1-8f901ba28981 | -11.01058 | -48.3818 | 2026-09-01 04:40:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 814c11c1-f019-3bd0-92a1-492016c34f45 | -11.6575 | -47.6033 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f3c94da-f363-3f9e-a871-0ddf93e74c21 | -12.06793 | -47.19844 | 2026-09-01 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab2f10f9-d94b-3169-a908-977406f82875 | -11.15633 | -45.0474 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4c78a24-4262-340f-829c-64635f7d9fb8 | -11.90841 | -44.81637 | 2026-09-01 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 781bf9bb-1a91-39fa-9902-782183575dae | -9.39279 | -60.56897 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d17caf84-6fed-3456-b787-711c4110b17a | -7.03764 | -59.22346 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 632f0d5d-487a-3f91-ad70-dfb67dc9c0d5 | -7.90121 | -44.24313 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cd8bc86d-eb33-38ed-a970-90063757238a | -11.29366 | -50.57527 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e23eae86-f12b-343b-868d-8fa7463bc39a | -10.77101 | -54.04498 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f121cce-1e60-3317-868d-63fc8752b883 | -11.25091 | -54.00513 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 215647dc-6f10-3c14-b80b-2691eca4717d | -7.03827 | -59.21992 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 816d7521-6988-3dbf-ad9a-67c6d9c48a60 | -11.27548 | -50.58313 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c8964ac9-c748-37e7-a9a9-9cb2f017e995 | -7.02716 | -55.64756 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 838052a5-1188-3936-8010-ec6ef49a976e | -11.24792 | -50.58591 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0104a747-ad0a-3579-822a-9d5533fa2436 | -10.865 | -45.34872 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f65239f-e9a9-36cc-933a-601acfcbaca7 | -10.43213 | -46.52899 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f2c5d74-27ac-3929-9337-5c411540b6a1 | -6.2546 | -55.43504 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8143aaa1-2672-3375-93db-c3b46c302f09 | -8.63961 | -47.32306 | 2026-09-01 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17e5c17e-6489-3651-8302-b58f32c68f24 | -9.39772 | -60.57396 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e12c1245-7009-39b2-add5-5ffda51d061d | -11.3743 | -45.23343 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff9cff82-cd8c-36eb-925f-8a455550f28c | -12.09741 | -44.982 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
