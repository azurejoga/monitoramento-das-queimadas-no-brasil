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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e535df3a-8d17-3673-9684-849ca74c911f | -22.37281 | -49.32812 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 2f7c1451-46b5-3348-ab0a-aad82af0aebd | -22.3723 | -49.32857 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 144e8077-9c65-3f97-bbe1-5b4e0212918b | -22.37161 | -49.30913 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| 000c6386-8411-34f5-98e0-8a2ced30d7a3 | -22.37151 | -49.33427 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 366c9d0d-ac35-3687-b49e-fc69ddfbfe04 | -22.37096 | -49.33472 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| f1bcf20e-2d18-3b4a-9ad4-07d545213b47 | -22.37037 | -49.31498 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| 1eff4259-0734-3d6b-b128-56af8dc910e9 | -22.37023 | -49.34033 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 696c3087-0915-3a3b-a229-b170f5ccc25f | -22.36964 | -49.34074 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 34229bc1-b62c-3fec-80fe-8b08b04e0eb3 | -22.36915 | -49.32077 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 847130c0-ad20-348f-b2ed-0bc1d65037ab | -22.36896 | -49.34631 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 1f1fa5ac-da92-31cf-9233-6545e75e9f41 | -22.36833 | -49.34674 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| b4c58eb7-d648-365e-b19b-abaf7d687066 | -22.36793 | -49.3019 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4bb12a7a-30b9-342a-8578-c37e46f1cf2d | -22.36786 | -49.32683 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| cd2e2c48-634a-327d-b25f-0525fc0d3a0a | -22.36667 | -49.30783 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8c75549a-ed80-3d32-8244-57de83255b18 | -22.36658 | -49.33288 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 26d22757-c822-36f6-b068-248d762091cc | -22.36542 | -49.31373 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c8f417c2-e3e0-3736-b382-2817acc551b1 | -22.3653 | -49.3389 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| d8ef5bc9-06e0-334a-816e-ff071494d3f3 | -22.36417 | -49.31964 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 85b7afb5-a6f0-37d7-b99f-df8015d305bb | -22.36401 | -49.34502 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 3a3759c0-af9a-301b-bf76-0cd64450ca03 | -22.36289 | -49.32564 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 1f7e3662-7ec3-3a1e-84dc-c7d62415d0a5 | -22.36174 | -49.3065 | 2024-10-01 03:51:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d06529a2-97a0-3801-86e2-d39f5ad0b691 | -22.36163 | -49.33162 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| d9b83412-6247-334e-bec2-ce078e472e2b | -22.36047 | -49.3125 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f331597c-6b1f-3e31-bbc7-7a0a1993cfa3 | -22.36036 | -49.33759 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 9790e46d-43da-3873-920e-eb1844ce6fdc | -22.35917 | -49.31863 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 3bb39e6d-ce8f-34ad-8e8b-cb93ffb51cb6 | -22.35905 | -49.34375 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 217ef7e7-db7a-3bd3-8a0e-7aab37de5a8b | -22.35788 | -49.32468 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| e861e871-5134-3247-8c1b-7fe256625a5a | -22.35662 | -49.3306 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| b184aff4-dff5-330e-b5fb-f08213242c7a | -22.35536 | -49.33652 | 2024-10-01 03:51:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 9cd1aab8-efc7-3988-b06a-76e89e1f3086 | -22.18521 | -47.52931 | 2024-10-01 03:51:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 91b23706-9051-36de-8812-f4683fc490a4 | -22.18072 | -47.52848 | 2024-10-01 03:51:00 | NPP-375D | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3ac0f273-1f42-3eb5-be9f-d653307b4a49 | -22.94864 | -42.89702 | 2024-10-01 03:51:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| be25209c-ddad-3adc-917d-473d485ce36c | -22.94518 | -42.89633 | 2024-10-01 03:51:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1669043a-4979-3e8a-8ac7-286465bd1ce5 | -22.78412 | -43.75905 | 2024-10-01 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c2471154-48f1-3686-8016-588af416a0e6 | -22.77076 | -43.58407 | 2024-10-01 03:51:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b6450f83-4e3f-3408-b56b-5fdb8bdd758e | -22.7691 | -43.75996 | 2024-10-01 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83969290-4d1d-3b66-836a-c02f283fe2a7 | -22.7655 | -43.75928 | 2024-10-01 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92ad0887-8f28-3c82-a024-6b951e43193b | -22.74449 | -43.77285 | 2024-10-01 03:51:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 42c33398-74f8-3b39-9c10-bdb3343ab54f | -22.73963 | -43.75848 | 2024-10-01 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b7674dce-2e67-32e0-b436-b2ab2c3539bc | -22.7368 | -43.75348 | 2024-10-01 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 08fef1a0-4e8a-3f04-bf95-0cc198abddf5 | -22.73605 | -43.75771 | 2024-10-01 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c03c53dc-cf80-3882-88fa-14860bbe8a0f | -22.67822 | -42.85341 | 2024-10-01 03:51:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 01e55d80-d817-38e5-af84-af7bbc61407c | -22.67751 | -42.85751 | 2024-10-01 03:51:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d9d32e33-bc6d-3e67-95d6-d6a17b329bdf | -22.67405 | -42.8568 | 2024-10-01 03:51:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9885a01-aac4-3cd2-9234-e284f029a932 | -22.61996 | -43.67632 | 2024-10-01 03:51:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b20e5085-24ce-3fec-8247-29226ddf48e1 | -22.61986 | -42.17045 | 2024-10-01 03:51:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a42e704d-7cef-39a1-9938-619236d6056d | -22.61917 | -43.67353 | 2024-10-01 03:51:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eb1ebbe4-28a0-31d4-b62c-0ca458f5de6d | -22.61646 | -42.16979 | 2024-10-01 03:51:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 148976c8-b7d3-3823-8801-3b4086381449 | -22.6156 | -43.67276 | 2024-10-01 03:51:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d41ef9ba-53bb-3961-a914-29ee64fffab9 | -22.59807 | -44.02631 | 2024-10-01 03:51:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 71336dcb-4cb4-36ba-b666-59a9ab64720c | -22.58367 | -43.8757 | 2024-10-01 03:51:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0dd94711-0607-3582-9f36-37332628e9ff | -22.5399 | -44.30508 | 2024-10-01 03:51:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 387b784c-e56a-3991-8689-813d9aed964b | -22.53622 | -44.30429 | 2024-10-01 03:51:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0ab02740-1c0d-34cc-98c3-8ea52bed0bfc | -22.50546 | -43.83171 | 2024-10-01 03:51:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ed1dde41-565d-3ba0-bb5a-542cc57e0918 | -22.50468 | -43.83607 | 2024-10-01 03:51:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 10f331d3-961e-3e0c-8259-52e4790851bf | -22.50388 | -43.84048 | 2024-10-01 03:51:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e1c8e579-71a6-3b04-a117-3981b015d740 | -22.49356 | -43.53993 | 2024-10-01 03:51:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0411d943-4996-395c-a7bb-a3d39aeaa94f | -22.49207 | -43.54832 | 2024-10-01 03:51:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3e242ae2-9f55-3e78-ba67-069763b0e6c4 | -22.45756 | -44.11734 | 2024-10-01 03:51:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7f237056-a3ab-3a77-9f41-c915397f59ba | -22.37663 | -45.79837 | 2024-10-01 03:51:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0c8201fe-6073-3740-b1ba-71fdc2f2cc2c | -22.37587 | -45.80236 | 2024-10-01 03:51:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c068778-688f-34b7-93a1-e847a6ab5ae5 | -22.20237 | -45.04002 | 2024-10-01 03:51:00 | NPP-375D | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2b0bf5ac-950a-3b75-b906-109968f7a19d | -22.19854 | -45.03911 | 2024-10-01 03:51:00 | NPP-375D | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0ea2dc84-d3df-3057-8f80-c33133c51e52 | -22.12344 | -45.91776 | 2024-10-01 03:51:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9510bdbd-9a47-3ee7-bc0c-66458f39c19e | -22.1227 | -45.9216 | 2024-10-01 03:51:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4282a466-652f-3530-806f-4b6d49aade85 | -22.05469 | -45.26719 | 2024-10-01 03:51:00 | NPP-375D | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63e0db8d-a88c-3cf1-b451-1585aa6f8401 | -21.9325 | -41.55287 | 2024-10-01 03:51:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ead717bc-7ca6-3e9d-9bc8-f003e1e3e43a | -21.93187 | -41.55669 | 2024-10-01 03:51:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d3afada5-01a7-3cad-9c17-48096ba0f635 | -21.84781 | -44.49966 | 2024-10-01 03:51:00 | NPP-375D | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5c4b854e-bcd6-39aa-8b96-4861fec14e98 | -20.82438 | -49.63474 | 2024-10-01 03:51:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 670019bc-9460-3669-8959-2bc148105be7 | -20.82365 | -49.63809 | 2024-10-01 03:51:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| dbe07937-982a-3c75-be41-b1a08de26a35 | -20.65353 | -48.76837 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d4f58e8d-395d-3dda-815d-c9fae7c8e87f | -20.65254 | -48.76851 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 065f6f24-ea57-3b33-88d3-67d6ee886a21 | -20.65224 | -48.77462 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a2081d42-8673-3206-ae3e-1a72529d2e39 | -20.6512 | -48.77474 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 51a15f3f-6f8a-3c00-b828-c002eec34a97 | -20.64728 | -48.77345 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 64622f5c-7daf-3048-b5ec-748264cecbc0 | -20.64614 | -48.75375 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7970dd6b-c582-395c-95ac-cd6f1a1786c3 | -20.64239 | -48.74679 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 45034eb9-3e8f-388d-8487-8906e615faa9 | -20.64118 | -48.75262 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| daa54435-d488-31d8-9e7e-bf37456bb765 | -20.63994 | -48.75862 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 95e1ad88-f3b9-33c1-8ebc-003f045df44e | -20.63621 | -48.75154 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c5e85c11-ae68-3f00-b6d2-7108673553f6 | -20.63497 | -48.7575 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 8fe16b58-9c10-31f9-9e29-ec17c656fa97 | -20.62998 | -48.75647 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| b428c236-cc27-3bbd-94b5-6d5c66682e26 | -20.62499 | -48.75546 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| af709e6a-ae0c-32c3-a4e5-3e97811448ec | -20.62001 | -48.75438 | 2024-10-01 03:51:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| d9b8fd9a-a1f9-33d4-8b6e-888bd730d27c | -20.17628 | -50.00808 | 2024-10-01 03:51:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54e9d05c-c8b4-3a0c-8b76-8d497722ee6e | -20.17602 | -50.01051 | 2024-10-01 03:51:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1d15c7f3-ee24-332f-b721-9501af7734d2 | -20.17549 | -50.0118 | 2024-10-01 03:51:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c259219d-b4d5-35b2-a494-b0a58524585b | -20.17091 | -50.00661 | 2024-10-01 03:51:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9bd63afd-521a-3b05-b77c-b5fcd4050d40 | -20.17065 | -50.00904 | 2024-10-01 03:51:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5943fc21-0113-32d3-9d23-4f193dbd04cf | -20.17012 | -50.01033 | 2024-10-01 03:51:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d9638be-52cd-32ec-af27-3fe217fa3402 | -18.04299 | -48.59802 | 2024-10-01 03:51:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| dee0f3ba-8911-3b85-a846-4ed6e12b5b06 | -18.0423 | -48.60139 | 2024-10-01 03:51:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a6b79cb7-c93f-3c3a-8a12-bfa02b39c835 | -18.03717 | -48.60002 | 2024-10-01 03:51:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bf487254-7623-3a44-b099-87b8768cee34 | -20.72405 | -46.89827 | 2024-10-01 03:51:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1ca802e-e65c-3741-99a1-01ca08381945 | -19.53895 | -43.11877 | 2024-10-01 03:51:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 615a9519-2d95-3df2-b0d5-6588ee050311 | -19.51768 | -42.87964 | 2024-10-01 03:51:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a25262a5-04ae-3929-a609-fa466cbb01af | -19.51412 | -42.87883 | 2024-10-01 03:51:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 09e04c33-48a9-3e5f-a262-25a739ff9afe | -19.51336 | -42.88316 | 2024-10-01 03:51:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9f2a78b7-4143-3eb1-ba07-95a41a1d8338 | -19.51056 | -42.87801 | 2024-10-01 03:51:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |


[Clique aqui para ver as próximas entradas](README58.md)
