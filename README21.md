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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d46ff95e-d407-3027-bcf4-5f0ef290ec7d | -12.16076 | -64.13344 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 767adb6e-10e1-34e8-846e-ca4e1375a60a | -10.46879 | -48.65586 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b15fca87-037c-3722-8965-0e3ff5b7dbfb | -8.63631 | -66.51841 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9ed8381f-c70a-3439-8b17-732a403000a0 | -14.6042 | -48.8485 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65b7ed16-16ff-3c34-89dd-b78dc2436347 | -14.50351 | -50.11461 | 2026-09-11 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91c33cc4-0ee7-3863-a596-7e6d865601a1 | -9.37307 | -55.96666 | 2026-09-11 04:53:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa769340-4b92-3bf1-bd6a-e3a3a4f5965d | -10.95906 | -49.64405 | 2026-09-11 04:53:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3c54dc4-7805-38a5-8d15-36b1fa958589 | -14.8437 | -48.17554 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4d48dc6-3ad7-336e-8adc-2388b7b7771c | -11.81466 | -60.46238 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c44807da-8a7f-3b21-822e-0a8bbb410e6a | -13.21775 | -61.63975 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7d8f4d9-5146-3e42-b87f-e3fb76d431e0 | -13.49728 | -48.54887 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0889aa62-a80d-3aa6-9eeb-6e8c6977c62c | -11.11364 | -47.55101 | 2026-09-11 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fd674e2-a2e3-33bf-8a9c-47d33fbad165 | -12.35403 | -48.20132 | 2026-09-11 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1cf2763-f63d-34c1-bf1e-637d416fca00 | -9.02363 | -65.41438 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cc12d06-299b-3d5c-9114-0ac63f68c8e6 | -12.23474 | -51.33184 | 2026-09-11 04:53:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ed450d1-d932-353f-9fd6-4d01bbe0a415 | -14.59058 | -48.85434 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51e9da66-7bc1-393a-b68f-990731662999 | -14.79217 | -48.08546 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59560cac-7894-34d9-97da-0b6b05c8ad66 | -9.07152 | -61.03534 | 2026-09-11 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9fe5fe0a-1651-325b-80d8-e14c1ef31bd4 | -11.41178 | -43.95063 | 2026-09-11 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14b37248-e565-3291-806c-64f7b6d00566 | -10.75252 | -45.92218 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59fd78a3-3b4f-30ec-bc80-fc0994ef6eac | -14.07137 | -45.63453 | 2026-09-11 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c526e839-7e2e-33ed-8dc1-f454f50886d4 | -8.63873 | -66.50589 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24468292-86b4-3dc7-bc96-f433490d7fd6 | -8.98791 | -65.41647 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e17c42a4-2f4e-38bf-b3e1-8c0dbf56650c | -14.78281 | -48.08804 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b963658a-82ce-3c92-af4a-183399fdc5fd | -13.36669 | -48.01595 | 2026-09-11 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3797775-5995-3e7a-8d3f-18a69972d75e | -11.4086 | -47.72885 | 2026-09-11 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 807df2a7-90f9-37fc-8ee9-e33a222077f8 | -9.0734 | -61.02486 | 2026-09-11 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7849f9fe-8c4e-3f39-ac64-3d78e367ef17 | -9.0183 | -65.40801 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 570794af-9906-3c06-ae36-67b351f0cedd | -9.07246 | -61.03009 | 2026-09-11 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f9362b1-c1de-3bd0-bb9a-7d4f5b7e864b | -13.29257 | -61.82273 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01e9e30a-50fb-39b7-96f2-3c65a4ad6f4a | -13.50024 | -48.55983 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53f25dd4-69b8-396a-b61d-3512846c675c | -9.75419 | -64.94508 | 2026-09-11 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34bc9550-e0e2-37f4-932a-d5d38dbe1d56 | -13.50074 | -48.55597 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01ca2faf-eb98-33ae-8f0e-53e4622b5173 | -8.84125 | -62.48339 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2f3dc082-60fb-3ed7-938e-c66981267f6c | -14.5859 | -48.85744 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0b434ec8-a7b2-3323-8a6a-2a04b2d78d71 | -14.9139 | -44.67222 | 2026-09-11 04:53:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8defdeaf-c4f8-3ef8-bca1-3fb82783e225 | -10.5291 | -51.35092 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdb8b966-ded4-340c-a782-79ce06c62051 | -14.6059 | -48.86817 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca141cb7-d4ea-34bb-9f52-f075d1e2e806 | -13.32969 | -61.67493 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83e6cc4a-e24e-396b-b089-1f9438c9ccd7 | -13.2879 | -61.82184 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9aa26a4-7e2d-3c16-bb04-034fcc054cf1 | -10.6714 | -49.07716 | 2026-09-11 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4075bc-5a58-326f-b249-3bd95bcbd3ac | -12.51466 | -56.90647 | 2026-09-11 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b52e13e-e965-3698-9cc4-e6ff8e223e32 | -11.29405 | -54.03409 | 2026-09-11 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 196ce0ab-0060-36e1-9f85-596a67d00194 | -13.77323 | -43.64413 | 2026-09-11 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 820242f4-4d08-38f1-be53-1e9a919f2dd2 | -9.0436 | -65.41286 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f7e2659-fed4-3452-b96b-5fed33016dae | -10.48586 | -48.65103 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01a85454-ffe6-3f21-b69d-5f5313fb9a9b | -11.81543 | -60.45803 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f7852e3-fa77-36cc-ae74-6bbd2339bb30 | -10.46928 | -48.65223 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5d3f534-8b7a-334a-9bdc-9abf844f2c28 | -12.18859 | -47.17623 | 2026-09-11 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c862e322-4025-3f9b-97bd-944b508b68f1 | -10.46693 | -48.65971 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bdf17ec-314d-39bb-9a26-8ed28c2fb416 | -10.64426 | -46.15639 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 263c46a7-f539-3572-b89d-2a9b2457819f | -8.82947 | -62.48812 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97cf5714-61d0-3bd3-8a66-fc70dbcd59a0 | -12.34978 | -48.20068 | 2026-09-11 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57413ca4-e985-3b71-a892-d083dfe0d8c3 | -12.18919 | -47.17154 | 2026-09-11 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 046df01b-83c2-3cfc-ab74-465541c60139 | -10.3608 | -48.13929 | 2026-09-11 04:53:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26f72d19-546b-348e-b649-b8ee0fa9fd0c | -13.34538 | -61.66774 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b542d177-e0e3-3dab-a168-6f5c1cf0d8ed | -9.03728 | -65.41164 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8311882b-091f-3acc-94ec-0d3832cf8397 | -8.98889 | -65.41126 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54df451e-67f9-39a4-ae9f-04a45efa42b3 | -13.34076 | -61.66685 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4beb634f-335b-3248-a964-83af48ea7ad8 | -10.4733 | -48.65288 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4c55f7c-f184-3ed7-863e-40c5e3c37701 | -10.10832 | -54.9259 | 2026-09-11 04:53:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45ce46a3-b775-3276-ae56-223242c0b500 | -10.46831 | -48.65938 | 2026-09-11 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfb2bb27-649d-3d96-a59c-f0033b37897b | -13.50499 | -48.55634 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51d133a8-de93-36a3-9ea7-e04149e47b7a | -8.6371 | -66.52235 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d4d22a9-1ac8-3756-81f5-0e4eb391045b | -13.32878 | -61.67985 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47ad04de-0b3a-3372-b0ac-c4bb209404e4 | -10.77541 | -45.93641 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ef21930-26df-31ac-92e4-4e31419c82a6 | -13.00006 | -44.1153 | 2026-09-11 04:53:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb5b4504-04b4-3dad-9526-b265807f0b19 | -13.2271 | -61.69271 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 889d9cb8-ae84-36d5-8c8d-283a9d2a5dfa | -8.84065 | -62.48668 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| df5bce9f-ce37-315f-b594-c5c15a42c38d | -8.83536 | -62.48574 | 2026-09-11 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 676f9ade-112b-3191-867f-0e5ad145ed81 | -11.41291 | -47.72967 | 2026-09-11 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 160c6bc0-debb-34f7-ad53-de97edc4aeb4 | -13.2251 | -61.62589 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ab6b2ac-6c93-3a93-91a5-e065fee91f0c | -14.85873 | -48.15985 | 2026-09-11 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cbe1e5a-f12b-349f-bb5a-8b2c8cd5442e | -11.81182 | -60.45295 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bec67ba6-2dac-3840-a795-0984c821236d | -10.78366 | -45.94901 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f05b3dc5-ad55-322a-baa1-656ea00004d2 | -8.46239 | -64.05882 | 2026-09-11 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c19f7794-ba14-3a26-81b9-c0fd554adfed | -10.78925 | -45.944 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8e165559-7993-3a6c-baf5-626d876b70d5 | -12.15959 | -64.13462 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d13460b1-9180-3df3-abaf-34545dc494ea | -13.48343 | -48.55588 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ed90c43-94f9-3f9c-9e9d-2f93aba906fb | -13.36278 | -51.77592 | 2026-09-11 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80c38277-547b-31b2-b5e0-cd56827dce76 | -13.22601 | -61.62098 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9383cf3-da6c-35b1-a23b-ebb25633c807 | -9.39943 | -65.86619 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf033768-de65-3892-b725-90a447c7a959 | -14.65679 | -44.12447 | 2026-09-11 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db51a192-4839-3f16-a577-eaaa29fb09fe | -12.15451 | -64.13605 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6697ab93-6e3d-3cb0-8e30-abce607ec51f | -10.53659 | -51.34838 | 2026-09-11 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af5a19b8-7b5b-31e5-a0ba-ea63efc1c5cf | -10.64365 | -46.1238 | 2026-09-11 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9665106e-f909-3da1-911e-dd561804bf08 | -8.63753 | -66.51209 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 15b302a6-e29e-3040-a284-80f90802a6ba | -9.07818 | -61.02566 | 2026-09-11 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c571ada-4207-36d0-be5b-ee0a8f184f82 | -13.50042 | -48.55753 | 2026-09-11 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6866da81-9a1d-38a5-bb5b-0c23e5011247 | -8.64311 | -66.51969 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f752351-7e0a-3f17-867c-41786c2b631a | -14.60641 | -48.86431 | 2026-09-11 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 213c1977-8add-3ed7-8e53-ecf4a10d3308 | -13.31954 | -61.67808 | 2026-09-11 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cf0863c-d188-3bee-bb60-be20ebd0f9db | -9.30033 | -65.89201 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12d762b5-e42d-3be4-95e1-75c85a74ce58 | -13.21866 | -61.63483 | 2026-09-11 04:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 860542e2-9dd5-3a1e-a5e3-646935703b99 | -12.36422 | -54.17133 | 2026-09-11 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5ec4069-c2ec-36ce-8419-618189bbc87b | -10.94546 | -54.0888 | 2026-09-11 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc858391-b87d-3047-b631-6dd801c39479 | -9.41403 | -65.8616 | 2026-09-11 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86b18ca4-ef9b-37b1-add9-793d8cf4e790 | -12.15809 | -64.14219 | 2026-09-11 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f05aeb23-a404-353b-8d50-fad40cd7a99f | -13.00616 | -44.11213 | 2026-09-11 04:53:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebf89154-abd7-30dd-9c88-d5bca00f5b1d | -11.39855 | -55.24395 | 2026-09-11 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)
