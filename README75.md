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
| e81d381f-bc47-3bf9-8ae3-f5846a1ac0cf | -2.98917 | -52.91073 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 59ad6abd-04cd-323f-b161-e8062a12f282 | -2.98859 | -52.91447 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ee0e82d-87e0-363b-8eaa-a0a2ee05d59d | -2.98802 | -52.9182 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 530e8b6c-2beb-35a9-9c58-702456929028 | -2.98515 | -52.91396 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0922731-6a58-34de-bcdd-36a9453873b2 | -2.97484 | -52.9124 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87890217-c69a-3c86-82ff-53e1a42b5a5e | -2.9714 | -52.91188 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d232a5e2-189f-332c-b114-b0327a290366 | -2.96915 | -53.10923 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea015e8a-0a77-3908-bca8-bc11d0e8f70a | -2.94178 | -52.92335 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 943d2789-0ff4-3d3a-a38a-997395a179b3 | -2.94164 | -52.92268 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31bcf21-1082-332f-b251-707dfa175679 | -2.93876 | -52.55384 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ecee893-0cea-3dcf-8459-c37e60f810d1 | -3.68374 | -52.39681 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b72b578-04e9-3721-a643-8e4e00077b62 | -3.68314 | -52.40081 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba61c27a-29ea-3188-9bb7-4b9f8bea078e | -3.59376 | -52.24897 | 2024-11-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d5818c1-3c07-3055-9e22-f70e453b0a89 | -2.67756 | -53.02014 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6371cfc-648e-339f-ab32-3008dfa6c4e6 | -2.67698 | -53.02385 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfc65a21-28da-3b31-8cf2-60e32e51c33f | -2.67414 | -53.01967 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43f30ab9-f4a3-3813-8bc4-ffa3067ae587 | -2.67356 | -53.02339 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e5bb6bc-44d3-392a-be8e-298bf7298bf5 | -2.62443 | -52.45277 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e415eff2-a177-3645-b2c2-8b31a36cabf1 | -2.62094 | -52.45224 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8524295-cc41-3f2b-bb89-797c21aa1836 | -2.61805 | -52.44782 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85eaa11a-d8ba-32d2-aa0c-942b143cb8e6 | -2.61746 | -52.45169 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a7193c4-0cdd-3cf7-a46d-b93b27b335b8 | -2.58265 | -52.25148 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 549d6df0-482e-3a71-946f-85369628dcd8 | -2.58205 | -52.25537 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 181aefa4-8152-32ad-9beb-b3026fd46053 | -2.57792 | -52.25879 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fbd9d4d-c707-326c-9c26-b78fcd9897b3 | -2.35589 | -52.69359 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54c8f0c8-6e15-3d7c-af7d-7515eddd8bb8 | -2.31871 | -52.91321 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4af3f1ff-c57b-3fb2-b478-7aa20552e23e | -2.31586 | -52.90897 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334c656d-186c-309d-b693-9c48b004fd51 | -2.31529 | -52.91269 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea546379-bce4-37e5-8b34-f7307bb56a30 | -2.29162 | -52.88315 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4e101fc-db10-3ffd-90fa-6240f2fad10a | -2.24946 | -52.83875 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e574e20-af8e-32af-a8f8-94fe89a6ea32 | -2.24889 | -52.84246 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb080800-5404-33d8-bff3-760ce683e566 | -2.24547 | -52.84192 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 859371c9-ddb5-3175-a238-c02dd7c63314 | -2.2449 | -52.84562 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee91064c-3795-34c3-9aca-5ae508c6be0e | -2.23922 | -52.7685 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bd10e57-c8bb-3690-9618-2498ac16beab | -2.23578 | -52.76799 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74b8894e-00a4-3080-8afb-b7513836b2b3 | -2.77118 | -52.06163 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07dbc6c9-06b1-34c4-823d-5ee3f3899511 | -2.76762 | -52.06108 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7fb6bf7-ca45-31d7-b096-5c900f37d4eb | -3.09022 | -53.23314 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e089d8d-26c9-34ab-b582-9f3956a8e175 | -3.08965 | -53.23681 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58fde63d-0575-3db9-bff8-12053fbd2976 | -3.08625 | -53.23627 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edb3f44d-b5f2-3497-920f-2a92865ad314 | -3.08285 | -53.23575 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fffe047-d353-37fa-a335-5433b7d97d7f | -3.08171 | -53.24311 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e625b25f-8992-3bd2-94bb-bb28c234c2cb | -3.07152 | -53.24151 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2def1e45-20d5-398e-82d5-5564186f9487 | -3.06642 | -53.25202 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cded14b-41b4-3459-9966-0d494a89376d | -3.06352 | -53.15782 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b31ab439-373c-3775-a80d-7a11555ef201 | -3.06302 | -53.2515 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85bb8098-1c61-30b7-a193-be59ba6f9e96 | -3.06296 | -53.1615 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdeb2167-8559-3a3c-8c04-49e14d07e400 | -3.06012 | -53.1573 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c41d22c-676c-3769-8fde-fc499131f6ca | -3.05962 | -53.25096 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ea4d225-d727-3330-918d-a608d85465a3 | -3.05955 | -53.16097 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8256fd8c-e2b3-3d08-b61a-3a48eb7107a9 | -3.05906 | -53.25463 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01e1090e-53c5-32cb-8a1e-dace5550003c | -3.05899 | -53.16464 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 487d3a16-2b3a-368d-a60e-c3b32df46587 | -3.05614 | -53.16045 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fce69b6-bd30-348b-8ebe-4d19d1789170 | -3.05558 | -53.16412 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9cf41b71-cadb-3de8-84dc-e40f565208ce | -3.05217 | -53.1636 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 626fd40d-c732-368d-a48c-48cfe80078c0 | -3.05161 | -53.16726 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d94c5431-95ae-3af1-87cd-722038ec3470 | -3.0482 | -53.16674 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6039aeb8-4345-352f-92e1-1af1f99466b8 | -2.97763 | -53.34635 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30ed28eb-38f8-3197-b70e-0594bbd2f00b | -2.97707 | -53.34997 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db964529-df16-37c2-b152-69b7fda61173 | -2.97597 | -53.2678 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e459a2ae-c6e2-3f16-bef7-8db1b8b49507 | -2.97541 | -53.27143 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e068c7f1-f8df-39a8-b43b-feb3f2191e6c | -2.97425 | -53.34583 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbfadf7d-51b8-3f76-8d5c-963ef5960c68 | -2.97368 | -53.34945 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 123c61f2-735d-36f6-83a6-0fff4182eb63 | -2.97201 | -53.27092 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1bca7073-6443-3db4-846a-ee97fab3cf6d | -2.96975 | -53.28546 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b046cad9-9f2f-37cb-9f1b-a3e384fe0733 | -2.96636 | -53.28494 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfd1661a-4c62-3d7e-87ea-11febf374f5c | -2.9658 | -53.28859 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2cb5c07-b7e5-3791-ad99-d2c449f9ab83 | -2.96297 | -53.28442 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f67775da-00dd-3c16-af35-4abb80a1b9b6 | -2.9624 | -53.28807 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddc8c434-c4fc-3009-83b8-bec7719cd12b | -2.95901 | -53.28754 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad7b1743-d3fd-346f-a698-f7e2f23ff827 | -2.95562 | -53.28701 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ea6ecc6-6e1c-3c03-abd8-f07e11a14ed6 | -2.95506 | -53.29066 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18092611-d642-3bf3-af6a-25dd08c5de07 | -2.95223 | -53.28649 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2810ce04-bbc6-3afc-84e0-6577487e329b | -2.95167 | -53.29013 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc9cea04-a711-3663-8b53-285c9861c0e3 | -2.95111 | -53.29378 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab46e044-4e90-3b72-9b21-bfa44366e5db | -2.94828 | -53.2896 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51b988a4-56f7-306e-91e0-4b0e80346ca9 | -2.87137 | -53.35243 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ec786b7-eac9-3f7a-8f7e-ac76aadfeeb0 | -2.86853 | -53.32615 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a3c0005a-e927-3ab9-b439-da72211b3caf | -2.86797 | -53.32976 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dbfc572-d5e8-30cf-8204-fa2434d41131 | -2.86514 | -53.32566 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f03539f-300d-36cc-96cc-f54d6e13117b | -2.86288 | -53.31793 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f60dfee2-3bb4-336c-bf22-d9f37fc42734 | -2.86006 | -53.33606 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4844578-88f5-33bd-88da-5b1def8921de | -2.85838 | -53.34689 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a2b734f4-e142-3820-9860-9ae1b6fe0ace | -2.85783 | -53.35044 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b926a6a4-6329-3312-8b20-60938eb845b4 | -2.85555 | -53.34279 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3987dc59-ce33-3d85-a103-dcfc79913aae | -2.85499 | -53.34639 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd95085b-d7a9-3484-b7fc-d42d34789f6b | -2.85444 | -53.34995 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 936ca713-c441-3367-b10e-a2bf2bdaa614 | -2.85217 | -53.34226 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1f056777-90db-3c5f-8900-68e3d351f734 | -2.85161 | -53.34587 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef3ade70-0e2d-3bda-a322-f203c829e0d5 | -2.85106 | -53.34943 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fdeda23-36e5-3cc2-9bfa-d8d5c2a17af3 | -2.84823 | -53.34534 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be3d5feb-5457-30ba-a367-d77452356ab0 | -2.84768 | -53.34891 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5ef7aed-b2d8-3de9-b081-df54f84dba8a | -2.84485 | -53.34481 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 232d6338-d89f-39d7-b812-9d623a9aeff2 | -2.84147 | -53.3443 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04d934fc-d1e8-3b47-8bc3-ccde94614925 | -2.84091 | -53.34789 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e7375043-3e71-3338-9d62-9e17f8a989a4 | -2.83864 | -53.34018 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5353be77-61c3-3a5f-a6f7-125e41e093e0 | -2.83808 | -53.34379 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ea503870-dd33-3086-9c16-61fd67485692 | -2.36815 | -52.02111 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15f5c0ee-0b2c-3b9f-b4d7-a9812b27724d | -2.36521 | -52.01657 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4af32181-0a28-37dc-86f3-586f9d87468b | -2.3646 | -52.02057 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README76.md)
