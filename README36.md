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
| 0ac608df-590b-3e9e-8923-8eb3bcbe05a5 | -6.17141 | -46.10819 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2a3209f-bd84-3e61-9d71-8246ae3da9a9 | -8.04437 | -41.11241 | 2025-10-29 04:23:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2ccee68-f7de-3f44-a34a-ce672b82577b | -6.90935 | -42.86423 | 2025-10-29 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 766bb3b3-a695-3e85-8603-73ad5fefaf56 | -10.56371 | -49.83411 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c899b95-2750-3f90-ada6-84620e16c79f | -8.84134 | -46.92984 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92a826b1-9923-31f1-82ed-041963e9c5fb | -7.78663 | -46.46975 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5d1a072-0620-3869-beb7-7f1fe37593ae | -9.71816 | -45.40324 | 2025-10-29 04:23:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7141bcc9-a5af-38f1-ae08-a57c2cf67f7b | -10.84758 | -47.88654 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 484117eb-5a5d-3344-af10-a47da6c65978 | -7.42565 | -41.85948 | 2025-10-29 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 09cd868f-e9a9-318c-8fdd-2ea42c090884 | -10.94269 | -47.62583 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ce32459-1c83-355c-a710-bd1b3677e7e1 | -6.13008 | -41.83738 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5eb10ff3-2c5c-34b5-9a61-a30e00692122 | -8.56474 | -45.76275 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0e2dfea-ac97-312f-85f6-d55f52c6100f | -6.77364 | -46.38254 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15cbfacf-a964-3ef1-a40f-924cd3327f70 | -5.33221 | -45.43443 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dac9063e-afa8-318a-b6d7-f53cc25dad6f | -9.87759 | -44.88187 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36c41365-35de-33c1-9387-5a4941eca61a | -10.88062 | -47.99815 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d867659-8634-3e55-a4a4-61c1feb91b60 | -7.43969 | -45.1147 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c438dc6d-0931-3eac-8745-2845b19084f1 | -9.1651 | -46.28659 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40954494-8dcd-37dc-b495-3b262c4c7aff | -6.23021 | -42.53259 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4e16c56-8325-3b2f-9711-06761432eb9b | -8.02791 | -47.41988 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6887af43-79da-341f-90c9-04efa062b8a7 | -6.14479 | -41.6835 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d52f447-f936-3079-87aa-09ff276d3af5 | -6.88532 | -45.048 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20576a4a-7082-345e-8c59-277c423d35f4 | -7.94788 | -45.46755 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 78bfeb72-8d34-3d27-9471-9b76fd09ad0d | -7.41958 | -41.87541 | 2025-10-29 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4db37a85-10de-3924-926d-774046a68e61 | -6.23368 | -42.53312 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68d0864b-d7e1-341f-8183-35995071adb7 | -9.13659 | -51.2998 | 2025-10-29 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac2431a7-4f00-3581-8d19-2cf7e05bc3d5 | -9.49383 | -46.99846 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc2b8a53-8921-3bc6-aa61-3fe75ccbad19 | -8.05068 | -45.03401 | 2025-10-29 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04ef66ac-dac6-3dd5-8c26-31fc5da33427 | -10.62281 | -47.84992 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 102981da-12ef-3158-8fc4-0134977b1a10 | -5.60921 | -47.11309 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7e98ec4-db20-3e85-a5a8-f648db59f3d9 | -5.85899 | -47.70068 | 2025-10-29 04:23:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc17b1d1-4726-358b-9c09-bf77950a7149 | -4.84789 | -47.53689 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e886591-98c6-3208-8cc4-0ffccba28b8d | -10.38002 | -47.56576 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3108d111-b840-3900-9686-ac0bedb08b5b | -9.21483 | -44.53802 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 575b21dd-10fc-322b-9d38-90e482b8243a | -7.20084 | -44.15901 | 2025-10-29 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cda0489-b182-3fa8-a18d-09ecedd0a5d6 | -9.89818 | -44.90324 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58a568fc-f99f-3347-a767-4cde64778f5e | -6.64684 | -41.5183 | 2025-10-29 04:23:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 727e8ada-0810-384b-be83-6a174652e9e8 | -8.03389 | -47.40508 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1118fe8f-c959-3757-9511-366e0b9ca637 | -11.33988 | -41.67116 | 2025-10-29 04:23:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 133dfa6b-7958-3755-a615-b1c3c21683c2 | -7.95677 | -45.45462 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d1d392b-5747-3427-9e1b-f06b0070aa36 | -8.61598 | -44.79781 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2343afd6-c189-37da-a248-016e0b789593 | -7.43914 | -45.11818 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c34c92dc-2143-3651-a1c4-c0bac9de546e | -8.90121 | -48.02135 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebf3fc21-d79c-36bd-8083-3ca37e1ba9b2 | -10.36841 | -47.14087 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24fccfa3-3745-3c80-8f29-37d78cbd1657 | -10.56571 | -49.83671 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b27d4e09-d68c-39d3-8609-8b74b5ff7159 | -7.64023 | -46.92177 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45ee8ade-8a0b-39cc-afd4-a03db8dbb652 | -10.65626 | -47.90621 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60ea55f5-4022-34df-94f3-11512e9518ad | -6.95708 | -47.74264 | 2025-10-29 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76cc2814-a796-39e0-b2e6-f53a97fd6fb8 | -6.54094 | -42.87747 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cea8a73f-d42b-354a-b863-b528355d6801 | -6.48946 | -42.24748 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 12e9d975-0508-3afd-ad45-9ffdc325f4cd | -10.87368 | -48.62608 | 2025-10-29 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cf26ca8-9eb5-34e0-96c8-fb6eb2331925 | -7.03597 | -39.48087 | 2025-10-29 04:23:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17dcde9a-0de0-3286-b33c-cf7c2674330c | -6.28087 | -45.31514 | 2025-10-29 04:23:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd71988f-442b-39ce-b05b-d66a86eca01c | -9.4977 | -46.93151 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc8be7e7-a393-329c-9928-4513848223d4 | -6.54151 | -42.87376 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee102b07-6f11-37b9-9262-9f018ca135e6 | -9.90152 | -44.90377 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88a90096-8c44-3404-87cc-210ea1c0f63c | -10.37186 | -47.14483 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70fa3ba4-b473-39e7-bb53-12791209470f | -5.4164 | -45.21799 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7622866f-8c03-3a92-82c3-7a5b026eb495 | -6.72265 | -43.57655 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7de52b85-4822-395d-8cdb-b966a05ee734 | -6.98647 | -44.01401 | 2025-10-29 04:23:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7be5bb12-5671-3a16-bbb7-aa323b7f1a96 | -8.83733 | -46.933 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b215b306-7109-3e1c-87dd-6ca6fc3fd81d | -7.27868 | -44.0991 | 2025-10-29 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 321263dd-3697-33a1-9046-db704fc8d9c4 | -5.59084 | -51.12825 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a03f60e2-3cb4-30b5-9201-f26e2d0cd34f | -6.52203 | -44.56359 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18cbfbdc-7605-3fe3-8d90-0fb397e15841 | -10.92103 | -47.61108 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db9609a4-b080-3394-b7d7-131b8ab633f3 | -8.61876 | -44.80183 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5305b115-5aff-3a4c-a522-f0f746443c75 | -11.18523 | -45.2162 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe2566f0-9318-34ef-afea-bc7e5c0cafdb | -5.65491 | -46.45185 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11d1b919-a01f-3abf-9113-357da9c6c5cd | -6.0874 | -42.14403 | 2025-10-29 04:23:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a689606c-33fc-3919-a1b5-6cc5f946e4bf | -5.59082 | -49.07223 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b04d2853-0e3a-3022-aa0b-4b3503a26640 | -6.472 | -43.39128 | 2025-10-29 04:23:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e480ca85-8ca6-3524-9d99-14dd02cbba1f | -9.89371 | -44.88807 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 703ae271-ea9f-37f6-b52b-8fe3dbb549d9 | -8.86053 | -49.06615 | 2025-10-29 04:23:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1ac8878-5baa-3abb-9afb-56b6f7858694 | -11.15174 | -44.93365 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7c74401-58ce-3024-b6ac-64a184e667f5 | -6.2424 | -42.56895 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e2c2705-aecf-310a-aeb4-af2563f167d5 | -10.64679 | -48.00758 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 764e2cbb-2027-314a-80f7-27a6492e3334 | -10.38404 | -47.11304 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2b19fe2-8716-370d-a338-66dcf71f3860 | -7.43919 | -46.60857 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbc41362-8d19-31a1-86f2-816021bdf359 | -10.65155 | -48.00035 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7388d0ec-36bc-3222-99c4-235333e84f93 | -6.33595 | -46.41088 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6887099c-c236-3b3f-a0a5-75476b7216fa | -6.65094 | -43.60987 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e334b97-04f3-3a8c-aa94-131e6c884f74 | -6.10301 | -42.43938 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 73e3bbd1-4a20-3f2b-876b-d2504e5c5104 | -9.51111 | -46.9562 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 856b60e9-7c44-3297-b9d3-2c4776be51ef | -7.06903 | -45.21244 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4115e1b-140b-3464-a41d-b6e8b4177a5d | -7.79575 | -46.45634 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6be5068e-c036-32cc-a76e-a86d4edf9496 | -6.49307 | -42.24689 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cdc2a5e8-7d9a-3a0a-b604-27b0c04436ef | -10.95889 | -47.61303 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0416229f-e691-3719-8e2c-6f46fe47ec33 | -10.22548 | -45.94105 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39c8aaac-a024-3710-9252-b80a91cc80ae | -5.42781 | -46.34344 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c4c7c8a-1134-3120-81bf-69cd93043742 | -10.52568 | -47.74021 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b42db93e-6743-3045-94a9-277e61b09994 | -10.56672 | -49.83952 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0b778c3c-c1f0-3753-b7ff-02f8f9c23a66 | -7.96033 | -46.75601 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2115462c-cc78-3adf-8e76-ec443754789e | -11.11488 | -44.02152 | 2025-10-29 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6efa8182-43c7-3798-8d17-93c057fd97e1 | -6.11021 | -41.74091 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7f9742f6-731e-3dcb-ae46-daefaadaf461 | -7.74854 | -44.71833 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbcb8f98-bc14-3c5c-a0d4-b1e644aa4833 | -7.49336 | -47.04547 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfa9b7a4-d22a-3538-8037-2b2130a10f82 | -6.53948 | -43.56295 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b93ef86a-ec82-37e8-b536-0d4f81c2b364 | -7.79693 | -46.44909 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c4aeac8-b075-3017-a852-b45739e708a1 | -7.28346 | -46.89883 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 695dc229-0c62-38fb-81c6-b2c19516382a | -6.13478 | -41.85463 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README37.md)
