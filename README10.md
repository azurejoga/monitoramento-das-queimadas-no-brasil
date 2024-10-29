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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de70c83-1b3e-31d8-9af8-e610a090dcfb | -2.9967 | -49.528702 | 2024-10-29 00:28:46 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 311cc1f5-120a-314f-89b4-d66b5126318f | -3.183 | -50.358501 | 2024-10-29 00:28:46 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae719e37-e762-3df3-84ca-af62f43361f0 | -3.1858 | -50.3713 | 2024-10-29 00:28:46 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d637819e-81bd-34e4-a6c2-04f37c3e7f25 | -3.1887 | -50.384201 | 2024-10-29 00:28:46 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8d6cfd3-b8d0-3e61-87ee-6ca47b37ec2b | -2.6172 | -47.939201 | 2024-10-29 00:28:47 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb328946-0867-3341-a69b-e3ac263ae58d | -2.5154 | -47.445099 | 2024-10-29 00:28:47 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0526d971-6924-36d9-a0f2-6ea6c208ebef | -2.625 | -47.928101 | 2024-10-29 00:28:47 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b279d2d-1ef8-380c-9b2e-df647163417f | -2.627 | -47.937 | 2024-10-29 00:28:47 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a304822-8482-3427-9c1d-fb545d76ee59 | -3.176 | -50.373402 | 2024-10-29 00:28:47 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7ab1bbe-3950-34c2-89b4-5f63967189d9 | -3.1789 | -50.386299 | 2024-10-29 00:28:47 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d92aa7-4c9f-3443-a52a-1c84d051dece | -2.6152 | -47.930302 | 2024-10-29 00:28:47 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa1ce2e-a72c-37ab-9332-15137d245050 | -3.2404 | -50.706902 | 2024-10-29 00:28:47 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1285976a-0666-3eb1-917f-b6f194256f69 | -3.2435 | -50.720501 | 2024-10-29 00:28:47 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 912d31ba-2932-3889-9a20-a87f045d1279 | -2.3158 | -46.6576 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23e95203-aa93-3c4d-9849-32e805679851 | -2.3175 | -46.665298 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbdb6b8e-61af-3da3-b5e2-976edebaa8f0 | -2.3193 | -46.673 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 010fe6d2-149b-38e4-ab67-c9824eae8f38 | -2.321 | -46.680599 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a6c635-7ffa-385c-a85a-8fb0ba9be0be | -2.306 | -46.659801 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6296c450-f425-3a85-ae2d-b501e6500334 | -2.3077 | -46.6675 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2469b335-a54b-3d37-a3e6-3384b4c2e1bd | -2.7696 | -48.7038 | 2024-10-29 00:28:47 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff0a53f-c9ca-309b-892b-041a1f3a4152 | -2.2927 | -46.646599 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3764b6eb-af66-3108-aec8-8823a4a72867 | -2.2945 | -46.654301 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6be09e83-0150-3656-91a6-0c7ea4bd975e | -2.8785 | -49.231701 | 2024-10-29 00:28:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c01bc2b3-632d-3990-aafa-e866423af90c | -3.2767 | -51.006302 | 2024-10-29 00:28:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10cc7c1e-43c4-31b2-a503-ce02a2b87ec6 | -2.2812 | -46.641102 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd90656d-d452-3c42-b9dd-b46d4873e918 | -2.2829 | -46.6488 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0b60704-8d33-317c-accf-34286270a4f6 | -2.3039 | -46.7411 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b29754fc-f9c1-3d29-9a09-775a1aab8fb4 | -2.3057 | -46.748798 | 2024-10-29 00:28:47 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c93bc800-1414-3fbb-a607-9451f9e7ce8e | -3.1713 | -50.580601 | 2024-10-29 00:28:47 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebcd6fdd-ddeb-314e-b8fb-2cb4f31c090e | -3.2637 | -50.994099 | 2024-10-29 00:28:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d06eec0-09fd-3ae7-8427-87e91033864b | -3.2669 | -51.0084 | 2024-10-29 00:28:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e72c93-a14c-36f5-932e-7cd1c5d362c8 | -2.2959 | -46.750999 | 2024-10-29 00:28:48 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0d4062-5153-3d38-ae54-ba76150cd331 | -2.2976 | -46.758801 | 2024-10-29 00:28:48 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9c0d24-5d1c-3547-81f5-3115099c984f | -3.1585 | -50.569401 | 2024-10-29 00:28:48 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a9d954-7ede-3438-82bb-e71c9037d141 | -3.1615 | -50.582699 | 2024-10-29 00:28:48 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 917d732e-3984-34e6-b2e0-7f9adf695523 | -2.2763 | -46.755402 | 2024-10-29 00:28:48 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c78aa6f5-2755-3167-a5a9-02127fe3fc00 | -2.278 | -46.7631 | 2024-10-29 00:28:48 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8074483-af35-3d4e-8b70-415fa1168b32 | -2.6041 | -48.198799 | 2024-10-29 00:28:48 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 906df0f3-8519-30d0-8e0b-8fa870e978b3 | -2.8345 | -49.2188 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f77a74f4-8ec8-3a8d-bfcd-c8fbe05cf109 | -2.837 | -49.2295 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0615217-c491-3ac0-b6fa-8586df0b26bd | -2.1988 | -46.460201 | 2024-10-29 00:28:48 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b144b82b-5a86-3710-90a0-639ed6b6e7c9 | -2.2718 | -46.7808 | 2024-10-29 00:28:48 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8528d1cd-061b-3b52-b2e5-9b1a11018f03 | -2.2735 | -46.788502 | 2024-10-29 00:28:48 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e747a490-2b3b-3342-b04a-e1943ecf617e | -2.8199 | -49.1996 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e65bc62f-a00a-3aab-be19-c52f6e86a5a1 | -2.8223 | -49.2103 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dea4c60-d58a-3242-9ccf-7dae117a189f | -2.8247 | -49.221001 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04716f50-7561-3f55-9bc2-dcc1586f2f6a | -2.8272 | -49.231701 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55e50b82-1eaf-345f-94d5-ded643e0eb5c | -2.6203 | -48.361401 | 2024-10-29 00:28:48 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4f997f-12d1-3fff-a1fe-65a767fc6521 | -2.8101 | -49.201698 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d23e31ee-2e86-3dc7-ae51-60445d31e903 | -2.8125 | -49.212399 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 760dfe14-a28d-3b8f-8966-e51d43cd45d4 | -2.8149 | -49.223099 | 2024-10-29 00:28:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c56616-9af9-33d7-bfcd-c396a8e435f5 | -2.1945 | -46.532398 | 2024-10-29 00:28:48 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3a0f15-4062-3abe-9e53-48fefab6f3da | -2.1963 | -46.540001 | 2024-10-29 00:28:48 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 241b16ac-2ba7-3ddb-9ea8-897ca6f64550 | -2.198 | -46.5476 | 2024-10-29 00:28:48 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c093a768-6250-3bbb-82f3-398764a4f609 | -2.2423 | -46.7873 | 2024-10-29 00:28:49 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 027653db-6b92-3cf6-a6c2-a0e307873678 | -3.0589 | -50.3988 | 2024-10-29 00:28:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7338889b-49c6-38c6-9954-09630322b81e | -3.0463 | -50.388199 | 2024-10-29 00:28:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 951c6836-6b76-3605-8bbb-fdd667f7301e | -3.0491 | -50.401001 | 2024-10-29 00:28:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71ffa74c-3f72-305b-840f-0c585abfd568 | -3.052 | -50.413898 | 2024-10-29 00:28:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 490d825e-535d-352d-97e3-e0a5c3296f61 | -2.1156 | -46.321701 | 2024-10-29 00:28:49 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76eca9f8-b7c4-3b46-a7f4-1b14941604c8 | -2.5225 | -48.111099 | 2024-10-29 00:28:49 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a394418d-43e0-3001-a2aa-2ddfe0c980db | -2.5245 | -48.120201 | 2024-10-29 00:28:49 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 630b30aa-a42c-3f6a-bf73-c94138ba5cec | -3.0393 | -50.403099 | 2024-10-29 00:28:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88be9d0-0b5b-34bf-9938-39f3d18e1a7a | -2.5004 | -48.058998 | 2024-10-29 00:28:49 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8efa18ed-24d2-3a43-9e7b-dc6bdf308ea5 | -3.1953 | -51.145 | 2024-10-29 00:28:49 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| debfd6b0-d49a-332d-b3d0-ec18db531d6e | -2.4048 | -47.682999 | 2024-10-29 00:28:49 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17e1df7-2b72-3e8e-b803-31f4dec3a45a | -2.7111 | -49.0359 | 2024-10-29 00:28:49 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0d003df-f40a-3d05-8c5f-742d3f736390 | -2.7135 | -49.0462 | 2024-10-29 00:28:49 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9fb5300-7a3d-3200-8c45-0c3cd596591c | -3.1855 | -51.147099 | 2024-10-29 00:28:49 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b9840d1-401e-3f8c-a787-9889bca6a73d | -2.3794 | -47.661598 | 2024-10-29 00:28:50 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5453ae1a-ec12-31be-9049-06daa2fa736a | -2.7488 | -49.2939 | 2024-10-29 00:28:50 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7bfbfb8-889c-3799-8508-e8f0a7793b67 | -2.7512 | -49.304699 | 2024-10-29 00:28:50 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9812697-5437-3785-9ef3-e7ef2da1d5d2 | -2.0845 | -46.501301 | 2024-10-29 00:28:50 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 678ccfc2-79ed-31e7-bdd7-2a8911bbfded | -2.0862 | -46.508801 | 2024-10-29 00:28:50 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc7b7e74-87d5-3c61-94b9-a8eb28ba55b7 | -2.9798 | -50.456799 | 2024-10-29 00:28:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6190f0-2984-3765-b902-1e6f54945e5b | -2.9827 | -50.469799 | 2024-10-29 00:28:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa3216fc-8336-35f6-bea9-2e7d8cf3a5d3 | -2.6877 | -49.341301 | 2024-10-29 00:28:51 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26c0a286-a9e7-32f1-91a6-855143c092c4 | -2.4612 | -48.475899 | 2024-10-29 00:28:51 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3407943e-3f76-3542-9a49-05bc2e5318a6 | -2.6657 | -49.380299 | 2024-10-29 00:28:51 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff6536af-84a4-3140-8ba9-dd111c2bf9eb | -2.6681 | -49.391201 | 2024-10-29 00:28:51 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9ac33f0-034d-30ff-98c0-f71d7603d204 | -1.9855 | -46.428699 | 2024-10-29 00:28:51 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6341c9ae-4783-3ab3-8859-4acd288fdb6e | -1.9872 | -46.436199 | 2024-10-29 00:28:51 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5edd8d-d3ac-3245-90de-c5b9f5afe8c8 | -1.9889 | -46.443699 | 2024-10-29 00:28:51 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f0d99d5-ef8c-3e35-9c6a-a956bd23b539 | -2.4557 | -48.4972 | 2024-10-29 00:28:51 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b817b3-9515-3f08-9610-cb68a9e7de06 | -2.6001 | -49.180901 | 2024-10-29 00:28:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 410ce669-488d-30bb-a4ab-e0daec198787 | -2.4111 | -48.527 | 2024-10-29 00:28:52 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd49a63-19b4-3166-b6ce-e1867ba7d0ff | -2.4133 | -48.536499 | 2024-10-29 00:28:52 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36d4f33e-60f0-3fbe-a357-2149fd240b67 | -2.4155 | -48.546101 | 2024-10-29 00:28:52 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5f3cf3-1199-3214-b694-895953220225 | -2.4396 | -48.6525 | 2024-10-29 00:28:52 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca9de8a3-b2e0-3c04-891a-714ff73fdf51 | -2.4035 | -48.5387 | 2024-10-29 00:28:52 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1ffa239-9143-3284-b10c-315274abe39e | -2.4057 | -48.548302 | 2024-10-29 00:28:52 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 362bce66-031b-3e43-bf53-3ae5c28f386b | -2.5108 | -49.058102 | 2024-10-29 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8e72fd-d794-37e1-bd16-ead2e39c4e65 | -2.501 | -49.0602 | 2024-10-29 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b0b76b-bdac-3d94-8bb5-3c5881c50455 | -1.9182 | -46.585701 | 2024-10-29 00:28:53 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3018e2c7-e5c7-3225-9f3a-fc5b2c8dc55c | -1.9199 | -46.5933 | 2024-10-29 00:28:53 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d86d09-53c8-32e5-a952-d966341e8ce0 | -1.9217 | -46.6008 | 2024-10-29 00:28:53 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cdb7aa8-fdae-3783-bf1a-e7c5d6ad0d24 | -2.4791 | -49.0541 | 2024-10-29 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c63678c2-be39-31a3-9323-0ea6fa9078ab | -2.4815 | -49.064499 | 2024-10-29 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49deda08-9d08-3b58-80b5-3879856738a8 | -2.4502 | -49.0173 | 2024-10-29 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 943d95fd-3b67-39ed-aaea-2383734fe020 | -2.4525 | -49.0275 | 2024-10-29 00:28:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
