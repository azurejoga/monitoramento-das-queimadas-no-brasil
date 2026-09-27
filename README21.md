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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea3e98db-5bae-3431-a145-ea7ef0e63bf5 | -14.80726 | -45.96336 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0435b4a1-1a83-3d83-a364-cb83666cfa0d | -11.88072 | -50.52034 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12674b7a-7307-3b71-9588-ac003c85d90f | -12.92568 | -43.20151 | 2026-09-27 04:10:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bdfc3dfa-cc88-3c7a-8a97-08cdeedb6ad2 | -12.30721 | -50.29984 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1b63df1a-88df-3a8b-8286-408b56dd3110 | -12.28613 | -50.2988 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| bec0d7ae-d9af-320e-b560-7767ff552edb | -11.0472 | -51.75449 | 2026-09-27 04:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbf54ca7-7976-348b-b4f5-871205680518 | -13.33354 | -46.80365 | 2026-09-27 04:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbf78bc1-fd76-329c-9fc9-c2734a9acccf | -15.14517 | -48.50264 | 2026-09-27 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e76e36a-d555-3584-850a-8f1053de5b7d | -15.42096 | -47.91077 | 2026-09-27 04:10:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 987a39b3-ba3c-37aa-bc4e-784096441a46 | -14.7969 | -45.95668 | 2026-09-27 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d685766-48b9-3bda-b62d-08d06a765257 | -12.69068 | -47.31527 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3611f35f-25db-3c47-9c7f-0c639a022142 | -12.29277 | -50.73927 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a9aac27-c1bb-3de5-9db7-e03df086a046 | -11.26977 | -54.44061 | 2026-09-27 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16d7ddb6-e3a8-3287-87ff-73e53bb5cad0 | -13.20917 | -42.22837 | 2026-09-27 04:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c674e295-f346-3bfb-9d57-8ed4f82c51b2 | -12.70327 | -47.32079 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1416d14-bb97-3a08-ab33-d95a2530e4a2 | -11.7745 | -51.02393 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bfad804-507d-3644-b987-75366363fe8d | -12.65931 | -47.29742 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5efd99e8-4879-3c7e-8559-5de2b3f3b2f6 | -11.94177 | -50.51086 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97f5e4ca-370b-3cc3-be10-f6d1c9503369 | -15.8145 | -42.61386 | 2026-09-27 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| da63cca4-f925-3d86-ad43-0899fb078d07 | -16.78487 | -39.42762 | 2026-09-27 04:10:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aaed5d30-baf6-3d75-a6d6-1ec18926304d | -12.29254 | -50.40457 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c665f3a7-0684-394f-aaa0-65735ee001c2 | -13.3414 | -51.34315 | 2026-09-27 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5bbcc19-2854-34d6-a876-66ba7e6c80fb | -13.27896 | -46.73104 | 2026-09-27 04:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09566c6f-b380-3c42-8c03-ab59a8fc2516 | -12.29315 | -50.4014 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f41a42fb-e66f-3937-a833-e7db5d8e4cec | -12.68581 | -47.31839 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97604241-9e23-3feb-90bb-69f55e5f246e | -16.67093 | -44.65963 | 2026-09-27 04:10:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00931595-ede4-3913-84a3-8e1e2c9fb8e7 | -11.8968 | -50.51869 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 76972b4e-08a4-359f-bfb2-7b6ce0d6907e | -12.68166 | -47.31742 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9446285-b4ae-3071-95e0-42b6811f1b20 | -12.27528 | -50.29985 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc0f5e20-ae09-3f28-a473-e20a0ad9616d | -18.79075 | -46.47071 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 256a5130-2445-32df-8d00-973299af6a6e | -14.95878 | -47.53591 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e6762f14-b641-3a25-b4f5-a64a818128ef | -13.70612 | -43.66259 | 2026-09-27 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6b3638b-a192-3124-b638-9c6b25808a4b | -17.83175 | -46.5643 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5b7d1c07-aa83-341b-90c7-f8ff43da8f93 | -11.97182 | -50.58178 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2eadfaba-a6c1-3e0c-bb55-843ac78fa589 | -11.57259 | -50.51481 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 684dd87d-eae7-3626-9af6-c8510e6eea8e | -11.77382 | -51.02749 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b449836b-07af-3b45-a70e-bf521f1fee18 | -12.30781 | -50.29672 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0f82bc19-1e99-327e-a559-c767fa8d9fed | -11.65784 | -46.76744 | 2026-09-27 04:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b5e4a3-0483-3e17-8692-81fc102a8698 | -12.66559 | -47.31062 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ddaeed32-7684-336d-a36a-3f3327da520d | -11.94558 | -50.57642 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e13474d3-bdef-32fa-a2b0-cb91a6117def | -12.29185 | -50.29672 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| a3d53523-04d1-3261-9564-ce60ad1a84ef | -11.27773 | -54.43599 | 2026-09-27 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 75e04b87-884e-3c3a-84f4-bf3584ce312e | -12.23404 | -50.70988 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be7f39c8-7206-3c37-98cb-c6f8d164f944 | -11.23625 | -49.85569 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1bf49940-45b5-301c-8a01-a285237d42b8 | -13.87734 | -49.03784 | 2026-09-27 04:10:00 | NOAA-20 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efff1015-778e-3b88-9c60-8fbb1054c7c0 | -15.47673 | -46.15659 | 2026-09-27 04:10:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7808c8c-b2fe-3efb-80ef-616b24430ea3 | -12.29065 | -50.30296 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d9a2e8c8-d183-337c-b4a4-ca090b5cfc1a | -15.72799 | -43.38192 | 2026-09-27 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf895405-fca5-32ec-b384-2ad65a4d7bff | -15.42438 | -47.91546 | 2026-09-27 04:10:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24fc5103-272f-3fcc-88ac-ddea7685aa4d | -12.02683 | -50.60432 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48b52344-ceef-34ed-80cc-4bb31b838b6d | -11.93425 | -50.55016 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91eb44df-1b12-3906-ab8d-346abd287bce | -14.99312 | -46.65718 | 2026-09-27 04:10:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e14ec622-ea61-3f74-89d4-7642f9956ec7 | -11.93132 | -50.50873 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9931523-16e7-35b6-a568-242e2ae94fdd | -13.68118 | -41.88876 | 2026-09-27 04:10:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 64a78c9c-816b-313e-920f-6190057d6160 | -14.09715 | -46.32619 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4088f870-33c1-39ce-a296-0ad55a268bd1 | -11.7718 | -51.00857 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77a35bc5-e760-3806-92cf-481685641c45 | -18.55091 | -43.58048 | 2026-09-27 04:10:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fd6d63c3-4aad-3743-87c4-4834498b545d | -11.89744 | -50.51541 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 809b10f2-5ff2-350d-a27a-200822e55351 | -11.94621 | -50.57313 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fdf9346-08e8-3361-8352-29c17ad6c2a7 | -14.79609 | -45.96127 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daca97e4-d111-30ef-9433-1106785812b2 | -14.78945 | -45.9553 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b20e005-2142-3875-87ff-bbcc35db34cc | -11.92547 | -50.51093 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bc87699-9e11-352d-9152-ebfcc6a8b94f | -12.46957 | -47.48034 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f05a9e81-56d1-329f-891d-f2480d1aca7d | -11.9424 | -50.5076 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1ae13d2b-4cab-3d7c-a0d6-7f28c77632d5 | -12.67805 | -45.03986 | 2026-09-27 04:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2e43c38-7ebe-3f5e-81f1-af05e4607525 | -14.11624 | -46.33041 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e21843b5-d5fe-3e40-afdc-45271f9ad9f2 | -12.27532 | -50.69413 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d18ffde-76df-34c1-8364-d66a85026ce1 | -12.03271 | -50.6021 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 37f5d40b-8a74-3e18-b375-6fc94803a863 | -11.85978 | -50.51609 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1715bca4-a4de-3535-897d-27fb92dcb9ed | -11.94075 | -50.54465 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9910cf76-fcae-3947-af29-6f89eba528d7 | -14.81462 | -43.30829 | 2026-09-27 04:10:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9dd90b4a-d645-3425-a25d-9ba39f2e7473 | -12.28553 | -50.30192 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7401e383-a388-3ae5-82cd-2ca67e2d8705 | -12.29463 | -47.17502 | 2026-09-27 04:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7384f09f-76e5-3f65-beb5-763a6633d9e8 | -12.18293 | -47.38331 | 2026-09-27 04:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bab4120-40af-3cd4-88d3-c8da28806c06 | -15.47381 | -46.15127 | 2026-09-27 04:10:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34624f40-ac18-3400-bf2b-0b6eec5697ec | -11.97884 | -50.57064 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b778fbc5-75c7-331a-9f35-bc6a0795835c | -23.00248 | -48.61867 | 2026-09-27 04:12:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 576a22a1-4f21-311b-9003-1dc3b0704995 | -23.54409 | -46.3487 | 2026-09-27 04:12:00 | NOAA-20 | POÁ | SÃO PAULO | Brasil | 3539806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d7508955-bab8-3c4c-8c39-c751a70e73bb | -19.9069 | -46.89602 | 2026-09-27 04:12:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 986eb23c-42da-37f8-af82-d32b2bb305a8 | -20.44754 | -47.46364 | 2026-09-27 04:12:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1dcd7750-09b5-34a1-b26f-1113529d134f | -19.87799 | -44.05291 | 2026-09-27 04:12:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 74df77e7-516a-3282-bbe5-425bed347384 | -22.83028 | -47.18102 | 2026-09-27 04:12:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c96c625-9d78-370d-a2f9-9cb92eb7fdca | -21.52611 | -45.11301 | 2026-09-27 04:12:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c652131a-0211-313a-b5eb-98461655e1b0 | -21.52547 | -45.11683 | 2026-09-27 04:12:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b94633cd-7780-3ef3-9cef-1515c56a2f7b | -19.96559 | -41.05855 | 2026-09-27 04:12:00 | NOAA-20 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 53e22a64-e8d2-31c4-b205-719284aa1a45 | -19.64018 | -49.68895 | 2026-09-27 04:12:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3984ecf9-ad16-3e8c-8431-806e4821e74b | -19.53958 | -43.87506 | 2026-09-27 04:12:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4d4a590-c69d-377c-a94f-d6f756f1083e | -19.63935 | -49.69328 | 2026-09-27 04:12:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b3c62e0e-f95e-3bd0-93aa-bca6d41628f4 | -20.46469 | -46.41554 | 2026-09-27 04:12:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 286f9f3d-681c-34de-ab2e-d44d8ef02269 | -21.08882 | -49.06405 | 2026-09-27 04:12:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 45be770f-ae25-3341-9107-13beb1aa574c | -20.68958 | -47.52355 | 2026-09-27 04:12:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a5a5d22-8ffa-3ab9-8c3e-bf5a9a2fb266 | -20.85287 | -49.06989 | 2026-09-27 04:12:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| b445fca8-194f-314e-97a2-dd66c72b2c50 | -21.08807 | -49.06791 | 2026-09-27 04:12:00 | NOAA-20 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 03370a98-59fe-3829-a706-dd74c83bab87 | -21.39612 | -43.86693 | 2026-09-27 04:12:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 53ba688d-d121-3456-8891-5e21700ddad4 | -18.79634 | -48.04821 | 2026-09-27 04:12:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 514e4959-c85a-362e-9c62-dbe83cff6b66 | -20.85359 | -49.06606 | 2026-09-27 04:12:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 1aabe223-7aaf-3d33-a7bb-26ebda10d3a7 | -19.96905 | -41.0591 | 2026-09-27 04:12:00 | NOAA-20 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 68428b62-e193-3536-a27d-0241d2f3b820 | -23.00534 | -48.62463 | 2026-09-27 04:12:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cc6f827-4c7b-3715-b8b9-6c965a6c8300 | -21.39672 | -43.86323 | 2026-09-27 04:12:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a17d641c-bd53-3db0-9b2f-249252d4ebaa | -20.03892 | -40.74826 | 2026-09-27 04:12:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)
