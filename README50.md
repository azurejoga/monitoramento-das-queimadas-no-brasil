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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69296d76-d490-37ee-b38e-0bd3fa05976a | -12.26713 | -50.40781 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bc1c9dd2-1c0e-30a7-b63d-1525b2441ca5 | -10.68447 | -68.86237 | 2025-10-15 05:27:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf8e8280-f0e2-3fcf-8e27-1f196eeb7a14 | -12.27452 | -50.39881 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 372c5cfe-220f-3bbb-a14c-925d640417fa | -12.24962 | -50.39573 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0736a3d-90b3-3180-980c-940c00f7fa5a | -12.22189 | -50.41703 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aca5499-4077-3ca7-8ada-4199a6b231f3 | -12.59169 | -62.02528 | 2025-10-15 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a95ac8b-0001-3d65-9864-7e73d8924024 | -12.23096 | -50.39342 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8774aaaf-ee53-3ef0-b336-36c3b43ca4cc | -12.21286 | -50.38619 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b88ba37-c62d-382d-a791-d0c50ae2f695 | -8.97276 | -61.97448 | 2025-10-15 05:27:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa0db4eb-9641-35d7-8fe0-a27f72ab764d | -12.22811 | -50.41781 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6eb33746-78af-3e17-b28b-85d37fcda31e | -12.26623 | -50.40165 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b45e0243-c1e0-37b2-9201-f3f9b8644599 | -12.27245 | -50.40243 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cae063bb-0945-32b3-b82f-50850b89e60d | -15.85606 | -54.00134 | 2025-10-15 05:27:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9cf1071-bdf1-3a79-8da8-03ae5119ab1c | -12.26207 | -50.39727 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e45ff0d7-3706-3f4c-a6ba-ae4e2de6c213 | -9.27448 | -61.82746 | 2025-10-15 05:27:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6bb1f745-8ba3-3697-b114-b52e4791b85f | -12.25585 | -50.3965 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbf590b3-eefd-35f8-a4d5-8c911bc18787 | -12.59225 | -62.02174 | 2025-10-15 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdf0d705-0c14-3b2a-bada-f5c443d37c8b | -8.9761 | -61.97503 | 2025-10-15 05:27:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d0a640c-5502-3b2b-95c2-bedcc9400138 | -12.27867 | -50.40323 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dc1b2b33-c55c-3ff7-ba7e-c5899a1d7780 | -12.21568 | -50.41626 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8f7b86c-a9bd-3d15-8f63-e3fb65477c15 | -15.87415 | -53.98159 | 2025-10-15 05:27:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e7c2a6c-67b1-3920-8a25-f44509ba6486 | -12.27812 | -50.40814 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5bde6c37-8d67-3e75-9bc6-a33e4ce464df | -8.97944 | -61.97556 | 2025-10-15 05:27:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9efc8181-fad6-305a-af29-f202c9ef9591 | -12.26771 | -50.40292 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7d43230c-9edc-3d53-a359-25705936c416 | -12.2253 | -50.38774 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0f2749e-90f1-3e86-bbe0-3fba54c6bb7c | -15.86937 | -53.97773 | 2025-10-15 05:27:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6706dc2-4901-3aa6-9ef0-3fe27649eeea | -12.25411 | -50.41116 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abf79e80-8ae3-36c6-9e26-eb84ec92cc68 | -12.22246 | -50.41216 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dafb6d18-f933-38b6-9c98-ff841cebdf98 | -12.27135 | -50.41224 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9a9e7012-b23f-3cd5-ab6f-9916d2acc204 | -15.85642 | -53.9983 | 2025-10-15 05:27:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16acad5a-3869-300a-9fa5-49cc046ce659 | -15.86899 | -53.98085 | 2025-10-15 05:27:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49ad05fc-06b0-33db-ad01-e242247adac1 | -9.01284 | -62.00274 | 2025-10-15 05:27:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 049887ae-cfa0-39d5-be07-5fc838c6bde8 | -9.01227 | -62.00629 | 2025-10-15 05:27:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61b13f58-1358-3587-9ce1-66334b1e4b47 | -12.27276 | -50.41347 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4f6e6a4a-63f5-3fb2-9847-26c0e2df382e | -12.20326 | -50.41471 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 970862ff-829d-3c77-8e68-ed3800a5e014 | -12.21908 | -50.38697 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e27bd9ca-8973-322c-98a5-f5692a313e90 | -12.25527 | -50.40139 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bcc8479-da8e-3727-84ef-2e4ace258964 | -12.2434 | -50.39496 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ef96f21-2f4a-3f42-99cb-b3b30eeffbc3 | -12.22867 | -50.41295 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 103da261-c37f-3b86-a176-ea375cb3e548 | -12.24905 | -50.40062 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fa4a117-92ef-30b6-9b56-fd377c3e84e4 | -12.26033 | -50.41194 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 138c3388-8381-3cd4-9940-1f2da006ce50 | -12.273 | -50.39755 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4e67b740-bf94-38b5-88db-a1bf777116a6 | -12.27335 | -50.40858 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 82eeb21c-c5e5-3162-81ff-412af84733c4 | -12.22473 | -50.39265 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a8b89ba-21bb-3f33-bf24-156fddc7a57c | -12.2719 | -50.40734 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b670c5b1-4320-33cd-b3cd-5e49587e39c4 | -12.26001 | -50.40086 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ab01437-7f70-3087-b7a2-c8ca78190162 | -12.26655 | -50.41271 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1e397394-abd7-3534-9bdf-2a10e0609076 | -12.24283 | -50.39986 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05502fe9-4509-3033-906d-ef8393199c14 | -12.26149 | -50.40216 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecda081a-9ed5-319c-95fd-3a09e12732db | -15.87453 | -53.97845 | 2025-10-15 05:27:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33a9b8c4-9503-3733-82d4-6608a2fc369a | -9.27504 | -61.82394 | 2025-10-15 05:27:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2627e455-64d9-3ffc-8f70-13e13a3ecc3b | -20.5596 | -54.65708 | 2025-10-15 05:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 726f4868-0e29-357a-b6ea-3ac89bda74fd | -16.20866 | -59.32652 | 2025-10-15 05:29:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e86a392f-9f0f-3e04-a6c1-41efeb3cff6a | -27.74981 | -50.39978 | 2025-10-15 05:31:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d5032815-198a-337f-b5af-87cd8fbc3906 | 1.87513 | -55.68123 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6850f4d5-8181-39b5-b802-fedd96d33386 | 1.86414 | -55.70443 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6a2338-5ad6-3d66-9fc0-d972b82dd180 | 1.77205 | -55.76553 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68673002-387c-39da-bca9-5f3904d952ca | 1.88014 | -55.66782 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24e477a6-4f41-3aa9-86e0-bf587752b471 | 1.77734 | -55.76458 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce3b7dde-8f56-3300-a2be-dc2a5ce05e40 | 1.85935 | -55.7086 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3d39de0-f42c-3966-a5e0-b1e5119dd646 | 1.87533 | -55.67199 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e89878-a21a-397c-a60a-3243ef41d4e5 | 1.87641 | -55.67874 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32c92c89-afe4-3026-a9de-e7bfa62e289b | 1.87934 | -55.6737 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dc722f7-a5fc-3b7b-aa56-f7891968f1e1 | 1.88067 | -55.67115 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 013e26eb-9ffc-33c1-a2ac-0b30b8104866 | 1.87457 | -55.67789 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7efd17e7-9823-3741-bfb5-a8a552873024 | 1.88835 | -55.66205 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c4c2c04-1ad0-3350-ad86-b58a7b734b75 | 1.87878 | -55.67034 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca65ffaa-9134-35ea-bc8b-11c158353887 | 1.81839 | -55.85686 | 2025-10-15 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d061a586-4336-365a-88f7-e1e76d56589c | 1.85882 | -55.7053 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa5cb6c4-5749-3cec-8f11-5c7f0d60f6fa | 1.77788 | -55.76792 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c92c5f4-36c8-33bc-b58b-204b4b9c5283 | 1.81893 | -55.86011 | 2025-10-15 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38fe9483-e615-399d-93e1-cd0a31b5bb7a | 1.87587 | -55.67537 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07e0ffe1-a1df-3c31-80f8-75eaff34ff72 | 1.89369 | -55.66125 | 2025-10-15 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fe8096b-eb49-317b-a10b-5f88e039c7c3 | -10.59516 | -69.02112 | 2025-10-15 05:48:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c4c1ed6-6f93-36da-b001-218149bd3e22 | -10.96495 | -68.4795 | 2025-10-15 05:48:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e354cc00-fc38-3cf9-bbe7-b9762396a64b | -10.00316 | -67.53945 | 2025-10-15 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3647d496-badf-3d95-bf17-dae0d0ba2759 | -9.25217 | -68.41166 | 2025-10-15 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c94c5f83-e043-33f1-a6b2-a235f839c8ef | -8.97358 | -61.97757 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f79c278a-9287-3bd4-a8a8-ad46bc470906 | -10.87364 | -68.68685 | 2025-10-15 05:48:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04739748-3f8d-36cc-89ad-0131e378f992 | -9.27679 | -61.82549 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f1c57e9-58be-3517-963b-8dadc7825fd1 | -8.60115 | -69.75012 | 2025-10-15 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b916702-b910-314b-ade6-e3f982064730 | -9.54985 | -67.42033 | 2025-10-15 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb69a3b1-b13a-3592-9b2d-0a5503b45317 | -10.96838 | -68.47629 | 2025-10-15 05:48:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e7cbbc4-d948-334b-8644-3cb2bd2de41c | -9.01505 | -62.00522 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f03521c-0b02-32b6-9cb6-b8f07209fb51 | -9.01128 | -62.00553 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e48baf19-278c-3571-8fa3-ba2a0dff3029 | -10.57657 | -69.02917 | 2025-10-15 05:48:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08bdc6fd-5533-373e-9281-c23576a11d7c | -8.9741 | -61.97389 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67b2ded6-d305-3b54-aebb-bc0f15321379 | -10.59575 | -69.01749 | 2025-10-15 05:48:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2cf4942-fa16-3618-bff6-45bc5346dac0 | -10.96551 | -68.47597 | 2025-10-15 05:48:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c75ee41e-aeed-3b55-8eef-ef8d6546a1a4 | -8.97767 | -61.97819 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fd8ef33-088f-3896-a49c-ea94d248b7cb | -10.81552 | -69.19567 | 2025-10-15 05:48:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3df3a00-f8ed-3f2f-a3c0-3763e880f863 | -10.68323 | -69.02046 | 2025-10-15 05:48:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c0d9347-11aa-38b8-b84c-0703644c4c2f | -10.68243 | -68.86485 | 2025-10-15 05:48:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2912ba3a-fbcf-345f-a889-11185eb7c3b1 | -8.9782 | -61.9745 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e267dd0f-f33f-3602-ab22-416bb1dfad7a | -9.01537 | -62.00614 | 2025-10-15 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05410bff-f48d-3189-b9ed-c054a06713f0 | -9.58182 | -67.41116 | 2025-10-15 05:48:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2328e9b7-dc9d-3089-9897-91051269e3b9 | -3.53801 | -44.02776 | 2025-10-15 06:03:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 60dffacd-470f-3356-8c1e-cea35acf7f93 | -2.95068 | -49.34105 | 2025-10-15 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e9e7bb92-7e4c-3382-9216-40b8d3c26d0e | -2.86977 | -50.73383 | 2025-10-15 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7f2f8e4f-cf9d-391d-91f4-8be7c86f921c | -3.05402 | -44.46975 | 2025-10-15 06:03:00 | AQUA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |


[Clique aqui para ver as próximas entradas](README51.md)
