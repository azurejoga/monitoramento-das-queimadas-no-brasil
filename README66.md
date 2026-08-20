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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f7478c1-92ec-30c9-b09a-f0d0bd2d2809 | -15.36544 | -52.7723 | 2026-08-20 05:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af49bc0b-ab0c-3933-901d-61ae05292671 | -13.441 | -57.07629 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77d53ed1-41a0-337b-b845-0da4939d6ad9 | -15.21997 | -52.80836 | 2026-08-20 05:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf97ac76-d753-349f-b962-d562e46ef30f | -14.34482 | -51.90275 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba86ef43-1307-3271-88cb-fd81e9fc1af5 | -13.43767 | -57.06647 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3731dbd3-be68-3891-84f7-ee599028fd3d | -15.85581 | -56.08857 | 2026-08-20 05:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b7f90921-c578-31cc-8d4c-5337fce7d102 | -14.1524 | -53.0461 | 2026-08-20 05:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49cdfaf9-31a5-3b50-becb-c7642d4e9f8e | -16.49876 | -55.18334 | 2026-08-20 05:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0bc56087-70d9-3203-91fe-172bf1487e80 | -15.2195 | -52.81272 | 2026-08-20 05:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06c9c41c-a636-3858-836d-f26d4e8c77b9 | -13.43707 | -57.07109 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fc6a6ce-c116-305f-83db-45c20960b0cc | -14.01474 | -53.67506 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e777265e-9fea-36b2-9c9b-578923762b14 | -14.01518 | -53.67135 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34ef43ef-34e1-33c8-addb-b657a6efdea6 | -17.3372 | -43.6139 | 2026-08-20 05:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 35b1ff67-c95c-398d-9050-8d27d2913c8e | -17.3365 | -43.6383 | 2026-08-20 05:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 98302e3f-d3df-366c-bcd1-943f491fbbaa | -8.6729 | -54.629 | 2026-08-20 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a465581c-f801-39c1-9bd1-630c5c5ad814 | -8.6727 | -54.6492 | 2026-08-20 05:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a0147630-54bb-3723-b68a-a0bceb53f8c7 | -6.7575 | -59.46781 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2138b365-1c8e-30ee-a75a-6a9ef994458a | -6.92026 | -59.34585 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a464620b-eb64-32c0-89b9-8abbb9092a9e | -6.70812 | -59.09669 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04779fd0-6958-3c64-aba4-c29086d6837c | -6.85773 | -59.02783 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 960727fe-7091-350a-b9a5-29e0f064063f | -6.58368 | -58.98116 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4360607-6a8a-372b-8c78-f0117f658235 | -6.84302 | -59.01904 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9f1ad6b-1eaa-3371-ba35-8bb2a32b22d8 | -6.71972 | -59.09433 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e12d4ed-d5ff-3f3b-b54a-3a565c2f7f68 | -6.59684 | -58.96799 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72ca81a2-d5f9-34d2-bdfe-126772dbbc6c | -7.10478 | -59.77322 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efc11716-3bc5-3c91-95e4-eca65204fca3 | -6.70712 | -59.10386 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6636687-5da9-3d3e-afda-7a74f40e816c | -6.84059 | -58.996 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dd2295a-99e0-330a-b11c-015a5706a855 | -6.70363 | -59.0886 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01da2f68-a208-36d6-8d75-63b12587eb75 | -6.96183 | -59.05362 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb99ea32-467d-3586-8ed5-eed1e8f701c4 | -6.86936 | -59.02565 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bab778eb-bfce-356e-8858-5622ce138aa2 | -5.8037 | -55.72245 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4eebbbb-b1a7-31f0-aea1-a4ae9e05691d | -6.91976 | -59.34938 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 624c11d4-d401-3e70-a8e0-a7cca16a66f4 | -7.42249 | -60.02971 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 01c001c2-8e97-3832-8b7c-6909aff0b14a | -5.49323 | -60.13646 | 2026-08-20 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64ae3663-8930-30aa-bee0-0d467715988c | -7.05293 | -59.84077 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85f28524-3cb8-3231-98af-d04d39a66f1c | -6.84908 | -59.01624 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 622e47f5-e24c-3f75-a668-13b1f1c6b86c | -6.8628 | -59.0322 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c414bf6-25fe-31af-8e1c-bae28f174fbf | -6.58418 | -58.97753 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a498feeb-015a-3988-a4d1-1f1246106f84 | -6.08499 | -57.91607 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a916012d-df98-3e21-8d47-c74b4ae9f7e3 | -6.69513 | -58.94604 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59781a5b-9e5b-3be3-b954-8bcc8c04339b | -6.69605 | -59.10251 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f448acb-44c4-3922-960b-2d8bdcca979d | -6.59634 | -58.97159 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 191d1646-6ac4-3bc7-8f53-1b00ab179f7d | -6.9772 | -59.58286 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3da04f1b-d879-32ec-9b4e-2ed220e95167 | -7.43393 | -59.79072 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93c41ee-6db4-3340-9f6b-7a2361da6120 | -6.91382 | -59.3521 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ad9e405c-5540-3553-96e9-6dd17ea20421 | -7.05247 | -59.84404 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b90bf1f-13db-37c5-880d-b256e31225ec | -4.38737 | -55.47742 | 2026-08-20 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb0c15d9-b975-3be6-a4b3-f3658e0e310c | -7.05696 | -59.8472 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38585511-c69a-3f98-8152-307cd3f79613 | -6.37682 | -54.94096 | 2026-08-20 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87bd1660-a475-3368-a4fe-44aa48d5a552 | -3.89987 | -55.8823 | 2026-08-20 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36938d1d-e061-3fa9-b58a-e0469843a321 | -6.59734 | -58.96439 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4574a93c-fe4b-3517-abe0-7a93dee1c9c2 | -6.85363 | -59.02417 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08b629ff-8a6b-342e-81c5-2fc1e5b73d37 | -4.78861 | -62.92403 | 2026-08-20 05:59:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a9ada9a-aa64-374f-9cde-4b4dbeebf0b4 | -6.69564 | -58.94239 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c0d2c18-0fea-3190-a205-d05e8babf849 | -3.09913 | -61.21272 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8efd569-67f4-3fec-bb24-a0303da07951 | -6.8632 | -59.03661 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd9bce2a-805e-382f-aede-9f45e55c8f21 | -3.10889 | -61.20945 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beec0185-5fce-3bda-8733-10c7c621016c | -6.85869 | -59.0285 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f154f667-3126-31c3-8381-a2d7199e8cf7 | -6.92712 | -59.34742 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b15bf5c1-d352-32e5-8e35-bdfb3506b3e5 | -3.10436 | -61.20881 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 950c5317-28d9-3295-aca2-c9c6b06bfa01 | -6.13313 | -57.87395 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16e0fbe1-b797-3a6d-a7fa-059c7fc15e55 | -6.85823 | -59.02413 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7abd2d5-4a30-3f91-8850-f27d3abad6cb | -5.80073 | -55.71043 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c29c4936-b792-3120-b8cf-71bb487f03ab | -6.84757 | -59.01911 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21e4afdd-b79b-3a89-ab51-c5b8514b0e02 | -6.75033 | -59.15862 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73bae66-5e17-371f-953a-186f2861ed0a | -6.85723 | -59.03152 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95c44353-ef14-3cb7-b3c8-a4b18408aa1f | -5.79777 | -55.71562 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b5ffd27-2551-35f1-91be-cf613deea59b | -3.09984 | -61.20817 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d958785-4668-3bb2-a707-c50138d945d3 | -6.14082 | -57.86232 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4840bca-6e96-3874-97ee-9a9fb5aa98c2 | -6.91528 | -59.35293 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 102cb055-9be7-3f8e-aad3-8fa1f1e57dce | -5.80288 | -55.72829 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a968344-3915-3593-89a0-c43813ada65a | -6.58468 | -58.97389 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 239cb4f3-117c-34f6-9d06-e65eb2fed10b | -6.76787 | -59.15344 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cd6211f-42b2-331b-9ba3-2bfce463c294 | -5.79694 | -55.72157 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99bb6abe-d003-3c4a-892f-f87f7ff51781 | -5.48903 | -60.12987 | 2026-08-20 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e800920e-1078-3017-a99c-a0dec8ee149c | -6.69554 | -59.10618 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9fe4ae4-7079-3d87-bc2b-d34fc5d1f509 | -6.76235 | -59.1528 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c21737aa-0568-3c25-be34-d055f28133fe | -6.79355 | -59.5831 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd9f87de-7fdc-3118-8aca-5cffbf32cda5 | -6.58924 | -58.98186 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b173d313-f51f-3a94-96b6-3524f9e0627a | -6.85314 | -59.0198 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f15c300-e933-31ad-aa52-4afb9ff547b5 | -6.69667 | -58.93487 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fffb7af5-5261-313c-92e9-53e2cfbd03cf | -5.79838 | -55.72823 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e535a715-3bc6-35ad-9a7c-71f6585cb751 | -6.59076 | -58.97092 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de3e2e4f-724d-3666-a083-65de7987ea50 | -5.49281 | -60.13939 | 2026-08-20 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d718afbe-4263-36d0-9c64-4baf4e07fe63 | -6.95627 | -59.05285 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae98bf1-0a05-3a50-a6dc-2d0ebe2d305f | -7.0059 | -59.59374 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0b90526-c7a0-31b9-9842-93fffc3d8c86 | -4.7875 | -62.91951 | 2026-08-20 05:59:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5ff278c-e9ff-3f81-8ed8-d9cd63086f84 | -4.38815 | -55.47181 | 2026-08-20 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 877f18e4-f7c1-3408-a94c-b230e54c0731 | -5.79916 | -55.72236 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56e0418d-7e57-38a0-95bd-63c75437c292 | -6.7192 | -59.09798 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d486c2c-ffe2-3180-b9cf-c69bc2896615 | -6.86426 | -59.02919 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bbeacb3-610c-3f2e-9a01-1d2827098101 | -5.79859 | -55.70968 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f91e715-0900-30f1-a9b5-e09f5935b7bf | -6.85415 | -59.02049 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c762b1-b792-3ca8-9609-dc76d432112e | -6.9611 | -59.05385 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a929010-07f7-3c00-9a72-cef9b2d86592 | -6.79935 | -59.58052 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8df1a905-a898-3974-90e1-f17da5d859dd | -3.10147 | -61.2061 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c62b88ad-7772-3345-ba19-75b0e1d0c464 | -7.09948 | -59.77241 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3efe824a-9e73-3c11-acc2-24a2f153d9fa | -6.79047 | -59.58251 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2ca12a0-6a77-34b0-89e7-2e3d094fb3ee | -6.74885 | -59.16946 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15522cdc-dd50-3320-ab82-1313e8debf12 | -6.14023 | -57.86648 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README67.md)
