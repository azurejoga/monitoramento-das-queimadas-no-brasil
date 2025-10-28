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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a66a87c-92b6-33a2-a8e4-2df0ca95ae76 | -7.45904 | -47.02824 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8f62f8a-33b9-3cf1-bb73-6dd83a2d0765 | -6.11341 | -43.70432 | 2025-10-28 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26690cb6-24e8-3c3d-870b-549f76a8bc69 | -10.74727 | -42.69265 | 2025-10-28 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e2aaf0ad-d41f-3f39-b68f-87038fa1e0fb | -8.45048 | -45.12328 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea4c47fd-96bc-37b5-9c02-d21579bf8d9d | -11.60728 | -48.53947 | 2025-10-28 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb030ca7-df04-31ad-8b70-6c7b4360558e | -7.86864 | -46.39801 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a72b19f-7597-36ad-8296-e5b798869407 | -12.05575 | -46.4702 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e77c759-89ca-38c9-ba63-a3551ef7b7d6 | -7.2609 | -45.00465 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4091be7-e5b4-37aa-ab7d-42bc838c6ae6 | -7.80528 | -43.83208 | 2025-10-28 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5d4c05be-17db-32d0-bc77-872028752bcf | -7.90227 | -41.78648 | 2025-10-28 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5947bdf5-3afd-314f-b254-7116af81bbe7 | -7.36746 | -47.78804 | 2025-10-28 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e7d218d-f606-3c15-9716-82d0725525ae | -10.5638 | -49.79204 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6606ec7-1b38-32f5-ac90-cdac0f725dcf | -7.96405 | -47.24179 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a5853ac-f558-3ad8-9553-a0ef5cedd03d | -11.28755 | -45.51631 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 932909e8-8fc4-3c78-8c5b-c1fc3af02070 | -10.99215 | -50.36159 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35822db7-a892-307c-8469-1fce217b0236 | -10.57082 | -49.80146 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9452e352-5d1b-3217-9540-0d2354d6e881 | -7.15711 | -41.19826 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a3fbb6d1-133a-3a30-ad17-74aaed76bc35 | -7.42702 | -41.86874 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6587ba7-8d85-3c17-a5ac-a84287069617 | -6.23947 | -41.83128 | 2025-10-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8387ffc0-467c-3d47-a999-c71dcd10fe88 | -10.57575 | -49.79825 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e0c8d0e-c91c-3492-8619-ef87d3fadf73 | -12.40685 | -44.71447 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8cb6105-c87a-3200-af4c-faa2919e59d3 | -6.98805 | -39.12877 | 2025-10-28 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fce95ed4-7323-394f-b4e4-a426a011d220 | -10.29376 | -47.19485 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 754b4c84-e2a4-30f3-9827-df29ce954f65 | -10.62796 | -42.31704 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5fda9acb-6ba8-3ad7-ab39-9ab16f29b59d | -11.10439 | -44.01759 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13ffea3a-590a-3672-a844-8faa16998c14 | -7.97782 | -45.95697 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4750cb0c-8049-3218-9ebe-664fe2a3b639 | -7.86576 | -46.39324 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77cb8b2a-c020-362e-813c-7261489f18d6 | -10.64088 | -47.90622 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c959b03-4150-3eef-83e8-216693b436c8 | -12.36504 | -44.06736 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad0c7182-7864-3993-9ba3-81528cc27b2e | -12.23108 | -47.91958 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff2e2bec-f6ec-30a9-a7d7-ac645185ec6b | -7.67858 | -47.41345 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f63ac471-0fb1-3eda-9e14-b54f46d9b986 | -6.09658 | -44.6841 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a8b0927-45e6-3d12-80ba-4b18423f49ab | -9.4608 | -47.73125 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19f3557-dda1-3e4d-b22f-f40da0367c65 | -7.95213 | -45.53261 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 049b60df-f22d-30f6-90b4-68cad34adba4 | -6.28429 | -44.71416 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ee78184-71da-3d8c-b536-bd8ba1c35b9b | -9.22644 | -48.59966 | 2025-10-28 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0a016c5-a0c6-3bba-93b8-8fc41e3b40c1 | -10.81352 | -44.26376 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 447059b3-3317-37f4-b16f-4e454c4c97fa | -10.92529 | -47.61726 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb0db90-022d-3581-a114-df46fba0001a | -9.17954 | -44.58909 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c446c99-36fb-3a1d-9664-b16cca8839d3 | -12.53119 | -47.54519 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7edbfb22-6a92-39a3-b0cb-22b110baf8aa | -10.98375 | -50.35247 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58b9662b-fac9-3183-8c90-f4ae88a4fd09 | -10.26666 | -44.10754 | 2025-10-28 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebf65df7-bf2f-3ab3-bd29-1f698fc05fa8 | -13.03872 | -45.85189 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 160c7e59-d590-36bf-8f57-78c4a0dad1bf | -11.73591 | -49.32964 | 2025-10-28 04:14:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c6dce75-e646-3cf0-b9aa-349db79df177 | -10.95073 | -48.05304 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eceeea07-d3f1-3174-a1e2-df766fdbf441 | -5.11256 | -48.48398 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a98c624e-8ba5-30a5-885d-c63ff389f74e | -6.83348 | -43.99459 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 825866ec-e93d-3391-892f-8651b5762c19 | -12.71759 | -47.73258 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 594ae197-b6e9-3547-b00b-a4c778fc9e17 | -6.13198 | -42.69815 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 203a3b94-8869-31f4-a141-a49d90872d5d | -8.64162 | -45.2893 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8bbf081-7598-3bd3-8910-92adb5ffde4e | -10.91462 | -50.25307 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b3abbb0-3cb8-3871-bcdf-3b1f135910a8 | -11.47783 | -43.25308 | 2025-10-28 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bca78290-6c97-39a0-a61d-ce3f3f7b8d37 | -9.22106 | -46.34835 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ef132fe-24ad-3a89-a4f2-0166ebaf8c85 | -6.86429 | -43.79902 | 2025-10-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5349eaee-f4f7-3b77-83c3-94e6bbe647c4 | -6.19099 | -42.40675 | 2025-10-28 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f978f635-2f50-3d82-8ab4-78e82f9e485e | -12.00788 | -46.78237 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 528d6a00-7c94-3f66-9e58-ce6b8f7221e0 | -9.54515 | -46.95509 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 035741bb-6f78-3276-95a1-289f32351060 | -10.96906 | -50.25826 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4a1a74b-c06c-39d4-9a1a-60ce9de9ad1a | -12.08618 | -46.3922 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2e9d6a90-8ea4-33c6-b8f9-7d307305931a | -10.86045 | -50.13154 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0330a2c-e187-33ee-8c3c-30bbc9588806 | -5.63193 | -47.61221 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72a931d4-8596-3968-85d8-c89ee7acba90 | -7.2343 | -44.99657 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e9970ec-4747-3dc1-928f-2b14b0f4e5d1 | -10.29887 | -47.20888 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8224804c-ad01-3bda-aad8-3bd95186fa1d | -10.67718 | -47.26408 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3feaa2f-ba0a-3598-8786-06a6b645af2d | -11.27766 | -45.50001 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebcf1088-9ac4-3a2d-bb21-99e02bda7f9a | -7.82914 | -46.40041 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 589b6f7b-e33c-391d-9439-fb4397ce8fb3 | -10.32938 | -47.22718 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 289c2026-f7de-3df5-ad26-fefca7fb2999 | -3.86439 | -55.69111 | 2025-10-28 04:14:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99d0f336-ad4b-3786-95e9-4feaa5ad5159 | -8.11519 | -45.95842 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae776c46-28a3-3ec2-ba1f-c8107dbab7d1 | -6.69381 | -42.03943 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d8a5d2c0-c839-3628-93ac-44641fb18fbf | -6.16679 | -46.09184 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e0dc912-4626-374a-b18f-08f6d9d81f76 | -10.86474 | -50.13231 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b74ddc64-9090-330a-ba1e-2c62f915e498 | -9.13365 | -51.30273 | 2025-10-28 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d72b8b7-3506-3fa8-9d16-8325fc10f20c | -11.10329 | -44.02457 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e96d7ce4-ad93-3f7c-9f39-a46a4c2d0222 | -6.75208 | -46.35154 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5af705f3-0cc6-3e1b-9e31-68edee1706f1 | -7.8182 | -45.38303 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f920038-31b1-394d-b417-a2a6c7a12d03 | -10.9953 | -50.36334 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e0439f6-08f9-373c-a1f0-21cf742729e4 | -7.46412 | -47.15921 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 518874df-e5f5-3cc6-a361-8390706ddbd3 | -10.324 | -47.14716 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95f7d90b-5124-3d96-96b9-895c89bf8988 | -12.90377 | -43.35294 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf504068-1eea-3fa6-a165-db4b186444ba | -7.39252 | -45.12398 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8442ed7-9889-36da-b12e-ffb42acc60af | -10.02479 | -47.16574 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f365b259-b0ee-39ec-8892-02727efe1dbd | -12.84972 | -44.64692 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7779c6d4-1a0d-37b1-b107-a908de1418ce | -7.95767 | -45.49839 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 667fab3f-6344-3d04-a9b4-9beb3449c944 | -12.48952 | -44.20964 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80bbd21a-3d67-3c88-baa5-bee25137408b | -9.57207 | -47.90046 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d2e8fce-813c-3ce9-befe-f6c8a5e605df | -9.21403 | -46.34711 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d5c83f7-4d04-3d11-bf49-6dae4fb19695 | -9.55688 | -46.99602 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52fd4234-1c46-34a6-afc3-84eb2572d7fd | -8.72109 | -50.00536 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd845434-602b-3d99-808e-f40e2133d6db | -9.16622 | -44.58702 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de028ef7-f807-386b-9142-7098bfd457a2 | -12.69029 | -45.11592 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8268a0d-2b5a-3579-aafc-b1ba673d5068 | -9.55445 | -46.94381 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6b3647c-9143-37c5-b9b5-ec72d7e569af | -10.91081 | -44.93975 | 2025-10-28 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8bf123cf-9b57-33d7-a6db-7834d73ca22a | -6.61131 | -42.06622 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9144490d-f3b2-318a-8e4d-752914f994e3 | -7.95079 | -45.49728 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9197e03f-d3a9-3630-84e2-368205b8c2ad | -9.27569 | -46.39026 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d65573c0-6c0c-3453-a24b-02002076be61 | -11.28419 | -45.51575 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e1f3cfb2-53db-3137-9389-33bf2f196760 | -7.06656 | -44.47853 | 2025-10-28 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2703b1c0-5c9b-3931-8894-18dbb943a636 | -8.70364 | -50.80582 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f5e0bd-9e5d-341b-acf9-0fbae1e0d2f8 | -7.42257 | -41.87533 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README21.md)
