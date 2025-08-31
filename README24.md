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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 992bbffa-0b8f-3a7f-801f-550628cb3bc8 | -6.29316 | -43.54256 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4c7608a-3980-314c-a799-bee84cb158ab | -7.40186 | -45.92072 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3616b31-58b9-3058-82cd-b81e390c15e6 | -8.87943 | -45.09649 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e3656b-d666-33d7-82d0-568e43ea2683 | -11.33875 | -43.63718 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03e6cfa6-d551-3dbd-8136-ffd7c720ce20 | -4.48119 | -48.11884 | 2025-08-31 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8012486f-0206-3a44-9d60-be265bbcb0c5 | -9.6933 | -47.04282 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edd76d3d-11ea-3047-9988-13e3126ac913 | -11.3145 | -43.69774 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16a465f9-f9f6-3d8e-b99c-e71fc7c527a6 | -11.34855 | -43.64279 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 49c8d8d8-2476-3695-95f1-d6db0212bf25 | -6.42576 | -43.96431 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c97b2758-f980-3cc1-a59a-bea97c87f8cd | -7.95422 | -46.38559 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b7542d5-7a14-339c-a285-589ebb023a7a | -8.28757 | -46.31551 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc4eca72-6dfd-3af7-9e9f-4f54cae4d253 | -11.2916 | -43.6415 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc5f310d-9b99-3a53-bc30-1902134a9894 | -11.34002 | -43.62944 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 748ae843-66dd-3d85-9467-ddc7b388d17c | -6.30823 | -43.61126 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bdda58f-180a-3486-bfcf-1462a286eed6 | -9.69898 | -48.29684 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2751333a-1a7b-3e67-a658-c9bf86daf491 | -11.29155 | -43.5773 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c81ccb18-e6ad-30e5-abe4-847aa5ee30d0 | -13.48011 | -46.96736 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b321d68-0c75-3704-ac1e-c328238add54 | -13.464 | -46.94088 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc7441f5-87a9-36e7-859e-b2757c715434 | -13.34768 | -46.98203 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e1dd6e5-1b0c-322f-8f16-3f82fce56420 | -11.86807 | -46.48994 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ef840a6-3362-33fb-97cb-6a76636a4744 | -11.8022 | -46.48048 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1f4398b-98fe-3358-b9a3-b6e9dfbd0c13 | -13.351 | -46.96349 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07a7cf5d-55a3-3c0c-b407-75e6aae7e577 | -13.67352 | -46.87288 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d61f172-e7c6-32c6-af6a-12b5231c6b6b | -13.47934 | -46.97166 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a356f92-aaf4-39b1-8c59-a6cae1a0298b | -13.67757 | -46.87336 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92e6f137-bc32-3c72-ac64-4bfc29a6b3c7 | -17.14996 | -46.06904 | 2025-08-31 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6687d69f-a5c8-344e-a695-a353e01a51f3 | -14.33532 | -51.87914 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a264cc-9182-3297-9526-6ca35540f6b9 | -14.34078 | -51.88032 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75c3504d-549b-371a-8cd6-d551bc2a465e | -13.4753 | -46.97092 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c518b352-dd6e-39a6-819c-fc4a247018eb | -17.85734 | -44.73748 | 2025-08-31 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79ee0847-d1bc-35c9-92f5-24122eb3cdd3 | -15.94677 | -41.4013 | 2025-08-31 04:04:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b14c8d76-79f0-3db5-aeba-7ee721b9a562 | -14.03641 | -44.56399 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed8740ab-3bbf-3e4c-bf37-74857214af58 | -14.66544 | -52.36908 | 2025-08-31 04:04:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48735fec-ea5e-3b6a-8063-a69d71521744 | -14.35823 | -51.90665 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3abbb3c3-0538-3a14-aef8-e45aef4ac593 | -13.30667 | -46.88037 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2def5c1-a520-3363-a017-fa0f3f50b998 | -12.75391 | -44.41358 | 2025-08-31 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ff4501-5e96-3fe8-81a8-f18eb6c27f11 | -14.13854 | -47.05862 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fbee1b0-e407-3133-956e-377ec9882887 | -17.60852 | -52.68613 | 2025-08-31 04:04:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2454adcc-59bf-34d8-89c2-22f6aa766fd8 | -11.56336 | -47.61999 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f74e7191-0dcb-3de9-845b-8485871f48c1 | -13.31408 | -46.88553 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96515370-4b39-3ba8-a388-f3b46227b271 | -18.92832 | -48.18132 | 2025-08-31 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a6a59f7-519d-3338-b2e1-cc6c693ca24c | -18.06743 | -45.9503 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04e94872-fd87-3cfa-ab1e-e5ed7272f5e8 | -14.53784 | -51.97927 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d5b5a76-56c7-36e7-a84c-0e109c374204 | -14.53751 | -51.9809 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ac55e04-3bc3-371c-a626-bc3c8ce8d054 | -13.3244 | -46.87967 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b8ba527-aaff-3fa5-bca4-dc51d6a161eb | -11.90743 | -46.69244 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b1f6bde-cb41-3720-ab3f-df19dc1b3e94 | -14.03574 | -44.56805 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d4820ac-0018-3472-8c92-e803ee12e495 | -11.82514 | -46.44419 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d99d7d19-1f97-3cd7-9f63-ac0a3e771cb9 | -15.21916 | -56.07033 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b280873f-a239-3456-a06c-fbe7b4d2ba22 | -14.54147 | -51.98944 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d99ce71-da7c-32cd-890b-c2e25b1fa5c2 | -13.33368 | -43.19428 | 2025-08-31 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12afb9d4-b145-3833-9ebd-f77707ebb3cc | -13.26359 | -51.98167 | 2025-08-31 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aad6e73e-92fa-39bf-9de9-e51730069e93 | -12.81403 | -48.0989 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 136af9f5-4a46-3754-95d1-80ec72422895 | -16.41098 | -45.64688 | 2025-08-31 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2405711d-1657-37ef-a601-e0ed61001441 | -11.83638 | -46.42712 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97d8c336-9e50-3699-963c-3ecbb35a11ed | -14.20564 | -42.02032 | 2025-08-31 04:04:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4b71841c-f0e0-3979-a35e-d274250c07a3 | -17.206 | -46.07278 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b40e5f4-8830-31bd-bc48-bab71bc55d4b | -14.33554 | -51.87588 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5074636-d272-3fe0-8334-8926e3a87312 | -18.43743 | -47.23662 | 2025-08-31 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55c5aa08-72f2-38c2-affb-ca9dc157a9f6 | -13.3544 | -46.96783 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31536208-98c5-3f80-9a51-3958b2c2ca69 | -13.38901 | -47.00855 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96fe9a2c-57d7-3a47-b26d-39e511e2f5cd | -13.34165 | -46.99239 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbd255a2-69ee-37cc-8530-11d66f1f0bfd | -13.40352 | -46.94973 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55c288e7-99ee-3604-b9a3-b7bd93b052e7 | -11.83174 | -46.78674 | 2025-08-31 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29600494-db16-318a-94b2-e3c79b2d62fe | -11.9484 | -46.69637 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c6843de-5860-36ea-8571-84084d88916f | -16.77254 | -50.30589 | 2025-08-31 04:04:00 | NOAA-21 | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1c6c435-7e2d-361f-9f2e-9bfbc0bd9098 | -15.67749 | -43.22972 | 2025-08-31 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2ccdfa56-fd1d-3282-8d5d-6666afe623d1 | -16.98256 | -49.31499 | 2025-08-31 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bc5e4fa-5d6a-345a-a005-cff0876067f6 | -13.32341 | -46.87968 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1f857bb-2232-34c6-af99-3e7b3ac122ff | -11.88807 | -46.73098 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a4365d3-831b-37da-a45e-cc15a9549093 | -14.98785 | -46.70846 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64f4724b-ec48-38f2-8464-ae031330d7ca | -11.91658 | -46.40306 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4797fe02-17ec-318b-ac54-bc226dd3a8c2 | -13.53915 | -46.96757 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ed34837-f76a-3af1-96c8-e033fbebd601 | -12.80687 | -48.08844 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0e22aeb-7ce1-3308-b006-7b5e6067e50f | -16.16195 | -45.84595 | 2025-08-31 04:04:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54fe86ab-fd74-334f-94bc-3c7bdd619d2f | -13.47128 | -46.97009 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb7b85ff-d7b1-34f2-9f6d-9aacdf04de96 | -13.30475 | -46.89133 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42da9813-d029-34fe-b1d4-be9c7ccd92cc | -10.94954 | -50.83556 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ce183dd0-9d64-3fcf-a3bf-c61d76ea204c | -13.54044 | -46.96041 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4da9d4fe-300d-30f4-97af-05c32483123b | -11.8859 | -46.35514 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0ac7852-4dd9-3178-8e90-07ac3a2cd0d4 | -13.39377 | -46.83989 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca09540b-78d2-3793-a55f-8910afd4ab8f | -10.24134 | -54.97395 | 2025-08-31 04:04:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7c9d341-b3a0-36c8-abd2-6bdadc9b9ab3 | -14.83943 | -46.7453 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f550bba6-dcf0-3179-9630-c3cad3024a37 | -14.03506 | -44.57211 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfc14333-8702-3283-ae42-6412e722a400 | -11.8968 | -46.49166 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1385826-0735-3c41-8e0c-e3e93993194a | -13.53452 | -46.97013 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ed769e8-b972-3410-8b59-2d8cc0ed80b9 | -13.35489 | -46.9417 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f35288e7-234d-31cd-a03d-f7eb3f6ebf69 | -13.98712 | -44.53448 | 2025-08-31 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 298ecc60-76de-3f2e-8cd7-7eac556ec272 | -11.86306 | -46.48828 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b091e9f8-cefc-3d66-89d4-6dac4c768247 | -14.82697 | -46.74746 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1309e28-97bf-3842-8232-3c0827027cc9 | -11.86483 | -46.50806 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e84b165-43ad-304a-b14a-559786496d01 | -13.34969 | -46.97082 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 664318b8-c18e-3ea2-816f-2fc4a99823ac | -13.5085 | -46.97178 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bac38281-5242-39d0-a880-fe44d63af2f0 | -14.99228 | -46.70136 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef88c0ba-a78b-39e2-857e-896e89235497 | -10.96402 | -50.85336 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 68ba593f-14f3-332c-92db-28c5535c9dfc | -13.32214 | -46.88702 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebf817a0-079c-3d39-a17c-b0e8dcfae489 | -13.34032 | -46.99978 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39f4df13-a21b-3fe3-9909-f60c97f3a1f4 | -13.48416 | -46.96801 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dafa34b-f373-3653-ba75-c3c4a7e98938 | -16.22184 | -52.6654 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b493b805-b873-3db2-b140-26558ccbd864 | -17.83028 | -45.25649 | 2025-08-31 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
