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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd86c7ab-8a15-3736-ac66-7d79f4c63251 | -6.40932 | -51.66903 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3466ea3b-8ec3-3b7f-ab5d-95bc81097307 | -7.50264 | -55.31076 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 874100b2-7ee2-3f93-8f6c-e0a70f9ec1d4 | -11.20641 | -51.26659 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7410b75-6c3a-36e8-bb74-3f9f1cff31ef | -8.59917 | -54.77651 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 774875ed-726a-31f4-90b0-ff5377782a2b | -11.17967 | -51.28436 | 2026-08-29 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c4a9418-5dca-3341-8596-1a9f7befcc77 | -12.19125 | -50.55159 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fdfaab5-6862-3ede-a8ff-3561d1cf3c2e | -6.82264 | -59.95329 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2350ac-5b76-3a0e-b546-9237cc52eb57 | -9.96774 | -53.93472 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8626f107-ec63-3409-a058-4e31857a06b7 | -10.76223 | -54.01053 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4fa4974-a841-31fd-b3bf-83de561e19e7 | -11.25498 | -45.07139 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f9dc4bc0-ed02-3735-9811-13dfa199fc1e | -8.9798 | -50.7872 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f87cfd69-62e1-37ba-926e-d72dee8a0818 | -7.35239 | -55.15956 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 105e8bb5-e2e4-3581-aa87-b6ab942599b5 | -10.32478 | -49.96262 | 2026-08-29 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6000ed15-6382-3729-b044-8903a67c0282 | -16.60958 | -49.40786 | 2026-08-29 04:53:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db853ed9-9554-3a9e-8b2b-10236b44d467 | -11.26583 | -54.04398 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b161d15-b823-3e4c-80d4-1c120cb80431 | -11.36404 | -45.15084 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55ce5b7c-7771-32e1-ae64-b5e8d0946c09 | -7.50637 | -55.31142 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 87c53680-8366-3335-95e2-653f86495940 | -10.88656 | -50.50132 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82047bbd-9329-381d-9a0c-c3d9042d05c9 | -12.37995 | -48.19127 | 2026-08-29 04:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cda1777-e514-3b8e-bdad-56cc3af00a42 | -8.5534 | -54.78586 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 465366b8-4803-3890-aade-42901001786f | -6.58021 | -55.44295 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74cb6039-a072-3626-bdbd-1df2c7bcccb7 | -11.26984 | -54.04081 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5048c51-9484-3bf0-a7ca-376df44ebd4e | -8.52967 | -55.3506 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a31d4fac-2e2c-36bd-8958-f0bf37afa4ce | -11.35877 | -45.15493 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 602f56a2-68f8-31b3-8b22-fe9b34919d4b | -8.94945 | -63.27237 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74df3345-c128-3818-8f9c-6da9aee447ae | -6.49598 | -53.25845 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 739a1c05-d8b8-3ad0-80b2-fddd7ed09da9 | -10.7575 | -53.97541 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75511b87-ab5d-3270-988b-9ad7308357d4 | -19.28028 | -49.52257 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6d96d25-5ddd-3038-be0a-52cd88334074 | -10.75263 | -54.0051 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72631db4-fff4-3a54-9b97-1f89ea393563 | -11.03198 | -57.22828 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 167878e5-4c98-3332-9abc-d6d70a73deb6 | -8.53261 | -55.35567 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 204d00de-b989-3511-aa2c-a7d93dc941ff | -7.25292 | -45.86005 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4c2fa7a-7b81-332e-9f2f-8bfc04323f69 | -17.3038 | -54.93446 | 2026-08-29 04:53:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ae61acf-3eeb-3529-b1bd-dbe25b22893a | -10.75578 | -54.02858 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ebde847-4093-3732-bcb2-a4acd39ebe48 | -7.34273 | -55.17199 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 972d52e2-ecc3-351a-87e9-c97e0699b685 | -6.15046 | -57.80505 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87b6dd39-4b03-35a0-b86d-87c8c108c6b6 | -7.55847 | -61.30668 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c18fc5d-245f-31cd-8a5b-93803e970d6c | -7.58156 | -61.33757 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a08eb513-12bb-3cdd-bb62-f5c7b58cf707 | -20.23076 | -47.39425 | 2026-08-29 04:53:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 432e592a-66fa-3683-b8ba-f8cdabfe4227 | -17.81996 | -50.94722 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 815f0452-dbe5-3675-9d3d-6f71bbdff389 | -6.16328 | -57.78434 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0372cfbd-86f4-3382-8b34-604402d576b3 | -9.87503 | -60.30051 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d36d0bda-531a-3c5b-98ce-98c767e25b4a | -14.17021 | -52.8286 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fc4e5e8-4e18-3a64-9de9-4bffb63db2f6 | -14.20165 | -52.84472 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b253ae1-cb95-3a79-ba39-6fd9563c4f0b | -15.55949 | -49.95335 | 2026-08-29 04:55:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 839ef384-c544-3a6b-a41f-0633103e08ef | -20.95429 | -57.58469 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 311c9b07-f6ff-3c21-b2b6-c3def18a58bd | -14.75914 | -48.7523 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c73b7cb-d94f-3129-b2b5-833a6266d0f9 | -14.9062 | -56.33619 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18567c88-a6e7-3f42-8333-d4236e764393 | -20.94312 | -57.56486 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 67676df1-37ff-3638-b2f5-9615b7d534c1 | -23.20101 | -46.9926 | 2026-08-29 04:55:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 392bfc21-4127-3bde-833b-fa6cbbdc8ae1 | -13.46803 | -57.04114 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 957dd453-7539-314e-8d7d-0713da3e01c8 | -20.95971 | -57.61661 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a96c214a-f289-3825-8de9-9c35d2075474 | -14.20883 | -52.84227 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ddbd9cd-b7f6-39d4-be02-d9a6a3be8ba8 | -14.9299 | -56.32749 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73f0b7de-c918-3ccb-ac6d-c9b202d9bd57 | -20.90631 | -57.56625 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ec24b78f-cd4d-3d33-b446-9b0942c1e806 | -14.90951 | -52.6391 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e08eb9f-2b51-3bb4-bcad-0bbcf58cd4f2 | -13.45193 | -54.02386 | 2026-08-29 04:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a745663-e3fe-380f-97db-083a9b68c126 | -14.75531 | -48.75159 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa90201a-1a33-3bca-946f-43d19f04b2f6 | -15.11813 | -53.57726 | 2026-08-29 04:55:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e41a6a7f-cca8-314f-80b0-9b43409b29cc | -14.94138 | -56.32522 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f406854-9621-3596-9b01-c0ca182532b4 | -15.59117 | -53.07738 | 2026-08-29 04:55:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0ce8a5a-33b5-3ca0-822b-5e5f58c0076e | -15.73864 | -51.16879 | 2026-08-29 04:55:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2bc9454-205f-3f53-84f3-9458e5fa3d0a | -19.22482 | -57.65382 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 22804bd4-2155-33d0-83a2-e772accc1d4d | -14.97953 | -52.60304 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7f16b5d-abc2-35e7-ac6d-630fcf6ac63a | -14.90335 | -56.3313 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc1e31cd-c2e2-39a4-a54b-71a1be028802 | -15.37162 | -52.67779 | 2026-08-29 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53d6e483-50d7-3ce5-9962-047090d74706 | -14.30394 | -51.70761 | 2026-08-29 04:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ee831f0-a466-3442-95ff-110bfff58c3a | -14.19722 | -52.85127 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56184038-2be2-35da-96a3-a6f3e90aba28 | -14.19778 | -52.84772 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b6e77f5-afdb-3323-8b75-f057b351272f | -13.85873 | -54.09196 | 2026-08-29 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b068972-284e-34a7-a0f1-f6ff672304ec | -14.7611 | -48.74963 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4f8eaff-d66c-3941-ae1b-23f3405f2139 | -14.89846 | -52.62262 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a756d84f-e49c-3df3-ba9a-2ef251cda609 | -14.20053 | -52.85182 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca47fe3-13a2-3cd2-a3a3-aecca45147a5 | -14.16358 | -52.8275 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb3b32db-14bd-348a-acc2-242213d12e88 | -15.12452 | -53.57816 | 2026-08-29 04:55:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ebdd4205-f2c7-38f8-943d-eed9d51ac8aa | -19.22408 | -57.65802 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 86630777-e2ec-3b9d-8b12-554df9835506 | -14.19833 | -52.84418 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8eee576-8e66-3622-843d-7639d47f6019 | -14.93634 | -56.33304 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e8459fd-617d-35e0-a6da-b76d933ef83e | -15.65967 | -48.37271 | 2026-08-29 04:55:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33774377-d165-364c-a7d5-55601c962240 | -14.94065 | -56.32946 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 351b382e-5007-3169-bf51-b15d78b85abc | -15.12063 | -53.58117 | 2026-08-29 04:55:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 29fbcd85-a2c2-38b1-a0d0-eedb54c55aca | -14.20827 | -52.84581 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28e210d0-c694-39dc-913a-7ab48fc3eb0a | -14.91061 | -56.31078 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27e470a9-845d-3867-8602-db15d5a24f2d | -14.18254 | -48.76059 | 2026-08-29 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce197ecf-2f5c-316b-9b1c-b9dde677ea95 | -14.90953 | -52.61715 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3466e63-5875-37dc-8692-50fbfbebcd3c | -14.1961 | -52.85837 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0124c1c6-0898-38d2-8dd1-3cbdb9330db4 | -15.66134 | -48.37371 | 2026-08-29 04:55:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a03c1c6-6d93-3fc3-97fb-5c663f900163 | -14.15971 | -52.83051 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3291379e-bcac-36e0-869a-933779538448 | -23.15932 | -49.23596 | 2026-08-29 04:55:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| def07c3f-a61c-3061-8531-5740f1d94e39 | -19.22104 | -57.65544 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 97411d83-a66b-3c94-9891-f4660be8d42a | -13.16798 | -55.65933 | 2026-08-29 04:55:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 132b61d3-6a4f-3108-b9aa-2c0cd63ac1ca | -14.19666 | -52.85482 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65aa7e5d-188e-3692-8e46-649fbb2d31ae | -22.45583 | -48.1587 | 2026-08-29 04:55:00 | NOAA-20 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40689b41-3b75-3397-aa73-83b7b69d89a2 | -14.2022 | -52.84118 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b287a76-1313-317a-8cc4-8b3c8a46d32b | -14.1939 | -52.85073 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 156721fb-742c-3a26-be99-fff9ae53362c | -14.90261 | -56.33554 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b838cdbd-ffd2-3e4d-8287-1f10e2159059 | -14.74149 | -57.65305 | 2026-08-29 04:55:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d464550d-f74a-3b50-88f6-263f432feab0 | -20.93253 | -57.56274 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 108d87f0-f37b-3d36-a5f3-1ddf0fdf1278 | -14.19446 | -52.84718 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12f0233a-3083-3294-abe5-dcf5dda4825f | -15.64203 | -45.92998 | 2026-08-29 04:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README56.md)
