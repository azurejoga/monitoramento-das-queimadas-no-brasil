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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d2b395b-c274-3508-91b6-e224fcc1a3cd | -9.16002 | -68.25934 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2636fa8c-c6e2-3084-98c3-be5bf1d6040d | -10.71645 | -69.40594 | 2026-10-06 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9342e318-2113-3a3a-a658-7c6897d40011 | -9.02609 | -65.71218 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a84bbd5d-f687-3697-8486-53d8a3f4fb32 | -9.10369 | -67.75153 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d69b723d-4137-381e-bb77-8cbfbb474b36 | -8.60634 | -72.72882 | 2026-10-06 06:01:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9c37bd9-62cf-342d-82fc-a2244f56ab78 | -9.13179 | -67.75996 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bd973fb-9466-3c27-927e-68a66ccce588 | -9.19051 | -65.89197 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63fbe657-dafc-34ae-a3fa-a9203021748a | -9.46078 | -64.33028 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6712a66a-a957-31b9-92e8-f6b121233292 | -8.45263 | -70.21123 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13853264-5c4a-3c6e-8c78-6dec860600ad | -9.26272 | -68.37772 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 939baa83-4a31-3a09-a6e0-27c066c2a899 | -9.22902 | -67.89432 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dbaecb2-e578-3792-8a4f-9e0293708521 | -8.54295 | -66.97711 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56444a57-d28d-36bc-bcd0-f33ec51c5572 | -9.46016 | -64.33449 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5e08d75-7ad5-32a6-8e60-e768656839ef | -9.54418 | -64.81351 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa396fb9-d68e-384b-a900-212879cab367 | -8.7229 | -68.9045 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f7b100e-d340-3db5-9429-361b71fdab72 | -10.69673 | -69.63204 | 2026-10-06 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f061c21-9927-3989-a4f5-764e02aaf370 | -10.87949 | -61.40623 | 2026-10-06 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d70d8f54-cfb5-3731-8171-de7ce69a46da | -9.68105 | -67.06837 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f53180d1-2d76-36e9-8509-7baccfa59fc4 | -8.69638 | -70.0248 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95bd0f05-32e5-3443-adc3-a4858cef58fd | -9.1273 | -68.27964 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dacb27ad-4dab-3161-8f60-87dc40f4d4c1 | -8.62403 | -69.5029 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecc456ff-3228-38c3-b719-b0a19d48caef | -9.12844 | -68.27255 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9bb792b-d9b4-3102-8220-be7606abce6b | -9.22958 | -67.89079 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15128326-adee-3e13-9d59-23ec55e307fb | -9.50525 | -68.4942 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 831523d0-1f53-33e2-a299-e9d9b679f0ec | -9.13948 | -67.81873 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c687b2da-2ad6-3d1c-9733-33edbb497dea | -8.77771 | -69.53181 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9885a0f2-ad7b-36b3-98a3-c6b9893276ee | -9.10207 | -67.69746 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8004d1c9-59ce-356b-9a2f-b5c132b8b737 | -9.13299 | -68.24418 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 095f9f86-2625-33de-b3a9-9a11b53b5f90 | -9.21947 | -68.16734 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f79fcda4-37d1-344c-9648-e5eec4efb8f8 | -9.08892 | -65.46205 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec29ef48-b25e-3386-9053-046ccfa0caed | -9.16369 | -61.40846 | 2026-10-06 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 294d5b5b-fc1d-35c5-9fe9-1fedfbd054d8 | -11.99135 | -60.47736 | 2026-10-06 06:01:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e46730db-4146-3b5c-8396-d1e11b0d511f | -9.48768 | -63.95781 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 930431da-c4cd-317b-aa52-73093aadb755 | -8.54572 | -66.98114 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baf7e4aa-f5ab-3249-90b0-805de500a8f5 | -12.60912 | -60.90195 | 2026-10-06 06:01:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 643941af-c8cf-3003-a60d-a44fbd85d552 | -9.29161 | -65.64185 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccb3634b-3d1c-37c1-a787-1cd091f60625 | -10.07592 | -69.17719 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ce3e100-ca83-3061-91ca-d4a395805db9 | -9.10453 | -65.35985 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c79c40dc-5e76-31b0-8e2f-39c6f39bd282 | -9.19746 | -65.77995 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebf677f1-0b1e-362e-9b52-1302c8a2172c | -8.64597 | -66.85693 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a32dd0-d326-3730-9a54-7aa381d8ef05 | -9.48154 | -67.66877 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6315a9b6-99e5-3e75-babd-7dcd070488ad | -9.38689 | -68.07486 | 2026-10-06 06:01:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48fd2189-d592-3ff5-a51c-449c4bde9fff | -8.34762 | -62.8351 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c771e67-4105-3e25-a7da-bd2670386a90 | -9.3666 | -68.85548 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6658f577-ca4c-3933-aa5c-c473737482e2 | -12.13372 | -63.15622 | 2026-10-06 06:01:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5ffec3d-cc85-364d-b303-5936c64fa46a | -9.43949 | -67.09815 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaab17f8-7f9c-30fb-8619-6840a37a49cc | -9.48114 | -67.09402 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e63d81-3084-3f53-b75e-ab0cabe87a13 | -8.65606 | -66.49784 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c915baf5-8259-3179-bb7d-29e0354b9c48 | -9.29504 | -65.64239 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8245825c-b2bf-3a42-ab4c-deb7f86c852d | -10.24947 | -68.26188 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e62a0012-1859-3e9b-b202-315e826481e6 | -9.2633 | -68.37418 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1bf5763-a67d-357e-8441-a3546d6d6f37 | -9.12471 | -68.21012 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a45e49b-6a1c-35d0-afc9-54de18c5611b | -8.76685 | -63.68892 | 2026-10-06 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7210fab1-bd0f-3f68-885e-4eb070e1a7b4 | -9.16961 | -67.67274 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af595b9b-3ad1-3e26-a411-67718d227159 | -8.76213 | -62.61852 | 2026-10-06 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 502c5da8-deff-3128-b9bd-743ea397634a | -8.56298 | -67.06634 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93108e92-8737-344c-adcf-184416a19c22 | -9.36831 | -65.80174 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aedb3920-4f55-3fe5-91d0-63f9661d70da | -9.48487 | -67.6693 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a4e3bfd-8472-3deb-918e-63bddb539b76 | -8.34445 | -62.82962 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42ef5ce3-5953-378b-a3ea-00fbff893ca1 | -9.15094 | -68.29427 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e8f760b-4e74-378d-ad5f-22e8663660fe | -8.63098 | -69.50404 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3222ebc7-dad0-32d2-b6d8-b6ea1a98fc71 | -8.62687 | -69.5073 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac30111-39cd-37b8-8302-5c20e10bad64 | -8.28574 | -71.07271 | 2026-10-06 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b5cf856-eebb-3301-8fd8-b822f003289c | -7.91663 | -71.77883 | 2026-10-06 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c58f946-6879-34b1-8b92-d2ace3322154 | -9.1877 | -70.79453 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10a7764b-fd9e-30f5-957b-c6706248ddfb | -9.14535 | -65.41668 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 943b7cae-d6e4-3c10-8e6d-be43ba56d0c6 | -8.97378 | -65.44035 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7068c6de-b90f-37f5-9b23-75e0b025f017 | -8.61047 | -72.72961 | 2026-10-06 06:01:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7be20bd-1743-3269-bb57-9bf77c1ef702 | -7.45313 | -63.55643 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f31d930-f5ca-306f-b55b-a34f21806220 | -9.1054 | -67.69801 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb456095-01f4-389e-8764-ec3d9e8f034e | -8.34519 | -62.82472 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d24707cc-8705-3eae-abd7-84d7eaf119f6 | -8.05084 | -72.34928 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8823ad7-d3ea-3c36-b2c7-aaf2aa34e5a4 | -9.22685 | -67.52762 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d279f7e-db95-3a39-82bb-e8a083e3c223 | -9.22821 | -65.68923 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c57873ba-9b7f-31fc-b64f-e342190fec3a | -9.13014 | -67.74891 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f52dccac-69a2-3126-ace0-d6d3237d8d28 | -9.32343 | -66.58803 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eafcbbd-97e1-3933-9edb-ed33946d7269 | -9.97038 | -65.01752 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8091e28f-1fa7-30b4-8120-8a547e09319f | -9.19347 | -66.00793 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e13df65-33b2-367a-9a09-59af1c9961f2 | -9.50189 | -68.49365 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a10e8e-b27d-3088-952d-954d4883d219 | -12.12895 | -63.16095 | 2026-10-06 06:01:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f06c5a12-4f95-38cd-a146-a816f89558d1 | -9.46779 | -67.07026 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2184e5cf-e494-3f68-a4b7-f5037a08a0d6 | -9.34025 | -64.71047 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc173e6d-cc4c-3871-bc3c-ce4a5a9bbca9 | -9.48902 | -63.949 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbef45f2-9a1e-3b8d-87bb-31aed4dca754 | -9.11203 | -65.35713 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 705cccb9-eb90-31da-a129-82eaab5ac114 | -7.67628 | -69.95638 | 2026-10-06 06:01:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff95b4af-9cad-3395-8c13-5a3f4066041d | -10.63791 | -69.2872 | 2026-10-06 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0d39c3d-662a-3998-a178-6ce83b054b52 | -9.25988 | -65.4453 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e47dd5a-05bd-3cf6-a62f-57d72a37a94a | -8.43182 | -70.11546 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2bfb52b-803e-3a3e-8f97-4f32e88922c0 | -9.2324 | -67.87325 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1023e205-dea0-37f0-a6db-ba6e7750dbec | -10.71387 | -69.63496 | 2026-10-06 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1732be4b-35f6-3a2b-8835-8b3291f5a3de | -8.92208 | -66.8471 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 748cda18-7b69-3999-86e1-b0c7bd83af20 | -9.09542 | -67.67484 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7ae5e14-8e29-360e-81fb-e31498fb95a3 | -10.03023 | -65.26012 | 2026-10-06 06:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee38cdd-8c35-3bc7-8240-74e0f939d8b1 | -7.4414 | -63.5591 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fb384e6-3d3c-35d5-be95-da7e85fcf9b3 | -9.20572 | -68.72894 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 139287c7-24df-3b80-a7a7-822b22b239cc | -10.24599 | -68.30483 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23e896e3-38c4-3849-90ac-d7eb3e09fbad | -8.42757 | -70.11893 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de83b58c-a3b8-3685-8b59-0f3c54f2a6b1 | -9.50317 | -67.68304 | 2026-10-06 06:01:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79e932a8-208b-3dc1-974c-580ced8c92bc | -10.11716 | -68.07796 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a29e67c6-512c-31b4-ae2e-9cf1709d182c | -10.24265 | -68.30428 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README73.md)
