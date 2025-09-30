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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6672ae02-92a5-3ceb-860e-794aabf2a2c5 | -11.43172 | -43.50547 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a1bdba2-3266-3b72-a983-2ec4ffa07e2c | -10.19581 | -52.55461 | 2025-09-30 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9edf8034-32b5-3384-99fc-8afd3da2711e | -11.64743 | -47.49024 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54dde31a-2238-3b10-83bb-446b874b0d4b | -8.15594 | -46.38163 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8ed86597-8766-35b6-9328-bd0845f5f179 | -13.22207 | -50.93092 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 47f2a2b5-94a5-3f53-88dd-2d40068d1ba9 | -13.01085 | -49.44139 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cda2ad8e-8514-3390-8441-6d2d8fd6c6ad | -13.60373 | -48.03238 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb48658e-44c1-30b6-ab01-36a2f87bc50d | -7.52239 | -45.43842 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9cad8de-565b-37c1-88b2-6a33d151f842 | -7.37062 | -47.04618 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0e9ea9e-1977-3c45-8b6e-cd4042754fcf | -8.83885 | -46.18496 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e60d070-dffc-3f10-ba77-44047338473a | -11.45757 | -51.50132 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b14d295-a367-39a5-b98c-8005d932bff3 | -7.01647 | -45.21934 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb883c70-b1fd-34d1-9ba5-67cc025ffcc2 | -12.88812 | -44.69391 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c819b19-b5b0-35cb-84c4-21f10fa8190d | -11.6468 | -47.49449 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e375466-4590-310f-87d3-0e20c95974b7 | -11.25722 | -47.22332 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ae7a562-4230-387e-9c19-8ee0971c4f16 | -8.01994 | -55.41314 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d6bbf4a-4adb-3732-a364-b104df4d7a99 | -14.44854 | -46.35477 | 2025-09-30 04:40:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b29b8f7f-f46e-3293-89ab-d50735b86e78 | -9.32197 | -50.62773 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6683bbcb-603e-3a03-a072-1334316b73b4 | -9.98806 | -45.41237 | 2025-09-30 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 501e4bdb-fa9e-3ddf-b6f7-bd3ac5cfd346 | -9.13063 | -47.62799 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c70978aa-8002-33a0-9b27-031604958c4a | -11.66077 | -47.48592 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 335aa392-59a7-3051-9606-e6be2ccc25af | -11.25142 | -47.23278 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 060a8ff0-ab39-35ad-8a08-df25b1a93027 | -10.41362 | -48.17168 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6008d00d-e9aa-3ead-a40d-0841114fdd94 | -9.39995 | -46.56784 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f8503d2-a131-35f6-993e-405f660540f3 | -11.88517 | -48.03542 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c635cc7-af7c-32f7-8afc-afa91ba8d08c | -11.46145 | -51.49833 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b22ca13-e701-34a3-9269-59cbad7d3cc2 | -7.50181 | -45.445 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e880762b-db0d-3c05-bd49-f8976408cc66 | -11.02659 | -49.8211 | 2025-09-30 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35a9b358-5b44-39d0-9d04-78d2430cbaaa | -13.21216 | -50.92932 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 67a8a0b7-cbf2-3472-9a20-bac181acf568 | -8.38157 | -51.06586 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f4e2c17-0571-365b-abe9-56f2acbad2e4 | -7.05493 | -45.19981 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9928a77-9e3e-3747-9b9e-f9cb15496266 | -11.25235 | -47.23147 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b7d8504a-7235-3483-83fb-cc73aa66b035 | -11.75006 | -46.85313 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 598a334f-daf4-3391-9520-2ef97738c15c | -9.51191 | -47.68749 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a9ffa11-405a-3870-bd07-8a988d605b5b | -8.45513 | -50.04027 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2dfcc35-2319-35ef-85de-d5fe55649136 | -13.65321 | -48.05945 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e51e927-45c4-3cee-b559-5f8b22ee420c | -13.63204 | -42.53653 | 2025-09-30 04:40:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66d3b6dc-c15e-37fb-93be-df2765db0bb8 | -8.25196 | -45.52749 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 958ec410-b785-3586-acf8-97374beab61b | -11.67134 | -50.96994 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4cb6dff1-6b09-3adc-9d2a-5bb8a8e512be | -11.25296 | -47.22712 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90bff155-0293-360a-8130-49e7bca71955 | -11.17689 | -47.23439 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db8fdebf-f247-3626-9759-66af8fd2ec7a | -13.39941 | -48.07164 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39d2aba9-3e1b-3c63-84a0-3c8be8d007aa | -10.19143 | -44.88321 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 8ea30e52-9baf-34da-86f1-051fe95b3468 | -12.46142 | -49.10316 | 2025-09-30 04:40:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 354b8d47-c231-319e-854c-3c49e58205f6 | -8.87171 | -46.65327 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6df9c9da-5463-31e1-9255-a86609d71129 | -13.60213 | -43.46447 | 2025-09-30 04:40:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbc96ae1-dccf-324d-84f5-7ed0e62faac0 | -9.46426 | -45.48396 | 2025-09-30 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1a8b8c1-41a1-3dc9-971a-2f317817c283 | -13.82169 | -47.47104 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79fb8136-1a30-3ddd-9cec-885f30b55ff0 | -13.3594 | -47.81386 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd148444-66e1-3e5c-982d-8fb926a1db67 | -13.74717 | -47.91719 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a525d74-85f9-38d2-9a70-00a5ff727cb3 | -13.76719 | -48.3261 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 988a2b5e-b3c7-340e-85a2-ae8b77c39925 | -13.78601 | -47.96608 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78c1a69f-3b3e-3732-b15f-02d27362c3a6 | -13.34855 | -47.81227 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f1e30b-7e65-3815-ab63-9f4f871593cc | -13.81448 | -47.94728 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93de6912-fb79-3236-a8bd-1a019e472dc5 | -13.79201 | -47.97567 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a76f8b2a-b1fa-3457-87b5-da307711f0fd | -7.49749 | -45.43246 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da82467b-2873-396c-83a8-94587ece7268 | -8.26177 | -45.51392 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91c3b7b0-20b5-3871-8f40-32a979a88483 | -13.38631 | -48.06129 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11a87799-fcfc-3d25-8cd2-b130a6d9867f | -12.95917 | -46.41795 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 680610f5-e5cc-3b6a-bf0b-00c1fa8f588a | -7.02422 | -45.22044 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8289e17-bead-3253-b622-69820ed6bc93 | -13.74538 | -47.90408 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be72494c-f053-363e-9d16-890c47d5cdd0 | -9.56331 | -50.9535 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0476bfaa-1a36-3989-9510-a0040fa5d363 | -13.00747 | -49.44085 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c3cfe77-d4e4-3159-9287-cc10771e97ff | -13.83595 | -47.47715 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f04f114-c118-32e5-b9bc-4c4719fe69cf | -11.15501 | -54.12852 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 18f66d1c-a288-3081-9f5d-5d10210c28c1 | -7.21961 | -46.606 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1fdccca-8def-339e-b72d-d10b68d2b81f | -12.9607 | -47.17445 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bad8bdf-54fd-3f0d-beff-462f69cd3b03 | -11.84489 | -46.61668 | 2025-09-30 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f87564bd-3519-3f9a-b4d5-091b38df8999 | -8.94343 | -46.72765 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b62f942a-d0c2-392f-9396-84f938d0095a | -8.84372 | -46.66393 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fb7dd08-4ed2-39c1-b019-0326a72bb2b8 | -13.22537 | -50.93146 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| da6b7f62-e59e-369a-a328-133e50f3405d | -13.15366 | -47.41974 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee7d81a6-b7d5-30ad-a6bf-d5ab3af20459 | -10.42756 | -46.14408 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a84117ce-c295-3239-84d6-29060d1e7325 | -13.84648 | -47.50996 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef6f6989-5ef9-37d3-acfd-1185363b58ae | -11.88988 | -48.02799 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35d76b65-a44e-3e33-9c2a-27d96819db12 | -7.91272 | -44.6257 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f1dd76b-d71d-32e3-aac5-ce68697633ce | -10.62409 | -48.54731 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7de48bb8-7daf-334d-843d-ce47f3da650f | -8.83134 | -46.18407 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ed7f637-0875-30ca-a30a-0af764755c70 | -8.15963 | -46.38206 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 975ff884-d460-3cb1-a66e-c25c8806c83a | -13.81942 | -47.46864 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de45958f-a002-3581-b309-b47dfd509cf1 | -13.21877 | -50.93039 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 9a5e0519-aa31-3475-a36f-77c6865d4331 | -13.20667 | -50.94287 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| aa65bcca-9a1c-318a-b604-3b71544ece34 | -9.37789 | -48.95299 | 2025-09-30 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a06e559b-7fe6-3b7a-83c3-bec8c44eb3d8 | -12.84067 | -47.01483 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eaf47efe-4a86-333b-8a53-668863677cee | -14.72785 | -45.21228 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40b203cf-dfc5-3286-9d1e-5b4ee7de254c | -13.63399 | -48.04012 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bcd7031-283c-3051-8127-989a927af84f | -7.04544 | -45.18346 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9c2e5d8-8db6-3e21-9bd7-1803fd41ed61 | -12.84443 | -47.01539 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72766b89-20a2-3158-ba51-24cbd21e38b4 | -10.33777 | -48.2122 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80332d6d-9a24-3577-a191-c9a72020f398 | -8.253 | -45.54799 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de2b5cca-62d0-3343-ade8-5e22e46480f7 | -14.04047 | -42.15126 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9fee8732-43d6-3d16-9b86-83f87f2f7bf4 | -12.78502 | -46.88621 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba117ac8-0ea6-3c73-aa4d-7d4fd821c5d6 | -10.96938 | -47.79425 | 2025-09-30 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21128ac8-42b8-3aa2-882b-c7ca3d9246da | -10.83442 | -47.97541 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f03e8d7-10d4-3fb7-b7db-e4ea6f5baf11 | -9.00855 | -47.84003 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05eeb044-b3c7-3017-9e32-e68e44f63699 | -11.66141 | -47.48137 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 022dd74a-8e97-3ec2-ba6c-699ace70df1d | -9.61062 | -50.89282 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a928415c-27c2-3f98-af28-c36802e310c0 | -7.05638 | -45.18998 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e24aea4a-984a-3aae-9a5d-a23ae65eac37 | -13.2192 | -47.32278 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47bc8afb-c01c-347e-9f9c-9b4e238843a1 | -13.06458 | -47.0714 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README62.md)
