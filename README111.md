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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecff7b88-6e98-3252-b402-eb6390e3df7c | -2.80653 | -54.08633 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 294ca323-f39e-3aa5-9803-7bf414c7b5a1 | -2.80304 | -54.0858 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18b34cb9-d74c-3a4a-9301-e9a72749d6a9 | -2.78283 | -54.0312 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2810c25f-1e19-3d7c-ad61-79ebde159a7d | -2.65281 | -54.30917 | 2024-10-14 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 52171ba0-1202-3bdd-a851-f5f55e46aa23 | -2.65222 | -54.31294 | 2024-10-14 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9e7ec8e3-dbea-3cc4-af35-8ba436b9e3ee | -2.57286 | -54.00821 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4ee37002-0db2-3612-bd74-600d2bebde0e | -2.57227 | -54.01207 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 092b3c92-7a0e-36c1-8a4d-bf8fa37d9096 | -2.56877 | -54.01154 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 052dac54-c3b9-3b6b-bfc5-d72b9b374086 | -2.33266 | -54.58903 | 2024-10-14 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e8f2afdc-15aa-35c5-a6a8-ee1e47893061 | -2.33209 | -54.59269 | 2024-10-14 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 968c24d8-85db-3d97-a10b-82561fa3fe13 | -4.51099 | -54.86556 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f6ff470-f9d9-3667-9245-b353bb599153 | -4.49612 | -54.96276 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56ff3b03-23b3-3f10-b9b9-1c2e3f175f25 | -4.49269 | -54.87036 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fc37c0d-6e25-38ce-af6d-30c3eba9ef85 | -4.49212 | -54.87411 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4d7e11f-dda9-3aa4-9fdd-b1fc98a534ef | -4.46211 | -55.07089 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65dcedaf-613c-3668-839c-ff8255f58c4a | -4.4587 | -55.07037 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58021ce9-b450-3721-ac20-3ab9e9a3d8ce | -4.45828 | -55.07072 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b083e848-ecaf-3523-9cad-fd6e9ced8b6c | -4.45814 | -55.07405 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59bf8c2c-0b66-3157-9cde-f6eb76340f78 | -4.4577 | -55.07439 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4926d681-48a5-37b8-82bb-c92add3e21fe | -4.45157 | -55.00183 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4c35e70-c5ff-30c5-a933-7c0af1c578fc | -4.4504 | -55.03177 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fe3a769-4af8-309d-8c9e-0b0c5e128118 | -4.44079 | -54.98116 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dcc5a23-7111-3e89-bee3-a31a1ee601b4 | -4.43738 | -54.98063 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae4d6d9b-2e48-360b-93b6-f00f038146d2 | -4.4369 | -54.91589 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44f07368-3252-3af0-951c-66606cbce040 | -4.42877 | -55.05857 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d5ace3a-0bea-3b46-8021-fcf6f2d415f1 | -4.42536 | -55.05804 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0acd9e1c-da13-3c71-81a1-e134b226b788 | -4.40948 | -54.98006 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aba4c21-9b2a-3717-be8b-b3268c03d141 | -4.40148 | -54.84948 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40ddd7ce-80cc-341a-b5dd-cdae85e6b322 | -4.36677 | -54.962 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a67caadd-b83a-3705-a8df-d381ff71d270 | -4.36653 | -54.96212 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bd3ad6f-6060-3a64-a01b-6d4507f79046 | -4.35789 | -55.13404 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fd2d4dfe-105d-323f-a720-064546481d8a | -4.35733 | -55.13772 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2231715f-955c-3645-ad63-0f24e7c1fbf9 | -4.35448 | -55.13358 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d5bdce7f-4cca-379f-a5a7-ec5284a7d206 | -4.35392 | -55.13726 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d530af2c-f868-32ef-b563-99f1f10a685c | -4.34769 | -55.13251 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3dc11e59-c57a-3057-8633-a853a0804d4f | -4.34485 | -55.12832 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c84ff39-8400-39ca-a0ca-a6b121438d9b | -4.34429 | -55.13197 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d898a98-913e-3afd-a7c4-3b1e7b375e1f | -4.34399 | -55.26958 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3947dfea-66c7-3a27-9849-d17f5d465f5b | -4.33451 | -55.05535 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1212dbe6-9722-351d-903c-a4c20dcbf6e8 | -4.27371 | -54.97435 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6298a79-02d4-3b21-9283-e130d9b78d3c | -4.27314 | -54.97803 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66c86861-ee76-3d3e-9f36-03cab4ce7c74 | -4.27029 | -54.97384 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f56e747-e56a-3af2-a2ba-b91abce9a794 | -4.26413 | -55.08223 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6c28901-4fd5-349a-9e59-a1d2c3f6104b | -4.26356 | -55.08593 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f95f62-dfb4-37ec-aadf-b2fdc89e8c1f | -4.26 | -54.94971 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b632b8f9-6c2c-3c49-9c9d-d34a271904fd | -4.25986 | -54.95013 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a1ea0d3-954f-3c2b-93c9-7c1c3ea5bf8b | -4.25943 | -54.9534 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4efad06-e6a3-34e2-8710-5eaff9891258 | -4.25928 | -54.95382 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa63f616-efc5-3c96-9c38-089ea7c92957 | -4.14505 | -53.94536 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a5c72ec-e03c-3e92-8413-a7b330f80328 | -4.14088 | -53.94884 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37560cad-b259-314d-8a54-79e8b316f286 | -4.06575 | -54.7346 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c73c4c7-5029-3f29-954b-aefc2ef7f767 | -3.81459 | -54.11711 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae6dff5-ade6-3550-8421-5a4beeaea37a | -3.81047 | -54.12044 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c81cd76-a0ab-3c95-a05c-3934e24d50c3 | -3.75585 | -54.33484 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa09b29-b19d-37d6-91d5-ddaabf398326 | -3.69349 | -54.57883 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac30b7e6-edad-3512-b19a-28627fd50b77 | -3.69291 | -54.58259 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7b1a616-4088-3b33-bb61-9e8691805273 | -3.69004 | -54.57827 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9ae4986-3e9d-3553-98d7-b1758cfeb3fe | -4.32575 | -55.43259 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f10ae62-88bc-36e1-b6c0-da0806d49f6f | -4.32519 | -55.43621 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba5e1e6-7ced-3eab-a408-de2a31b4de46 | -4.2977 | -55.4356 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0679eb9-08ca-351b-b6bc-f795a3377529 | -4.29488 | -55.43148 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1f446d-114b-3389-93ff-3353309c99b9 | -4.29255 | -55.4347 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84928ede-1ecf-34aa-be57-0be51790e8c7 | -4.29199 | -55.43829 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a205818-3bf2-344e-bb78-62b6f4773c35 | -4.28975 | -55.4306 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f2c9227-bf73-375f-b637-5a018843a633 | -4.28919 | -55.43419 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71b76dac-71c9-349f-8c70-8d783e040344 | -7.09576 | -56.46489 | 2024-10-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09ae7c25-696b-30f1-8d01-0f1c07907df0 | -9.70478 | -56.64905 | 2024-10-14 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0980d4-5821-3365-bf86-4ef4ce98f138 | -9.47627 | -57.66671 | 2024-10-14 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4383ce8e-b749-33a5-b328-fab1b95b80a1 | -9.47296 | -57.66619 | 2024-10-14 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 514f92c3-ee55-3094-af18-6ecce24761ff | -7.52617 | -58.29297 | 2024-10-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 368948f0-7697-3850-983e-00ce26d9c29e | -6.52563 | -58.41099 | 2024-10-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826a696a-5d3a-3d93-abd3-d0796b2886a5 | -6.51952 | -58.40639 | 2024-10-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81a7ab23-5482-3600-bc26-8118f358fe9e | -9.1195 | -59.02154 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad68af88-3428-36c3-9873-ac55325671ff | -9.09725 | -59.01081 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a46ee24-441e-3110-89ad-f3e4d15fcf0c | -9.09391 | -59.01028 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec679a3-036c-3321-887d-30accb10bc97 | -8.18174 | -58.25123 | 2024-10-14 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1219cd3c-0dfa-355d-9f44-f1aa9cc3dead | -9.17218 | -60.42732 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 067b59fb-f7c9-331e-ad48-c843b0e5d1fa | -9.15069 | -60.39623 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2eff0bb-f833-3d8f-9bf4-496990012162 | -9.1146 | -60.39825 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 125f2841-a7d1-3227-bd67-4741a51681d5 | -8.80451 | -60.14682 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 993b010e-daa4-3ff7-b8c4-7ca5d24143b1 | -8.80387 | -60.15072 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d73f4bb1-9184-36e9-9677-412201858aa7 | -8.80323 | -60.15464 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4a096f5-f26e-350a-9c42-b378b257b6fb | -8.80169 | -60.1424 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38d7fa25-95f9-39e5-bcb4-ad65a0b1018a | -8.78092 | -60.13911 | 2024-10-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc0725d5-07f3-329b-bc4b-4958236fc193 | -10.36821 | -61.19562 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d681770-1fba-322e-a583-e8d5e818f2c8 | -10.28624 | -60.99072 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1324657a-4c36-3e68-a3e5-74dce6c8addb | -10.28271 | -60.99009 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb670520-2608-3e7d-bd02-5906a90357cf | -10.19658 | -60.89801 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe2c69ce-ffa3-39ef-88cb-b7f974b333c5 | -10.19593 | -60.90191 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74839001-6b7b-36a2-a737-24a528cdd4a5 | -10.19527 | -60.90586 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e40833f-6b3c-3b53-972f-0e919cc78aa0 | -10.1946 | -60.9099 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31ac5aba-9b1b-38ea-a27d-7abc323b4a56 | -10.1911 | -60.9092 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b707243-4f5a-34db-a42f-5a9c796de803 | -10.18692 | -60.91252 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bbcf4d1-7f49-3162-9e19-affe8ae2867f | -10.18338 | -60.91206 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9c36386-ee2e-3908-b770-2a177d68a021 | -10.07147 | -61.12698 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0572819-ff3e-3292-9c6b-724011d57bdc | -10.06792 | -61.12631 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5a32075-6d59-3a44-bbd4-577a6df404a3 | -10.06723 | -61.13045 | 2024-10-14 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bd0fc5e-7803-3513-816e-b2b2a6fa4c17 | -9.85646 | -60.27993 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47b20ef9-d4e9-3243-9a1c-f2ff902a1688 | -9.85302 | -60.27936 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9fe00d1-36a4-31c6-985d-b0ffe8438cd6 | -9.85144 | -60.31043 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README112.md)
