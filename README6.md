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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b0ec47b-6730-3161-9eed-df111bc8ea40 | 4.16132 | -60.35662 | 2026-01-09 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c54aed4-5110-32b8-a299-d8e41dbd083f | 4.32003 | -59.86308 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69594c7f-619f-3874-ab04-eda548cb011c | 4.16279 | -60.35536 | 2026-01-09 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af34e07f-9d8e-3791-91b1-8052d2b601d6 | 3.17193 | -60.41325 | 2026-01-09 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e68a0f6e-09d5-3c79-ae10-c08354bd0e53 | 4.46629 | -60.73261 | 2026-01-09 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e09b9e92-53bf-3619-a9e2-9496f739a888 | -0.81163 | -51.91013 | 2026-01-09 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e2286e-d3f5-3662-a650-6884e3741bc3 | 4.32247 | -59.85216 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a216c270-24c3-3696-b037-8f4b6a78e0cd | 4.34642 | -60.39446 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74216622-9442-3532-ae52-c5ff58863922 | 4.00664 | -59.66054 | 2026-01-09 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95f7e965-ff88-3057-b743-b5ea3e4821d9 | 3.37743 | -60.24158 | 2026-01-09 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9a233b-3255-3100-8cb9-29bc74fec14f | 4.35879 | -60.39251 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ca817ce-0a38-359a-972e-6176401f03d8 | -3.49347 | -47.17171 | 2026-01-09 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d284962-b0ee-300e-a8e0-2612685c02de | 4.35056 | -60.39391 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ad29336-7e97-3c23-a35c-1df2411310b8 | 4.35116 | -60.39786 | 2026-01-09 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fdb433f-31f1-3916-aa46-16a35a666a3f | 4.46686 | -60.73648 | 2026-01-09 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b44b4a1-2999-3dcf-b538-1d92466a089a | 4.15874 | -60.35637 | 2026-01-09 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0925df-df88-38e3-b762-c068e54ad73c | -3.56451 | -54.86607 | 2026-01-09 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09184baa-7b04-31bf-ace3-cdd4315bbf34 | -3.79047 | -54.40819 | 2026-01-09 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ac852bb-c83e-320f-b3cd-70ec1305e1a7 | -3.5035 | -54.67627 | 2026-01-09 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4cf04bc-b05d-390a-b64e-de6a0b6ede75 | -13.48767 | -52.94588 | 2026-01-09 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 536b3801-37ab-3d7e-a3a1-499dac4b6b44 | -15.78028 | -59.74561 | 2026-01-09 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ffdc4c1-b393-3e84-83ce-f23041091fdb | -16.10547 | -56.7551 | 2026-01-09 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d86b42ff-4461-3538-8775-4fac6dde66e6 | -16.10967 | -56.75143 | 2026-01-09 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc405ed9-87c9-37ff-9e70-9ccb2be13444 | -12.40317 | -58.04138 | 2026-01-09 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9e96f3a-4a5c-3711-a2c4-87d5dfecd084 | -16.10608 | -56.75089 | 2026-01-09 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a764d18c-1a7e-3cdf-b7f5-f1f28d050e20 | -15.78418 | -59.74258 | 2026-01-09 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99745f90-bbae-34ef-bf77-25fe2883c2ba | -16.10248 | -56.75034 | 2026-01-09 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc5f5457-feb4-36a0-8d50-4ddad2b6f7aa | -15.78085 | -59.74202 | 2026-01-09 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2e1ad7f-6176-3f3f-bc1d-2c2c7234e7e8 | -12.40373 | -58.03779 | 2026-01-09 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68aa61ef-d094-3ab5-8027-37f4c7cee9cc | -15.78361 | -59.74617 | 2026-01-09 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b122f747-b1a5-3113-8f59-4367d3f6fd09 | -16.20823 | -59.32495 | 2026-01-09 05:18:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcc8f951-9f95-3f11-9b3d-feb421819c21 | -16.10188 | -56.75455 | 2026-01-09 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdd75e52-f9d9-39ab-b059-724207f0fc09 | -19.80095 | -57.37508 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a985face-694e-3317-959a-b99fe4e84c79 | -19.43545 | -54.77435 | 2026-01-09 05:20:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0ff287d-df81-3350-9c74-e9757df4e9e1 | -20.55967 | -57.94916 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7bb07963-bc15-3c69-986e-efeb0da9f58d | -17.65958 | -56.36192 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 31cf8162-c5d2-3b06-a93e-5c0cc16c3519 | -17.66021 | -56.35731 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9b9d8210-5a1a-3843-94a7-fbc2d238f9b9 | -19.29829 | -55.25943 | 2026-01-09 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0da94236-69bd-3ca6-8553-ba6759b44ec0 | -21.23266 | -56.24865 | 2026-01-09 05:20:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54d2610a-018b-3d19-9e98-ee80d90b5ecc | -19.13221 | -54.53639 | 2026-01-09 05:20:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d552ad79-adbb-3d10-a120-f0e53079036f | -20.55194 | -57.95228 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a8834b0d-463c-3bb2-ba2f-89e4b8f75c87 | -17.65212 | -56.36078 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f280b9b3-0b2c-31f0-96c2-2daa1b28d3c4 | -19.79972 | -57.38389 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4c869fc2-9028-3401-b372-1cba544ea48d | -19.30235 | -55.26002 | 2026-01-09 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9161d84b-49ca-3126-9d28-0e276149824c | -20.55551 | -57.95285 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0e631da9-23a0-327d-a03e-8d020ba8a352 | -21.23198 | -56.25395 | 2026-01-09 05:20:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ca7d3d0-8f48-3b25-9fa2-7cc41df36100 | -20.55135 | -57.95654 | 2026-01-09 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d5c80a58-eb36-3bb5-92e1-54b42b531496 | -21.22873 | -56.24811 | 2026-01-09 05:20:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f0cc512-c89f-3245-8165-47efad8b1524 | -16.26096 | -60.0361 | 2026-01-09 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4edd800d-9039-3ce6-9cc7-4682fefefcf6 | -19.17563 | -57.54119 | 2026-01-09 05:20:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3d98efde-ba61-31cf-be9a-627ffa19cb00 | -5.74321 | -35.38028 | 2026-01-09 05:29:00 | AQUA_M-M | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bc9b4fb1-3b09-3885-a9f8-805a20bd29f9 | -3.26323 | -42.53936 | 2026-01-09 05:29:00 | AQUA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| dee8a714-11e2-3415-b215-a6461699ef48 | -3.35465 | -39.12854 | 2026-01-09 05:29:00 | AQUA_M-M | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 9cf03a8e-90a4-3a49-a3af-dad6b2e3a1d0 | -6.88976 | -42.83487 | 2026-01-09 05:31:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9614db64-1294-3a09-bc60-fcd811f7d56d | -6.45894 | -39.77427 | 2026-01-09 05:31:00 | AQUA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 62abb03f-6a92-3565-ba32-b16c596153df | -10.9227 | -37.50606 | 2026-01-09 05:31:00 | AQUA_M-M | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ef5cbe1b-5507-39ad-8eb4-32c96c7d903f | -10.92137 | -37.51497 | 2026-01-09 05:31:00 | AQUA_M-M | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 7d3ec5f5-8e5f-3ffc-b6f5-2f1e2dcd4925 | -6.45721 | -39.78525 | 2026-01-09 05:31:00 | AQUA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| e89230d2-1022-306f-bcfc-a358d3b94a00 | 3.38234 | -60.24652 | 2026-01-09 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf4a8101-6e2a-3b71-9225-a43ecf9ff5df | 4.52521 | -60.20634 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cff8888-fe7c-3213-9b29-1456d02dc2c8 | 2.55193 | -60.5804 | 2026-01-09 05:33:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8db10266-adf7-3403-ae8a-a0684405893f | 3.3784 | -60.24348 | 2026-01-09 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c8ef61-e416-3bcb-b543-c45862cfd261 | 4.36031 | -60.39164 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac2cc924-bd37-3297-b963-bb299c53b815 | 4.3224 | -59.854 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d33a684-8d85-3214-935d-ef07c6da4b17 | 4.34481 | -60.39696 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 628f9cd6-59c7-3b0d-ac4c-e6f10aff7ee9 | 4.33478 | -59.84475 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d655e542-05f0-3389-a3c7-6b443033cf07 | 4.35085 | -60.39664 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b8e3f7b-0b0f-3286-852b-ccfc79978c47 | 4.52187 | -60.20687 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d003cb01-637f-3876-af8d-6d87cf998605 | 2.42575 | -61.15349 | 2026-01-09 05:33:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dc19027-7fca-39e7-b404-3a13b9392290 | 4.19869 | -60.5278 | 2026-01-09 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d071958c-1e33-3bca-8260-a516c455994c | 2.54857 | -60.58092 | 2026-01-09 05:33:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c3e7704-7f51-37f7-a546-828fb978a3d7 | 4.19813 | -60.5243 | 2026-01-09 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4d64020-c4cf-308f-9312-6c17ed6e9088 | 4.32356 | -59.86124 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55006738-d0d1-32dd-aa62-1799d7ae0ef9 | 4.64137 | -60.27535 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bae555d2-ad85-3497-ad1d-966b9054ae90 | 4.34752 | -60.3972 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bad9c532-1ae0-3ad9-b72c-eb64c2b10c15 | 4.35752 | -60.39559 | 2026-01-09 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05263095-02f0-34e5-bca6-b8a45e12fcdd | 4.27838 | -60.81514 | 2026-01-09 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbab15e2-9a3a-310f-a0a2-bd472ac0505a | 3.38456 | -60.23883 | 2026-01-09 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49e99736-f78c-303d-b895-e683c7979260 | 3.38177 | -60.24294 | 2026-01-09 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 015d39c1-1932-374b-9198-9a301d5530ee | 2.55249 | -60.58394 | 2026-01-09 05:33:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 010c20dc-f5f0-3e3c-b0f1-1b4f66f5c4ae | 4.16065 | -60.35373 | 2026-01-09 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d92ace73-f008-3850-b8d5-0c9f2830a556 | 4.27893 | -60.81858 | 2026-01-09 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5deb53ce-8c4f-3da3-b1f3-08d6d412bd13 | 4.00704 | -59.65898 | 2026-01-09 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1359d21c-a14d-3a83-8263-822cd675f0b7 | -13.63178 | -60.55008 | 2026-01-09 05:37:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0994b71-f611-3e46-ba51-ee01b2c7a752 | -6.9608 | -35.1392 | 2026-01-09 05:40:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 68c09c06-e651-3767-b4bd-a52c11fca893 | -17.65865 | -56.36505 | 2026-01-09 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2ec45345-2680-34b3-96f6-1155c70403d6 | -16.10448 | -56.75974 | 2026-01-09 05:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49c54676-7558-3f9a-9cf2-723ca5269571 | -15.78259 | -59.74553 | 2026-01-09 05:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a889fbd-dd2d-3784-b2af-54e5d6cc9a46 | -21.23266 | -56.25343 | 2026-01-09 05:40:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc58fa7e-a4f5-3473-aa4f-853cbbde42b1 | -21.22678 | -56.25304 | 2026-01-09 05:40:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed0bb7a0-eaa9-3763-b725-76c5f66462d5 | -17.65799 | -56.36086 | 2026-01-09 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b38e6e56-12b8-3025-8597-edfea2d318ce | -16.09528 | -59.11096 | 2026-01-09 05:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0923f69d-4dd9-31b8-a1d4-29a4ec5a0610 | -16.10526 | -56.75301 | 2026-01-09 05:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cbb9d7c-6bcc-3043-b1d1-0f63e2ab6e81 | -16.10565 | -56.74964 | 2026-01-09 05:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf2fbd79-d150-3bb7-9522-0af0c4f00f06 | -16.09992 | -56.7524 | 2026-01-09 05:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da210be6-09b8-3934-bbb2-76090eba45c7 | -17.65907 | -56.36122 | 2026-01-09 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| becde1e1-fd3b-3e85-ac03-7c50d5304156 | -19.57774 | -53.50879 | 2026-01-09 05:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edb67feb-2965-3f8c-96ca-473d13b395aa | -15.78413 | -59.74464 | 2026-01-09 05:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 524635ba-81a6-3942-8e12-0a68c73b0334 | -15.77925 | -59.74832 | 2026-01-09 05:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08195b8f-636f-3f0b-b39c-840825d06b5d | -16.10487 | -56.75639 | 2026-01-09 05:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
