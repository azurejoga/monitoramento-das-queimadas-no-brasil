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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58e09da7-1a70-3aac-b1f9-cc5829759fec | -13.39968 | -45.33475 | 2026-04-27 04:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb7bd00d-e6d1-3288-aa88-be29c3ccbe3a | -23.32306 | -46.87998 | 2026-04-27 04:57:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2079fc4f-e408-3cf5-b12e-4245697081f5 | -19.49484 | -54.21099 | 2026-04-27 04:57:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 258fcc16-7b82-3689-ba0d-3fead02151d9 | -21.73228 | -54.5195 | 2026-04-27 04:57:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 994327d8-9883-3e56-9737-36466bcaa9fa | -21.34381 | -48.64902 | 2026-04-27 04:57:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 37f3abc1-a58f-3724-bb52-d638baa8e4a8 | -21.49645 | -51.76885 | 2026-04-27 04:57:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 50927346-7bf1-3fa2-8270-f31c92d3b6e9 | -21.50162 | -51.77291 | 2026-04-27 04:57:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8ee52623-4529-36cf-8849-6a870a5ece2e | -21.49805 | -51.77234 | 2026-04-27 04:57:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 389a1ff6-3c71-339b-87e3-f8e993f149f2 | -21.49941 | -51.77375 | 2026-04-27 04:57:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cf88e008-1369-3ce4-a056-f8f0eb1b0d32 | -19.49426 | -54.21465 | 2026-04-27 04:57:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d881c962-1b29-327a-be71-b658b2e9db8e | -20.16913 | -46.87662 | 2026-04-27 04:57:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3d9c65c-b35e-3220-a460-ca04e0a6e5ca | -23.32797 | -46.88027 | 2026-04-27 04:57:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 972bed9e-7a0e-3787-902b-c052536029f5 | -32.30804 | -52.42712 | 2026-04-27 04:59:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 7baa6aa3-4867-3b8d-975c-b06904e9cefe | -31.95948 | -52.131 | 2026-04-27 04:59:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 9d83bc44-ed1a-3f2f-a964-74c53503969e | -31.96147 | -52.13193 | 2026-04-27 04:59:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 3a64b338-44a1-3155-8bac-a291165f0d46 | -31.95751 | -52.13129 | 2026-04-27 04:59:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| bf682727-68f7-32b6-930d-6bcf99015e6e | -13.39383 | -45.33894 | 2026-04-27 05:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10dc050c-098a-34bd-88e6-37a150236586 | -13.39934 | -45.3394 | 2026-04-27 05:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 239f9151-855c-37af-a149-02e5ba799be8 | -11.83947 | -55.02003 | 2026-04-27 05:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a58fdd9-2ccb-3d3c-b184-9d84d79e3bf7 | -13.6003 | -54.8661 | 2026-04-27 05:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f433e6b-8703-39a1-acc7-4fc00815503a | -10.86926 | -51.30155 | 2026-04-27 05:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be5c847f-2117-39a6-8463-5e6320057a8d | -10.87387 | -51.30218 | 2026-04-27 05:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e21ce309-d88d-3dfa-a2e3-91d737b6261b | -11.84246 | -55.01893 | 2026-04-27 05:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73f4c0b6-f750-3441-bb2e-a56674d1e4b4 | -13.40082 | -45.33966 | 2026-04-27 05:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5686feca-98db-3d5b-9d59-1326e6e57716 | -12.20547 | -54.31064 | 2026-04-27 05:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 323b0b8b-8be6-3b7c-9bc0-9c4c29efa76f | -13.40005 | -45.33265 | 2026-04-27 05:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1bc56fb-afec-3631-bb29-8cacec980234 | -13.40157 | -45.33292 | 2026-04-27 05:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a6a7cd90-5331-373b-954a-9de0160a36c7 | -14.20196 | -57.4242 | 2026-04-27 05:16:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4016418-eb06-3df8-804e-692366038fb3 | -14.72276 | -53.95589 | 2026-04-27 05:16:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee0c3740-6020-3388-9807-353977888503 | -19.49344 | -54.2123 | 2026-04-27 05:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40a4390b-987b-334e-badc-844edc93d777 | -14.33961 | -54.92667 | 2026-04-27 05:16:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d453746-bcaa-3cfe-8988-2262332403ff | -14.34056 | -54.92962 | 2026-04-27 05:16:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2368294-d280-3104-83cf-796ed62f5f29 | -18.08438 | -46.85075 | 2026-04-27 05:16:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaef69d7-8374-3663-8038-3c9d72493090 | -19.49633 | -54.21151 | 2026-04-27 05:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8fef7dd-84f9-3aa3-9ec8-c6adfab0d9d6 | -16.59447 | -58.23957 | 2026-04-27 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 762f9a50-e06f-3127-a6ce-74e8e4ea9367 | -21.23117 | -56.92662 | 2026-04-27 05:16:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee1ef508-ecfd-394d-afc5-69afd8fe920f | -18.08489 | -46.84508 | 2026-04-27 05:16:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b63e376e-2758-3589-9ccd-0f21a32a01fe | -14.72225 | -53.95971 | 2026-04-27 05:16:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8ad7026-dd96-3027-b545-bf4507d9af0b | -14.72634 | -53.96021 | 2026-04-27 05:16:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3ab8205-6ed4-3f09-9bde-987324901f6e | 2.73106 | -61.35347 | 2026-04-27 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35b0bac5-e12d-33ff-aed7-93bf285a6f49 | 2.73029 | -61.35357 | 2026-04-27 06:31:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f352b549-bf50-387d-83a4-0750fc50d46a | -13.3955 | -45.321 | 2026-04-27 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 6d6a86a4-70a0-3040-891b-08c77163c9b6 | -13.3955 | -45.321 | 2026-04-27 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 91d6a543-8d12-3e4c-be85-eb9a667ab05e | -13.3955 | -45.321 | 2026-04-27 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| fcdfa2fc-f885-365b-bda7-d69ef8ba488e | -6.84467 | -42.79748 | 2026-04-27 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| bec9ad60-4e5f-3beb-9dbc-62a164443d1d | -3.49782 | -42.50862 | 2026-04-27 12:00:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a1c6eeaf-807c-3408-b656-9ba0a9c52955 | -15.51107 | -43.29386 | 2026-04-27 12:02:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 18.8 |
| a26924d6-bd20-3403-b627-bb09f6d269fe | -13.39258 | -45.33702 | 2026-04-27 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| d47a3c73-9706-37cf-916f-b302a75be6dc | -9.41798 | -50.68021 | 2026-04-27 12:02:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| def8fffb-f6dc-3f97-b2f3-7b24d29af5c5 | -15.51291 | -43.30067 | 2026-04-27 12:02:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 29.8 |
| d3740de8-88f9-38ad-a345-7906d9e6cd1b | -11.72775 | -44.73166 | 2026-04-27 12:02:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 54b02a00-3bca-37c5-ba43-6ae75d93832c | -13.39419 | -45.32453 | 2026-04-27 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 5c785123-2a97-3545-899e-33c3e844d28d | -15.50879 | -43.31299 | 2026-04-27 12:02:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 11.9 |
| cf423b80-b429-320c-909c-7c17942fa598 | -13.4045 | -45.32583 | 2026-04-27 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| ae4de0d1-f0ef-39be-b85d-3442124bd702 | -7.46736 | -48.12873 | 2026-04-27 12:02:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15b02ef4-b176-3583-b92f-f7e9146317fa | -13.40287 | -45.33834 | 2026-04-27 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e619e08d-1148-3d69-9856-4539bd3ee149 | -20.19213 | -50.55363 | 2026-04-27 12:04:00 | TERRA_M-T | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 2ca89f50-5ddd-38c4-9885-9b78f8d992b5 | -20.14863 | -50.65584 | 2026-04-27 12:04:00 | TERRA_M-T | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| f44dc946-059b-3b57-8e01-b1a08b5cfe04 | -19.16968 | -45.46452 | 2026-04-27 12:04:00 | TERRA_M-T | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9c976f9e-2cb4-3b64-a2fa-24aad825a93d | -15.8482 | -46.54222 | 2026-04-27 12:04:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a7075ac1-de59-329d-9cad-53021cc561d1 | -20.19079 | -50.563 | 2026-04-27 12:04:00 | TERRA_M-T | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| df07e7a6-ab98-303b-a593-efea08379f16 | -20.16652 | -46.87194 | 2026-04-27 12:04:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4bbd1ac6-7eda-3b5a-b82c-3449c9d5c4cf | -15.84963 | -46.53086 | 2026-04-27 12:04:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 06a9d947-124f-340e-ba0b-c680a7c3f0ec | -13.3955 | -45.321 | 2026-04-27 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 71f50a37-7a72-324a-a05a-2357970929cc | -13.395 | -45.3443 | 2026-04-27 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| cdea2ef2-eff9-3413-84b9-f1704ed45153 | -13.3955 | -45.321 | 2026-04-27 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 3e60e231-58b0-3999-9759-058f8bde1995 | -13.3955 | -45.321 | 2026-04-27 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 61ad18e4-5a1a-39a7-a801-d9de0acbcfe6 | -13.3955 | -45.321 | 2026-04-27 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 684c2e53-2899-33d7-b6b7-d28ac64f8e08 | -15.0498 | -51.8828 | 2026-04-27 15:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |


