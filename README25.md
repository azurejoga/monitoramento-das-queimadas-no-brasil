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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a96221b0-f8e7-376e-82c2-8ca8bdd18607 | -8.69134 | -64.11995 | 2025-07-15 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb711479-942a-3a20-baa3-ab879480a78e | -7.4052 | -72.59654 | 2025-07-15 05:50:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bb4cc5b-c805-3d1c-82c2-e48bb6576df1 | -5.23216 | -56.01352 | 2025-07-15 05:50:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f56ee97-7232-363e-9d87-67009faa084d | -7.78147 | -61.36894 | 2025-07-15 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2b8f2c6-8f08-39d6-9292-e0fac1d158cf | -5.22998 | -56.01518 | 2025-07-15 05:50:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0513300a-f4e8-3093-8d55-67255248c36e | -9.02177 | -61.22559 | 2025-07-15 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bda75135-8e13-31eb-b6b4-a5f0a292365e | -7.34562 | -72.79616 | 2025-07-15 05:50:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9566db3d-0e45-34d6-80b2-c60e13e61f78 | -5.23589 | -56.01606 | 2025-07-15 05:50:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fb82553-9cbe-3ab9-87e4-d6c1b445003c | -6.90939 | -52.86071 | 2025-07-15 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b7f5651-ac72-3002-a486-2946b1a21cf5 | -12.4369 | -63.69785 | 2025-07-15 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fc114912-2ef6-3adf-a4fa-d75515824e58 | -9.73503 | -63.40792 | 2025-07-15 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d99288b-e00a-3465-86d2-b688d3055347 | -12.57859 | -56.98151 | 2025-07-15 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95d04ee6-29f8-3eee-9628-e3534ead5299 | -9.64871 | -65.73957 | 2025-07-15 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 096a53c1-4697-3c09-beaa-73009f5146e9 | -12.58416 | -56.98697 | 2025-07-15 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29a9599b-8d16-338e-80f6-751923e184e9 | -10.05501 | -59.10739 | 2025-07-15 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90bf1e14-2dcd-3047-acb7-c02094ad9d54 | -10.88404 | -54.04629 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d583929-b3dd-35a0-bb0b-40655b706300 | -10.88317 | -54.05366 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00ddf081-c41f-3fb5-a467-411013ee41ec | -10.06015 | -59.10814 | 2025-07-15 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 035cd5f5-fde3-3e80-b272-49752aaeb772 | -10.86344 | -54.05702 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99fe3628-d0d9-3d63-a5c7-98254ce746f5 | -12.03247 | -63.7678 | 2025-07-15 05:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e94e4977-4b59-3ece-a75b-c9550708c472 | -10.87059 | -54.05788 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1b61f97-39d1-3b73-95f2-f75239990d6c | -9.78596 | -62.49017 | 2025-07-15 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07fbd17a-472c-30cf-8464-a1ff8bf9bf16 | -10.87855 | -54.05154 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e43f29aa-0d63-3621-9499-dc8571744568 | -10.05461 | -59.11045 | 2025-07-15 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b1b2524-e163-33d3-bb0e-40fe0e6145e2 | -10.06055 | -59.10511 | 2025-07-15 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59c1d206-3e35-35f3-896a-7e2d9d81c50f | -10.87774 | -54.05878 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64eb6f3b-d75a-3369-ac56-77679bc3dacb | -9.29197 | -63.72525 | 2025-07-15 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3be23772-e7ec-38b0-b89f-c7cef02f7664 | -10.86802 | -54.05913 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5b5f6ff-b6c0-3422-986e-c2e947a40e9f | -10.06095 | -59.10205 | 2025-07-15 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81814373-5d03-3f30-9073-c3725f06d070 | -10.88569 | -54.05246 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 838135d0-5e4d-3d01-bfb9-03a4d4ea32c2 | -10.05976 | -59.11117 | 2025-07-15 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b327ba74-1f6d-3975-bab8-df6f4ea9b676 | -9.96475 | -64.95039 | 2025-07-15 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 382105ee-2843-3038-803d-f891137fc717 | -9.29947 | -63.72638 | 2025-07-15 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d0a3e62-2aab-35b2-97c6-795fdf3f784e | -12.44082 | -63.69839 | 2025-07-15 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdac6d4e-d166-37d2-b92d-bce5104592d6 | -9.29263 | -63.72073 | 2025-07-15 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41b7bb2f-83ba-32d1-be58-09d50889fbed | -9.69327 | -65.49117 | 2025-07-15 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d24957e0-9cc1-3709-8da6-836d6deff297 | -10.05936 | -59.11419 | 2025-07-15 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33a941e-f178-3336-b5a0-738608ed8ccc | -7.73655 | -72.73671 | 2025-07-15 05:53:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae12aadc-f47a-37a2-aa53-e8f01f86daed | -9.78646 | -62.48655 | 2025-07-15 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1db725f-a87c-3cab-a254-21507f222890 | -10.52781 | -68.05357 | 2025-07-15 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f8cee21-8ee7-38bc-aeda-2fc159ce476d | -9.89655 | -67.01056 | 2025-07-15 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8d08dd1-8895-330a-bcbe-a4d28bb54e2c | -10.87517 | -54.05997 | 2025-07-15 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e22455a-c0f1-3b50-8a0c-a6e7bc87cfbb | -9.30013 | -63.72185 | 2025-07-15 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72fc4db5-4e3c-3ac0-9207-05ad5cb1483d | -9.71494 | -61.28846 | 2025-07-15 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b620792-85ca-353c-bd25-83399ac2dfcc | -9.64528 | -65.73904 | 2025-07-15 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aa4daa8-a20d-300a-9f07-dab2241d40fc | -11.4584 | -45.1126 | 2025-07-15 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 88f561b6-c64c-309c-928a-c4c3cb1cee94 | -10.5586 | -49.1337 | 2025-07-15 06:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 592b67a5-6e65-3956-8432-55336663b6bd | -11.4389 | -45.1385 | 2025-07-15 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 083cbc95-2670-3666-b166-c0de2bf72c1e | -11.4393 | -45.1154 | 2025-07-15 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 39120a42-f10f-3b4a-b183-b6f2f82e569f | -11.478 | -45.0868 | 2025-07-15 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 277a2f5f-e282-3784-8f9d-2d9631c9b70c | -11.4397 | -45.0923 | 2025-07-15 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 16f9e3ed-bd99-32ef-a4b4-43422a4aa800 | -11.4588 | -45.0895 | 2025-07-15 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 2df5283a-132f-39ea-aa5f-07a01a49f85f | -11.4397 | -45.0923 | 2025-07-15 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 593a64b7-8def-364b-89b7-206dda3b6e18 | -10.5586 | -49.1337 | 2025-07-15 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| f87401e4-e0cc-31b3-b691-b184f04ea81f | -10.5776 | -49.1316 | 2025-07-15 06:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 612e65af-3175-39f8-b540-26117ff58642 | -6.4652 | -45.3701 | 2025-07-15 06:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| e411322f-c301-33bc-8dd6-2148a43f79f6 | -11.4393 | -45.1154 | 2025-07-15 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 981d086b-6e5d-39a0-95da-cb52f4e40bb2 | -11.4588 | -45.0895 | 2025-07-15 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 1d0276f6-721d-3885-93ad-85a807edaeab | -6.4839 | -45.3686 | 2025-07-15 06:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 38650d12-d3fa-31f2-8936-8506fc338032 | -11.4389 | -45.1385 | 2025-07-15 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 40b59099-ac31-396f-b87c-f2da48b3e745 | -11.4584 | -45.1126 | 2025-07-15 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a09683eb-4bd5-39b6-b335-808b45ca0026 | -9.29296 | -63.72568 | 2025-07-15 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87ecefd9-a8b3-387f-81f7-f07df9597b36 | -9.29872 | -63.72645 | 2025-07-15 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e6e3e3e-e4d5-3973-b137-a0304467b032 | -10.5268 | -68.05573 | 2025-07-15 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2c5cbd1-59d0-34fe-b74e-a401b69bdf62 | -7.40525 | -72.59561 | 2025-07-15 06:14:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4d58af5-da67-3203-8b5f-5f17c1a164c3 | -9.29728 | -63.7297 | 2025-07-15 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1c18ce1-d1f7-3387-a1e6-5826ed14acff | -7.73714 | -72.73377 | 2025-07-15 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67d39661-158b-344d-995b-c9307a657966 | -12.03284 | -63.77089 | 2025-07-15 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74efad91-f222-3884-a5a7-1d50cd8c4186 | -12.43526 | -63.69955 | 2025-07-15 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14d30738-0830-3b92-a163-4ff98e41e1b5 | -9.64604 | -65.73956 | 2025-07-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c547b13e-38c5-37b9-a59e-54835e8d1ba9 | -7.34704 | -72.79538 | 2025-07-15 06:14:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 472016a2-a7ad-39c5-bc0a-96a0ad4bf7b8 | -8.37671 | -71.1815 | 2025-07-15 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f78f39f9-d3b5-3078-91c0-a9c0bb2ee633 | -9.78464 | -62.49128 | 2025-07-15 06:14:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc0b93b9-f292-37e6-a308-e234504c6786 | -9.78285 | -62.48905 | 2025-07-15 06:14:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 719d6d65-6323-3092-a025-9b3f73b5367a | -7.73659 | -72.73729 | 2025-07-15 06:14:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0866e7cc-65b1-3ffb-bebf-847d7797de98 | -9.29782 | -63.72568 | 2025-07-15 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ad98ff8-7530-3653-8898-40d128891752 | -9.29347 | -63.72164 | 2025-07-15 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a0ac246-3af1-309a-a9d1-f0f7ba6e3d81 | -10.52796 | -68.05485 | 2025-07-15 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72b2d895-a290-3f1c-89bc-27024b739627 | -12.03337 | -63.76649 | 2025-07-15 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57ab5ffb-16dc-3eed-ae93-c8425aa9fdc6 | -12.44127 | -63.70021 | 2025-07-15 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb688d19-a3b3-3292-98ff-426479e6664f | -9.29207 | -63.72493 | 2025-07-15 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57ebdedd-42cf-3c39-afb7-23ebdc3a9c2a | -9.78911 | -62.48985 | 2025-07-15 06:14:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08bb8c94-7d6c-338c-a760-c0e0477c2cae | -9.2926 | -63.7209 | 2025-07-15 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4ea61fa-30aa-3343-929a-9a706602a927 | -11.4592 | -45.0664 | 2025-07-15 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 0935b1c4-3d22-33aa-a44c-9f2f60477d27 | -11.4389 | -45.1385 | 2025-07-15 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| e6ee10d0-25e6-3e21-a64e-d814cc1ed1e7 | -10.5776 | -49.1316 | 2025-07-15 06:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 76dd592a-5744-34fa-96c5-8d6152f51438 | -11.4584 | -45.1126 | 2025-07-15 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9fa4fbe9-ca11-38f7-a1a6-9b667a05c3eb | -11.4393 | -45.1154 | 2025-07-15 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e711ad80-499e-3462-b6a0-2e38b131e772 | -11.4588 | -45.0895 | 2025-07-15 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| ce022fc3-19b8-309e-94c9-842e6788c50d | -6.4839 | -45.3686 | 2025-07-15 06:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 500e09a6-9551-3c39-a169-72319f969a47 | -10.5586 | -49.1337 | 2025-07-15 06:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 923593e7-d874-3a4d-a9f2-00c504cf7af5 | -11.478 | -45.0868 | 2025-07-15 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c35ea095-cd0a-308c-8478-caf535107030 | -11.4584 | -45.1126 | 2025-07-15 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 6f09fb2e-84b5-3c63-bec5-328ea91c975c | -11.4393 | -45.1154 | 2025-07-15 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 49cded9b-ce92-3b99-a0d0-21cf51ff0bb4 | -11.4397 | -45.0923 | 2025-07-15 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 8173ee32-72a3-3368-8e69-99cbb177d621 | -6.4839 | -45.3686 | 2025-07-15 06:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 6f3f75ba-c6c7-33b2-98fc-7de0a6018608 | -11.4588 | -45.0895 | 2025-07-15 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| e10d5e2f-9c53-331f-8c1c-39fcf6d7d18d | -11.4584 | -45.1126 | 2025-07-15 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a373b5f9-98a8-3326-8a2d-945e0f68dae9 | -11.4588 | -45.0895 | 2025-07-15 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| ef2b279e-4e6f-32cd-9484-ad9f169cf376 | -11.4397 | -45.0923 | 2025-07-15 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |


[Clique aqui para ver as próximas entradas](README26.md)
