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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87cf08bb-e62c-39a9-9b25-6d99add75e62 | -16.63311 | -55.51691 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 060d8856-f7e8-32b0-957e-6cec1381546d | -16.14416 | -55.92455 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 48c2e8f1-c682-3542-8b5b-43e2cc59d4dc | -15.89411 | -55.4036 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3eb3746f-4cd3-3698-aa00-54ae86c9ba08 | -16.65979 | -55.51715 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 361c2aef-9648-3dbd-a946-d6813d46f2a2 | -16.65954 | -55.54031 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 24a71cd5-3775-3f1e-bad8-644a4c5f3824 | -16.65823 | -55.52604 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cd38ff3d-d123-3570-9029-b4d407c5dd3e | -16.65666 | -55.53496 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1b2d070b-d91c-3a32-a05d-97bc99a2c498 | -16.65531 | -55.52097 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ec740dad-eb6f-34e5-b68b-d821bbcc27db | -16.65454 | -55.52533 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 43ea6236-4bbd-3e9e-99b4-18adc2fa21e0 | -16.65296 | -55.53431 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bb92cdb0-1b8c-3446-a215-9ca88d4bce85 | -16.6503 | -55.50605 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 623d078c-e2e7-3f31-9232-54469303bdf2 | -16.64842 | -55.53835 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ce4cd20f-c4c2-3869-af1d-c47fbb14df54 | -16.64741 | -55.50079 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9254d7f4-37f0-39f3-8206-d0de75866ab1 | -16.64419 | -55.51902 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f2efed4b-bb8f-3b73-9381-a7a9bb90d8c9 | -16.64259 | -55.52807 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fb165f07-7887-33e1-b240-a95a358f9f03 | -16.63392 | -55.51235 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| db96feb6-72e5-313f-8894-0ffa71cc7218 | -16.57826 | -55.91224 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a0c5c9d8-8729-3159-a3c2-f03ecd1ce020 | -16.57363 | -55.9163 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1e4c8447-cb4c-3097-afee-6183bd585e69 | -16.14505 | -55.91956 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a82ab78b-2095-3fff-9400-1d285ae921d8 | -16.13446 | -55.91279 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 172d6c08-0ffc-345d-9826-2c05abd1ea51 | -17.15402 | -56.15129 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cca613d3-6625-33c3-97b4-cd23c5e7ef04 | -17.15142 | -56.14902 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1565711f-a52a-3fa4-bb66-fa21a860f6e0 | -17.15049 | -56.17074 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a2b5d84a-8f34-3d05-a102-ffc185619433 | -17.14886 | -56.16362 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5a8de396-472b-350f-99cd-8b35aea38064 | -17.08194 | -56.67785 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f935c26e-7914-3153-a5a6-03f0b3f1a5c1 | -17.07802 | -56.67708 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| aed404d2-84a9-35f8-911a-149b45dc0439 | -17.0772 | -56.38984 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0a7fb4d8-65a3-3bce-9e6e-47e98e551726 | -17.0763 | -56.39487 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f530f28e-4c20-3f45-b906-17caa36dccca | -17.07611 | -56.68748 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ad28d48b-6473-388c-9e3d-567d899cf296 | -17.07315 | -56.6815 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1890449f-b398-35bb-8ff3-7439e0ce4658 | -17.06923 | -56.68072 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8090e717-b112-3705-81a6-069d64417600 | -17.06828 | -56.68592 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| af65ec95-3086-3e85-8567-a08a945c9a81 | -17.06138 | -56.06431 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6ca98d2e-64aa-39d4-a37c-642c8f7b8235 | -17.06122 | -56.68318 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 21f25d3e-b47f-3c39-88ec-a9fa5810910a | -17.06054 | -56.06914 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d767bc92-473a-34d1-ada7-628a4b6c5332 | -17.06044 | -56.68438 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dfeafedf-b007-3753-b700-83b396594018 | -17.06031 | -56.06624 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ee06ccf1-754a-3dd2-baa3-16eabab1c577 | -17.0603 | -56.68839 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 74de0b89-6d2c-3eaf-a620-77f318cb89ec | -17.05944 | -56.07106 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7d0b0bc9-462d-3240-9a46-fb835eb0f5e5 | -17.05759 | -56.06358 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| e2f3011d-7a87-3f62-90f9-317447d8ea94 | -17.05675 | -56.06841 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3978902a-875d-364f-8044-62df41875d35 | -17.05653 | -56.06551 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 66c119fa-089d-3a1d-8a8d-84c30d86c44b | -17.05391 | -56.07994 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fea647da-e204-3191-909e-87eb928379d2 | -17.04772 | -56.68724 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 539da838-93b8-33ec-b03a-9451de898e0f | -17.04761 | -56.69127 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 070725a0-66cc-33fd-86bd-5d9acf944574 | -17.04676 | -56.69245 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c3fc8279-c9b7-3bb9-a24e-d1bca55bbd13 | -17.04667 | -56.69648 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b4378d53-41a4-310a-a611-7ed2a5f1c23d | -17.04579 | -56.69766 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b8bd083f-bf7c-3060-8118-001d563d6096 | -17.04462 | -56.68526 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1a693db8-8616-3edf-8741-ca8a9e0d0694 | -17.04369 | -56.69048 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 917b8ddf-4ba5-3958-aaf7-d7e99ee12ada | -17.04275 | -56.6957 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 90d8f699-bf64-334d-b5f2-c259c0584050 | -17.04069 | -56.68449 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| b2071bf3-bd67-34c1-8131-fa019bbcd890 | -17.03976 | -56.68969 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 2280cf21-43b3-338e-b515-5030754c109e | -17.03883 | -56.69492 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| aade4e4d-1e58-3545-ab26-ae91328ff0c3 | -17.03677 | -56.68371 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 5eea4af2-1f77-35c9-8b58-ad023dc912a0 | -17.03584 | -56.68892 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 1143f09d-6bea-3b1b-bdd6-4d1b2465f020 | -17.03491 | -56.69413 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 914aff37-63f5-314d-a19a-a7fbe4abbc9a | -17.03397 | -56.69934 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 32769b2a-ce74-341f-ad37-dc77deff6231 | -17.03192 | -56.68813 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| 7d614832-f710-3770-a463-cb065114287c | -17.03098 | -56.69335 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| e8749d12-677c-3b65-9e7b-762cbc8f401a | -17.03005 | -56.69857 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| d2d45d53-8e28-3c9e-b86a-0c9d5ed7188d | -17.028 | -56.68735 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| 3d2a7fab-926e-30a1-9af6-b969ae967689 | -17.02706 | -56.69256 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| c32a98d2-950d-31da-8512-22e67eca3dec | -17.02612 | -56.69778 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| b9a07f18-ba3b-365b-a89d-c0c11a7fd8bc | -17.02408 | -56.68657 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 0a49655c-8874-3520-8328-bed2568865aa | -17.02314 | -56.69178 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| 87112aef-9389-34c4-a2fe-a5119ee4762a | -17.0222 | -56.697 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| afbc7dbe-3196-3769-8781-85d9f26bcacc | -17.02015 | -56.68579 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 3c969f15-5438-3b22-804c-cf6c292a1fab | -17.01922 | -56.69101 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| e34d4db4-d7d8-35e1-b877-b20b9a0b5481 | -17.01828 | -56.69622 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| f2ede05c-f3ed-3c0a-a2dd-653bdf43866b | -17.01623 | -56.68501 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| f27e1185-e380-3169-aa23-12260784e032 | -17.01529 | -56.69022 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 8fdf26d1-2523-3343-8e44-0e943fda1df4 | -17.01435 | -56.69544 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 21d4e8cf-71fd-3072-825c-4ce205cf766a | -17.01137 | -56.68944 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 313d640a-a27a-3e2a-bc0e-4f07de83ae71 | -16.98266 | -56.15432 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6665070d-d622-3de5-a7ea-eb3930482a40 | -16.98179 | -56.1592 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a8ce9d92-6308-3588-9487-ec59409e3fef | -16.97593 | -56.14795 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c9179238-5ebe-3943-96dd-ced89b370dd0 | -16.96451 | -56.14574 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 66dfbb4c-7922-366b-bd90-bd827f44d0b1 | -16.92842 | -56.59063 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7b75b2f7-731b-3aca-96d4-53f4b7d248e0 | -16.68676 | -55.49381 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b7d16266-c3be-346f-bae8-98dc517dd9b2 | -16.68093 | -55.48359 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 770e2922-4fb4-327a-ba25-9119f94fb482 | -16.67938 | -55.49246 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3592fb45-91ed-3e57-bc50-6211635898c9 | -16.67724 | -55.48292 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 96837457-ae13-3452-9b23-5fb062e84768 | -16.67645 | -55.48742 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 992c502d-b9b6-372f-99a9-8b59eb9b0962 | -16.67489 | -55.4963 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1bfe34ee-aaeb-3878-a778-93d212699af2 | -16.67355 | -55.48224 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 761cf86c-b899-3cb3-afe5-6f85f75bf096 | -16.68949 | -55.92098 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c463ca64-525d-3581-8d33-9c9d9ab7a173 | -16.6879 | -55.88615 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 32d43756-8da1-3430-a5b6-6c793c4ac42e | -16.68365 | -55.90997 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e657ba6e-4d39-381c-81ec-f5f27350a714 | -16.68279 | -55.91475 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3fd5994e-7aa5-3fc1-83d6-e4669a5a4c0a | -16.67716 | -55.54885 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fff7ef07-887e-3580-9363-9e00bd70ced5 | -16.66897 | -55.55199 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fe53ae3b-dc52-3ba3-8d9e-ce74a77c836d | -16.66771 | -55.91185 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8d6b72c5-e4ca-3d5b-867a-17a627f8415b | -16.66691 | -55.54189 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e7b32067-b099-32ab-ad90-5a1e57737af4 | -16.66609 | -55.54656 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ea7b1a1b-d4f4-3026-9c36-67b9a3aa879a | -16.66527 | -55.55124 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 4c9eff9b-a1e8-3b0d-8e62-499de50ee028 | -16.66479 | -55.90633 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f886fb35-8399-386b-81fa-9c8ca5ec2933 | -16.6643 | -55.51323 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ea708709-2f0e-3644-9065-37ddd6d2b3d1 | -16.66241 | -55.54577 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 93812843-ec94-3490-af5e-31a163795836 | -16.64884 | -55.90821 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |


[Clique aqui para ver as próximas entradas](README121.md)
