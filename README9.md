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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93bd2b13-1b2f-3f9a-9594-2675ee3849a4 | -20.70419 | -50.52165 | 2026-07-10 04:38:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ca735b3-fb7a-3c1f-baef-4ead28ca6212 | -22.28873 | -54.82874 | 2026-07-10 04:38:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c8e6402-7f2d-3f57-84d3-0af5885d833e | -20.70751 | -50.52221 | 2026-07-10 04:38:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27a37802-1f9f-34d4-a239-e36b9a575be9 | -23.89712 | -47.89449 | 2026-07-10 04:38:00 | NOAA-21 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eee5c0d9-2f4c-3ef5-b734-7e371a4f1d18 | -21.44841 | -54.56448 | 2026-07-10 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd609a9b-bc13-34fa-a0ac-2d46f0124edb | -21.12819 | -54.37425 | 2026-07-10 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b983fc7f-0305-3f85-bf7c-4e495aa41a7e | -21.09945 | -57.46806 | 2026-07-10 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de68d922-d045-3204-b6ab-9c43968a1e2e | -21.44408 | -54.56812 | 2026-07-10 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc75ae46-0197-32f7-a7bc-4c4ebdbb9b23 | -20.70363 | -50.52536 | 2026-07-10 04:38:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ee3b179-59aa-3761-b526-0e5fd07906ce | -23.56429 | -47.50928 | 2026-07-10 04:38:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 08539aa6-215f-3edf-8859-59f5e96e9e87 | -22.92264 | -49.20647 | 2026-07-10 04:38:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05e161d-f75b-3e48-a85d-848be7804a92 | -21.7617 | -56.30069 | 2026-07-10 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 976b01a0-b80a-36a3-9118-5b8cf2ecd483 | -28.83186 | -55.70473 | 2026-07-10 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| b66a0d97-307c-3bf2-9a8d-9a984f98897b | -0.35903 | -52.02041 | 2026-07-10 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53c880ac-d4b9-3a6e-a18a-790892d8be11 | -7.72725 | -44.56284 | 2026-07-10 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ce895d-7951-3bb0-9395-159abd9702eb | -8.50694 | -48.06683 | 2026-07-10 05:08:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40251be4-82c8-34ec-a6bd-529b47c2ddb4 | -6.67709 | -45.73367 | 2026-07-10 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dd2e1f7-d573-305d-a13b-e6c9f6432014 | -6.06867 | -44.0084 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d882cc6-ee41-3a2b-8ea5-5589ce6b389c | -6.0698 | -44.00635 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d4c2bbb-1e49-3254-8f8a-5d6cd1463182 | -8.72243 | -47.83487 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ba8a289-6ea0-30d0-b47a-3e84cd704d3a | -6.55535 | -55.15926 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a690e2-8a24-3d73-992d-8b35fe0dd998 | -6.50377 | -42.21625 | 2026-07-10 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d8823071-0864-3c41-8b47-f3a66ab4d99c | -8.50759 | -48.06215 | 2026-07-10 05:08:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 267832e3-9732-3100-80ca-5ba71612f23c | -6.55647 | -55.15226 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2500fe01-7781-380b-950f-daa28614efa4 | -6.55981 | -55.15279 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8d4792c-ae3c-3016-bad8-ee56ce8d9bbc | -6.5715 | -55.14386 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a49b20e-c298-3830-8bed-e8bbbada4b44 | -6.49724 | -42.2153 | 2026-07-10 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c9d907e9-5ca9-3993-91e1-af33020abb51 | -6.42134 | -55.79242 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1039e4d3-26c8-30de-91a1-edfb272b08d2 | -8.71779 | -47.83413 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7be42080-c3f5-3702-b96a-34b5a6596c64 | -4.61714 | -49.04905 | 2026-07-10 05:08:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1515cb3d-3a0c-3549-84e0-4d0c563aac8b | -6.07448 | -44.00919 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 662e4ec4-ce49-3c9b-9596-868e435c4da1 | -8.03607 | -47.4318 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 550e6eca-e07b-398f-9090-377dd865ff22 | -8.71981 | -47.83599 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b01905bd-1c1f-3259-a33e-b3ce6271f7a0 | -8.11938 | -47.59144 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 040e0abb-93b0-38ab-b666-90ee275d9067 | -2.22694 | -51.93618 | 2026-07-10 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46ad6466-1991-33bf-8de0-5bdf9820cfbe | -8.72103 | -47.84465 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2896a75-3199-3779-ac0e-a262efcae7ac | -2.74614 | -54.59471 | 2026-07-10 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cb63d77-2afa-348c-bc91-bc24db8939c9 | -8.72379 | -47.84164 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db822fa2-0fc5-37e3-9341-9ecd5edc4537 | -6.0751 | -44.00473 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f4f663c-16a3-37fb-8e94-f0ac3176ef48 | -8.11604 | -47.09981 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cef760f4-1b46-3206-a1c3-a71696d70ad1 | -6.07389 | -44.01348 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| faca04cd-bc2a-30f0-9666-d6b32f9cbd0b | -8.03747 | -47.42152 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca926cbc-9696-3d89-9434-e17025bfa3b0 | -6.55201 | -55.15873 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6b22a4c-9831-368b-9d3e-657079c92e76 | -8.50303 | -48.06143 | 2026-07-10 05:08:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50d5c0c3-ec29-3874-afac-6e3c8b1dcbe6 | -6.55145 | -55.16223 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8202619-450a-306e-8f44-6700d3d6a3f1 | -8.11119 | -47.09906 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c9f183e-2dec-3bf8-9537-a2ab24c0a5b7 | -5.46662 | -45.4265 | 2026-07-10 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 158b3015-8cb0-3be0-8a80-8950917ccaeb | -6.49799 | -42.20986 | 2026-07-10 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c17ac415-a232-31bd-9418-dc703008cece | -7.01529 | -45.4201 | 2026-07-10 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ae98d25-3097-358c-b89a-8bd98961dd1a | -8.03528 | -47.43002 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bc721619-5a36-3691-8689-804158350dd5 | -8.03133 | -47.43114 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9806b19-0f96-35e5-b0e8-838cb0568ce2 | -6.56314 | -55.15331 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d8034e8-ca69-37a3-9da5-33cdab6ecb02 | -5.46617 | -45.42965 | 2026-07-10 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2719dec-1c9e-3b4c-9877-c6d5c5c9a25c | -6.55924 | -55.15628 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a1bcc4-bcad-3b51-bfdd-c74802e610a1 | -6.42752 | -55.79711 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f84603cb-2e92-3626-a4b6-0cf85edce488 | -6.67665 | -45.73685 | 2026-07-10 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 444b8f66-9d01-397f-ba64-7b6d171f4eae | -7.90253 | -48.05612 | 2026-07-10 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4e97619-107a-38a1-8c5f-c201fed0d184 | -7.08997 | -44.34868 | 2026-07-10 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 713a2326-9c93-36fb-b0e0-cf081152d981 | -8.03676 | -47.4267 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c54b3a3d-f2af-3580-8fb4-5c57d33f2519 | -8.11866 | -47.59642 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff8d115b-4274-34a4-b4c5-f05e04a3a367 | -4.15343 | -43.09518 | 2026-07-10 05:08:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84ce3132-773c-3560-9bfe-bad9e84330af | -8.72512 | -47.83187 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b27ba8b2-6dc2-325e-803d-22e9adfd3793 | -6.55591 | -55.15576 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0a1542-5915-3cff-aae5-00f6a4b5b00b | -6.50452 | -42.21085 | 2026-07-10 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7368ff7f-d29d-3792-ba01-9ef3da02bad9 | -8.13392 | -47.87166 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 904296fc-ca1d-32b3-af4b-5f4de0014f3c | -8.03603 | -47.42488 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7b93985f-8d73-3084-aff6-27b793bbf34f | -4.15942 | -43.09604 | 2026-07-10 05:08:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba848e21-ba49-3dac-a77f-52fe74f4e66b | -6.42076 | -55.79602 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6c827bb-2e0f-3c93-afdc-2e4fc6496779 | -6.06919 | -44.01056 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9459a081-6669-37db-9f5f-25370c8f3b2d | -8.72174 | -47.83974 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 315701fd-d8e9-3b30-997f-9c68c8ce8a57 | -4.20186 | -56.0406 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 806a08c4-9b9a-3f4a-8e85-957153de3afd | -6.4309 | -55.79765 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ecaee9b-92e0-3dfa-8d77-c39279c77b84 | -8.72047 | -47.83114 | 2026-07-10 05:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a084b2-aa47-3c50-9fc2-5f3255fba3f8 | -3.94304 | -54.84146 | 2026-07-10 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19c748b0-10eb-32c7-94b6-e513ebbc65e5 | -6.42472 | -55.79297 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3f1e917-21df-379c-b41a-99ea80a059b2 | -7.72778 | -44.55893 | 2026-07-10 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd9a986a-bcba-3ba9-acf3-1741cadd0d21 | -6.42414 | -55.79656 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 029d6143-8297-3f98-b760-36262a08ec0b | -8.04004 | -47.43053 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d10b33e5-3245-3293-aee4-2638befeb899 | -7.08368 | -44.35003 | 2026-07-10 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be310cbe-996b-36c7-9876-e5cc8d8eb05d | -6.12576 | -55.80843 | 2026-07-10 05:08:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9935ff4-9e91-304a-9fd3-531fd5f141de | -5.47184 | -45.42736 | 2026-07-10 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d642acb-14fc-3d0a-bf85-4081ab9227da | -7.00992 | -45.41947 | 2026-07-10 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bead1e5f-8a7a-3494-bcc9-f0c5f43f8384 | -8.12866 | -47.87566 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48b6d5e0-0106-3529-b4be-361573c3c032 | -7.08418 | -44.3481 | 2026-07-10 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3358beb-41c0-36aa-ab97-aa31920f73b5 | -8.12932 | -47.87099 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 044730ba-f12f-3c4e-b8f9-5cf86253444a | -8.12047 | -47.59419 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b82e45f3-da74-37da-b239-63a399bf4517 | -8.50239 | -48.06607 | 2026-07-10 05:08:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4e3294e-de89-3093-b33b-7b5ec9a76ffc | -6.58572 | -51.69986 | 2026-07-10 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 398da64e-77ce-379c-a7eb-9d8f883b5f6a | -6.58633 | -51.69586 | 2026-07-10 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 350a0d2f-7685-3e2f-a01a-b9e69d139440 | -6.50261 | -42.21332 | 2026-07-10 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| cef21b8d-c179-3938-be85-3a3b5204165a | -6.08031 | -44.00986 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 96026f9c-a4e7-3583-8739-a2619681a336 | -6.92 | -43.70303 | 2026-07-10 05:08:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8105f32-c8cc-3e6c-b749-a31780ca2cc1 | -7.08422 | -44.34618 | 2026-07-10 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28cd3de2-5919-38e9-9ee8-4ef3455207bd | -8.04083 | -47.4323 | 2026-07-10 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c5bc512-2612-3f5f-bae8-f982a26b1192 | -6.57093 | -55.14737 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4f3acc5-a634-3c71-aa8b-01a36f82110a | -6.08093 | -44.0054 | 2026-07-10 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7d61a7a-cc7a-3267-bd43-97df81dabb78 | -6.56592 | -55.15734 | 2026-07-10 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca5356e1-f36d-3480-ac27-948e3ca6bc78 | -4.94401 | -48.24703 | 2026-07-10 05:08:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6327592f-9c78-3c12-b325-5d076412cdd0 | -7.90417 | -55.42907 | 2026-07-10 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52adddf0-17f6-302c-8077-53b73f4bacbf | -11.47324 | -52.92076 | 2026-07-10 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
