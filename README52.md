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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cb5bfd8-07b8-3d28-b84f-b90098d0da84 | -14.79639 | -42.72352 | 2025-08-15 04:51:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1f8aa99-a95a-3a43-b601-4810eb92012e | -9.49737 | -60.55407 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7f5c76e1-b3a2-324b-9427-5ac0163cc86f | -8.10617 | -61.21326 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3eebd671-5f3a-3228-bdcc-bf2402523b4b | -12.58468 | -46.96318 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2db49345-ffa8-36f9-87ac-4b260e64c447 | -10.35871 | -50.81532 | 2025-08-15 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b85b0f49-f907-38af-b8ec-3f493141938d | -9.49829 | -60.52832 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f6fd2bb0-909f-3266-960a-2788ea297813 | -7.52115 | -61.37744 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7231dead-b17f-3d3f-a9ad-7fd0d6778713 | -9.82791 | -60.76371 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b81a2db-a990-34e4-929a-93ac73b6ba44 | -10.00791 | -59.21903 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f54c781b-7cac-307b-8a14-d0ba96f2626e | -7.86503 | -48.23033 | 2025-08-15 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6dab04a8-bd06-3588-8743-961606d50f81 | -7.31787 | -60.61835 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c6f6340-4786-3548-a2e0-cd90974683f6 | -10.96294 | -49.56987 | 2025-08-15 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2e80a5d-48ed-3a9b-a88c-0f1c8b177faf | -6.47947 | -62.93954 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 850d7fca-b78e-3fad-9131-79e1ef25b1b9 | -6.90756 | -59.13141 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a778730-4371-381c-b2f3-46021166da57 | -9.50463 | -60.54041 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcf9d936-0714-317f-bc80-31f18d77f409 | -9.20843 | -49.67617 | 2025-08-15 04:51:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e5d9bd3-ffa5-3fc0-9cc9-67ad1033faa4 | -13.31591 | -45.23094 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ff0559a-88ad-3620-bc37-324c1b172c7d | -10.32129 | -63.62556 | 2025-08-15 04:51:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21ee19c4-bdbc-390d-b883-7ea4ef32ada2 | -13.46874 | -43.75314 | 2025-08-15 04:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed83160a-a2f7-329c-a155-d217d60b94b4 | -9.50325 | -60.55433 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 61eebe79-a8cc-3cf9-a9db-ff07047f92c4 | -7.07798 | -59.21813 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ecf9e5e-0386-3d5b-bb1b-23458efd405b | -9.17507 | -59.6859 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1f20205-f905-3739-81dd-d3415f0f118c | -7.3893 | -60.00717 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c9f6c6f-a3b4-3308-9786-569763187d40 | -9.21008 | -59.66594 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a0df342-da1b-338a-8809-202befabd3d3 | -9.3946 | -60.54908 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7bb9090-7926-391f-984a-0c697eeaa447 | -7.31692 | -60.61837 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b4c1e3c-0686-3981-a465-3db30c23e096 | -10.96676 | -49.57043 | 2025-08-15 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d7a0db7-6879-3427-8e67-672fffca9bcc | -9.50375 | -60.54519 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 983faa03-4fde-38e9-a9a6-7142cd721bbe | -6.72675 | -58.83942 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b175190d-9fe8-301e-b181-382994160315 | -5.89211 | -57.74569 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b845d49e-60d1-3ffb-89eb-375d09b813dd | -14.0159 | -52.04384 | 2025-08-15 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4312827a-4567-3ff9-8185-53635f6b575e | -7.87547 | -61.82243 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54523983-679d-3405-b8c0-420ae7f3ef33 | -14.23937 | -44.58457 | 2025-08-15 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af1f2979-7e12-3fe2-aee2-99d6a3ff5993 | -15.40137 | -46.59798 | 2025-08-15 04:53:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c01e55fa-450f-3bf0-b244-2f9643280185 | -16.37047 | -50.8968 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4d3abbb-c646-3477-a6af-97edd3ac5118 | -17.0595 | -51.79853 | 2025-08-15 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6e2bfe6-502d-39e1-9084-11094a07a94a | -15.89468 | -50.17736 | 2025-08-15 04:53:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6f9ba486-5dbb-3ff4-8401-016bb54caf6d | -15.39258 | -55.77834 | 2025-08-15 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 508b64f6-da34-3161-a435-c1fbf14bf902 | -19.47579 | -43.61674 | 2025-08-15 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf89df4-c416-3ac7-99cb-f7ad672ca623 | -18.69795 | -48.17761 | 2025-08-15 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7c0958c5-5a31-3734-b0b9-5a6239cd5c95 | -20.32456 | -45.22577 | 2025-08-15 04:53:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b3f2ef8e-a027-37d8-b19e-9d9c431a10e4 | -14.37618 | -53.36939 | 2025-08-15 04:53:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e567b23-cc1c-3668-adcc-5797d7040092 | -15.32803 | -51.51619 | 2025-08-15 04:53:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7317fae-deb6-3954-8777-aac38b20a670 | -16.47441 | -51.98526 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31376479-3429-3113-b94b-12abc3967b3e | -15.38453 | -59.81949 | 2025-08-15 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d2254fe2-9f3e-3722-97f4-e6a84d6d767a | -19.47242 | -43.61506 | 2025-08-15 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e7e467c-041a-3695-8680-070690f15ac3 | -16.60007 | -47.04536 | 2025-08-15 04:53:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27b38753-dc95-33c0-9db0-8714f3bf8eea | -19.5516 | -44.8436 | 2025-08-15 04:53:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3d76be4-d0d3-3f42-8828-0a61b898d878 | -17.5577 | -49.41609 | 2025-08-15 04:53:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8a25ac3-d986-34e4-8ffa-091e692b7473 | -15.39283 | -46.58568 | 2025-08-15 04:53:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93cd47d0-a8fc-395c-af0b-86ebe2794b1a | -16.38244 | -50.89401 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e2221a6-d90c-3557-922b-e1da1a0fac21 | -16.38737 | -50.91389 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfdcfe2a-e488-31ac-99af-2158620e798a | -16.38399 | -50.91048 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf0303f5-625d-3b00-80de-96f3034363ec | -16.31596 | -52.9201 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35eff034-6121-332e-a5f4-2fa4e52a16f6 | -16.47737 | -51.99022 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e497e9d9-cdd3-3fe3-9bb2-94baaa781709 | -16.3154 | -52.92387 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 745c7bc0-fcf2-3603-b6eb-bc144b3488fe | -17.64722 | -44.50524 | 2025-08-15 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23e75fe5-b58b-39de-a36b-b1a1fc44ad35 | -16.29934 | -52.91355 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521326e0-cef2-3526-95f9-be8758b0c26c | -16.37868 | -50.89333 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9b8981f-d35a-3f81-bed6-d85a357d13fb | -16.31652 | -52.91631 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa6157bc-db3e-3569-b50e-11289b738eed | -20.32415 | -45.23 | 2025-08-15 04:53:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a4e38309-eb17-3462-acea-0ee04c98409c | -18.00726 | -49.39405 | 2025-08-15 04:53:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbaa0b24-83dc-3936-93cc-9a0bd57a506e | -20.97609 | -47.41819 | 2025-08-15 04:53:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f035408d-76e3-31a7-b165-0695c94c1a71 | -16.30965 | -52.91518 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 162961c4-4a1b-3f27-92c0-22638d73cda3 | -15.92967 | -48.15961 | 2025-08-15 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2b93dce-8e42-345d-b41a-3d43e70b8a2c | -16.48094 | -51.99088 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddc1f1cd-6653-30b5-85d3-715a1c3e0e43 | -12.88705 | -62.093 | 2025-08-15 04:53:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57b0419f-79f8-34ef-abeb-261bae5b0935 | -18.94441 | -48.18159 | 2025-08-15 04:53:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1b9edeb-5e94-3f8f-a471-6cb298c5e9cc | -17.05646 | -51.79372 | 2025-08-15 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f2e4b89-e8de-383a-895a-2a5e4a7480fa | -16.39216 | -50.90712 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a398a31-7eed-3288-80aa-09d56cd560e3 | -15.32441 | -51.51565 | 2025-08-15 04:53:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad149f31-8d08-3fe5-b0b1-520614ff8517 | -19.55112 | -44.8416 | 2025-08-15 04:53:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95d07308-e5a6-3979-89b4-10b725b00f30 | -20.04707 | -47.75044 | 2025-08-15 04:53:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d842504-d28a-3c14-8465-a39d977efb03 | -15.59484 | -53.93857 | 2025-08-15 04:53:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a8ea18e-bf9b-3049-9998-b0452a5e5d65 | -16.31599 | -52.91574 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca7b4a1-7025-3cc9-9bd3-29204ea7f461 | -19.11796 | -44.47264 | 2025-08-15 04:53:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f92a6cb-a07b-36e0-8ce7-decc8d338c18 | -16.378 | -50.89819 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbb12efe-5b9d-3a5e-bc68-3e6668a065e1 | -19.67306 | -44.59972 | 2025-08-15 04:53:00 | NOAA-20 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c9180fa-821e-3608-abbe-1dceb088dffd | -16.90987 | -52.54938 | 2025-08-15 04:53:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7866a2e-8618-36a6-b10d-b3cabf6eb4a3 | -16.59586 | -47.03911 | 2025-08-15 04:53:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b2237ff-7764-3ce5-b925-ad7cb0443f1a | -15.17447 | -49.74208 | 2025-08-15 04:53:00 | NOAA-20 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b73541f-3d5c-3784-aa04-b926bd03a095 | -16.39179 | -50.90995 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bc77b8a-1860-3b3c-8a8e-0ea51e7759e2 | -15.89535 | -50.17242 | 2025-08-15 04:53:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ea23f708-223f-37f7-ab16-e2c64b868ce9 | -20.39604 | -45.39948 | 2025-08-15 04:53:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7cfe8f1-001d-37a3-b21f-b2fce30030c1 | -19.64202 | -46.09725 | 2025-08-15 04:53:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd18705a-1a17-3d18-8aa9-2c27ea7d0b58 | -14.50724 | -53.28897 | 2025-08-15 04:53:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a517e317-b02c-3046-93d8-dff86196ac4e | -17.49216 | -47.83929 | 2025-08-15 04:53:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f55f1a5-4603-35b2-a539-6077e4759b20 | -14.51733 | -53.24549 | 2025-08-15 04:53:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 774ff107-c644-36b4-8f69-b7044be8f946 | -19.47864 | -43.61636 | 2025-08-15 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69b9201c-5bbe-3334-83a0-43eed2fea7a6 | -16.39278 | -50.90255 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5888b710-d4c7-3c70-b2d9-2b7cb57c2076 | -15.39214 | -46.59138 | 2025-08-15 04:53:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb69c60-3bf7-330e-9cc1-73013d13c6b4 | -20.97576 | -47.42123 | 2025-08-15 04:53:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd3626df-5074-3236-b3a0-6f5e3abaa682 | -16.47145 | -51.98032 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d095acc-adbf-3b1c-804e-98b9892f4c35 | -15.66688 | -56.38119 | 2025-08-15 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9d3b04c-9d45-3758-85ff-d8afcdcd3ce5 | -16.30853 | -52.92275 | 2025-08-15 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fe1bc0c7-d6b6-31cc-978d-12830586d6f9 | -16.38715 | -50.91565 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9327eecf-cfd3-3a39-a436-57ec0b1e671d | -16.39243 | -50.90541 | 2025-08-15 04:53:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 466fec70-ed17-339f-ba45-693e7a8abf84 | -21.20651 | -46.69341 | 2025-08-15 04:53:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e31de41-f91d-3b07-8f03-1977302c4072 | -16.47796 | -51.98606 | 2025-08-15 04:53:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80054fd3-4010-3c8a-8ba3-a74259660a69 | -20.40098 | -45.40788 | 2025-08-15 04:53:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README53.md)
