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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78e97425-55f3-3322-bf90-90170f200f85 | -20.57155 | -54.57874 | 2026-07-19 05:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63a4a67c-ed52-3dcd-8561-44a953f6cc1c | -20.5297 | -57.4009 | 2026-07-19 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 836003cf-0a00-3fec-86e3-46dc4d37d189 | -16.49314 | -52.72442 | 2026-07-19 05:08:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4def41fa-875b-35f9-b527-2189b61002e5 | -16.32123 | -54.76138 | 2026-07-19 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5bfda5bf-8043-3cb4-8bd8-1629eea1be51 | -16.80776 | -54.58918 | 2026-07-19 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 21a67794-bee2-32b2-a0aa-d020c00dc039 | -20.5722 | -54.57371 | 2026-07-19 05:08:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de5f712e-b1da-358c-927e-04ba3c25da9b | -15.43294 | -55.93679 | 2026-07-19 05:08:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdccce6c-da09-3762-97c5-3bc95174edd3 | -22.2523 | -52.87803 | 2026-07-19 05:08:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b5ad4236-f260-38b1-9e5f-d0766454ef2a | -20.5376 | -57.39431 | 2026-07-19 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77fc59a5-e614-3aa6-98d6-b961234841dd | -18.73293 | -54.20193 | 2026-07-19 05:08:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c17c5173-5a71-3d6c-a447-04aa88ce8c0a | -20.53083 | -57.39318 | 2026-07-19 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed2df31f-f28e-345e-89ac-e3658b84ac29 | -15.95845 | -47.19002 | 2026-07-19 05:08:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2220fd7c-2377-3159-845f-01f22f9fd59a | -15.60771 | -52.96131 | 2026-07-19 05:08:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7d30493-7ad8-3004-827a-689d3a57dd57 | -15.43636 | -55.93731 | 2026-07-19 05:08:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef17c44f-da55-3c91-8f31-8ee3f7d54986 | -22.25667 | -52.87857 | 2026-07-19 05:08:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 93b519de-e8a4-3e39-8769-1bea29ab8852 | -20.52631 | -57.40034 | 2026-07-19 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60f107ca-943e-3fe0-bd60-24095e0932e6 | -15.43861 | -55.9221 | 2026-07-19 05:08:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c90a37c-b416-3507-a93d-100f65bb2583 | -21.5348 | -46.76344 | 2026-07-19 05:08:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ab13c589-18ef-35f3-91ac-8b6bab6ade45 | -15.60842 | -52.95595 | 2026-07-19 05:08:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b0f257e-0705-30c0-b733-baf3babaeceb | -15.35259 | -59.99433 | 2026-07-19 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81400b57-d826-3d89-8b1e-e55e3217867d | -15.43805 | -55.92591 | 2026-07-19 05:08:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd595797-aba4-3209-b9f0-6106d01a4ddb | -21.53702 | -46.76275 | 2026-07-19 05:08:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fa776e67-fa41-30c3-8726-40ebc6bcd1fc | -13.6764 | -48.7786 | 2026-07-19 05:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f024efcb-e4f9-3c83-af86-bc322bb892c4 | -22.23049 | -56.01327 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f13aa66-8002-3ce0-8973-92244b411279 | -29.07109 | -50.721 | 2026-07-19 05:10:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9f653a1a-cefa-36f8-913d-ce7b8feb8843 | -29.36014 | -51.09413 | 2026-07-19 05:10:00 | NOAA-21 | NOVA PETRÓPOLIS | RIO GRANDE DO SUL | Brasil | 4313201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 19013657-91b3-35dd-b3fc-344b5b389085 | -22.25836 | -55.97164 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 55303384-1dfb-38f3-8be8-3e1f0a7bdb26 | -23.14247 | -49.06073 | 2026-07-19 05:10:00 | NOAA-21 | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb5ee661-ca0e-3735-8364-fbba2aff6763 | -21.99826 | -56.02253 | 2026-07-19 05:10:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| faa99735-15e1-303e-9602-bc682703c9ec | -29.54013 | -53.73594 | 2026-07-19 05:10:00 | NOAA-21 | ITAARA | RIO GRANDE DO SUL | Brasil | 4310538 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7022429c-4768-3745-9d96-87e438237b5e | -23.76972 | -53.27906 | 2026-07-19 05:10:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 043d1b2a-5b74-3868-a698-741ba9e5b358 | -22.2547 | -55.97121 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30f72c72-7a0a-3e8b-a4d7-03414c16affd | -22.0055 | -56.02361 | 2026-07-19 05:10:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e9344bdf-6924-372b-a4a6-384ce71fb004 | -22.22926 | -55.99483 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29675635-b638-381c-9678-bf09831beeb8 | -22.00129 | -56.0275 | 2026-07-19 05:10:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a0a5e47-30a1-3800-9f3d-3d103af44143 | -23.76538 | -53.27851 | 2026-07-19 05:10:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 65985989-41a9-37e3-bc20-4f56e7b7067b | -29.54888 | -51.39102 | 2026-07-19 05:10:00 | NOAA-21 | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 600b3d56-577c-382a-a46a-1950c59f1976 | -22.22562 | -55.99432 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75106bdf-b027-321e-92d4-0347d1bd6974 | -29.01818 | -54.50082 | 2026-07-19 05:10:00 | NOAA-21 | CAPÃO DO CIPÓ | RIO GRANDE DO SUL | Brasil | 4304655 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 8db45e63-9c58-384a-a4db-d89a374b7f66 | -23.14211 | -49.06478 | 2026-07-19 05:10:00 | NOAA-21 | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 85b7c467-abc3-3eb6-aad3-7a6ab996efbf | -28.66438 | -51.06882 | 2026-07-19 05:10:00 | NOAA-21 | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9fcd2c8d-910f-3465-a62c-1a894360902e | -21.99464 | -56.02198 | 2026-07-19 05:10:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75426445-d70b-3482-b5bb-184ea56659b4 | -29.24071 | -50.67376 | 2026-07-19 05:10:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e0bd9402-2c9a-3cf2-ae42-3fd6bac9ee21 | -22.25898 | -55.96709 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 311d1b80-7893-3a45-86f5-04d6d7a84a33 | -23.76543 | -54.58731 | 2026-07-19 05:10:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b86a8754-acea-3484-8934-07414841e8ad | -22.0049 | -56.02808 | 2026-07-19 05:10:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 93fd673c-5861-3d28-b903-47e1b80406ed | -23.76587 | -53.27415 | 2026-07-19 05:10:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7d8b69f5-407b-35ec-91a0-fe56f9b26e86 | -22.28114 | -56.08256 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab022eec-b19c-3df4-82c3-f86cc9cf5264 | -29.53918 | -53.73541 | 2026-07-19 05:10:00 | NOAA-21 | ITAARA | RIO GRANDE DO SUL | Brasil | 4310538 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ee67ef55-7f6d-336e-9a0a-a6726f1ad53a | -22.27752 | -56.082 | 2026-07-19 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39e1938a-bcff-3afa-aa5c-74a38b5bd4e9 | -29.63345 | -50.4744 | 2026-07-19 05:10:00 | NOAA-21 | RIOZINHO | RIO GRANDE DO SUL | Brasil | 4315750 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 85f7ca92-2f12-3286-83e4-8933d515048b | -22.00188 | -56.02307 | 2026-07-19 05:10:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 40914883-b749-319a-a05c-766439af9548 | -28.591 | -53.62128 | 2026-07-19 05:10:00 | NOAA-21 | CRUZ ALTA | RIO GRANDE DO SUL | Brasil | 4306106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 866d050d-28e1-3917-b273-637a0a73967b | -13.6764 | -48.7786 | 2026-07-19 05:20:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9bd76cda-457e-3faa-ae00-769a2eb5f2cb | -10.7094 | -46.6232 | 2026-07-19 05:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 87154ab3-ad6d-3bb0-a93c-94cc5bedcffd | -13.6764 | -48.7786 | 2026-07-19 05:30:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e042ab7d-b43f-3c0b-9512-9689e684b727 | 1.76687 | -60.23188 | 2026-07-19 05:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79ddbc7a-4969-372b-bd42-e765d9fa4623 | 0.75609 | -60.45427 | 2026-07-19 05:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac0a52c7-233c-38e6-8329-690e03609469 | 1.77018 | -60.23135 | 2026-07-19 05:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3e83023-2ef2-3e77-a097-8f077b278695 | 0.96921 | -60.41032 | 2026-07-19 05:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd0cc970-9091-3f11-aa0d-c76c4601c356 | -10.7094 | -46.6232 | 2026-07-19 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 02ffeaa3-5cec-3821-ab6e-f4cfddb29577 | -13.6764 | -48.7786 | 2026-07-19 05:40:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 106de71d-40eb-366c-94c3-7410af07c2af | -9.10339 | -50.61196 | 2026-07-19 05:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e5d1f53-b4de-371e-86e6-590e6751de7c | -2.7883 | -49.52642 | 2026-07-19 05:40:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27183e75-5fce-3c5f-9724-0bbe0fad4e96 | -9.09614 | -50.61668 | 2026-07-19 05:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cad6a510-93b6-3963-a148-8df9a1553eaf | -7.69254 | -55.36596 | 2026-07-19 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc8cd3de-5be3-3759-896b-ed71a46722ed | -2.71371 | -59.77002 | 2026-07-19 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88443902-be85-3f4e-b962-17fa42bf99c1 | -2.80137 | -49.52599 | 2026-07-19 05:40:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22a32add-aaf5-319a-8a51-5f877889dbfd | -4.03738 | -49.25127 | 2026-07-19 05:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b71637d6-3a2f-309c-9df8-4a921e81ec4c | -7.69325 | -55.36102 | 2026-07-19 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edff471c-e097-3a74-8316-9b359f5871f0 | -6.89172 | -59.01382 | 2026-07-19 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2551142b-5578-3f6c-881b-5bc6866e042c | -6.13043 | -55.80753 | 2026-07-19 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2f0f9fb-dbad-3b49-9253-758b7455aff6 | -2.80121 | -49.52827 | 2026-07-19 05:40:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83271570-d8ca-385d-9bf8-4cac908e5059 | -4.03655 | -49.25711 | 2026-07-19 05:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a114bac0-eb02-307c-a245-8c246323f77c | -7.80853 | -63.83633 | 2026-07-19 05:40:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2383d324-6c3b-3ebc-a855-a34270c8f17e | -9.09705 | -50.61678 | 2026-07-19 05:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fd996dc-bca9-3580-b432-53e64d698344 | -9.10434 | -50.61205 | 2026-07-19 05:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2139ddc-7e60-35c0-bdd3-e2cffeaf5741 | -2.79475 | -49.52735 | 2026-07-19 05:40:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78b0c360-07b2-3593-9792-a18a34b6dd1a | -2.77781 | -49.46473 | 2026-07-19 05:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 44784b1c-713c-3be2-bc13-cb46fce60346 | -10.89472 | -50.31575 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c60e065a-8748-3750-aca1-f0c21ecc2b15 | -9.91428 | -63.06881 | 2026-07-19 05:42:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37802eb9-0170-39a4-ace4-c2c7eb61d182 | -11.68075 | -54.58499 | 2026-07-19 05:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90787254-45d2-38e0-bb7e-ead6798abea6 | -10.8203 | -50.23706 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88866344-14eb-3658-8e30-5c5b71d2c6f8 | -10.89362 | -50.32233 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2116cfd8-c0dc-3882-8a29-0538bf723bf1 | -15.43702 | -55.9239 | 2026-07-19 05:42:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 07885254-beb7-39f9-8410-47d73906863b | -12.07784 | -53.3549 | 2026-07-19 05:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 97f9f4b3-78d9-32a8-9c4c-c28ea407a2d3 | -9.91919 | -65.00636 | 2026-07-19 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88232eee-94d8-337d-80b8-7840a2ac3afe | -9.48023 | -57.32156 | 2026-07-19 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31b0a8cc-cdba-3389-9383-dabc9182c8fc | -9.15944 | -61.41161 | 2026-07-19 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd3d85e0-70b8-339f-9b91-1e86ca1c88da | -9.4766 | -57.31804 | 2026-07-19 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6ebdab2-00f3-3287-b936-7beb88a1b846 | -15.44209 | -55.92448 | 2026-07-19 05:42:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 58c5ede6-a556-3bb1-8eb0-94a98a767fdc | -15.60619 | -52.95993 | 2026-07-19 05:42:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 927f6fbb-8307-3896-ae9c-31851303ebe6 | -9.09923 | -59.40244 | 2026-07-19 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8f0367e-bf99-3adb-ae1a-a00a83b622a7 | -10.90014 | -50.32908 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1595945d-7fa2-3012-a6df-322b7f5dd1f1 | -12.07833 | -53.35088 | 2026-07-19 05:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53c0c745-3e6f-3568-9ab2-c928d40263aa | -10.81345 | -50.23618 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 408f6bb8-ebb6-302d-9de5-df1a95ee4909 | -11.99556 | -50.57666 | 2026-07-19 05:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80315719-c452-3210-a3d5-e6ac309c567a | -10.82101 | -50.23081 | 2026-07-19 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1499babf-8e15-359f-9c3f-b6811506f0fc | -12.16078 | -59.76424 | 2026-07-19 05:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 452d6219-c670-3418-b717-8ce673e4b413 | -9.47601 | -57.32092 | 2026-07-19 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
