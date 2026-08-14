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
| e7896dbb-f144-3a26-b856-6a5480df5b95 | -5.30569 | -43.06176 | 2026-08-14 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a97ab69-adbf-3524-abe9-9b8906a3dac0 | -6.60185 | -56.34969 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2879e92b-8fdd-3383-9ef6-0372adbd00fc | -6.61712 | -59.04845 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dc4937f4-4749-336b-b439-e7c81c8f47c8 | -10.72937 | -47.92376 | 2026-08-14 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 699e449b-2baf-33b3-a1cd-5569d4d9583c | -8.55182 | -54.59478 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89155af8-a0dd-39f7-84a6-5bde1fcc598e | -7.01033 | -47.97566 | 2026-08-14 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af0410d4-688a-3181-a675-4e93b8e1c063 | -7.45326 | -46.15115 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1fbd389-95c7-3825-b3ac-a9893983c7cf | -4.10232 | -50.45575 | 2026-08-14 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 293d9915-3f1f-32a8-9188-c769480d4450 | -6.77857 | -58.75271 | 2026-08-14 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee288c24-05d9-3d42-b668-f9d7bf3c5032 | -6.92632 | -41.99884 | 2026-08-14 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b830fe1b-0b96-3450-91af-18063301d100 | -7.39851 | -42.85749 | 2026-08-14 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6b48c26-9a88-366e-a437-196b6b2afd22 | -6.99916 | -44.82942 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b35a8813-c14a-3c20-ace3-74c8e43c5824 | -4.49087 | -42.55181 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2bb24fda-0106-391c-bd43-0a8984e1632a | -6.98428 | -41.29017 | 2026-08-14 04:32:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af9c4ee7-a86b-3724-b781-4b4fe530c498 | -5.75849 | -47.34499 | 2026-08-14 04:32:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd1142ea-f2ba-3230-b7d6-a77fbb403cff | -6.91923 | -43.64011 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b49cbaae-d770-3133-a1a7-964e19205827 | -9.49564 | -47.28615 | 2026-08-14 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7d44385-42d3-385d-b28d-9f88168daad0 | -6.77953 | -58.74749 | 2026-08-14 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a856f5bc-b63e-3859-a4b6-9c8b86f31051 | -4.49954 | -42.54434 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3fab63e7-0e76-3916-ba30-17b387d7c01f | -4.50188 | -42.55352 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43f3cb3b-2903-3c24-bab9-b14d1e7de763 | -9.49407 | -51.63136 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce911cb1-0417-3a3a-ae52-d6a385314e86 | -6.60377 | -56.3387 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfb56865-099e-32ca-b965-b7f23e6782b3 | -2.96353 | -49.20683 | 2026-08-14 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b3cac20-b16f-3b62-b0fb-9d19f8a0eaa4 | -6.20713 | -47.1325 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a614a4b5-edeb-31b3-b1fe-543d4e6cdcab | -6.99576 | -44.8289 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c8cd04c-9ece-318b-9c3b-9bc51ee6b0e8 | -6.6017 | -56.34314 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55d32c13-712e-3b40-924a-c9b5c69bada1 | -4.19269 | -46.80855 | 2026-08-14 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da3bcda8-de36-3a13-87c6-2fd7de91c75f | -10.19698 | -45.82223 | 2026-08-14 04:32:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b45b5f24-799b-348d-80bc-96fc1ae918ed | -6.11081 | -53.0758 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da3bc38d-007f-3cb2-9629-1cb5a379321c | -6.59343 | -56.35703 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d366477-7881-3a8e-bcf1-59371ad51485 | -6.91628 | -43.63552 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77ccd737-cec6-3c7a-9e37-74deb0e0857a | -6.5981 | -56.33147 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f916517-6b9c-323c-ae89-de50623e009e | -9.06054 | -50.62 | 2026-08-14 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76441839-a3d7-3d5d-8201-99279593ff44 | -6.605 | -56.33167 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf4425f1-7750-331c-aed6-5a6ca6b58ce5 | -6.99632 | -44.82523 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf87a6db-7e07-3863-b817-7768282ab0c9 | -6.19226 | -45.24606 | 2026-08-14 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 160444a2-32a4-33fb-9aee-e5b127bf42d2 | -4.71927 | -42.76903 | 2026-08-14 04:32:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e2c7216-c79c-393e-94df-6cb72de0b10e | -4.50689 | -42.54546 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f446b18a-accb-3180-9fe0-52ec25d6c84a | -6.60813 | -56.34653 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec8c28d2-fd62-38a8-929d-ade9336777e3 | -9.48645 | -51.6223 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8086be6-8214-3bda-afb2-dd4f85daec0d | -6.60364 | -56.33252 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f31590d-f9f7-3380-88a0-87879d306b8e | -8.55346 | -45.33564 | 2026-08-14 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30b364ab-96ea-34f2-97a4-5c59e74f5900 | -6.9121 | -43.639 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f950426-3ab0-3946-9c03-eef95dcc2c3a | -5.59386 | -37.74256 | 2026-08-14 04:32:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5bf63866-19ac-3d7a-9ec2-c02898d8183a | -6.9374 | -52.78949 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 372894a0-befb-33b4-9ca1-22fd667000a3 | -6.5984 | -56.36125 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d52c17dd-4152-3861-aded-54fbd88ac710 | -6.91271 | -43.63496 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ba786007-4a14-352d-9e60-5a1552f354fa | -5.96556 | -44.28782 | 2026-08-14 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4065d9fb-26a9-3311-9195-aff622c2daf1 | -6.40544 | -39.26508 | 2026-08-14 04:32:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 96f5cb45-7fc6-3acd-bff8-aa9f699710aa | -6.60983 | -56.33001 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2df7867-d360-3520-905f-352f9dad7a14 | -7.33161 | -47.8145 | 2026-08-14 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d9b4aef-7132-3578-87a6-78a7d566dcb6 | -8.7182 | -54.60024 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b369abcc-dfcb-33de-b1c8-e0b4bd9b9fb3 | -8.23731 | -49.96324 | 2026-08-14 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85e80afa-0250-387f-9317-f43ecf33b144 | -6.603 | -56.33603 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b218e94d-d5fd-3ea1-9f4e-70ba0bd8ffc9 | -7.60669 | -46.47124 | 2026-08-14 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3f1f8b8-e18f-35bb-9f60-d71f15b4ae33 | -8.55471 | -54.60612 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccd4061d-bd49-3180-bbc0-da1697b99857 | -6.95036 | -59.2997 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a7ca415-4323-3fea-8039-eb70bdba7f31 | -6.91814 | -45.73049 | 2026-08-14 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abd52333-a84c-372b-8548-9eaf4d607ed7 | -6.24219 | -55.62363 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc400b5b-bdb5-3c73-bdd3-e4e8f2c1889d | -5.73162 | -44.50732 | 2026-08-14 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d0661db-b029-398d-a212-9ff767572bfb | -6.59499 | -56.35612 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 672a91bf-267f-3b33-821c-cc02626ef198 | -6.91985 | -43.63607 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 582eeb2d-9b61-38ff-bfec-9ed094b4a50a | -6.24204 | -47.69847 | 2026-08-14 04:32:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42e91e42-64a4-3482-a66b-c068c8c514c5 | -6.6095 | -59.05293 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf379fe8-3a31-30ff-ab74-b9460ca36d6e | -6.61456 | -59.05364 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2f06fd2e-f52e-358e-9835-bdae88ce4fe7 | -6.5962 | -44.55767 | 2026-08-14 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e581eab9-88d0-3b9e-aa6c-fd1f2f701236 | -2.97353 | -51.6867 | 2026-08-14 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30cc051f-c5d5-3755-a091-41a4afe2d0c0 | -6.86586 | -42.92807 | 2026-08-14 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c9572ea-43c7-3495-b6bd-0295e408e825 | -7.70848 | -46.23461 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2bb3dd3c-7046-3b68-a23a-8c7d6bf60249 | -4.50756 | -42.54114 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| adfbd1ce-4a90-31db-8587-f88955a9d184 | -5.63011 | -47.10809 | 2026-08-14 04:32:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80f1f5f7-c266-30dd-b343-552d8d577778 | -6.80845 | -44.88405 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77368bd4-fd92-35a6-b947-37c935eb3423 | -6.77979 | -58.74872 | 2026-08-14 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7dda07eb-c3ea-39c8-b735-a78e52b124b4 | -6.90799 | -43.92575 | 2026-08-14 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf5b123c-632b-3584-ba57-7e526cafc2fa | -9.12628 | -46.39771 | 2026-08-14 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bce5682-7a46-3fb1-9edf-8c7129650960 | -6.26464 | -43.279 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcd8ab30-db24-366b-9495-680edb1cbcc0 | -6.61894 | -59.00169 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36b3628a-cd24-350e-bb50-4bf6b245a370 | -7.70462 | -46.23756 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5c74e2c-a388-37f7-a6b0-563cfb4a2045 | -2.95985 | -49.20622 | 2026-08-14 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34fbba40-b981-3f04-a61d-427f21b5dc3f | -6.60731 | -56.34383 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bac75ac5-01bd-3a4c-92d8-26bcbbd188f9 | -7.80779 | -44.11923 | 2026-08-14 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26206e80-fbc2-3273-bed9-ecfa60f09170 | -6.61117 | -56.32911 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cef91f76-1443-3886-982e-1d1db0f59a99 | -6.59821 | -56.33773 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df409d51-67f5-3b52-85af-720b87c99de0 | -5.24828 | -42.85496 | 2026-08-14 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5592cb16-0cf5-3fb6-8dff-94a3258bcbb9 | -6.88062 | -41.9553 | 2026-08-14 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a6acddd4-3f9c-3321-bd71-7022b7964c97 | -6.88109 | -41.95198 | 2026-08-14 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7958153a-1ebf-331e-b574-e2f9c3bd54ef | -3.26372 | -49.52889 | 2026-08-14 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a75ba65-c0e4-3262-86f1-343cce510c93 | -4.50021 | -42.54002 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 819e1b1a-a059-3e10-ae09-96dbe247537d | -4.50255 | -42.54922 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9e1d1b29-752d-3b08-9f03-95e676c60f41 | -6.8365 | -42.90748 | 2026-08-14 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 21252455-d64f-3564-a08c-003fccc62fec | -4.49588 | -42.54376 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| cbbb836c-839a-38b5-958b-e1c4d0a8fd99 | -10.73269 | -47.92429 | 2026-08-14 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5309befb-b7b6-323a-87c6-033969f92d4d | -15.51736 | -45.85744 | 2026-08-14 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 590a553d-8eae-3d16-b4c7-eb64d9cdd830 | -10.98271 | -50.54714 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9262da6c-e4b9-301d-ade9-c26f5378dfdc | -17.51048 | -42.37901 | 2026-08-14 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5f3d3cf-5e80-3bec-a387-f154828fd008 | -14.4507 | -51.85958 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61d89a35-be5b-30fd-9050-c7021db40771 | -13.25286 | -50.3795 | 2026-08-14 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74dd8e29-3ccc-3fc0-b558-d818db6dc294 | -14.95292 | -46.6119 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e93c9b-0c8a-3a55-92b0-c8d2533a1f40 | -13.90731 | -53.7784 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f25c90a9-d17d-3869-ac81-017a67e0a498 | -16.91104 | -54.1456 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
