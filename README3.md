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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62907771-5c0a-3865-9301-552b0eee11fa | -11.6631 | -47.707 | 2024-10-04 00:16:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ed753954-d362-3108-a741-1a45c9d38bd4 | -11.6635 | -47.6847 | 2024-10-04 00:16:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 102711f8-d190-3468-b7e7-3ca6cf24857c | -11.5991 | -65.0204 | 2024-10-04 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2decaa7d-4436-3b8b-bd14-ba244b3d276d | -11.5992 | -65.0015 | 2024-10-04 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 141d6d9d-dcd2-39b2-b5c1-798a7840b3c4 | -11.618 | -65.0007 | 2024-10-04 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2832e412-55f3-3b9d-85bd-e4cc35b222c2 | -11.6181 | -64.9818 | 2024-10-04 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 72e68989-c2ba-3dce-9957-89aba4ac1bfd | -11.6369 | -64.981 | 2024-10-04 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 78a81739-254b-3a46-90ca-af50881c0c1d | -11.6744 | -64.9793 | 2024-10-04 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f466e593-8220-3775-84c1-3df8f159b97d | -11.6932 | -64.9785 | 2024-10-04 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 121.2 |
| bf90b6cf-fb74-3b8d-9f7b-a94771039dd1 | -11.712 | -64.9777 | 2024-10-04 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 49f44cae-30d3-361e-9c26-e91f15ce7155 | -11.8052 | -56.6024 | 2024-10-04 00:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 727ac03b-6141-337b-a315-8837d2ec7a6c | -11.8242 | -56.6009 | 2024-10-04 00:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 7050c0b1-4ad4-3c40-bdac-04348c82287c | -11.8244 | -56.5808 | 2024-10-04 00:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b10ad5f7-7494-3747-87c9-bd51bb07910e | -11.9147 | -56.9539 | 2024-10-04 00:16:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c634dfd2-7adc-3944-8ffa-5048ec28c6f7 | -11.8739 | -63.2975 | 2024-10-04 00:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 73087259-0179-3b32-807d-628010ae0f34 | -11.874 | -63.2784 | 2024-10-04 00:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 84bd7a20-8562-3901-ada7-d405a7f7cbf6 | -11.8928 | -63.2774 | 2024-10-04 00:16:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6b20c40b-3840-3705-8217-4b339685fb17 | -12.5898 | -53.1359 | 2024-10-04 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 33cadf86-c818-38c5-9ddf-0bb5a384732d | -12.5901 | -53.115 | 2024-10-04 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 1035a84b-458a-3de5-a70e-c20fdf16d362 | -12.6295 | -63.1225 | 2024-10-04 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 403a535c-b04f-33c7-9aac-64a509e731f3 | -12.6296 | -63.1033 | 2024-10-04 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 10e64286-27c6-3650-80e1-52efbd7ab5ed | -12.6484 | -63.1214 | 2024-10-04 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 5e40e331-4239-39c2-bb1a-2fa8f86330e9 | -13.1254 | -46.3063 | 2024-10-04 00:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 475d3be6-4d9c-3631-87b5-89ed887e1e57 | -13.1447 | -46.3033 | 2024-10-04 00:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d94baf47-9814-3d0a-adca-f2244dc344fe | -13.0786 | -51.1385 | 2024-10-04 00:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4596b075-d0ee-3c25-9060-6815b5035450 | -13.0971 | -51.1789 | 2024-10-04 00:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 5834bf47-5232-3157-bb21-87ec016a50f7 | -13.0975 | -51.1575 | 2024-10-04 00:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 8227f3f6-4d09-3c8f-9fe2-8371a2bbe13e | -13.1163 | -51.1765 | 2024-10-04 00:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 091c82a3-3f8f-3806-aa88-d0ee24295119 | -13.1166 | -51.1551 | 2024-10-04 00:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 5c610d7b-047c-3674-9672-cf4e307582c6 | -13.6143 | -51.22 | 2024-10-04 00:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f58a1a5a-471c-3793-b07d-79bb1bc56b2a | -13.6146 | -51.1986 | 2024-10-04 00:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| b7e73839-ceeb-37de-a5d5-d19ebaf2d84a | -13.9845 | -44.0236 | 2024-10-04 00:16:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d4931a16-358b-3639-9819-dd567c4a1650 | -14.0035 | -44.0438 | 2024-10-04 00:16:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1610cfdd-b0e5-31a7-bc2c-b5b35135f052 | -14.004 | -44.0201 | 2024-10-04 00:16:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| c21bf8d4-1908-3150-9301-d692cd84a3ad | -14.7939 | -48.0275 | 2024-10-04 00:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6ae09fa2-c810-3068-9bb9-bc0d9f374abe | -14.8134 | -48.0243 | 2024-10-04 00:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 4d1ea77d-ae29-33f1-a504-7017cc20a6cd | -16.3956 | -57.3845 | 2024-10-04 00:16:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 7c0adb41-d365-3fc0-9c97-eb04ef54d88e | -16.4148 | -57.4028 | 2024-10-04 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| d452a024-3520-3346-bd9e-bb5516c198bc | -16.4151 | -57.3823 | 2024-10-04 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 46684cd4-9704-3878-8e49-5c7781b9258d | -16.4554 | -57.2962 | 2024-10-04 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 13329633-1d79-3824-b700-54ef46d61641 | -16.475 | -57.294 | 2024-10-04 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 00455a6b-2280-31cd-aec9-6c703bb6969b | -16.5783 | -58.198 | 2024-10-04 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 9df953c2-3da0-3fff-89dd-a66609877a34 | -16.5935 | -57.1988 | 2024-10-04 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 0065588e-80ff-394e-b9d3-2311bec89118 | -16.5938 | -57.1783 | 2024-10-04 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 9d0736ce-cd3d-3787-8ff3-9b0adfc42d7b | -16.5941 | -57.1578 | 2024-10-04 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 47d5cc05-c1f4-332c-81d8-0864efdd73a1 | -16.9302 | -47.1224 | 2024-10-04 00:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| df54ca60-b53b-3a04-84e4-3f212608db8d | -16.613 | -57.1965 | 2024-10-04 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 19335198-6833-37d5-a335-8387cee7c736 | -16.6133 | -57.176 | 2024-10-04 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 159.2 |
| a24ad212-3e12-335f-9961-c22fbec4a101 | -16.7606 | -57.7512 | 2024-10-04 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| c0809349-5881-3cd8-bb86-ccb2db1e3077 | -16.8433 | -57.4562 | 2024-10-04 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 5094462d-14f3-316a-ba1f-1c8cbcba4e1b | -16.9087 | -55.843 | 2024-10-04 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 1b7091bf-df99-36e8-9837-ae5b85d7fa67 | -16.9283 | -55.8405 | 2024-10-04 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| bafeb079-4ae8-3d45-b90d-31f27e4fd40c | -16.9287 | -55.8197 | 2024-10-04 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 4656bd1e-65ea-3554-8ca8-1c507bacff05 | -16.7856 | -57.4015 | 2024-10-04 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 4aba5b96-33c9-36d9-ad3f-d2632eb013e2 | -16.7859 | -57.3811 | 2024-10-04 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 385.8 |
| af6c17f8-5413-379e-848a-9a7c926eed07 | -16.7862 | -57.3606 | 2024-10-04 00:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 7bdb8bcb-c4c8-3030-ab4c-7c0e66a9f38c | -16.8055 | -57.3788 | 2024-10-04 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.6 |
| bb4396ee-2f67-332b-a429-f4bad64bf4d5 | -16.8058 | -57.3583 | 2024-10-04 00:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| ce87359f-bb65-3a2e-bebb-6809102ee59a | -16.843 | -57.4767 | 2024-10-04 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 9e6a5a9f-3ede-3730-8229-c9a91ae9c193 | -18.8613 | -43.5837 | 2024-10-04 00:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.7 |
| df88abc0-3ee0-3538-93cb-b8e4f59b650e | -18.862 | -43.559 | 2024-10-04 00:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| 1ea5ca70-a76b-3ec1-b13e-698084db117a | -19.0344 | -43.1944 | 2024-10-04 00:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.4 |
| 05baf604-7c06-31b6-94e0-ba853a113e1f | -19.1667 | -43.5051 | 2024-10-04 00:16:51 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f734f53d-1094-35b1-925d-f25a13f3c32a | -19.187 | -43.4997 | 2024-10-04 00:16:52 | GOES-16 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 887b0b1c-7609-3c81-b594-c9cd2ed22ccd | -19.4899 | -42.8746 | 2024-10-04 00:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.0 |
| 4eb5b554-3e7f-3929-9a15-4755e2bb0b17 | -19.5104 | -42.8691 | 2024-10-04 00:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| edbf5e58-24c0-3c4c-b408-6b94b6ed4a09 | -20.0517 | -41.2473 | 2024-10-04 00:16:56 | GOES-16 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| dbf21ac0-2641-347c-aa1f-766328e515fc | -20.083 | -43.4332 | 2024-10-04 00:16:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| 0513e234-aa36-3522-ac60-e8de4cbecbc9 | -20.0838 | -43.4082 | 2024-10-04 00:16:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 9d5b31e4-ea48-39b2-9253-c807a128becd | -20.1036 | -43.4276 | 2024-10-04 00:16:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| 0fdaab6e-d72b-317d-b4e8-ba1b27d5959b | -20.1044 | -43.4026 | 2024-10-04 00:16:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |
| c884c685-6ab2-3409-975c-062b92d4b8e1 | -19.9907 | -48.6913 | 2024-10-04 00:16:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7aece626-9fa9-383d-8800-d93f462a9205 | -20.0111 | -48.6869 | 2024-10-04 00:16:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| f875e020-4479-3ceb-bc76-05b431eada45 | -20.7984 | -48.9033 | 2024-10-04 00:17:01 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| 501cb581-42b7-3195-9a6e-a583e367bb7a | -20.8183 | -48.9219 | 2024-10-04 00:17:01 | GOES-16 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.4 |
| cf73f842-cd8d-3806-be35-dd2a4496480a | -20.819 | -48.8987 | 2024-10-04 00:17:01 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.7 |
| 9631fb2e-5868-354d-9c42-7cd24c1ba181 | -21.3328 | -48.8277 | 2024-10-04 00:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 43d34ee3-dc4c-382f-b698-21775c232599 | -21.3334 | -48.8044 | 2024-10-04 00:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 208.8 |
| 372b4cc8-f0cb-3073-8a1a-ff459aff531a | -21.3534 | -48.8229 | 2024-10-04 00:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| a2e989e3-9aed-3915-a162-21242c0c6b24 | -21.3541 | -48.7996 | 2024-10-04 00:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.1 |
| a2b6a8c2-b409-340f-af49-47910efbb656 | -21.8079 | -48.7626 | 2024-10-04 00:17:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 9a506cae-084a-3657-8717-840c816d15d8 | -21.8189 | -48.3876 | 2024-10-04 00:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 80eb93f5-398e-3230-89b8-639bc4ed4ee2 | -21.8196 | -48.3641 | 2024-10-04 00:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 10ef110e-6e71-3203-8b1e-cadda29de02c | -21.8376 | -48.4531 | 2024-10-04 00:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 063d30b4-a607-39ff-98b5-d0956e97f054 | -21.8383 | -48.4296 | 2024-10-04 00:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 66cb2a4a-2abf-3c3a-b57f-c3b8609cca8d | -21.8397 | -48.3826 | 2024-10-04 00:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c12d8f51-2fcb-386e-a972-e049b6c824d0 | -21.8591 | -48.4245 | 2024-10-04 00:17:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1d50289b-aa57-365d-bb9b-7a241732f81d | -2.9493 | -52.7952 | 2024-10-04 00:25:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8c0b44a5-b2ac-38ad-80ae-b17f433c6488 | -2.9494 | -52.7748 | 2024-10-04 00:25:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 43c1135a-7248-3516-ba13-8a3bb107f3be | -3.2349 | -50.3695 | 2024-10-04 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 185d0c91-3611-3a2f-8a67-c66734b7e6e2 | -3.2534 | -50.3689 | 2024-10-04 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 14e00f15-4bf1-3c16-8c09-7353062dd8c9 | -3.404 | -42.2858 | 2024-10-04 00:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f158912e-7410-33cb-b3f9-f9d5e13d2cc1 | -3.2899 | -50.4725 | 2024-10-04 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 2ae416f5-4f8f-3f04-8ab5-f14f6e6338fa | -3.2899 | -50.4516 | 2024-10-04 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 293.6 |
| 3876354b-b303-317f-bf24-9dc1e1e6b1d8 | -3.29 | -50.4306 | 2024-10-04 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 5649bf9e-7d02-3d8a-851b-51e4399e886b | -3.3083 | -50.4719 | 2024-10-04 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 4ee9dbf2-52ab-333b-a117-30d605e11551 | -3.3084 | -50.451 | 2024-10-04 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 208.4 |
| c51b4e66-df20-3387-995f-d40f8362ed09 | -3.4915 | -50.8004 | 2024-10-04 00:25:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f78005ea-fb24-3a50-a3d8-699efab9a5f2 | -4.0763 | -48.4902 | 2024-10-04 00:25:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 28963681-5b05-3658-b84e-7382220ab9d2 | -4.0949 | -48.4894 | 2024-10-04 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |


[Clique aqui para ver as próximas entradas](README4.md)
