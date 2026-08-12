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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c50eccdf-e361-359b-95ee-2395681c29b0 | -14.99856 | -46.58371 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce420857-21e7-3737-a683-138cf8f6342e | -11.89096 | -45.83504 | 2026-08-12 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a5a65a-b594-3dcb-9af7-7fc215382df0 | -12.18175 | -50.1595 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bb364b5-6f5f-37d4-8c92-39a23674b8a1 | -11.94518 | -46.33552 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 26cd5332-2142-37a6-9cc4-9968e7fd696c | -13.88334 | -53.82451 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89f85da0-ce37-359d-9c98-1afc8b2e2888 | -14.53837 | -50.33438 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8aa5227-05d4-3e0f-9858-078a2af0acd0 | -15.17323 | -49.2671 | 2026-08-12 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fb4b8f7-8c42-3912-89bd-f47a94c72b51 | -8.89474 | -60.57598 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efbe0b17-7ba2-39cf-9266-ab89b89f32aa | -13.90209 | -53.79916 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa6ad3a9-ec6a-38cc-9bd7-8200ebe3e857 | -15.01655 | -46.60184 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51556110-abd5-3e34-92cb-fff4f9c6ab30 | -11.83892 | -51.88382 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8441ed4a-f94a-34ba-a2c4-b50265c3d831 | -15.1714 | -52.77851 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d648c617-3c1f-3c00-a6bd-bba959132599 | -12.79044 | -51.78448 | 2026-08-12 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e75f00c0-4e6a-3fc4-b10a-8dc53e9ca58f | -11.4952 | -54.61275 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6192e50b-14f3-36f4-851d-af62bcc363c7 | -15.16865 | -52.77428 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 674a1387-43c9-38d6-9507-0ffab6dbfe42 | -12.17117 | -50.11758 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7e495f8-f4b4-3ded-86b3-0118584376b6 | -9.34192 | -47.51017 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5179fb43-1f9c-30ba-a6ad-c130b53af88f | -11.94583 | -46.33088 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 90768184-12be-3611-9220-bd61a165ea5d | -13.82909 | -53.82461 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b408e6e-29b8-3067-bdf3-62ceb7183be0 | -14.59332 | -46.76263 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a31feaa4-c388-3629-a034-c5d1c1461fa7 | -11.83004 | -51.87497 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ebe07d6-e099-36bf-855c-c3fb8c29c406 | -16.67429 | -45.03856 | 2026-08-12 04:51:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5489f126-7b3e-3adc-914e-d0f8f91b2282 | -8.95561 | -60.53748 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2789e9f2-c737-3f93-895f-be1b856c80c0 | -15.187 | -52.78874 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e8dca84-1dc5-32ee-8cc1-5a3d497dd519 | -13.43598 | -57.0529 | 2026-08-12 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bbf68ef-1a2f-3cd0-a13c-a49045690b0f | -14.36204 | -53.23285 | 2026-08-12 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 63557034-336f-3d44-a21b-51e54d5bf0de | -11.81338 | -51.88367 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f80373a-d7f4-3b72-95ce-574a5a48a9c8 | -11.95224 | -46.34199 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 71f2b579-cd7e-376a-9202-5b90a5cfa567 | -13.29919 | -49.70475 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5699b8d8-58ef-3bec-b148-be2ed0d4e455 | -11.78393 | -51.85291 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9f398de-bea8-30b3-8f0a-e5ef2844ec49 | -13.87531 | -53.82854 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1270c9a-c6aa-3037-b0e3-7eb0f73754a8 | -10.22063 | -45.93162 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5d858b72-4073-31aa-bcdd-7a6d168a8094 | -8.66271 | -54.95509 | 2026-08-12 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eb2492e-87c0-3d5a-9f01-46013a822c2f | -11.46974 | -44.55772 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d475887f-25d3-3b22-aa72-8a5d30405581 | -8.98006 | -60.53373 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 510bf1cd-7cb4-3c3d-a6fe-c1728af56264 | -11.9516 | -46.34654 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4bab14ae-a0d6-37f5-bc3c-8a7278b12849 | -15.29984 | -48.87068 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 2d67e270-ef0f-3eed-b326-c5b8b6069ad5 | -13.30201 | -49.70898 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f41febd-d326-36f4-b089-1db1c36504f0 | -15.51911 | -45.85504 | 2026-08-12 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c975f350-f9c8-3d41-8d83-89fd64c38d6a | -9.34254 | -47.50613 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5b21526-ade7-3ae9-ad41-d1f081b5d232 | -11.78844 | -51.84631 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ba06de8-4970-34c3-b7c1-ac4b3f6e5e8d | -13.43672 | -57.04892 | 2026-08-12 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da9923a9-f0ec-37f5-89f2-883d38ed57ae | -12.16561 | -50.13132 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1de52b14-13f7-39c0-8880-efd604914bf7 | -11.47534 | -46.6118 | 2026-08-12 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6b24f81-8752-39e7-ab20-ca4e750f59bb | -14.35849 | -53.64583 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dca3c7ab-31fb-318e-a366-d41adfdb936c | -14.98907 | -46.59363 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88d32418-e315-38e5-959f-cd49f5f01b64 | -14.35408 | -54.869 | 2026-08-12 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc42fc23-2ed1-3c92-9822-0a721338af8c | -14.97811 | -46.60704 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f56244ab-8e37-3888-80b4-018eff6cfa57 | -9.34315 | -47.50209 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23b03d0d-24de-372d-bf73-1c0c6afe9bc6 | -8.88335 | -50.17661 | 2026-08-12 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2c3cdb9-72e5-3443-b8f7-a99e58420194 | -11.80671 | -51.56332 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26a62178-e47b-38c7-9430-6fece8bd3545 | -14.33745 | -54.04525 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 10d0cb5d-f8f7-3d5c-ab22-8f591a026eab | -9.3467 | -47.50265 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6060eac-3941-3861-841e-5e3ae426c651 | -12.10436 | -47.19089 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f72ea25-37d5-336a-b0b7-d17e88bdfc05 | -12.61359 | -47.86508 | 2026-08-12 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5becd8e-e238-393f-90c2-20f3203e9945 | -11.95309 | -46.39213 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9024849f-157b-38e5-be2d-b5f55609f1f1 | -13.26808 | -49.65816 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c301eac9-578c-3ca9-ba21-a9ca4fe95e91 | -11.97962 | -46.40124 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 28ee420c-aa0c-3809-8216-a8f5efc793ee | -16.10184 | -49.8895 | 2026-08-12 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a0639198-8610-3d76-9d48-de80c4b00273 | -11.93379 | -47.35135 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45ca6e15-42de-343c-9dcc-f584476665b0 | -14.49555 | -49.30286 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ed73032-47ce-386f-bfc2-1ed749a6494a | -12.85744 | -52.0421 | 2026-08-12 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15daaef1-2893-3009-a497-3a44a5989d3c | -8.95664 | -60.50035 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99088d96-1dd8-3f6c-b358-53c637ea8e2b | -8.96161 | -60.50546 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05be5718-d919-3c56-8cfb-80d6d08fd9a1 | -11.4767 | -44.57164 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| aaf2e14a-16e0-3e9c-ac74-a2f459f27968 | -13.90003 | -53.81125 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f08fd5b8-ecf6-3020-92dc-5b5c6d132475 | -11.46915 | -44.56195 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd6b2798-b13a-3da7-b81d-1e3543b9dbd6 | -13.89929 | -53.79448 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4136425-b625-3c51-a2d8-7be3e76bc996 | -14.35828 | -53.0659 | 2026-08-12 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c65d8ae0-1969-3d06-89d9-5739765d64ee | -12.55635 | -48.34986 | 2026-08-12 04:51:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f41b3791-2118-3fe3-9cb6-d579a914b9ef | -11.82148 | -51.83339 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0251924d-3985-38b2-b2f0-01a1004ff5b5 | -11.60708 | -54.65834 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1c0700b-c230-3b54-9fc8-57c9cf218352 | -13.838 | -53.79316 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffd79109-1404-3327-a843-0d37fa328e1b | -13.57282 | -46.25243 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2c9abc4-25fc-36db-8126-f1ea70678e7d | -13.56328 | -47.64099 | 2026-08-12 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1de4a62-4279-3255-814e-5f9fa994343b | -10.84286 | -50.34781 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1801a86-8f00-398b-8e85-d3987e845f8e | -14.99572 | -46.605 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06e2124a-abf8-300e-ac79-f4b7317dd566 | -11.94702 | -46.35074 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 218d8ad3-a0af-32f4-9312-70dd57a12376 | -9.92331 | -48.67784 | 2026-08-12 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6720d3c4-76ef-31d8-b22a-a85deaed1b70 | -14.33677 | -54.04926 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b92a8c14-c6f5-3df2-8c9d-a6116552bcc3 | -12.60997 | -47.86452 | 2026-08-12 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1be5acb-2535-3c3c-ac24-8cc6a022821d | -13.85496 | -53.82089 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49e38696-4045-387c-b86c-52c0decbab2b | -11.46596 | -44.55287 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a935c6b-7be6-33a2-b4cb-5d5289dc7513 | -11.93251 | -47.36012 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd1c3574-5279-3e83-8730-11ccf94d3030 | -11.82685 | -51.85231 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67c3d872-de4e-3a6c-bc1b-121e10431beb | -9.62385 | -48.33096 | 2026-08-12 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cba60416-151f-3a99-aff7-7ce5c89dbc4f | -10.36931 | -46.38808 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bcf02ea4-f672-3ab4-9be1-d1063ee70e9b | -13.02313 | -40.34728 | 2026-08-12 04:51:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3249184a-2d7a-3166-bbb3-fb274315a562 | -14.53944 | -50.39429 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9de7a7b7-807c-3ff4-9590-48c5178c6868 | -10.87444 | -50.2556 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a34800c4-9718-39c5-bbe7-3ae981374da3 | -11.47234 | -44.57101 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b83c3974-caaf-3d88-bb8f-44f446fed2d0 | -11.97644 | -46.39565 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6594043f-7a7d-3ef7-a243-a7ce782f77de | -13.87196 | -53.76236 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b2dbb3e-1989-3d62-8935-be6e2307d3b8 | -11.98573 | -46.35864 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 197f484d-31d0-31bb-a7c7-2934c13a2a7d | -8.8978 | -60.55998 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a298b003-9130-3854-8033-8dec9531fe21 | -11.81201 | -51.82814 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 290fbfb7-860f-3772-9145-76a0b2fcf35a | -12.32362 | -53.18655 | 2026-08-12 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3e4d89c-0abb-3e9b-b574-7d670fcc01f2 | -14.28697 | -45.29016 | 2026-08-12 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d91016c-d28b-3682-b430-84a4332e28ee | -9.15955 | -48.83132 | 2026-08-12 04:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af1c6ce4-c9b4-3385-96be-75a3b15d2049 | -11.55474 | -50.23043 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
