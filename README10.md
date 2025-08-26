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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d119c37-6534-35dd-a591-667009917494 | -17.598101 | -46.674301 | 2025-08-26 00:42:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9d40ba-788c-3247-935a-ba803778426a | -3.9703 | -47.861099 | 2025-08-26 00:42:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2e1d8aa-10a9-3136-88d1-2ac59f379bc8 | -6.3131 | -59.846401 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6afd5a1-2eab-3231-855a-9075308d96e5 | -9.1601 | -59.548599 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0718c26a-30c6-3598-b2ea-163d6486de33 | -7.7383 | -50.2967 | 2025-08-26 00:42:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d30efcc1-f39f-35bd-974d-88678976346f | -6.8236 | -59.41 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccc082e9-813d-319a-9f39-50584a223d05 | -6.704 | -58.533901 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b20ac5d9-e345-312a-b02d-72d5acc4747a | -8.5581 | -62.617001 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a6c86e52-ad9c-30b2-a11f-ada82e30b30b | -9.2496 | -60.893501 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53e290d9-f39a-3bbc-a8a5-611d45dee99c | -6.6511 | -53.173901 | 2025-08-26 00:42:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9336eb0d-b254-331b-9fec-1a7a2d00020e | -6.8462 | -58.948299 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47af03f7-4a92-356c-a85c-aec691b2f4e8 | -6.263 | -59.993099 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 808fc958-da1f-3fb3-9bca-cee6a7e4aaf3 | -8.129 | -55.542 | 2025-08-26 00:42:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53d16632-e38f-3163-a310-c831605b0c42 | -9.2713 | -59.7826 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd96dde4-cf71-327e-a271-8845abdff762 | -6.6926 | -58.5285 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 076d8bae-29a1-3319-9822-9cad13f84e55 | -7.7424 | -50.270901 | 2025-08-26 00:42:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0da861ef-a606-3d28-a5ef-85b97a17a456 | -9.2414 | -60.8055 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9d69825-a3bb-3c05-bdf0-c68a4859fc9d | -7.7327 | -50.2733 | 2025-08-26 00:42:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa856579-c87f-3b8d-ba00-b2158f66c5a1 | -9.172 | -59.508499 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd14b77e-dab0-3494-a22d-0e9e8f4bc54d | -9.2647 | -56.900101 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 423e0fe5-9fa5-3442-bff8-f2649eadf28a | -6.2472 | -60.014702 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d8e28c9-7ccf-3503-83ef-3b7f6bedd6c7 | -8.8647 | -62.426601 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4e08e9e-bc32-3403-b04b-dfe93b427ce6 | -7.8822 | -62.988701 | 2025-08-26 00:42:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89806d90-7996-37f4-990a-f7ab0e7ea93f | -6.7107 | -58.564301 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 058537ef-9339-39e1-b533-d2fe5c5b2b96 | -8.9795 | -65.389801 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23acb7c1-e3fe-3fec-b265-3505c818c5b9 | -9.2631 | -56.892899 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26cb4634-f50b-3905-aec6-dbfadec56eee | -6.8254 | -59.418301 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e89bac09-eaf3-33cf-b403-1813e32aa0e7 | -6.3523 | -55.795799 | 2025-08-26 00:42:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2b440bf-fffa-3250-9eb4-dd6f8dc11f99 | -6.8444 | -58.940399 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05d02f19-456a-337e-ad98-d4f4583e5c43 | -9.1701 | -59.499599 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42619575-6bfd-354b-90b0-c346ea62cf93 | -3.2397 | -46.899101 | 2025-08-26 00:42:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cad2d66-f644-31c5-b4c9-a0bcb499ebd3 | -3.1331 | -58.985802 | 2025-08-26 00:42:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e9ead70-ba8b-30e1-91be-a242b936efc5 | -9.6193 | -55.344002 | 2025-08-26 00:42:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3e84f8-d0e3-37f5-87fa-993a0277483e | -7.6219 | -61.025002 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5be63d6-64d3-3483-864c-5135060b55d7 | -6.7977 | -58.633301 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a20944f2-f3b6-31b8-8d1c-75de32abaef8 | -9.3287 | -63.153301 | 2025-08-26 00:42:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 319eb949-de37-336f-8078-7e95b2c2550c | -8.9849 | -65.366302 | 2025-08-26 00:42:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fec3fec-905d-3ab4-9c17-3f9d285d8162 | -6.8283 | -58.9604 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff6c9fa-b158-304e-a6ff-3bc50cb0347c | -9.6454 | -59.616199 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c13f9c3-c50d-35a9-a371-b6c0b296240f | -6.6797 | -58.844799 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0132e3-e52f-3d34-8a35-20649ac84ec9 | -7.3557 | -59.640202 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc3ce59d-c765-30a4-8076-8dbf1135fb47 | -7.6622 | -61.455101 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e935237a-1ea6-3706-b337-00a79656ba0a | -8.8898 | -62.4496 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7f68ee9-718e-37db-8279-db2a50c742e9 | -7.4293 | -60.6017 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc1f4cfa-f113-3a8f-bd44-9f530a2d2f0c | -6.6912 | -58.850498 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 959a1f52-6370-3abf-8e20-80eab8fb2aa0 | -8.2198 | -49.556 | 2025-08-26 00:42:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86b86cd6-d4c9-3048-b714-4be60291dc16 | -9.5718 | -55.362 | 2025-08-26 00:42:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a01288a-737f-37ea-a0c4-c992b94abf40 | -9.1897 | -59.495399 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a239cf17-94c3-3d64-a6c1-a08ec945844d | -7.1087 | -59.2108 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82a6d3ea-094a-3524-bc04-a75dbbb9486f | -6.7188 | -58.5546 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8564e85e-1790-39b6-9804-2efcad2df400 | -7.6317 | -61.0229 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7cad6a-d4c1-3856-ac1b-63f0d415fa93 | -9.1955 | -60.781799 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e15523a4-4e2a-3b0e-b9d1-8646312b047d | -9.1739 | -59.517502 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b9c2f40-d7bc-30df-91a4-091313fe90da | -6.6661 | -58.782799 | 2025-08-26 00:42:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f09c15fe-bcf6-318f-be25-292c0870e059 | -8.8522 | -62.415199 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e2c8a43-fad1-3232-8aab-59a8fe3de377 | -6.7749 | -59.6576 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30497ddc-046d-378f-9d4d-e8a94ebd36f9 | -6.8381 | -58.958302 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6407cacc-1df4-3bcd-b50f-4af975170320 | -8.5553 | -62.603298 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da8df578-7e18-3e3f-a983-8f5194523baa | -9.1582 | -59.5396 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 441adb96-91c9-3889-9559-a840e5745365 | -9.188 | -60.794498 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77a3913e-ade2-3f4f-8fff-10025a28af5a | -9.1995 | -59.493301 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed418a2-d439-35d0-bbc3-1d409530644a | -9.1976 | -59.484402 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e87a9f21-0405-37d4-a0bc-6c6193fc19e6 | -10.4021 | -57.688499 | 2025-08-26 00:42:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 642d4962-e365-38f7-aef6-950867ccd9aa | -8.8968 | -62.434101 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0ece73a7-fa7c-366f-b0b1-c6e3ed0a7272 | -2.9244 | -53.678902 | 2025-08-26 00:42:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9908795-4e63-343d-9559-aee70236468c | -9.1844 | -59.422199 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aead9ac9-fddf-3e64-8882-4598610318d3 | -4.7008 | -56.056 | 2025-08-26 00:42:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f6b7c6f-4b25-332a-a5ff-e280530b190a | -9.1878 | -59.4865 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2790938d-0359-310c-a043-30845eda4d2d | -6.9145 | -59.355801 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dcab1188-be4b-3caf-9c32-783055d23126 | -9.2858 | -56.902802 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be4fe4a8-bb24-3d4f-9689-30756e754597 | -6.2453 | -60.006001 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5579ebc7-0fb8-31ba-a2a6-d761c9f56cec | -9.1872 | -60.839199 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81eaa3d7-0dfe-389a-b7d4-e7927bf7b654 | -9.335 | -63.183998 | 2025-08-26 00:42:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f76418b4-171e-32bc-9258-bb102bb1f94c | -9.2827 | -56.888599 | 2025-08-26 00:42:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5964bb0a-da80-3ca8-9720-284cf0861aad | -8.1086 | -62.853901 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea4df3df-561e-3c68-bea6-a4214450147b | -7.4875 | -61.353901 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60c95ba9-a20c-3327-94a9-548cad003227 | -6.815 | -58.9468 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a33152b-f80f-382a-94e5-72b5b90623de | -8.2507 | -61.437099 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9e101ea-83f3-3514-8afc-f18870a81dca | -8.3534 | -62.906399 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 443dfb5a-cc8d-3ad6-b4db-047b2bada47f | -7.7452 | -50.2827 | 2025-08-26 00:42:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31d481bd-2f01-360a-9c16-c766a7a36514 | -9.2014 | -59.502201 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68ed797f-83ff-3a3f-be80-cf1c5799c530 | -3.1363 | -59.000401 | 2025-08-26 00:42:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f39542f9-ea05-3787-96ef-55318cb0d332 | -9.2157 | -59.424801 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad1d393-e931-3c53-9953-d75928011452 | -6.2434 | -59.997299 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c17b69a3-e046-3937-b295-4dc2cc2b14fa | -6.7629 | -62.848099 | 2025-08-26 00:42:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a8f9fac-498f-371b-a4da-2e88e119be45 | -6.2513 | -59.986401 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71c0fe36-bd00-325f-8f11-6a085561491a | -9.1672 | -60.743599 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| baad0f78-f362-337a-b7dc-0e9b61d1ee2f | -7.4852 | -61.343102 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6364ee53-6edd-38d5-94c9-4d6b7494fd10 | -9.1803 | -59.450901 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70608355-e084-35a4-95f8-da766d66082a | -7.2969 | -59.652901 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 663e286c-4d98-377f-a58b-fce778f73d57 | -7.6295 | -61.012501 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e26f62c-03e3-3f96-a3d6-d15bd88e0828 | -7.5387 | -61.354599 | 2025-08-26 00:42:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86308e90-0a41-3b8c-bc32-8fe734d2d4d1 | -7.3839 | -64.308998 | 2025-08-26 00:42:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd0f5bb-2846-3ab7-9994-357243ec7da7 | -6.8329 | -58.9347 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7d59b0e-5910-358b-bb47-f4c77033d9be | -9.2421 | -60.9063 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42bced71-f9b9-30b5-8d79-3e84bd4faea8 | -8.862 | -62.4132 | 2025-08-26 00:42:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c46bf848-c913-3678-8ff4-354eba98d3c3 | -21.6089 | -49.690399 | 2025-08-26 00:42:00 | METOP-B | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3cfb634f-0a4a-3b94-97ba-93178c93f4c8 | -6.7601 | -62.834801 | 2025-08-26 00:42:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd7390cf-829b-3af8-be29-83952824f10a | -9.2791 | -59.771301 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49075a38-3028-321e-8b53-aaa044846a64 | -6.8168 | -58.9547 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
