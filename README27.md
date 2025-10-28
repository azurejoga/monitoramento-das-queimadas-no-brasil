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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae1acdb8-a01a-38cd-bbf9-269e2386b05a | -6.56062 | -41.59689 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4fc8fb31-78a3-3462-a9ae-e8182cf98650 | -9.56402 | -46.97545 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d6e253f0-1185-344e-a951-515ea43d7b0a | -7.35228 | -42.46458 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 779a2ecd-e4ba-34fd-adfa-49ec64ff4b6a | -10.93072 | -50.27304 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0313702e-8049-3eea-8152-47e964ca67f6 | -5.83891 | -47.65119 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 697a9dd8-6d13-308e-be7d-75fb526e852d | -7.84213 | -46.41101 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b0df6bf-41a8-36a4-afba-6c7bf70e0909 | -4.85529 | -50.67787 | 2025-10-28 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70b0d1c2-2cb7-3d0d-9186-7eca0caa7bc2 | -6.38588 | -45.7655 | 2025-10-28 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6c048cc-44f2-320b-9a67-89fcc38d149f | -13.55586 | -44.2639 | 2025-10-28 04:14:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8284b922-98b0-3515-b80e-81b2b3b5d5ef | -7.83719 | -46.41878 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89f959f0-8c9c-3660-8257-7b871de0437e | -10.35114 | -47.70789 | 2025-10-28 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bc69f94-c2ab-36e0-83c3-ac9d4faaab12 | -11.36209 | -46.09022 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6da32242-a80b-3588-aa4b-a53ad83f1a82 | -9.27504 | -46.3943 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96268f31-98ac-30dd-9637-c250d0e0358e | -9.25123 | -45.5623 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89477de4-614c-3c65-a072-c3d82681e7a4 | -9.3598 | -43.59806 | 2025-10-28 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e884b559-ae6c-384f-9e21-72696e6fcec9 | -7.47313 | -47.1513 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 351b1564-626a-3f30-a53a-cc3fe03f1a0d | -5.64837 | -47.63572 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23237ca0-de58-3dc5-939a-09af066b9b9d | -10.56514 | -49.83333 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d055310-99e1-3ef8-bf9b-a2d62b259f0b | -8.56577 | -47.01429 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb4a738a-670b-3262-8827-77e506eebb68 | -6.12396 | -42.44595 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 32b4f36b-ad50-3bcc-bbbb-bdfd158c1ffb | -8.32188 | -46.8311 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5654db2a-d2ed-3410-8c13-a596581ed094 | -7.07645 | -44.94829 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4eaca647-22c9-3a96-ad92-28e295d35855 | -10.75979 | -44.75549 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e8addd3-8219-3d9f-9366-dece88a11d25 | -7.81586 | -46.43663 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6794b9f9-8cf2-3e4d-9182-e553d492f03c | -7.41559 | -43.95171 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9748f379-1947-38d4-bd1b-2af339958a8c | -12.7087 | -46.34831 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30f6dc4b-43d6-3333-89ef-50554ced5393 | -6.03538 | -46.55723 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee10c715-b06b-3eb1-9973-11958708cfde | -8.15052 | -47.005 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20bc5e59-8478-3016-b274-6898b967f785 | -13.53842 | -44.13376 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e3b6b54-7a43-3882-a581-cfc1f6cc89a5 | -6.89239 | -46.36395 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdce1b5e-fac3-3b6c-89d0-1e5c3206c173 | -7.47688 | -47.15191 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24268d96-d4a7-39b2-afa5-d08e1f14128d | -12.20179 | -46.50262 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bdc783b-9845-3d33-a337-554230cfe64b | -8.56799 | -47.02356 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6edeb796-d436-30ff-a035-a21fde3077be | -6.27113 | -42.72048 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c8a95279-dcb1-3ba8-bc9f-75916940a14e | -7.76092 | -45.38969 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d298d47-5400-3bc4-8497-5fbc40057858 | -7.54998 | -46.24422 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9197849-dec0-34bf-adfe-f785c72595ad | -7.94611 | -45.50437 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c3b5f57-3049-3c6e-82d2-9b3d4717322a | -7.38851 | -45.12719 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c8ef4d3-f45a-3a5b-b8d2-06648b39e37d | -11.74657 | -50.21878 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1a09cdf-1bcd-3ea6-9fb7-e83b37fb4f27 | -11.30721 | -45.35276 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1535d75a-5f53-34dd-b019-c70187c5920f | -10.94878 | -50.27194 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fa07cdb-9f4d-39f2-8650-8df36870d41a | -7.49628 | -47.03429 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd36f3bd-876a-36e6-922e-acb70a4836c6 | -9.57312 | -47.89736 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e0f24fe-d6be-3756-95c0-351cd183c87c | -10.58489 | -49.77125 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 7e45eeab-d17b-3254-86b9-ddfe300cedbe | -11.26824 | -45.04559 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b8100cf-8fcc-3a56-825c-e9910cdd98ab | -8.16386 | -42.82432 | 2025-10-28 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0cf93a07-88fa-3a51-8099-4ac08c4348c7 | -6.9812 | -39.12293 | 2025-10-28 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5436deb7-21cf-3f40-bba8-bd340ddc96b3 | -10.29662 | -47.17772 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 181d47fe-b203-3d1b-afa4-aae4b2f6b993 | -11.71405 | -44.44633 | 2025-10-28 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6449755b-4cc4-3acc-9459-e06da95387e8 | -9.56694 | -46.98027 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df29902c-6ad8-32de-8706-67f97ca95f04 | -6.46372 | -43.18888 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cab503c-4b51-3be2-a0a3-0b5da6f57a37 | -7.00113 | -46.99329 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8d820b7-71d1-3a14-a271-2b77029e359d | -6.48747 | -42.2292 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9fb620f1-f02b-38ca-8b32-1d3b99f74808 | -13.55201 | -44.26689 | 2025-10-28 04:14:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5744422b-922b-34cb-8f27-bdc2f8f25f32 | -7.97507 | -46.28556 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cad6c0ed-a1c8-3678-9f79-f02abdf9144f | -8.57389 | -47.03344 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89dc1fc9-4e17-3a36-b40a-b6feebcb4b41 | -7.96592 | -45.53479 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3829b999-7b3c-3056-8113-0b7ab92f7b3c | -6.16456 | -43.099 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7effdd64-494a-32f2-b6d2-d2edf458304d | -12.47528 | -44.49508 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b217712-9bd6-3c0f-b253-4c1ccb49a053 | -11.15042 | -44.63162 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55daaf5d-47ee-3e8a-83ee-4c680836b606 | -12.19119 | -43.58773 | 2025-10-28 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e30388b-4441-3e54-86a5-c816c840f547 | -7.97377 | -46.73363 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adb2eb98-c43d-38fe-966c-09d90ac3101a | -7.35488 | -47.64879 | 2025-10-28 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7e17e61-f3db-3008-8d8b-63778cc83d80 | -9.95795 | -47.11538 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8f17a649-9f3f-34ab-b372-1cd75472e506 | -7.81789 | -46.42422 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 286ea4c7-3c29-3ace-a0fb-b698b9f79eda | -10.56447 | -49.81264 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3252b0f-fdad-3615-81eb-a4ce5d1923fd | -12.22446 | -46.49059 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52b6b6e8-c27d-326e-b7bd-8786394313f8 | -9.53871 | -46.97135 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bc90120-87ea-3a6e-af11-dc3510946f7b | -10.30541 | -47.21439 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06d66de4-47b6-3b61-8294-80cf666674c7 | -7.40616 | -41.98254 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10b8c89c-be0b-3bce-995b-1ac9a01140b5 | -10.56067 | -49.7841 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 68baf037-4985-3f35-ad4a-18d48e13c2c2 | -11.75804 | -44.23091 | 2025-10-28 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 945ef33a-e5e2-3c9a-9b6f-594ff05ee11c | -7.00271 | -46.99158 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a27d747-5af3-3208-baed-6fbefc70c746 | -7.97026 | -38.28081 | 2025-10-28 04:14:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c3157bf1-4faa-3c04-b033-5d69f247ea4b | -7.18785 | -39.67333 | 2025-10-28 04:14:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb7bff8b-fdf6-3878-bcce-cf9514d6da85 | -8.64697 | -45.25616 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f627ab4d-ecba-323a-ae1e-48d29f829c8f | -8.19211 | -44.44044 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 229bcb42-ea85-3a29-a410-1a39fd2bd418 | -12.80707 | -47.56399 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 441ed304-392e-31ec-b85a-4c855e570b7e | -7.92524 | -49.73827 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e80a273c-721e-3d5b-b72b-b638d4ad4c64 | -8.18494 | -48.17698 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3a84274-25e8-30bf-881d-5f198375f3e3 | -12.08677 | -45.65255 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4990a9fe-05bc-3271-8779-a940af60aa8a | -7.31247 | -44.10756 | 2025-10-28 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eba1f0e7-d96e-3146-bade-4ffd30fe926e | -9.8873 | -44.88942 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d99c6608-5fe2-3eaa-9bf7-6269eda87677 | -8.18099 | -48.17632 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95fa379b-2b9c-3362-80cf-f57904bf748b | -7.92964 | -49.73898 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebc55fb5-f94e-3742-aa30-a618d15ab5e3 | -7.26711 | -45.00941 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1039b198-7172-3a94-8987-b7e283641e7a | -7.97881 | -46.72569 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3cd1a35-a6f1-33df-8f48-fd0004e9c774 | -9.97112 | -47.17043 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03671b81-6fe9-312b-9a37-dfde09cd59c1 | -6.92053 | -43.48793 | 2025-10-28 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad2b9788-3183-3141-808f-5db9f7ffad3f | -7.34641 | -46.9143 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89396c64-2bb3-325c-846b-21fc170a45fb | -11.90934 | -43.82787 | 2025-10-28 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97b6c609-a971-36e7-9cd3-56b7e8186fd3 | -7.79138 | -40.41631 | 2025-10-28 04:14:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e926ee44-f2f4-3e86-8812-0d973a1b7e79 | -5.3049 | -48.26926 | 2025-10-28 04:14:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cf3a884-d795-39b3-975e-9c2e4e7129b9 | -10.12612 | -47.70551 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3da21ad9-fae0-3344-96e5-70a34d5288da | -10.92282 | -50.2673 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76d8e06c-15b4-3485-9120-3b8d37ab81c9 | -12.705 | -46.32825 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb866ff5-eede-3f01-850d-b1e33f94cf1a | -5.44218 | -47.39603 | 2025-10-28 04:14:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fc1f069-a0c1-38de-99ba-8729ff46f6cc | -6.89363 | -46.36368 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca831cd-5f2f-3cf1-9857-77e7e03302c3 | -7.85621 | -46.39221 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e7d835a-f022-3af8-9e97-236bebc9d154 | -9.39148 | -47.70285 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
