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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 613b31cb-1dfd-3b1b-8b47-6185fd30c3c3 | -13.02855 | -56.83498 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cad2843-c249-33b2-b11a-405189c1741f | -14.64973 | -54.92419 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb055425-348b-3626-a9e1-2bbb0e8f2eca | -9.94846 | -60.173 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2b6db1b-a57e-3d15-b199-fc11b68a8616 | -14.257 | -58.5414 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 142397d5-a6d7-38a0-b3b8-18fbdf5f4046 | -14.62232 | -54.8395 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce130458-e650-3f9f-af02-2b9a3dda4bda | -13.44124 | -57.17416 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e728fc4-a87a-371d-9c2c-59f363d4fa05 | -13.46711 | -47.02868 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| afcc2cda-aecc-35db-b1f9-16654ed66de3 | -14.69915 | -54.91393 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77a2e557-a589-376a-803a-3b45e4cee29e | -13.43419 | -57.17293 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9007854a-4067-30a6-ad2c-ad31d006715b | -11.19817 | -55.04001 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 313893d2-929c-3028-a778-2794bc504bce | -8.90243 | -62.43091 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 240faa41-5363-3707-82af-07545c91234e | -13.03618 | -56.83227 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b76d80de-d88c-300f-bc2c-9fc72dfa6b0d | -14.59935 | -51.9956 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78138703-58f1-3671-9b14-05e6435b3276 | -10.10672 | -57.76215 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5214da8-c23b-3d22-9e42-bc1f26274da6 | -14.35972 | -53.12238 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca73abcc-f348-3ebd-9850-9ba747f31b2a | -15.18561 | -48.11005 | 2025-08-23 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a8178f9-cc4e-3ac3-9c0f-7fe259a7fde8 | -12.97875 | -56.87534 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 342cbddd-e716-35cc-a621-76d1bf18ecfd | -14.80211 | -45.43606 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0504ae3c-7bc4-3b8a-8db5-3d4aa7e734b4 | -12.98442 | -56.88456 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da7ac2b7-86ea-39b8-971c-518e61e0543a | -11.54591 | -54.39474 | 2025-08-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aa5781d-d871-351a-87e6-408b352f2034 | -14.93958 | -48.00824 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c6949dd-6d48-3663-9595-9213c2b26425 | -12.50206 | -53.80445 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d203bc92-7f4d-374e-98e3-43bf9af7f518 | -12.96058 | -46.24472 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 494ca5f5-dfb6-3f9f-a3cf-6d5f85045720 | -11.32959 | -55.2211 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 838b2455-fa0d-3076-ac6e-234e2e3618a0 | -12.50758 | -53.81257 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8743efe-0919-3a9d-8868-47eb798355c8 | -10.62899 | -52.34458 | 2025-08-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e940cd30-5166-3868-b0ed-2bdc5f7d8c81 | -12.30413 | -49.99168 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15fc3d5e-ca58-3e20-849f-57e1b584789b | -14.66343 | -54.86063 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995090d3-accb-3bd3-ae13-fa6f327a8db4 | -15.71191 | -48.23306 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9968fdc3-b25d-3e57-9853-b34de818003b | -12.31865 | -49.99867 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 396b13f6-225e-31a1-83b7-0ace3146a0ca | -9.42715 | -62.25327 | 2025-08-23 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 882086cd-764c-33b1-a699-f3fecea7f243 | -12.79183 | -48.72059 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f733376a-85c4-3c7e-ba5e-92f28f8ad588 | -17.26836 | -46.76158 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 457803e7-9dcc-3dd4-9d98-98b4efb42bb1 | -13.4794 | -46.89488 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a37dc2c8-fea0-3460-bf64-a7394ec6a577 | -15.3079 | -56.17476 | 2025-08-23 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaeb369a-0e9f-34fd-b006-6a38e3189ea9 | -13.42208 | -46.25958 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b4006eb6-3ff7-3288-a572-14f9bb4ad39d | -9.50933 | -60.50749 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7661f75b-fded-3c77-8208-788f9b5a9f90 | -12.98159 | -56.87995 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc05b609-bfc9-38f2-9031-7a438fa788da | -14.57619 | -54.50391 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91e56bb2-8550-3a3f-9cd8-3371786eebd5 | -9.95436 | -60.19835 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 0ce25478-92b2-3ac2-966b-c1a8de5e1c9a | -14.66231 | -54.86773 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58c6f995-c1e0-3e77-a875-1fcbf913727f | -10.46107 | -59.1372 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f51f735-1859-3b15-929c-02d58d190b74 | -14.77592 | -45.23502 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6efce010-5ad0-382d-bda9-2f116d26e48a | -14.75795 | -55.99481 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fa48fcd-2f03-34c1-8b43-ca154c6a754f | -9.65413 | -59.63673 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd205cc4-1f8f-3803-b13a-3a0f843b8f3d | -14.7165 | -47.52004 | 2025-08-23 04:53:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8e4d0b5-9db5-3365-b4a7-d49b3d1f15fe | -13.32782 | -54.39765 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88a0464f-722a-3418-9aa6-20762b2cccbf | -12.48994 | -53.81697 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7523e37d-8484-37d5-9144-52156a50ca70 | -13.37756 | -47.50808 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b76edd5-1727-38fb-9120-c993c4426d53 | -9.95051 | -60.18694 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b0b2117f-f128-3b7e-9121-b6fd2c7bf5a6 | -16.49688 | -46.74477 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9028185e-1b34-3590-80fa-b421443f30bf | -9.46246 | -60.37054 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecfb8a93-8e47-39c4-928b-2f4e63c9c490 | -13.03815 | -46.32476 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ae59d7f-5045-3d40-8130-041904503f0a | -8.89134 | -62.43227 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e89d767-101e-3ab3-a64d-23739a5444b0 | -13.02224 | -58.00148 | 2025-08-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dea3668d-d47e-36bd-8f18-01e7ba3ca20e | -10.34531 | -58.60585 | 2025-08-23 04:53:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86a096bc-e1bb-3854-af28-e7fc5bce3250 | -9.95006 | -60.17036 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2aac743b-fed7-32a5-89f0-5b857336d31e | -10.62562 | -52.34406 | 2025-08-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15d943ee-ab4f-3a52-8f9c-47fc9235b4a4 | -12.79133 | -48.72434 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d3b1b5b-1588-377c-bbc6-953384a494b0 | -14.46174 | -55.93324 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 293268ea-bd86-33a2-90d6-0f5a1fd3400c | -15.19007 | -48.11068 | 2025-08-23 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85eee497-a56a-3831-8e66-0654d52ff488 | -13.34546 | -54.39328 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 837c0b22-7380-3f82-a231-7334905eaf88 | -12.99582 | -45.23574 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5baec0d5-370f-3c34-a8a6-ac6adf845abf | -9.51595 | -60.52337 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e0c663d-1307-32e8-ad22-4c35c428dbae | -13.1316 | -46.90903 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69f07805-d799-31d5-a73e-f93ba2804298 | -15.56873 | -55.00716 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e447e02-2b0f-340a-a42c-65eeeec719c7 | -15.07027 | -48.49616 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d2c89ed-afac-3b67-ae26-d2cf52f8f7d9 | -12.49877 | -53.82561 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba3057a4-4ff4-33e4-b43a-8fb42ebaffb1 | -14.37052 | -52.05355 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9df6f46-c011-3a3f-b969-da1b19fc1d6e | -14.65029 | -54.92064 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a686c3f2-0a97-3ea0-974b-52e72dbb492d | -13.4384 | -57.16946 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c9cdd5d-041d-3630-812d-06663ace50c8 | -14.74074 | -56.03711 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 044b517b-4b40-306c-80e1-c91043b63859 | -14.7435 | -56.04134 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a722fe5-fee8-3c39-8756-9d0a648e0ac7 | -12.70527 | -48.10114 | 2025-08-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b3f03cc-8211-3fd8-912d-cacc0ba68f35 | -14.61464 | -54.82366 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e44b023c-6134-3a05-b21a-040c49d30e76 | -9.21389 | -60.78437 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e47639b2-f1bc-3f3f-be57-6a56fb9aac4f | -11.18421 | -55.04142 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24fce8f9-64a2-3f24-8973-6cf2e320e2ad | -12.48827 | -53.80585 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7b12f95-5ab7-3af5-92fa-2b111582c59e | -15.63863 | -56.31053 | 2025-08-23 04:53:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b17e1485-9e33-3923-a6f2-8718ec5a99ac | -12.99057 | -45.23499 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4434124a-e42a-396c-b70b-05a12a4cb410 | -13.38178 | -46.21925 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b6e9ab5b-cd89-3c93-ba9b-a3c8a9c3b5a1 | -11.32288 | -55.21998 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b7d915d-ec72-3051-b0a9-c65a0febf49d | -9.95817 | -60.17632 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 641f0a5c-73de-3de3-8678-e41aafeb2216 | -9.96108 | -60.18595 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 94b3b9bb-37b8-3075-8840-84d6263e16c1 | -11.90286 | -55.89693 | 2025-08-23 04:53:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2bb39981-b2d8-3f58-b025-64e2ef11ed4a | -12.94361 | -46.30274 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d57b1985-a17f-3132-b3f4-a30a2a47d70f | -14.38336 | -52.06371 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da4bd3ff-7d64-3511-b5fb-9c8b443a1646 | -9.65836 | -59.63786 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4912d73-a46b-366f-a9b3-1115d01143a3 | -13.37468 | -54.40166 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c9825e-4bdc-3056-92f8-159ed9a01500 | -14.94853 | -48.00943 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c26f9d68-5b53-3091-bd10-637765d62c6f | -17.26717 | -46.7704 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 80672abf-f98d-39cb-b979-7856c77c6187 | -8.88083 | -62.43036 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10b4d1b9-30b9-37dd-9470-4d7005d66ade | -12.15729 | -60.76851 | 2025-08-23 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a21d0ec7-1ac9-32ea-acf4-fccac08eab12 | -12.50208 | -53.82615 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a1e0095-b1cd-3c11-86dc-3c2d7108576a | -15.55488 | -50.32059 | 2025-08-23 04:53:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1b743dc-39fc-3a35-a42d-6b99adbb5067 | -13.48354 | -46.90005 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cace9de4-4b9c-32e3-91d6-982eb492c5a2 | -14.26977 | -58.53425 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a1c48b3c-90a9-384b-99ba-b0ca000ebe28 | -12.54744 | -45.62382 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcabb2c7-b0ad-3757-9d62-7cbab16000d7 | -12.79234 | -48.71683 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28ec99fe-23b9-3259-8204-4e717c1af172 | -14.31366 | -58.55515 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README47.md)
