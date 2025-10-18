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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c759db74-ed33-3f0c-8d86-93e8da648d5e | -3.6639 | -42.5799 | 2025-10-18 13:30:00 | GOES-19 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 47f86b50-92cb-35a5-b0c7-369ef57fc9ed | -13.2005 | -46.4084 | 2025-10-18 13:30:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 53f52129-0c08-383c-8934-e9923ec506ea | -11.9713 | -45.3373 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ac9a3afd-02f1-369f-b18f-f4b0cd255160 | -11.6104 | -44.0913 | 2025-10-18 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 423.4 |
| c8bc2392-952a-33b9-95e7-bba18ecd35e4 | 1.7665 | -55.9411 | 2025-10-18 13:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 451edeae-4a9b-3045-8f5e-fcc00c8d985c | -14.09 | -43.6475 | 2025-10-18 13:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3e9f7b66-20a0-34e4-8c65-0f6cbb6bf3fd | -11.4001 | -44.076 | 2025-10-18 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| a5db44a6-5a29-3b17-9a45-4e6203b36d2f | -3.7438 | -41.7456 | 2025-10-18 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 5c84e57b-a0d6-3a3f-b169-c64bfc5fab02 | -15.7923 | -43.643 | 2025-10-18 13:30:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 136.2 |
| bbd50528-b096-35a9-a0aa-931f7add01b1 | -11.8544 | -45.4464 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| da36907d-5cf7-338a-a42a-e034924efdec | 1.7664 | -55.9608 | 2025-10-18 13:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b49fedac-8b63-3c1b-a10d-8641269e2e25 | -12.1673 | -45.1003 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| b45f68da-0808-3ffb-8723-50a3512405a2 | 3.1652 | -60.3465 | 2025-10-18 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8bc40319-d053-3bd6-b7e3-ff40d7b28405 | -12.487 | -45.4664 | 2025-10-18 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| b361f4fa-261e-3631-8a7a-39554a2d91c6 | -12.5059 | -45.4866 | 2025-10-18 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 51aa7a65-3cd9-35af-980c-e4cc91835994 | -13.9438 | -42.35 | 2025-10-18 13:30:00 | GOES-19 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 4feb647e-3741-3e71-8b99-cbf83085d84e | -11.5724 | -44.0736 | 2025-10-18 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| a1eaaf8f-bbc5-3b0b-a583-e83ecf6d8649 | -11.9521 | -45.3401 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 76decd01-80ce-306e-81ed-ea707bbfeca7 | -12.9519 | -47.3499 | 2025-10-18 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a1866b5d-2a7d-37e0-8315-1d5a84795144 | -11.5917 | -44.0707 | 2025-10-18 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 426.1 |
| d4f0362c-9cbe-33b0-acf3-7b7ca6cd03d6 | -13.2644 | -47.1007 | 2025-10-18 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 6591bf35-640e-3a2f-b795-4b8f33272e6f | -3.0632 | -43.2161 | 2025-10-18 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| b682e748-2a51-3200-b40b-90cf883e8130 | -12.9716 | -47.3245 | 2025-10-18 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9ece45d3-c824-3d9f-9591-08eb18592299 | -12.4678 | -45.4694 | 2025-10-18 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 47af3713-2c34-37b3-9f2c-f1c9b94b65ae | -12.1485 | -45.08 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f9ae25f8-7bdd-3237-899c-fedfbc4bb96f | -10.8293 | -43.9248 | 2025-10-18 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| a0e4b06b-b2db-32a9-9546-4f9da22c666c | -13.0303 | -47.2709 | 2025-10-18 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 8716301d-0621-3849-80b8-115937bdb677 | -11.9709 | -45.3603 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 2ff6b050-24e0-38ef-9f0f-1cb8c7ab6569 | -10.8101 | -43.9275 | 2025-10-18 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| eab7318e-20df-3e9f-83c4-87191561f3f0 | -12.1678 | -45.0771 | 2025-10-18 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 68473c40-69f5-371b-b82e-42973770835f | -10.8293 | -43.9248 | 2025-10-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| bece326c-aa3c-3ffa-880d-d1d954d722f8 | -13.0303 | -47.2709 | 2025-10-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8366b5a1-f4dd-3557-988d-57874d081add | -11.5724 | -44.0736 | 2025-10-18 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 9272f25a-01a1-3be2-a124-cca4fdf041d5 | -10.5132 | -43.4289 | 2025-10-18 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 47ab19af-1be0-3c18-a5cd-ad037322a69d | -10.8101 | -43.9275 | 2025-10-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6cfaeac7-7e87-31e5-96bc-3e9ee3109c1f | -16.4783 | -43.057 | 2025-10-18 13:40:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 561f55ac-a811-3c80-a75b-8066e09423c5 | -10.2939 | -44.0221 | 2025-10-18 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 213.9 |
| cfc01bb5-9bcf-39b7-a804-1b91072f00e2 | -10.475 | -43.4342 | 2025-10-18 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| fa40b0e7-34c6-339c-924e-87debd094849 | -12.1481 | -45.1032 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 874551a4-d4cc-3ab9-b9c9-18cc7b8042e3 | -10.4941 | -43.4315 | 2025-10-18 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 303.3 |
| 03d0c33b-521a-3bb6-97d5-3216bb2d7d47 | -10.2363 | -44.0532 | 2025-10-18 13:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ed602764-cdc0-3bae-a232-e58cc54e33fa | -11.9516 | -45.3632 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c3b6fba7-5b42-33d6-aebc-6b0a63d0bc82 | -15.7923 | -43.643 | 2025-10-18 13:40:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 138.9 |
| ec56c48d-9a0e-30be-9026-84fe2dec5336 | -10.7044 | -44.548 | 2025-10-18 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d320c45f-5f3e-378c-9da6-b1587654975c | -12.9712 | -47.347 | 2025-10-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8de3f3d5-73ef-3970-b093-a471fb558840 | -3.7626 | -41.7207 | 2025-10-18 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| c9fcef1c-e6bf-3f4b-9011-7ea5fb163c3c | -13.6368 | -43.9446 | 2025-10-18 13:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 809e5326-dcb1-3b21-aa60-58ddea1186ac | -10.6853 | -44.5506 | 2025-10-18 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f36d0a41-a24d-31a1-829f-8bd5ae2d6a50 | -13.2001 | -46.4312 | 2025-10-18 13:40:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 61232421-96fe-34f3-a9e7-b56e3a42c054 | -11.5912 | -44.0942 | 2025-10-18 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c2c9fca5-8c26-3688-a167-c987a4c78ca0 | -11.3588 | -44.2458 | 2025-10-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| ce9e9fe3-3226-3b77-8116-51948768a4ed | -12.1673 | -45.1003 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 78a3dede-71e0-3de8-8c74-ba66cdb45ed7 | -10.4754 | -43.4106 | 2025-10-18 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6ea734e6-837d-39dd-a675-c30ee6673ea1 | -13.2451 | -47.1036 | 2025-10-18 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 750e983e-0da3-3afc-a702-fa5aa1cbdbc4 | -11.3963 | -44.2869 | 2025-10-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 3b7c0289-4cc3-3b25-8a13-a14bcc59fa1f | -12.9716 | -47.3245 | 2025-10-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ab40c496-dc91-3ba1-b4e9-b7084dd6af0f | -12.7196 | -50.8622 | 2025-10-18 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d9c8c0b4-d6f5-343b-b02f-0cd1f39c636e | -11.5917 | -44.0707 | 2025-10-18 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 485.0 |
| 333cdca4-529f-37b7-b385-92bd46cff8a2 | -13.011 | -47.2738 | 2025-10-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 66f2d25c-0979-33d3-871e-bfc94bd89805 | -13.2005 | -46.4084 | 2025-10-18 13:40:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c3e187ee-cfd1-3a0d-a649-58a3496a88d2 | -10.2935 | -44.0455 | 2025-10-18 13:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 95297daa-053f-32aa-91e8-02e0c1bccaf5 | -11.9709 | -45.3603 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 1b380228-cdca-3a80-aec3-1d17311d863b | -11.6104 | -44.0913 | 2025-10-18 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 336.9 |
| e8b630b2-58c9-3297-aa3c-9480c2f766ce | -10.2558 | -44.0273 | 2025-10-18 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d4088e4e-1971-3558-baa9-02223136bb09 | -11.9521 | -45.3401 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 2e7a1d56-6253-3b9f-8cad-8074e7e7998e | -13.6373 | -43.9208 | 2025-10-18 13:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 802a39f3-ae11-326d-a9fc-d06655bd73d5 | -11.3603 | -45.2646 | 2025-10-18 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| abd33f07-43ee-3500-bf12-190e7375e9e3 | -11.3772 | -44.2897 | 2025-10-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 339.3 |
| 571ae04f-204e-3234-a9a9-027b74624d58 | -10.938 | -45.4146 | 2025-10-18 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 31a6ce4a-a43c-3fc1-9f44-32de435781a6 | -11.3767 | -44.3131 | 2025-10-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 00f4f435-d6ac-3ad0-8f7c-ed8d3dfe698d | -12.9708 | -47.3695 | 2025-10-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2182b546-4037-312a-96df-8ff623e1d2ba | -10.4937 | -43.4552 | 2025-10-18 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| be0802e5-904d-3e4d-b30c-20f57a2e7d87 | -10.2554 | -44.0506 | 2025-10-18 13:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 17edced5-5798-34a1-a81d-a64046e97b50 | -10.4945 | -43.4079 | 2025-10-18 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 55046707-eb17-38b5-91f6-ff0e22b7e5a1 | -14.09 | -43.6475 | 2025-10-18 13:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a673150a-100c-3369-a80b-4c5a3ffecaa0 | -3.0632 | -43.2161 | 2025-10-18 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| dc8baeb3-8e68-341a-b139-d5518913a6a1 | -12.1485 | -45.08 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 693297d6-3d74-3187-8eb7-16f1b356f93e | -13.2644 | -47.1007 | 2025-10-18 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 5d647511-fb5c-329a-97ac-8ac1bb597c83 | -12.9519 | -47.3499 | 2025-10-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 504a0829-9d98-3a5e-b66d-1048da672311 | -16.0324 | -43.4953 | 2025-10-18 13:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 06147e46-4a6a-3372-b32f-08b2e734c819 | -11.358 | -44.2926 | 2025-10-18 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 68cf49cf-cffe-3ef2-a340-e55f23fb3c9c | -3.7625 | -41.7446 | 2025-10-18 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 1ea21db5-1216-3ddd-bbee-3d0fc5346700 | -11.9713 | -45.3373 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 361.4 |
| 9b3f27c4-7b91-388a-93e2-8af2323273b2 | -12.9524 | -47.3274 | 2025-10-18 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 7d2cc51f-04b8-32fb-b26d-d1772fcfafef | 1.7481 | -55.961 | 2025-10-18 13:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 92331366-5d4a-34dd-8d5e-b9e84ae8250a | -12.1678 | -45.0771 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| d709823b-c6db-3f6e-9253-07c3f2a2fadd | -14.0905 | -43.6235 | 2025-10-18 13:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| b521f4b1-641f-304d-a45b-df97ef724e6a | -12.1682 | -45.0539 | 2025-10-18 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4c45477e-bdc3-3e23-b513-020e0200c9bb | -10.2939 | -44.0221 | 2025-10-18 13:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 5c1b0a9a-d946-37b6-8cc1-2ccd42ea21a1 | -11.5917 | -44.0707 | 2025-10-18 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 460.3 |
| e2df8d2a-9c77-35d6-864b-c358d6361c28 | -12.1485 | -45.08 | 2025-10-18 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3892823c-fca3-3011-a29f-40b7f5754572 | -16.4783 | -43.057 | 2025-10-18 13:50:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 122.3 |
| dce3fa48-ed09-39f1-b83b-20c32561da16 | -12.1678 | -45.0771 | 2025-10-18 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| f34015fd-7c0f-3b48-a0b7-aa42e8d1b828 | -10.475 | -43.4342 | 2025-10-18 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| f16d6ae5-9981-35ca-a52f-98ebb23b9812 | -11.6104 | -44.0913 | 2025-10-18 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 377.4 |
| 516db4ad-f4a5-370a-b552-fea78e60f3d9 | -14.0905 | -43.6235 | 2025-10-18 13:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 0579742b-78f7-392f-b5ff-e18858cd00c7 | -10.4754 | -43.4106 | 2025-10-18 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a28060b8-034f-326e-a13f-730821d08031 | -14.1252 | -44.7053 | 2025-10-18 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 664c6f7c-9f36-3e67-8b57-59e28a2657fd | -10.5335 | -43.3552 | 2025-10-18 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 4d56d0f1-be33-3acb-b4ca-ef8b404c690c | 1.7481 | -55.9807 | 2025-10-18 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |


[Clique aqui para ver as próximas entradas](README93.md)
