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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5826607b-873a-34a2-80e9-634ccd13f388 | -16.07827 | -50.48552 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f21de4e8-68c4-352e-a229-a5b5f2463a88 | -18.61614 | -49.92642 | 2025-09-09 04:36:00 | NOAA-21 | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| fd310e67-7139-308a-9eaa-4e41b6e8a417 | -15.08852 | -50.09355 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6cf76a1-c7ca-3752-9211-2afe032a3497 | -15.70512 | -49.89278 | 2025-09-09 04:36:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de6c996c-d485-388d-85d2-3ad1a4ea7990 | -15.77948 | -56.42463 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b549814-ff31-3fb8-9206-4cc06dd1d18d | -18.45875 | -49.54457 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 288f9e40-fbfb-3851-b88a-9ab78924cf2d | -14.54936 | -48.7648 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a68dff12-05a0-3a16-9128-4ec3ea1e1eb5 | -16.42509 | -49.29859 | 2025-09-09 04:36:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22c032f6-cdf1-31d7-ae2b-e4a81c12fef6 | -15.09916 | -48.07463 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 676e581c-90c0-340f-bee8-f4e47b8f0c38 | -15.7454 | -53.52819 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7cdd231-c910-3f64-b56e-d5a6d7dcfdf7 | -15.23839 | -53.76165 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ef0db48-dab2-3a84-b12e-2af4cf4d36d8 | -14.53464 | -53.15236 | 2025-09-09 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d0f3b3a-beb4-3857-865d-93520bcd6f0b | -15.24909 | -53.81016 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd7a9d7a-cf39-345e-b66c-4bb22c1c45d0 | -17.57269 | -44.54374 | 2025-09-09 04:36:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ed6e8c8-f8bd-38f2-ae4e-9f040a112681 | -19.36451 | -47.46548 | 2025-09-09 04:36:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f1f93bd-8736-3a8f-bb8f-bd44625db658 | -16.08158 | -50.48607 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93280f9b-379e-36a6-b21e-d1c6929d3a0b | -16.69191 | -49.32978 | 2025-09-09 04:36:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46923472-abd5-3a03-bcc0-38eed39b9d7b | -16.06667 | -50.49457 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7f9b623-1854-38c7-8a9d-6f71ad2a521c | -15.16948 | -52.40381 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 854ba6e8-1917-3709-8b5a-a7fe762bbebd | -16.42953 | -49.29189 | 2025-09-09 04:36:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 175d8787-016d-377b-8ac6-7679053c8a4d | -20.91659 | -44.04582 | 2025-09-09 04:36:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5d5938e-3df3-325d-b806-712fd97c91ed | -18.66652 | -47.55079 | 2025-09-09 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a1c8e47-8f47-37aa-8ac4-545be721db68 | -16.28273 | -45.68483 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 43e4ba85-c4f7-31c1-a73e-b345e7d51c3d | -17.30342 | -46.71849 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bdde18d6-b4b5-31b0-b658-1d268f98d3c2 | -16.07005 | -50.47313 | 2025-09-09 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 485319d7-7270-38cf-b64d-ac9030c90a6f | -19.82984 | -50.94114 | 2025-09-09 04:36:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| be2d3137-cb6c-3656-b35d-e9abffcc0960 | -17.6709 | -52.26558 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6761188-7c30-3bca-a4c7-c7c3fe2752e4 | -16.32524 | -52.93012 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef0672c7-4a3e-305f-ac84-7b7fd6dd92d8 | -20.70951 | -46.61532 | 2025-09-09 04:36:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe2f6a6c-c419-3a76-8ce5-528143bc5ebf | -14.4477 | -53.24043 | 2025-09-09 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| decffc26-615c-3371-8085-0ed0b73920b1 | -15.83023 | -48.95988 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fa6a0de-d248-3aa3-af62-4a05c516fbe2 | -14.70489 | -60.25646 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82fb7c61-25ae-38e8-b5bd-8149601c0e8f | -14.35881 | -60.31446 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0b9849b-82ba-3de5-96d2-5902dcf81cbc | -17.57645 | -44.54828 | 2025-09-09 04:36:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a894466f-3357-3bb5-8527-cba4cfbc978b | -12.90374 | -62.08022 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3a229be-705a-34d0-a19f-ceb79c82787f | -16.30766 | -48.92591 | 2025-09-09 04:36:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 420702a9-9657-3c45-a35f-492f0f48d186 | -14.77127 | -47.78025 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 487ae5b4-2c77-3882-a241-04faf1628b57 | -15.8667 | -52.20402 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 31e81712-5f22-3605-9d75-755f4fd1c285 | -16.33013 | -52.9225 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 204c6dfb-4a40-346b-b403-3506b6700b3b | -18.77219 | -48.19472 | 2025-09-09 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abe19526-2b7a-367a-bac3-2f4797d1147c | -15.09574 | -48.0741 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcf5f842-77e3-3b24-b54e-ecb117ac75c5 | -15.31271 | -52.8542 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ca01f97-ac73-3ef0-87a8-1dd974b755d5 | -17.58583 | -49.79596 | 2025-09-09 04:36:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63425261-aea1-3cac-b5fd-91724bbb27ce | -13.11034 | -56.80141 | 2025-09-09 04:36:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7338f6f3-535e-3646-b578-d05048693605 | -14.53899 | -53.14868 | 2025-09-09 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bbf458e-0517-3e6d-8831-9ebbf49a51eb | -15.25239 | -48.80822 | 2025-09-09 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd8f0f22-098f-37ad-be81-0a2e1641181e | -19.92818 | -46.16928 | 2025-09-09 04:36:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d2d92672-d9b0-3aff-b2b9-636b9db674d7 | -17.15 | -44.44794 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8473944b-4cff-3867-8d73-1fba00deb367 | -17.73133 | -44.48193 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dea96166-b759-3871-b842-1d63cd6861d5 | -18.01245 | -45.63932 | 2025-09-09 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 351022d7-9afc-3041-b2eb-6a7fece2f10e | -18.79885 | -49.63389 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 91e262d8-4e0a-3de6-a761-87f95c93e053 | -16.32874 | -52.93065 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe4995e8-fe2b-3138-a6e8-3cf86909da02 | -15.09907 | -48.0513 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951a1041-7bae-3137-9791-eccd0c79b6f5 | -15.82666 | -52.25552 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 68e08d8a-9bfb-3baa-9fc1-1fe0634a6104 | -15.63821 | -48.09891 | 2025-09-09 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2565899-acdb-3993-bec4-49cb02e3456b | -15.26228 | -53.79272 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a75cbec0-6804-3e44-97c8-14e3d90baa04 | -15.53406 | -48.40122 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04c6df2e-6a64-390f-b94c-d00edac53d9e | -15.166 | -52.40327 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50256ec0-f428-38ae-8399-c5e5e895a725 | -12.87755 | -62.1092 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1561f15e-2550-3179-a686-40bcf4dc41f4 | -14.72256 | -60.24512 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d268700-d295-3e2c-a527-2000c762b113 | -14.70248 | -60.25762 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eef40382-cba0-3a30-9308-c82b14beab5a | -19.59064 | -49.46627 | 2025-09-09 04:36:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 323f6c8d-046a-389f-8498-aa34519d2945 | -15.31306 | -52.85312 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3915a337-fc0e-35f0-bcc9-b6413300d227 | -15.06257 | -50.12934 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f11cdcf0-5b79-3c72-bb2a-e9f316a5f1a5 | -15.75974 | -53.55296 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eed5f71-79b8-37e6-8f9d-a10cd44e3dce | -17.05795 | -48.56465 | 2025-09-09 04:36:00 | NOAA-21 | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67c59ef5-9c5f-3aa4-b483-96e7f43b0b5e | -20.07476 | -47.36378 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa0825d2-f2b3-3cb2-b4e2-bbc42426d352 | -15.26033 | -53.78891 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43b56fc7-672c-36d8-b5e7-896b3fce6b1a | -17.28803 | -46.69259 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71197038-586e-384e-98fa-d4bacaef7e0e | -17.4909 | -43.33684 | 2025-09-09 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 090f2501-9e31-33f1-acc9-9088a13b85c9 | -15.2551 | -53.79727 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 537a0704-bd2e-3ae4-978f-98bede9ac1c4 | -15.81996 | -52.27475 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba041c27-001a-3912-b233-969f1cc21a3d | -15.23471 | -53.76098 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9580597-3b97-3dab-b620-af0c8306675e | -20.07906 | -47.35981 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be1d0b86-6ffe-35e7-8c01-d853cd8f023f | -15.53177 | -48.39328 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d90e7b91-b659-3df4-a575-342cac01eb72 | -15.24849 | -48.81134 | 2025-09-09 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65c998b2-6e37-3c07-b237-503e4f6e3b12 | -13.96084 | -54.0118 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f43150b1-8b92-3f5c-a250-24cd125055ce | -15.26886 | -53.79861 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90e7b38b-6f41-3e78-bf22-a2c32e9f02fa | -15.06587 | -50.12989 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdffad15-2985-3097-8e2a-0abcd449b27f | -14.79561 | -48.18395 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9bdf28a5-097e-30ee-8a33-04e87a3e7fef | -16.33644 | -52.92778 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa1e9fdc-f14a-3de1-9c23-94b2b99a745a | -17.72705 | -44.48144 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37a4f966-9b39-32a9-8ab4-c2ddc2ae633b | -18.4744 | -49.55474 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa658eaa-c05b-3e0f-a601-418829e9b74f | -17.2731 | -46.74656 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ade6bbbf-0ccc-308e-9853-9ef6090e38fe | -18.8346 | -49.69313 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bd9101d8-578c-3311-9489-d6fe34b254e2 | -15.2554 | -53.81013 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f514e22-2299-3129-8997-f30f6d9f368f | -15.83078 | -48.95618 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e70e55a-691c-379a-ba46-5f3101466238 | -17.34927 | -43.58693 | 2025-09-09 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa0b3c49-52e4-321a-a807-52d0804f28c7 | -17.34474 | -43.58645 | 2025-09-09 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 062d8686-9531-3a73-8218-33c9c252f81d | -16.07441 | -50.48853 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f14ddfbb-ae3f-30ce-aeff-5ca9d1210be3 | -14.67888 | -48.1924 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96fe8582-b72e-3962-8cb9-f40b055c6d3f | -17.6749 | -52.26242 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80ae338f-4fc4-3558-ba5b-395b04560b2d | -12.88629 | -62.09953 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f108d9d-8a12-3237-9d72-4a48ad6aa2c9 | -15.82882 | -48.95269 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bd8de51-ebed-36b2-93d1-2927c3a85f62 | -15.78223 | -53.55239 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 604de3fa-a3e8-3c35-a6e1-f7f09959a379 | -17.28431 | -46.6921 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1ffb8c7-6284-356c-8143-5485e7457060 | -17.15474 | -44.44466 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 281a2c9b-ca1e-3edd-a7c4-0082fff47b22 | -16.07384 | -50.4921 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f90c5807-506e-362a-a363-8e6c72fea4dc | -17.71521 | -44.47182 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eefcf477-3107-3790-8efc-5578c3214247 | -15.27831 | -53.80981 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README51.md)
