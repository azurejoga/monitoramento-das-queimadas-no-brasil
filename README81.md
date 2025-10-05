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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e73d154d-6526-38cd-9e61-29f50a720b41 | -13.09928 | -47.8437 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 143c6890-e85f-3232-a80a-776205125e83 | -9.05299 | -47.01586 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fd465bb-3ecb-30a6-81dc-1faa565b7ae1 | -9.83385 | -58.07786 | 2025-10-05 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ad8359d-91cc-3832-b71a-dfc9738856cd | -11.04547 | -47.78617 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a048c54-557b-3793-a20f-d50471212f82 | -6.42893 | -46.01958 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18615db7-0342-3797-943c-5fb34c091c76 | -8.55685 | -46.26332 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 64a94e75-db29-3084-8223-630abc441664 | -6.45976 | -44.58417 | 2025-10-05 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8b49e1aa-c486-307f-ab54-34d173e8edd9 | -6.10746 | -51.73044 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 335513e1-f06f-33cb-b526-7781e75e8adc | -13.08215 | -47.91214 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4058eee1-99b6-36ad-b414-e2f989b101a2 | -13.33758 | -48.06267 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| accd88e7-244a-33c7-bfeb-77aeabbe23a8 | -11.80068 | -46.81693 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7300431c-71f3-395b-9484-55978819cf89 | -11.69828 | -47.49434 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3edf1418-29c7-3bc5-9df0-e416e0aed9af | -13.12152 | -43.84076 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 42cad1c0-2186-3987-8722-11131d60b862 | -10.83333 | -57.17986 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27a90925-1ac8-3fcb-af05-13a7ea73da85 | -10.5739 | -48.71918 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e26a22c-c48c-38a7-b5c8-2bc029720a8b | -13.35059 | -47.57856 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03b194f9-f290-3441-8bae-d72ff31e10ec | -12.2717 | -49.18974 | 2025-10-05 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 517ee239-6f2b-3af0-bfac-a8bb980ef233 | -13.3509 | -47.20185 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49032dc8-65b1-3d4c-a9ff-3b696d65e841 | -9.62311 | -55.02972 | 2025-10-05 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f31ef47-b196-38d7-8591-dcc2368e7936 | -11.67671 | -43.90011 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 31f504cf-ef7d-38c5-8395-e876ce706dec | -7.46188 | -47.18088 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 822a4715-4121-395c-8bd1-33a2e9a9f36b | -7.72425 | -42.39322 | 2025-10-05 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70c988ab-d21e-39ea-99a4-06d7cc414b56 | -7.61322 | -45.46521 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cc987e6-3b56-3081-bd01-ca030dd80f00 | -12.31162 | -55.14576 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bff575f-7dc8-3105-9def-eec1668920eb | -11.09526 | -47.73889 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54bf6882-8a2d-3c29-9ed9-608d5ed18066 | -13.07511 | -47.90408 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 251dac42-7ea5-3859-938b-d68c5a911795 | -12.09544 | -50.93639 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ad95c13-215c-3cb2-a8f6-b92b2968619f | -13.30492 | -48.09832 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bdb625fa-861f-34c2-b637-b692325f5a47 | -8.12005 | -44.09641 | 2025-10-05 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7b03220-8ad1-379f-8f58-599c77b095de | -13.27044 | -47.61509 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b62a11fe-3842-3b6f-a245-e4ded3692298 | -12.2072 | -47.77946 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe4ea3dc-ff98-3797-9a0a-0eb0cd48f3ea | -7.69299 | -42.58781 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 569235ee-89fc-3ef4-9605-5dea5fcfea5c | -12.30218 | -55.13268 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97eb8483-b228-3afc-825a-6098ae98c48f | -7.4324 | -46.51521 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6ba6864-337d-3c20-9c1d-f819ae8c0c00 | -13.48033 | -47.2286 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 433e19d8-7287-3c36-ad78-f7b64b1634f2 | -7.85735 | -61.40285 | 2025-10-05 04:46:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7712be44-12f4-3aa7-ae34-bcd966214041 | -11.1231 | -47.17196 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b73319d5-5ebb-3067-80ee-cc76a29671c1 | -11.87367 | -56.87852 | 2025-10-05 04:46:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e2839d33-dc83-3fd2-8778-041b105badd3 | -11.10296 | -47.74011 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e69e32e-5743-3fce-bd68-be831be5c8d9 | -8.54747 | -46.27375 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ccdd61ca-5a10-37a8-bf3c-0ff630a4bd54 | -11.46475 | -51.52396 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7c62aae-6c2f-3876-9111-5ed9a0e9966a | -10.40113 | -51.58498 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59416df7-60b6-3b7c-a5dd-888587f32195 | -8.6142 | -54.9698 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc6efc11-5dba-3575-9cc3-f004d1830c05 | -11.11772 | -49.86302 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff2306e7-984b-3020-b3a3-602c47c38252 | -11.14929 | -47.93015 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d701c325-c9b8-364d-9c02-e7dbad3f6b57 | -7.64943 | -45.42419 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83e47bba-3517-374b-a981-5d0681339640 | -13.26836 | -47.60027 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe091f5c-b3d0-3b8e-bd3d-2d13d4a78d68 | -9.67298 | -48.20685 | 2025-10-05 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd809916-e6e1-33ec-8a7a-df73e24512a4 | -13.085 | -47.89071 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4db0ecfd-1909-3a73-911b-24f8d29350cb | -11.06985 | -47.69501 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4425a8b4-ded9-327e-bded-55422c453575 | -12.45973 | -45.51469 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a64e4b4-aaab-3a5a-b240-38bcb586273d | -10.83116 | -57.1685 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f59bf0b-af56-37d5-a491-890c5a9d6de0 | -10.01972 | -48.28745 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34ee2eb6-ae99-3d46-8bef-2f9f09ee62a7 | -8.23217 | -46.81251 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 39528abc-5d74-3522-9472-fd22effb5040 | -13.13679 | -47.97931 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1ae863a0-7c7a-3966-b5c7-8cb47b71d1a7 | -11.24829 | -47.78347 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c733f83-2ce1-3ded-be56-bf84f0dba087 | -13.119 | -44.07349 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e64e270-b809-3b66-ae00-2e541578fa9e | -11.81921 | -45.04785 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcb570f4-84a5-37dd-b377-48067d5d2d1e | -11.91497 | -46.23819 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 864a4927-4e54-39eb-973f-472eaf51e4a9 | -11.01607 | -46.68975 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5d734fc-ad87-300b-b763-1b6f3e95a4a8 | -7.63233 | -45.48353 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6a134e4-9fa9-3f4e-8478-6249b66a53f8 | -8.60329 | -46.28907 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8bfbc64-3092-3808-afc2-12d3eff1ef33 | -13.08148 | -47.91563 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bac6fa0d-e3a2-3cc0-ae47-551529df92ee | -7.11805 | -44.17255 | 2025-10-05 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ef48884-fd12-3f5b-b211-d8e6164b4a0d | -11.39017 | -50.8312 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9e07a6f-4f4f-3b85-8498-ddbe3ea3c414 | -13.52182 | -47.28757 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f1c7b4b-b4fb-3740-92d0-47dee0ec265b | -9.61945 | -50.54375 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a65ed830-9e87-35cd-abe2-49f3f0a4fb4a | -12.69572 | -47.58212 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f7267e7-553a-3052-b663-452bb621d2cc | -9.95689 | -43.77198 | 2025-10-05 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 324d858f-b9a6-356e-83c1-48f3adc062d6 | -9.98699 | -57.82014 | 2025-10-05 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed199e2d-9c1e-3a0e-bded-145b98209d8f | -12.92412 | -47.80806 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ead45c8-da40-3566-a068-fdcecb97d858 | -13.27397 | -47.18903 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67af9ba7-03c2-3090-a8eb-2ca6b36d799d | -12.32011 | -55.15972 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbf3453f-1679-3db2-b0c0-2a4002d251f8 | -13.10536 | -47.97636 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf3f708e-398e-32f6-bda0-3a43794a80cc | -10.99934 | -46.51765 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7fe3fb16-1e02-3a69-acd5-5f8b9db2a64a | -7.42581 | -46.51187 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f563651b-48f1-39ae-bde8-80c448305627 | -10.84667 | -47.19494 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23026f1a-71fb-32bf-a78b-78374487958d | -10.84715 | -47.19151 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4106bab1-eb7e-31f5-9a86-8018725fd557 | -13.1442 | -50.93942 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2535ea7f-d76c-3eab-b7d1-068dc3e80491 | -6.76473 | -42.23686 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ec56c9ae-cc37-3786-b346-ecf9de80693d | -13.38533 | -47.56348 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1b25ad-769b-3a9a-b662-2a8707c75359 | -13.46326 | -47.26181 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a193b84-3cec-38b6-8d6b-f9ed4274cbd1 | -7.84768 | -56.55029 | 2025-10-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1503383-64f7-3e3f-8716-4a92e52bb03b | -10.05779 | -45.56398 | 2025-10-05 04:46:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f41d93a0-2898-3009-8ec3-9d7e01d16150 | -10.65646 | -58.76075 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c09ba569-cda5-310a-b88a-d5428de323a8 | -13.45888 | -47.29408 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aa4841b4-65d0-3d9c-bf78-3f9594479f7d | -12.2642 | -55.12217 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8fa9e92-8e23-36ea-967b-f7b5398efd5c | -11.52592 | -47.66854 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8502e1b8-79a8-3244-b62b-977a59446a00 | -9.30147 | -45.99521 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 14041874-5a44-3beb-a8c5-19b7aef776ac | -13.48632 | -47.27673 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9d8794c-e65b-3455-878b-4f9fea2a3522 | -13.15842 | -47.96696 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3b561a1d-ca34-39ff-a6a4-b17a57da6716 | -13.37044 | -47.55205 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91c1fa33-5f66-308e-81ca-3ad9bce57cb8 | -13.34726 | -47.78621 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d95dd77-9578-363a-ba6e-12a86c6bb46b | -13.35386 | -48.05993 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3595c7e6-4c4f-3808-a221-7b74bf3b8305 | -12.59306 | -48.1411 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c1b5562-666b-333d-a7c4-44c023c855bf | -7.71213 | -46.26869 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4354a618-db8e-34d3-a31c-8e4b8e72bb77 | -11.13156 | -47.8966 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6d8da7c-1cd0-3a4a-8a38-3be18ce0a33b | -11.74068 | -46.8252 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ea63bf9-f447-33ee-a9a7-2fa564d183d7 | -11.25596 | -47.78485 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 85f82864-239c-3065-8bf2-cb91d93e96ff | -11.73676 | -51.48009 | 2025-10-05 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README82.md)
