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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5daaf3b1-d12f-345b-85a2-099449800a37 | -14.86297 | -48.13412 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dba06b1d-6b1b-3f53-a8e9-0d224be80184 | -8.54378 | -54.71151 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19d992eb-d219-3bd5-b2f2-1089ddecd2cf | -8.40832 | -54.72564 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb55c6da-73c6-3b8e-8365-2ce17b2c4e5b | -8.56379 | -50.15496 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2b38d6b-9b0b-316a-8e21-8bf6209d5d62 | -8.81865 | -45.89132 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b15746e1-927f-3164-863d-5405fc6056e8 | -12.12714 | -57.18385 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3371c124-34bb-386a-b0b1-b5da18be7efb | -13.06987 | -48.60204 | 2026-09-15 04:34:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f139825-7ce6-34da-b9c9-998984201dfd | -9.25364 | -48.54382 | 2026-09-15 04:34:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22757f7a-e601-3b2a-8559-eaf64355685b | -10.43749 | -48.64031 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d1dbd51-27b6-33a2-af88-614e22e0726c | -13.39048 | -57.04077 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1acfaa24-279d-3611-b876-9da562307bc3 | -8.48462 | -44.58032 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44c28b1f-9f8e-3c1e-8436-44dc6f453a05 | -8.81208 | -50.48964 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 320fb9ef-b673-3db9-b8bc-6b3836d90063 | -13.55397 | -43.52528 | 2026-09-15 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5117a2b-087f-3d0c-a23b-b8f219530384 | -8.81921 | -45.88775 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7d93d79-4e2d-391a-a1b7-a8ae0c879cf7 | -9.17187 | -49.99985 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 655de8ed-663c-39e9-8d8c-84313759d4cc | -6.66302 | -54.98514 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8198086-7df0-3d98-b371-de1568d675a5 | -13.57151 | -51.44747 | 2026-09-15 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c69d492c-908a-3cdd-8096-f301bab7cce8 | -13.30222 | -51.28902 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31bab8a4-b66b-311c-853c-313aaf8b7026 | -9.45399 | -40.38984 | 2026-09-15 04:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 033e0ac3-fb61-33dc-ab26-5a6a2ab04c7d | -8.60944 | -44.46422 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c812b35-3455-3293-81b2-b41f1883209c | -11.34152 | -47.31752 | 2026-09-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96b2f14e-be43-3802-9746-a362a30d3e49 | -6.87956 | -59.64425 | 2026-09-15 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4670701f-8857-3473-8645-62562db11d4a | -15.20502 | -47.94456 | 2026-09-15 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a41fb911-fa6c-30a5-a93f-c61fcfcea7e2 | -10.67739 | -54.17738 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6b224a9-c4f3-3c0a-b71b-25bdddb51e88 | -11.244 | -43.44342 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84e07a99-dab7-3803-a4d3-6d9ba8ca32a6 | -8.5434 | -54.70828 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a5a4a67-0f59-320e-a16c-bc60982a573b | -9.45495 | -48.55818 | 2026-09-15 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb9f5cf4-60a2-3317-8283-cf8839bbd257 | -11.81742 | -46.59418 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36734834-6967-3b0c-bdbf-544b7a169698 | -8.9782 | -49.68069 | 2026-09-15 04:34:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c94ebd6-6740-346c-8072-4bf4a2f29d7a | -8.84991 | -45.90273 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cba3191b-126c-3e28-af31-17b635c02e3d | -13.61969 | -42.44599 | 2026-09-15 04:34:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c40ea96b-3ca8-34c5-b3eb-2464e19c7c04 | -13.26835 | -51.28487 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c511e518-3172-3769-ab93-5b69b55c7e90 | -14.86231 | -49.95359 | 2026-09-15 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05bf0ca-53ce-310c-8f4a-0c8136722d48 | -8.8275 | -45.87009 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e86edd9b-6547-3a3b-be76-658952583e07 | -8.11698 | -54.80796 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a251ba2b-a475-324f-82f6-e854c7f17bb7 | -8.536 | -54.69926 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1087fc2d-953b-3bde-aff5-d38c0cf56b1f | -9.41519 | -47.85316 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e749b0de-c8b6-30a6-ab1c-4081dd522aa8 | -15.04988 | -48.58492 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 698fb689-8bb9-3272-8603-e5f61e3e4d81 | -14.96032 | -47.53229 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3086d67-d1d4-32c4-a4de-ad43f6a11f0c | -13.51688 | -44.17085 | 2026-09-15 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34661ecd-f377-3c91-acd3-c5aaac67a79b | -10.29784 | -54.16757 | 2026-09-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c42c94f7-f84e-3ca9-a669-fa9855470f9f | -8.82695 | -45.87364 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c0c51b6-1825-3852-8275-4040220df180 | -9.25422 | -48.5402 | 2026-09-15 04:34:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81d7fc2c-d68c-31d7-8df3-1f64c4cb081d | -13.38595 | -57.03653 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3d69ab3-f07b-3ac4-8b10-9f8c97bc643a | -14.85965 | -48.13358 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43aad16b-585c-3fab-bfd3-2aa59ca63074 | -13.61781 | -48.27812 | 2026-09-15 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f8bb5de-3aff-3fb8-82d0-b61832317d2b | -7.86768 | -54.72374 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 196463cf-4d2e-37ba-8ccd-3c8b9d735e6f | -12.48648 | -41.41546 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9669885-f99b-3fd0-a681-6ee18c2438cd | -15.20114 | -47.9476 | 2026-09-15 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e09bb173-7264-33de-8db7-4de25398c7cb | -10.88481 | -51.55598 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c504096-8f14-3f03-b1ee-3262dc4d4894 | -10.58106 | -47.74399 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ce15bb33-c3bd-3589-a060-9c68e1b8f172 | -8.79186 | -45.90907 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d2ef69e7-1a0f-3cf6-b231-174ac40eeb99 | -14.99934 | -48.51779 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ff25631-68a7-34ad-8b9c-7fb47b8da0cf | -8.50172 | -50.14869 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15889aae-e2bb-336b-8ba2-b5b04970ff0e | -11.33193 | -47.67916 | 2026-09-15 04:34:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3b23f6e-fca2-3f58-b852-996e015356b1 | -10.80188 | -46.20708 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90087e96-71b7-3ff1-9f78-cfa4a97c7964 | -9.35626 | -50.17578 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f2a9946-7158-3f11-b818-4dc9fa8ecd13 | -9.76237 | -46.10746 | 2026-09-15 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d954f3f3-557f-3770-87d4-686ad8a0bd72 | -10.94228 | -54.08829 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0977924e-e42e-3b03-b8ba-15efc1a3382b | -9.47788 | -45.46186 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab644749-9e47-3597-845b-7d64613b3def | -8.79297 | -45.90198 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ccc4d0f1-4d24-3493-badf-21851157192a | -10.575 | -47.73941 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4eeb83d7-bde8-36b7-b7b3-f058e5f3232f | -9.69544 | -58.17952 | 2026-09-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e974533-c43f-3f5f-81b9-b2e0c756ead9 | -8.58306 | -44.49609 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf99cd90-e97c-31e3-8f6d-7b97ef610898 | -13.59871 | -47.90452 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff449106-c941-34d5-a36e-d1926ff7c2b0 | -14.20367 | -47.4224 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 80790e8f-2978-36a5-9232-2e2b5e29419d | -10.58549 | -47.73754 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f73033a7-e3a8-38be-9197-d66cfe974026 | -8.83085 | -45.87062 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7ad886c-4498-313a-897d-abb6f134fcfb | -9.87988 | -47.7737 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 43ecfb1c-7cc6-3654-a940-11961d7d5201 | -13.62796 | -47.91313 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14c9014e-62ed-3848-bbf3-deb83a6783a5 | -11.17631 | -42.80912 | 2026-09-15 04:34:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 08ef6d08-1dbc-30f8-8531-f14197eb7cb5 | -13.27124 | -51.28978 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d16991a4-a165-3b8d-9923-7821969ad044 | -8.59713 | -44.47436 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daf904de-aa4e-3414-8d07-114006ff1d96 | -6.66355 | -54.98219 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41a58622-a206-3253-acc8-6850d9c8227a | -8.47649 | -44.86841 | 2026-09-15 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdb6c2bb-3793-3de1-ab67-19ea4826734e | -9.42065 | -50.09801 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1fb678aa-2d18-3677-97df-b6612df4731a | -13.57076 | -51.45176 | 2026-09-15 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4245ce72-16d0-3883-9bb4-416d58ec9d51 | -13.64261 | -45.98419 | 2026-09-15 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa9b00b5-ccff-3842-817c-f8ae6c022cd0 | -10.45821 | -48.6735 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61e65de0-ebbc-349f-ab00-db58f2afc69f | -15.25549 | -40.99905 | 2026-09-15 04:34:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 90c8b968-ebe1-3cfb-8693-f67432cf064f | -13.7641 | -48.80838 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 101963e5-13b3-34d5-aa9f-871101b21a4c | -13.27911 | -51.29361 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cca81455-3727-3081-9f0b-d17a847af45d | -13.56891 | -47.8996 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a8645d42-71f4-3d2e-a6f8-df3275681e4d | -11.8868 | -43.83082 | 2026-09-15 04:34:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f50fb98-ecc8-321a-8ff4-be55cbc51d7d | -10.58493 | -47.74104 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebcc35d3-af40-3b95-9be9-5a527b8076b3 | -8.59653 | -44.47826 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa3b141a-072e-3022-9bd2-3a875637c1d2 | -8.48346 | -44.58805 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9d1f7ac-a0a5-3592-a3c1-0181feae08b0 | -12.31977 | -41.78041 | 2026-09-15 04:34:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 26cb7eae-2f1d-3227-ae38-aa182bc3ac42 | -13.55166 | -42.41217 | 2026-09-15 04:34:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb2bce81-3722-3e42-bba5-7b618dce7977 | -9.42994 | -47.44267 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf8fc759-4e4c-35e1-ad02-b3321248dd0b | -13.30076 | -51.29751 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e3782d4-2e29-336e-8e3e-50820b5279bd | -13.51313 | -44.17029 | 2026-09-15 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64e721d5-7aa3-3bd2-86f4-906040e6af5c | -10.67453 | -54.1675 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36472c39-95cd-30a7-9b42-8ed1872b186e | -8.54081 | -54.70013 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 138198c6-4008-3e0a-9b0b-26ce6838248b | -8.6104 | -44.4634 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19f1aa37-dc7c-351e-83f2-f5760396c3f5 | -10.75733 | -44.8171 | 2026-09-15 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c0ceb162-efde-3fae-abaf-9b9274feda4f | -10.98049 | -48.32617 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d6a653a-671d-329d-aa69-8fdf33b02fdc | -11.81184 | -46.58588 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3ac7e2-fa49-32b9-bcd9-6b319b6da003 | -14.16596 | -47.40134 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a293d009-b481-300b-8914-bfd9d739090d | -9.35868 | -50.09589 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README46.md)
