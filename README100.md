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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02defb26-ac8c-35f6-9e42-0593f7515a21 | -8.89609 | -49.94199 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e5c931bc-c46d-34cc-8383-41f8a0f529d1 | -11.53947 | -50.40459 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fd942278-6f26-3ab7-9eaa-8cfa7f946e4b | -10.8602 | -48.15787 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d14d37b-ac99-375f-a905-72efaa251c35 | -10.40337 | -50.02557 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 446a4028-6294-318e-a830-09148a298232 | -10.44177 | -50.61253 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d633d75e-eaa4-3450-aa94-e2cac8466991 | -11.5393 | -50.59185 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4f0b7d3d-6b5c-3c96-9e69-7a1100d8f7ef | -8.04765 | -52.32293 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14acd591-4341-3447-9821-e8dfa22b0945 | -9.80985 | -47.81508 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eecb88e5-2488-3ed9-86be-d060d7aa432b | -12.98981 | -47.99895 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0fdb70ab-275a-33f7-85e6-baf51451d981 | -9.87311 | -62.14627 | 2025-09-12 05:18:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e7b0990-1857-38a1-a76a-8b6766dfdaf0 | -11.98019 | -51.17443 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41a81a4e-139c-3507-bd4f-0abe5fd21d80 | -7.41933 | -50.65646 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cf7374a3-27b3-3f43-893b-3c258cfc54bb | -10.42193 | -50.59515 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0edb3561-e48e-3cd6-a954-9ee0128efd85 | -11.18567 | -48.62308 | 2025-09-12 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00255541-04fb-3511-b53b-92b7a5524751 | -10.48732 | -49.3714 | 2025-09-12 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28cdfd80-6389-3510-8d2a-94e4c41487f4 | -12.25144 | -46.75505 | 2025-09-12 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a246ce73-0491-30b0-a203-468258aa2cea | -11.91941 | -50.69172 | 2025-09-12 05:18:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cedf19de-174b-3c16-8201-5985caf255d0 | -11.1999 | -55.07584 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f137f753-8b9c-361e-886f-ee0b219706f5 | -11.18531 | -55.09191 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 148dcf42-96b6-39d5-bc3e-dec7d15c9c5b | -11.23128 | -54.99939 | 2025-09-12 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b78a50-d82f-3dfe-82a1-4a992dd3d564 | -9.08076 | -47.00082 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3909372e-81af-367c-88d7-75838dfb2c85 | -8.63278 | -53.1037 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e49a6d7e-24d1-345c-b829-0caeaedb0ef1 | -7.45546 | -51.80576 | 2025-09-12 05:18:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b8e175f-6641-35e2-9c73-6aeb44150355 | -10.54056 | -51.53252 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 230bf221-54dd-3192-bd1a-a29af08c787e | -9.04293 | -47.05553 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7d2e1b35-67d9-3dc3-9522-d94c2cd2aa37 | -11.93071 | -50.69861 | 2025-09-12 05:18:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f592461-c529-3019-9fa5-e0590c1fcbd1 | -8.89748 | -49.9309 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c9da9c90-8d0a-3fa0-8fb3-50bcab495c34 | -9.04074 | -47.11018 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 670e51be-c200-328c-9b42-e41991066fee | -9.79873 | -59.10136 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 000dbf03-82a7-3d1b-bcff-de7cda8356b8 | -8.85853 | -64.23343 | 2025-09-12 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0311eff3-48f9-3275-88f8-54a1d215ef6f | -9.34779 | -65.4558 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7b446a4-8e0e-3103-881a-a98772411291 | -8.04639 | -52.32389 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8fd37e0f-907b-3ae1-b22a-833a3fc16e78 | -11.94753 | -51.17673 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7ae0493f-8f57-3485-a2b0-fbc5433386f6 | -8.08646 | -54.73954 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8cf9366-3439-368d-a799-854a0975c29e | -11.18581 | -55.08836 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e702f8e9-91d5-3db7-b6e7-35a4dc7c2ebe | -10.7114 | -48.63209 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 754b9df1-e893-38d0-85c7-e3d8a884ac46 | -11.53992 | -50.40085 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 65dbe1b4-42c2-3301-b478-e909eb801717 | -10.35009 | -50.53423 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9438f05-f30e-37e2-918b-ba69787814ab | -10.56313 | -52.02325 | 2025-09-12 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa045cbd-d0b3-3d89-a67d-5da9eb0785c3 | -8.04235 | -52.32692 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0e439ab-98d0-3133-8620-f7add7d2fd5b | -9.97999 | -57.80947 | 2025-09-12 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 69498604-cbdf-3b0a-b59b-550742ec0d8f | -9.72775 | -64.94912 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d36741b8-9341-33aa-968b-def8d27fd320 | -10.56135 | -51.49105 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8efbe8a0-f297-30d1-a794-ae44dd6b4721 | -9.51979 | -54.63647 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0675ac44-a426-3a63-9c80-ff449886018c | -9.59663 | -54.99856 | 2025-09-12 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 788a39c8-134f-355f-9ebd-499d7ebdb3c9 | -9.07891 | -58.96298 | 2025-09-12 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8a000b1-3d4e-315b-8f0e-e37eac1f8034 | -9.66876 | -47.55226 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a80bb21e-037c-3ba4-9f34-d8803d3519c2 | -9.78649 | -47.84813 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1083779-7c98-31cb-8fc1-17983d1d9544 | -11.20344 | -55.07993 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e650999-17c0-3566-8210-f09f1d066404 | -11.15518 | -57.19302 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c111e4b0-a670-3bde-9f2f-6205fa9d64b4 | -10.44223 | -50.60886 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47abd81f-df0d-3c87-81da-90d6ee7cf1ed | -7.4793 | -61.58886 | 2025-09-12 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8793f6c-c41a-36d7-a744-5f80af339dfe | -11.97814 | -51.1466 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebaad42d-55c7-3d63-94d1-2f32b40c4832 | -9.72014 | -46.88749 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b76eee01-b792-3b43-8537-2fe7a0b2de3d | -12.93011 | -48.00887 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6cb1926-dbb0-356a-951c-ae106561ae53 | -10.52107 | -51.52292 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9f6587f-d015-333c-a3ab-2a658c95e2f7 | -10.65823 | -48.65924 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72f6df7f-cc87-310b-895d-0d2e0d9e8fd0 | -12.27561 | -53.91452 | 2025-09-12 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 912b12f4-e731-3525-bcdd-bb60840c2fbc | -11.107 | -51.9767 | 2025-09-12 05:18:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 56a0556c-ffe1-33c6-ab43-ff9aa17108f3 | -12.93326 | -47.98021 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1f0a3b2d-4f73-3aa0-9ec0-458e45d66270 | -7.44854 | -51.82041 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 635d1bdb-2f1e-3add-99d5-f4a68555d52d | -9.70271 | -64.92657 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63083344-53f1-375b-9652-5692bc6f201b | -11.1893 | -55.06329 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d2ca2c1-73db-3749-81e7-e52cd2e42e4e | -9.03412 | -47.10922 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 094ae5ed-f265-3129-bac8-390080eb570a | -10.66652 | -48.64161 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ceedfe25-0eb8-370f-86e6-0edc530d12f5 | -7.81031 | -56.66982 | 2025-09-12 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1681fa73-1203-32c2-a4c2-f02f83a93f34 | -10.68339 | -48.65727 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f55231dd-ff3d-3bc3-b2ca-1676240bd67a | -7.488 | -61.40392 | 2025-09-12 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69e4348a-049d-399b-85f9-7491659d9c8d | -12.93773 | -48.00019 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dae65f1b-396a-3ca7-b881-9d746f002337 | -11.95371 | -51.18015 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9357049f-dd2e-32cb-8fdb-05ed75c7ab4f | -11.49072 | -49.27168 | 2025-09-12 05:18:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89ccd7a8-90b9-3320-a5c3-c1cb08bdd7e4 | -9.03815 | -47.07501 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 630e355d-b466-304a-bd60-e03df3dd73ec | -7.57583 | -61.16239 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 733c300d-1de6-3de6-9726-72ed328eb6d5 | -8.34865 | -47.58838 | 2025-09-12 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4344550-e206-3f09-afa5-622622b2e365 | -11.48426 | -49.27501 | 2025-09-12 05:18:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97bdd104-2040-3e65-9494-cce6bd6380b1 | -8.88561 | -49.93824 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e94242b7-9ee5-319a-83a7-e2757729ff94 | -8.87496 | -49.53578 | 2025-09-12 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a481bc61-4846-3945-a9cc-2e06522a1d6e | -12.56664 | -49.14119 | 2025-09-12 05:18:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34eba7a6-bb28-37b9-ae81-3a7f319e520b | -8.95791 | -46.7221 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| ca36b4d2-f6c6-3a3c-901f-4e8a62091eb0 | -11.18829 | -55.07056 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c73bcfd8-2424-3fbe-9d51-e321ed27870d | -11.1863 | -55.08483 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d429434-bf83-39ad-9d99-de7d83b9c0ea | -10.745 | -48.18398 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 647ae505-040b-3db1-99ed-b6f17ed9f54b | -9.99645 | -51.71644 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0bb68d59-a558-3a26-875b-44a2d255d048 | -10.4049 | -60.81469 | 2025-09-12 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed9233cf-672a-3f31-93b0-3f07dd5e6f08 | -10.68217 | -48.66714 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e1d2c9a-7fc5-3f28-9cd8-2c501f0aaadd | -10.14056 | -47.90654 | 2025-09-12 05:18:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf9bb719-d55c-3c4b-b7b0-bfb4153711d4 | -9.67662 | -47.54178 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 747b0887-99a7-3e6e-9f4a-ea431d5389d5 | -8.89702 | -49.93463 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 58f9de0c-15d4-3f13-a2e2-34f7c8967612 | -8.43548 | -47.25612 | 2025-09-12 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2b7b1ca5-0390-37ec-b453-e6b2399ee9b1 | -10.35727 | -50.5209 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2bcd3558-df49-3b27-9e82-f8a09805e336 | -12.50303 | -47.43353 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34e9de31-0d93-3078-86c8-2607fa00aac2 | -7.72054 | -51.08109 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d67b21d5-9045-3d60-855e-f1e7edce7c08 | -9.42178 | -58.98809 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1bc4523a-e84e-3e72-94a4-11d771422d06 | -11.10824 | -50.71549 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d68d9bf5-cd3a-376c-a1bf-18beba631bea | -9.71947 | -46.8932 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13520570-5604-3103-bc58-38ed1a66857f | -9.72619 | -64.93418 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 641ab6c4-04b3-3c08-9019-56c48a76fb3e | -10.14503 | -46.30818 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dea371e3-269b-3b2e-b1b1-deba92d83029 | -11.09402 | -48.4063 | 2025-09-12 05:18:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f24cf15f-fc5e-3bb5-bba8-afc174515727 | -11.96426 | -51.17219 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 38b77d8b-310f-3d29-bdf5-b6bd4e8699de | -8.05106 | -52.32432 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README101.md)
