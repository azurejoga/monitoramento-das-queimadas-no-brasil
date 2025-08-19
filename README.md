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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b22abd0-d34a-3114-9bfe-117d7c69ac91 | -9.1894 | -59.6558 | 2025-08-19 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8773c72e-ce33-3c41-995c-2b38c0f0cae3 | -3.982 | -42.516 | 2025-08-19 00:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 239.9 |
| 2c78f241-4a71-3f6b-a5b2-245bc83e3ef1 | -12.6729 | -45.8052 | 2025-08-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 3acfe310-5516-37e2-8f39-81c8c4089212 | -12.9778 | -56.8614 | 2025-08-19 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 63d42250-14f6-3939-a575-3d1bdd88fbd9 | -6.9527 | -43.585 | 2025-08-19 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| ea2175b5-ae37-3b9e-b0ac-db24051222fa | -9.1897 | -59.6171 | 2025-08-19 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4945fcf4-51a5-3a43-a53b-ecacb48e536e | -13.2563 | -50.8162 | 2025-08-19 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| ce4cba3e-1132-317c-98ed-560c8611dcc8 | -6.9712 | -43.6066 | 2025-08-19 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| acbb656c-0bf5-3ce6-8401-2c109d264eee | -8.6283 | -67.2705 | 2025-08-19 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| b75e9bbd-dd99-31ab-8cd1-a36a0ba745fc | -5.7887 | -43.6134 | 2025-08-19 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a4e53d5e-4457-38e2-b15d-c1fc5f940445 | -9.1709 | -59.6374 | 2025-08-19 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 848ba258-015b-3759-8586-15ee1126ea91 | -12.6725 | -45.8282 | 2025-08-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 0249c16c-e869-3690-88af-383f1abcc938 | -9.5616 | -47.4032 | 2025-08-19 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 7c42cc89-fe67-3802-945b-1ec9b5505721 | -9.5802 | -47.4233 | 2025-08-19 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 10775525-2d84-3cfe-b9bb-009564bb784e | -6.9524 | -43.6083 | 2025-08-19 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 2df3fa3e-e677-3640-a178-46132a463184 | -13.0162 | -56.8378 | 2025-08-19 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 985dcffe-9f44-39bd-9364-e0e22e6f4595 | -5.8807 | -48.1125 | 2025-08-19 00:00:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 49f88884-7464-3e5e-af95-ada00982e453 | -6.7494 | -41.5437 | 2025-08-19 00:00:00 | GOES-19 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 199da54b-6e71-3c9f-a5c2-78a2585564ce | -14.507 | -45.9396 | 2025-08-19 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| a55e216e-4c4b-3d33-8a71-54be966e42c6 | -16.4857 | -45.0939 | 2025-08-19 00:00:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 284460cb-0da5-37c1-89be-9c02409d0c6a | -14.9812 | -54.7951 | 2025-08-19 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b02bb5a3-bfc3-39bf-8bf8-aeae160dfe95 | -16.4863 | -45.0702 | 2025-08-19 00:00:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f546fe40-69d0-35b2-b21b-ec4d0b7d808a | -9.1895 | -59.6364 | 2025-08-19 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 534ea1cc-6a9f-32ae-a145-4fc56a1b5560 | -7.2989 | -46.2897 | 2025-08-19 00:00:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7cc15b94-a084-39f1-b8e6-373ec8db2391 | -3.9822 | -42.4924 | 2025-08-19 00:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 8ea8249a-50c5-3694-ac51-122afccf3338 | -9.1708 | -59.6568 | 2025-08-19 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7f413c66-ae76-372e-a9ac-1f97b6899094 | -12.6532 | -45.8312 | 2025-08-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f03bc037-5708-3f3b-be84-9bbdc73497eb | -6.9336 | -43.6101 | 2025-08-19 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 7cf0f85f-887b-3d3a-9974-7e8ee52a431e | -6.9339 | -43.5868 | 2025-08-19 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 2a1a0e80-2c3f-3e71-942b-8000346efb4f | -7.2602 | -50.1613 | 2025-08-19 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| fbd7283d-9f3a-3071-a1e0-7fb528cc8cf3 | -9.5613 | -47.4254 | 2025-08-19 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4e49600b-ce46-3153-9ef4-ae702ace1ed4 | -14.9809 | -54.8158 | 2025-08-19 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9b834248-08ee-3db2-8189-e3a19ca38163 | -6.9715 | -43.5833 | 2025-08-19 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 61ce241c-9198-3fcd-95b2-2444f2e49224 | -9.5805 | -47.4012 | 2025-08-19 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 1485ef17-4b11-384a-98d0-adb7094ebe0f | -13.1746 | -54.9337 | 2025-08-19 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f23f35a3-48ef-3017-8d35-be070770bb69 | -3.9819 | -42.5396 | 2025-08-19 00:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 052bf730-1d4a-3c4b-9f3a-37707a85b439 | -12.6536 | -45.8082 | 2025-08-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 39ff6fe1-6528-3c28-9393-329d75d03d78 | -12.9971 | -56.8395 | 2025-08-19 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ebf8513e-8eba-3ea8-b5cf-a24163436086 | -12.6536 | -45.8082 | 2025-08-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 271.0 |
| 01e2618b-0201-3cd4-af8a-eb06d17b72fd | -14.507 | -45.9396 | 2025-08-19 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 77d8868f-55d3-3bab-ac9c-4a2b235cfb8e | -9.1708 | -59.6568 | 2025-08-19 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 38ce5fad-a446-38be-94ca-115addb28596 | -5.5785 | -44.0914 | 2025-08-19 00:10:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 14de5581-016a-30a1-a732-e66956233015 | -7.2989 | -46.2897 | 2025-08-19 00:10:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 07aa1066-a065-317c-8893-570ac2f46ac3 | -12.6729 | -45.8052 | 2025-08-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| be120d0b-f486-3e3e-9234-89605d9d39a4 | -16.4857 | -45.0939 | 2025-08-19 00:10:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 4319a667-0c52-3b88-8530-528072194c62 | -12.6532 | -45.8312 | 2025-08-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| c9eef811-0bc2-3475-9fd9-6a9838730bc6 | -6.9715 | -43.5833 | 2025-08-19 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 409d83a7-5420-3ceb-8e8c-8a8a2f9dde61 | -9.1709 | -59.6374 | 2025-08-19 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d8e47b70-b61b-3faa-92fc-863137b0a6ec | -3.9822 | -42.4924 | 2025-08-19 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| ce89a43b-c608-38c7-a307-d918954bf9d2 | -6.7494 | -41.5437 | 2025-08-19 00:10:00 | GOES-19 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 6171568e-75b2-3b56-a04c-28e025f22856 | -7.2789 | -50.16 | 2025-08-19 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0880345c-b766-3d42-84de-4c92ce07f914 | -12.6541 | -45.7852 | 2025-08-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 165517ca-ef8e-38b3-8e62-26c9c3884b90 | -12.9778 | -56.8614 | 2025-08-19 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6e67a510-6b8b-3705-b451-982ead6608f9 | -6.9339 | -43.5868 | 2025-08-19 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 80cab649-2fb8-30e4-a0a5-e71ea6cfc6be | -5.8807 | -48.1125 | 2025-08-19 00:10:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ce848f57-7576-333d-a065-2d40e5971219 | -9.5351 | -63.5771 | 2025-08-19 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| fddc658b-6f87-340c-81ba-03623bda91c5 | -9.1894 | -59.6558 | 2025-08-19 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c2edd087-3493-3933-89d9-6a8ba0d9cf41 | -3.9633 | -42.517 | 2025-08-19 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 04fb8750-a23b-3858-a6c3-4c53ed99bc4e | -6.9336 | -43.6101 | 2025-08-19 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| d3281864-7cc5-3c06-9cf5-f17ee8facc91 | -13.2563 | -50.8162 | 2025-08-19 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9bd3105c-28b4-32c5-b671-21950bd1c1e8 | -13.0162 | -56.8378 | 2025-08-19 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 73a69f43-7f7c-3a62-89b9-c8fcf1e8402b | -6.9527 | -43.585 | 2025-08-19 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| c925d1f0-e03a-31e3-91c2-2cd61de5655d | -14.9812 | -54.7951 | 2025-08-19 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e986e23b-4537-3645-86bd-014084b93822 | -12.9971 | -56.8395 | 2025-08-19 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b139f883-7a56-3100-8ebc-098665af60f0 | -9.1895 | -59.6364 | 2025-08-19 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 80760e3a-7312-36b3-9981-6f1c021460cf | -7.7807 | -66.9577 | 2025-08-19 00:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 5f2456f1-1f96-38d4-b62a-b5a253b90f65 | -16.4659 | -45.098 | 2025-08-19 00:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| bde05777-2c9f-3994-b9e3-d7c6c3ee0cd4 | -3.982 | -42.516 | 2025-08-19 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 254.0 |
| f79d9233-78c4-3293-a969-cba02021ec49 | -13.1558 | -54.9151 | 2025-08-19 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d758b990-8b4d-371e-82ae-a1a0d1044e07 | -12.6725 | -45.8282 | 2025-08-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 63d19108-677e-3aef-85e0-de03aa147f1f | -7.2602 | -50.1613 | 2025-08-19 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 3392f291-a231-3570-a071-23b18d28ce5a | -4.0007 | -42.5149 | 2025-08-19 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| c857f068-74c6-34f1-8ffb-acfe1bafceff | -6.9712 | -43.6066 | 2025-08-19 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| f9e9cfd9-f574-34f2-9a29-a40397f2d589 | -5.7887 | -43.6134 | 2025-08-19 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| da807e75-0db5-3471-ba03-58f320e54a7d | -11.8702 | -51.578 | 2025-08-19 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 85bc8b1d-c42a-3fae-a8d3-c7996bfaf0c7 | -3.9819 | -42.5396 | 2025-08-19 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 73510fd3-0b4b-3ffc-8714-8c807f8c4e2a | -6.9524 | -43.6083 | 2025-08-19 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 44a45eb3-e734-35c7-9d2d-dee79bb2ed19 | -11.8702 | -51.578 | 2025-08-19 00:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 201.3 |
| d60c8e4e-7db8-3c0d-8fe4-819504c3edd5 | -12.6532 | -45.8312 | 2025-08-19 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5ae5f900-9a26-30f0-811b-766e5de97255 | -5.5787 | -44.0684 | 2025-08-19 00:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 04c22f94-4f76-3a7f-8394-7d5adee3628e | -6.9712 | -43.6066 | 2025-08-19 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ccae34df-3e31-3dc4-ad60-56c221d63475 | -6.9715 | -43.5833 | 2025-08-19 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| bd693751-dba2-3321-a5db-63d5db264b28 | -13.2563 | -50.8162 | 2025-08-19 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ac01a972-3408-3c44-b195-28ffda278a36 | -6.9339 | -43.5868 | 2025-08-19 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c38a950f-0f77-3ad2-afb9-cb3d2af1a438 | -9.1708 | -59.6568 | 2025-08-19 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 73ee346a-2d8d-3c87-adec-f7678d1977c1 | -9.1709 | -59.6374 | 2025-08-19 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8c865221-072c-3230-8540-612a03a0451b | -3.9819 | -42.5396 | 2025-08-19 00:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 132.7 |
| b83bbc9a-50d5-30ed-85c5-e0e76adbfe69 | -14.9812 | -54.7951 | 2025-08-19 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f7ac30fb-a93c-3b45-9faf-4de8ee5eb2d4 | -16.4857 | -45.0939 | 2025-08-19 00:20:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 564746b0-4c69-3c3a-984c-cc26ee71f5eb | -6.9336 | -43.6101 | 2025-08-19 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1745d1c6-15df-388a-a07f-d88a372d6127 | -4.0007 | -42.5149 | 2025-08-19 00:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| b3901ca7-0e16-3878-9953-44077f45a9f5 | -7.7807 | -66.9577 | 2025-08-19 00:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| d7f64053-5b33-3dbf-b843-d617a06f4bf5 | -16.4863 | -45.0702 | 2025-08-19 00:20:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d2a1024f-e3fa-3484-8044-0baa30669153 | -9.1894 | -59.6558 | 2025-08-19 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1f1f2121-d9fd-301e-b461-362257a2aece | -16.4665 | -45.0743 | 2025-08-19 00:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a9f4d266-f8c6-3fa2-9f82-159c363e2c0d | -3.982 | -42.516 | 2025-08-19 00:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 324.2 |
| e2ea6cac-da04-34f7-9c28-8446f29b88f1 | -6.9527 | -43.585 | 2025-08-19 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 130f7776-970d-35f8-b7bb-78bb13557987 | -7.2602 | -50.1613 | 2025-08-19 00:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 414868ba-2bac-3352-aaa2-cb751366a7be | -3.9633 | -42.517 | 2025-08-19 00:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| ff67f2ca-8d25-3907-b21d-e8cfc7c21335 | -9.5351 | -63.5771 | 2025-08-19 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |


[Clique aqui para ver as próximas entradas](README2.md)
