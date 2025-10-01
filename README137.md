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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a79cce89-5be5-3804-9cf0-1f2851106949 | -14.35861 | -45.93973 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 44f1a7f9-692a-3ddf-b15a-e5d2e9fb86f4 | -15.23623 | -48.73618 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf9a9ae7-e640-3775-92f6-9d3d4528387e | -13.77445 | -48.01273 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bed0e9f1-02b1-31b1-a685-cab804ef96fd | -15.2367 | -48.73198 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d699bf57-9b12-3e07-921c-c277b9a6736c | -14.95245 | -47.51725 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b88125ae-286c-3f23-9905-67f4eeaf05a1 | -16.37792 | -47.06857 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d837c1cb-2eac-3f2f-9f17-6ac4a62eb1c4 | -14.98306 | -50.76502 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f7f0e0b-699b-39a5-846b-61ea7fe8b4b4 | -15.76722 | -56.16708 | 2025-10-01 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0ab2e522-e31c-3ccc-8889-af436d57c27b | -14.71118 | -48.1284 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 927615a4-4d46-3aac-91b2-0318be355932 | -15.3426 | -56.63724 | 2025-10-01 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bbdb30b1-2537-37c6-84b1-d2d60c8f24bd | -14.91453 | -47.82177 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0927ebf9-0dcb-318c-9055-624328e58921 | -16.40507 | -47.05925 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5222a120-9aef-31c0-a24a-f92d1b206187 | -17.89256 | -57.58607 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| f2cffe9f-f199-375f-a45f-357e4c4f55df | -15.2675 | -49.29407 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 398b46e3-d3bc-38cc-b559-274ec76f1583 | -14.19228 | -46.10619 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 497e1e08-9b59-369a-9c2a-8aa731022f81 | -13.69692 | -48.64943 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1969ebe3-5979-3374-9365-80646f718de3 | -14.09335 | -49.74425 | 2025-10-01 05:12:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8c906ed-ec60-3a6c-93a0-e8b66084611f | -14.71067 | -48.2702 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7dbac9e4-22d9-3156-805e-2721bd27e641 | -15.28143 | -56.78288 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee114b48-bbd9-3ac6-bbe3-8e6cdd4cb42a | -16.40457 | -47.06441 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 966837c5-99ff-3cf7-a070-7915f87e2094 | -14.69978 | -48.26012 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc7b97a7-87dc-3c8b-857d-d0e705e8a474 | -14.68218 | -45.28777 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1fe38f1-76eb-331f-85fc-0334e67e1902 | -14.49097 | -48.44891 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bf64a7e8-e80c-3025-ad41-b125530004bd | -13.94116 | -48.11147 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 447abe95-0eb3-3932-a262-46c98f09471b | -13.30545 | -50.66739 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5ec73f82-986c-3a81-90e6-1da30eefeca6 | -14.90308 | -48.1119 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a3adb2d-66e1-3bd6-ac2f-233760051859 | -14.79821 | -48.32979 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44cc46cf-cf13-301d-ac1a-16f2723e5c22 | -14.8689 | -56.44545 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70162292-254e-3811-b631-8bbd93948c97 | -14.68476 | -48.11953 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 82a3e916-83e8-35ac-b966-68b8d23aec5c | -15.23818 | -56.80959 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fda28dd2-5eb9-397a-9f00-9d628832ae54 | -13.81246 | -47.49811 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69a6dca4-efe6-37be-b363-01347f388504 | -14.71002 | -48.22115 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2256373-9559-3885-ad13-c6de165f7b7b | -17.38809 | -47.14439 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12a93ae7-1ef2-3035-9a2c-d6dde024124b | -13.93821 | -48.12087 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c65141a7-a0aa-32c9-b930-e3a2e56d75c7 | -14.89917 | -48.12454 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 49c34924-ff45-3f44-b5a0-6e3cd7723222 | -15.33665 | -47.94072 | 2025-10-01 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eedf37ad-239e-3205-80d9-486dba45fe84 | -14.91112 | -51.67177 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| caffce41-22d4-344f-8f4b-5352017e4435 | -15.87909 | -54.23542 | 2025-10-01 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 201defe8-cfda-3691-b582-51f932adbc97 | -14.3531 | -45.92658 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4698f800-2103-37c2-903e-0d462dbe5ee0 | -14.17461 | -46.11323 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1edd2a91-7998-3861-8c1e-ea3b35e26967 | -16.01104 | -50.87858 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc37d9a1-526e-3171-af07-faee0958ce81 | -14.96471 | -46.87195 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aa7dfdf-e205-3b5e-a699-0df1b89504b6 | -15.31039 | -46.39993 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 044a18d8-a08f-3dfc-9b41-7db0dde03dd1 | -15.13227 | -46.4534 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ec1759-8757-33c0-8c6e-e1bc662813c3 | -13.8123 | -47.49998 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aebd9278-e830-3334-98e8-c23952e60527 | -13.91786 | -48.10537 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd691151-3e3b-3b1c-9aab-323598a4aa70 | -14.04925 | -47.98964 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c3884be-cb7b-3d86-8e57-e0b2d156a867 | -14.9881 | -50.76566 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fc4bdb4-4093-32a6-9be5-74a79ec40016 | -14.76177 | -45.75785 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 261d64ed-f1c6-38ee-a96c-175be378156e | -13.76753 | -47.96632 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 598654e3-ef27-3f78-b101-98cacdc821d2 | -17.38704 | -47.15539 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 070420de-306d-3263-bc3d-5b05df6fdc97 | -13.97567 | -44.88005 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b4822b1-82d8-3e56-b143-1c39de6d1f95 | -14.14766 | -49.20467 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b96c48c-23f6-303c-86b3-374fc3095723 | -15.31655 | -46.40552 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53891d2e-8f9e-3a99-8ac7-e44881c83235 | -15.23964 | -50.08459 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40748026-dc67-38b3-84ad-3e4059d898fc | -13.63407 | -47.64859 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68ab7127-d601-385a-b1aa-8d89411afd96 | -14.90905 | -51.6804 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37dcf382-39b7-3347-b1be-adc8816c3698 | -13.66813 | -48.06903 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b30bbe0-ad79-34c5-b8b8-ae8bc06ee2cd | -15.34195 | -56.96153 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 897d5a4c-664b-3628-b893-09233b18cadb | -13.6726 | -48.08254 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 29943cb5-33d3-3328-902b-358e5a4a6b5f | -16.2932 | -48.98001 | 2025-10-01 05:12:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82bdfb49-2a62-392b-85ad-d5f5f28569d0 | -15.83096 | -56.21906 | 2025-10-01 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f424b72-dfd9-3657-a2db-3c5c319e92d8 | -16.41111 | -47.06208 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0cde0e09-80f9-346f-b8e4-61a3b4d3e4cb | -14.98342 | -50.76201 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49e69630-4ccf-3cf4-9545-3ddf3a3444a1 | -15.29312 | -46.19386 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c002e489-5754-3d6a-8519-05f7971ec80e | -14.59412 | -48.22339 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddd72a87-ab82-35d4-9f23-94ebed2afc87 | -15.2645 | -56.84923 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b3d90e-839a-3c0a-b0a2-28adb545e919 | -14.90431 | -51.67978 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e90eb691-64ec-300b-90e6-894906cfb2a1 | -14.72328 | -48.15472 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fda67585-89a8-300b-8745-487778ac7eff | -14.75494 | -45.75768 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8a770a00-8165-34cb-98a0-cc8a60554080 | -20.59998 | -45.88287 | 2025-10-01 05:14:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37e3bea7-8996-3b84-be13-2f7e38ddf1f0 | -23.22606 | -49.4055 | 2025-10-01 05:14:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c9aeeaa9-630f-3b4e-8f40-89d863fe8fd2 | -20.59782 | -45.88781 | 2025-10-01 05:14:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c849e314-b8c7-3f37-b77e-ee4c7a710531 | -20.12348 | -46.34134 | 2025-10-01 05:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea3221c9-3353-36a2-81b0-235129df8cab | -20.13062 | -46.34066 | 2025-10-01 05:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c815c3a4-4676-36c2-a868-23be9be9b285 | -22.26544 | -46.73036 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e398426d-578b-39b7-b2b0-77721611a399 | -22.27244 | -46.73109 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 83977010-1c61-3ea2-8696-4c2f06b3e3d0 | -22.57563 | -46.78276 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| c5fe7bdf-46d9-39df-a9f8-b2291b40dab5 | -23.05733 | -47.03161 | 2025-10-01 05:14:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e8473ec-8b35-3ba1-b16f-e34ce6ec42c9 | -22.26095 | -46.71596 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f94c12bc-168d-3300-946a-89f3c1a1bc24 | -22.27485 | -46.71886 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1caf531c-aa1a-328b-ba5e-5d7dd242c471 | -22.27443 | -46.7246 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e91bdf5f-7dda-3d65-806e-c7951486308c | -20.12136 | -46.34085 | 2025-10-01 05:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8f2a749-d9cd-36ed-9dce-83f0abc568dd | -22.43242 | -48.31437 | 2025-10-01 05:14:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e35ca164-e82e-3aff-b13a-9811e0417978 | -22.57404 | -46.77817 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| f181703f-f40b-3ae2-8cc8-d9ce735d7665 | -22.58101 | -46.77934 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| eb56d162-d740-3715-bead-9e112c8e479f | -23.42072 | -49.45889 | 2025-10-01 05:14:00 | NOAA-20 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e425cf74-bd7b-3ed1-aece-d4d7b433c35b | -22.26786 | -46.71796 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 77bccf73-89dc-3870-a724-66c09233a60e | -22.27401 | -46.73037 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a818d9ea-54ff-36bb-a57b-3837e4a82ebe | -22.4389 | -48.31428 | 2025-10-01 05:14:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89cbc5d1-6eea-318f-b4c6-334cb1fc1b99 | -22.58058 | -46.78593 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 42ebaca3-9143-345a-b29d-d3c783aa06fb | -22.78596 | -47.22971 | 2025-10-01 05:14:00 | NOAA-20 | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 569269e7-864f-351f-a1de-f5fd0a21323e | -23.06376 | -47.03312 | 2025-10-01 05:14:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c49c45e4-5d5b-31e6-b509-4eda9ae1131c | -22.26701 | -46.72966 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| db6cdaca-dcc1-31d9-b710-c1eb177a553f | -22.57614 | -46.77577 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 57ff7cc8-575f-370f-994e-21a748ea300c | -23.42033 | -49.46383 | 2025-10-01 05:14:00 | NOAA-20 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8359f976-bd1e-308b-bc9c-d9aaa315f6f2 | -22.58215 | -46.79013 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 7d2da17c-381b-32b5-b644-b222b9dbba81 | -22.57493 | -51.11314 | 2025-10-01 05:14:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83dd0548-c611-3113-a0d1-c2261d85eab0 | -22.56884 | -51.11963 | 2025-10-01 05:14:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b5eed03-b4ca-35bc-babf-6e485c15eddb | -20.12849 | -46.34015 | 2025-10-01 05:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README138.md)
