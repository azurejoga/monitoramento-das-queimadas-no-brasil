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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05a83eef-9f69-33d7-a319-8dabc5dc8713 | -2.6785 | -57.531 | 2026-09-13 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| db478df7-43e9-3209-a9e7-b27ce5d03bd2 | -6.8445 | -55.581 | 2026-09-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5854a28d-4727-3e08-8f46-4e9ed8239609 | -3.728 | -61.7555 | 2026-09-13 01:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8ccc538f-b787-3bd7-b7ef-7344431df42d | -6.1111 | -57.6645 | 2026-09-13 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7813d3bd-a3a6-3741-b8be-415a3f6b1475 | -9.7197 | -54.3587 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac407e02-09af-39a6-af4d-c900b15c4cf1 | -7.8593 | -54.7024 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b39391b6-a2e4-33df-85a5-e00d7cc78a25 | -12.1628 | -48.9645 | 2026-09-13 01:05:00 | METOP-C | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 448ef35f-ef10-3c21-895e-c1375a35ab8a | -8.0571 | -54.845699 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d771c8-afd2-3cb8-a9b4-9a38af461232 | -13.3953 | -57.0294 | 2026-09-13 01:05:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de1a358e-180b-3027-8a04-727f03c87f75 | -9.8974 | -47.586201 | 2026-09-13 01:05:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d62c4ecd-e915-3e64-abb8-892e504b4852 | -11.3352 | -48.544998 | 2026-09-13 01:05:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c3177d7-afe3-39a0-aa06-3d47e09fb9fe | -13.6095 | -47.873299 | 2026-09-13 01:05:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d884041b-00fa-3658-a51b-a66b45acd386 | -5.8081 | -53.815601 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cde75d3f-93d7-33c7-9c58-f42a716c68ea | -7.5241 | -47.332298 | 2026-09-13 01:05:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc130a19-f96d-3939-99c0-7c7056941176 | -9.4121 | -50.104801 | 2026-09-13 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2c9f5b4-5d05-3ad0-b26e-5b03e24ee7b6 | -10.4692 | -48.638 | 2026-09-13 01:05:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5b438fa-bde6-399a-93d9-e3258429a0d2 | -10.6962 | -54.1642 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32992c70-d528-34c9-bee5-bfdd41d60453 | -3.5667 | -53.005798 | 2026-09-13 01:05:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b41a986-2118-3c0c-acc6-dc631023b3a4 | -15.2504 | -42.747101 | 2026-09-13 01:05:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5347379-455c-3f03-b00d-605829816e2e | -15.2475 | -42.7743 | 2026-09-13 01:05:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b6dbc44-d129-3173-a3f2-475eece26c19 | -8.5313 | -54.709202 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 857a9b53-fa67-3786-a4f6-f6fdca7764f0 | -6.1737 | -57.724201 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0da349d-5fec-3c8c-b0bb-3a68a60b458e | -2.9697 | -50.414902 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9148a068-ff4b-3019-bb8a-e7ffd4ae1e90 | -6.0816 | -57.864101 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009d7da7-b00b-3c5b-9414-08d00b246c9b | -6.5978 | -58.842999 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 804b5848-3eee-39e5-91a1-f32fec6957cd | -1.2275 | -54.124199 | 2026-09-13 01:05:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a317b23-7725-3047-b02b-60555c5be95b | -5.1283 | -55.972801 | 2026-09-13 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64756433-afd0-3cb6-bb38-888edc8b23c3 | -10.5534 | -51.331402 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8a7dbb-8c86-3526-a5fe-c6c23c7da949 | -7.6268 | -45.979099 | 2026-09-13 01:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f813715-e511-3a83-9e7f-38e3d0c1d97a | -5.8162 | -53.806099 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30aaeb08-a3d3-3d02-a1b5-a67669288374 | -2.9418 | -50.384102 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc15e322-1983-33d2-abe8-6608374ca982 | -3.8815 | -51.181301 | 2026-09-13 01:05:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 718b0db5-910b-350e-a1d9-b85a2c6f9cec | -6.1604 | -57.711201 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6cfd0f-f58e-328f-ba56-f7145d95c985 | -12.6688 | -54.7323 | 2026-09-13 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc613b12-16bb-3cb1-9168-edc3db574145 | -7.3749 | -45.351501 | 2026-09-13 01:05:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82a508af-7df0-3b73-b64c-ff010aabef5a | -9.4096 | -50.094799 | 2026-09-13 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c307a1c1-e881-34fe-84d1-ddc4b9fe2d59 | -6.668 | -58.881901 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3e4dc4b-7873-3346-86a6-1852b4fb25c2 | -6.172 | -57.716599 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d36c42-50ae-3158-8551-6fdb3b04fc46 | -6.6661 | -58.873299 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c79566e-6c12-3692-9e8f-78d79afabb9d | -16.2918 | -53.847099 | 2026-09-13 01:05:00 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 947f7e00-6151-3e1d-afb4-794b13819567 | -2.6097 | -54.751598 | 2026-09-13 01:05:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b46d62fd-4df8-33b9-8f9d-cc19bbf8c934 | -8.5829 | -54.574299 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a013f579-e8e0-3409-b9a2-3e5271b1157d | -10.5114 | -57.4487 | 2026-09-13 01:05:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9774728e-e84b-3c62-828a-d2436aa36842 | -2.6113 | -54.758701 | 2026-09-13 01:05:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda0a763-9747-3c17-bf81-4cd7c31fdc89 | -15.5575 | -53.785198 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7c8cce0-5803-38bf-ae3b-e549f3fec2ce | -2.674 | -57.506199 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e49d65f9-386f-3e7a-bfd4-8d7047123d00 | -8.1195 | -54.8027 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f449ad8b-ffe1-3e0e-9c23-03441b7bf26d | -9.1806 | -59.448799 | 2026-09-13 01:05:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90ae5113-e706-3bc5-a1d8-8d1ffd249771 | -2.9446 | -50.395901 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90973e3b-8614-3aad-a9e2-8dea319610b4 | -9.3975 | -50.087101 | 2026-09-13 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 543f930f-731d-3bab-a3b6-e17a76c812b1 | -10.5359 | -51.3881 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c399a85b-bb81-361d-91e3-ca1e0ef00302 | -6.9592 | -59.7384 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80cbdfc6-bb98-3dc8-a7ec-7a4bcb3ae043 | -6.3866 | -55.251999 | 2026-09-13 01:05:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab63e4a4-3021-3c11-873e-67cafe5f063d | -13.562 | -49.480099 | 2026-09-13 01:05:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88257d07-1253-3fa5-a6d8-5fd6706cfb81 | -2.96 | -50.417198 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbc6904-735d-344f-85f4-ebbbc17cd94e | -11.3491 | -46.7911 | 2026-09-13 01:05:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce5e29f6-7b43-3266-b07a-ad764aa97964 | -6.3421 | -57.879299 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1dbae5-0953-33a6-9e12-0646addb8fae | -6.1703 | -57.709099 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26d6a6b0-589d-3b80-a3a3-c3bef9f330c8 | -6.7234 | -50.472401 | 2026-09-13 01:05:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85531d55-c80a-38e4-82b2-376b6fc0739c | -10.6337 | -46.094398 | 2026-09-13 01:05:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d478e3b-64fe-301b-b382-fa762234f727 | -13.3912 | -47.993301 | 2026-09-13 01:05:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa5b5373-d31a-389d-a23c-89605789355e | -6.8224 | -58.651501 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd49c8c-21d4-332f-abad-d8b61a109f92 | -6.6778 | -58.8797 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 139ae971-35ca-3a99-ae34-fa19c79e8b9d | -10.9137 | -47.807999 | 2026-09-13 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c337386c-602d-395d-ba46-672f6ab28cf8 | -11.3254 | -48.547401 | 2026-09-13 01:05:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b802c3f-4c2e-31a6-9c04-d5d755e7b8e3 | -9.6726 | -48.009102 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2de4a69a-562c-3f9d-b546-c42bdf9a4d34 | -8.121 | -54.809502 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08f2132d-dbfe-397f-867b-175fb182179a | -5.9775 | -57.767399 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 103191d5-0cbd-3e57-95a8-f986f671d4bd | -10.5132 | -57.456902 | 2026-09-13 01:05:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 811ed0fb-562e-3aa6-a01d-6df7d4f4ad8f | -3.1595 | -58.644199 | 2026-09-13 01:05:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| abf5ea56-f112-3780-a7f7-1b1d4c99136c | -8.5813 | -54.567402 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c774423-6fa5-326f-b016-63225596e038 | -3.5686 | -53.014 | 2026-09-13 01:05:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9030cd0-5599-305f-bef1-b84a7fb0810e | -10.6832 | -54.1525 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f6bec71-df4c-314b-af9e-1a1a962f711e | -6.7577 | -58.962502 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d62695f-44d3-378d-9594-34e4300c763d | -6.7333 | -55.641998 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36abb052-a4fd-3961-9e44-37103ee6aac0 | -6.0932 | -57.686501 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33537b48-99e9-3a15-9657-304388e3bd76 | -9.5805 | -55.1534 | 2026-09-13 01:05:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 272ebc2b-373b-3434-970e-4a596ad3215b | -7.8707 | -54.707001 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4712d1a1-87f5-35d7-8ff1-ca7760fd5f08 | -15.5508 | -53.801701 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a4502ee-3367-3a8e-8f0b-82a0cb1dfd3c | -6.0847 | -57.648899 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce8ffcd6-0250-36f5-ae15-8c7afcddd2c5 | -10.5692 | -51.353901 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 022ade1b-c957-35ce-b890-e2fbc4719d5e | -11.3225 | -48.535801 | 2026-09-13 01:05:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17f1a3f8-3d75-3ea1-aef9-f16966035749 | -8.0277 | -54.852402 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c99c2fe4-aa20-3cf7-a5b9-958c768b3e38 | -11.2459 | -54.1329 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af63df18-0f28-3983-8e42-6ab6f6b6ced4 | -2.9778 | -57.211201 | 2026-09-13 01:05:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db426b4c-ffe0-37b8-b4d2-81321e754f6c | -15.0318 | -48.5093 | 2026-09-13 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a661c9d4-6d2d-38dd-927f-1e707819e92d | -10.5515 | -51.323101 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad4e11be-a996-341d-8d3c-0aa9550859e4 | -1.2257 | -54.116501 | 2026-09-13 01:05:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c613ea8-874e-3571-b734-15b2992716e4 | -15.2638 | -42.795502 | 2026-09-13 01:05:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f21d3664-f045-3493-819c-9a0775ca452b | -15.5606 | -53.7994 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2234dd1-abe2-35fa-a251-32a185c34074 | -6.9614 | -59.748199 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4961d04-5eba-380f-b1de-987a1eb9deeb | -6.5861 | -58.836601 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 017e79bb-c986-3888-9ae0-92b4db4cd2c1 | -9.7153 | -48.097301 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a385247-f322-3d58-9176-8b36181187d2 | -9.6824 | -48.006599 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e504665-27e1-3e77-909d-f5596c63ffd0 | -9.4024 | -50.107101 | 2026-09-13 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32b1d3c0-9a4f-38cf-9310-e555a56e4761 | -11.5222 | -54.625198 | 2026-09-13 01:05:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de2ff9de-7fed-3b5c-9cc1-84422dfdbfb2 | -9.7056 | -48.099701 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b909488-06c5-3560-8716-0b2d33b57fa8 | -5.1267 | -55.9659 | 2026-09-13 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d97a9c69-f005-3324-a1b7-159eb1dfe348 | -5.9853 | -57.7103 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c097b547-9470-35c4-a672-6f9a58d90dad | -9.7181 | -54.3517 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
