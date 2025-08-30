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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bb46597-aaaf-3eee-b735-70d406da92df | -9.0614 | -65.4355 | 2025-08-30 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b952dafc-108c-3922-be81-249e94cc8d58 | -11.8384 | -46.3607 | 2025-08-30 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| da9903b6-dffd-3f64-b355-f170fa23126b | -13.9918 | -44.5884 | 2025-08-30 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 09c06dd1-8dae-3a79-a445-cf2655c6342e | -9.0799 | -65.4536 | 2025-08-30 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| defcc47e-672e-3f1d-bdf9-378cbcffdbac | -13.4019 | -46.9667 | 2025-08-30 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7f67c2aa-1fb2-31c7-8d84-5cf5826f8a95 | -11.856 | -46.4487 | 2025-08-30 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f5d98162-5c38-3dab-915a-1abfb81b06b1 | -8.8843 | -60.7315 | 2025-08-30 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 242c256b-0d82-3827-84fc-e4dc8198ab21 | -13.3821 | -46.9924 | 2025-08-30 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 37bdcfcd-da20-316a-a881-3c33263cb996 | -9.0799 | -65.4349 | 2025-08-30 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 31cea326-04a0-3a59-80db-75aa5bf5982e | -13.3628 | -46.9953 | 2025-08-30 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 738826a9-88b7-31f0-8cc1-9ff4ae2ed0c1 | -9.1156 | -65.7513 | 2025-08-30 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ef43c61a-caf8-3504-aa3e-74c8d874d7e1 | -13.3623 | -47.018 | 2025-08-30 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 97ddd529-835f-38d2-bafe-7f30c22bccbc | -5.6268 | -45.0025 | 2025-08-30 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| fc64d078-ddaf-302b-a60e-22f3051870ce | -11.312 | -43.6428 | 2025-08-30 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 844c0722-b4ac-3c0b-a0ac-0ac3b04fd542 | -9.462 | -60.549 | 2025-08-30 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 14458c96-c934-3972-a3a9-0128c99f0958 | -9.4433 | -60.5499 | 2025-08-30 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 191.5 |
| beb9af59-3109-3225-90b4-58635563f462 | -9.4432 | -60.5692 | 2025-08-30 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 8bb1eaa7-50dd-32e1-a54c-92308039c062 | -13.383 | -46.947 | 2025-08-30 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a9cca72a-fd22-3b74-be51-f7962e731064 | -8.9126 | -62.1058 | 2025-08-30 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 0b17c0c1-3f59-3333-a577-dfa552c30f2c | -11.8576 | -46.358 | 2025-08-30 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| dac6a8bb-0b0f-349a-b8a5-e82bd2229f0b | -13.3817 | -47.015 | 2025-08-30 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 26777282-b069-3b9e-8498-a74b2b33b603 | -9.1155 | -65.7699 | 2025-08-30 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 64fbd846-4740-39d6-998a-8736d715d9e5 | -9.0613 | -65.4542 | 2025-08-30 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| eea41169-5ddd-3547-976b-97a2a70a0cf6 | -11.8568 | -46.4034 | 2025-08-30 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 710a3164-0a0d-3b38-a6c2-cc26430601a8 | -13.3825 | -46.9697 | 2025-08-30 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 149.3 |
| ecd21707-d9ff-3d55-80eb-7500df71f4c4 | -11.8576 | -46.358 | 2025-08-30 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 7831deca-13a8-3575-8736-53e3aac3d3ea | -8.894 | -62.1066 | 2025-08-30 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| eda3d4b2-d0a4-3936-8872-d1c85e4dc371 | -9.462 | -60.549 | 2025-08-30 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ed11effb-0974-3f6a-a3b3-261311e70c54 | -9.1155 | -65.7699 | 2025-08-30 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 387f5519-c991-31fa-be7e-08d603375a3e | -9.0799 | -65.4536 | 2025-08-30 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0364a69f-7a66-3fc0-b4c3-c2eaeef2f729 | -6.1853 | -43.3257 | 2025-08-30 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| fb7d9d75-cdd5-3412-8957-b9ea74e3a25c | -13.3628 | -46.9953 | 2025-08-30 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 3d61442a-6d03-376f-b87e-a55343e915f9 | -5.6081 | -45.0038 | 2025-08-30 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b685d135-6648-34ad-83ea-4e2bf3861883 | -13.4019 | -46.9667 | 2025-08-30 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 932069c5-6991-3327-ac45-2e6a5566e06d | -12.6339 | -57.0127 | 2025-08-30 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e1470a4a-64c8-3d8f-b61b-321a85535c0f | -11.312 | -43.6428 | 2025-08-30 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4ffc4597-e7be-3c65-842f-35e263ab62d4 | -9.0613 | -65.4542 | 2025-08-30 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| fc21d34c-15b7-3c9c-a530-8b9a36a6850b | -9.1156 | -65.7513 | 2025-08-30 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 2a8b3cd7-cd5a-389f-a937-7107f4bc00e0 | -9.0799 | -65.4349 | 2025-08-30 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| dbb339ed-1023-385a-96b4-1ce276ed7e65 | -13.3825 | -46.9697 | 2025-08-30 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 151.1 |
| ddc0a211-a5f4-37f6-8a5d-12998dc70f20 | -13.3821 | -46.9924 | 2025-08-30 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 164.9 |
| b78af428-9ac2-31f6-93a8-51d01263dd53 | -8.8843 | -60.7315 | 2025-08-30 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| e68c3f6d-4a86-325c-90ed-dfb3d7181125 | -13.3623 | -47.018 | 2025-08-30 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 5c42f641-1a24-32ba-9348-028d4a184009 | -5.6268 | -45.0025 | 2025-08-30 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 8a9a4c7d-6c69-3425-95fd-0d854da2448d | -9.4432 | -60.5692 | 2025-08-30 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9bac838c-f777-3e13-b3b6-1460d64dc43f | -13.3817 | -47.015 | 2025-08-30 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 131.6 |
| cb254f89-4252-319c-a86f-33f691e298f6 | -14.0113 | -44.5849 | 2025-08-30 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| bdb5e7c8-54e6-3aa8-98f4-8c8baeded31a | -11.856 | -46.4487 | 2025-08-30 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e6517c0f-39e9-34fa-8937-2fa8aed63ceb | -11.8572 | -46.3807 | 2025-08-30 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 22293535-8ccc-367d-a513-2ae09ee3f9df | -8.9126 | -62.1058 | 2025-08-30 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 4ad1a9e2-a92e-3f7c-a216-21e0a7fc8843 | -9.4435 | -60.5307 | 2025-08-30 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 9c12d947-7933-312c-9a95-77def0f8070b | -11.838 | -46.3834 | 2025-08-30 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 9c99690f-baf7-32c1-9cb8-fc5499f01185 | -11.8764 | -46.378 | 2025-08-30 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e9c36f75-3277-39b9-aaf5-0eb5aae3a5d0 | -11.8564 | -46.426 | 2025-08-30 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 924b09b8-9e28-351d-8f81-7e4f5eb93ac1 | -9.4433 | -60.5499 | 2025-08-30 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 8d9eabc4-1d49-332a-9d2b-59cbd1e5f3f6 | -14.0118 | -44.5614 | 2025-08-30 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 7a9b3f33-2cd0-3b78-af26-3ac710b3d0cb | -11.8369 | -46.4514 | 2025-08-30 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a2868eac-ad5e-38fa-aea6-0eee606a5481 | -9.0614 | -65.4355 | 2025-08-30 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 247138da-7e39-3db4-93ad-42385fd436ef | -11.8568 | -46.4034 | 2025-08-30 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 519b028e-58e0-37db-9a34-8dad6ff4872f | -12.0153 | -43.9818 | 2025-08-30 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2e7ab20f-27af-3d07-a6bd-254fd61d787e | -9.0613 | -65.4542 | 2025-08-30 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 77e77b41-5530-3a69-ba0d-e7ee42092c02 | -9.4497 | -62.3485 | 2025-08-30 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 9432ff0e-6639-3ca5-a7aa-b47edb28feab | -6.1853 | -43.3257 | 2025-08-30 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f1583edb-c655-32ab-8bc3-f059510ddc17 | -13.3623 | -47.018 | 2025-08-30 02:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 860b1a36-fc19-34c2-b8d1-dbb47940e1bd | -14.0118 | -44.5614 | 2025-08-30 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 37d0ecb8-ba57-3fc3-9123-aa7c41664454 | -13.3825 | -46.9697 | 2025-08-30 02:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f6eff5df-6f5a-395b-b93a-aa814dc40b1e | -5.6081 | -45.0038 | 2025-08-30 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 56e2c11d-f1d5-34cd-b10e-01c720e103b7 | -11.8369 | -46.4514 | 2025-08-30 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6ad3c724-63dd-3eb9-b6d6-c3f51e619a50 | -9.462 | -60.549 | 2025-08-30 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 31b1292a-6b4d-3ac6-9b4e-a39ee15cbb56 | -9.0614 | -65.4355 | 2025-08-30 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 85f6b933-8e23-343d-b760-c2433a9ff0c3 | -9.1156 | -65.7513 | 2025-08-30 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c95ec9ed-3cbf-3b5c-887e-10be7072e6f8 | -13.3817 | -47.015 | 2025-08-30 02:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 7fd5c1c3-36ab-346b-b781-611245ed4620 | -13.9923 | -44.5649 | 2025-08-30 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| edd506fc-6b33-33aa-86cf-884812627c15 | -11.8572 | -46.3807 | 2025-08-30 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 408859bf-99aa-30e6-b2c6-e8c821fc6db3 | -9.4498 | -62.3294 | 2025-08-30 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b9864781-29e3-3474-83c8-914a51df0712 | -9.4432 | -60.5692 | 2025-08-30 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 3402072c-aa77-3536-bf6e-15ff72e88ccf | -9.4433 | -60.5499 | 2025-08-30 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 196.3 |
| 59571504-e079-34ea-99ce-57e0b838d179 | -11.838 | -46.3834 | 2025-08-30 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 314d0c6e-4f1c-3ffd-a291-91ec1b5087e0 | -9.4435 | -60.5307 | 2025-08-30 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 46c8ba96-e5a2-3a78-a350-1529fdcc8cbb | -6.1665 | -43.3273 | 2025-08-30 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6ffffb09-aaaa-395a-9d17-b7e22184cf2b | -11.8568 | -46.4034 | 2025-08-30 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 721958b1-b419-3241-a908-d76b85f47f31 | -9.0799 | -65.4349 | 2025-08-30 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c1cfc49f-e2b1-3d50-b9ee-a99175653e9f | -9.4684 | -62.3286 | 2025-08-30 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 99486475-68e9-32c9-823c-1e4aad7b7473 | -14.0113 | -44.5849 | 2025-08-30 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 5a3d99c1-acc9-30be-bcbe-81222815043c | -9.4499 | -62.3104 | 2025-08-30 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 54b82140-9227-378a-9f55-64f8af3158b6 | -8.8843 | -60.7315 | 2025-08-30 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 9296f187-0b55-3d99-92b8-596f44e74e59 | -13.3628 | -46.9953 | 2025-08-30 02:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f72edb4e-6f94-36ec-a404-fa08b6e993e2 | -9.1155 | -65.7699 | 2025-08-30 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 23cff717-b0f4-35d9-b3b0-da613372bcd4 | -13.9918 | -44.5884 | 2025-08-30 02:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ba67dc9c-6202-3756-9a56-20580cb2aa9f | -13.3821 | -46.9924 | 2025-08-30 02:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1fe4f6fe-3ee5-37cc-b7ff-ef2b809b476d | -11.8764 | -46.378 | 2025-08-30 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6c1819dd-86ae-3933-b408-1187daf47e54 | -9.4497 | -62.3485 | 2025-08-30 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| abf8c3bf-5b25-3854-8515-b3944b841e25 | -5.6081 | -45.0038 | 2025-08-30 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 743b8968-3510-3637-8d2d-8a85d7c49d27 | -13.3817 | -47.015 | 2025-08-30 02:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 157.1 |
| c9fe080f-190b-37cc-a8fb-438cc2ff0dfc | -12.0153 | -43.9818 | 2025-08-30 02:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ba75ad9f-a854-3291-ad2b-edf69afb7db4 | -14.0113 | -44.5849 | 2025-08-30 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| e5a51115-aee0-30e8-b395-2bb40a8e0461 | -8.8843 | -60.7315 | 2025-08-30 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| daebe7a4-3289-33e9-b520-739d92ec74b4 | -8.9126 | -62.1058 | 2025-08-30 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ec14f9e2-fd80-3075-a224-99753dbb9195 | -9.1156 | -65.7513 | 2025-08-30 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 26c47b01-7dd6-3cc8-8f2a-db5be3c83d91 | -11.856 | -46.4487 | 2025-08-30 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |


[Clique aqui para ver as próximas entradas](README9.md)
