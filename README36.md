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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1defd400-b877-34a2-948b-a6bb202f5400 | -4.15908 | -46.18489 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bafb57e2-8c9d-31cd-bd68-d0368488f10f | -2.58516 | -51.92194 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e071230-401e-3cd6-86fd-e8860da3e55a | -3.79464 | -49.94395 | 2024-11-27 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f470d45-a528-3321-9c3a-f62c3aa4d608 | -4.21672 | -46.44796 | 2024-11-27 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b39e11-7980-3aed-8b3d-85b6dea74f13 | -2.83857 | -53.98619 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 552f3c09-8f1b-3428-87e0-a56e7c0de3b6 | -4.23732 | -48.64059 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 393e625b-b4d8-321e-928b-7845199520f0 | -3.31294 | -50.50013 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8394747-37d7-3edc-b84c-2ea730180abd | -3.77227 | -46.68001 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57fb78a4-31b6-30db-9765-fe35e290649f | -2.83875 | -54.12468 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| cf77fe25-0b9b-3d04-b8dd-9d95a7ba6ed5 | -5.19632 | -43.07604 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c74bd33-334c-3c92-9de4-f495c2ee7f1c | -4.59025 | -46.11797 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9aafbd2a-11db-38bd-9b4f-f062ba5b117b | -3.67017 | -53.55552 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fd9dd63-4429-3274-b689-99f64a216006 | -4.11459 | -48.48743 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e11850a2-b09d-35b3-aa98-c490583d137b | -5.40629 | -41.53979 | 2024-11-27 04:18:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9581b3ca-dabf-35cb-bf12-841671a54436 | -4.81026 | -46.84483 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2973ffe-df1b-3513-8edd-e0c5d04675aa | -2.82186 | -46.82889 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58a971e8-5a72-3ef8-a058-edb26355f04d | -2.69353 | -45.65829 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e38207ad-184f-3614-bd6c-663ca3dd427c | -1.64205 | -52.4948 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f38e89c5-5aca-348a-8eaf-2c6d866069ce | -3.10646 | -48.01754 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ac51c66-b8ba-3cfd-8888-f6204ffcd75b | -2.814 | -46.83186 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67469983-c98b-3ae9-8ed8-ca0c97415b2a | -1.79227 | -52.73836 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ecb76c8-b5f6-3e3a-a6ce-a99cd1b08b52 | -3.23251 | -50.67839 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e39c5cef-aaa5-3607-aeb0-6d956b036467 | -3.2515 | -50.62016 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49c6aa48-57d0-3ad8-bf1e-d7cafdd3a258 | -1.23157 | -51.95539 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 382f6a8b-d341-3333-baae-27662599227d | -2.57569 | -45.47403 | 2024-11-27 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5589803a-3f44-31a3-b013-8a79472ab824 | -2.84644 | -46.83697 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3a73923-ded8-3b1f-bd3f-c819213aa198 | -3.10363 | -53.2669 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5f9b28-d410-3cff-81ee-a929e97dfbe0 | -4.16988 | -46.72007 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d66eaae3-7ece-324f-8555-77441572eafb | -3.96409 | -48.06479 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c206f7c-2910-3886-b510-b439a1aa720e | -1.65066 | -47.70891 | 2024-11-27 04:18:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb3d6757-d0cd-367c-b4db-6c8c292b1291 | -1.80195 | -52.74693 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39f52181-77c4-3a49-afad-c4181e351028 | -1.15026 | -53.68072 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66486057-9a79-3e60-b7ba-086137f809cb | -3.15886 | -45.93559 | 2024-11-27 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df9e54bf-e05c-3a90-9b7f-1bb4d6716791 | -3.09735 | -50.35941 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebebe23c-a75b-30cf-901e-56c6d7ffe347 | -0.54826 | -49.52038 | 2024-11-27 04:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92a5cc82-5748-3042-86ae-63e520dcce7e | -4.27206 | -42.44015 | 2024-11-27 04:18:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ff70418-74b0-3cce-a0cb-1d4fb27d6598 | -1.78689 | -52.73748 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 553f8276-977e-3de2-bdbe-ad1b92a8e2cd | -2.39522 | -48.96455 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d0a03b6-eb35-3ce7-b6c3-318775cb071a | -2.71729 | -46.26023 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0666a8a-c6a0-3807-94ba-26496f12a789 | -5.3667 | -35.61597 | 2024-11-27 04:18:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1613c62-9c05-3234-972f-b3392b0a06b4 | -1.76342 | -53.62516 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2c38498-43c3-3ac1-bd3c-fc188a0f261e | -3.04544 | -48.51223 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| c7d3ded8-38bd-370a-8f80-cc176036b1f9 | -2.58234 | -50.64419 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76c5eeb3-77a4-36fc-9663-d525ab9ecde4 | -3.67136 | -53.54835 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39fe8ead-2517-357d-95fb-34aeb0beef6f | -3.68988 | -50.22626 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2678ca8d-b9b0-3d53-bb35-891eefeea49b | -2.93416 | -48.0136 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33bf3f03-391f-328e-8461-7f36ae0884bf | -2.9371 | -54.78944 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a4b3cf0-b45e-312b-a3f4-8e36deb5a8f3 | -1.65845 | -46.94234 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 142487b2-950a-350b-884f-ee6debee066d | -3.97916 | -46.65019 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f9b0025-4c13-3ef8-933a-45b2407d9af5 | -3.97563 | -46.64967 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7541f16-ff86-3d71-af95-7f7808df04a5 | -3.10651 | -53.255 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ded6911-f5e6-314e-bf78-4de31b7f4fba | -4.15417 | -43.81794 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a140881a-5f7f-3dec-927b-dd7c4f31afde | -1.79768 | -52.75073 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2a3327e-ba4d-38d1-b568-d7c815ce7b44 | -3.22917 | -45.38484 | 2024-11-27 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c0c5102-c073-3771-8b5a-5581b9ee87bd | -5.83731 | -39.21039 | 2024-11-27 04:18:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2dfc762c-1a2d-3584-b6e9-a534bcaca825 | -3.1108 | -53.26273 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd0167d5-ac85-3924-8b47-40692526cb0c | -3.67568 | -53.55647 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb038d38-9c70-326e-b3f5-cf334c1503f8 | -4.0526 | -48.32663 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aa5c988-d149-3e31-aa1b-90177b9ee346 | -2.82128 | -51.79521 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5242d499-c30b-34d4-8f95-b92d40fd56b1 | -2.99985 | -45.46464 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| af704286-34b6-33c2-a993-fa240fffa991 | -2.10392 | -46.55963 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21729f44-5d56-3e21-974f-ead344350995 | -2.69822 | -51.98255 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7111b3a-d59d-3671-a0f6-f673e3ce064f | -2.53556 | -46.40579 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd474ee4-4b19-3534-a679-8d3d50e813c2 | -3.03836 | -48.50591 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1838e5c3-5200-3bf6-8b6a-1677c9b191c4 | -3.78574 | -50.2707 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86bcbe4e-653e-3204-8341-3ce71c05c75b | -3.5681 | -41.9609 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60bfb875-e69a-378b-b6db-69ca7dfd3fd1 | -3.28361 | -41.77293 | 2024-11-27 04:18:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 37214900-bb3d-3f89-b094-4588b77f9ce3 | -3.44965 | -50.2947 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ab8aad1-415a-3efa-a14f-5bc0b74d663e | -2.81524 | -54.12691 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53b9aa6e-b2ee-35cd-a13c-5035a53fe011 | -2.83365 | -54.11967 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| d48b731c-bcc0-3d35-9b93-b210dc78c90f | -3.72673 | -50.19143 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1323d8e9-703e-3958-aa53-b60016c62af0 | -4.14306 | -43.80204 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 444ed0e7-959a-3bf0-9123-1692fe106009 | -1.78043 | -52.74334 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3de5374-b0d5-3114-a696-b30752b36cdc | -3.71926 | -50.18351 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5a030c2-5960-3bc0-9ae0-5b8ff6794426 | -3.17833 | -50.2189 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ee57221-b484-3803-b808-d3e09b3edd8b | -3.13053 | -51.02145 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5cfeb90-f15d-3257-81a6-ca6f68b2952a | -5.00557 | -44.85966 | 2024-11-27 04:18:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ed9343b-c500-39b4-9050-c069bebc96f7 | -2.83435 | -54.11561 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ce3baf7-68e5-3787-a717-0f5d5628daea | -1.66513 | -52.72416 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75a29a18-1168-35d5-9759-058dfcc9fd60 | -4.22086 | -50.90691 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58fd35a4-5768-34f8-b0f6-466d6e1b12e1 | -2.83497 | -46.83941 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f24d92cc-8377-3d1d-b9ad-77001c05e32e | -3.14942 | -48.53592 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa219605-3b57-3f04-bc9f-7fefab45ce46 | -2.53803 | -47.32582 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d2868ee-ca43-3c47-ace3-116ef5b4f524 | -4.6973 | -44.96444 | 2024-11-27 04:18:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb9aaf8-86e2-3260-9ef1-4ee4dbee9665 | -1.60515 | -52.75269 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 818d5768-01e3-3ab8-b974-bce07f4250b2 | -3.99846 | -43.25603 | 2024-11-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c3cf7c9-a00c-3ba5-b37f-11b7d897569b | -3.11685 | -53.26011 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac25e6df-5f8f-396a-b565-2440f8988b02 | -3.08587 | -41.14295 | 2024-11-27 04:18:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aeb60214-e7e9-3ff5-a738-a2d9306c8b58 | -3.23101 | -49.43377 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18d0fe3f-0b6f-342c-b7e2-775cb4d523e3 | -2.99368 | -47.34687 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c58285c-e057-3a78-9e5d-be558f4f302e | -3.97697 | -46.73076 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a05c66bf-332d-3c8e-b08f-0b6d2f1cd22f | -3.5796 | -41.95502 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4e1097d2-7357-325e-844b-88da2f65313d | -3.27927 | -48.75572 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5acf1f86-26e1-3958-bc12-1564c03ade60 | -3.69427 | -50.227 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b4f3b66-5de7-317f-8217-19150ad25362 | -1.79173 | -52.74175 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8879c9-dd12-352b-9422-d727c6931024 | -2.83987 | -46.83176 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60e7fbd5-6fbd-377d-bbb5-f9358908f0bd | -4.29342 | -48.20046 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6571e1c2-febe-347d-a8b2-a0fcec5bd52d | -3.29208 | -50.54303 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9123d76-672f-3018-be98-ced8407d727d | -4.72236 | -43.25339 | 2024-11-27 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12a72f52-c1b4-37e1-9c7a-22a726e2a823 | -4.15948 | -43.74081 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README37.md)
