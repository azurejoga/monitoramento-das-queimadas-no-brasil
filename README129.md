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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6fd9b41-7fdf-3641-b311-51e5898c004b | -12.9265 | -41.8118 | 2025-10-17 14:40:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 276.1 |
| 7a38e2af-1023-3555-a864-5164c2ccd172 | -6.3544 | -41.4846 | 2025-10-17 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| edb68fd7-b1b7-33f0-b36b-2f1eed718cad | -10.2558 | -44.0273 | 2025-10-17 14:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 164.6 |
| a615d6bf-9733-303e-8b3f-4e99e2ab89b4 | -8.2558 | -43.3596 | 2025-10-17 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| af63d5ba-ea79-3211-9c4d-1319fe466b8e | -8.2744 | -43.381 | 2025-10-17 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| f94d5299-7694-3f0b-b138-de4caab7ea6e | -8.2551 | -43.4066 | 2025-10-17 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 9c153425-33ae-35e4-94d3-66e2e6a8d879 | -18.3739 | -55.4587 | 2025-10-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 168c8d96-9277-3bf4-8f8f-901a1b317004 | -12.1547 | -50.3735 | 2025-10-17 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| bb3d23c3-b985-3779-92d7-037e24474819 | -6.5898 | -44.15 | 2025-10-17 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 224.5 |
| 17f2bec9-67e8-3ca2-a0dd-b1769cde7b56 | -10.938 | -45.4146 | 2025-10-17 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 61e8815d-3cef-3275-83da-ffa62799deab | -10.8987 | -47.9134 | 2025-10-17 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d9924329-942a-3fc0-97e9-ff791231aedd | -6.201 | -41.7629 | 2025-10-17 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| d79b0b8f-f740-3aac-acde-517dcc94d623 | -6.4255 | -41.8865 | 2025-10-17 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 4a484395-0bde-3d21-9dc4-45cd9e5dd362 | -9.6807 | -45.6417 | 2025-10-17 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 006e5815-9e71-3cf3-afad-a2f557694c11 | -7.9817 | -44.1342 | 2025-10-17 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 96bde1ba-1050-367e-b7fd-dbee4fa71fb5 | -10.9938 | -47.9019 | 2025-10-17 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7044b6cf-f844-3c2e-9267-2ec32e2f28f5 | -12.1682 | -45.0539 | 2025-10-17 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 8d5ef30e-4fd6-3d5d-b8df-abf1eacbfc22 | -10.514 | -43.3815 | 2025-10-17 14:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8ade1c57-97d5-3cc4-bc93-0f7ed02f9625 | -8.5608 | -44.5803 | 2025-10-17 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| cfa77dbb-89fd-3033-811d-03b90c15f38c | -10.2748 | -44.0247 | 2025-10-17 14:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 93f106b3-79b0-341d-a762-a18dc0e73734 | -10.9942 | -47.8797 | 2025-10-17 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0179c343-7bdb-3527-b22a-2d8439667ee2 | -7.8499 | -44.1246 | 2025-10-17 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 5fcebc18-9484-35c0-a9c6-822f5d9e58f2 | -10.1337 | -44.5313 | 2025-10-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| c650640e-4b91-3095-bab1-090aae73d608 | -6.3921 | -41.4811 | 2025-10-17 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 884e4787-c2cb-3023-9319-ef0d8584dba7 | -13.4977 | -51.2992 | 2025-10-17 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c89fe7cc-ff5f-3e91-9a61-c5125291f4bd | -3.9635 | -42.4934 | 2025-10-17 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| d045db9c-8a62-3ca3-9d80-b9f2737552f5 | -10.9748 | -47.9042 | 2025-10-17 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 034cda87-81ec-32d6-a6c1-580e6d553047 | -10.1333 | -44.5545 | 2025-10-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 241921b0-5c76-3ce2-8a99-67d6f14404db | -10.1139 | -44.5801 | 2025-10-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1d2ae5da-7c2e-3efa-b280-f860326da66a | -12.154 | -50.4165 | 2025-10-17 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| dba68d18-ede7-3f5a-af75-da1ad31f264e | -14.156 | -47.9283 | 2025-10-17 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 89a49152-380a-3265-a37f-6c01266f5672 | -11.3992 | -44.1229 | 2025-10-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 2dd13d66-b746-3928-8c2d-24c30ab41cc3 | -14.1754 | -47.9252 | 2025-10-17 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| eeb673b8-2a13-3245-86a7-a3bca61b0e3c | -8.4717 | -44.1746 | 2025-10-17 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 23c22057-0384-3e3f-adbc-fe961bf90a72 | -12.9607 | -47.9294 | 2025-10-17 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| d7a9c821-1ab6-3a13-97e7-3242ff14b64e | -10.534 | -49.5471 | 2025-10-17 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7d137b20-2b93-3edf-9b7f-d9e24ff46fba | -11.4184 | -44.1201 | 2025-10-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| fa0df722-2529-3c06-8caf-a54589f2ca51 | -10.4945 | -43.4079 | 2025-10-17 14:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5fe4896c-e0a2-366a-91d5-1e2eb744ffec | -11.3603 | -45.2646 | 2025-10-17 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9dea2347-6736-3db9-b621-6dac9c86b700 | -12.4866 | -45.4895 | 2025-10-17 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 25f5ac91-28d6-36cd-80e3-176529a202b7 | -12.7374 | -48.6247 | 2025-10-17 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 96f527e5-7cb4-302c-a030-9ff2699a5f6d | -13.2447 | -47.1262 | 2025-10-17 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e765a15c-9c6d-32e3-9221-921c80c47634 | -14.866 | -52.4193 | 2025-10-17 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 87eab331-cb9a-3ec3-b17c-a714a7d66180 | -20.8687 | -55.1408 | 2025-10-17 14:40:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 832b2301-f443-3b59-b8c7-335775cc788d | -10.1063 | -47.6525 | 2025-10-17 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| b792839b-610e-3bde-87a9-85b17c5ad706 | -14.8657 | -52.4405 | 2025-10-17 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c3a652a3-5461-3aa7-a544-6a11a13624ff | -8.1149 | -45.5622 | 2025-10-17 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| afe9bffd-2389-3d4c-92aa-805740421402 | -18.3938 | -55.4559 | 2025-10-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.7 |
| 255c7b78-ba1a-3088-a853-5c16376c861b | -8.0791 | -45.4071 | 2025-10-17 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 559129dc-a04a-354e-84ad-8f9df86a9ff4 | -10.8797 | -47.9157 | 2025-10-17 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 49c5171c-9226-3dfd-ad48-a1036475dd70 | -6.2012 | -41.7389 | 2025-10-17 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| bc019865-cfe1-3062-bfd3-f828f1596829 | -8.2467 | -44.06 | 2025-10-17 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| c56076df-63fa-3ebc-a7cf-751cda4dfc90 | -7.0238 | -45.7077 | 2025-10-17 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1ec1a084-e3f4-3b2f-b32f-abb5f97f8940 | -9.9638 | -47.0256 | 2025-10-17 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| fb345a16-c982-3c6a-9dc8-90476e95a960 | -6.4448 | -41.8368 | 2025-10-17 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 418e00bc-9c15-360f-ad8c-f462440b6e97 | -7.8307 | -44.1497 | 2025-10-17 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.2 |
| a2817c7c-79b5-390d-9aeb-994f2821f87a | -8.5605 | -44.6034 | 2025-10-17 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2819f69e-c7aa-3f95-aa7c-a86ac0c16ad2 | -11.5724 | -44.0736 | 2025-10-17 14:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| b5aea443-01c2-39e0-9c29-a2e402f81507 | -12.4678 | -45.4694 | 2025-10-17 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| a322a272-e5a4-3abd-a9af-5de12c41ba60 | -9.9831 | -47.0011 | 2025-10-17 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0d8e29a8-dfb6-32c9-b226-9f2e24a86224 | -5.872 | -44.7573 | 2025-10-17 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| bf00188a-c325-396f-b5da-2bb56d72b021 | -10.1718 | -44.5264 | 2025-10-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 1c393806-55dd-332d-85b7-e361028f15f6 | -10.2939 | -44.0221 | 2025-10-17 14:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 4e648bd6-6d66-3528-8e35-5d55e0a3150a | -11.0214 | -47.3443 | 2025-10-17 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5e97a521-354e-3ed9-be70-37310d9d598a | -10.5136 | -43.4052 | 2025-10-17 14:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 82316923-f3f0-3dc5-9a5f-9477f39e0ad6 | -8.523 | -44.5844 | 2025-10-17 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 7915f111-e404-3570-93af-0b7b74a9e51b | -5.6987 | -45.337 | 2025-10-17 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 407a0f7a-24fa-37a0-b90d-79f0012f65d1 | -10.6214 | -47.4155 | 2025-10-17 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 0515066e-8941-3c73-934e-4184dfe3ab8a | -10.6028 | -47.3955 | 2025-10-17 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 774f5b4e-5ee3-3fa0-81bc-edd382de527d | -9.9828 | -47.0234 | 2025-10-17 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 383.0 |
| 142ca302-bb99-3852-948f-d1a3e889a037 | -12.699 | -48.6299 | 2025-10-17 14:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a6ac233a-daa1-3fc0-922d-049d335938e3 | -8.5419 | -44.5824 | 2025-10-17 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 194.2 |
| bd4c6a0c-85bd-3c5c-b075-3dc95d4f2321 | -11.1419 | -55.1869 | 2025-10-17 14:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2a16874d-f149-34d5-904d-682023519acd | -12.0879 | -47.4277 | 2025-10-17 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 20af77af-0a44-3b51-b7bb-d2f3aa983c86 | -4.0962 | -42.2258 | 2025-10-17 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 69762eb8-fce2-32dc-ba65-3cc0a10a8b6d | -5.9095 | -44.7545 | 2025-10-17 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 9d89a9bf-1076-3d78-881a-58cf2484f134 | -8.1151 | -45.5395 | 2025-10-17 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 6c8ab118-7aec-3706-a963-0efc285ed405 | -5.8907 | -44.7559 | 2025-10-17 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 8917be6d-fb39-393f-a05d-7cd813cbf561 | -8.5684 | -45.4479 | 2025-10-17 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 49b5ce62-9786-3964-a0f1-d7ebf0eeb214 | -8.5687 | -45.4252 | 2025-10-17 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5480e0d5-3a9a-372b-9c6b-eaec4c6ea57b | -10.9189 | -45.4171 | 2025-10-17 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 30957436-48f6-3ad4-808e-428ceb9f4349 | -11.4193 | -44.0731 | 2025-10-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| b1292afa-0b5e-33ce-8c96-2b4aaf90213a | -7.831 | -44.1266 | 2025-10-17 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c5ab87f3-f4ea-379a-a42b-d5d1106a74bb | -5.4561 | -41.0054 | 2025-10-17 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| b4209ec6-622b-33b2-8c45-a54ff4de10f4 | -7.9693 | -45.1453 | 2025-10-17 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 637.8 |
| 01b9bcac-915b-321c-b16d-fad39da7b3dc | -4.1523 | -42.2226 | 2025-10-17 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 74f03267-6f23-307b-b9c1-0e82d90a3e34 | -8.4531 | -44.1535 | 2025-10-17 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 95e88ef0-0dc5-374a-9b90-00b41985230d | -10.133 | -44.5777 | 2025-10-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 96ec4542-20b5-3e7b-873b-1e796bc9a38c | -3.7626 | -41.7207 | 2025-10-17 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| fca4e2c9-f542-3aea-b8d4-7abff3897b4c | -6.4066 | -41.8882 | 2025-10-17 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 177.4 |
| e542f75f-5841-3d3c-8fb0-393aa6ea4b25 | -5.2487 | -43.2574 | 2025-10-17 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 0014fbbb-f17f-3904-96bc-63a59b0b5736 | -8.134 | -45.5377 | 2025-10-17 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 214.0 |
| b0ba4a20-19f7-3175-b7b9-406e3368bf4e | -11.3988 | -44.1464 | 2025-10-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 67770f46-1b68-36c8-b75a-e0e10dabb5fe | -12.1678 | -45.0771 | 2025-10-17 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 711c38db-9a8e-3ad3-98c4-14266e2d0ce0 | -12.1356 | -50.3758 | 2025-10-17 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ed8fdb11-a2a9-317e-b35d-a0a41e7f4934 | -10.8101 | -43.9275 | 2025-10-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| cb0a32b4-5106-3028-b53a-52d602c4946a | -11.4773 | -44.041 | 2025-10-17 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 246b2e53-ec43-35e1-9a00-b9a5f126a460 | -11.4581 | -44.0439 | 2025-10-17 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 24a201c6-4252-3028-a1be-236af080e26a | -6.823 | -41.705 | 2025-10-17 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 60e2dca8-8446-331b-aa25-89ca96034970 | -9.879 | -47.6779 | 2025-10-17 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |


[Clique aqui para ver as próximas entradas](README130.md)
