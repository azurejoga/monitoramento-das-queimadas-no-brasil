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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92c8002d-9192-3c53-b120-fe12bb5e932f | -6.10672 | -45.87988 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bcb2d68-a8b0-3810-be4b-fd5825d20c86 | -4.29452 | -48.05879 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1341217a-df57-3123-b780-af5349975f98 | -8.35113 | -45.6501 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b94d30de-0dfc-30f6-bd13-09dd4104fbad | -6.65419 | -47.58052 | 2025-07-13 04:19:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c2beb03-dd93-333c-b770-9444fec3d53e | -7.31363 | -45.32463 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b98ee55-ff0b-3277-8861-9ac4f9a0c819 | -3.78732 | -47.09009 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1161acca-3543-38d3-84c5-9b1d8a2e8e3a | -6.45392 | -45.36121 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2690ccbf-33a9-3778-b4eb-3d5e6a5039b9 | -6.16164 | -45.91747 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9b2b713-5bb6-36c4-b9ac-c0233c0f1736 | -6.45945 | -45.36921 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08306e5a-8086-38ea-8d8a-4a98b94d3c8f | -3.75512 | -47.10964 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fffa6bd7-234c-3142-9dff-c9bc023a9243 | -7.1467 | -42.29373 | 2025-07-13 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10e71bd8-6307-3922-b6eb-743a2dce0f02 | -6.14137 | -44.09722 | 2025-07-13 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff76fc3e-2a54-3f6b-87fe-af89b6114125 | -7.32375 | -44.03418 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f035602c-5bb1-3116-904d-ba15a15141b5 | -8.04618 | -50.10364 | 2025-07-13 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f55d9498-f93c-3c9d-8c8a-c8aa353c17c8 | -7.33863 | -44.00384 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 902c4b11-edc2-3fd8-9712-c6f8fc93dad9 | -6.42822 | -48.54274 | 2025-07-13 04:19:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99d144c9-352b-345c-8810-413c7c5ec17b | -5.20703 | -44.35452 | 2025-07-13 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dd64c2c-21a4-3fbe-b73d-1f8450af39ab | -13.8474 | -46.8964 | 2025-07-13 04:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5b530a8a-3fb8-382e-8402-456ff80e448f | -13.14156 | -47.3243 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc2fd151-b616-36f8-8a2f-b18bb96c9709 | -13.88647 | -44.46383 | 2025-07-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19a6f0a0-481b-3104-908e-466012b01c4b | -10.72279 | -44.04366 | 2025-07-13 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d124b8c-01d9-3eb1-a4f8-f01ead16880b | -13.83852 | -45.89701 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8027840-9efb-3d3e-bea8-b4a198c3f692 | -13.12461 | -47.28391 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 651bbb00-ecf2-329c-a5fd-bbf0c5de1c13 | -11.56446 | -44.83396 | 2025-07-13 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9c3855c-5625-33d2-9e5e-8c0235351107 | -16.09936 | -47.98093 | 2025-07-13 04:21:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c31b7b0-7390-3ac7-8bfc-7f341a3ec050 | -15.08031 | -48.94397 | 2025-07-13 04:21:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f9081ad-badf-3c15-8b37-694e59c5594d | -13.85266 | -46.89818 | 2025-07-13 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 2d8c4445-5ac9-3a75-b01e-3af4f4a0f7dd | -8.9215 | -47.34405 | 2025-07-13 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e4db873-b7b5-32a7-805b-fabeac204277 | -10.59552 | -49.46563 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58e2dcee-8af1-30c6-bf74-474cf8e98df9 | -11.73448 | -47.46152 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eca29674-ce24-3e9d-9559-509d08e571ae | -13.16162 | -47.30572 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85446e88-5a29-3a37-98f2-abbf622e43a6 | -13.14133 | -47.28337 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b57c97d8-f71e-3b36-ac38-4b273b5d93a7 | -10.57108 | -49.12287 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50295c36-c983-3520-9a56-8e4266bdf45a | -13.84936 | -46.89764 | 2025-07-13 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 585ffedf-03c1-35e4-b784-cd840cace4ff | -13.14214 | -47.32068 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5089050c-c518-3147-bd03-71922a3e2427 | -8.91688 | -47.35096 | 2025-07-13 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a163d78e-f032-3155-b800-297f1a746bce | -13.02696 | -47.82981 | 2025-07-13 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69cd1b56-15f4-33d0-8953-706271d72866 | -10.57471 | -49.12343 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f8adc29-6ea3-3f20-afb7-125d4b7093bc | -11.73111 | -47.46096 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35981720-86df-37fb-abcb-4854ba7a8d4d | -13.88303 | -44.46329 | 2025-07-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3fbad55-abc3-3663-9505-2219b5d861f6 | -13.85322 | -46.89465 | 2025-07-13 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 506ef98d-5f18-30e1-812a-fa69bf620f25 | -9.79964 | -48.56777 | 2025-07-13 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 490505a6-497e-398a-9e91-7cc078b30ead | -16.07051 | -43.65043 | 2025-07-13 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55d86bd8-3375-3346-be3e-2b327db7c706 | -13.0248 | -47.82177 | 2025-07-13 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8508461c-a61d-3687-8f90-26e1bde646de | -13.83411 | -45.90361 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca2fe8ae-b717-32d6-af17-f6fd96536b6b | -10.56964 | -49.13145 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73b01cb9-fbbc-3369-9c0a-bd6c236f483e | -11.73053 | -47.4646 | 2025-07-13 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8d78a5a-98c2-399b-b9a9-25f02f45acec | -13.10847 | -47.29953 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cce5684-ea0d-338c-8f0e-33f7bf51e178 | -13.91285 | -47.41851 | 2025-07-13 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b6ccc5d-071f-3078-affe-e02898dd0330 | -12.07843 | -43.48405 | 2025-07-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0f36ef7-7f3a-3934-89cc-43b222158f02 | -13.28266 | -43.60811 | 2025-07-13 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b13cf4c9-36fd-31e6-87e0-dcb88ead2a65 | -9.11893 | -48.53187 | 2025-07-13 04:21:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b40bf2d-67da-3507-ad1c-993c68ff7a15 | -11.06746 | -47.1031 | 2025-07-13 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7025a185-4e3d-3b6d-bbe9-f96c9664a27c | -11.94404 | -46.3596 | 2025-07-13 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c063f06-5069-37d6-9a34-4afb176262e0 | -11.79871 | -44.88109 | 2025-07-13 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b4b058d-ff24-3b07-a267-4b776e5b995a | -12.61234 | -48.37223 | 2025-07-13 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3974f97-fd4c-3019-b1b6-025af15788c1 | -14.32011 | -52.74271 | 2025-07-13 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dce24546-0f64-3a16-9c54-630697e123bd | -11.72917 | -48.521 | 2025-07-13 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ebe5bfd-e061-305f-aabf-64ff90630d6a | -12.7086 | -44.40008 | 2025-07-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fd9bf6e-f0a0-310c-b057-5939cdfd3ef6 | -13.88074 | -44.45509 | 2025-07-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f120dc8e-77fa-3bc6-a7f5-3935b050fe3d | -13.84351 | -45.90877 | 2025-07-13 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8e3cd90-1972-37ec-a802-712c6d030d93 | -12.75127 | -44.41828 | 2025-07-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44b27ce3-d521-37e9-ac12-493fdaef5f31 | -10.05834 | -59.1093 | 2025-07-13 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27e13d46-eccb-313f-a963-1db26984bbfc | -13.9195 | -47.41959 | 2025-07-13 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35b16e01-18f6-3d5b-9c79-4710f3ae60f1 | -8.92894 | -47.34142 | 2025-07-13 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc9260d4-f5aa-32de-8e10-117f67844129 | -12.07494 | -43.48338 | 2025-07-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baf3daaa-41e1-38a4-aa98-77d82bd90329 | -12.02118 | -49.5252 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10bb9e2a-4fdc-338b-ae55-56e52a6f083f | -8.92492 | -47.3446 | 2025-07-13 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ad36984-3419-3df6-a755-4d0575a9a696 | -13.0002 | -46.26204 | 2025-07-13 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84ce9902-b25f-36d2-a0b5-3089ab3fe5ab | -13.11294 | -47.29285 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17dc8b1e-2df3-35ab-9a2e-4d31d7989a1f | -12.6089 | -48.37168 | 2025-07-13 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bb03d3d-82ce-38dd-96ba-df62a7142e59 | -8.92211 | -47.34032 | 2025-07-13 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4bcf9517-07f4-3f4d-961c-73c35b0fe8b6 | -10.56746 | -49.12223 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10b5b1d9-8448-3490-a1f1-51f55d247abf | -10.57399 | -49.12775 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4534db29-a4ca-3a72-9f52-ec914372e216 | -9.31927 | -47.79649 | 2025-07-13 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f5b344-a3b5-3229-8dc9-1073ae765d95 | -10.18377 | -49.50335 | 2025-07-13 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51b86fd7-d724-30de-9415-6896ea9c842b | -11.93486 | -45.76497 | 2025-07-13 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1aafed1a-a472-3511-8828-4b6b64a9dd6e | -10.50616 | -53.59112 | 2025-07-13 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33266ae9-114b-3852-858d-797f050e9b68 | -10.50732 | -53.58934 | 2025-07-13 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0df9be5-ca69-333a-8c58-d554e7986453 | -10.05018 | -59.11451 | 2025-07-13 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd9b21ef-2860-3204-9a73-f770f6ed918e | -11.42022 | -46.4255 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65decaec-174e-3afd-bee5-7c3eab8b178f | -12.44681 | -50.46855 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f1a6859-3441-3bfc-bd23-b3f827597254 | -12.42099 | -50.45907 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a624290-c0a6-3199-9d22-c700902e25e5 | -16.0699 | -43.65483 | 2025-07-13 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8d6a5f2-4bd8-31be-836c-7d36eb384335 | -11.01782 | -45.21114 | 2025-07-13 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efda985d-784b-3b11-9236-6abb2149c436 | -10.5025 | -53.58847 | 2025-07-13 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b41b5ab-3dd5-3797-af5b-6a65818469c8 | -10.64932 | -44.48601 | 2025-07-13 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb22b469-64a4-3d05-a87f-6b9f608f2f14 | -12.07573 | -43.48288 | 2025-07-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 566be091-8e39-3b2f-8bd0-7e3878d808a4 | -13.12405 | -47.28745 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef6814eb-548a-3a16-8956-508b6ab12de3 | -8.35964 | -51.07888 | 2025-07-13 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f11cd85c-9d10-36fe-97e5-51c986e76c50 | -13.1924 | -47.26284 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bba7f55-18f1-3070-82a6-92cab9b874e6 | -10.57036 | -49.12717 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccb66ae6-6646-3ecc-ae1a-5a9a19bedbb8 | -14.31513 | -52.7459 | 2025-07-13 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c0b31b9-2f33-386a-b353-b50501e771db | -8.80638 | -49.55431 | 2025-07-13 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9490f7b6-22b5-3c30-aeca-b9c01bea6663 | -13.19573 | -47.26339 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d7c58a-d93b-3d9f-a268-258fc72f8878 | -10.57327 | -49.13204 | 2025-07-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f4d6ddc-cef7-371c-8589-474dc2e9e59c | -10.95885 | -54.37403 | 2025-07-13 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f480eac-1493-37a6-81eb-cf5f90fdae2f | -8.88751 | -48.08832 | 2025-07-13 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c59aaaa-b971-3056-8f91-dff851119673 | -13.14331 | -47.31343 | 2025-07-13 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e954e32-c361-3352-a85b-41929d63d61e | -13.02142 | -47.82126 | 2025-07-13 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README8.md)
