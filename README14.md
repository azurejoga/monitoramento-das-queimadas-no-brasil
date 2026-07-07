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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14039cf4-c905-3dcb-816f-d3b4830c4f33 | -13.2724 | -54.23594 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ca1cbb0-ebba-3442-afd3-4ce9d91b1a12 | -10.93629 | -43.06487 | 2026-07-07 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 39c7f780-618f-3cd2-a149-275af942f57b | -11.91972 | -43.37761 | 2026-07-07 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 187d5f9c-a7b2-3982-812d-4552a60d5119 | -12.75916 | -44.55826 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e28f9c7-0322-3e7e-8430-48ef233ca5d0 | -12.78689 | -44.51199 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 05c03560-71d3-3c85-a411-8241ca18fdf5 | -13.27368 | -54.35641 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa47afa3-16c6-361b-a0f3-0e14d9b74bbf | -11.66599 | -44.56097 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35613f48-b65a-39b3-a669-483df594775d | -9.28563 | -49.5839 | 2026-07-07 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 991cfe02-4069-3592-8ed3-273595eb7310 | -11.6321 | -46.36528 | 2026-07-07 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdaee786-1c00-3cc3-beb4-caaebc216e07 | -13.27435 | -54.35308 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 570c4e8c-d587-3254-9c24-4a30974319aa | -11.67706 | -44.57722 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f96c254-edb6-34d6-b74f-82c0bc3289e7 | -12.6809 | -47.67732 | 2026-07-07 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b3c6a6b-53ed-34a7-859a-3dc690bf8a30 | -13.27902 | -54.35758 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a53665d6-ad6d-3721-b270-58f12499594f | -10.93236 | -43.06796 | 2026-07-07 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bbfcf46f-fbf2-3f62-9854-91b646600b0d | -12.79245 | -44.49837 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e68a427f-f4f3-3318-8d01-751fef33db15 | -13.28903 | -54.36315 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 327d4425-a995-3069-a552-13f326c5aef0 | -12.79078 | -44.509 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55fc7566-27fb-3782-b10e-0d523a57681b | -13.325 | -54.37827 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 266fcaea-2858-3661-ab83-e5da5e6cc810 | -11.66376 | -44.57505 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cde4d41-40d6-31d4-bafb-87fd066517d3 | -12.75971 | -44.55473 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b16e90a-1eed-3889-a5be-46598ec75b1e | -10.3175 | -49.919 | 2026-07-07 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 117fb81c-ad6a-37fc-98d1-8dd0e81b0c31 | -11.66711 | -44.55393 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a15128ff-76f7-3a10-ae66-c3b2eadfa1b4 | -11.67817 | -44.57018 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfe43aa7-d388-35a0-a772-f41dd8f5b817 | -11.99259 | -45.1427 | 2026-07-07 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce63cb14-7eff-3cda-b6fb-cc6b5af00402 | -13.30441 | -53.34642 | 2026-07-07 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbff33cb-976f-3c99-9ffb-d2e54b51f415 | -15.50849 | -42.20122 | 2026-07-07 04:25:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10f4c7fd-c89b-3abe-89ef-109e63f4db48 | -13.26312 | -54.22691 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a02eb992-9394-325e-a252-16060158363a | -13.25782 | -54.22582 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98962c62-4dcf-32d0-a926-8ce920ea760e | -11.69773 | -44.12921 | 2026-07-07 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 049ae568-2028-3113-884d-240edce07903 | -12.78524 | -44.50083 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 662174ba-a645-36ce-abca-54b40f458ab1 | -13.27835 | -54.36091 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b217feeb-d115-3fc3-83b4-f4df28b98ac8 | -11.66044 | -44.57451 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46bf626b-50ef-3c4a-97f9-ef1eeb2a881b | -11.6682 | -44.56855 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a94c7e2-c881-3a3b-a3cf-0ceb5b66a3ba | -9.28632 | -49.58004 | 2026-07-07 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d27041e-8784-382e-8dd4-3d05c725139f | -11.68094 | -44.57425 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d3fb25d-5eeb-3d17-9b75-d933f4c4c523 | -11.68317 | -44.56017 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d042fbbd-4ebc-33e5-a9d6-ed1c66cd49d5 | -9.37729 | -44.71637 | 2026-07-07 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9126245-78b2-3b69-953a-d2d653b340d3 | -11.7005 | -44.13328 | 2026-07-07 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fa18c9d-01e7-3903-88a9-15371eb41feb | -11.62464 | -46.36786 | 2026-07-07 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4c9a5cb-918e-32e0-ae7d-4f447ef00077 | -13.27194 | -54.35283 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64bad269-5d37-3227-a4c0-e77b7f946d06 | -9.20605 | -45.31818 | 2026-07-07 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b828b60b-776e-37a9-b313-54a9bcfae7d7 | -11.69094 | -44.55421 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8026f4f5-26fd-34b5-b23a-e5468a8c5c25 | -13.28103 | -54.34749 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e74cb2f-cf98-309f-b90d-0d30a25846a6 | -11.67376 | -44.55502 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 80772ce0-3b35-35cb-a24d-69b8774aba53 | -13.54554 | -52.91348 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cb6c98c-c9e5-38dc-acd9-84490e6f4ac3 | -9.37616 | -44.72342 | 2026-07-07 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3eb16bb6-817a-3c5f-95e7-351f1e75e156 | -13.2671 | -54.23483 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ca996c9-dccb-3241-9a02-2bb042de4697 | -13.32568 | -54.37478 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6022ed20-1b35-36cc-803e-a5a3d3060d76 | -11.67097 | -44.57262 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e26e7e97-8b3a-31f1-a3c4-5c69f0efd1d5 | -11.68928 | -50.38689 | 2026-07-07 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4390919f-2f9b-3207-afe4-c6dc379c826c | -12.7941 | -44.50954 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 761be6d1-d29a-3429-b721-9616274b9c70 | -13.28744 | -54.39914 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5e433b-3cb6-33a3-ad8c-21330cd5eab8 | -11.66267 | -44.56043 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e351461-9814-3d40-8878-10ca8a41f676 | -13.25972 | -54.34286 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| adfb16a3-4b88-313a-87e6-21af5e71c1c3 | -11.69717 | -44.13274 | 2026-07-07 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c2d5c8e-a08b-3744-ad55-00de5f0015af | -12.79354 | -44.51308 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6f2f80-c75c-3e5d-b874-d0b92e27bb20 | -9.21883 | -48.55601 | 2026-07-07 04:25:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75562fe5-fb2d-3c38-a775-4aaebb5b5eab | -11.44963 | -52.92938 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80d85cc9-e6ad-323a-9433-19ea28fbb983 | -13.53482 | -52.91702 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea995593-cceb-3c0b-b5ef-bc9537045141 | -11.66099 | -44.57099 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b4d4bcc-4c54-3679-ab1c-613b6a6c9734 | -13.26661 | -54.35163 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ae5073c-0d18-3736-bd91-18e58035d303 | -10.6938 | -49.60923 | 2026-07-07 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa309fd7-93f9-32d3-8370-21f571dbb416 | -12.65889 | -46.9986 | 2026-07-07 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79617b41-2c13-3fdc-9217-7fddadee41d5 | -13.26836 | -54.35524 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9114a3d-4501-3934-9e6d-2e508197e16d | -11.67985 | -44.55962 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3e8a65e4-ef86-3d7b-88ca-1ce31976fbc8 | -10.3182 | -49.9151 | 2026-07-07 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d54734c8-846b-3df8-9ef9-79ea12ae107a | -12.78912 | -44.49783 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 48cd65e2-a848-3820-9e09-fdef00f6eedf | -11.72732 | -49.8477 | 2026-07-07 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c3f65e58-67c1-3a37-95a5-da06c6475884 | -13.30556 | -53.34047 | 2026-07-07 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b15ea9fa-7f64-3b15-9663-d2f880761248 | -11.68373 | -44.55664 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dbb41e9-a737-393a-848d-4f95f6a0dba1 | -11.66155 | -44.56747 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6da3da11-a758-3f3e-9741-dfef60eb45f9 | -13.44081 | -43.85439 | 2026-07-07 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd16af32-a5aa-322e-ac88-5e206d263199 | -9.30955 | -51.91405 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03a560af-759a-30b4-aed4-828042a898cd | -11.65546 | -44.56286 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86f30953-af7a-3e5c-865e-d79b289e76cc | -13.26505 | -54.344 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a992c91a-2ae6-3b6a-b6bd-7227d387ece5 | -13.2604 | -54.33947 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ad83bebd-90cd-3b9d-961e-ab2984433536 | -13.26259 | -54.3437 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b3910f90-b85f-3181-b6da-926bbd0803a4 | -13.27532 | -54.3641 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e50bcb58-9178-3d3c-ac17-d99fee2f5ac7 | -13.27466 | -54.36754 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f995708c-e3a5-3baa-b10a-64cce3c652f4 | -13.31179 | -54.36061 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8217107-09f2-3325-8840-833b1d67b731 | -13.44416 | -43.85496 | 2026-07-07 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec6d9119-e3bc-3ffd-b446-11f697d77b1e | -11.66929 | -44.58319 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 674fc50e-dd77-3e9a-a0cc-0d44f176625f | -13.28571 | -54.3519 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62603d72-475f-3424-8412-5ea8bd6f646b | -11.63333 | -46.35781 | 2026-07-07 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bca75e1e-bcbe-3ac2-b32a-65875c51dd9e | -13.27388 | -54.34277 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a144341d-067d-304e-a0ce-a89708eeaed9 | -9.37786 | -44.71285 | 2026-07-07 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfff4923-7c0a-32af-b51b-420d3d6be2d4 | -22.38264 | -49.79295 | 2026-07-07 04:27:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0def268-bd78-383f-ab2d-443d02fc6989 | -21.90234 | -49.45369 | 2026-07-07 04:27:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ef9594f7-ae6b-3787-933e-459fea50615d | -22.28241 | -46.86616 | 2026-07-07 04:27:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f447a83-b2eb-36ce-9c4a-d5be67672427 | -21.44899 | -47.90118 | 2026-07-07 04:27:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7cda063-006f-3c6d-a151-f77e9fe9267e | -22.82946 | -47.14759 | 2026-07-07 04:27:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cca0c5fb-b09e-3c6a-a1bc-d4f1edb9fde2 | -22.02489 | -48.22575 | 2026-07-07 04:27:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a705cfb-2454-3eb7-9583-230108018134 | -18.08911 | -54.02605 | 2026-07-07 04:27:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a4aa99f-e540-3e12-b9f6-fd6942dd3049 | -19.85082 | -49.07531 | 2026-07-07 04:27:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 891002a8-9d8e-396d-aea5-95999fa7797d | -16.65443 | -49.51104 | 2026-07-07 04:27:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30aefda5-db6f-3699-92ce-e4c276897ede | -21.25531 | -49.17752 | 2026-07-07 04:27:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f37dbcef-4fd5-3c99-a0e9-3b7ed44e7818 | -18.19408 | -46.2387 | 2026-07-07 04:27:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ac0b2fc-9672-37e5-a9fc-51b4f1a9a956 | -21.50881 | -48.81847 | 2026-07-07 04:27:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11d36f37-d50e-3212-859f-83745188c092 | -18.0926 | -54.02859 | 2026-07-07 04:27:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 957c2e31-e3c3-3f35-a73e-1ab24a1bf9f9 | -22.27908 | -46.86555 | 2026-07-07 04:27:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README15.md)
