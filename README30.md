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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04f7a811-4619-349c-a4fc-b6e66a720e1d | -13.53771 | -55.38184 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2db00853-df44-33ea-87e9-a7aa3325cd42 | -13.70016 | -54.7646 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a966fe81-5fe6-33b8-b44c-af0d412b59d8 | -13.68323 | -54.74661 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e0bb56d-c1d8-3674-890f-063403b10291 | -12.32741 | -49.99796 | 2024-12-13 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef409049-ccea-386c-bc6a-5e0eeaea4505 | -13.06395 | -52.04044 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a2ff7e0-9570-3fc1-9cd8-2229bf2ec6f5 | -13.69735 | -54.76015 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9851f0e-64dc-3090-bb6d-44f51af4b948 | -11.51814 | -45.00566 | 2024-12-13 04:44:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 624b9483-fcf7-3c1d-958b-dcd7add7dc42 | -13.36876 | -54.24736 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e58cb64-d3a8-30e5-9e0c-ffa8851eaa5f | -12.53635 | -57.73425 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5a81c56-cc0d-36cf-b20b-90318da4a976 | -11.48037 | -48.23185 | 2024-12-13 04:44:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b79d5dc3-d39f-340e-b293-25076a134456 | -12.49716 | -55.74249 | 2024-12-13 04:44:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c37e062-6e5b-3a09-8475-f832a8c0b720 | -10.52836 | -47.81478 | 2024-12-13 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19e1d7bd-e984-33d0-802d-02a7a4fe7113 | -10.5197 | -51.96161 | 2024-12-13 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abed7a88-e2f0-3b61-846a-545e52efad02 | -13.68541 | -54.75492 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 411f1b4c-f002-31f9-a5c3-0dc13eaddb10 | -13.37278 | -54.24418 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9dc3102f-4b93-3e48-a169-6bfa4fc9aa1c | -13.075 | -52.03497 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be24af56-201e-39c7-8d65-15b8f788cb6b | -13.07168 | -52.03444 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d60eb7b0-21e9-3765-bcd9-3c26842d87b2 | -11.53724 | -51.27406 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f79758b-06a5-33be-9e14-6ebc5aa1e678 | -8.71616 | -44.00351 | 2024-12-13 04:44:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa46ce39-4b84-3caf-adb5-b668d7e8797e | -11.2052 | -53.8325 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e8427d4a-8080-3a7a-a18a-4baa96575bd3 | -13.07113 | -52.03798 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9630d19-1027-3f2d-9903-0ea8e938db86 | -8.43196 | -49.8663 | 2024-12-13 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa695cf1-d037-3715-bd41-3e642ee684d0 | -12.33844 | -43.67107 | 2024-12-13 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf943f42-995a-354e-bf08-46490055102e | -11.20057 | -53.83942 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d8ec5e2-03a5-38f6-961a-2e0313324ab1 | -14.76695 | -52.65599 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9b3c245-f2cf-3469-be34-a7aa3ce94fd7 | -14.76643 | -52.63765 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 895715f9-b953-3c63-ad41-c0576c2172a0 | -14.76807 | -52.64887 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d00cf6b-6a26-3618-b980-04359ad99b6b | -14.91541 | -52.87777 | 2024-12-13 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2c17fd3-5fb4-38aa-b17f-611ef4c6b784 | -14.77968 | -52.63984 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20528467-106b-31c9-bc82-172252cf539d | -14.77637 | -52.63929 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07a17864-0fcc-36b2-a3a9-2259142c9f06 | -14.77306 | -52.63874 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12e887b2-5c4b-31b8-8120-c0f3be5bcf7f | -14.76256 | -52.64066 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd295880-d701-32fc-94d0-babd469985ae | -14.77138 | -52.64942 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bdde31c-02e7-3b55-8d49-3dd1670c6e1b | -15.30401 | -53.31933 | 2024-12-13 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3f8ac496-5418-31ee-9277-6491466c168e | -14.783 | -52.64038 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 35b148ad-9baf-348a-bbec-255f08f3a509 | -14.77027 | -52.65654 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ccb3bbb-44ef-3a12-aff9-d2ca7d024d22 | -14.7725 | -52.6423 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffb8a42b-a291-3784-ad87-3d8fc48c9f5a | -14.77526 | -52.6464 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e8d08fa-136d-36ba-a296-960e5536c704 | -14.77358 | -52.65708 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fba9cdb4-2dd8-3875-9c33-11aa1f382984 | -14.77083 | -52.65298 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ae58395-905d-3470-9dbc-f7a2cdd1b3d4 | -14.77362 | -52.63518 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9454fec-ea42-3989-a46d-10ae229eb72d | -14.76919 | -52.64175 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f97c2c2-faef-3335-a09f-b462c161930f | -14.78575 | -52.64449 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86de2a00-45e6-3160-9d29-5459963e9180 | -14.76144 | -52.64778 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d3baf47-d16c-376c-8948-27324cf302c6 | -14.76476 | -52.64833 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc9229b0-f36f-3444-b3d5-45fb9af2b6b7 | -14.78244 | -52.64394 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 599c0023-2362-3077-a07a-53bec4747823 | -14.78519 | -52.64805 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 941895db-f96c-3e54-80e3-74b9b25e44ee | -14.77194 | -52.64586 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b066e8f-a952-3b6e-a1be-bc372c693632 | -14.76312 | -52.6371 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f3b2796-f5b1-3db2-9cfd-4dde9d5bced6 | -14.76971 | -52.66009 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35c8dbea-a0cc-342b-866b-6ee0c4938637 | -14.76587 | -52.64121 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a879e434-6bbf-3a91-814e-94899df46c6a | -14.77581 | -52.64285 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a73f10d-6b86-3e3f-b84c-52110ebf4e54 | -14.76751 | -52.65243 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25ca3b37-fd97-314c-ae65-a4951158ba3f | -14.76532 | -52.64476 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85785d08-143e-3f82-8c0a-f7bc8886c8de | -14.7642 | -52.65189 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ac1051-66f5-3de7-b620-489bc2c065fe | -14.76863 | -52.64531 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ddbee804-c0b8-33d2-92fa-22a1b25f56d9 | -14.77414 | -52.65353 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80b87ff4-ae93-3111-b30d-f366567c39d8 | -14.76699 | -52.63409 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90f7c3f0-fbce-3085-bfa6-65a3102278ef | -14.76974 | -52.6382 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8378776f-6db8-3a8d-9fe0-fe7b3a02fa09 | -14.7703 | -52.63463 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 746cec0f-bd83-38f2-b2d9-9235bb3c04eb | -14.78188 | -52.6475 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7ab9573-dc6d-3edd-8d1a-c8d2e6ea19d0 | -14.77913 | -52.64339 | 2024-12-13 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c803f671-f346-3286-a1f0-eee497263d99 | -14.9121 | -52.87721 | 2024-12-13 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b83e3a8d-a453-3ff5-9798-01e69f1f142e | -6.9158 | -43.5185 | 2024-12-13 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 0b168a65-e97e-3946-b21b-0c466cda8618 | -5.2108 | -43.3067 | 2024-12-13 04:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| fbfb61f5-ef2a-30e6-a63f-5c4266b2b6b2 | -5.211 | -43.2833 | 2024-12-13 04:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 85bfbd21-66b7-3547-aab7-e1cce34f5db6 | -11.2151 | -53.8125 | 2024-12-13 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ce5caadf-d2e0-3b74-b8bc-6da211be69c8 | -11.1962 | -53.8142 | 2024-12-13 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 5460b98a-ff56-3b17-a5eb-e10bde6f1123 | -6.9344 | -43.5401 | 2024-12-13 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 22ef688c-1dd8-3ef4-81bc-de8fc94773d5 | -11.1959 | -53.8348 | 2024-12-13 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f42859e8-1372-3b19-a427-edaf45b121ab | -6.9156 | -43.5418 | 2024-12-13 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 8e436133-028a-3b85-87f0-c68eb07941a7 | -13.0644 | -52.0326 | 2024-12-13 04:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| edba2bf7-03cc-3b21-a7cf-373a7938fafc | -11.2148 | -53.833 | 2024-12-13 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f34e6e69-2014-33dd-bf36-9cae50bc38ee | -6.9346 | -43.5168 | 2024-12-13 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 708b43d9-eae6-324b-894e-d716c564ae05 | -29.14352 | -52.8699 | 2024-12-13 04:50:00 | NOAA-20 | TUNAS | RIO GRANDE DO SUL | Brasil | 4322152 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c625bc55-916e-39ad-854e-243ea6bf57cb | -29.62322 | -51.97061 | 2024-12-13 04:50:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f326af92-0c33-3429-b75e-88e420daea65 | -29.62259 | -51.97589 | 2024-12-13 04:50:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a25ddd8d-820d-3a60-9dbb-3b8a580af07c | -5.2108 | -43.3067 | 2024-12-13 05:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c2a2f0ff-b311-328b-912e-12a2071ce094 | -5.211 | -43.2833 | 2024-12-13 05:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 16c7fc30-8afa-3e6c-809b-870cf5041998 | -13.0644 | -52.0326 | 2024-12-13 05:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 688601b4-5bdc-391e-9d35-8681eb0615dd | -12.5497 | -57.7196 | 2024-12-13 05:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b3b24623-52b8-37f5-b8e0-aa62bbe757f2 | -5.2108 | -43.3067 | 2024-12-13 05:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9c7b58d1-64d8-3dce-bf4d-5a7475e562b9 | -6.9161 | -43.4952 | 2024-12-13 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| ba3f2e9b-a714-38e0-8e96-a81bc2058993 | -12.5499 | -57.6996 | 2024-12-13 05:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 3deeabcb-f708-3090-80b4-bf60fe636ae0 | -5.211 | -43.2833 | 2024-12-13 05:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ec14470f-55c6-3358-926c-a712b457729f | -13.0644 | -52.0326 | 2024-12-13 05:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 008cb51d-5f23-38b6-bd06-1bfb0ee113a6 | -0.74589 | -47.75787 | 2024-12-13 05:10:00 | AQUA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4ed7efbd-d2b7-37a7-9392-09dfddab8219 | -6.92165 | -43.52507 | 2024-12-13 05:10:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8c1e6d73-10ab-3170-8245-bae31b39d0cd | -4.77869 | -48.49364 | 2024-12-13 05:10:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3b32e656-f69e-3102-88a3-61b213e7cead | -6.92441 | -43.50682 | 2024-12-13 05:10:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 580322db-02fe-3162-84b5-f486226971cd | -4.15841 | -42.43575 | 2024-12-13 05:10:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 32d1ecd2-d607-3aba-930e-48af9d63a88e | -3.28666 | -45.5971 | 2024-12-13 05:10:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b7fd1b1f-2db6-3ace-bc7a-e4aade18ee0f | -6.30386 | -43.46044 | 2024-12-13 05:10:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dca0ebdd-a994-3838-847d-524555bdca02 | -6.75762 | -44.82666 | 2024-12-13 05:10:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52fcb3c5-ad93-3852-9976-f0b8c9f09d1b | -8.26621 | -48.0191 | 2024-12-13 05:10:00 | AQUA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 671cb52a-d2a3-3c9c-94b3-97a74ddcba7a | -1.61917 | -46.66101 | 2024-12-13 05:10:00 | AQUA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 56d3d15c-e9da-3f5e-978b-b0a9ec62052c | -5.08125 | -42.56131 | 2024-12-13 05:10:00 | AQUA_M-M | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 423f0b3f-fe32-315e-9d48-bd7376569c91 | -3.66881 | -39.5779 | 2024-12-13 05:10:00 | AQUA_M-M | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 7c4b8bef-efb6-3f65-bdda-be9c4a14530d | -5.20164 | -43.29073 | 2024-12-13 05:10:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 94714fbb-e60b-3017-a999-a23da6cc9a83 | -4.65265 | -43.81231 | 2024-12-13 05:10:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README31.md)
