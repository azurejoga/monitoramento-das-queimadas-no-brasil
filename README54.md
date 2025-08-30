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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce9f09a7-cabf-3ddc-966f-419c688a0fbe | -11.89344 | -46.72105 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f6c779b-4d34-3173-880c-7168c86d3a49 | -11.29331 | -43.57972 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59991ed3-feb1-3c26-91be-2ccb86a3dfd7 | -11.84206 | -46.44252 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 525f815a-bc84-3585-9a90-7fa35393084c | -11.8802 | -46.44725 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0101c8e9-3ce1-35b8-9ba9-5d0f1143abae | -9.46011 | -60.56687 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fe1c7eb-fb7d-3146-aa3d-4e00cc41b9b2 | -7.08462 | -44.29519 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de9f1aea-d53e-36b2-8936-11e42611b61c | -10.02652 | -48.09634 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af866d84-4c84-335d-8b1a-d2470e9cb12b | -9.2806 | -60.4598 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb7ba382-d816-391f-a8b8-666828af85ba | -9.44242 | -60.54638 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 147f2322-c0bd-305c-aff5-52c5fa1fd8d7 | -12.56085 | -44.80181 | 2025-08-30 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2fa5290-7711-3c81-977e-a6ff75009b72 | -11.31963 | -43.61659 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 757b23ea-5056-3308-85c5-89e4ccf649ca | -11.31217 | -43.63417 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9e72683-5e8e-36e1-a457-63df0884416f | -11.86787 | -46.37909 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9834591b-0b24-3484-bc59-a4d3db2e60ad | -11.0683 | -52.04296 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeae8a22-44a7-3580-831a-ba839bf4bb1f | -7.10381 | -44.58714 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 25cc1232-c105-31b3-8c3a-bf480e1c0511 | -8.87888 | -60.73587 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9e70d40-88ea-37e4-87e3-9e32e285256f | -8.28113 | -47.19733 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab8aaa23-b867-3a34-8d4d-6edd3f03be63 | -9.70278 | -47.055 | 2025-08-30 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16f7e7eb-af7d-33fb-9275-faf9f871fd11 | -9.24145 | -59.77898 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc8130c7-901d-3487-8277-26a03c9c9c69 | -8.56548 | -51.31164 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60b8c80f-3cc7-3b2f-b94a-f860a9cfc176 | -10.70049 | -47.0616 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 498fb9ca-ed04-32d9-a9bc-e057e716cebd | -9.17547 | -59.5715 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc813340-a060-3e17-b38e-0e5783762cb0 | -9.44043 | -62.35487 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9c076f9-ca35-3a33-beda-e3ca42dc2668 | -11.48714 | -48.29197 | 2025-08-30 04:49:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1b8d22f-d392-3baa-b100-5066f9559a8f | -7.73771 | -50.26888 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 07099b79-806f-3525-af8a-74ad5164d8f5 | -11.30516 | -43.60847 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2684b6b-6535-3b25-927a-a16a08690345 | -8.28632 | -61.40491 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d2dbe66-55ec-3e67-96f0-b991d0b4a36f | -8.55383 | -63.02558 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75a2cd46-4cbf-3dbb-a36f-2905f569839e | -10.88323 | -55.76914 | 2025-08-30 04:49:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 620beafc-4c3d-3145-99e1-3ac3ea9f48d1 | -7.72497 | -50.30682 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61953f79-485c-3cd4-af62-a3e8525f354c | -8.85241 | -64.15136 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d45fdd2-4387-3673-b199-0587b737c74b | -11.8305 | -46.46903 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 918a69fb-d246-39cc-8cdb-8c360d9de7f6 | -9.17524 | -59.58046 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2e11eff-791e-3184-bc1e-df08aff141dd | -9.45188 | -62.34571 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 85018255-881b-3070-ab9f-069023717fa6 | -11.84679 | -46.43937 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2ace342-00dd-3e86-922a-6b5b33cfcaaf | -8.51712 | -54.71838 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e322bdbf-d062-304c-92de-8f0877a8e2a7 | -9.4432 | -60.5692 | 2025-08-30 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 65a2a505-282b-3eba-a0a1-76098df46ad3 | -9.1155 | -65.7699 | 2025-08-30 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0643ac24-0b4d-3ced-a321-2069191ff1c4 | -9.4433 | -60.5499 | 2025-08-30 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 00044273-7f33-3367-ae24-609b0f756378 | -9.4435 | -60.5307 | 2025-08-30 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| efcb4776-8718-3b13-866b-03e80febf7e0 | -5.8884 | -42.9753 | 2025-08-30 04:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 1aab2f6d-e813-3447-9ec9-6b45f3873dc3 | -9.462 | -60.549 | 2025-08-30 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 15a91606-3483-37e3-b3f0-e2b5157bd802 | -5.8886 | -42.9518 | 2025-08-30 04:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| db2fdac3-78dc-3236-a481-7079ef8ce705 | -6.1665 | -43.3273 | 2025-08-30 04:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| cffbdec2-3e30-3f4b-b58e-de1d37aef973 | -9.1156 | -65.7513 | 2025-08-30 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b7944770-2b58-3dd2-a1aa-6a4ea68906ec | -6.1853 | -43.3257 | 2025-08-30 04:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 63a8512d-2142-3954-8b42-070a1f61f091 | -5.8699 | -42.9533 | 2025-08-30 04:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 6c18b86f-14db-3e2c-8a87-50c25741e12e | -6.185 | -43.3491 | 2025-08-30 04:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 3d84d97c-0745-3bef-8935-0bd882996eb7 | -13.98233 | -46.32052 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43368012-7c7f-3519-a886-e0cbb7282f7b | -12.92495 | -46.3545 | 2025-08-30 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08e6fed8-e271-3ee4-a2e6-30e03ed1bd30 | -13.36737 | -47.00037 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 761664f7-a279-3c68-ad71-6d0dcdd82f1e | -13.39476 | -46.95412 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7582c573-269b-3e67-8d03-395b87ca383a | -13.36995 | -47.00176 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e1cba99-6cfb-3e43-a472-45ab5557358f | -14.99784 | -46.70063 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d432596-fa55-3121-8c06-a8e333f1594b | -14.00311 | -44.56776 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 691eb13d-c158-332a-b1a1-703d0cee39a6 | -14.6228 | -48.07453 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d32da946-6924-37a2-a12c-3b59ae7ee8e4 | -17.45316 | -44.48648 | 2025-08-30 04:51:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01f52f63-444e-35fe-a93a-620add48b77a | -14.00879 | -44.56275 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afd2de20-84e7-3ce1-9f21-407f2b7a3857 | -12.8954 | -48.88132 | 2025-08-30 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bae93f45-bf8b-306c-b5d2-f6bdb65f8e39 | -20.08592 | -48.27242 | 2025-08-30 04:51:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12f7af1f-a604-3d02-976e-02e7deed2e09 | -13.62685 | -48.25359 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2afbca8f-6110-39e9-b534-4ad05d27b69e | -13.62971 | -48.18542 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9918630-561e-3e97-a760-3666ac42c581 | -12.92272 | -48.11107 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1a0a3c1-c047-3548-af75-caf97714f92d | -13.50007 | -46.83646 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cfc148c-4685-35dc-9f3d-861f180817d7 | -13.36476 | -47.00858 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cad1a29-8181-3b1b-a630-88881d7f3155 | -12.4314 | -63.91936 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b94e89b-48f5-371f-b7c2-4192fc5982ab | -13.53587 | -46.95342 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ff312b8-a805-3a46-8885-ed6ab933d3e0 | -13.38074 | -46.96354 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4764ea68-2716-37c5-bb44-71676ec0303e | -12.71224 | -48.18972 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3cf3ee2-31c1-3b11-9ff8-67314019b924 | -12.63077 | -57.01223 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0d355ea-ebb9-382f-a4fc-8d0444082b12 | -12.83681 | -48.12693 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8974ff42-71bb-34c9-9f04-016776371cf8 | -14.47825 | -48.38126 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bae07c25-b0b3-36e1-983c-cc3fe69aadec | -9.76043 | -65.08506 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5506053-b1ea-36fd-be74-be731b05dfbe | -17.4479 | -44.48619 | 2025-08-30 04:51:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a702dc4f-c86d-3fdd-a891-b22f70a4a591 | -12.93223 | -48.12753 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e2d4298-0994-34ca-b8fc-c802393c08d4 | -13.36786 | -46.99669 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0874de9-d87d-3ff4-9bab-aee3f7d3c664 | -14.50472 | -52.05381 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1ead6b8-7d64-3a59-8f36-342e5bbaaa94 | -13.43804 | -46.94903 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec820395-8f16-3d9e-bd2c-4a9c59e2944f | -14.79155 | -59.73511 | 2025-08-30 04:51:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be05f631-9417-3ab9-9b4f-54229a14f7b4 | -14.32445 | -51.95433 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8258b62-75b8-3a23-b7b7-b7e3476cd597 | -13.36538 | -47.01544 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb837185-9660-30ae-be0d-182bd9d938dd | -13.38883 | -47.0303 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fef78da7-98c3-300b-bee7-c35504523b53 | -14.27811 | -51.89869 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ef17a406-3f9b-3c8f-8939-6f75d9fbfd28 | -16.53296 | -55.04502 | 2025-08-30 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 49742271-1b05-3af1-9a96-d6a1ef148ba5 | -13.45568 | -46.94471 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73feb7af-00ce-3ae7-9d1c-b6d70c27ed71 | -14.02096 | -44.54903 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1f9b1de9-8683-310a-8f31-f4cf760ea3f4 | -18.91686 | -56.25547 | 2025-08-30 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4e03182f-e62e-3104-b34d-f953904c5edb | -12.93292 | -48.12261 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f9edea9-0192-3b6e-bb9a-4e13dbfb73fa | -15.67143 | -52.76698 | 2025-08-30 04:51:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23f81255-d24a-357e-844b-22d061748fc7 | -14.0283 | -44.48949 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 399a8d06-e36b-3fc6-8029-bbdec12ad431 | -13.39349 | -47.02715 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fb94cd3-2f0d-3d3a-a3f0-fe836e4f980d | -15.17778 | -48.02948 | 2025-08-30 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0eb9e592-96b8-3cba-a326-c9419f1a325f | -13.39337 | -46.99636 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d03c90e8-b05a-312f-bb13-7fcc08a3a3a0 | -14.35482 | -53.09613 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0b8b0c0-2aa4-333d-9432-759885681cb5 | -15.63886 | -46.43079 | 2025-08-30 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dddfad0a-1853-3305-a02f-f586b5d80e97 | -12.43752 | -63.92072 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ba0712e-5cde-3a62-9ae1-1416fa8826cd | -13.38487 | -46.96444 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db8b1af9-e5dc-3bdf-b9fe-e388c6a4596c | -14.25097 | -45.24488 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6135fe5-7af4-37c5-ada4-6f16936892f0 | -14.53253 | -53.0047 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab6983c-f378-3d36-8b67-5af8443566c4 | -14.04149 | -44.5048 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README55.md)
