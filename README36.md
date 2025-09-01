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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f652dd04-74ca-314b-95cf-017036a47353 | -6.31059 | -43.51302 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 140eae05-7db9-3093-9d71-7ca1b6ccade2 | -11.87583 | -46.70771 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9d646ce-0c3d-3b7b-8533-67ef6d44cfb9 | -6.5797 | -43.63634 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c1f2923-4cc4-3078-813c-71b9ecc15636 | -7.74371 | -50.25839 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7336c231-8de8-3181-947d-f85c8ce74d10 | -7.08853 | -44.3403 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 93b63206-12ac-38fa-a6f2-4fa32bfca092 | -9.2186 | -47.11391 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 173d699f-6c7a-3373-b88f-ceed261e40e6 | -6.81251 | -44.31067 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec89bf27-9b28-38fe-9c9a-e972d084d2eb | -6.82321 | -52.82645 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 068760a0-3b2e-33fa-b114-8427076ace45 | -6.8967 | -44.38918 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec8dd1bf-7749-3358-a1fa-59bf3e90e489 | -11.02926 | -46.94674 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0ab6146-0c99-33b4-a0be-7f73834f5d8f | -8.86444 | -49.55414 | 2025-09-01 04:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8433254f-cc61-3df3-8233-69dece985a23 | -11.48361 | -46.80133 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d3983c5-d9bd-3fda-af1e-a85024596d80 | -11.00988 | -46.94311 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58f50ce0-94af-36be-960f-1e2978eb22e3 | -7.11142 | -44.76141 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03253ce2-a8a9-3f1c-9db3-17bfe140c5c4 | -6.52184 | -43.54583 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3c85f5f9-efc9-3d2e-8aaf-1b7eeadfeab5 | -6.30856 | -44.76469 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf67ab7b-d320-31b3-b7dd-abe3e186550d | -7.72763 | -50.25984 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c778737-4ec1-3143-aaed-8991b38bf6e5 | -9.64375 | -47.81816 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f00c316-801e-39d3-8488-d234d88ff1bc | -6.80928 | -43.34654 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 23948e36-4d45-3fab-a61c-30fb7da999ab | -10.93054 | -50.8537 | 2025-09-01 04:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40e1d1b7-b5da-33a9-b409-f60dca5edaaa | -6.30365 | -43.64421 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 725a46fa-f93d-3256-87ec-74150a3aa859 | -6.1907 | -43.34327 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79605e75-4e6c-39ef-88fb-ab034b2b556d | -11.37338 | -43.57288 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4907c4b9-f14b-3670-acfd-b23d71b6449f | -7.93903 | -46.44853 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8a8291a-4054-35b8-88dc-f0670ef45884 | -11.02207 | -47.05813 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c5ed8af2-e60c-3309-8bbd-986e37b37238 | -6.74003 | -44.00236 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2baf7cbd-a9df-3de3-b278-ead35e1b75c4 | -6.24665 | -43.39073 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0e51783-3ad4-3a30-9d9c-24c533468053 | -12.09084 | -44.72377 | 2025-09-01 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9414b292-8fe8-3790-bfd8-4a206966b144 | -11.89281 | -46.73847 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b77c8ae9-2231-3242-8304-ab0b26f114bb | -6.46208 | -42.41971 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2dc69320-5ff9-35d2-9cc8-cf7c153685c3 | -5.29259 | -45.13795 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14b5c81a-ca04-356b-ac24-ceeacf6b7058 | -6.2764 | -43.52674 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62edd59b-08d6-30ce-a862-c23dbb0015b8 | -11.33971 | -43.67437 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb7dfd26-2855-3494-86ef-3e9f8c99c54d | -11.37558 | -43.5806 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53d76512-b108-306e-846f-438233a2c919 | -6.64196 | -43.96313 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78b9386d-32d5-30fa-8260-7cd39c60880d | -8.19825 | -46.77903 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 224ec3f7-7e60-3ab4-96ef-9efca52891e8 | -11.3535 | -43.52545 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 943ec2d0-b926-36a3-a3a5-8cdf149ab89f | -6.30387 | -43.62076 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4aa7e2f3-0428-3346-9000-950ff1dbf4bb | -9.69584 | -48.28256 | 2025-09-01 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dc31a43-1d88-325a-b4f5-f269814bee77 | -6.27557 | -43.55368 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8aaa7d1-ba39-35bf-8d0b-c7b548b1b3ab | -5.88164 | -42.98804 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b71bd17-ed5c-3f18-b56e-2dfcfac1d1d7 | -11.90227 | -45.03821 | 2025-09-01 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd87811c-d735-3a21-89b9-7bd67d79a9c8 | -6.74424 | -43.78012 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72bc9fd8-51e7-382c-89cc-b2555af75798 | -9.22857 | -47.10415 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e7b5303-1735-3c81-9156-e5f1e83af885 | -7.10501 | -44.84684 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f72f816-21d8-35af-baa5-84883dcee9c1 | -12.17272 | -44.00833 | 2025-09-01 04:10:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5ed1d96-1127-3dce-8acd-8c6534a13397 | -11.89894 | -46.68112 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4956801-c07e-3d0c-bf0a-f9a091bb2e52 | -7.10725 | -44.56007 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af27b466-e94c-3ed6-b375-50fa7afac15b | -6.26516 | -43.5521 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc9992b2-08f1-32d0-ac12-42b053ee4cb7 | -7.95087 | -46.45055 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ff978fd-fb09-3d83-a967-c4cacbe0caf2 | -11.85077 | -46.78623 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93baaa75-c892-3947-ba93-5780bd7c2d1d | -5.40534 | -42.34276 | 2025-09-01 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb5fc118-6a6b-3ccd-a665-92da9192ef34 | -6.63245 | -44.37925 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82affa67-6567-32a7-9490-0f8336a5f97c | -10.04094 | -48.11853 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ac0367b-cf64-33fc-af06-8ce462da2723 | -10.04243 | -46.02275 | 2025-09-01 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54da138b-c5c7-3502-a2ba-e1616584c54d | -6.54088 | -44.60063 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27e014f9-01c3-3c94-a479-1149387860f2 | -9.14212 | -47.94347 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fc888a9-64be-3842-b3bf-6f76e6c2420c | -6.27999 | -43.29261 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e25644e9-d29d-3c91-a36c-ec39ad1da9fe | -10.05302 | -48.09988 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a860241-27a6-306b-8b0b-9319639bea41 | -6.23398 | -41.81186 | 2025-09-01 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dbd58fc3-3e8b-3b69-90fb-ae72228ea1eb | -6.17148 | -43.3179 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8eed027f-3a71-3aab-b35c-01a7069a6451 | -7.08073 | -44.35219 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd82f3f9-1f50-307d-bcc1-e61b08e8bb35 | -5.56512 | -47.41283 | 2025-09-01 04:10:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8bb8666d-d530-331a-97ee-fee9eeb27bbe | -6.96876 | -44.3061 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69a875c4-3482-3599-9ac9-99d6113706d2 | -7.09208 | -44.34092 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fbfbeaf1-22b7-3407-9b94-531746b4b763 | -7.41899 | -44.08796 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1ece752-ff95-3944-9dbe-a4fce5322046 | -6.87111 | -44.32264 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c10b6dd-acbf-394d-aa2c-e2aab163e62a | -6.53599 | -44.45113 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34070557-9bb6-3de3-a012-e8139f44bfda | -10.28269 | -54.25182 | 2025-09-01 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd2c4773-e8ee-32ff-b14f-48d7ad8937e4 | -10.2386 | -51.10714 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f5e0925-cbfa-3db4-8028-73aebfb206ad | -6.18605 | -43.35018 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb74e148-a9ff-35fe-8c12-39155b4fb687 | -7.11368 | -44.77042 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c9f3c27-2fe6-3d7e-91c4-51dc983639cb | -5.40389 | -43.36768 | 2025-09-01 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d89ad84-1707-3287-ac58-4cda64e2cdbe | -9.69076 | -48.28603 | 2025-09-01 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 316f80bf-56eb-361f-b919-c2e76e24cc94 | -6.28343 | -43.29316 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b05456d-47ff-3d33-84c2-e6028a224a99 | -6.17623 | -44.11738 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07e510fb-4dba-3cd1-a580-674fc6eb3f36 | -6.93762 | -45.56396 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1832867-f3d8-370a-ba3e-7aa6c5c9f082 | -11.20488 | -45.04119 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b55a9634-b357-3192-b29b-8b3207b65813 | -6.28118 | -43.28517 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8e10892-8c81-37b8-bdc3-261d332dd5f7 | -10.24376 | -51.10817 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b7ad1f0-854d-3bc3-9554-da4bee6faf1e | -6.79443 | -52.8111 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c055a46-12a4-3e37-a0e4-61dc79f0d38f | -7.09074 | -44.34897 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 1b67c71b-ae74-38b1-afe9-43e37275acf2 | -11.89784 | -46.69279 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ede89583-4ce0-3e24-9cda-917379abcb3d | -8.84762 | -47.49866 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa90354f-6a70-3026-9dc0-34978ab72e5f | -6.30101 | -43.5503 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a52fdd95-071c-3654-9419-ce0abf4ee33d | -8.95076 | -47.85032 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc3a3a0a-4021-3341-b45e-23c0c913c6d7 | -9.38636 | -48.00987 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf752610-41b0-3e09-81d9-e361d8cc992b | -5.84887 | -42.53712 | 2025-09-01 04:10:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13e81ec9-66ba-3abc-935b-c79c828e4d52 | -11.87103 | -46.73608 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e352e69b-989a-35e6-89e4-b80d6abd39f1 | -11.05084 | -45.14349 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| a993cea0-72b1-37fc-805f-9a01246af25f | -11.07801 | -44.73949 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e448a8cd-fd74-3493-b2b3-9d76563159a1 | -6.8333 | -43.32303 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f1fcb844-2e26-3f27-a665-09fe9b3469d4 | -10.6004 | -44.32799 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7ecbf33d-a094-36fe-8e9e-d0fceaccb02c | -11.3721 | -43.60209 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3ff957e-58a5-34eb-b759-6408bd444dde | -6.81216 | -45.69257 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 208cad38-c088-3a69-86d0-e3e84cfd3fea | -6.45866 | -43.95819 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d406581-b51a-3871-b1b4-47775981c52d | -8.19947 | -46.77195 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 902b3c3d-0ecc-3a30-8d63-7e36f39f0b48 | -6.45872 | -42.41918 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1fba48c-4046-3895-9464-3b9478ccd153 | -10.66766 | -46.26003 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9babd82-272f-3cd3-bf85-aa1a879f56b7 | -11.02809 | -47.02321 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README37.md)
