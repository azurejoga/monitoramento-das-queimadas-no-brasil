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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fc585f9-8ef2-348a-8841-48f3aa326aee | -12.41688 | -63.74612 | 2024-12-02 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ba5597c-2180-3ff1-b540-48e7dac91f4f | -13.50651 | -61.53317 | 2024-12-02 05:46:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6789e659-23c3-3f9f-b10b-fd6239eafde8 | -12.79956 | -62.00987 | 2024-12-02 05:46:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17022db3-5373-3af1-86a5-b349b9b72536 | -13.50477 | -61.53357 | 2024-12-02 05:46:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2b527c24-35fe-3901-bf2a-6f72fe182bea | -12.80146 | -62.01022 | 2024-12-02 05:46:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a197b8a-3d03-3a63-a0f9-6c9470cf4845 | -20.73019 | -54.42438 | 2024-12-02 05:48:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a22b9de3-70a2-3432-b22c-570cd7611500 | -20.72967 | -54.43208 | 2024-12-02 05:48:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0609ca5a-4dbe-3278-8181-0094dd82c34d | -20.72254 | -54.43149 | 2024-12-02 05:48:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5da7ac5a-e6d4-351a-87f7-9e78959826a6 | -20.72617 | -54.43119 | 2024-12-02 05:48:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a0029581-2f81-3ccc-9e2c-3016197ac171 | -20.72675 | -54.42353 | 2024-12-02 05:48:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bdbceb85-1b13-3d16-9f54-6e14fac924a1 | -3.2591 | -53.6186 | 2024-12-02 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 268d28f1-e1ce-3fa6-bf76-ae3ccfdfbe62 | -5.5882 | -45.1412 | 2024-12-02 05:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ddef97b5-2886-3e3f-887b-49f2f686a038 | -3.259 | -53.6388 | 2024-12-02 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 11d596e3-0ff7-3f18-b50f-3d09a8f281ac | -5.5882 | -45.1412 | 2024-12-02 06:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d411ae2b-6254-30d4-a890-200232d932ed | -1.27598 | -54.54832 | 2024-12-02 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8d4eeaf7-aa90-3f89-ad79-e92b8ae0b985 | -2.56371 | -54.33583 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a82300c5-8eda-3c4a-bba7-5c280d946c22 | -2.45305 | -53.71289 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b4afe451-77af-397f-a1a7-b94ccdd91b94 | -3.26835 | -53.62937 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6250be93-d03b-3269-82c9-19fc9b679345 | -3.01779 | -54.01122 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 816a1070-a8f6-3412-9503-b987e3f0b11a | -3.77904 | -52.0352 | 2024-12-02 06:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 156e7818-d753-3ea3-a43c-433ea6eaeb34 | -4.26428 | -50.83794 | 2024-12-02 06:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5d3f7a63-1adf-3448-93d8-b62c2e9730bf | -1.68637 | -55.00839 | 2024-12-02 06:03:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcbc0dcd-e1d4-3c5d-bf3d-5bacd3a2650b | -4.26202 | -50.85333 | 2024-12-02 06:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 318e36cb-1d54-3386-b703-2799b6b0b8b7 | -2.99282 | -52.50724 | 2024-12-02 06:03:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 561e21cc-11d3-3881-9b56-f935407e57f2 | -2.63272 | -53.36412 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 228509c5-f864-3bc0-b229-2c548d0aa89e | -3.06583 | -53.68689 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ee84c741-ca96-3139-8a9e-438d46dc8d0f | -3.11505 | -53.97413 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 539541ab-0c22-3220-b178-641b03b57edb | -3.12557 | -54.52844 | 2024-12-02 06:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7db230d5-2025-30a9-86ac-527e696514c8 | -2.46189 | -53.7102 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ad395b5c-a6b7-3083-96ee-61b62e77951a | -3.11225 | -53.993 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b8a797d-310b-3a43-8a24-b3e6906de33c | -2.70906 | -51.99948 | 2024-12-02 06:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f45ae48f-0c7b-37e6-8992-c3a901568db1 | -3.96398 | -52.17381 | 2024-12-02 06:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1d625747-4f30-390e-ac24-be8ccea2798c | -2.80195 | -54.0346 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 932b8d5c-2aec-3439-916d-1fa484de0af2 | -1.64548 | -53.86333 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d6766a2-8c5a-310c-86da-8f8ea03ec065 | -3.25158 | -53.93164 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8b5c62c4-88c1-3384-96f8-6c9c79f5f1da | -1.69259 | -52.63227 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d2e38d5b-6708-393c-9152-a547bc6f2644 | -1.735 | -52.77235 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f09ec788-686c-3a71-9bc8-0f62344b1f1a | -1.57337 | -55.34131 | 2024-12-02 06:03:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9f591820-911d-3bb9-a9c2-585660934474 | -4.26135 | -50.84476 | 2024-12-02 06:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| dd66dd62-3abb-39e6-8f42-b6503aecd148 | -1.72636 | -52.63202 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fddc9f87-94b5-35ba-9f0f-2cd900ba9bee | -3.70505 | -54.60319 | 2024-12-02 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b0ce0eb-95f5-3b4d-937a-2f355e026cbe | -3.10528 | -54.03998 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 539dc332-b323-3ca3-bb16-a0d64eb18f3d | -3.29171 | -53.83729 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e910a5dc-a36d-34fe-9479-f0e92ae4f0ed | -1.23072 | -51.6098 | 2024-12-02 06:03:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1a99361f-5775-363a-9d1c-7e8c408b0ec0 | -3.25123 | -53.61682 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e0052bfb-1140-3fdc-b7e3-66dcc8c0811e | 1.2147 | -56.00624 | 2024-12-02 06:03:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 067acedc-1df4-3e1f-978d-b7b905e21e55 | -3.2021 | -53.12093 | 2024-12-02 06:03:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 084fa82e-e83e-3dc8-9ae5-cbc1317757c3 | -3.10389 | -54.04938 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 74f277e0-3953-3118-9720-9981e5137a6b | -3.09513 | -54.2946 | 2024-12-02 06:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 263f1892-e442-344d-9fe1-855322b14944 | -2.80057 | -54.04393 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 132af086-6778-3997-81ab-165a30654c4b | -3.26806 | -46.43814 | 2024-12-02 06:03:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 887d3dff-5b75-3d28-b1c0-07c7ecc03e9f | -2.44759 | -53.62393 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5caafc11-508e-36c2-a21b-76fc83d118ad | -2.98819 | -51.32932 | 2024-12-02 06:03:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 112dbdec-670e-3f92-a785-118871ec1027 | -2.89387 | -55.21685 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d420d80-dbd7-30c6-b9f6-2aa9c887fc9a | -1.23249 | -51.59777 | 2024-12-02 06:03:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5883b8b8-6a3f-3643-af0b-507b75cc4cd7 | -3.2903 | -53.84687 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e75ff4c-825e-39f5-be03-164d66adbe6a | -2.83136 | -54.08643 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 802297c6-a262-3470-96d9-64c304e0306f | -2.45825 | -53.6156 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5a09f3e0-bbd8-3865-a165-a1b540ea7c6a | -3.25906 | -53.62805 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 8048b1bd-29ee-3d00-86aa-16135d2ffb2a | -2.71079 | -54.95512 | 2024-12-02 06:03:00 | AQUA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 816682d0-82e5-32fe-9793-7dd3641d71db | -1.61829 | -53.85954 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 363c92b3-6df9-3ad7-a488-436e45871829 | -1.69591 | -52.63842 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48ebaa62-b24e-30f3-9bd8-473f38def6b0 | -1.98925 | -53.2877 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fcda5ce-e827-31ed-b0e2-e2b29a8cbcd6 | -2.63418 | -53.35417 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 6963f97f-8e16-3f16-9ef4-0cca3287fda4 | -3.63913 | -54.67702 | 2024-12-02 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd694525-0cf4-39d2-bdbc-375c2a9c7173 | -3.78085 | -52.02284 | 2024-12-02 06:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a4b4f015-266f-302b-a858-ba87de225f75 | -3.21164 | -53.12234 | 2024-12-02 06:03:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ffe73e03-6a84-3e8c-9b7c-bf7f1770252f | -2.01355 | -54.31133 | 2024-12-02 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2ed91e5-8c0a-3fff-84d9-63e721f3932b | -3.25805 | -53.82562 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c3c53d33-69a7-3032-b43e-89f53b1cfa38 | -4.27551 | -50.68088 | 2024-12-02 06:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3aaa9714-2e23-3234-90c8-aa66f72d2def | -3.7473 | -54.504 | 2024-12-02 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4e73fdaa-3e36-318e-a2fa-6cbb8222d052 | -3.85333 | -50.89503 | 2024-12-02 06:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 194ffad1-6f38-3e10-a11c-58590e20ec8f | -1.33069 | -54.97682 | 2024-12-02 06:03:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5ab0df50-d61b-3a0b-a38d-feb3a74c37b2 | -3.2669 | -53.63916 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5f9a5210-6f21-32aa-aea3-3f5ff3a6680d | -2.43838 | -53.62259 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 276ac511-382c-3383-a395-45b42fc77e21 | -2.43981 | -53.61293 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f14ac7c-110e-3ed5-ac4e-7369b7a653ca | -2.35669 | -54.48726 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6da04487-6fb4-323e-a90f-7ee7c7a9741e | -2.56457 | -53.39814 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8b6c602c-691f-3ddd-8d82-c10bd6810972 | -3.24382 | -53.92095 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58c622f4-c0fe-3fb3-847e-37dd35b07520 | -3.08511 | -54.11345 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 13f41e71-fb4c-3f04-a258-0421992f1f4b | -2.6574 | -54.07705 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bfd6110-8f91-36e9-bff6-bc207249d20d | -3.08373 | -54.1228 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9181c83-e29a-3208-ae1c-7d7882c32ba6 | -1.7821 | -52.74324 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ddd5f399-d407-3e9f-b296-22e2c9a648cc | -1.67313 | -52.79519 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 006d0a62-bb01-3114-85b7-45497d26e38a | -4.1949 | -50.68061 | 2024-12-02 06:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c54f9280-b9f4-337b-b015-ea669aea1a4a | -3.26052 | -53.61819 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| b376a8e2-3755-310f-968b-95280d0af51e | -1.71912 | -52.4783 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b9ae15a-bdec-30b1-b090-b73fc01c5511 | -2.55378 | -53.40667 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e88b621f-98cb-3082-af73-bfab767f11f5 | 1.1358 | -55.97663 | 2024-12-02 06:03:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a74f403-52b6-3515-a0a9-de53f0e58329 | -2.88477 | -54.1575 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94ffb002-25e7-313e-bab9-1ef4a905432a | -2.41352 | -53.85205 | 2024-12-02 06:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6ffdd687-658f-322e-900c-9f590a151133 | -1.90611 | -52.86215 | 2024-12-02 06:03:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b88f8eae-1a10-379b-89b6-72fbd33885e4 | 1.20723 | -56.02263 | 2024-12-02 06:03:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c426fae4-14e3-3b37-854c-6566a97734f3 | -3.74595 | -54.51316 | 2024-12-02 06:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ef5ef15e-b3ee-3110-b10c-f8b2f05e6826 | -3.09479 | -54.04802 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b8172d78-d8a6-3b80-abfb-23d5b171b48f | -3.42498 | -53.88142 | 2024-12-02 06:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c40067e0-9c89-39e9-b99c-974e69088718 | -1.67962 | -53.94397 | 2024-12-02 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 71d655c6-1e0d-3b50-a446-b649fc15b454 | -2.89381 | -54.15887 | 2024-12-02 06:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e030806-a2f4-3e7a-a66b-f74071fa12d9 | -3.18246 | -54.33166 | 2024-12-02 06:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b41fd993-53d7-3ffa-b6f4-657c73fd7d96 | -1.2507 | -54.53561 | 2024-12-02 06:03:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README76.md)
