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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0985d033-4f94-391c-ba4e-eb30e1cabaca | -7.95522 | -44.12172 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc0a3cda-dc50-3f3b-9493-781c4535e392 | -7.34065 | -44.15795 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa399b61-fc0d-38ba-8f4c-f74b9838d969 | -9.89401 | -47.66817 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a0e02a91-7152-3fdf-b33d-4d02bc7eadcf | -6.47335 | -41.85102 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bcc30e38-7d58-3d7e-b682-25a5a29711b5 | -8.41877 | -44.73008 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18945700-6726-3515-9f6e-2db1aa9d0a6f | -5.27842 | -43.2194 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad3508be-46f9-3dea-9e12-5c3ae60a2082 | -6.81766 | -41.70519 | 2025-10-17 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ada7c54-7fbf-3909-9769-7430573f1da7 | -5.46056 | -43.47117 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8cb1dbf-8316-3b20-86a5-2d93117f75b1 | -6.54131 | -44.28785 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2dde91d-a3f7-3174-b805-e60e6e70493e | -9.88948 | -49.12031 | 2025-10-17 04:19:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cc0a801-902a-34ec-a9b0-ebe901e19876 | -6.99961 | -39.22973 | 2025-10-17 04:19:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8270477f-741c-3edc-a207-ea761a4dc6b4 | -10.1174 | -44.61108 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7568f5be-9654-3906-a094-09a1334845ba | -6.37331 | -44.70984 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24195e61-e614-3e65-8688-4e69db9c7070 | -5.41419 | -44.25146 | 2025-10-17 04:19:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd10ef49-bd7a-3c7c-973d-4337880116b2 | -8.49533 | -48.49059 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff103616-b535-3020-9af3-5007cfde21d1 | -7.45602 | -42.15675 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 943bb8e1-a0a2-3fa0-b884-43472f5cf6c3 | -9.71395 | -44.5587 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 381ac602-c31d-395f-b936-5938b1e96fd5 | -5.99386 | -44.15596 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa570c4d-1045-3c84-ab67-d2bb8a2dd4ab | -7.86258 | -43.88284 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48e36efd-c787-3d44-a624-53b1c6bffb4d | -10.30043 | -44.03865 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 816ee8e5-e0ae-3f52-b025-c549395d695f | -5.45756 | -41.01357 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3259dd7d-e5dd-3b31-b058-73d43b4db631 | -5.32512 | -42.89437 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dde0c2b1-a3e6-3abb-b484-9619a67b24ac | -5.52605 | -44.5998 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d79aa06-e94c-3d2c-b1c2-5e91da3f2526 | -6.40448 | -41.89872 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19753ed1-c9f6-3448-8328-9939a2702c59 | -7.27565 | -42.94257 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ae8c4ab-0cb4-3105-ad43-c5b967089328 | -10.27571 | -44.01991 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 938db8e7-7a8d-310e-b727-33f5739b0ce3 | -5.32793 | -42.89849 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 41d4e397-7603-3312-9fc8-ed934547c407 | -8.25404 | -43.4323 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 792abb87-09d8-34c0-bc87-4a8f236c1ac5 | -9.26603 | -44.35461 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa5f4c55-424d-355e-ad46-e8dd2a7c5fee | -8.52407 | -44.57918 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9db36d4f-e9c5-3b08-95ec-00209acfe414 | -2.87232 | -50.73832 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ab6acac-c68c-368e-89b4-81b43757f25c | -6.20658 | -41.74623 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 395982cf-8528-3751-8b97-5df042f1a35a | -7.35582 | -44.06025 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1547317a-9122-30fb-a422-8e695019f3f9 | -6.13381 | -41.77396 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b496b9a-9571-3832-b63f-3339d2634b07 | -10.11891 | -44.5572 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9011b2a8-cfc3-3f2b-892d-d02c6493a0cd | -6.09802 | -40.88807 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54ddbb07-23b3-3df6-a6e5-78714dd5009f | -6.74555 | -42.37107 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8795bcbd-df5a-348d-8067-c64a15142e4f | -4.86618 | -45.7835 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91cd3efe-b7b9-326f-a84b-8dd3b5de0bce | -7.48306 | -38.99603 | 2025-10-17 04:19:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 508dce34-c065-3b81-bfc1-3a63d9f81d55 | -5.86218 | -47.58187 | 2025-10-17 04:19:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 08dc14cc-ad76-32fb-acd3-083fcee9f711 | -4.1561 | -42.2105 | 2025-10-17 04:19:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc21ce63-a196-3705-a9fa-dc5b1fd5fe8d | -8.23997 | -44.01791 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bca193da-5348-3679-969f-c692065b224d | -4.45512 | -44.13871 | 2025-10-17 04:19:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41da8842-2fba-3de7-b83c-c7c34f0553e9 | -10.11504 | -44.56021 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8627d75a-e093-3417-bd10-c00c17927c1a | -8.36449 | -44.77478 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 622e771c-d88f-34d1-b2cb-8c2e647920af | -5.20652 | -43.7487 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fefe4ee-6376-3c11-a784-f3217005cd62 | -6.94255 | -47.72604 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9998df36-18b1-3c29-bf93-a2ce8bcfa0a9 | -3.65964 | -50.26579 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d334d522-9b97-3a59-b510-c9907f1af20d | -5.34024 | -44.89542 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcf86d10-435e-39a3-9aff-3fa3d4e3146a | -9.10305 | -46.66949 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11a8a3d0-06c6-34c8-8de3-faf5bccdea01 | -10.29479 | -44.03043 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1650b461-a5d0-3f88-81e7-c8455d71579e | -4.88582 | -49.94642 | 2025-10-17 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84ab738-7478-357d-b890-34f456164103 | -6.38512 | -41.47187 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c6175474-6389-3db3-bd39-e288c766b615 | -6.192 | -41.7248 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b71d8318-d9c2-3d68-a4f1-d04d75045543 | -6.82393 | -42.98401 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cd505569-7f22-3d5c-9ea2-1c503fc4c581 | -7.09658 | -44.2619 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe42b861-227d-3038-a922-4a6351f55aab | -8.23438 | -43.43724 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 680d1054-7b33-3809-9478-a59e1f4b99f8 | -7.97949 | -44.09661 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff5172da-23b7-3a76-ac18-b7dcc1562a50 | -7.29774 | -41.9547 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 58bdc28f-e8ec-3d1a-a9ce-63438eea9656 | -8.22244 | -43.31171 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3e9e0d9c-fcd1-38a4-a470-e8412d4bdef4 | -10.517 | -43.39827 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e7ef061-711d-3a01-83ee-83cb4b79270e | -8.13879 | -46.89985 | 2025-10-17 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49437071-39a7-3a37-bd48-13f9916b5117 | -6.13794 | -41.77054 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 072cc94a-6a2f-3c6c-8c2d-34c611e699bb | -11.48643 | -44.17436 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 554363c7-ce22-3fd1-9a8a-1f0d698c8aff | -10.49639 | -43.41815 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fac6a13-7dc7-344f-98f7-d18424197500 | -6.22282 | -44.14911 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d68fab9-4606-3f2c-bccc-643b6d46edb8 | -3.50565 | -52.49311 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3686f4c7-e766-3ae4-b241-69c69bbeea2d | -10.52101 | -43.39504 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab597477-fed0-365c-8256-0b7f293e853b | -9.14847 | -46.64358 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 66f69a7b-a15d-3c4e-9d2c-1d8cda61cac4 | -10.57101 | -47.4417 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b08ec3d0-3fd4-32a4-b260-24db22b4a58a | -3.53739 | -49.00958 | 2025-10-17 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecca0c85-26b3-3e20-9ed9-7fd7b9e88981 | -5.23672 | -42.00462 | 2025-10-17 04:19:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb0ca1cc-217b-3318-b5e0-8c11f9269855 | -7.12643 | -44.8328 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9412c937-ea63-3da2-a79b-88a60a7bd3de | -9.29947 | -46.93279 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ac02e78-1ccd-38e7-b840-6cd2f6f4cf53 | -3.98295 | -44.69463 | 2025-10-17 04:19:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e36d2819-4981-301e-a4fd-bd131aef51ee | -6.29451 | -44.01476 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d8a38df-e930-3fba-8243-6ec876ac323b | -7.83027 | -44.13763 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e3b6194-29d7-39d4-a40f-4ccec4a2ce92 | -6.12972 | -41.75291 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3c9fcad8-80f4-3707-ae8d-298f598501ae | -7.08997 | -44.26086 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b1ec08f-73d9-34fb-9959-db02aeee592f | -4.96938 | -44.96054 | 2025-10-17 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2167b31e-8681-3f50-85d1-9927174bc0f6 | -5.23626 | -49.22738 | 2025-10-17 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a06cd4e3-051d-3bf1-98e6-68f905cbd490 | -10.28132 | -44.02832 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45cc4533-7fdc-3620-9461-8e13a3b43840 | -6.09689 | -42.39232 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca808663-595c-376d-b7d7-11d56f3d95b4 | -7.11685 | -44.74297 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 050bcaf4-f944-39a9-97a6-d10e8c632c8d | -6.20564 | -44.43249 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a7d017d-c045-37af-bdb0-72b285dacdfc | -8.39424 | -46.24709 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6761a39e-a648-30d3-8f9d-e2ae185b4400 | -7.39929 | -44.7455 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7745e793-d5f2-371a-aaaa-d3e8296a3695 | -7.11205 | -44.79522 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caaea04e-c6e0-35d2-8f6b-7371425213bb | -6.7412 | -44.16339 | 2025-10-17 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95c94861-ff9f-359d-93c4-fdd34d8b43a6 | -6.23693 | -44.9707 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7f48491-a0c9-3a79-a1a4-940f324a6dbd | -7.47682 | -46.90568 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dce4dd75-94d0-3ceb-b460-17f3c53f3ca6 | -5.33457 | -44.47476 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fdaf4a33-b769-355c-ac5b-592e3c777abb | -5.8823 | -43.91145 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73fa779d-4b78-38a8-a201-1a627a737c20 | -9.05504 | -46.99014 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6c77166-ed9c-3ad7-b5b0-e57067fa7477 | -7.48815 | -47.03065 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0341964-7202-30b7-9e01-0858e30f130f | -10.28526 | -44.02513 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67840fe2-25aa-3181-96c8-5eb04be77e9b | -8.25583 | -44.04547 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76915a8b-8402-3375-9379-58b720f72dc7 | -10.50551 | -43.40435 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86985e3e-2799-3f9a-bc98-d635f533436b | -5.62486 | -42.6764 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae5ab0e3-2c97-3a73-96bb-7d37e8efe610 | -9.08057 | -45.02713 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README40.md)
