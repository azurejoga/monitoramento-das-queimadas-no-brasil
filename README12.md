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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97e7991f-d836-3522-830c-2dd4ffe3314d | -10.14132 | -52.13958 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e098d03-372a-3b8e-bb3f-0a2e56fad389 | -13.88624 | -54.6797 | 2025-06-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2aa6357-2bd4-329d-b5bf-f2cf9cd59fa7 | -9.95865 | -64.96926 | 2025-06-06 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dfc011a-86bd-3e7c-9893-251caf1a3b85 | -10.69431 | -57.64733 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65f8a7b7-14c4-37d1-ae30-c78bfdbea363 | -9.22433 | -48.86181 | 2025-06-06 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d238911-2ee8-3648-83d1-8a9e4fc640c9 | -11.7971 | -55.43587 | 2025-06-06 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7982bc6f-7d09-31e1-a4dc-3c6060ae00b4 | -10.29988 | -58.43848 | 2025-06-06 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83a97b3f-fad7-360f-9d6a-303f66d9c1e7 | -11.3847 | -56.54816 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 662f473a-1641-30a8-86f7-6b4873fbeb3f | -12.95861 | -46.7732 | 2025-06-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78bcab7c-69c8-3a00-a32f-ab22a0b1c496 | -11.5348 | -56.45709 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e468f1e1-fb98-3121-86bc-af591fc2a34e | -11.54473 | -56.43701 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cc10ad3-5a5c-336b-93e6-91b01d5e3576 | -12.67188 | -58.2181 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca7a6875-6d8f-3ae6-8de9-cb8b988e3d6e | -11.94365 | -62.84402 | 2025-06-06 05:04:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e89ea18c-0055-3ec9-b264-4b46f7cdd16c | -15.00904 | -56.06109 | 2025-06-06 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7354658-2979-3c58-a9c7-c69f008beda5 | -10.68619 | -57.59138 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 523f369a-5f7a-3659-b801-ca5fb3033514 | -13.08053 | -49.24172 | 2025-06-06 05:04:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a515ef9-9ebf-3239-b4f4-721f0f6a5546 | -13.51118 | -56.56106 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e526137-4cdf-3d94-a7fd-a5839543d8e6 | -11.65177 | -58.26105 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d4a8e30-409b-3f1e-ba2e-600037c7ffa0 | -11.92116 | -54.82412 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 74763189-0a50-33b9-a5f9-73942d7d9d6d | -15.00961 | -56.05728 | 2025-06-06 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdda2370-7177-391d-9fa4-c32420065cc9 | -12.6652 | -58.21697 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a0d4c29-a344-3dc3-8a38-4a32ba79597c | -9.80517 | -54.72595 | 2025-06-06 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98ce441d-e368-371b-9ada-084a099eab17 | -10.70154 | -57.64489 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1018b5b-d5cd-3b6d-b90b-47fd38c877ac | -12.15916 | -43.20979 | 2025-06-06 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d23aa45-84d2-350e-aad9-515994234ced | -9.39231 | -48.42489 | 2025-06-06 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 502a0bd0-f5f9-3d6a-a16c-36b4d03a8dc3 | -10.69821 | -57.64433 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccfab634-ad75-38ba-b626-9801025f5163 | -10.45942 | -47.95112 | 2025-06-06 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 57fbe64e-158d-3b43-aa3c-3a9731dc7b8c | -10.81745 | -56.95971 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec5f1a12-a86e-3e96-b6bb-b115a3aa3c45 | -11.37514 | -54.3502 | 2025-06-06 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e751edbe-2f62-3c12-8d42-07863748d962 | -12.28936 | -50.10917 | 2025-06-06 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ebd1eff-ee79-33db-8e15-c57e3c4214d9 | -11.29545 | -53.98601 | 2025-06-06 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0aaf20f-c7d1-30f2-bce6-440f9aedb15a | -10.07475 | -52.7526 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 597474c0-00a8-3318-84b2-28f93be9fbae | -9.24523 | -63.28694 | 2025-06-06 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56dde8b2-2c45-398f-9854-b1e29d94d2a0 | -11.78916 | -54.7697 | 2025-06-06 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0116aee5-f0e0-3f46-8e04-3f7f5f31ffab | -10.30326 | -57.13869 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5abac1c9-3439-3ea8-9dd1-7dec2cf02be9 | -13.51784 | -56.56214 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45d92e68-109a-3570-9c39-76f29de06ec9 | -10.81414 | -56.95918 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d8bc9ab-f72e-34f4-bb8a-6a36a87254d1 | -10.6823 | -57.59438 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1f004f9-9055-3e7e-9e02-26860f6472c4 | -13.07422 | -49.25219 | 2025-06-06 05:04:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08b03690-8e52-34cb-8d72-26798051951c | -11.53149 | -56.45655 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a72b2dfd-cc4d-3ded-a3f5-d1a210a8e3e4 | -11.71529 | -56.45304 | 2025-06-06 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cc1083c-0e15-36d7-8aec-82223f8ecff3 | -10.6904 | -57.65033 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccabf018-e9d3-311e-aaff-0081d936b84a | -11.92173 | -54.82028 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 06dc2e36-c79e-3aad-8d11-bdadb16a4ea9 | -14.23152 | -45.48801 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e79add86-e2df-3db2-b81a-63354c1594b4 | -10.69764 | -57.64788 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c02d2d38-6d66-315a-9e06-d448ef870423 | -12.66854 | -58.21753 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fda193d-2bbd-3832-aba8-2d486e09feba | -10.49053 | -53.65836 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 960d99c0-98af-321b-b672-b2b8267a432d | -13.5195 | -56.57343 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63d9529b-aa41-3057-9f09-aeff5e7adc72 | -11.53259 | -56.44951 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d80ee646-d500-3e24-9c57-373b2d2ecc8a | -12.66244 | -58.21281 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89103c21-38bd-3526-a455-4beae460c5d9 | -10.49471 | -53.65478 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8b27958f-93c2-3a8a-b473-a58696c89ef1 | -13.51895 | -56.57701 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d9ef8a2-7514-3db6-b199-2910a0dfa380 | -13.52283 | -56.57397 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4de8c2fe-dd58-3b40-afcd-ab823ed31f0e | -10.07542 | -52.74807 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5241836-f24a-33a6-9888-2669eecac2fa | -11.0752 | -54.77369 | 2025-06-06 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51c4bae3-0706-3721-a9be-d1f3ffbbf379 | -11.13888 | -53.94233 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3ecefd2-2717-3ed1-b1bd-e6930349b08c | -13.88685 | -54.67557 | 2025-06-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e1c8c0b-1d6b-3fda-81aa-953cb2c48024 | -9.24649 | -63.28533 | 2025-06-06 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d303f311-8d0f-3add-95bc-78ab11182bc6 | -9.24565 | -63.28995 | 2025-06-06 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 178e8a36-571f-3b8b-9126-9edc1dfdc430 | -10.29331 | -57.13709 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cf4f86b-da39-3cc1-a3b1-f0106e1aeb5c | -11.54805 | -56.43754 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c7c3c7b-fe4f-3124-bb8c-502ddccf67e6 | -12.2644 | -55.07462 | 2025-06-06 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7c96970-5b78-3aac-98e0-1e47d7dc14b7 | -9.6076 | -49.02071 | 2025-06-06 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 819c6601-fce9-3b75-98d8-83775d2a1f37 | -10.49709 | -53.66363 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abac0a9c-930b-3334-a23a-c3836dbf32cd | -11.38138 | -56.54763 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d780aac-60c5-343d-9408-56c2e37572a1 | -8.4734 | -49.60701 | 2025-06-06 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a4ce13c-295a-39ee-b384-e79814848a03 | -10.3027 | -57.1422 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de51f81a-6769-398c-9cff-cae780306889 | -10.29276 | -57.14059 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c6080ab-2a91-3f4c-ae95-c25d8895a93e | -13.52117 | -56.56268 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c845aa7-b1f0-39ed-9f07-43dd737972ba | -14.02474 | -55.13651 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba342fe1-0f7f-307f-afcb-3fe1a1a3a938 | -13.51673 | -56.56931 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fd73af7-97e8-354a-961f-158df78dc9c6 | -14.02939 | -55.12916 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ae74914-b0aa-3f59-86a6-669ca262b148 | -13.52173 | -56.55909 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68e489c5-f7f1-3f5d-8fea-01b06244319f | -9.52494 | -54.77131 | 2025-06-06 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23c09339-40ef-381d-b2fa-110c7c2c2a04 | -9.81253 | -63.36243 | 2025-06-06 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af8ac609-b15e-38a1-9b66-8824cf9bd60f | -9.66946 | -48.71352 | 2025-06-06 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfe36252-716f-3a61-94c3-462c0ceeae8d | -9.26809 | -56.29553 | 2025-06-06 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfbdfa4c-c968-36e6-8765-6a48b8397a87 | -11.70866 | -56.45197 | 2025-06-06 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| add87e43-71a1-3aad-966c-1447826c54a8 | -11.41073 | -56.72864 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b8675f6-9e00-3197-9562-fdb880dd3918 | -10.86732 | -57.66874 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14cb1ddf-b7d4-359e-b407-ffd7294e7240 | -10.69878 | -57.64077 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a12335-5594-35f8-a557-6aa9b7c4bda7 | -10.68287 | -57.59083 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b19cd69-cc81-33c6-89af-e6c061ee2d96 | -12.52361 | -58.3566 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8e207f1-0787-3d42-8641-dde81d843d5f | -11.71198 | -56.4525 | 2025-06-06 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18e22bcb-bee1-3e13-ac07-ebb70ffbf680 | -15.07579 | -48.94384 | 2025-06-06 05:04:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 340f13ab-a430-314b-92cb-17397471c85d | -13.71353 | -57.48206 | 2025-06-06 05:04:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a756eef9-8185-3f09-989e-89e064b5a7a4 | -11.53423 | -56.43894 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713b23ef-18a3-31a0-a03f-a2b35cdca164 | -10.29994 | -57.13815 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55f66aad-7d34-359f-a8a5-62f5f99e39c8 | -12.83639 | -47.3852 | 2025-06-06 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7203030-65b1-368b-9118-aa404f19b06f | -11.38415 | -56.55167 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3dd50ae-07e7-339f-97c6-d669b9325a13 | -12.53091 | -58.35408 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5813605a-05b6-3cf9-8a55-396946ce94cb | -14.73533 | -45.09496 | 2025-06-06 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5c6ea64-b49f-3131-b902-1142a931f6f7 | -10.67327 | -57.62925 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d01936-51c0-3e87-b7f0-8bc1d1771a5f | -10.49769 | -53.65948 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 821024af-5716-339d-ae21-0d3b7ad8fb1d | -10.94479 | -55.33212 | 2025-06-06 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d820d3f5-ee50-3154-8281-96b92c97b45f | -11.92577 | -54.81697 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2ff00d47-4000-3221-b336-4f0c9c624299 | -11.71252 | -56.44897 | 2025-06-06 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67de18af-9fde-3979-bfc4-b96370bc2ef6 | -11.13829 | -53.9464 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84771386-e2f8-3c99-ac8a-c5f560b261e3 | -10.80487 | -55.8701 | 2025-06-06 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9fa49e0-c38a-3cac-b04f-01c82a9140c6 | -10.94423 | -55.33577 | 2025-06-06 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
