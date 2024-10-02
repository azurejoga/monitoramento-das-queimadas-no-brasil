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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 175f55d5-0dee-39e7-b017-368edece434d | -17.1036 | -56.117001 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37557fb0-54ad-36ff-8973-54ed94ac0b44 | -17.0907 | -56.105 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66e27446-f487-36a8-aa59-49ec196da496 | -17.0923 | -56.112099 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4b920f2-5ce3-3d4a-9e5d-483683bcbf07 | -17.117599 | -56.2271 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9df37702-de9f-3d0f-8c95-17a22f95b5ec | -17.1192 | -56.234299 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8541460f-4433-33cd-bb29-26738b6e1a88 | -17.0762 | -56.085701 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0833f39-aa8a-3bfd-a2a4-242599c73748 | -17.077801 | -56.092899 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c319571-483e-3fdc-b6b8-48c028e40399 | -17.079399 | -56.100101 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3012b88c-13f7-35af-8258-dbf3e66c1569 | -17.0809 | -56.1073 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c564aa4-46f0-3a8b-9e45-b71f0f5020cf | -17.0825 | -56.114399 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12ffb0fb-cebc-3929-a31b-2e2e9ca092c5 | -17.084101 | -56.121601 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8e97b2e-b8ba-3295-9336-b79666880653 | -17.1063 | -56.222198 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abdd4032-962c-31e1-b79d-85cad3e34206 | -17.107901 | -56.229401 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a7073c8-8852-3fcf-be73-6469e3fbe599 | -17.109501 | -56.236599 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 342f295e-649c-3865-8b40-414ec1b3b637 | -17.111099 | -56.243801 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca2634ee-387b-3710-8853-dd569fd9cee6 | -17.0648 | -56.080898 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eecc0c58-6b60-3881-aa56-2c84d8d0fa66 | -17.066401 | -56.088001 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f77988ad-e0ff-32c1-b625-52d42cb3887d | -17.068001 | -56.0952 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d914c4f2-4507-3829-b491-7fe230f6ff63 | -17.069599 | -56.102402 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32d8ff72-1860-35df-8763-d6065641525e | -17.0711 | -56.1096 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00d06cf6-a709-3535-91f0-dc7521d1de27 | -17.072701 | -56.116699 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f0444232-3a9f-37f4-914c-3fa93f271b61 | -17.074301 | -56.123901 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cfc012d3-bd6e-3c74-a13f-c4ccf409b35b | -17.093399 | -56.210201 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1fc34ad-b749-3037-805a-a4942a89b5d9 | -17.094999 | -56.2174 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8070d66b-feba-3ca9-8f8e-e7123e5506d9 | -17.0965 | -56.224499 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d97b767c-b71c-36b6-8194-e2e0b04802bd | -17.098101 | -56.231701 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f965a6a-917d-3e52-ba34-29f708391e5d | -17.099701 | -56.238899 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e86b565e-a53b-3191-a197-9b2610cce465 | -17.055 | -56.083199 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4019807-e27f-3c76-a961-a9f5a7b3b824 | -17.056601 | -56.090302 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ec0ebf4-4260-37e2-8166-d433f9bd1f9d | -17.058201 | -56.0975 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa80f5aa-0180-3cda-8f63-a3866488d57d | -17.059799 | -56.104698 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7ebaaaf-005a-37ee-84e2-31d860e42792 | -17.0804 | -56.198101 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b43f7799-80e3-3f7d-ac82-666d5ac00649 | -17.082001 | -56.205299 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7985f3d-d06e-3951-9f5c-c4d1e566a29f | -17.083599 | -56.212502 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0d3ceeb-fc5a-3c87-817f-6479e7c51daf | -17.085199 | -56.2197 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba5ba87a-246a-31aa-9e7f-08064727fd1f | -17.0867 | -56.226799 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e66259a-4374-344f-b345-87a0b05d091f | -17.070601 | -56.200401 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c286817-9d3d-314c-b9e0-6b43722fc09b | -17.072201 | -56.2076 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f432c5df-50e4-3b76-b019-d4f700c091af | -17.111799 | -56.387699 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08346379-5d77-3858-bc15-7f4103550553 | -17.1134 | -56.395 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9978376f-d135-3798-a1df-22e86acf4926 | -17.115 | -56.402199 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| add9e5ce-b6ef-325a-99c2-aaa12e6fa9dd | -17.0777 | -56.373001 | 2024-10-02 01:23:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99f08124-febc-37ee-bbf7-34f00a4c392f | -17.0793 | -56.380199 | 2024-10-02 01:23:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a5ea6ab-164f-30d6-9c18-a53e39dab7e4 | -17.0679 | -56.375301 | 2024-10-02 01:23:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d4d7ff2-1962-317e-b069-95e88348883f | -17.0695 | -56.3825 | 2024-10-02 01:23:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1dc8935-b985-356b-89d8-05d647e8b333 | -17.136 | -56.733601 | 2024-10-02 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82b4387b-c35c-3a9f-a189-ac8c81e3a3c0 | -17.1376 | -56.740898 | 2024-10-02 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f2eaa78-1248-3fd6-af60-3530675ed9ae | -17.124701 | -56.7286 | 2024-10-02 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ceaeb8cb-91d5-3dea-b7e4-9959c61ca525 | -17.126301 | -56.735901 | 2024-10-02 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 543ab1c1-fab8-3437-9c4e-f348e435d302 | -17.127899 | -56.743198 | 2024-10-02 01:23:51 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d08339f8-4766-322a-a3e4-e9010b746e3c | -17.105301 | -56.686901 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7df51421-9c5f-31f3-a462-4bc8d38345ea | -17.106899 | -56.694199 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8714b7d-5cf1-3678-8ef3-1513b66c5827 | -17.114901 | -56.730801 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce744d79-a335-350a-9fef-0c5e61e72669 | -17.116501 | -56.738098 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45b64be5-ae16-3021-9d41-271023d251de | -17.097099 | -56.696499 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7a14c3b2-0476-3097-95ae-0b3295b59dad | -17.0987 | -56.7038 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 846e36fe-5b24-35a3-9d67-f96e9f496ae8 | -17.1003 | -56.711201 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f75a5fee-3af4-30f1-b5fc-bb4a6a622245 | -17.1019 | -56.718498 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb9de7e6-c94b-39f2-a025-72f2c7dd1577 | -17.1035 | -56.7258 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7125365-2bc6-3f41-b027-6c975e0bf7c5 | -17.105101 | -56.733101 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90196686-d5fb-385d-a1d6-cf5885c48b9c | -17.106701 | -56.740398 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3b6a720-c852-373c-9573-17ce4918f805 | -17.108299 | -56.7477 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ebf1250-df56-3f18-bc6c-27a35b2bc048 | -17.1099 | -56.755001 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| feeefbd6-cfca-39ad-8a05-9f7956dd5ec9 | -17.087299 | -56.698799 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0fe5758-9c36-372b-83c4-8e1ff6545959 | -17.0889 | -56.7061 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d738457-1277-3b7a-a71f-938368d07a11 | -17.0905 | -56.713501 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d960cf95-f04e-3544-8aee-e02f3f925b88 | -17.095301 | -56.735401 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 064e8aa8-2b43-379b-a427-abf20f9cdb45 | -17.096901 | -56.742699 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb2c7220-caf3-3f0b-8cca-95a6573376d4 | -17.098499 | -56.75 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c57681f5-29b8-311f-8d26-ced99b8308a5 | -17.1001 | -56.757301 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8528b5d-31b3-3a4e-849d-9aa5ef6e3749 | -17.1017 | -56.764702 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea6bf612-f17c-3415-aa34-29ab64af060c | -16.886999 | -55.8368 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c13b30bf-808e-3c58-92e9-a0fe887335d9 | -16.888599 | -55.843899 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 444fc9b0-9e8e-30cb-b515-f18a82907856 | -16.968 | -56.201801 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8ba647a-d9b3-3c1e-b0a5-f115a452cdde | -16.969601 | -56.209 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6176b60-87d2-3df4-8adf-c7e212e0dc7b | -16.971201 | -56.216202 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97877c4d-058a-3555-8b66-2432253fc7ed | -17.075899 | -56.693699 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3600fcab-38a2-3edc-9746-e74b1d0d119d | -17.077499 | -56.701 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 188e1db4-6605-3f1b-88d7-7929098e7f20 | -17.0791 | -56.708302 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df2380ea-c8aa-37d5-a3e6-230becf9d5a3 | -17.0807 | -56.715698 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca223e58-d9e1-3229-997d-28033300653b | -17.085501 | -56.737598 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be36a3fe-9498-381c-a04b-4f6ba5dda34c | -17.087099 | -56.7449 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 63096e4b-cb21-3083-b5a7-3998ad3cd49d | -17.088699 | -56.752201 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0dc2524-9e31-3d18-9e99-b85afcaa921c | -17.0903 | -56.759499 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50d92ee7-b140-3406-9a7e-eaa8226dc697 | -17.0919 | -56.766899 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d1bccda-1223-3d99-afc0-6841b85a1624 | -16.8741 | -55.824799 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17a59067-ae52-3d96-829f-9147555bd468 | -16.8757 | -55.832001 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7344bab-69bc-3eaf-9337-5bb9d3940295 | -16.8773 | -55.8391 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2cff6f14-b0b6-376a-8b7f-f45d13cfcc93 | -16.878799 | -55.846199 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1cf1bb2c-cfc6-3c93-9499-0e585083a82c | -16.9566 | -56.196999 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df4ec15a-eeae-3c46-abeb-80dc17118708 | -16.9582 | -56.204102 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1cc513c-5d92-381d-bacc-af331ef6bf06 | -17.0646 | -56.688702 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f640aad6-f225-3d8a-b351-9b15a12b7322 | -17.066099 | -56.695999 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51286868-2556-37ad-961b-50561ff42d3c | -17.067699 | -56.7033 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a716c9f3-5b15-3b68-af39-cc9bf2ec946c | -17.0693 | -56.710602 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef7f4146-96ed-39df-8002-5a30797a273e | -17.078899 | -56.754501 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5beaba2-b526-3bf2-92cc-d4aeffe99f9f | -17.0805 | -56.761799 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9da8bde9-beba-38ff-8f02-11535dda6bd1 | -17.0821 | -56.769199 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51a59b7d-3857-32f2-888f-6bf7666fa283 | -17.2124 | -57.372101 | 2024-10-02 01:23:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 273d1866-3e37-32bb-b4cd-6d599a2677af | -16.8643 | -55.827099 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README23.md)
