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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 681f31c5-42ed-3594-91df-e78fec7d82b7 | -11.80759 | -44.27965 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8bb06db1-0ab2-36b9-ba2f-b821a7e6a9c7 | -11.15418 | -48.67383 | 2025-05-21 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faf5a6b1-ac8b-3ef0-bebb-445f4eaa9212 | -10.12778 | -48.68792 | 2025-05-21 04:14:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eeee7b5-d5ae-34ff-8d3d-3f7328b8e9e3 | -11.81364 | -44.28421 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c56a3f69-549d-3156-99e6-1201499f8b40 | -11.81144 | -44.27668 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 98984a81-8456-3c58-b684-ed539f2015c1 | -7.20611 | -43.09197 | 2025-05-21 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ef78ba7b-e9c3-3cb8-9a33-c1120feb529e | -9.38484 | -48.40987 | 2025-05-21 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ab6f6c-1d1c-39bd-99c6-4f01b785965e | -10.79379 | -49.58723 | 2025-05-21 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b67603eb-0487-3b64-9512-f54e38576873 | -9.25343 | -44.48643 | 2025-05-21 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85437337-1556-3c6e-a02f-1836aeef27b2 | -10.55015 | -42.43248 | 2025-05-21 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5b5968c8-4e07-3093-85d7-ef226d3f82e9 | -10.36209 | -47.97311 | 2025-05-21 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b74559ae-de68-3dc6-b258-7b6289bff17a | -11.20675 | -49.16513 | 2025-05-21 04:14:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7319a4c7-c930-3ec7-9a1a-ab4d9800ee8b | -10.6607 | -44.49863 | 2025-05-21 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 315dadcb-aa62-351d-aeac-1beca65034fb | -11.80814 | -44.27615 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f0e7e90f-4c8e-38eb-9b23-fb9ffb9dd1b4 | -10.36907 | -47.01755 | 2025-05-21 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3a69fd1-1057-3045-ac4b-71b17d2be21f | -11.29214 | -53.97933 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fef6286a-6218-3827-8894-0bf03279daa6 | -14.0255 | -55.14209 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60affa4a-c0f8-387e-a162-3cfe396f1843 | -17.61662 | -44.63784 | 2025-05-21 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fb11d21-479c-35c1-805f-dbfe430c6052 | -12.35928 | -49.97521 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3aed53d5-a9f5-3637-aebe-aeab317df683 | -19.15934 | -47.82188 | 2025-05-21 04:17:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90bb901f-36e0-3612-ac39-42724f196450 | -12.49376 | -57.19275 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b9f62b9-7335-3452-8821-df246a320854 | -14.02221 | -55.12963 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8e18565-4110-335e-b17f-8794cd9c90bd | -19.4552 | -45.30797 | 2025-05-21 04:17:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58e55dfe-4ff7-360b-875f-cc1b10f11dbd | -20.95139 | -56.60295 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e1380bb2-8d92-3696-a285-067209d3fcf3 | -17.62076 | -50.91452 | 2025-05-21 04:17:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f8ef2b7-0573-3097-a20d-3215d1ccc76d | -23.60617 | -48.29368 | 2025-05-21 04:17:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3829b973-0eb5-3ac5-8c4c-207d91cd8cc0 | -12.03592 | -54.96971 | 2025-05-21 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad5358ad-9f0d-3fea-8b3f-4adc7079b640 | -11.92219 | -54.41166 | 2025-05-21 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 234f6ef0-83a2-39b5-9fd5-0b949b66342f | -15.51782 | -53.51027 | 2025-05-21 04:17:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 497bf783-7308-32eb-a86b-14ff86025833 | -10.68593 | -57.59114 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 076affb7-5b80-3241-9cf4-ccf56ae64089 | -12.43429 | -43.72404 | 2025-05-21 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 14753616-321b-3454-8bda-456159516c35 | -12.0351 | -54.97393 | 2025-05-21 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94cea983-0cf0-31af-85f3-8a4d6bac9ae3 | -22.31602 | -53.63111 | 2025-05-21 04:17:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aa67f752-4cbf-3e4f-913a-36277ee741fa | -17.70845 | -47.49702 | 2025-05-21 04:17:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2633b742-8436-34b1-a849-baad8444f2dc | -23.70959 | -46.89415 | 2025-05-21 04:17:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6860d14-2d99-3b24-8dd9-797e0de66932 | -11.29144 | -53.98302 | 2025-05-21 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 865847e5-ff07-35f2-9e15-fbf0dcf17251 | -12.48081 | -57.18994 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48486c58-6ffe-3521-a255-2f22092b07c9 | -14.69398 | -45.11663 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9c4b341-f95d-3e7c-b570-9e7e84b270d2 | -14.01991 | -55.14099 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b03ab68a-03c2-3e70-9632-9d0b9d4ca182 | -12.36605 | -49.97717 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ceb03bb-d0c1-39a1-bda7-f9e308b6194f | -12.29018 | -52.47491 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f4d1170-e216-33bb-a0fd-ba2cc39e4579 | -14.15565 | -45.46746 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84f7c28b-8c8a-3b92-a3a9-cec6542d3a0d | -13.66771 | -53.94094 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3e402bd-3a91-38df-8730-2aa1a27be17a | -18.75181 | -47.47898 | 2025-05-21 04:17:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7275f67-b474-33de-8336-455ad87c9244 | -12.84196 | -47.3979 | 2025-05-21 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e402a6b-cfe3-3cca-a117-75333c052040 | -12.03427 | -54.97816 | 2025-05-21 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 550feabc-ef2d-3e8f-ba13-2918848f8c94 | -11.40974 | -56.72941 | 2025-05-21 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0857f535-8c21-39a9-af1f-217435e0b834 | -12.50863 | -57.21953 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9bd6e6c-5cb4-3b38-bc27-d2db0082c1e2 | -12.29293 | -43.53754 | 2025-05-21 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 161c4ccf-74e7-3044-961a-5eb82b25e6c7 | -12.83776 | -47.40133 | 2025-05-21 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 933ddb6e-27ab-3c7f-a7b6-ffbcc041dd56 | -15.89703 | -46.0101 | 2025-05-21 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7672c23b-ddd4-3893-a329-781d6407a590 | -14.69453 | -45.11309 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04ffa56d-baf6-34c6-a379-6b87669a2c72 | -13.7162 | -57.47271 | 2025-05-21 04:17:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85041ba6-4187-3d1d-bbe3-52d88c8c73ec | -13.61073 | -55.45972 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dfdb788a-b4d7-3c38-b6e3-ac541f141dea | -15.05065 | -45.66145 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a72c63b-33db-3dbb-836e-81569fe525c5 | -14.04986 | -45.51161 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61e8092b-b842-3055-b3b5-3002062520d5 | -12.12831 | -54.6632 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbdc1c02-990a-3bc4-a92e-eb229d2ec288 | -14.68464 | -45.11146 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d378b5dd-1183-3b2c-8c4d-f38c698479b7 | -14.58117 | -48.3595 | 2025-05-21 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c750666-ffc5-3b70-97df-3eeeb361e581 | -20.96134 | -56.60895 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da0d0bce-b83d-36c3-8669-d6c2188ec713 | -10.67655 | -57.60233 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 580345fa-d407-3c57-bf89-34577c99ba99 | -14.01509 | -55.13608 | 2025-05-21 04:17:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 019a1fd1-ee45-37b5-a99b-abccf8f4d92b | -14.15509 | -45.47102 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e9dd535-977b-3ad2-8e3e-48f1cdf9dfa4 | -17.91904 | -45.52984 | 2025-05-21 04:17:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19efd52e-74c8-3f0c-88bb-aec61013f80c | -12.28916 | -52.48036 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cdbab0bd-c38e-33ea-81ee-a756c789ef58 | -12.68874 | -58.12667 | 2025-05-21 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 228a79e7-aecc-3015-a7e2-127ec0144172 | -12.34004 | -49.96405 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e74644a-1ab9-3854-b31f-a73185cb48bd | -12.35993 | -49.97142 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff9f2601-6a6a-3719-ac4f-117ccda90185 | -15.90034 | -46.01067 | 2025-05-21 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b445484a-5333-386c-8b4c-b1daecc49d41 | -17.50562 | -46.7411 | 2025-05-21 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f5a3022-73b0-3e72-808a-9946e427474d | -17.87067 | -43.74562 | 2025-05-21 04:17:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c8a54ac-65b3-3196-9487-f41185880b91 | -23.7187 | -47.38118 | 2025-05-21 04:17:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4accce9f-594e-3503-bdc8-79a73118267e | -14.68408 | -45.115 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b003c7a6-28aa-39be-9a0c-4398e2b05fb4 | -14.68793 | -45.112 | 2025-05-21 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54916c4f-2d92-32ca-b81b-867f078e1ff2 | -10.67661 | -57.60343 | 2025-05-21 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2dae197-35ac-3aab-b870-ef47598ef544 | -23.6095 | -48.29432 | 2025-05-21 04:17:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2dbac40-df3c-3860-9429-94cabb9fde51 | -14.163 | -50.50198 | 2025-05-21 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2451e20-9a95-35f5-b108-a568d41f8c13 | -14.15783 | -45.47512 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a39d6398-706c-3ed3-9413-373d9e3dd655 | -12.1238 | -54.6688 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05bcb971-e870-30da-8fe0-0a1a16fb546a | -11.08291 | -54.77151 | 2025-05-21 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 03e0dc8d-d245-3254-92ab-e9946dfb98a0 | -13.6741 | -53.93581 | 2025-05-21 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f05b4a77-d201-3989-8e9c-bef85cf98372 | -12.29887 | -52.48218 | 2025-05-21 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 104db0bc-1f21-329a-ad5d-1e034bca3916 | -17.48079 | -45.01976 | 2025-05-21 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abc9ed88-029f-393a-a28a-f9db2f5a4008 | -14.16557 | -45.46911 | 2025-05-21 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 384678a8-19c4-364d-af9c-c3efbc2f6ed6 | -12.50109 | -57.21941 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00d5a27b-b052-315f-a89d-e99c22444a72 | -11.92146 | -54.41539 | 2025-05-21 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca77810d-b9d1-35b3-a333-dd431432a5a2 | -25.19376 | -49.3285 | 2025-05-21 04:17:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dade2dc0-23bb-3d1d-a4eb-1cdf4a039ac9 | -19.84041 | -40.08222 | 2025-05-21 04:17:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c18279be-65c2-3ec9-b05f-9b1e4efbcc56 | -22.61276 | -49.75653 | 2025-05-21 04:17:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 520122de-24a3-3fd2-a96a-b76010db3404 | -12.50761 | -57.22065 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fc247a5-ab1a-3b49-a0e8-95f24ca509fa | -12.4734 | -57.19004 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f73fbb6-1ceb-3988-b897-6f600c0b1827 | -20.96058 | -56.61246 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 151bf62e-9f76-33c1-9ad0-4b3e367cdb2d | -12.72249 | -54.97382 | 2025-05-21 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ef277c7-986a-32b0-87af-ea2b86287dce | -22.74582 | -47.14075 | 2025-05-21 04:17:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77125922-6f84-35e1-939f-0f509ac6d4f0 | -12.36536 | -49.98096 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c4a1f2f-bcba-3615-b435-24c6ee508439 | -20.95675 | -56.60418 | 2025-05-21 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1ffb6945-bae6-3641-bd25-f438b5fb19b2 | -12.36195 | -49.97639 | 2025-05-21 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83196f5f-495b-39e1-ada4-d283d9b986e7 | -17.9196 | -45.52624 | 2025-05-21 04:17:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0eeff0fb-0aed-3a40-8356-a0de705fd077 | -12.47429 | -57.18873 | 2025-05-21 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40e98b66-7320-3ea2-bd2e-5cea24e1c699 | -13.51941 | -46.81538 | 2025-05-21 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
