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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c28f9001-9ff5-36d0-9c60-939432c9dc30 | -14.66768 | -53.37552 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4459abde-3fe0-3a58-a8b9-587cf74aa7cd | -14.67458 | -53.3867 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 79f3fdba-28dc-3b4c-9a66-b4be0916922c | -14.67141 | -53.37787 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f56c580-f295-33d0-9ce7-5e871da56481 | -14.66718 | -53.37729 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae609032-823b-373e-8020-546298cdbf69 | -14.84623 | -52.28271 | 2025-06-11 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 958c9d1a-059a-35f2-91c1-35c0b26525dd | -13.72238 | -58.67528 | 2025-06-11 05:12:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06b24ec5-e0a1-3723-89b1-415eb000a93a | -14.67089 | -53.38194 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2d8d514-c1b4-342d-8534-f9045fc4db28 | -15.38258 | -47.89708 | 2025-06-11 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff0072e1-5187-36a6-8aa8-3adf9d34134e | -15.38211 | -47.90147 | 2025-06-11 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caed912d-cf34-31a7-a429-3e318a2b1c14 | -14.67511 | -53.3826 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a168a852-7e6d-36e2-99e5-b4a016ae8820 | -20.76102 | -48.53269 | 2025-06-11 05:12:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09ae2aba-73d0-395c-b0ef-8452d60ad095 | -18.41022 | -54.57266 | 2025-06-11 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59a112ae-371f-3bb7-a480-361a016f1154 | -14.67136 | -53.38014 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab79fee1-d4fa-3b3e-a144-5ffcde044496 | -14.6708 | -53.38422 | 2025-06-11 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3ee4116-d808-3847-af0c-aa5f87544874 | -20.54309 | -54.12965 | 2025-06-11 05:12:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4530a03f-c5ce-31fb-9297-46de8c6ff43d | -15.37691 | -47.89199 | 2025-06-11 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bece7ef-bce5-36de-aab5-56f9e0312cd5 | -20.09466 | -50.86762 | 2025-06-11 05:12:00 | NOAA-20 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6f2db2bd-f910-3052-a1d5-3cd87aa7975e | -21.04011 | -55.62862 | 2025-06-11 05:14:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e672d39-ed5b-3993-a6a6-0f31401f20be | -21.04273 | -55.62764 | 2025-06-11 05:14:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60bf304e-5877-3d23-8c66-6557e6349c82 | -21.81507 | -57.54843 | 2025-06-11 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3243e23-004e-3f3f-9c41-cf317b3a80d4 | -21.18463 | -55.72378 | 2025-06-11 05:14:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c99977dc-c227-3a9e-9a52-77f0a39acea3 | -21.82848 | -56.26729 | 2025-06-11 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60befd47-4fc1-3ca7-8e3a-1bdf3e32e13a | -21.76547 | -57.0302 | 2025-06-11 05:14:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dd2e10b-1b7f-3886-8c08-7ad54ed0d101 | -21.82948 | -56.26373 | 2025-06-11 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52c6fe16-7ab0-36a0-a089-38edc66d9634 | -21.04201 | -55.63315 | 2025-06-11 05:14:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee85e9cc-4c14-3f03-a797-230c0f4b018f | -10.30423 | -57.14331 | 2025-06-11 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 319518aa-4c05-3ede-b805-e524c1b9feca | -10.3617 | -57.50572 | 2025-06-11 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4db22b6e-827d-3f17-8a77-1933b6fe1e8d | -9.78227 | -57.42514 | 2025-06-11 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43475dbe-f1b0-3f05-bc36-d56eea725576 | -9.2418 | -63.28576 | 2025-06-11 06:01:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bdfc1bac-b46e-39bf-9535-5341091bfb91 | -10.36235 | -57.50881 | 2025-06-11 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9571ca04-9934-3010-a09e-a5b53b88c40b | -10.37011 | -57.50316 | 2025-06-11 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07945178-7ec4-3e67-ac0e-db397f6aab5a | -10.36313 | -57.50219 | 2025-06-11 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77334347-be02-3103-986e-0f3756b91d31 | -10.36944 | -57.50002 | 2025-06-11 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69287ee1-f9a8-3662-801d-d7286ab0deb6 | -9.78149 | -57.43177 | 2025-06-11 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71fd5356-1e62-33ff-8d05-c1e7d6456c58 | -10.29709 | -57.14248 | 2025-06-11 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 071153b3-bae6-3c12-9d4b-67423a90638c | -10.36869 | -57.50671 | 2025-06-11 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbf3fa9c-fd81-3aa2-97cf-9d86aa9196fe | -12.51657 | -57.21319 | 2025-06-11 06:35:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| df9f97bf-29d7-3f63-a3bb-9ac78c01fac8 | -10.65009 | -49.42153 | 2025-06-11 06:35:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 07352ac4-e0da-3cab-8461-2cc65b866d6a | -10.36485 | -57.50214 | 2025-06-11 06:35:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 864ecd96-5d1a-3f88-85fa-3795e3916910 | -12.51499 | -57.22439 | 2025-06-11 06:35:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 8704ee2c-ee87-37e8-92c5-f12647ab4b52 | -14.1862 | -45.4872 | 2025-06-11 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 2cbc24e3-4861-39bf-b22c-8293e3a0ba04 | -14.1862 | -45.4872 | 2025-06-11 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 262.6 |
| 86e6976c-d403-3e47-ac9b-161b006f92ac | -14.2057 | -45.4838 | 2025-06-11 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 90745355-870e-324b-b3b1-d518be99126d | -14.1862 | -45.4872 | 2025-06-11 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 279.7 |
| cbcf7a56-6697-398e-840d-b6a63ac2de72 | -11.7754 | -54.3756 | 2025-06-11 11:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a2fc9e60-dedc-3144-9456-ba00825ff6fa | -11.7754 | -54.3756 | 2025-06-11 11:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 8fb2ee8e-7dff-3565-9d4a-36b72dd7ff02 | -14.2057 | -45.4838 | 2025-06-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| fc75e94c-4454-3a3d-a150-551c32d37e91 | -14.1862 | -45.4872 | 2025-06-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| b70873fc-2363-3e1b-9d6b-0b90947b8a20 | -14.2057 | -45.4838 | 2025-06-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 23b40646-e74f-3d47-b71c-eeececc19efc | -11.7754 | -54.3756 | 2025-06-11 11:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 5bf85121-9513-3195-8113-99c7050f4cc5 | -8.1173 | -45.3579 | 2025-06-11 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 0528c6fb-a19c-3b32-9281-91e1b122ceb1 | -14.1862 | -45.4872 | 2025-06-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 277.4 |
| c3d7d228-b6e4-3e80-bf16-732c84e41794 | -14.1862 | -45.4872 | 2025-06-11 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 332.2 |
| a6abf9f3-2312-36d2-b81f-4d8d967e5a27 | -11.7754 | -54.3756 | 2025-06-11 12:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| d459c0e0-051b-3aa0-a6f5-8a6257c1d656 | -14.2057 | -45.4838 | 2025-06-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a2133efa-f68d-3290-bd57-900223325936 | -11.7754 | -54.3756 | 2025-06-11 12:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| ac065f8b-3b4c-3c55-affa-fffefac3ed1d | -14.1862 | -45.4872 | 2025-06-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 306.6 |
| 749c6d15-b56c-3c3f-bb77-95ad931f7779 | -14.1862 | -45.4872 | 2025-06-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 353.7 |
| c10d15c4-aa53-3e69-bd1f-8f99cce38000 | -14.2057 | -45.4838 | 2025-06-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9e3d9328-2b95-3ab3-b6eb-af155e7017ad | -11.7754 | -54.3756 | 2025-06-11 12:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 9ef29ff4-9736-3312-a691-5b35b2f9c62a | -11.7754 | -54.3756 | 2025-06-11 12:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| d564b734-4c01-3282-9273-766a021284b2 | -14.1862 | -45.4872 | 2025-06-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 302.0 |
| 76e5b239-1e56-33b7-83e1-85a0a59867bd | -10.8694 | -54.3151 | 2025-06-11 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1bf48589-d0ff-3e08-9849-2c116706cdbf | -14.2057 | -45.4838 | 2025-06-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 884b1764-3d12-3e0e-af08-ded98c470c02 | -14.1862 | -45.4872 | 2025-06-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 339.8 |
| d7bad141-b48a-35c6-b4da-73451946329d | -11.7754 | -54.3756 | 2025-06-11 12:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| e30b5bb8-22e1-3f9c-bcca-fb0d540333c0 | -14.1862 | -45.4872 | 2025-06-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 379.4 |
| 14b12216-fcd5-35d4-93a6-327e02ec64b5 | -13.726 | -45.2421 | 2025-06-11 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c366d4e8-ac02-37e9-9610-44237725be87 | -11.7754 | -54.3756 | 2025-06-11 12:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 5ae9f69b-6721-30d2-9ca8-5e60cebedd86 | -14.2057 | -45.4838 | 2025-06-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 78dbee84-8f3a-32ed-b598-9e362efe7430 | -10.8694 | -54.3151 | 2025-06-11 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| b259ec29-435a-3277-821c-ee4970bcb5f0 | -11.7754 | -54.3756 | 2025-06-11 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 5bf81395-9bbb-3fdc-a69e-fe1f7aa6dda5 | -13.726 | -45.2421 | 2025-06-11 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| db20e1a8-5f7b-3cb7-9674-3f595dda8ce4 | -14.1862 | -45.4872 | 2025-06-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 512.3 |
| 8ec0582f-c670-31d3-82df-1cd71f88b47b | -14.2057 | -45.4838 | 2025-06-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 4e5ac1e1-f713-3b20-83b5-32183c4366fe | -14.1862 | -45.4872 | 2025-06-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 460.7 |
| 4587688c-309c-3474-ad1c-95cdf389cc33 | -13.726 | -45.2421 | 2025-06-11 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 4ff47353-9a16-3ea1-ab3e-2bc9eee5ccf0 | -11.7754 | -54.3756 | 2025-06-11 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 40366caf-4168-3b50-a115-4267ce456da0 | -14.2057 | -45.4838 | 2025-06-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| b89a44ba-a03f-3110-b005-b3a99bd76f60 | -11.7754 | -54.3756 | 2025-06-11 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f033ceea-8755-3a9f-90e8-d41ad30ed467 | -13.726 | -45.2421 | 2025-06-11 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6749927d-7bb7-379d-8cd4-699a22526ff2 | -13.8864 | -54.6519 | 2025-06-11 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d4fbe651-d5f5-31dd-a673-3c0e41b363be | -14.2057 | -45.4838 | 2025-06-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 61174e6a-0276-335e-b247-0229244e10f5 | -14.1862 | -45.4872 | 2025-06-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 549.3 |
| a2799f2e-779e-344d-8adc-f6719d7064ac | -13.9056 | -54.6498 | 2025-06-11 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ac0bfff1-9668-3e99-a46a-fc8938ba13de | -10.0643 | -45.3448 | 2025-06-11 13:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c50c23b1-d0ef-3424-a68e-64bf06750c11 | -11.7754 | -54.3756 | 2025-06-11 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| f7b5de13-b8d5-3e16-8553-ddd0e2eb6a21 | -14.2057 | -45.4838 | 2025-06-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 80038767-315c-3e69-886e-28ff623fa504 | -13.726 | -45.2421 | 2025-06-11 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 762a1d0c-0376-3302-add2-e99786bd372e | -14.1862 | -45.4872 | 2025-06-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 486.1 |
| 02f1fb6e-3f6a-3d70-99c9-ccf0253cff5a | -6.991 | -47.0922 | 2025-06-11 13:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4dc2f1a2-ccf0-3914-b084-7e0e05ec53e1 | -13.726 | -45.2421 | 2025-06-11 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ca56778d-dfc1-3c8d-ad00-d8adf83f44a1 | -11.7754 | -54.3756 | 2025-06-11 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 295711cc-7482-3102-802c-c2295ac77e55 | -10.0643 | -45.3448 | 2025-06-11 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b96b14b9-9007-3983-a969-6e787ee8e018 | -8.7993 | -45.1044 | 2025-06-11 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| bb25cc69-8c3b-3102-a8fe-dd1de6dda7c6 | -13.726 | -45.2421 | 2025-06-11 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| dfcfa390-2c66-30b6-a7a0-8ac200c4110a | -11.7754 | -54.3756 | 2025-06-11 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6b6f99f7-42e1-3b8a-ab1a-535e593e543b | -10.7048 | -49.507 | 2025-06-11 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 7f0d5778-77c6-3596-9551-5ca47dd94c94 | -8.7993 | -45.1044 | 2025-06-11 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e57029ad-96ac-34ff-9a34-fe7b8e0017ab | -10.7048 | -49.507 | 2025-06-11 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |


[Clique aqui para ver as próximas entradas](README14.md)
