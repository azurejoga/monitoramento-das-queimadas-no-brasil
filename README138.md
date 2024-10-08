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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29edd5bf-6dbf-396c-8692-3dce67af1f2d | -16.9924 | -56.7003 | 2024-10-08 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 10b3483f-6f53-3cfc-a0fe-728d69fbe113 | -16.9211 | -57.4881 | 2024-10-08 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| aa74fde4-d99a-3dc2-abc2-20cef695aaa1 | -17.0123 | -56.6773 | 2024-10-08 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| a615917c-a206-3f0f-92ce-36215f93e041 | -17.1375 | -57.4221 | 2024-10-08 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| eb63f5ae-d55e-3531-b443-e204668651ae | -17.1175 | -57.4449 | 2024-10-08 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 819275de-cf9b-333d-acf5-46c58552f364 | -17.1977 | -57.333 | 2024-10-08 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| c96f16c0-eaa2-399f-bc3b-ff0691168c0d | -17.0982 | -57.4267 | 2024-10-08 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| e5244753-c38c-384c-9d14-80e462c40bd3 | -17.1178 | -57.4244 | 2024-10-08 12:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 172.5 |
| 09a5ba82-3191-32e4-9961-6b59c83832dd | -17.1584 | -56.1429 | 2024-10-08 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 2409d11c-5d36-3e23-83ed-4247100c7058 | -17.178 | -57.3354 | 2024-10-08 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 7e3e50b8-fc67-325d-b612-5593f2172571 | -17.1588 | -56.1222 | 2024-10-08 12:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 2bfc5e9f-ca81-3a10-8e72-4d0dfa326eb7 | -17.6692 | -53.0174 | 2024-10-08 12:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 328.4 |
| 74046efb-c58a-3a5f-8262-68a2319c2753 | -17.6688 | -53.0389 | 2024-10-08 12:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1f5a7e7f-df39-3d89-af5c-44d423539e2c | -18.6984 | -57.2708 | 2024-10-08 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 178c99ba-40fe-3e65-b9e7-7632c85847f1 | -18.7183 | -57.2682 | 2024-10-08 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 740df761-a2f1-344d-82bc-56e4271e0040 | -18.718 | -57.289 | 2024-10-08 12:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 787da1d2-3ba9-3ebc-af60-7f49c20dee5d | -20.3724 | -48.8372 | 2024-10-08 12:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 162.4 |
| c544fef9-0d37-31e2-bd8f-6edfd9323c8a | -20.3513 | -48.8648 | 2024-10-08 12:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 4fb422ae-8705-3ddb-9634-ef74b5f27da2 | -20.3717 | -48.8603 | 2024-10-08 12:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 203887f1-ac5b-3cb7-bd65-7479c5f75ba4 | -21.9782 | -46.5507 | 2024-10-08 12:47:07 | GOES-16 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.1 |
| 8f7e8641-6494-35c2-9e9c-c0d83c399431 | -14.71 | -45.16 | 2024-10-08 13:03:59 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0cb2da1-dec4-37b0-ae20-6c8d394653f5 | -16.67 | -57.13 | 2024-10-08 14:03:50 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6aff9f4e-0f97-3440-add7-6078c002d84f | -13.88 | -44.56 | 2024-10-08 14:04:03 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2e2bff8-932f-385a-ba79-bda640d15b0d | -12.31 | -50.85 | 2024-10-08 14:04:14 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38e8b494-9ac1-30c2-9126-e27d00bc58c6 | -12.27 | -50.78 | 2024-10-08 14:04:16 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |


