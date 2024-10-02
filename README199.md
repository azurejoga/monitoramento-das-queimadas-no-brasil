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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d0b8028-5b65-3dea-bf3f-0906b58cdc9e | -15.5486 | -56.8873 | 2024-10-02 07:26:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 2bbf6554-1714-3e19-9399-2b26c561cdeb | -16.578 | -58.2183 | 2024-10-02 07:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| af10f600-cdb3-3440-8f8d-090d9cd882d2 | -16.5973 | -58.2365 | 2024-10-02 07:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 416.2 |
| 30a9f0bf-fbd2-3de3-9e0a-0b33c0f01b26 | -16.5976 | -58.2162 | 2024-10-02 07:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 352.8 |
| 4fa6711b-7d46-3801-b4c1-2884bcab5137 | -16.6168 | -58.2343 | 2024-10-02 07:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.6 |
| 7d69a2c3-b323-3dd5-ad13-7a706f38f113 | -16.6171 | -58.214 | 2024-10-02 07:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.5 |
| 252f35ae-776f-35e3-90d3-173a93d8ef32 | -16.5778 | -58.2386 | 2024-10-02 07:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.3 |
| b08515bf-05a9-3759-b4fc-a03b34ead202 | -16.8695 | -55.848 | 2024-10-02 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 151.4 |
| 07ceb611-a63f-3803-93a4-b69e3c9c97f3 | -16.8295 | -55.8945 | 2024-10-02 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| f7ae4c8a-1f3c-344f-818d-e76238c4afc8 | -16.8292 | -55.9152 | 2024-10-02 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| ca312166-fbbe-3209-ad77-9d38c29d2549 | -16.9179 | -57.6926 | 2024-10-02 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 91587a07-8333-306a-a36c-a6fd7338c6e2 | -16.9176 | -57.7131 | 2024-10-02 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 5fa7a011-d862-35bd-b93e-0c91a7edd8f0 | -16.8986 | -57.6744 | 2024-10-02 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| cd345744-be6b-31a8-9203-04fef82a030c | -16.898 | -57.7153 | 2024-10-02 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 6c706ba6-0170-3c50-ac5e-db38ec2f48e7 | -16.8983 | -57.6949 | 2024-10-02 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 133.1 |
| 576d38be-57ed-33a9-b319-d673bd0de47f | -16.8698 | -55.8272 | 2024-10-02 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 2cdaf5b0-5576-3727-884a-e297677e59c0 | -16.8787 | -57.6971 | 2024-10-02 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 96340d9d-ba81-35d2-9584-d150faeb3f21 | -16.8894 | -55.8247 | 2024-10-02 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.9 |
| a390dd91-0f4f-37b2-b67a-9d8d4da942d5 | -16.8891 | -55.8455 | 2024-10-02 07:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 206.7 |
| 36ef0e94-72e8-37f7-a187-60995253e9ba | -17.1088 | -56.7685 | 2024-10-02 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| faa0f874-92f4-3eac-865a-9fb768d63169 | -17.0895 | -56.7503 | 2024-10-02 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| d9487dd5-ed7b-3e57-b9e3-0525315f7e3b | -17.0892 | -56.7709 | 2024-10-02 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 019aba79-9186-3fab-bf7f-00db93399ea8 | -17.1288 | -56.7455 | 2024-10-02 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 3ac48aeb-19a6-3c4d-99e7-fb8bdff66fb5 | -17.1091 | -56.7479 | 2024-10-02 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| 0f80d4ac-16c5-3065-ac3c-ede502b87519 | -22.3929 | -49.2727 | 2024-10-02 07:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| fae724b7-cb6a-39ed-b93b-4118b9cc79a0 | -22.3922 | -49.2961 | 2024-10-02 07:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.2 |
| 40d44c7c-eb63-3e2a-a407-f79946d792fc | -22.372 | -49.2777 | 2024-10-02 07:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.9 |
| 0ba50226-2401-3365-9416-9c816d706157 | -22.3713 | -49.3011 | 2024-10-02 07:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.9 |
| d086994f-e8e3-3167-80d8-fe7b67eb794c | -12.6484 | -63.1214 | 2024-10-02 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ac6ae714-13d0-3b00-be08-4c232e32f869 | -13.1125 | -51.4115 | 2024-10-02 07:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5bf75746-b6d1-3a92-8c18-4742ca475e79 | -13.1348 | -51.2169 | 2024-10-02 07:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 8bb92768-3b8d-3a53-b8a8-030c77b25623 | -13.1351 | -51.1955 | 2024-10-02 07:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6491b55d-3ea7-3583-8e08-348d1faf5c95 | -13.154 | -51.2145 | 2024-10-02 07:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 4e127f64-edc1-3f8d-880c-de56beed5055 | -16.5778 | -58.2386 | 2024-10-02 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 172.3 |
| 08b68802-596b-334c-b46a-d909e4d8fea4 | -16.578 | -58.2183 | 2024-10-02 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 60bc270f-7a1a-3516-964c-7c9a078a9f4d | -16.5973 | -58.2365 | 2024-10-02 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 408.4 |
| 16191bb1-b52b-33f5-a465-879dc092017d | -16.5976 | -58.2162 | 2024-10-02 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 314.6 |
| b5e0aafc-e422-3ce4-b585-403ccf2b9100 | -16.6168 | -58.2343 | 2024-10-02 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.1 |
| a7a6565b-e144-37b6-a376-2e73d959b83b | -16.6171 | -58.214 | 2024-10-02 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| e09a75e6-d687-3ff8-8db1-d953b7e6a8dd | -16.7452 | -57.4878 | 2024-10-02 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| f0866f38-2919-3576-9df6-6d6fdbb11d71 | -16.8698 | -55.8272 | 2024-10-02 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| d28e3657-82ca-35b2-8c2e-3698db0d1841 | -16.8891 | -55.8455 | 2024-10-02 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 174.0 |
| 10d48a56-203f-33a3-a569-43338e7f5383 | -16.8894 | -55.8247 | 2024-10-02 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 85a5d50c-4986-3bdd-b69e-8b210c08548b | -16.8983 | -57.6949 | 2024-10-02 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| a7b34c38-0bf3-3cc9-9f6f-9b90ae2247c7 | -16.8292 | -55.9152 | 2024-10-02 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| dbdadb08-20b7-3397-a2b3-2a3045d0b8f0 | -16.8295 | -55.8945 | 2024-10-02 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 4dc4ed95-7c2a-351d-9260-dca010c8eb99 | -16.8695 | -55.848 | 2024-10-02 07:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 132.4 |
| 8076905b-0b68-3259-a17f-c53470961215 | -17.0892 | -56.7709 | 2024-10-02 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| bfa94632-ccb0-3547-85b0-9957742461ff | -17.0895 | -56.7503 | 2024-10-02 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| dcede97c-6f54-35f0-9d32-cf6826d87aff | -17.1088 | -56.7685 | 2024-10-02 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.0 |
| 86fc440c-e1c5-3ad5-9c03-32585b646efa | -17.1091 | -56.7479 | 2024-10-02 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 0f60e371-f03a-3e2e-b655-e588349ad80b | -21.3661 | -55.6807 | 2024-10-02 07:37:05 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 35.1 |
| a65be450-3a53-3c91-8ea2-324c1dc5ef27 | -22.3713 | -49.3011 | 2024-10-02 07:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| 3eeca6ed-3d10-3b82-9512-69f8affe061b | -22.372 | -49.2777 | 2024-10-02 07:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 57ca56a9-886e-336c-ad22-d5fabcaa2981 | -22.3922 | -49.2961 | 2024-10-02 07:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.2 |
| 401098ef-25e4-3921-9237-70e9d7a6cf09 | -11.2565 | -60.6019 | 2024-10-02 07:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e1a4f10b-1afa-3d15-82c7-eb601452e552 | -12.6484 | -63.1214 | 2024-10-02 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| eed0aac3-1879-38a0-b635-99fdcf433834 | -13.1348 | -51.2169 | 2024-10-02 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c68c35e8-68d9-3671-b34a-dd6a8f7f9a21 | -13.1351 | -51.1955 | 2024-10-02 07:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d30e7070-0133-3735-ad31-130672c4e123 | -15.748 | -49.9586 | 2024-10-02 07:46:34 | GOES-16 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| dc1c5b01-3d24-3516-b2d0-0b495fb47b2e | -15.7484 | -49.9365 | 2024-10-02 07:46:34 | GOES-16 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b4c13fc1-e1a4-3b40-8da9-b90a66f7b027 | -15.9003 | -50.1537 | 2024-10-02 07:46:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 918676cc-07c1-3004-aad0-6446d5e2f427 | -16.5778 | -58.2386 | 2024-10-02 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.6 |
| 7ef97779-a918-3fa9-844e-9601028c821a | -16.578 | -58.2183 | 2024-10-02 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 1401a876-cc9c-3e14-8c36-9b0199f53c39 | -16.5973 | -58.2365 | 2024-10-02 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 389.5 |
| 668ff3e0-89ec-3be3-ac67-9f4758538cf8 | -16.5976 | -58.2162 | 2024-10-02 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 308.3 |
| 4cf369b5-d02d-3c50-94f7-86dfb8d02aaf | -16.6168 | -58.2343 | 2024-10-02 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| aed4e230-2b4d-3a17-a92a-f5c4558ddd93 | -16.6171 | -58.214 | 2024-10-02 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 7bc9f834-e482-38f8-9aa5-56eef6fd97f6 | -16.6322 | -57.2147 | 2024-10-02 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| cd01f609-1f6e-3b2b-934f-38c5307a3137 | -16.7265 | -57.4287 | 2024-10-02 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.3 |
| fa20e32f-f013-3481-b9e2-cb3dcb246fb4 | -16.8295 | -55.8945 | 2024-10-02 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 08fdea32-d7ce-3911-95c2-6b17e1c91f8e | -16.8695 | -55.848 | 2024-10-02 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 5bc00700-668b-3a0f-92ca-ef00209d15c9 | -16.8698 | -55.8272 | 2024-10-02 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| c47db044-bfb6-3a1b-9967-0bf2362c2ecb | -16.8891 | -55.8455 | 2024-10-02 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 159.9 |
| 077d36db-3716-36eb-8241-d0c44a9b2c6d | -16.8894 | -55.8247 | 2024-10-02 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 10be8782-3b56-36a9-a846-4615882a1229 | -17.1288 | -56.7455 | 2024-10-02 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 57cae357-891a-33eb-b074-9118af103f17 | -17.1091 | -56.7479 | 2024-10-02 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| fdbdc4f5-7eb2-3e36-aeb7-29e6361300e1 | -17.0895 | -56.7503 | 2024-10-02 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| e318d1ad-254b-3643-9a66-98119820bc9b | -17.1088 | -56.7685 | 2024-10-02 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| c1e2b8d2-d042-3b88-8051-602c57690dcd | -17.0892 | -56.7709 | 2024-10-02 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| c0b0fb25-1cef-365f-988f-eeb556c57c5d | -22.3713 | -49.3011 | 2024-10-02 07:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.6 |
| 507f85cf-dca8-36e2-b6be-f4391642341d | -22.372 | -49.2777 | 2024-10-02 07:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| 9488d056-37bd-3d34-9902-1019289d5581 | -22.3922 | -49.2961 | 2024-10-02 07:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.8 |
| 17a9c6a3-b7d3-3eee-93f7-ac6f357b8219 | -22.3929 | -49.2727 | 2024-10-02 07:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| 5676613e-eb17-3e67-8673-25aee8bb89a5 | -12.6484 | -63.1214 | 2024-10-02 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 28708bc5-3426-3167-afd7-f9d2b83ab4c1 | -16.7461 | -57.4265 | 2024-10-02 07:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 9fbb669a-c2f3-33e0-8af3-1658989c59ee | -16.7265 | -57.4287 | 2024-10-02 07:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 22e1ca16-fc14-3470-9d9a-9bf30198dd29 | -16.6124 | -57.2375 | 2024-10-02 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 60d86255-594b-3520-a106-12a378c7cffb | -16.6127 | -57.217 | 2024-10-02 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| b1f2c838-2c5a-3f45-b21e-2ee93ba92313 | -16.6322 | -57.2147 | 2024-10-02 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| a3039701-fc4e-35bc-968a-449b6c434098 | -16.8295 | -55.8945 | 2024-10-02 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 8a3c3b08-3ffa-38a4-99a8-e561499f2706 | -16.8695 | -55.848 | 2024-10-02 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 805f87f5-f436-36e1-a49f-edc4a4d2bbe1 | -16.8698 | -55.8272 | 2024-10-02 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 7c1a2095-25aa-3dcd-8dc4-232544c92660 | -16.8891 | -55.8455 | 2024-10-02 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 142.0 |
| 4d5fc107-4fcc-323d-a84a-3af1b56b9e9b | -16.8894 | -55.8247 | 2024-10-02 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 6aee5054-22af-39d5-a96f-44dfb926ce13 | -17.0892 | -56.7709 | 2024-10-02 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| b8730a29-bf6a-36b1-8587-d0dfd0f5f024 | -17.0895 | -56.7503 | 2024-10-02 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| d5b3128a-4b34-3fbd-88ee-65a74dd9e36c | -17.1091 | -56.7479 | 2024-10-02 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 2a4319fa-43c4-3c58-bb40-e2d4af351003 | -17.1288 | -56.7455 | 2024-10-02 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| f8b8fb99-68f1-34d9-99df-96bf54bdde67 | -17.1088 | -56.7685 | 2024-10-02 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |


[Clique aqui para ver as próximas entradas](README200.md)
