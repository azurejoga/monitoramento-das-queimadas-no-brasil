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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5668f1c-129b-3f79-a831-0f077d072731 | -10.8188 | -46.9233 | 2026-05-29 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 21bb3161-1a0c-3216-aa1e-edb25ec5ea47 | -6.8232 | -43.387 | 2026-05-29 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 1e254982-172c-3ec5-89c8-9eb9acd77464 | -10.8379 | -46.921 | 2026-05-29 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f967435f-8760-3f34-989a-260b8f78b50e | -10.645 | -49.729 | 2026-05-29 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 01afa553-a993-30dc-8b4c-202e5bbf15c5 | -6.8232 | -43.387 | 2026-05-29 15:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| d7dfcdc8-3d82-364d-b051-b56ec48d2766 | -8.8351 | -46.7024 | 2026-05-29 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cde81964-b0f2-30fd-96be-dd23a1ebb3f0 | -8.8348 | -46.7247 | 2026-05-29 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 928526bf-0bc9-3c0d-9952-9bae6de3dddc | -10.8188 | -46.9233 | 2026-05-29 15:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 800d771b-79b1-35d7-9650-194323964ce6 | -10.8192 | -46.9009 | 2026-05-29 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 6dbab9b1-e89f-3f9c-8940-3714616d6745 | -10.8188 | -46.9233 | 2026-05-29 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 46f53ce0-0258-3ec2-aa3e-d7751c3bddaf | -6.8232 | -43.387 | 2026-05-29 15:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 148fc96f-5b25-3190-93b4-a41b680c9bff | -10.8195 | -46.8785 | 2026-05-29 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 89d1ea96-b730-3d3d-94e3-5e0beb6081e6 | -10.8379 | -46.921 | 2026-05-29 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 9cd708f0-ca11-33ba-a0ba-4601a9bc902a | -10.8382 | -46.8985 | 2026-05-29 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| eea7c9d9-869f-3d1a-8cff-dba4c8b7708c | -8.8351 | -46.7024 | 2026-05-29 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9de6c620-a492-36a8-bb76-71fa3939aa0a | -6.823 | -43.4104 | 2026-05-29 15:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 79.1 |
| d8ca71af-e7ea-3897-91b6-332533771f33 | -10.8379 | -46.921 | 2026-05-29 15:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1e1c646e-ab7f-34e8-bb62-5544ab594f89 | -10.8192 | -46.9009 | 2026-05-29 15:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 22b63c0c-1864-3ce7-a2e9-b9cfc7a5f314 | -10.8382 | -46.8985 | 2026-05-29 15:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d669f138-7308-3ad1-a184-7a9ef619d42c | -8.8348 | -46.7247 | 2026-05-29 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 31abca5e-d608-3464-9239-55f57d9ebf4b | -8.8351 | -46.7024 | 2026-05-29 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1293c46b-290a-32a2-a488-30752ce0d150 | -6.8232 | -43.387 | 2026-05-29 15:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 48c0c347-533f-3e82-af6d-5aaf52db0637 | -6.823 | -43.4104 | 2026-05-29 15:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 22ccb09c-f235-3c6e-be43-2ffc44c19cea | -10.8188 | -46.9233 | 2026-05-29 15:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 7800d1d0-f4dd-3b98-8800-183537828609 | -10.8382 | -46.8985 | 2026-05-29 16:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 1c1c1136-fd33-31c0-a00d-f7e586d19d62 | -6.823 | -43.4104 | 2026-05-29 16:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 106.8 |
| cd51a301-ff5b-3eb9-bfdd-7b3a6c99a383 | -6.8232 | -43.387 | 2026-05-29 16:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 49a035c3-f2e1-3348-904f-81c7e53b3f40 | -10.8188 | -46.9233 | 2026-05-29 16:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| c3635b68-73c5-31ff-b9b6-e69c1e738216 | -10.8192 | -46.9009 | 2026-05-29 16:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c3e68bee-14d0-3e69-aff7-453cf0a63adf | -10.8379 | -46.921 | 2026-05-29 16:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| b02708e1-9e17-3b06-9082-75c96c949702 | -8.8537 | -46.7228 | 2026-05-29 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 976178ac-9a0d-39c5-80ff-519f9797e032 | -8.8348 | -46.7247 | 2026-05-29 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 08922b49-0a5e-3fa5-87b0-179d890ef2bc | -6.8232 | -43.387 | 2026-05-29 16:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 26863516-e9c1-3599-8cd5-640fa4b8ee64 | -10.8188 | -46.9233 | 2026-05-29 16:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d5e644b6-b4fd-3f1b-8276-72357047a670 | -6.823 | -43.4104 | 2026-05-29 16:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 109.1 |
| e2dcd3e1-8e35-314a-a07a-9719c7a3d699 | -10.8382 | -46.8985 | 2026-05-29 16:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 257.7 |
| 210f79f7-a948-3abc-b95b-653affe633e2 | -10.8379 | -46.921 | 2026-05-29 16:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 486722ca-07f2-3d3e-af5e-e5624cb1c87d | -6.8232 | -43.387 | 2026-05-29 16:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| f171da68-5f8e-33d5-bc7c-d29b03c2b3b1 | -8.8537 | -46.7228 | 2026-05-29 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 12c7b9e8-0fe3-31aa-9549-8ee05b2f8354 | -10.8192 | -46.9009 | 2026-05-29 16:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| d4637a50-3f5d-364a-a8cb-24d54265c62e | -6.823 | -43.4104 | 2026-05-29 16:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 0dd11c33-5289-3d8f-ae7f-eb2cecd226b6 | -8.8351 | -46.7024 | 2026-05-29 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 5b505503-49cd-3dff-9d80-0ddaf96a8368 | -8.8348 | -46.7247 | 2026-05-29 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7a1f91a9-5fc0-31bf-8c6a-d4da5a2996fe | -10.8188 | -46.9233 | 2026-05-29 16:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 8171b3a5-11e1-327e-b6d4-1f56274b6705 | -10.8188 | -46.9233 | 2026-05-29 16:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 08778bbc-d818-37f4-91d7-96923401d9f0 | -8.8537 | -46.7228 | 2026-05-29 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 1070ea5e-bb05-36f4-9140-1530cf4c7e7a | -6.823 | -43.4104 | 2026-05-29 16:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 93.4 |
| f4e26bc0-6d9e-3511-ab76-6de202b21691 | -8.8348 | -46.7247 | 2026-05-29 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 24a1acf3-862c-3433-81d6-dd94dbc2c384 | -6.8232 | -43.387 | 2026-05-29 16:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 12d1a025-ef0a-3e1f-9fcf-b7c447018e36 | -8.8351 | -46.7024 | 2026-05-29 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 3bbee6a3-9812-3323-b19f-f86c2a8656d0 | -10.8192 | -46.9009 | 2026-05-29 16:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 625adee0-6f54-3aba-a494-382f47b4e06b | -10.8379 | -46.921 | 2026-05-29 16:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 5ed5c820-3e4e-334f-95ab-fbb88c09ec91 | -10.8188 | -46.9233 | 2026-05-29 16:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 178.6 |
| d8027a07-3e52-3d83-9c20-b706aa61febc | -8.8537 | -46.7228 | 2026-05-29 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e196bde1-df4e-3f06-9446-4b6aa328411e | -10.8382 | -46.8985 | 2026-05-29 16:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| f50b36fd-a4f5-3800-8cc8-8a2a79372566 | -8.8351 | -46.7024 | 2026-05-29 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 824ac036-d4b7-31b6-8e24-3eb4e9488b12 | -8.8348 | -46.7247 | 2026-05-29 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| be0af705-1562-3aa1-af59-8e7ca3d6ca53 | -10.8188 | -46.9233 | 2026-05-29 16:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 91d36436-8a88-3264-96a0-5305e9301734 | -8.8537 | -46.7228 | 2026-05-29 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 6376bea6-c820-307a-bd50-568c068e8ea8 | -10.8382 | -46.8985 | 2026-05-29 16:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 9cf25c63-c993-3f2a-9fc4-eeb2bc2e21ad | -8.8351 | -46.7024 | 2026-05-29 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| ec7af274-90f9-317e-9f10-a7e22de63b78 | -10.8192 | -46.9009 | 2026-05-29 17:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 3790c72c-1079-3113-8be9-61e8f56203d6 | -8.8537 | -46.7228 | 2026-05-29 17:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 1769bca2-5208-389d-a313-cd5ab854195f | -10.8188 | -46.9233 | 2026-05-29 17:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 244.9 |
| 2e0a344a-071a-35ed-a63e-eb7b68b4a219 | -10.8382 | -46.8985 | 2026-05-29 17:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 6c6a7faf-cb43-3875-8832-f8cefe1a278d | -8.8348 | -46.7247 | 2026-05-29 17:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 75c7daee-551e-353f-8afa-6537d4bdd0c9 | -8.8351 | -46.7024 | 2026-05-29 17:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 00632638-9026-385c-b130-e95a9aad62db | -8.8537 | -46.7228 | 2026-05-29 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 28edb0dd-d3f7-3fa9-af1f-6a6ee297a1b4 | -8.8351 | -46.7024 | 2026-05-29 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 07acd849-eac8-393a-9449-243056c2ed3f | -10.8188 | -46.9233 | 2026-05-29 17:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| d823f7a8-2e61-3fc9-8c7d-f946fc8b803c | -10.8379 | -46.921 | 2026-05-29 17:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 241fc5a8-169f-3104-a862-477a9b74ce7d | -10.8188 | -46.9233 | 2026-05-29 17:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 90a322db-93d4-368c-95c7-0e19ac6aa014 | -10.8188 | -46.9233 | 2026-05-29 17:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 59089cf9-cf90-3462-83a7-971e6c2eae49 | -10.8379 | -46.921 | 2026-05-29 17:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |


