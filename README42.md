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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b00a2f22-daa7-3932-a809-0e9231f5a737 | -3.98762 | -46.63475 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90179d39-ee53-3fc1-8b94-059b96c76ecf | -3.5398 | -50.18047 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d46a323-6d0d-3d9e-bf14-281796a79e42 | -3.26382 | -53.34507 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d081c92-0dc1-39d3-b7f4-d1fd7bf97176 | -5.81574 | -46.47406 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 22e97c17-9e21-3fbf-9c48-1f9452d2a868 | -3.29244 | -53.67253 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9a45bffa-b902-3925-b775-5bd394be52ed | -4.08424 | -47.35976 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db2f0136-100c-3b0f-a06b-109ee51478c9 | -3.26452 | -53.34081 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 564d9dbf-74a5-3821-8e85-d5abcb77b2cb | -1.79034 | -52.29195 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef7c277f-5647-32e0-921a-31f54a7820b5 | -1.75464 | -52.80776 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4db0c901-6f59-33b4-89c0-631ce69dd7c0 | -3.18483 | -51.16309 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c923428-af2f-3e01-b8e2-8c94ac813a68 | -4.0766 | -46.69477 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4d67353-7b74-3b5e-8565-89a65e2b650c | -2.6652 | -46.59818 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 594b0012-63b0-3e66-91b1-386e4cae3441 | -1.38514 | -53.55628 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a8868520-bfbf-327f-8f48-b987dd04ac06 | -1.95081 | -51.20818 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ed6ed1e-d6ff-3ad0-9220-c0c56d97bf6f | -2.29282 | -46.37368 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa6fc741-80b3-34f7-b337-6fa0a95763f3 | -3.55189 | -50.1741 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9ccc27a8-e934-3473-a2af-a4d73ec7d923 | -4.03309 | -48.26537 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aebccd31-2b06-3607-9ee4-fc411af414ed | -2.59837 | -46.54902 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca006d26-97d5-3d10-b93d-8f941e3f6b59 | -3.26771 | -45.37352 | 2024-12-03 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 691c7e8a-c860-34f2-a8b7-36610bc28218 | -2.6617 | -46.10154 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d13a278b-e278-346e-be00-d74516ff1980 | -6.1145 | -43.96214 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e480b9e-838e-313f-854a-77e0baef1377 | -3.17201 | -46.29128 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d1befba-081e-343b-84b1-4d0a9aae4bcf | -3.34201 | -46.04921 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| db1b43c1-f1f6-3044-9f92-cf16c62b666b | -3.29091 | -47.02688 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75921f94-f785-3684-9c4a-14c08fad6042 | -3.82949 | -51.3487 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b452914e-2ca9-3127-b452-2d0543820067 | -3.95744 | -46.5022 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd5463cc-8715-3285-834e-7813bcc70fe4 | -4.31423 | -48.09769 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 006d969f-251a-394f-93fd-fcdbec7579be | -2.28951 | -46.37316 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cb99d0f-5e99-3e4c-ba16-592b747addb1 | -6.26824 | -48.52476 | 2024-12-03 04:29:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74489d70-9526-33d7-b960-6252374596bf | -3.86047 | -50.89929 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df34d783-e5f0-38eb-b213-543365889c39 | -2.00234 | -52.09853 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f5c3c3c-0c42-3ea3-941a-fb9ac12868ed | -5.1226 | -43.20607 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| efb84f2a-58b9-3910-98fe-4065bedd3835 | -5.58324 | -44.88345 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af00f290-b03f-3202-be12-7bd081a3b971 | -2.45353 | -46.54016 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4ae887c-f198-3f93-b60d-b31ecef6d6d1 | -2.80417 | -53.06522 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f6be604-4f81-3bb2-9294-94365a258c22 | -1.7413 | -52.62804 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa93c3e8-daa8-38b0-a22f-be33cad575e3 | -4.04978 | -48.268 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c1a6bb-2607-3eba-8d58-fef842e6add8 | -4.03364 | -48.26184 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f020020-f1c8-3ae1-bf1e-49bf0f7fad5a | -3.92657 | -46.72098 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 212d30f5-5a4a-3bfc-ab43-8b194708507d | -4.1182 | -46.90675 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 769b001a-ae24-36ff-b2e6-661a5b93af0b | -2.54952 | -53.41424 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61b35d55-6c3a-3c6f-ac41-79c21bf140f4 | -2.82286 | -53.05974 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b12dafc-b1a3-3b7e-b831-a50d213dea7d | -3.50827 | -53.82728 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3337c10-94ac-34ce-a333-5ceee1f161da | -5.80515 | -46.47604 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a3853b65-7a4e-3f26-9a1a-07c94b4e645e | -3.3664 | -53.21061 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7dd313-cdf1-3a52-b636-615253449ae9 | -3.15653 | -50.62277 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb8e9921-51cd-35a2-9b09-e564a496bfbe | -7.10408 | -46.45911 | 2024-12-03 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91208bee-9b5e-39a6-b021-426f4e247b14 | -4.52937 | -45.73161 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf7af60a-0e08-3c07-a63d-4471493db076 | -5.11662 | -43.21971 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c776a46-c075-3ee2-96db-963418a2b46d | -1.65549 | -52.75196 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0eb73bc1-50cd-3ff0-83e8-a41dddcea518 | -2.72097 | -46.2 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 714c3be9-5187-3906-94c7-7790eada4d54 | -2.6845 | -46.60469 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90ab20d4-80fc-39de-8601-69b780213c98 | -3.13413 | -45.98866 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 171c4680-7cee-32b7-bb56-1a9d23688fe8 | -2.5116 | -47.42331 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a7af283-4063-38d0-b0c4-71a24100e1b6 | -2.75569 | -46.13065 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62f3d340-31cf-314c-b624-16d5427911b6 | -4.0012 | -46.93752 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8536db60-bf0b-3e99-84c3-aed5bfe14405 | -2.15104 | -50.69651 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68731e53-35e4-3eb6-8e4e-f5dffa2db559 | -3.2086 | -53.62231 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e79799d-3575-3655-abc4-cd8420b17c0d | -3.97 | -46.66043 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5e1d842-43e6-33cb-b0e9-757b9270dad6 | -2.66225 | -46.09806 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b449aa-25d5-3b0d-bbab-c9b85f397f64 | -4.0389 | -46.82689 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54165e81-d066-38c7-b7d6-a451d9f945ca | -2.83186 | -46.85634 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 147967e7-7a3d-3156-b484-7dc4003097fe | -4.47294 | -45.71546 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 418297d1-6ab8-3e74-b4af-d7c640e74698 | -4.94147 | -47.80548 | 2024-12-03 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb6f371-5657-3218-9dac-717cca8a91e3 | -3.25482 | -50.57599 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32736034-dba6-3a83-bd3d-436d54fc01f5 | -3.09504 | -54.05199 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06ad95a4-9d49-371e-8f7f-1936c0a3a72d | -2.43247 | -46.50164 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf5138fe-83c8-363c-bea3-53e61a8e036e | -3.34256 | -46.04569 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 39871dd7-b1c5-351c-872b-0a130e4fdf9b | -4.31201 | -48.09019 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b2a8e06-14a0-3541-99e0-410d4752cb95 | -2.59017 | -47.48463 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 723c2d16-2287-37fe-85a6-29099545890a | -3.14406 | -46.59887 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 326870b6-0e32-3293-8967-1edf0a1b5264 | -4.32808 | -48.09631 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fa076d8-79df-3b43-ad4b-0b6e25a35721 | -2.51215 | -47.41985 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 805d3884-e992-33a2-87fc-14f02043980b | -2.51007 | -51.81199 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2d3b7f6-5774-35c6-9358-e576f281c880 | -3.91868 | -52.3879 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b2e8b9-b748-3406-a9f5-8a94aae3bffb | -5.38779 | -42.96215 | 2024-12-03 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a13499c8-c7d1-3755-9e85-83b037373a50 | -3.26171 | -53.63485 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 892343c0-3150-3c94-95b2-c2305c62bd34 | -5.42194 | -45.11563 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df1aa3d2-7fc8-37ec-acde-c01bcad40ab5 | -3.08652 | -53.38169 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9f5428db-4bc0-39b9-aa8e-8540e173cca1 | -5.57206 | -44.88581 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dbbe10d3-34f7-370b-8708-2fc3620b1957 | -3.13972 | -45.99672 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5da4d11d-8576-3a4e-8af6-dbec4e2feb23 | -3.40305 | -50.25431 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d4cfb76-85a2-34e6-a024-64abe89a6356 | -4.34458 | -43.7513 | 2024-12-03 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba17bf80-1e0d-3f2b-a7d0-1f9cbce8241e | -2.78376 | -55.36778 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb0d4b2e-dab7-3b2c-9162-5a0afe705760 | -3.19093 | -51.17369 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd94471a-7507-308e-8b25-439d69992214 | -2.6818 | -46.62189 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb9a3e60-c743-3b1a-b6ef-ef2af5f21069 | -4.81076 | -44.99507 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40b142a0-8beb-3573-88cf-6facf5ef50ca | -3.69134 | -47.11483 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a688ce10-3fc1-36cc-8b93-0c28d471485e | -2.29528 | -47.50261 | 2024-12-03 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 041b75b2-f43b-38d8-9023-6787cb18b028 | -4.48076 | -47.73289 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90730e7f-9454-340a-8ae0-c43944f59b3a | -5.41982 | -46.11431 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 218dfa11-0012-3e25-9132-8a474c35f589 | -2.66851 | -46.59869 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b7bbbd3-bd28-3254-8a43-49ffa7421f79 | -2.6173 | -51.81841 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4407d0c-2007-3758-90dc-7a4f5ed3d55b | -5.33098 | -45.44112 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b5b7013-b4ed-36f5-80e4-c068ba13294d | -2.34097 | -53.80527 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df9a8fac-ab5d-3b4b-9635-de4c802e0fe2 | -2.50401 | -46.24058 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7434c91-8fdc-309c-a842-b17d379c4854 | -2.24065 | -48.80346 | 2024-12-03 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e330e60-cc68-380c-9c7b-0e9c0dec9a91 | -2.19845 | -48.33635 | 2024-12-03 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04b5393d-291d-3195-a120-3695e1481c9d | -3.95541 | -47.66086 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d249008a-ef11-35da-8bf3-3890e4b6b55c | -2.68673 | -46.61209 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README43.md)
