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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f6f9423-853a-31b8-bd66-30f391dbb42a | -3.26848 | -49.89132 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f14dbd2-ec01-392f-bb51-d9d015107ff9 | -3.29333 | -53.68625 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08e9c9b8-9828-3a15-9911-60867dc66573 | -2.75625 | -54.11996 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2c3771f-66ed-3243-9f92-8967fe6d333a | -3.94064 | -46.72118 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 195a9e3f-a360-3465-8e12-05eb206b64f2 | 0.27375 | -49.8035 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a86abbb1-9b6f-3e6a-a7fb-d40d95ec60e8 | 0.94675 | -50.74776 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a092fc4-88e8-3aa9-aabc-7f2b655478b7 | -1.91126 | -52.88515 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41c57c88-02be-3d4d-bbd5-5833c05e6719 | -2.56546 | -54.33775 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1967b3e8-2b53-38d1-97e8-a54e5b5b1a0d | -2.58065 | -54.24068 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c8aec75-168b-3374-90c8-121ee97919c4 | -2.88805 | -53.9957 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9296b1fd-2b00-3dff-a509-5b9ac30957dd | -2.85856 | -45.53761 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0e1548b-7469-3bcc-af0c-53b095586722 | -3.2877 | -53.78737 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a60152a9-7043-36e4-8bf8-8e92f9f24a73 | -2.96568 | -45.23256 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae2bd7df-be53-347e-ba34-e661955f8385 | -3.12429 | -53.26522 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b305eb92-5621-3d39-8b71-dfcdc03f5b09 | -1.59561 | -52.2914 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 958bda22-01cf-3591-b92f-9d03e814fd85 | -1.39393 | -53.62738 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c064471-6424-3937-9161-debf1925ad2b | -1.27557 | -52.16282 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c852d6b-e350-326e-a460-47a2d6d1813f | -3.70721 | -47.13382 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8bcd1731-eb29-35fe-a6dd-622fc9de36e8 | -2.73065 | -54.10817 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56e86599-3b48-35a8-ab4f-51736af291fb | -0.05242 | -50.82158 | 2024-11-29 04:57:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1757ff97-8a23-3c1c-a4c7-cd1b5c86fc87 | -0.5727 | -51.6956 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a173ee3-820c-3976-b51a-d3399b1d3bf7 | -2.57319 | -54.33183 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e0a5655-7b51-3b82-9142-26490e2bd171 | -2.53601 | -54.00387 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c1757f-f31e-3019-a57c-8f344a9a5aa5 | -3.67248 | -54.28454 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c277d67-4935-30d4-a718-56691976a48c | -2.75679 | -54.11652 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 52d5067e-b4a8-33e5-a3c6-b58ec50cfdf4 | -2.88178 | -53.94544 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af7c27c7-7b40-3e51-9e5f-3367abc90580 | -5.43355 | -48.13733 | 2024-11-29 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a60b1e8-afc5-3eca-a232-6d018d4f3bd3 | -1.27359 | -53.0251 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8060e75f-2e53-3d17-a11d-8d6d7a7f8717 | -2.85372 | -53.95168 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ab04fc6-be3a-311e-97b4-dff16ea72882 | -2.62524 | -54.30437 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2603cb69-c4ad-375a-8914-3f42a8944a6f | -2.53394 | -54.03886 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adf3cd36-d7f0-3ac5-b54a-4d2847038481 | -2.01721 | -51.43313 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 071c874e-14d0-31db-b5d9-3ed5d3191fc6 | -3.52605 | -50.48211 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d991882-66ca-3e9c-a9ad-667c5e1fa35a | -2.84852 | -54.02833 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 807224c8-b092-379e-ba42-76bca93a15f3 | -3.38948 | -54.29008 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a8eee9d-718b-3a3d-84ac-2d46694f512e | -1.59113 | -52.27633 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e0a193e-dcaa-3d99-b237-806a04875060 | -4.72627 | -43.25344 | 2024-11-29 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48b68e7c-c862-3b68-88b5-bc43ef76f87d | -3.66401 | -51.04195 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f25f9b4-071d-3586-a036-6168d23cf56c | -3.2431 | -53.63614 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1f95819-608c-3059-a7ce-97ebe9d575ac | -1.08979 | -53.37587 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbbb505a-8f36-3396-81f8-2a1d7907a018 | -2.66222 | -48.78621 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 78eb87aa-4831-3046-bc9d-5614d602b917 | -2.68091 | -54.25265 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c9e822c-ddee-30b9-8a1b-3bd68b53dd1d | -2.72008 | -48.67531 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb1695b0-1b64-3a21-bb26-a8bfefc52138 | -5.04348 | -43.61729 | 2024-11-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a39045a2-7140-3012-8512-63df441d372e | -0.95061 | -51.65424 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ba36362-6203-3bdd-b754-c76cd45ddde3 | -2.28349 | -50.57306 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d02b7106-547e-3197-ac39-e089ffbfcfb2 | -4.25165 | -48.06433 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e70c8fa-3320-36c3-bc41-16c555d10f7a | -0.82065 | -51.6119 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8845f009-313c-3950-a2ff-cc6c4429809f | -2.23098 | -53.69209 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 78fbfbf3-1823-377a-a409-0714a6d3c83b | -1.92343 | -52.89409 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a815d860-73b7-39ca-8bf2-2a1e0468b59b | -2.94397 | -51.58667 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 356cb0a3-1214-3f1e-a563-e1d4c85fcc5f | -1.23781 | -52.536 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b62c78-2a3f-39b8-9e31-41c4ee3a4637 | -3.02606 | -52.3816 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c51a2097-3816-3640-8e57-a14e53895df3 | -2.25438 | -53.62891 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 337c7df8-4e30-37ca-8da9-0ed6fe33989c | -3.09118 | -54.02013 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf5953f8-679b-3d3d-9481-e126eab12e1c | -1.66662 | -52.20486 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81c5889d-e00e-34a5-be97-8a9ef33ee188 | -3.21503 | -53.38197 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae891cf5-4c19-3f12-af80-45d6f797a75a | -1.06945 | -53.37624 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6c97864-91b7-32aa-9d8b-8b2fc296b5ea | -1.94786 | -54.71894 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3cd5788-3dea-3612-8776-08858f8987d6 | -3.79046 | -52.1034 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c5cffea-b7cb-3789-b760-05f6c0566b6d | -1.43369 | -55.24297 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 65126c53-8388-3110-bc55-651f7dc6ec09 | -3.71502 | -51.79694 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d766632d-e762-330f-b33e-f58f3e615ac8 | -2.57811 | -49.99698 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6bb0b0c5-d92b-37be-b705-380fb98ddcaa | -1.26435 | -51.75741 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e02cd2e6-1d13-3478-835b-47b67a67a3ff | -3.18905 | -46.60212 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e86f6c3c-4af1-3a27-8149-e411413502c2 | -3.0585 | -51.30183 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aadabd40-c8ff-374d-8fb7-c130a64fcd02 | -1.16584 | -53.67227 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8f4c1b3-81c8-37ae-8c30-feceecec4556 | -2.52378 | -48.51613 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1793b6a-c212-320b-b846-0548b258cef4 | -3.09449 | -54.02064 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a895cede-c7b4-3896-a5c3-dd09a5b8e814 | -0.47652 | -48.63363 | 2024-11-29 04:57:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2edbfc4e-a55b-3b80-aeeb-049b940c5ebb | -2.96458 | -53.72258 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eac9907a-4883-34e9-aebf-fb19a4d42050 | -2.73796 | -54.14815 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6736416-7195-3be2-a6b0-8f2b626feedd | -2.78779 | -52.86932 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e5daaea-cf18-3f39-a127-021de6df916e | -4.11242 | -54.23404 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e483bd28-3551-3e02-842a-3e8f2c50e3a4 | -2.62579 | -54.3009 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a22a75c-9470-3763-8d67-8371456dc7a1 | -3.37632 | -50.77054 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dea9d78d-d143-34c6-ae82-426efe866367 | -0.01633 | -51.09846 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da19e262-2492-33fe-821d-045c35b17a99 | -1.94951 | -53.3387 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e44967d-4e55-3c23-816d-06899fd3036a | -3.272 | -53.71461 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba470aaf-1e7e-3b50-84b8-fc186647dfda | -4.10779 | -48.2495 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eecdc385-4c1c-3271-937b-4fb138cbec46 | -1.21719 | -54.19438 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d35c670a-a1c9-3ec3-976d-7a9687d5b869 | -1.25813 | -54.54263 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 182136a6-ee7e-34bc-a972-91cc92087f70 | -1.20249 | -51.75524 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d39523c1-eeca-33cc-9869-d51efe731dfe | -1.67919 | -52.49747 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0287930e-0b16-3005-b505-ebf4aff6c078 | -2.27281 | -52.83511 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 564d53cf-a318-3026-9539-f1f52b75161c | -4.07732 | -54.1123 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49182921-c214-3868-977c-87e27b4a3a05 | 1.84788 | -55.82466 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 217cb69a-0f7c-3b09-88ef-dab3f221ed64 | -3.64991 | -51.39588 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11c062bf-b162-3b2e-9ebe-0056da86cba6 | 1.20964 | -55.96198 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a4b4a43-f08a-3411-8636-8d63c486033e | -2.66826 | -46.60229 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f78f95d3-5302-3449-a9dd-180e11578bb3 | -3.78636 | -50.12911 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0923a3a8-8754-3138-844c-aaec8f40467e | -4.10155 | -53.97877 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffb47da6-4a19-3fbf-be74-fd3b0bbcc8cb | -3.24365 | -54.22084 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20e05fcd-cd42-34fd-9425-ab0eec3aef36 | -3.28331 | -50.15849 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b80c94a7-0d73-3187-8dca-8b2fb0068257 | -2.76394 | -54.02507 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97de4809-9bc5-36f5-a6bb-d5fd1adec3cc | -2.20018 | -48.34385 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69d1163c-0476-3b2e-8094-f19fd94a0889 | -2.84521 | -54.02782 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c559b69-d5f0-30d5-b60b-60591837bcff | -1.05688 | -53.65185 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f02c8bb-bf52-3cc3-ad33-a82d846f2205 | -3.24327 | -51.55865 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52f5b8a1-b887-37cd-9bb7-a66fbc14ec2e | -1.87866 | -48.54626 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
