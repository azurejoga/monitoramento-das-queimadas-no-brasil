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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f2c2506-cfef-3faf-9af1-78d91bd5bc4a | -9.4956 | -45.3449 | 2026-10-02 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0ab8845f-274f-37f4-996e-5f7f8f23d882 | -4.2491 | -50.7514 | 2026-10-02 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 2c58bac6-fa55-32f0-bbbf-47a59f15bcc8 | -12.825 | -51.4466 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b075d973-8106-33d9-969d-5e24a7f16d03 | -6.9132 | -59.2806 | 2026-10-02 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| cf9b6e80-2083-3b79-99c8-f3634db86071 | -4.2953 | -49.1021 | 2026-10-02 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 280.6 |
| 5c76c141-f07c-3278-b440-8d11dd08328b | -11.7182 | -43.4386 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1827fce5-ec2f-3696-ad1d-a730d834c579 | -9.4959 | -45.3221 | 2026-10-02 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 7f464f13-d67a-3252-973a-3329db9600b5 | -11.7169 | -43.5098 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ba0df9eb-edc6-3199-8d93-1874ff26c8b9 | -12.8247 | -51.4679 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| cc63cf27-c09d-334b-9e64-104534a15460 | -12.8244 | -51.4892 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 701cbbdb-492c-38a5-9e48-67490aab6e53 | -11.1424 | -44.6029 | 2026-10-02 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 254.0 |
| c61c61f7-6f9e-3eb3-8fd4-247a9b4a9d54 | -12.7881 | -51.366 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 479578f7-4b1d-3e31-a965-481e22da3696 | -18.6573 | -41.6456 | 2026-10-02 00:10:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.2 |
| 1acc2855-cfb6-3b6e-a7e2-b2073026dd68 | -11.6771 | -43.587 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| ffef4dc4-76f9-3599-b1d5-7e7790a48405 | -11.1232 | -44.6056 | 2026-10-02 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 55e31d8c-e508-37f5-b151-12edb40c9708 | -11.6959 | -43.6077 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 368.0 |
| 417230b6-6835-36a8-a7e0-2e5e971d8327 | -6.4137 | -56.415 | 2026-10-02 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2f911fef-5af7-3422-8b22-42cd565cfd9d | -12.5329 | -43.091 | 2026-10-02 00:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 124.3 |
| 441da70f-925b-3010-b9e6-5a5af5102546 | -7.2889 | -55.5973 | 2026-10-02 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 21b488fa-90f6-3d46-8445-1da1baeac169 | -2.0576 | -56.8786 | 2026-10-02 00:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 162a4c4b-ad31-32b2-a32c-0d04b9217a95 | -12.2126 | -47.9669 | 2026-10-02 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a70e26e8-e97f-3f1a-9e7d-46dda4c4b542 | -6.3952 | -56.4158 | 2026-10-02 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 249f5d66-d624-37f2-810e-48207ce53b7d | -2.8897 | -54.1313 | 2026-10-02 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| db2e102c-d85d-3242-9ae1-e313c6d0d5d7 | -4.2677 | -50.7297 | 2026-10-02 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 735f640d-fcb9-386d-8ec9-6a924ca28896 | -7.1827 | -52.6078 | 2026-10-02 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1dfe20be-7534-36eb-b614-d8cd07c34ff7 | -8.0745 | -54.8902 | 2026-10-02 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6d394ea9-fc83-3752-a69e-9585527a64d2 | -4.2954 | -49.0807 | 2026-10-02 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 9978bc1b-dfa2-380e-b12c-c8b79840d58e | -11.1615 | -44.6002 | 2026-10-02 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 7d0a7fef-6d89-31cb-b506-172e85e4c1fe | -3.0188 | -53.9876 | 2026-10-02 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3437622f-109a-322c-b5a6-1a3ae2a46c22 | -4.286 | -50.7707 | 2026-10-02 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1c08f67d-d2c5-3533-b7d1-86c1c0dfffb1 | -12.7877 | -51.3873 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a3122df1-a39d-36e9-94f5-d64da24b3d81 | -8.543 | -54.557 | 2026-10-02 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 19e329b0-3e14-3ce1-a2bf-0427182a28cf | -9.5335 | -45.3405 | 2026-10-02 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 79a7db56-17ca-3bb9-b15a-5b681c89890e | -11.4695 | -43.4062 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 74486835-1331-3391-8804-a833256f45d5 | -7.0478 | -55.6302 | 2026-10-02 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 33ee61b2-b1fa-350f-b77f-b8401b8b0b85 | -11.737 | -43.4593 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d82fb359-dc8f-3ab1-b19e-24c7815c418d | -5.7563 | -45.152 | 2026-10-02 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e973f73a-07c8-3614-ae33-855824a83dbd | -12.8069 | -51.385 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| dcab1e0a-cc8e-3409-9e0d-a08ab28487db | -6.914 | -43.6816 | 2026-10-02 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 231c8e5b-f72d-30bf-b8e8-8791a6aa153f | -11.6977 | -43.5128 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| b700b134-5fdb-38be-8e08-882b5fc3de7d | -9.8925 | -60.2945 | 2026-10-02 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6f80e858-8db1-3226-ba10-a7da80cb79d2 | -11.3425 | -51.3182 | 2026-10-02 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3613b695-c01a-3652-a9c6-7f71329bc7ba | -11.142 | -44.6261 | 2026-10-02 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 057e7a19-0ee7-34a3-b1d3-3942b0d856a6 | -11.6964 | -43.584 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 4c7784de-8932-3848-9ba6-3ccb300622b5 | -3.1839 | -54.0839 | 2026-10-02 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f604e89f-0d6b-34c2-be78-29fdab4c329a | -11.6981 | -43.4891 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 94032b97-b80b-3810-8c53-9dbdbce9668e | -9.5149 | -45.3199 | 2026-10-02 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 313.4 |
| d0868bd2-1dfa-3bff-b41c-4412b28bfdbb | -11.69 | -43.64 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c741b9d7-1c9f-3d72-b325-1d46388150fe | -11.8 | -43.57 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 241cf043-2469-349c-8ef8-d4b32a779886 | -11.71 | -43.6 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7b7395f-7d2c-3c90-bcd8-5b6cb8101f4b | -11.69 | -43.59 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82913e28-1975-3624-944f-667fab8f3a72 | -11.15 | -44.61 | 2026-10-02 00:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a5483da-66f2-3d68-9e95-cc608b7088e4 | -11.15 | -44.66 | 2026-10-02 00:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 281a0739-6103-3946-b9c9-b8cfe06669b3 | -11.72 | -43.64 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc647ee6-dd7c-31c3-b426-14ad1cb64355 | -11.12 | -44.6 | 2026-10-02 00:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d75ec810-6a30-3dd5-9bb1-d870d2a4374f | -9.52 | -45.36 | 2026-10-02 00:15:00 | MSG-03 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6821dc73-4609-38c3-804d-ee3eeb3b3cd4 | -11.74 | -43.47 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74c01bec-1a9f-3dd7-8f99-48404779d0b1 | -11.77 | -43.57 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87b5674f-7525-365d-abed-7b773bca1302 | -11.77 | -43.61 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e4d9ecc-6e79-3ab5-a904-b34830f82aab | -11.66 | -43.63 | 2026-10-02 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2446413-59c6-32b0-ba00-5459f0ec1a5d | -6.9143 | -43.6583 | 2026-10-02 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 9a8a0af3-290d-3584-80b0-e0eb4079cdc4 | -6.3952 | -56.4158 | 2026-10-02 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 9b7d20a5-6d78-3804-81ce-ec7d8bc907f3 | -3.1839 | -54.0839 | 2026-10-02 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 16c1fc7d-5a78-3d18-8b40-ec608fa81433 | -6.9132 | -59.2806 | 2026-10-02 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1f431aa7-5342-3972-851b-37ba12e94f1c | -2.8897 | -54.1514 | 2026-10-02 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| da921a89-48af-3482-b069-7e6420ef2892 | -11.7567 | -43.4325 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7a05d6a9-762b-3e01-8311-765f167f00ac | -4.2953 | -49.1021 | 2026-10-02 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 254.3 |
| 736dbd21-192d-33f1-999a-c08a1a2033e1 | -9.5338 | -45.3176 | 2026-10-02 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 180.2 |
| bc3cbc65-ebd1-3c0d-b9f7-f178caf6d682 | -12.1857 | -48.4345 | 2026-10-02 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 84994243-c362-37a7-8d8c-991907fa59d0 | -12.8244 | -51.4892 | 2026-10-02 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| afc2c073-19f1-3e83-b12f-fed896397f6e | -11.142 | -44.6261 | 2026-10-02 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9d6c416d-a714-313b-97da-61ef9d36386a | -12.825 | -51.4466 | 2026-10-02 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 56bf5f55-75a0-3fdf-aecf-aa410a520190 | -9.5146 | -45.3427 | 2026-10-02 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 3f6754fe-f982-32db-b2e0-d7d3f588c3c8 | -4.2491 | -50.7514 | 2026-10-02 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c8cc11ec-ae9c-371d-b349-3c1716749dfb | -6.914 | -43.6816 | 2026-10-02 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 8697e7e4-18c0-3bbb-b49a-47826e3e4c71 | -11.6767 | -43.6106 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a2d7da0e-f85b-3f12-921b-bf36e3fc6647 | -7.0477 | -55.6501 | 2026-10-02 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 74525c72-ff81-3a52-91b8-90400532a0bc | -7.8308 | -55.1262 | 2026-10-02 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4fdace04-cb2b-303d-9835-c2b79740b7bf | -3.1838 | -54.104 | 2026-10-02 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| b52e63d5-790c-377f-b5de-17f22be216c1 | -11.7169 | -43.5098 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ddfb9f0e-1445-3ff1-af60-2f861cf8469a | -11.6771 | -43.587 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d09de932-b4db-3d32-8694-3963cc41f484 | -4.2676 | -50.7506 | 2026-10-02 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 5b436f93-d8b7-3286-b53a-98b08ffecf5b | -5.5499 | -45.257 | 2026-10-02 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9d4a85a6-cc5f-36ac-bf48-275a8b759030 | -11.4691 | -43.4299 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 40806b07-01bc-31be-9996-a97bb9cf519d | -7.2889 | -55.5973 | 2026-10-02 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 11ce5337-0ea5-366d-ad8f-6c1cb3f09322 | -5.7357 | -43.2682 | 2026-10-02 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e2066e92-8bca-3f4a-aa98-a3afd44cb645 | -11.7375 | -43.4356 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 772e37ba-75ea-3567-a225-13caae924626 | -8.543 | -54.557 | 2026-10-02 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 78f6f76b-9bc9-33d3-acac-228a969d67ac | -4.2677 | -50.7297 | 2026-10-02 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 12e60201-7102-3ab7-831c-bfa657edb8d3 | -11.7182 | -43.4386 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d6a51aa9-0077-34f6-876e-cc843e08abae | -5.7563 | -45.152 | 2026-10-02 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f6090738-89ca-3b97-ae43-e989a191e8a0 | -5.7565 | -45.1293 | 2026-10-02 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 55626731-4e1f-39f7-b5ab-feb22e42bded | -9.5149 | -45.3199 | 2026-10-02 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 326.5 |
| 3afce16c-fd41-3b77-b1e0-18b2bb83abb1 | -11.7563 | -43.4563 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a418681c-5269-3199-9bf0-3e2825b46cc4 | -11.6981 | -43.4891 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c1ead5b1-b32c-3cc2-b17e-305c9544d1e4 | -12.5329 | -43.091 | 2026-10-02 00:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 5abf22e2-fed8-3b39-be8c-227913959e1b | -11.3428 | -51.297 | 2026-10-02 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8ff3bb8a-0032-35ba-9d38-5524bbd5d16d | -11.6964 | -43.584 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| e08beb32-fa04-3899-9773-bacebd95912c | -11.6959 | -43.6077 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 36426bee-9920-39ec-92e5-37f4c793ca56 | -11.737 | -43.4593 | 2026-10-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |


[Clique aqui para ver as próximas entradas](README3.md)
