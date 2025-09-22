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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6d2591e-0c96-368f-9b95-3334b9db763a | -15.76008 | -59.42241 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abd072db-c2ed-33ed-a647-6851823d6d37 | -11.55543 | -48.59247 | 2025-09-22 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b1bcdf6-2e0e-3ea1-96b4-073c07a8e3cd | -18.39674 | -42.85314 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa34ec66-9b73-36bd-a146-09199e1aa98c | -11.02587 | -45.90235 | 2025-09-22 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4426334f-2124-3c53-b741-fb3db925f5aa | -17.3558 | -46.81365 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a438db70-4c7f-317d-b160-c782e00e5b15 | -11.46465 | -51.48605 | 2025-09-22 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e9b90b1-3656-34cd-aaa6-2bb87f77490a | -11.32774 | -54.34654 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fb123bd-fcb4-39f2-9d62-a7f020a7cd53 | -16.00636 | -59.45226 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0cd4b8b7-4a3d-3998-a02a-4ec7cf40cfdd | -15.99254 | -59.47226 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 885c320a-be21-3cb8-a4e5-dc5aaa43f304 | -12.96705 | -47.19098 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26409ed8-95aa-3e7f-9768-29c8e011b05f | -12.74806 | -47.75434 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e3376f1-e37d-3336-8807-8009a4d7ee55 | -11.62958 | -52.86382 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1605dd0c-3a6b-3f0b-be93-51efee42523b | -15.92593 | -48.35184 | 2025-09-22 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d836e57e-a879-340a-888a-91be4097d530 | -15.97303 | -59.396 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c08ff901-f179-3177-8c23-eae56597c5e4 | -11.31658 | -54.34449 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d4ed3fa-822c-38ca-b531-97b80058d9e9 | -12.85029 | -47.06603 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b5a373a-cbfc-3313-ade2-55dbadc8c48d | -15.25106 | -43.0902 | 2025-09-22 04:40:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f6109d84-ee34-33f7-a2a2-fca80d9b7076 | -15.83787 | -59.50251 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 018916fd-2162-37a9-8b00-8de21318dbf5 | -14.43617 | -46.52853 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a4d0be7-d898-3a24-84f9-adc8584e7a2c | -11.47062 | -46.93765 | 2025-09-22 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0ec1118-7b34-3443-beb1-81f7a0e98284 | -17.34583 | -46.82716 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc2386e3-275a-3644-8af2-2f3cb79b293d | -9.0992 | -64.00745 | 2025-09-22 04:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05a42998-979c-35d7-aa98-5a1b9c100eea | -16.12476 | -45.6761 | 2025-09-22 04:40:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7be040ec-d16c-37ed-b666-bee959bc363d | -13.08048 | -47.0206 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 984094f6-b6d2-3f20-8d5b-5ae45eb7e27b | -12.97856 | -46.3773 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc741b29-112c-3c02-b6bb-c3b05d6abaaa | -11.63561 | -52.84898 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9cfefb17-f254-3de8-a652-791d53645355 | -17.43228 | -44.79991 | 2025-09-22 04:40:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f6b37e3-f609-3127-9efe-2d499ccbaec8 | -14.44082 | -46.52378 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f56bc54-2d79-3447-b3bc-158f7f25a612 | -12.79389 | -60.18973 | 2025-09-22 04:40:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 600ff154-4adc-388c-8f28-4484d448557e | -11.8552 | -64.94733 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffe31e2d-0a89-3208-a080-e6589465fa9d | -17.27197 | -43.45186 | 2025-09-22 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2bcae922-0082-39d1-87bf-0964c54f9a7e | -12.34871 | -44.09905 | 2025-09-22 04:40:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 843f5e65-3acc-3744-999a-be4fb094b647 | -11.63843 | -52.85343 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e6575fd-a66f-370a-bb95-afef4c90fedd | -11.74529 | -54.72248 | 2025-09-22 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 12f63a69-8f89-3cf2-8924-dd005ff8ad05 | -11.63087 | -52.8561 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8749b8d-3c4c-371e-b6a9-995d89318110 | -11.87959 | -64.93777 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b4a790c-524b-3a4d-822c-913a7ebcafc4 | -11.63433 | -52.85669 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3acc7c7a-d94a-34f0-a5e7-18b419c93a48 | -15.04848 | -55.28582 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5abd0b7a-c3af-3634-98c9-3b306c6c45e5 | -15.26673 | -56.85424 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52b343d1-774d-3eca-8657-f1ff7fb75382 | -15.27298 | -56.82041 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdafd604-ba99-301a-b261-f823ed25bbc1 | -11.22345 | -46.16552 | 2025-09-22 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 058825f8-d56d-3d39-a9e9-1a9e0722a114 | -15.04314 | -55.29436 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12cf94c9-c1d8-3f7a-bee5-c9d2b8219bc0 | -17.26813 | -43.43949 | 2025-09-22 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c725dfa-2f32-3d4c-a992-72fc2c0de97f | -17.06129 | -44.89903 | 2025-09-22 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79a2b8e3-ddc9-38b8-9026-e57a15b52c91 | -15.83252 | -59.58673 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92e352e1-4a9b-32ce-a150-c8a25aa3eb71 | -17.35937 | -46.81762 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a393da6d-4a31-3ead-a795-93450cf4ded6 | -12.06466 | -44.81822 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1b9f28f-583b-35be-a40d-e9bd46d3e3bc | -17.34228 | -46.82309 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 309a1f50-8c32-3c16-bdb1-c4f2210aa6d6 | -12.98634 | -46.37837 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52522100-516e-31bf-bcbd-e62fe315d9d5 | -16.07104 | -43.47458 | 2025-09-22 04:40:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b89c65e-f138-393e-8329-7d1bbab45c82 | -11.61238 | -54.66082 | 2025-09-22 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40c68565-f775-328b-a386-e8b3ac56558a | -12.98102 | -46.38795 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c411080e-c751-3258-8d0a-e24181c417a4 | -14.68744 | -48.78397 | 2025-09-22 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c71bd613-5710-37b1-96b1-13b83ae1e823 | -15.83557 | -59.51872 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5c65eff3-956b-311c-8ef1-1ca82d5dccf0 | -13.30292 | -47.29615 | 2025-09-22 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a93fe846-4e7a-33a4-8aae-48e69b48f574 | -12.08049 | -44.797 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dcb9e566-86e9-3336-b827-ccb01490c820 | -11.52273 | -54.68361 | 2025-09-22 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 971b40ce-c8a7-33b1-abca-b193c35d58a6 | -12.27351 | -47.84038 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdf79c56-c4d9-347e-bbc6-d30ff65442b9 | -12.74029 | -46.889 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7505ba6e-90ad-3386-b0d8-cf32e7959f18 | -11.08323 | -50.74615 | 2025-09-22 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2523ed71-f6da-3d7e-9cad-fe3e80e8205d | -12.74019 | -46.88662 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d82d6437-cdd7-3e25-ad09-fbf17b950f4d | -11.46132 | -51.4855 | 2025-09-22 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eefcabc2-a451-37a5-b02e-4caeb8447cc1 | -12.74446 | -47.75382 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 937511df-fd72-3a53-9e5b-64ec6a9c8f09 | -15.94728 | -59.39931 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cb3083ae-01f4-3543-b40b-075178491f98 | -11.45873 | -43.53246 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 687c29c8-8128-307d-9343-d7f7bc483ba8 | -17.34182 | -46.82661 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ca81f60-1c58-3770-99b0-231ec7c30608 | -13.67937 | -47.70943 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dd388e3-82be-3f85-a5f0-eac567780dbf | -14.35459 | -47.78593 | 2025-09-22 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7dcd2e2-27fc-3ec6-a3ae-00a480906a41 | -14.3589 | -47.78184 | 2025-09-22 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2dfb3d0-8a39-3810-ab57-e202aa4220f8 | -12.0752 | -44.80411 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0cf7be1-d406-3be0-8f56-581a06e9ed4a | -15.00471 | -55.31562 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4afd1ca3-2ccf-35d3-a96a-942dd5351a29 | -12.71825 | -47.6952 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01fa70d4-83b1-3974-a0ac-d4bd16b69d1d | -12.96381 | -46.9451 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70219b4c-3106-3244-8c8a-caf6abc74d17 | -18.09685 | -44.26389 | 2025-09-22 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b663f6b1-6209-3e87-9dfd-5a4589883947 | -11.63559 | -44.33422 | 2025-09-22 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22a7392a-3c6b-321d-98e7-f057357e8a14 | -12.08102 | -44.79304 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c6eb544-72c5-340b-9f31-3cb352c33c16 | -15.82184 | -59.59025 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 898cfdfd-6d23-32e9-ab91-634e3bd1a1bf | -14.97097 | -44.43343 | 2025-09-22 04:40:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 012b72a7-09dc-3b86-8727-68de2563ab61 | -12.97715 | -46.38733 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e20b447d-f3e0-3e44-bcbc-68fd30172d73 | -15.76577 | -59.41856 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4932785f-7ebf-34ee-b4e5-ef81a1f4fd13 | -17.27272 | -43.44556 | 2025-09-22 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2fec3ff0-3dc6-314b-ad32-df86e6d47a21 | -13.71307 | -47.58078 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3946a2a9-8b72-30b3-847a-5e9f699907e0 | -15.99843 | -59.46745 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe1730f3-a1d0-3d79-916d-ba669d46f67a | -11.62612 | -52.86324 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d88f5c3-e6e4-36c8-b9c3-1b90b8695d82 | -15.02864 | -55.26734 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f8f8a0-be68-3f47-afef-0d8e87a828a4 | -11.32106 | -54.34063 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e775f598-0be7-326d-87be-c5ff11545232 | -17.05167 | -44.90234 | 2025-09-22 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fef58a4e-963e-305d-8e02-364cc8a3ab70 | -18.40535 | -42.86399 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 05b93d79-7b38-3d32-94a0-48e0c71b41ea | -15.95407 | -59.38963 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69f00c58-ffd5-396c-b8f1-d55352a6fff0 | -13.70938 | -47.58039 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56470bd3-ea26-3889-bb99-2acc94370e61 | -16.73776 | -43.02199 | 2025-09-22 04:40:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c8c35716-75c6-3040-a1bb-6a61482d4127 | -11.2698 | -47.47437 | 2025-09-22 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4db16108-3a17-3896-92f8-d686a84e7306 | -15.3062 | -56.79977 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc09eff2-9378-3361-9ddb-412266b3818b | -15.97774 | -59.39709 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d84c8bb9-d149-3409-8ccd-34c3bb841b7c | -15.76322 | -59.43077 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1f55a0c-5dad-30e4-a0ac-098ccc508aa3 | -15.957 | -59.37441 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 674ddd92-ff6c-373c-a0f7-2657d68eff8c | -15.44451 | -55.99106 | 2025-09-22 04:40:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4418a62-2d1c-3bb6-9353-614556e1b2e7 | -13.85894 | -44.19927 | 2025-09-22 04:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdf254b8-5d6f-366e-a43a-a6fea7ad3333 | -15.95608 | -59.37919 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8dc38697-4795-3aea-95d4-d905cf2384fc | -11.26934 | -49.22912 | 2025-09-22 04:40:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
