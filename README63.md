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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79440696-6634-3748-9b87-6ac3175da913 | -8.88467 | -62.39812 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd773432-7585-3422-8a29-76f23c2c0eb6 | -10.78149 | -46.43279 | 2025-08-25 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aeb93e74-6ae3-35ac-a5c5-2768c19e2da1 | -11.27019 | -44.99074 | 2025-08-25 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 044de357-5c86-335d-8d64-5d8aa3683f7c | -10.59721 | -44.32607 | 2025-08-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 402b92d0-f4e3-386e-af73-ae8800642856 | -6.62939 | -58.55186 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d3eb86c-0f1b-385c-bc55-7298f1071b52 | -8.60149 | -62.59024 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e0ebb51-cc46-3d76-8678-098c8b31f29f | -8.21758 | -61.37806 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2165f023-ec3c-345c-86a8-159c527fe521 | -8.11917 | -62.87859 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7893949b-c4d3-3353-b6d0-df59b50ed160 | -9.2204 | -59.71545 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b377dbd-4607-364b-878a-67691e68e2cb | -7.99592 | -63.46119 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42b677b-62d1-36ec-a61c-df4fc8751052 | -5.42373 | -60.17223 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9cd7613-3eae-3e9f-a9cf-e391fc70b7da | -8.24474 | -61.46412 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 143b96ac-f244-3f06-8afe-0cec46e59549 | -10.58516 | -47.14071 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3f69e51-784d-33fd-af2e-7ceb5fbd87aa | -7.47119 | -45.0214 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 846999f2-d77b-3409-be90-434157a99ede | -9.20305 | -59.49992 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c826b9f-363e-3cbc-988f-e16776e079df | -9.15669 | -59.51328 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae08fd26-827d-338b-ae7a-d89a4f7229a5 | -8.54541 | -48.85446 | 2025-08-25 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 433120d8-f921-3ae7-9587-bf73581aa1ef | -6.82539 | -58.95447 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 64b38b2a-837b-3bd9-8a63-2da528cefc35 | -11.13559 | -46.33478 | 2025-08-25 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f1a21e2f-8e5b-3a6e-a1f7-8eccca8d187f | -8.22447 | -61.38644 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 623eaeab-a1d0-34ea-a48c-349aa38d9ad9 | -8.54962 | -63.51873 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 710fb00e-7a4c-3a11-a23d-b27a39b28b59 | -8.89539 | -62.43776 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82286713-cfcf-333b-8ce9-ff8ecd2d2f40 | -6.43899 | -44.56017 | 2025-08-25 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa61b9fe-3480-3593-b678-9887d0f23965 | -10.60246 | -44.33803 | 2025-08-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cb4a7145-4e02-36db-a65f-2e0d7e79b3c1 | -11.19457 | -48.4741 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b878e80-170f-3ddc-a134-096c77e91392 | -9.07249 | -65.71658 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc22f544-9cf2-30d6-89c1-e7e6f39d6455 | -10.4792 | -57.93907 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ab21783-7c05-3495-9c79-b50ec0920c24 | -7.62103 | -62.72019 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 783166e7-fb59-3490-8545-0171041ba4bb | -8.2192 | -61.39296 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6366ef0-33fe-3856-834a-d0fbf02b39e2 | -7.66036 | -42.67883 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a62e072-0170-3d80-88da-a9b9a0dcd7c7 | -9.04211 | -65.732 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05fb84a7-0d7f-3ec8-ade6-77b5cffbd4b2 | -9.71137 | -54.98561 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c049b9c-72ce-3012-9cb0-5fc335836171 | -9.01239 | -65.39639 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94bb3d38-ba92-3c13-abc8-74aa6411bad4 | -10.39424 | -57.69086 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d0e722ac-7d41-3c15-a08c-8634b510db74 | -8.22244 | -61.42305 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0029d187-bd42-3e02-a372-bdb403ebd534 | -11.17295 | -55.01912 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 570e25cd-6157-31d5-8d80-3607921295e7 | -11.59752 | -46.36969 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2f740c3-e18b-3903-8faa-8d5f7a6e11e6 | -8.22263 | -61.3973 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0b66b55-b372-35eb-b787-63f73584ca26 | -9.15837 | -62.34976 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 838501b7-5ec0-3703-bd84-7e203014f00c | -9.21797 | -60.93838 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62edf50c-c124-3b2e-ab4d-0113956fc91c | -9.19956 | -60.92305 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 672fdfb9-e5a9-30c4-9f8a-8467215ffaec | -8.23053 | -61.42446 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d4b8d2a-c51b-3652-a0f5-f009a77bac39 | -6.91468 | -44.4187 | 2025-08-25 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cea28e3-2915-38b7-910b-3ddadeb56269 | -8.62857 | -62.64635 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d5d1320-863b-34ed-8d7d-1755cef55848 | -10.78829 | -46.42547 | 2025-08-25 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a28a8e9-6603-3a21-ad83-9082fb814e93 | -7.58192 | -46.24765 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6e83e4c-d8d3-3ec7-8876-7ce256d0ff87 | -9.20372 | -59.4958 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6f6ee7b-3c34-32eb-953b-a8baf07d22ec | -10.59655 | -44.33164 | 2025-08-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5aaaf19-c651-3ddd-93e5-d2b64714aa70 | -8.23398 | -61.42873 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e567dacd-2ce4-33bb-bf27-a8e1e03d6bcd | -9.13705 | -60.77747 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9a6f1bf-8616-3dee-b149-ae2c3d1f16b4 | -9.69356 | -48.34516 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53b3d8c9-4eda-3bf1-b4a2-cfb0e86cbcaf | -6.25678 | -60.02346 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea59b53c-c9ba-342a-9b0d-d6907b5ee878 | -9.19181 | -59.61297 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a1d2e51-9d4d-367d-b9ec-492eea1239ef | -9.0101 | -65.37946 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b6d44c3-3647-3404-b5bb-9b0066e6d09e | -8.51559 | -60.57394 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed0c74c0-be7d-3004-a88e-377713a20fdd | -9.15077 | -59.48264 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7dc2fdf-79de-3bfe-9ee0-3c0504cb38c9 | -8.90253 | -62.44744 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc829a51-7ccf-3720-94de-63508c3d72d6 | -11.46478 | -55.47019 | 2025-08-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8bc9f54-a61b-3c3b-8f5f-6b209b03ac61 | -9.19146 | -59.48103 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 852f3346-e9f7-3704-b4a0-376e64efcfb7 | -9.50978 | -60.50698 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c93a5ed-1057-38f7-82b7-37cf2d440113 | -9.80995 | -64.25976 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2ff2fa0-619a-35d6-a2cf-db02e3ea20d9 | -8.97737 | -61.72089 | 2025-08-25 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c3c7c6f-122f-3e66-8c21-7bdd8a51557d | -9.15723 | -59.48798 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c72fe30-543b-3f7a-865a-b977e47787f1 | -5.8015 | -59.21624 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 826e5212-c0f6-3082-9cf5-fe4108fe43cf | -7.57455 | -63.43486 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6acbd37d-6e02-3f71-ba9b-d5e9021cbec5 | -8.57036 | -63.92099 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71e82c27-9de3-34d7-8dba-be0cf18cd792 | -9.80927 | -64.26263 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ef0368f-9afe-3294-b61f-cd815c334af7 | -9.26544 | -60.7775 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c121b211-f64f-3278-844d-e59acde8ea81 | -9.6939 | -48.3427 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30fbe2bb-0d07-3b55-8571-1d2e92b688b6 | -9.20101 | -59.51228 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45b5c9cd-a286-32f1-a089-5c62a41f81a6 | -9.2153 | -59.70163 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ea6a5b8-84cc-3714-aed5-984754463e43 | -9.2073 | -59.49642 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc4325af-4955-356d-8a0d-e94eca159f00 | -10.25706 | -59.10549 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b770ee6b-fb5a-3578-97a7-1b9866b704cf | -8.9175 | -62.43743 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6404be0-5f31-39c9-83ac-3a703da83202 | -7.6247 | -62.72545 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e035b596-c2d9-3f95-91cb-c156ea2b6488 | -9.19382 | -59.78476 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9937918f-17ce-3b33-88cc-77d6672b0315 | -9.04931 | -65.7229 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91e0fbca-44cf-310c-b340-24e913076e04 | -10.48255 | -57.93961 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f46319e4-d355-30a2-8da2-b2ae44df164f | -8.21859 | -61.3966 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0375887-c2c0-383d-868f-67798af79ad5 | -7.13696 | -56.40381 | 2025-08-25 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ea623cf-f666-347b-83a1-ea08366de442 | -9.20181 | -59.44062 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3f690c8-6407-3a23-9404-aa83b5c38c31 | -7.47195 | -61.31784 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c659d74-ee69-3fc4-96fa-a90bd378262e | -9.20811 | -60.91952 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79d7a1b1-a653-3b39-9485-97262b3d47a1 | -9.26418 | -59.7877 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753f5b89-1c16-3cdd-90fa-a07a246a47f7 | -8.69463 | -63.83569 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4d37a32-71fd-3072-b4f6-6d308785c6fe | -9.24747 | -59.64248 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5a6a1c1-17d8-30e0-af95-97fe9d85ad69 | -8.22324 | -61.39367 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7817bf9e-26f4-3ee9-bb04-300695a4ac45 | -9.07628 | -66.06886 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a742cbd8-b618-3978-8b2f-ed636d5282b1 | -5.52095 | -52.00322 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1dfa0f8-a917-31af-8ea7-3b037feb7b15 | -6.14515 | -51.75366 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e72921c8-e3bf-395c-88bf-7c854855a6f1 | -9.00835 | -65.38899 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ce2adaa-51b3-35a3-9190-a3328903a11e | -8.97755 | -65.40978 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 82650786-c641-31c1-8bd8-d64825bde9ee | -8.11623 | -62.86883 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ddad709-c375-3817-b2b7-a24af4f4c43a | -7.28341 | -57.65351 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac2e0e6-e195-3bca-9b5d-32d6e5bf6237 | -6.63419 | -58.54452 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6448f4a9-e677-3219-97f6-74ec01f9538e | -9.50119 | -56.09958 | 2025-08-25 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bf909f4-68e9-37da-998d-b5296341a5b2 | -9.64898 | -59.64505 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f5b1440-6d8b-3f09-9bb8-eba15554fa07 | -9.15159 | -59.4997 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5df80a6c-d2fd-3a06-947a-8a11e91d2dbf | -9.18925 | -59.47219 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d99bb51-5275-3375-855e-f8ec8ec88667 | -7.09248 | -44.62576 | 2025-08-25 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README64.md)
