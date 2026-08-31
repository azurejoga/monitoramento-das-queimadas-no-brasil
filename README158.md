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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffb03798-30d4-35bf-9e59-30896b4bad1c | -10.7331 | -44.88121 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b3a67dfe-5a04-3043-8916-d7e073fe27d3 | -12.10062 | -47.15314 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 295dc68c-2c54-3606-80d1-04892126d73a | -9.59332 | -47.6004 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6a3607b2-c136-31dd-a37e-8ef66eee449c | -11.16518 | -45.04458 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1c5dccf2-54af-31d0-8c61-dacec3de75c0 | -11.18903 | -55.0945 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ce24416f-9cd7-331d-9c8e-cb963c6e5f1f | -11.21164 | -45.10465 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d9b9f49e-44a6-3708-9892-81b3c8bd9194 | -11.19017 | -45.04031 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 95fb8db2-4476-33f6-9ad8-a52fcf726ae9 | -7.5655 | -61.36867 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fc963461-c61c-3e6a-acb0-b728be9d6586 | -6.98019 | -45.39525 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c330f1f7-3141-33b2-acca-9bc615329a6f | -7.93391 | -61.34875 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b2926ad1-c7c8-3265-94a8-cc7a8704b06f | -11.09267 | -51.53556 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 42ff818d-fea7-3f7d-b90c-09e8d2c8a5c5 | -8.17815 | -54.9367 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| d75ee47f-e61d-3cd5-985c-e9a3786d6a66 | -8.9416 | -62.36982 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c596976a-0064-3d54-9dde-37a7540b01d3 | -7.55535 | -60.46173 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 472f1f54-c4ab-3620-b282-5dc9047b73b0 | -7.92318 | -61.33679 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 503f9b0c-4dd4-3141-b171-bda4efef327c | -12.08408 | -44.98856 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 2290db78-af36-32cd-a2ca-0d311c6e9fa8 | -12.957 | -45.9286 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f7bab7db-1a30-3075-ac1b-f2755ce93f42 | -9.2174 | -59.39685 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f6fab856-76f8-3f21-92fc-0601aa8b7302 | -9.89296 | -60.27341 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b235c05d-b542-360b-ab17-b99ac5f67e4b | -8.03696 | -36.13617 | 2026-08-31 16:50:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fbdb14c3-f2e2-3959-a3fb-395016d49e2f | -11.93998 | -45.06211 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d7c8832a-f269-3890-b0a1-f6164a1b27e3 | -10.11788 | -50.32382 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a03d11c3-e21a-30aa-b266-9c449676e59c | -7.58239 | -61.34308 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4adad5b4-ab1b-3f1e-a728-eb5ef045a8d5 | -7.41948 | -44.25233 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f50e7e78-e4c2-3b8e-9d05-427e48c11a96 | -11.67615 | -47.61377 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 46dd2919-71a6-3519-9ac9-cb17bf372b5c | -8.72718 | -45.37926 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6ce0da6d-42c4-36ab-802f-bdd2221e26cc | -6.9166 | -55.70485 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f670184b-4e19-31f7-b36f-3a007aa3ee69 | -7.59798 | -46.19235 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e495852e-fab5-350d-b1a9-c814c3c6ef6b | -10.11225 | -50.30922 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| eed7193b-3de2-3e25-a4b4-5950cc305b19 | -14.12229 | -52.80676 | 2026-08-31 16:50:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8f0cd90a-3a86-39cb-a8ab-384972b3d96a | -8.90161 | -57.25979 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| db9cf0eb-cf56-323e-834e-d03318b2725e | -8.93974 | -50.18177 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d64eb493-3875-39ce-9261-5840b0e76ef1 | -9.15308 | -59.53474 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| ad035ce8-041b-325e-8e3e-05d5bea92202 | -5.77272 | -44.11957 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bd7c36d4-5a5a-360d-bcec-391d23cb520c | -10.7992 | -50.72201 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dbace42f-cfdc-30f7-a341-3e2762cc9001 | -8.75622 | -46.47028 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c5cabe27-fa7b-355c-a24d-c1e653170d62 | -11.23522 | -45.09219 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d0453ada-b984-3ca1-af95-f0efd5c7ed55 | -7.97756 | -46.53256 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a9f47b8c-04e5-3f1a-90c8-bde958beaee8 | -8.87581 | -46.03146 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 471020b0-51a0-3285-a01b-584d0c689fd6 | -10.7566 | -54.0709 | 2026-08-31 16:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 15868b81-bfd0-3b3e-950e-9fd3a9aaa5a8 | -6.68114 | -52.85204 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4adae322-95ce-3276-9b73-446aa57ddb67 | -9.20575 | -51.56258 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3618647c-1c83-37f1-b1ad-050c8d40dd8a | -11.32699 | -45.19103 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 48eb2877-f9ca-390f-aa6b-f91ab9fdb3f2 | -6.96172 | -55.6988 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 153c610a-fc3b-36f8-9850-001911a1db28 | -9.96401 | -46.77492 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 363b4a2b-17e4-3c48-98a9-39aeb6830f99 | -8.0489 | -47.27567 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c04cd1ec-8f8b-31fb-8dc8-06a1aeb7ae4c | -11.17104 | -45.59261 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6c8f2e10-4eef-3270-b2d5-51e75cdc4e8d | -12.11202 | -45.02889 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e64df619-35e6-3253-b2f3-6737dfb78453 | -8.44197 | -46.90127 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b6e9b91-92ca-32f5-a38b-dc0b9483f324 | -7.92653 | -61.34384 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 67691ea0-a029-3d16-ba04-34d9d6d03e2b | -12.10154 | -45.00656 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 72fd4e01-dabe-35b8-bbe5-36d8127cf4ec | -5.58245 | -42.32788 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7494f089-38af-35b3-a789-2c1480b502df | -11.79077 | -47.67449 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 8885ea29-9d18-31e6-af53-09e6c8253b93 | -7.35648 | -55.19241 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d9fd970e-db82-39c6-99aa-a297c275fa7c | -8.88631 | -46.02974 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8f56ce4-31ed-3dfb-bbe0-cb11c99d9b63 | -10.99335 | -48.3866 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f8484384-34bc-3670-853a-3937464b0d9b | -10.80213 | -50.71753 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2d8eee91-c3eb-3193-a7e1-d45044987398 | -8.80169 | -62.50023 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 310e37b8-39bf-3ca7-b007-2945d4e31480 | -9.41177 | -51.67896 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 668e4d9a-b4f3-369e-9636-ea9e38b52d4b | -7.93051 | -61.34164 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 140d5f75-4476-39f5-95df-d21b40fd1c80 | -6.93412 | -55.6337 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| b7fb9966-757a-352d-bd5d-c6979feac814 | -11.25411 | -45.11875 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a960a882-eeab-3c4b-8cad-0c8d7f86411d | -10.45214 | -46.75476 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f4acca79-3be7-3002-9b86-f9cba1040a1c | -10.08302 | -46.62015 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3895782a-cf68-35a9-a306-caab629c55d7 | -6.78633 | -55.67459 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ee3fa4af-1577-3511-a8cd-51726cf691e5 | -8.36858 | -57.67247 | 2026-08-31 16:50:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1bf6c6fa-652b-3d5f-919e-cbf80845f2bf | -9.59387 | -47.60392 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f14408a2-4111-3050-bd7f-5981d558890b | -8.42674 | -44.98704 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 60b1c3d8-fa1c-3e40-8ce4-b2fde88d7d58 | -12.10069 | -45.06882 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0f159c4a-469a-3294-aa0a-5835c405ff66 | -12.17183 | -50.52925 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 45916eee-5e60-3e79-a9f3-d27bbf69b58a | -13.41843 | -51.38302 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89de008d-b965-36cc-b3d7-68b6b557d223 | -8.32756 | -47.58034 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81705bea-0993-33be-8103-70dda8eebf00 | -13.85122 | -54.08773 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4659388c-f4eb-3034-b126-d2e39604c08f | -8.79786 | -62.50237 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| aee9137d-7f45-36a3-b7c1-512ce2351a3a | -11.1704 | -45.58865 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 841c739c-c673-3e42-b528-d1c543be2d84 | -7.09686 | -45.79452 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ab8b0a6f-a6d5-3671-bae6-412fb5aa9864 | -9.83948 | -47.8304 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a76442ed-64fb-39df-af58-bcaf5fb25902 | -10.02153 | -45.56292 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cc741596-4899-3679-966b-29a3d3179fac | -7.34688 | -55.15493 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 5b79c3f1-b84d-3564-95e4-35b5c6812804 | -11.92561 | -45.0852 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1efe09f0-0bb0-3471-ad35-677bb2c8d351 | -6.81884 | -43.53197 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 67901bef-0ad4-333c-a73d-765542154946 | -10.00264 | -46.41985 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a2f11a33-c2ec-3903-9072-ecc26ce8d424 | -11.64606 | -46.74459 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 32278afb-418c-3c1a-8d6b-7ca6f6f299ec | -11.24316 | -45.1414 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 464bf0cc-f256-37e0-88f7-d26198424b3f | -9.68532 | -46.54022 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 51fb89b1-a44e-3f6c-b22f-1f468a3fe5ac | -12.1847 | -45.02899 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 09058738-5751-3931-8608-c9b51b092cf9 | -8.13775 | -45.58174 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7562db4d-c26f-3a6f-a174-13062f9821e1 | -10.16462 | -45.72901 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2b1ff8f1-154f-3925-aacd-92c8bd974174 | -13.97424 | -54.41086 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9a6bc976-3184-3b6c-9c02-0fb36756a59c | -12.10178 | -41.53936 | 2026-08-31 16:50:00 | NOAA-20 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 07a46fb0-a431-32cb-b6d2-e33bb32deaf5 | -10.0674 | -59.40828 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fb9eb6e8-c803-3102-b235-293301e5eb4b | -11.0719 | -51.52085 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| a6fd22fb-06e9-30cc-9391-974e19311afa | -9.32438 | -48.25494 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f20e27e0-5d30-38ad-aad9-871a5b79cb94 | -13.30433 | -51.5935 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d9aa0591-3ce8-303b-b5e1-96d74f538285 | -9.48088 | -57.02453 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a0a2c25f-7f44-3ff0-8796-d1c5a1afc16c | -7.36658 | -45.07701 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 25f9fa55-4849-3631-acce-95814624a75c | -6.94372 | -55.63687 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 349afde6-697c-3bd5-86c0-24ba0d392c7b | -11.69371 | -47.63974 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1adbd880-8456-37c4-9900-9b726322a011 | -10.08245 | -46.61647 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0550dac6-7166-323d-bf80-6b2e23295709 | -13.97486 | -54.41573 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README159.md)
