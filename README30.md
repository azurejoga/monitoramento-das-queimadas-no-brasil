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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 501ee1ad-99ec-3913-b0a3-45c6d7187148 | -10.88568 | -55.78604 | 2025-08-25 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89e67f16-d55c-3d72-8232-9bff04fa0690 | -10.41673 | -47.16489 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf2fb32b-0cf0-3788-9c06-801bd1d81f7d | -12.99303 | -45.22299 | 2025-08-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 976e0e12-c50c-3323-977d-8ccb129b2db7 | -21.56228 | -42.25319 | 2025-08-25 04:17:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f8b65a4-78b3-3c27-b829-00844af5ceff | -15.09342 | -48.70934 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe660279-ae43-3e75-a833-57d03c4ade10 | -11.13164 | -44.79527 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bbaef37-534e-33ea-9a5d-111b299f30d8 | -21.5936 | -43.90535 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4d0fcebc-6bde-3a6d-bc08-2e0dacdcc7c1 | -13.05816 | -46.32198 | 2025-08-25 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 155ed102-9709-3ed4-8b4e-be15aad430c5 | -13.4576 | -47.01373 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b035d508-0e4f-3d7e-899a-fa3704fecb95 | -11.59607 | -46.36618 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41e3fbd2-0591-3cdf-88f0-d29afeb1757c | -15.49807 | -44.41316 | 2025-08-25 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3d3bc6c7-5c33-3fc5-9838-08d97a251805 | -11.26587 | -44.9791 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11a5094b-a848-387b-a833-9195b414a695 | -13.45286 | -47.02094 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ee864e0-5a71-363d-a4a3-22a08c1bd5b7 | -15.0359 | -48.51629 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a80b4c2-b12c-3a15-ba1f-6981447bae07 | -11.92648 | -46.72949 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 547245c0-d827-3e90-b339-77d1fe41a57d | -13.4291 | -46.91061 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 65c688c5-0178-34b6-adec-fa69c4476835 | -21.63116 | -44.02414 | 2025-08-25 04:17:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| eb547ddc-167a-36e9-acf4-c5671373d899 | -10.72166 | -47.12088 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f35e773-3d5c-3798-9c1e-8a0adc11e183 | -13.42972 | -46.90685 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d29ed763-fde6-37d7-b611-71769bcbd65c | -19.94536 | -50.44147 | 2025-08-25 04:17:00 | NOAA-21 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0a4e39f1-9bc0-3bbc-8440-b449af88fe22 | -13.45709 | -46.91154 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 439b8e44-d61e-3261-b74a-730fe0badc0a | -9.70837 | -54.9818 | 2025-08-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 669a31ca-04c7-3d2f-947e-f20814bfce8f | -11.26475 | -44.98616 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6dbbc85-29d0-3aac-b097-b30e9168ed83 | -22.18173 | -46.63116 | 2025-08-25 04:17:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 33aa682a-0316-373b-8d26-b9ad3ed0a5aa | -11.14819 | -44.79793 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c9d5f2e-b939-3fcb-acaa-a08175b62801 | -10.58503 | -47.13715 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a40ccc4e-1148-3a5b-8ebf-96070233ef51 | -20.29951 | -47.18017 | 2025-08-25 04:17:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97305d2a-739d-3d56-8e10-a5e1f096f923 | -10.6077 | -50.13972 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 855bd21b-586d-3b00-8650-e87963ea6e3d | -8.86435 | -52.04203 | 2025-08-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b3d663f-5dc1-39d5-9f3e-d6c2faf4f4f0 | -20.38804 | -46.73096 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 53b12b88-53f8-3eaf-baae-10c45714522d | -12.7287 | -48.14075 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e78828ea-442d-30c2-b553-e08ab91066ad | -11.6128 | -46.23858 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8873206b-6499-3319-94d8-2a882fabb8c2 | -14.33691 | -51.96272 | 2025-08-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7607fdef-eb45-3872-b2ab-a132440d102a | -22.54666 | -46.82065 | 2025-08-25 04:17:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7b1c910d-69bb-32a2-b1ad-5cda4a988960 | -14.12658 | -49.12634 | 2025-08-25 04:17:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dd58245-3125-3abd-9c91-da951daa0a5d | -15.13658 | -48.15415 | 2025-08-25 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 192e84ef-bded-336d-8269-652adee74ae1 | -14.92447 | -45.5288 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67ddbc9f-7cb1-3e07-98ce-ab71c28604d5 | -11.61706 | -46.23884 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cb2190f-39b7-3806-b27d-eab0b3c3a312 | -11.09415 | -44.77482 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fedb575-1bac-3842-b786-1dde26550357 | -10.82324 | -48.32989 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffbeabaa-b096-321e-a1b2-a3cebd5cd0a1 | -20.98575 | -45.48814 | 2025-08-25 04:17:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2390fa9-852e-374e-a3b8-fe2e82522e40 | -11.63589 | -46.23042 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 859c9353-2998-39e5-a825-a0572528f604 | -10.71571 | -47.33135 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d10a45df-70f5-3c29-a29a-77cdaf644df6 | -13.45767 | -46.90805 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9142dbb-3a4e-355f-b1eb-09796da11283 | -10.72588 | -47.11747 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf2b8e22-2a2a-3242-8638-fd6d4fe47220 | -13.43065 | -47.0303 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb7b4c0d-d97b-3ec3-853f-775eeda384b1 | -15.14421 | -48.6358 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d5fd172-d804-32ac-9b75-24164bc2cd30 | -21.2984 | -49.94098 | 2025-08-25 04:17:00 | NOAA-21 | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fcd4d99d-b8a1-3285-9ec1-2a31e005b46a | -20.54373 | -41.68801 | 2025-08-25 04:17:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bda7b4a2-49c9-3609-9ec7-49fc259bcb04 | -11.28758 | -44.9284 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fcb5e5a-d01e-3823-a11d-f46a9d9696cd | -9.70763 | -54.9857 | 2025-08-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7e86f56-1930-3cd1-b1ff-975044ca9772 | -12.75663 | -48.10884 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b8e3b6a4-0cc4-358f-9254-20d0ab52a3ed | -14.76176 | -55.92389 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b66d86a6-e425-3134-b6d4-14bec3490e9e | -16.80978 | -49.52776 | 2025-08-25 04:17:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83954f21-40ad-3529-958d-2e7756eff10e | -13.46171 | -47.01029 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b68b9f35-7cd2-3597-abf7-6f42868c26d0 | -12.98916 | -45.22599 | 2025-08-25 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77f41c6e-b796-322c-a6d9-2eda85d52de9 | -12.6871 | -47.83337 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23c4f863-9961-3b7b-ba2c-0d32d45afdb3 | -13.15461 | -53.74201 | 2025-08-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae596688-6a1a-3f70-99ac-c5d5cda81e36 | -22.48261 | -45.15858 | 2025-08-25 04:17:00 | NOAA-21 | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c7d0a940-893b-3af8-a0a2-1b298edce665 | -20.94695 | -46.83217 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f9c02e0-ef8a-3f64-a83e-269364a5ce08 | -13.61292 | -48.17956 | 2025-08-25 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e97ee8-aa5f-3cc7-8c91-0e958d3c7751 | -15.09059 | -48.68208 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 664fc314-7260-3b94-90a0-28eea2fb6a38 | -14.91175 | -45.54491 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2887b65a-8214-3607-bd81-abef8c70b343 | -15.6412 | -52.72565 | 2025-08-25 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 009ac723-5d5e-351c-96bc-9c69fb26dcef | -13.50803 | -46.90097 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc91103e-22a1-3a14-8440-613ba829cd3d | -16.68601 | -46.64328 | 2025-08-25 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4fc97e3a-3c26-343f-a17d-378055579570 | -11.39614 | -50.6819 | 2025-08-25 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaa02a4d-332e-3d2c-86f6-c10d15933c4d | -9.57133 | -55.37155 | 2025-08-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 922e9a15-0131-3115-b27e-54dd0a02fe20 | -10.60845 | -54.88367 | 2025-08-25 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa66901a-f954-35a1-be5f-031df1bf94de | -14.42877 | -56.46542 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2766e3da-2943-3b29-99e7-a3d3e7a8b646 | -15.14082 | -48.15068 | 2025-08-25 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 470037f8-fdb3-36e1-af8d-9da99356ae15 | -11.67124 | -51.58488 | 2025-08-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68985da9-cd48-32fa-ac0f-59ca1d015a66 | -16.4184 | -49.93915 | 2025-08-25 04:17:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b180c6cf-7b42-301f-93fc-ac27cc3701dd | -13.40151 | -47.54064 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b81c5928-fa83-36d1-93b0-ace8c132824d | -10.02903 | -51.07544 | 2025-08-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a73009ce-7ebc-3f75-bd28-65610006ff1d | -13.47262 | -47.00837 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0964f7d4-d658-3992-ad97-fb7180a754e3 | -16.85475 | -49.24678 | 2025-08-25 04:17:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3511d853-c09a-3cd2-b6a6-11ed0435bcd1 | -20.27108 | -46.6535 | 2025-08-25 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c375c943-d219-3cf6-8543-e44622c79e4a | -11.27194 | -44.9837 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4101e476-7965-3a5a-9d2c-92e512054573 | -15.14782 | -48.63647 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 055afb80-9dac-3c53-9c28-05056b948618 | -11.2875 | -44.9717 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a281a18-d858-3711-994d-9c8d9a710fd0 | -11.90461 | -47.13062 | 2025-08-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb5a556a-7372-35af-8f8e-2a460d0f4b1a | -13.43437 | -46.89994 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af770e98-617d-3973-8c35-71c58f6e1bd5 | -12.75359 | -48.12664 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6fa4b5a-43ec-3c3b-910a-7ab1b93fb5cd | -15.05396 | -48.51917 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d18326f0-c2dc-3620-a366-04b272f90645 | -14.25368 | -58.61778 | 2025-08-25 04:17:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55663fd4-14d2-3ad4-987e-0dac2318c534 | -20.37233 | -46.76588 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b10a48bd-f07c-39ac-b07a-b2f64b0b9b40 | -13.4015 | -47.51929 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2678bca3-77fe-3628-9bfb-997ed6df5361 | -13.65729 | -46.89057 | 2025-08-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a507f778-c457-3da3-8b3b-ae33a189c9fb | -19.93573 | -47.49316 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2976058-ecbd-3253-a939-43db3dc4e2c6 | -11.19617 | -55.04225 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1407252-ff22-3b97-a01b-02d92343fac0 | -15.12916 | -48.65299 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4351babe-87ca-3ec3-8df6-0247abafefba | -13.05479 | -46.32141 | 2025-08-25 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 364809d3-675e-346a-adf8-2b4e059b9f03 | -11.60998 | -46.23441 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05f31cda-b850-3c16-8278-1b529f2af92a | -20.55469 | -43.43227 | 2025-08-25 04:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8deb68e6-172c-3494-9b6d-d90f699d15c5 | -22.179 | -46.62684 | 2025-08-25 04:17:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 304ce833-2613-3e6f-9a3e-3069ae85ec7c | -14.71679 | -55.93526 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fb77e83-8ce7-3352-9c5d-e4aae059f6dc | -11.60694 | -46.36404 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74da8d9d-044c-35b3-acef-44858b8d210f | -15.03801 | -48.52576 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 280822f1-1bc7-36ec-9b0c-59fbd7439aa0 | -15.04077 | -48.16241 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README31.md)
