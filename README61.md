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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 894c7452-1123-386c-8ca4-36056df2058a | -17.01966 | -55.08058 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9ec5c1bb-885f-3c3f-a710-66bf849e0161 | -17.01711 | -55.06514 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ca3cf851-acab-3a85-92e4-caa3bc06d71e | -17.01694 | -55.06232 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 904db644-4875-3420-bf3d-4a6932a3b763 | -17.01601 | -55.09726 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ca82c194-6ea5-3de1-a2ef-2029720dac19 | -17.01085 | -55.09282 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6883593f-5a98-3f04-abf7-78c05af33263 | -17.01057 | -55.06071 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50c970e5-f768-3bec-be24-3bee44580a81 | -17.00963 | -55.09564 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 478a555a-c92f-3398-a445-bda1bcba81d7 | -17.0096 | -55.09835 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f0ef0d23-7a18-3e58-9bb1-edc2d4827b3b | -16.90215 | -54.55355 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| faa5cb36-3ff5-3965-9243-0608d6ffebef | -16.90212 | -54.56602 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b2cf268-a934-3a97-882c-1bc956e2218c | -16.90117 | -54.54028 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6fcedf1-a0af-3790-baf7-235f77f1b4dd | -16.9011 | -54.55827 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 739d4f25-ceb5-36c3-9f8a-7a5da3aa0c23 | -16.90013 | -54.54509 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ff2cefd-9305-31eb-a368-00ac1b14f2b2 | -16.90003 | -54.56303 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4569e5c7-5554-3ef1-8661-4d7750c99703 | -16.89917 | -54.53768 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 69e3bf8d-5ae6-3ee5-bfb4-7e1116b203e3 | -16.89907 | -54.54998 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17d0fcc2-778d-3d65-a9b4-88aafbe127a3 | -16.89809 | -54.5425 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e6dc56d0-359c-342b-b395-a870491f1285 | -16.89801 | -54.55484 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 844414b1-c6ac-343d-bc23-941752adb598 | -16.89701 | -54.55944 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 972213c4-a8a4-36ed-8dd2-d4a27e5e6c95 | -16.89701 | -54.54734 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7fcb0ff8-6704-3ab8-af0b-aa09291c8724 | -16.8959 | -54.55227 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23f21f94-b314-3bc0-90e4-4f13bd53dece | -16.89494 | -54.53893 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71f93d50-57cb-337d-aef0-c87eb2d946c2 | -16.80343 | -54.10798 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8f1e7498-c416-399b-9b17-074b69198353 | -16.80237 | -54.11282 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3ef8242d-c55c-3316-9026-dc728212383b | -16.79736 | -54.10658 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 56d60326-2f1b-339a-9543-639e655d3d5c | -16.79688 | -54.10825 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d2fc126d-a5e3-39d3-a3e8-a1564e64f1fe | -16.79631 | -54.11138 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 37514d26-e6b6-3cab-bc7e-47c4c8cd6cd2 | -17.79192 | -53.78473 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 45069dc3-892b-31dc-bd2c-96b62afdc3c5 | -17.77435 | -53.7808 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1fc05530-c87d-3461-a8f7-d62530d1eb0a | -17.77333 | -53.78546 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c23ee9f3-6aca-34a6-b016-8bfd0de4a786 | -16.62706 | -55.56706 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c9559781-3905-33dd-a0d7-7032526c447c | -16.62563 | -55.57343 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 26c2a836-d48e-3e26-b331-2dcd9ab8ce42 | -16.62049 | -55.56528 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c2880d16-9d15-3a71-b307-71277db007f8 | -16.61912 | -55.57136 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 982ccf70-e3a9-3725-808a-1449dc87d966 | -16.61757 | -55.57826 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8d7fbe42-bcb0-33e9-ae4b-281c87320aea | -16.61614 | -55.5846 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 65871d44-9166-30a1-8c6b-75e321d8f6ef | -16.61237 | -55.57043 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1e27b9db-e329-37ca-a621-dae99f9db6a7 | -16.61095 | -55.57668 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e9027c79-bee0-3a52-b4a7-ff5099e3e988 | -16.60954 | -55.58293 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5a464f5f-fbf8-33ed-b3ce-1e0ea14269e9 | -16.60292 | -55.58135 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 40710b6b-1e08-342d-874c-c4131896d3b2 | -16.56152 | -55.91996 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| da6b1385-4846-3b07-99a8-053b6e9bde5a | -16.55479 | -55.91826 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c0c337b8-3bfb-367c-807c-af05e101f31f | -16.14037 | -55.87328 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ad816828-8adb-398a-8395-c3addc79d1a5 | -16.13358 | -55.87172 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5a2e373b-3dec-39ed-9113-9dcde188cc37 | -15.69599 | -55.77134 | 2024-10-07 04:02:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2dd54c0-e061-30bf-962e-102916e038e6 | -17.0263 | -56.6863 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 9f88db4a-068f-3504-91af-fd2a8e3895d4 | -17.01936 | -56.68447 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 8ca0c7e1-6e75-3bf2-88ca-70007a8ec2de | -17.01774 | -56.69143 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| e1b40726-57de-3a76-ae7d-60abafcca9c3 | -17.01242 | -56.68262 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 64ab3e83-754c-3bba-ac40-c28f7fd33b6d | -17.0108 | -56.6896 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 07bb51b2-defa-3b07-aa4d-011ad0dc20b7 | -17.00385 | -56.68776 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a48dd330-9fab-3c39-8ccc-c7900446cee1 | -16.97212 | -56.6135 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| beda72e6-5ecc-3dfb-92b9-2c6a4665b4ad | -16.97054 | -56.62042 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 607fb568-07e0-3f54-b532-9d575c9d484e | -16.97001 | -56.61246 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| b389c3ba-5cde-3f05-8980-e66e1d5c1aea | -16.96838 | -56.61937 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 5a722666-45c0-365b-a167-2998828cf66b | -17.15029 | -56.14887 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e80fbf37-5252-3577-a484-c82b6b2a158a | -17.14881 | -56.15533 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a8a0c512-4644-3a73-a5ae-0e68bdb093a7 | -17.14583 | -56.16834 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f97c8e3c-dbf3-3000-80bb-5c6d5d41b0d8 | -17.14057 | -56.16012 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e2cc31d0-cf79-3e68-9fd3-beda539f7af0 | -16.66956 | -55.88889 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a055f4c8-76ec-3c57-9d34-34ad079e69ac | -16.66813 | -55.8952 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1df5dc56-a7ff-35a9-83b7-ec614ae99967 | -16.66142 | -55.89348 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5d5bb0c1-891b-353e-9a3e-d7d387e67529 | -17.11127 | -56.84918 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 859d485f-2976-34f5-b2eb-498a9e704479 | -16.62101 | -55.90816 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cbc98340-573c-343c-9a72-ca31d6c3e270 | -16.61429 | -55.90648 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 00db9d0c-2a03-3dd8-8fad-60743915daf6 | -16.61287 | -55.91283 | 2024-10-07 04:02:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3d3a6430-c2dc-3f48-aab4-8ff21fa64925 | -17.1302 | -56.8315 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| db60c1d0-d861-3f9b-bf92-9518ba1b7d60 | -17.12855 | -56.8386 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d4baa661-e6fc-382a-93c9-d8fd8be7e39f | -17.1272 | -56.82981 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 56536bf8-f3b3-3b4e-9945-a2617b6bffeb | -17.12551 | -56.83689 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 92d74994-0927-3110-8d5b-641cf3ceb1e1 | -17.12383 | -56.84397 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 47839b7d-0955-3dc4-8bb4-52174bc3cad3 | -17.12322 | -56.82962 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 49e74d80-abb4-324e-bec4-1f8dfe5c2f1a | -17.12157 | -56.83673 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b4808e37-b291-384c-ba95-0891503fd127 | -17.12022 | -56.82796 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 89459725-07ee-34cc-b5e6-9677673f3bf9 | -17.11992 | -56.84385 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| e1292be8-4988-33d8-a55d-375d4b81e5d1 | -17.11853 | -56.83505 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| aa3da593-2d0a-3adf-a28d-eb1ba2a84e61 | -17.11683 | -56.84217 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f59f6d09-e5e9-33f3-b213-addc23851747 | -17.11513 | -56.8493 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 64fb1a35-8853-3ecb-815d-fbc61341703b | -17.11293 | -56.84201 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 885acd38-0f0c-3527-abac-fb9c7b5d6b8c | -17.11155 | -56.83322 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| dea8e992-32a2-30df-9b37-f0fc85980d30 | -17.10984 | -56.84034 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 25129e7f-8e9f-39c1-a4ab-35f2182b0463 | -17.10814 | -56.84746 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 607523de-9b02-35ab-9b58-5a51170bd9e1 | -17.10761 | -56.83299 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 075ad973-8e40-3933-abed-e2908a2dfced | -17.10595 | -56.84013 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5f71d405-8c77-3b34-a268-07c6447595b5 | -17.10428 | -56.84729 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b38b9e82-ed9c-300b-a341-ff4c74bd6108 | -17.10286 | -56.83848 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f05e63fe-e188-32f5-a30e-2513246b83e8 | -17.10115 | -56.84563 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1364a576-ef62-334b-9b31-1837a2b9a72a | -17.09896 | -56.83829 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c175031f-becb-397a-90ae-abf658e9d0c0 | -17.09729 | -56.84546 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| e37aecaa-b161-3b7b-a97c-6395a63834f2 | -17.09197 | -56.83644 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 274a1b30-21f6-3242-baf3-53d6a2aa68f6 | -17.0903 | -56.84358 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 2d6414c6-9441-3201-9b0b-7fe85699072f | -17.08666 | -56.82746 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 72e76ee0-9209-31ef-a23f-59f0181a8306 | -17.08498 | -56.8346 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| fea28370-18e8-3db6-89ca-a99d72a29716 | -17.08331 | -56.84174 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 9d1230aa-3bca-32f4-91df-7fc3545ba305 | -17.07967 | -56.82562 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| af599a4b-5007-3fa1-bee8-4895d8ba2810 | -17.07799 | -56.83276 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fcd8093e-b6c4-353f-92dd-787aa134cf42 | -17.07632 | -56.83991 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9200643a-a8a4-357f-b3fa-4cd71d665c23 | -17.07463 | -56.84709 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bed16e35-9ef8-3664-ab9f-75b2c7b25dbf | -17.07101 | -56.8309 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c1bab6ef-1c80-3015-85ba-393214fe975b | -17.06932 | -56.83807 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README62.md)
