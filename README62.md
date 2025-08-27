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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b05eccf-07b8-3a87-94a7-72aa4fe25be0 | -6.79279 | -59.63769 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3e035cf-6f5f-36da-b043-b796147ec177 | -11.80263 | -51.46769 | 2025-08-27 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e845a84e-d584-39e7-a0ad-6a40591ba53f | -9.19032 | -59.53291 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68d73a7c-1d75-3079-b5bf-e0d7d3634dde | -10.79095 | -47.0803 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fc78bb2f-9ff5-39e5-bd53-a1d0e3f0fadc | -9.28725 | -63.72225 | 2025-08-27 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5aa83b04-e180-3ca4-af30-14e78c0549b4 | -5.43206 | -60.17554 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a12a3d3-a818-392f-9efd-0bc32e9142b4 | -9.59251 | -55.38447 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03211a07-dc2b-38bf-ad31-7fbce97c0719 | -8.88827 | -62.47758 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b56589f6-684b-3852-937e-2b57350f4965 | -6.84683 | -58.96554 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a6ffe42d-1bf9-3faf-a8c1-d7271fc895e1 | -10.52027 | -57.98403 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e4de859-513a-38f0-b96b-ef4eb10f2320 | -6.61895 | -53.32809 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 321b631a-e1e1-316a-b9d5-9e28af7baec5 | -8.93447 | -65.93382 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a26517cd-3688-3667-b86a-b1f65942621b | -9.4058 | -60.54298 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cf033c1-712b-37b6-86e7-75e8f18ddbcb | -12.31736 | -55.30486 | 2025-08-27 05:18:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13005c07-92d9-3874-8a5a-7cefd3b4b4a1 | -6.78894 | -59.64063 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10d68665-148c-349d-b2eb-7434bb69a4ff | -6.67963 | -58.86163 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d26cea5-cb7f-32cc-ab44-d1096944877e | -9.16392 | -59.55013 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 516d165b-8789-3085-ba86-8cf7045a30f9 | -7.37839 | -64.36359 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4120eb82-80ea-3b6f-84b9-77938c4900f8 | -7.26344 | -57.68274 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21e14e5f-70e2-3c1d-ae33-c50d3197c057 | -8.07009 | -61.54015 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf2f626c-57a0-3df6-a539-1af78844c6d6 | -9.01126 | -65.69238 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d14fdb57-cbee-3e4c-a39b-0cc4e0d629d6 | -8.96554 | -63.38372 | 2025-08-27 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97a9adee-053e-32a7-9262-e97f4b5b2799 | -7.8069 | -63.55433 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5d2ef05-a68e-3e4b-aa2e-5cc4267777b9 | -9.80836 | -64.29192 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6ca846-92e7-35fd-b1eb-f3c499dbd3fe | -9.15319 | -60.78445 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 537abe4e-a0b6-31da-bebe-36660e664e79 | -6.57249 | -59.86947 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 227e005a-c435-3ade-99c5-9bcab3952ff1 | -9.60624 | -55.37147 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 947ac5ba-0fcd-32a0-beb7-43b7e4b7bb83 | -9.07998 | -65.72006 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97deef93-f8a1-36cc-983d-6d765c8b8073 | -8.88093 | -62.45577 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 936255a6-6646-3b97-b8e6-093b062ec226 | -8.90083 | -62.46728 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfaa93be-d200-35b8-add7-380488801402 | -6.91778 | -59.36309 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caa7ad6d-6c78-3cf2-9ca2-f64bfa2c1ee1 | -8.95327 | -65.9544 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 84441cfc-6cd8-3b58-9606-ce1b7e013c92 | -10.59641 | -54.89035 | 2025-08-27 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a9a0e17-3467-3d17-9408-530229518c86 | -9.17415 | -59.46267 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b8ce306-eda7-3191-815f-6aabfd666b27 | -10.41125 | -57.7099 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a202870b-a29d-38b7-8e2e-cbe26949ec7e | -5.42761 | -60.16026 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4a0cb76-4181-3607-ac8b-7b5299456518 | -8.24509 | -61.45679 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cda66a86-e4a6-3a31-8acd-c0fc18afcc71 | -10.40986 | -64.39837 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 972866d0-9ae2-367f-946c-c761b050aa26 | -6.83307 | -58.96694 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 746fef5d-062c-3412-ab2f-c55e70e26708 | -8.88121 | -60.78052 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6b627e1-64ff-33d6-b8ab-e7684f8c9dee | -9.25329 | -59.60698 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1150b0f8-0804-3eb4-8239-4b1acc6e0e70 | -8.33225 | -62.94282 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3ac42d2-b0ef-3e6c-b27d-690cbff20f59 | -11.91597 | -46.73834 | 2025-08-27 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0e03470-a30f-345e-a375-82bbdc4922ae | -11.83112 | -46.81054 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2733188f-f821-3947-abc8-7c35ebc8ff4e | -6.23754 | -60.00967 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 342fe7b5-5dd5-310f-ad88-589c9337b117 | -7.5705 | -47.48954 | 2025-08-27 05:18:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3893aef2-f75c-3a47-b427-7302ad2060bb | -7.54206 | -63.83795 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c3d458f-6fdd-3c8b-8c32-ae3401661491 | -9.58932 | -55.37902 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b3ddfe7a-0de4-34c0-8183-27c2e174561d | -8.90436 | -62.46786 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b90b68a5-85af-30d7-b007-1156f422f861 | -8.91201 | -60.71627 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6266208-3df8-34d6-b5f2-529b8130c6b8 | -8.95294 | -63.36796 | 2025-08-27 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f8b43fd-7800-37da-8bfd-400973ca7b01 | -7.47888 | -61.35048 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc0fb94b-f694-3fb2-a84f-8137cad2bc3c | -9.9463 | -46.3732 | 2025-08-27 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0447d5e9-bb21-311b-99f1-70d59480bde2 | -8.91868 | -60.71733 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 403f2ff1-95e2-384f-9ba3-baa6c075b615 | -9.80102 | -64.26572 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3e2b1c9-070d-3322-9625-8cd0cda0e397 | -9.40193 | -60.54597 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c23f913-2096-381d-9118-41df7ea41839 | -8.50697 | -60.56761 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc844566-0107-3f56-a68d-81820a287cf6 | -10.27633 | -64.4976 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9aef684f-2563-3f1c-b3d4-dbfdeb7952d3 | -10.3182 | -46.79218 | 2025-08-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 418fc3ec-a0c4-3af0-842c-d62b1ec132c5 | -8.10448 | -71.25304 | 2025-08-27 05:18:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d68721ad-414a-31bf-8f41-1514a4e97ad4 | -8.95906 | -65.94672 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 15b49a78-7be9-3d55-ba26-755aed7e2d0d | -6.35063 | -58.17553 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 747c3675-bcf2-3ca3-9b41-3e60a3159988 | -5.60875 | -60.23964 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91773bd2-f322-3210-a4e6-95fa2b967193 | -8.2982 | -57.37972 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66d0c638-82c3-3b41-933b-106e7ca66df7 | -7.3679 | -70.14478 | 2025-08-27 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 979cefad-7c33-33ee-8ce2-a467ced187df | -6.82868 | -58.97334 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20c22d63-01ca-35de-9bb2-8837904e3cee | -6.61951 | -53.32405 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 91adfd00-42df-397a-a536-94b60f18cc49 | -9.05226 | -65.72783 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a341e22-a985-30cf-98f0-d5de634e8e55 | -8.933 | -65.94228 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cee30626-350f-33dd-87b8-aaf0ce354b38 | -8.88512 | -62.45234 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 473eb39c-02da-3377-badd-a1c73c5bac13 | -8.53487 | -62.66456 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c88cf90-30e1-3d2f-9a80-e90010189244 | -7.10937 | -59.22327 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff0a5a88-7b4f-3620-8c56-10826e59f94d | -8.88539 | -62.47297 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| def5ce0f-afdb-3f30-ba26-b7e4dd9dd5e6 | -9.19029 | -60.80497 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 570e4d41-6320-34d0-b950-044a3ce0ae00 | -9.15652 | -59.5519 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e3069ab-d5ef-3f6d-8e14-654f8c585c1b | -6.96341 | -58.36782 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d4a17a4-14ad-34d2-bdf9-ec0ff89ac545 | -9.12775 | -60.72941 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fb84e03-0d2a-3112-ab9b-1062b8894f7d | -10.03611 | -59.3628 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e31793e5-154c-37ea-ba9b-cee861e2d3dd | -9.79932 | -64.26312 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64d92484-368d-3daa-a1be-e8b5118d4873 | -10.27245 | -64.49695 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 93f5353f-bdfa-3b88-bb5f-443e9dfae0c9 | -8.90867 | -60.71574 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32a6d384-2707-332e-b1d3-ccdb86210393 | -8.61366 | -62.64673 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f957044-02b7-3cea-9c60-900172022227 | -9.06546 | -66.06424 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c52a2982-346b-30c7-b024-3224dafbb38a | -7.48109 | -61.35851 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d14ffa4-9ca2-302c-9b12-ce274f395801 | -10.08571 | -62.89931 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f709a51-44b3-31a4-a7c6-c83031ab6b0f | -9.17784 | -60.86129 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e26045e2-ae58-3268-bf14-7f646e626efc | -8.90131 | -60.76187 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d590c489-30b8-3734-85a3-583d740d66eb | -10.0328 | -59.36227 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b430c32c-b2da-3b7d-bfb5-bbb0799a4787 | -6.94468 | -59.55854 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c195d402-0b24-3e0a-9f15-9073bb2d6860 | -6.65538 | -58.79756 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 205e1ccc-8bbb-3c4d-806d-7b50c2168c70 | -9.16988 | -59.51191 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e3dfbb8-d89d-331a-914e-a905c6efd647 | -8.93085 | -65.92888 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 82480f87-1cf5-326f-96da-9c6500c5beeb | -9.20824 | -59.43949 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 823459e0-3e0e-314f-a173-f0d6835138c6 | -9.18203 | -59.52095 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9c0c218-1460-3fc1-8190-e47f52fc5c70 | -6.8193 | -58.96834 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9deac68-637b-32ed-9060-4d122501adbf | -9.2193 | -59.67286 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2edb9028-ff0b-32a3-8d68-1b6f7bed6d19 | -9.10163 | -60.31426 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3101febb-8548-3433-a881-727a6cbed301 | -10.27853 | -64.50814 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1bede5e-4971-346d-b10e-b19c18b22d8d | -9.79163 | -64.26181 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31ce4a72-bf18-33ce-bbf7-f6286ae14858 | -12.80316 | -48.11633 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |


[Clique aqui para ver as próximas entradas](README63.md)
