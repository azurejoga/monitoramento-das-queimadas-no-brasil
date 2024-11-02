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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05f27ace-d0fe-30ea-a851-316e7a0c6c12 | -2.77675 | -52.89924 | 2024-11-02 05:48:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed15e084-40ab-3212-9f5b-3a0785a355f6 | -2.77382 | -48.71137 | 2024-11-02 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 05166f3d-9e76-38d9-89ca-6adf006f7ed5 | -2.77257 | -49.83145 | 2024-11-02 05:48:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c9d5b591-2bcc-303e-919a-0eed49508bef | -2.77202 | -48.72353 | 2024-11-02 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 76b60c9d-e5d5-3352-bf1f-81e49566e6be | -2.7409 | -54.11305 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b713322-7f15-37f4-9b47-72fdca253bab | -2.74013 | -51.72899 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 256e45e0-64f1-3dd4-be62-651b7bc29940 | -2.73944 | -54.12264 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7074b03e-d506-3c82-ad21-ce12c56530cd | -2.73881 | -51.73787 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d00469fd-040c-3e1b-8212-dd9f93ac1e73 | -2.73763 | -48.74337 | 2024-11-02 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 866c2652-e84e-3132-8687-91701aa4dd30 | -2.73125 | -51.7277 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3c09c7ef-e2ae-3292-a967-019a11107098 | -2.72603 | -49.17138 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 932c0409-00f1-3c20-b831-6e7eddc86591 | -2.725 | -51.70864 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 948f2b2e-1bbd-3863-ad50-e73adda20f15 | -2.71064 | -49.2791 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 313f6433-f210-33f2-8572-285e5c630d5a | -2.70923 | -49.28361 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8985aee3-08f5-378e-89e7-0896b8a5b3d4 | -2.70904 | -49.29027 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b5746f1d-a2ff-3213-8bf5-753c40c86af3 | -2.70331 | -48.63325 | 2024-11-02 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09acfcdc-fcbe-385c-92b7-92643f625e27 | -2.67556 | -53.02298 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0b20ffc2-dcab-3a85-94df-838cd70a963a | -1.21469 | -53.65013 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f070586e-2fc3-3cf0-8d59-4ef319057bda | -2.65888 | -49.84133 | 2024-11-02 05:48:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8503b325-00a4-3890-bad5-da16bad3c844 | -2.65316 | -49.25285 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad6eddae-db56-3219-abae-7ad6b758f50e | -2.65128 | -51.70952 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 25527c09-8398-31fd-9763-158250784968 | -2.64996 | -51.7184 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bda52d0b-99c1-384d-b013-9be26a2086f9 | -2.64933 | -49.83997 | 2024-11-02 05:48:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5bfd668d-7232-3163-8297-171f18fdc638 | -2.64468 | -51.75386 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bade59fe-d765-3ff3-bc9f-98e3c35f4de2 | -2.64108 | -51.71711 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b43f05b-1b4a-3c47-881d-081def9912f3 | -2.6364 | -54.25883 | 2024-11-02 05:48:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b9143bc4-4320-3aa0-afb1-618ddf871009 | -2.61456 | -52.44868 | 2024-11-02 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47001737-3750-3ffa-89d0-bae32e694f75 | -2.61343 | -48.33165 | 2024-11-02 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7665d4a3-5ace-3b54-b0b3-b509526249e1 | -2.60023 | -49.8157 | 2024-11-02 05:48:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0f5663b2-60cd-3568-8e68-f701b7ad02b5 | -2.59949 | -49.33005 | 2024-11-02 05:48:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5075d735-1252-367d-9849-310ca21fe2c0 | -2.57488 | -50.05163 | 2024-11-02 05:48:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 49bc237c-d20c-3f77-8179-7f32725bca3f | -2.5571 | -53.99851 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dc724934-2283-31af-8016-ba6b001d02ad | -2.55568 | -54.00803 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a6ebc822-19f7-345a-aef0-cc8b16c8981c | -2.55503 | -48.17183 | 2024-11-02 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 81df0ad7-fbb8-3b7e-a4d9-5123b045ffd6 | -2.54433 | -48.17038 | 2024-11-02 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ba1b6e21-7284-3860-9d76-3b22b0f23c82 | -2.52229 | -49.23305 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b008acfa-8312-3ca9-967d-cb379f010f68 | -2.51995 | -51.7776 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f7ac99c-f78b-3253-84be-225d274e32d5 | -2.51863 | -51.78645 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d35a7acc-be40-3560-9a69-2059f6ec46e3 | -2.49418 | -49.0794 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3aca79a5-93f2-333d-9134-2f8b2236278e | -2.46401 | -49.77983 | 2024-11-02 05:48:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b04b3164-301d-32cd-a57a-726a57592570 | -2.4625 | -49.79021 | 2024-11-02 05:48:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7a46ad1a-e4a8-37cf-83e8-7831ddd9dd4d | -2.42396 | -50.50465 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 05e96191-c336-3f19-a0f5-ac91954246fe | -2.41618 | -50.49376 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de131bcc-2d8d-3339-a8d0-48134c0fc087 | -2.40774 | -50.42389 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cfe92aa0-6c89-3a3c-8d5d-db0b4df8a64c | -2.39569 | -50.31334 | 2024-11-02 05:48:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bca20cb0-5558-3496-9fad-91962d6d787d | -2.39139 | -50.59719 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e92c881b-8463-3323-a00b-d38606e320d2 | -2.37924 | -49.66511 | 2024-11-02 05:48:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7fe653a9-02c7-3204-a081-ae04773645b7 | -2.36 | -47.62022 | 2024-11-02 05:48:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 3f54c66f-b6ce-3912-9a56-a9d76acf0837 | -2.35885 | -53.71663 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cf845337-8898-3b13-a529-0f40597ea799 | -2.35805 | -49.16956 | 2024-11-02 05:48:00 | AQUA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 03105c9e-ed47-3104-a6a9-dee3d492df4b | -2.35791 | -47.63455 | 2024-11-02 05:48:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a75d53a8-526b-3ed7-8724-308b3deec80d | -2.35744 | -53.72591 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e0f36077-845f-3052-a99f-86606cb8e97d | -2.35678 | -49.17427 | 2024-11-02 05:48:00 | AQUA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f0306eb3-ff15-39f1-b4a1-767241b3a9b1 | -2.32242 | -50.4442 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db7601fa-dad0-3734-bacc-720615fbac35 | -2.31426 | -52.909 | 2024-11-02 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9d31e16-1510-3c1b-a2bf-0d8aa9da0e15 | -2.29903 | -50.66399 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2abded30-802c-3d43-991d-c73ba8f49caf | -2.2899 | -50.66271 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 83195c81-db38-32ec-9756-490a8ea0aa16 | -2.2885 | -50.6721 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d0cdd200-868a-3526-9ca3-f7c3eb034221 | -2.27788 | -51.91934 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 360d5f0c-25ff-3571-8b4c-53c50a143ea2 | -2.27657 | -51.92814 | 2024-11-02 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27bd5eeb-89cd-3448-aa83-d16e8b33dd31 | -2.274 | -51.13863 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab3f0d78-e089-3ed6-a41a-d7a50b58764c | -2.27222 | -53.73622 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 107787e7-dd8b-33ec-be90-3956666849da | -2.27081 | -53.74557 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f563fb48-e14b-33a7-9a01-b023b5371278 | -2.26939 | -53.75492 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 15426f9a-2625-3816-9259-49bd3b983af2 | -2.26532 | -53.65905 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 22c3e865-d9ed-3e56-8128-3f35432d7b5d | -2.26453 | -53.72553 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58942ace-de86-3b30-a5dc-03f805420131 | -2.26312 | -53.73488 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a55d9fc5-fd78-3179-aea0-9ec41d14acee | -2.2617 | -53.74422 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 24dec6ed-f535-3e86-b85d-dc603656cff7 | -2.25862 | -50.43907 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f4793e08-be39-3092-957d-646288a8717c | -2.25718 | -50.44867 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 83925a64-82af-3df3-b839-376c6840fe67 | -2.25085 | -50.42815 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| dce4f98b-8e63-34a3-b785-05123ebff0cb | -2.24941 | -50.43775 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a69dafb7-284c-33c2-86e9-8d32a1efad6c | -2.23597 | -50.71243 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9dafb139-ea59-3d6e-a0d6-2819c3b66994 | -2.20973 | -50.32373 | 2024-11-02 05:48:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 381d6e00-84ff-3a4b-8f6d-51139b30f393 | -2.19263 | -50.31136 | 2024-11-02 05:48:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e46069b9-abe0-3e96-bc20-02287909c9b0 | -2.18667 | -50.79476 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e7808b3-f859-3e69-b95b-4193976691c2 | -2.17738 | -48.72424 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d6e14abd-074d-3536-9bd4-ee4a0dc5b744 | -2.17097 | -53.67657 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6cdd037d-9c3e-3e39-b210-086767589319 | -2.16955 | -53.68593 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9d6e1368-232a-3d31-8656-254170a471ca | -2.16719 | -48.72277 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dbd08479-349d-3b63-8f2f-2983088ec1b5 | -2.16547 | -48.73467 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9a81ddb3-7e9d-3394-aca0-540cb2e103a3 | -2.16329 | -53.66595 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 845bb637-ab2d-3ced-a7b2-f37a497b8c12 | -2.16187 | -53.67528 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e230a067-4872-3920-8851-3964e8b6ec15 | -2.15462 | -50.13942 | 2024-11-02 05:48:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0cff28ad-d707-389d-808c-9b6a34ff4b0a | -2.1191 | -50.13868 | 2024-11-02 05:48:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ad33d100-540f-343e-b4c3-9235c4d355e3 | -2.11633 | -50.83196 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8e5e52d-8ab5-3115-b285-cf30c88cc466 | -1.88683 | -52.125 | 2024-11-02 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e4fe132b-8294-3bcc-b5bc-0c21a1f2c615 | -1.88551 | -52.13377 | 2024-11-02 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d172bf1c-d9a6-3b53-ad08-8e24a2b34cd7 | -1.86544 | -52.32815 | 2024-11-02 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5f37b5e7-c667-30f7-9d96-15d9f4d6868c | -1.79578 | -53.04014 | 2024-11-02 05:48:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a6fba6d3-ec91-3a76-9b6d-73d6a55b4977 | -1.60436 | -47.20335 | 2024-11-02 05:48:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 4ce9ce92-781e-39d5-b2b0-003cff548462 | -1.60215 | -47.21833 | 2024-11-02 05:48:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| f742835d-a8c3-3813-9a0e-ccd7223fb4cb | -1.59957 | -52.37009 | 2024-11-02 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ad40423b-2570-32f6-9636-67e329ec5b86 | -1.58693 | -52.15285 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e45d8e2b-101f-32c6-87a7-8da7e1902b28 | -1.58562 | -52.16163 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 8f0f0ba9-368f-3a82-8ad9-1a0380555bab | -1.5843 | -52.17041 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4211844e-00ec-3442-9d28-b2c6ee6d3153 | -1.57941 | -52.14279 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 96d07be9-d6c9-3ee3-8d00-e12445d2e26e | -1.5781 | -52.15157 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4bc0ba97-1732-3652-a171-9858c402b8f3 | -1.57678 | -52.16035 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 84901b1d-c9eb-34da-9df1-91f0d99c891b | -1.56269 | -52.19417 | 2024-11-02 05:48:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README100.md)
