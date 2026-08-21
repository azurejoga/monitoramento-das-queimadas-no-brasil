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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65f678c2-e80f-3e65-b359-ce9e86b7c1ba | -14.02722 | -58.87061 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3769a3fe-bd24-3fab-aaff-23de280ec9b4 | -12.51753 | -54.76645 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d76de7f6-24ad-3ced-9b9c-4001f5c28a61 | -13.38774 | -54.3805 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7051a568-bd7f-3c3d-8657-4313302f5d42 | -14.31681 | -51.89207 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3c168fc6-3090-355e-affe-bb07e54ce8f1 | -14.33657 | -51.90892 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b07877c-8747-3eb1-a791-3fc4446c185a | -13.40081 | -54.37322 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39e05cfd-8298-3538-906e-b5b555297e84 | -12.50066 | -54.75955 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd179fe1-9302-31f8-adb7-0c5f71ee441f | -13.9319 | -53.8511 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bf7507f-3e0f-3f8f-87fe-d714f3db9dee | -12.49536 | -54.75461 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 52362706-055f-3ab7-b922-452e2c659770 | -13.0945 | -58.1875 | 2026-08-21 05:44:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7c1503-4ece-33ff-a096-a2874358de48 | -13.0956 | -51.58627 | 2026-08-21 05:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3c134fc-8c58-3c5e-8217-af619006fbc9 | -13.92565 | -53.85023 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d293832-0279-3473-bd01-c46c2c049705 | -14.33798 | -51.8946 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ae4ffa6-846c-3e7f-8aad-07d7435a202a | -12.50117 | -54.75537 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a65abcc5-7908-309a-8197-e8dba93c9287 | -13.37573 | -54.3788 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b21a6447-6a79-32ed-8ec0-0598dd408b36 | -13.94382 | -53.85814 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb80a073-5bdd-3d3c-8a02-0089ab78450d | -13.39272 | -54.39029 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 360e0801-6d18-3524-b0dc-c6d72094b4b7 | -13.38226 | -54.37512 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 602854c3-8e9f-32c4-adb4-da117b9cbe8b | -13.3752 | -54.3834 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3d0db034-91ca-3846-9242-e1aee5c77505 | -13.7424 | -51.85825 | 2026-08-21 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4f20248-727f-3414-8333-b45c1993e10b | -14.32249 | -51.90699 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58a7234e-059f-36f2-bb79-d215cad2d6bb | -14.33132 | -51.9159 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 93c5c9c7-ace8-3d06-8417-8149099ec763 | -13.39533 | -54.36778 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ee8f980-a357-3e5b-8785-6d76d7772dbf | -15.00768 | -52.6765 | 2026-08-21 05:44:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c019cab-4fc2-346e-aa83-258ec24d7b3e | -15.00089 | -52.67567 | 2026-08-21 05:44:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c3413f9-b958-32e9-8a8a-06a4c900872d | -14.30977 | -51.89106 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 63e457d0-c4e9-362f-bbb9-874c9fa1f92b | -13.38069 | -54.38876 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ede06fa4-20b0-3620-a881-ff954c255dca | -13.93812 | -53.8522 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edb08ed3-310f-3aac-b7aa-3ec9ea0bc462 | -14.31242 | -51.89188 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 85eb8c58-0a69-3646-bc6c-f705cd78e104 | -12.51224 | -54.76137 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa0f552f-ed7b-315d-bca3-71b02f8cf35e | -13.92508 | -53.85545 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f25ccd6-c34f-33cc-9a89-bae1f54fda19 | -14.10512 | -58.85107 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f04b2eb-edb2-3526-8f35-dd5f75e82dd9 | -14.3117 | -51.89882 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| cb36ecb8-33cd-3c7d-ac32-96d3a235d829 | -13.39324 | -54.38575 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f01a07e3-d18b-3a7f-941c-d02d4049d97c | -12.51327 | -54.75295 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 167b961e-d60d-3406-b726-ab7f07ea9ff0 | -12.5187 | -54.75422 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4d8d2d5-3d53-304e-b390-6c96ac471272 | -13.3948 | -54.37237 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5dce6b3e-41d6-3495-88fe-7c55e6914aca | -13.39925 | -54.38657 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0309ac3e-5019-3968-9c8d-860fc179153f | -14.10089 | -58.81247 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2dea828-f3a5-3611-a546-3800951dd514 | -13.93134 | -53.85622 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 429f4b77-f700-3d48-a4ed-ad855ca131a0 | -12.50696 | -54.75623 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c3e166a-e2ba-35f0-a289-0ce27c4ff558 | -12.49485 | -54.75878 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| baf8822a-984b-3e7b-9e42-2dcc53e2e51e | -14.03173 | -58.87122 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 32c81e8f-0595-37ed-89a5-0b9d9d279c5f | -12.51122 | -54.76978 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 608ebda0-b62a-32e8-bd33-8d5883e1b67e | -13.36919 | -54.3826 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ba1d862-354a-3a21-803c-b9453af6fae6 | -14.34503 | -51.89555 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6616d27b-e4f6-3bfe-802e-5ee2757543ad | -14.31044 | -51.88412 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1bd6ab6d-424a-30a8-8c3a-f6c1bace4794 | -13.93757 | -53.85728 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c7a117d-d5ef-38bd-a499-33cb67b26540 | -14.31613 | -51.899 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 00501f60-6990-34a2-8aeb-782f1e05dc8a | -13.9277 | -53.854 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1ff40f8-3b59-3f4a-98c2-1f6286d246bb | -13.40134 | -54.36863 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 675cc6cc-00f0-3a87-8d4b-3cb526eeeb60 | -13.38174 | -54.37965 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9b60c0a3-65bd-3cd4-abc3-13ff916122e7 | -14.32318 | -51.89997 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4f424ee6-cd03-3ff3-8761-e8aecd552f18 | -14.02332 | -58.86536 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01ce624c-40b3-3a98-807b-725fddc3646c | -14.10481 | -58.81781 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d262f506-3ca2-3f5d-9295-d8a3404f377b | -13.9308 | -53.86124 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 283e21e0-bf35-30d5-983b-70daf6a91ffe | -13.39873 | -54.39106 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccdeef87-4ced-3804-902d-09b75d21d692 | -13.39427 | -54.37688 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c4354267-418e-3b34-a603-f09dfba8ed24 | -19.72922 | -57.96944 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 434e9f51-d7c9-30b0-b776-8c07c49df4d3 | -19.74406 | -57.97781 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b59f446e-7ffa-393e-b53e-62059d5fd46c | -19.75923 | -57.98293 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 579016fe-358b-3f14-9cb8-e6c14e921a61 | -19.74889 | -57.98168 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| eb213645-9dbe-38cd-b1d3-e74de33329b1 | -19.72956 | -57.96619 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 63f85fa5-96f3-370d-a1eb-7ce9d5aab39a | -22.6232 | -54.99827 | 2026-08-21 05:46:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fe05e9c8-b555-3637-94da-b3f46697b01c | -19.72439 | -57.96556 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c9d2a2e2-accc-30ed-9cf9-d87e450354a3 | -19.7344 | -57.97005 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 36755b26-31cd-3918-a2f4-a304aa010ddd | -19.74923 | -57.97843 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b53542d9-d92f-3d07-a06c-cd6f3b657bc1 | -19.7361 | -57.95377 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| af5ff9b2-50eb-3fd7-a41c-d6a3a404553b | -19.73645 | -57.9505 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c312277a-ae62-3d26-9857-3f82c77d6ffb | -19.7544 | -57.97905 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 351cb82e-3d06-376d-87f3-3ca72ade3f51 | -19.73991 | -57.96743 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6a41b1f1-3d34-3fb7-b9b6-b5c4d6b55b80 | -19.72405 | -57.96881 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ff6bf7cf-dcd0-329b-b737-5e8a8ccac4a7 | -19.73372 | -57.97655 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 5f70aa3d-e958-34f3-a25c-fd48e5ea1c07 | -19.73406 | -57.97331 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 43244688-3a4b-34e5-880c-c70e209f8f49 | -19.73889 | -57.97718 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 41e7503a-cec6-3fb6-add4-00e9e430f85f | -19.75406 | -57.9823 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 30db9680-6069-3aff-87b0-20a99f150d42 | -19.72888 | -57.97269 | 2026-08-21 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 1d6d9764-8e05-3564-8a27-eadb96da3076 | -7.3791 | -45.8119 | 2026-08-21 05:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2862dfaf-a978-3a70-9d53-b8efe445aec2 | -9.4257 | -60.416 | 2026-08-21 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 4ecfb6e1-ba4a-3078-b05d-8a4ec269600c | -6.8755 | -59.4364 | 2026-08-21 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ab876282-641f-317b-b8d7-26dbfcc89987 | -9.4071 | -60.417 | 2026-08-21 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 269.1 |
| 2e963c1e-2b08-3be7-8cc3-124909d2e43a | -13.3923 | -54.3965 | 2026-08-21 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 0e1b19aa-e3c7-3031-b96d-2f4419ab1f77 | -13.3926 | -54.3758 | 2026-08-21 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 162.6 |
| d37696fd-1e87-3564-ab0e-c70a84f9424d | -9.4256 | -60.4353 | 2026-08-21 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 364a17ce-0147-3aba-ae08-bff1325ded75 | -6.2341 | -55.6109 | 2026-08-21 05:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 598e1c50-8128-3898-a767-3b1558d25d5c | -3.5406 | -48.1889 | 2026-08-21 05:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 4b2a1b5d-a79b-3fba-aa1f-cfe3677678ab | -13.3734 | -54.3779 | 2026-08-21 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e5001e02-882e-37aa-8262-85cc92fd7ace | -7.3603 | -45.8136 | 2026-08-21 05:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 83f6e953-f88a-3d66-96e2-bfca3115f016 | -9.4069 | -60.4362 | 2026-08-21 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 633da018-530a-32fa-ad33-a5f070dea750 | -9.4072 | -60.3977 | 2026-08-21 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2cf10994-6359-3885-b1c3-8c328f766fa0 | -11.1747 | -54.0216 | 2026-08-21 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1b0fa988-1c6d-37fa-989f-1e18e5254287 | -11.1747 | -54.0216 | 2026-08-21 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 64c4b90b-cc1d-308a-b0ca-2c3800ee73dd | -9.4257 | -60.416 | 2026-08-21 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| d5aa150b-41b1-3fb1-b26d-7f274b36965e | -13.3923 | -54.3965 | 2026-08-21 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e30999e9-ced6-3d48-8c24-07f7c2dadeeb | -9.4071 | -60.417 | 2026-08-21 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 288.8 |
| a8e70ea7-d7b3-3be0-9e58-c198208c13e2 | -9.4069 | -60.4362 | 2026-08-21 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 35597191-0e74-361e-8cda-118993adb541 | -13.3926 | -54.3758 | 2026-08-21 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| cac5924f-1830-37db-821f-97d5e6e484a6 | -7.3791 | -45.8119 | 2026-08-21 06:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4e9da3c2-3af6-33ec-8042-2649e403192a | -6.8755 | -59.4364 | 2026-08-21 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 76dab3bf-3b91-358e-83ef-14d4e599a788 | -13.3734 | -54.3779 | 2026-08-21 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |


[Clique aqui para ver as próximas entradas](README85.md)
