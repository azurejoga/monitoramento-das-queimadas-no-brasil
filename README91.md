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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e7ee7e6-3fa8-3d26-be25-4049c415fe86 | -7.76859 | -42.59816 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8f6d834b-b3d1-3e3c-aa13-331a8f0b45d0 | -11.77777 | -46.8272 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b5408b-1d62-38a8-ae60-ec768c76a07d | -6.67962 | -42.8346 | 2025-10-03 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a37d7c7-5c1d-39f2-a155-736d499499f4 | -7.77467 | -42.52558 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f7fc38d7-a10d-37bb-8528-66f7273b9542 | -7.71337 | -46.19532 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c420d2f-e280-38e2-8d36-ed07d7303c10 | -10.93215 | -46.7295 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2cb4126c-59af-3b1e-bcb6-b162c6ba6192 | -7.75061 | -42.56118 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| f1cbfd3a-75c8-39dd-844d-16a00d4b18e8 | -7.76339 | -42.60497 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 3b3d9580-9461-3e69-8d46-257647fed496 | -10.10536 | -50.27754 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f0984b8-dd27-3c22-b644-665a7253af1d | -10.94357 | -48.56171 | 2025-10-03 04:32:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 651d7d07-d550-3261-9e72-1084167820c0 | -11.80686 | -45.01116 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| acd287db-c3f2-3943-a4ea-300b46aa7111 | -11.10182 | -49.80743 | 2025-10-03 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e558874d-faec-3ab4-9b78-ce5fbd813510 | -11.91889 | -46.28309 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| f005744f-bac4-3ae1-88b1-a0c41a2b37a4 | -6.23083 | -44.24479 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb5ae40f-cb59-338a-bbc4-f02be728aeac | -4.66545 | -45.78761 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e85942b-3a98-37ae-8377-791cb516336f | -11.91119 | -46.26191 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9dc62fce-d0a8-36be-a074-25e8edd8ecd5 | -7.30628 | -45.26292 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 475c026f-b101-39c1-906a-949b394b5ec4 | -7.31607 | -42.88715 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 667a882a-e1ed-3b88-9737-f5a3bf285674 | -10.86039 | -45.4084 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4797f8c-1393-30c2-a2f4-59524f5ab70b | -11.10347 | -47.83916 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 601ee11b-d209-328e-b830-859cd97caa30 | -10.87486 | -46.71725 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14210028-8e74-3f01-903c-8ee4c6650ce9 | -5.83934 | -43.36889 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f21804e2-392a-34bf-9ee8-ace9d5491825 | -10.25586 | -48.07533 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb0c5ff9-9018-3fd7-8759-3af64144d885 | -9.66035 | -48.21342 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a9e27bc-4920-3f25-b39b-27f6262c9d59 | -9.31925 | -45.9618 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f420d3b3-1b9a-3d83-b182-60f476b39f65 | -11.14503 | -43.3964 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a5514ca0-5c5a-3ea3-99c5-d428d28f829e | -7.00344 | -47.1824 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56f62b4f-9594-3ae0-9502-532378aaed48 | -4.66901 | -45.79574 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b23274e6-68ca-32c8-af95-8a92fefdb7f7 | -10.89604 | -46.71671 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8270ab01-931c-3b6c-be92-80522cc8ecce | -4.89041 | -49.96564 | 2025-10-03 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4594aa65-2d18-3d8f-a536-789b6b238f30 | -11.54088 | -49.82513 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33453b3d-45d4-3429-9195-d55bb1ae082a | -5.90945 | -43.90369 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4758044a-58c5-31cb-b29d-ffa81f32310e | -6.92791 | -44.40574 | 2025-10-03 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4c9d2f2-bb7d-3fe0-923f-55cce1b9f5cb | -11.8353 | -45.00267 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef0b08e8-524c-300a-a50b-aa43e72d4d2b | -6.22218 | -44.25252 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e12928fa-890b-3a6b-b2af-94d226ae8d95 | -8.89963 | -45.03014 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 650a39e1-d323-38f9-b17e-cb91fbb8da04 | -11.09909 | -47.86761 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48452a59-306d-3d1f-9d2c-9a1c32bef17c | -7.77877 | -47.37168 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efbab63e-c940-3838-972b-2a28e1989b57 | -11.61864 | -48.50098 | 2025-10-03 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 709e0956-2e01-3090-bae4-f4ad32fc96c7 | -11.8076 | -48.8988 | 2025-10-03 04:32:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 308a0c04-f584-3be1-9d6b-6d6b6391a89d | -11.83203 | -45.02597 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6983933-3b28-3f0c-8ea4-d353c2df11c3 | -8.37551 | -48.6499 | 2025-10-03 04:32:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c32ec04d-92aa-35c8-96d2-a8d329b5d52b | -7.2903 | -44.18511 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5239228-8b43-336b-8ff9-bbf38153b1ca | -7.74773 | -46.24609 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e634c5d-f331-3fe9-b064-a8a6242df42e | -8.62247 | -54.98196 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a43e51c-0b9b-3d1e-af0f-d49f50f58b54 | -5.91098 | -42.7774 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7025f222-dbe5-3a0c-a0c6-bce631608c0f | -10.00383 | -48.27542 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1f39b3d-53ac-32ad-a445-5f22dc3a807b | -7.75816 | -42.53891 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a607c7cb-64de-3b1b-9c49-285f995117e3 | -11.66508 | -44.27372 | 2025-10-03 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 981b95b0-79c2-339f-b1f8-1c96f283aecb | -8.17261 | -44.15918 | 2025-10-03 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daa103d8-1838-3b70-a0e6-d02a00c47132 | -11.30706 | -47.83818 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20120c51-abe0-3c4f-9311-153a62caca06 | -9.62262 | -54.31058 | 2025-10-03 04:32:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2177379-eae2-3cee-ada1-fd2e5890547c | -8.58747 | -41.06205 | 2025-10-03 04:32:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| deab6e63-69ec-3cdd-ae88-da5167b9a5fb | -10.06549 | -48.18491 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67f86f84-6d55-34b0-b5bb-dc82e099c6bf | -10.07211 | -48.18597 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65e06d37-7f01-345c-bb57-2e2fbf0a3a17 | -7.25404 | -48.48059 | 2025-10-03 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb78431b-399f-3c29-ae08-3bf39311dbcd | -7.76806 | -42.60187 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ef003db6-102a-3f43-965b-c12d67282314 | -9.07143 | -46.65294 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a8c7af9-5d6b-3608-8fc5-2905a591f0a7 | -10.87887 | -46.714 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0be41648-f2fb-3c85-a8e8-faf0fb3be8cf | -11.83706 | -45.0447 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67ad98be-1cb0-3ab6-9e8d-a109dbf6bdf2 | -6.04919 | -44.63498 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10bf6f12-b9e7-3b02-ae31-e479370c35d3 | -10.63872 | -49.07268 | 2025-10-03 04:32:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 249a454f-8880-3e0c-8f03-dd03f0dd4315 | -10.76233 | -45.33832 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14be018c-344a-3368-a294-575f7424bb37 | -4.66845 | -45.79936 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7713cba9-833e-3780-891e-cc5c391f5af3 | -4.51338 | -55.45987 | 2025-10-03 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31edfff0-c8bb-3fd0-96b9-aaf591ec3d65 | -5.89759 | -43.90658 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00a8f0f0-eb94-3219-ae17-aa954ebe9b74 | -10.89833 | -46.72481 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cb83b7b2-c7aa-3627-a5b6-0d67ed43e593 | -11.04741 | -47.80841 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 480aab5c-15f5-3da1-91d6-80f6f923051d | -10.86745 | -47.04165 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3aebb9ad-b082-342b-a359-3d050b2d3f46 | -11.10904 | -47.84738 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41103a48-4327-36f6-a7a9-a91689dd4c3a | -8.7112 | -47.98703 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f53b143-d96d-3a5f-ac94-30860302d802 | -5.96894 | -44.22276 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f47da16-579b-37c9-9ea7-f136a52f868c | -4.64671 | -47.95583 | 2025-10-03 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c27fb90a-3afa-38f4-b437-3630b7027c28 | -5.48111 | -44.11199 | 2025-10-03 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a1103ff-2c2a-3085-a910-86cbccf792c6 | -6.37487 | -43.86956 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea46a51a-9c10-36db-837b-a8a06eead3a9 | -4.65048 | -47.54557 | 2025-10-03 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddbc8bb4-6abb-3214-8f44-b54ff4f18866 | -12.22172 | -43.76645 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79a5f2c8-1c8d-3dd5-aaa6-4f014a88d59a | -10.88459 | -46.72266 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dca61de-0174-3d92-8c40-02ff54f76e59 | -12.40773 | -40.92094 | 2025-10-03 04:32:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d792a89-5e38-3af2-892b-9535cbe8de38 | -6.64564 | -42.78586 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 594fd1ac-dafd-3b13-9263-65d2bad41223 | -11.63737 | -45.06382 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9463ad4f-b85d-30c0-abb7-5d5657e585b3 | -9.17496 | -48.53502 | 2025-10-03 04:32:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f99d1e7-67ec-3c9a-a1e3-4c9245616ea1 | -8.82485 | -46.77651 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a41dfe9-b5bf-3dee-854a-32e9b1818a8f | -11.58794 | -47.66816 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 195cd1ab-47de-36e9-9ba5-36346102e730 | -9.32665 | -45.66957 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60e06720-ca09-33c3-8753-10a0bc44d079 | -11.64316 | -46.86609 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f8c2470-35df-389b-bd9f-45a630e12556 | -9.42158 | -40.72159 | 2025-10-03 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3f8ae55-0b6f-3d8b-af5c-f71380a65d07 | -6.29388 | -44.42258 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3f35ea7-393c-33bf-9023-ee32e54a5162 | -6.3265 | -43.88515 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4438dfc7-bb85-3d8d-b741-f5907b97b783 | -11.45138 | -44.9597 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3335e061-c122-314b-a5bf-6e15ca5880b5 | -7.7428 | -46.25328 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe37570c-e68a-3dc1-bc03-d8d5dbdd5833 | -7.74796 | -42.56447 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| b5108cb3-8aa3-3f16-b545-8037ac81dcef | -6.69216 | -42.83303 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aac5c9c0-5636-3df2-a5fd-bf6b2f250802 | -11.10996 | -43.18904 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5032f86a-2abc-3621-ab0c-906fe107130d | -7.78785 | -47.37671 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae057f50-2740-39e0-a4d0-166477aa21ef | -11.90509 | -46.74739 | 2025-10-03 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a087a30d-ed5f-3867-b8be-2535147b6e64 | -10.06825 | -48.18894 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9612e97-5f0e-3627-bd05-d8b4019d8a25 | -8.07655 | -48.22095 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0fecd29-e4fe-3b7e-920d-cf77f2f88519 | -6.87545 | -39.28309 | 2025-10-03 04:32:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dbd56ddf-d6f8-3b95-b096-5e7cd89879c7 | -9.94721 | -43.75742 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README92.md)
