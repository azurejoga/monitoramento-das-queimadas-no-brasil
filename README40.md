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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6575a5ad-f57f-3dbc-8ba3-fd43d103ae3f | -6.78618 | -59.46394 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 905a9d72-3a4c-382f-a939-f14680b532e0 | -8.9544 | -60.58437 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52f9bb23-5bce-30ea-ae78-df0747b8b6c4 | -8.95149 | -60.60022 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9ea2763-b496-3fb4-8fbe-433190dee090 | -10.07456 | -60.49775 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f693273-eb0f-3c58-a69b-03fcdbaca309 | -7.39465 | -55.47918 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d19bd695-1ac0-34ce-9b22-2eb0846b3003 | -12.71049 | -48.47978 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16f13bc2-7b1a-32e7-9e59-a7319bf5fbbe | -7.3931 | -55.48853 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 592922fe-dc46-3d07-84f5-a600fa8b39ab | -13.50561 | -46.23452 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d79a557b-cbce-3a43-9440-39269a743dc2 | -13.26404 | -51.65676 | 2026-08-17 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37cde11a-72f1-39cb-8b61-1b22284e9d50 | -11.7124 | -54.61398 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c259fa52-f50e-3f87-b412-e37b7868326b | -6.63699 | -58.97219 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5c0747a-3266-37ec-a4f6-3db120eb95be | -11.71175 | -54.61785 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18f09b6d-f037-347d-a78b-ad5922ea6a67 | -15.06252 | -47.0446 | 2026-08-17 04:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 71f95955-010c-3cdc-a552-a2b9da65949d | -12.04305 | -46.48375 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 185270b2-285e-3284-a69a-0bef6eb42c74 | -14.37875 | -53.13841 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1cba616-525b-3777-a233-2f137c301a0e | -12.69239 | -48.5245 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 534a6aea-856e-3603-b7f5-c5b999abc665 | -8.96021 | -60.52348 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4510e97-8eab-30a1-b948-e39e71c004bf | -12.66391 | -48.50626 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70d3d3f5-0589-30ee-9356-2720d6386f53 | -13.81077 | -53.84818 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c737ee49-8716-3a74-8a83-47608d885249 | -11.82619 | -51.77367 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b222c4c-0fa1-3bb0-8ef0-5247230a9ff4 | -8.59381 | -54.6861 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef9c8656-7b4c-388e-af61-30ceb7b1dce8 | -12.24899 | -43.15307 | 2026-08-17 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 46fecfd5-0c3a-341c-9b33-3d79a418473e | -8.02289 | -55.14767 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca1a9c25-4432-32ec-ad70-3b57170bb5ed | -12.00523 | -46.47256 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 434e31e3-0702-32cd-a845-a293f30a60c9 | -9.35269 | -63.56654 | 2026-08-17 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65ba8448-10ef-323a-8fd8-25c88638da94 | -8.67243 | -54.77435 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80a7517b-c25c-3a71-b109-d2b6f67af6b2 | -7.36183 | -55.48817 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 976f8cd0-efef-3238-adfd-ef6e722ee173 | -12.32698 | -47.25063 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4ea2eb0-0c8e-3889-b80b-f90255d4b88d | -6.84823 | -58.96869 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc5661e-dd94-320a-9560-485f0a265e1a | -8.09431 | -61.3554 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9acb2d0c-737e-3cc4-adfb-06549f88cf49 | -13.78772 | -53.79966 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aaf9e33c-49f1-3803-a5ec-2e7e497be24e | -9.60028 | -60.50278 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b032a39f-4164-3cb0-8ab1-394c09f74d51 | -8.58885 | -54.69375 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3485a5a3-b2c6-3b67-aba1-a2e9ef4c861a | -12.33056 | -47.25488 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0123ce0-11c6-33b6-9f00-a628c2dcbfa8 | -6.76973 | -59.76627 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83bc645a-edb4-3539-b5f2-53ce634f64c7 | -6.69797 | -56.1675 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de3b2c3-6984-37c8-832a-6e5d63c2a6a4 | -11.71587 | -54.61457 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45aaec38-0575-32a8-a4ce-db2396a46e69 | -8.59877 | -54.67841 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01f2b3cf-350c-3a3d-8c37-6efc806a7bc5 | -6.7812 | -59.46291 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2b919cb-2235-3137-9162-ef1744ef3581 | -12.00095 | -46.47188 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b3c8104-60c4-318c-a34e-8890cba92be3 | -6.70168 | -58.96311 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18ce4f0e-003b-37b7-9e38-626b76a1cf80 | -14.87187 | -46.66393 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 271fb82a-f3ea-38b1-bfea-f20eda8b93a6 | -14.86904 | -46.65113 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac76c905-860f-397b-b0fd-51755d3fa176 | -10.2797 | -48.28496 | 2026-08-17 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdb71fe4-407b-3212-a54f-b1c57f37bbce | -12.00634 | -46.46443 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f605534e-a9fb-3909-ad1e-ac0b86118d84 | -7.80872 | -47.83346 | 2026-08-17 04:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 324ed7a3-e586-3a42-957e-b1cb43beb7d5 | -7.34122 | -59.60095 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 573ec628-7775-3035-9699-a11ca5549135 | -8.08743 | -46.89406 | 2026-08-17 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf8a728a-d97f-33a6-a6a5-6410dd2ef4ac | -10.46709 | -46.29746 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1246a8eb-c884-3f13-b72a-d7206cb3c658 | -6.86121 | -56.43167 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fad04405-c5b8-3775-b200-5fa2feaf8e4e | -11.48014 | -46.57513 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad3c187f-cd1b-38a8-9ee0-f989374fa748 | -15.83142 | -54.21218 | 2026-08-17 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f25c0946-ec33-3859-91fa-ec1bda6abc23 | -16.08851 | -49.78833 | 2026-08-17 04:59:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a3e9e59-fb26-3b9d-a9f9-98abff25895a | -16.22687 | -49.70504 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4340db86-6bb6-3337-b6a7-3d64751a7473 | -15.72729 | -45.97511 | 2026-08-17 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad63c894-f6a8-3dc3-b425-47696cc0fa34 | -17.53647 | -49.20938 | 2026-08-17 04:59:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c55b9466-7632-3559-bed1-597da9e6e906 | -16.23187 | -57.65087 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9fcb8179-1937-331c-8967-f928525a1bca | -14.20707 | -60.20296 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 834111f8-10b3-321d-8ad3-4596d76d3124 | -15.24013 | -56.47491 | 2026-08-17 04:59:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07c5cf84-577e-3b06-a8c2-ce42aae74941 | -15.90853 | -55.52026 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0304fc72-8028-31ac-b8ee-eaf8add46748 | -16.22807 | -57.65015 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a1bc6a99-5233-3830-a890-05a65dc352a9 | -15.73069 | -56.12125 | 2026-08-17 04:59:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f2d57675-54fc-3cf8-b54b-94ce9f219847 | -19.27652 | -44.97074 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e73804dd-831e-350f-8afe-e60bfb63532d | -15.70002 | -53.81129 | 2026-08-17 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a90fcdf-ab78-36e3-999a-856e579dfb3d | -15.02529 | -52.72503 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ab158e8-c19e-3571-bf69-14d3177d2fac | -15.16541 | -50.08125 | 2026-08-17 04:59:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c4fd6f1-d87e-35ef-ad90-81c9a9462467 | -15.94383 | -47.8393 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69e1b850-0028-38fa-8248-cdf1872e21b0 | -18.80573 | -46.73595 | 2026-08-17 04:59:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c04a97d4-525b-31d6-84ed-5f73e00e9e7e | -15.90806 | -55.54414 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2e33bb7-30fe-325a-97e6-8ce54ab1675d | -16.22489 | -49.7031 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bae0727c-2d0e-3fb1-b89f-efd6f469ee1f | -15.91979 | -56.48314 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de02c999-9ece-3da9-b3a5-ab8ba8ca30a5 | -15.92299 | -56.48129 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f72d671-f301-35e4-ad9d-7376a445e605 | -16.60417 | -52.59644 | 2026-08-17 04:59:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f132dc9e-9a68-3195-9b08-fd473a8ccd15 | -16.32977 | -55.38588 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6db3a739-fcac-3d51-98ba-07491c608fbd | -15.81461 | -48.17008 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eb0668f-b1ac-39c1-86fb-c76ca3475f33 | -18.4257 | -49.69796 | 2026-08-17 04:59:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dbde9ff8-fe67-32a6-8faf-db7d0e648ed9 | -15.90527 | -55.53956 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 745e599e-d155-317e-9b2a-fb3972771db1 | -14.09248 | -58.4405 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f2adea6f-c216-38cc-a7e2-1e48b73f4cc1 | -16.1814 | -46.80346 | 2026-08-17 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd65ea60-d25f-3785-8ab0-33b614d1e207 | -16.17841 | -55.95461 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6846cf9a-0627-3af7-8f06-23ced851954b | -16.18278 | -46.80503 | 2026-08-17 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58d4bbd7-7173-379b-b108-22d27aa847f3 | -15.90444 | -55.52342 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 516aef9b-7d44-3a93-be75-16886ed6dac6 | -15.90871 | -55.54026 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9f109ad7-4043-3bb0-ac26-cad8c4f75a18 | -15.94649 | -47.85143 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3af159f-1943-33e4-9b73-af9e5a5dadc5 | -18.44394 | -49.7359 | 2026-08-17 04:59:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2512e6c8-744c-3f7f-b291-b474e5d3f31b | -15.21161 | -52.70794 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ae3388a-d668-3342-915c-b95cf06e26e4 | -16.81923 | -49.07163 | 2026-08-17 04:59:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae7b640f-b32d-33f8-8d78-94a637930db6 | -15.94643 | -47.84102 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5609549a-fda6-39c5-875b-5f09c9f43a36 | -20.89591 | -50.50505 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c25f9292-26c6-3d61-9259-4c984defd598 | -15.28666 | -56.11718 | 2026-08-17 04:59:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db12a3f6-a449-373c-9049-00c1f6eb5206 | -15.11622 | -53.58324 | 2026-08-17 04:59:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0923611a-9513-3b8a-b480-87687f065a6b | -15.86526 | -56.34432 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a96e8139-568d-3249-b892-2ac819902e22 | -15.91494 | -55.54551 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9113b05d-6585-35f7-9380-dbf268f38888 | -16.21835 | -57.63853 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc69186b-38eb-30a5-9b1e-b693f500cfaa | -16.67093 | -49.44782 | 2026-08-17 04:59:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03bcfc0f-3190-321e-94d8-c826e6dae702 | -15.84605 | -50.10428 | 2026-08-17 04:59:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83de4a1d-b3db-3071-99b8-755bbc6d7e54 | -20.12757 | -44.86333 | 2026-08-17 04:59:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fd53f36-799f-3edd-aaf7-9823eda4ef44 | -16.41096 | -49.62939 | 2026-08-17 04:59:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c621cce5-105d-3883-a8ff-a22e02285152 | -20.73446 | -47.8227 | 2026-08-17 04:59:00 | NPP-375D | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91dc21de-38d3-3b4f-8979-ed6c0b643243 | -15.17022 | -50.07354 | 2026-08-17 04:59:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README41.md)
