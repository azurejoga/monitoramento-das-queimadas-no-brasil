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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7927a61-f033-3b85-9575-eca7f1600344 | -6.49791 | -44.45782 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ed143bc-c684-3103-b4ca-3952d13619a5 | -10.66067 | -44.85928 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77743050-48fb-3883-a828-c28e9811962a | -6.32819 | -43.95309 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2a36d6b-0540-3386-8abd-e2e08b9062ec | -5.20921 | -46.19033 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8107b5b8-3d80-3206-b5df-959166be4d41 | -8.4558 | -45.12608 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a19d8433-faec-3291-addd-21c7db442bbf | -5.85355 | -44.46503 | 2025-10-17 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8011d7a-ae21-35e6-9c58-c018f3c3bb25 | -8.10625 | -41.14349 | 2025-10-17 04:19:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1ad1ee4-2985-3c7a-a716-c4fff2ffe780 | -4.47937 | -42.93304 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a56fe44f-88bb-31db-b065-19271bf54bc8 | -5.89801 | -44.74747 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c76e3233-afc0-34a0-ba8a-75586a45a1b5 | -6.5556 | -45.90486 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f97b9f1c-481b-3dcd-966b-01b0847ad9db | -10.27178 | -44.02307 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6a525f19-ce45-3481-a225-62cef47f447d | -5.85479 | -43.86799 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 602d68ff-df62-3af1-824b-847e613696e8 | -10.14038 | -44.57117 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfac52d0-78f0-3fbf-b710-65b30da7d692 | -11.48363 | -44.19276 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d523ffed-f5c8-386d-aa60-45e35848abbc | -8.39707 | -46.22932 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 875110a7-5854-394c-8bec-2de51e7abae7 | -6.28958 | -44.02467 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8863d13c-6255-32a7-9085-906f402d924f | -10.26846 | -44.04494 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c1ab324-c466-37e8-a117-8ee93cfface0 | -6.52939 | -55.05307 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5834bd45-de0b-3c63-b93e-35e24f9439a8 | -8.7278 | -43.87092 | 2025-10-17 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e411c33-ae51-3836-b913-f1175e03fcaa | -6.36467 | -41.48565 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c4d34c13-d6b1-33ab-9ec8-b054bddae467 | -6.13441 | -41.76998 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fe2963d7-8f07-36fb-b02c-a0f541b50cde | -9.95491 | -49.02076 | 2025-10-17 04:19:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adf05b1b-3e39-3f0b-8564-f79275b21d05 | -4.93334 | -41.54493 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1606e718-4ed1-3b3d-9e81-48519d0c2d2a | -4.40856 | -48.94396 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fd7512a-bca2-38c7-859b-5d4eddec4407 | -6.90315 | -43.99621 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4e19abd-440d-3597-bf4a-aebbd567f55e | -5.51398 | -43.87149 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68d0c9fb-319f-38ee-a023-ef9e50b2f969 | -11.46085 | -44.04552 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c00aa1-2de4-3c66-8fdd-93076ad38fe5 | -5.91881 | -44.93784 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b92bf4b1-cc5b-30ad-ac06-9be7c82c7f28 | -8.18686 | -43.31742 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39a72900-7223-36fb-92d3-4a3329b4eb0f | -2.86775 | -50.7376 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e27f6f31-327b-3c87-8f5c-514cbb8c756c | -7.47187 | -42.17144 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5f8468f-80ee-3a0c-98a3-4153690dc3b1 | -7.27963 | -42.93939 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d8f31e9-3660-3de6-b3e4-ebed91d756cf | -7.74131 | -42.50294 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 904394d4-4db3-332c-b78a-54c01d55811f | -8.24665 | -43.4125 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b94461d4-bf5e-32e6-bba1-52cc0f31a04c | -11.27942 | -44.03695 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03af4278-aab4-3b0a-94f4-1230b6b92a93 | -4.4218 | -47.75516 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40d15899-acac-3190-9917-940f6e0e2474 | -9.45932 | -40.5867 | 2025-10-17 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ee895b7-5bd1-3bf0-a122-f3568c14bde2 | -5.5706 | -47.61419 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 231c00b3-ebd2-3875-be96-9d19f19ac299 | -6.30798 | -44.71727 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72fca2c9-fd4c-3d41-a0ea-e46a7f78f5aa | -10.50724 | -43.39293 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dade0f5c-64fb-3546-904f-55a0a11305d1 | -11.48699 | -44.17068 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d26f4713-c53e-340b-8356-1767cfd7cdc5 | -8.37673 | -46.31378 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fe5965c-f5bb-3d30-9a60-7d70e1961f85 | -6.21129 | -41.76337 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74ed6cdc-6447-3e17-839a-45211e5d7ccf | -7.47884 | -42.75827 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a1834f1-de56-3434-a519-b3611d706d1b | -7.94688 | -44.10964 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 584c9791-ba1c-3823-a1e5-63725a0da765 | -9.98389 | -47.01 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4cc3d258-70ff-36a5-b0b2-cd0086524d3a | -8.45536 | -41.26784 | 2025-10-17 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 32bea376-2982-3c2e-b58b-8851b60e4479 | -7.1827 | -42.191 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d6fbffd5-8299-312f-80e8-0496f42175c4 | -10.57464 | -47.41948 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3983b64c-76f9-36c5-8c1f-e7172d75c00e | -5.77575 | -45.73793 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8814f30-849f-3faa-a8f8-ec29bbbf99d4 | -11.50157 | -44.05185 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b68d0184-4112-3d87-842d-6fa79f535a05 | -5.27909 | -43.25928 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c4ac0b5-51ea-3a28-86bf-24ecdb3af873 | -2.97713 | -49.22173 | 2025-10-17 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a7cc128-a9b1-360e-83a2-c6f0ee79b29d | -8.93822 | -48.65401 | 2025-10-17 04:19:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 740f0e10-b109-353f-8893-da596496a101 | -2.9592 | -52.50299 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f9771ea-4efd-3926-ae23-837320fcebf1 | -11.4504 | -44.18382 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f508efe7-c3a7-326e-99e0-0c3e92b88e5b | -5.88775 | -43.89805 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f756f34-1895-31d6-a9a1-d2828d81185b | -5.50812 | -43.7784 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 982995e0-9b5e-3a86-a702-d312fa997452 | -5.48225 | -42.95148 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4dc427df-b9c2-3500-a0a0-910dc52f9887 | -8.27363 | -48.00412 | 2025-10-17 04:19:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 585c70e0-cabe-3abc-a9ac-1365ecb67c8f | -5.62544 | -42.67268 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3f2f390-c6f3-3b2b-b5a8-b0b3da536156 | -3.13393 | -50.21394 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d637b083-d7b7-3694-9b1f-c5ba443af6e4 | -10.84347 | -43.95258 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f1c299-e7bf-37d9-b7b6-c399beac43fa | -7.4795 | -42.16856 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 849545f9-bf5b-39d7-b5c8-afdda7e6eacf | -11.48191 | -44.15857 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a230b5d8-bea1-32cd-8085-792503f514d7 | -5.03525 | -49.21809 | 2025-10-17 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98b43168-6e48-3b3d-af16-cb09e75d6ca6 | -4.42233 | -40.17836 | 2025-10-17 04:19:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| be26b762-00a7-396a-a216-2fe4d2ccdbff | -5.47407 | -44.67275 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc916eac-c12d-3435-976b-3adedeccff9f | -4.81829 | -43.20275 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b71f344-5de0-3591-ab5d-dacb126e8e5d | -5.59939 | -42.70628 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 523cb513-b18f-33b9-a14e-09dc1d81efa8 | -5.01069 | -44.67708 | 2025-10-17 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e8e0db9-71f9-3251-b6a8-a390ab905fc2 | -11.48757 | -44.18961 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7635c58a-ab47-3708-a658-1456a0fbf4b2 | -2.98124 | -49.22236 | 2025-10-17 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98399415-9e54-3d2b-9024-3202350296a0 | -6.31171 | -45.53386 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af846867-d1aa-35a0-ad44-7df5a4af1346 | -6.3251 | -44.32127 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c88f6d3-6032-3669-b850-4b77ffc97a76 | -11.39476 | -44.20901 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 767d4443-c54f-39f0-9aa6-41989bbdf7de | -6.99545 | -39.22907 | 2025-10-17 04:19:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dfa832e6-5e6e-395b-8d2a-30873de44f1a | -11.4603 | -44.04923 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3e8e15d-c555-39cc-99fd-e9d97100ff24 | -5.84923 | -47.03668 | 2025-10-17 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e86b367c-fe3d-368a-8a27-4c4974d0b2a0 | -6.75774 | -42.36099 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9b5a9f8-7be3-3cc6-b3eb-ce17150cf327 | -10.56943 | -47.43002 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cf1ba19-7c15-39d0-9dd7-6d3c54ee229c | -7.74422 | -42.50731 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b22a5475-ea58-32b2-86b5-0c4f306855be | -6.29463 | -42.97916 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23be7495-cdde-3933-b927-5fd19e935d5a | -6.28787 | -42.97813 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92e930a2-a56d-352e-a305-926a87f43f2f | -8.22774 | -44.00877 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 133d4e4a-a300-3712-a17d-1b75c113b71f | -7.76279 | -42.47836 | 2025-10-17 04:19:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 36d27de4-ec6d-3f19-99c0-57de485c920f | -11.46964 | -44.26194 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e09619a-5699-3a57-9623-7e45a1b29b0b | -8.45549 | -46.24612 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fcc718c-3349-30a0-bbe1-53e2789d1552 | -11.48307 | -44.19644 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7d56b00-1a3c-3adb-9cb5-0ca4d69ed99b | -4.93063 | -41.53762 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39a9618d-f0e9-3382-b18c-de885889b698 | -4.95229 | -44.96145 | 2025-10-17 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2a09406-7e76-351e-9678-fb5a094dfe07 | -7.20795 | -45.37748 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99c67359-3e41-30db-9e44-0a91f9c3be5a | -6.9984 | -46.99581 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5114ba7d-07c2-3e53-bb98-3ff71491a630 | -5.56021 | -44.60233 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7ecc80d-1676-3705-9a9e-b5ad9a0a587f | -6.70571 | -44.39181 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 611824f6-f7f2-3876-b17a-2d4c468984d2 | -6.63269 | -44.44397 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98aff63e-77b7-3d03-9a85-b9a637fcab3d | -9.71093 | -44.4896 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04dc84e9-fba3-3220-b270-7ef8521be938 | -8.18429 | -43.9585 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2c4be90-1c15-3011-b069-47f18e709100 | -3.4983 | -51.60051 | 2025-10-17 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eff892c-f3d1-324a-8a3d-9d6dda7a9fb0 | -8.23303 | -44.82805 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README61.md)
