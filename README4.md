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
| 67695831-ff91-3f43-a013-3bcae701dc1d | -7.6572 | -46.09963 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2382345c-9496-3e0c-a50a-4098182127c7 | -8.12169 | -45.89609 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd7aa4ed-9dde-3258-a83f-bc7d39de4daa | -7.59407 | -43.37874 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db01df91-3784-38c4-a1d8-cf1612ce73ef | -8.07293 | -43.13434 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5bbb0936-f529-3ad3-81e5-3f0cf9ef6cca | -7.60118 | -46.27995 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9366ce52-cb0c-3f31-99eb-75884c5b04bc | -9.37409 | -48.40947 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1df2aa4b-f937-3dfc-89c8-093871aaa2c9 | -8.02359 | -43.18377 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9cb73397-c22b-3fbc-89de-ca71d50a350c | -8.02303 | -43.1842 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 449075d0-c450-3874-848c-fdd682b8beba | -7.48003 | -43.36846 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd2847b-42cf-3246-8924-fd5f021189db | -7.64439 | -46.1158 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5f3c35d-c228-3b89-8ca2-2dfffe5bd986 | -7.4688 | -43.37415 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d6af17d-3e5d-3587-8035-9941f3e4b901 | -9.71363 | -48.61462 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33b88560-355b-3b94-8c06-762ae40f15ee | -7.64105 | -46.11527 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27816038-e8df-3f29-a050-cf8cdb2ed085 | -5.68343 | -44.12631 | 2025-05-26 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49ceab73-1773-3e43-ae62-43c8715ac521 | -7.6006 | -46.28355 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70995585-fcc5-32de-a38a-d528ea8063b8 | -6.83714 | -44.63 | 2025-05-26 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6590c9a4-eabe-31c6-8326-b55509dff959 | -7.3578 | -43.32024 | 2025-05-26 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0cc142b-2142-3b07-a6b8-1330c376859e | -8.05193 | -43.15776 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d9c66ce-52a5-3121-ae53-5547010879b4 | -7.60292 | -43.32042 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b3d7826-6fb0-3707-a5f6-c9311b27eea6 | -7.1521 | -43.311 | 2025-05-26 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fbd942c3-c6fd-37e9-a336-781defde5c69 | -8.11726 | -45.90256 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f55651fc-e4d2-3b0a-8135-c9177cb6a98f | -7.59226 | -46.27126 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70d0fa86-637d-3343-a808-b887bf2051cd | -7.35442 | -43.31972 | 2025-05-26 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11e408f6-a7c6-3291-9ee7-b87083084f40 | -8.44296 | -49.62706 | 2025-05-26 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f520764e-a493-34d5-afc0-1345ae52cbb3 | -8.44214 | -49.63193 | 2025-05-26 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1c00c034-4b3e-3730-bddf-64e0955b419b | -8.44601 | -49.63253 | 2025-05-26 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4674482-0166-3b5b-960f-bb213f81c801 | -10.65628 | -44.49406 | 2025-05-26 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7021a8e9-db0b-35a1-ab69-4469c33c5fbf | -10.49902 | -42.42435 | 2025-05-26 04:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| cd9c69e3-10ab-3f96-9a87-7731d831d1fb | -8.11395 | -45.90204 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61542fa0-124e-3b6f-9195-50b6a80d7627 | -8.03271 | -43.19271 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| f0456c72-1bd3-37b5-b595-ae78b60fc88a | -7.65942 | -46.10725 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 106eb54b-a665-3b8b-81a1-ba6d5956a3a1 | -7.16105 | -43.29751 | 2025-05-26 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4d8c6390-29b3-3a15-aa62-96da87a3c55a | -7.36008 | -43.68882 | 2025-05-26 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9690efe-b3e9-38c8-abf1-d60efcd883da | -8.01791 | -43.1948 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa4c69a8-5f85-3cc8-99dd-890cbca13689 | -8.07405 | -43.1269 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1484c61a-637b-31e9-a5e4-418576077b9d | -7.49016 | -43.37005 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50c67c14-ffe4-3b7a-a8ed-2006b1933154 | -7.59296 | -43.38603 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f31443fc-f77d-3231-a817-224484bc9a9f | -8.02137 | -43.19859 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 146dbd3e-43f4-3739-abe0-da12420ecee5 | -9.38257 | -48.41833 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a01f16a2-e62c-396c-a9de-4bccf794469c | -7.48341 | -43.36899 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 152b078e-d9aa-3de1-939b-9ad5e27f573a | -6.99029 | -46.31461 | 2025-05-26 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c97fffa-ecc8-3d93-9096-1565bb7d11f1 | -8.02076 | -43.199 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c906cbf6-1ca7-3ffa-a4e8-af1676c9e1ca | -9.73022 | -48.31733 | 2025-05-26 04:19:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9ec979d-1442-33d9-9dd8-a1d5ce092602 | -6.69305 | -42.82184 | 2025-05-26 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 605c27ff-4513-3c1f-9c14-eb69b89b522d | -8.05137 | -43.16147 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ba74d605-3d32-30bb-9a57-a8d14015f44b | -8.02189 | -43.1916 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3a410115-2f82-33e6-be6b-632e89702286 | -9.37766 | -48.41005 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0015cab2-ea18-3f88-b328-54f142263376 | -7.68297 | -46.10722 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 760c22d9-02d8-352b-a1f2-99446fab3e19 | -7.65998 | -46.10369 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2646b1b9-5414-3790-bfe2-1c1cbdd96ace | -7.56705 | -43.37455 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f38eacc-01b6-3a8e-a2eb-c180fb73bf44 | -7.91172 | -44.4768 | 2025-05-26 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7e9092e-5c3c-3bdc-9c83-6833ef7d67da | -5.79544 | -46.30408 | 2025-05-26 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4095517b-4fb2-3ae5-a497-e3201688b969 | -7.59573 | -43.36781 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 107379c0-140a-3ba6-a137-e01220ff7b3a | -7.47666 | -43.36793 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76596222-d893-31db-afd8-0282597d1f13 | -7.35284 | -43.69134 | 2025-05-26 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e47b0530-e8e2-3f7e-921d-3833407d0c02 | -7.66608 | -46.10831 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 41186034-aeda-33d1-a445-feec55f1daf8 | -7.16394 | -43.32397 | 2025-05-26 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d95e49b-8803-3a88-88b2-6ebc9bf07db5 | -7.47273 | -43.37103 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bebe8f89-c77a-353e-8cd9-b52f06149900 | -7.51941 | -43.35958 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e087f3e2-e65a-31f2-9a51-850c186bfa57 | -8.02193 | -43.19489 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| e928b694-c762-3fe5-baff-49d4c03acb2f | -10.49541 | -42.42381 | 2025-05-26 04:19:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5dfcbc27-89a7-348a-9cf6-2e98dbd17ec8 | -7.6802 | -46.10315 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 406e4f42-5dfd-3372-9a4c-7e66ea927e32 | -8.07349 | -43.13062 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c284cddb-e4d1-3e94-93ef-852db11c3a4a | -4.29088 | -48.27156 | 2025-05-26 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f84e0edc-1046-3109-8273-d6d2dbb932d3 | -8.02756 | -43.18057 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ec35207c-765d-3e72-9241-4335f8527d23 | -8.02304 | -43.18748 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| aaee588f-5daa-3980-9f67-6bde9004aee9 | -8.02132 | -43.1953 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3de29066-d102-3721-9df9-bf8757002497 | -8.02082 | -43.20229 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| af04239a-7799-31e9-9015-9c0cba5a7ced | -6.83768 | -44.62656 | 2025-05-26 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5b20864-9149-3702-91e2-e67259fc7017 | -7.54408 | -45.82543 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 190de423-8a05-36dc-8fb7-17c54141ce23 | -7.65331 | -46.10264 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e454f4f7-bb23-328b-bdfd-f161e290d8c6 | -6.95845 | -42.06561 | 2025-05-26 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a861de87-f1aa-3d05-a761-52ac0b7eee45 | -8.027 | -43.18428 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 560c04ae-cea4-3371-abfe-4e413d546329 | -7.66331 | -46.10423 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0b57f561-80d5-3353-a7c9-75f647895b18 | -7.91118 | -44.48027 | 2025-05-26 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c2bd140-3838-3490-ba58-8dbcd0d20f2f | -7.17388 | -43.2586 | 2025-05-26 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d673c28-8ca0-3007-a911-16273e78cc80 | -4.29012 | -48.2762 | 2025-05-26 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf5be51-e652-3f9b-b784-3fd348f0e59f | -8.24521 | -46.80498 | 2025-05-26 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 204474a8-e304-35cb-9055-d27d8e805216 | -7.64049 | -46.11881 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5da338-a891-3569-825e-091aa9a57783 | -8.02534 | -43.19539 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 8a4668cd-6154-3c0e-9eae-b37b2fa0c028 | -8.02479 | -43.19909 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 2172bd24-0374-3417-af1f-abb7520b9326 | -7.66665 | -46.10476 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ed2c7b86-6342-33a4-88da-e2d899a1f681 | -8.0315 | -43.1728 | 2025-05-26 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 09f8d4db-5400-3d09-abe9-aff8cad4cd6c | -7.6574 | -46.1013 | 2025-05-26 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| e7cc6da0-e74b-336a-8810-3604a00bce41 | -8.0123 | -43.1984 | 2025-05-26 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| cf387b30-7ce8-323c-8ee5-83fd372e71b3 | -8.0312 | -43.1964 | 2025-05-26 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 175.6 |
| 6afecb44-cf9f-3aca-b6fa-9ae4e714e16d | -9.97896 | -52.13982 | 2025-05-26 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93aa7203-3a11-3ee1-b380-3acc7501dbc8 | -13.78695 | -54.31675 | 2025-05-26 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9b9a86c3-b0d0-3dde-b956-9be3af500fd9 | -10.64056 | -46.96618 | 2025-05-26 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39d6f9cf-7d8c-3891-a889-f99b91b87399 | -11.29318 | -54.01838 | 2025-05-26 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5074aa0-8eac-31f0-acb1-cd84b991fe64 | -13.7809 | -54.3191 | 2025-05-26 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8dd65bf-93de-3b47-be06-0f40de836c2a | -14.13738 | -41.691 | 2025-05-26 04:21:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8609953b-b25c-3845-970e-7f9387c83aa9 | -15.42988 | -42.16858 | 2025-05-26 04:21:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d53b4161-9751-35a5-94cf-e7a6215f706c | -10.15515 | -51.60905 | 2025-05-26 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62c1b415-4a3b-347f-82aa-732e0e0c82fa | -13.78196 | -54.31361 | 2025-05-26 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9caa1fb8-0e1a-3fcf-98da-499bffb72a58 | -13.53462 | -46.72805 | 2025-05-26 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b915195-5995-3101-bb10-e9b8c1c67501 | -15.93775 | -48.07388 | 2025-05-26 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c459078-d365-3225-b680-1e1f9f2e078e | -11.14123 | -53.92433 | 2025-05-26 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c9718422-8cb8-340b-b5c5-f98b61f415a2 | -14.88313 | -47.85659 | 2025-05-26 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0abcc027-9582-38e7-9bfc-b3b78a14cad3 | -14.57508 | -48.34755 | 2025-05-26 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)
