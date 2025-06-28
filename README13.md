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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a016a125-5359-3f9a-8b56-6f5cd4704bf3 | -13.99983 | -44.02829 | 2025-06-28 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b261316-11b6-3099-8d97-68bfee378739 | -15.35248 | -49.04958 | 2025-06-28 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ac06bf7-9453-3531-bcca-6243dc4916d7 | -16.68269 | -43.88274 | 2025-06-28 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 725cdf07-c036-30cb-ba32-641fbf25b1a4 | -10.81892 | -53.74443 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d54f9b3-f8d3-3c1b-877a-dac96e6ca371 | -11.44357 | -54.46695 | 2025-06-28 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37173162-a7b1-3bb5-aae0-92e7433b7e16 | -14.68824 | -53.38758 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c6233421-c334-3511-ba54-099d34d11b0c | -11.26977 | -52.74852 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| e20d95ba-e1ae-3da0-9886-f2231db61a63 | -14.69921 | -53.39498 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd35738d-c3db-3ccf-9714-b74ec875dbce | -13.30046 | -47.51682 | 2025-06-28 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 446247ce-816f-37b2-a937-02b0353825d0 | -14.47792 | -51.07117 | 2025-06-28 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 261526cf-5cd0-3e75-beee-750f94a8560a | -12.25658 | -46.76246 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4607aa4d-a62d-3af4-a298-c853add01904 | -13.94615 | -54.49234 | 2025-06-28 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adff48b2-b274-30b5-a2f6-778005ef6cd2 | -17.75419 | -52.43463 | 2025-06-28 04:04:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cab9e31-ed04-3da8-9f4f-7ae02fa2dce0 | -19.16978 | -49.13809 | 2025-06-28 04:04:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f02b897-991f-3c08-8bc4-a4efd17e2abe | -12.26037 | -46.76299 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e89d4f17-a03c-3d6a-9a16-bd3de59e4011 | -13.57592 | -45.25847 | 2025-06-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 783da9d0-23de-3300-b6ad-b546a2acf5ed | -13.29623 | -47.51617 | 2025-06-28 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c686ba3c-f870-3282-b49f-124cd0837389 | -14.47854 | -51.06799 | 2025-06-28 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1568fab-96f1-3a83-af87-18e8f1646b04 | -11.57761 | -52.11349 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b1c3e1e7-4519-38a7-be2f-e38a0f620df2 | -10.83616 | -53.75983 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da256520-3365-3594-85a8-4f452be39193 | -12.6589 | -49.46758 | 2025-06-28 04:04:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 115aed00-a14d-3d6e-90e0-59ec44572681 | -12.02211 | -47.77036 | 2025-06-28 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5638c3d0-9459-35ce-ae03-0a770e99fa21 | -13.64033 | -47.6861 | 2025-06-28 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c091a80-37f2-3c29-a348-fc12b45e1305 | -13.94702 | -43.24128 | 2025-06-28 04:04:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80a161aa-6d19-38bc-8025-95fc958979a6 | -12.26104 | -46.75928 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f66f869e-faba-346b-8360-421d2af51675 | -12.26245 | -46.77482 | 2025-06-28 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 8629fd72-43c0-31c6-8243-2851216f81a0 | -12.10781 | -54.58007 | 2025-06-28 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abf9cbe7-56b1-3f1e-8d1f-d0a4d92035fb | -10.84269 | -53.76113 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e7b5194-e130-3642-8a5c-e04f3133d176 | -19.4457 | -44.15309 | 2025-06-28 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9eb31dc-8c26-3da2-a75f-5700185c6f69 | -10.87287 | -53.77995 | 2025-06-28 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1758429-7326-3a05-8422-36fa1030e7b0 | -14.6959 | -53.39207 | 2025-06-28 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 720709a3-9b2d-35a9-8575-00919fea6143 | -12.10521 | -54.59253 | 2025-06-28 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e12fc2c8-1c8f-3a82-b48a-d50665385040 | -15.55617 | -42.65811 | 2025-06-28 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c6028d2b-6c61-3acf-a3fd-f5f6f46722b5 | -13.66948 | -43.66555 | 2025-06-28 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae28b97a-ede3-3df0-abe9-adb343b0956c | -13.99574 | -44.03157 | 2025-06-28 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 400428fa-9a6b-3f36-ab8f-7c144ef9f7d1 | -11.2688 | -52.75335 | 2025-06-28 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 62a83e72-f769-3136-b010-9af93a8ddd60 | -17.04807 | -43.77455 | 2025-06-28 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 605565a4-4180-3d1e-a985-0aef4eecc259 | -12.02648 | -47.77118 | 2025-06-28 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8801cdc6-3004-3421-abc8-ffd819428719 | -19.77424 | -47.9016 | 2025-06-28 04:06:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b6b6069-d3c0-320d-aee4-8624451608e0 | -21.203 | -48.51743 | 2025-06-28 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c4a8fa2-0b13-3497-a044-f00c09b99e4b | -21.62721 | -43.46526 | 2025-06-28 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04de1982-e04e-39da-9aa2-29569df0a4c9 | -21.1786 | -43.98147 | 2025-06-28 04:06:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 584284dd-532c-3079-8fc7-73c4617ebea4 | -20.99529 | -51.79387 | 2025-06-28 04:06:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ee1e8507-f34e-3db8-abbd-ed5c939fc29d | -21.10802 | -45.71491 | 2025-06-28 04:06:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| eae83378-e051-382b-a29a-0e92b00dc0c0 | -21.80578 | -46.85764 | 2025-06-28 04:06:00 | NOAA-21 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 590f07d6-4546-3efa-8e90-7999788e378f | -20.76271 | -46.76927 | 2025-06-28 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 91fc8529-df02-3c2f-9898-02e40f19fc17 | -20.30859 | -50.3696 | 2025-06-28 04:06:00 | NOAA-21 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| dbc0e88a-b36f-3178-adec-9f3242de8df7 | -23.59564 | -47.43839 | 2025-06-28 04:06:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8c5f062a-da60-3ec1-aac7-13a499e7d057 | -22.92137 | -45.41367 | 2025-06-28 04:06:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e7aa2290-7f6a-3f2a-a5c2-d099e5ac6feb | -20.76448 | -46.7678 | 2025-06-28 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78ab68f1-0e0a-3eff-a619-a391530bf538 | -21.62333 | -43.46836 | 2025-06-28 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d627963c-2567-3e72-abe5-544140f349af | -21.66434 | -41.94897 | 2025-06-28 04:06:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 220c5990-e2e7-3c77-a77e-c046af720806 | -22.94551 | -45.41431 | 2025-06-28 04:06:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 84c76ccf-49c3-358f-97ad-a689b9c0c8f9 | -22.85616 | -42.98257 | 2025-06-28 04:06:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d5642e5-b837-3344-a865-5de897073efe | -20.85453 | -45.52887 | 2025-06-28 04:06:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6481d42a-54e4-3020-b985-d1c7b1c6b434 | -21.11145 | -45.71556 | 2025-06-28 04:06:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| fddaebf7-543e-36af-ae12-c9705ffcdf06 | -20.24532 | -46.74053 | 2025-06-28 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3296b8ed-78f6-36cb-aacb-90bad1bf9d47 | -22.07114 | -43.1875 | 2025-06-28 04:06:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f00284b8-f30a-3ac5-9e8a-7f0a6e1dc0d6 | -20.85387 | -45.53283 | 2025-06-28 04:06:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0ec25b1-45f6-3db7-958c-c75d4849d4f0 | -21.943 | -48.52111 | 2025-06-28 04:06:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fd76308-510e-3603-bbfe-6f4250e47e74 | -20.24087 | -46.74452 | 2025-06-28 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b5d85b5-bb70-30b3-94e6-faf701376f4e | -21.20693 | -48.51574 | 2025-06-28 04:06:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da2c27a1-f410-3e1c-ab23-27f955e03486 | -20.90168 | -43.81849 | 2025-06-28 04:06:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d2506113-a800-30e1-89a0-8dc7942dff9d | -20.31093 | -50.36755 | 2025-06-28 04:06:00 | NOAA-21 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 96682ef9-b550-3a85-9bf1-4314ffa82182 | -23.59361 | -47.4397 | 2025-06-28 04:06:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 01762848-91dd-3f59-b361-4bd836455d0c | -21.66773 | -41.94955 | 2025-06-28 04:06:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f32731e5-d15b-38a5-8b93-94693494bf94 | -21.1087 | -45.71091 | 2025-06-28 04:06:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d2be6d4c-31ef-3275-8744-0a4d7bf55885 | -20.31 | -50.37233 | 2025-06-28 04:06:00 | NOAA-21 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 8818b830-359d-334d-b9aa-05ed395ab8fe | -9.7041 | -56.1843 | 2025-06-28 04:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| eed68c0c-6ad5-3cf3-8272-b69889736954 | -11.2664 | -52.7527 | 2025-06-28 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 0bb980b2-b3eb-3f7b-bb19-2dcc0a0374c3 | -11.0644 | -55.3757 | 2025-06-28 04:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a1d7148d-d5c8-3608-8502-2e7dd5a9361c | -9.7228 | -56.183 | 2025-06-28 04:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 29a919a5-56fa-3d41-988b-ff9945c109c0 | -6.9108 | -43.9834 | 2025-06-28 04:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 9417fd29-9e9e-350e-90ba-4a4910df646b | -11.0455 | -55.3773 | 2025-06-28 04:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 4b1eb62f-c017-3abc-b614-e22fd9bb44ac | -11.0457 | -55.3571 | 2025-06-28 04:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4e5a6b6d-e467-36b0-97c9-e8acdf86e5eb | -9.7041 | -56.1843 | 2025-06-28 04:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 6ff8e2d2-1c39-3ad7-9a6e-1bfdd9877635 | -11.2664 | -52.7527 | 2025-06-28 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 16e9f7a2-0347-3c7c-a932-cc257cf47783 | -11.0455 | -55.3773 | 2025-06-28 04:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| af187a11-03ef-3685-978c-395c08f17372 | -9.7228 | -56.183 | 2025-06-28 04:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 508b9397-adb9-3ad1-822b-be88ab4bb5df | -4.5429 | -48.0151 | 2025-06-28 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 761de491-3175-34c2-a69b-9f46aa36cffd | -2.4486 | -47.50085 | 2025-06-28 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b1dd3eb-1a15-3086-82c7-62c699b983ad | -2.44574 | -47.49653 | 2025-06-28 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32707aba-032b-33fe-aa53-3c8876591374 | -3.46628 | -42.8638 | 2025-06-28 04:25:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 084e7154-6788-394f-9265-44f04cbf62c6 | -2.62636 | -44.25675 | 2025-06-28 04:25:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bd5ff2f-900c-3f85-8fa4-639e4cd76ef1 | -2.44064 | -47.48413 | 2025-06-28 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60490af7-8a04-3ad3-8616-052b1d1ddfdf | -3.38004 | -43.12182 | 2025-06-28 04:25:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 417d6cb4-cf0b-36d8-b5a1-f23e784e3236 | -7.11018 | -44.19223 | 2025-06-28 04:27:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b54ed5fc-cf8d-3f63-bfbf-7c0856b5df25 | -8.00096 | -49.71077 | 2025-06-28 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b061bdc4-1b25-3c99-9123-391ca03f242f | -10.27529 | -44.64615 | 2025-06-28 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbb85278-1eb4-3247-9a6e-ba3de4e6a6f3 | -4.37655 | -48.08261 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b46dd1be-b4b6-388b-a90e-5ec0b1a85add | -4.43457 | -47.61593 | 2025-06-28 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 622b21cb-6ae6-341a-81bb-0568d1e8a081 | -6.55688 | -54.98361 | 2025-06-28 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f93ccb43-51aa-3cb5-aeff-ac809be7d5a1 | -6.71751 | -44.40516 | 2025-06-28 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9a8e0b7-b381-33db-b28a-4f7191cdee62 | -8.85292 | -47.95399 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 953f5966-e6e4-323f-8b36-88eb615f698d | -9.15516 | -46.37213 | 2025-06-28 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5429e8c6-8402-3fb7-bb27-8e15cc54818f | -5.77438 | -42.28271 | 2025-06-28 04:27:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6276d6d1-27e3-3338-a60a-c070fb707b98 | -9.11898 | -49.48365 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d49b330-554a-3910-9d23-4f7314749c9e | -4.37147 | -48.07003 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2bd7661-63ea-343a-a616-5501e4a0c786 | -5.45485 | -43.08039 | 2025-06-28 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1288a44-6185-3085-a95d-8aa8095d940f | -6.84139 | -42.80093 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README14.md)
