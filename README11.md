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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e91a6cd6-132f-3506-8d23-a929b5a009d9 | -8.5984 | -46.0549 | 2025-11-16 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| cffa5e6d-728a-3b04-89d2-94d884e18eb5 | -2.5238 | -47.8115 | 2025-11-16 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 06635901-f94f-371a-a419-4ea060f2ae67 | -3.3294 | -45.8487 | 2025-11-16 01:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e3845177-e9d9-3956-b4c7-50a327b63aac | -4.7027 | -46.3176 | 2025-11-16 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ef1b3afe-0309-32d9-852a-c7ada65c966f | -12.6672 | -47.167 | 2025-11-16 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| be1a2d2a-6bb7-3c69-94ee-2017dfc6d131 | -12.0195 | -49.2659 | 2025-11-16 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 93e847b9-d757-3518-89cc-4a744534871b | -4.4059 | -43.4049 | 2025-11-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b767dbca-3f3a-32da-8bab-32c836193e4a | -12.2047 | -49.6121 | 2025-11-16 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 68810690-4ee3-3933-8e80-656767a7e071 | -6.7013 | -40.7962 | 2025-11-16 01:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 0ff88ccd-3581-3098-ba82-cf50002f6f50 | -4.4246 | -43.4038 | 2025-11-16 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 51ad0f62-b608-3f1d-abde-0036f35c2492 | -2.5053 | -47.812 | 2025-11-16 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 86404cbe-69ef-3715-a35b-67e91758b02d | -9.7436 | -43.9542 | 2025-11-16 01:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 634ad05e-b00a-3022-b1b3-537a8640257a | -2.5423 | -47.811 | 2025-11-16 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 15b7ecdb-5558-3558-8e83-24632e33d600 | -2.8925 | -53.2842 | 2025-11-16 01:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fcdb7d08-421a-3788-ac7a-3c22ca5faecb | -10.0255 | -36.351 | 2025-11-16 01:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 78.1 |
| dd2f98b0-cbfe-334e-ad37-52d05cb0cc5f | -16.5637 | -47.6042 | 2025-11-16 01:00:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c119dda9-7fa6-3876-9c62-e76d48bbff19 | -10.0062 | -36.3544 | 2025-11-16 01:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 5f2fd63b-d6a5-329f-a903-249e9d901b12 | -4.7395 | -46.3821 | 2025-11-16 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3f65d9ca-9184-3a62-a49d-35c140d29c23 | -2.5238 | -47.8332 | 2025-11-16 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| f82de8c3-9d61-379a-9e60-21fcf8522128 | -8.5795 | -46.0568 | 2025-11-16 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d31953b9-5d9d-3a7c-9657-f70f7ea32b5a | -8.5798 | -46.0343 | 2025-11-16 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 1e07180a-012b-3234-8363-a9ed2222dabd | -12.0 | -49.2901 | 2025-11-16 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 8a0ce5de-3aaf-3019-b6ca-bc5b181ee6cd | -8.0513 | -43.1001 | 2025-11-16 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 85fcdcef-b124-37ab-9d1d-9ae70f8379ea | -2.8925 | -53.2842 | 2025-11-16 01:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| dfdd8e95-47ca-3762-b4c0-74e20bdd3e6b | -2.5053 | -47.812 | 2025-11-16 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4adaf455-54df-3012-9267-c797569cdcb3 | -9.7424 | -36.05 | 2025-11-16 01:10:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| cef435b0-b1c9-3310-94bc-b4453c1580bd | -12.0195 | -49.2659 | 2025-11-16 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c48ba3b0-b8fa-34b5-af24-2b860727d920 | -2.5238 | -47.8115 | 2025-11-16 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| e2e40c01-ace1-34ec-8fa5-3218eb03370b | -8.0513 | -43.1001 | 2025-11-16 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 5089496e-ca52-3030-8d58-f771617a0b51 | -4.7395 | -46.3821 | 2025-11-16 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d8afcae5-4486-3230-a7ae-51290689de66 | -4.4433 | -43.4027 | 2025-11-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5d76d496-9e4d-3ecd-8519-517d11d1cc5b | -1.9886 | -47.3465 | 2025-11-16 01:10:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fffd1704-1cbe-356c-bb6c-452c927244b5 | -8.5795 | -46.0568 | 2025-11-16 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 672b6686-25d4-323c-adbe-200cf143bcab | -4.4245 | -43.4271 | 2025-11-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 91312828-aaf5-39c6-9325-b61645066d63 | -12.0004 | -49.2683 | 2025-11-16 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 8bd585d0-cfca-3817-964f-06f875788ceb | -4.4059 | -43.4049 | 2025-11-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 269ecfea-b4c3-38bd-ae77-eae9789490d1 | -12.6864 | -47.1642 | 2025-11-16 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 40ffb3f5-f20c-3a6f-b912-ba431715a3d2 | -9.7436 | -43.9542 | 2025-11-16 01:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a3338f93-3ceb-392a-9a3c-850bc6fdd147 | -2.5423 | -47.811 | 2025-11-16 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 61db8687-08c1-3a8e-95ce-d60abc073d36 | -12.0 | -49.2901 | 2025-11-16 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| ce8b9fa5-e647-3b60-b35d-4a59df40455a | -4.4246 | -43.4038 | 2025-11-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 94a42b37-5b0d-3607-9a46-5002016fc513 | -8.0703 | -43.0981 | 2025-11-16 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.1 |
| 74bee42b-1cb4-3a44-b93f-d84ad9c92edd | -4.7027 | -46.3176 | 2025-11-16 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| afdedb63-9a88-3d7c-94f9-2b9d3a4fbacd | -12.6672 | -47.167 | 2025-11-16 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| bb2a3c89-f4b5-35c2-803f-4ffc8df9753c | -2.5238 | -47.8332 | 2025-11-16 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| fff79128-e2ef-3e9b-a707-788cc0fc2587 | -16.5637 | -47.6042 | 2025-11-16 01:10:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 68728dd0-f36f-3ebf-aaa4-b25d6abd82ad | -12.2047 | -49.6121 | 2025-11-16 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 9aff46db-9bfc-36f2-861b-9b15e0af172b | -12.0004 | -49.2683 | 2025-11-16 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 920f4f3b-b098-3d23-a09d-a18f8588a2f9 | -12.2047 | -49.6121 | 2025-11-16 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b79b9184-b9ef-386e-86e5-2ee3980eda08 | -2.5053 | -47.812 | 2025-11-16 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ec0e95fa-de97-3389-b7d6-3d7cfd52bb8d | -2.8925 | -53.2842 | 2025-11-16 01:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6110df16-51f0-34bc-8f78-7c0cf84cdec3 | -8.0703 | -43.0981 | 2025-11-16 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| f730e702-a464-3fc6-82e9-8db4cec1bbbd | -6.5631 | -51.1126 | 2025-11-16 01:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d74a181d-a939-3afa-a40f-714709624a9a | -12.6557 | -46.7407 | 2025-11-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| f0503bf9-43e1-3bd3-8887-ad1c845c0f62 | -8.0513 | -43.1001 | 2025-11-16 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| f555347e-2421-36dd-8327-20af116c1b7f | -8.3411 | -41.2486 | 2025-11-16 01:20:00 | GOES-19 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 8a78e71b-a0f1-3a91-8124-784cb6b3f0e5 | -16.5637 | -47.6042 | 2025-11-16 01:20:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| acc5fa40-02d6-3357-8b75-6c373a068bd2 | -4.7027 | -46.3176 | 2025-11-16 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ef4a9f4f-7023-3284-9430-f2dec460fe77 | -12.6672 | -47.167 | 2025-11-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5996e032-9fe4-3c24-9e7d-47f2b5d21641 | -2.5238 | -47.8115 | 2025-11-16 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 172.1 |
| a56476c5-e364-31a3-8755-4accd6b47600 | -2.5238 | -47.8332 | 2025-11-16 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| fb11fa55-3c64-33d1-ae27-5ce7131d376e | -8.5795 | -46.0568 | 2025-11-16 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| a6918ffc-ded7-351d-8688-9eeec3d77bb9 | -12.0 | -49.2901 | 2025-11-16 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9a700301-a894-3a90-ad6c-614ace043854 | -2.8925 | -53.2842 | 2025-11-16 01:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 86cbf080-6a12-3da9-8ff0-24ceeb1ee887 | -4.4246 | -43.4038 | 2025-11-16 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 9561ad0a-7ff0-3417-b741-b7d9d75e0e4d | -12.6672 | -47.167 | 2025-11-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1bdc68ed-ac26-30e0-b59e-0e3747c67363 | -8.0703 | -43.0981 | 2025-11-16 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.8 |
| dfdd4127-3f23-3e2a-b4d2-eecdb128f122 | -8.0513 | -43.1001 | 2025-11-16 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 5379cb22-67b1-3211-a62f-0c9907115caa | -2.5238 | -47.8115 | 2025-11-16 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 180.2 |
| 12b99630-9c8d-3eca-9ac2-dbb9febd076d | -2.5423 | -47.811 | 2025-11-16 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d1806ac5-fdf6-37f2-9663-d5cdfcdf645f | -8.3411 | -41.2486 | 2025-11-16 01:30:00 | GOES-19 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 57528da5-ec0f-3df8-be32-210431707411 | -4.7395 | -46.3821 | 2025-11-16 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d8c4f8fc-980f-3bde-95db-8f6cf0e753c3 | -2.5053 | -47.812 | 2025-11-16 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 44d5baf5-0946-3764-8636-7528e0392fd9 | -2.5238 | -47.8332 | 2025-11-16 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| cdcb8825-bcfe-39ec-a52d-0191baf0ce21 | -4.7027 | -46.3176 | 2025-11-16 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 697a35b4-df27-365f-8615-0369514761b4 | -12.0 | -49.2901 | 2025-11-16 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 45c510fd-ed52-3570-9206-c0547d55b56c | -5.3162 | -35.9204 | 2025-11-16 01:30:00 | GOES-19 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 9b79d02e-414d-3d68-b135-9a03c7c203c9 | -12.2047 | -49.6121 | 2025-11-16 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 62ca2a2d-f1ad-3acc-ba23-8e1b3d1588b4 | -5.3159 | -35.9473 | 2025-11-16 01:30:00 | GOES-19 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 93476d73-1cdb-3175-a5fa-ff4246d40ce7 | -8.1092 | -46.0363 | 2025-11-16 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 34f9493e-383a-33cf-b668-fc6657c23672 | -12.0004 | -49.2683 | 2025-11-16 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| b6c4e5d3-b9d8-324d-92c6-6086321780e8 | -11.9996 | -49.244099 | 2025-11-16 01:34:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81e1d16f-1a3e-32ba-a08e-8a5ae73ee91e | -12.1978 | -49.627201 | 2025-11-16 01:34:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cc052e3-fdca-3681-9876-e45f3979cbf9 | -12.2073 | -49.6245 | 2025-11-16 01:34:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06eb5056-bd4a-3a5a-b402-12d20c40d822 | -12.0066 | -49.306702 | 2025-11-16 01:34:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3db74873-f37a-3db9-ac0b-b1b18ffabdf2 | -11.9983 | -49.276798 | 2025-11-16 01:34:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9784f279-9189-3b75-8450-e9b686725acf | -10.6628 | -49.358002 | 2025-11-16 01:34:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f700e3d4-606d-3f3b-a2b9-89c5bfe9729f | -6.5676 | -51.119598 | 2025-11-16 01:34:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 452d67ee-480b-3c47-94e0-0a977a65c1f2 | -12.0161 | -49.304001 | 2025-11-16 01:34:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aaca1a63-1703-35ed-a3ad-df0cb53db414 | -12.1901 | -49.598999 | 2025-11-16 01:34:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35c850a0-6730-3b1f-a768-190f6cc75acc | -11.7071 | -48.856499 | 2025-11-16 01:34:00 | METOP-C | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af8f1d91-6415-33be-842f-2fdd1276f939 | -12.0607 | -48.207401 | 2025-11-16 01:34:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad55308c-8c1d-3d29-a7f9-6210155d0d9e | -16.564501 | -47.602501 | 2025-11-16 01:34:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64c04577-33d8-37d1-98f0-a26150190c50 | -6.5772 | -51.1171 | 2025-11-16 01:34:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3048a3-be8a-33f7-85a9-fbce350b4f3c | -11.9901 | -49.246799 | 2025-11-16 01:34:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b21458e2-f23f-3ea2-bd65-f380d9f86326 | -12.1996 | -49.596298 | 2025-11-16 01:34:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0155b22-c220-3966-a0a0-83b75ffb83cb | -12.0078 | -49.274101 | 2025-11-16 01:34:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edaddca9-55db-3611-903f-480fb3638969 | -2.8963 | -53.284199 | 2025-11-16 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa6cbed-a785-3150-97b3-bb09234ebed6 | -2.8866 | -53.286499 | 2025-11-16 01:36:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b3f3b3-8a14-3f8b-a6f8-4bb49c71ed17 | -2.5238 | -47.8115 | 2025-11-16 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |


[Clique aqui para ver as próximas entradas](README12.md)
