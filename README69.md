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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7246037-b5f5-3b06-9da5-12ef4e5d8094 | -7.83794 | -49.98018 | 2024-10-11 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b87d969-8361-3062-b8c9-08d3b6697023 | -7.69052 | -49.82775 | 2024-10-11 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b174d26-8109-3a4b-8b5b-89e5b9dff012 | -7.68914 | -49.83626 | 2024-10-11 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 52a2dcef-0378-39a7-8f9a-5cf4acd54f4f | -7.68844 | -49.8405 | 2024-10-11 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d1404aa-c9c8-365e-9bd9-39b28a676dce | -7.6869 | -49.82714 | 2024-10-11 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5d6fec3-2c4a-3e99-9e3e-03468382f11d | -7.6862 | -49.83139 | 2024-10-11 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80c84936-3a21-3cce-8e63-cdae3c9c8751 | -7.68188 | -49.83503 | 2024-10-11 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a3b4dab-9874-32e3-9593-2d85e090890a | -7.57548 | -49.57358 | 2024-10-11 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 865ec6ed-8aff-3beb-bd56-d68f7d2b366f | -7.40171 | -49.64548 | 2024-10-11 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09674d59-f88b-3a1d-a01e-4313b56293bd | -9.02721 | -48.81111 | 2024-10-11 04:25:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e630ebf-5c9c-3656-9592-b1e001b1941d | -8.83213 | -50.06738 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e60e32f7-26e1-384d-9e1a-2e58a0f1b12c | -8.79077 | -49.79187 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17876252-89c8-3ce4-a0c9-cb07f37a456b | -8.7872 | -49.79125 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 731e000e-b5a6-3451-aa63-c5b174347a7a | -8.71349 | -48.99492 | 2024-10-11 04:25:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bee6efd-6d13-3129-a144-4d0b989eae37 | -8.7075 | -49.98322 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f8bf8bc-f685-3b24-ab1d-f879c7f3bb36 | -8.62948 | -50.04539 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b228526e-7a37-382b-9e06-848287af10be | -8.58612 | -48.93517 | 2024-10-11 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43458a4a-b381-3515-951d-faa50193680d | -8.27688 | -49.91175 | 2024-10-11 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b665d48-1680-3bdb-937a-fe177bcd8819 | -8.49617 | -48.64522 | 2024-10-11 04:25:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d9d2f770-ec12-395d-b3ca-e491f5462abc | -8.38365 | -48.64713 | 2024-10-11 04:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5cf20b1-8a57-3cec-b4e5-05e385a86aa0 | -8.38304 | -48.65087 | 2024-10-11 04:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b52ad608-ec09-36c5-8c6f-bb3f939fd270 | -8.38023 | -48.64655 | 2024-10-11 04:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3e9310e-cdd9-31d5-9d92-845c5877e404 | -8.83937 | -50.0686 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4f09de4-a9de-3b03-b092-be91838f0a34 | -8.83575 | -50.06799 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87d0e50f-e259-3841-8fd9-5e9fabff1f8c | -8.83505 | -50.07223 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de4f2a7a-a77a-35a7-a7ce-bf5931bb715e | -8.78363 | -49.79065 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e5a0501-b922-34fd-a9ff-20453d4da697 | -8.73022 | -49.71428 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06000132-cbc9-398a-98a8-0d94a4b8bcaf | -8.72099 | -49.94669 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eaa23ec-1269-3d4e-8d85-3b78e5daac12 | -8.7082 | -49.97902 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58c6890b-17b3-3cbc-857a-30dcc07ce3ee | -8.70459 | -49.9784 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3236144a-18a4-3354-9cc8-747382206581 | -8.70389 | -49.98261 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d4fa3eb7-1b74-3f6d-b671-6e4d2ac5185e | -8.69385 | -49.9982 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd8b1388-130c-3f3d-893c-64a547ec8aaf | -8.69315 | -50.0024 | 2024-10-11 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8747a39-9055-37ee-8c19-3ac940bdabfd | -8.44148 | -49.44478 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 092aefdd-bdae-3e9c-ac5c-281142a673ee | -8.33442 | -49.96921 | 2024-10-11 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1e95c0c1-f3cb-3ab8-96d7-932d1f142a05 | -8.33079 | -49.96859 | 2024-10-11 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 799829d0-316b-31b8-be4c-b891d4d7ef38 | -8.22685 | -49.60287 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8729c850-1148-3e4e-bea6-b0a8011d91c9 | -8.178 | -49.76402 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e952df7-20cb-32a1-89e8-951db35b3761 | -8.17715 | -49.20024 | 2024-10-11 04:25:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52e54255-a512-3bc1-992b-f4767a90762f | -8.07075 | -49.66597 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9065d3e-aaa0-3c1e-bddb-965ffb278910 | -8.06104 | -50.03662 | 2024-10-11 04:25:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 907be069-f785-33a1-8cdb-68ba4dad38d2 | -8.01632 | -49.82984 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc0f0ad9-55aa-3d5a-9427-f6bf2d1d6af4 | -9.87169 | -50.15567 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82f525f1-1df4-3741-b09b-437dc0882ca7 | -9.8681 | -50.15506 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 347e9d5c-e7d0-3501-9930-bcd6d0b0721d | -9.79968 | -50.06744 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9adb6370-4c42-3eaa-a502-0aa0b513de5c | -9.7961 | -50.06683 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2344875-e58b-34a4-9c35-3f223d72f0a6 | -9.79321 | -50.06208 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edf8497f-b3b5-3cc0-8232-cb8e2e500f97 | -9.78894 | -50.06561 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09713b00-0e0a-3033-8523-5e566ce2ff0f | -9.74306 | -48.96095 | 2024-10-11 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dea0289f-4b94-3017-8845-62f29bb79b76 | -9.67626 | -48.9194 | 2024-10-11 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e100b46-7698-3a2b-9c82-99c80fc53634 | -9.67284 | -48.91887 | 2024-10-11 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 099eb2df-3b1a-39a5-825e-ddd372ff20cf | -9.62631 | -48.98856 | 2024-10-11 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6ea655a-1e95-3723-9876-e7361152ed73 | -9.62569 | -48.99234 | 2024-10-11 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d58e300a-ad95-3bb3-b7be-46c428666e1c | -9.62288 | -48.988 | 2024-10-11 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 53acca19-f515-37d1-b289-7368a3ef55cf | -9.62226 | -48.99178 | 2024-10-11 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ab2c818-02b5-30f3-aa70-f7afa6ca4205 | -9.5822 | -50.08931 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28c88c00-9712-3c53-9717-f6596f7b5ae4 | -9.54899 | -50.22197 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfb6de5c-07f4-3d7f-ab62-66b09d15ff22 | -9.54608 | -50.21712 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 056ab43b-ea97-33d1-9437-1ada6c7aa66e | -10.86093 | -49.74518 | 2024-10-11 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2206c2b-9863-3661-9e80-89064bfae97b | -10.56039 | -49.94119 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d128d5fa-d571-3c85-af38-5878e9ede1bd | -10.55686 | -49.94059 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e0f2f47-162b-3507-ad7f-831b82bf61b9 | -10.55619 | -49.94462 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb7796c8-cb33-3cb2-8f10-69fd47b28b6f | -10.54627 | -49.93879 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2505282c-35d4-377f-83ce-52d33f06daee | -10.54274 | -49.93818 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad1c973d-1edd-39d7-8943-7e750339ea66 | -10.54207 | -49.94221 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c82cc1ac-f08e-3f09-b529-48b79be7a8ac | -10.53854 | -49.94161 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 532b6acc-6442-3355-ac35-f7d4acf23cd8 | -10.48856 | -49.95876 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 970713de-8efb-3dcf-8a21-62e3f4edce6a | -10.48503 | -49.95816 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84dfb48a-9313-35f8-9ee5-ce7d0626d163 | -10.46972 | -49.98468 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 951c18c9-5a5c-3e1c-b6dd-b7a7c95385fa | -10.46667 | -49.95919 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa2c1ab5-f2dc-376f-8637-9ea197c63e2f | -10.46246 | -49.96263 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e3ae154-9183-3513-a94c-bacfcd610637 | -10.45977 | -49.97882 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a83c8fc-6540-3a00-9086-cb75cdd686d5 | -10.45623 | -49.97822 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28b74233-0fd4-3b6c-9bb7-b33e1876b14b | -10.45118 | -49.96487 | 2024-10-11 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44b33d00-99e2-3864-bd4a-62ae704b69b8 | -10.32767 | -50.56659 | 2024-10-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e98401e5-ae9d-3338-bc1b-8387227fc797 | -10.32402 | -50.56596 | 2024-10-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d48d79f-c4ee-3fbf-b49d-4e6b87787377 | -12.1365 | -50.5389 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38f40db1-568b-3dd6-99b3-4d54f8ed0941 | -12.13581 | -50.54304 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de65e64e-bd90-333a-aef7-3505311f624a | -12.13362 | -50.53413 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c47df8b7-e2bf-3c36-ad25-d7f6afe7c550 | -12.13293 | -50.53827 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04ad4eca-dbad-35ab-a674-9729a7b908c2 | -12.13075 | -50.52938 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5093dbe6-e7c6-3539-b5f7-0390935c61fa | -12.13006 | -50.53351 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdcc18de-da6e-326b-8587-83a29b7052d5 | -12.12867 | -50.54179 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc9103c9-351c-30ff-b730-814f801e1ddc | -12.12788 | -50.52462 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33427ce5-685f-3be8-b436-92e537462f34 | -12.12718 | -50.52876 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b9b7546-e5b8-3bd8-86fb-7aac7f4ae513 | -12.12649 | -50.53289 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95e67b1c-0714-374b-97e3-ad52c82267a3 | -12.1258 | -50.53703 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41c296fc-6b1b-37c4-b367-4cbf2873fb35 | -12.12511 | -50.54117 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ace1f630-eb53-37b6-9395-eed39e5671fa | -12.125 | -50.51987 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1793f17e-ff98-3b2e-b0ae-fb899f4bbc8c | -12.12431 | -50.524 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2420f57-518a-3b17-a3b0-23eb5fdf39c8 | -12.12362 | -50.52813 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad28c07a-751c-3ebe-8438-980bb1f588cd | -12.12293 | -50.53227 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1c48aee-df46-3342-9dd7-62c6841fb7e1 | -12.12223 | -50.53641 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e32888c5-1b00-36bf-a1c2-aedfd0ffa337 | -12.12154 | -50.54055 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 27ad9d68-9b5d-3b41-a5eb-4102d321e591 | -12.12144 | -50.51925 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fecb7ea-ee06-319d-a68b-09a182e0638c | -12.12075 | -50.52338 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5686411e-fba3-3818-a2a1-38222c76d215 | -7.96254 | -54.76812 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 82303955-f7d5-3fc1-a719-28b2479e7019 | -7.96152 | -54.77376 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 034892f2-5820-33aa-b5ca-18580f5feec1 | -7.95861 | -54.76154 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6ea29a9-1f9a-35bf-bd80-b9ae54adbb6f | -7.95789 | -54.76094 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README70.md)
