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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d12ffaf-63d1-37d1-bfd5-086fc3885359 | -11.31529 | -55.2155 | 2025-07-21 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73441cdf-adf6-3561-b7d8-62b3b42fd883 | -7.27127 | -60.17923 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3cf39c24-cd3f-380f-9e53-c28f83245fc2 | -7.27058 | -60.18371 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59677b02-7956-3464-a962-eb2b1da4d37f | -7.28366 | -60.17868 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f260da-9241-365d-9033-677e6dd2ee1a | -7.24622 | -60.19362 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d869f1c8-4ce3-326d-994b-d2f61c784fd9 | -5.30397 | -55.97405 | 2025-07-21 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43d48fd0-4b9a-3f7e-b6db-61aa52ee6b12 | -7.25433 | -60.19033 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d75ab726-afd2-3866-94c8-c7353740e034 | -10.38235 | -62.7631 | 2025-07-21 05:38:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87d49385-1e59-3210-840f-1812fe7567d1 | -7.28805 | -60.17481 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0fdc7650-2220-3dcb-9492-3bb7c818b593 | -7.844 | -63.24933 | 2025-07-21 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f85129-1fe1-3242-8969-15f18ef2fbc8 | -7.24249 | -60.19304 | 2025-07-21 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1c0c5cb-0f1f-34b9-a2a0-e128940db5f6 | -9.01997 | -59.53902 | 2025-07-21 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52b68b06-a05a-3eb0-b3d7-e48d82eea467 | -8.49526 | -64.03602 | 2025-07-21 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8b076c5-bc2a-358e-b192-76e987a3a116 | -7.2772 | -60.1698 | 2025-07-21 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e293c58b-437c-3036-81b8-ed10afe7b2c4 | -7.2402 | -60.1904 | 2025-07-21 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4108d2c5-ab59-3a4b-ae45-90d3951f9b07 | -13.45485 | -60.97533 | 2025-07-21 05:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24357f48-97f2-3ad2-963e-97a61a95ff4a | -12.27413 | -57.36058 | 2025-07-21 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 313f6422-ff06-3672-a974-6195758718c1 | -12.27329 | -57.36163 | 2025-07-21 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e04c37-6cfe-3368-9c72-2915d81f20bb | -7.2402 | -60.1904 | 2025-07-21 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3065e3eb-f76c-388b-8505-ecd1401a0e99 | -7.2772 | -60.1698 | 2025-07-21 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 25001b66-bfcb-3306-aee4-5f14e9394e45 | -7.28133 | -60.1817 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca058988-65ca-3cd5-bc12-b2808b7cd742 | -7.29436 | -60.17158 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bdf8bdb0-6c2e-3b6e-b44f-9103c7d56b14 | -7.27416 | -60.17899 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1560d24b-32be-34c0-bd63-a0da1e9a7501 | -7.24225 | -60.19868 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac3de80e-2ce3-3266-bc49-11c168e03780 | -7.28811 | -60.17461 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4d2a1e04-cefe-3ed7-8dc2-41efb0f3c8c6 | -7.23759 | -60.19017 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6801feda-ff42-3702-8d2f-2e5e9b6eda15 | -7.24486 | -60.19286 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce3ee36d-d50b-3a16-9176-5a493efa244a | -7.28291 | -60.16984 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 133a7d0c-7744-36b1-9fce-32306f2b5b52 | -7.23707 | -60.19394 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 744496f2-be00-3fe9-938f-00cef20cee46 | -7.24537 | -60.18899 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e08da14-c75c-3c66-805b-6231c39f48f9 | -7.26785 | -60.18232 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50f4abdf-eab6-3521-89df-c43d73d6bf33 | -7.24332 | -60.19094 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc0928c9-5523-3477-8b18-c6918bafd1fa | -7.28917 | -60.16675 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c1b53f57-5b11-3000-8d7c-d218078b41c4 | -7.27359 | -60.18304 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 936d6570-6f90-3a9d-8fb6-44f8bfb4d4ef | -7.26157 | -60.18556 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a18e9f4-502a-3b7d-a72e-ef06bed22041 | -7.2949 | -60.16757 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67c684e6-9747-36e2-96ce-bc2f668066b5 | -7.26984 | -60.18031 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b7e97a5-2d9e-30c5-b8ac-5294a8bc0aa6 | -7.23084 | -60.19683 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 52ce26eb-e28a-3861-906f-cc3ae27e6e46 | -7.26304 | -60.18761 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e9e528a-daf1-3405-b961-85d21ee2a3db | -7.28239 | -60.17378 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 705fd416-0595-3801-b7c1-b6102e9e9652 | -7.26053 | -60.11795 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e61a5fc8-4186-3f68-9f6e-1cfb0c57903c | -7.26412 | -60.17946 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0734d961-96e7-383b-a11e-30089f5a8d15 | -7.28864 | -60.17071 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4c80014e-7feb-3536-9c42-bc11eff80d52 | -7.24435 | -60.19675 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2336974-2851-3baa-b548-23b215276e61 | -7.28186 | -60.17769 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e228535a-7131-31f0-837e-cbc5e56efc26 | -7.2553 | -60.18863 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ef7e841-59e5-391e-97cc-5d03de7a9b47 | -7.26729 | -60.18638 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58b8ee4a-10e7-3bb5-8ded-45540ca28a4a | -7.17098 | -59.63759 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 061c30f5-a68d-329c-8cb1-d99bb7e97310 | -7.26358 | -60.18354 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 793e3dbd-b220-328c-a76a-e52a488df98a | -7.26101 | -60.18955 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2dde8fca-6945-3b65-9e1c-8a6b1fe55f99 | -7.27472 | -60.175 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 86c2c3d7-3328-3062-af04-63b22bbd1379 | -7.26213 | -60.18151 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74824cca-d8ca-3895-930c-306ec3f631ff | -7.24278 | -60.19479 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 80a13fa7-e051-3ff2-a89c-d5505b501280 | -7.16505 | -59.63682 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df50cd5d-1557-3b03-b198-9560d04f3646 | -7.2693 | -60.18438 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7733d17-5360-349b-93d8-e40068fdcf61 | -7.23137 | -60.19297 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aa934de6-e084-3301-976c-b6b803074b21 | -7.26629 | -60.11863 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8d8ebea-ba5a-3902-92f2-00327527a0e6 | -7.27665 | -60.17301 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 18038440-8499-3b2e-98a2-fa9a75becc34 | -7.23654 | -60.19778 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f04c97f6-a93e-3acc-974b-b4429151662a | -7.27559 | -60.18099 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c2e743d-c2c1-33dd-96f2-46c99425bc0b | -7.25733 | -60.18668 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 931d068c-f9de-3ff3-8329-6d032c1e09c6 | -7.27612 | -60.17697 | 2025-07-21 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18a5cd7a-760b-3e02-958f-228ce2e607e0 | -7.2772 | -60.1698 | 2025-07-21 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 170c73f1-f1f9-3e76-8151-7525f0c8ffee | -7.2402 | -60.1904 | 2025-07-21 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 80753dd9-007a-3d7c-9c95-83adea337552 | -9.47722 | -67.61796 | 2025-07-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2287ca90-0da9-3c47-9018-7002f855dbc9 | -8.49741 | -70.31668 | 2025-07-21 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcca3333-1129-3edd-8846-1bc50caef182 | -8.28315 | -71.07251 | 2025-07-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51eb06ad-6528-346f-8f05-c82bf7529f79 | -10.29716 | -60.54393 | 2025-07-21 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67ec6587-9972-31d5-a096-5f471eb76fd8 | -8.99384 | -69.23337 | 2025-07-21 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0087af2-bce7-3906-93e4-f41bed00ed8c | -8.98771 | -71.57687 | 2025-07-21 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef42a21-671f-3190-afe3-eeed6b673f61 | -8.77613 | -71.30529 | 2025-07-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5afb8b6-735c-389d-9741-ffcf0d86d009 | -8.99329 | -69.23701 | 2025-07-21 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbf43ed1-cc60-3673-b21a-ea61a6b2e618 | -8.4947 | -64.03926 | 2025-07-21 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b492f899-e5b0-334b-9dab-4992a8381bd7 | -8.49533 | -64.03477 | 2025-07-21 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fb57997-2126-3ce0-968c-185367112b1b | -8.28646 | -71.07304 | 2025-07-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd65463-49a4-3259-9ceb-951322fcb828 | -13.4525 | -60.97536 | 2025-07-21 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b614c955-3c27-3421-a2f9-fc225f3aa5c0 | -13.45201 | -60.9797 | 2025-07-21 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df04a696-487d-3331-8868-deb6d131f2ab | -7.95065 | -71.45328 | 2025-07-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f065054-ac63-363a-9899-2f0e1f5ba8d3 | -10.29658 | -60.54424 | 2025-07-21 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b23e9c47-5ad7-36a3-8df1-2d5b86c767eb | -8.98827 | -71.57335 | 2025-07-21 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2de42bc-50ad-3fc5-807c-a17f348167e9 | -10.05778 | -64.99619 | 2025-07-21 06:01:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e311ca-883b-3489-853a-94f0a47cc023 | -7.95398 | -71.45382 | 2025-07-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98dcfe12-b8fc-38b9-97c1-61a530f34c9c | -7.2772 | -60.1698 | 2025-07-21 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5dcd2b7c-7012-3705-bfc7-1fabeb43910f | -7.2402 | -60.1904 | 2025-07-21 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0a6e0924-a6a0-318a-a9de-c111c02d9692 | -3.03904 | -47.85696 | 2025-07-21 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 27535058-9292-302e-9158-0ea46d348780 | -7.23882 | -60.18629 | 2025-07-21 06:16:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fede11d7-09bb-3dc3-b01f-706741991a0d | -10.14437 | -49.64917 | 2025-07-21 06:16:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 73959d44-1b21-30c1-8fd9-fefbed1a83a2 | -11.8042 | -56.95882 | 2025-07-21 06:16:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 393149c3-213e-3024-a156-bacc82256909 | -10.66191 | -46.76311 | 2025-07-21 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 8e97e88a-fa41-3f97-b7fe-b936f9621a2c | -10.13355 | -49.64771 | 2025-07-21 06:16:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0fe92564-2d9d-3f04-9078-3502a8ae910c | -10.14254 | -49.66284 | 2025-07-21 06:16:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5a8046fd-1df7-3388-85e3-7fe4cc2a5204 | -10.66892 | -46.76918 | 2025-07-21 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| f0d68353-e731-3aae-8c11-1c3e030a0293 | -10.67567 | -46.76501 | 2025-07-21 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 779f9340-2fc3-38bc-85ae-cc769545f09b | -7.26859 | -60.16953 | 2025-07-21 06:16:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| bd624cf9-7edb-3e88-9994-284670f8064c | -7.28515 | -60.15081 | 2025-07-21 06:16:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f84e8756-bbc2-3919-847c-02cd27450a34 | -7.28169 | -60.17175 | 2025-07-21 06:16:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ca50b5af-9ca9-3c44-9e13-8af0b2c7986c | -7.2409 | -60.18161 | 2025-07-21 06:16:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e3326af5-5821-3276-b2df-c6aa9cdbb9ce | -20.19429 | -50.49622 | 2025-07-21 06:18:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.1 |
| 5c67f870-e6f1-3110-8783-7f78fbbadeed | -20.18772 | -50.50254 | 2025-07-21 06:18:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.8 |
| 67f2faa1-425e-3f86-a39d-3f1632a140b0 | -7.2772 | -60.1698 | 2025-07-21 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |


[Clique aqui para ver as próximas entradas](README14.md)
