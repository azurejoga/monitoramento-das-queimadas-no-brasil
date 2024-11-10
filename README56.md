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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30122745-a73b-3d3a-aed3-bc8a53be32e5 | -2.67143 | -46.79445 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 692428f4-6db8-370e-8562-723ba39fa13d | -2.03559 | -50.89449 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42629f0b-d4b8-380e-b3a9-7a199e1d6e24 | -1.48173 | -54.30413 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdbb878d-1385-3e13-afbc-6cb836f41297 | -1.34103 | -54.62373 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f1751c0b-f1b5-33e0-99d4-865db7b82d5a | -1.65064 | -47.91605 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6584034-fe81-3374-b098-f22d964fa827 | -2.50974 | -47.46876 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 836a37f2-ff81-3f6d-aeb7-1ab433243ddf | -2.11749 | -46.47764 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba8dbb77-b829-3945-9880-74d1c7e835af | -2.4057 | -46.77671 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67854a99-3e17-323d-8483-0f228736da0b | -0.14555 | -51.56342 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27a1cf73-93e7-3ca9-9d27-63d5ccba144f | -1.2183 | -51.76247 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad3c550e-0aaf-3bea-a6b5-6ec41331cce6 | -2.56462 | -47.34766 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72582afc-7222-3e4d-b8c7-9471c29bd1d9 | -2.23392 | -48.70258 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 958a8971-454d-3c92-af8b-aa368606e325 | -1.65639 | -53.26999 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bcf4e4b-f06a-3b0c-9212-b93c10a31637 | -2.22642 | -48.45065 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffd432d7-48b3-3eb6-bc0d-4392c67b0502 | -2.53417 | -47.35712 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e419c690-b55e-34a3-8dc5-0b1c8458c167 | -2.20288 | -47.73975 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f67b3dff-652a-36fa-af23-793392ff8572 | -2.34453 | -48.51849 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3495668-02ce-315e-89c2-67a462adbbfa | -2.24489 | -45.52663 | 2024-11-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7bd73d70-df8e-3106-af8c-6ea9761dc1c3 | -2.64076 | -46.78971 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e191d94-0c18-3758-8266-cfed7169319b | -2.30185 | -46.18292 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f7d6483-b936-3ce1-9020-1691de7b112c | -2.35121 | -46.63357 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6cedbca-7db7-34ac-9f6a-0b270fb744e7 | -2.13492 | -48.75074 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49c45ced-13c7-3d4d-9d42-94042c09cf0f | -2.09332 | -48.82584 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7f873719-2582-3bee-bcbf-505f5849f440 | -2.09161 | -50.38644 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60507f56-e6bf-365a-86af-1a7d4c7104a6 | -3.52131 | -40.90456 | 2024-11-10 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1c8f5ae-d589-3640-b86a-ac1d45bcad04 | -1.6211 | -52.23678 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5236eb76-6438-3e4c-bf50-233f1427199f | -2.16588 | -48.32141 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd2d845e-f5db-37fe-b2ce-2515880ed25d | -2.27599 | -48.7162 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 651852ba-3cc3-3d2f-8090-c3a3659f81f2 | -2.16286 | -48.85425 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cada1477-1e6a-3a21-a768-632ae62e68e4 | -2.39377 | -46.78609 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f79dcf12-103d-33f3-98fe-db2b44aa58db | -2.52753 | -46.30551 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f35813-a773-35a3-bef3-6effc5d5ce18 | -2.19564 | -46.69217 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77bf4dcf-183d-3517-a5ef-c113ad61a530 | -2.90234 | -45.56268 | 2024-11-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94535bc3-fa6c-32ae-b7a8-b1b8981842e5 | -2.79879 | -45.97229 | 2024-11-10 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbc6d49b-73da-384b-a990-f5e1a232ec5d | -2.18365 | -48.37698 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00ccef7f-8257-3786-8600-3ec736b400ae | -1.52975 | -52.20607 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| db4f9d0a-f34a-39b5-be98-44a8a35c3e15 | -2.28648 | -46.51068 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08c9872e-f933-36b2-a890-d66cdc67493e | -0.18624 | -50.22566 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86aa3169-f911-3d38-b05f-8e402a0bf3c0 | -1.51071 | -51.54522 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 807cb0cc-401c-3ffd-b078-a8f5211dfaa4 | -2.40861 | -48.38776 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e53c221-14db-3e37-91f9-2f68df972319 | -2.64645 | -46.79804 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e772945-1fda-3acd-8e47-3959d552f5f6 | -2.12144 | -50.15568 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb3c1fc0-251c-37aa-9f7a-76cd551b9f69 | -1.78018 | -46.1523 | 2024-11-10 04:36:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d44d28a9-2d01-3896-afb7-71e32a30a905 | -1.66971 | -47.81642 | 2024-11-10 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5a308d0-6047-3ff8-bad9-776681b337bc | -2.27931 | -48.71672 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21e15ae3-fc38-3dc3-a27f-fe47e6c49c6a | -2.62424 | -46.16471 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df8ce7ac-5453-3d91-ba1b-1ab800a75e94 | -1.24659 | -51.7759 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae0b745c-66b6-3a5a-97a1-ebe89361d7a0 | -2.39516 | -47.7195 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dcde9a6-f91b-3358-b02b-1c85eace6f48 | -1.67029 | -50.49219 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c427ce68-6e47-3469-bbfa-3adbae3d6f3b | -2.29489 | -48.55313 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c665967b-9678-3e0b-8427-edaf5f891959 | -2.74989 | -46.00933 | 2024-11-10 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92d42afa-98c8-3942-b7aa-61e29dcb1b97 | -2.45625 | -47.1637 | 2024-11-10 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d38f9a0f-41d5-3a80-9057-47daf0326bab | -0.40567 | -51.4796 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a96f942b-8909-3311-9da5-eb6a7bbd6ac5 | -1.40826 | -54.5628 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44bfbf90-74eb-3561-8564-0cc2cb5bb300 | -2.68166 | -46.79601 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 136b5218-c68a-3919-83af-b4998e579926 | -2.15194 | -48.28043 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a80dbf4-15e6-3527-b5df-366d3784a3f8 | -2.09258 | -46.34423 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84bcd2fb-b332-3a44-a889-b039964f28c7 | -2.53674 | -46.31467 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acb39f91-2738-3979-a3bc-47ad1469bc12 | -2.11471 | -47.89284 | 2024-11-10 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d5a82b9-adad-32f1-b141-6d89612c5263 | -0.40498 | -51.48393 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baee3bbc-3c03-3b09-9d60-96dd57528480 | -2.32114 | -46.7376 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad1a6844-7ea2-332e-9610-34952cc8a881 | -0.45343 | -52.03107 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 620ec97e-cf02-37a2-a473-7cff8f718b94 | -1.53047 | -52.20147 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 53673a03-b993-3db2-b74b-02d4afb947f9 | -2.26832 | -48.74329 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85fe171e-f73e-3d2f-b796-80cd931387a7 | -2.39867 | -46.50856 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae748a9f-6441-396e-8180-905a581cb110 | -2.04371 | -46.07857 | 2024-11-10 04:36:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e50a4b3-27b7-34b3-8d38-6648f1732c74 | -2.34066 | -46.5682 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5069cf8c-951d-34e0-b823-89612e1d9195 | -2.07078 | -50.90004 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c79b421b-28db-3a53-8207-09a78871985d | -2.2941 | -49.1133 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5312874-95d5-3a40-a77b-c1b311019226 | -2.3629 | -48.85048 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa674030-d309-3117-b342-38bca08639e9 | 1.08405 | -51.30343 | 2024-11-10 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc24fc27-27e8-3c0c-8852-adedd45a250e | -0.9801 | -51.77874 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a434fa0-f4d2-3138-bdce-833ce8ba452f | -2.18575 | -48.34202 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11b4111a-e5a2-347a-af53-5dbca15e20fd | -2.19761 | -49.12641 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bd240e0-e6df-3b06-9034-e9d20ab1e893 | -1.43887 | -48.14392 | 2024-11-10 04:36:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fddf208c-d23e-31b0-94e3-e45ccc6c3385 | -1.94 | -51.40189 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae435f38-25f9-3533-9fdb-f1b55e4b5dd0 | -2.19082 | -48.37457 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29285b6c-b867-39c1-b8af-7534dbf3a0cf | -1.83063 | -47.93316 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0025a94-6f61-3c66-a444-d80886de4cda | -1.3468 | -51.42673 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8145ebfa-a4f3-33fe-aaff-0f2a24402a8d | -1.11877 | -48.3482 | 2024-11-10 04:36:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55845726-8751-3b25-ba60-9665b6042201 | -2.19483 | -49.12241 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90d74e7c-17a9-305f-9315-1f03b80bb1ad | -2.40456 | -46.78398 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 799e3c10-a17d-339c-86b4-4195dee79c79 | -1.62868 | -52.23798 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 119bc036-3b6e-361e-a4b0-b441f06fff06 | -1.74443 | -50.4839 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e12afef8-b81c-3eea-865c-3aa2c8fb7f94 | -2.36994 | -46.80476 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ae49968-85ac-3059-92bd-dad6e09cea2f | -2.11822 | -50.35236 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb46f49-7882-388f-82ab-7a8da6db628d | -2.17911 | -48.34099 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b246cad6-7d4b-31b4-b3e1-56d9710fc35e | -2.08058 | -48.25875 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 388aedf9-c06a-3008-8d3c-a15585b35479 | -2.20149 | -49.12345 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fce00fb-8235-349e-bb13-9713ba4be8d8 | 1.62178 | -56.04965 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbfe4000-1e5b-3bbd-aff8-434c017f8708 | -2.17529 | -48.3264 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd9328ff-f612-394c-84d9-8abab88180a7 | -1.48315 | -51.74308 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 281526f9-994a-3d8e-b0be-3926969c45dc | -2.4269 | -46.68651 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d724b443-f115-33ef-b552-b379a210ad75 | -2.35007 | -46.64091 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b76431e6-e233-3c10-aedc-a52039e00a8b | -2.39266 | -46.77099 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26978380-7fba-31ad-a9c6-2ce9282f7547 | -2.27763 | -46.85748 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c80b677f-cbb3-3575-bdac-ca8bf89d04af | -2.46171 | -46.33088 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99377ea7-7d48-3aef-9a09-e9cc2bdd7b91 | -2.66404 | -46.77458 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f538ce8e-d2fd-3bd8-bd27-25a2c619a6c0 | -2.24932 | -46.50113 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce30435a-b302-3c12-a55f-249c22beb894 | -1.87396 | -48.45521 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |


[Clique aqui para ver as próximas entradas](README57.md)
