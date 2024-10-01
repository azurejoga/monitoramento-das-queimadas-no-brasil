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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36568f27-fc01-3cf3-8315-b777bd8c85c8 | -19.129601 | -57.454601 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a25cd4fe-1005-3609-a3a4-41b0b517a5cd | -19.131599 | -57.463001 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f218bff-4efb-3e44-9907-ca4900469041 | -19.1336 | -57.471298 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0259f23d-33e4-3517-ac65-005c312a2f41 | -19.119801 | -57.4571 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a9a6b85-e748-31a0-907b-43ce802025aa | -19.121799 | -57.4655 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b3bd9e6e-5992-3ebf-a8e7-ba51774588ba | -19.1238 | -57.473801 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 158b9a03-fcc3-3856-8d2a-9e020310e2c6 | -19.112101 | -57.468102 | 2024-10-01 01:44:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 867960eb-322b-3765-9df3-0dc9295dd242 | -19.1141 | -57.476398 | 2024-10-01 01:44:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0e7b75fe-c0de-3860-95da-85230c73d942 | -17.1752 | -56.151501 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a738e70-0e2a-3930-89be-07752cdc6157 | -17.177799 | -56.161598 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2eeb1400-9f1c-3a2d-aff4-d60bb4ca2961 | -17.1803 | -56.1717 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| edff1491-8247-3e09-bfe8-e7cdac759081 | -17.1828 | -56.1819 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 496e80ba-e44a-3b1c-a7c7-1ac111e6cff4 | -17.185301 | -56.191898 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eab19c7b-7fdd-3ca1-937b-d1ee0060fb25 | -17.187799 | -56.202 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3dee258-f7ae-344a-9d14-6dc2db80266e | -17.163 | -56.143902 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a29dffa4-11b8-33ee-aee5-749eb1157f15 | -17.165501 | -56.154099 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0fed3a7b-dc17-3433-9987-36a7cf38fbc7 | -17.167999 | -56.1642 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 731142b4-a808-37b3-9224-a2a72e78be60 | -17.1705 | -56.174301 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 081f2e62-ec7e-3cc5-a9db-0aefeba3c8bb | -17.173 | -56.184502 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a38ddd7-5f10-3fc0-ba0a-d76a5d82e5dd | -17.175501 | -56.1945 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78393a83-87fb-3687-986e-84f682f16399 | -17.177999 | -56.204601 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eff5bddd-8c0d-3835-b148-5ac015a446fb | -17.1805 | -56.214699 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb1c765a-642b-32fa-87a8-b0aa0134113a | -17.1558 | -56.1567 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0bc12d6e-5510-3210-bab3-694530775095 | -17.1583 | -56.166801 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ba298a4-0acf-3345-9fa0-7e8a0800cf60 | -17.160801 | -56.176899 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3770a21a-1125-3856-bcbb-877fba7a4b11 | -17.1633 | -56.187099 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 616f535e-e250-3eb0-94b0-815f4d1915fb | -17.1658 | -56.197102 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e721c3ff-4955-33f7-8104-7d0bfdf1ad6b | -17.168301 | -56.207199 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ea38166-93fe-3de2-80ca-ebb77ba38659 | -17.170799 | -56.2173 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66c26956-0ca1-3fc8-87c7-d7950a2aae5c | -17.1733 | -56.227299 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f45705f0-01c1-3379-af14-1d631e0d7f1a | -17.1486 | -56.169399 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2690dc98-bda6-3d07-aed6-ba74efba54d9 | -17.1511 | -56.179501 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 074873f2-902c-3590-a8fb-09d55b340d83 | -17.153601 | -56.189602 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 749a4d63-7978-34ff-9f79-6c9bc3e95aa1 | -17.156099 | -56.199699 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6860d37-afd2-3085-8679-426de0bc5879 | -17.1586 | -56.209801 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01309770-6ebf-3428-960e-d48b1029611b | -17.1611 | -56.219898 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f00bfda3-b17e-31a0-bd04-81368da54d7a | -17.171 | -56.259998 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 620ef8d0-a6a7-390f-8fac-63df472faec5 | -17.138901 | -56.172001 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 792d7af2-6333-37b5-b187-3dafc5140bf1 | -17.141399 | -56.182098 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47836190-9a0a-370c-b334-370f9f33d2bf | -17.1439 | -56.1922 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c3d2be0a-791e-3365-837e-5212ea99c6f4 | -17.1464 | -56.202301 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af1787e4-5516-3011-a466-f012faf47067 | -17.148899 | -56.212399 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40ce4966-e380-39a7-a81d-2700e29832aa | -17.1514 | -56.2225 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b58efa9b-832a-3b2e-a406-7b27b2856ab3 | -17.116501 | -56.123798 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| baefd446-697d-36fa-bd30-d49bf79c4042 | -17.118999 | -56.133999 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93724f60-78c2-339c-b619-748d957358e8 | -17.129101 | -56.174599 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a99274e-14cf-3169-a7e4-98471918edf7 | -17.131599 | -56.1847 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a79020cd-e837-3be6-be66-ccc32baf645f | -17.1341 | -56.194801 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 25586312-75a0-3f4c-8ce7-600b906de271 | -17.1366 | -56.204899 | 2024-10-01 01:44:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb0a2964-bf06-3651-9bfb-427d66a3bec2 | -17.1222 | -56.230202 | 2024-10-01 01:44:37 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13161506-7da0-37c4-9246-bd21eba846a3 | -17.112499 | -56.2328 | 2024-10-01 01:44:37 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 261f0b3f-7167-3ee3-8d80-a0262049ab95 | -17.102699 | -56.235401 | 2024-10-01 01:44:37 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67eaf2ae-5956-33c2-add2-0b14d187a2cc | -17.060301 | -56.106098 | 2024-10-01 01:44:37 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f9598c1-4c2e-3158-8798-87642d2e1161 | -16.441601 | -53.9212 | 2024-10-01 01:44:38 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5b67d76-93c7-35ea-9af0-2866b9e4fc37 | -16.445299 | -53.935398 | 2024-10-01 01:44:38 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecdc93ba-f912-33e5-870e-6b0430e1234c | -16.4282 | -53.909698 | 2024-10-01 01:44:38 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5de6af3a-479f-32d5-8cd6-d8f923884bea | -16.4319 | -53.923901 | 2024-10-01 01:44:38 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fdc92baf-5959-3c17-b979-6bd4c7b3a9bc | -17.101801 | -56.6936 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc96a134-c594-3ffe-9767-eb55e2f233b5 | -17.104099 | -56.703098 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7dd64b4-7c22-3bdc-9b93-bf2f3a754329 | -17.1064 | -56.712601 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f67e5fae-3c57-3537-a8b6-af3ae11ceeb9 | -17.1087 | -56.722099 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d29afec-dbc3-3eb8-9515-e5c353b1d060 | -17.111099 | -56.731499 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c221193-47a3-324d-90fd-290adf4bb978 | -17.091999 | -56.696201 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b0070cc-462f-372d-9194-af51cde756db | -17.094299 | -56.7057 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c60421b-fc1d-3d6e-bfc8-e4c8cce464c7 | -17.096701 | -56.715199 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47a0bd8c-b071-35ac-b199-8a73fde2e725 | -17.099001 | -56.724701 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d08073c3-4e79-33f6-9a0f-274f88af856f | -17.101299 | -56.7341 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ebdf5f3-38b5-32eb-b1f8-7c55ceab82f2 | -17.08 | -56.689301 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 325f4c0e-5de7-355c-a875-19ddace2c3b9 | -17.0823 | -56.698799 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0b388c1-dd3b-3d06-b3b3-6b0a900e6ead | -17.0846 | -56.708199 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e7a34cf-9e16-3854-9ad9-18570bd84042 | -17.087 | -56.717701 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68557298-6f78-3002-b5f2-040edf3a7b02 | -17.0893 | -56.7272 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77c043f0-4752-32de-919c-3bc595dfa973 | -17.0916 | -56.736599 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0841ab83-6e09-30a8-9976-9858be97053d | -17.093901 | -56.746101 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 80a3aa8e-9970-36ae-9f2b-3e04f67d38f4 | -17.0702 | -56.691799 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1141a6d-21d0-3f5b-8e99-e92b1b67974c | -17.072599 | -56.701302 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 397b9c9e-da05-3b0e-98b0-6ff2a1e32f41 | -17.0749 | -56.7108 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52e6596b-37bf-38dd-8103-16167d27c214 | -17.0772 | -56.720299 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b21292eb-4981-3a77-ac7e-aed5a21e9145 | -17.0795 | -56.729801 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ef64d7f-0e61-3f8f-b645-06646df56cbb | -17.0819 | -56.739201 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a6ab643-c08b-34bc-82b1-7085c19d2192 | -17.0842 | -56.748699 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85ae3cb1-6e4e-3537-b9a4-7475e39d8d63 | -17.0865 | -56.758099 | 2024-10-01 01:44:39 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 25d5b12b-f03e-3f40-8514-b69dfe3337ab | -16.867201 | -55.913799 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40e7b02e-90a4-3101-9ee5-1f3fb576f804 | -16.936899 | -56.193401 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa46cd0f-d444-3e00-bc5d-d31e26e20193 | -17.060499 | -56.694401 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd854b24-619f-301c-82e5-4f8232b39b7f | -17.062799 | -56.703899 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61f45c7d-e8b3-33e1-a3a1-6d521e37987d | -17.0651 | -56.713299 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e704ec1c-8cb6-3f43-9692-d4cd102fbc5e | -17.067499 | -56.722801 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b58acafd-7563-3574-88ba-2a6699f9d404 | -17.069799 | -56.7323 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4fa8f296-7f1c-3491-bc0a-722a57762efb | -17.0721 | -56.741699 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4db3c38-48de-3870-91bf-ff469cf7ea70 | -17.0744 | -56.751202 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 18619776-b050-3eff-bcf9-91d3caa73317 | -17.0767 | -56.760601 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75649b4b-ee2b-3e1f-87d3-619e1a6baca6 | -16.852301 | -55.895199 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd8f5ce2-9b4c-3ae5-92ff-1853131d5baa | -16.8549 | -55.9058 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5016b9cf-166a-3c11-b571-2c3eefb8eb4b | -16.8575 | -55.916401 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91aadf8e-d62f-3d76-b189-991105c1a35b | -16.860201 | -55.926899 | 2024-10-01 01:44:40 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e73e9b9c-3a76-33c9-af5b-84b3b15be93a | -17.0508 | -56.696999 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17c696b1-bcff-31d3-b93f-4a8a368a5422 | -17.053101 | -56.706501 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a25788e9-6b84-395b-9739-1f93feef11ba | -17.055401 | -56.7159 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45caa184-9f6c-3025-83d5-03e0ab84e6c7 | -17.0578 | -56.725399 | 2024-10-01 01:44:40 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README26.md)
