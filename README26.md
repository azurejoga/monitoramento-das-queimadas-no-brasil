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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 872bc6eb-69a6-3920-afb6-75c44c9a32dd | -12.41362 | -38.83639 | 2024-11-02 03:49:00 | NPP-375D | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c7a5ab9-5269-3459-8c6f-9b4710f62a08 | -6.26358 | -39.77207 | 2024-11-02 03:49:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| afaa1bdf-5352-36ab-a11e-6d1144ab3d6e | -6.62539 | -39.75062 | 2024-11-02 03:49:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9b24896-6c4d-38d2-9b2c-09a47f6ecafe | -6.97306 | -39.97738 | 2024-11-02 03:49:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bbf429d5-8086-3cda-9d5f-805d1815f68a | -6.68431 | -39.45622 | 2024-11-02 03:49:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f2ed63a-7b59-3e91-97b5-5a6dcce868e2 | -6.62179 | -39.75001 | 2024-11-02 03:49:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 66477c8d-8baf-3f37-bdda-633f299cce24 | -6.62246 | -39.7459 | 2024-11-02 03:49:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6805e678-6c3b-32c5-b2da-ec3c6811cc29 | -6.3362 | -41.92323 | 2024-11-02 03:49:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd4168ab-09aa-39a2-8cc1-9057bb5bae80 | -6.33272 | -41.91889 | 2024-11-02 03:49:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81a0d123-9e46-33fc-8933-32dfed84e537 | -6.14253 | -41.86473 | 2024-11-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0d497e93-7574-399a-9d68-21a673646eb1 | -6.00362 | -41.83167 | 2024-11-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a7ae80fc-70a2-3d96-9833-5b93fd733976 | -5.99951 | -41.83101 | 2024-11-02 03:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e343584-bb2d-3127-a4fb-135eb98d3ca5 | -12.44632 | -44.40025 | 2024-11-02 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18fe64ee-fd78-3828-bd96-ee057d0df486 | -12.44118 | -44.40372 | 2024-11-02 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c50fa81-139e-36aa-996c-32d9fd12f764 | -5.00627 | -44.37077 | 2024-11-02 03:49:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3424e7c4-f496-3bd5-a1fd-b92c23655a81 | -5.00534 | -44.37627 | 2024-11-02 03:49:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4457b31-ba5c-3b17-a42b-f0a8ec342bb3 | -4.92165 | -44.65625 | 2024-11-02 03:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a70f6b9f-5a29-366b-b736-85c325023c4b | -4.92064 | -44.66214 | 2024-11-02 03:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76cbbbe1-280b-3f98-acab-c44fb1584236 | -4.73509 | -44.33989 | 2024-11-02 03:49:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23b3a1d4-5b6e-399b-b625-9832e7423d70 | -4.73389 | -44.34426 | 2024-11-02 03:49:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7f8f4506-35c5-35c4-a915-f71463589d60 | -4.73015 | -44.33887 | 2024-11-02 03:49:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f13736da-ad41-349d-9706-24ad3a2d0189 | -4.72895 | -44.34324 | 2024-11-02 03:49:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e321299-6f7b-3a3a-ac3d-2d026d70f0d5 | -5.01123 | -44.3716 | 2024-11-02 03:49:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf93310-e2cd-363e-9651-decf789bb7ca | -5.01029 | -44.37716 | 2024-11-02 03:49:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f63bf2f3-3db8-36d8-9569-151e4483b18c | -4.92115 | -44.65921 | 2024-11-02 03:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59f5aafe-451f-3d5a-9fdb-ad3ad04ac9d4 | -4.73482 | -44.33857 | 2024-11-02 03:49:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c7f45b2-d3ea-330b-afdc-1ccf9f4f9756 | -5.14572 | -43.83101 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43dca88e-cd58-3099-b026-edb0d6195547 | -5.11307 | -43.96296 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1fce4e97-2fde-3c28-a818-f9749e824c0f | -5.14725 | -44.17109 | 2024-11-02 03:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b83f27-b39a-3b7f-9778-6ed882fdd187 | -5.07056 | -44.2287 | 2024-11-02 03:49:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07dd91d0-34d5-3e0e-a48f-6e7f9f84012b | -5.72766 | -43.52925 | 2024-11-02 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 269dc571-e7bc-3b00-9ca5-7f2b828fe1f9 | -5.72466 | -43.52655 | 2024-11-02 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65ae4bb9-ad28-3794-a39e-3b934b93d6a6 | -5.72304 | -43.52851 | 2024-11-02 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24b29f3c-5839-3f13-8c44-4cfffb5dfd52 | -5.28485 | -44.78307 | 2024-11-02 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 638389fc-ab7f-36e6-8da2-f5a8caf1f889 | -5.207 | -44.30603 | 2024-11-02 03:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa4ff308-4b33-38f3-acfd-bcb0f9804cf7 | -5.20209 | -44.30516 | 2024-11-02 03:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c742601-09d1-3102-afc0-d6a629d10cd2 | -5.07158 | -44.23122 | 2024-11-02 03:49:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 178b0e9a-2948-36f0-a0a0-b51c9cc6880f | -5.06965 | -44.23417 | 2024-11-02 03:49:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4340b9b3-a228-3cde-a389-d475422c78c0 | -5.72387 | -43.53128 | 2024-11-02 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65d041f-20e1-345c-a1dc-141ea49a7a37 | -5.25773 | -43.3446 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b67522d-ae28-3a92-8e2a-a366e2b0d18c | -6.93819 | -44.28956 | 2024-11-02 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a03f9d8b-ed72-33e5-b3f5-52a23a58acc2 | -4.81154 | -44.79242 | 2024-11-02 03:49:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1adc16d1-496a-3bb4-bdc6-0825f7bc61d8 | -4.81103 | -44.79542 | 2024-11-02 03:49:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8272f47d-72d3-3f99-8226-a216e1028c8f | -4.96553 | -45.87439 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74cc5b98-95c9-311e-9f59-01e039544653 | -4.89786 | -45.70723 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed1c7cbd-d68e-39da-822f-6e91ae5268db | -4.89727 | -45.71067 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edc64b4b-51a2-3fd5-a49f-4abc117f5c74 | -4.89424 | -45.95872 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ecf1ca5-f6bd-3150-ac4a-6670b1c379d4 | -4.86197 | -45.78601 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f22ab098-3194-3cb9-bb49-02f68259b029 | -4.8565 | -45.78508 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 697dbeb2-825a-3f52-a6d9-c3e383692452 | -4.85098 | -45.78446 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7ffda7e-b619-34b8-964f-b64b47789c44 | -4.79648 | -45.77394 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a24f059-bb06-3096-ab20-7c4cd7b43e87 | -4.79638 | -45.77488 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17aa91ff-6f16-3ac1-bc41-b26004c04a39 | -4.79588 | -45.77747 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abd084f2-1c36-396b-b486-6c2b80afc3e6 | -4.79576 | -45.77842 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8653918b-ac44-3e7c-b135-49b96e2bb7e6 | -4.75444 | -45.65892 | 2024-11-02 03:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e19e8c01-e42b-3a53-bd1f-2d88f8c7e2fa | -4.75381 | -45.66257 | 2024-11-02 03:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e726547-5291-3b29-b943-651382fc6a8d | -4.72841 | -45.74454 | 2024-11-02 03:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33bd7818-5273-3182-9866-33b780c39412 | -4.72778 | -45.74818 | 2024-11-02 03:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0482044-7cf6-3bb8-a0c6-d382e8421bac | -4.72286 | -45.74412 | 2024-11-02 03:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 800bd312-8389-3271-bd29-e34d0d2fcc7d | -4.69178 | -45.65797 | 2024-11-02 03:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fd7c87c-4498-3a73-8c25-ec033998ea69 | -4.69121 | -45.6613 | 2024-11-02 03:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a6ad099-e60e-390a-bbe9-57aa9de48259 | -4.57581 | -45.6783 | 2024-11-02 03:49:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9d73e8e-ff67-3b77-84ff-43acb231f23a | -4.57519 | -45.68196 | 2024-11-02 03:49:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa67d7b7-f119-3f15-8878-f4ea845d7c64 | -4.57456 | -45.68565 | 2024-11-02 03:49:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c09b2d-c7b6-3574-af22-c128dbcd5b0b | -4.4892 | -45.55529 | 2024-11-02 03:49:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94d82f28-48fa-3f6a-be3e-172d4bd3e051 | -4.41794 | -45.64495 | 2024-11-02 03:49:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bd129176-2d7c-39e6-98e2-7284227ceeeb | -4.41732 | -45.64857 | 2024-11-02 03:49:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ae821cb-3a9e-32cc-8b22-4f08b29898fa | -4.41182 | -45.64791 | 2024-11-02 03:49:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83cbafdf-9bf0-3eb2-a3a7-d187c9f721a2 | -4.38584 | -45.79761 | 2024-11-02 03:49:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eea8f3bd-f0f2-3f5f-8f39-86b3183b7385 | -4.35537 | -46.00604 | 2024-11-02 03:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e8215f7-19b3-333e-94f0-e3094cdd2e69 | -4.35471 | -46.00985 | 2024-11-02 03:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3273cfa6-1196-3a57-ab06-06481f3e4199 | -5.01794 | -45.15785 | 2024-11-02 03:49:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57895cea-fadd-387c-8de4-79eab37487d8 | -5.0174 | -45.16093 | 2024-11-02 03:49:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d435d4d-acab-334e-b55e-7d9848933623 | -4.81721 | -44.79004 | 2024-11-02 03:49:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7981e1f-fea2-3bee-a186-4456b78eb525 | -4.81669 | -44.79308 | 2024-11-02 03:49:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71b2ae5a-7ee2-3621-b9b9-cdff3e488d11 | -5.49717 | -45.40321 | 2024-11-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c80c3c8a-1dbe-3e0e-b45d-6fb8c9b9003f | -5.49661 | -45.4065 | 2024-11-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 938849f5-5df3-33c1-9e07-a53a9d047e61 | -5.34245 | -45.36142 | 2024-11-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94ad64b2-eb1d-3970-bdd9-8a348ff8bb5b | -5.33721 | -45.36034 | 2024-11-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9d32be-9861-3b47-9f0d-57ee5c916d64 | -5.32524 | -45.15099 | 2024-11-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d7e4bd6-1702-3e9c-8654-664e4cf01713 | -5.32471 | -45.15409 | 2024-11-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 006d5c0f-768e-3ad5-8ccb-0710178eb517 | -5.17068 | -45.33204 | 2024-11-02 03:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80fb6ef5-52b4-3390-8c4a-22f8333e0952 | -5.22234 | -46.14974 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd84e0c8-c50a-32d8-b9cc-10ebaed9455e | -5.21678 | -46.14877 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efd78bbb-c758-39af-aa85-bdf9a3781202 | -5.21611 | -46.15258 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44f5904e-9ec4-36e2-9184-deba5c46fd55 | -5.19362 | -46.18281 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48cddfec-7c75-3e44-a247-4f234aadc6b7 | -5.19323 | -46.1523 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0dc0bc3-97b0-3573-9ec0-1a9a5e99d6c0 | -5.19258 | -46.15598 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 976ef0c1-8007-36dc-b5af-ce5d42207049 | -5.1676 | -46.11283 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2cb06b1-e327-3f7d-a068-89316512cf8f | -5.16575 | -46.11326 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ba534ac2-1335-35b9-8ad8-591bb5001def | -5.16203 | -46.11197 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d773eeb7-3cfa-36bb-ba7b-0ea059f3abf6 | -5.11624 | -46.11201 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33a03987-c001-3d25-9cd2-b576bdb248c1 | -5.11427 | -46.02496 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3e06843-cac8-3588-8ff2-3d3a14d86544 | -5.11366 | -46.0285 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d7849a8-3773-3ed0-a2b7-1deaebbf87d2 | -5.11071 | -46.11091 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 677cb927-0d5f-31b7-9f92-c040212acf8c | -5.10813 | -46.02755 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1e99206-b660-3926-88c9-f40e721e3943 | -5.09488 | -46.07056 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83afdded-f5a2-39be-99fc-a6ad378a3ee7 | -5.00601 | -46.02905 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bff0a3dd-02d4-3d9a-b7cd-df0e1ea9c237 | -5.00535 | -46.03286 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f30c85f5-b1c8-3e1a-9ef7-454bbd4439da | -5.00049 | -46.02799 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README27.md)
