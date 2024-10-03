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
| afe848e4-38fd-3935-aef4-27af00b848f2 | -16.76394 | -57.83175 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 8b88bdc4-5e62-3b4f-8dd1-c083af754b87 | -16.76296 | -57.75138 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| cca8dc43-9ca6-34da-8511-5cc90206e725 | -16.76058 | -57.81235 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.9 |
| fca89d88-ac06-3d47-b576-8ef9d1a5a23a | -16.75957 | -57.73172 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 089792ff-99a3-38bf-9fef-39e25b912e24 | -11.98912 | -57.20547 | 2024-10-03 02:06:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| f3dd0381-8a79-3cdd-9de7-2433cbd9c60c | -11.98723 | -57.2125 | 2024-10-03 02:06:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b020d29c-6c83-3edb-bd7b-17ee883bd4ac | -11.98277 | -57.18621 | 2024-10-03 02:06:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 1a354fb2-6dd5-31d4-8257-96b3874572e2 | -16.59684 | -58.22454 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.1 |
| 452f8d4a-3030-3b44-81ee-ecb5d4a39d53 | -16.59324 | -58.2318 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.5 |
| 481a5df5-8f9d-3bae-92fc-169d0f284838 | -16.56896 | -58.23614 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| 3ec89c04-06e2-35eb-b103-7776e23a0eb7 | -16.56586 | -58.21788 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| bb162341-a322-3e74-b9af-76272115173f | -16.56275 | -58.1996 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 6194c64c-7242-3ba6-a5de-f1a9a4c1d13b | -16.55373 | -58.22018 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| 06702053-de2e-3d0f-b271-3c424f15ee4b | -12.95541 | -60.1002 | 2024-10-03 02:06:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 967a5542-4c85-341c-a430-a2fcb6cfbfea | -12.94525 | -60.10755 | 2024-10-03 02:06:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1b98fd25-41d1-3bc3-8cd1-c8843a1e6635 | -12.94417 | -60.10212 | 2024-10-03 02:06:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| e7c2af87-f969-3746-b1a5-b4d6d28b32fd | -14.40194 | -59.56037 | 2024-10-03 02:06:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4c3bfdcb-a9a8-382c-8a9d-8f48737ae42b | -11.2597 | -60.59896 | 2024-10-03 02:06:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| d3aba35e-36b2-35a8-aa5f-75da50ced5d6 | -11.25739 | -60.58406 | 2024-10-03 02:06:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 43b52bfa-c9ab-3875-861c-6041b6f69c1a | -11.24844 | -60.60019 | 2024-10-03 02:06:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 31.5 |
| e23fdadf-fb5c-3f5d-8889-cb390064ec0e | -11.24616 | -60.58557 | 2024-10-03 02:06:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e68ce9e8-4bb1-333a-92a1-c88e58927b66 | -12.08861 | -61.19589 | 2024-10-03 02:06:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1e9173d1-4947-3446-9c29-f5deef5d4447 | -12.05367 | -61.03909 | 2024-10-03 02:06:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8f5dc94e-ec16-38ee-b45a-7afefd89718a | -11.48489 | -62.481 | 2024-10-03 02:06:00 | TERRA_M-M | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ffe3d9c2-ee46-310e-a323-1574ada0c268 | -12.65099 | -63.10753 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f3990228-ad3b-3be3-8998-0e80032e39be | -12.64171 | -63.10899 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 9eb8f9e3-5f92-3c73-808a-466f87ef0f41 | -12.63389 | -63.12043 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| aaaa5ba2-5846-3205-a9ab-fab6052c7d8b | -12.41153 | -62.99254 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 52c99169-15d7-3147-b9bc-cdca687930d3 | -12.40217 | -62.99401 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| f8030b97-123f-32b8-81a4-c5eb2d661c1d | -12.39433 | -63.00564 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 0d30e0dd-fe56-39e6-b793-8e8f1b8a27b5 | -12.90844 | -62.48356 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| ac63c3e2-ae21-3911-929b-704f8edb34df | -12.90685 | -62.47291 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 556c814b-a843-3481-aa6f-65507e4b0679 | -12.90207 | -62.50637 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 190da36b-f293-3c2e-b971-bf2ed48b15a6 | -12.90048 | -62.49572 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5f3b37b1-2893-3705-bd2d-a1430cb2acf9 | -12.89888 | -62.48509 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 714ebbe1-85b7-3a63-9ace-f26e84b4ceda | -12.8973 | -62.53963 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3920b99f-504b-3231-a3c4-0e7bd2b89383 | -12.89729 | -62.47444 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 00713e4b-8790-3135-b9ac-efc26148a5ab | -12.89569 | -62.46378 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.3 |
| f95c65ba-98aa-381b-9c82-babad0a6bfeb | -12.89409 | -62.45314 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 2fa8c1d4-b81a-3ec6-a787-f458cd4cf863 | -12.89253 | -62.50791 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.4 |
| a76b0399-627b-3431-813f-bfa8fdbfe321 | -12.89093 | -62.49724 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2cbe8e00-d5ba-3f67-9016-79142116cf0d | -12.88937 | -62.55171 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3f490af7-528c-31eb-944d-78945de390a7 | -12.88778 | -62.54115 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9d5a59fd-b6f4-31b9-8d18-3b8fee1a4998 | -12.88612 | -62.46532 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 881181dd-9c53-3c49-91ba-e11546a64c86 | -12.88452 | -62.45467 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6c8b496b-b87c-3903-b943-78008d40ac5e | -12.87985 | -62.55323 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 109f222c-0e94-32fe-b5e0-11a308a0a155 | -12.87825 | -62.54266 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c3a1390-667c-378b-b6f3-21c513071bb1 | -12.87656 | -62.46686 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 40.4 |
| c2519fb1-2dea-3a15-8569-d530736663ad | -12.87494 | -62.4562 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f8727864-fd59-3756-95e5-19de3f769892 | -12.86537 | -62.45773 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e0b4811d-cf47-38b4-8404-58ef008874b5 | -12.85742 | -62.46992 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 965d61fe-af94-34ef-8d66-5f18075fb26a | -12.85275 | -62.46616 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f36795d3-0490-344e-86a4-db96f12a886d | -12.83519 | -62.47989 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e4cc0e9d-8190-34bd-8eb5-b8e27efce49f | -12.82562 | -62.4814 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 921f72ea-98c7-3c1b-a2a2-1052286b42ba | -12.81764 | -62.49358 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 781eee95-49c8-3f7d-8a57-6b48c81668b5 | -12.81605 | -62.48293 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 88626c85-25cd-3adb-bedb-f456da59be55 | -12.80013 | -62.50728 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 432d48a6-5e33-3b6e-9ea4-e9cb72e758b2 | -12.79853 | -62.49667 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5a6ff031-f464-3286-a38f-7f20c38b3409 | -12.79057 | -62.50882 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d568e883-4ad5-34cb-a2c1-55ee7e25ae48 | -12.78897 | -62.49821 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 63dacf62-3d17-376f-a542-4794c3c25660 | -12.78102 | -62.51037 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e598acbb-1058-33f8-9756-98cfa69c9cc4 | -12.98642 | -62.71231 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 99c164eb-6e69-3f1d-8d0d-8c401e631acb | -12.98056 | -62.70848 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0ede0c6f-6f5f-34ca-95fb-1e8d4d6e07db | -12.97904 | -62.69812 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 097920ff-1423-356d-a500-a0b671c5fbb2 | -12.91297 | -62.70858 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 833a1db8-90b2-3b71-b9f4-547101a54502 | -12.87066 | -62.78517 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3ceec438-6456-3b84-ad82-a50eb0cb70b6 | -12.86125 | -62.78665 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 666cb1c4-c9b9-3a9f-a494-355b197ea134 | -12.85338 | -62.79844 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b8c7c73d-365b-3a37-a7ae-ab5e80d30f42 | -12.8455 | -62.81018 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 96b52d01-0a15-3f52-9e30-3418009a9153 | -12.83457 | -62.8014 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e0388839-6184-3153-9dfb-a85a343e2ba7 | -12.7793 | -62.92044 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 65c452e2-6694-3c46-b1cd-87ee15f7e7f0 | -12.75299 | -62.87249 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3e2fef22-2c73-3625-961c-28ebf981a403 | -12.75124 | -62.92487 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 28456331-59fa-3b66-ab00-acd0dd9b877d | -12.74667 | -62.89436 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6fb82a8d-6676-3e26-9cb6-c14ee71eb681 | -12.74514 | -62.88416 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 8de67de3-f928-31be-ab9b-38a07caaec72 | -12.74361 | -62.87396 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 52b0567f-f44f-3cad-a466-89fabf681636 | -12.73883 | -62.90601 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6e7b2e84-3f1c-3682-a41c-eed1e1a29809 | -12.64463 | -63.12894 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 43b1723e-73a8-3ea7-b6ba-c019fc649571 | -12.64317 | -63.11897 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 53cc42e6-5fbb-3b28-a1a0-fcc10aab4875 | -12.40368 | -63.00415 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.2 |
| fcbaea5c-0316-3141-94ae-9a0c013cb2c2 | -12.98489 | -62.63813 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 9a6ead18-f27c-3e42-ae2b-a572308e6ee1 | -12.97542 | -62.63962 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 981857d0-ed31-3b8f-9d6d-06750c29b646 | -12.92396 | -62.71747 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 89483e4b-681d-309f-97fe-62f83d3e5f12 | -12.92241 | -62.70709 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9f67b891-6523-3f92-8a35-f95c9b93714c | -12.91142 | -62.69821 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 54e8df06-6b2a-31ef-ace4-8ec08fb2e66c | -12.90045 | -62.62528 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 434a1fa8-070e-305e-8829-eb5ca7f3e1c3 | -12.87703 | -62.76306 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fd94d830-b09e-31e3-8126-975d8b65d3a7 | -12.87551 | -62.75273 | 2024-10-03 02:06:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9ff570d3-90fe-3f76-8839-9ced909d9d94 | -12.85185 | -62.78814 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e0280a9b-2471-378a-984b-16643f42d85c | -12.84397 | -62.79992 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 657ece0e-49b5-30a4-b72b-2eec2c26fc4b | -12.76591 | -62.76532 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4d27f48e-752f-3f1d-a495-d7104c395541 | -12.46875 | -62.69273 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 200d8e15-1c38-348b-baa5-ced5bda2d005 | -12.45916 | -62.75834 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| daebf99f-e0dc-30f7-83b9-d4ccee0ed3f5 | -12.02061 | -63.78215 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 78db32d6-6f47-3ace-ad88-7b3b615928b6 | -12.01925 | -63.77261 | 2024-10-03 02:06:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 887aea4f-abbd-3e81-94e3-58a39f98d38f | -11.78206 | -63.66474 | 2024-10-03 02:06:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e47c8e58-c352-340f-ba87-92b172d18422 | -11.7367 | -63.79563 | 2024-10-03 02:06:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b54312ef-5700-38c6-b510-0b305a6124a6 | -11.76038 | -64.28051 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8ee90054-b24f-34cb-98aa-53df013afac2 | -11.75604 | -64.18655 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 824f4de9-fac7-3a58-8221-0f33da429e0a | -11.74706 | -64.18791 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README48.md)
