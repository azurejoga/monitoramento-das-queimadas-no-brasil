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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b01022cb-48e9-3c08-9d5a-59e261cc16c2 | -9.38632 | -68.32981 | 2026-10-06 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e4364c7-5d2d-3969-ab33-ac312428bf50 | -3.68829 | -59.63989 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bbfa072-70f3-3eb9-9ee2-b8496f3bb8f6 | -9.10622 | -67.75088 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97bcf414-f7ac-35bd-bc40-d395ae05a943 | -5.95766 | -55.34787 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da955510-7f23-3c94-b9dd-e41c66f2c4af | -3.71 | -58.92985 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2979831e-4786-3314-af7d-a5ec0e4e090f | -4.45737 | -54.96663 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d89dc38-dd9c-33aa-9002-53e8880e5ef9 | -9.13174 | -67.75977 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 695df631-cc93-381a-9840-c8852d310083 | -9.13464 | -67.76913 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc412f14-61e3-3cfd-9b3d-791a0138da1e | -9.16052 | -68.24555 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02191e8b-df47-3ca0-8748-9ff13f7a20dd | -9.46771 | -67.07166 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9321a11b-e53d-3744-a779-80d05f05af6d | -9.54327 | -64.81493 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29286c46-e044-3e87-b6f1-e72be54b5b0a | -9.23488 | -67.86977 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c49bd006-e90d-31fc-bf93-9bc2be45c792 | -4.46512 | -54.96404 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de3ddaba-1d60-3181-b79a-424372d9606e | -10.61493 | -68.67693 | 2026-10-06 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c98fb77-4a5a-3d44-a853-cddd111c3f8b | -9.5975 | -61.82423 | 2026-10-06 05:25:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d7e47cc-8da9-3855-a722-6ae1ccd2bf46 | -4.35599 | -54.86483 | 2026-10-06 05:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5da71e6-204f-393c-aa15-06847fd9809b | -9.34792 | -68.92314 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1c3e7de-875f-3f8b-b6fe-f9c0b588a9e0 | -8.93754 | -67.34429 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43c355cc-f19b-34f1-9511-a0991d9a2fcf | -9.73389 | -65.09196 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| f4e52736-0ba3-3dba-a978-abe40953529b | -3.70666 | -58.92933 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae1e0768-dbfb-3f2a-8da4-ff8bde0f98d3 | -3.97077 | -59.35426 | 2026-10-06 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45e08a66-dfd8-3077-aca5-eca5fa9cfb27 | -8.92052 | -66.8418 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e0cce3c-d89f-3b82-bbf0-4f0a30735645 | -5.67883 | -53.49766 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10bb0911-a727-3a17-8076-16d0cc3ee644 | -9.75815 | -65.0825 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdfbfa5b-6a0d-3c77-8d73-342f7bf216ba | -9.12468 | -68.21088 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1121bf7-84ac-3e51-a84e-da29d468b174 | -8.88369 | -66.76907 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf07e885-63a0-3a08-96d4-b13066c096c1 | -10.49 | -67.84615 | 2026-10-06 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8471855b-a7f8-31d4-92bf-520939d0ba03 | -9.48548 | -63.95215 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58551bd9-155f-37cc-a80e-41697561897a | -3.70611 | -58.93287 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d06ca5b-c0b8-33ef-840e-edac06a719b4 | -5.68412 | -53.49368 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cf77551-2eaa-3619-aa41-90872ded5ecc | -5.82413 | -53.86258 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fedc2013-e075-37e8-b842-2681a4cf7dae | -13.50286 | -61.13555 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a82cc6e-bad2-3a26-bebc-c87851e1b578 | -9.94915 | -62.27163 | 2026-10-06 05:25:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01295933-846f-3a60-a03e-962616c63e67 | -8.62526 | -69.49848 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d06640ac-1dc5-3a23-bb1c-1335bb5a3605 | -9.14609 | -65.54826 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d59ab07d-24ef-32f9-9ff4-6694a70376b6 | -10.28738 | -67.24139 | 2026-10-06 05:25:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05580aa9-c447-3acc-8580-a16c4975471a | -5.96477 | -55.35646 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3297965d-af7e-3a6d-965b-f7f79fe39aec | -3.74978 | -59.28769 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7acfff03-7a0e-3311-8e19-0adf96a65d9d | -6.69515 | -55.20693 | 2026-10-06 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbeeed48-eeec-3680-840e-619af5c5a8b3 | -8.62923 | -69.50507 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa519e79-00cb-3cdf-8ca3-09ab9db2d7a4 | -9.11446 | -67.7038 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fe1cee32-0d24-3968-892c-6869b15a6769 | -8.87343 | -68.53683 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25d7edb7-a3b5-3665-869a-f1ed2fb77025 | -4.46457 | -54.96783 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5767aedd-7d21-3b7a-999d-2c4d31b30531 | -7.89166 | -72.35155 | 2026-10-06 05:25:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 50ab4854-0c8f-3064-a4f6-fb7feb047930 | -8.62426 | -69.50419 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb20bc08-b17c-32a4-b6dd-1db1dad0a6af | -9.23034 | -67.89607 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c54f3227-53cc-3b14-9415-5ad6c172185f | -9.16155 | -67.84972 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6509ea22-4869-3c46-84ad-6cccf13ae1cd | -3.7403 | -59.41432 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f37c88b4-c74e-373d-98f0-4301976b7554 | -3.67706 | -60.53917 | 2026-10-06 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40e84550-cb00-3bcc-9829-2ea28a0a7fed | -10.24663 | -68.29932 | 2026-10-06 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4a9a857-40a7-3e17-a947-4ca5177041d0 | -9.48351 | -69.01834 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beaeb00b-25a5-3cb0-b075-ad0e74c75e81 | -10.95737 | -60.90957 | 2026-10-06 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04ee9613-c63a-3558-8f38-02526c1a83a4 | -6.37146 | -55.15335 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3dbe35b-af3e-3f79-aaba-662b95bcd29b | -12.09272 | -60.84171 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8377ba6c-190a-347e-bb89-929955cfda06 | -9.10723 | -67.69375 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 387324f1-1f77-3052-b04b-7031e4409025 | -9.16133 | -68.24094 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f9fe4b5-e522-39c7-86ab-940598ee45a3 | -8.60563 | -72.72938 | 2026-10-06 05:25:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| daa08d8a-024e-3b3f-b9fd-826af225631e | -8.77948 | -69.53358 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9593688-406d-3f95-95b1-103240d0a851 | -3.68052 | -59.62457 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dffdc803-c9b2-39c2-88f2-633debb1839c | -12.13354 | -63.15351 | 2026-10-06 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 985f66a5-cd95-3662-8f47-78c2d12821b5 | -4.42131 | -55.75599 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18b739f6-0489-319e-ba9b-dc90345769af | -9.13001 | -68.20706 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2555e0b3-335b-36b7-8d23-583fdcbc4f2b | -8.63024 | -69.49934 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ec8eb5f-a4fa-332b-abb6-ea1807fb88b4 | -9.11484 | -68.31936 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a768760d-cb52-3bbc-9b9e-5f1f0311ca2c | -8.7745 | -69.53276 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93009603-847f-33a4-ad9a-cb23c8907679 | -9.49116 | -63.96111 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d1f262-64c6-393a-b285-f2fb948e17e9 | -9.33332 | -65.4524 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7336cb3-9a38-3498-8e6d-d92d38e45d18 | -9.23083 | -65.69151 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6289866-47e5-314c-959c-cab290124aee | -9.71797 | -65.10009 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0034d4c2-dfb0-391d-a004-d17b4ab5098a | -9.68135 | -67.06952 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4314d329-5dce-361f-94f6-76eca26ce373 | -9.1568 | -68.24016 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3f4f580-475c-3a48-9c4f-7371daea12e8 | -9.48481 | -69.01655 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7354bfe0-ddf2-3451-86be-5a0e39b254f9 | -5.68482 | -53.48874 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 164f78ab-50cb-37a6-a009-a6240dfd932e | -9.5942 | -61.8237 | 2026-10-06 05:25:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d51a088-5da8-3684-aed6-9bf3d4112062 | -9.45928 | -64.32825 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0780e37d-a61c-3857-aaf4-7669c12ded8b | -5.67422 | -53.49685 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d3b68f8-9384-3fce-a85e-7b88aacdcca8 | -6.00402 | -53.51735 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee0ba9cf-bee5-3107-bc24-832f86274a62 | -9.11666 | -65.91002 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 160a593c-4c21-3b35-ba82-1a5bcf869561 | -6.37059 | -55.1494 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce6461d4-d87b-3c66-b151-acfeaf58283e | -9.10746 | -65.3613 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 171c206c-64d4-3c89-9e16-4612e95d1c20 | -8.92813 | -66.84698 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dc144c80-417f-31de-9c74-957dcc72f386 | -9.47146 | -64.34277 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bddbec70-d282-335b-aa17-560baa0ecbc7 | -8.99998 | -65.72144 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 203a6d75-f469-3fad-b203-611e9823f414 | -10.44572 | -67.89459 | 2026-10-06 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc51147-a89c-354a-bb16-45e07691ba32 | -9.39672 | -68.26968 | 2026-10-06 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83f8fc85-eb8b-3e50-8f6d-babd303f71df | -4.45118 | -54.97338 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bbbcbb9-d81a-3fba-8fc3-edbb44425050 | -9.48787 | -63.9494 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4594481-3eb2-3db6-adb7-41e7c3e9e49a | -12.61379 | -60.90058 | 2026-10-06 05:25:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5534ceab-04f2-3416-9094-6f84760d30cf | -9.60356 | -61.82876 | 2026-10-06 05:25:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa859f53-5457-350d-80bf-91730384ecc5 | -10.14443 | -68.39522 | 2026-10-06 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 898d4d02-78dd-3ac3-93d1-1470338360f4 | -4.4635 | -54.97524 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b466f9c3-69a6-3ba4-afe0-554479c2b9e0 | -6.45937 | -55.47486 | 2026-10-06 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0fc8e53-cc02-3255-954e-8f14aeea9d0b | -12.16222 | -60.74521 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b162296-d346-3f7e-8f0a-6d0cefd2a700 | -8.85799 | -66.79559 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cf078ad-c370-35e0-93d5-c6e0cc4a64ca | -9.59384 | -66.14154 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e04f7287-ef64-3241-be8d-1a487d4e075d | -9.29391 | -65.64333 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a13ca736-109a-3664-8f88-afc83411208b | -9.04904 | -65.43233 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ca8c3b1-709a-325e-84a8-497f30e495f4 | -9.62237 | -65.7438 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7527b01a-f421-3a68-9b20-b864d1d9e9ec | -6.69572 | -55.20311 | 2026-10-06 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 709338f1-18e4-3236-98a3-43481db057a0 | -8.62476 | -69.50134 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README66.md)
