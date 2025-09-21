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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0785af95-c27a-3208-b058-22b8f6cdffe9 | -5.5254 | -43.86988 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0325a534-69f8-3514-99ad-f658b49a8c37 | -9.42005 | -44.70766 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6128fcef-6226-364f-9238-ac635a64e26f | -6.60867 | -43.75816 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0568cac-26bb-3d64-b5c3-13a9a0cb8a17 | -6.54171 | -44.27431 | 2025-09-21 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82275199-f104-3aaa-8858-6b733da2cc31 | -7.94167 | -44.09919 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b9c719f4-3564-3cb0-8c39-41ee0cdeef80 | -7.72724 | -44.46321 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4e679367-a70e-3ae3-88da-d6924c5a3974 | -7.92731 | -44.10075 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33d0b28b-a1a5-3ed9-b0d2-f16e26c49782 | -8.01694 | -39.91549 | 2025-09-21 04:08:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64e89de6-9b6f-32d2-9eb1-ecd174c7894d | -5.63645 | -45.95403 | 2025-09-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 96a2ac64-3af6-3b07-8b2f-df51fe702fa9 | -3.75705 | -54.81159 | 2025-09-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9009bbe3-7ac4-33ee-87b3-9f8dd37e14bd | -5.41938 | -43.26573 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ab4f9afb-612c-30ef-a001-e0ef2d704296 | -7.35599 | -44.57629 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0bfb863-b14e-3bfe-82c4-1c8be217c3d5 | -8.34827 | -44.70589 | 2025-09-21 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b56e19a-75a0-3dd6-b061-89eff9081c25 | -7.56616 | -44.73573 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e117776b-a7a1-3976-af8f-b95d389113fc | -7.62163 | -44.44298 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e4e084b0-949d-3935-b2bf-489d5dd9dc0c | -6.55058 | -43.52719 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d98ad8eb-a674-3824-ad2e-8aac53bc630c | -10.2697 | -46.05252 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a61648f6-0370-3a67-a61d-a0bd757a2710 | -3.76421 | -54.81243 | 2025-09-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4afce2d-30b6-36dc-aca7-cb03213f732b | -10.23999 | -44.97923 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e6f07ac-e837-33ed-8332-af2b37ff5892 | -8.84307 | -43.03965 | 2025-09-21 04:08:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0da013cb-ff98-3183-9c29-f2d4f64c2453 | -6.5528 | -43.53522 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cff45d54-2994-3ebf-9258-2ca877a504a4 | -7.9358 | -44.1137 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 431e9982-da8f-3444-a067-6b8d03fb8a12 | -11.49206 | -43.57206 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9ef7d94b-1321-34f5-8c55-46809bdad84b | -5.27241 | -44.81709 | 2025-09-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cd18e19-5c87-3562-877c-c9f7023acc82 | -7.41952 | -44.54443 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 143b47e6-29e0-39d4-add7-9cd6a5bc737d | -8.84202 | -43.00349 | 2025-09-21 04:08:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf3ab605-6d14-370d-9752-e8e074eb42fc | -11.23065 | -46.16898 | 2025-09-21 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d23e495a-6321-390a-bf85-0289e7c34610 | -6.55339 | -43.53514 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6c2d76d-2938-3232-94a5-44a5521cc3c0 | -6.01699 | -44.32817 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1dd7f00-8762-3f2b-89e6-c39e55711e16 | -11.49036 | -43.58268 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9494e9d3-e668-331a-b151-16eb87ead087 | -6.08691 | -41.00204 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a742188c-20ca-31f6-9bc6-28916979efe7 | -6.19581 | -44.05272 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36dfd0dc-2fb4-3ae2-93c5-476deebdb462 | -9.17501 | -44.62125 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60f1692d-22bd-3fda-aade-4e05c9c46acf | -5.65146 | -51.46479 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cf7e22d-a35d-3a6e-ba92-12ba1552a473 | -7.93075 | -44.10131 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73eb07f5-c633-3b93-9be3-97eaf24b26b9 | -7.35792 | -44.56427 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b65866b4-a1e2-3937-8e46-08a4805d2496 | -3.30028 | -52.58838 | 2025-09-21 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f5f744d-637e-339e-a286-ad33771f8ce3 | -7.7231 | -44.46656 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 035856ee-32ad-33b8-bc24-4c3f455bb739 | -10.41583 | -47.85274 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fde9c2f1-eaa1-3dcf-89ee-a1a9e86b371e | -10.01766 | -46.23672 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04b9fe2b-77ee-3aad-afa0-e161f452b000 | -3.6265 | -47.52363 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c4f5974-2201-393d-b259-8f24ed462195 | -6.94706 | -44.74799 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c96db16-e205-3daf-9d16-7fc177724afa | -7.19603 | -43.81997 | 2025-09-21 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d1d5604-fd95-3fa0-9b4c-64abd147c5d5 | -9.43202 | -44.72154 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc7f7273-9f2c-37bd-8048-3744ec79f747 | -6.30556 | -42.36385 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 253d56f3-2f91-3460-b1fd-5f9f20c47856 | -6.85164 | -44.17135 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a524801-4821-3b81-80c8-05e1c8912048 | -9.43138 | -44.72538 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbfad9ed-c53b-3515-ac01-e4a24dc4cb40 | -11.78168 | -43.76172 | 2025-09-21 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 609c26d1-29b6-35a6-8f58-1843afd4e830 | -4.66032 | -43.48536 | 2025-09-21 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21e85c34-a45c-345d-b4cf-da90e9b97bca | -4.19628 | -48.54905 | 2025-09-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bcd0ba6-64b2-3b15-b0ed-dc03aef7b8ea | -8.8128 | -43.01619 | 2025-09-21 04:08:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba3c9621-94ed-37f9-a98c-48b165abab70 | -5.7581 | -42.57455 | 2025-09-21 04:08:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ca769270-8a19-3a52-9bc8-cf03cd7cf115 | -3.59984 | -47.52558 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d1cba49-1487-39c6-a67d-d1332869211a | -4.65071 | -43.39076 | 2025-09-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5cafd38-60ed-39bd-8a37-c455f40def9c | -5.60054 | -51.49104 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58daf1dc-7ca4-36be-b599-a8f4edd3ba94 | -10.36192 | -47.89919 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0459d47-6fd5-3493-88a1-21d58f8ce7c6 | -5.51905 | -43.86498 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 92c0ed51-ba01-3efa-a779-1a74db8015ab | -9.00831 | -45.06487 | 2025-09-21 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 085bd2ef-65ab-361f-b338-3ed9753ecd45 | -10.34684 | -47.88902 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06a5e6cf-0355-3c7f-ba3c-7cdf3e8eed0e | -5.74962 | -43.37455 | 2025-09-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ead8ce8-977d-3b8d-b16d-da03231d3256 | -11.49093 | -43.57914 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af718026-3e3d-3029-94c1-bc863fb99ab2 | -10.41706 | -47.84579 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cfd2fe4-2709-3c64-9576-44464a0871ee | -6.08754 | -41.01984 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 335c1964-5d49-38d0-aa9d-e140e3f96274 | -5.47595 | -44.41898 | 2025-09-21 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 769eefa1-eedc-39a9-b7e3-4e9d6f680402 | -5.00981 | -45.20599 | 2025-09-21 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89e34549-be90-332a-8e92-b0c9f4dd095c | -3.6043 | -47.52623 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7f9bc78-baed-350e-9791-1e9e5c8bd02b | -9.17736 | -44.76096 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 896d7122-b3d3-3c80-be17-a0210bc7f730 | -11.48655 | -43.56391 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 606a2062-cd6c-350f-8c81-c88edd53acdb | -6.17349 | -43.68957 | 2025-09-21 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0067db42-9220-3459-8313-af04528d0798 | -5.75775 | -44.20249 | 2025-09-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6122d54a-fafb-3e12-8914-3ead3733fd12 | -7.92792 | -44.097 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 616f7224-be4b-3558-a6d6-9dc8f1074ede | -6.34789 | -44.68568 | 2025-09-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a7454b3-d41f-3aab-aa76-eb10139f85ee | -10.26532 | -46.05627 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f47f8f1e-094b-3a7a-8103-04f1a61aa1e1 | -5.34113 | -44.90294 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 878f723a-9074-315d-9fd4-20321bebbcd2 | -4.19545 | -48.55411 | 2025-09-21 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a95d760-d596-3fb0-af46-8d15ca979618 | -11.77779 | -43.76473 | 2025-09-21 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8bc9604c-b962-30e1-b92a-fdd3f654990a | -9.77717 | -47.19173 | 2025-09-21 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0250170e-c8f6-3c68-832e-594951c2e8af | -6.19995 | -41.19341 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04f2de09-1d29-34bb-bd2d-ec70bb30f28a | -7.59831 | -45.4921 | 2025-09-21 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5de1a091-6fe9-30ce-9a43-e94a41714c54 | -7.47963 | -46.6663 | 2025-09-21 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55e54199-b6fe-3c06-8a78-6594bc23806c | -7.36081 | -44.56875 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e6eb0ff-eb5f-33d6-af81-74558336effc | -6.39609 | -43.31062 | 2025-09-21 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 849fcba2-0a1d-3a28-a715-1e61eec9d872 | -6.25519 | -44.09317 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6364d6bf-6ea4-3c92-9c65-6aa0a8221786 | -10.34392 | -45.22636 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7fc6b3f-6de4-384e-a2a0-2b87c2bda345 | -7.91983 | -44.10341 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 366e5cc5-9fc8-35c7-906a-5e2974481c9d | -11.2819 | -41.847 | 2025-09-21 04:08:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7160e9f6-f7f7-3971-a004-0f0956a864da | -7.92144 | -44.11527 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62320823-84b7-39f5-8f54-88a05dd63219 | -10.22339 | -48.07064 | 2025-09-21 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 931f021c-8835-3ae9-94b6-004e5e3882b3 | -4.79718 | -47.28043 | 2025-09-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90ac8d5c-91d1-3961-a540-bda18efbe7fa | -5.42337 | -43.26258 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 03e6bcb7-5719-3ad9-9d56-6690f485958e | -9.73843 | -48.08438 | 2025-09-21 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4f19f53-2146-326d-bdfc-2a575d7f61b9 | -7.03675 | -43.43508 | 2025-09-21 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d2a3067-967d-3380-8968-12903c2ed86a | -5.95093 | -42.51852 | 2025-09-21 04:08:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8c6fc0de-34ae-3885-bd56-4767e57708fb | -10.28217 | -46.06826 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee5d7f9f-cc8c-32f6-a930-f86277679690 | -5.27313 | -44.81273 | 2025-09-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7315c380-9f11-37f7-90b7-e4e6e7401635 | -5.15121 | -46.06209 | 2025-09-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a92cbda-7674-39b1-9b12-9464b72a2f2a | -7.94389 | -44.10728 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f2b648f2-a134-327c-9ef7-1fd5da60dde4 | -10.02361 | -46.27002 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fc4c61d-6721-3c4b-b6cf-585e96f38f4e | -5.58954 | -51.19602 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef866ec0-0f68-373e-97d0-df1ba8d10b1c | -6.59454 | -43.58337 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README12.md)
