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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e917ffa7-7276-3f15-8418-b515c6abbf64 | -17.77863 | -50.4721 | 2026-06-05 04:25:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34b7c30a-80f0-378e-b73f-610dce51d23a | -16.59813 | -58.23739 | 2026-06-05 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b944901d-19f2-39ea-a602-18503f6eaa41 | -11.88467 | -57.83412 | 2026-06-05 04:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1839bc2-b005-32e8-919f-03215d842b63 | -12.44059 | -58.40981 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01634437-36bb-3d1b-a169-ed31d343225a | -11.33195 | -51.38999 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a203241a-9c46-3f0e-8808-46a8b6a3482d | -10.84776 | -53.75569 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de798e36-b4d2-3961-b6aa-8e3f19ed76ad | -11.55415 | -52.80262 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 92071c53-70a5-3dd7-a631-5c02aeef75be | -12.51302 | -48.2748 | 2026-06-05 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b8c0eec-6748-3c18-a751-99976fb3a691 | -14.37699 | -45.5831 | 2026-06-05 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 809b83ca-93c3-3256-a927-6f6adcef8be3 | -12.52392 | -46.2797 | 2026-06-05 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74b5bdf0-992a-3619-ad5c-3a87a569344c | -11.55304 | -52.80844 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9e37f4fa-0454-39c5-bbad-19a11985dba4 | -11.55803 | -52.80939 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a04790c7-da38-350c-9471-1614695af246 | -11.05667 | -56.92492 | 2026-06-05 04:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89e2a586-faeb-3959-9f2b-3bb33041cd3c | -12.44598 | -58.48717 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b35826ae-bee3-34b9-b561-80eceb488f9a | -11.01241 | -54.3146 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cff157e-9827-3cf6-96c9-f36419e82738 | -10.84303 | -53.75127 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2f87088-cc2d-38b3-8c20-31c77bb42f4d | -17.86261 | -51.78517 | 2026-06-05 04:25:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7e9b758-6ef2-32c0-aea4-19726913ae6d | -11.27016 | -53.9747 | 2026-06-05 04:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a9a1414-02a7-369f-8058-b059d2522699 | -17.77953 | -50.46716 | 2026-06-05 04:25:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b986520f-da3f-308c-8095-b176033d5c43 | -14.37319 | -45.56409 | 2026-06-05 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69219aa0-7c0b-38f1-ad37-6861f787dc84 | -12.72674 | -54.73432 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c35e1a6-b27d-39b3-9100-5520cfe64615 | -11.56023 | -52.79787 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fa62ce36-743e-39ed-a49f-0a52d6af7ad8 | -11.54897 | -52.80725 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c78163dd-6563-3d4a-ac3a-3dc1ade7ee65 | -10.85703 | -53.7365 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c27f677-eb18-3329-af95-e832085d6f03 | -12.44536 | -58.41523 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52c45967-39b2-38d4-a778-78be232ea7fa | -12.44072 | -58.46973 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4a49173-091a-36d0-85e3-8bb59ca931ec | -11.60129 | -55.3375 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cd0f524-9ed4-3cf1-ac74-6b622bd757ae | -13.42843 | -49.64513 | 2026-06-05 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5ce4738-f637-3d60-adf4-23dfaa2e012b | -16.59687 | -58.24299 | 2026-06-05 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 92b8a381-df40-3ea1-addf-9f699461640c | -14.79705 | -42.80759 | 2026-06-05 04:25:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b10cd5fe-307f-3067-afa9-f3731e9f06f3 | -11.57769 | -54.58155 | 2026-06-05 04:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95475ab8-77a2-3f15-b3a7-2cd5d35e0725 | -11.05011 | -56.92379 | 2026-06-05 04:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ec5a46c-0fda-3cf8-b669-8216f0b00373 | -12.43919 | -58.41638 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a214d2f0-e1ca-36ae-bb84-a99b98229f5d | -11.3311 | -51.39468 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5282e89c-53fa-3b9b-9399-736011834c84 | -11.55005 | -52.80141 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 298042eb-2a6f-3f9f-b36d-36e78342938c | -13.51658 | -54.31115 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 654edec2-1862-3ddb-9fff-d03462fbcdd3 | -10.8684 | -53.73528 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15ed1919-9193-34a0-a1ce-c109ee57b02e | -16.95517 | -50.49242 | 2026-06-05 04:25:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4f8d653-cf7b-3780-82ba-2a1c9c458e79 | -12.53419 | -45.68174 | 2026-06-05 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa8ef7f5-7ac9-35b2-9812-567407a215b2 | -12.45004 | -58.46791 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3f4d279-1c3a-3ff1-bc21-7ffc0fad042f | -10.56999 | -57.32475 | 2026-06-05 04:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce466c6-9504-3e42-96cf-5dd6c133a8d3 | -12.44198 | -58.40324 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1fbafd2-b09b-3fbf-9199-6960078f542e | -11.60876 | -55.34064 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea320692-9fc1-33db-9ce9-5b49895d9ae5 | -11.57213 | -54.58023 | 2026-06-05 04:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| da30cf81-9c49-3f21-b000-5d6684abb898 | -12.43796 | -58.48239 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| deaf93b0-d35f-327b-b223-a2fc0c780cd1 | -11.57138 | -54.58411 | 2026-06-05 04:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0af2cfe-9cea-3b4a-a5b6-fb53ff03a5b0 | -12.08977 | -51.99931 | 2026-06-05 04:25:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb1ef67-2edc-369f-b059-c1bcb42febb2 | -17.86563 | -53.26358 | 2026-06-05 04:25:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b28bb13d-551e-310e-951b-34cac143ebfe | -15.43642 | -46.33634 | 2026-06-05 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 874100bb-b59c-3dd8-b767-79de57daf8f4 | -14.14946 | -51.58928 | 2026-06-05 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75e6bf77-c7ff-3acb-be3b-5d63250ecb6e | -16.60344 | -58.23869 | 2026-06-05 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6c90548b-7dab-3433-bbba-e7d77b7369a4 | -13.91523 | -42.10327 | 2026-06-05 04:25:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 22a436fe-7eb3-3e0e-a706-7f47d4b15f2d | -13.66715 | -47.75909 | 2026-06-05 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 664d0d0d-e0c5-36e9-bf71-979fc2583871 | -12.43653 | -58.48893 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd0ef5a0-16b2-3aba-b16d-01d20dedcd84 | -11.60715 | -55.33873 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b024277b-f1d7-315f-8cce-7e9780cab689 | -14.37377 | -45.56052 | 2026-06-05 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f5a889a-0597-36ac-9b8f-1e13cfab76cc | -12.73303 | -54.7316 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22760488-31fe-3268-a717-ff370b90bb11 | -11.56003 | -52.80335 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 68b783f0-6ef8-3c7a-85ee-fd31c20bd6bf | -11.56411 | -52.80464 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 725e8976-f683-3c09-aed9-8bce15a6944e | -11.87923 | -57.8264 | 2026-06-05 04:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0e14339-dbf3-34b6-a7d3-65e83698bc36 | -14.94689 | -49.55111 | 2026-06-05 04:25:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49a39dc9-97f3-3ff9-820e-c5b6b23be763 | -12.44679 | -58.40866 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c636cfb-f5f0-31d0-b00f-6b954a8d3d18 | -12.08695 | -51.98835 | 2026-06-05 04:25:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b27690ff-5757-3916-b29f-a7164758cf18 | -12.44042 | -58.47912 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cda53115-e22e-3844-86b1-419db74a08af | -12.43761 | -58.49241 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d689b352-df6b-3203-985f-4531a032296c | -12.80849 | -54.86564 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d850290a-07dc-33a3-94bd-5d8cec2c5f4f | -14.77573 | -52.67305 | 2026-06-05 04:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 956c3349-a9ac-3332-8b43-b89e1f180877 | -11.55897 | -52.80912 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b56a42ac-40ee-310b-bf8c-1ece142eecfd | -12.73451 | -54.72417 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f200019-0075-39f2-9f0b-8826b84c628d | -14.78646 | -50.6377 | 2026-06-05 04:25:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14a50c9b-2380-372d-b756-57a045d8467e | -13.66854 | -47.75097 | 2026-06-05 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 441f820a-6579-31c1-91ab-0d42a5bfa317 | -12.22775 | -57.28265 | 2026-06-05 04:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c12dd0b-f1ec-3149-9a27-ee6ae330d35d | -19.0578 | -44.80362 | 2026-06-05 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59e5ecd5-eb70-3897-b871-b6eee3c2c7fa | -14.77477 | -52.67808 | 2026-06-05 04:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25de6e20-fe82-3c5e-96da-6ac2862a1c51 | -12.53142 | -45.67758 | 2026-06-05 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a23be06-bd0c-3dcd-bf14-f0d830c03b69 | -11.83582 | -49.43522 | 2026-06-05 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ac51103-8d22-30d0-a334-4067e531c4d6 | -12.44175 | -58.4728 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0469855f-07e7-35b8-a21b-afcb30e69492 | -11.99349 | -47.77325 | 2026-06-05 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3ab52e6-3688-3bdc-8ced-f200f97108c6 | -10.86304 | -53.7342 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ef92b42-c50d-3da2-8095-5e22163a3b42 | -12.09164 | -51.98919 | 2026-06-05 04:25:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a044090-6686-32a8-a824-74b3e5240092 | -13.66646 | -47.76315 | 2026-06-05 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23ff2d74-cca0-3864-9b2e-25390bb1390e | -10.57121 | -57.31862 | 2026-06-05 04:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e66aa76-fd0e-3074-bee8-30dca705e427 | -12.06188 | -48.07601 | 2026-06-05 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e62407ab-e6a5-3fb2-9b54-06e2fd2c4e04 | -11.27086 | -53.97108 | 2026-06-05 04:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb701d97-0988-3adc-98f6-0addd2a48163 | -11.01723 | -54.31952 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc455495-964f-3086-a28f-db6813467995 | -11.565 | -52.80438 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e41d57de-0de7-33cd-90bd-2ddb3b3e385b | -12.43905 | -58.48559 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f37da19a-17d4-3fa2-a663-98da16fa5068 | -11.55398 | -52.80814 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9bc7c383-93b3-3084-b69b-d8f01731bf1b | -13.51824 | -54.31484 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60a5b184-49b8-3c8e-bdac-f130a07f1133 | -12.72748 | -54.73058 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7c5a072-687e-31cb-bf63-12f2f6652b27 | -14.36205 | -45.56956 | 2026-06-05 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3bb2a187-19e1-315b-92bb-f20516e58310 | -11.00131 | -54.31232 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1008d81-a3b8-336e-aa3e-7554aca80e5b | -10.85445 | -53.7499 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fff48d9e-bd36-3954-8981-953facb0e5b7 | -14.37642 | -45.58667 | 2026-06-05 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 100383c5-216c-302f-8994-06d263a55604 | -11.00203 | -54.30857 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c120f152-80cf-3cec-8697-4fed8b60e9b2 | -12.73155 | -54.73908 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b33abca3-9aad-3cb8-a05d-c3736a0440a5 | -12.44631 | -58.47744 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cccefce2-3fe1-326a-8e4d-8565d925c1c7 | -10.8624 | -53.73756 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 913e26e0-126d-3a72-8937-b62a1acfd11b | -12.22893 | -57.27695 | 2026-06-05 04:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40ba4361-fb87-3118-8ca0-2065e8207824 | -16.60447 | -58.23898 | 2026-06-05 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |


[Clique aqui para ver as próximas entradas](README9.md)
