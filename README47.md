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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba5d908-bd44-34f9-a717-36368773ca23 | -10.6446 | -55.8938 | 2024-10-09 01:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4488d958-1d58-3852-acd3-6d03bff734fb | -10.8567 | -63.9177 | 2024-10-09 01:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e0d532cf-0881-3378-a3d4-306d978b18e5 | -10.8754 | -63.9169 | 2024-10-09 01:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 75e9aa6e-d3c0-3854-b6f4-33c4947fdc6b | -10.8755 | -63.8979 | 2024-10-09 01:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 92855cd8-36de-35ee-8537-3a65245d68cd | -10.8941 | -63.916 | 2024-10-09 01:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ceeaf437-f629-39c6-bf4b-5e8ebdbd3167 | -10.9112 | -64.1615 | 2024-10-09 01:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 0f8c64c7-f2af-344a-862f-b26835fe32c6 | -10.9113 | -64.1426 | 2024-10-09 01:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 120.0 |
| ab59dfec-118d-320b-ae27-3b1b14f12b9c | -11.5726 | -58.9619 | 2024-10-09 01:36:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| ab4bb4c3-e97d-3b89-bc21-316600b62af7 | -11.6806 | -64.0312 | 2024-10-09 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4e49a7ed-17b5-39ad-8202-bf409a2ef39c | -11.992 | -51.0553 | 2024-10-09 01:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f70b4026-8ece-3971-a24f-7648ab73f68b | -12.0107 | -51.0744 | 2024-10-09 01:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f47cee63-e4be-3686-9ea6-180d53fe10ad | -12.011 | -51.0531 | 2024-10-09 01:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 39dc12c0-f1f8-3f89-a0a5-475daa6fd7e1 | -12.6676 | -63.0819 | 2024-10-09 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 450cc695-1015-3a79-8993-4efa991946d3 | -12.878 | -62.8007 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 13d03729-e2e8-36af-b1cc-96faf3bb8460 | -12.8782 | -62.7815 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 46bfda41-5671-3950-baab-55c0c8034687 | -12.9166 | -62.7214 | 2024-10-09 01:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9034207b-24b2-3b1d-bf22-6c4494c33dc0 | -12.9377 | -62.4697 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bf677e1b-b1e5-368b-9872-246a6fa2636c | -12.9378 | -62.4504 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b33018ae-a2b0-3020-ba2a-fbf0c383dba6 | -12.9566 | -62.4685 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 79c91ea7-8502-3e2b-937e-704d9f37ce87 | -12.9568 | -62.4492 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d6728f37-efed-3432-b16b-2308973bb786 | -12.9756 | -62.4673 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 47a5b786-319c-30cf-b534-485adb879a86 | -12.9757 | -62.448 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a761089c-79df-33c8-876f-ca2d5aead1b5 | -12.8591 | -62.8018 | 2024-10-09 01:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 104.9 |
| e3767a44-065e-3aab-a96e-50e0776d1034 | -12.8779 | -62.82 | 2024-10-09 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 80b9fc46-5c4d-39e2-b9c2-492323ab67a9 | -13.8364 | -44.5927 | 2024-10-09 01:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 30a1f114-a1e6-3386-88e8-975edbfb0703 | -13.8369 | -44.5691 | 2024-10-09 01:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a4213039-ef45-369b-a3a0-99193812d746 | -13.8564 | -44.5657 | 2024-10-09 01:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6721a2f8-ceb7-34fc-8ee6-1d42dff4cf95 | -14.1192 | -44.9872 | 2024-10-09 01:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 005d72de-9c9f-3c9b-97a1-f24c5fa99f08 | -14.1197 | -44.9637 | 2024-10-09 01:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 0d2918ca-711e-305c-a7fd-b120c7a6935d | -14.1387 | -44.9837 | 2024-10-09 01:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 70e41e98-cd43-32b1-b0c6-655333c6918a | -14.1392 | -44.9603 | 2024-10-09 01:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 1a304c79-a994-32c7-a77e-6160fd8dcf3d | -14.1397 | -44.9368 | 2024-10-09 01:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5ea7bc43-366a-33d0-9b7d-d227ef61e788 | -15.5996 | -57.3699 | 2024-10-09 01:36:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| e560963e-574d-3155-83c1-e8eba2fb7c43 | -15.5999 | -57.3496 | 2024-10-09 01:36:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5e61aa5f-4728-3d18-9445-f906d8faea03 | -15.6791 | -52.5206 | 2024-10-09 01:36:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a8b27af7-b617-3d85-b5be-e14a6b658179 | -15.6795 | -52.4993 | 2024-10-09 01:36:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7c65f80d-548c-33e7-b057-058be9bd6a32 | -16.4184 | -55.9455 | 2024-10-09 01:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 663bb01a-ba1c-34b0-919a-59c0597f0bc4 | -16.4187 | -55.9248 | 2024-10-09 01:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| df73ca4b-82ef-3492-9a0d-64c13b5d2cca | -16.6871 | -57.4536 | 2024-10-09 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| d16c886f-7714-3f85-8bc6-29f8f9c769de | -16.7067 | -57.4514 | 2024-10-09 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| fa50f3c1-474a-3c24-bc5c-c1fbc067fb92 | -16.7849 | -57.4425 | 2024-10-09 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| dfbef0c6-44c1-39bb-973e-d2b8c4e37ff9 | -16.8045 | -57.4402 | 2024-10-09 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 95a62833-8780-3367-84bd-398c41f8e2a8 | -16.8048 | -57.4197 | 2024-10-09 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| c3820a2c-c5ff-3436-b4b8-0a61d8afcd51 | -16.8241 | -57.438 | 2024-10-09 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.4 |
| c0d530b8-908b-369b-9277-a45237c63a5f | -16.8244 | -57.4175 | 2024-10-09 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.5 |
| 1820b344-4cd0-3473-8404-5adf4c7b3a85 | -16.8898 | -55.8039 | 2024-10-09 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| e7bfdfcf-cf05-33f1-8ebe-977f856ba253 | -16.8901 | -55.7831 | 2024-10-09 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| b28a1dd8-7b08-3b65-8729-bf9ea8c111b8 | -16.9091 | -55.8222 | 2024-10-09 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 913eff60-2ebe-35db-afed-a3a7eabe206d | -16.9094 | -55.8014 | 2024-10-09 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| aa5e0313-b1bb-3d73-a145-657aba36c03f | -16.9098 | -55.7806 | 2024-10-09 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| ea404899-6382-3275-9d32-03b312ccae6c | -16.929 | -55.7989 | 2024-10-09 01:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 01530884-9be5-3a99-9012-fb6e5aebfdce | -16.9518 | -56.7875 | 2024-10-09 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 1ec1ab0a-6115-3c6b-b4a5-c5607e4afcd8 | -17.1467 | -56.8463 | 2024-10-09 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 86df5ca5-9b0e-3136-a175-c1286dd41a37 | -17.1588 | -56.1222 | 2024-10-09 01:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 42b46be6-d791-3f8b-baa8-b07004feee90 | -17.335 | -55.0366 | 2024-10-09 01:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| b593715d-ac7c-3d31-b942-05f3fbcfaa32 | -17.1271 | -56.8486 | 2024-10-09 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 4e1e6bdf-2948-3a62-8bdf-7faf654396d8 | -17.3353 | -55.0156 | 2024-10-09 01:36:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 5be7e1d3-b55f-3527-aea7-1b84a1aedd32 | -17.3547 | -55.0339 | 2024-10-09 01:36:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 94559374-4816-3aed-bf9c-34cf2c47b25f | -17.3551 | -55.0129 | 2024-10-09 01:36:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |
| 478fbfc6-4da1-38c2-9f40-fe69a6992ab3 | -18.1193 | -56.3921 | 2024-10-09 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 2e7a946c-108c-3af0-9de8-89e59925b0f4 | -18.5993 | -57.2629 | 2024-10-09 01:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| c6cdfddf-455c-3da2-876a-f382db54151c | -18.5996 | -57.2422 | 2024-10-09 01:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 151223c6-3b72-36af-acd2-1afd97efb2ab | -18.6991 | -57.2293 | 2024-10-09 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 2902dc80-d21f-30b0-9aa0-21fb052bbff4 | -20.2915 | -43.9444 | 2024-10-09 01:36:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 17aa6531-557e-3adb-a01b-8dd1097fe9f0 | -20.3346 | -48.7307 | 2024-10-09 01:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 390.8 |
| e5c6b2c5-43f7-3d27-b87f-02c01e6f5a9a | -20.3352 | -48.7076 | 2024-10-09 01:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 446.8 |
| 76be7e2a-7965-3749-a7f6-8bbc9e1f8e32 | -20.3551 | -48.7262 | 2024-10-09 01:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 585.7 |
| d424fbf9-1311-3201-8ea4-e33ad950b03f | -20.3557 | -48.7031 | 2024-10-09 01:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 592.9 |
| 4942065c-f461-398b-b323-d5d72b1b2f62 | -20.3755 | -48.7217 | 2024-10-09 01:36:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 2d1891dd-4f9d-3d06-a833-9a0996fa7227 | -20.3761 | -48.6986 | 2024-10-09 01:36:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4c7554a4-5f9f-3c2e-88ea-ca51ede0d07c | -20.7839 | -47.2559 | 2024-10-09 01:37:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 7f199acb-73b4-3aff-bcd5-b359f61f0e18 | -20.7846 | -47.2323 | 2024-10-09 01:37:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 133.3 |
| ab3bc918-ef63-3014-807e-76690d9bc176 | -20.8045 | -47.251 | 2024-10-09 01:37:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c6a94b7c-b42a-3204-a504-9ba02fe69117 | -21.0926 | -47.2043 | 2024-10-09 01:37:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a5986b56-5b4c-3d3b-b8aa-338de1ee325a | -21.572 | -46.9898 | 2024-10-09 01:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 28133d4e-a9e8-38f8-bf85-b47f7366d84b | -21.5727 | -46.9659 | 2024-10-09 01:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 94174f99-5aa7-35ef-9863-0099e1394240 | -21.5864 | -47.8827 | 2024-10-09 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 6704e89f-b6a2-3b68-be65-c8c4bd8eca1f | -22.8137 | -48.4225 | 2024-10-09 01:37:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2f9fe75c-8d2b-3336-a87e-4f8b39e5ffb6 | -1.11 | -53.6173 | 2024-10-09 01:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d3e4360f-15f5-3899-82e3-aa711a3a70a3 | -3.8007 | -41.6229 | 2024-10-09 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| f338c851-662d-3ba4-bd5c-7feb1ddb7a35 | -3.8008 | -41.5989 | 2024-10-09 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| f3e60a6b-469a-3cfc-be58-24486c5b3469 | -3.8196 | -41.5979 | 2024-10-09 01:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| eefee629-fbc9-3a74-a18a-0b48cb14843a | -3.9021 | -46.4689 | 2024-10-09 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4c281c31-21a9-361c-b896-f1c6e52007a5 | -3.9023 | -46.4467 | 2024-10-09 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f9920797-6db1-3f58-8626-98dc6ecf3b43 | -3.9207 | -46.468 | 2024-10-09 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 79b0078d-aa67-3847-9bfe-b4d1ac2e83eb | -3.9208 | -46.4459 | 2024-10-09 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 8c97886f-1ca2-36e9-8349-3a9c4dc2512f | -3.9393 | -46.4672 | 2024-10-09 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 34d3e1ce-481e-34c7-b6f9-a4b3eeba6d2a | -3.9394 | -46.445 | 2024-10-09 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 4ddcbcdf-afc8-3377-abac-a602eaaf8ad1 | -6.7613 | -60.0751 | 2024-10-09 01:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2e6d5512-8a12-3965-8635-ad8bdc15a7e6 | -6.7614 | -60.0559 | 2024-10-09 01:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 223.8 |
| 0646a0b2-4334-3f9d-a81c-b4489cd4bbfa | -6.7615 | -60.0367 | 2024-10-09 01:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a12b29ba-679d-308e-b521-e192a627b225 | -6.7798 | -60.0552 | 2024-10-09 01:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 73616025-4a56-312f-bbaa-18fd70481f20 | -6.7799 | -60.036 | 2024-10-09 01:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| bf97641a-baea-3016-83ce-9de592006d03 | -7.1871 | -59.7893 | 2024-10-09 01:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 931b3a8b-1704-37ed-95a5-7b4f5d4756c1 | -7.1873 | -59.7701 | 2024-10-09 01:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 158665b4-b1e9-3f53-9101-65827f582048 | -8.3403 | -44.1195 | 2024-10-09 01:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 782ce986-85f7-3b27-b58d-ed1589d3ac1a | -8.3406 | -44.0963 | 2024-10-09 01:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 3f575778-3036-34c9-a355-69aac8e68572 | -8.3592 | -44.1174 | 2024-10-09 01:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 4f7be6d4-cac6-3d7b-9c7e-f737586d904e | -8.4919 | -48.6476 | 2024-10-09 01:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 185ba3a2-710c-37a8-89b3-1b3d882aa8d8 | -8.4921 | -48.6259 | 2024-10-09 01:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 97.0 |


[Clique aqui para ver as próximas entradas](README48.md)
