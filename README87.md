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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41e4f7b2-1003-335c-9ed2-97a8725deace | -10.9159 | -50.6632 | 2026-09-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| bcbbca1f-4d95-3b15-8a44-40ba2be3acaf | -11.8802 | -50.8977 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 12391c30-84ea-3770-9366-c9102df4194f | -11.8618 | -50.8572 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| dea42f13-3d91-325c-a645-f745016292a5 | -11.5625 | -50.5283 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 6b445711-591e-3629-9915-c6aa2fec9fdf | -9.977 | -50.248 | 2026-09-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| ed2b6f6b-ce66-331d-adcb-1914ed61ce34 | -10.1095 | -50.2135 | 2026-09-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| f18ed978-7eba-3578-afe0-af0d6584bac8 | -11.5628 | -50.5069 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0184548d-110a-30aa-bed3-e74ad4558015 | -11.7828 | -51.0578 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| d2b1c79a-653b-3e6a-9adc-f84af2c1ba2c | -10.9156 | -50.6845 | 2026-09-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b7105f70-6d38-33e8-adff-67ddf96e158b | -12.0694 | -48.5377 | 2026-09-29 15:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 09b3c29e-7a55-37af-91f0-3e40b6b5ef4e | -11.152 | -50.0388 | 2026-09-29 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| bf85a017-e95f-31fa-bebd-48ccd9756694 | 1.8587 | -55.5846 | 2026-09-29 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 9158a5ac-be8d-3b10-913e-91800adbf1f6 | -12.2696 | -50.3381 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 208f6558-30bd-305e-b8d4-f88cc40d32ad | -9.9781 | -50.1626 | 2026-09-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c01d50fd-6591-3618-ac39-f6bb3a73ce38 | -10.2067 | -49.9898 | 2026-09-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 20e097fe-9a5b-36c3-a0b0-22ff1244fc71 | -12.2897 | -50.2712 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| bf956094-815e-3b10-a763-c18406ef5801 | -9.4813 | -46.3646 | 2026-09-29 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 395dff19-86df-33e6-ab7a-337857b20bbc | 3.6383 | -61.1343 | 2026-09-29 15:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 9bad3992-3d32-3bd8-906a-265ac0c9e321 | -20.9159 | -57.8246 | 2026-09-29 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 139.9 |
| 8205390a-d3a7-3b56-a785-15f47353a407 | -11.7319 | -50.6373 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| a9a6aee8-87f6-3e48-b2d4-e783dd3db79d | -12.3488 | -50.1563 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d9891d91-f1ed-336b-a959-a6d54c90b30a | -11.7129 | -50.6394 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| aaca17b1-4c99-3958-998b-e7c1236cc40c | -11.8097 | -50.5214 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ffc51540-0dac-3146-9a09-fe83e7626e4f | -11.8675 | -50.4718 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3adc0c6a-a167-3af9-8f0c-4778ac58a921 | -11.7643 | -51.0173 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 19fa85a1-67d6-3506-ad7e-3f8ee46e5f1d | -12.3088 | -50.2688 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ad0eaa30-f61e-333d-9033-fefa8c15fdc1 | -11.8608 | -50.9212 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| aa908ef5-f83c-30ae-937f-f8a0934e9b48 | -10.9533 | -50.7018 | 2026-09-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 50a73e8b-48ad-3587-88b2-1fa0f5db079b | -11.8611 | -50.8999 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| f29fb889-0bd4-3ce9-84ff-bb1f1cd318a3 | -11.7887 | -50.6521 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6c63bb36-1c42-3c3e-a405-870e7c226a8c | -12.1741 | -50.3497 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| c3ab2d59-ac42-39c7-8a69-47d9ecba9eb4 | -11.7126 | -50.6608 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ed1891d6-bf17-3241-b223-43d4c3c5ec9b | -20.817 | -57.6919 | 2026-09-29 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 131.9 |
| 098f94f5-d7c8-3d86-885b-6239c8673385 | -12.0129 | -50.9251 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| a5c2b534-0d2e-36bd-a220-458699f42f1c | -15.3998 | -47.9261 | 2026-09-29 15:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| fd2d8036-42a4-39d9-ac33-45163117f509 | -11.8866 | -50.4696 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8308ecbe-ad15-3cfb-81d2-99eafc973f6c | -1.4672 | -48.931 | 2026-09-29 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 824c06fc-0006-3996-b248-53f618fd9882 | -11.7647 | -50.996 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 32fd6625-6b49-39c3-9816-6f249e25d9f8 | -12.2699 | -50.3166 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a8c03fe2-6d15-34e9-950b-f4eb75692884 | -11.7697 | -50.6543 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| df569d2f-a745-3c9c-8127-53f18b41a4da | -11.8859 | -50.5125 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| cdb308fc-a28c-3164-9764-69163c16b887 | -1.3193 | -49.061 | 2026-09-29 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 461836ca-128f-31a8-a3f8-d696b7760e65 | 1.8587 | -55.5648 | 2026-09-29 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 5e5f32e8-a5b2-3fa9-a76f-d86d9776cca2 | 1.9241 | -50.8202 | 2026-09-29 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b15e9bba-541f-3f42-9be3-979995b98a58 | -10.9154 | -50.7059 | 2026-09-29 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9f3dddc6-a9c2-333e-92b6-418f0a7f2497 | -10.2065 | -50.0113 | 2026-09-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 018beabf-eaa0-36db-8dac-728eacee3e28 | -12.289 | -50.3143 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f0744437-6aa4-3e17-9a54-01be7a53778d | -6.9795 | -71.7732 | 2026-09-29 15:40:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 585.0 |
| 92762ed7-62e4-3895-91ed-f7f301e2bff7 | -10.2254 | -50.0093 | 2026-09-29 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6315e283-9654-393b-a539-f3e67419862c | -11.8614 | -50.8785 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 10ca0039-7939-3291-a72d-a8f1bfc2535f | 1.9425 | -50.8199 | 2026-09-29 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c4d7a172-84a5-3b9c-aea9-895980cd7bdd | -17.3145 | -42.69698 | 2026-09-29 15:44:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 6ad56e15-f3cf-3c92-8455-cbe41a4dc93e | -17.24 | -40.77499 | 2026-09-29 15:44:00 | NPP-375 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 05ac7da6-a2b4-34da-b23f-a0fa2088367f | -16.90934 | -42.10861 | 2026-09-29 15:44:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c2531535-38f2-341c-932b-5103b250a2f8 | -15.95187 | -39.94165 | 2026-09-29 15:44:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 24110cd3-00dd-3bec-a309-38ce4538f264 | -16.35355 | -42.58075 | 2026-09-29 15:44:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| cfa998bd-9efe-3214-b316-b0bae8ae5ce6 | -17.81818 | -42.58113 | 2026-09-29 15:44:00 | NPP-375 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 9bdd4310-01ab-3fe6-9185-def541c01ad9 | -18.38276 | -41.97542 | 2026-09-29 15:44:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4ed52c03-31ec-36f1-ab74-13e90cf68a36 | -16.35398 | -42.58939 | 2026-09-29 15:44:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c7113b3a-e92c-3923-b60c-8522d0b06cc4 | -18.35262 | -40.03477 | 2026-09-29 15:44:00 | NPP-375 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5f3cd1f7-e846-3831-a348-9c31ddbca411 | -16.627 | -40.58477 | 2026-09-29 15:44:00 | NPP-375 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 58c9ead9-5c39-33e7-8d72-93ba5d56e74d | -16.16323 | -42.85762 | 2026-09-29 15:44:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2649804c-b457-3ed2-9c5c-1dbcdcf9729c | -15.98991 | -40.70687 | 2026-09-29 15:44:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 27282dd7-c765-3de3-b256-11a7795e13af | -16.35418 | -42.58773 | 2026-09-29 15:44:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b278e90d-693a-3ec2-a6b8-e4b6a8c8c311 | -16.35948 | -42.57446 | 2026-09-29 15:44:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 286f7b26-e740-3075-a7e6-d2f365d5353a | -19.3606 | -41.50224 | 2026-09-29 15:44:00 | NPP-375 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 9091ba7c-2b42-3874-8560-9d7fd176a30e | -17.29011 | -42.4856 | 2026-09-29 15:44:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c66d4948-ef16-35bd-8493-ef96599dac78 | -16.35332 | -42.58263 | 2026-09-29 15:44:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9605d528-1f0e-30d1-858e-9bff5a172250 | -17.81314 | -42.58942 | 2026-09-29 15:44:00 | NPP-375 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 5a1f1a83-cff2-3fc7-8105-092979476b3d | -16.20349 | -41.40689 | 2026-09-29 15:44:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d7973c5d-361c-3634-95e3-f739ebf2ac35 | -16.40331 | -39.45345 | 2026-09-29 15:44:00 | NPP-375 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0469bade-2921-3f72-bec7-e15e457f0c01 | -17.81247 | -42.58193 | 2026-09-29 15:44:00 | NPP-375 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 996af502-f061-347a-b176-50ebe756ec8c | -18.92811 | -41.0828 | 2026-09-29 15:44:00 | NPP-375 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8547fe78-9627-3eee-a91e-3b99c8bc3af2 | -17.3215 | -42.69629 | 2026-09-29 15:44:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e1296100-67e4-36a6-9796-e5cb173d4677 | -17.31512 | -42.70415 | 2026-09-29 15:44:00 | NPP-375 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 53.7 |
| db513e44-954f-3b4b-871e-713f91be986e | -17.31638 | -42.69188 | 2026-09-29 15:44:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b6a9f5a0-fb48-3391-8a06-e8616eeec467 | -17.81112 | -42.58107 | 2026-09-29 15:44:00 | NPP-375 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 8020325c-3849-3de9-9320-234a1c4b7b1e | -21.05636 | -42.69856 | 2026-09-29 15:44:00 | NPP-375 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8de0b740-9979-3e63-859b-cbd06022b4fa | -16.0956 | -39.07161 | 2026-09-29 15:44:00 | NPP-375 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 67dbbebc-0ef8-3369-8246-3f004ac53424 | -17.23775 | -40.77283 | 2026-09-29 15:44:00 | NPP-375 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 563cd8b7-6cd2-3a61-9058-b243c6f87df4 | -15.95233 | -39.94593 | 2026-09-29 15:44:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ca8e1b46-b4a6-3664-b233-ada860277d7b | -18.92773 | -41.08227 | 2026-09-29 15:44:00 | NPP-375 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3537f2ad-166e-3022-a0d6-d100687f0c9a | -17.21926 | -39.29324 | 2026-09-29 15:44:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d4c932c9-28a2-3d9e-95ea-8f1adaadd773 | -16.67467 | -41.86878 | 2026-09-29 15:44:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d5c5f2a4-e40e-314e-94ba-78e3adc9abba | -16.76118 | -41.20811 | 2026-09-29 15:44:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 051b7541-1b01-3371-87f3-94f730831fc3 | -19.36109 | -41.50824 | 2026-09-29 15:44:00 | NPP-375 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f203a672-9534-329e-a7f1-623a69ceaaaf | -19.23352 | -40.27274 | 2026-09-29 15:44:00 | NPP-375 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b4a5f5db-8ee3-30ab-882e-0da1b897e0f0 | -18.38447 | -41.97299 | 2026-09-29 15:44:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d369f5dc-d2fc-3e9d-8b48-569af92016c6 | -16.36038 | -42.5794 | 2026-09-29 15:44:00 | NPP-375 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8a542f0f-e574-3da0-b27c-fe854f762622 | -8.21824 | -36.29428 | 2026-09-29 15:46:00 | NPP-375 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d3919119-e36e-3bd2-aaad-a5963275e40a | -14.71093 | -41.31003 | 2026-09-29 15:46:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 02cff260-c25f-3b7e-a321-bbe907fddbe1 | -9.98794 | -39.15988 | 2026-09-29 15:46:00 | NPP-375 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f3751a90-3cfe-31a6-9466-61c1509c52f3 | -11.41767 | -43.42487 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| cf4870f1-caa2-309f-84a5-8c56661a4bca | -9.05985 | -45.00745 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 45a3c7ee-ef41-3300-8919-d504e43afd62 | -14.60289 | -40.76817 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 11f3fe09-3754-3b83-9c81-d98ca1370142 | -15.23518 | -41.74399 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| 764dbb11-bed6-3163-ab53-acf53bd8222c | -9.43863 | -41.82507 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 121.5 |
| f75e8eef-f5d7-3473-a1d2-9ac920620d38 | -15.21241 | -39.78334 | 2026-09-29 15:46:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 97cdc417-c829-3c01-ab06-7ddb7e449fce | -11.14546 | -40.30307 | 2026-09-29 15:46:00 | NPP-375 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3c2896f7-4e11-3465-8a56-feba1d346445 | -9.06633 | -45.00806 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README88.md)
