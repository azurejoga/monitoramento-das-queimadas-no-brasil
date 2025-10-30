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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e8a8fd3-08b7-3838-bc81-9e800cec8b27 | -3.60596 | -52.6506 | 2025-10-30 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95c14faa-5670-32b8-a3ec-af10982100a1 | -6.13213 | -41.58347 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a7c4317-1a00-30f1-ae98-c8cf7f0bce80 | -9.81946 | -47.58213 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43e7f003-4e3e-3029-89f4-8fc16ce3a65b | -7.79464 | -46.42149 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85e79828-926d-36fe-942b-dfcaa6b1efd7 | -4.84097 | -45.8895 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 981421cf-1938-31dc-a5da-fb672d1dfda4 | -9.9009 | -44.8886 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5614abd3-fb9c-3a48-ba9f-c6139fdec8a3 | -6.15671 | -41.66487 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 42e3ad0e-cf5a-30e8-9d81-39e6da851a7d | -5.59417 | -51.12515 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e9e890-bb72-3b25-b385-395b1eedf4ac | -11.68632 | -49.05219 | 2025-10-30 04:25:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3211b04b-f376-340f-bce9-29402b9f9b06 | -8.6997 | -47.90902 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c221093e-c396-32fb-95bc-beb81d3cd061 | -4.84597 | -45.42801 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 307e79d2-3ef1-3b9a-802f-9c26f2f000a7 | -6.49621 | -47.60022 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ba094ba-4628-30cd-87e5-bc8dc58ed0cb | -8.43437 | -48.69952 | 2025-10-30 04:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 77206f67-91f9-3151-90a2-322863703b44 | -7.79519 | -46.41803 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ded57f5f-cef6-33d6-a838-2cf41cc3fb07 | -9.93803 | -47.17826 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e959173f-f0eb-36b1-a942-49e47f504f44 | -9.2906 | -48.41984 | 2025-10-30 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a0b948b-d2e4-30d2-ba1b-94028cd0c68c | -7.41932 | -45.97859 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8275e41-bec2-3672-8f44-398efa1bf893 | -3.79888 | -51.64521 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50f82af5-f6ea-3541-b328-ac7759970743 | -10.64679 | -48.79808 | 2025-10-30 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7ca21b6-3f3f-3aa2-bb7f-fd2c1e8e1ad6 | -11.17365 | -45.22107 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6fe99d6-d78c-3542-bf94-021c55be6413 | -6.92105 | -42.2497 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bab1ee90-ce02-3902-8f1f-eff4ff212905 | -6.65636 | -44.60328 | 2025-10-30 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 718b178a-5bf4-307d-bb3a-d5bb45cae556 | -7.78472 | -46.41992 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| faeb3eb7-d6b3-3ff2-a779-1e2a7399f92d | -6.09816 | -42.4468 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ca5a179c-85e2-3eb7-a7a8-8c7bb6f46a4c | -6.91682 | -42.25183 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bbc441c9-70fb-3239-bdff-6f3bf2317ee8 | -6.91727 | -42.24908 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 57603bcd-36d7-32b7-8e9e-12f95cbb7c57 | -6.16604 | -42.38686 | 2025-10-30 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6cb987e4-350f-386e-a31a-232ed079f7f8 | -7.09968 | -45.22195 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9072191-a1e5-3c7a-acd3-0b7f65e8cd18 | -4.84419 | -45.84769 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85a186c8-1df6-3ad5-bced-64b38482714b | -10.01145 | -48.23173 | 2025-10-30 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5a16f5b-7b9d-3e70-8bcf-720e206c9e82 | -4.21912 | -48.35497 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fc146e7-7176-370c-899b-c3e903f8c6ec | -4.94301 | -43.83689 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99fabdaa-bfc6-3339-bffc-1360e8d09490 | -10.61598 | -47.89242 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 211e08a0-5f6a-395b-9295-a3d0f6451335 | -6.42688 | -42.32092 | 2025-10-30 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3a18a2c-bc75-3f4d-b86c-fa0f55758295 | -4.86828 | -45.54458 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd4f1703-f428-3209-b411-330ab1b61784 | -7.86581 | -44.23102 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c681ccf-a623-3f37-be1b-6aa8bd2a511a | -5.70138 | -43.15223 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 61fe0988-36a3-370f-99c2-67cdec79b011 | -8.70435 | -47.9869 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41e44ad4-4974-3df8-a4f1-9da9850f3640 | -10.1293 | -48.06751 | 2025-10-30 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2031bcdc-f2fa-32b9-9e90-2cfefe3e0aad | -7.80402 | -48.91031 | 2025-10-30 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 972fef4a-6a65-348c-ba88-54a859095671 | -4.17687 | -47.65043 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1dd801f-9083-3319-b492-4e17bc569f6d | -4.98191 | -45.03739 | 2025-10-30 04:25:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1eeacd2-8a0f-36d8-9567-5d9e0f8a1ed6 | -4.61518 | -45.68497 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 893db249-2092-3e38-a45b-59d85f527962 | -10.23582 | -47.63515 | 2025-10-30 04:25:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0114d78a-1101-3dca-9069-41a67798508b | -4.53486 | -54.9658 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2602ce97-1c64-31b8-8575-212a21980735 | -4.76021 | -46.85104 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6961522d-2f58-38f6-8206-6764239d9dbc | -6.12331 | -41.86564 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 695a8169-c36d-3260-873a-bc6ffb5d0d01 | -11.06309 | -47.53969 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5e8bb757-3e78-3d7c-9541-c4eb70c3d9b5 | -7.88308 | -46.74478 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f4439e8-824c-37e1-9d5b-7e9493b72b91 | -5.41309 | -46.01202 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f145a85e-8ae3-33c9-ba9d-321f979f59d6 | -6.15044 | -41.59875 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6a00e4e-73c1-3463-9283-370262352279 | -9.08761 | -47.90967 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ddbb58b-ec4d-3941-a522-c47f0953ce0d | -10.17306 | -44.66133 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35c2408a-7b51-3088-b7af-02597054480a | -6.15328 | -41.60177 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0b553de2-2e8d-3b02-b53e-c2a7030ef319 | -8.05045 | -45.17509 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acdbcab2-6245-3387-98f5-2bc2d7c4c73d | -10.76303 | -47.88693 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67b72c49-3e2a-3baf-aaa2-e63a5854ab42 | -7.92474 | -45.5055 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1fdf8191-1b00-32ec-a772-e73771f7d89d | -6.14537 | -41.68811 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 82657339-9c32-300e-a131-4641af05d53c | -10.76635 | -47.88744 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bc8d861-5e99-337d-82dc-a1ecb0052bb1 | -9.85295 | -47.69215 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f382ccf-48d2-3124-ad7a-1b22075fb97c | -7.06007 | -44.94558 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c0a7a7b-5026-3161-855f-f47dec391b58 | -7.23071 | -44.99054 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48f4d0ec-e984-305a-b0d2-790d04bf40d0 | -9.81693 | -47.70432 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e23135-604b-38f1-8b9c-3d9d33abf381 | -11.0047 | -47.7785 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b54f4a3-5f79-3fb0-8192-1d9700a476dd | -11.47285 | -47.07465 | 2025-10-30 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1905f64-ba8f-3f29-b375-b43865313fee | -6.85526 | -42.14448 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e2abc086-b8df-3437-920b-235fbcc5ae95 | -10.58835 | -49.75274 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee324a7c-178f-3130-9c61-6069c979f802 | -11.17765 | -45.2178 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aab6232d-6ec3-3934-821f-f78876ab78a7 | -9.29457 | -48.41676 | 2025-10-30 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63101ac6-3858-359d-8a4c-c491d883912b | -4.00272 | -49.2844 | 2025-10-30 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22b0198-1dd5-3f07-abf3-fd749f4f85ea | -7.34043 | -39.7123 | 2025-10-30 04:25:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d13e6fd-62a7-3983-b06d-c6fff3613bd2 | -7.96403 | -46.72568 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fa356a1-06af-3f5d-80de-f3352327345b | -11.64165 | -44.04654 | 2025-10-30 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f905751-ac42-360c-bc3f-52e888be7db6 | -6.14279 | -41.67046 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05f0f09a-57bf-3d6c-98e1-2f40b3c842a9 | -10.26029 | -44.57934 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7ed5b224-2715-32fd-8878-cd90af1ef2bd | -6.4807 | -46.88769 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69c30d09-4b46-37a5-85bb-ed63acf1e2f4 | -7.92807 | -45.50603 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b219e492-a144-377a-ad0f-df1eeecf4884 | -5.94706 | -46.65276 | 2025-10-30 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa34ee62-fff1-32d8-aa6b-967793f1f175 | -5.68067 | -49.15295 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a0c3fa4-cab3-3187-a1aa-35bbd4ca02ad | -7.38409 | -43.01244 | 2025-10-30 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a44cb372-d409-3760-8d4e-3147cd0c2f49 | -10.74892 | -44.74615 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17a2cc49-1dd0-3cbf-a0dd-79b286c9fd91 | -7.41987 | -45.97512 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17807f6f-8d23-3912-b9db-72dd272e5c6a | -3.82028 | -50.17605 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1991459f-6f6d-3327-a1b2-a147f24b676a | -7.38302 | -47.62396 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2ef6fab-8a0b-3b6d-9be1-e8ebdd29b35c | -7.3506 | -47.63333 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04f01260-fde1-32f7-9b38-7ae25a2a2f34 | -6.1431 | -41.59008 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3d5e519f-0727-3204-85ba-8bb5abbabc01 | -10.35754 | -48.69857 | 2025-10-30 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f64a7bda-a86c-3aaf-82c0-0d5e5a06f095 | -7.66441 | -43.91582 | 2025-10-30 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef15e482-009b-3184-8b8d-96d1cdd61f06 | -4.99083 | -45.5218 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd99be3c-e11a-394a-ab76-81944bb60b8e | -9.94354 | -47.18631 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d813f0db-7460-30cf-a4fc-cc436a9732ee | -4.53187 | -54.96539 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53be365d-3f43-3283-bf27-1a3f2a34fe9e | -6.13512 | -41.67685 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cf21db4a-be1a-3c79-9ddf-7183fdb53f80 | -8.16185 | -45.48825 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35fd82d0-ada4-314f-9b0b-41916fc0b097 | -5.63205 | -41.09622 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5137056b-580e-3e5d-abb0-2bfcc2d8fe68 | -8.69912 | -47.91259 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b8df603-309f-3678-a965-e64760dcf5f9 | -6.12714 | -41.8663 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5e002404-a60c-3847-91cc-e741ebe8e9db | -5.4307 | -45.33902 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de41342c-5218-3853-b65c-9c807d7d5e50 | -7.59248 | -45.8493 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8e76714-2f6c-3332-bff7-e88829cef005 | -5.70033 | -43.15546 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a17c87c8-3f30-3543-b028-3a9df6015741 | -11.145 | -51.06399 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README42.md)
