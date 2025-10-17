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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9a5de70-944c-391c-8d20-7e18f04abd46 | -8.62668 | -54.56433 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e20455-86fe-3348-b8bc-f71953ee9b35 | -4.18554 | -48.92953 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbc26254-14d4-357f-9beb-eb042f86dc85 | -10.40833 | -48.07227 | 2025-10-17 04:19:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 618f124e-358e-32d2-9c93-7d4526f3cccb | -7.46659 | -42.15841 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 40a0c419-5fe1-363b-b6da-4c5a971b84fe | -7.83605 | -41.11617 | 2025-10-17 04:19:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 270b4ec1-7a18-3806-aa04-690dd3773ab9 | -4.04612 | -47.50241 | 2025-10-17 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 523c445e-16e3-3f2f-9a64-ca738ae5da04 | -11.46197 | -44.03809 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580ce431-4f48-36f2-b79b-6aefe6c8946f | -5.86691 | -44.83788 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6784efb-035c-3a22-aab6-f25c7eec1a8a | -3.68334 | -47.63391 | 2025-10-17 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df82ae6e-d806-38ea-a6b2-02fbf01f745a | -10.28469 | -44.02882 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0164599a-e983-3851-a5cc-7f9de576ee74 | -7.33903 | -44.16839 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f8f3c94-6692-3713-a93e-f0cc850c9d2f | -7.61777 | -47.83934 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43b97d02-1b99-36bc-ac5d-dea48c97f2bc | -11.06223 | -44.65739 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd088420-194a-3c5a-bcb6-ca1dec903429 | -6.93581 | -45.13866 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 278d5eb5-3ceb-31b6-b1fe-60a51ff56dc7 | -7.00245 | -46.99258 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf72d7c3-c70d-35f1-ad79-2832762db584 | -6.20598 | -41.75025 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1aca3ffa-340f-38a8-a951-b9aff55152f1 | -8.3848 | -46.24193 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e49345f-47d3-306f-80b7-21f5467653a6 | -9.61985 | -49.1203 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6dfe7e6-c791-3538-97b2-c16534a27d04 | -7.20637 | -45.49473 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a4cb4a58-584e-382e-bae4-500f20e142b4 | -10.51871 | -43.38696 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 057338b3-7dcf-376e-af2e-a705e6d789c7 | -4.40342 | -50.49566 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db3676fb-cda3-363d-b6bd-ae2a6fab330a | -5.91559 | -46.51761 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee6af6c-6805-3906-9baf-03569401a05d | -11.45382 | -44.20694 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5278654-9440-376c-9f30-242af45a01e8 | -10.49574 | -43.37564 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e94e199-f3ae-37e0-885d-03449e25819c | -8.12293 | -45.55204 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f95a7272-5249-347e-bfa3-7aecf24da8ce | -6.23549 | -44.15462 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dbbe4fb-f2dc-3126-aa22-3e3ae98c4b7b | -10.8782 | -47.9296 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 250a8655-f06c-3e9c-8560-beada43c3095 | -7.30023 | -42.32107 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 081f4475-e744-31c2-b6d8-320cd118725e | -7.30718 | -41.96444 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 88b316f3-acc8-37e7-93bc-3110cf1f2d59 | -5.71626 | -44.51743 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de0c13f2-2ea5-3ef6-a0e5-d7e250017628 | -8.96925 | -50.25048 | 2025-10-17 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 814937bf-3695-3ef9-a750-bff5fb831a5c | -6.09747 | -42.38855 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1c9ddddd-56ed-3d7d-af3d-a659aa81cea6 | -4.81162 | -43.20173 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a69c20fa-14a2-3ca2-95a7-10c19eefea2e | -9.62086 | -49.1278 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2e38e97-f03e-39c0-9b42-bb04950957c9 | -5.50759 | -43.78186 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7924ca47-f7d2-3d31-8380-3a1c47c1faa7 | -3.51123 | -52.49095 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 189b4c55-f156-33f5-88ae-46f41135de40 | -11.49818 | -44.05132 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5daa840a-2469-36ec-b444-e23efa46d754 | -7.35301 | -43.85848 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1c9e5cb0-f8a2-3730-9726-828ac47960f9 | -7.28769 | -41.94897 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9108032a-9039-3dcb-8def-42632972948a | -7.27869 | -42.3217 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d7cb15c-b134-345f-8b0b-ed9509029e59 | -10.28585 | -44.04387 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 726e4b48-c839-3f39-b817-dea3d8a8aabb | -6.07098 | -41.89929 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bad49706-0929-3915-a37f-6711ee25ef66 | -5.29818 | -43.55293 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a1e64a9f-887a-3158-81ba-4449b53e4b97 | -6.74523 | -44.37676 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f8451ab-d21f-3a48-9910-d15d72d7afe2 | -6.23781 | -41.54433 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 91eab85b-f7bf-3c69-af1d-b54b75ba9ca6 | -5.4962 | -42.16334 | 2025-10-17 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7326fea4-08a2-3e00-82c8-1ede5ebadb9f | -6.8015 | -46.88686 | 2025-10-17 04:19:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0d6ccfd-28c4-37c1-9853-ba2ef53301ea | -6.49402 | -47.49247 | 2025-10-17 04:19:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9a71e61-6285-399b-8deb-d83e2bee060d | -6.40082 | -41.90101 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2af36bcd-3a57-355c-8495-0970b3ba6ca6 | -9.14952 | -46.73627 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4aef90ad-1552-3c9e-a995-136fcd97fd1f | -10.11837 | -44.56072 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3849afe-e92b-30d1-9dab-72afea44d734 | -4.82093 | -43.16348 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c684ad3-02c4-3bd4-8257-e5dd6f37201b | -9.35057 | -46.92588 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7ec2d97-1ade-376d-8b1c-335621ae5ad6 | -10.09785 | -47.64671 | 2025-10-17 04:19:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6fb75ac1-50f6-36ed-acb2-0d37cdfcd92a | -7.04315 | -44.25712 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2917ab33-73a9-3bec-ba82-5348a9fa55b9 | -5.17394 | -42.92305 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ab32cfa-0cd0-3b75-865e-51305628ac08 | -7.46893 | -42.16692 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7230e050-6dbf-304d-82fe-3baef1448e10 | -10.61922 | -45.23727 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e3de715-46c3-3f5f-9d7a-f0ad816bb210 | -5.87405 | -44.83547 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 721a0f42-b05b-3638-b623-3874299ae4e8 | -6.83073 | -41.71554 | 2025-10-17 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef01c1c9-cd19-3a13-8a55-7f0e0b84fa09 | -8.26257 | -44.06821 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ecb81fe-b15b-31c1-a4dc-05db93efe4e4 | -10.29031 | -44.0372 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c7fda900-54b6-3f3f-8d73-e88ee10a29f7 | -4.33283 | -47.89029 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d1ef54d-b027-3695-b596-5c692b92cf55 | -6.23219 | -44.15411 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afa9c649-8a2a-3ea8-b5c4-2274435c1dfd | -8.07988 | -45.4171 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b36ebe1-9444-3a69-a810-b2da5a0ea4a0 | -10.264 | -44.05167 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dccbc998-3efc-37bb-8e96-f9ad8484b61f | -6.20947 | -44.42956 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faef0358-4521-37f5-824b-6ec7664dabbc | -10.10078 | -44.60852 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3b07a76-a0c7-31a2-8d15-56a055056c8e | -5.55102 | -45.19873 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7983cc09-e6c3-38c1-848b-a2bc738b488a | -8.12127 | -45.54108 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acb863d0-1b79-3b8b-a9d2-8783f4e0c787 | -7.09382 | -44.25792 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0ff3749-59ce-3d83-8580-2dc6c0803d31 | -4.26317 | -49.69072 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77322ba6-5263-30e5-936f-231342a2d12b | -8.39699 | -46.25126 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19cdde02-3114-352c-8979-0bc599cd913a | -6.14169 | -41.72141 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f368644-8109-39b6-a04e-2008b8c0f4d2 | -9.13727 | -46.64912 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7fbd5984-939c-3447-ae2a-a3e18bac5008 | -10.11063 | -44.56675 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e23402d2-495a-3c9c-b373-d026457d0d11 | -10.29087 | -44.03354 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a548a9c4-9ac9-3faa-9fe0-da85d97134be | -10.53343 | -49.55162 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| d442b906-eb3e-3d27-88bb-f9b1ac56d53f | -8.16443 | -46.0649 | 2025-10-17 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd046b01-d768-3f3a-998e-b2fb0256eb43 | -6.20893 | -44.433 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff0492c1-cd25-3733-bd7b-41b836809b0e | -9.245 | -44.35853 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43b76428-90fe-3331-b49b-dd5aed0f0745 | -4.4139 | -43.39735 | 2025-10-17 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e8842b7-f71e-32ff-8f08-01d25014f17e | -8.40486 | -46.22332 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3ae9660-a48b-3c71-a769-53b74eb0c810 | -10.2618 | -48.8266 | 2025-10-17 04:19:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4ae10ec-eadd-3675-b5ba-7f9761995be0 | -5.91611 | -44.73973 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c26adc-75e3-3841-90a0-ddcb3cf0173b | -8.37696 | -46.24813 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 533ee229-88ec-35e8-ab85-453c3589505a | -3.13025 | -50.2122 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b224cfe-abbc-3ed5-8301-6d348fcfc9b4 | -9.67741 | -44.53142 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 065a4c2e-6ea5-31b6-a70d-cacb382028dd | -3.55166 | -49.95451 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ee8d708-c700-366c-9f67-d87467392328 | -3.16 | -49.74727 | 2025-10-17 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33c5867e-b37d-3873-b789-b4d66592b273 | -8.4767 | -50.10392 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d139d60-1b52-3f0c-ab03-89c1dc150e7c | -6.14925 | -40.91672 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3788b13-bcd2-3953-894c-17c3083ddba6 | -6.23064 | -41.54329 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce5d5fc6-53f9-32e0-a353-1731eaa29b5d | -9.28612 | -46.90807 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80c94bbb-f392-387f-a937-31c1e4e28ff6 | -11.16709 | -46.12688 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 039f2df4-597f-3394-b34e-250063bc9c0e | -10.64683 | -45.2989 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ecdc5b8-0bfa-334e-9f45-782a11f64b24 | -10.16188 | -44.54198 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 312f4036-274a-39ca-9331-61d72a4600f1 | -5.33853 | -42.5574 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d9af683d-0ace-3756-a955-ee93e12672c5 | -8.4043 | -46.22688 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57bd7a3c-1f6e-3862-89c2-43d36826df2f | -9.97657 | -47.0125 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README52.md)
