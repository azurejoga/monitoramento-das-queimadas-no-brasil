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
| ba206d04-6610-3a7f-bcfd-434e678f1b09 | -12.18828 | -40.88427 | 2025-09-12 04:04:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6759564-d01e-36d4-a563-ee4edef367a5 | -9.34227 | -48.94635 | 2025-09-12 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26d96968-92d9-348c-bab7-966da34d0ee8 | -11.36956 | -43.51318 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6324a15-dfdb-30c5-83c2-9c9860c15491 | -9.71441 | -48.30659 | 2025-09-12 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79dcd482-a5b8-3f04-9a05-210ea238e242 | -8.95341 | -46.72432 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 709c4b6e-15e7-3363-a441-ecc7904e93f0 | -6.81922 | -45.65245 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d0f9497-9cb3-338e-8fc2-04646dee9639 | -8.89267 | -49.94368 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a26146ca-23b1-34bd-a6ef-7d05b87601e3 | -9.05986 | -47.0438 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0ca4c59f-302a-39aa-b69b-563f6efdd23e | -11.15439 | -45.31841 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66da7984-4ce7-3348-b0be-24da6431d83d | -10.21849 | -46.24792 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7cd2a407-a7e2-388c-8661-dd9f652301fc | -11.67016 | -46.61695 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 327776c6-dd90-35c8-82e2-8ee090cba14b | -6.30453 | -42.21632 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7ba017c1-8172-3889-8faf-f845b5c65fdb | -10.08191 | -50.39322 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dac75381-647a-3819-9fcf-b7e38dd20fcd | -9.00885 | -46.1189 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3d51610-87ab-3b4f-bdad-714a71ff4b97 | -6.161 | -47.27931 | 2025-09-12 04:04:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e25f2aaa-0b6e-35a8-9759-f37f1783a145 | -7.52268 | -44.68211 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8406c6e6-3a8a-3732-88d7-c5b4181cdf26 | -5.29029 | -48.1255 | 2025-09-12 04:04:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd366fd9-3151-3114-a3cf-874c73e8b590 | -6.26397 | -43.48943 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d51ab79c-eea0-3eef-9906-114e70582f5b | -6.47894 | -45.15512 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b6e725c-ab9b-3122-8f91-d0f0506e34c4 | -11.67712 | -46.56812 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6936546c-54ae-3dc2-8f7d-fb5eba33168a | -9.71328 | -46.88626 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2d9320f-656a-38e0-89ff-abcccd85d4f6 | -7.32311 | -44.36837 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76df9e70-aedf-3e94-9565-8dd1f61ab690 | -7.46924 | -45.29394 | 2025-09-12 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9f89027-a51e-315b-8f79-ebb6e82dafe3 | -10.539 | -51.53809 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f947d89-4495-31e7-9521-d6fcd81b4966 | -6.48012 | -45.1481 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb3db211-6da3-3233-be06-4ea7d98e5920 | -11.56637 | -43.23719 | 2025-09-12 04:04:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8125a6ab-3c58-35ec-8379-5255c0c5b5b7 | -6.28486 | -42.40471 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8d10e7e-9de2-3529-acc7-e5face176d01 | -6.5439 | -43.10889 | 2025-09-12 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ddbf205-6422-309a-a510-e34703de83d0 | -6.18197 | -42.74539 | 2025-09-12 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4345d022-1314-3f54-9638-ff14a3219a88 | -11.67848 | -46.59453 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d630904e-8e8c-3b00-be61-634a5c6fd4a7 | -7.21843 | -43.98024 | 2025-09-12 04:04:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 723fe285-77a8-3008-9b5d-9edf8086b4dc | -7.55911 | -44.39277 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7027b824-e260-355a-9bd0-ebf6a67e67ac | -8.41011 | -44.76452 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a8de066-0165-3d63-a3ab-9a6edc057a4c | -5.82877 | -45.27156 | 2025-09-12 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3784549d-a0cd-3a76-962b-687c967fd64a | -9.84744 | -43.54467 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d90b7ad4-25d2-3bf9-8d48-055b0657490b | -11.70425 | -46.49857 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d8fe0b2-3959-3b38-bfd8-494dd9d42655 | -7.51486 | -44.68073 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efc7e20a-5ea3-32b9-a17f-1a0910fe5d9e | -11.14878 | -45.23717 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 908c985b-b341-3275-b9c0-091fd0636fc9 | -6.10037 | -45.94146 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c55d205-97ad-365e-800d-a7ce1edd391b | -10.70658 | -48.62207 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f875067-61c6-39ca-8750-af074a8046cb | -6.49 | -43.8748 | 2025-09-12 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23060799-2017-3ba2-90f3-c4db8428c9f2 | -10.4292 | -50.62137 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d1792b9-6630-38f9-89d8-8211cd34977d | -8.89876 | -49.94121 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 683cef52-4283-3f2c-82be-5aaa6247deb6 | -7.85085 | -46.06661 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 766d577e-68dc-3f1b-ae3d-30f43fc51eb7 | -7.17856 | -44.87228 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 01730254-9d3f-36a4-aa61-669c6828a275 | -10.53179 | -51.51974 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd701c21-d606-3e28-8741-4ceb21acd683 | -11.67494 | -46.56684 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eeda6ab8-0c2b-309c-847f-aae7d2e94538 | -6.82827 | -45.65016 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 482b5a56-f2f7-31a8-bdfc-74a484347b9c | -6.68086 | -44.1507 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bc5baed-af9c-320c-8fc3-13363e324c64 | -10.53601 | -51.52936 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71f7f6f0-30b0-3b30-8a46-bb5436e1e24f | -7.07898 | -44.1449 | 2025-09-12 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14169aff-ecf8-3842-86db-84b589803a46 | -6.49632 | -44.49773 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c6ae330-da47-335b-b68e-a25b2728a157 | -7.69636 | -44.69635 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0acaacc9-1867-32b7-9c40-412a5f49f1c5 | -7.97881 | -43.66244 | 2025-09-12 04:04:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8846d90e-e583-354f-9e6c-27d565dea291 | -7.40105 | -44.35905 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43acf0bc-368c-3666-9ba6-5c714baf073e | -8.95077 | -46.10514 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 518431a5-5c24-3755-a81b-84bc710fb56c | -8.43526 | -47.25866 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9e134b3-0522-325c-9310-fb765286d0fc | -6.25328 | -43.4311 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f22624ea-23b0-3128-a051-cfaf975bdb2e | -5.49797 | -42.67958 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4150b624-606c-3d53-a594-ed2b796434fd | -12.18772 | -40.8878 | 2025-09-12 04:04:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09c5f09e-9ea6-3678-925a-6260cb58220d | -11.68368 | -46.53019 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa578e3c-dd4a-3a26-8996-313a930341c4 | -9.15845 | -45.56083 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68d8d492-c504-31b2-9216-fc67004340c0 | -6.65559 | -44.13654 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aba89397-c9fd-3cfb-b99e-5e81b78fd3bc | -11.41525 | -43.7123 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32e388b3-5544-30d3-9188-f86008a24ae3 | -11.67647 | -46.57187 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 022e30d7-eee3-317c-95cb-ba8548d9a2b6 | -7.85016 | -46.07068 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 732555c5-b9c1-383b-ab85-7bd1d5681e91 | -6.82473 | -52.79222 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac104db2-7953-3510-98be-2c3a53943252 | -4.4861 | -48.11358 | 2025-09-12 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ffb62570-3c53-3508-9c86-5b924f1021b4 | -7.07441 | -44.14885 | 2025-09-12 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93a8bc83-0cf4-328e-89c0-683714d07435 | -10.85903 | -44.79041 | 2025-09-12 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4afe78b0-7cc8-3224-b414-33d4256d809d | -10.78685 | -47.26105 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dfeccd1-ff20-3e8a-bbc3-8239295f2bfe | -6.89389 | -44.34678 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 069f0368-fb46-3fba-8c65-0fd1f1c98072 | -8.94855 | -46.09321 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8f6c840-ab1a-3ed3-8193-9a94b7e1235f | -6.08487 | -44.82523 | 2025-09-12 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff8c35e7-13b5-3b0a-9aca-06f7d37353b7 | -9.03801 | -47.11582 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4800844-4e4d-3569-9156-ea3da265875e | -8.42695 | -47.25241 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2747aaa7-7ed2-33d7-82ca-3a3fb7118f4e | -12.021 | -43.78687 | 2025-09-12 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9e79ca1-9e97-38c7-bce7-175e1941ed00 | -7.73894 | -47.42283 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 203eba79-2c24-3d40-9f09-9afee212fa51 | -9.6653 | -47.55274 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e172952-57d9-317e-af8b-d56f0c0490fd | -9.09048 | -47.07932 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29a8c961-58d4-31de-b445-3267717c4721 | -10.08047 | -48.17673 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 015184fb-26a6-38a7-82ce-4449a2bad7cd | -9.11103 | -46.96017 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3580cc70-6d2d-3591-afa2-aa258588d0c3 | -8.18442 | -46.10682 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dea77691-0a3c-364a-bfde-8e2fbee9bb0b | -7.54598 | -44.40038 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1044d570-d3f5-35fc-a169-93de075298b1 | -8.34594 | -47.58805 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7cab417-a73c-3900-98f6-c9f5c7a0bce2 | -3.60309 | -51.53259 | 2025-09-12 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a340d386-b89b-3839-aaac-75fe3448e257 | -10.13452 | -47.91487 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cea7d17-caf9-3552-b892-4b042babaa04 | -10.55234 | -51.53186 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45c15398-da64-32f9-ae83-d65ea380d0ea | -8.37284 | -44.84395 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef2847fc-ef07-32a7-a642-bbb9246b7a51 | -5.75887 | -52.37635 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 126d12fa-9a68-39e7-98a2-62abaa6923e0 | -11.67355 | -46.55094 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 139f154c-6d0c-344f-81b4-bf7914c606d0 | -6.59199 | -41.45176 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8742f002-df23-3c3b-aa6b-3d8a8524f5cd | -10.22076 | -46.24389 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b481e681-6bb5-3511-a2ae-4a12f46323f6 | -10.41775 | -50.62135 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a40ceaa-d8b2-3b4c-8820-55af435a1edd | -4.48092 | -48.11272 | 2025-09-12 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fff6946a-15f2-36ef-a90e-85eba504932b | -10.09286 | -50.39534 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb8aec98-5985-371d-ba21-e8b94fa5bd5e | -6.42133 | -44.51099 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86d80e8b-0a92-30d4-b1e7-82664bae930c | -12.10245 | -44.87348 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a15cb70a-cac1-36a8-bac1-6c76b539f169 | -7.32232 | -44.37304 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| da097f20-9078-34cb-ad0b-e742ce17f883 | -11.67222 | -46.58189 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README32.md)
