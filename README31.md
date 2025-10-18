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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70579e48-9e73-3565-b717-37cc77c55bcf | -13.51656 | -48.00663 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a0a8f55-c561-309c-9d62-0f678b865862 | -9.09478 | -47.78811 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfb8fe27-9033-33bb-a7c6-1b5247fb2c60 | -10.53549 | -43.37507 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d99827fc-349d-3214-beab-286cc369f2d9 | -13.47696 | -48.122 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72a16745-bf6a-3d72-a527-efa7cc30adde | -11.36962 | -44.25908 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6e73854-ec4f-3cbc-a3e8-a1ae128ecf42 | -8.78587 | -47.93748 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b624c638-70f2-3f79-87e9-2c1b7d678f2a | -8.87863 | -47.97238 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32f77163-b79f-3b34-acc1-0e69d81442ec | -13.19945 | -46.41947 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35c7039e-56f8-3b66-a1da-390884fc364b | -8.23452 | -43.31969 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3a96d60f-11c9-3f50-b1fa-34b4f5f2ae4a | -13.46072 | -43.76174 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0950b9ba-1541-3f15-953f-94361f421c61 | -8.27616 | -48.00576 | 2025-10-18 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4f8307a-e789-306f-b721-1685bb465cfc | -8.09698 | -45.43555 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bea41dd2-8485-3a5f-be61-98683f0f2a1a | -12.15666 | -45.08968 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b85a857b-139e-3f96-8a55-d9284dc287a3 | -10.63494 | -42.3065 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9b0121f2-0bb9-3d67-a356-7aef28e08f79 | -10.75441 | -47.88755 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00357e0f-0cfb-3ef7-8146-9dfcfbec4903 | -12.15928 | -45.06372 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f84f0db0-5350-3caf-b5af-401168bd4f91 | -13.5174 | -48.00214 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3804b70f-9abb-3a6c-bc3d-eb63458b9c45 | -10.68294 | -45.33298 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44f518d8-c5da-3119-b7cc-3cf7b5cc66f2 | -7.36712 | -44.06881 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e43c31f-baec-3a5e-8306-961c1865b22e | -10.62091 | -42.30793 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 242e3e46-c226-362c-9191-bf516600caed | -10.79344 | -44.0924 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47922a11-608b-3897-a828-40dfa780d5ed | -7.9868 | -44.15548 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a112ae9e-2de3-3b33-913a-3845d385c2af | -13.76698 | -48.22257 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d349ab3-9f40-3c0e-a82f-354ddff45047 | -12.21764 | -42.24397 | 2025-10-18 04:02:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14e3be8b-e7f8-3679-a90f-299d91076940 | -10.49979 | -43.43901 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 601fdd49-5123-39fc-bdba-18f757c77b66 | -11.49009 | -44.23496 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c9c797a1-a079-3ea4-b12e-d3ce1160a0bc | -8.09317 | -44.10172 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0537480-bdd1-3db0-9bbd-437560888ae1 | -13.0384 | -47.28404 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7d36771-093d-39b5-a641-77e376b9fe56 | -13.48896 | -47.95668 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c4c5f2e-3386-3850-8e22-cad298bac47d | -13.53557 | -48.00156 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66a2ea8f-e9d3-3a98-bbf3-6e43cd5be7df | -7.58402 | -44.98972 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b650c24c-6e32-3370-ab7b-0899dd35d4a4 | -8.37612 | -48.70729 | 2025-10-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f3c8410-0ba5-3e30-bfc8-0ad3e462b858 | -10.25684 | -44.03336 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68f9ff16-41c0-3487-8900-227b67f29e2f | -10.69257 | -44.55539 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a2f4a61-95a9-39e8-b4d8-3908206acba7 | -7.44858 | -42.68782 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13ddad1e-73f2-3233-aaca-7173815d856d | -11.20414 | -47.8301 | 2025-10-18 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e9c76eaa-a663-3192-abfb-ab2051a19cae | -10.49828 | -43.42646 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c75e12b-ada9-383f-9e68-4549557e94cc | -7.34043 | -43.86121 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2e271b21-b669-3275-9194-e1b045f7202e | -10.16021 | -44.52826 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ea420690-6c01-355e-b251-2f4bcb044696 | -13.19241 | -46.43631 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 518dc870-0027-3f71-8de9-d5c81a16bd71 | -8.10853 | -45.44092 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d08bdece-9f1c-3df2-83e3-77a2d94be854 | -7.95844 | -44.11852 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5eefb527-c99a-3c4f-9591-6183c9ff8a95 | -12.57395 | -43.76623 | 2025-10-18 04:02:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffedbb36-32e5-3a18-9ded-3e5f0dab1def | -8.35931 | -46.21311 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c511bf2e-aa82-3c70-93d6-badbedd09d2e | -11.36723 | -44.18513 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 940d29df-9568-3f95-9098-a13285cbb9e7 | -13.04287 | -48.1859 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64fa04cf-6596-3c2f-a3e1-63ae12c232f2 | -10.49279 | -43.43786 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| cc2f0944-0326-378c-a660-58ead0ec8ce2 | -11.40323 | -44.07991 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d4b7959-ed16-3a8d-9bd4-72e991b5112a | -8.216 | -43.97367 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa342255-6571-3806-a226-504f606f12a7 | -11.51785 | -44.06843 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90ea9338-fabb-3229-a5d6-34250256915d | -7.45843 | -42.69339 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82ea0b3d-1eb9-3926-91d0-9a22096b079c | -11.49149 | -44.22656 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f107580-57b3-3c00-abeb-5a842ca77bf2 | -9.17882 | -46.72789 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 569a293d-b9a7-3cb0-9858-aab34ad4d5fe | -11.57893 | -44.04818 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c9a963c-048a-3d14-8b69-a727b5de58c4 | -10.30292 | -44.03198 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e23d374-6756-3305-874a-c070ea131290 | -10.61286 | -47.38329 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dae3a74-f7f4-3582-8655-2b6c52937a29 | -12.70523 | -48.62932 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06033cde-fbf0-30fe-8fcb-05c8abe6ec0d | -7.47505 | -41.52133 | 2025-10-18 04:02:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 63cb7da1-1094-306c-bb5b-13f2a940590a | -11.35152 | -44.21265 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc4a6f7e-9013-32f7-b1c6-1bf0f52a1a99 | -8.39471 | -46.2352 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 47ee67fb-ddb4-3638-b3a0-155c53351a52 | -10.29644 | -44.02647 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec29a31a-6a44-31a5-bae8-c22f5e89f8e6 | -8.54556 | -44.57986 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40ad4f07-112a-3071-9d79-8767e9a10295 | -10.50613 | -43.44415 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1385c37-48e4-387e-b81a-cd0a0df65193 | -10.72214 | -48.14832 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5872798d-fec8-3018-9efb-e1949a5b559d | -11.4564 | -42.94762 | 2025-10-18 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 06704d31-6210-3834-80f6-6761a76b2f06 | -12.72965 | -44.86547 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdeb5569-bbd6-34c3-9ee7-4c98e207e0ef | -10.25129 | -44.06722 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f5d7661-77ac-37c5-9ab1-9104da4112b2 | -12.78972 | -48.63132 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1edcfcd-ce03-34ca-ab1c-8dd0b9a11f69 | -8.19254 | -43.31395 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e92c2218-6ad0-3beb-8b67-f877ea6c4090 | -7.62494 | -47.8396 | 2025-10-18 04:02:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15a3c590-3bac-3f2a-ab7a-9a48d4c285ae | -11.50206 | -44.18528 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01685135-f4cd-3804-bebb-6d885ce73577 | -9.72562 | -44.54554 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7aa7a3e8-09c6-3890-ab01-26df3e646ba7 | -13.45676 | -48.11038 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d717da4-d673-38d4-b9e4-443099602411 | -9.6206 | -46.31546 | 2025-10-18 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6a11428-3954-3cb7-aff6-512dfa36bb87 | -13.83417 | -42.63145 | 2025-10-18 04:02:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4102ed7-f87c-38b1-add3-21f943afc831 | -10.13205 | -44.53695 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12060f4b-906a-3c8e-a844-816eac0b5da3 | -8.19527 | -43.31335 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 700b2643-1608-3416-8792-a320f9e14bd2 | -10.49365 | -43.45433 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d317d215-6aad-3139-a2c9-bd02307eb13c | -8.07403 | -43.90502 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| effba8fb-ea27-33bc-99ab-ccfae8557441 | -13.92185 | -45.60201 | 2025-10-18 04:02:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e56d0162-882a-3c71-896f-d50633a481a2 | -12.16209 | -45.05836 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e509ed09-ccf9-3a04-bc86-b96452afaaa4 | -6.96139 | -47.11722 | 2025-10-18 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9451bef8-23b0-310b-a045-3e59cd3d6cdb | -12.91235 | -48.58239 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dec5157f-b530-316c-9378-c6bce8fa8905 | -12.1563 | -45.08151 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6865b48-fe50-37c7-85a7-85c8ef4efaa3 | -11.3711 | -44.27237 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c630b58-310a-3325-878d-5348bfb08513 | -8.19972 | -42.35114 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce495173-5b31-330a-a248-641cc26e212e | -9.72185 | -44.56833 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bfe3c3c-66ed-3f42-bafa-f0e7428ecdba | -10.59281 | -47.99854 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3063b95f-8e4d-3ee7-8ef6-a3003133ef27 | -7.12551 | -47.23051 | 2025-10-18 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81a63781-1f89-32d9-be2b-c6d352d69ab2 | -12.16413 | -45.09085 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d0de1a8-79cd-39e5-ba92-5059c93d5ed2 | -7.76027 | -42.4837 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 509a9541-5dbe-3327-972a-ec1ba797cbab | -10.53842 | -44.5086 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1852120-96b1-3a14-815e-f2c6b1c1196d | -10.43659 | -45.0143 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f56f635d-400d-3d31-b16c-1d4efa981f42 | -13.6057 | -42.42069 | 2025-10-18 04:02:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 73adeaea-36f0-39a6-9990-c6cd006b607e | -10.63158 | -42.30594 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 31dfb705-b62f-3705-bbbe-3807987b7f50 | -9.61737 | -49.67875 | 2025-10-18 04:02:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a314fb89-8509-3db6-87cb-47a65795117f | -10.46701 | -44.06581 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 720a1fb9-6bf7-389a-aae1-c7447f34f599 | -13.83808 | -42.62841 | 2025-10-18 04:02:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a861b45d-ac7e-3de9-80c0-ad5d5ad3ac41 | -10.49695 | -43.43446 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bd5821de-dec2-3b62-ad76-6a0d3e55d163 | -8.69409 | -47.06327 | 2025-10-18 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
