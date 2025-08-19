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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e94fd9b-f42f-30d1-8717-77d24e60c085 | -13.17789 | -46.88534 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12ecc99c-76c2-3217-80e3-23bf36d91e0e | -13.48061 | -47.08368 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e89d001c-b726-3336-9005-ad1343d279b6 | -13.24654 | -50.79837 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab564df4-ecb1-392b-9397-263b386112e0 | -14.8512 | -48.07364 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 710c2467-552d-365c-b468-5a5a9c761fea | -14.17532 | -45.30395 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b24ad9d3-4f7c-3806-945f-71c5770de125 | -13.01414 | -56.84341 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 60962a58-f6ad-3581-9291-7f027242e915 | -14.84789 | -48.07309 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90b969c7-3abb-3e3d-97f4-f3e4aa8e0bba | -13.176 | -54.94828 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1854a7c2-cda3-38c2-9f8d-2d3b4d93861c | -11.83862 | -50.59298 | 2025-08-19 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f6517d0-be7b-368c-be48-5b04163b12a6 | -13.59333 | -46.99493 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f174d46-e4c8-3776-b7dd-f713e87e2ed8 | -8.70741 | -47.86427 | 2025-08-19 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 006cd588-9ab4-3e49-86a3-1d17920f50bb | -13.2536 | -50.79959 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72a9658d-f413-3904-9bf7-aeb3df32f724 | -13.18138 | -54.94445 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 135c5866-b808-35bf-b0fc-138393c2c299 | -12.98425 | -56.85996 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cc15489-527a-3c77-bf95-fbdc4bba5722 | -12.63676 | -46.89247 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7e8e0f2-57e6-37cb-b5d8-866759a9c93a | -12.98938 | -56.86103 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 050fbd22-7a08-3a32-bd17-059a3efa7351 | -13.42421 | -45.91228 | 2025-08-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa7f1670-bd40-3f4f-8cf7-af07ed63e687 | -12.99699 | -45.20912 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4dbc5b78-6dc2-38f9-8732-aad2b458e548 | -12.61636 | -46.896 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f516ddd1-55e7-3872-964d-4348c2b90cd3 | -14.16762 | -45.30696 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bbad099-f006-32b6-9312-47582d86f6c0 | -13.13822 | -57.1536 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 050b0abc-678c-3677-a7fd-4be2240bf804 | -13.18233 | -46.87859 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71ddf52e-f3ab-367e-ba97-8d7c65e48bac | -14.86663 | -48.0616 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b63813b-1132-38bd-9fbf-e99b1feb2cc1 | -13.86643 | -45.54342 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d2d05ff-a917-334b-8a76-dd8004e50ff8 | -13.31561 | -50.7978 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f7b4c20-d5f9-357b-8393-9cb6cca5fa36 | -13.14966 | -54.91422 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b0d9f59-b344-3470-b879-2fc55ab5c4fb | -10.29738 | -59.45966 | 2025-08-19 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 770b6210-f8af-3837-a73d-6ae9413a5dae | -13.01084 | -56.83302 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7f4f23c-baf3-3811-b048-2728b016a0f6 | -8.09861 | -44.83833 | 2025-08-19 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6efc9559-80cc-32db-811b-e0985779c77c | -12.99536 | -45.19381 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbb3ac4f-0e9d-3361-9cdb-0f2bc09aa20c | -12.7376 | -45.05265 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c537fa6b-0929-3402-839c-ce73bfa38794 | -12.96055 | -46.15335 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b44ff3b-b6be-3fe1-aa5e-9fb0a67913a1 | -13.44293 | -56.90048 | 2025-08-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e64c6f8-26fd-347d-99cb-860e65cb41bd | -10.08582 | -46.35654 | 2025-08-19 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41865057-9718-3f65-9792-6eb83ba8f00f | -13.15881 | -54.9402 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d9d5ba37-8cfb-3151-ab35-940748437e6a | -12.43283 | -48.70142 | 2025-08-19 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 702e6e62-d211-32d2-98d0-8603d00ce0d7 | -13.61895 | -46.88755 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 954517f7-b96b-3388-8d9f-268eb1dcb626 | -9.33377 | -48.51871 | 2025-08-19 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5745cdb5-c4ba-3502-ac8c-90c5b0c3f837 | -12.88441 | -46.07989 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac2d6e1b-ee2b-3f90-87bd-e3ad61203415 | -12.99224 | -45.19182 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 415f0ecb-3f20-3b33-87ee-a006a5bcb586 | -12.98159 | -56.84637 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98a31f97-1c82-3369-9e73-f4eaafe40a23 | -13.31628 | -50.79375 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f7fc966-9af0-3778-b8a0-7dbd9b9ebece | -14.17771 | -45.31278 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9480abbb-2410-3c41-8e98-12aeae1e93ae | -13.01655 | -56.831 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebcbe63e-7259-35df-a5bc-bcd2028ef30e | -13.34834 | -54.40717 | 2025-08-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 049fe4de-d5db-3463-a074-0e59617176d1 | -10.88987 | -48.49508 | 2025-08-19 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d78150b-6c23-35af-8959-67f31e969fed | -9.35069 | -50.2518 | 2025-08-19 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fce12485-2ff7-39b5-9236-8a3af6c59c4d | -13.37522 | -54.40754 | 2025-08-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee29dd89-d640-36f1-b170-4f40672126f5 | -13.56334 | -47.01194 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9f82bfc-a094-3531-83c8-3c25a92786d7 | -14.1706 | -45.31165 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbfcf061-2cfc-3f30-a09e-16ae00d14f05 | -14.16704 | -45.31111 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36fa4d3a-8e70-35ef-9c1c-71a0ee2fb208 | -12.98363 | -56.86316 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af604ac1-250b-3807-afa2-c68f95c42489 | -14.31569 | -53.38298 | 2025-08-19 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9351d345-3ed8-3206-9685-7c1f59bfc1f1 | -15.67716 | -47.58575 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eb51a63-7ec5-3af8-91d7-58571f11b63d | -15.75476 | -46.60575 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 468d790b-5139-31f1-981b-e2d67aeb730a | -15.98144 | -48.08241 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 562e66b4-90c3-393b-9753-1d82d9fd9ba0 | -19.8205 | -44.32404 | 2025-08-19 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ab255c6-0902-3680-91ae-fe481dd9a983 | -14.97525 | -54.81086 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cd3ddeae-7b9b-30b9-9114-ee15439ad618 | -16.48886 | -45.08966 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1a345e5-0094-3040-a972-b4c23bbcbd8c | -19.3092 | -46.84263 | 2025-08-19 04:29:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 413a62df-2598-3eb3-8eb5-7e60720301d3 | -16.80984 | -49.20207 | 2025-08-19 04:29:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f281adf9-7598-3614-94c2-fc13357355bd | -15.18591 | -48.75988 | 2025-08-19 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fadda0e5-a0fa-3f1d-8aa2-3b8cea8a549a | -14.98553 | -54.80372 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94747bc0-1223-3754-bb07-1c3b28dafd6d | -15.74738 | -46.60825 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceca8eca-5b16-39be-9711-9dc870003273 | -16.47473 | -45.09004 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9108713f-1fa5-3b9e-ade6-f7abe0d7e7fb | -16.62289 | -51.35604 | 2025-08-19 04:29:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dde70cb7-4362-39b6-90f5-6fe791af182c | -16.81783 | -49.36593 | 2025-08-19 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67a61021-3dd6-3ba7-81ea-2deda24c940e | -17.41654 | -46.70713 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a644224c-78dd-372b-aeba-715120a09232 | -16.67886 | -49.19125 | 2025-08-19 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e010ea20-f661-32b0-99ca-5c3ae1d3bc97 | -17.93219 | -44.36575 | 2025-08-19 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c56c2a43-ce42-3101-9067-da82ee09d8d4 | -15.07964 | -55.42449 | 2025-08-19 04:29:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70b9c282-9b34-3cf0-a0be-f3ea2fc0dfec | -17.42058 | -46.70372 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f4e6384-3d64-30a2-8422-c08c08216089 | -15.01651 | -54.81295 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ad0ed16c-ab9e-30d2-8a3a-28d32310775e | -16.08651 | -48.08456 | 2025-08-19 04:29:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d941507-a6f1-3e10-b82b-ff18be6d8423 | -17.33711 | -47.17647 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19bea694-8d90-3550-990e-09971294b0d7 | -15.03921 | -54.81148 | 2025-08-19 04:29:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a378ec48-4609-3891-9498-8e732d539714 | -15.96715 | -43.903 | 2025-08-19 04:29:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a044786a-68db-3baf-b250-f4d8a48791df | -17.98756 | -46.35672 | 2025-08-19 04:29:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e32f0630-dd8e-3d48-af1e-6a762db1d3cc | -15.03308 | -57.18828 | 2025-08-19 04:29:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d5cf756-99f0-34bf-8d91-bec0153ff7b1 | -15.81252 | -48.27515 | 2025-08-19 04:29:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1fbe87d9-d5d6-3a08-98b3-d1dac8de2504 | -14.40512 | -56.45272 | 2025-08-19 04:29:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3174cb90-df4f-3634-a679-ff3f51e3ee28 | -14.97171 | -54.80569 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13672493-1003-3082-b25f-8a9b07e4a9d8 | -14.62335 | -54.9234 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea88b3a0-241b-34ef-8e38-5d242bed6c6d | -15.02175 | -54.80894 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0a7a1be-8185-3afe-955e-56ee2527e029 | -20.0298 | -45.643 | 2025-08-19 04:29:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8296f35b-c9dd-3a76-8f91-96b3754f0905 | -14.96819 | -54.80048 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76114ae3-bbdc-3199-8f9a-d341ef49693d | -15.16201 | -48.78153 | 2025-08-19 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eacac4b-3a1f-3d7f-a192-4dac4da46f45 | -14.97878 | -54.81606 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76550a45-887b-3bcf-8d98-3c3c145e4e57 | -14.9801 | -54.78443 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30a894fb-9f30-3d41-85df-9882a1293218 | -15.03053 | -54.80998 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65905fb2-6859-3849-a71f-933652a6724e | -17.3451 | -47.09863 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b1969bc-aa7c-3305-a649-974376c83fd3 | -15.1587 | -48.78098 | 2025-08-19 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab9e95a1-2585-39e8-a8d2-fdf29d66efcf | -21.23948 | -49.08384 | 2025-08-19 04:29:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 63fc3cfc-9e99-38f4-bda3-a570501d51a5 | -17.88851 | -48.6071 | 2025-08-19 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22aa3ddb-fb73-3190-9a04-62880ff568da | -14.62418 | -54.91891 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca4e789e-6436-3128-aec2-3eab3c4058cb | -15.03317 | -54.81983 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d46e538-737c-34a3-a340-a577c6d5e495 | -17.64189 | -52.20237 | 2025-08-19 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a364286-f61d-3e44-b2c6-a1ce7ee7e0bd | -16.47348 | -45.09195 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f79f1c6d-6d84-3f87-8acd-67634e4f81e0 | -15.39885 | -49.13327 | 2025-08-19 04:29:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86752381-a442-31e6-b37e-f7e373e3c705 | -16.48147 | -45.08854 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README31.md)
