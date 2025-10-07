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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a51d81ec-f3a7-3ce1-9386-6e4dbbf8d1a5 | -22.17833 | -49.37555 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 693cae94-7581-3c07-922a-e7a649fd3bdf | -22.18095 | -49.37142 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3e05222-cb01-3f18-9be9-5fc6682f7dac | -22.54724 | -44.45506 | 2025-10-07 05:01:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 067f73c9-7000-3be0-a8a9-ddb0724c8c82 | -22.78982 | -54.66846 | 2025-10-07 05:01:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d4de0597-8591-3d09-87ab-698b466c6f00 | -22.15253 | -49.38428 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c9bcd85-8045-3f85-b092-a6725c5fe54d | -22.31909 | -47.13348 | 2025-10-07 05:01:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5986d4f7-ae50-3beb-9c27-fb1d60deba5a | -22.17772 | -49.38125 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e9582ce7-ed2a-3afa-8530-d525d9a7c27a | -22.54713 | -44.98468 | 2025-10-07 05:01:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 95647321-aeac-36ea-aea2-5f8fcff947a7 | -22.1771 | -49.38689 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 755ffc78-102a-33e7-8a22-6b0ac7653f07 | -22.54683 | -44.46071 | 2025-10-07 05:01:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 84dad481-6b2b-3a1a-b1d1-0915fe12cda0 | -23.10466 | -46.18638 | 2025-10-07 05:01:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d23f9ef1-1214-3b51-b3ba-874b038336eb | -22.17979 | -49.38287 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c3097b04-e43a-3194-ab3f-8a26cbe1a726 | -22.94254 | -49.30013 | 2025-10-07 05:01:00 | NOAA-20 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3fa0084d-a7f1-335f-8e52-00c9adae3423 | -22.1519 | -49.3902 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98bbc98b-a2d0-3cc9-9b66-5ab7e8467012 | -22.55386 | -44.45631 | 2025-10-07 05:01:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 888b8d47-0d38-3ff3-9a78-55a236f4f492 | -22.78858 | -54.67746 | 2025-10-07 05:01:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9597fa47-5319-3b78-9f14-e2f4144c9361 | -22.54668 | -44.99047 | 2025-10-07 05:01:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 96723fbb-7811-3a7b-bf97-d54bd7e8827a | -22.54059 | -44.45414 | 2025-10-07 05:01:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0eb9182d-cb1e-3c94-a514-68da50b7905c | -22.7892 | -54.67296 | 2025-10-07 05:01:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c4e9e346-ec14-343b-90b2-ec0e0f2e3b61 | -22.15806 | -49.37905 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5aa3c7ec-b746-36e6-a099-4426f67a6877 | -22.7856 | -54.67239 | 2025-10-07 05:01:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5226c5db-ac9c-32ec-9cd1-56b58c351c8e | -22.17922 | -49.38854 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8cce84c2-935f-364e-b3b4-9cdde6b72551 | -22.55427 | -44.45067 | 2025-10-07 05:01:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a8719a25-928f-397a-963b-6864186ab3fe | -22.15743 | -49.38492 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58506366-df9f-3dba-8c13-f2fadcec6dbc | -22.78622 | -54.66788 | 2025-10-07 05:01:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a4c1103f-8eb3-3f4d-a398-b03dfd9415f2 | -22.54018 | -44.99026 | 2025-10-07 05:01:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6560f05f-189a-3d47-bea2-800efde08e29 | -22.54018 | -44.4598 | 2025-10-07 05:01:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a31c0615-bd30-353d-b3a5-d495f37f1800 | -22.52579 | -49.11144 | 2025-10-07 05:01:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d50fcf-a4db-3026-8095-2f80d2b6f08e | -22.66926 | -49.19774 | 2025-10-07 05:01:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9087177-c490-3918-8b4f-81b4cad99f27 | -22.54763 | -44.44965 | 2025-10-07 05:01:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2dbd8b96-cc44-3abf-92df-dc9ad28141b4 | -22.7928 | -54.67354 | 2025-10-07 05:01:00 | NOAA-20 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 094d2f6b-d05c-30df-81a4-7aa998bd942c | -22.17649 | -49.3926 | 2025-10-07 05:01:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 877da73a-4109-35a4-9e1f-d20ff03f8a9b | -23.09858 | -46.18592 | 2025-10-07 05:01:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 02125741-8cb7-3d95-885d-ae30db54af7d | -1.09077 | -53.70306 | 2025-10-07 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 670db4f3-d8f2-32b9-bf79-a938cd75b605 | 4.50179 | -60.17283 | 2025-10-07 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97570cf3-5e3b-3134-ac30-ca29e22d5fcc | -1.08434 | -53.70214 | 2025-10-07 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd6e31ed-2a86-3a21-b03b-7fb48f984a37 | -1.34086 | -55.4726 | 2025-10-07 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ff345b-45bf-3a63-9151-d37b803b50ba | 4.50106 | -60.17508 | 2025-10-07 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5e3f664-62ad-3c53-8ee1-0014d72a730c | -7.13751 | -63.12764 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9439910-d4eb-3490-85da-41747a49506d | -6.70023 | -62.83715 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c8c991-251a-3abd-afa4-39b3bcc17516 | -4.56887 | -55.96192 | 2025-10-07 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 325664b2-9c36-302a-9eb1-ba79f01d0c94 | -8.61947 | -54.97131 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05748409-b698-30d4-880f-cc8218aaa354 | -7.46174 | -63.61943 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b73f12f1-fc07-3dc2-8644-d98f59f9778c | -6.69193 | -62.84069 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0313dee-2b66-3ed8-b217-7efaa50afd34 | -8.62206 | -54.96102 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a116e0d-cba7-3f7c-b0ce-8a283428d46e | -6.58258 | -62.95249 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f2843a8-15ac-3fc5-a612-e48a0eba785e | -7.68455 | -61.06151 | 2025-10-07 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 168a315d-1893-355a-bce8-c5969d45517b | -8.62065 | -54.97218 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b2ce26a3-1bc5-3f1e-8452-0cff68a17a62 | -5.09927 | -56.15612 | 2025-10-07 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 607d81cc-2600-342f-a3f8-18a556149e26 | -7.49513 | -63.67329 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92485592-a5ce-3af3-9663-dfc616cf4e6d | -6.84434 | -62.88259 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f393dc9-b0a7-3a00-b13e-e0f33040ce10 | -6.70333 | -62.8424 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe254af7-b6b8-349f-b988-78a1b44b735a | -6.97051 | -63.05066 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1181722a-74fd-36a0-84b4-0bb86cb6c9df | -7.35975 | -64.65686 | 2025-10-07 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c06ae263-0306-3b0d-880c-6cd4502fe6f2 | -7.62149 | -61.35176 | 2025-10-07 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f526180-962c-3285-b397-c9fb7c32cfd8 | -7.46542 | -63.61998 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e008b568-0d48-3bc7-b214-2e7a8d791f62 | -6.6198 | -62.88233 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02e393a5-037f-3b47-9775-b53932778133 | -7.48228 | -63.55553 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20ae85b2-4bfe-3c53-8748-592735ff41fa | -7.48101 | -63.56432 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2110e0cc-03b2-37e0-908a-ff59e41ff002 | -7.47707 | -63.61728 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 301bc4c6-3912-3623-912b-411a383835a9 | -6.7483 | -63.06002 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c293b59d-0b60-30ba-b08b-0ad7bdc49cfa | -7.51443 | -63.43837 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 792e41bf-a2e6-34a1-b7c2-496980fa130c | -7.41474 | -63.03224 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3210d3d1-8878-3d14-abfc-ccb968d10cf0 | -7.47831 | -63.73685 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c514c015-6656-34d1-a7d6-2435d6f397ff | -6.62427 | -62.87824 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3595b91-3313-329e-8511-94f481aef389 | -8.62136 | -54.9666 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 630cd7e4-161d-37fa-b997-563d6980dc08 | -6.86419 | -59.96864 | 2025-10-07 05:48:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fca4d85-11f7-3e3c-8050-8cf2bbdef424 | -8.53371 | -54.86187 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ea033c5-376c-3ae0-a3fd-588939a85c8d | -6.96742 | -63.04549 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 584d4eed-2549-3e14-8a9d-018ab9fa51be | -7.61781 | -61.34715 | 2025-10-07 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 282ab59e-2a32-33b8-8a8a-5048ddeb4e5f | -6.73906 | -63.04465 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c28a4be8-ef2b-3077-ac99-718b37c05f5f | -6.74455 | -63.05946 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9577051-5d61-3e05-a05b-5d13fe05c864 | -7.60965 | -63.37234 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 065436ed-c06f-3d46-b05c-ee33166d1e20 | -2.70817 | -59.68501 | 2025-10-07 05:48:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75ec6984-495b-3531-9cee-5332da26ccfd | -7.62205 | -61.3478 | 2025-10-07 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05cc907f-59f3-32e2-b60c-82b2237a258c | -7.46254 | -63.61713 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee37b7b4-5be9-36d8-974d-d149a1705810 | -6.73944 | -63.06801 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 748a8794-b66d-3517-ac38-d7f9e868db24 | -6.74011 | -63.06345 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42a52a0d-64b9-3289-a383-efc7cda42de2 | -7.46621 | -63.61767 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 099d2d81-aaf2-3ade-8a20-2d0fd07fe8c3 | -7.63342 | -63.44468 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 757ba775-2170-3730-8f00-94a090f7d485 | -7.51508 | -63.43391 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67716a93-04e0-3e90-ac20-65801c178126 | -7.61725 | -61.35113 | 2025-10-07 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a84e0ebd-938f-358c-82af-398c6f27626d | -7.06421 | -63.02028 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dec54b3-6f4f-3ca0-8a44-dd69f686eb3c | -6.58163 | -62.95519 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cd5b486-f7f9-3e12-90b7-088803f43b0a | -6.70404 | -62.83771 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7adc2e20-b15b-3ead-accd-e5f95c625312 | -6.82349 | -63.07795 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06a1fcc5-a58c-3992-a0f6-7bddb1d3d285 | -7.41543 | -63.02756 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd89fef5-ff10-3380-a2c7-d607bede8ea2 | -7.46605 | -63.6156 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21e6e689-a494-3b0f-9ed6-d5f12fdba7c2 | -6.69573 | -62.84126 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68aa9b32-88c6-30e9-8511-ab7a46c3f87c | -7.27666 | -64.65307 | 2025-10-07 05:48:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8558fa09-ce86-35bd-aa1f-8233eb97de4b | -7.48164 | -63.55993 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d0e297d-7431-3f5b-bfd1-77305432bcee | -4.56948 | -55.9577 | 2025-10-07 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7c95da5-faca-36e4-8bd0-6be27dd6531d | -7.49576 | -63.66897 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2778fac-6378-3b7f-87b9-95e5fe5278eb | -7.80727 | -61.50518 | 2025-10-07 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21db2073-29b7-38e7-b754-6538946389b0 | -8.62013 | -54.96574 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf982bcd-12a3-35b9-bf87-d45bbc5dc613 | -8.11028 | -55.08007 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0df9e2af-02f7-3dd3-a473-887e36a12dab | -6.69953 | -62.84182 | 2025-10-07 05:48:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef6613c9-4d11-35ea-bbc8-0c4fad8a253a | -8.10404 | -55.0809 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68b141ac-43a3-3e0b-83dc-3f7578912bc7 | -6.62987 | -56.2798 | 2025-10-07 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e458adef-fa39-3117-99b6-9485cf519d68 | -8.10381 | -55.07904 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README105.md)
