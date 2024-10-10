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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d060de27-ab77-36ec-a7a8-8772d4410b6e | -6.52243 | -58.39941 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc3884ff-6c8f-314c-9c7b-459bed4cc7c2 | -6.52157 | -58.40435 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07c38913-39c3-30a7-8d92-e9e111a8ab43 | -6.52069 | -58.40938 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f62de05-da8a-3aab-bf4d-3cde5d5b7c94 | -6.51599 | -58.40848 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1066b38-993e-3c43-be10-f26f79bb5a56 | -6.51505 | -58.40655 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8da3e40-e203-35d5-9f39-d166b790157a | -6.51422 | -58.41148 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25c1c1b2-9ea1-385e-807c-12f7444a6d2d | -6.51129 | -58.40762 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 553e9955-bbc4-3f90-a7b0-12bf50839262 | -6.48165 | -58.43182 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc96bf40-9fd8-3a65-b37a-2421ce2f2484 | -6.48077 | -58.43701 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc1e7862-9166-33d1-90c2-4b54ce13304c | -6.47989 | -58.44223 | 2024-10-10 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec98b0d6-15a9-3be1-adb4-8d12152c5e03 | -6.92134 | -57.77716 | 2024-10-10 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a062609f-ee91-3399-8937-9b143273d8f0 | -6.91685 | -57.7764 | 2024-10-10 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc2f4de8-9d88-3871-b4f1-a2a57dc9c2f4 | -6.81604 | -59.03755 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4593c137-d5f3-3e98-870e-75028e2f3d32 | -6.80889 | -58.99102 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18979c0c-55b5-33b2-8acc-092b07acc892 | -9.22066 | -58.92371 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 916615ed-4375-39ac-b1fd-15e568b17f96 | -9.18692 | -58.89677 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed06f5da-7993-3bae-b410-6fe4c0f89375 | -9.18227 | -58.89586 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 942181f3-137e-3720-940c-7c5ac795d844 | -9.1218 | -59.01795 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5cd3085-5861-3c53-9b39-55b77c1e25c3 | -9.05223 | -58.96293 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec41b260-62c9-36ae-878c-128581cef3d4 | -8.80634 | -58.20113 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d94bb83-e45a-3758-96da-235d96d608b6 | -8.80363 | -58.20221 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fd44092-1ae1-367e-b7d0-43a60f12b3c5 | -8.11649 | -58.04096 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1522cda1-1f29-38f7-a015-2370bc6e5a44 | -8.11568 | -58.04556 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be640299-9134-3f12-b52e-90965e82d9b3 | -8.11201 | -58.04016 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5fb91d58-c498-38b0-8d57-eeb1b56763d1 | -8.11119 | -58.04484 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1243c6b8-3b2b-3efb-b290-2e26f90baf11 | -8.10753 | -58.03942 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8d39e5b-58b4-39ef-bf28-23e6bc41b950 | -8.10671 | -58.04409 | 2024-10-10 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29edabf2-73f0-3777-9f7c-db5f77f26784 | -9.89112 | -59.50639 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 905e1f46-f165-3a3d-881a-9a3650858a2d | -9.89019 | -59.51163 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35d49bbd-a474-3ad8-a45d-74b878a044da | -9.90751 | -58.68625 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83470995-e06a-3837-a8d2-7ab8a29a646c | -9.89045 | -59.50725 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76727011-cc38-369d-87b3-e490cb87430e | -9.54825 | -58.9629 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 089a62f8-f528-3f74-b8de-6b1568e97942 | -9.54687 | -58.96022 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2758f3c5-7bd4-3772-b12c-9aa876f96ca5 | -9.54359 | -58.96212 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3e7ef8d-632a-3e12-a14e-7060db298fbd | -9.54221 | -58.95948 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77f91f57-3ee2-300f-b42a-0ddedb683e93 | -9.46881 | -59.03122 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b87cd56-e06b-3d84-8766-ff5097bc6b18 | -9.46413 | -59.03041 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b3d6d41-33de-323c-ac40-93419a374a4b | -9.44717 | -58.94959 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c446e17-7c38-3f6b-b472-61157798178c | -9.44588 | -58.94477 | 2024-10-10 04:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d82de75d-848a-317f-aef9-d043661a7793 | -9.44497 | -58.94976 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 470088ce-533d-377a-b015-04e429b3a195 | -9.44251 | -58.94877 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43ec5072-4c91-3f25-b7e0-bcde674fc57c | -10.40872 | -59.15291 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ea78a00-2417-3c71-bd1f-d9e9a805fcd9 | -10.40497 | -59.14717 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 793bd7cf-1ea9-3f9d-a7f5-a72f8763c4f9 | -10.40408 | -59.15204 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b344d54e-dcc3-3538-8fd0-8d7cf1f4a6cb | -10.40211 | -59.13661 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee7e30e8-cbe0-3ed9-aff5-5cc598cb2b9f | -10.40032 | -59.14639 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0d7e398-5f18-352a-9c27-a933022c416b | -10.39943 | -59.15127 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fcac96b0-29c1-3144-931e-69906cce24fb | -10.39567 | -59.14561 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c99b0087-ec10-3b21-bce7-fc7369755111 | -10.39477 | -59.15051 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e72c2f4-960c-31ec-ac0c-c2679ea8886f | -10.12458 | -59.00312 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8183f546-4522-3bc4-9024-0334cc4ab83c | -10.0606 | -59.35744 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5dfb9052-54fe-3af3-82e1-0e8f16d4e920 | -3.20676 | -59.37815 | 2024-10-10 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16f05a33-34d4-3fbe-9a69-3086d149e164 | -3.20622 | -59.38145 | 2024-10-10 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17eaab3f-28bb-381d-b104-9890bfa3c26f | -3.205 | -59.37883 | 2024-10-10 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dbbdd93-6a4a-3f24-ad58-dfbc23a6a410 | -3.20443 | -59.38216 | 2024-10-10 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1916c66-fdd2-3293-b4c9-3e5b2dc14710 | -3.14307 | -59.10899 | 2024-10-10 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd2d2d6-834f-3f1e-b7a5-d54244093ed0 | -3.01515 | -59.10051 | 2024-10-10 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 004ec3d2-58fe-32fb-aadc-2ede8d93fac8 | -3.01462 | -59.10372 | 2024-10-10 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1646eb91-1473-37f3-9dc2-774b92237ae1 | -3.00832 | -59.10933 | 2024-10-10 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f2688df-195f-3cde-ba86-6af997569725 | -3.00779 | -59.11256 | 2024-10-10 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bc33322-ec8b-3eef-aa50-9c0226d2ea50 | -4.52647 | -59.90255 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 265461fc-84ab-3bc6-abf2-43c630edefe4 | -4.52471 | -59.90066 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cef8161-861b-3d15-9a54-b1b08b6a401e | -4.52414 | -59.90411 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fad26ba2-339b-372c-b35c-6371a61b87ff | -4.52108 | -59.90161 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d82d8313-a03d-3f19-9909-f9f558dc6093 | -4.37683 | -59.94135 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2b1ffc3-f1bb-3569-a55d-98be0406ca20 | -4.37623 | -59.9449 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90192e01-e1b2-3f48-a2e7-faa1b8c02720 | -4.29118 | -60.01665 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00fed4d7-7cb0-3f2b-b411-507f664effc8 | -4.29057 | -60.02016 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 294971c4-22fa-3154-8212-65a74d29feac | -4.29033 | -60.01685 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99bd0c33-80ba-3039-ba31-23721516de07 | -4.28975 | -60.02037 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b494946-dbdc-3540-990d-afb44f05ef3e | -4.28573 | -60.01572 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 613efa03-a02f-389f-a774-729d444586b3 | -4.28488 | -60.01591 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfb2efa9-c06c-367b-b1b3-86216d373ae0 | -4.26742 | -59.88657 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45338f9e-1135-3a62-ab20-97262a2d12de | -4.26683 | -59.89006 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa4258e-32c3-3f98-a280-81d4d6ab3249 | -4.26624 | -59.89355 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e6272d8-1cd6-3bd2-8daf-53f23416757a | -4.26141 | -59.88914 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efca6658-98cf-334d-bcb0-d72d26d2a028 | -4.26023 | -59.89612 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6a7a0d0-be15-3f18-86ab-73dc5c05e88e | -4.25455 | -59.99597 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 287fb3f6-87f7-3f43-9d77-eb95f77ace77 | -4.25395 | -59.9995 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74623924-d263-30b5-8c8c-3ffc9d8555db | -4.25335 | -60.00304 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e467bab-d68a-304b-adf2-f58b9659cc4e | -4.2491 | -59.99502 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83eac599-95e4-371b-b2aa-78b15f240125 | -4.2485 | -59.99855 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d3fc4e8-32b1-38a4-b6a1-ddaaf32ae0db | -4.22593 | -59.86868 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b571d78a-4c61-3643-b73f-ae44b49d6b04 | -4.22533 | -59.87215 | 2024-10-10 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ed420d7-28a2-35c9-95f5-a3cc45da0869 | -4.21034 | -59.99195 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28ad91d3-5c68-35b3-bfbb-d73ad62afa54 | -4.20973 | -59.99546 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4291e90-5b2c-3778-89e2-02aac0465b24 | -4.20488 | -59.99104 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a53a74b-4e5d-375b-9830-c076df6c4d9e | -4.20428 | -59.9945 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4db30522-18e9-39b9-8d69-b48a282b7813 | -4.20368 | -59.998 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 824b9816-6ee1-3121-bced-ee611adcb4de | -4.15595 | -59.94198 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4c9675f-3d2b-3a3b-9b43-6c38b4d5902d | -4.15537 | -59.94547 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc003c08-43ac-3013-a2f4-66b07cee362e | -3.96243 | -59.16957 | 2024-10-10 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 497b260e-32dc-3d94-b8e0-6057d579dff0 | -3.9619 | -59.1727 | 2024-10-10 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd7969cc-de59-3c06-8d37-15abb88d342e | -3.89514 | -58.80027 | 2024-10-10 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de14a63b-d1c3-3a00-8121-96be1b385073 | -3.89465 | -58.80318 | 2024-10-10 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a22e0e4-e2a1-315f-83e2-55fa98dddc59 | -3.88959 | -58.80234 | 2024-10-10 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f9a5821-2ef7-3bdd-a4f6-f0a53ae27f2b | -3.8891 | -58.80526 | 2024-10-10 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50ab52f5-5156-3140-a32b-6b4beb45ef47 | -3.6148 | -59.79578 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb7498bc-71f6-389a-bd5d-19b000608350 | -3.61421 | -59.79929 | 2024-10-10 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 230858de-2111-3bd5-a667-51fbda4f8f32 | -5.29616 | -60.10237 | 2024-10-10 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README115.md)
