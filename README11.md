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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0b214f1-db02-310b-83ce-03c254e7d764 | -18.53397 | -56.81092 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7f895daf-1ae7-3791-8fbb-9c936c22bf8c | -17.57429 | -47.50204 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 45cf9adc-463c-31a8-8466-745838410f05 | -17.5842 | -47.51007 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d6b010e-02fe-37b0-8f6a-aa4d2f6a9e44 | -17.57963 | -47.50266 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 121b7f9e-d24a-3721-96e0-1403021a3947 | -18.53672 | -56.81513 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 133ce403-5486-366b-9b36-b5988a7d9eb8 | -17.58383 | -47.5134 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92869fe1-a8da-3571-970d-1b8a9d4c234f | -18.53454 | -56.80728 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2d4e6d41-b852-3fca-997e-29dfc56b434c | -15.43884 | -55.89013 | 2026-07-22 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| baec4c16-f71a-3e70-a124-3cf195c4785b | -18.53615 | -56.81877 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| c2147f75-8324-3980-8fae-9566c38c293c | -17.57885 | -47.5096 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 04da5038-83ed-3d76-a5e5-44edb72e43df | -18.53122 | -56.80671 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0764f7a5-f236-3d1a-b404-defceec3f1b9 | -18.54335 | -56.81627 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 93c7b313-ed4f-3c85-8dc5-b412eccc7aac | -17.57775 | -47.51939 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f190fb53-7473-34aa-873e-293c60cf1320 | -18.53786 | -56.80785 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 42bb969c-84cb-30f2-b504-cbad9b692d16 | -19.19462 | -46.44595 | 2026-07-22 05:06:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56886a1b-a0d6-353e-9f0d-59f064a26f22 | -15.4416 | -55.89426 | 2026-07-22 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 44877c4b-685d-348a-85c9-a54b5956bfad | -18.5406 | -56.81206 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7045e779-0aac-381e-9b70-ce3ad537b850 | -17.57352 | -47.5089 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 83dcfd4e-8489-30b0-b21a-c53a8f7bd754 | -17.56857 | -47.50483 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9a3e524-b1a1-31f4-8bed-de776aa63b74 | -17.5682 | -47.50816 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e09bb79e-5b30-319f-a93f-345bf5b234fb | -17.57315 | -47.51224 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cf139a2d-68bb-3fdb-b3dc-6f702e3ea7d6 | -18.54004 | -56.8157 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| f270ef4d-424b-3059-94c0-68285f78abc8 | -17.57924 | -47.50615 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 30d611e4-46ff-34d9-ab3e-a99267359409 | -17.57811 | -47.51619 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d47740f6-545e-3415-bb44-54bd44a229b1 | -17.8425 | -52.48738 | 2026-07-22 05:06:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2eb17ca0-a25e-3528-b85b-3a0dfc003a14 | -19.20041 | -46.44695 | 2026-07-22 05:06:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b47cd4a-887f-3ad6-a29a-e39b41360611 | -18.5389 | -56.82297 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 67d94270-fe42-330a-b0a4-38f02eecb4ab | -17.57847 | -47.51295 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f7d68ab-ba84-3cd2-af43-78a4965b0eab | -18.53947 | -56.81933 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 9328bf6a-e264-3a7e-a3b5-35a155d46939 | -17.84349 | -52.48943 | 2026-07-22 05:06:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fb1b5de-fd47-33be-9b3c-13d0d2f013df | -18.53179 | -56.80308 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 53d76cba-a0ed-3a7a-96e3-1449b99d29ae | -18.55273 | -56.82161 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 77a8b951-b910-3da6-90b2-537280dff8f6 | -21.51593 | -48.61184 | 2026-07-22 05:06:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb8be311-2055-3aad-81f8-270d08872b8d | -17.56325 | -47.50408 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 375696e5-c23c-3bee-a318-8d2840e8de86 | -21.20109 | -47.88242 | 2026-07-22 05:06:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8abc810-a903-3d06-b98e-6b079b1200cc | -17.58347 | -47.51662 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1df765d8-434b-3de0-ade9-b760b471f464 | -17.5739 | -47.50552 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f1d02019-6d1d-3282-a41e-2a72af132c3a | -18.53729 | -56.81149 | 2026-07-22 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fa6d8178-1960-3dbf-854c-2de9f3c6b648 | -17.73649 | -52.74926 | 2026-07-22 05:06:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e803e225-31dc-30ea-949e-fa99edba02da | -17.7403 | -52.74981 | 2026-07-22 05:06:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7dc2827-df58-3aa2-bab3-cc3bcfc32edd | -17.58003 | -47.4991 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8be64da4-919e-3f60-8e32-bfbbacb33cbf | -17.56895 | -47.50138 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96673318-332a-3fb9-89b9-3efe9cfe0571 | -17.58459 | -47.50666 | 2026-07-22 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 838e7b54-43e0-3738-b838-f08b837dcdee | -23.51659 | -47.21441 | 2026-07-22 05:08:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b637e10-6125-30f9-a239-ef5bd9011ea5 | -23.27625 | -46.16381 | 2026-07-22 05:08:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5682ab2b-4bdd-3af4-9027-16c1e0aa7079 | -23.18101 | -46.12228 | 2026-07-22 05:08:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cc84a8ac-bb1c-3912-9448-3127497d4f43 | -23.17476 | -46.12229 | 2026-07-22 05:08:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d027b6d4-993a-3c14-8790-d109fbe18a3d | -23.17519 | -46.11698 | 2026-07-22 05:08:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 65d989b0-3240-374d-b886-6eec114bf036 | -23.14445 | -48.67256 | 2026-07-22 05:08:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7281cdf3-69d8-3f54-b626-59569142afbf | -23.18036 | -49.69136 | 2026-07-22 05:08:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4acc765f-6cc7-3be7-8cfe-d573870d15a4 | -23.13877 | -48.67601 | 2026-07-22 05:08:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1b59f2a-3fe4-3688-b5a4-39b57b9103a7 | -23.18143 | -46.11712 | 2026-07-22 05:08:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7813f678-73ab-3135-8871-66c977a8cf63 | -23.28283 | -46.15965 | 2026-07-22 05:08:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4078d48-ffef-383e-b0b5-bf79b778d168 | -23.52239 | -47.2153 | 2026-07-22 05:08:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5e6f26d2-07ea-334c-8679-148410f2b418 | -23.27665 | -46.15878 | 2026-07-22 05:08:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a41c019-b77d-39fe-a3c5-855ad43c1119 | -17.5748 | -47.4996 | 2026-07-22 05:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 451e3341-1a96-347f-910a-114e957a6328 | -17.5947 | -47.4956 | 2026-07-22 05:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 41a289da-c8b4-3598-b078-bba12432ccef | -17.5748 | -47.4996 | 2026-07-22 05:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a5cb26dd-0efe-3227-81c9-3129e9ae25e5 | -17.5748 | -47.4996 | 2026-07-22 05:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 72bb9504-abac-35ac-bc67-468e0465d42f | -17.5748 | -47.4996 | 2026-07-22 05:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1263ec73-1347-384d-a685-a6744942688f | 2.51849 | -60.65134 | 2026-07-22 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d63ff950-bae0-3fa0-8ea7-2687264157b8 | 2.51923 | -60.65606 | 2026-07-22 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11fa4c53-41a3-30a9-955b-34da079c9c61 | -6.22026 | -55.60266 | 2026-07-22 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26ae885c-a2b2-34f9-a447-c72bd8e92409 | -1.81614 | -54.48322 | 2026-07-22 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f1ba70d-c116-3403-8395-b0d6059c919a | -1.81687 | -54.47839 | 2026-07-22 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d3e35a2-9d48-3629-8976-677b1867c46e | -17.5748 | -47.4996 | 2026-07-22 05:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b136f187-a833-340c-9296-0ce572210c8f | -9.10317 | -59.40028 | 2026-07-22 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afd1fa7d-f5b6-306d-b992-ec16220a820f | -9.47556 | -57.31868 | 2026-07-22 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65c00340-0ebf-3c26-96a6-b10841ce01c4 | -9.97082 | -64.94247 | 2026-07-22 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 422eaf2f-2a3a-3d74-9fcd-5db33e02f149 | -13.31868 | -54.33319 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90aa306d-0c90-3a9e-ba9d-8882ef7b123b | -9.10244 | -59.40597 | 2026-07-22 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7dcef4e-55e3-3999-b093-2c327c69ad99 | -9.48127 | -57.31954 | 2026-07-22 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6242f702-20ee-3ed1-ad72-fcfbc6e71843 | -12.88266 | -58.29059 | 2026-07-22 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1277f68c-bfa2-3828-ac7d-3806b3281ff6 | -9.60767 | -66.33884 | 2026-07-22 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3ba4980-3b48-33da-af45-d41fc623f2f3 | -13.33447 | -54.32046 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0fe4f6ea-a384-3ba1-b2d4-0f3f5d47ab66 | -13.32657 | -54.32687 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49161a9a-543e-3578-9e77-6f7e4e8e1007 | -13.3273 | -54.31945 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b77d29e2-877e-3755-90ee-56e18e76a903 | -13.31941 | -54.32575 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f3b1b3e-4813-361d-b6dc-b5aa5e23945e | -13.31646 | -54.32817 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1a2fbba-fa38-3356-a201-27747e9717d4 | -9.9501 | -67.20744 | 2026-07-22 05:50:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34541c42-4f26-336f-830b-1870ee5d6637 | -10.10225 | -68.17126 | 2026-07-22 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eab48293-dc1f-348c-8f88-2a700e487a97 | -9.18806 | -58.06594 | 2026-07-22 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b5cda26-7e42-3477-be7f-db2b8f3d1178 | -10.16577 | -56.79975 | 2026-07-22 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddcc55bb-41c1-3fae-bf50-cf0c481b960b | -10.02301 | -65.05255 | 2026-07-22 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc3eb05b-1bd1-3c0e-bdf5-383325b12261 | -9.10711 | -59.39888 | 2026-07-22 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f116433-0791-3e4f-93b4-0fa76a1a59a7 | -9.11801 | -61.09064 | 2026-07-22 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2251de52-5d93-33fa-97b9-b2b3392c2a29 | -9.10137 | -59.40392 | 2026-07-22 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81c98242-a3a5-3ffa-a8fc-f11bcc4e0781 | -12.41506 | -62.03666 | 2026-07-22 05:50:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dda9d1d7-c680-3bd4-8a45-f87f67535618 | -12.88312 | -58.28677 | 2026-07-22 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8dff448-d2a4-3510-a833-ccc8a8d49ef6 | -13.32438 | -54.32196 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 957d4f81-2734-30df-90f8-eaf6fd101ebb | -9.18762 | -58.06944 | 2026-07-22 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03790a82-c6df-3c35-9a5c-31a395136145 | -8.49388 | -54.77633 | 2026-07-22 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfad1749-bda7-32d3-9773-f9158fe1e7f2 | -9.03795 | -61.34097 | 2026-07-22 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3cdd6ab-faf0-31a4-9168-a72041529798 | -9.10216 | -59.39821 | 2026-07-22 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b80779f3-afc5-3305-90f0-7baa94cba0e9 | -13.33154 | -54.32297 | 2026-07-22 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b2f0ae0-773a-3faa-a33d-b613daac09b8 | -10.01643 | -67.69998 | 2026-07-22 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a9985a4-914f-36b5-9deb-2bb5b1c35dd4 | -18.53525 | -56.82191 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6c46e186-e832-3997-8ea2-ebf8b02a8d4a | -18.53632 | -56.81023 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| de94bd23-462e-3546-8d1c-d7b07462e526 | -18.54182 | -56.82267 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f082fd0a-c91f-3aef-93d5-f3c0196b06bf | -18.5346 | -56.81482 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README12.md)
