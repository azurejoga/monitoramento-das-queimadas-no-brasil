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
| f1ee89b8-f06c-3fd7-b743-6a244497a749 | -1.63164 | -53.27608 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b1d002-b2f5-3a3c-b027-4b6351e2533d | -2.11082 | -46.41889 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd569a1a-b4a1-38e6-b0c5-f5324bb1199c | -1.86652 | -50.9678 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e15a22e-370e-3dfb-a095-2734f86a6451 | -2.60341 | -54.04633 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e296ba5-16ef-34da-a966-da02521fe907 | -2.13136 | -50.81687 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c789a25-52b1-30a6-b36e-af1eaeb01c92 | -2.59769 | -54.03759 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6051c833-12c9-3cbc-a2a1-5fe06af938ea | -1.13492 | -54.10233 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 377bf3fd-7837-38c6-930b-541b3076aa13 | -2.39729 | -49.03941 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8612f80a-f53c-3ccf-9131-02ec676e1bab | -3.84846 | -46.64556 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6e50666-00de-3c3e-b6e2-b0b050b33209 | -2.58312 | -47.47817 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cad04d3-01f1-3406-822c-b4a9a7c9ec19 | -2.20067 | -48.81242 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c742bb-79e0-3d03-afef-d3939f176a37 | -2.14506 | -53.71069 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43225ace-f1c6-3307-ad6e-618ef5092e46 | -2.22307 | -46.8243 | 2024-11-16 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d795b53f-0b07-3dc5-b578-e2c253c7443f | 0.42891 | -50.9154 | 2024-11-16 04:48:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2344976e-0da6-3fc2-a490-cde0bc07c17b | -2.35302 | -49.11688 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11443d78-d53d-3c4f-ba1b-c6e8d78d5b22 | -2.4361 | -48.59598 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4b46561-25ca-3392-b190-fa24789ecf1d | -2.14195 | -54.41968 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d879e708-4e50-38e5-8980-d307949de4cd | -3.41185 | -42.38686 | 2024-11-16 04:48:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb27fc36-7d4e-3cd2-9761-f0faa4e31c1f | -3.9248 | -45.85534 | 2024-11-16 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75172e68-0e68-33a5-9c36-a76bcdb2183a | -2.65716 | -46.16862 | 2024-11-16 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0f2807e-5b0c-3362-9e79-4d1e243966da | -2.16287 | -46.40465 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c422943-3dc2-312c-9a5b-70c491deabed | -3.50021 | -47.20714 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a3e6f44-87d2-3238-9987-38f380c88954 | -2.1633 | -48.91341 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fd1ecf0-5836-3dba-bb2a-238b36707237 | -3.28101 | -45.50298 | 2024-11-16 04:48:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c12db48f-9b61-3162-a959-d478280a852a | -2.23981 | -47.2124 | 2024-11-16 04:48:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc4c5fac-11c6-3e40-b3ad-196d7e89ecba | -2.97305 | -47.98929 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3258112-9a7f-328f-b21e-b00a3f1e639d | -2.72183 | -47.90588 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebeb66ef-7e68-39e0-a615-0b2ada0a3187 | -2.90187 | -48.31345 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8abbe76c-bea4-37aa-bb90-99dd398fbfb5 | -2.02454 | -53.94372 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09201ecf-8b49-3dcc-aa40-04798e585cbc | -2.56064 | -46.90129 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9561241a-9136-38ec-b00e-37394f9e98ec | -3.57486 | -45.67333 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e78dbccb-b643-3bdc-9020-195d62776e5b | -1.86678 | -54.28204 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61e0a84e-129b-3eb3-bb62-07d1ef80a9b0 | 0.11918 | -49.8513 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81ed20bd-d3ea-3ce3-9a24-cd55500d6a4a | 0.01201 | -49.86053 | 2024-11-16 04:48:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e894776-f1b8-3d5e-a562-96466b986454 | -1.86703 | -54.28107 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ddaab36-3ebe-3aa2-b942-d3700f090c32 | -2.5572 | -46.89723 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 348ee864-1174-3ee2-9602-d44f31aa47de | -2.59994 | -54.04582 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 984c11a2-98a5-33f8-81e4-d6e5542dcf4c | -2.36108 | -48.56925 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 334a7eb4-da24-31d8-a324-3eb3fb9904ad | -3.95575 | -46.70653 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 908f8d0e-be98-3d71-bfa6-1f2fc7eb70ee | -3.7903 | -43.91527 | 2024-11-16 04:48:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1a1196c-68a3-365f-a8ef-32b6a0782557 | -2.64782 | -48.47784 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e2dd9592-afe0-36a3-bc1b-2feb9e04002e | -3.7392 | -45.65668 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 96ee377a-d297-374f-9b78-edb417b37c32 | -2.39584 | -49.09543 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af98193a-be3e-30ef-a52f-1af2efe09250 | -1.0882 | -54.2136 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4313f0e-f88c-3c14-9633-1d809dc56bfd | -2.15134 | -53.7155 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 804482e7-a98e-3d4f-85b3-053bc042b8df | -3.50181 | -47.22297 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f7a97dc-6fa2-3c76-ab1f-c588751ca920 | -1.62825 | -53.27549 | 2024-11-16 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0991592-b19b-3a8d-b63c-d6e0267700cd | -2.02659 | -53.94365 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe8ab743-2fb9-3285-a002-b88763e56447 | -1.74612 | -50.47828 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c20c6cd-727d-304f-9151-9c7292080b2c | -1.69235 | -54.26293 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38bc5aa0-7ab8-35a7-baba-eb0be51ad38a | -2.20775 | -53.71155 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16437d74-eda5-3808-9150-b6d241c26f52 | -3.24871 | -47.90557 | 2024-11-16 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea000c95-f203-353d-b1ad-9dc7922fc809 | -2.577 | -54.41623 | 2024-11-16 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06160a1c-876b-3044-b57c-60e02d6b0de2 | -2.9496 | -48.01794 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7a1eb0e-9809-3cd8-9f67-594a311e7c52 | -2.8982 | -48.31287 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c210edaa-0abf-3d01-bdb4-f3690bb95ba2 | -2.39377 | -49.03887 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b39abe1f-0583-3b38-9942-ad12f14b7688 | -2.15713 | -46.41486 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fbc9fd4-5995-3bb1-8cb9-56452d5a3d67 | -2.23116 | -53.60859 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cbe9c389-23cf-37b2-a721-fe0d8c7edfe6 | -2.34722 | -48.96427 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd23f1c-60d7-3738-8d92-020ee80798a9 | -2.46081 | -53.97013 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77d7e19f-ab18-3d99-a339-d0e37ee6d073 | -2.74364 | -48.55993 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efc75fd7-2a98-3b9c-a239-a3a8755d1f21 | -2.28821 | -46.45576 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b8887ee-1b48-37d5-bdfd-f761b543d866 | -2.79188 | -48.56585 | 2024-11-16 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1b89dbb9-3f7a-38d0-aeb5-cd0befd181e7 | -3.9475 | -46.7054 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6382caec-c910-30bf-af5b-4788964e6dd1 | -1.13643 | -48.76823 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4df01133-12a5-3686-ab40-bc63b291f2a8 | -2.20259 | -49.28569 | 2024-11-16 04:48:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3260eb4f-d122-34f2-b893-7822a7dcd535 | -2.55283 | -54.03909 | 2024-11-16 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfa76688-2657-366b-9f59-3b4fc3922325 | -1.55071 | -54.31102 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4806aa11-f736-397e-a4c5-84de11794191 | -1.85681 | -54.27642 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ddc05f6-8ed6-34b5-b086-065c26be0c57 | -2.25288 | -48.73384 | 2024-11-16 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5141238e-b94f-3574-a9ab-3a0d3fd718c0 | -2.80909 | -52.92328 | 2024-11-16 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb0cc733-31e0-3caa-a537-f55f6937d099 | -2.14382 | -46.55622 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 226fd63d-60e3-3e62-973c-be97b5adb0cf | -3.94817 | -46.40873 | 2024-11-16 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fff4a9f-8c7d-3996-950c-1b5bc6364e31 | -2.2032 | -49.28186 | 2024-11-16 04:48:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c357796-3555-3c13-a15e-53f7e66b2871 | -2.09748 | -46.58911 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba5f274e-612a-3bda-82e3-86f5e13fcec9 | -1.40568 | -51.09026 | 2024-11-16 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1e00839-a08a-3481-8904-90f0dab8bc90 | -3.74434 | -45.65173 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9fd0000c-e01d-3199-94e4-6537cc0bb714 | -3.72908 | -45.66398 | 2024-11-16 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4c0068f6-2b9a-3ce6-a5c9-3a2cdc4203bc | -3.02922 | -47.99787 | 2024-11-16 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f34d8e2e-7855-3338-9c7d-b576d433c1b9 | -2.14841 | -46.55329 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fedae43-77cc-39ce-a3e2-82858e09b04c | -2.90595 | -48.30827 | 2024-11-16 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b3f5274-1929-3947-a9d4-f0f23939e9ef | -2.19379 | -46.60736 | 2024-11-16 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa99981a-ae07-387d-99a8-cc4604669fdc | -1.70982 | -46.1605 | 2024-11-16 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54fa96a5-cbaf-30ff-881c-6eeb532f637f | -1.65834 | -50.49678 | 2024-11-16 04:48:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ff61eba-ed43-3e50-b8ba-e4c20b575814 | -1.86767 | -54.27711 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40cbe7bd-b00c-30ea-b3e3-cedb60a3aa99 | -2.31304 | -48.46568 | 2024-11-16 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae8cdc0d-9915-3ddb-b3af-c940a3bbc42d | -3.88015 | -44.09388 | 2024-11-16 04:48:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f272a3d7-baf2-30e5-8f77-53934edcf237 | -2.15219 | -50.72733 | 2024-11-16 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5f32877-038d-3a56-b234-5098ac183540 | -3.79704 | -40.99739 | 2024-11-16 04:48:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9976eff6-99e6-3144-94d3-b2e1a556a1f3 | -1.19034 | -53.89062 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 182bc6a3-767c-36fa-b51e-c0d75974fc25 | -1.07328 | -54.10128 | 2024-11-16 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e490234-898b-39cb-98b4-2ff5d49c807a | -3.73479 | -45.65604 | 2024-11-16 04:48:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 18848310-db08-3af6-87d4-a1a24da6db13 | -3.06617 | -45.34481 | 2024-11-16 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d58a2716-dac2-3dd5-92ee-a3922ad2eab5 | -3.49865 | -47.21725 | 2024-11-16 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| efa18ec1-4f98-3982-8c91-fc9ac51bcd86 | -2.78 | -48.5806 | 2024-11-16 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5f237e05-65d1-37c9-84a1-2813de9ffd11 | -16.9384 | -57.6291 | 2024-11-16 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 46ec3521-9585-3a36-919d-7db4be8c3ccc | -3.2009 | -45.5405 | 2024-11-16 04:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 376f96fd-6ef8-35a8-8bd6-3fad14584c37 | -17.2547 | -57.4493 | 2024-11-16 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 2f039436-2a4b-371e-8b48-5828a72f5ed3 | -3.2008 | -45.5629 | 2024-11-16 04:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4f86b4c0-08b7-3bd4-80cf-09aa6f6ae862 | -17.5478 | -57.5375 | 2024-11-16 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |


[Clique aqui para ver as próximas entradas](README48.md)
