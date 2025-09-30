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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64af2260-ec2f-3c44-afa6-623fc09ed194 | -13.36512 | -47.29725 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71d3e2fa-c113-3432-809e-5e06ab0ef9f5 | -8.05119 | -49.70309 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87012481-3b23-3890-a717-113202859284 | -9.58167 | -40.35376 | 2025-09-30 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0fb06099-141c-3479-8854-5f8805273a0c | -11.35023 | -45.06243 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a99fa9bc-13f1-3dd0-badc-bb7519bd5453 | -11.30453 | -53.95666 | 2025-09-30 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7ce6f8b-04e9-3385-8ecb-2f6085733153 | -13.38512 | -48.06945 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e1bc020-4ff3-3b5e-b2a4-d6350ac0135f | -6.99913 | -46.20916 | 2025-09-30 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52c7e23b-b899-3ab4-b3ed-6a8a81ab05c2 | -11.88982 | -48.05259 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 33b09e6e-902d-3dd2-bf73-d40882ee75d1 | -7.90973 | -44.61765 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69127ca1-40ee-3145-a697-2a6aa14fa9b4 | -13.85302 | -47.96141 | 2025-09-30 04:40:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9db1f4c3-5ed5-3715-9bce-d64facf3981d | -7.04473 | -46.40963 | 2025-09-30 04:40:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcf7c1eb-8f99-3036-8e60-77f894cbf889 | -13.8118 | -47.48804 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc03cd5a-abb9-36a0-9b39-6551033487c3 | -10.0158 | -56.19936 | 2025-09-30 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cbe01af-e81f-3b96-adee-e3ebf4483717 | -8.24428 | -45.51348 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 85dd1a09-fe6f-3204-808c-ff22f9eb3165 | -13.80296 | -47.9763 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 692c74a3-15ce-3461-9fdc-202c201708bc | -8.7138 | -47.98316 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b788a22-7cd4-3297-be1c-0aedf3da3ffe | -11.94471 | -43.91642 | 2025-09-30 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53ba0625-b343-3c67-bc99-35554cde5721 | -10.40673 | -48.17053 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0c3116c-5403-3707-84f3-9f500bbef261 | -13.81309 | -47.48636 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ed229e2-cc80-3e16-a442-b357cb1b27f0 | -11.91044 | -48.06272 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df5047b3-951e-3154-8f0e-10cd9e659f21 | -13.40909 | -47.54032 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ca6a598-72fc-3037-8825-b64ea3a47f10 | -11.14919 | -54.11768 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2ae23d4-4f4f-3e14-8a0a-6ad720f7f2e6 | -10.10047 | -54.18575 | 2025-09-30 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb692d0c-9e11-3552-99fc-41c96bf46bbc | -7.01401 | -45.20898 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6525b02c-02da-31d8-b9a4-972b2cbc9583 | -7.7039 | -46.82632 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ce2adc0-de5a-33be-a2e1-334ec7a256ae | -7.2114 | -45.47738 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df330200-8db9-371a-bc5c-4791a86d44d4 | -13.72124 | -48.64119 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62950077-314b-3a0f-b46d-05ace3b49ceb | -6.80017 | -47.07768 | 2025-09-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2696a15e-d42c-3089-a0fb-48eca9198157 | -11.75023 | -44.74728 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7d0e9582-661c-3345-b1ca-f2bf24fb5a74 | -10.06432 | -48.18734 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d500ca48-93ea-3afe-8b68-2611714d2bab | -9.55714 | -54.63442 | 2025-09-30 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78d7e749-5661-34d4-8bcc-2c4a4b2a2c4b | -13.57031 | -48.06094 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90c6da0d-97a0-3c2d-a146-1ea116701a0b | -9.44706 | -45.49208 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4a46ad3-90d6-3b01-b013-d794ad46b829 | -7.56826 | -42.40016 | 2025-09-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a695adf7-e304-3cad-aed9-8b3207e25f75 | -8.87044 | -46.66207 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96ad1aeb-a595-3bf5-9b82-5ca7b73c814e | -11.46018 | -44.9823 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03c540d4-9df7-32aa-b1d3-b41f59d975aa | -12.84261 | -47.00101 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75c39d7f-2548-3943-bf8b-2e7523871bb5 | -11.89516 | -48.04391 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e59f3b45-d5cf-3f49-b3a5-774f8262121b | -7.05565 | -45.19491 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6500c8bd-d542-39ae-b6ea-e26909665311 | -11.44622 | -43.50986 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89fa1295-2acf-31c6-a30a-d8bca0d38df7 | -11.84422 | -46.62134 | 2025-09-30 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cc3f4e7-8956-3168-a2f3-e188cb54826f | -10.80393 | -45.35499 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1933004-c94a-3a22-a472-9914483df0b8 | -11.22614 | -47.20225 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6229cf5-acbc-3353-a0cd-ddd04ce51ed3 | -7.50299 | -45.44824 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6509b317-d596-35ab-8b97-066fbb85ac2e | -7.82786 | -46.98845 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c66cdd44-049d-350b-ab50-b2679f118450 | -10.99629 | -57.05003 | 2025-09-30 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7b13f09-2188-3820-b339-73316f2b57ac | -10.06318 | -48.19495 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45741b01-1502-3d02-9d24-9d7732d2fb96 | -13.72415 | -48.6457 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6752b0cb-fa5e-3301-adaf-543e54a9e8e6 | -12.83233 | -46.88114 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28937245-1682-3336-886b-00815391c2e2 | -7.6624 | -47.41984 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e787dddb-e3a0-3a5a-bfde-456ff103359c | -12.80073 | -46.88422 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76fadb58-61f0-3d6e-a7af-9d90746d6a64 | -9.41952 | -54.70882 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80bd9bfe-28e9-391d-bbee-ec2ef8a6b662 | -12.01875 | -46.61679 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef45d5e4-e75a-3141-8ab8-93fef80cc909 | -8.94372 | -51.69456 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8b1f798-463d-36de-b5c8-0a4c53a2bfd3 | -12.77773 | -46.85579 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4619ba24-a08b-3d73-a9a6-d515f501a0dd | -13.72884 | -48.68663 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91487c53-aa1e-386c-9ae5-e29e3440ed64 | -7.52141 | -46.69277 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5869925c-864b-33b8-91a4-359d42b07861 | -11.89066 | -49.90702 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e93e08dc-384b-3697-b9cc-839d147c185d | -6.9485 | -46.40087 | 2025-09-30 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31833667-81e7-3a44-b88c-53c47dca27ec | -7.8667 | -47.25875 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8faca7b7-3eab-3887-b25c-ec27fe6c3a9b | -13.75438 | -47.91837 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d34f4b29-850d-3e85-9e47-4fcb2f8922e0 | -8.73062 | -47.31804 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5290328f-0df5-36f2-9ab0-887b642b3c99 | -7.82372 | -46.992 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51bd4b1-671d-3e7a-9d35-ee9e327b1984 | -12.87123 | -46.90657 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| df68cbc7-716c-371d-8aa1-0ce6c1bfd467 | -11.45452 | -45.05699 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6a2b16bc-1856-37fe-9d38-eb0b8b5ebea5 | -14.01214 | -49.63276 | 2025-09-30 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8e93343-d0e9-38f0-862c-922bb39adbb1 | -9.77758 | -46.22127 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05e67a64-857e-3058-8a6b-b27e31b0e61e | -9.51149 | -54.65881 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 243ec3b6-62e0-3426-94e3-8db42b4893db | -11.88338 | -48.04749 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 57a5c4c4-0534-30e0-8b5d-c4c015e57a8f | -13.36 | -47.80961 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dad3648c-f2b5-3cec-b946-57224f43983d | -10.66276 | -48.54559 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 38d4aa8f-66c2-3bd6-941a-bb275dd29b1c | -13.38571 | -48.0654 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04613dfb-8bb8-3fa4-8579-e9d7b61b2d2a | -11.88809 | -48.03997 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c08a2968-1349-395a-ab7b-ddbb12fca52e | -13.66576 | -44.30627 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dd408fdc-e772-34ac-9e6a-96736b75d299 | -8.0204 | -47.05663 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68cbf161-5d04-3cfd-8819-ae3d28c4ac01 | -9.51015 | -47.69922 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4582f24-9946-3de3-9db3-fe34350c8976 | -8.84984 | -46.64989 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c94033a3-2cbf-330d-bd31-315c7592a7bb | -8.87599 | -46.64948 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 437027c1-1a9a-339d-b922-3592249976c2 | -12.77324 | -46.86031 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20071287-f1bd-341c-9938-035b7687b204 | -13.76891 | -48.31427 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3934bb34-4ae9-3ef6-98ff-5f9bdc55929f | -9.13879 | -47.64526 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7266af0f-682e-31f0-8192-65394836f201 | -10.19296 | -44.90289 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| dccd85ea-89c8-3a36-9d65-47b33b3a28e6 | -11.43634 | -43.50615 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83101120-e121-3641-a19a-4df01ded3ee7 | -8.64801 | -50.19907 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bda409b9-5ada-3fe1-9ee9-99ca0c7a6885 | -11.43295 | -55.04187 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99412fa2-e12a-3d11-8285-69425cc82f5d | -12.76054 | -46.86826 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ffe1a5c9-0654-3ecb-ae1c-d96f428cde4a | -12.15823 | -47.77245 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70518da7-62d8-3856-a3cf-924965e885a7 | -12.87437 | -44.63056 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1447eda6-0939-376d-925a-6e87535f5536 | -13.62586 | -48.03147 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f07731e-078b-3e47-92b9-8ec9cb0a19f5 | -13.82312 | -47.46917 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1160725-53d2-3ad8-8eed-972812872104 | -10.38313 | -48.16291 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53691fe2-4706-3253-8ce3-caacf3a883ac | -8.64906 | -43.98271 | 2025-09-30 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6634d487-d5c8-30e3-96ef-6b83bfc3daf4 | -13.38869 | -48.07 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b37ab1ef-da3c-337b-8ec3-5c5130436140 | -12.76777 | -46.84414 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 791ef1bd-ccb4-338b-87ac-95988969e667 | -7.01964 | -45.22473 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 757ee006-8e32-3402-bad3-87e8b34377e3 | -10.08831 | -50.21287 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31760081-24d1-3740-998a-d66d890db6fe | -10.19867 | -44.892 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 689cc259-0405-3db7-bb80-94aa83e15db2 | -13.75491 | -47.92498 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2eaedbf2-17de-3b07-b969-e692ef0ebeb8 | -10.62519 | -48.53674 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7de549f-d7a9-3272-8895-6e5c61168482 | -14.7294 | -45.23422 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README68.md)
