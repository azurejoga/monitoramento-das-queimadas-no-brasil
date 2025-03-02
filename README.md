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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aed2cdec-e211-39bb-b2b8-bcec11b9ecc6 | -14.01 | -45.5641 | 2025-03-02 00:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d137a540-1148-34e4-8227-295ea8c8fb93 | -13.99 | -45.5907 | 2025-03-02 00:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 46b76412-779b-37b3-9db5-31c56b3e07f6 | 1.3217 | -60.4262 | 2025-03-02 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 252b3bc9-4702-3d06-9459-3311e35cd6ab | 1.9419 | -60.3827 | 2025-03-02 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9b800319-95bd-309e-8490-71f730995987 | 1.3217 | -60.4452 | 2025-03-02 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 0aac8fd2-7ef7-3e06-82e2-c0fab027ccc1 | -14.0095 | -45.5874 | 2025-03-02 00:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5f4b90be-535d-3b25-9cf7-af21d4ecf179 | -13.9905 | -45.5675 | 2025-03-02 00:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| b0e543fc-9b64-34b5-9e52-73757b1eee0b | -13.9706 | -45.594 | 2025-03-02 00:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| fc084660-c283-3ddd-aadb-9a01eefcdfd6 | -13.9711 | -45.5708 | 2025-03-02 00:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 6a4568b1-ca4f-3258-9624-7c78b954cd4b | -14.01 | -45.5641 | 2025-03-02 00:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 3e7ec5ba-4c50-31d3-9ff6-b7a3b6573162 | 1.3217 | -60.4452 | 2025-03-02 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0ac3257e-cf1d-3952-b01e-1c74bf092dfe | -14.0095 | -45.5874 | 2025-03-02 00:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| f47a3000-33f0-314b-869b-25b985bb6a5c | -13.9905 | -45.5675 | 2025-03-02 00:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| e2253477-dec4-393b-a453-ab9a071482ef | -13.9711 | -45.5708 | 2025-03-02 00:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 8bb05019-ed0a-3295-ada8-6485e701b150 | 1.3217 | -60.4262 | 2025-03-02 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 3d6babea-9a90-3a9e-930b-fe7947535f50 | -13.99 | -45.5907 | 2025-03-02 00:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 2122445e-5f56-36fa-81b5-b89685dd6947 | -13.9706 | -45.594 | 2025-03-02 00:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| e371a2de-d72a-3ed2-aba2-3eb359dd84ef | 1.3034 | -60.4263 | 2025-03-02 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 042aa7d5-fda7-37e0-848b-3c26029a6aca | -22.32787 | -42.74749 | 2025-03-02 00:11:00 | TERRA_M-M | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| d37c7cd5-a4c2-3692-b7d8-ecdfdd6cdef3 | -22.67253 | -42.8614 | 2025-03-02 00:11:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| ec8028b8-0fb5-30d3-9a2c-160c2358bb8a | -21.20674 | -48.54894 | 2025-03-02 00:11:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.5 |
| 85f9ae18-b36f-3127-b19c-72bfde074d63 | -13.98265 | -45.60744 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| f4afdaec-4964-35b5-be22-d26c1d508542 | -15.32412 | -42.35724 | 2025-03-02 00:13:00 | TERRA_M-M | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| e31023f9-3473-3a97-8d5b-d938b6aef13b | -13.98149 | -45.60205 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 7706f81a-8b70-317f-83ab-2ee9bc6dcb99 | -13.99441 | -45.60044 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| e7bdf9bf-2f95-30f5-84f8-c2e25bf9442d | -13.96634 | -45.58312 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| ba5d3356-86bd-3173-b2b1-8bcc6563cfc3 | -13.99312 | -45.58534 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6ab7f8c8-5ac6-3491-b734-6fd6dcf65813 | -13.97782 | -45.56648 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 26293632-c56b-3931-8c2f-d9bd98441464 | -14.00503 | -45.57841 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f63033bd-5005-30a1-be99-bb6adb369082 | -13.99212 | -45.57993 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| eb046831-a038-3d00-83e3-3160a89af9ac | -13.96495 | -45.56807 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3fc25983-64b4-3261-8d68-97cae46816d9 | -13.96734 | -45.5885 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 75be6950-1fa8-3884-a6eb-bc4d2d3db84d | -13.99556 | -45.60586 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 8777ea5e-2584-32d1-8c08-3a7b891f2834 | -13.97923 | -45.58149 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 488.0 |
| 22b7bcd2-54eb-39cd-9c71-6a432756ccd2 | -14.00733 | -45.5989 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 74f69510-3581-38bd-b3ec-2124816e9a0c | -13.98023 | -45.5869 | 2025-03-02 00:13:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 397.0 |
| 6bdc4d83-78ed-3a64-b403-6301fea6640b | -9.81375 | -38.10653 | 2025-03-02 00:15:00 | TERRA_M-M | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bdbf6ccc-9ba8-38c8-8ce3-4a9e29692cff | -9.81235 | -38.09688 | 2025-03-02 00:15:00 | TERRA_M-M | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5ba0604a-15c5-3846-b5b9-b104c9ac7bd5 | -10.48792 | -42.4131 | 2025-03-02 00:15:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| eb241ae7-2c18-36bd-80cd-1c88ea5972ac | -10.52101 | -42.44115 | 2025-03-02 00:15:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3532ade6-0289-33c1-a8b2-72bf536c7151 | 1.3217 | -60.4452 | 2025-03-02 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f2eca531-20bf-3219-9ed3-62d6bd3fe2fa | -14.0095 | -45.5874 | 2025-03-02 00:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| a9428ea5-a98a-3eee-bbfd-b6aafe22126b | -13.9905 | -45.5675 | 2025-03-02 00:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 218.6 |
| b480d0d4-a696-3f24-b8aa-76272e4e4a3e | -13.9711 | -45.5708 | 2025-03-02 00:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 213.3 |
| fd8abf70-0905-3bb1-aabd-81c59e993849 | 1.3217 | -60.4262 | 2025-03-02 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 119.4 |
| e265c398-f166-37e6-9dc7-f589973d2143 | -13.9706 | -45.594 | 2025-03-02 00:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 3975b407-7c8d-370a-83b2-50b5388795aa | -14.01 | -45.5641 | 2025-03-02 00:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 31a13c1f-27bc-3abf-adfd-22651dca032b | -13.99 | -45.5907 | 2025-03-02 00:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 202.3 |
| a05772ef-fd21-3e67-8ee4-ec2db4ed2c47 | 1.3034 | -60.4263 | 2025-03-02 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 567456bd-518e-37b9-93c3-e42a0ed9a62e | -13.9711 | -45.5708 | 2025-03-02 00:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| ae4d939f-8d85-3d16-a696-3edc5cb635d7 | 1.3034 | -60.4263 | 2025-03-02 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1ddfaaa8-9ed9-3146-ba27-267e3e3ef7a2 | -14.01 | -45.5641 | 2025-03-02 00:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 18b418c0-8145-3dce-b2a1-021c2fdd3517 | -14.0095 | -45.5874 | 2025-03-02 00:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| eceddf63-8f16-3834-a05e-e1bbe28ac78b | 1.3217 | -60.4452 | 2025-03-02 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b9ee29a1-92c8-39d7-91c1-9c34c07ed162 | -13.99 | -45.5907 | 2025-03-02 00:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 696246b5-e9c3-3264-ac39-ab5774968038 | -13.9905 | -45.5675 | 2025-03-02 00:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 3615d2e2-d24f-3413-beac-332157b86ad6 | 1.3217 | -60.4262 | 2025-03-02 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 5d0e4b68-cd9f-3163-8adf-98554fa8f9a8 | -13.9706 | -45.594 | 2025-03-02 00:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 91634aa7-2b8d-36b7-9df9-23bee772b751 | -13.9706 | -45.594 | 2025-03-02 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| b8392383-da6e-3d03-98cb-cc8d03fed7bb | 1.3217 | -60.4262 | 2025-03-02 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 54c1bdc7-3838-3ce2-8bbc-0bfb0d8cf356 | -13.9711 | -45.5708 | 2025-03-02 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c533d4c7-915a-319c-bfcc-850002711062 | 1.3217 | -60.4452 | 2025-03-02 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| da5ff4e3-6f6f-3974-8b1b-00b5b3ca5f40 | -14.01 | -45.5641 | 2025-03-02 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 44d743d5-b616-32b9-b93e-d484f5cf96fe | -14.0095 | -45.5874 | 2025-03-02 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 5918fd8b-c6d3-356f-9ee4-dd11954f239c | -13.99 | -45.5907 | 2025-03-02 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 07d7a902-3cd3-3cbc-8b9d-e7ee097aa1b2 | -13.9905 | -45.5675 | 2025-03-02 00:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 232.6 |
| b46feffb-0398-36e3-9aa0-4e8fa241d1dd | -13.9905 | -45.5675 | 2025-03-02 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| b4413ba0-d615-3b38-87df-7cf8589a4bcc | -14.0095 | -45.5874 | 2025-03-02 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 9e8bd7f1-8172-305a-821f-e83cab021836 | -13.99 | -45.5907 | 2025-03-02 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 87f102a7-a48a-3f07-b3b7-1f253766bb30 | -13.9706 | -45.594 | 2025-03-02 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| a4ddb24a-1020-3af9-84e6-2c3f8a4923ca | -13.9711 | -45.5708 | 2025-03-02 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 50c9179d-37fc-3db1-9a92-718d01ff0086 | -14.01 | -45.5641 | 2025-03-02 00:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 82dc901e-0f9a-3f8f-996e-76c03105243d | 1.3217 | -60.4262 | 2025-03-02 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c4dc2532-41d9-3f5d-a126-97fc5c1b5b07 | -13.99 | -45.5907 | 2025-03-02 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 238.8 |
| 5ea20576-ba51-355a-aa4a-505219be109d | -13.9706 | -45.594 | 2025-03-02 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 35edd61a-12ae-39e8-8562-dc9f85561b21 | -14.01 | -45.5641 | 2025-03-02 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 102ff195-1142-3e57-b14e-b38313d2cb23 | -13.9905 | -45.5675 | 2025-03-02 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| fc025f1e-90b9-3d10-b0f6-1d33dbefe379 | 1.3217 | -60.4452 | 2025-03-02 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ebacc42a-6b98-3d82-8a8b-f53a2a9ddf41 | 1.3217 | -60.4262 | 2025-03-02 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c0bfdd64-9a3b-368e-80d7-b62fc29b6c82 | -13.9711 | -45.5708 | 2025-03-02 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e6c09346-f367-3b27-8007-006c761b6ebe | -14.0095 | -45.5874 | 2025-03-02 01:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8d72c724-d307-3e9b-9ac2-e56036b0c473 | -13.9711 | -45.5708 | 2025-03-02 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 618e0fd4-69d4-3f98-9d9b-068ee2362d91 | -12.8462 | -43.8223 | 2025-03-02 01:10:00 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5cb817d9-0333-3e2a-a563-be69f45193dd | -14.0095 | -45.5874 | 2025-03-02 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f0c7bb17-a62d-3548-86b0-7ef21b45eca1 | 1.3217 | -60.4262 | 2025-03-02 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d9b13de7-8d6d-39d9-b589-990feb48cf90 | -13.9706 | -45.594 | 2025-03-02 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 05af176d-7c5f-3fcc-ade4-647d63addae0 | -13.9905 | -45.5675 | 2025-03-02 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| ee5f8a2d-26ff-344e-956b-2b20f212a94d | -13.99 | -45.5907 | 2025-03-02 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 233fa36d-8615-3133-9d39-68609a66c3a4 | -14.01 | -45.5641 | 2025-03-02 01:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 01d049fb-a02a-373d-92e6-d2d5ea28e005 | -13.99 | -45.5907 | 2025-03-02 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 2a4f504d-a6c5-31b8-b9e8-4ec021ba954e | -13.9711 | -45.5708 | 2025-03-02 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 222869d0-c599-3082-b31c-566d7a8c7dfe | 1.3217 | -60.4262 | 2025-03-02 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ccb442b9-fd3e-3591-bb9e-3e59082b6955 | -13.9706 | -45.594 | 2025-03-02 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| c909c2e2-fe9f-3dd2-90cc-ba5cc8a94373 | -14.01 | -45.5641 | 2025-03-02 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| dfa83f98-ddf1-3ada-8366-77c627c4f904 | -12.8462 | -43.8223 | 2025-03-02 01:20:00 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 2fe70304-f555-341f-a5a4-16c7e1c29417 | -14.0095 | -45.5874 | 2025-03-02 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 126e7082-dd35-35d0-9b63-375df40444c3 | -13.9905 | -45.5675 | 2025-03-02 01:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 27bf1268-e613-35c1-a688-9c32acde2a44 | 1.3217 | -60.4262 | 2025-03-02 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a0d5c655-5708-349f-be47-f14c693b8992 | -13.9706 | -45.594 | 2025-03-02 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 8bf95780-4fe5-36a7-9599-7b92e7ad1ba4 | -14.0095 | -45.5874 | 2025-03-02 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |


[Clique aqui para ver as próximas entradas](README2.md)
