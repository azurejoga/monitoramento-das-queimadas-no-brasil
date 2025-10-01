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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12154561-ed1c-3021-a49a-9046bae659d0 | -10.65103 | -48.52562 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f69ff6e-1298-3950-9b16-845f6da51570 | -11.75692 | -46.86732 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e483c398-15f9-3007-89ed-03a1637f0032 | -11.14867 | -54.11932 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49887852-e733-3c22-96bc-8a5d72e45498 | -10.23749 | -52.69789 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89b2aa84-5678-340f-a73e-14071bfd9e84 | -13.3155 | -47.22468 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f842836b-1ba2-3dd1-97ec-3a7e10842e02 | -11.12121 | -49.78324 | 2025-10-01 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6edb0a46-7514-3061-a284-e9d10c7c3555 | -7.82946 | -47.06458 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fdd044a-d44c-3b26-aadb-0eb89d601cae | -5.85551 | -50.07055 | 2025-10-01 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49a92a32-c761-34a9-8a1b-ced965c16d2d | -13.30966 | -47.20665 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 737f3088-e69e-39f0-a48f-f4c63ce2ca2e | -11.84406 | -44.99893 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9b983e6b-e5ed-3405-8fe2-aebc8f5d6d9d | -9.60287 | -57.74518 | 2025-10-01 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c66f0e19-77b3-3475-893e-e5706e8d1860 | -10.06481 | -50.27282 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1795f43e-83c0-3170-b76e-d28d9bbad4c7 | -11.58738 | -45.04161 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00addf61-aeb6-375a-8980-7c9b687f9ae9 | -11.15072 | -54.31449 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f04e047-f8cd-3840-aa17-29e29a4a13fb | -6.72938 | -49.6403 | 2025-10-01 05:10:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec3e2f45-cf02-3058-a0a1-66138a505e35 | -8.5581 | -44.74013 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7672dc55-8d2c-317c-94aa-aea65a0a8180 | -10.5729 | -57.81767 | 2025-10-01 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 634ff508-bc1a-37d3-88ee-3e429064cbbc | -13.35377 | -48.14505 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a61d75c-6da5-35f1-81fc-7ca47427a2a9 | -12.82113 | -47.02173 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88dfb2f4-3ff4-3070-9581-5c1a9c42fe14 | -7.12192 | -47.78607 | 2025-10-01 05:10:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b37abea-a0d7-3e33-93f3-92688b3365b2 | -10.60021 | -49.63845 | 2025-10-01 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a691905-94ed-3861-acb0-8b9cefcb8268 | -10.85004 | -45.41309 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1110f125-e886-39ae-b515-72cf7f2c8acd | -8.54951 | -44.65075 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da38296e-8033-3450-b6f2-f15fcfecfcb4 | -7.87132 | -47.27697 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3650686-13bd-39b7-b0b3-e048cf0dc7a4 | -7.47476 | -46.46978 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e42224b-0a79-3fa9-b12e-86cfb42e387b | -11.83302 | -44.9713 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d044a54-959a-3fc7-bbd0-3e4d1ef5b861 | -11.05183 | -47.82156 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfb7c983-3cf1-3766-8bbf-5f3d6efb8879 | -11.76955 | -46.86741 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0781056b-2495-3cc9-9d30-38d868c95094 | -11.14695 | -54.12133 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e92a61d8-fb09-34e3-b506-68614dede046 | -14.75302 | -45.77721 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 073f4084-5410-3073-86b3-0a9c166b73df | -14.35185 | -45.93867 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9127e9e7-b049-30c9-ae32-27f2e9980747 | -17.39242 | -47.16816 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19f90aab-be07-3bb7-90fa-b49fe1d66899 | -13.77121 | -47.95831 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a75a117-f9d4-3410-b1e9-208a2b4685b1 | -15.4763 | -45.87977 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e41ffd80-b2f8-3a70-8ef9-c314d00c5a23 | -16.00603 | -50.8774 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c33a3e8-bfc9-3cd4-b498-c5ffb5694d90 | -15.39104 | -49.19308 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 384257f9-1ac2-3d14-85ea-bc955d6081d6 | -14.43291 | -46.36425 | 2025-10-01 05:12:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db4db595-5da6-37ad-996a-23ec6a56a557 | -15.27319 | -49.29374 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b079c56c-045a-3f35-ae91-2a6a1ac18625 | -14.34754 | -59.86884 | 2025-10-01 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d6aade7-8cb6-304c-bab6-4837e3bb62ed | -17.86687 | -47.14277 | 2025-10-01 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c840a7-7b5d-33e4-ac75-8ebe47edff78 | -14.95542 | -46.8901 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 991da7aa-ca93-3956-8987-fabd8f7de82d | -15.0165 | -56.04426 | 2025-10-01 05:12:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b71e91ed-0baf-3763-87a5-73b87c127a84 | -15.34486 | -56.96592 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e16e3a0-0a71-3116-a4fa-b8cb18f1cae8 | -18.80724 | -47.5499 | 2025-10-01 05:12:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1875ac03-12f6-349e-9466-a0aeef053794 | -16.19115 | -57.60096 | 2025-10-01 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f109d402-34a7-3d9d-b95e-f15c95fbde78 | -15.94648 | -48.11876 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fec4c972-b023-3e70-bd1f-1fb70856e7db | -14.89324 | -48.12333 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3085480-6dfc-3603-beb5-0c85f7008ce0 | -14.68361 | -48.24321 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4c64443-f525-3a02-8481-de8fdb4010fd | -14.58993 | -48.29834 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76435b26-bbc5-386f-b95c-2eab8757576d | -16.01074 | -50.88116 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ceecb98-c5bf-3f2a-a683-3dfdc789d55b | -15.84807 | -59.59847 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de9bd6c7-c624-3484-8435-bd4092df1f2c | -14.59134 | -48.23032 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f97a8a87-4b79-3f13-a9d3-be7e6a01f90f | -13.93778 | -48.12481 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5aa94504-ad6e-3b06-82a4-201ae35d6f96 | -14.9055 | -48.12215 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43bc8a3b-23c5-393d-8533-9cf24ef52bff | -15.00991 | -56.03876 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5e2b3f5-d0e0-361f-9c0c-0d2a9c8da88d | -14.68165 | -48.12226 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d63d877e-278f-3c99-886a-5ec1080f55f9 | -15.87465 | -54.23545 | 2025-10-01 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b648183-c3cb-3e7b-a153-de05ef015757 | -14.49775 | -48.44122 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee327258-8c96-373f-bda2-7d4f28bee59c | -14.67762 | -45.28605 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c82370fc-4019-3e1d-9a4b-a171c82644af | -14.59766 | -48.22741 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc37fa3c-0da2-3d87-84fd-17a6661f11c7 | -17.89601 | -57.58672 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 6ea6a30c-6d8d-373b-9976-665f90ad8198 | -15.36253 | -46.11336 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b724533b-3da6-32e2-aed8-eb59ac435c33 | -14.89773 | -48.10515 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f138da20-7e51-3172-bb10-9dc305aa4bca | -13.94517 | -48.11208 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 474d73eb-95eb-3251-ab39-b3619b6dced9 | -17.39814 | -47.17714 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 104c8437-151d-3f1d-adc5-e6fab3e2defc | -14.05814 | -45.03386 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5a1ed360-e8c4-39e1-8c3f-2e0cb713c9ef | -16.39903 | -47.05371 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 643a8a79-b688-328f-8a76-3aef9b05e664 | -17.38652 | -47.1609 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c64432c-ddff-3541-823a-0aca783a16f2 | -14.79869 | -48.32539 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c576805-5123-3f48-89f2-dcc3d33fc551 | -16.01135 | -50.87592 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24d804c9-f144-3098-bd4d-3a54bcd2c2c3 | -14.52937 | -48.37119 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8ac5f5c-03ed-3fb2-a595-d2b6666ae030 | -13.76864 | -47.95629 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a784af4-c628-3462-9c89-bd82c654ca5a | -17.89782 | -57.57449 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| cb760cd9-18a4-3652-a33d-70d5553ad828 | -14.18863 | -46.1088 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff35a555-8ba6-3850-8a43-730e45b74a33 | -14.14292 | -49.19697 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35417a63-4b4e-3dd7-b3c6-3919c530806d | -14.49187 | -48.44091 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 346ccb7e-642c-3a4c-818a-8bb958206fe6 | -14.69301 | -48.12872 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33472f2c-59d7-33af-83dc-11462b96c211 | -14.87622 | -48.3275 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40b51498-e580-3b50-a8dd-76dc33b4133c | -16.36056 | -49.96475 | 2025-10-01 05:12:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef3b4171-f6e9-3542-aaf2-81b687683198 | -15.33721 | -47.94248 | 2025-10-01 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ca8c169-7688-3e4a-adab-45bd4ed3e527 | -14.09638 | -49.74811 | 2025-10-01 05:12:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a24a7371-13ce-30da-aa21-8d6aaad7274a | -14.89962 | -48.12052 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9aacdf46-6cb7-36a5-9cfa-e09c4225ff1e | -14.04279 | -47.9932 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4be98673-45d3-363c-ac92-952d1c8d1f39 | -14.52262 | -53.12227 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbbcd869-8297-37aa-b9c7-4da3d209697e | -14.3488 | -45.90163 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| caea318a-2518-3269-b0b9-8c7dcff4285b | -15.15453 | -49.10358 | 2025-10-01 05:12:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44f1ec88-3ef5-309e-8fe8-c58b434a416d | -13.78282 | -51.23166 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2c9dde2-b4fb-3d3e-ae27-b40c35ec3736 | -13.78892 | -47.99118 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45e9dca2-478d-3452-a978-84a238918890 | -15.99284 | -59.51998 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94126b94-ad2c-3de7-82a7-a7bf01ed8cb7 | -13.76591 | -47.95196 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b1ee7d1-4565-3595-939d-50177e8fde61 | -13.73789 | -48.69492 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed1e85cc-8b3a-301e-8c9b-1a3a4703bf92 | -14.01661 | -46.32315 | 2025-10-01 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7f9f3f8-32c4-3a91-95e6-6b1187e33ee7 | -16.02591 | -50.88354 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e13148b-c32a-36ef-8704-4eb84b7f69d9 | -14.91068 | -47.20825 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71452744-fde0-3b70-8423-3200f02bbb0a | -13.77937 | -47.96857 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e14f6758-b7da-30ac-bac2-999a48b4bbd6 | -13.66042 | -48.0843 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cbe0266a-5f25-35b9-8515-e044e336634d | -14.59511 | -48.21483 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bef4d801-cf6c-31b8-bcf7-c7883dd7d73c | -13.77537 | -47.97432 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bedc08fa-4121-32cf-8408-8b28f8c5bcb9 | -13.70428 | -48.63564 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d12d8f4-b661-39d7-b311-b39ce62cc2de | -15.28846 | -56.78376 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README130.md)
