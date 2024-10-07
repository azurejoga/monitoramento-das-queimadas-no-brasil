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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbd13e31-3cac-3d96-ac99-806a8f5d04dd | -10.8755 | -63.8979 | 2024-10-07 02:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c10e5e2d-b234-36b0-8397-b3e8cec30b0f | -10.8337 | -68.3636 | 2024-10-07 02:56:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e59e4e23-8312-316b-8e01-b82e77e814e0 | -11.247 | -51.3706 | 2024-10-07 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8b1b3603-42fa-3665-8595-a5ae6c88f64f | -11.2657 | -51.3898 | 2024-10-07 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 27b03c5d-0af8-3bbe-aba3-298f168e266e | -11.266 | -51.3686 | 2024-10-07 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b56dff1b-4286-3a8f-9459-19352a05d4e8 | -16.4161 | -57.3211 | 2024-10-07 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 0591857a-f59d-3b42-8d2e-731fa1c0a1cb | -16.4164 | -57.3006 | 2024-10-07 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 8dd48f3a-aa8f-3c94-8850-4d33bd4f4adc | -16.4167 | -57.2802 | 2024-10-07 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| be444adb-fc74-3940-ad19-6ea6a4002e53 | -16.4362 | -57.278 | 2024-10-07 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 185.6 |
| c26452da-32c8-3aad-a600-05f64ad283d3 | -16.4365 | -57.2575 | 2024-10-07 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 187.0 |
| d620ffc9-10c2-3ffc-bdc7-7916fb5c2526 | -16.4948 | -57.2713 | 2024-10-07 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 29f67ca1-f1bb-3320-86df-ee10936ed9f5 | -16.6136 | -57.1555 | 2024-10-07 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 32fc3fa4-43cc-31d2-8366-90e78583b98a | -16.614 | -57.135 | 2024-10-07 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 600a8cf6-124a-3155-9db4-d437097b5b8f | -16.6332 | -57.1533 | 2024-10-07 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| f9b26218-16d5-395e-8ebc-0423f795c124 | -17.02 | -55.0791 | 2024-10-07 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 25880e68-3ee6-3bcd-a236-2e316a0fabd3 | -17.0203 | -55.0581 | 2024-10-07 02:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 349cc502-c89b-36a3-a69c-8309c47bb2d7 | -17.012 | -56.698 | 2024-10-07 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| a115ab26-66d5-33b6-b145-c72ff7194c4e | -17.0685 | -56.8352 | 2024-10-07 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 12ac2378-63b0-3951-a416-13539c8e6b10 | -17.0881 | -56.8328 | 2024-10-07 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 3bbafd1a-86b3-368d-bfc8-5a19c88b91d7 | -17.0982 | -57.4267 | 2024-10-07 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.2 |
| 50f27435-285e-3983-b895-06b8b3831498 | -17.0985 | -57.4062 | 2024-10-07 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.1 |
| 25d1d004-f1d8-30e6-b8bf-ea15b46fa004 | -17.1074 | -56.851 | 2024-10-07 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| b254100a-7599-3fcf-a0c2-abb55bc23120 | -17.1078 | -56.8304 | 2024-10-07 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 9fc13749-3a7a-32ea-8009-76061023f46b | -17.1274 | -56.828 | 2024-10-07 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 1231f1f9-5d72-3530-a46c-5c6ea1eb8a2d | -17.1278 | -56.8074 | 2024-10-07 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 9b0cdc39-04c0-319b-9547-744d64593b98 | -17.1571 | -57.4198 | 2024-10-07 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 21bd92ec-38aa-3d8f-a15d-7b69e5d9ad75 | -17.1581 | -57.3582 | 2024-10-07 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| d01079e3-d05d-369c-8a17-ed0246e1593f | -17.6279 | -53.1094 | 2024-10-07 02:56:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 6448fb23-1a3a-35aa-8548-d8e917a53de7 | -17.6283 | -53.088 | 2024-10-07 02:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 19f6f804-e8d7-3a7e-9c38-88ac4fadce2e | -17.6477 | -53.1064 | 2024-10-07 02:56:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 23edf616-4d3a-3d43-b2b8-0be849923446 | -17.6481 | -53.0849 | 2024-10-07 02:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 0b9cb359-f09c-38f0-8de9-f5c838a1fee0 | -17.772 | -53.8132 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 150.2 |
| fe528d84-a8cc-31e5-883d-c6c8c5519270 | -17.7724 | -53.7918 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 69b712a9-57b7-3da8-a81c-afe0145a2c12 | -17.7914 | -53.8315 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 9b7ec9cf-0d5b-31bc-b675-8e99facea2ed | -17.7918 | -53.8102 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 457.4 |
| 3a5cacf1-23f5-3eaf-9936-0ca40d046203 | -17.7922 | -53.7889 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 342.5 |
| bf2da6ea-7693-3266-aeec-33a2410e97c5 | -17.7926 | -53.7675 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 45657009-d8aa-38a3-8277-f859511e5a11 | -17.8314 | -53.8043 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| a7fc0649-4fb1-35f2-8d91-9e82ff5140a1 | -17.8319 | -53.7829 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 2a63e941-7a14-36cf-a336-bba3c9cc0442 | -17.8517 | -53.7799 | 2024-10-07 02:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c798417f-b462-3f8b-877c-efb415a38e9a | -18.301 | -47.1425 | 2024-10-07 02:56:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 90eacc0d-6c7a-3fb1-abab-17f8443cf1c0 | -18.3016 | -47.1192 | 2024-10-07 02:56:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 50ae1ffd-1d85-365a-9ab5-97653aea73a8 | -18.4518 | -53.5165 | 2024-10-07 02:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2c873c32-e6a6-3688-8bb6-e56c19cbf737 | -18.4718 | -53.5134 | 2024-10-07 02:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 13670ded-7d19-3842-8bd2-ad6a37913436 | -18.6387 | -57.2785 | 2024-10-07 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| ac2c01aa-c6e4-3890-be62-a7ace6dbdaed | -18.6391 | -57.2578 | 2024-10-07 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 7ef74893-8622-3871-af76-49af12073e39 | -18.659 | -57.2552 | 2024-10-07 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 28320824-dd72-3e0c-9059-78e3fbd8c95e | -19.1963 | -42.5301 | 2024-10-07 02:56:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| 0b5d18cf-7966-3537-a497-bbbe70456503 | -20.1223 | -49.0748 | 2024-10-07 02:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 023473f7-8725-3bdc-973e-0e97fee5903c | -20.1229 | -49.0518 | 2024-10-07 02:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 454.8 |
| 5f14d67f-024a-3e23-bb3e-ea3a91421d5c | -20.1236 | -49.0288 | 2024-10-07 02:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 1d58c655-95e8-3da9-b86d-3fa7a83cb288 | -20.1433 | -49.0474 | 2024-10-07 02:56:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a3293792-f7e1-31c7-97b3-0d0b33892582 | -20.4449 | -47.6875 | 2024-10-07 02:56:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 453.6 |
| c3d35b73-8f0c-37ec-bc1b-62b777d2fbe6 | -20.4456 | -47.664 | 2024-10-07 02:56:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 382.1 |
| 6ce084f5-5fa7-365e-be9c-9cd496038ace | -20.4655 | -47.6827 | 2024-10-07 02:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 578.9 |
| 74083807-1662-33f5-b11c-95b6a53e21dc | -20.4661 | -47.6592 | 2024-10-07 02:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 496.1 |
| c3bd7715-805a-3645-a864-59d4c93de314 | -20.486 | -47.6779 | 2024-10-07 02:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 78b75da7-091c-3a7e-bff6-a65e2a83d4aa | -20.4866 | -47.6544 | 2024-10-07 02:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 132.9 |
| e5310666-57b7-31bb-97a5-4a242caa4cf8 | -20.5848 | -48.5137 | 2024-10-07 02:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 0a1815e9-989a-3d60-8030-c6b8b7a229f9 | -20.5855 | -48.4904 | 2024-10-07 02:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 317.2 |
| 438d70e3-03d2-3fee-ae23-88d3e0dfe275 | -20.6053 | -48.509 | 2024-10-07 02:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 6fb85483-b228-3dc1-95a1-68efe3292c86 | -20.606 | -48.4858 | 2024-10-07 02:57:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 228.6 |
| b0607399-ccfd-366c-8b09-575d5590146d | -21.5691 | -47.7696 | 2024-10-07 02:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5e7664d0-1cad-364f-a6fd-16b29f843047 | -21.5698 | -47.746 | 2024-10-07 02:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 4f270413-6ec6-3d0a-925a-e79aea7b4693 | -21.5705 | -47.7223 | 2024-10-07 02:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 04272f3c-1977-350b-8b08-c648f4d83af4 | -21.5843 | -47.9536 | 2024-10-07 02:57:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 4ee3301f-448d-3c63-b3ec-778a9a43bdc5 | -21.5906 | -47.7409 | 2024-10-07 02:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 9c0e54d5-ef55-369d-8457-dcdcbd4582a1 | -21.5913 | -47.7172 | 2024-10-07 02:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 214.0 |
| b9de52db-fc7a-364d-a8a8-37b995e44f85 | -21.605 | -47.9485 | 2024-10-07 02:57:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 9540668d-5918-31a9-a765-6f55f3cc5a79 | -21.6121 | -47.7121 | 2024-10-07 02:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9507e399-6228-3e08-be4c-e7058855a1a1 | -21.59 | -47.73 | 2024-10-07 03:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ecce82e-abf7-3ef8-b673-cde54322438d | -20.57 | -48.48 | 2024-10-07 03:03:25 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 80e55720-303c-3d67-b800-20f11d098701 | -20.58 | -48.53 | 2024-10-07 03:03:25 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d1c2ae8d-5169-3fcf-bb85-05f922f74a56 | -20.41 | -47.69 | 2024-10-07 03:03:28 | MSG-03 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d6d87f10-5f5a-3d7b-a960-e69aa9172402 | -20.44 | -47.71 | 2024-10-07 03:03:28 | MSG-03 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 70056f8a-357d-3eba-87ab-22fb49cdd3b4 | -20.44 | -47.66 | 2024-10-07 03:03:28 | MSG-03 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4c7824f3-bc0a-331d-a997-076d1d9b1182 | -20.48 | -47.73 | 2024-10-07 03:03:28 | MSG-03 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0a5b50fd-1d45-3bac-8647-2867d512b4b8 | -20.47 | -47.67 | 2024-10-07 03:03:28 | MSG-03 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 52a44435-81e8-34f8-bec3-326e726c6d9f | -2.8754 | -52.8989 | 2024-10-07 03:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3eacd03a-6644-392d-b0c5-3bd0679de6f9 | -4.2728 | -43.7601 | 2024-10-07 03:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| edce44ce-ae0d-3b8f-8934-426816e519de | -4.2729 | -43.737 | 2024-10-07 03:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 42ad8816-d608-35c1-bbac-b3d664765918 | -10.8754 | -63.9169 | 2024-10-07 03:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9e959dda-2dea-3d0c-b2b8-6e0c5319a50c | -10.8755 | -63.8979 | 2024-10-07 03:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9bdbf203-05a7-3872-877f-3af50e8cccdb | -11.285 | -51.3666 | 2024-10-07 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0106d82a-9a20-36aa-b936-a14627dd8ec7 | -11.266 | -51.3686 | 2024-10-07 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 4beec5f2-9823-3181-8766-5ea08b8196ba | -11.2847 | -51.3878 | 2024-10-07 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a401aa5d-e034-31b3-ba54-870d2f25a390 | -16.4164 | -57.3006 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 7bbdc624-a9fc-3519-9e0b-01b39b4395d6 | -16.4167 | -57.2802 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 11905630-c99c-3523-a797-fb5b9559ef58 | -16.4362 | -57.278 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 4f9f58b6-def4-3bbc-bed7-db013ff1b3f2 | -16.4753 | -57.2735 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| db9aafd3-9047-304b-b7f8-bd43697ebcd7 | -16.5072 | -57.7387 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.5 |
| b8481aa0-47c9-3cd7-b2f8-d2270ee1db8b | -16.5075 | -57.7183 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| f7cefc3b-4791-3677-86a6-feedb8faa8ef | -16.5267 | -57.7365 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| ecc1a610-e149-35d4-80ea-7ced44e21095 | -16.527 | -57.7161 | 2024-10-07 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| a16d51ad-aeef-3ba2-89ba-d6e03c685995 | -17.02 | -55.0791 | 2024-10-07 03:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5cfed510-e68e-31c9-a4ae-241b5b2a1ffa | -17.0685 | -56.8352 | 2024-10-07 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 0ec55261-68af-370a-9a0e-b45b1f41ec37 | -17.0786 | -57.429 | 2024-10-07 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| b8e70d78-fd62-3319-888e-c9a34f88bdb7 | -17.0789 | -57.4085 | 2024-10-07 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 77b74503-e01c-396c-a6b3-e78699cf70d5 | -17.0881 | -56.8328 | 2024-10-07 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| 67d3bece-20f9-3094-a5ab-de7df1d65df9 | -17.0982 | -57.4267 | 2024-10-07 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |


[Clique aqui para ver as próximas entradas](README38.md)
