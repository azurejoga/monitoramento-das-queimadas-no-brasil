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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28557622-1b0c-3b58-8ed0-381044a31047 | -1.20089 | -51.77962 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff468f48-930e-3108-ae73-ea192ec60754 | -2.60001 | -51.79257 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfc0e01b-0d98-3214-9ad2-eb82a1db7fec | -2.91394 | -53.06848 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a6256dd0-4235-36e5-97a8-e6d455c85677 | -3.13967 | -52.98049 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e97a4f04-0e66-353e-82d5-2f9cab1f41a6 | -2.45222 | -53.70024 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 257e4ea5-f55b-3ba8-bd8c-500aeff4a9b7 | -2.65886 | -46.61155 | 2024-11-20 05:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e22c3f69-074f-33d4-b0e3-38a1b186414d | -1.72696 | -52.8013 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b3e358d-5b1b-3b37-bf6f-36818a2dca7c | -2.74042 | -51.72667 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbedcddb-8bf2-386f-997d-387711756386 | -3.10483 | -53.10027 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35decde2-0b91-3093-a367-c5317c4f20fd | -1.66487 | -52.66389 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f92e670-23a4-3f49-ad3c-02296a3e868b | -0.91371 | -51.78374 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a83180ce-80b0-3b4c-917a-eddc41c2b25a | -1.25816 | -51.7663 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45e2c51a-5781-3ce4-8998-50ec4186348c | -1.19779 | -53.6804 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 84132b1e-9b11-3e04-bdd8-f1295b79dea3 | -2.05511 | -53.43661 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6caf4a6-cdd6-3100-886f-a4a717cf3bf8 | -2.28108 | -53.63519 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2031720d-41aa-3d05-95b3-2eea9764ebd8 | -2.46737 | -54.75084 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20bf7a96-69f2-3baf-9505-d67652e1530f | -1.60416 | -52.41025 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90689669-f542-348c-b96e-5dc339e6281e | 0.12168 | -51.05404 | 2024-11-20 05:14:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 022b0668-caac-32e4-ad7d-0d1a3da34cd8 | -2.8505 | -54.00787 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c1da2c2-f51e-3e28-97f0-6e99c379fe1f | -1.51553 | -52.08931 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8bdb9f2-77b5-361e-b7bf-b6867e0d7774 | -1.11248 | -52.39088 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35d7ef0c-ce4c-35e0-a4d0-6acb8ccedc68 | -2.72058 | -49.34319 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d5bfdc1-e2cb-3824-8f26-3c843cd0abc5 | -3.13937 | -49.12324 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1a4ebea-69bf-3d9e-adaf-44e4a84e6b85 | -3.77208 | -52.66279 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2598aea8-0b98-32e1-a22f-e0776b3895fc | -2.13842 | -48.56911 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c3f41aad-2358-38c9-95e7-9765faf7f832 | -3.61199 | -54.75043 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f84ae8e-4c1b-360a-9908-02170b530f2d | -3.13794 | -49.13304 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d089ebc9-5ec3-3d3a-a82a-39e94e655e46 | -4.10668 | -51.05349 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9900d336-beea-3b66-8a4b-23428cfd33cc | -1.32538 | -52.40355 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e24f1563-feb1-3c8f-8ac2-e3a6e8ff68e2 | -2.89276 | -52.44299 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ed31de1-a0a6-37aa-9311-9315b0dffec9 | -2.72675 | -49.33762 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09e9664f-cdb1-3344-b6de-04ebd0af0d6c | -1.51689 | -55.48472 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c65a4ed-10ca-37f5-957d-ad3da14d9a94 | -0.28033 | -51.44373 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9935771-3251-3441-9413-868e1fe7f116 | -0.97647 | -51.71903 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63ec108d-ac77-3ba6-a172-f361ef1419df | -1.75261 | -52.37118 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1528b8c6-3c2d-3fd5-abe4-3ca698ab193a | -3.20015 | -54.32618 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ff2b9a43-122a-3090-9d21-a32e63368e04 | -1.52653 | -51.51495 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c8c267-fac4-3fd2-b976-2ca563d86977 | -2.53813 | -54.55923 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 859663d4-a3f6-3803-8950-91fb2055ef84 | -2.72628 | -49.34077 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d746bdbf-ec97-378d-972c-eb12edf7a262 | -3.31373 | -54.74627 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7797af18-a7a0-36fc-94d4-488b1079ee2f | -1.32701 | -52.40428 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dd6fd052-3ec3-32d8-8b88-695c588b0be1 | -1.25532 | -53.36337 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f578c812-76cb-3405-a8d2-e254a22ca015 | -2.56555 | -54.07475 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3b4c1ce-7019-35aa-b141-8fa6f3f89800 | -1.2153 | -51.7443 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 725b3803-4f73-3ff9-84d2-99b1413b98ab | -3.22001 | -53.02574 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c423df8-0928-35f2-84d0-64a6b92ebf9f | -1.3939 | -55.17786 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1d5a667-9c7f-3833-8460-a25d16ae6541 | -4.44384 | -46.582 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 3c5f7d33-7026-3865-b115-d0566e0ad139 | -2.92316 | -53.06235 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f58ede5b-436e-3843-8ead-dc5274778584 | -0.97217 | -51.71836 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 666e0609-b3c4-39f3-b57a-be4555943baf | -1.22307 | -51.7942 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f965a67-9830-3611-b9c8-a20b837fb38e | -2.71001 | -53.17337 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6bdb666-ae77-3ed9-b3fc-f98165c244a7 | -3.06043 | -54.40298 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81eec62f-0e97-38dd-b9f4-2a079cd54415 | -1.31346 | -52.40978 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af76a93a-1088-3f5f-a549-6e0237ff4611 | -2.68394 | -51.80415 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4a8568a-0695-3fe6-839c-8e8585408cce | -1.14035 | -51.68674 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebe4875c-07bf-3208-827f-79e87204b43b | -1.47833 | -51.15912 | 2024-11-20 05:14:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70122c6d-a867-35e7-b310-5f535b79b14e | -3.58019 | -53.71863 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1de5eec1-7bda-39cc-8cb6-a07936b674f3 | -1.24709 | -52.03395 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d28f52ff-09b0-3fda-87b6-4fa85b8765e1 | -1.5391 | -52.04866 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d792578-c474-3715-9bee-928b736485b8 | -1.05632 | -53.09606 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d486ab36-d269-3a3e-8323-0e0b0de099d6 | -2.33941 | -54.77938 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c59ca94d-c6a0-3cd6-bbd0-9cd69a1a7711 | -4.38857 | -47.76034 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f2c91e3-05f3-3f7f-a088-f6a677b8f390 | -2.74836 | -51.82411 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 73e1787e-2c3c-3399-bd8f-7c9ced3041ac | -3.31314 | -54.1726 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9361574-5399-3e63-a027-5bcd123fd06a | -1.63019 | -52.40655 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb75dade-12e1-329e-a199-cd3c9220d4f5 | -1.93158 | -54.06507 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b242a1a-34d8-33ff-bde0-703e077eb7e1 | -1.48634 | -51.13726 | 2024-11-20 05:14:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9d2ea4b-ab89-3043-8e3d-58d197f2c88f | -1.14852 | -53.51885 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25a501b6-5bf0-3131-8b30-0d776c8045ea | -1.45874 | -52.67761 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 83dddd2c-10dd-39ac-b186-9e8b90f94809 | -2.93017 | -53.0706 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b3dae90-bc2d-3b6f-9a42-33fa6fb3e8fc | -3.42929 | -53.29014 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644ad4f9-3e28-3ea2-825b-1800f6b94d69 | -1.60773 | -52.41462 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49950a56-f985-3a9f-9e8d-78a7b87bcdb2 | -1.20589 | -51.76246 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75e0f0f5-66bd-3531-9e8f-17c5b26474a6 | -3.33941 | -53.30481 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 543ac45b-5958-3119-8942-5cf8ac216097 | -3.06943 | -49.20174 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f51a3343-9f52-3d3d-bac5-1cab13dcb185 | -2.78639 | -54.02437 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f13568a-134c-3b6d-b2eb-35ba45a57a37 | -0.95371 | -51.72383 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c210da9-8682-3afe-acb5-a1ea6b4bdb6f | -3.03952 | -49.47112 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7416a542-cbf4-386f-9cc0-588c9ac46f52 | -2.72437 | -49.35337 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a95e5353-bfc3-3f4d-8fde-6b21a8a5ef30 | -2.82908 | -51.82672 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af69c47-d376-3e3f-8b63-7a81a3d9d3c6 | -2.38055 | -53.6679 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b81c6efa-f992-3897-9cf8-001a29057511 | -2.6315 | -54.27304 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4c50ec4-b158-3a71-9482-1e798046355b | -3.76719 | -52.13946 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a72ce527-bc16-325f-8eb3-c07559b11cc8 | -1.6217 | -52.59047 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba7baad7-a882-3734-8d4d-33be2441beca | -1.42101 | -46.80446 | 2024-11-20 05:14:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b382d0c-af73-30ee-8520-24f1fdca8044 | -0.89116 | -52.68545 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e021f00-181e-3c9e-86b4-651fa15047b8 | -1.63304 | -52.68115 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca6de578-f2a4-3cc2-92b3-41b7e219b237 | -3.31006 | -54.74572 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5976eed-83b4-334e-83d8-da84461c51f4 | -3.1043 | -53.10378 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac796b59-040b-3ac1-a4de-a978e778d97f | -2.57714 | -54.0253 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8a86cdc-11e3-3e0e-8693-9ed1dfd3e66b | -1.92566 | -49.52276 | 2024-11-20 05:14:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa81eab3-73fe-38b0-aa2c-136006469457 | -1.73325 | -53.02716 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c4cbc7c-65ec-314e-b83e-b201fde27fe9 | -2.74869 | -54.11768 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f28c0f8-be78-34e7-b923-50e022dbcd43 | -2.87008 | -51.79326 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e2b5209-2394-3d16-8dcf-c60ef33ba1e7 | -1.34575 | -55.43998 | 2024-11-20 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90dacb91-8ecc-32ca-96cf-7b42603e8536 | -1.41233 | -52.22422 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3082924-1b68-357b-b14c-5237b33d4c54 | -2.76168 | -54.05853 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc0afbac-fbe0-3319-855c-69f0b16f9d4c | -1.19723 | -51.7749 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 830b8866-b993-3263-98af-0c0751bc8b31 | -2.21319 | -46.48775 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d003322e-45d1-3db3-84b0-31506e22de1b | -2.7258 | -49.34394 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README69.md)
