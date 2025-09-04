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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbd54c6c-2255-3d47-9f80-d23dc8366478 | -11.0381 | -45.1256 | 2025-09-04 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 9d573cb1-d757-310f-b781-e11dc624c2ab | -17.1888 | -46.261 | 2025-09-04 03:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ca78dbf9-17c4-3bef-906b-34a0f263d455 | -6.7504 | -58.7268 | 2025-09-04 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| afe409ed-d72a-3fdb-b6d8-322e0f82f562 | -11.6838 | -57.3319 | 2025-09-04 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| cae39709-bcc0-3a16-a79e-1c0f38cd89ce | -3.13567 | -40.07005 | 2025-09-04 03:13:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aeda2b31-21af-38bd-b093-6da7cc373eb5 | -8.60985 | -40.31369 | 2025-09-04 03:15:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| da2fa6bc-e46b-3eb1-ac8b-5715c2267a20 | -8.60706 | -40.31432 | 2025-09-04 03:15:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 058f96bf-3387-354f-a5d4-42bf70b39452 | -8.61094 | -40.30796 | 2025-09-04 03:15:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 20682412-9b08-362f-836f-4935087ddd88 | -8.60819 | -40.30857 | 2025-09-04 03:15:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 021b9393-979d-355a-8e06-0a7f2e1e852e | -20.57304 | -42.23597 | 2025-09-04 03:17:00 | NPP-375D | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| fafc5fed-b88f-3038-b679-75b25f7d51c1 | -20.09874 | -44.13677 | 2025-09-04 03:17:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 348246d7-a116-3a16-89ca-83c270beaf13 | -20.36767 | -43.62434 | 2025-09-04 03:17:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6d7d6832-09be-30de-b0c0-f304a750298a | -20.09675 | -44.13797 | 2025-09-04 03:17:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dd3e52be-d7a9-3c52-b74f-4087347c7739 | -20.25049 | -42.02332 | 2025-09-04 03:17:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4254ed28-332b-3885-b133-2e0f1feb4563 | -23.3991 | -46.845 | 2025-09-04 03:17:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8b5ab63b-9f5e-3b1a-abc7-24bd011ba3d6 | -20.47097 | -42.45628 | 2025-09-04 03:17:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 474d906b-e54e-3d09-b282-61fc86abcb45 | -20.08969 | -44.13792 | 2025-09-04 03:17:00 | NPP-375D | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bfed4103-d991-3c9e-a4a4-0373f0e66dfb | -20.46497 | -42.45462 | 2025-09-04 03:17:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3cf386a9-178d-3e2e-a02f-14fa6dde266a | -14.32326 | -42.95296 | 2025-09-04 03:17:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1b7db40-24ab-35fd-bf87-bbebaa5ab1ad | -14.3264 | -42.95959 | 2025-09-04 03:17:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1b92bb8f-e502-31a4-9f27-12912592fba1 | -14.33018 | -42.95468 | 2025-09-04 03:17:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ced4b7ff-c230-3761-8b6e-e5c21c4bf51f | -20.36924 | -43.61761 | 2025-09-04 03:17:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4c6e5b3a-3e89-3012-8796-06271e014ae2 | -20.57197 | -42.23489 | 2025-09-04 03:17:00 | NPP-375D | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 032cd8b5-ce5f-3a9c-bcf4-1a4ebaf24f9d | -20.57111 | -42.23869 | 2025-09-04 03:17:00 | NPP-375D | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b8cf7e43-4aaa-3dde-96c4-304772a237ec | -20.09175 | -44.13639 | 2025-09-04 03:17:00 | NPP-375D | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f0715a77-7a80-3b76-a3fb-789f2e33c615 | -20.57216 | -42.23975 | 2025-09-04 03:17:00 | NPP-375D | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| c7a4d15c-26c0-3464-af4d-b212c6248442 | -14.32798 | -42.9526 | 2025-09-04 03:17:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7669aa7f-a0f6-373d-ae94-6944fcf9fe98 | -22.91483 | -42.42511 | 2025-09-04 03:19:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4fbc7c9d-3da0-3a57-8e09-0c1afc162747 | -22.90934 | -42.42655 | 2025-09-04 03:19:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 006a5f5b-8f8b-3c0a-9414-9f9c97f70e1a | -22.65572 | -43.69345 | 2025-09-04 03:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 97c0b84c-f848-3cea-a6f8-24fe53bcf323 | -22.66227 | -43.69359 | 2025-09-04 03:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 9fd1222d-33c4-315f-8a03-ab5b0ab33944 | -22.91603 | -42.42391 | 2025-09-04 03:19:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c2de59e8-9209-339f-8cd6-ddb3e4a2fa8c | -22.91586 | -42.42075 | 2025-09-04 03:19:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| a61a953c-9c57-3b8e-8f18-20822be86a4c | -22.91132 | -42.41792 | 2025-09-04 03:19:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a39d74d5-43de-3b28-9c13-dbf2729aee35 | -22.7774 | -42.89738 | 2025-09-04 03:19:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9bd0ae5b-4038-35f5-ba76-51931421827d | -22.77587 | -42.8958 | 2025-09-04 03:19:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 81fc8fa8-62b4-355b-a52a-57b3d5b46c74 | -22.65714 | -43.68761 | 2025-09-04 03:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e12456cf-d940-3c83-b3aa-c6444ba6212a | -22.54913 | -43.56008 | 2025-09-04 03:19:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f2c85d47-540e-3e15-909e-de055bbbfd1a | -22.65075 | -43.68682 | 2025-09-04 03:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2a907194-fd0b-3051-8f6f-35e087f12cb9 | -22.54706 | -43.56891 | 2025-09-04 03:19:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 11e6b985-65a4-3def-9e20-cf260b7a6bd4 | -22.78174 | -42.8975 | 2025-09-04 03:19:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fe1c9837-bb41-3959-b481-38ad7fdbc4c6 | -22.91702 | -42.41955 | 2025-09-04 03:19:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a8341b26-2588-3901-83e3-7c803aa64a22 | -2.9619 | -49.365 | 2025-09-04 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 67300450-5d7b-35a3-9d92-c94f4c51c099 | -12.9009 | -56.9287 | 2025-09-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 24b86581-2255-344d-9fd3-38cc046be80f | -17.1888 | -46.261 | 2025-09-04 03:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2b8c82b3-8bd3-3464-b8c0-c5f33651d82a | -10.9723 | -46.8368 | 2025-09-04 03:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a38344ce-a659-369f-9ed2-46ce4994cc20 | -6.7503 | -58.7462 | 2025-09-04 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 27680ca7-2656-308c-ac2f-8675a4ea07f7 | -4.9951 | -56.256 | 2025-09-04 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 95939018-9dfb-338c-a070-2f2800d16d0e | -6.7318 | -58.7469 | 2025-09-04 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 454e7d2d-5067-324f-9f65-359a1980d308 | -12.9006 | -56.9488 | 2025-09-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ef352dbf-7aae-3a82-abd6-820ce91a79a3 | -11.6836 | -57.3518 | 2025-09-04 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| cb270115-20c9-3da1-b5d4-8c4767fbadf9 | -11.6647 | -57.3533 | 2025-09-04 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 00af5c27-0d38-3adc-b553-fceea3137d45 | -11.6649 | -57.3334 | 2025-09-04 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 51694dfd-e3c3-3159-a5f9-1a971c40c501 | -11.0381 | -45.1256 | 2025-09-04 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b8ec3bfb-71c0-3206-b450-6cc507699845 | -13.1079 | -57.1109 | 2025-09-04 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 066fbe3b-7a64-36d0-9538-5ec91f93c5d7 | -11.0377 | -45.1487 | 2025-09-04 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| f03ad28f-3da1-34e1-9676-ec01f7414885 | -11.0568 | -45.146 | 2025-09-04 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 639e808f-5cfb-35dc-a776-48d597014761 | -6.7504 | -58.7268 | 2025-09-04 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 6db374a0-fd24-321f-a661-d2b509d3752e | -6.7649 | -63.1292 | 2025-09-04 03:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d96be396-cffb-3054-bc23-a314594587f1 | -10.5746 | -55.4161 | 2025-09-04 03:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 3be62052-55ab-3cad-8619-c9b58b233050 | -6.839 | -59.3608 | 2025-09-04 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 64f23a32-9e42-32f0-be95-6f5202eaf4ed | -6.7319 | -58.7276 | 2025-09-04 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| cfd2d542-e5f9-3370-a68d-6931a4df3aff | -11.6838 | -57.3319 | 2025-09-04 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 08dcb947-129c-3720-88b0-8a3b822808c9 | -6.6796 | -48.4049 | 2025-09-04 03:20:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 45b3db3a-df95-3cfa-9e79-6639f9c4bd8a | -6.7465 | -63.1297 | 2025-09-04 03:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 89a5180c-bbf2-373d-b16d-3b17ce652a54 | -6.7319 | -58.7276 | 2025-09-04 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e6620c9e-32e4-3c0a-8a96-bc40ad14df41 | -6.7318 | -58.7469 | 2025-09-04 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 211ce4c3-e4e7-383a-b240-f863161bafb1 | -12.9006 | -56.9488 | 2025-09-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 43f4d7d7-a852-328d-b90e-f26bd7153ca3 | -4.9951 | -56.256 | 2025-09-04 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 29f56635-cbce-3a43-aa84-eaaeaf19f88b | -12.9009 | -56.9287 | 2025-09-04 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| cbc15724-cb8f-3f0b-923a-4236c7206399 | -11.6836 | -57.3518 | 2025-09-04 03:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| e3237811-b473-38b9-acca-db900b046d0c | -6.839 | -59.3608 | 2025-09-04 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bbd43b9f-c69a-317c-8332-c7e070338052 | -18.3278 | -50.974 | 2025-09-04 03:30:00 | GOES-19 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 46503f5c-91cd-3149-baa3-8d3cf5a3399c | -6.7504 | -58.7268 | 2025-09-04 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| f5822248-412a-3cf4-befe-442d62ff7cf8 | -6.7649 | -63.1292 | 2025-09-04 03:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 553a23a6-38df-3a9a-b71f-ff63cffcc669 | -6.7503 | -58.7462 | 2025-09-04 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 3d13de39-bacb-35e0-8614-f7d16ced6ae0 | -6.6796 | -48.4049 | 2025-09-04 03:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2ae5b324-4d0d-3a7e-a174-cd7ce591c5f1 | -2.9619 | -49.365 | 2025-09-04 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| de17b81a-b5cd-3390-80a4-309b85d0a12f | -17.1888 | -46.261 | 2025-09-04 03:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ceff4067-826f-3c4f-9d21-a2688cb92b5a | -5.89478 | -44.35335 | 2025-09-04 03:34:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36d84996-a65e-33c4-a35e-cb274522f6b4 | -6.28357 | -43.51783 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b978d80-4feb-35cb-92d8-420e3ffe8c0c | -4.9582 | -42.06863 | 2025-09-04 03:34:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 340e02b6-5da1-32f6-b87e-93817292e747 | -6.22075 | -43.54585 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64252dff-2062-3b9b-987a-220949419f9f | -6.24266 | -43.55264 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5afdf7c-db5a-37d0-8ecc-e0475d775f40 | -6.22958 | -43.37624 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4c54cbbb-8c90-3270-bc6f-6d8d416ce4bc | -4.78481 | -43.82317 | 2025-09-04 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e75d529-4827-3b1f-99a4-584f1d827eae | -5.98367 | -43.8207 | 2025-09-04 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc80e7d9-7107-39ba-b1dd-289ebd050c5c | -6.17154 | -43.32185 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 713b68f4-9b74-39f5-adf8-a513d259f7c9 | -6.20078 | -43.34523 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9be2162-ea56-39b0-9681-e345fac525fb | -6.23908 | -42.61313 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1a51c5b1-b172-3cc6-b583-3f8498ec72b1 | -6.21926 | -42.44989 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 954e512a-2dac-3498-b1b3-1fd99807aafa | -5.6043 | -45.02066 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 055b241a-fe40-3cb6-b803-f8f226776e86 | -6.27322 | -43.32004 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c927d89e-1fd7-3727-bad5-03b7dc161a92 | -5.78464 | -46.16621 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fab7e64f-1305-319c-873d-0ae05a6ecfe0 | -3.48526 | -43.3317 | 2025-09-04 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52c196ac-30e3-3feb-bf67-39cf707e0b8d | -5.70437 | -45.16785 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b74dc779-548c-3a82-996d-e2e845fd608f | -6.12353 | -44.14374 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9121dad5-632e-333f-8cb5-e482cc9154f7 | -6.21718 | -43.38171 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f62dfc2a-bafc-3b69-8e9f-73e9ea5efe5d | -5.69897 | -45.16185 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad0ce391-c1c6-3080-a98d-ae391d28f455 | -5.92303 | -45.55686 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README15.md)
