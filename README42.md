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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dec31fcf-927d-38ec-a0cf-bc20cb016e98 | -15.63271 | -44.37778 | 2025-09-14 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36efed1e-1d21-3a21-8392-7519d8f428bf | -17.30392 | -46.11036 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 408124c4-ff83-3fc4-89a1-3a4a531730c5 | -14.47832 | -47.34032 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc810fc1-12c9-3a5a-9f8d-d05a7c193d20 | -14.42738 | -47.34443 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1067cfda-a601-38c4-9c6f-02fca4213bf6 | -16.54304 | -49.22029 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d165aaee-1f7a-31c2-ac02-fffc0d54b24d | -19.43165 | -47.41137 | 2025-09-14 04:42:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36ec41a2-50ee-3d1a-ac00-0e65805ddd5f | -18.58806 | -47.20079 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7bdefa0-a3eb-3bec-b209-f10308ac236b | -12.6935 | -54.70872 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6e0d1878-6597-3baf-9865-7f9c6f4b8061 | -17.40711 | -49.26509 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 467aad06-404b-3ad1-bf6c-6c122dca4906 | -16.32783 | -51.53013 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ad744fd-f42e-3c4c-9e2e-3bf8f2e1e410 | -12.67669 | -54.67382 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6cbde2f-fd2e-3da9-a732-95b17922292f | -18.08686 | -42.9379 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| d216b6fb-155c-393e-b4cc-a7ead37bddad | -15.64777 | -47.04171 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 662ac7da-4175-3625-a054-b107e2abaecc | -14.78261 | -44.90808 | 2025-09-14 04:42:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 024a4f7c-b9c5-337b-967d-addfb915dcda | -16.58434 | -55.17247 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7e90d692-88f9-39ea-a486-3359e45ddf7b | -15.86324 | -51.84828 | 2025-09-14 04:42:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6280c86-ca76-3cc9-97bd-e2fc9cfd26b7 | -18.38107 | -48.34108 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 587b4e16-1cc3-3c54-b0e0-9555469879ca | -16.65124 | -49.76666 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f51a739-4034-3c90-a38d-1a1520afc9ad | -17.41837 | -49.23528 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 237c8606-dff5-3330-bc09-2bd907ae7e6d | -17.30013 | -46.10623 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 620b52ca-d912-34b0-8cd3-b1f96edade3b | -15.34617 | -59.18823 | 2025-09-14 04:42:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddd99692-aabb-358e-b8cd-4856aab06959 | -15.11354 | -52.49709 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff897288-bfa3-3927-86da-d1b8c40c33d2 | -14.19195 | -44.79787 | 2025-09-14 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 054ca730-edde-3128-8aa1-b21df5e39c46 | -15.46565 | -55.97598 | 2025-09-14 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79587fd3-811b-360a-af2e-3767fbc21b5a | -12.6949 | -54.72279 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2bf6bcb1-9029-343f-bd34-3e632d561547 | -15.17306 | -52.46652 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cef4a14-3662-360c-88a9-6623e4e9e474 | -12.9395 | -54.74448 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7984e09e-6476-365f-9129-78bd4316f9b9 | -12.91223 | -54.74878 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9de4c48-68b6-34cc-bd49-f1b1440a665d | -18.08777 | -42.93413 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 35c7a622-1197-3fdb-8be5-96b8531ef677 | -15.80091 | -52.20041 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 855d2578-9e04-307a-90e6-d8f618e269e9 | -18.465 | -49.57458 | 2025-09-14 04:42:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e9943a0a-1829-3386-8e58-e843d2e90346 | -14.48424 | -53.93518 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 970b4117-5141-38e4-803f-2bff00bbb196 | -18.1637 | -49.20354 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fcd0ccdd-0273-3555-b213-f8e2272da27b | -15.19402 | -48.72028 | 2025-09-14 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b0b764e-1c97-38b2-9358-ed44a015a87c | -15.67841 | -52.24263 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e445be1f-b50e-3074-b819-e2084ae51a7c | -13.89508 | -48.30115 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3373bf23-0dc4-3548-b569-4e383a8d0a58 | -13.90163 | -48.30627 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0509cb0-0918-34b5-a74b-49db9e0fbaf4 | -15.1811 | -50.11205 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b95b1da6-b115-320a-8821-2c1b0782a9ef | -14.43917 | -43.19532 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5920be59-168b-399e-890b-a71f7b078a77 | -12.67885 | -54.68333 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8dfa09ac-0f1e-3a44-9c4b-c4ecc2e272b8 | -15.76372 | -52.242 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66e1613e-3810-367b-b16b-acd0a03bdbbb | -14.57451 | -51.40845 | 2025-09-14 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d271fd9f-7502-32d9-a184-f019140e1efe | -12.69802 | -54.68215 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e69ada2d-366f-3e07-96ac-cf7b443721a0 | -17.14652 | -53.8927 | 2025-09-14 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06ca3dda-81a5-360c-b6e0-0107b209a1d0 | -17.43431 | -49.2248 | 2025-09-14 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42978205-dab6-3d4d-bb41-d720514b4da0 | -15.29734 | -53.77915 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9132b7c-2453-33d0-9267-120a660de41d | -12.67453 | -54.66431 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 08893100-0212-31a0-8a70-40088cf38a53 | -18.06767 | -50.73617 | 2025-09-14 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2583e49-079f-39a1-88f8-d3574b18e218 | -15.19175 | -50.11005 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a751d935-2a97-3138-81c7-bd41c9c870af | -12.66414 | -54.68066 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b8db4dca-f7dd-3211-a58d-e227c6c88b49 | -18.26057 | -49.46129 | 2025-09-14 04:42:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f69e388-dde2-38e1-938b-76a2b85abe67 | -17.36775 | -52.89693 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 217f6882-3c05-365a-a7b4-0b333525e7ed | -15.17581 | -52.47062 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67ce7b46-782a-31a3-a251-6749af33088a | -15.10632 | -52.49953 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f54e40b8-2aac-3016-af0d-a8de8a4b4ba6 | -15.67711 | -49.91022 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7d08ba8-2d57-3793-96cc-509b99410aa7 | -12.92922 | -54.73803 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2ad520f5-8834-36ee-936b-ded98cc8a92c | -19.43211 | -47.4077 | 2025-09-14 04:42:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98c2dfc4-eded-3965-ae4f-0910598a99d7 | -17.29121 | -46.10867 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae27ea9e-f659-3a31-8300-b3fa8a58335f | -16.55475 | -49.21361 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f090cfe1-32f8-3034-9dbc-74ecd3463dd4 | -16.49342 | -55.12003 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 76cd8d8a-2798-367a-bdf9-1ba22eeaf2d1 | -17.31816 | -46.09975 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 635bd8c5-3b03-3f3e-9e35-5f16eb1455f3 | -12.94467 | -54.73625 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 77e477bb-d523-326a-bfbb-2a76a9443439 | -12.65906 | -54.66614 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45c8b4cc-d3bf-3481-86f7-07713490187e | -18.91454 | -48.01525 | 2025-09-14 04:42:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 96dd9f76-a1a9-3162-97fd-f43fb725716a | -18.2962 | -45.10732 | 2025-09-14 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f62c092-3282-326e-9d2e-7a18afb58185 | -14.37886 | -52.93201 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2123348d-4f2c-3b59-a6ec-34a3cbf992d9 | -15.40471 | -52.97325 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64642ff2-f505-3b69-afc5-7fa957f625d6 | -14.40092 | -47.34096 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4133c6d-5749-387e-96e3-681bd1cff010 | -15.12983 | -52.45939 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18e2a4cc-41dd-3cf5-8d1a-f79853e60824 | -17.44967 | -49.2444 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bbd11bc-ef18-3787-a9b0-20f1fd8fc36d | -15.20142 | -52.47916 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d211e8e8-5419-3cae-bcf7-4378bf9b26fb | -15.75952 | -49.78192 | 2025-09-14 04:42:00 | NOAA-21 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1701e11-184c-3009-ba8f-08c20e412d44 | -12.6715 | -54.682 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cade47d5-bdcb-3b57-b09b-6eb266e40b74 | -15.77318 | -52.22521 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08946f77-c63c-327c-bbf2-dfc262b95d4c | -13.71682 | -47.92671 | 2025-09-14 04:42:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb193b4b-b47d-3a0d-979b-c5ec84b252a7 | -14.48356 | -47.33026 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0898bd4-e187-3a9e-b4b5-3b63a1d94f5c | -15.10689 | -52.49594 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fb05e7d-11d7-314e-b08b-498fefe4984e | -15.85663 | -51.84718 | 2025-09-14 04:42:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 524d7aa8-b96e-378a-abc4-b1ef05e7f178 | -17.97333 | -45.27396 | 2025-09-14 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 175622bf-f69d-33cb-9f17-c778f638ce18 | -17.39079 | -52.92344 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0929173b-fda9-32c4-8fe8-9319663092e7 | -15.75611 | -49.78135 | 2025-09-14 04:42:00 | NOAA-21 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9573e461-a21a-33c4-ab8e-30f877d3241d | -15.67428 | -49.90588 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 164a1cfc-1929-32d9-9d6a-e8b651ffa5d5 | -14.16192 | -46.24909 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc449bde-3e33-395e-a352-6b7d5ca00fde | -15.28503 | -56.02468 | 2025-09-14 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df8b68eb-53c3-32c3-a800-39f478a2723f | -16.09006 | -49.98479 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1e250af-0cb3-3700-8925-ed4187d32cf0 | -19.72083 | -45.44021 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38d67006-2d21-32ea-903b-99fb7da297c7 | -15.93412 | -49.97613 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 16c825e4-416b-393d-abef-26a968d90420 | -11.77064 | -64.94337 | 2025-09-14 04:42:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6902f0f7-d6c5-3599-95e7-ee331abd96bd | -12.92997 | -54.7336 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fef8d736-f97d-3163-9eea-ff58e3efddda | -14.64 | -52.11587 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cbd3e95-118f-37f9-9265-05b52fcf7d76 | -17.36599 | -52.90791 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a8804f0-a17d-3740-ab22-0cab45f6d93f | -15.93071 | -49.97563 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b41f6a-99bf-34fc-a30d-720fbb1d0fb5 | -16.33224 | -51.52354 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78b48429-af81-39b2-baeb-c4c88312c753 | -12.69358 | -54.6859 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| e6ab860c-228b-3988-91fe-400d0fcbfc6b | -14.47423 | -47.31396 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95c00342-1948-36df-a72e-31b834bd8961 | -15.67655 | -49.91398 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fb2416f-6235-3efe-a3c0-6a8f9536e3f4 | -17.32337 | -46.09258 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dcbab164-8d78-33b6-84d4-da8126afc576 | -13.26318 | -51.67844 | 2025-09-14 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a62dcb82-5b9e-3d2c-b952-56522da7ffb3 | -15.63797 | -44.37344 | 2025-09-14 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2301a386-395d-33d2-a300-f7c926342ea7 | -14.47733 | -47.31946 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README43.md)
