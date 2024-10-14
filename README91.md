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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a2753d1-4dbb-3d47-a4e7-01822c3df631 | -11.19914 | -53.97791 | 2024-10-14 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7bb4be4-b997-3f36-adc5-0a1f8852461e | -11.10288 | -54.21749 | 2024-10-14 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f2bd25c-2b89-303e-bb4c-81a0c19d8a20 | -11.0994 | -54.21692 | 2024-10-14 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8346f80-e057-39b4-856f-5e1182a717d4 | -11.0793 | -54.7967 | 2024-10-14 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a53978-c68e-3728-8ed6-293b53e85bf1 | -11.07707 | -54.78807 | 2024-10-14 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea6f0f1b-3fb5-3d06-87b4-6314b6c657da | -11.0764 | -54.7921 | 2024-10-14 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fc499ce-12f5-34b0-9b4b-9c73cdba4c5e | -11.07574 | -54.79615 | 2024-10-14 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a1da01-3c01-3274-a852-241b420f80f5 | -11.07506 | -54.80024 | 2024-10-14 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47ff216b-a67a-37b4-9474-beec5e4ba783 | -12.59894 | -55.18904 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39106c11-3072-389b-bfa1-774366b6c37a | -12.59825 | -55.19317 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28f0d696-d981-3fc5-a6c1-d6b5b5eff382 | -12.59538 | -55.18843 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e816394-fe4a-3aba-a028-c74998300a93 | -12.59468 | -55.19255 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6adcbaa7-f39d-34d8-93d4-961bce774aac | -12.49911 | -54.50972 | 2024-10-14 04:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7c2d666-54d9-3023-883f-d3c88c042131 | -12.49846 | -54.51361 | 2024-10-14 04:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a401ed6-f2e6-3ad1-b626-3adcd60ddb4f | -12.46382 | -54.57166 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73f24ef-abc0-36f7-9717-d804f9e5a88b | -12.46164 | -54.56327 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19533e16-723e-37a8-8104-07630af2d072 | -12.46099 | -54.56715 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75482171-385b-37e9-b76f-225191f3d221 | -12.46035 | -54.57104 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fd96e51-1e84-34dd-b799-6d0c56f38719 | -12.4597 | -54.57493 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4f24b49-e66c-3170-aa6d-ea3d90cd501b | -12.45817 | -54.56264 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52ce10c4-e945-3ac4-a993-3f83e8e3fad1 | -12.45752 | -54.56653 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3878f1b9-20f5-3d2d-99ef-fa7b97e87fdb | -12.45687 | -54.57042 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8927cca-8883-37e6-be85-e32e785dfc02 | -12.45623 | -54.5743 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07354bfd-9b48-3c74-8df1-6b323560d942 | -12.45599 | -54.55428 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5f0cc1c-111a-3d4b-9b82-2c16877d9d7f | -12.4534 | -54.56979 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 705a7c5c-68c8-34c1-9f8d-f921347a22ea | -12.45275 | -54.57368 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e592fc9a-9e3f-3dcd-9d05-3715578094ff | -12.45252 | -54.55368 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54c68297-2245-362e-ab09-4283a3264df3 | -12.44928 | -54.57306 | 2024-10-14 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ab86634-0a38-31bc-a9d9-b9ac1d0a8103 | -14.98346 | -54.99857 | 2024-10-14 04:46:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae20446c-8c18-39ae-b456-19e2f3f5a430 | -10.5307 | -49.7843 | 2024-10-14 04:46:03 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| af974edf-d449-344d-8bdb-f279712037bf | -10.8552 | -52.3971 | 2024-10-14 04:46:05 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b8e0ffd3-1bf7-30f6-b0fc-8a89cbdd71ce | -10.8363 | -52.3989 | 2024-10-14 04:46:05 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 261bf420-ba0a-3fe3-9d45-b7751ed0b57f | -17.0004 | -57.4176 | 2024-10-14 04:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| d86b35dd-1936-355c-9085-56e7b17f9e21 | -17.1957 | -57.4562 | 2024-10-14 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 90d24d49-63c7-39fc-a8c2-209d82248628 | -17.196 | -57.4357 | 2024-10-14 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 18d27a18-7756-34b4-9c8a-0c1295b9f517 | -17.6876 | -56.2409 | 2024-10-14 04:46:42 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| eec3e2e1-499f-3fe7-8bf3-1d25a0599cb0 | -18.2342 | -56.6055 | 2024-10-14 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.9 |
| d49511aa-b917-3931-90ff-ddce420831c7 | -18.2338 | -56.6263 | 2024-10-14 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 74116ff7-8d14-3b96-80bb-b11eed16d8dd | -18.2147 | -56.5873 | 2024-10-14 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| b475e9b8-3509-3fde-9015-d3a5933e3b1d | -18.2144 | -56.6081 | 2024-10-14 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.1 |
| 5b530384-9f4f-33f2-8a07-6475b9273ee1 | -18.2104 | -56.8368 | 2024-10-14 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| a1799ec4-095f-303d-aa84-a5dc2a31f70d | -18.1905 | -56.8394 | 2024-10-14 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| c8d63a34-fa34-340a-8569-5937e3432438 | -18.2346 | -56.5847 | 2024-10-14 04:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| c2f870d4-7dcf-3d29-bc18-b4d4f1e9cbfb | -17.97742 | -57.33025 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c2d1ff00-9d2a-3c05-869d-e0fb0cadca5f | -17.97372 | -57.32952 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4fbabc88-d86e-3d88-9b17-12862bc4ae82 | -17.97291 | -57.3341 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6a6a289d-7ad7-389f-ae1e-a1b54ba92826 | -17.97002 | -57.3288 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0649f6c2-3b32-3699-95df-e313d86267bb | -17.96921 | -57.33339 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e513183c-ad93-308c-9a5e-002781e1530e | -17.96876 | -57.31436 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9ae05cae-ff00-3d40-acfb-61f136ac7b52 | -17.96795 | -57.31893 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b48718cd-c3f5-3c32-bcc0-23c38e64f9bf | -17.96461 | -57.29463 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f79baffc-c534-3534-ac96-c59c56aeddc7 | -17.96173 | -57.28936 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| e3d32159-b63e-3f21-b680-411e4a64f495 | -17.96136 | -57.31292 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 377.2 |
| e6fca3cd-5385-32e4-a0c1-01a4421bd0ea | -17.95974 | -57.32206 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 657.1 |
| 2c701a8d-9db6-3f6c-ada6-e4739df892d4 | -17.95929 | -57.30304 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 370.9 |
| 8fa349f7-8975-3212-941c-5ea1671cb5b5 | -17.95892 | -57.32664 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 657.1 |
| 7149fe3a-37b5-302d-aad5-ee8a82154c2f | -17.95885 | -57.28409 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2624af96-e9ee-3d9d-b644-ceb63912bbda | -17.95811 | -57.33122 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.6 |
| 189c4065-27ee-32d4-ad98-b244b264f1e4 | -17.95804 | -57.28865 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f9d9a051-bbe0-3760-ad99-8f2556140ddd | -17.95434 | -57.28793 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b3e538ea-e40a-33ec-9f0e-72ef16f2556b | -17.95397 | -57.31147 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 716a6d92-7f3e-3514-ae7e-d7952865a18b | -17.95316 | -57.31605 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 05eef4e5-fbc9-3663-8423-17799816db7b | -17.9519 | -57.30163 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 66992b2c-ea3d-3db3-bb1f-688ce5719015 | -17.95109 | -57.30619 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| f7e17516-794f-383f-9471-4580c7ad9f10 | -17.9507 | -57.32979 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.4 |
| 5fd0f723-f193-3fbd-8ccd-b44d27586941 | -17.95065 | -57.28722 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9556e52a-2c3d-3571-a8c9-93a86df0c31c | -17.94864 | -57.31992 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 50f0284f-12cb-3765-bfaf-e67b84f7ee11 | -17.94821 | -57.30091 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.2 |
| 73f4e234-c1b9-3c5a-8853-2e570d14ea4c | -17.94782 | -57.32449 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 164df493-b538-33b3-a867-e1cd7038dadb | -17.94777 | -57.28194 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5cc6b4b3-12d0-3540-9508-9d9ee79787c8 | -17.94739 | -57.30548 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.2 |
| a1ab6cb4-75b4-3b02-bbf1-46c1256ee964 | -17.94701 | -57.32907 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.4 |
| 92746182-d5c2-38f4-96b6-532843505441 | -17.94614 | -57.29106 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| ba1e4785-307d-31f9-a73f-4a74ff55e25d | -17.96713 | -57.3235 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 1e19b013-c19f-35c5-bec6-85f97ff2cadb | -17.96506 | -57.31363 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ae6f37fd-5acd-3362-9718-c0334fd6da26 | -17.96344 | -57.32278 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4314d912-8ca4-356f-8860-f8c82be8db6d | -17.96092 | -57.29391 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5ff3a701-adda-3148-926f-4fff67996fea | -17.95027 | -57.31076 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 4ae73594-b239-321e-8881-50d9a6a1e1e4 | -17.94984 | -57.29178 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 4ceacff0-c89c-3884-9beb-849f318c39de | -17.94657 | -57.31005 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 08e4ba1b-1ce4-3d79-b08e-bfc615bd3695 | -17.98482 | -57.33169 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 22a211e1-535f-3337-8c84-369e323fca5f | -17.96551 | -57.33266 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| aa35d9cf-940a-33b3-9136-af828b7ea384 | -17.96181 | -57.33193 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 60cc8279-dca9-301a-b307-85f25f87aa41 | -17.91987 | -57.3096 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6ea32a7e-cc65-3ff3-aed8-43447be27d2d | -17.91709 | -57.29746 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 0eecc24c-c872-3d1a-87c5-b08196db6566 | -17.91549 | -57.30662 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| f9c68b23-f2c6-3109-835d-8d82d2711142 | -17.91499 | -57.28759 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.9 |
| c7cccbaf-8cc9-37b9-9617-431d10360730 | -17.91289 | -57.27774 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b3e4bd98-81d0-3dbc-bd80-8fc954663376 | -17.91129 | -57.28688 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 226.3 |
| daaf5b30-6555-3526-9911-ff38511ecdcb | -17.90809 | -57.30517 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 39a9dec1-2502-30ca-8d8f-99d2c02b6170 | -17.90359 | -57.30904 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| fe7867a3-d2af-320b-86f6-fea76d335871 | -17.9031 | -57.29001 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 200.8 |
| f4d50b1c-2460-3490-974a-c26f97e9ea13 | -17.90181 | -57.27559 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 06367976-8d0d-3f99-b3e6-9bde8e7d59ce | -17.9015 | -57.29915 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| ad5d1c03-007c-35ba-a39b-788c94d7263f | -17.89989 | -57.30831 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 66633ea8-5ad3-3d0f-8730-582857ddec65 | -17.8994 | -57.28929 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 200.8 |
| f18f5718-1e2f-3585-938a-8c2d9c0aebc6 | -17.897 | -57.30301 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bf096a07-1504-37ec-8095-effd8a321f8a | -17.8962 | -57.30759 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6d30ddba-13ba-33de-b807-8ba1be1a6339 | -17.89571 | -57.28857 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 0f88e4dd-9dfd-35a9-af16-81c43412013a | -17.89539 | -57.31217 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |


[Clique aqui para ver as próximas entradas](README92.md)
