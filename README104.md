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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 412aede8-f506-3086-9f57-0e09a94f2d96 | -6.1663 | -43.3506 | 2025-08-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 224.2 |
| cdc7a376-78ae-3dc2-af15-d9186cfe2831 | -11.0679 | -52.0206 | 2025-08-30 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 02ac997a-904d-38e6-920a-794fa1b49046 | -13.3628 | -46.9953 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 9b43608a-27c5-3823-b3e6-bd77290ecbef | -11.3713 | -43.5394 | 2025-08-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 3dc3cf17-1b8a-3215-beb2-08ffddf9721d | -7.092 | -44.5887 | 2025-08-30 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| da88c674-a37c-3b9e-b5bc-6e2eced9c366 | -9.4433 | -60.5499 | 2025-08-30 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 139.0 |
| cf2ed63c-61ef-39f6-acb8-e32d88e228e2 | -6.7816 | -43.7632 | 2025-08-30 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| d9e4aedc-729f-3524-8893-9fe97afe8658 | -11.3521 | -43.5423 | 2025-08-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| ec8e2711-6a35-314b-8edd-c6c45cddad9d | -8.8665 | -45.7335 | 2025-08-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9f4989cb-7a4e-3253-bf86-0677c1e7547b | -9.4247 | -60.5509 | 2025-08-30 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2733406a-5162-301b-afb1-961851e7e25f | -6.1853 | -43.3257 | 2025-08-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 1aecd250-45b8-3749-a515-4b7d0b319007 | -13.3632 | -46.9727 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 160.0 |
| b8b235f2-3f2a-38a0-a328-21818224cde8 | -13.3649 | -46.882 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| e14bae1f-1a81-36db-8797-d816c30c3396 | -11.3517 | -43.566 | 2025-08-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 300.5 |
| 2411c044-c1bb-3a35-ba01-c2c4e4ed23f5 | -8.1212 | -61.2252 | 2025-08-30 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 5d3458e0-c170-3e27-86b0-da1d5363afd6 | -7.603 | -42.7232 | 2025-08-30 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 212.7 |
| 8fa1d749-2d2d-31c8-ba9a-43e251b2813c | -10.3812 | -57.8245 | 2025-08-30 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0292fbff-d972-393c-8b22-86e18e4e4595 | -20.5048 | -57.0861 | 2025-08-30 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 6318ee1f-8fc6-326f-8cc6-6a394ec3d6fd | -9.4312 | -62.3303 | 2025-08-30 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| cd42e384-ba04-3d2e-ae1a-3a2a033de8c6 | -11.0087 | -46.9442 | 2025-08-30 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 5b639487-bea8-3ced-8066-45191c3704ac | -14.0128 | -44.5142 | 2025-08-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 39a1c053-60de-3f8a-8716-22d1abca7c12 | -6.185 | -43.3491 | 2025-08-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 199.2 |
| d03c3cb7-7a44-3f56-8069-5d8dcebbcf78 | -7.0951 | -44.3128 | 2025-08-30 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 8b86ed38-b7b6-3222-bf8d-7bac08f3042c | -14.0313 | -44.5578 | 2025-08-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 849dc261-6157-38cd-b4bd-11e1a06a314c | -7.6033 | -42.6995 | 2025-08-30 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 119.8 |
| abf574e6-4f25-39a1-8e48-e28f93b6f5b1 | -13.3452 | -46.9077 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 24d98d03-b372-3f4e-83d3-f0e01425879e | -7.7257 | -50.2751 | 2025-08-30 14:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8cd36526-314c-35f3-bb5f-e77bfdf31c6b | -12.6494 | -48.1731 | 2025-08-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 196.9 |
| b29a091a-41a0-357f-bc46-93ad1e3c7c52 | -7.6028 | -42.7468 | 2025-08-30 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| dba5927b-bb57-3de7-bb89-121fb67735f5 | -13.3645 | -46.9047 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 1f180c12-42d9-3a42-a1c9-f2a4c7813d05 | -14.0118 | -44.5614 | 2025-08-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 138c9644-a815-339b-9f4d-596efdd2cbd4 | -14.0518 | -44.5071 | 2025-08-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| a617482c-c8ef-32ff-98bf-718d7bad9a16 | -13.3258 | -46.9107 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 9a658caa-c9b1-3a17-a307-4bdfdd4c6d8e | -14.0328 | -44.487 | 2025-08-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 0cbd83ad-5f4d-3206-9e49-84ba3cf4c95d | -13.401 | -47.012 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3cf05f3e-e41d-32ed-ba26-c83ab69a13fa | -13.3623 | -47.018 | 2025-08-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9da037a0-48cd-3059-9c3d-9066d7e6f2d9 | -6.7814 | -43.7865 | 2025-08-30 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 76159661-c69a-3128-bbb5-bf2b8dcbf921 | -7.1959 | -43.7019 | 2025-08-30 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 277.3 |
| ec04e672-7d6f-3686-9ed9-e289f1026db3 | -9.0799 | -65.4349 | 2025-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| a6a5ec13-d55d-3c3b-91ce-f49f3bd85e08 | -11.0676 | -52.0416 | 2025-08-30 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 99562154-aa05-3fdf-9e16-4ab9fd39220b | -8.9669 | -48.2114 | 2025-08-30 14:20:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e7a63672-8687-3c71-806c-e41aaf5cd05f | -14.4484 | -51.9858 | 2025-08-30 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 29b8fec2-3373-390b-87a7-1ecfb730a78f | -7.2142 | -45.443 | 2025-08-30 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5518792f-1be4-3eaa-972c-33c9d32c85bd | -9.462 | -60.549 | 2025-08-30 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 41f5deb5-82ca-3c26-a73b-936adae2aaf1 | -14.105 | -51.7754 | 2025-08-30 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 05042730-8cad-3edd-8256-cda7fabd9f24 | -14.4671 | -52.0259 | 2025-08-30 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 8a42808e-85eb-3609-9e5c-de9719e388d7 | -6.3815 | -44.3515 | 2025-08-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d0a1252a-e0fd-3f81-9dcb-80e43442ae3e | -12.649 | -48.1953 | 2025-08-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 145f8970-99d3-36d9-9d6a-ae7c72caa359 | -13.0154 | -56.8982 | 2025-08-30 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| c63bbaef-c2fb-3649-820e-069456c18fac | -7.1108 | -44.587 | 2025-08-30 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| bcd49b4d-30ff-39b7-92bb-3b14f76da5cb | -6.2096 | -42.7607 | 2025-08-30 14:20:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 1d287475-5b4d-3799-bce0-19c45f4a539a | -7.6219 | -42.7212 | 2025-08-30 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 1ed4a790-0eff-32c3-8c90-11e401f13f68 | -13.3628 | -46.9953 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 320f0842-0c2c-33ae-abea-04243a2d11b2 | -11.3713 | -43.5394 | 2025-08-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| b874ff46-e826-31ee-8898-b1cf6f824a38 | -9.6758 | -65.0214 | 2025-08-30 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a3b225bc-f242-30e5-aa9c-c50da6d0a056 | -9.6679 | -47.9209 | 2025-08-30 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 10d546a9-82fd-346d-8358-575e2e6cb8b4 | -9.1378 | -49.623 | 2025-08-30 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6dae999c-9eb3-39ea-a074-808aea7a8d33 | -9.0613 | -65.4542 | 2025-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 0c018ec0-6c89-33a0-8567-d6bae78c2cbc | -13.346 | -46.8623 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 44ad1c46-35d5-3387-a5d3-7740a5fec1b6 | -14.0113 | -44.5849 | 2025-08-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 325.2 |
| ba38f8b8-e730-3052-959e-5974570f5d23 | -10.0351 | -46.03 | 2025-08-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 336ee564-f86e-3437-8387-5b9c9d243629 | -11.0679 | -52.0206 | 2025-08-30 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 18a8af93-5964-3828-bfec-188a30f59224 | -14.0118 | -44.5614 | 2025-08-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 09db0dce-3dfd-34c1-ad9b-4fa10e6cc984 | -14.5642 | -51.9917 | 2025-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 237f89c4-9397-3292-b823-e1aa9b84aec6 | -9.4312 | -62.3303 | 2025-08-30 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b6127f77-7159-33d7-9f98-a7cecc497c4e | -12.6494 | -48.1731 | 2025-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 287.8 |
| a6145631-aadf-3996-9bdd-90438727bb6c | -13.3452 | -46.9077 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| a348e549-d788-3161-8903-6a75295256f6 | -7.4463 | -44.8307 | 2025-08-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| a7893071-97d0-3af1-b82b-14ac428db28f | -6.2096 | -42.7607 | 2025-08-30 14:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 125.5 |
| 97d26608-ae1d-37f1-8795-d83c5c24c1e7 | -6.4068 | -45.6004 | 2025-08-30 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 376e6777-7c5f-3a14-be97-0ccba8cec1ea | -11.3705 | -43.5868 | 2025-08-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.8 |
| d1e55f21-6394-31ce-845a-3c5aef8bdebe | -6.7814 | -43.7865 | 2025-08-30 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5e99a5ac-4486-3acc-b67e-187bef6289bf | -9.0799 | -65.4536 | 2025-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| b741d0b0-38cc-35f0-9afc-1a3ee09df923 | -12.6686 | -48.1704 | 2025-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| be0556f9-8be7-320c-be71-0c02b129d103 | -13.3645 | -46.9047 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 133.0 |
| e61e3e89-9d98-31a2-80d4-1148e658059b | -10.3812 | -57.8245 | 2025-08-30 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| da60c50c-7e58-34a4-b5e4-f31e2e07414c | -7.603 | -42.7232 | 2025-08-30 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 201.2 |
| 41bb611d-7d10-382b-b887-d7deacb32e11 | -8.8665 | -45.7335 | 2025-08-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| dcd76e17-005c-3838-9015-8e938e13e677 | -6.7816 | -43.7632 | 2025-08-30 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| edda5281-bd23-3f0f-95a6-bc75f3fd1dcf | -9.4497 | -62.3485 | 2025-08-30 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 6c2d3fe6-95a4-3fce-8c08-addebfe37c68 | -10.8161 | -47.1024 | 2025-08-30 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| cf3d0214-b1a7-3488-b330-9ce0d780559e | -6.8611 | -45.1336 | 2025-08-30 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f1f6967f-de89-36cf-8fb4-ce76c7d696e6 | -14.0328 | -44.487 | 2025-08-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5f94d056-fce0-3894-b934-a0252293e164 | -13.4986 | -46.9517 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 41006808-97b9-3205-97d5-87bf42da5e45 | -12.8601 | -48.188 | 2025-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 8d62ecaf-0758-30b8-847f-648b217bf984 | -11.0676 | -52.0416 | 2025-08-30 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 648b5b74-374a-381b-98d5-9e386e2df7a9 | -10.8164 | -47.0801 | 2025-08-30 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| c84e9ba2-3fc0-380b-a144-8dbb381ec656 | -14.4481 | -52.0071 | 2025-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 1a510122-7937-3416-8557-e65c05a6a85c | -8.4049 | -44.964 | 2025-08-30 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| ca8ee751-1fac-3cc4-b50c-7a9cde4cb092 | -10.3624 | -57.8258 | 2025-08-30 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 14a495b0-fb62-3fd5-ade2-9d7ad000a26d | -10.99 | -50.783 | 2025-08-30 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 615c614c-584d-39c6-acee-9d3bdde0e6e1 | -7.6033 | -42.6995 | 2025-08-30 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| 1ad9bc26-dfb3-3a55-a13c-75b44d814940 | -7.1108 | -44.587 | 2025-08-30 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| bfa52871-0eda-31cb-be3e-e7c13484d44e | -11.3709 | -43.5631 | 2025-08-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 4c6f203a-e421-3654-a610-9b67b976d229 | -11.7347 | -51.7618 | 2025-08-30 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| dbe7e925-d250-345a-b317-498eaf250ac2 | -9.4495 | -62.3675 | 2025-08-30 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 706db1d6-b556-3e6d-8592-e66bd60ac3b8 | -6.1853 | -43.3257 | 2025-08-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 241.7 |
| 8c20db70-e4db-391d-ab4e-3b6f2d4df15b | -8.082 | -48.4019 | 2025-08-30 14:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4b0c1fc5-00bb-3c12-b7a7-26ea6a0bcada | -9.0799 | -65.4349 | 2025-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 165.6 |
| e159380f-0cf1-32bc-9f08-9834f7f785a5 | -12.8413 | -48.1685 | 2025-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |


[Clique aqui para ver as próximas entradas](README105.md)
