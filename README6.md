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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f38efb32-2ec9-39b6-be0d-7fff22e6f747 | -13.90479 | -54.66779 | 2025-06-01 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08efe61f-4129-384c-a05c-f46b3f40c785 | -11.42197 | -55.08913 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74759c67-43c0-3ec4-8bf6-0797db17afcf | -14.68802 | -45.12037 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da1386c8-72d9-33ce-8689-87ad1c6b8f6c | -14.69565 | -45.09491 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 657eadbe-9a84-3773-bb00-0828902f877d | -15.97559 | -48.28892 | 2025-06-01 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae426968-f81b-39b3-8f09-1bd018754b0d | -19.4692 | -44.29746 | 2025-06-01 04:10:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79cd162a-27f9-36eb-ac57-9a48ed6c9a5a | -14.68128 | -45.11919 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77b99fdf-370b-3a7c-9ffc-dcaf7a7273f7 | -15.89504 | -46.01323 | 2025-06-01 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf27009f-4620-3439-bcf3-d1a3eb67f25a | -11.08525 | -54.78363 | 2025-06-01 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93010371-a3d8-3053-a5c5-98549d519fa8 | -12.77019 | -44.4123 | 2025-06-01 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a9f095f-26b9-3c0f-96db-2c70feff3a0e | -13.09191 | -45.26736 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a46e6b5d-b1bc-3ce4-8dcd-1ad3262ea50e | -15.0628 | -43.86871 | 2025-06-01 04:10:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7812856d-219b-365e-981b-a8c5c129dda8 | -14.68465 | -45.11978 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 555e026d-ae9b-3e4a-a85f-7bef3e8f7bc2 | -13.10093 | -45.2768 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d90865ec-124a-33fc-be9f-21c1a95ed5a3 | -14.45961 | -48.45273 | 2025-06-01 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 495a2613-a925-3b6d-8429-dd388d4eabb7 | -11.07356 | -54.77634 | 2025-06-01 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b174c9b-55ea-3110-a373-de5d394f5bfc | -12.72132 | -54.97452 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 64cb0dfa-fc89-3976-bfe3-67335000553c | -14.60656 | -47.96557 | 2025-06-01 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdd5066c-0069-3e0f-a86a-141a7d70aa56 | -13.91162 | -54.66488 | 2025-06-01 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18ef5f2f-adf4-38dc-96a6-9857403bd5af | -14.69538 | -45.1178 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7888eac5-4eca-3004-8dc9-937675044941 | -13.09407 | -45.27562 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad5a4d38-8dba-3022-b1fd-623748fb4bec | -14.69228 | -45.09431 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2634966e-aebb-355a-b523-07259fecd090 | -14.80954 | -48.36903 | 2025-06-01 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f96fa2c9-a867-33d5-994c-f2abff09211f | -13.09127 | -45.2712 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17ade623-67c0-37d7-befe-38192fbe9fc5 | -19.97148 | -44.21429 | 2025-06-01 04:10:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cf4227a-8922-3d42-88ea-52201fcbd8de | -12.46101 | -54.91587 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95f66612-dffd-30c8-9c60-f8a85fea11aa | -15.89779 | -46.01355 | 2025-06-01 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f55acb7f-ce3b-3e40-bc9a-4a4325f908fb | -11.8276 | -51.27592 | 2025-06-01 04:10:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de845b6d-61fa-3071-8bd8-00846895bc51 | -11.4381 | -55.00964 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dd5fd0d-f45f-3391-abda-a5e89a10e11f | -14.6733 | -45.12549 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 700c347f-3700-302c-a289-7e577bb6e24f | -14.82527 | -48.09744 | 2025-06-01 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fe6df99-7b95-3ab6-89b3-8bf6ce4e10ce | -13.10843 | -45.27416 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8a15325-557d-31c4-b324-5da4db82543a | -13.64164 | -52.1813 | 2025-06-01 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 745cfc43-9e41-3b02-b42b-9b63d6aaf075 | -12.12511 | -54.59538 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a9e0c3ad-5ee5-3e08-a664-0ed269968975 | -14.65016 | -45.41536 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26055706-c7a0-33c4-a3ec-5c74d7957a50 | -22.67709 | -42.85384 | 2025-06-01 04:12:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40284f8c-d282-3586-893e-c7c135d5f78a | -25.19127 | -49.32795 | 2025-06-01 04:12:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a927ec29-b4d7-3a05-a9a6-68a9f79f2a0c | -21.15961 | -47.14305 | 2025-06-01 04:12:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5355c3d7-14d5-3330-9937-a865d780f0d3 | -20.31125 | -45.58204 | 2025-06-01 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c205608-bb51-32c5-9746-235faa930799 | -21.15366 | -49.23445 | 2025-06-01 04:12:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 815b17df-ef2b-362b-aada-ccf7d0c0885d | -22.93648 | -46.53244 | 2025-06-01 04:12:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5af3f664-891c-335a-a3c7-411139ee8864 | -24.93579 | -49.36657 | 2025-06-01 04:12:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ad1a40cd-8056-3eca-908f-9936e09defa4 | -20.31397 | -45.58631 | 2025-06-01 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45ab5cf0-7472-3094-b9f6-7ade64b5c604 | -21.1603 | -47.13905 | 2025-06-01 04:12:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af661a54-6575-3e9b-91dd-5136bb84cf85 | -23.34019 | -46.77246 | 2025-06-01 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d160dc9b-ab90-32d9-9fa4-6d3996ab6ef8 | -21.62526 | -45.85956 | 2025-06-01 04:12:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 78014451-1149-3323-b1a0-0e0f6858347b | -20.4555 | -44.18253 | 2025-06-01 04:12:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 43028400-7e03-3760-97c1-04cd6924dc00 | -21.19624 | -44.93674 | 2025-06-01 04:12:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b55b939a-1855-390e-b3cd-a866a286dc57 | -20.76484 | -46.76803 | 2025-06-01 04:12:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 01c19566-765b-3e8a-9e65-21655017d59b | -22.78567 | -43.75866 | 2025-06-01 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cff43691-39a4-3d3d-884f-ab01b8723865 | -22.54175 | -48.81515 | 2025-06-01 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87eda342-6e4f-3add-a3a7-9f1d52c094bd | -23.36124 | -46.74899 | 2025-06-01 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4dca8ac-3767-348f-a4de-8c157d5d40fa | -24.9402 | -49.36271 | 2025-06-01 04:12:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6e6ec3d8-4e2c-3b06-843e-18bed5407c5e | -21.16019 | -47.14005 | 2025-06-01 04:12:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70e32f4d-e4cb-3dbb-8523-c6e075bec5f6 | -27.66395 | -48.70386 | 2025-06-01 04:14:00 | NOAA-21 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6f401d31-2105-352f-9ff3-fc28dad6e38c | -30.15173 | -52.02549 | 2025-06-01 04:14:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| b44aeeb3-8020-320a-92b0-f257d05eabe3 | -27.03762 | -48.79937 | 2025-06-01 04:14:00 | NOAA-21 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8ea71e7d-3a32-39d3-a850-7f4873f40270 | -10.46757 | -47.9425 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 901224b7-466d-3c55-832a-29c1eeffffdc | -9.33602 | -40.28798 | 2025-06-01 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6cc8af99-a19c-3459-ad97-3ef58962614d | -2.58511 | -51.92462 | 2025-06-01 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73de7fc5-6550-3162-9153-07d3a3f28b5c | -8.67075 | -46.63759 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bbd8241-4ed9-3c96-b142-318465be3048 | -4.80913 | -43.22667 | 2025-06-01 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efc789ca-6155-3f73-b6ce-f7f94cb68d92 | -5.41622 | -47.56922 | 2025-06-01 04:34:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90ef3772-4dc2-3105-88e0-da5a17ad0bc2 | -7.58208 | -45.86482 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efcb20c3-6fd1-31cb-a6c8-06e678283b74 | -8.68388 | -46.64345 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc5e822d-928f-3bf8-aca3-7a43d5e7bddf | -9.27428 | -50.65845 | 2025-06-01 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 526dbd2e-4a33-3b0f-a29a-268a7afab237 | -10.47036 | -47.9466 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0638e42c-ad00-38b9-9ecd-c6e496be7161 | -7.2254 | -43.12185 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56bca59f-5818-3c13-a671-90d0445e8bc1 | -9.34245 | -48.9458 | 2025-06-01 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da7498b1-6a49-38ba-bb81-918e9a3c4db2 | -8.67418 | -46.63812 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1634726-d3d5-3ebc-9444-a2792a3d207d | -7.09511 | -43.16366 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9da9e57-41eb-30c7-85c0-6f0c7580effe | -8.7074 | -50.03801 | 2025-06-01 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc21c8f8-5cc6-31ea-a6a1-8f48e6d920d3 | -9.40323 | -48.94469 | 2025-06-01 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16406a08-4ae3-3f4a-8a24-3868cad66ef0 | -5.0577 | -43.2511 | 2025-06-01 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e087fce9-8d26-3a63-b75b-f9dfc67d487c | -6.86827 | -47.84065 | 2025-06-01 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96621171-1667-3692-ba42-9605720410e5 | -2.37596 | -51.87698 | 2025-06-01 04:34:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89804a05-070b-34b2-8c7e-afc23efd03f4 | -6.63499 | -47.34677 | 2025-06-01 04:34:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42517402-a507-3101-af73-d9b850527348 | -2.37541 | -51.88045 | 2025-06-01 04:34:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95c71304-7636-3135-9426-349e52309298 | -4.48516 | -48.86226 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e051523-d6c2-3f63-b762-3a1a8e53aa14 | -8.67303 | -46.6456 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 534884ee-89d2-39c8-b241-b5af1937a6dd | -10.47261 | -47.95425 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c92bf78-e64d-3c08-a202-c0753bdad72c | -4.48459 | -48.86586 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d67f595d-8f55-3c8c-bb05-08ac599a09b9 | -6.44723 | -45.72657 | 2025-06-01 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e206f3-1580-3900-a6c0-3e5a389bba5a | -10.12179 | -47.20029 | 2025-06-01 04:34:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd339a12-1230-37b4-9029-de7e864d2c9f | -6.49506 | -47.48235 | 2025-06-01 04:34:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2197566-d1c3-3a67-b116-fa1aab31520f | -5.68422 | -46.57438 | 2025-06-01 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c12ec1cd-117b-32c2-b065-a9d1cccb63a8 | -8.72638 | -50.26536 | 2025-06-01 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8f21c13-80d2-3d43-9b57-e9e388a5d59a | -9.12439 | -47.98921 | 2025-06-01 04:34:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62bdf7b3-7c66-3e18-8332-a86ab1225ba2 | -8.42654 | -49.10858 | 2025-06-01 04:34:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d3e9725-b56d-3622-8b2b-d18d06ce5b46 | -9.8467 | -49.34166 | 2025-06-01 04:34:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25a48410-4419-3199-81f9-a952c4ca4ad9 | -6.27358 | -44.20704 | 2025-06-01 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 837c1279-af42-3823-b26c-166f75269c37 | -4.48449 | -48.8691 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f670ef0e-f3f5-3336-9d33-a30a50faca20 | -9.04711 | -47.02629 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c639725e-03f2-35df-8a43-ac176d6b62ef | -7.24418 | -43.24688 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 40ab9a7d-588f-3078-91e6-9bd42606e857 | -6.17934 | -48.06952 | 2025-06-01 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d17ddd1-ad99-39db-bb32-45530145243b | -6.68653 | -55.199 | 2025-06-01 04:34:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f476968-9479-3041-92cb-d275fd598ab7 | -7.21984 | -43.13183 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fd67e5fd-ca97-3427-9786-da235b3206c1 | -7.58557 | -45.86537 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c5c0a0a-34c9-3c7c-bd14-9b785678cc9b | -8.6736 | -46.64186 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5ac38b5-71f1-3c82-b430-7081d677a22e | -7.27984 | -42.91798 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README7.md)
