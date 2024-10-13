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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14923a2e-9b75-3df5-81a0-02975163aacc | -17.65246 | -56.30147 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c71ba71a-bb82-3516-8397-86135728fc6f | -17.65216 | -56.28149 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 3378ca95-d361-3731-914d-16c5e0256618 | -17.65186 | -56.26157 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 12da2bcc-5018-377e-b5ca-0d1295ccfe59 | -17.65129 | -56.28629 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f9cf4373-ce9c-3ff7-8e34-6a962cee6ce6 | -17.65042 | -56.29111 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 26965f62-0b0b-3cb3-b741-8ce2b0e1e2d4 | -17.65013 | -56.27116 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f416c991-9464-3a22-9a05-c0d11c8da218 | -17.64955 | -56.29592 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| af3f9f2a-e415-3394-93b4-fff91003702b | -17.64926 | -56.27596 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 80de4f3a-65c7-32e9-9a6d-954b3f9b6957 | -17.64433 | -56.26013 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a9e19139-6951-338d-b7e9-4a64a1c5a718 | -17.64375 | -56.28485 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5bae4b27-342a-38bf-8b71-40110ca02e3f | -17.64287 | -56.28966 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 125445f0-414a-344e-9148-b364c206de18 | -17.64259 | -56.26972 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5661b481-c421-334d-bc75-e62ac9ae1636 | -17.642 | -56.29448 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| db9d5fe8-1ad0-301e-9a75-5d91413e90bd | -17.64171 | -56.27452 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 990abec7-92fd-36eb-b40c-39c38850d3db | -17.64084 | -56.27932 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 0f39fc36-b746-3e39-b44b-27906de4763d | -17.63997 | -56.28413 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e3e39480-2e58-382d-aebf-06967665e2c0 | -17.63765 | -56.2762 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ae7b3a11-5e0c-35b1-a065-14918afb8261 | -18.22206 | -56.54121 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ec5b99cb-38f7-3d6a-96f4-e8fb2c869665 | -18.22316 | -56.49096 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dcb8a840-e9b8-34fa-b87e-18b9f4294a93 | -18.22251 | -56.45071 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1db5b57e-556c-346e-8872-bb5a72da49ca | -18.22229 | -56.49582 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1f53a831-d3d1-3095-9ba9-2831a008423b | -18.22165 | -56.45555 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 70283740-1387-3063-876e-f841460abcd0 | -18.22119 | -56.54611 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 09453f74-69ff-3d83-9846-c430d1e0056b | -18.22046 | -56.44031 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3abaafb1-acd3-34b6-ac70-ebe2846ff731 | -18.22032 | -56.55101 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5c509c34-9a11-3401-bcbf-6ecfdb9c8214 | -18.22024 | -56.48536 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5c73524f-1db3-3312-b781-72394adbac98 | -18.22014 | -56.42028 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a7fb81ca-ad0a-311f-89be-90f1d0bec503 | -18.2196 | -56.44514 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c648b972-09c2-3e54-9fb9-d403f724d01d | -18.21938 | -56.49022 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f0349aa5-1960-3ccb-9baf-b672a38e25a2 | -18.21873 | -56.44997 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fb4bdd8c-c91f-3791-9fec-37ec68a1f7fc | -18.21755 | -56.43475 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 950cc72e-acea-3db1-b634-b232a32d7e92 | -18.21739 | -56.54536 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bdcea7b6-8315-3161-857a-77b6448dfdf2 | -18.21668 | -56.43958 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5ccf2843-82e4-370e-a756-13aca5be8171 | -18.21652 | -56.55026 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6f721f41-950f-3265-8a5e-a73a9b40e2e0 | -18.21582 | -56.44441 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ae79149c-162d-3728-99a6-84fd7d94b86e | -18.21565 | -56.55516 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8af9d224-e6f5-308b-aae5-905ccec6c4a5 | -18.21496 | -56.44923 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d615840f-f27d-3195-a817-bb83436a94f8 | -18.19544 | -56.8531 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 68b2f402-8a45-3f94-8696-c217b06fbb00 | -18.19345 | -56.84219 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ee1d585f-81f4-38f3-b708-b8384299e7fc | -18.19269 | -56.83989 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e3ed14c9-f794-3199-92cb-cbaa69997d8f | -18.19251 | -56.84726 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a666df4b-9412-35a0-88c6-ff28550fda5a | -18.19158 | -56.85234 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 34683a3d-982b-3571-9f6d-06decb71596d | -18.19088 | -56.85006 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 961ce5c2-6d2d-3732-bf50-1f6cb28de0d6 | -18.18959 | -56.84143 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 63a49a26-492d-3c03-bf69-bdfad5c1f18b | -18.18771 | -56.85158 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 207817f5-2e55-3f56-ab49-7bf2bc4471f9 | -18.13135 | -56.30557 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0ad38b44-1f99-394b-a0de-4045a30a8848 | -18.1305 | -56.31034 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 880fecd6-9309-3e8f-a77d-4321f19515a3 | -18.12893 | -56.2756 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ee306da5-de1c-321e-a00e-f99b3bda766c | -18.1276 | -56.30485 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 35ffa374-71fb-343f-bf17-8355123e46ba | -18.12675 | -56.30961 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c4f4ce2e-ace9-3d29-952f-0a1962489337 | -18.12519 | -56.27488 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 965d1749-0017-3b7d-af90-43ae853141a8 | -18.12059 | -56.2789 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 003ddb10-893b-3010-8caf-6ddee8c07468 | -18.11685 | -56.27817 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 64ec8fbc-cccd-3c44-8093-cfaae9defe8f | -18.116 | -56.28292 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e909b9d8-08be-3590-a439-7103d5326f14 | -18.09426 | -56.44757 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 20e81a41-4501-3c56-9a12-87745aaf5889 | -18.09222 | -56.43714 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| eef5bf1d-14b7-35c1-b1e2-30b65e279c8a | -18.09135 | -56.44199 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f3b70f0f-4e7c-3013-a0f3-2a571580bca8 | -18.08931 | -56.43156 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c75eab8c-3bc1-3252-a416-f9ea87cafb6c | -18.08844 | -56.43641 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2c5bceea-ba39-35b0-9833-54214309c388 | -18.08611 | -56.40593 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| efe092c3-fe2d-3b88-9d93-6f44a8daf34f | -18.08577 | -56.32143 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 5d252ef6-8589-3b80-8eba-09a1edb1732f | -18.08553 | -56.43083 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 002f9be2-2d2f-348c-b13d-8655082f74f7 | -18.08524 | -56.41076 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 436759d5-3d42-3f45-9749-45b313dc9ee7 | -18.08466 | -56.43567 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4085b939-7cfd-3e3a-b9c5-236fbba9a4b3 | -18.08437 | -56.41559 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5d50f0dd-5bbb-353c-b7a0-ae92aade401a | -18.08175 | -56.4301 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b30a17ec-e0ef-3ab5-b51f-ee0932db0286 | -18.08088 | -56.43493 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6bbe46cb-bcc0-328f-9f2c-d1101a3ff3ca | -18.08029 | -56.33025 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9579fd9f-3181-3562-a22f-e7ae47d35bae | -18.07797 | -56.42936 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e122c237-3ee8-398a-bff8-332043abc385 | -19.58879 | -56.53268 | 2024-10-13 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0185bb9d-75c4-3a54-9c31-0d89339cd38e | -17.90012 | -57.33268 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2b5cf590-f9a8-3168-b240-0a058033861e | -17.90878 | -57.33064 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 558ee1ae-c013-3043-9793-e6b6968c7457 | -17.90871 | -57.35328 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| c3c4b680-df12-3c10-99bc-3d5838df0e15 | -17.9081 | -57.33427 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7084f07d-ef71-3cad-a6a6-a502720fa0d5 | -17.90804 | -57.35693 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| d3354f1b-62de-3118-b348-b33d45eb14bf | -17.90742 | -57.33791 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| cd44f4bf-5525-3962-9000-d0da5b3a799b | -17.90736 | -57.36057 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 31bbb5bb-ad1a-3075-9dde-534676e0233e | -17.90675 | -57.34155 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| c3df3faf-5b76-3f23-b7e8-d35f6db0eb48 | -17.90668 | -57.3642 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 409d8cad-61c1-3e8c-bfa5-c39605683eda | -17.90607 | -57.34519 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 204fe736-ba7e-32a1-94e3-c9ba774d151a | -17.90539 | -57.34883 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 6791729d-653d-323f-9508-037d6a1a7242 | -17.90479 | -57.32984 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 1a1289ac-53e7-3f2e-8096-a68944fbbb20 | -17.90471 | -57.35248 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 8c98911c-0ee4-3b05-9bf1-048d92453567 | -17.90411 | -57.33348 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8b10b9c8-624a-33c0-952e-678184a44441 | -17.90404 | -57.35613 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 9cd2f87c-6ab0-3cea-8a9e-47fabaa73ba3 | -17.90343 | -57.33712 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1c4b62e5-3283-39c5-a85d-f88e8b7a3750 | -17.90336 | -57.35978 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 1fd764de-f230-3229-90ae-2d9678912ddf | -17.90268 | -57.36341 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 8c2f0531-6a07-3aa5-8e1c-02da104fe039 | -17.9026 | -57.38617 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3ee502d4-5eb8-3cdd-8b95-0e94d8ecd4c3 | -17.90207 | -57.3444 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| d81efe4f-104f-3f53-96e7-51dc15d4e917 | -17.90072 | -57.35168 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 509bcc6a-d960-3448-892f-4ebf1a79a96c | -17.90004 | -57.35533 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 93454a20-5d57-3f03-aaeb-c945c77f43bf | -17.89944 | -57.33632 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 031c2c6f-8567-352e-afd3-fcc79b990bc3 | -17.89936 | -57.35899 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 1a6311b2-d80f-3ace-8db3-2f5b18059fde | -17.89928 | -57.38169 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 916a1707-1b7a-3f09-a3d1-257f09c6cb24 | -17.89876 | -57.33997 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 5081d35a-e532-36e7-9fa7-8d48fff40202 | -17.89868 | -57.36263 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| a2250d44-054f-36d5-9fe9-ca2e8213a097 | -17.8986 | -57.38536 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 793461ba-6cea-3d94-bbe8-537142065dd5 | -17.89672 | -57.35089 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 7616e7dd-87e0-378c-a956-3553a49ba152 | -17.89604 | -57.35454 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |


[Clique aqui para ver as próximas entradas](README71.md)
