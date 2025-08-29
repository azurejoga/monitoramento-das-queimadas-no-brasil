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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d40b0e6-a2e3-3f26-9dc2-02c06a961a80 | -9.4618 | -60.5682 | 2025-08-29 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| fd8d688c-58c7-3cb6-80e7-00974b533ed5 | -9.773 | -64.2469 | 2025-08-29 06:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1b56de40-fc5b-3042-908b-0c0f159ce552 | -9.4433 | -60.5499 | 2025-08-29 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| dbb009e8-a96f-3ffd-a22b-4b431535487b | -10.3624 | -57.8258 | 2025-08-29 06:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| b8930fa0-1fd3-3b19-9b74-2c42aee80e04 | -10.99 | -46.9242 | 2025-08-29 06:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 86bcae18-fbf5-318d-9741-73e420fdb4ee | -8.53352 | -70.74577 | 2025-08-29 06:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f353487-3a83-3bbc-bf64-99bd3a3f5277 | -8.64646 | -69.57078 | 2025-08-29 06:48:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e495953-d503-35cc-862a-693f29187f2b | -9.80138 | -67.84821 | 2025-08-29 06:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d077240f-8b70-3360-b9b6-631660fc2d93 | -7.53184 | -70.11869 | 2025-08-29 06:48:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ce0b74c-91cc-3d9d-9412-c3e186b8f5fe | -8.53765 | -70.74487 | 2025-08-29 06:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84649137-1804-34be-8ba4-449a112b313d | -8.44803 | -70.14371 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85a5f7f9-6be8-3e0f-9a11-b379153be281 | -8.044 | -70.09677 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28684e44-c604-3270-9d65-9ab9e6c88f8a | -9.80223 | -67.84106 | 2025-08-29 06:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 162a84d7-f72f-3802-8479-7472c74ca7f3 | -8.53894 | -70.75095 | 2025-08-29 06:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55a42393-def8-3e62-8400-30188de15be9 | -8.44183 | -70.14289 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57ddd6b5-806f-3d4c-83da-fc30fa261523 | -8.03782 | -70.09591 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0fe58ef-a65a-3d82-9140-c258478a609b | -7.99432 | -70.28883 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2655cc7c-a7bf-338e-bf17-0dde43352046 | -8.93181 | -71.27409 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb23f14c-7029-3fac-8e68-07efc651625d | -7.99496 | -70.28417 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8de998de-0e56-3998-a713-da5bfd17a92e | -8.44245 | -70.13801 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aeef8809-f01a-3433-a25f-6d0ce2c0e639 | -7.99448 | -70.28549 | 2025-08-29 06:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea36fa37-c62d-3ad4-b446-ad60025207c4 | -8.53949 | -70.7466 | 2025-08-29 06:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9be55bf8-cbfa-3d78-bf38-f0feed0ebb66 | -8.53707 | -70.74921 | 2025-08-29 06:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5a0b5331-ecdd-3929-b72b-81a3bf4b966f | -8.65289 | -69.57169 | 2025-08-29 06:48:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97936bdb-4981-3d35-b014-4bd8a5767f35 | -9.4433 | -60.5499 | 2025-08-29 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 92101019-a01b-316e-9964-e80eaa4fdcfe | -9.462 | -60.549 | 2025-08-29 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 690f29c7-a490-33ed-93b0-457e4e99cd91 | -9.1155 | -65.7699 | 2025-08-29 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 12cfbe44-392a-3114-818c-ff8c92d9e53c | -9.7728 | -64.2657 | 2025-08-29 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 8628c519-2c8b-3c4f-90ae-f2330c950d87 | -9.773 | -64.2469 | 2025-08-29 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 763c5de6-676c-3fcb-b8a2-f8df8d37a51e | -10.3812 | -57.8245 | 2025-08-29 06:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 622388d8-7542-3ae2-92bc-ea6c6c7e29c5 | -9.4618 | -60.5682 | 2025-08-29 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c66dca7b-92c7-3298-9498-3e731c079351 | -10.99 | -46.9242 | 2025-08-29 06:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 6d38aaf7-d610-38d6-aee2-137d993d980e | -14.3149 | -51.8969 | 2025-08-29 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| bbad38d9-3f84-3da8-baef-8ac73566752f | -10.9709 | -46.9266 | 2025-08-29 06:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2b252eb0-6cb8-3c46-9df4-313a20723f6b | -10.9896 | -46.9466 | 2025-08-29 06:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c9be0612-f78e-316d-92e1-762a4208d4ea | -14.2949 | -51.9422 | 2025-08-29 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| dffa0234-2155-3653-95e4-06ff11bc5629 | -10.3624 | -57.8258 | 2025-08-29 06:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 97be9ec3-9dbd-3b62-8dd3-8f2622654f8e | -12.6875 | -48.1899 | 2025-08-29 06:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b5d265e9-d549-375f-bdd7-00d040da8e4d | -9.41407 | -60.57206 | 2025-08-29 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f32358a9-5eb5-3a4b-9455-a8fcadfd1395 | -9.45186 | -60.55433 | 2025-08-29 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 462cdd24-f438-3c0a-be91-4e7a77a50d3b | -9.45046 | -60.56408 | 2025-08-29 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b398d820-c0c6-37cd-bb20-38639905d094 | -9.15766 | -65.77461 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7ed1ffa3-8c21-3dd2-8907-7f453b4ddd65 | -10.85447 | -60.81869 | 2025-08-29 06:54:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 95b9f237-543b-39cd-af26-a980a724b5d1 | -6.98115 | -59.33883 | 2025-08-29 06:54:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 06c31f18-440b-30cd-b040-ded66ac15ac5 | -10.29503 | -64.48486 | 2025-08-29 06:54:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 656c351a-7fc3-3957-aed1-0f0a627fe3ab | -9.45327 | -60.54448 | 2025-08-29 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 57fee049-605e-3092-a6f8-3de599e9a4dc | -8.95355 | -65.96046 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e0539fea-176c-39ce-b59b-d184c4d8fada | -9.10763 | -65.76099 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| f1d4ea8f-7844-3c4c-9d11-67591c7dc5a8 | -9.54009 | -65.69541 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7841e684-adf1-3aab-b4e8-78c622aa1862 | -9.45969 | -60.56534 | 2025-08-29 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ed2b24d4-11b6-3629-a6f6-e639809f1e22 | -3.76118 | -54.80766 | 2025-08-29 06:54:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 08d468b8-bc99-344b-9e86-f86e20902c43 | -9.7784 | -64.23884 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 845b5dd0-c2e8-3ab2-97e2-4f38cd1c3d30 | -9.13121 | -65.29128 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 69f38649-7843-3ce3-b496-2781dd7e1220 | -9.7875 | -64.24024 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b7516271-e69d-31f9-8e47-afb4a5f18f22 | -10.07656 | -62.89024 | 2025-08-29 06:54:00 | AQUA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bf6379ed-2097-3c3e-a18c-58ad786f65bd | -8.29291 | -61.40752 | 2025-08-29 06:54:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26efd177-27a0-37b9-bba6-bc0c6d1daaab | -9.77544 | -64.25795 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 1f06eccf-1eab-3e45-83cc-123dacde5334 | -6.9731 | -59.32692 | 2025-08-29 06:54:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 7adbda92-b534-3bf2-a5cc-538840bae820 | -9.77692 | -64.24839 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 57d0d5d7-a9c6-3243-abd7-b135240d4696 | -10.36702 | -57.82057 | 2025-08-29 06:54:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8d79bd32-4a11-35c0-a0b4-2456b70eab73 | -7.34398 | -59.64783 | 2025-08-29 06:54:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dd7ec604-f444-377e-a1ac-25f2026f975f | -8.18007 | -61.36609 | 2025-08-29 06:54:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 5db3fc71-35b7-3f49-aaad-2860b28bcb36 | -9.78603 | -64.24981 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 137617fc-967a-3d1b-a596-d4bcfe6f2496 | -9.21406 | -60.86136 | 2025-08-29 06:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3f79cf02-4dca-3cf2-b676-df8e7916bae8 | -10.46639 | -57.938 | 2025-08-29 06:54:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7f71e1fd-c216-3071-b203-68434ca04613 | -9.10766 | -65.76663 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d094446b-aae7-3134-8e02-1d47349d381b | -8.95547 | -65.94836 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9f97c10e-7f6e-3905-8b09-03bb632569e1 | -9.5419 | -65.68404 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 82dca838-4417-3d74-8cad-e71c24e29ee7 | -10.36777 | -57.81228 | 2025-08-29 06:54:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3f059ef9-2ed8-3014-a6d1-d7a7d8c60988 | -6.98267 | -59.32831 | 2025-08-29 06:54:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c6b848a2-dfaa-3715-bcd9-8d60ef0ab088 | -9.72808 | -64.90436 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| fd2e74a7-accf-3eaf-88c8-90fed4a51a86 | -9.15953 | -60.92387 | 2025-08-29 06:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e580ce6c-3f07-3844-86ca-62897edb6d7a | -9.8027 | -67.83812 | 2025-08-29 06:54:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bec72fb1-a107-38d6-81b2-974e17bbd6c7 | -10.8559 | -60.80878 | 2025-08-29 06:54:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 03aa3a8f-11eb-347b-b5ff-b24d23678d50 | -9.15816 | -60.93325 | 2025-08-29 06:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f46c9409-c9d2-376b-95c9-635b815c143a | -3.75843 | -54.8271 | 2025-08-29 06:54:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 48c52e41-41b4-3878-b761-2b8f5fb68163 | -9.21269 | -60.87085 | 2025-08-29 06:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 278223c6-aee2-36d3-9ccd-aace6778cc76 | -9.76633 | -64.25653 | 2025-08-29 06:54:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 9427b0c8-a4be-3564-a78f-4160e00b3f5a | -8.25079 | -61.44722 | 2025-08-29 06:54:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 01749395-5e3a-3639-8744-f58ef12f2c26 | -9.46109 | -60.55558 | 2025-08-29 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d7f55c0d-512d-3d05-8595-c6a71bff4973 | -8.13675 | -61.21561 | 2025-08-29 06:54:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 86344b79-08b8-3dfa-b349-ecf117749add | -9.10581 | -65.7726 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f2dc496f-8a87-3b09-8756-ff48965275ed | -9.11765 | -65.76827 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 1a969957-af53-3b7b-b4e3-9754e2450ed3 | -8.1876 | -61.37638 | 2025-08-29 06:54:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fcd28641-63a8-3c9c-8ab0-fb7cf046c3c5 | -9.13294 | -65.2804 | 2025-08-29 06:54:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba5872ec-e08c-3e1f-b06e-fe5da62ccec5 | -8.28405 | -61.40623 | 2025-08-29 06:54:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 671f4219-beb1-36e7-a955-86d5f50e2418 | -8.17874 | -61.37508 | 2025-08-29 06:54:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 84bb67ae-a39f-3972-8830-ec774d113045 | -12.42636 | -63.91435 | 2025-08-29 06:57:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cd65d0fc-892d-365e-85a4-d7c2d8a495e3 | -13.01646 | -56.91221 | 2025-08-29 06:57:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e56141c7-c9b9-3368-9e21-368f7a4f6c4f | -12.92933 | -56.9756 | 2025-08-29 06:57:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6ef585c7-957b-3bad-a587-d7b07a69269e | -14.79451 | -59.71392 | 2025-08-29 06:57:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 75eb942e-3e18-3ddf-b49a-521d29b13517 | -10.93632 | -63.62914 | 2025-08-29 06:57:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 95e25919-409e-3bad-88ff-c7b941524324 | -12.43522 | -63.91574 | 2025-08-29 06:57:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3f393156-fe7d-33cf-aae1-b7dc8151ee48 | -9.7728 | -64.2657 | 2025-08-29 07:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 760e711d-de8a-3835-819d-2d0857edf5f9 | -11.5519 | -46.3551 | 2025-08-29 07:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 274.0 |
| 89943d19-8af3-31ab-95c7-329d0a24a4d8 | -9.462 | -60.549 | 2025-08-29 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a03b714b-6c80-39ae-b2b9-b6de5dffbeae | -9.1155 | -65.7699 | 2025-08-29 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 73d16f04-33d5-3c85-88c2-4dbf617159f8 | -10.9705 | -46.949 | 2025-08-29 07:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 42290872-9411-353f-8d75-0e5579f9c973 | -9.4433 | -60.5499 | 2025-08-29 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 42c4034a-5576-324a-b49c-bbfb89a89d4c | -10.9896 | -46.9466 | 2025-08-29 07:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 169.8 |


[Clique aqui para ver as próximas entradas](README90.md)
