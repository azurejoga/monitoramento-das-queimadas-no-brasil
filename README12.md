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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f40d597-b64b-35a7-9131-0d424f17ab12 | -9.76103 | -45.92055 | 2025-09-25 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8edc94ca-bb05-3eba-bd0a-39c3eae11b78 | -12.05897 | -44.832 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73bf27d1-e615-3473-b40f-d5307ee3e6d3 | -10.59408 | -44.08526 | 2025-09-25 03:42:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d950fda2-914e-35f1-ba41-f5eff9864c71 | -11.53342 | -43.64355 | 2025-09-25 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc2d857b-9d5c-3146-8c63-51d20caa1b8c | -11.67463 | -44.40355 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da0b0fa4-9a48-3479-b867-abee043afac8 | -7.28898 | -41.86227 | 2025-09-25 03:42:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8382b64b-425b-39aa-947a-7d773361cc96 | -6.34814 | -43.36283 | 2025-09-25 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94bd81f4-47ff-3ba9-b03e-c770d86f3f75 | -11.78 | -44.91335 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22b5d5b9-b271-3025-a2c4-adcee0494e6d | -7.59075 | -42.32933 | 2025-09-25 03:42:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86cfec86-6692-30a7-af87-c4de6ffc4401 | -11.38677 | -44.95191 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3b18579-d146-3a44-a428-3157d30e449a | -11.64189 | -45.35356 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75902633-b6d1-34a7-b3b1-57b391d34ab9 | -10.80145 | -45.38757 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fb83b0d-ad8d-3f54-9d0f-1747cb5a290a | -6.42695 | -43.08351 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| bc524775-9425-3b35-8460-058fb84e0ca3 | -11.1131 | -44.88993 | 2025-09-25 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4c7b142-3605-35cd-95d8-7d231a0b6c51 | -11.6413 | -45.35669 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79c96735-0952-3bc9-9e64-8dcfd8fc37f7 | -6.22853 | -44.66116 | 2025-09-25 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfaeae38-b630-3675-9ce7-ad8d845908ee | -7.25824 | -43.01776 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e6b90df1-5052-39a0-be6a-08a6f63e462e | -11.63189 | -44.40562 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b98370dc-d4b5-3ccd-b745-15313a4227a0 | -9.24371 | -44.49334 | 2025-09-25 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd76e2e4-3db2-379a-9183-8e039817748e | -7.26227 | -44.90766 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 267a9390-037f-3823-81e4-909c33703f22 | -7.04439 | -43.9565 | 2025-09-25 03:42:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1626b81f-babc-342a-b61f-2825b0d2933d | -6.48879 | -43.79469 | 2025-09-25 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c876df8-1c73-36a7-9e71-a275b23828c2 | -11.92413 | -38.33098 | 2025-09-25 03:42:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4543a740-42dd-352c-96df-5a4cb1e88006 | -8.30164 | -44.94038 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63c212e1-4f45-35da-b1c6-55df3eacdeb4 | -6.7219 | -43.97596 | 2025-09-25 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9510e9cb-bdc3-330a-9692-28f3192f1d0a | -7.38455 | -39.64273 | 2025-09-25 03:42:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 510b43af-fff6-3aae-b5e6-5172e128e9e0 | -10.3853 | -46.13588 | 2025-09-25 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ec82df8-c33f-37b4-8c30-4fc227ce22cc | -11.76723 | -37.57359 | 2025-09-25 03:42:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d887c224-3b95-37bc-8313-0d9322c0fb91 | -10.58541 | -44.06527 | 2025-09-25 03:42:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c79c9cc2-8dc9-3a60-9211-5b6fd181227b | -11.52851 | -41.42838 | 2025-09-25 03:42:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfe4b5c7-6b1e-3a34-85ae-5eafc14f8aad | -8.47679 | -45.01075 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96bf3c2b-0327-3814-9bb6-f1c6816157bd | -8.28534 | -44.95745 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd8b5f2c-c6da-3cf5-9b4f-e1789c069534 | -6.41711 | -43.08195 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| b7daec14-b023-327f-918e-c04922a9a6fc | -7.28309 | -42.98909 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8783ccf2-463a-3ff3-9262-54f8bdbcc17e | -6.34761 | -43.36588 | 2025-09-25 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91dd756a-e667-30aa-919a-16025e9ddf2a | -11.62107 | -44.44527 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5516fe96-e58f-30a9-9a07-521358a8a7ae | -11.38731 | -44.94902 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e01cd022-2b81-34e1-986c-6c7353c1557e | -11.42055 | -44.92795 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d89b070-7f83-3ce4-9539-c0062590c37f | -7.25918 | -43.01242 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21acedce-b939-32cb-9f1d-7b90c9dce49b | -11.66661 | -44.41934 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b0c0b35-fbf7-3a97-b60a-b9d30ec16ba1 | -11.42112 | -44.92498 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a70334a-9c8e-3914-9e0b-a475e6a48b60 | -7.22471 | -45.18048 | 2025-09-25 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8b1b718-5fce-3e09-88cd-7e5b9cbe337d | -6.79468 | -41.76279 | 2025-09-25 03:42:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f9b0fa4-9894-3795-a223-cc7a4582f012 | -12.31159 | -44.21327 | 2025-09-25 03:42:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 821d93c1-27a7-3a80-931e-e51b828a7ac7 | -6.68551 | -43.14132 | 2025-09-25 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8da53faf-01eb-3898-a799-bbfead7e4bc3 | -11.61683 | -44.32201 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ae59959-9c64-3a7c-9e66-c3042c7fe471 | -10.15435 | -36.18979 | 2025-09-25 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b4f12a8d-b9bc-3a92-ab49-47a5e9a13f9d | -11.67255 | -44.41472 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e202436a-a635-370f-b4e7-805c31b4358c | -7.01827 | -39.25946 | 2025-09-25 03:42:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3db9c0d0-905c-35fc-a1c4-00393f113937 | -7.28401 | -42.98384 | 2025-09-25 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e399400-b95f-3a73-937e-0f46548b1775 | -10.24847 | -44.96554 | 2025-09-25 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd3c0064-2127-33bd-aacc-7b3d3078bebe | -11.39983 | -44.96699 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb1f5d7a-08ba-3e35-8367-eca7b27c9c5c | -11.93143 | -38.32803 | 2025-09-25 03:42:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3dbaa4f1-0773-39b5-b411-342fc9b994f9 | -7.45319 | -41.90123 | 2025-09-25 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c590e272-95e9-3cb0-b53b-c2a50a8f430d | -7.3001 | -43.91351 | 2025-09-25 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d207ae04-1f60-31d6-bcda-2c90062933bc | -11.53164 | -43.65343 | 2025-09-25 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce3e4474-6ca1-3844-bd30-87c5b7ff56e1 | -11.69033 | -44.40087 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d9fe26f-7fa1-3cae-8a5a-0fcf53b17d2e | -10.15491 | -36.1863 | 2025-09-25 03:42:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 23e6c698-4d4b-3668-832c-0f59dee17e9b | -10.93629 | -44.26664 | 2025-09-25 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af3bc8ba-f80b-3a10-86d4-cfcec605dbd1 | -7.26647 | -44.91574 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37f38122-7c8b-39a3-9dbf-ea00d3a20e70 | -11.40315 | -44.96354 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d82a3ead-d24a-3256-ad00-a87003ff5162 | -10.82714 | -44.82391 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a848d7c8-5a19-3cf3-bc39-77122cdc0a5c | -11.40641 | -44.96003 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2679a945-3a8e-3fdf-b475-00fa7b5674ff | -8.85148 | -42.47791 | 2025-09-25 03:42:00 | NOAA-20 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 336dc53e-5b33-3ad6-918c-2a4f2667f575 | -8.12963 | -44.13828 | 2025-09-25 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15bc0d79-ec34-3c62-89aa-a32c94fa7e40 | -8.48712 | -45.00407 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7650570-83d2-381b-b6b8-23b46cc358be | -10.11327 | -45.31517 | 2025-09-25 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b63a901-25e8-3c78-8018-adb24a4067a9 | -11.68648 | -44.39434 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1d7bae9-b524-3bb8-85e0-1ddf64e28b4e | -11.41539 | -44.92736 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10cadd66-43d8-307d-b3f2-a3b5a472c7fc | -6.4152 | -43.09306 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c7be6e5d-0c6d-35ae-8ff4-7b943baa0031 | -11.62474 | -44.4449 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92670fbb-89d6-3acf-82c1-b3a95280b4c4 | -10.38456 | -46.13976 | 2025-09-25 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebca5334-07ee-3181-b01c-f5f1a5c9516c | -10.93911 | -44.27885 | 2025-09-25 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80d4a506-aef8-319b-82f3-859840ee6e3c | -8.50684 | -44.99892 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4134022-3e75-3755-aa13-12b1e9339c9c | -11.62597 | -44.44623 | 2025-09-25 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10edf2ec-a73e-3298-81a0-2ea848a0a0ba | -11.42799 | -44.94426 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a9a7e0d-b733-3dcf-b2b5-d645fc1f3f82 | -6.41617 | -43.08737 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 48aa1d8e-beeb-33e1-8312-fbc2c0f39d9b | -9.18799 | -41.5839 | 2025-09-25 03:42:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae0ec77f-68b3-3912-892c-f3a7827815b7 | -11.40084 | -44.96156 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f531eb57-ea67-37a2-b187-b5c3238206a5 | -8.48281 | -45.00837 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09a481f7-93f2-3c72-be4f-b0ded91b9cea | -11.40613 | -44.97556 | 2025-09-25 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77d941e3-4952-3a94-96a0-6b4e7e9fe0a4 | -6.34969 | -43.35385 | 2025-09-25 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 848a5f3d-c730-31cf-bdcf-2c68b3fbf0aa | -11.01839 | -45.91694 | 2025-09-25 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6d7beb9-40dd-396f-9d44-22c3c2b194cc | -7.2568 | -44.90672 | 2025-09-25 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b47dc39-66be-356d-9268-0ac4806f19b8 | -11.91024 | -44.77168 | 2025-09-25 03:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1551b2c5-79d2-39da-ac23-350066c98c68 | -8.48349 | -45.00472 | 2025-09-25 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7e45c88-0c73-30fd-bc0c-fc1b94a793c3 | -12.54158 | -45.79757 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b29b614a-65fc-3d72-8287-3a1d698b78f0 | -13.39106 | -44.19073 | 2025-09-25 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d05ec36f-c9b0-3379-8aad-a0f310a06717 | -13.83984 | -45.61798 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82fe5211-de48-3174-b320-6c67179980c2 | -12.41171 | -44.74407 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 885ccf70-87f7-3e46-900b-9043ca3b73d3 | -12.85164 | -44.67851 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3a26454-635b-3df6-9fcc-65ea4d8364bd | -12.53763 | -45.79573 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3016917-674d-33bd-a6b7-623e7a82bd96 | -16.85232 | -50.51546 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b830b987-af3c-3f99-b5fa-07462f60a6bf | -13.83356 | -45.62301 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9186cac-20a1-3ca4-a78e-2f3d135c0e41 | -13.83416 | -45.61994 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21f497ed-383a-3967-917a-078ebb16083c | -13.82967 | -45.61578 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d52d8f38-f2d5-3e79-b57e-3ab9845d0c54 | -12.84853 | -44.69519 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68e0ddf9-c9b9-3890-81a9-d803281c9def | -13.84835 | -43.61255 | 2025-09-25 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 481bd1a1-a5cc-37c7-a159-284f7fe70370 | -13.39572 | -44.19177 | 2025-09-25 03:45:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88535db0-48a7-3fe2-bf25-b241f6c365f6 | -16.84709 | -50.50853 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README13.md)
