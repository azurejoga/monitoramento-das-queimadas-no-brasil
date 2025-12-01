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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35fd68ed-61af-3863-859b-c2385753518a | -17.75354 | -47.29526 | 2025-12-01 04:29:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 939e839c-e1ba-35a7-987c-cb00dff005d9 | -17.75335 | -47.29269 | 2025-12-01 04:29:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1194fbc-b489-31ea-8ac9-d58ea51a1907 | -20.21796 | -50.7978 | 2025-12-01 04:29:00 | NOAA-20 | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0cf1122c-5a46-3902-9b42-f7f4bcd9c1ef | -21.53547 | -49.5295 | 2025-12-01 04:29:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e504122-b9a2-33a8-aa2f-90ab40755086 | -18.11267 | -47.15918 | 2025-12-01 04:29:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95c64676-ce85-3e5c-8fc4-53e926403aa9 | -20.01823 | -57.43591 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8357dca1-7e11-38e0-8a4a-ca0be00f6d97 | -20.45678 | -50.83673 | 2025-12-01 04:29:00 | NOAA-20 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 63aab496-37ed-3f3e-b1e3-54fc30e40819 | -19.21772 | -45.80495 | 2025-12-01 04:29:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c37d8f4e-cf61-37f4-867d-823a484a8b8c | -20.02351 | -57.43943 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| cb43a309-8907-307c-9517-3e21a9b66181 | -20.92034 | -46.79583 | 2025-12-01 04:29:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a329a58e-6da1-35f8-9407-a52494ebffca | -15.42786 | -52.19389 | 2025-12-01 04:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71de829b-678f-3d7e-9f46-b82113fabdcf | -19.31997 | -45.81892 | 2025-12-01 04:29:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3ce72ac-908a-3ec7-8177-fef5216fba20 | -16.46609 | -46.42855 | 2025-12-01 04:29:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8113d228-a2ab-3321-ab64-bf844d8bf132 | -20.02101 | -57.42773 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 80117a16-af1e-3c51-acab-50a66ecddc82 | -17.21325 | -47.28487 | 2025-12-01 04:29:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dc773e5-b224-3495-9679-bb3d7962b999 | -20.02242 | -57.44474 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4685ed5a-a0a7-3d1a-a362-c403c817bd9e | -20.21734 | -50.80158 | 2025-12-01 04:29:00 | NOAA-20 | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f90f0140-e719-3395-a6c2-b08f9e6af53c | -19.79678 | -47.80404 | 2025-12-01 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f6a9d0f0-fef9-3385-8ea2-7c42b79fb80a | -17.00134 | -39.77585 | 2025-12-01 04:29:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2e9e263c-80eb-3686-bb0e-abb2241c948d | -20.02461 | -57.43412 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 277e57ea-611d-3ce0-aa40-3fb77196d176 | -20.0146 | -57.42949 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5e800418-e3af-3b6a-8762-0796c1b1ede1 | -16.24714 | -48.04461 | 2025-12-01 04:29:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a55ba56-e418-3606-9328-925720a5badb | -20.01632 | -57.42663 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fee42269-7105-37a5-8211-74b4354954f7 | -21.5475 | -48.89491 | 2025-12-01 04:29:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73369125-e721-3fd5-9840-d1e4e7192ab2 | -21.76386 | -44.30114 | 2025-12-01 04:29:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b003a80e-5d26-335d-a9f2-357311d483f4 | -19.80017 | -47.80458 | 2025-12-01 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c54f858f-6ab3-3f6f-bcf8-933aaa05b7de | -20.01193 | -57.44788 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0630a4ef-a2e5-381b-9b33-5b714879dbc0 | -20.02492 | -57.45648 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| df0b59a8-6cb2-3030-9f22-4f869ebe331d | -20.01717 | -57.44122 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 283390f2-4fe1-3a0f-8cbc-4e3b2dfb1694 | -20.01882 | -57.43834 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4dc5826e-239e-3a59-86a0-0a7bed7c04b4 | -16.46668 | -46.42463 | 2025-12-01 04:29:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8fd5b92-7e14-3cc2-a5ae-52a8f9d8abaf | -21.98107 | -44.51831 | 2025-12-01 04:29:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f27bddce-6778-386e-969a-5c850ce7b63c | -21.53216 | -49.52891 | 2025-12-01 04:29:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10499b01-a0f8-3a76-a262-a31ecb5d3fea | -18.95026 | -49.23541 | 2025-12-01 04:29:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d62adb19-7574-3cee-8a63-e1668c8f4d6e | -20.01992 | -57.43303 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| da11eabb-df61-3762-9c37-f5465217bdb3 | -20.02132 | -57.45006 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c041953c-de20-3231-850f-6b07bf413f6c | -18.1324 | -48.53739 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eda3140d-db8c-30ce-aa17-46fdf88d08f9 | -15.42047 | -52.19248 | 2025-12-01 04:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8a02a72-ac45-32cc-8385-04f20447cf39 | -20.01523 | -57.43194 | 2025-12-01 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| aeb7d3d6-f926-3988-9472-f7039f3e11ea | -19.3333 | -54.1758 | 2025-12-01 04:29:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 878d73fc-6e16-3fe9-afea-b07acd5ee106 | -19.06535 | -47.00334 | 2025-12-01 04:29:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69d69188-90a5-3ae9-aeb0-b956c80d0ebc | -19.83079 | -42.45555 | 2025-12-01 04:29:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| f0472fbb-ba30-313b-b139-fa5c52fc5f92 | -5.3396 | -43.5768 | 2025-12-01 04:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 967b3699-504b-36d8-9291-b39bd448491d | -4.3703 | -43.1508 | 2025-12-01 04:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f8467a88-c644-3811-a3e4-3dfa134c91de | -5.3398 | -43.5535 | 2025-12-01 04:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5206a363-8233-3d5c-af7f-5386df528877 | -4.3879 | -43.3129 | 2025-12-01 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 68760a46-8238-338d-b557-c99dddad99bd | -3.6008 | -47.2739 | 2025-12-01 04:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 8cfe1bbd-11f2-36d3-bc2a-490eeecc8877 | -4.4064 | -43.3351 | 2025-12-01 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 61ca852f-694c-35c0-b26c-da3cdd15bb90 | -4.3877 | -43.3362 | 2025-12-01 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| cc114763-9c43-3699-a1f5-9c5c36561043 | -3.2174 | -50.139 | 2025-12-01 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ea114f51-36a6-31db-acf9-749ec7e10ce1 | -23.17907 | -45.66412 | 2025-12-01 04:31:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6cf57090-6725-3317-9d73-3767f17c7e79 | -23.11852 | -45.28627 | 2025-12-01 04:31:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cab333f5-56cc-367f-85c1-bfed799ad74b | -22.72605 | -47.3584 | 2025-12-01 04:31:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c4f8198f-4a3b-3c53-a275-892f0e8014fb | -24.1237 | -50.14875 | 2025-12-01 04:31:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a5077809-718a-36f6-b765-ec143b9b92d0 | -23.12576 | -45.29277 | 2025-12-01 04:31:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6b8117f5-ef85-35b0-83be-4123957d4d2e | -23.12181 | -45.29222 | 2025-12-01 04:31:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 7956d850-89b8-3d76-b623-0cdd5942f8b3 | -24.12098 | -50.14436 | 2025-12-01 04:31:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6b2c2ce7-afb9-3317-9e37-e87b99f0111b | -22.7262 | -47.36016 | 2025-12-01 04:31:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 981deb0c-f1f5-3c02-b924-d8433a9bbb0f | -23.19219 | -46.98996 | 2025-12-01 04:31:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e950f87b-027f-3e36-8a01-e52467f1c3ad | -23.12971 | -45.29332 | 2025-12-01 04:31:00 | NOAA-20 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b86be65c-3e13-3431-a105-83a26faa5182 | -23.18292 | -45.66491 | 2025-12-01 04:31:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 23277de2-b2a4-3931-abde-13f5a6a1e8b0 | -4.4064 | -43.3351 | 2025-12-01 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c2b290aa-1555-3008-a812-c807ea7046e1 | -5.3398 | -43.5535 | 2025-12-01 04:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 93d121b0-9489-397c-accd-179311b3b11f | -4.3703 | -43.1508 | 2025-12-01 04:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 41e5bb5c-2a89-3fec-9e12-04b0dc8397d4 | -4.3879 | -43.3129 | 2025-12-01 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ab2f1c49-f8d3-3fbf-a4aa-522363d14721 | -4.3877 | -43.3362 | 2025-12-01 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| c864c2e4-0c5a-3d71-8a5e-7e3bdf548f73 | -5.3396 | -43.5768 | 2025-12-01 04:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 28f17ca6-a643-3b8f-9261-faae78c84d5b | -4.3877 | -43.3362 | 2025-12-01 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 3c2bd3a3-d7b4-3738-a94f-f626b388bde2 | -5.3398 | -43.5535 | 2025-12-01 04:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 43663bf0-64fa-3c69-b383-1c4733ec52bf | -20.0343 | -57.4457 | 2025-12-01 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 8276de38-78fb-3903-90ea-4ea2e4c29f84 | -4.3703 | -43.1508 | 2025-12-01 04:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| d21be5c8-4a07-3f47-90c5-8d200313e654 | -4.3879 | -43.3129 | 2025-12-01 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| cbf88f21-28ae-3b45-ad25-8e2b3de54712 | -5.3396 | -43.5768 | 2025-12-01 04:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ea5be618-903f-395c-9a31-98e892f59383 | -20.0343 | -57.4457 | 2025-12-01 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 87f802c4-f3c2-3850-b8de-ddb579387285 | -4.389 | -43.1497 | 2025-12-01 05:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 5a1f7031-a0c1-308f-a44a-5d6728756954 | -4.3877 | -43.3362 | 2025-12-01 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| fef8a138-4912-3d65-a494-37c6e937c18a | -4.4064 | -43.3351 | 2025-12-01 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2f987e6e-896e-3b4f-a9b7-e464343b56ae | -4.3703 | -43.1508 | 2025-12-01 05:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 570fd07b-a421-38cf-819d-c45a8eea1596 | -4.3879 | -43.3129 | 2025-12-01 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4fbf5e55-679f-37c5-9bf1-9707c4c2c5cf | -5.3396 | -43.5768 | 2025-12-01 05:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a06655b8-8fef-36a5-abc1-f1bfb4b05f8f | -5.3398 | -43.5535 | 2025-12-01 05:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 14d917f4-9216-3917-8ff8-0870637dd59b | -4.3877 | -43.3362 | 2025-12-01 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 676ef325-cda8-3bed-9c51-61008d374c73 | -4.4064 | -43.3351 | 2025-12-01 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a6991103-570a-3269-8291-abb302af4890 | -4.389 | -43.1497 | 2025-12-01 05:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| fcb9e0e7-2113-3327-b925-6311ddd1dad6 | -4.3703 | -43.1508 | 2025-12-01 05:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 28fac081-6451-345e-a6a6-66d10dd35b90 | -4.3879 | -43.3129 | 2025-12-01 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 11935c0c-0b7d-3de9-957c-fe528852eb33 | -9.09512 | -35.33035 | 2025-12-01 05:10:00 | AQUA_M-M | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| a9a476b6-b106-3e6f-8d24-229f5383b84d | -9.09676 | -35.31992 | 2025-12-01 05:10:00 | AQUA_M-M | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 464c2c5d-4b7b-3005-adaa-e9d952d39a3d | 3.47888 | -51.2672 | 2025-12-01 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a793df0-e24b-3dee-8697-68eb3f71b60f | 3.49572 | -51.42012 | 2025-12-01 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0c5702b-aaef-366c-8994-a629caee08a2 | 3.35294 | -51.30598 | 2025-12-01 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a45f1f0e-abb2-3db2-b168-eb2c618a4835 | 2.70195 | -51.38521 | 2025-12-01 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d42d875-5745-3f6f-90f4-71680fad190b | 2.29414 | -55.95441 | 2025-12-01 05:14:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb5d2b82-c81b-3a7a-925e-0eadee6f7560 | -3.21134 | -50.13459 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 69dd8024-9ad1-3e3a-82c6-1cc4e058740c | -2.94061 | -53.28141 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5bb1c20-5d98-3fa2-8c05-458be0f9893c | -2.14541 | -53.6477 | 2025-12-01 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 817dec7f-6f2d-3c5c-b1d0-70b00ae903ac | -2.93936 | -53.27729 | 2025-12-01 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54e8f7ab-d229-3835-9cda-b1f0e5939f0b | -3.17814 | -50.31185 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31ed81b4-638d-3dff-a52e-44db4f4659af | -2.25181 | -45.61267 | 2025-12-01 05:16:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d091dc42-f907-37a7-ab0d-9aee372a0cf4 | -3.45034 | -50.55056 | 2025-12-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README18.md)
