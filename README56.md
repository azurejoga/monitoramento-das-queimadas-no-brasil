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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66c4c7f2-9abc-3b39-8268-088432e32875 | -10.0126 | -48.2344 | 2024-10-25 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f016f2eb-a2fe-3be3-abe5-1ee5ec47d8b2 | -10.01204 | -48.23812 | 2024-10-25 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 496249cc-7258-3fd7-9952-022276dc4b32 | -9.92672 | -48.13616 | 2024-10-25 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b39b282-6a1a-3aa6-b7e4-bcc49918a18e | -9.92396 | -47.84932 | 2024-10-25 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79bdd024-9f3f-3299-b28d-71598a975123 | -9.86459 | -48.40578 | 2024-10-25 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df2209ff-effe-37ec-a2fc-9892c24b319a | -9.79789 | -48.1322 | 2024-10-25 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4c84c4e-8e74-3dd6-a9c2-6b6d88ff7464 | -9.65201 | -47.64368 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 162d055d-75b5-3108-b477-e907c5eae909 | -9.63039 | -47.71618 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd2ffed2-e8eb-3742-a375-424fc95d82d7 | -9.62981 | -47.72005 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6200e58c-65c8-34df-b2b4-7c27364fccbe | -9.53665 | -47.62258 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 378a8e94-f317-3629-9766-a6d89e6c80c2 | -9.89334 | -48.65137 | 2024-10-25 04:38:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0723196-f410-30ae-9195-f61152b906d5 | -9.85341 | -48.57019 | 2024-10-25 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44676532-d611-32ff-8373-477bcf4821b3 | -9.7617 | -48.6651 | 2024-10-25 04:38:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b8d4328-9434-333d-a271-f5e8aa9bbceb | -9.6069 | -48.87875 | 2024-10-25 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bbb712b-904e-3cf4-8af7-962f586b836b | -3.69848 | -47.62075 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ea7d8a-a928-3bac-8a27-20805a33d566 | -3.461 | -47.66749 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0283090-7455-3ad9-aa29-e50358d808f3 | -3.46045 | -47.67101 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6780f14a-8ad2-3407-a089-3a7181673e7e | -3.4571 | -47.67047 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecd1af5d-5e75-34c5-946e-d4058b55a310 | -3.45656 | -47.67398 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a12e0907-b1f1-370d-ab3e-fcd68290fb69 | -3.07295 | -48.11453 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8cf13a7d-7416-3be4-a6a3-e743a23667bc | -3.04558 | -48.04992 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e60e5a0e-1647-3ee9-a020-9ede28080abb | -3.01287 | -48.09117 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d041782a-03e0-3a7c-944d-958b10299a72 | -3.01009 | -48.08718 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c75e1fa7-aecc-3787-b7e2-cb5713932e3f | -3.00954 | -48.09065 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bec78047-4a3b-34c7-a967-4757dad1df9d | -3.009 | -48.09412 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 589a7c83-9316-3a6d-850e-cc7a341457d8 | -3.00731 | -48.08321 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3768626-4353-3fdb-bf73-82d3b7a8315a | -3.00622 | -48.09014 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 097e9294-946f-32f0-8baa-5dbc5cef7a8f | -3.00398 | -48.08269 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86b5d09f-bba3-3f19-901a-ea3651ad4d1f | -2.96494 | -48.0056 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 951fc2f6-125d-3cb8-acc8-5cc2a70c8133 | -2.96161 | -48.00508 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9756ceda-9cc8-3e8a-b875-3d4a3c35209b | -2.89373 | -48.28871 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eb24449d-0117-3e76-b377-5092d70358cb | -2.89258 | -48.27439 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 429b341d-4447-3ec4-88e3-0b59049696c2 | -2.89204 | -48.27784 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9cafbb33-9142-3095-8295-0cfeab82537b | -2.89095 | -48.28474 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dfbd2572-b2f4-322f-b4d9-1268afde0d62 | -2.89041 | -48.2882 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bfc2acd7-eae3-39a4-821a-bd602a9bed00 | -2.74114 | -47.83902 | 2024-10-25 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0668d39-8db1-3063-bede-ba30330d6b86 | -2.58155 | -48.1445 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a6ccc3a-c768-3529-bb7a-79bd8462dd8d | -2.57823 | -48.14399 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a61f752f-a7ca-3e0b-a542-2f9dbd8c6674 | -2.47865 | -48.49586 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3ab7250-c90a-3ef2-9aff-d184839eea67 | -2.45325 | -48.50602 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70ff4beb-db6e-3c08-a174-59464f734f81 | -2.44969 | -48.61492 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6852627-0d7a-3028-8826-2f1f70146f1f | -2.44377 | -48.47984 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b8bdf99-f0ac-3cc5-856e-0125ca7265c2 | -2.4393 | -48.46502 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b77d644f-5814-3a51-9021-b66b8291a3b6 | -2.43876 | -48.46847 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 5a85dade-6b85-3c96-9983-9c61a4f7fe10 | -2.43786 | -48.53893 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4fc1188-ba2a-3558-bc98-da427668c27f | -2.43732 | -48.54237 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a11c37e9-a49d-396d-a9db-633ae9dddf09 | -2.43577 | -48.46796 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55fb5e44-89ca-3684-8470-6eeb79b730db | -2.434 | -48.54186 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68745893-cda1-3a61-a64b-1d023b65575b | -2.43068 | -48.54134 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c03e4025-827f-3f0d-bce4-022bf3ae498b | -2.42371 | -48.50137 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61bea312-a4ac-38ff-84da-9ff576c6c511 | -3.27196 | -48.46458 | 2024-10-25 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 548e531a-1399-3595-a8b6-a3f2e28e294e | -3.2012 | -48.65496 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4aa14bf7-9de8-3e22-a1ba-ee294ece6d24 | -3.12124 | -48.6491 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 796c0deb-0c40-3b41-9943-7db22e48edfd | -3.12069 | -48.65255 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 738bdd7a-a552-3e3e-82bd-7de9582876ac | -3.10892 | -48.59773 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5ca8dc2-a67e-3145-bb86-2d936f779df5 | -3.10838 | -48.60118 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 440f0dd3-5a4f-30bc-8a68-76292feeab54 | -3.10193 | -48.66376 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 331a027e-9293-3f26-8c14-5d665b887f99 | -2.97883 | -48.62686 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb3cc5c-0a1a-34c4-972f-6a1b414ff880 | -2.97551 | -48.62634 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f63ab926-3160-334a-ade8-a2437ae9d72f | -2.97497 | -48.62979 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a669687-e1c6-30f6-aafe-ca8da49c4c0f | -2.97443 | -48.63324 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7854f18b-3b1c-3c2a-83dd-786fd220bdd0 | -2.97165 | -48.62928 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d03fe388-40e3-3282-ab37-ff6b48a7a17c | -2.97111 | -48.63272 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b0cf51-924f-3edd-a4e1-cd419c9ae1cf | -2.9647 | -48.71652 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d23469e-4eac-3cb4-a7a4-dca54efde98e | -2.95075 | -48.61556 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c118238-a241-3e31-b66f-1ad399de69ce | -2.94653 | -48.74549 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47ced225-4c5d-3c48-82d2-eda8517c1ec1 | -2.88329 | -48.61211 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d42fe60f-349e-3c4a-9613-e18254b483d4 | -2.88275 | -48.61556 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 224f6260-eccb-324a-a4c3-7a9ac3386d34 | -2.87998 | -48.6116 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d30f398-e43b-31b5-944b-826f986bb2bb | -2.87943 | -48.61504 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fdabd70-8d16-3693-a961-cf288c06a0de | -2.87611 | -48.61453 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40948e5c-b5a2-3d13-bbf3-73acbe0feadd | -2.85662 | -48.45961 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d40c8ce-34cf-3b42-bf09-2eaf7c501e23 | -2.8273 | -48.45151 | 2024-10-25 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c34962be-72c1-374c-afc2-a59f3b37f05f | -2.79317 | -48.68988 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c63a727-d3bf-35e0-8024-1e72162361f2 | -2.77898 | -48.56406 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89c2af69-9021-3458-bf5d-b9de39e0f17c | -2.77826 | -48.69816 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8cadf6e-bcac-344e-af9f-786f1368742d | -2.77548 | -48.69419 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e771afee-fbd3-3169-8168-cfe70ddbf1a8 | -2.77494 | -48.69764 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca64c611-6f90-3abb-b1c0-e97038f753de | -2.7744 | -48.70109 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c23761b-c64d-3ed1-ae71-b8454c22fa0c | -2.77205 | -48.65127 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07b0f4b5-2190-3e49-b2d3-320adf1e371c | -2.73233 | -48.68747 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f56b417-3a19-3481-92c9-f8cdd610380d | -2.72867 | -48.67234 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1174c34-d7bc-3cb2-abf0-8c849d2dc4df | -2.72812 | -48.67579 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6348ec2c-268f-3dcc-9e9e-aa573daec2f8 | -2.69758 | -48.63217 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afc9ee35-16fb-3ec6-a9d0-58664499787f | -2.68654 | -48.63752 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44cfd954-3366-3b2c-a89a-734894eb800e | -2.65183 | -48.49087 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbeb01db-21da-3805-a49b-3245caa233e4 | -2.92323 | -48.95769 | 2024-10-25 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4e0fef8-f5c1-3b70-8cc0-5cbf410b4e84 | -4.50656 | -48.78833 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32af63cf-deca-395b-9b3b-e59f0d369757 | -4.14162 | -48.74228 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d599842-973c-397c-9b53-526eca3038ea | -4.14108 | -48.74574 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abb40767-701f-3501-9c2a-3d1f2f4deac1 | -4.14059 | -48.77043 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f32512ee-fa99-3fe6-a5aa-b48633b2041a | -4.14002 | -48.96843 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b587f9db-89ae-3842-a2b9-091b57bdc43f | -4.13948 | -48.97189 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf7e33eb-57a2-332f-b1d5-e00acc30c72c | -4.1383 | -48.74176 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34cb7fdd-65c5-3538-b5eb-0d2f4f348879 | -4.1367 | -48.96791 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a8a5bbf-7fe6-3f86-a3ce-1b853b354ac9 | -4.13616 | -48.97137 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeae24c2-3715-3717-9a20-0ec3588df0f9 | -4.13612 | -48.41155 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6dc8f186-743b-3e3f-92e9-7b9323f8e94c | -4.13284 | -48.97085 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b6e7e0d-b224-3de4-ab82-f2b09f00e911 | -4.1328 | -48.41103 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16001d48-b920-3699-82ab-0823161f21f8 | -4.09845 | -48.23861 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README57.md)
