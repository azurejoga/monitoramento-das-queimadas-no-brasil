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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 617a3b91-d03a-3ced-919b-ce95814d0b43 | -3.20925 | -53.84452 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 807f0070-aa94-3fab-a394-8c2dd06c78c7 | -2.53333 | -54.03497 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d2bbb53-98cb-3a48-b946-0939a4167482 | -2.55588 | -47.04093 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cb74477-048f-3b96-8483-b0d86eb83674 | -1.03235 | -53.18618 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94cd27e4-1618-3634-839a-d136bfee8e40 | -1.79822 | -52.75473 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0bac917-b7b6-33c4-9b4e-e1d0b83365ad | -1.5911 | -52.27238 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bb82179-71a1-3148-a1e7-ebdeab4acba7 | -3.00829 | -53.23177 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 28235233-2953-35d1-9f4f-d6be2e6b5d2e | -3.23939 | -53.92494 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| afbe4141-f8ec-3094-a0d1-5df7517ef82e | -2.87045 | -53.99788 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eff53834-40c3-3660-b67a-b41fca1077f9 | -1.49863 | -54.95339 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d4c2820-636e-3eda-be84-6aa3949edd42 | -2.98613 | -49.58714 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a5d23e9-a176-33ae-a128-8539dbd616fa | -3.11507 | -53.98552 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a737dea3-dfc4-3488-ad4f-84fa485bc70d | -2.57067 | -54.33281 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8951767-8874-3d96-b057-cc6616bb3dfd | -2.22879 | -53.62031 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53b0274b-0d2a-3a2b-97fc-b8a1ac4f8f1c | -2.43027 | -48.17197 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0008c77-027e-37ee-98ec-c29a083773a8 | -3.29476 | -50.36101 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f1f0ac6-1499-332e-82a0-40fc9f83d8ac | -3.67975 | -47.12619 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3d5de4de-f89f-3a69-ac10-3a676ce27449 | -2.23837 | -54.91738 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8456ed-b242-3f6a-9bd2-dd9d7d494e79 | -2.69167 | -51.98344 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10bf1ec0-a4ec-3749-a5fb-1570df396bd6 | -3.63476 | -54.16623 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8203421-0dcf-303f-bb5e-41529c7f114d | -0.9863 | -51.77967 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4123ecb-4b47-33fa-aa7c-b050faf801a8 | -3.09368 | -53.33434 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8876abfa-bd60-3a06-a15b-8a69d917ac21 | -2.32599 | -50.67642 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b74eda3-68dc-3896-951a-eafe65092396 | -3.39525 | -50.30001 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2218b040-5d0b-3cea-a9a2-508abdcb5f37 | -3.0235 | -47.80061 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7610639b-c7c0-33b8-a766-4d4b8461648e | -1.99379 | -52.0966 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6751cc2b-f1e5-3d80-ad07-f48bde08a45b | -2.27506 | -46.4303 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bf100d5-ee48-36f4-a5f7-d365849456ea | -1.65007 | -52.6339 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 616704c4-5860-3e39-9569-6097f7cc806f | -2.76138 | -49.22295 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bba3cea9-8aae-39bb-95b0-0416b09b4a4a | -2.44916 | -53.70546 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a16ece0-a689-3d07-a6c1-defa69242028 | -3.02624 | -53.40936 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35404942-86b3-3906-bc75-8b4f06815f9f | -1.34091 | -54.98527 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7fc02317-8738-3b0e-8ac9-9226e46bdf19 | -2.89934 | -53.95908 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f34dc0f-de39-3be7-9afe-b2edc171f0f3 | -3.02512 | -53.41657 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a633e476-2a02-3df5-8c6d-2073c1f91d59 | -2.53612 | -54.03898 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b327e71b-504d-3305-a0f0-12f268745982 | -2.96903 | -53.93024 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a82bf32b-c191-3c3b-a18e-bb082f712567 | -1.18397 | -54.02848 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e60b05c-b90a-3c6f-ba29-80a19c72a96c | -2.99458 | -52.91497 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31382392-b3e3-3a2a-b656-9fb793b7212c | -0.95219 | -51.65703 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47495b70-d5b5-3f8e-9398-369d4da10c73 | -3.24356 | -50.59163 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1691a48-d409-30e6-b44a-c9be85b01eaf | -1.38227 | -53.64946 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9718bc54-c683-32dd-ac55-40ac9041ba50 | -1.28277 | -51.73356 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81245a10-dd64-3eff-94ee-3fdc4234fa43 | -2.81289 | -54.14655 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab23f4b3-5ff7-3361-af13-03271530e774 | -3.29093 | -53.27843 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e6bcc66-e086-3278-a672-50368d2db1b4 | -3.77515 | -51.67487 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc426a2b-6edd-383b-ac68-dedf3f26821f | -1.8943 | -54.54589 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e5f72d8-7df9-385f-a4f6-5090953caf8c | -2.77047 | -55.32262 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31735bd9-d23e-355d-9169-27ede02d8219 | -2.60995 | -51.81363 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48a08982-1c71-3232-b9a8-356a5b2ac27c | -3.78288 | -46.69673 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebba327d-d1d8-3f04-b6b3-f3897e9ea1ce | -1.08346 | -52.43407 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25379df7-bd0e-3a8e-b0db-7409513ef8b9 | -2.73949 | -54.03516 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de9e753-998a-38a2-b003-925e6c8e6303 | 0.69499 | -51.44201 | 2024-11-30 05:01:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8f4cc3-370f-3b95-a171-b845aea045f4 | -1.5106 | -45.89836 | 2024-11-30 05:01:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b8e2996-df45-3a93-b210-f99bae2b5165 | -1.44747 | -54.37381 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6676e458-17b6-3dd6-a118-d4bfe7e4a709 | 0.0307 | -51.10254 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2b50712-46c7-3f69-bb04-005813c614a7 | -1.04706 | -51.7401 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 307af2d9-097e-3f7d-8df2-64574f3dd613 | -1.10993 | -53.57853 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 930cc8e7-f5f1-3ace-87c3-d1c410ff2d94 | -3.28697 | -53.66294 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 686b62aa-aebe-351a-841c-33af9308eba5 | -2.76241 | -54.08527 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7609f713-28a0-32be-a4c9-1df964efc3ba | -1.23907 | -51.61497 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80aed5fc-079f-382f-8931-c49ea446ccd1 | -1.19902 | -53.86735 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50555e6e-29bc-3d74-b943-36a5de32f44d | -2.63156 | -46.19814 | 2024-11-30 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b02685d5-c96a-36f3-829c-16c5c0daedc1 | -2.38456 | -53.71369 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08c0e8ed-8925-34cd-80ce-e7338fd87935 | -1.74752 | -52.65587 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecd51c8a-8fd1-3875-95d7-2f677b4f1986 | -2.60773 | -54.07495 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed50a19-6b1e-30fe-a1b4-78ecd1ecf67c | -3.04123 | -54.04915 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6033b4a-8857-3ef7-90e7-ffc2b7619536 | -1.61595 | -53.6275 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8756d509-082f-3735-b240-369020ea6fd4 | -1.3315 | -52.38966 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 530a6cd5-1435-3d28-91c3-98e0a6dfa84b | -3.52894 | -53.78756 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d612179-3805-3f04-b84b-dd4e06f7f3e3 | -2.26997 | -46.42947 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eaec226-1d9a-32f3-8c1c-a619f58c8691 | 0.98323 | -50.12409 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e1406c3d-f84b-3d3b-9d48-bb1363c7a24b | -4.25041 | -47.57726 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92fc7810-0950-37b2-9e18-c61561561c5e | -2.97808 | -53.29068 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea215e16-5854-3af6-b224-1182af39e0af | -3.31699 | -50.02524 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f07fc8ba-f9b8-38c3-b504-450dc6f5b5a0 | -0.24423 | -53.76133 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d0995ce-e208-3b16-a3ba-9a1d9648f9fd | 0.06855 | -51.49208 | 2024-11-30 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68916e0a-3171-384c-a5bd-08cc33cb4200 | -1.58002 | -52.27461 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb1691e7-0741-3072-bda9-bd068ea07f50 | -3.21322 | -53.4194 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87be3604-8b58-3b33-a595-c95656e21b3d | -1.23458 | -51.80812 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdad7c25-64bf-3d4a-8ba1-4c0cce177ee7 | -2.60306 | -53.99556 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 721ad7df-57f8-3584-b85c-f4712a34a1b7 | -1.35866 | -55.6447 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e268a9a-742f-3d46-9b8c-605bf7043213 | -2.80202 | -54.04112 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 944bf3b4-7b3c-3dac-9579-7953372a6c56 | -3.85737 | -50.14929 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caef8e14-4a44-3f59-ae99-09909bf7a800 | 0.94469 | -50.74945 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ca008d1-c841-38dc-ac66-284a2755be03 | -2.23441 | -53.62844 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74348211-6740-3e84-81cd-bb2f2d1f94a0 | -3.25452 | -53.28779 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a43909a8-ae1a-3aac-bb3c-aca1013cd367 | -3.13215 | -53.26492 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a7de9eb-f85f-30dc-9ff7-1bdd12d1a0e8 | -1.57473 | -52.28559 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1213a6a5-10cd-3d80-b127-160039ca3190 | -2.95834 | -52.92099 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fcd9207-ba8e-342c-b29a-015f236279da | -3.14314 | -53.82697 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d6e9850-aafb-3a59-9ebc-72b9cb033be9 | -3.80582 | -46.53666 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac89cac6-ffb7-3a2e-9968-3b260d8ef4ee | -2.2014 | -52.24233 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2ca14e3-3364-3d17-b8b8-02acc5b67507 | -3.14015 | -45.98373 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ac319d8-0352-371b-9a64-b9cf4f5989f9 | -3.69785 | -45.67831 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c38b56ed-6f4d-3bb0-bae1-d69b8dd7d656 | -2.14824 | -50.62231 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d710c7-0069-3649-9548-2c6dc0d5db4c | -1.69641 | -52.42884 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a25aa511-10c6-3dd9-b3cc-d77804280285 | -1.24521 | -51.7401 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 271c8f3c-3521-3bae-89c1-1c80f70c486a | -1.45945 | -54.49207 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1eb1523-f754-3e65-be2a-0f37e897a80d | -1.29988 | -55.74415 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1c8987b-f69e-3f61-a917-561b117d8801 | -3.15213 | -53.83555 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README89.md)
