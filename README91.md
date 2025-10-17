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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4aee6a6-1985-3336-b16e-3482b83aa212 | -11.47742 | -45.08561 | 2025-10-17 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d2d60dc-a22e-35f0-b0e5-7294b8f31aa4 | -10.27458 | -44.03596 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b62ae535-3050-36fd-bb06-93ac66d02b4b | -8.39239 | -46.24411 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2fcf9651-d79b-37b3-b423-8637f9473e76 | -9.17717 | -46.74277 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa0e9e88-7887-31c6-9257-ea58838283d0 | -12.15004 | -49.68054 | 2025-10-17 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f313ccbd-5b45-3b57-b75d-d1bd9defc64c | -10.43081 | -45.02173 | 2025-10-17 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7769a967-a76a-31f5-a45f-6a79bac8d026 | -10.27485 | -44.04218 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19697fec-5052-324d-b920-0e2191e1d8e7 | -10.27286 | -44.01876 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13fc223e-3c27-35a4-a95c-a0b04d70b478 | -12.92527 | -41.82688 | 2025-10-17 04:51:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 17b79cbe-b522-38b9-a583-241289452590 | -9.40393 | -47.60435 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8d486a-f91b-30b6-9a48-40ccaf070e32 | -8.12437 | -45.56841 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0c2dd22-775b-38f6-84f5-fb82691bc443 | -13.28959 | -49.57704 | 2025-10-17 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5dfcd53-cba9-3fc8-9775-66aaee18bb82 | -11.51666 | -48.22855 | 2025-10-17 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe87dee7-e1ab-305b-a784-51edb8573aaa | -8.37441 | -46.31156 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 023647bb-ad9f-3a2f-8c21-59c8b4a832c2 | -8.06765 | -45.4108 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5d9e9ce-3a3a-319b-bca5-e3a70038710a | -11.39305 | -44.22176 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 469be7ba-e311-3ec2-afce-9eb47700c71b | -10.27315 | -44.04643 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ff0e4c-a1b9-39fc-ab81-2e5107bf4200 | -9.21076 | -47.84657 | 2025-10-17 04:51:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87b2e379-e839-393c-a0f6-e2074cf549b8 | -8.12183 | -45.55579 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eed702ec-ec93-366d-b760-588456a17eed | -14.35443 | -51.46656 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ed0bdbf-5a58-365e-939c-c65d0733da9c | -12.16268 | -45.07867 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88e46f08-311c-3579-baa3-ff7661a0285f | -9.14438 | -46.65164 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 965363f5-aad6-3bc3-917b-01df90fa29a4 | -10.61723 | -42.31264 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c71e6336-7c8a-3fb0-9b81-af2207d6f75a | -9.15593 | -41.05936 | 2025-10-17 04:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5f993565-8bfe-3230-9252-7a45217db4aa | -9.52706 | -47.86604 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1b5f0ba-ab22-3701-8464-4e6b5cd7223a | -10.50184 | -43.43147 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1f8f5ca4-e40d-39f2-808e-e405711877d7 | -8.21584 | -45.04892 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ecd7bb6e-9ede-34a8-9d31-24766deabdfc | -14.91399 | -49.54128 | 2025-10-17 04:51:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b18f5d68-4ab6-3c9a-b7c0-0338f5e5e4fa | -12.71642 | -48.63284 | 2025-10-17 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1c678371-e8fd-37bf-ac27-a8941055328f | -9.33794 | -46.91206 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71e3ce45-c750-3b89-9814-9b38019d5a74 | -12.43375 | -51.30338 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dbc476f-ef2f-3bb3-abec-60361caab960 | -9.9855 | -47.01134 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 78f73fc3-caf9-35fc-8b17-d95a7e83094e | -8.27855 | -47.11887 | 2025-10-17 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2313bc3-c5b4-3711-bc0e-d7ce7a81892b | -13.57746 | -48.49424 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcb33542-45f7-3bea-813a-1a2fbc2ebf3e | -9.88202 | -49.11677 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a42339f-f009-3817-879e-9f22a7fcaf1e | -11.44055 | -54.09789 | 2025-10-17 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0500f85f-50d6-3dad-ad56-1d8aa0962c0f | -13.27816 | -44.48463 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8badb33-c76f-32d4-822d-21e4dcf65ae7 | -11.57206 | -48.56485 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 547aac9d-5033-37d9-bf33-7b4db8912639 | -9.72418 | -48.91581 | 2025-10-17 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af266c0e-6d42-37d2-9369-79aad69f1ba4 | -10.50699 | -43.43217 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 97a7b4ae-ff69-3ae3-acde-138500f3f944 | -10.52834 | -49.55434 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 44f94314-d545-3151-82f7-a36d024c5979 | -7.68915 | -55.17498 | 2025-10-17 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a57673b-3fec-3517-b415-6cdbad0ed4ee | -13.4476 | -47.94113 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d106a446-f67b-3f79-8c0f-f13a91ed686a | -10.53566 | -44.50132 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bef6054-75e6-3c84-990f-6292cfb85040 | -11.47468 | -44.26212 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ddd4fda-ff16-3366-be1b-c00c1df045b3 | -8.45719 | -44.17319 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a82a93e6-4fdb-3a3a-8f6a-7ece36af8530 | -12.17557 | -45.06673 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f681ec82-743e-3767-8e35-a9b8d93fadd9 | -11.82122 | -57.94485 | 2025-10-17 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a23c28d-f1b5-3ec5-b26a-4ee600c686f0 | -8.07196 | -45.41164 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0405d806-efe8-3baf-be7f-c7bd632688ea | -10.50297 | -43.42279 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82cec14b-a95c-3655-9549-746c7252a690 | -9.86518 | -51.44666 | 2025-10-17 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ff3dabc-6f07-3936-8e5c-f74a5e9007a0 | -14.32728 | -51.4394 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 493f1dcb-db67-342d-b48e-5698fdd24d1d | -13.73975 | -48.21884 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c48b4fb-ee91-34b0-99fc-f9981b101d20 | -14.23659 | -54.90584 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b555c76d-19b0-3f28-8623-9e728fe037b9 | -13.41733 | -44.06166 | 2025-10-17 04:51:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d5434bf7-678d-3cf5-8b50-852497081fd7 | -9.09876 | -46.68128 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f7e7e89-3653-35f4-a700-684073208e05 | -9.90824 | -48.15472 | 2025-10-17 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68c67da2-69ed-3dbd-86aa-27a283053152 | -9.67588 | -44.53109 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5a8125b-7a81-3e7c-a16b-9f7e11298765 | -8.33274 | -46.2309 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef88f86e-e116-3859-a36b-a67f38ca6360 | -13.4389 | -47.94558 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 950b26de-6f90-386e-84d2-a3685a3c6de2 | -7.85422 | -49.65221 | 2025-10-17 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f72a7f69-2e7e-3e37-a948-3cec4d48d12c | -12.42645 | -51.30593 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 74f7ebfa-1066-33bd-9c5f-b13d6137f3e2 | -12.31523 | -45.64262 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d740ea5-e43b-3adf-8881-1693d4087db4 | -9.29824 | -46.93258 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d46af5ad-376b-3732-b3dd-dca14f251ef8 | -9.04339 | -47.91221 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3de6c3bd-476e-3594-a82a-d7ba47c28abb | -11.61045 | -49.08505 | 2025-10-17 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8791dde-0172-345e-a3b0-1a262fa9c0c7 | -13.42949 | -47.95523 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a8ff9c1-73d9-3341-af86-c6d537110bb9 | -11.95262 | -45.35814 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31919ef8-740d-3d06-8abd-a68bc38181d6 | -11.9693 | -46.55142 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa160cda-b126-3340-979e-f5843f3d59b0 | -8.21379 | -45.04668 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6405acc0-631e-3d0f-a76e-792c7cccb456 | -8.09349 | -45.41586 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e24b753b-2140-3669-a5fe-e8fcdf6a29b9 | -10.98002 | -47.90084 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4cb34c6-ba1a-3f31-ab35-0d880806ffb1 | -8.46601 | -44.17946 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7eddd576-1dfc-3bfd-9a3e-28abff89c01e | -9.08029 | -48.02981 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77aabd18-f225-32a6-9fbb-4d7735d7c046 | -13.93702 | -48.69305 | 2025-10-17 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f290839e-d21c-3d86-b454-23f2bdfb401c | -13.41416 | -46.70912 | 2025-10-17 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73e3f950-a395-37e3-8e0f-5bd0fa04a5b2 | -8.49976 | -48.49221 | 2025-10-17 04:51:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27f884ab-e7cb-3215-8180-ac6e9e6f85e0 | -12.48536 | -45.4761 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e648d49-c9dc-30c0-906d-cdac9910151f | -10.28605 | -44.0255 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3e74bc7-9c4a-399b-b8d5-d3bdbe3d289c | -10.80636 | -43.93518 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4abc435d-793a-357c-a97c-2cb0221a8ff0 | -10.10138 | -44.63013 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87936a5c-9637-3ee7-8b18-27cb924c1146 | -9.14185 | -46.64056 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e91d3c8d-176d-3371-90a5-444409eda411 | -9.13982 | -46.65454 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d96e5208-560b-388f-8e61-56243ba29de0 | -8.46195 | -44.17381 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a72d5093-eceb-3425-8081-0409aa00f2c9 | -8.25786 | -44.06599 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dcf3155-5e46-3fe1-b4a5-367ec8f1f045 | -13.42921 | -48.56398 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51af471a-31ca-31fd-8a25-7ed34dd33ce6 | -14.23876 | -54.91413 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab80893e-131c-30ba-8bd4-f1a39b3f80b8 | -14.91032 | -46.76785 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 176845f9-74e1-369f-b4b6-13521db8ee06 | -14.33294 | -51.44791 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1648ed01-6563-3a45-8578-2f00865e2e2e | -11.97354 | -46.55209 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5c27ab5-fe99-3884-9b2b-2a7215888024 | -8.68151 | -47.00486 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c404bba-7a0b-3987-b971-6e03f1a455b9 | -9.14032 | -46.65109 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d31ada51-9f23-36ea-8458-a9096197ebd0 | -9.22174 | -46.88839 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce190c88-7012-3ce4-a982-1193b01e6dd6 | -10.29392 | -44.04954 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a666c925-4a67-3a90-958f-2519c490cff8 | -9.09066 | -46.68021 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c5931cf-1cfd-3bfb-a8f7-0493527c2d12 | -11.46975 | -44.26144 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76cee15a-4388-3e7b-aa4d-33ce2e1efb18 | -12.44835 | -51.32058 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3ac1ab1-98c2-31e6-8360-6fb577398585 | -11.95322 | -45.35353 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd720d4c-6961-356f-96ff-af98ec5e04cb | -12.16005 | -45.0757 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a5f9e80-7e22-3621-bc8b-dae68e2a5813 | -9.0387 | -49.09808 | 2025-10-17 04:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README92.md)
