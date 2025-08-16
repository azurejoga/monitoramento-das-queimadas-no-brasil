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
| 8774b2c0-4531-3714-aac0-10129c2def2e | -12.56001 | -46.95229 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 57012205-7217-3d2e-b543-331de6ebb69b | -13.60805 | -46.91659 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef1733cf-07ee-3389-a7ce-9b7734aea9de | -6.94166 | -44.56535 | 2025-08-16 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab7ad310-cb52-3044-ba81-d52df0d18840 | -6.60851 | -42.75322 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bb697f63-3db0-3476-a722-cf29de8ef840 | -12.04605 | -45.7676 | 2025-08-16 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1783ded-3f8b-3ada-bc46-cf7f7d17b854 | -8.1882 | -45.02538 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9946f11f-a8a8-34cb-9d7f-0bb28ee75014 | -13.6127 | -46.91217 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fb9cb74-943e-3532-a765-f17cd9fc41c9 | -13.61968 | -46.9159 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c79b7cbc-ccbf-3187-862b-199cbfc51721 | -13.61358 | -46.90721 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| abc5b3ca-89ba-387a-bacf-356f7bd3c04b | -9.19783 | -45.33038 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc295358-a4e5-3c8f-a562-22e4d9a58810 | -11.35484 | -55.41991 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a6c63d5-6709-36eb-be7b-6adc1bab5cf3 | -12.82814 | -46.00645 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57126f3c-7835-31b8-9ca3-de22be23e88c | -10.92529 | -43.74432 | 2025-08-16 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08ae33fb-378d-3215-9a79-fe9fa47fcbd9 | -6.56291 | -43.03942 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf363bba-5948-3289-8e1d-d9d88f81efb1 | -12.49229 | -47.50018 | 2025-08-16 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e643234b-a58c-3d2e-9ef3-053b63f1286e | -12.79662 | -45.96782 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aff1797-2470-3230-91b8-96876030c6df | -12.25666 | -44.58205 | 2025-08-16 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5c69bbb-1f36-3b6b-98c2-bbf4be4c7774 | -13.60891 | -46.91174 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 297f3007-488d-394e-8f5b-f063a620738e | -12.40886 | -47.78716 | 2025-08-16 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3820ce3-4eef-3fdc-bfb2-6f1adc3791dd | -6.60908 | -42.74963 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 77f93a23-3c89-30fc-a286-10c25629a867 | -12.52827 | -46.96497 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e45ef923-4091-36b5-b6b9-152b6e774c1d | -10.35867 | -49.92735 | 2025-08-16 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 244b5cc9-9173-3afa-a899-4abdb2bd13db | -12.59754 | -46.93948 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4fc66af7-f20c-3659-8cf1-176f418b2810 | -12.81156 | -45.99481 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97aeeff7-0b3f-3f7f-9025-fe75968f195c | -6.5595 | -43.03888 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 087fb495-b398-3496-8b52-968137258b10 | -8.18117 | -45.02135 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d02b6db8-6b76-376a-be0f-db198f962dd0 | -6.95805 | -42.86395 | 2025-08-16 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c673e565-c169-3f26-bfd9-7834db7bb40e | -12.56671 | -46.9589 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8b4bb0cf-fcfe-34d7-bfcb-77c1bafee1ce | -7.66361 | -42.22509 | 2025-08-16 04:10:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9bad48ee-0b22-3bcb-a794-cc3f849eacc8 | -12.45048 | -47.00521 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0e8367c-4483-3370-89cc-94ea307ebc07 | -11.35767 | -55.4396 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eae0f0d-8489-319a-9801-819a5e995790 | -6.61074 | -42.76809 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8a4f4e9e-c4d3-33ec-ad26-8df563397247 | -8.17684 | -45.02499 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9bfede2-e2aa-3d45-85ce-31db156b5ea6 | -9.17961 | -45.32725 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73be9dc9-3635-3f3f-b07d-9726f11131b0 | -6.93805 | -44.5648 | 2025-08-16 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eb81eb4-bfc7-35de-935b-deab90722b4a | -6.55328 | -43.03414 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 39d3bf79-1e1a-350a-a840-4f549f897b7f | -12.80074 | -45.97137 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0edeecd3-d331-3547-938e-9418dea5dded | -12.43277 | -44.70078 | 2025-08-16 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 843cd5a7-7a9e-3491-927d-104c274be2f8 | -13.42744 | -43.68089 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1aa852dd-c031-3d20-8894-2ec865116cdb | -11.5053 | -47.24466 | 2025-08-16 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1880cc4e-14f1-3224-9e76-d85332bb6130 | -6.55386 | -43.03049 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fe922849-5910-33dc-82b3-7ffbb7f9cbba | -13.65154 | -46.93291 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6e2c7bd-6073-32cd-a378-cd4bf0b5a98a | -13.87296 | -45.55709 | 2025-08-16 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6cad147-0337-342f-841f-34d22375879b | -9.36427 | -47.98252 | 2025-08-16 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc90eb1-29fb-389e-9dd9-c26c7bff4e45 | -6.54211 | -44.54296 | 2025-08-16 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab7c9f65-c8ed-3df4-995a-483432259f09 | -8.19158 | -42.26622 | 2025-08-16 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 870c49c4-b786-367f-aa5a-df080780762c | -13.57181 | -46.96972 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 548160c2-6708-379a-bc3c-18d5ede5da14 | -6.54132 | -43.04343 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 077cc4e8-e56d-349c-bc89-6ef1f1579812 | -9.69987 | -46.26312 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa85b9da-b223-3091-afbd-fb61ff1d05da | -7.59088 | -45.16038 | 2025-08-16 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0af5bf7-a3fb-3f4b-9d0f-8da374a2f6bf | -6.92344 | -44.16873 | 2025-08-16 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d297fb26-9177-366d-a374-dd9cbd396c42 | -13.42468 | -43.67676 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7a6393e8-8337-3054-b7fc-194bd033568d | -11.65972 | -51.6292 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0c00c8d-fa96-3a86-b750-bf228f3772ca | -5.93317 | -53.65478 | 2025-08-16 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d62d7ad4-eb7d-3b39-a964-e309ea32d76f | -10.45618 | -48.81057 | 2025-08-16 04:10:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09b8733b-7654-3fb9-905a-a6387ea8751f | -7.0132 | -44.32067 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a2242f7-bef8-3cc8-a4d9-604c54ed8acf | -6.56784 | -43.03242 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7529c25a-5386-3a6c-8d60-1ccbfb49a60f | -12.5923 | -46.92445 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5680bf94-8b93-31e4-9dd3-6db175c94f6c | -12.56547 | -46.94351 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2f68e9b-b909-355c-9aba-974e070217d5 | -6.51392 | -44.21828 | 2025-08-16 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92d0aaba-06f3-3b2b-83fb-f2a00b98f8fb | -12.82454 | -46.02752 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3999f625-5271-3c2f-a843-168a698c7e8d | -10.96686 | -49.57293 | 2025-08-16 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9ef81377-aa60-3571-a09b-67da23d3110b | -6.56689 | -43.03631 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57f84c56-92b3-39ce-91c5-ac3681664a25 | -6.55785 | -43.02739 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99270fe8-11ba-358f-8322-f8ddc300a1e9 | -6.60793 | -42.75681 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f1027647-2c66-389c-9b9a-5aa12a615032 | -12.45512 | -47.00123 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b79d8bb-bdf9-3f66-a502-6efca600c762 | -7.1504 | -44.38812 | 2025-08-16 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd78231b-40a1-3a97-bc56-a335788281b5 | -11.34779 | -55.40641 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af438ba8-f5c2-3029-a49b-c0eaf1239de8 | -8.1957 | -45.02377 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a366580-37a7-38e2-9a5a-3a59da30fce4 | -11.34438 | -55.43682 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ecf721f-db67-38f3-b83e-cb119a81d2dd | -12.57385 | -46.94042 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6dcc670b-30e6-3683-8624-062dd0186bdc | -12.2607 | -44.57888 | 2025-08-16 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97eabd61-c293-3c4a-8c08-f0e3ea85fe46 | -11.91082 | -43.43381 | 2025-08-16 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 675ee871-ed0e-3024-a603-0aa63c7f05f3 | -12.80939 | -45.98582 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb0d8355-1989-3945-b201-810cf4dee269 | -5.93571 | -53.65181 | 2025-08-16 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25535b49-2233-370c-b159-c0af4cd3ff76 | -12.60805 | -46.94678 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6878b792-37f8-38fe-92bd-7729a0a08e97 | -8.89173 | -44.40356 | 2025-08-16 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25e214ab-0e3d-3795-8740-3097b04671fb | -12.59668 | -46.94451 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 14caabdc-cf08-32c3-be61-13d1ba7d0067 | -7.66583 | -42.23262 | 2025-08-16 04:10:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d1e04fb-2272-30d8-8138-a65f9acb2c57 | -6.56057 | -43.05406 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c4848ef-7434-3018-9502-5db1f7837a10 | -8.19547 | -45.02657 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92637c72-76c2-30f9-99af-dacbc2321303 | -6.54988 | -43.03359 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2786f817-bf85-3d39-823d-30956bfdffd6 | -13.41744 | -43.67922 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9a77d190-043f-3e24-b2b5-3d70ed338125 | -7.66638 | -42.22912 | 2025-08-16 04:10:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c51c044e-2adf-3032-a0ea-cec1726ff6d2 | -9.16868 | -45.3254 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 346e38ca-40ce-3b73-8803-e5f2b582dd64 | -12.57134 | -46.95485 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71b3d654-64a3-38ae-b66c-8ff908710334 | -7.07437 | -44.94037 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b639b41-c0d1-355f-b35d-bb07fbba050b | -11.5062 | -47.23956 | 2025-08-16 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0ec38be-eaa0-38bb-8830-9b1fdb6907b3 | -7.0926 | -44.41702 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81f06db5-2af8-3832-b95b-647937f9edb8 | -12.5362 | -46.95372 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47c46d46-3063-3d45-abe8-357311b279dd | -12.83392 | -46.03794 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6828c04c-be3a-3a4e-a9df-cdafc95c67c6 | -12.60343 | -46.95088 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8019a368-627d-3f83-9702-6f536b7eed71 | -13.64724 | -44.20174 | 2025-08-16 04:10:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4d17ee2-f5de-31b5-bbee-b4c92bd88b1b | -8.19639 | -45.01954 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 661a9ce9-3e02-32f4-b3a6-3e1883b053b8 | -11.66091 | -51.62288 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e24d086-2353-3c3f-8498-116cd9032f1d | -6.55668 | -43.03469 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fc39b82f-ceab-385f-accf-dcca741788ff | -7.5872 | -45.15974 | 2025-08-16 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 461139c6-2336-3ebf-a6c5-5d818d62c4da | -10.9717 | -42.33601 | 2025-08-16 04:10:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 34da7583-aefc-3818-9f51-290dc7b08f1b | -12.80091 | -45.96435 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6942fbf-0963-33ae-8a5b-d8631016a4ff | -13.61736 | -46.90766 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
