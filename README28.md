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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 324821af-ec03-3811-b947-3b59315d58b6 | -11.81966 | -46.42818 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b539f3e2-882d-3ac6-b1a2-f2d31d70bd1d | -11.81375 | -46.43833 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 78e44b90-d3f7-3a33-bfdc-6ea5ed399c4a | -12.82165 | -48.08212 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f58e113-8004-3353-b978-219b30fffbdc | -18.05995 | -45.95916 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb404ca8-be81-3650-bdc9-bb0d613f4834 | -15.96288 | -43.90268 | 2025-08-31 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c610b484-b7d9-326e-a714-a8c203e92597 | -12.091 | -44.72136 | 2025-08-31 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e1604fe0-a4fe-3e2c-abfc-75246947349a | -12.83928 | -48.085 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e2ba8949-1f5e-3afc-9f7c-c2e25b79f576 | -10.95788 | -50.8559 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2e08309e-e95d-37ee-b1ce-e13167f3ede7 | -13.99063 | -44.53509 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd48cfa6-49fb-3714-ae39-85579cee2be3 | -11.81249 | -46.44547 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff11239f-a262-3544-9752-1235c68440f6 | -10.23994 | -54.98064 | 2025-08-31 04:04:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10c237c7-f4e2-32fa-9ae5-b9cf7149cde5 | -10.96185 | -50.86024 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88dc7b6f-bbdd-35a2-bc74-2ede50565d38 | -14.98742 | -46.70628 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef8c7940-ed5e-3f9c-a003-3f361c96d8ed | -12.4024 | -46.46945 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e5144a8-4819-3073-98cc-2e688afb03d6 | -13.34211 | -46.94318 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 508b898b-9ffd-3669-b827-1df06ac75f03 | -12.56302 | -44.79432 | 2025-08-31 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8043c174-ef21-33cb-b9c9-3ea4c53132c4 | -13.35035 | -46.96715 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e3eefe5-e89a-397b-8444-5e34c624f0f8 | -12.41495 | -46.46811 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af9ee619-e4f5-3f1e-aa6f-8f5a0aa78480 | -16.22189 | -52.69338 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 42d5bdc9-ab4c-31ca-9399-356afd14c351 | -14.33607 | -51.87547 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d0c4065-1d6c-328e-a654-6915f3a1ab6c | -13.36865 | -46.95819 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cc45ab2-f892-3367-80b0-3d1a18ae2c85 | -11.86459 | -46.5035 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bbce432-67bb-32d8-91dd-f2fc5aedc65b | -16.99759 | -49.33251 | 2025-08-31 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8058ec2-a418-35f4-9709-6fc739b417f0 | -18.4421 | -47.23244 | 2025-08-31 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 313bfcd9-a026-34de-9cd6-0cf8c997d56e | -13.32715 | -46.86452 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f82e69e6-14b7-30e1-beca-13c59edde495 | -14.34574 | -51.88193 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08f2a7ee-42da-3205-82de-48f580a1773f | -14.84811 | -46.74173 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18aeb813-647a-3ec2-88e2-261c873deff3 | -17.2029 | -46.99229 | 2025-08-31 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d83c94a3-d7e0-3bc4-a695-32c357722af9 | -10.96663 | -50.86489 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10908f80-be9a-3113-bb9a-4a6c66311d0f | -11.84293 | -51.49378 | 2025-08-31 04:04:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9c306a00-01d5-3f84-aeaa-29c2c1bc701f | -17.62098 | -44.25538 | 2025-08-31 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2472dbc-1146-30ba-888e-d87c47823e55 | -17.8682 | -44.30973 | 2025-08-31 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 627efef5-10f3-3251-8718-54c55ad29150 | -11.82029 | -46.42459 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7f2b1c7a-a113-34f4-b91e-a2e4e88bddb6 | -13.53846 | -46.97135 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c24f49e-a449-38b6-81a4-be8d0ff12d5a | -11.79801 | -46.45721 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5dcb80a-6b06-3be1-8478-a3d0e1a947d8 | -11.86275 | -46.51423 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b3f5841-346c-3044-9f09-969370d03ea5 | -18.12168 | -44.98838 | 2025-08-31 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8888968-bfae-3367-8527-e075fce66584 | -13.98771 | -46.31292 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8595fc6f-0ffb-3a10-8cb1-4e6c7f282688 | -13.34231 | -46.98869 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e420c33-8de8-3c34-83ba-814579d5c3e2 | -13.97698 | -46.31911 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aca9fbc-13f3-3db8-84be-52eae8739e7d | -13.68804 | -46.88417 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fd4300d-ab5c-39ba-85a6-0c4f642d3251 | -15.00069 | -46.70402 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53168e66-39e8-37f7-bb11-da2e94f4797c | -17.96889 | -42.98589 | 2025-08-31 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4a0fae03-8fe5-3ec6-8c89-970bd2c50700 | -13.3546 | -51.75765 | 2025-08-31 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64f77d78-62e6-301c-80e7-2b0997104eb9 | -11.81003 | -46.45952 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2386f32e-8533-30dd-a0f6-d4d9a671a375 | -11.81503 | -46.43105 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0d85e2dd-4417-31c9-9f26-f5afb9f338c4 | -11.55792 | -47.62036 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a21ed869-6ea6-3c79-a57c-185cc4bbcf91 | -14.00134 | -46.32568 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a801e7-cfdf-3687-b2fa-788183747200 | -14.5309 | -51.98549 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb8e31a2-bbaa-3e9e-8158-d755437349b9 | -13.48699 | -46.83515 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98b7739a-ad4c-365a-8d14-ee1d1a9876c5 | -11.89587 | -46.38046 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd80730c-4fb0-3f29-b4cb-70a2721cf92f | -17.73836 | -39.52452 | 2025-08-31 04:04:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| faab5c51-1fab-31c2-9c5b-536b5f22e97f | -14.34624 | -51.88148 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fd5805d-80db-3c91-93e8-95aff6fbc8e7 | -12.55869 | -44.79797 | 2025-08-31 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95d86e50-a0ec-3265-a0f9-7b2f5190d076 | -11.84043 | -46.42761 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d293522-cf32-33d8-9a8b-3c43df06b18a | -13.46458 | -46.9376 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 751195f6-b5df-30e8-b508-9d8bbec49020 | -13.47209 | -46.96556 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a51b8e90-54da-3be8-8eaa-e453e49a79ff | -12.83358 | -48.14132 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 433d2265-f4f1-3393-8510-6f3b51eca48b | -14.99365 | -46.69859 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06aa7e45-7e75-3e5d-8b04-0ab3b7d44274 | -13.35703 | -46.95313 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d793549-4956-3791-9e83-ba2b55515130 | -13.39538 | -46.94857 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e583c972-8cc9-3404-9a62-6dcef9912384 | -13.3646 | -46.95751 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26fd4497-d9fb-348d-b1ac-83ebb6bf2d7f | -11.56379 | -47.6125 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6f89705-8f67-3bde-ba4b-e5703bc7eead | -11.82432 | -46.4252 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f069253f-e176-3eaf-b1d1-47d3fe07c851 | -10.95382 | -50.8477 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b3e13559-d3db-355f-be54-2fd5e265ad98 | -12.09462 | -44.72198 | 2025-08-31 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 56db6d35-1406-3008-bc86-dd88b0420e87 | -14.53638 | -51.98668 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ecc7882-73da-3d0c-9191-1b8d80cf96f8 | -16.21703 | -52.66061 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60cfa747-bf0a-3969-bf38-8408a1c19148 | -16.46132 | -46.86863 | 2025-08-31 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92a288ac-8e9c-3325-a43a-e33a7db70c5a | -13.48087 | -46.96309 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be19e475-7337-3003-aa22-0705cf6dc235 | -15.67807 | -43.22608 | 2025-08-31 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7c4a1e04-9e74-333a-be37-3d403dfbe17a | -13.34742 | -46.86733 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07679ccb-80f4-369f-bb65-b2a9d5561f16 | -11.81527 | -46.45323 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dc9ef94b-7d9c-34d6-8763-e4b0f422cd2a | -13.54502 | -46.95807 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9b39919-a8a7-3128-ac72-feb344861cbb | -12.86099 | -48.09034 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| becd0e86-3b43-3818-935e-d6575ea55f10 | -12.63369 | -48.19506 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9938e22-f3b8-3ada-8f6c-e0ffe9ce092c | -11.90594 | -46.39331 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 027749ab-dd94-3540-a4e1-569ee2b42731 | -11.80667 | -46.45503 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a2eb44e-7605-3ffd-9326-53813ebddae3 | -10.96263 | -50.86053 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cc13dee-c1a5-34e7-b2bc-c0aec4867e8b | -13.48891 | -46.96473 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92115c56-3f08-3c1f-8482-886c5676dc77 | -12.75459 | -44.40949 | 2025-08-31 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e80dfcc0-dcac-3711-95fb-1929549cdbf9 | -12.80521 | -48.09745 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f8547c7-e8bc-3307-bf01-d78d3d597370 | -18.05067 | -45.94876 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 957caa8c-9787-3eea-bfb2-7e7c9f7ce98f | -12.81134 | -48.08886 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3b05153-5e8b-3f2d-93f7-d7aca14d45a3 | -13.31811 | -46.88629 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c9d6879-f00f-3c3b-93cc-f6d635ea23e0 | -16.07984 | -43.62176 | 2025-08-31 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d443021-40b9-3248-b8d0-e08c381050c5 | -12.80242 | -48.08796 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b05bde8-26b6-30eb-baff-a0618c0ea672 | -13.58805 | -46.90346 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 94407578-abb9-3ff5-abf0-c9fba95545a4 | -11.81566 | -46.42744 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 08b9a004-414d-3fc1-b9ae-3097f2efcb04 | -11.82807 | -46.52256 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23706a54-e747-3c3d-951c-addc794ab31a | -10.96252 | -50.85665 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e56bab7b-544f-3e28-87ce-6f4901c6d47f | -12.39656 | -46.47943 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0088917e-42b0-3d08-bf2e-d8b6a14fe659 | -14.98478 | -48.16935 | 2025-08-31 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01b0eb3c-f8cf-3524-9de7-1f1a45c5f374 | -15.49746 | -41.51741 | 2025-08-31 04:04:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d439a5c0-9f50-3807-87ed-121cf4008f74 | -12.45406 | -44.05371 | 2025-08-31 04:04:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670d22bf-c88a-3a79-b353-af6c39602cb0 | -14.80957 | -46.75469 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48dbd9f3-a094-3cfd-bedb-b02d46122bb7 | -16.23594 | -52.65316 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eb0af86-e71b-34d0-93db-57ad44fc674a | -16.98163 | -49.31987 | 2025-08-31 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10ca06ba-fc83-3f47-8bc0-d6f5cc3dd979 | -14.49185 | -40.48335 | 2025-08-31 04:04:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 81a4a52a-b8ca-39cc-ab47-eaa7b690a851 | -11.56228 | -47.62111 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README29.md)
