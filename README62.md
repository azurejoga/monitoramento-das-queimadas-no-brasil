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
| a40322c5-0079-3254-9156-f59c6a029a04 | -10.1393 | -44.5783 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0e68dc30-36bd-3bff-aca0-a04d36604ea4 | -3.5144 | -52.49277 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f67099e-3958-38de-ace9-1b98276f8b30 | -7.15645 | -42.52826 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8a72d054-a89e-38bd-a097-210e3af69bc9 | -8.59766 | -44.93629 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0b31bae-14f8-3cfe-bc8d-9b0687f5c394 | -7.46717 | -42.65223 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c135aea9-177f-3b06-9bb6-460863b9e0e2 | -5.3351 | -44.47132 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f32068-408d-3d89-bf5c-1c399b8f07d8 | -5.03865 | -49.22219 | 2025-10-17 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f952b2b7-27e4-38e1-95a9-ef4baa64fe93 | -11.46064 | -44.25304 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09692fe9-4e45-350c-8647-9788599fbde6 | -5.45861 | -44.64215 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e5151d7-2347-369a-97e0-75abddd595ac | -5.25057 | -44.90244 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db3d0b57-bd62-34fa-8ec1-72d949871cca | -3.68264 | -47.63826 | 2025-10-17 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e88f308-d8a7-3d5e-84db-9cfe38f04dc5 | -6.20312 | -41.747 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 13f32cf4-6e67-3b02-ad69-c0d85835be12 | -11.46137 | -44.01898 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5de3af07-f2a3-3848-af30-c17aff37eeb6 | -7.97683 | -44.13587 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf4e11b2-ee16-3f73-9e42-261525e5735a | -7.1733 | -46.93403 | 2025-10-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 998557d8-1593-3434-9f6a-9efb4e5016cf | -8.45269 | -44.18116 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05353fee-03f6-3732-836c-8aaee6aa7dfc | -6.07549 | -41.89856 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 332272dc-6236-3226-b2a3-74d041d31304 | -10.27067 | -44.03044 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b60bd77-2558-369f-88d6-a3055a38d114 | -5.18636 | -43.81292 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e0b100-2262-3584-82b4-279f8a5c20b2 | -6.22996 | -44.14668 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95778f48-6668-389d-a7aa-f87098ff7ec1 | -11.40441 | -44.23679 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07eb5ed5-06ef-3efc-8449-68381e7c0f80 | -5.89162 | -44.83116 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0470515-55fd-3b2b-a49e-0bc0a18f08a1 | -6.16795 | -40.89271 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bc1559d0-58f3-37b8-99ca-e36d2a278733 | -6.09345 | -42.39179 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f2d12d5-4082-3049-b813-c8b57bd0c614 | -5.28877 | -43.5479 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3836e759-8899-3856-a951-15f1512248ce | -8.20831 | -43.31329 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cdcfa1ca-4cb7-319d-b790-c70e27b183f4 | -10.47159 | -49.1873 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ff199f3-ff4c-3e6e-a643-832a85e5f96e | -9.0916 | -49.78838 | 2025-10-17 04:19:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b41d1c3-7d67-3266-8ff6-28a457097292 | -6.74853 | -44.37729 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66cf927b-bc90-3c01-ae85-115407ef229e | -8.21993 | -43.99307 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cebfaaad-dfda-397c-bca1-d77262194271 | -11.37952 | -44.20722 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61369790-936b-342b-b1cf-750632625d6a | -3.53876 | -49.01097 | 2025-10-17 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c76b88b7-a868-377b-85fe-29c4f16c125c | -5.86966 | -41.23772 | 2025-10-17 04:19:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0854cf3-6b5e-37d3-8b28-e6b85049baab | -6.93757 | -43.68528 | 2025-10-17 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82164f4e-131f-37bc-8f33-97cbdc98b6db | -7.12669 | -46.44117 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 444dcf85-4d83-3bc2-8d1f-c2a1fcd6ce53 | -8.27608 | -47.11357 | 2025-10-17 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a08bddf8-0761-30aa-b58f-2976da7b5538 | -11.45608 | -44.2148 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89286364-0471-3f9a-bcb8-15833197d559 | -6.22814 | -46.08009 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fe08db8-9e29-3260-a760-7355d61669ac | -7.64765 | -47.65491 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bfd29e9-4c64-30eb-bd7d-55220b79e84d | -5.89053 | -43.90202 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5b21b84-4484-3b9a-8f9f-358dc5ed6900 | -6.42622 | -44.72178 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8fef45b-aa66-385f-9cdb-5c7c5f798cd9 | -8.33483 | -46.23735 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 815dfc90-f2ba-3758-9ff4-bf1675dda265 | -2.87307 | -50.7337 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0e43388-e832-39ce-9bc5-8dcfe8b14758 | -10.83497 | -43.93998 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1d7173b-910a-3a8f-aee2-0247c11908b3 | -11.44771 | -44.24728 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44bf4fe5-f14f-379e-a5f2-2e02469333d8 | -6.0745 | -41.8998 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 865027c6-0db8-35a7-ae73-3af4c4cf9bb2 | -6.77499 | -44.66753 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32faffed-edd6-38b6-8b34-7e0512675baa | -4.57075 | -48.02464 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 856dc2a6-3d55-3dc7-8f53-dc8cf6bb6e82 | -5.51708 | -44.98389 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40f20f55-e42e-351f-9225-003655a7b563 | -4.30951 | -48.08315 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa50e76a-c5b0-39e5-bab2-18ce66039d92 | -7.07398 | -44.25483 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b962c267-c51d-3135-b78a-17d9d8fec941 | -10.15244 | -44.53691 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7507f65d-8e98-32db-aa9b-fe34121f9821 | -10.2954 | -44.04898 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1b1fb0d7-e9fb-37ec-b426-5a431d0fa2f2 | -5.89492 | -44.83168 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa1d9743-db11-3fe9-8463-a33f79afe9fb | -5.25659 | -44.21202 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c577d2-a018-37da-86a3-f81b9596ad98 | -7.95182 | -44.09959 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 725c430c-e607-3e64-aca1-f0889068d7dc | -8.17787 | -44.02258 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22ed7c64-4756-3d37-be9c-b0e957668adc | -6.75189 | -42.376 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 72dd4488-895d-3706-a622-7078a6b172af | -8.12334 | -41.18299 | 2025-10-17 04:19:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3555e984-775f-3401-8d67-0555be3cceb3 | -5.25712 | -44.20859 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cf049e7-2808-30f0-9678-314746ffd259 | -7.20251 | -45.49769 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c48376f-7e94-3ee3-b180-7e4c3e812e96 | -5.60052 | -42.69897 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0056dba5-a075-3089-b7b3-09dce04dcbc3 | -7.54286 | -42.05934 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c028414-1d0a-3d6e-9f53-0596b0f3170d | -6.24022 | -41.54317 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4121830a-f062-3b9c-944b-24cc63fb98d6 | -8.25014 | -43.33475 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 042c40be-dc6f-3fb4-ad35-84053af2b545 | -7.46248 | -42.16184 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b415c58-ff15-3f38-af19-44c7dd864928 | -10.61591 | -45.23674 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 303647a1-1f49-3a8e-8859-31dc56e52f28 | -2.87914 | -50.72516 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 738f009e-f53f-3575-ab7f-d61e10292524 | -7.76278 | -42.45459 | 2025-10-17 04:19:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99d4c1be-7fe8-371b-a8ac-92b62ef0797b | -6.25669 | -43.90933 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f151f33-0640-3095-8695-11ac84c4dfc9 | -6.49385 | -47.22471 | 2025-10-17 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14e9ac1b-75e3-3492-a7b4-e689a95a8408 | -4.92907 | -45.62534 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d4c8cb8-f07f-3427-a859-4f79fcc2ad77 | -5.26042 | -44.2091 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 340693de-3dc1-309b-8ea0-d5ab31b44cec | -10.88227 | -47.92631 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30053c45-0096-3e14-accb-c349afd702cc | -8.72445 | -43.8704 | 2025-10-17 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5978d5d5-75a4-3f47-90ee-3a2ccc56bbd5 | -4.87925 | -45.9407 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc716a13-86ee-33bf-a385-8fa85d1c125a | -11.48251 | -44.20012 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74200816-33b7-3303-b846-0ea28ff07fb3 | -10.27403 | -44.03096 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43ea4297-b1c5-34e5-bc7c-5533d112292c | -5.06445 | -41.20749 | 2025-10-17 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b432b5e0-86f0-3226-9d6f-0c19d38c3b39 | -10.11244 | -44.62116 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9d56b5d-1018-3210-bf06-ad837ae68aee | -10.16133 | -44.54556 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6da598da-c5bd-349b-aad7-5fb56a5812d4 | -8.44991 | -44.17712 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 638e8558-5f81-3499-adcd-870dcf868b0c | -6.49034 | -39.60664 | 2025-10-17 04:19:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a14bd8f-7e77-3ef6-a8da-655ccb2a381f | -7.96288 | -44.09401 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e0ecdb-4210-33c9-b679-da0b7edb55b2 | -7.60564 | -44.00602 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c88acda4-11ff-3b01-8da6-48b12f0d0aa2 | -5.42669 | -44.21465 | 2025-10-17 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaed1a11-a6a8-3d25-bfe6-fee730680794 | -6.20834 | -41.75882 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5dfeb47a-6f3b-3379-be20-92549db06c23 | -7.75871 | -42.45797 | 2025-10-17 04:19:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6cf20f8-dc06-32dc-9750-c8f0918e9699 | -10.1145 | -44.56374 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b34a8c88-1657-3972-aa72-96ed0e8c357c | -7.57584 | -42.67624 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71bc564d-3c91-3987-8ef1-0a06c7dc8bc9 | -3.50661 | -52.48726 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f428d6c5-d1a0-3e10-9977-ec22d7aba3cc | -4.53973 | -48.41255 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7997c696-e85f-3a19-a17d-5f69df8eff63 | -8.08264 | -45.42106 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d5df526-ebe1-3caa-bccd-e599d8bc8d84 | -5.91107 | -43.94427 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c20d9b5-4af0-3d01-8d1d-ff12b45a4f58 | -8.52184 | -44.57169 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7d5ff5e-592e-38a8-80be-d18932882bab | -5.90239 | -44.7411 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf121bf8-d524-31b9-b4e4-280a4c71201a | -4.53592 | -48.41195 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a3b499b-c609-328c-b528-475f7eb6f283 | -10.28189 | -44.02462 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af6a25cf-2f69-3614-8b94-60e3770952c6 | -6.08771 | -42.3832 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 524d3331-6331-34d1-87f7-224f5a5782cc | -10.84072 | -43.99358 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README63.md)
