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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c18778a-741f-3cb0-8a17-518c0da47ef1 | -3.25834 | -53.41821 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e0bae20-b8a8-3141-ad9a-ea55bc3ca6ac | -3.25825 | -53.35138 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 852b9521-a29c-3cc4-a366-f657feb850e9 | -3.25769 | -53.35499 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6cb30d67-3f71-331c-842f-f405dea45907 | -3.25719 | -53.40324 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8b812fb-0244-3d8a-b34a-54ee29c40f1b | -3.25663 | -53.40686 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c6a439a-b25b-34ae-abea-c0110de606ed | -3.25607 | -53.41047 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 01c2bdf9-fe7b-3281-a664-e1399ee64877 | -3.25551 | -53.41408 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8c3e186d-6cc2-310e-9666-fb9693c1becd | -3.25496 | -53.41769 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9841f5cd-2191-35cf-9e9b-409244019c32 | -3.2537 | -53.33581 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c996e42-d6fb-3b34-9a26-52b16c046e35 | -3.25314 | -53.33946 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1b7cd59-006a-3267-97bf-d8ba90fc78ff | -3.25268 | -53.40995 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| f70bdeee-523c-335c-9a50-17b20624c018 | -3.25258 | -53.34309 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 495318ee-2319-33ff-bc53-80906022c761 | -3.25213 | -53.41356 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 16d0038e-2eb4-3012-bdc8-0b2104c9d774 | -3.25157 | -53.41717 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bab89ad-62b5-3675-a72d-059cf4f6c08a | -3.25031 | -53.3353 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4398d2d7-2807-326b-85d2-e8303b0ce1dd | -3.24986 | -53.40582 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35cbb478-9c5b-3898-abb6-595af5d23d04 | -3.24975 | -53.33894 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcadaf5d-74ae-3489-80c0-e0e79ad77224 | -3.2493 | -53.40943 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| bf0c5d23-6b3f-361f-a84d-7ee6a3da4e12 | -3.24874 | -53.41304 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 2d22b81c-a626-3481-8b87-d5891bce2a9a | -3.24691 | -53.33479 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df4c1951-9a92-3f73-8969-5a519e374bbd | -3.24647 | -53.4053 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 445a7dc8-d0ad-3a60-a606-66884480152f | -3.2464 | -53.36073 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 499c50f2-4a43-3cc0-a45f-3e32850ac2ae | -3.24636 | -53.33842 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909b7a66-52a5-3498-a004-c809eea69b5e | -3.24591 | -53.40891 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec599915-5963-3f6d-ba7f-2ffccdc648e8 | -3.24536 | -53.41252 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3aba487f-5dc1-3f87-bd48-30d4bc9d3f31 | -3.24309 | -53.40477 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c1ab1a28-0059-3c6c-88d9-6bcbf6fef6b0 | -3.24253 | -53.40838 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9339e864-e0a6-3398-94b9-3ffd746408a7 | -3.24133 | -53.37107 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d77af38-81db-3258-9d51-2efea50276ac | -3.2397 | -53.40424 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c55023a-154e-3b83-8295-6a8be431f1c0 | -3.23915 | -53.40784 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a7ffdc9-961b-3498-bf0b-371469dd7b9a | -3.23906 | -53.36333 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a18da7be-9581-3d5a-a338-98fc31ce0d45 | -3.23859 | -53.41145 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f1ea600d-e030-310e-8546-b0765b45e4bb | -3.2385 | -53.36696 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 64cda9dd-d177-376c-ba97-cb840b7f3a26 | -3.23794 | -53.37058 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7b70860d-0d9a-3286-8781-168440ecad42 | -3.23739 | -53.37419 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9aba514f-6027-3334-b112-eaf7559b6f55 | -3.23576 | -53.40731 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f170015d-f338-3ad1-b143-86cd2e33c75b | -3.23521 | -53.41092 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4e0e530b-83b5-3d10-a6fa-5845998f2a8a | -3.23511 | -53.36645 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ef607e94-0ad9-3b14-b2ae-1bce8b249b57 | -3.23492 | -53.27699 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7af9c887-af94-396a-88e6-0a211b2bb87e | -3.23455 | -53.37008 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51874224-8a00-3d81-8e55-063d514bed7e | -3.23436 | -53.28065 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb34d57-dde4-34c5-ac1f-8434203a0c91 | -3.234 | -53.37368 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4db744b7-c167-3a48-96e6-18bd6530e5cf | -3.23293 | -53.40318 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 76f76dad-3dfb-3c17-a10c-527763666df2 | -3.23238 | -53.40679 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2aa01091-f631-3e80-a5e7-57ac81f03b10 | -3.23182 | -53.4104 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b5915e4-2222-3389-8663-ce3b9ca9e6f9 | -3.2301 | -53.39906 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fb3af2d0-9816-3322-bf60-95ed764e4145 | -3.22955 | -53.40266 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 96f61b15-fa49-3900-b999-a7b10f2c47c0 | -3.22899 | -53.40627 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44397ba3-98e7-34fb-aec9-fb4ad8181dfd | -3.22844 | -53.40987 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bf6428b-43c9-35c7-8de7-a082378f374e | -3.22671 | -53.39853 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8aaa3a76-2e19-373d-a47d-d15ab670e33c | -3.22616 | -53.40213 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8a8330a3-fa31-3695-b006-d0335be2f3c5 | -3.22561 | -53.40575 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ec875f7-cb1e-3882-bc79-5b8b67217605 | -3.22388 | -53.39438 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c0b23b9-9ad3-336c-bd0f-98ddf75f9b74 | -3.22333 | -53.39799 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| af59bdca-2dea-3e0a-be9c-7373b371d610 | -3.22277 | -53.40161 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00f33d3a-f5b7-36dc-82e5-7b86c02c3a2e | -3.22222 | -53.40524 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e784e3d0-ff00-395b-9dd4-81f317be0984 | -3.2205 | -53.39385 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c6f77c0-22a9-36cb-8f63-bbcbe5416b3e | -3.21994 | -53.39748 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ce19f3e-b624-335d-a95b-775321761d00 | -3.21939 | -53.40111 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 014702c8-3095-301d-b3a8-13a973239dc9 | -3.21883 | -53.40474 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91f9c9f9-de53-3ddf-87f9-b02e0fc29a14 | -3.21827 | -53.40839 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa679ad5-063b-32d7-96b5-26c9ff33f707 | -3.21771 | -53.41203 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 17e62d4b-af26-3500-a615-9823cdefdeae | -3.21716 | -53.41566 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 15690896-b6b3-3b1b-a318-6fe6b272926e | -3.21655 | -53.39698 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1fe1170-1923-31f0-85f3-43a8d6229628 | -3.216 | -53.40062 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b26dea66-3728-3d50-b0f0-c0876ccbd5fa | -3.21544 | -53.40427 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 631d6f45-1613-3814-91d6-42d2f7aad283 | -3.21488 | -53.40791 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6a07160-b02b-3d68-bf2c-46afd965912c | -3.21432 | -53.41156 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 64bda60e-787f-3350-8648-9c0c8159962f | -3.21377 | -53.41519 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e5582ac5-47d5-3606-827e-f1ff61662b36 | -3.21321 | -53.41881 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7296377-99da-3978-866f-3a1dea64adcd | -3.21261 | -53.40014 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd454946-38fe-3dcc-96d5-395328966a5b | -3.21205 | -53.40378 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fc8822bd-2384-39be-8272-34cd8e0d2fd4 | -3.21149 | -53.40742 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 14427f61-54bf-35e3-b4d5-5e0c927e53b0 | -3.21094 | -53.41106 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 73398674-5ad8-34fc-a9ef-07fe8a9156f9 | -3.21038 | -53.4147 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 35f68ecc-9133-39f3-80a3-f2305c0b484e | -3.20983 | -53.41832 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f6f2001e-ffee-3c82-8c73-3664f67100b8 | -3.20922 | -53.39962 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcafdee2-1133-3bec-acad-9be69a36aa6c | -3.20866 | -53.40326 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9f292470-b7ef-359f-af84-2e0c1987dcf9 | -3.20811 | -53.4069 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ddb17e12-0780-3019-871c-8f7f1e165dbf | -3.20755 | -53.41055 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ef278131-4c41-3e1d-a076-20c34b4fadb1 | -3.207 | -53.41418 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2c757d1c-5900-3eff-af62-5494f1de1b7b | -3.20644 | -53.41782 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1330d75e-351c-385e-8b36-fe142c971462 | -3.20528 | -53.40274 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be5cd500-694c-350e-b659-151d7d68b628 | -3.20472 | -53.40638 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db36d42c-6730-30de-9083-0997e9daab75 | -3.20245 | -53.39859 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803032d2-8ea2-36e0-b53e-45d421851acc | -3.20189 | -53.40222 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c68e436-8fce-3a8d-b555-57033668316a | -3.20134 | -53.40586 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1cbec83-285f-31d6-adc2-24cc40975623 | -3.21316 | -53.00562 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c552c21b-c4f1-311f-a6fd-f0173bb1acdc | -3.20973 | -53.00508 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97915e85-7294-3a69-a0bc-dcb7a4c0da17 | -3.16799 | -53.00252 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca28b145-97d4-38ae-b263-fc86523b781b | -3.16742 | -53.00623 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e9f940-9620-33f7-9875-d101ff37cc62 | -3.12097 | -53.12505 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0704f8fb-fded-3e73-bf88-cea6dc48391a | -3.10453 | -53.05058 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c42d2ac8-81cf-30c2-9976-3e67bd0f5b78 | -3.10396 | -53.05427 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ec34b2-9409-31d1-88a1-78cac4c7ba94 | -3.10339 | -53.05795 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd0685ba-ccdc-38ad-8345-1578a41b77d2 | -3.10283 | -53.03889 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98411df4-cb8c-3f2c-8307-c2b74d063140 | -3.09997 | -53.05741 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 896afd87-e7b0-3fb6-a626-d0430e42841c | -3.03496 | -53.04755 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2f75791-90dc-3797-b9cf-06d9e3e87537 | -2.99544 | -52.37159 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bf5f7a1-b27d-376c-a379-399085c2d8c0 | -2.99022 | -52.35872 | 2024-11-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README75.md)
