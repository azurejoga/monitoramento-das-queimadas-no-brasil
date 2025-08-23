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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c50e12ec-2e29-3ce2-896b-b403559907b4 | -4.33691 | -46.45313 | 2025-08-23 06:16:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 803273f3-d09e-3731-bb03-9983f0c65b12 | -2.93154 | -53.69777 | 2025-08-23 06:16:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35828b46-a07b-31d5-a4fd-324fc45b6b63 | -2.55225 | -47.70684 | 2025-08-23 06:16:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| dda612a7-0d44-3948-8886-bda0df874329 | -4.33831 | -46.46077 | 2025-08-23 06:16:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| fb794f71-8355-35b5-8882-e9b41aab3727 | -3.43216 | -49.0349 | 2025-08-23 06:16:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6236d8eb-38c8-3808-99e3-18d6b5118120 | -3.43048 | -49.04644 | 2025-08-23 06:16:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ade6a49b-f6cc-3fc0-b006-67dd2ecdd3b8 | -9.52028 | -60.53004 | 2025-08-23 06:18:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| d40ffd13-9f22-37e9-9b0c-a5540a4017b2 | -5.74778 | -57.58393 | 2025-08-23 06:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| ac8da431-2618-3b31-aa2e-9887603503c2 | -6.57505 | -59.87098 | 2025-08-23 06:18:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 89b1cf26-66da-3192-b472-37a8d1bd09b2 | -6.18366 | -45.42487 | 2025-08-23 06:18:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| af68baa2-2cea-3d22-96f2-0e08871cb72d | -5.73427 | -57.59695 | 2025-08-23 06:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| d07da887-d73c-35f6-8722-d749b210f3c7 | -9.16173 | -59.59705 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 44d27d34-94c0-37c5-af73-823b7fa82b51 | -5.87085 | -57.75243 | 2025-08-23 06:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 86bae6f1-3535-340a-9cbe-d21fb5aec405 | -6.60452 | -44.56397 | 2025-08-23 06:18:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| f024c768-119c-38bd-95db-df3f8c9f9b8c | -9.51079 | -60.50632 | 2025-08-23 06:18:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| a659b7c4-68b0-39ef-8b79-13fb7d51c1c5 | -9.2004 | -59.43647 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1fe54b21-c648-3ffd-a4d2-863ce6b1e266 | -5.74545 | -57.59858 | 2025-08-23 06:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 909470e5-9b55-379d-b927-65ae993ce1c9 | -7.02003 | -44.64299 | 2025-08-23 06:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 42351d83-efff-3569-8842-322c6a3510c0 | -6.72156 | -51.97406 | 2025-08-23 06:18:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0b5fd400-6b94-3f5d-9404-7226ce046e2a | -9.18478 | -59.62691 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 27fc9e7e-b6f4-3fa5-a5f8-d7d8bcd4bbea | -5.73661 | -57.58232 | 2025-08-23 06:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| fdfb956c-5970-3471-bdfb-26ebebd3e31d | -11.11114 | -44.74008 | 2025-08-23 06:18:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 9e807dee-0195-378c-8b48-1ad095fe8e6d | -6.45541 | -53.39032 | 2025-08-23 06:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 438bca8d-d359-30d3-bb1b-83a77d1d4fe2 | -5.82322 | -52.06252 | 2025-08-23 06:18:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6a7b87f9-a8f6-389a-83ad-89061964b590 | -7.01902 | -44.64783 | 2025-08-23 06:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5f5b6dba-1f13-3e9a-985f-e5919a513e31 | -9.15218 | -59.50195 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 236f4487-40b7-3309-ae83-5f40dfd4d477 | -9.51664 | -60.55149 | 2025-08-23 06:18:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 504c6d49-6b3d-3866-a54a-f12c8c330716 | -6.05641 | -53.87903 | 2025-08-23 06:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2f5dc07b-9e69-3ec3-ab3c-721d8636c8ab | -11.11886 | -44.73332 | 2025-08-23 06:18:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 5b97fd4b-1c3a-3694-bc3f-3442a1b7e2d6 | -9.44076 | -47.64931 | 2025-08-23 06:18:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 26d6d005-61e6-3d5c-9bbf-a2ae963590ff | -9.18788 | -59.60854 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 8b5be583-7f8c-337a-b4dd-81ee5cae3ae4 | -7.02273 | -44.61838 | 2025-08-23 06:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| deaf8b2f-da4b-3932-aaef-2ad92bc95c31 | -6.60697 | -44.55652 | 2025-08-23 06:18:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 97bba932-45e5-3500-9069-2adbd495e951 | -9.20013 | -59.46193 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0cf0d1de-057e-3dce-a160-8cf83f3d373a | -9.20314 | -59.44416 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| adfa9e95-e74e-3bd1-b527-c69fa7824f3f | -9.16641 | -59.58613 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5d266238-3118-37ef-8e3a-ac92a2bfafa6 | -9.19752 | -59.45425 | 2025-08-23 06:18:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| bbbd1707-f445-3618-8df0-1955d25e3683 | -7.02398 | -44.61339 | 2025-08-23 06:18:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 778b38c0-616a-3fce-83ce-dcf38345c8c0 | -5.75009 | -57.56942 | 2025-08-23 06:18:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9f876d5a-86b8-3a98-80cd-1fdc96011108 | -14.2744 | -58.5266 | 2025-08-23 06:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| b097a3d5-2f46-340d-a0ac-90b9fd9ea46e | -20.4035 | -45.6162 | 2025-08-23 06:20:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 67.5 |
| eb873a43-c16c-385e-9eed-a1138c8353bd | -9.968 | -60.1937 | 2025-08-23 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| bff8e2c1-e677-3176-8355-e896d646b97f | -9.9495 | -60.1754 | 2025-08-23 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| fb12439e-c22c-38ed-a368-9dcc06e25c87 | -15.0761 | -48.4957 | 2025-08-23 06:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 04f5b4fa-3af0-3914-b116-e3f5597a6634 | -12.9921 | -45.2252 | 2025-08-23 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| bf4a73f9-1ec1-308f-aeeb-298020a5f1d5 | -9.9681 | -60.1743 | 2025-08-23 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9d66f55f-7bcb-38b8-bc0f-9b17d8fbc2b6 | -15.0756 | -48.5181 | 2025-08-23 06:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8c607d63-a871-33b4-bf9d-4f68004b9506 | -14.2742 | -58.5466 | 2025-08-23 06:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 5b74018c-2fa1-3f85-ac7b-69b1536e0069 | -9.9493 | -60.1947 | 2025-08-23 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 8bdc0652-4764-38fa-b780-f6325471d522 | -20.4042 | -45.592 | 2025-08-23 06:20:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| cd65739d-4eb0-357d-8628-56b8edf28cfa | -5.7431 | -57.5814 | 2025-08-23 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 75c1b9c5-b183-3172-bd5e-d14ce0c4e72c | -5.7429 | -57.6009 | 2025-08-23 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 514cd710-062c-3619-a333-643c82bd8d72 | -14.2553 | -58.5284 | 2025-08-23 06:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b96ef509-7b6d-3813-967a-9cce40d3eff2 | -5.7614 | -57.6002 | 2025-08-23 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 00be5ab6-d03d-327e-9054-d9b5c8531bf1 | -5.7615 | -57.5807 | 2025-08-23 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 90e6bcca-3599-343e-8fad-5c06764a9ab9 | -13.02664 | -56.81873 | 2025-08-23 06:20:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c97bc5cf-26ea-3b46-8002-00ed6d6c4c11 | -14.94499 | -48.01231 | 2025-08-23 06:20:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 731aeba8-6f0a-3edd-8954-9ffde4cc2861 | -13.46263 | -47.02718 | 2025-08-23 06:20:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 124c5f28-8c75-36a0-b7b2-cb78ba684515 | -9.95103 | -60.16548 | 2025-08-23 06:20:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| d18eafd5-5f15-3cd8-a289-58a3247139f8 | -14.61546 | -54.85332 | 2025-08-23 06:20:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8b5295b-a364-3829-9d88-767151418f50 | -11.18711 | -55.03294 | 2025-08-23 06:20:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 89d24145-adcf-3b60-9d65-a7aa48f5781c | -13.02501 | -56.82904 | 2025-08-23 06:20:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b890e156-84f4-34e6-a3c6-2792bd497b3b | -12.99774 | -45.22056 | 2025-08-23 06:20:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 52bc413d-0737-317c-9227-1b3880d234fb | -9.96041 | -60.18723 | 2025-08-23 06:20:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4250d8c0-8896-34dd-8626-d96d6a7996c1 | -13.4197 | -46.25732 | 2025-08-23 06:20:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 3b2016ef-fd75-3925-a9e2-a7505c7eb7e8 | -11.32543 | -55.21755 | 2025-08-23 06:20:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f0e710b0-5972-3075-a2d1-d00c9fe8e29a | -11.19711 | -55.03176 | 2025-08-23 06:20:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| beae8cf5-9e7e-3c06-ae35-f21ffd24ede8 | -9.96371 | -60.16761 | 2025-08-23 06:20:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 96d8b9d6-4872-3685-ab11-14fd01f8be07 | -14.3686 | -52.04427 | 2025-08-23 06:20:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| feea26cc-1505-3155-aee2-bc2772097a99 | -12.70577 | -48.09293 | 2025-08-23 06:20:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6a6cd1d6-8dba-3a6b-9bb9-584c127eef76 | -15.06777 | -48.51601 | 2025-08-23 06:20:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| fd281bbc-2a34-3ed6-be37-a97492d4aeaa | -13.41817 | -46.2522 | 2025-08-23 06:20:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 861272b5-98db-3136-9f73-fe2d07dd30ab | -14.61346 | -54.80682 | 2025-08-23 06:20:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6f96926d-f271-3460-859c-23835a207ace | -13.41491 | -46.27884 | 2025-08-23 06:20:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| b488d628-9941-3eb3-9675-a7ff9661bf0c | -12.70267 | -48.10419 | 2025-08-23 06:20:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| d8d71043-7b82-39ee-ab48-aae5da99cf59 | -9.94772 | -60.18497 | 2025-08-23 06:20:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 210.6 |
| 149624ee-df32-39d5-b04d-7c2b9bc8549f | -15.07018 | -48.49582 | 2025-08-23 06:20:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fa447d0b-cd94-3cd8-87d3-4e5de9ca6afa | -11.1885 | -55.02379 | 2025-08-23 06:20:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0cf6b63b-05a2-38a7-9ee0-b399db9a27c2 | -14.6121 | -54.81584 | 2025-08-23 06:20:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 85c32ef9-b8f9-35b3-8432-47d13f68cade | -14.3671 | -52.05505 | 2025-08-23 06:20:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e2b3a72e-b170-3e7a-8e29-5419960baf19 | -12.70354 | -48.11138 | 2025-08-23 06:20:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8c2a62ba-9141-364b-b9ab-8213acad445d | -12.99244 | -45.22459 | 2025-08-23 06:20:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 702bf891-f435-35df-b344-a6c3f8fdde28 | -13.03555 | -46.79582 | 2025-08-23 06:20:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| e6a29ac8-28f9-3755-b689-2866a8fdb7cf | -13.42537 | -57.16356 | 2025-08-23 06:20:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 16ad4467-c123-3264-b0b8-05216856d49c | -9.94442 | -60.20451 | 2025-08-23 06:20:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| dff2059c-2f81-39b3-a9be-eeda9235ef70 | -15.02567 | -54.90186 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cd02d0fa-596f-3cb2-84ef-1e838dad2aed | -15.01824 | -54.89145 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 38155e06-f9f1-3a12-a8d4-ce6a396e01aa | -14.26267 | -58.52117 | 2025-08-23 06:22:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e7821bdb-c763-38b7-a518-b50f107c37e3 | -15.02839 | -54.88379 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b4619c69-f527-315c-9e7b-0dd6701c7a8d | -14.28616 | -60.38728 | 2025-08-23 06:22:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 17290faa-1228-3ea9-a866-87773c195a98 | -15.02703 | -54.89282 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 8704080f-ea9c-35f7-9b64-4e5bc68ac4ad | -14.25027 | -58.53189 | 2025-08-23 06:22:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3e867f4c-5b9b-356d-85b4-e96deda72989 | -15.06163 | -56.40247 | 2025-08-23 06:22:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6fad89ea-30ce-3d8d-921a-c45788b31a57 | -14.26056 | -58.53367 | 2025-08-23 06:22:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 4653a99e-5016-3bdc-ad7d-df38bef06583 | -14.75695 | -55.98758 | 2025-08-23 06:22:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ad8fb958-4271-31bc-88f5-c8c7e8801f4e | -14.6617 | -56.59002 | 2025-08-23 06:22:00 | AQUA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 72e082df-9034-3e31-97e1-151f415421ce | -14.66349 | -54.9128 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 19043afd-b3c2-3b71-9a9f-187c50c226b4 | -15.58613 | -54.29463 | 2025-08-23 06:22:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c37bb2ea-1699-3933-8306-977e70593429 | -15.06316 | -56.39284 | 2025-08-23 06:22:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3401256f-ceaf-3610-b070-9b55c0a38d61 | -14.66329 | -56.58004 | 2025-08-23 06:22:00 | AQUA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README83.md)
