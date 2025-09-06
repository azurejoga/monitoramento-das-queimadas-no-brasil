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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4857bbc9-73d4-3e17-9918-d7b18ccac849 | -15.7246 | -53.60151 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6162de54-6ab9-31c2-a35f-d30868b4d4c4 | -17.06701 | -46.47506 | 2025-09-06 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83234b7d-7cba-3036-a7e7-f652ee56fe3d | -19.40236 | -44.30927 | 2025-09-06 04:19:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f11cb67d-35bf-32d0-9d9c-96d2d205795b | -18.26302 | -43.02427 | 2025-09-06 04:19:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ec3a09b9-4ed6-3a5a-a7f6-cc91eec9a3ae | -12.09193 | -45.6932 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be5be4d9-972b-3bfc-bcdd-e6bea5573ab1 | -12.68473 | -45.05151 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f325c079-e4b9-326e-811c-a23ee78c8472 | -10.97348 | -46.81662 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daf891b1-2cb2-3493-865a-685b2348970f | -12.5328 | -48.06313 | 2025-09-06 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11dc831b-5e22-3ca1-948f-4852c6f4cf35 | -18.01129 | -49.26432 | 2025-09-06 04:19:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fedd6e3a-d30d-3bea-8927-4da735e081e0 | -21.82532 | -47.99601 | 2025-09-06 04:19:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 933376d9-f2f0-362c-9c85-714f6651761a | -12.947 | -46.56704 | 2025-09-06 04:19:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 07c8d335-bca5-3e31-8f5e-76edd7011861 | -17.62348 | -43.76528 | 2025-09-06 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0caaa528-db0f-302a-a06d-8b03b9d05ee8 | -12.09253 | -45.69261 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48786c90-07ef-31a3-80dc-0bf3d76de473 | -17.60683 | -50.56405 | 2025-09-06 04:19:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff8ab3c8-bbd6-3cb2-9772-427262a7d4a6 | -10.77744 | -47.77184 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66e539d7-1c1f-3943-86bc-723737675a36 | -15.71765 | -53.55838 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9698bb82-f06e-314d-8f8f-8ecbc2c6a2c1 | -9.21087 | -57.08916 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90adfe63-abc7-30ba-b583-f20373466030 | -11.38316 | -43.54647 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74e17599-ed63-3572-a394-526fdb57c08c | -19.07204 | -41.13947 | 2025-09-06 04:19:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d04aa59-1353-3f42-8471-2bb927459f37 | -19.41151 | -44.3184 | 2025-09-06 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7974c52a-4061-3c2d-82e2-03d8382e71db | -22.25069 | -48.75172 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9190b1b9-5ff5-3c26-8006-06d9bdfffff2 | -19.79389 | -40.84884 | 2025-09-06 04:19:00 | NPP-375D | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2fedfa2-2408-37ec-860b-169662497014 | -10.47093 | -53.62466 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fc7109f-6589-371f-b8dd-317745ccc8ac | -11.54656 | -47.31912 | 2025-09-06 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c21c0b83-6378-35b5-b50b-fc5a4c09e17c | -17.91268 | -44.53476 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0bc8501-3f63-37e6-96bb-f9149395dd27 | -15.73076 | -53.5964 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 756bc843-27a4-33a8-a8c6-05a287423006 | -17.69445 | -44.50349 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad3304aa-a8a8-3786-b766-b5cb2da48d98 | -12.55733 | -41.30762 | 2025-09-06 04:19:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c878e371-02fe-3f30-a4a1-d6d2205ee188 | -11.23536 | -50.69444 | 2025-09-06 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a522901-1a16-3553-a0a9-72043f71d9da | -23.09339 | -47.04732 | 2025-09-06 04:19:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 367343ab-b57b-325c-a57b-029ce1e513ee | -18.53644 | -47.41906 | 2025-09-06 04:19:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a5537174-782e-398f-bd31-5bbc6de6a224 | -10.20918 | -49.72233 | 2025-09-06 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83cc1736-19e4-3d25-8ffb-14300fc3d7c1 | -11.28566 | -43.56694 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf52285b-f1f1-34dc-9660-d947ee1b2cdf | -19.8103 | -57.95279 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c934fa13-b365-3d75-9096-e287f0a6818d | -19.97753 | -43.39347 | 2025-09-06 04:19:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ce084d28-a7bd-3211-9363-44df1028991c | -11.66475 | -46.87506 | 2025-09-06 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60a02f91-aecf-375f-8704-6118cb99ed23 | -11.40268 | -43.59687 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 013cef7d-5c11-3f9c-a56b-f8aff7321002 | -22.65506 | -46.82224 | 2025-09-06 04:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 082b3d9d-3caa-3422-8506-951c9daad6e7 | -20.91972 | -44.01205 | 2025-09-06 04:19:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03dafabd-9823-3959-94d9-f83eed176796 | -20.46465 | -48.79107 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 77e10f50-60e0-3774-bbf6-5edd0eaa33f2 | -16.32638 | -52.94481 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ded3d0fe-dc89-3a03-8f8f-9b958514d2e1 | -12.53944 | -48.06888 | 2025-09-06 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7ff5ab1-e419-3034-b071-c9081a185cdf | -22.85507 | -51.34267 | 2025-09-06 04:19:00 | NPP-375D | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 07fa617c-4d17-31d1-a6c5-aa5d8287a8a7 | -15.76037 | -53.65649 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed957962-6b46-3053-a7f5-2dcd99faa86a | -17.91671 | -45.90506 | 2025-09-06 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6b5dd3d-39fc-3c97-8c7a-1cc7271275b4 | -15.73033 | -53.57243 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44147f98-19a0-32fa-8c92-0f0a61c3135f | -13.03204 | -40.16319 | 2025-09-06 04:19:00 | NPP-375D | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e51cb2e-c3ef-3e4c-854d-1a1b1d5f57fa | -17.75916 | -42.51352 | 2025-09-06 04:19:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7575d493-750e-374d-83e2-06117f25e4dc | -17.69892 | -44.49683 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 522be7ff-1d27-355e-b254-b3148511e600 | -19.75934 | -57.9545 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 76752bbb-8e2b-30b2-a5da-8d08655328a9 | -18.56478 | -43.61872 | 2025-09-06 04:19:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a4fee1d-b8e1-3f51-9701-80278c8085c8 | -11.21061 | -55.02934 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b97eb10-66fa-3afe-bc5c-41d48f5aa7b0 | -20.5309 | -46.46075 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dbde3cc-973b-3eb7-9d0d-bb054215a66a | -23.33954 | -50.86349 | 2025-09-06 04:19:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dbd62f88-091e-375b-ab95-d852ede849bc | -22.24179 | -48.76238 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f5a0623e-5b23-395b-b08a-f04b14834f98 | -19.81253 | -57.97563 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7c1cc574-6c85-39c9-8077-e05a0b7388a7 | -11.9047 | -46.64596 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df1296ac-75a0-3a68-bff8-bcd13e8ced7d | -22.73985 | -47.0338 | 2025-09-06 04:19:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0893dd9b-2138-34ee-834b-34ef63e500ef | -12.68782 | -44.96804 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 260ca1c0-d53d-3d2f-b7b0-3299f5aa87ed | -12.95045 | -46.56762 | 2025-09-06 04:19:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1d5439a-6e41-3792-9366-6df558ee7b06 | -21.21618 | -46.25272 | 2025-09-06 04:19:00 | NPP-375D | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 15e76f0c-ed62-3582-9890-c8c0497f3c1d | -10.76497 | -48.27627 | 2025-09-06 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e490e44-5ffa-371d-88c7-8494ca3af1a8 | -11.17679 | -55.04524 | 2025-09-06 04:19:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7be262e-67e6-34aa-95a6-0daf658a0a06 | -22.25695 | -47.30244 | 2025-09-06 04:19:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ddecadf1-c690-371d-8a47-f9b0ca59022b | -20.30212 | -43.70922 | 2025-09-06 04:19:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f139e38b-aaad-33ec-aa15-37261ee60d57 | -20.3637 | -47.7854 | 2025-09-06 04:19:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd7a35b1-a851-3d21-a4c0-80bb5b4919a9 | -12.09252 | -45.68954 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9ea3368-37a5-3db0-b6fb-2b23c5597425 | -13.00345 | -45.21325 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c56acb89-b412-398a-b64a-79ee164037f5 | -9.21768 | -57.09096 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21c9ee97-c5c7-3ada-8d1a-e92cd78f44b3 | -12.09134 | -45.69685 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 166e752a-96b9-36b2-9361-b0ed51df30dd | -20.1069 | -44.31818 | 2025-09-06 04:19:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dbbb8e91-2a3e-377a-8be5-d54f498dd81b | -11.21648 | -55.03068 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df2a7e2d-d423-3ee8-b6c5-4b456ea211bf | -22.04562 | -47.93335 | 2025-09-06 04:19:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f85f92d2-fcaf-3df0-8a21-94060745784b | -10.74203 | -46.33957 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed9caf11-6239-3f89-ae7f-c5eacd0e701d | -10.79562 | -47.73307 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61ab2c8f-f777-3ace-9687-c2f15b6c10a2 | -19.62359 | -46.01685 | 2025-09-06 04:19:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ca94795-66f0-3795-a105-ead247de825d | -22.65839 | -46.82285 | 2025-09-06 04:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 21cec861-6e09-3822-9daa-f7be66dac1db | -22.2459 | -48.75904 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e886fdf8-0f62-3bf6-b533-13e7d7283514 | -22.56116 | -45.77269 | 2025-09-06 04:19:00 | NPP-375D | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9cac02da-616e-3173-9f38-2c233e344197 | -12.01278 | -47.78498 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c8cd825-0360-35a1-84fb-5eaca3a3c5b9 | -13.00621 | -45.21737 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0db3570-f9e2-39ac-bcd6-3ce642e3ad36 | -18.81065 | -53.27229 | 2025-09-06 04:19:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1efa2a66-555b-3cd3-b72d-7d0e3ec5fd0f | -11.59005 | -47.74474 | 2025-09-06 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6aa363b4-382b-3a19-ae68-019f7ca43880 | -16.30319 | -50.48322 | 2025-09-06 04:19:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b8d212e-d1d1-33c5-ad74-9b1115796e40 | -18.53708 | -47.41525 | 2025-09-06 04:19:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4409dc70-4944-3a7c-ae97-2c5bfec27010 | -9.25007 | -57.07025 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8513186c-36de-3c53-b10b-5c7e3121f02e | -18.43727 | -45.93418 | 2025-09-06 04:19:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca944252-7e00-3588-86c6-396a6ce12acd | -11.20474 | -55.02805 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87921669-ea6d-38fa-9e98-ea38cf16a4c0 | -9.9893 | -51.62284 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad31b1cb-b1e8-3fad-b474-abd722f3ef52 | -11.63347 | -47.80239 | 2025-09-06 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 684941cf-59a7-3ce3-9204-b9220240ce61 | -20.53305 | -46.46873 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7c19a23-f6bd-3dbc-adc1-d5195b55c7d1 | -12.69115 | -44.96859 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f41f5d75-f47e-32a9-9f3b-e092efdb0d14 | -10.7911 | -47.73711 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 966e7125-4202-38df-bb73-c509e1fc4892 | -18.68945 | -44.60543 | 2025-09-06 04:19:00 | NPP-375D | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4acff246-c565-32e0-84e8-abee38ff2460 | -18.54047 | -47.41586 | 2025-09-06 04:19:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34008615-344e-32f9-aef6-1a1ae9d0e30a | -23.05081 | -47.07813 | 2025-09-06 04:19:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 82b5644b-82bd-3e7e-a27f-f6a843678e39 | -19.1018 | -46.68033 | 2025-09-06 04:19:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4187f8e3-bb37-3638-9606-607c71b06e3f | -9.39688 | -54.75328 | 2025-09-06 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab3ba113-3716-36f8-8de9-d5f3da2f41f6 | -11.38371 | -43.54292 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66dcf4f2-ac4b-3e2c-a051-88f841788570 | -9.39774 | -54.74888 | 2025-09-06 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README51.md)
