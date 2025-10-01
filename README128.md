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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7570c20-c8f6-3319-824e-2ab54b8f5f80 | -10.80193 | -45.35665 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2ef1031-5f7f-3d8e-8406-111a8343b727 | -10.48595 | -55.58444 | 2025-10-01 05:10:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5086e8e-2807-39e3-a439-b69cd2d88ed2 | -9.44664 | -50.89979 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e222beee-48c4-33d2-991b-b376b7a91bd5 | -10.08945 | -50.19828 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78f54f69-34f4-322b-9b2f-81d06fb589cc | -7.48018 | -46.4754 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7cfc5e2-1a46-30b6-b317-34a4f7f809be | -7.81715 | -47.0675 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 154c4a74-8e09-3360-b93d-fb225f5588b2 | -11.47584 | -45.09767 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e15f2deb-097a-3071-b765-9c590d38323f | -13.33235 | -47.85514 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7cac904-7245-3d7e-a6a8-2e4aaf71e8ea | -6.58157 | -51.68283 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e34a84fc-46c2-3103-b11c-7d166492749d | -11.85178 | -44.99318 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bd64dbf2-4c87-3353-8e33-0e5489bcd2d2 | -13.20903 | -47.3363 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c36c6daa-8dc6-3bf4-9537-bce9d5f865b5 | -8.15794 | -46.26167 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d687ff3-012e-3d2d-adce-c7428ba02e55 | -11.60802 | -45.04347 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c34da254-01c5-383b-bdd7-46ef71fd8546 | -8.53393 | -44.71259 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6437f2ce-5514-31a3-a2c1-1662ef47fbd0 | -10.06554 | -48.19237 | 2025-10-01 05:10:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25f24c3c-c37e-383a-924d-368f481cb36c | -12.84807 | -46.95105 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a496400-68a6-3668-83b5-2c97ab8fc4fe | -10.64452 | -48.53274 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3a1c5d1b-46f4-3093-b8fe-086a12af5569 | -11.12632 | -49.78395 | 2025-10-01 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24610d4c-7c3e-350d-9a33-fb93b1f9338f | -12.95917 | -48.43858 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19399350-76fe-34ab-93b2-946ae6438a52 | -8.92602 | -47.58459 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a21c227d-12df-363d-ad97-d824fd232f59 | -11.85092 | -44.9887 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 23b6cb7a-be7e-3cd3-aadc-cda0655a3a2b | -12.88477 | -46.90835 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b858f51-4381-3004-bc40-6ed012bfdcbc | -13.55133 | -47.27332 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f10f68a-9538-3865-860c-89d23bebfd8c | -11.84477 | -44.99267 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 37134dc2-e3b9-33a4-8b14-c699e9465c32 | -12.03813 | -47.90884 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ceb9e59-b518-32e7-a429-9a87842c3ddf | -9.81728 | -47.86393 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 58c509bc-4a61-3f69-a164-0b2936333262 | -12.9539 | -48.43409 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f0572a0-e3ef-39ab-a5d0-279a48ef7831 | -9.58108 | -54.59437 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea2818b4-eacd-3a20-855a-bf59fecd6e03 | -12.95497 | -48.43709 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c103f83-d88f-3b7d-8e02-bcb3400c6ab0 | -10.63951 | -48.52798 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cfd75942-af95-3a9e-8648-4100af028cff | -9.55461 | -54.59718 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 470269d8-6b04-3706-a53e-f8ed82bcb395 | -11.76393 | -46.87451 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97e2c32a-2dfc-377f-bfc2-4ec62dfc3291 | -12.04354 | -47.91325 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91941444-70f2-37d4-b5e2-e87ac3b63520 | -9.98851 | -48.35396 | 2025-10-01 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 720626af-d928-35b5-b866-354d193ef106 | -8.50509 | -54.59905 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67a0b4ee-d0f7-3413-80a9-896cb48c9dde | -13.32371 | -48.15472 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fa0a59e-02e3-338c-9e04-0f6d296fa722 | -9.50788 | -54.66064 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7414ae35-c507-349a-82f3-1a712864dbc3 | -13.36861 | -47.29852 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85d8fa8b-fbe7-3a1c-ac21-f364ddf0f10a | -11.62637 | -52.24251 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| accd92f2-2191-3b93-b8e7-40a4c4c45d1b | -7.82828 | -47.07314 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c0f55f5-9d44-3f80-90ca-820cf9693ce2 | -11.43217 | -55.0543 | 2025-10-01 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15f9c3ef-df3d-3574-8b2f-0487c7dc29d9 | -12.1767 | -51.4203 | 2025-10-01 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e00d577-a107-3bd9-a5dc-c8239ac400fd | -11.5691 | -50.18327 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9258787-440e-347d-bcee-8d4d16345ff3 | -7.62715 | -46.67766 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 290cbf05-c7d3-3f79-aea0-117e30425652 | -13.33105 | -47.86691 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f60a3221-72f1-3dc4-aced-ade630a2f0ca | -10.19014 | -52.55171 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a69c8fd-4e34-3ca6-bf6b-7e88c1e9ade0 | -12.7821 | -46.88115 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 145c2374-3f72-3882-9159-ae1366980453 | -13.33344 | -47.81896 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3838bdb-c581-3e4f-ad73-61c5b06514c6 | -11.80916 | -44.99511 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb96fc4f-d107-38a0-ab5b-6df7047a0ee1 | -12.76166 | -46.89242 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2b0d072-a4a6-3e07-bebb-d94d7a6baf2f | -11.47338 | -44.99247 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e90ffcb-12f2-3b8b-8c8d-06f8a3a28736 | -12.82678 | -47.02792 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 717b6471-7008-31e9-989e-4995a060743b | -7.41823 | -45.41296 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12593877-2830-3eae-ae36-f36450576878 | -11.75443 | -46.83335 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0aff419-1573-3ea5-9cdd-6483dd2729fe | -6.03595 | -51.89369 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 532a3b4a-16f7-3f07-8b10-5cf059fa4bdf | -10.77689 | -45.37434 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8516eb52-7689-3920-ae6e-08ecef8fdb26 | -8.89974 | -45.04464 | 2025-10-01 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d13d9895-3b74-3513-aed4-6919ba3cad54 | -12.8534 | -47.01669 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64e42edd-7baa-3191-bb32-53ea0a0339a6 | -13.32037 | -47.33794 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4912bbc-9ac7-3be5-9bd1-8ed22396c9c0 | -6.57793 | -51.67842 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67a6a35-9144-3e8e-b431-aa714cd8536a | -13.38463 | -48.08425 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10f6f337-12b1-367b-9ff6-c90f278f1408 | -9.42907 | -54.71068 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88ff4495-8abc-3857-b6fa-8d01a4edbc8e | -8.55031 | -44.6442 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f1a9f1d-eb4f-3314-8320-ed05380a3293 | -10.47995 | -55.62413 | 2025-10-01 05:10:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d8ac93d-98e1-353e-94d1-933656aa8ca8 | -9.47639 | -67.89427 | 2025-10-01 05:10:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e94ce546-a333-3cc1-997e-0b006bcd6518 | -11.8494 | -45.00304 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ec9ccd3c-e04b-3990-bc80-1f2ca912f2bb | -9.41829 | -47.33643 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e09e0b23-c530-3b9f-8f61-a0a44383797a | -9.82577 | -48.26832 | 2025-10-01 05:10:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3def7a0-18ca-32e4-a9be-09f2ff64470d | -7.41103 | -45.41755 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cc263c1d-590e-3c84-966a-ef7f123ca73a | -10.07013 | -50.28247 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 68eb522f-3801-388d-8676-7f0455b7fa5b | -11.84552 | -44.98601 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5681ce87-263f-3ca9-b8e5-2883a94450ae | -8.38325 | -48.65055 | 2025-10-01 05:10:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a07c5e58-151a-300f-9554-26b6deacf5c2 | -12.94347 | -48.42416 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52c8d6f7-6f0d-336f-926d-dcc3206b7c40 | -6.95395 | -63.10872 | 2025-10-01 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8a54ce4-5a80-3444-adc7-39cf6a61b4b5 | -13.54008 | -47.27447 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c7f730d0-ce4f-30db-ad97-7adad225d1df | -11.80085 | -46.621 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 64652372-d5da-38b6-9a9c-730447de2e83 | -10.83298 | -45.3839 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77ae9bd5-3789-3fd5-a707-deaf9e4f298e | -9.48644 | -51.78812 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3416aa9-101b-3c62-8df1-ec16776d73d8 | -11.83236 | -44.97721 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35883f06-274c-38fe-8371-d7d3649ab5cc | -13.20875 | -47.33679 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1a6d9cb-d987-3de6-9b71-efdfe8a61239 | -8.26331 | -54.96222 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17c8ff01-9436-377b-a7bd-b37b1cae8a8d | -8.55251 | -44.73988 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 532dd9aa-b06e-3db2-9aae-4c556d3405cb | -13.30021 | -48.70646 | 2025-10-01 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d95c4e78-5a1b-32a7-bea5-078782cf30e1 | -10.06968 | -50.27348 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a2e0405c-63b8-3eb8-a1cd-06f56f842616 | -8.92423 | -47.58667 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f71ab629-a3be-3442-897c-1f390ed977fc | -13.29982 | -47.23944 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a09590b0-b218-3ef6-8037-aa9d76a82e2d | -11.91465 | -47.9062 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 508826ea-8995-372a-b141-51c18c0232d1 | -11.67227 | -46.96613 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7b02a975-e3af-3e04-a40f-8031ad6c5a9f | -11.83791 | -44.99074 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9aa941a-62e3-3a13-9d30-97d32ac824d0 | -11.33181 | -56.20947 | 2025-10-01 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d30dfbc9-9496-3956-8148-763fdefd8e0c | -10.1054 | -50.2284 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a570fd01-c001-3db8-a89d-cfba2088576c | -8.92504 | -47.59232 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e96a3459-cb14-344c-86d1-6434ae77e38a | -8.53575 | -44.70688 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e095703-01bf-3913-93d7-52e9091f4885 | -11.12593 | -49.78702 | 2025-10-01 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f09808ba-8a92-3b84-88e0-24f31d620ec2 | -10.57068 | -57.81012 | 2025-10-01 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f48f2db0-2bae-31dd-af4a-30865232190e | -11.82389 | -44.98971 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b7055f1-51fa-3884-997e-7e9ef62db0a2 | -11.765 | -46.85175 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f2ade16-f7a7-33aa-85b9-becdb8499304 | -11.15139 | -54.30981 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09dd322e-7b00-3e1d-aff1-5f002f4972e5 | -10.09707 | -50.2161 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac78b238-8532-394c-99d7-308eeef00366 | -12.43031 | -50.1834 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README129.md)
