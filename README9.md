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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5850a11c-0010-36e2-b8cb-a193d2a32709 | -10.50927 | -47.575 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de6b9ef0-3aee-330f-931e-1d80c82dfa31 | -10.46056 | -47.04113 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc863e80-d028-3a02-98ed-c8037918aa30 | -7.27188 | -45.36607 | 2025-06-21 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2e94921-b2c8-3c4f-b14c-b9919a86fd09 | -14.1201 | -41.67721 | 2025-06-21 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0cac4e73-7e6c-3371-b177-bf6c91efb32f | -10.50883 | -47.57843 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1923f8f-959b-3246-a9e6-db5b79afd6d2 | -8.00457 | -47.66572 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8390a28c-d2cb-3462-8a3f-c3bb52a06919 | -8.01782 | -47.65875 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb152eb2-6caf-3ffd-8dca-4f98f4df56ed | -10.54059 | -46.77818 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c429c71c-6c3a-3ac1-b150-5a7c3c3eb6eb | -10.54139 | -46.77412 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1cbe708-a013-38f2-a932-1329d99de9b7 | -12.15655 | -48.68268 | 2025-06-21 03:42:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 414985e7-d9b8-30bd-b43a-18154081b7cb | -12.28312 | -50.10786 | 2025-06-21 03:42:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3ebf164-bd53-322a-aa10-c8926f04aa31 | -8.01682 | -47.66414 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75fedfbe-0752-3d54-b617-40d0e13d2a94 | -11.06653 | -49.62597 | 2025-06-21 03:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b39b0560-4a7d-3aa5-bdcd-fa3f292a6065 | -9.09491 | -50.02691 | 2025-06-21 03:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| debfd6df-8cfc-33dd-9048-dbadf036263a | -8.0258 | -47.65853 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 816d17e3-e2bc-384a-ad77-0abc8b6764f0 | -10.50741 | -47.58477 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe4cc066-8e34-3863-b9a3-819605e0ca47 | -11.93565 | -48.42192 | 2025-06-21 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1813bc24-b887-3858-a19c-68f5ca757dc8 | -10.4411 | -47.04673 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff091109-ae7e-316d-8d27-c6a6471e7591 | -8.3719 | -46.97092 | 2025-06-21 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d68660f7-b48f-33db-9b99-5478ad4d2fcd | -10.5365 | -46.77068 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13345733-df2f-3c92-ad71-10411493a8dc | -8.37102 | -46.97571 | 2025-06-21 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97c32516-864c-37cb-b4df-5b864cd24cc9 | -12.26368 | -44.59919 | 2025-06-21 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| af96b29c-e3bb-3294-b112-fd43c610d220 | -8.01837 | -47.66277 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0b688de-eb96-3c40-8701-1aa8172439f0 | -8.0306 | -47.66111 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b432440-5d89-373d-8d8a-60055f8f3db0 | -8.01096 | -47.66691 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1fb1678-4548-39bd-9ac8-ce2702d2a85f | -10.46221 | -47.03252 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ddd1f94-22cf-3b83-8ab0-5906dd9845fc | -9.50378 | -45.43282 | 2025-06-21 03:42:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d7509fe-1081-3cef-a935-b46638c9fe4e | -12.28449 | -50.10142 | 2025-06-21 03:42:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a17e30ed-4bc4-320c-ae70-a610ccc4bd35 | -10.45546 | -47.03582 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a53d462d-e1d9-3327-a310-dbb3a4f762d6 | -12.43819 | -48.14119 | 2025-06-21 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bd1f86a-8697-34e0-85e0-917883298e87 | -12.16289 | -48.68394 | 2025-06-21 03:42:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6130119-c243-31fb-9cd0-33c666a8cad1 | -10.55465 | -46.76999 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a57715b-c4f1-3092-9f58-0a332cf94a67 | -10.5149 | -47.57972 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e2a4ab5-870f-3f6e-81e9-f6c3fda5d014 | -8.13301 | -46.82876 | 2025-06-21 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a05c57c7-b4e8-3395-9475-e4f5214c8414 | -10.44196 | -47.0423 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba1d6347-9199-3d0a-b542-8fe62234deba | -8.73432 | -47.98446 | 2025-06-21 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c7c5fe4-d989-386a-9662-e0918248d454 | -10.55379 | -46.77226 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77dd04aa-2f0a-3860-ba7d-cf92f61c2bf1 | -8.00306 | -47.66704 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 150be639-6439-3198-8891-c64a15ee5ba1 | -10.50833 | -47.57992 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96e16072-70af-3a4c-86ec-9e47315dc3e1 | -10.51535 | -47.57631 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bc220a4-59c9-3ca4-8876-f61f07477c8e | -8.02321 | -47.66534 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52a517c4-b676-3c8a-9b96-c12e5275aab9 | -12.28995 | -50.10941 | 2025-06-21 03:42:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd4b1f33-1e50-3e02-bc64-fc7a70cb9069 | -11.20435 | -47.84138 | 2025-06-21 03:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84e999b8-dc18-34ba-9414-ee59a4c659ab | -12.4437 | -48.14638 | 2025-06-21 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49666edd-8dee-38d9-9eed-8db41259a781 | -8.97644 | -49.86406 | 2025-06-21 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcfc2cef-a0ca-3645-9a5c-bb8d74e5135e | -10.53572 | -46.77478 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77675dfa-9422-353c-893c-f797c1d7ea26 | -9.50775 | -45.4341 | 2025-06-21 03:42:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a71b81dd-6c4f-33e5-b32b-00ff5a8f36d9 | -10.52099 | -47.58096 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87923f4c-ab6b-33f7-8085-b268e7bd6b5c | -11.76272 | -43.37169 | 2025-06-21 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80e278e0-9d20-3084-8d94-afb0b714dc09 | -10.14553 | -48.98905 | 2025-06-21 03:42:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9569b456-f8b5-3f57-8125-9eb59a1389fc | -12.43762 | -48.14501 | 2025-06-21 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5efc5d81-e69b-3c46-bca8-16a4236c677f | -12.44308 | -48.14832 | 2025-06-21 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92372c77-edec-3e62-8c67-9fd30794eec1 | -12.1618 | -48.68925 | 2025-06-21 03:42:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a5ca045-274b-3a13-819b-2e1037289a8a | -8.01199 | -47.66156 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cbb8d48-b20a-360e-a8d5-d8728499184d | -10.58358 | -46.92976 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daaf6175-4e89-3085-b810-6628601b933c | -16.42702 | -44.51929 | 2025-06-21 03:45:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca9aadd-7751-32e9-9ec3-7701cf28d863 | -16.38757 | -41.15939 | 2025-06-21 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 234dae4f-7101-3afd-aa95-ef6480e7fe15 | -21.69471 | -41.25711 | 2025-06-21 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 43c3d630-796d-3e56-b530-3589cffec15e | -19.71684 | -40.35191 | 2025-06-21 03:45:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 127fb34f-b0a6-3a74-bf31-699765c4f708 | -15.76783 | -43.26684 | 2025-06-21 03:45:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8cad295e-df05-366f-ad86-cff56cbbb434 | -14.15135 | -45.47995 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 121fb8cc-646d-3c01-b3b8-71a8df0817b4 | -17.78177 | -42.80756 | 2025-06-21 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80f59dd1-8481-3646-b333-8ed71b7fe296 | -13.2359 | -49.83585 | 2025-06-21 03:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c1e9eafd-2d5f-3038-a646-143cadc0c3ba | -19.54408 | -49.66048 | 2025-06-21 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e59cecc2-0ec8-351b-abc9-a05385a9cb1f | -14.22278 | -45.51328 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e4f35bc-4212-3892-a6e6-4c93e8f4d4a3 | -14.22776 | -45.51437 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ed8d403-a0f9-3b53-956f-e042a10515f2 | -15.76705 | -43.27094 | 2025-06-21 03:45:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 30daac16-e471-3795-b11d-ee9c612455b6 | -19.54308 | -49.66495 | 2025-06-21 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5911e819-1263-3587-bfab-467ec5399b97 | -14.15145 | -45.48125 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f045480-0068-3de5-a3cd-62cff8f1978c | -14.96638 | -46.26344 | 2025-06-21 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86eb8caa-409d-384d-8e83-374b25da8f79 | -17.58181 | -43.79743 | 2025-06-21 03:45:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26113f46-1996-38a4-8b43-c0879026d567 | -14.96697 | -46.26374 | 2025-06-21 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4e4ce7d-c96c-3a2e-b393-e71c837b8866 | -14.96763 | -46.26052 | 2025-06-21 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5aebda88-e986-3748-9e1b-4273505b40f5 | -13.39126 | -48.44888 | 2025-06-21 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe0edc47-2f29-35f4-8f87-46ac5e7df56d | -17.57683 | -43.80069 | 2025-06-21 03:45:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31e86f24-fdff-3196-88cf-1dca2b35f45b | -15.76744 | -43.2691 | 2025-06-21 03:45:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2d9ee972-6642-3da1-b26a-104fbc9006ac | -14.21901 | -42.85767 | 2025-06-21 03:45:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27fb38d6-40de-3461-a8a5-59b45b343654 | -14.81017 | -48.47328 | 2025-06-21 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afff4cbe-b39e-3118-b1bb-b331382fc12c | -17.74925 | -42.89587 | 2025-06-21 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb6a65f4-c9d6-3b01-8684-2fb7849c75d4 | -15.92048 | -44.25022 | 2025-06-21 03:45:00 | NOAA-20 | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a28f0e53-ad0a-33b1-a67a-0d75f6952b4a | -20.25544 | -40.90049 | 2025-06-21 03:45:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 20b7922f-3a89-3922-98c2-7d0074f148df | -17.216 | -44.79962 | 2025-06-21 03:45:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a259ca-e194-3d0c-bc8e-f819c0b99322 | -14.2272 | -45.51731 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f070b943-4c24-37db-883f-a10ebf7d68a1 | -14.15202 | -45.47829 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 799ced64-cf22-3d88-acfa-a63f907b2845 | -21.69818 | -41.25779 | 2025-06-21 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 390e1933-2985-3ead-85fe-0499a2913e56 | -17.58023 | -43.80581 | 2025-06-21 03:45:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e52a6b9-37fa-3f8a-baf8-bf2e7fbc27cd | -15.08359 | -49.48842 | 2025-06-21 03:45:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 207385fd-d934-34d3-a6b9-bfc499c3a174 | -14.81148 | -48.46696 | 2025-06-21 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4177c8d-7dfc-31fa-9e6c-7c3760c77ef0 | -20.95526 | -44.34628 | 2025-06-21 03:45:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4982b907-46b5-354a-9015-8676c0c436df | -16.46585 | -45.00288 | 2025-06-21 03:45:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19834766-9109-3bbb-a548-3934c381c10d | -20.95602 | -44.34231 | 2025-06-21 03:45:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f718d1ec-f307-3de4-b7cc-f3afeef18e01 | -17.57603 | -43.80492 | 2025-06-21 03:45:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 533307fb-9fd7-35de-bdf8-3ea60c1d841b | -17.77783 | -42.80678 | 2025-06-21 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88da20d0-54d3-3e31-a166-2a4b4ec74e13 | -15.71762 | -48.36306 | 2025-06-21 03:45:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c4afb25-1fdf-3abb-ab8c-e6ab2cb296d3 | -14.22334 | -45.51033 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f77acfd-992b-3a8f-9ce9-3936cb712467 | -15.77164 | -43.26994 | 2025-06-21 03:45:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| aa39b5b1-b1c6-3219-8869-fe87a58e38df | -16.68031 | -43.88521 | 2025-06-21 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b148544e-fb15-33b8-bac2-c02c0522166f | -14.80894 | -48.47918 | 2025-06-21 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb2c8314-132e-374e-85e6-6212f0eb2c51 | -13.23893 | -49.83919 | 2025-06-21 03:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c295a8f3-5ecd-32f0-977b-b10e6f965945 | -14.22221 | -45.51622 | 2025-06-21 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
