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
| 0ab77a57-2c75-3c09-acb0-7e4c24346311 | -4.93444 | -45.66044 | 2026-09-25 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecbc03a0-1878-3e42-8b0d-3b1438f9d4cb | -13.77799 | -54.04507 | 2026-09-25 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdff3b84-1214-38fb-ba80-ad6ce7366813 | -11.4687 | -44.2111 | 2026-09-25 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a5e900a-3b3f-3a12-9d75-4cbc6da481f5 | -14.67663 | -48.75871 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f738640f-6b40-36c2-a728-a0f7af0207c2 | -12.18505 | -50.79097 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4805e3c5-ac9b-3be3-bc24-acbd2dc263cb | -14.78972 | -48.55564 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c80fad4f-d6a2-3feb-a1f9-f4863e4caa03 | -11.36832 | -43.3938 | 2026-09-25 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9041dafb-379f-3ae0-9be3-af098223c529 | -12.211 | -50.7448 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f52edb8-77a4-30db-8369-69ac70e8e336 | -10.90377 | -53.94318 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e6b18f0-4920-3b46-b8a0-b4ae6c1969ff | -13.69759 | -48.79869 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5079252-e72b-3f8c-8c3d-667f5886434e | -17.04568 | -50.87555 | 2026-09-25 04:27:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55fad1cd-ad26-3631-861f-8c88a6a379fa | -12.22331 | -50.75158 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f78beaaa-2675-3b99-97c4-25814d1779f6 | -10.61801 | -53.98935 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf8e10af-3ca6-3023-9dbd-45122932980f | -12.18351 | -50.79961 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e96ab270-7740-312a-8f0e-ddc53b219dd1 | -14.67579 | -48.7635 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d6aace2-8db9-3134-aa84-7916afd6b818 | -12.20268 | -50.76537 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4287351-c07d-37dd-a021-1593c1d7dc69 | -17.04613 | -50.87624 | 2026-09-25 04:27:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b34e00d-caf8-30e4-a1fc-47cb2bf4e1a6 | -12.20667 | -50.79282 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00595380-a14e-3981-af57-f808a1f8147d | -12.17475 | -50.79793 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 415bdccf-7de5-3bae-882b-b2149430e6ca | -12.18583 | -50.78666 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cdc6fba8-8c10-31cc-8e4a-c0c4e75ee93a | -12.18529 | -50.76429 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b71813d5-7c07-367d-b0f4-031674ac0e88 | -15.1837 | -56.05935 | 2026-09-25 04:27:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8da85fec-9b7f-3267-afd1-6cd7c4bf23e8 | -12.21816 | -50.75502 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d72c9c3c-0be0-3f4a-875e-8aa6b1c5212f | -12.1799 | -50.79445 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a177bc9-decc-31f5-8c7a-b91e9c10d6d6 | -12.18956 | -50.76289 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b148498-0311-3cda-9254-37c39d726f33 | -13.70055 | -48.80412 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bd0c4e3-75de-33ef-b062-9ca631408aa2 | -10.62536 | -54.00166 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f9b55fa-da55-320c-a17d-7b0209e9f904 | -12.20506 | -50.75252 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ac3ca023-849c-356b-8e0f-69f4b84ed323 | -11.37279 | -43.38719 | 2026-09-25 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a1b4027-771d-37a4-a084-e23584102d4b | -16.69605 | -50.66921 | 2026-09-25 04:27:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e6c744e-56ef-3912-b483-243aeee465ac | -16.05119 | -45.02407 | 2026-09-25 04:27:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 469090c7-bcf5-3003-b409-5b783f1032dd | -11.2777 | -45.37516 | 2026-09-25 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ac6bf02-23b5-3839-b1ad-84841b13f93a | -10.41847 | -53.78401 | 2026-09-25 04:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18912a60-ff8e-34e0-adaf-357bb9350f87 | -15.98342 | -42.99542 | 2026-09-25 04:27:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dad137c6-80e2-30fe-9e1e-fb6834f8473b | -12.20784 | -50.76191 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| e8b00ea5-1f88-350b-9621-52c16edce744 | -12.21221 | -50.76274 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1ed6f095-d8d3-3786-a6e6-2b538ad26b09 | -12.20547 | -50.77478 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e1b046b-4f23-38b3-bb26-f010790c1ac1 | -11.77166 | -50.90301 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deb1e737-9870-315c-8b43-70c344dacef6 | -14.72997 | -46.229 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ce7e502-6c12-388e-97b1-f341d0f2bddb | -13.78325 | -54.04626 | 2026-09-25 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56207d6a-f644-32f2-986f-f93078cc187f | -17.04972 | -50.8764 | 2026-09-25 04:27:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50deb00c-eae2-3ba1-9243-986c4e3cd731 | -12.21694 | -50.73709 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fe51bf0-52c1-3a71-9321-1e258618d5fd | -10.28744 | -49.95297 | 2026-09-25 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0dcb23f-0952-336c-9b54-f9206520af9c | -14.72383 | -46.22415 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a9ffeb0-ed73-3bb7-a3f2-1d460a2b84c9 | -12.20664 | -50.74398 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b894182d-5577-3886-9aff-2748b32bc9d7 | -12.20308 | -50.78768 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5e54a24-2c59-3359-9d4a-c2eaf6876152 | -12.19382 | -50.79265 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4c00dabb-dc42-3433-968e-fe4eaa7b43df | -12.22131 | -50.73792 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0189d0b-6ae7-368b-bcc8-f8eb5f6c9542 | -17.76307 | -46.6298 | 2026-09-25 04:27:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f4f9d40-5f5e-372f-8ef8-fad2d4eea4c9 | -12.17913 | -50.79877 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3f788f3-150a-39c0-91f1-df9e8bf30b4a | -12.19918 | -50.76249 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d06e7c9-11a9-3d67-96e1-add4f20ca390 | -15.68386 | -44.38519 | 2026-09-25 04:27:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86622dfd-9563-32a3-984b-9b98c1a08346 | -14.68411 | -48.7598 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 219190fd-51a3-3159-a99e-d3652fe953d2 | -12.20069 | -50.7517 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6adfcf7-9f7a-3a5a-982d-e2000051fb16 | -11.80282 | -51.01096 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23d8ec1d-16af-341e-abd8-38e77c6e9aaf | -12.19473 | -50.75942 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5699bb05-1496-31f1-8cdc-abf55c26752e | -12.213 | -50.75846 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0bd2460b-3e3e-330c-81c7-9e3fadc04e2b | -12.16958 | -50.80142 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1921ad0d-a199-398f-b450-a9a1f8c94d0a | -14.76368 | -48.47478 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 046453df-a826-36ac-8e0a-fcfe219a9d91 | -10.61659 | -53.99688 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8717180e-f22b-3b69-9c04-30afb6539da7 | -12.20388 | -50.78338 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a15ffb3e-e566-32f3-bb08-4a5bd23a2f71 | -12.95382 | -44.83132 | 2026-09-25 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fad020ec-7c2c-39a9-8fc2-17d13ce6adf8 | -13.72189 | -48.79348 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3857fb15-fb1e-319d-9270-6a0c1eee9433 | -12.18375 | -50.77288 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20d77a87-bd6e-381d-8fd6-fb033dcc4e5d | -10.89753 | -53.94584 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad31dc70-5019-3837-b961-fffa87b6aa97 | -13.22179 | -51.55742 | 2026-09-25 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af4fe0f0-afed-3f4f-8f15-a45b1fce0707 | -12.20306 | -50.73888 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6830fe27-f8d1-3e5c-bc18-4c52faf69563 | -11.28648 | -51.29281 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f28d09ee-5a6b-3f8c-b0c8-42aa2547305b | -13.19718 | -48.31795 | 2026-09-25 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 266d4bac-abbb-3efe-bd39-5d90f18bb9b5 | -10.28674 | -49.95704 | 2026-09-25 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d77e2de-a89a-3302-86ed-ddbc9e9396a7 | -12.53874 | -50.06871 | 2026-09-25 04:27:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cc288b1-9941-3bea-9559-e641c1339ee4 | -13.70435 | -48.80468 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d187524b-7f07-30fd-a4ba-d959705227ac | -11.27644 | -45.37528 | 2026-09-25 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b60fafa3-13ef-37be-9441-3e05b0e82de0 | -12.21063 | -50.77133 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cca030a3-4104-3f56-81dc-0cb853cbef61 | -12.18429 | -50.79529 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 858e5df6-51de-3d2c-9fdc-1b5fefd80a09 | -12.20028 | -50.72951 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8971f5d4-ba3e-3db4-84cf-5d55e5bc06c6 | -11.15819 | -50.65727 | 2026-09-25 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b66a65c2-801b-34be-965e-96932d61b7f0 | -15.16345 | -43.57035 | 2026-09-25 04:27:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0081fda0-737b-3117-8757-d4e52fe9fb9c | -12.20148 | -50.74743 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b682ac5-e92a-3e23-b7e8-fd626897a000 | -14.58951 | -45.60473 | 2026-09-25 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e97f8e0d-4d38-38e8-b893-f732fe33ec2e | -12.2241 | -50.74729 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c30d3970-b0b8-3c6f-9813-4751375d8b14 | -12.21737 | -50.7593 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 782bcfb0-10f6-3184-84b0-417396fef919 | -11.28383 | -51.30728 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf25baaf-e969-395a-8ceb-68b713523636 | -13.22093 | -51.56208 | 2026-09-25 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95d875c3-89f3-36b9-8ace-6786148d0dc2 | -12.19432 | -50.78602 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5ba0cef8-c3bd-3d2c-8fc9-889a638f2019 | -12.19043 | -50.76082 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd4b316f-a64c-3ab1-b54d-0d2a5d73de23 | -15.82101 | -53.11312 | 2026-09-25 04:27:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1681eeb1-c867-3023-863a-a5258a336c3c | -14.76259 | -48.47311 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee3fa283-c81b-3161-9e0e-c5c9ed7f559c | -12.18168 | -50.75916 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de26a63e-b601-3196-a95c-522938871b8a | -12.21537 | -50.74563 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1008406f-ab47-3349-b2ea-5c88b6d90d5c | -12.20188 | -50.76966 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| baaf10d5-7fa2-3296-8697-6c43db37fbd1 | -12.17397 | -50.80225 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fead29bc-cc8a-387d-8357-6aa0bcd9c633 | -12.17885 | -50.74973 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba336337-cec6-33b7-bdae-01dcda8e0e8b | -12.20743 | -50.73971 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 668a5568-2253-3bf9-8c40-4d50bfcd63cb | -10.62125 | -53.99309 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d001da5-489f-39eb-b7d0-2fb8be0b5ae7 | -14.66914 | -48.75758 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 045f7dab-5ba1-31b2-bb0b-5edafc18b696 | -12.18091 | -50.76345 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 992e7e5a-d997-3653-9d98-397482c1a2d1 | -12.20229 | -50.79198 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 87a80050-1001-376a-8275-8a9ade9e600c | -11.15457 | -50.65203 | 2026-09-25 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| baaff5ab-705e-35f3-bc60-05adc3d0445f | -11.28844 | -51.30814 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README18.md)
