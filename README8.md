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
| 011054ef-b411-349e-bd52-e7c2d1300618 | -17.7037 | -53.269 | 2026-01-24 12:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 912a0299-6226-3b6b-a51e-174726b49a76 | -19.6836 | -56.8674 | 2026-01-24 12:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| a0260b59-8786-3b84-9ffa-7b0fe6d61c24 | -17.7037 | -53.269 | 2026-01-24 12:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| bf5a8d08-a3bb-3e4b-ada0-a1ed3db4ee6e | -5.4676 | -37.8278 | 2026-01-24 12:50:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 24510d1a-c13a-3868-9fee-d47b196b5fb9 | -19.6774 | -57.2026 | 2026-01-24 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| a582e2f6-5830-3b37-bf3a-cbf02b437334 | -17.7037 | -53.269 | 2026-01-24 13:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a06826f0-bc17-3fff-b228-ed3db30e2602 | -19.6836 | -56.8674 | 2026-01-24 13:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| f70360e1-d53e-3c6f-9952-d755ea28195e | -19.6836 | -56.8674 | 2026-01-24 13:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 282bef7d-d73e-3d85-a883-023ea82d40a8 | -19.6836 | -56.8674 | 2026-01-24 13:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| f1589ac6-edd9-3ad2-9e12-17c5adfed38c | -5.4676 | -37.8278 | 2026-01-24 13:20:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 120.4 |
| d4358c12-34e7-3553-bd60-526e213d8b62 | -19.6774 | -57.2026 | 2026-01-24 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 2478eb9e-cf9d-36c1-98b9-72095098a550 | -19.6836 | -56.8674 | 2026-01-24 13:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| c199f5a5-a67b-3d30-973f-f277539ccb1f | -19.6836 | -56.8674 | 2026-01-24 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| ef91ff0f-6ce9-3b35-8aaf-a0afe30fc2c2 | -19.684 | -56.8464 | 2026-01-24 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 39b3ef92-82c3-3939-88ae-cd013bf8cf70 | -5.4676 | -37.8278 | 2026-01-24 13:40:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 4b77f89e-c92d-31e2-97cd-9cb738a4257c | -19.6774 | -57.2026 | 2026-01-24 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 0472a4a9-fb24-3a27-bd84-fd60d8296916 | -19.6774 | -57.2026 | 2026-01-24 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.4 |
| 0ebc6af7-df5e-32de-83dc-e3eea3ff955c | -19.684 | -56.8464 | 2026-01-24 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 4c091df5-899e-3fa0-836f-9a1bcaf7e316 | -5.4676 | -37.8278 | 2026-01-24 13:50:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 136.4 |
| c8fcdacb-8eb0-3a51-a63a-4fa5f0b26d2c | -19.6836 | -56.8674 | 2026-01-24 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| e409888b-221a-3915-acd2-7cf1b2660e83 | -20.3291 | -57.8433 | 2026-01-24 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 30307888-6b4c-318c-bfc0-f2408d98c502 | -20.3493 | -57.8406 | 2026-01-24 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 4ed3bf52-db1c-3643-ae6b-918e7496649a | -19.6573 | -57.2053 | 2026-01-24 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 45e5d3d9-9d66-37cf-99b3-6c07ca7edf0d | -5.4678 | -37.802 | 2026-01-24 13:50:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 118.7 |
| 5b726514-673c-3865-99cc-8345ae46987e | -19.4365 | -57.2354 | 2026-01-24 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 93c313aa-928c-38ad-bde5-f2530481afa9 | -19.6836 | -56.8674 | 2026-01-24 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.8 |
| f3909935-48fe-33ed-b5a9-0e97e26ba657 | -19.684 | -56.8464 | 2026-01-24 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| c4a62f51-c9aa-3f1f-9090-f154098f88ae | -20.3291 | -57.8433 | 2026-01-24 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.3 |
| fd9b0716-b474-3f32-ad67-ec2695c1e37d | -20.3691 | -57.8587 | 2026-01-24 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 13dc810a-95d8-3860-b8c0-0b0eb8168487 | -20.3493 | -57.8406 | 2026-01-24 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 6cbc3c41-c65f-3aad-a1fc-39f33ccf661f | -19.4365 | -57.2354 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| a055c1c2-32fc-3f00-9c48-bdfb88cd3c01 | -5.4676 | -37.8278 | 2026-01-24 14:10:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 45e52238-d753-38cd-911e-5ee6d9d8aba5 | -19.684 | -56.8464 | 2026-01-24 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| e474fc47-7b8e-3713-9d3e-660199f72063 | -19.6774 | -57.2026 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 8a4edc94-1438-3ebe-b635-96c45b4509b7 | -20.3489 | -57.8615 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.2 |
| d14ddf27-a345-38e8-adee-fecf9c7e5dff | -20.3291 | -57.8433 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.7 |
| d6a7cf43-f2d2-3781-8ef6-2b5f4fc40a46 | -17.7037 | -53.269 | 2026-01-24 14:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 3f5e9200-a259-3380-8f1d-8f7c35d7ade7 | -19.6627 | -56.9122 | 2026-01-24 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 1d294996-38a6-311b-8693-d3e36f3b35b3 | -19.4361 | -57.2563 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 116b7550-8e35-34fe-94f6-40b1dbd25abf | -20.3493 | -57.8406 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 2611e2d8-4888-334c-9b76-1e4075e427d8 | -19.6623 | -56.9331 | 2026-01-24 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 37228aa4-2bbe-3fea-b0eb-8155771f74c5 | -19.6836 | -56.8674 | 2026-01-24 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.8 |
| c9be4d8b-415e-3436-9f4b-a80302f268f4 | -19.4558 | -57.2744 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 6e0a7163-b6aa-3ae7-bab5-e77b477f4ca3 | -20.3691 | -57.8587 | 2026-01-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 3056ab29-4268-3f01-b075-67e6fb8ae632 | -19.4357 | -57.2771 | 2026-01-24 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 130f98ce-0af0-3c32-bf26-7e9efd01ea10 | -19.6836 | -56.8674 | 2026-01-24 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.8 |
| 83515ef3-fb3a-3069-b889-625021481356 | -17.7037 | -53.269 | 2026-01-24 14:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 6007aeb5-7660-31fb-90d7-180b2b0eb7a8 | -19.684 | -56.8464 | 2026-01-24 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 514b4efd-4eed-3ef9-a1a7-34ab6a167dbf | -19.6774 | -57.2026 | 2026-01-24 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| de30c8f1-bd08-3e05-96f8-35da98835678 | -17.7033 | -53.2904 | 2026-01-24 14:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 218308c0-22ff-3e35-8f2c-62b5d44432e3 | -19.6774 | -57.2026 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 0928fe61-92b1-3e8e-a693-141c283efe8b | -20.3291 | -57.8433 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.9 |
| eaee133b-f9ea-37b4-b9e4-7ee91d3600e7 | -20.3088 | -57.8461 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 6990752d-5fc6-3dcf-b394-5455ab715152 | -19.6573 | -57.2053 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 2e6e0aa8-ab57-3451-abbf-d9d22c732dfb | -17.7033 | -53.2904 | 2026-01-24 14:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4cd821f3-899d-3d99-a976-930e17ccc629 | -20.3489 | -57.8615 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 8368e081-a577-3a39-a454-22262567ad3d | -17.7037 | -53.269 | 2026-01-24 14:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 199.1 |
| d065ad70-2d15-3a4c-929a-de7f3b1aab58 | -20.3493 | -57.8406 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| dec2627d-d2ce-3867-9f70-1f87ee32e83b | -19.6836 | -56.8674 | 2026-01-24 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 59de5cf1-b3a3-3645-b920-e9d493161090 | -20.3691 | -57.8587 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 1d1394ed-a31c-3890-939c-4180f66e31da | -19.684 | -56.8464 | 2026-01-24 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 5949e652-8721-39d5-91be-981c7c6ebb44 | -20.3287 | -57.8643 | 2026-01-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| e3f19fd1-adb3-377f-b24d-e918a2eadc32 | -19.6832 | -56.8884 | 2026-01-24 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 5809320c-5805-321e-a3c2-01bcc30b4c4c | -17.7033 | -53.2904 | 2026-01-24 14:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 9071b20d-9469-3383-871c-58ea7b5378d9 | -20.3287 | -57.8643 | 2026-01-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 338e4f5e-4189-3a9b-9084-4f45a9b8ba67 | -20.3489 | -57.8615 | 2026-01-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 3368ba63-883c-37e8-8ec0-fc47039d6250 | -19.684 | -56.8464 | 2026-01-24 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.2 |
| e391ba70-9480-3b87-bcf8-2d264ec7cda3 | -20.3088 | -57.8461 | 2026-01-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| b2c6e63b-1c4a-3ca4-812f-8933eaadf956 | -20.3291 | -57.8433 | 2026-01-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.2 |
| 75d8844c-3fdc-369f-b97b-3bdf55352081 | -19.6828 | -56.9094 | 2026-01-24 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 747312f2-f2dc-3e16-a0b5-63a17586ca2b | -19.6627 | -56.9122 | 2026-01-24 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 1a712ca8-7c23-3f7f-922c-37eaba5b944e | -19.6774 | -57.2026 | 2026-01-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 6e4eb4ec-a9d0-3ee5-9dd4-6bd6d252f4c2 | -19.4369 | -57.2145 | 2026-01-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 83436554-894b-3a67-a73f-ef733ed860d3 | -19.6836 | -56.8674 | 2026-01-24 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 42e1bc78-466a-3e47-8682-9a90d1c838ab | -17.7037 | -53.269 | 2026-01-24 14:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 224.4 |


