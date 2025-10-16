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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d35917ff-d715-382e-a7d9-8055c2037f21 | -11.47887 | -44.08028 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c64bf7d-c0db-37c0-b58f-67abebf1143c | -12.66937 | -44.12656 | 2025-10-16 04:40:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60281f72-e6c6-3e55-b959-a8fe9f1e7e96 | -11.36505 | -49.37425 | 2025-10-16 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 796ee872-e64e-3cdd-8785-74ee7c4a1415 | -10.47214 | -55.58889 | 2025-10-16 04:40:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbc19d4b-0a9a-3a73-8ab8-7e6e5427c569 | -13.19769 | -49.97016 | 2025-10-16 04:40:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c46c28e-d056-3076-aef3-913895615529 | -10.12706 | -44.58122 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6176c7bc-1103-3575-9143-1800312618ed | -9.68846 | -44.5057 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 397a30af-79c0-3e39-b042-ea123d0d6551 | -13.73331 | -44.23547 | 2025-10-16 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5735829e-a692-31ae-b8f9-e7c132d8991b | -9.69736 | -44.50318 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 014883e0-e813-35e7-8cdd-d50c486af4a3 | -15.78924 | -43.65238 | 2025-10-16 04:40:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11a70c90-9303-37d4-8b03-dbf5f2ba5ff2 | -11.20001 | -46.42266 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f29e245-a95e-35e6-976a-e6ee8cabfac4 | -8.4061 | -46.23452 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 781c3fb0-1ab5-311c-a64d-eda1235a9fb1 | -14.17137 | -44.36657 | 2025-10-16 04:40:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a91ffc0-a950-34da-940f-3f2ab0eacf48 | -10.51388 | -43.36421 | 2025-10-16 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4666143-709c-31ec-a116-1a1e6f9ed704 | -12.24329 | -49.38874 | 2025-10-16 04:40:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e7739e6-6c52-37a9-b031-a7370643da77 | -11.48323 | -44.07904 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90c75791-8511-3690-8a91-da989b28594b | -8.82143 | -44.9017 | 2025-10-16 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f87c5806-810a-3593-b0c6-e837bdd48326 | -8.39129 | -46.25857 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa72dc09-f797-33db-8e70-e56539fab158 | -9.15971 | -46.86553 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| aeb8d365-4ce8-321c-95df-35a274436022 | -10.83752 | -44.00761 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46bb9030-e550-3ba2-8d30-29ad914f4921 | -11.62724 | -48.52413 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e985e3-0782-351f-a2f4-8c06b22b7e6b | -14.12368 | -42.62489 | 2025-10-16 04:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ab54a62-863a-3012-a442-5e562607dfed | -11.54982 | -49.92028 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0647bd5f-c3d2-3309-a87a-1016ef6a4a59 | -10.03465 | -43.83624 | 2025-10-16 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc69ece7-9dad-347d-b162-f9911039617f | -10.14616 | -44.54412 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73deb86d-626e-3ddf-b885-1dbd31246efa | -11.87871 | -49.9038 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f222f161-3d9d-3db7-89e8-cf5f87eda77d | -8.46829 | -46.24757 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49079275-fe00-3bd2-a4ad-bbee8163b8c6 | -8.41609 | -44.73792 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 617ab71c-50a5-3754-8c9b-e068cbe80e92 | -10.72569 | -47.58669 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11f4ff7c-fcff-3d45-b944-17acd46636a9 | -11.50764 | -44.06458 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b77ad5c-c90b-3c1f-8356-c7a83f29f229 | -10.99249 | -49.54237 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16caf234-5cce-3afd-8c36-ae09e3b0488a | -9.10272 | -46.66364 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63f9e6ad-1d80-35fd-a6a6-815819b01eab | -10.12794 | -52.34287 | 2025-10-16 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f73cdd5b-295e-3253-a018-88fc56a7e71d | -8.47143 | -44.1934 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| eff90462-264a-31e7-a84e-14c808f41d30 | -11.57848 | -44.07459 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 837c6653-5883-3a6b-86e3-195ee06021bf | -10.81991 | -43.93912 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da8e7216-a358-323a-b620-f24846d96cfb | -8.27328 | -48.00451 | 2025-10-16 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faaa3ffd-e9be-314d-9eba-0dc7aa011cfa | -11.2007 | -46.41774 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 42f8a362-71c8-36c3-b1ee-23175bfd7611 | -10.12561 | -44.56138 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb708db1-0640-3dc6-9233-07887880730b | -11.43089 | -44.13594 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f90a0149-de33-3ba1-a44e-5d139897c939 | -9.15734 | -41.06329 | 2025-10-16 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 9182d7e1-e387-33b7-b2f6-6697f78db92c | -11.54597 | -49.92329 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8013dc78-7ff2-3863-b249-2fb0d0a5c63c | -8.47194 | -44.18972 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 676e18cc-b5e6-3953-91d4-10ea7faee78e | -8.39805 | -46.26391 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10081697-ef4e-35d0-be33-724d1983aec1 | -10.13126 | -44.58174 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a7c59bfd-62e0-383d-b0a9-55c66b7d4022 | -14.07954 | -44.27949 | 2025-10-16 04:40:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d514258a-153b-33eb-a4f9-d7e6492fa225 | -10.83258 | -43.94524 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b389136-5352-3feb-987b-4da8939f57f6 | -11.49306 | -44.10736 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d2d8632-f582-305a-bd21-b7dd60f2c994 | -9.69101 | -44.51783 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a46c226b-3080-3bab-a2f1-f6d5cd007219 | -8.39436 | -46.26336 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8d0ea62f-fb08-3631-9426-26d0403883cc | -12.67775 | -43.43174 | 2025-10-16 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 658e512a-881f-3e7e-a810-4c724fe9d0b4 | -9.71304 | -44.52351 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d9b0b16-158e-3b5f-b8ea-67e384af37b8 | -13.69936 | -43.70933 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c43fdc1a-ead1-3ffa-85f4-0b8354df1c06 | -8.19729 | -47.01611 | 2025-10-16 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aed06dc2-f068-3540-a359-31cb96a1ec17 | -12.7197 | -48.64672 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c8134d49-e5dc-314a-b0d0-6ea41cc5e208 | -9.06638 | -48.84567 | 2025-10-16 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ea07ec2-daaf-3b1b-9066-ef84cd1e1aa4 | -12.72368 | -48.64361 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9fc70507-df2c-375c-ad4f-272d0daf931a | -11.19622 | -46.42219 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4947668-053d-3761-9e57-d78ea01d1226 | -10.64777 | -45.24778 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 53bd3174-c016-33b2-8370-2c4f32b18152 | -11.49363 | -44.10297 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efc5bc36-91f5-304a-a998-06c2a6f97a91 | -10.13294 | -44.56998 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e74e37c7-8a5b-3bc1-880e-8f47d3d8e5d8 | -11.44995 | -44.16081 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16666604-1ec4-3070-ac3e-2c357e8ef153 | -11.72468 | -62.29639 | 2025-10-16 04:40:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c700876d-2e4e-3c18-885d-3bdfa20fa505 | -12.67241 | -43.43615 | 2025-10-16 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 26d4c9ec-e431-34a9-b33f-7ee5b8cff14b | -10.8105 | -43.94207 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b70b7a8b-ecaf-31f4-81ff-57abeb8c1788 | -10.13416 | -44.5695 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87f11e27-53bc-3c6d-a9c2-ef363f0e4277 | -10.80885 | -47.92847 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59aac3fe-2f07-378b-a588-dc5c9bebeafc | -10.88843 | -47.90729 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e0469b1-0cd3-3e2d-8d86-276e6107b0cf | -11.13188 | -45.84802 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bb037e2-375f-3b9d-935b-9df870b8ae3c | -11.5835 | -44.0708 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa49c7b0-a842-3d61-b9ba-17400db68beb | -10.82816 | -43.94466 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3135d6f7-7763-3717-8172-594acb5c7f22 | -9.14037 | -48.4433 | 2025-10-16 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 591ab1e4-416b-305f-b5d3-1f621ff504cb | -11.47382 | -47.64117 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a0dc50f-7c50-3afe-9e48-3c59d2939de7 | -10.83811 | -44.00331 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b115be96-3e4e-3969-9b36-6cee795bffd4 | -9.68574 | -44.52486 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9dfb4958-00a8-3186-82ae-fd7fa3eb5c38 | -12.67305 | -43.43108 | 2025-10-16 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 98a24def-88a3-3158-92b3-9a8cad1770bc | -10.61665 | -42.31176 | 2025-10-16 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a8664285-0dea-3d09-a26a-a2230f48f1b9 | -13.65675 | -43.92526 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15ba2dd1-9702-3fa3-93c8-84bf9d46f70a | -8.20203 | -47.00857 | 2025-10-16 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c95c54a8-a765-32e5-9303-25d86cddb14d | -13.60674 | -43.57217 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f01583-a7f2-3f5d-9cc3-9f0ea14d47a5 | -15.60561 | -42.66312 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7320d870-28c0-3f50-badf-29b29cf4421b | -12.83485 | -43.81408 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8714b9f-670f-3fbf-908c-339e5f1612e5 | -9.76637 | -48.75469 | 2025-10-16 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5616918b-de9c-3a15-aaf6-75af33950068 | -9.22512 | -48.6019 | 2025-10-16 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a2b4bde-1690-3dcf-a6ef-036a8c948287 | -7.40505 | -50.63591 | 2025-10-16 04:40:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3532f95-ea0e-3e22-9e0a-6d0bafde11a1 | -9.96436 | -47.00959 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b836f060-8a4a-331e-a31a-d96706bedea0 | -11.45532 | -44.05447 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee92d7db-43fa-3827-9017-76f94266c8dc | -11.43148 | -44.13158 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b2e77bf1-419f-3a01-97a0-4d08b3c05a38 | -10.52627 | -43.37642 | 2025-10-16 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c3466f0-f088-3451-b0c5-362c3f6296f3 | -9.68429 | -44.50503 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8dec9c5-e400-327f-a64b-dddda21cfc09 | -10.65283 | -45.24116 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b8ca3cef-52ce-321a-b614-58f2bc53d90c | -8.41406 | -46.25737 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33a7acf9-afdb-33e0-84c6-db61a5206d02 | -11.84892 | -47.92135 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86356169-c607-3a09-adb4-1132e594f442 | -8.29177 | -44.96538 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d5fa9f5-a3f0-3108-86ba-3c9892a02054 | -10.65181 | -45.24835 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6816dde3-d853-37b3-bf7e-0b9009139cc8 | -14.075 | -44.27893 | 2025-10-16 04:40:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 469aaf66-b6c5-3ed4-ac47-a26d4c322f0e | -8.55208 | -44.59921 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7abbde36-d4ca-34d2-ada0-35476205733d | -8.28374 | -45.40406 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da0bf008-b8aa-3674-83d4-5a717b76becc | -10.81231 | -47.92919 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331b00da-282d-3b9e-8830-3b57bb16a09b | -12.44353 | -57.81394 | 2025-10-16 04:40:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README63.md)
