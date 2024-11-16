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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ba75587-6b87-3ea1-8c67-cde04e24af4c | -17.56776 | -57.57571 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 895b7156-e9ee-3920-9585-3d9a5dc47501 | -17.57539 | -57.56446 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 552c3197-2a1f-37b2-bc6a-c3702aa88029 | -17.59305 | -57.58139 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 76961c3e-e6a1-3186-a0d6-48a5cb2ab66a | -17.58684 | -57.49241 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e3ea604b-bc5f-3922-a9eb-ee88af637d1f | -17.6278 | -57.5666 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 7bd3c110-8aa3-31de-958b-a62b8ffa36f9 | -17.64545 | -57.5577 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 0d5810ca-2769-3ee5-be9a-fe7dbd98e288 | -17.64041 | -57.55656 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 82cab00c-c5df-3dd2-a930-284cb5d6eb8b | -17.68452 | -57.56044 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 90f3d759-2b91-34e8-a281-cee41acce8de | -16.04177 | -60.12164 | 2024-11-16 04:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9170c46a-a66e-3536-8fdc-17a60bf049f6 | -17.62275 | -57.56548 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| d068f95e-a750-300b-8e3c-19410092dd69 | -17.68515 | -57.55738 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d14e6fd7-3c6c-3324-8b4a-3aea4e8f8515 | -17.65803 | -57.54767 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 21faf603-e6f0-3f64-857a-30fecb856435 | -17.54863 | -57.52538 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9837c3f5-4f9d-3483-bfb5-2a1c8164fb23 | -17.588 | -57.58024 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 93c83ef6-1ac4-3149-bedf-bec59c75b14d | -17.65081 | -57.45355 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eb5b9de7-735a-3eb4-ad20-e5266931d729 | -17.69079 | -57.58113 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 8f262c89-e7b5-3d12-aaaf-efb5ccb5819c | -18.03288 | -57.35113 | 2024-11-16 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 57eaae90-e1a2-3c14-9b02-5b298e326148 | -17.58035 | -57.57776 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 624b32f0-06a1-3537-98c5-8f5129d59871 | -17.62023 | -57.552 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fa921590-ce21-3802-984d-adfcaaeedaf1 | -15.92058 | -59.27153 | 2024-11-16 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f20ef4-099c-318d-a0f9-8964f8da556f | -17.68765 | -57.55761 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 327e4f54-fd83-3ee9-9363-31be494f479a | -17.66748 | -57.55304 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9d28d64e-9eef-38ca-87fd-94b3c3d3b1e1 | -17.58358 | -57.57601 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8f6d0505-649d-385f-af8a-ee3c8d4b5a72 | -17.58294 | -57.5791 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 6b8da69b-2eb5-3fda-9f4a-e1ecfdbcf896 | -17.58677 | -57.56059 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8783be2c-73d7-3b33-b098-6e8b92171435 | -17.56961 | -57.57861 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2f748408-95ed-3d43-8cbb-67cd89c372f3 | -17.57482 | -57.47373 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0e7821fb-fd87-39e1-bd86-8f93fc9f9a9c | -17.82866 | -54.54128 | 2024-11-16 04:27:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36e51809-18ab-307f-858a-7dfe46328d52 | -17.59126 | -57.49661 | 2024-11-16 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1aa712d6-41bc-30a8-9e14-377c3c38c2f4 | -17.54676 | -57.53462 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| acd35e00-a5ef-3be4-b42b-d65a6440d84d | -17.23344 | -57.452 | 2024-11-16 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| fa9c89d2-eae7-39b2-8b42-f1aaa8d9c4cc | -22.05166 | -56.00716 | 2024-11-16 04:29:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1a88bc3-bc04-3a22-8c4c-e791f3967a5d | -22.2716 | -56.10732 | 2024-11-16 04:29:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a679744-00ba-3440-a042-5fd372c37964 | -20.21119 | -56.62632 | 2024-11-16 04:29:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 80e34cb4-86af-3ef7-8e5a-d501a9f34018 | -22.27243 | -56.10311 | 2024-11-16 04:29:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d04d3d59-4a92-3d3d-b7f5-ab6e315f42a0 | -21.21582 | -56.35558 | 2024-11-16 04:29:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80c64440-2117-3772-bb82-3c52c4358a12 | -23.65403 | -52.94062 | 2024-11-16 04:29:00 | NPP-375D | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 0c05f981-6404-3136-b1d8-df0bf73bdb99 | -22.05501 | -56.01248 | 2024-11-16 04:29:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c0d3f4b-d5ee-35aa-afd7-c123ab0f0d1a | -21.22019 | -56.35658 | 2024-11-16 04:29:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a9a1bb7-3fdc-31ef-8174-0aa8672a2e2f | -22.05585 | -56.00823 | 2024-11-16 04:29:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18608d8c-1eea-3623-92fc-306f9c4c0454 | -23.65053 | -52.93986 | 2024-11-16 04:29:00 | NPP-375D | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| fa45987b-214e-3331-a22d-2a2e28ea154e | -2.78 | -48.5806 | 2024-11-16 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| d8bc6927-af60-3884-aedd-308eba7ef1c8 | -2.1562 | -53.7039 | 2024-11-16 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 850ee787-d090-36d1-8d1e-f98e83c2f788 | -17.5678 | -57.5146 | 2024-11-16 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 820957cd-8d6e-3aba-af15-196c9bd71d0c | -3.2753 | -45.5151 | 2024-11-16 04:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 617d9854-460e-36a1-a8b1-ded893c0b199 | -17.5675 | -57.5351 | 2024-11-16 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| f9cb3a2d-9b40-3fd1-942b-ccfd9d6ed883 | -15.9219 | -59.2722 | 2024-11-16 04:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 978a8d85-5326-3180-93c9-49e95071b9b3 | -3.2754 | -45.4927 | 2024-11-16 04:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 9b54949c-3efa-33c2-9622-b1f3d4c6a04a | -2.2299 | -53.6219 | 2024-11-16 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0c283bb6-0292-3099-bee7-a792f994b65e | -17.7045 | -57.5803 | 2024-11-16 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 1f183e05-cf85-3dba-b9ee-4483c6789426 | -3.7394 | -45.6523 | 2024-11-16 04:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 5a7a76e6-1177-3d55-ad10-c19d3dd6be43 | -15.9025 | -59.2741 | 2024-11-16 04:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 7e7cf3e5-25f9-398d-82ab-a0508356a48a | -3.7208 | -45.6531 | 2024-11-16 04:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8d657742-de90-38b0-9062-a6d4f8b3c50d | -2.2299 | -53.6018 | 2024-11-16 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 79f33907-252d-3767-ba3d-034d24eda84f | -3.2009 | -45.5405 | 2024-11-16 04:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ca87967a-728c-3504-87ec-b05a5b43a83c | -17.5478 | -57.5375 | 2024-11-16 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 92d6864d-31e7-3d82-9813-70cd8e857a31 | -15.9028 | -59.254 | 2024-11-16 04:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 128777e7-a53d-3a86-b1b0-1af095e3c5a5 | -3.7393 | -45.6747 | 2024-11-16 04:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 00267e58-0245-33ed-8eed-5ba495928c3c | -29.90161 | -54.92559 | 2024-11-16 04:31:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| cd9dae39-11a4-359a-8389-992ca2d6b843 | -29.90079 | -54.93013 | 2024-11-16 04:31:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| a999e0db-baed-3ec2-b989-6bccc5fd072f | -30.12836 | -51.59426 | 2024-11-16 04:31:00 | NPP-375D | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f0eed99e-5973-3ad0-9af0-9c8a7caef0ed | -29.6303 | -51.96581 | 2024-11-16 04:31:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 40513259-c7d9-3fc8-a20d-b41e7d4163b4 | -28.41904 | -55.72509 | 2024-11-16 04:31:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 04966c2f-3513-32c8-a0fe-d1dd24f5a7b8 | -29.87432 | -51.15748 | 2024-11-16 04:31:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 544e1233-c2b0-35f7-bc72-ab9e53bc678f | -28.41532 | -55.72419 | 2024-11-16 04:31:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| a503f1fe-4d24-3020-b02a-3a626924d2a1 | -29.28636 | -52.01724 | 2024-11-16 04:31:00 | NPP-375D | CAPITÃO | RIO GRANDE DO SUL | Brasil | 4304697 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0481cc58-172a-399a-88b4-fd0c829fd83b | -28.39981 | -51.35229 | 2024-11-16 04:31:00 | NPP-375D | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 26558d44-ed09-3976-a581-36572819ab20 | -30.13169 | -51.59495 | 2024-11-16 04:31:00 | NPP-375D | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 345216fe-a5ce-3c13-ab09-4236498f6d9f | -29.72876 | -51.19975 | 2024-11-16 04:31:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 8e0ac5aa-db7c-39f1-b7d0-f60b5ebd2c1d | -29.62697 | -51.96511 | 2024-11-16 04:31:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8b881762-d546-36b7-9b44-09af53b888ea | -3.2753 | -45.5151 | 2024-11-16 04:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b74f6610-c67d-3b50-afb5-df2cff1d2909 | -2.2299 | -53.6219 | 2024-11-16 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 37525643-5dfb-3fa0-a922-8b3fb7af3df4 | -2.1562 | -53.7039 | 2024-11-16 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6997819b-36e8-319e-9b5c-1ce1bb318974 | -17.5678 | -57.5146 | 2024-11-16 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 12465712-3f86-3ef6-b00e-f7c836e0c084 | -3.7394 | -45.6523 | 2024-11-16 04:40:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7c2f38fa-3112-3878-858a-249c2e5de383 | -2.2299 | -53.6018 | 2024-11-16 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2811d539-2c2e-3bbc-951e-f6a99c064588 | -15.9219 | -59.2722 | 2024-11-16 04:40:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c0eccd15-c99d-30b3-bf09-c0f295349afc | -15.9028 | -59.254 | 2024-11-16 04:40:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| bd853344-1b88-39fb-aa4c-7dc1a3e4bb3a | -2.78 | -48.5806 | 2024-11-16 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 53def839-9728-3c52-88a7-502492592ce6 | -16.9384 | -57.6291 | 2024-11-16 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 2be734b5-91fc-3c7a-9469-d46cef6fec7c | -15.9025 | -59.2741 | 2024-11-16 04:40:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| dbaee71a-84de-36ec-b32e-c7908c67f531 | -3.2754 | -45.4927 | 2024-11-16 04:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e32ffa66-7843-316e-bc53-c0f336653412 | -23.6665 | -52.9275 | 2024-11-16 04:40:00 | GOES-16 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| 376511dc-9555-3f48-a7b9-6f3deceac075 | -17.5478 | -57.5375 | 2024-11-16 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 6315c15f-705c-3583-b855-283c060f5821 | -3.2009 | -45.5405 | 2024-11-16 04:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a47a2524-4a0b-3321-b675-d20ec2e752cb | -3.2008 | -45.5629 | 2024-11-16 04:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d89c4aa0-e6d7-341f-b90a-4f348ebc8630 | -17.5675 | -57.5351 | 2024-11-16 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 4b914bb5-da90-388e-8f4c-d6b5452c0569 | -2.7466 | -48.56467 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b02f1ce-f82f-38f2-9cac-d42b73fbdc7d | -1.20002 | -53.69624 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 846f197a-8adc-3a7a-8767-a814fda27522 | -2.15338 | -50.52296 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 350cb8c3-d38d-3b83-a7db-1472600e964d | -2.15933 | -46.40041 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1997f38a-2354-3cf1-b1b8-3355f8e4773b | -2.0957 | -50.2168 | 2024-11-16 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de701dff-83ff-33d7-a48d-3c505c7aaeea | -2.78826 | -48.56532 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 76bfb880-5225-3ee8-bc08-7781794f4b2f | -2.90622 | -48.3097 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91d92fd7-1497-3b7b-8437-1217639b70b4 | -2.37474 | -50.40894 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52bbcf51-89f1-3279-b96e-972857b89be7 | 0.11527 | -49.84828 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5ae38f3-55e2-3a62-9aec-4220ffdc0123 | 0.05917 | -49.5568 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 301114b1-188e-346c-8b6f-b4961d06f07d | -2.66794 | -46.18202 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 068c0e98-6c80-30d1-81c8-bd75db6dfa0c | -2.25393 | -48.75056 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d7050bb-9e77-3741-9156-d43a3b51e802 | -3.19258 | -45.55334 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |


[Clique aqui para ver as próximas entradas](README41.md)
