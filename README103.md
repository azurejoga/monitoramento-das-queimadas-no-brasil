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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43cfc346-ffd8-3d7e-8f0e-3fbe56e4c480 | -8.5398 | -46.2181 | 2025-10-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8947bb39-d0a3-350f-ab6f-12ccc5be8578 | -13.2825 | -47.1655 | 2025-10-08 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e62c977e-a1d2-360f-81d8-2fb7937dbe82 | -8.2266 | -44.1548 | 2025-10-08 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 1b68bcfd-c622-3035-9f25-aac061f551d7 | -12.7825 | -50.5112 | 2025-10-08 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 789bf09a-f6e2-3f15-8277-a2d0eea0a7cb | -8.6106 | -45.102 | 2025-10-08 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 5208b437-abad-3948-bde4-da33f5876051 | -8.2263 | -44.178 | 2025-10-08 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 228.0 |
| 9f1fa68b-70e3-387e-9f2e-5973767c1f45 | -13.3018 | -47.1626 | 2025-10-08 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| d2caa107-d49a-313e-978e-843a336579b8 | -8.5602 | -44.6264 | 2025-10-08 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6ce0a68d-0542-3f91-b07e-2541a7cc8865 | -8.1804 | -43.3445 | 2025-10-08 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| c4e31102-e75c-3d44-ab07-f2fab1cec629 | -13.8117 | -45.7826 | 2025-10-08 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 308691b4-f89c-3655-9069-e252747ab7e8 | -8.9309 | -46.5809 | 2025-10-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 7d0cb1e9-1c4d-39f8-a288-95657f3d2800 | -14.3889 | -46.0063 | 2025-10-08 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 175.6 |
| fbc00b8c-43d7-39d2-a3c0-2b264bdf9f9e | -14.211 | -43.4573 | 2025-10-08 13:10:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 4726ea4d-84eb-3df2-9150-1a1a02240abd | -13.7918 | -45.809 | 2025-10-08 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| a4e60f8e-62c8-39e4-8970-45a058bf3b1b | -15.6198 | -52.5715 | 2025-10-08 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 73744417-8983-35e1-bd43-04c3213730a9 | -8.8621 | -46.0724 | 2025-10-08 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 2e3e41fa-5ae6-3f97-9af3-40039ec63f8e | -8.8807 | -46.0929 | 2025-10-08 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e6059fed-71dc-3680-bd2c-f2239129dab1 | -8.5016 | -46.2669 | 2025-10-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 346.5 |
| fd5cc9ff-21b1-342a-ad2e-0e62e8d781f3 | -8.5207 | -46.2425 | 2025-10-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 484.4 |
| 158714b7-e6a6-3264-873d-228594c57158 | -13.2434 | -47.194 | 2025-10-08 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 40f8f595-d3f4-3739-9600-f6ab2001d346 | -13.3245 | -48.0101 | 2025-10-08 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 3d059215-3579-31d7-aab6-79c05569cf32 | -12.2525 | -47.8728 | 2025-10-08 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| dbc2b953-87d6-3bf0-8d3f-3e165893d21a | -12.4262 | -45.6366 | 2025-10-08 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 363.2 |
| c3c2d193-50b5-34be-b95c-768646b6aef7 | -13.7368 | -45.6569 | 2025-10-08 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| e535251a-02a4-3be4-9024-efb308a27c3a | -8.2449 | -44.1991 | 2025-10-08 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 0febb205-fba6-3ba2-add2-b9a868305726 | -12.1083 | -50.914 | 2025-10-08 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a7c1f1f6-2c80-37b0-bd1e-85407f23c42a | -12.1274 | -50.9118 | 2025-10-08 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0deb889f-572b-35f3-9eff-8883e6b79241 | -8.1807 | -43.321 | 2025-10-08 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| 0cca064b-0d54-34e3-bb4a-beedb2f9ee56 | -8.691 | -44.727 | 2025-10-08 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 688d6ca1-a200-30ae-8f31-9a6f4a27c46d | -13.2662 | -48.0409 | 2025-10-08 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 38db812a-dfa2-342e-bf71-8c36d49323a5 | -14.7184 | -46.0636 | 2025-10-08 13:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 713d6399-97a4-3e0c-ab57-7be453183dd9 | -12.0122 | -45.1929 | 2025-10-08 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 97a7b75f-7287-3c39-8e30-b8c0368a48cb | -13.7364 | -45.68 | 2025-10-08 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 593.3 |
| 5e697837-5de1-3f0f-bdfa-5a02df24033c | -14.3884 | -46.0294 | 2025-10-08 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 0b01d3d0-add1-3565-862a-066bbeb2cd82 | -15.6393 | -52.5688 | 2025-10-08 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 187.9 |
| b1a09c0d-8277-3fb1-9228-1041838fd672 | -8.1993 | -43.3424 | 2025-10-08 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 166.6 |
| 9e45ae61-b135-37c9-88ba-a16c66f35c87 | -13.8112 | -45.8057 | 2025-10-08 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 615f1b15-74c5-3de4-807d-c7028fd35593 | -13.2438 | -47.1714 | 2025-10-08 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cad088c6-5777-30f7-abad-00db29b279f9 | -17.954 | -44.4124 | 2025-10-08 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 119.0 |
| e38c8d22-b941-3d60-9fd1-b6e2dc5f4467 | -12.4267 | -45.6136 | 2025-10-08 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 357.7 |
| 7ea6cc9b-ee5a-30ee-9244-450497ae6909 | -8.8618 | -46.0949 | 2025-10-08 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 81c2ea38-4fe2-3472-a3e9-6300b917d3a4 | -14.7174 | -46.1098 | 2025-10-08 13:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| b7a9da31-4beb-3932-bd02-37d434c64190 | -12.5297 | -54.7326 | 2025-10-08 13:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9b2ccd2b-9c54-37c8-9785-1f1e6ef3e8d8 | -7.5801 | -49.8829 | 2025-10-08 13:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 49870ac1-4364-3379-b4de-47ff00bc31fe | -12.7829 | -50.4897 | 2025-10-08 13:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7a06a3cc-fe2d-32c1-a610-053176100fad | -14.7179 | -46.0867 | 2025-10-08 13:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 4dc176cf-6da1-370c-9b0c-fd107a154f9e | -15.6195 | -52.5928 | 2025-10-08 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 66a0c717-64dc-38fb-806e-5c245f8e2905 | -9.6607 | -49.9373 | 2025-10-08 13:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 254.0 |
| ba4732cb-2f58-366b-a961-6ad72cb0db26 | -13.7364 | -45.68 | 2025-10-08 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 283.7 |
| cb19a4e1-fc3d-3966-b0f7-9ce5b028678d | -15.321 | -46.1622 | 2025-10-08 13:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 847d472e-620f-38d5-917c-75898d530652 | -8.9306 | -46.6033 | 2025-10-08 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4b2443f1-92a8-3c29-94e4-bf5158d347f6 | -10.9296 | -47.1329 | 2025-10-08 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c19a34c5-4c8b-383f-9985-7ecbb34002a3 | -14.7174 | -46.1098 | 2025-10-08 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 246.9 |
| 481a1094-da60-3243-9b4c-400edbb50796 | -15.6202 | -52.5501 | 2025-10-08 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d0df4a8d-5d4d-3435-a83e-727e4f270c8b | -13.7368 | -45.6569 | 2025-10-08 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c01c3799-c713-3af7-aa63-a505e9a2d842 | -10.8732 | -47.0953 | 2025-10-08 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 29e2f0dc-8941-3001-b628-ecb5fbca534b | -14.8824 | -51.4992 | 2025-10-08 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e553d75f-8eb4-3d33-9554-3c25f0653de8 | -8.6295 | -45.1 | 2025-10-08 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 290.7 |
| b168e2d7-a5fc-396f-a3f8-ddfe1600c2d7 | -8.1807 | -43.321 | 2025-10-08 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| eb79de32-309e-3a61-9f5e-5498069e80fb | -8.9121 | -46.5829 | 2025-10-08 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b4fade65-c8f9-3331-aadd-8beaeb24d93b | -15.6393 | -52.5688 | 2025-10-08 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 281e1b9e-fa0b-3a6e-8eac-e374ebfc0be0 | -12.1274 | -50.9118 | 2025-10-08 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2abfd9a3-6c93-3e98-9d8d-cdcea09182e9 | -8.691 | -44.727 | 2025-10-08 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 5718d47f-63db-35e3-92ec-c5e9ea99fcce | -14.4079 | -46.026 | 2025-10-08 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 93967cc9-79c2-31df-89c6-6710117aec59 | -13.7918 | -45.809 | 2025-10-08 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f769cf45-bd30-3d01-b6a5-04fed6c8596c | -10.4245 | -45.3907 | 2025-10-08 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 428.9 |
| fc3d74da-690a-3e8d-89d1-b841ec238770 | -12.5109 | -54.714 | 2025-10-08 13:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 31cf18b4-db3e-3840-9fe8-7d24078717d3 | -12.2525 | -47.8728 | 2025-10-08 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 90ede222-3989-315d-8c9f-713464a645a6 | -7.7922 | -44.2229 | 2025-10-08 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.0 |
| eb4b18df-54d1-3155-8f4c-4f73b2a33398 | -14.3889 | -46.0063 | 2025-10-08 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| e4af4de2-fb49-39d7-b933-64ae44f2d265 | -13.3774 | -47.2411 | 2025-10-08 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7a6adc08-c94c-3dfd-9bab-77d4bc44cde2 | -10.4251 | -46.591 | 2025-10-08 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 701efb64-12bd-3964-beda-53843d6e1498 | -10.1871 | -46.0116 | 2025-10-08 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3d59c92b-cf9d-35aa-a495-9714b8e0807a | -13.3513 | -47.6042 | 2025-10-08 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6abfcd65-fa20-3770-b2c5-1106959a3986 | -14.7184 | -46.0636 | 2025-10-08 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 179.6 |
| a3766ad3-182a-323a-a5c9-42f1d32cf898 | -9.6604 | -49.9587 | 2025-10-08 13:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 3ed7b896-a574-3d27-a70f-93ddec9251fb | -17.954 | -44.4124 | 2025-10-08 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 7c789e5d-7ed0-324d-8e4c-66c16f2e8461 | -7.7924 | -44.1998 | 2025-10-08 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.6 |
| f2d36252-02fa-3fe0-a08c-fe4301bd1a79 | -8.1804 | -43.3445 | 2025-10-08 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.1 |
| 42a4c025-f027-3552-8ba0-71ca9153d764 | -12.5297 | -54.7326 | 2025-10-08 13:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 4cbea11f-2046-3255-9126-a13ae57bdda2 | -12.7829 | -50.4897 | 2025-10-08 13:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 12f5a04d-67b0-3bcf-a969-77d0e23fff18 | -9.6793 | -49.9569 | 2025-10-08 13:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ffb616c6-dbdd-3b44-add4-4ef91de636cf | -13.2434 | -47.194 | 2025-10-08 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 83229acd-6d9d-3f13-8933-2ed15e9d20a6 | -8.8621 | -46.0724 | 2025-10-08 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 3b25ea9d-139b-3611-a303-64591fa14db5 | -12.0122 | -45.1929 | 2025-10-08 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| daa89201-fe06-3a06-b6aa-f46a724a5535 | -14.8828 | -51.4777 | 2025-10-08 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4f0b11e1-f3e8-308e-b7c8-fefadd4d7164 | -15.3979 | -48.0164 | 2025-10-08 13:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4741bb66-3a1d-3003-adfb-4543861e1863 | -13.8117 | -45.7826 | 2025-10-08 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 771d2359-90ba-3bad-b995-4cb3b7762524 | -8.6106 | -45.102 | 2025-10-08 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7a571310-ee0f-3304-ab03-4374db62daa2 | -12.1271 | -50.9332 | 2025-10-08 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| cd96ad2d-dca4-3137-9f27-cf1ef070c9ce | -8.4824 | -46.2912 | 2025-10-08 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| aa1bf894-fc60-3590-afea-2f44d6b9bb96 | -13.3778 | -47.2185 | 2025-10-08 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 87ef0c88-00e5-3667-baa7-d123dc53d6e6 | -8.9309 | -46.5809 | 2025-10-08 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 757e983e-da2d-3105-8317-fc4d42fabf47 | -15.1505 | -52.763 | 2025-10-08 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d91680eb-c04c-383a-8d1a-4eb238d2bce1 | -14.6983 | -46.0902 | 2025-10-08 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 6017b40d-32c3-3578-a530-f9bafcd303d6 | -14.3884 | -46.0294 | 2025-10-08 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1eccf7aa-58a6-3386-bdbb-5a45821a4093 | -10.8922 | -47.093 | 2025-10-08 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6209f9e3-f6cc-3d5d-90ec-996ea9b45bc0 | -15.6198 | -52.5715 | 2025-10-08 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 349.9 |
| 0c73e134-bc38-38ef-8ff7-107266de2cfd | -10.9106 | -47.1353 | 2025-10-08 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 4c39bfbd-b3df-39fd-b974-a63cb65eec91 | -9.6795 | -49.9355 | 2025-10-08 13:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |


[Clique aqui para ver as próximas entradas](README104.md)
