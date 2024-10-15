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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9c34bfc-f8d8-31e7-8bb9-be2915cd0eff | -8.20058 | -55.21071 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22926110-c468-397d-8b33-24b5df5b4531 | -3.521 | -55.43658 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53840dc9-dc29-33ed-80a7-40e9cdda0b31 | -3.5203 | -55.4409 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a0c4c87-9a21-3e86-afa1-cecfd50dd669 | -3.51733 | -55.43599 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5517f7f8-d7e9-32b3-b69e-deab30dd4e0b | -3.48673 | -55.46197 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e77c8af-fc9e-3910-bf48-f7b9c86b57c4 | -3.48305 | -55.4614 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8d8ed7f-bacf-3913-8220-ae683679b76f | -3.48061 | -55.45844 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8361b311-7a15-3aac-85c9-4d896be23cc7 | -3.48008 | -55.45649 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a21cca62-d0a7-33f9-84b7-71cc81925a37 | -3.47937 | -55.46082 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 127f2640-467a-325c-b6f0-7d3e4dc46fff | -3.09697 | -56.61419 | 2024-10-15 04:49:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afe6f543-7a60-3c9b-b838-f3f46d967704 | -3.90556 | -55.65194 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8ba077d-be29-3b50-9930-3b6e88e90583 | -3.87802 | -55.77403 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12ffe91b-dc51-3fee-b00f-1cb6c9cbf76b | -3.8743 | -55.77345 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1491ae80-0733-3797-8e01-0552fe0e5b43 | -3.87057 | -55.77286 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3ed916f-669e-31da-82f9-19777d624b96 | -3.83132 | -55.98843 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 920244b4-3b1e-374b-93f8-46807463f606 | -3.83071 | -55.99144 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a65662d5-8c46-342c-b12b-b986f4419b49 | -3.83057 | -55.99302 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48c11818-d9cf-39e6-978f-0a5e59d6e37d | -3.82755 | -55.98783 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef762061-5c5f-39a5-870b-b78ee4c091f5 | -3.82693 | -55.99083 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e92f01c-6267-3d59-ae2e-4de49715d498 | -3.8268 | -55.99242 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3de68603-3fce-39d6-be9b-f3e954b475cf | -3.82621 | -55.99542 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dbc85eaf-4d6f-37aa-a03c-ad316d4c3acc | -5.0075 | -56.17482 | 2024-10-15 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37129744-d43d-3668-b945-2902af7d663c | -4.86357 | -56.00767 | 2024-10-15 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 663f8e2b-2396-36b7-aa9e-6c467862c354 | -4.63965 | -56.04933 | 2024-10-15 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b93e978c-b6c3-3262-8456-c1faafe6ba9e | -3.98922 | -55.73572 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45d9a8c6-7d27-350d-91b0-18ea83c9afbd | -3.98551 | -55.73515 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3743f9d4-ab3d-36a0-a489-5937c25bd248 | -3.97878 | -55.7402 | 2024-10-15 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f84cecc5-2ed4-3add-a261-4180948d81ab | -5.30376 | -55.97265 | 2024-10-15 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 318485fe-41ae-3506-b484-a5bc534c71c5 | -2.20862 | -56.89478 | 2024-10-15 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b758561-aab3-32a5-80af-c3948e7156c6 | -2.20803 | -56.89845 | 2024-10-15 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb472f02-054a-3ea5-b10d-c8d106e1c842 | -2.20454 | -56.89414 | 2024-10-15 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce695eb1-3b15-351d-854e-f9befa449e9c | -2.20394 | -56.89782 | 2024-10-15 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4096e71a-d15e-3d57-ba70-9eda7e9bb2e0 | -2.77075 | -57.60148 | 2024-10-15 04:49:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4824dc-cc5c-367e-b0b8-166e21301fa7 | -2.76651 | -57.60078 | 2024-10-15 04:49:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0d2a779-88dc-3172-bbcf-a72a153c0a2f | -2.76523 | -57.6087 | 2024-10-15 04:49:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad417714-0c62-343e-b531-6eab91759fb1 | -2.60087 | -57.55507 | 2024-10-15 04:49:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42b9a28c-2afe-3208-b0d9-59878a45d2d7 | -2.60041 | -57.55453 | 2024-10-15 04:49:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1e7ca1f-6bc1-3d36-9296-50adaf784224 | -2.53158 | -57.41898 | 2024-10-15 04:49:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ddc1e5b-d510-33d2-b3ba-bb8e50a6ff9b | -2.09778 | -59.31884 | 2024-10-15 04:49:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 029f3877-b4fc-39d6-ba93-cf7e89e38f08 | -2.09628 | -59.32091 | 2024-10-15 04:49:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57c3fd2e-dad6-3e9d-8317-ccc89d36ab23 | -3.18744 | -59.01179 | 2024-10-15 04:49:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85bc553e-4c97-3121-8597-9bce1be099e8 | -2.6318 | -59.38309 | 2024-10-15 04:49:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 601061fa-e6d1-3248-b85c-8cec3a5e0428 | -1.84489 | -60.04078 | 2024-10-15 04:49:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 907388e9-5815-3bf5-96e4-6bceacf90f35 | -1.8444 | -60.04383 | 2024-10-15 04:49:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c191938-e7e8-3b48-b71e-1ee3d0e98758 | 4.81613 | -60.33253 | 2024-10-15 04:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bcba10d-d111-3770-8acd-e673f1dbd6b5 | 4.8155 | -60.32793 | 2024-10-15 04:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c187e41a-d931-362a-b958-abe64aebf995 | -7.95101 | -63.63627 | 2024-10-15 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd490c16-2db5-39b9-8ff9-37af9ef403ea | -7.94596 | -63.63091 | 2024-10-15 04:49:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2578773b-7c08-3e31-a882-580a40544464 | -9.77894 | -63.15268 | 2024-10-15 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17eba082-0aec-31e3-8908-a1b124bc6c5d | -9.40565 | -63.66695 | 2024-10-15 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a49d0480-bf50-3d05-b007-ceaf6aeae6d2 | -9.39994 | -63.66584 | 2024-10-15 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bab39df-9e7b-328d-8b07-e4ae968cc62a | -10.2586 | -63.11054 | 2024-10-15 04:51:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b265831b-4dc0-3be6-9ff6-c42d0a89faa4 | -9.28341 | -64.55995 | 2024-10-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5bda71-8461-3f55-905e-17a5e3e6fffd | -9.28253 | -64.56452 | 2024-10-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e033fe3f-2fa2-3e99-afce-8fa1f7bc1292 | -16.17768 | -43.86457 | 2024-10-15 04:51:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c42073ca-5286-360f-9be8-b2689825a902 | -12.87421 | -44.61405 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f22671dc-762b-3289-b590-a40df7fadc5a | -12.87378 | -44.61765 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88148167-315c-3b39-bcf8-e4fd42a32907 | -12.86878 | -44.61349 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 134c380d-6adf-32db-8fe2-0550a95df4f2 | -12.86837 | -44.61702 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c08855b-b15e-3ad9-86c7-fb6600629ec4 | -12.86337 | -44.61291 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c151243-d20b-3bdc-acec-8498b46c2694 | -12.86296 | -44.61636 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c9023f7-d2dc-374b-b8bd-4ec385292fe0 | -12.86255 | -44.61978 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4d15bee-397e-33c1-a0c6-63fc2af90d25 | -14.09553 | -44.61076 | 2024-10-15 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f47f1dc-e6c7-3317-9dd3-1472a5071a1b | -14.09045 | -44.60655 | 2024-10-15 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9ff25de-c2d6-394a-b5f4-e4aeb0089cc0 | -13.89543 | -45.84341 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 614a581a-ac27-36f4-91ad-25844282297c | -13.89507 | -45.84641 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 025d60b2-ff90-3da0-bd4c-b1ed8a436ca5 | -13.8929 | -45.82169 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 806cf4f6-a57f-31d5-9f04-02d3b0646b97 | -13.89254 | -45.8247 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b4fefcb9-4655-33f1-aa29-384fb5f0f18c | -13.88244 | -45.82956 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b75cf1eb-1a3e-3bb2-8d9d-83c19344495a | -11.9189 | -45.76612 | 2024-10-15 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7b7232d-caf8-3b1b-b053-44039055eac6 | -11.91817 | -45.77177 | 2024-10-15 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daabafb0-5e16-313c-8790-61ee0efc3116 | -11.91323 | -45.77112 | 2024-10-15 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f1dcf2f-6350-3fc7-86ff-2aea1b2f3f1d | -11.91251 | -45.77678 | 2024-10-15 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d9e0ddf8-1822-3e5a-ab48-f65541cca55c | -12.08057 | -43.88939 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5fcb3e9-cc07-3938-92aa-934a23ca4a8e | -12.08012 | -43.89316 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23195e39-aada-3905-b1a5-b2e75cb781d8 | -11.89009 | -43.81752 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bae09ec-54c1-314e-8b62-c9c67f8aa86a | -13.91963 | -45.81287 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfdf7819-8c87-3025-92c4-ae418e1592cd | -13.90301 | -45.82298 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2bfafe3-683b-392c-aaad-786b330e969a | -13.90264 | -45.82601 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fbae6ea-8886-33f6-8808-3f0bd205552e | -13.89218 | -45.82771 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2b96296f-a319-3cd2-ae76-b1c36f8d9b3f | -13.89182 | -45.83073 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 9a0195cd-8dd9-351d-be47-96cd75290ad2 | -13.89146 | -45.83374 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 1c5d6dbc-5234-3cd2-8efb-078d4fd5d2be | -13.8911 | -45.83676 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 47cfa3a6-a732-37d0-afd1-86305e05da28 | -13.89074 | -45.83975 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| fa2bc6fb-c7f0-3e31-be0e-ee98c088bf47 | -13.89038 | -45.84275 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99b1107f-3e4f-3c2c-bcc3-585d8f39397f | -13.88206 | -45.83257 | 2024-10-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 37befbf8-6621-313c-b397-7e30115d71af | -13.59528 | -49.78955 | 2024-10-15 04:51:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c0dc7f9-b588-3e35-a8c5-884fd2170b5b | -12.08246 | -43.89054 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5718744-cbc5-35c1-bec8-e21946412193 | -12.08199 | -43.89431 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93c3e7d4-af17-383e-9e43-03ba496ade04 | -11.88794 | -43.81633 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1a59361-f316-316a-a75b-134a62bb8fb5 | -11.88748 | -43.82016 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b85e6eb4-1b92-3fc8-9cf9-87db963092ed | -11.88447 | -43.81678 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9fc9dd4-e25d-319b-b915-26e12f55ac07 | -11.88399 | -43.82059 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20d59d8a-4f3c-3e1b-b578-e145f3e92e0e | -11.88276 | -43.81175 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d77e9f4b-6a3b-3df1-9747-05df7b7df14c | -11.88232 | -43.81557 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b592137-0238-3dc5-8d75-8a68b61b8439 | -11.88186 | -43.81939 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed3b868b-4b32-38e6-9e2b-e3955e51b5da | -11.87932 | -43.81223 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd7489f3-72fb-3a8b-8b9f-86af6910f729 | -11.87885 | -43.81603 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce350ff8-774f-3745-bbe5-f7d77b0c6a2a | -11.87714 | -43.81102 | 2024-10-15 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee07308d-4be0-3abc-a874-b8363f371317 | -12.86125 | -44.61288 | 2024-10-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README67.md)
