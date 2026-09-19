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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 499b5cb0-de0c-35f9-a582-ad0a7f0a96a1 | -7.09757 | -46.44756 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5981cfcd-ea64-309b-83b2-75b80a48b392 | -9.25146 | -45.92031 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49775887-aa0e-3c5c-9afe-faa823c183ae | -6.49299 | -43.81548 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb1e1bc2-d34e-361c-8053-8bb167f60319 | -6.9381 | -43.10982 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3eb613e-bdec-3b2d-aec4-a8ba8e954a8d | -9.9582 | -46.55425 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cd909f6-c845-30e8-9ba2-9935b789adee | -3.36735 | -50.45079 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae29dfed-406b-3946-a250-ce9aaf21f6b4 | -10.20516 | -46.58211 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bf47be0-6114-3e07-a53d-817b12ba42f9 | -10.17171 | -48.45875 | 2026-09-19 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ece770ed-3f7c-3dc4-97a6-35a3efd88cc0 | -7.29322 | -38.95971 | 2026-09-19 04:02:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8cda8b2b-46d1-3af9-bff0-c4ebfad176d9 | -7.04723 | -42.08474 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c4414cc0-9af2-342d-9201-c5fd94d7e4d6 | -2.96422 | -52.14511 | 2026-09-19 04:02:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9001d3e1-b037-366f-ad64-cc60513668b5 | -10.75991 | -42.1142 | 2026-09-19 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0cb09c6-2ac0-3b2b-b45d-e09405ba9f2d | -9.00797 | -44.91774 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 773ae4df-b3cc-35ee-99a0-7575cce97709 | -10.53166 | -46.73835 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 951ffbca-5030-3ae2-a44c-2c25030ad31b | -5.87868 | -44.98193 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58751e76-1e0a-355f-975e-48675447d542 | -10.31916 | -45.30933 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 17380d8a-d4f1-32c3-91a9-a75966996c4f | -7.58354 | -43.45182 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c282d297-9195-3c04-b26a-7301152c74a9 | -9.55951 | -46.57395 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d32b923-fd4c-333d-9d16-4a13ff69a384 | -10.32114 | -45.31221 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dccfba12-034d-3dee-8243-b63cf006410d | -9.82124 | -46.39748 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56307062-fad2-36bc-904a-c5d3706c881d | -7.43507 | -42.1162 | 2026-09-19 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6166880c-651f-3f8a-a012-eb3a76080385 | -9.23862 | -46.18854 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77ccc48f-444c-3923-a75c-00f549b9ccd2 | -8.77693 | -48.67041 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8fb00460-0bf8-3f55-9575-3ade622bc8b0 | -5.57654 | -42.73242 | 2026-09-19 04:02:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4f4463e-a95c-3f40-9b82-2ae0f69989ba | -4.56905 | -42.97658 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8d707aa-9234-3715-b665-87cf61034820 | -6.02154 | -51.76355 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eec2d939-1c64-3f06-bdcb-5ff2e5ad1863 | -9.90672 | -46.52991 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 759ee08f-0d44-31a0-8b11-4410a6979418 | -9.89421 | -46.55213 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad03c594-b01d-36c8-b474-e4e6e97af2b3 | -9.76006 | -46.59208 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78263964-5d66-33b4-b39e-cbcdbf74783f | -9.00416 | -44.91714 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c15bc8b9-1124-3d2c-a854-34ee7c365487 | -9.74804 | -45.07135 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f42f1845-6839-38d5-bad4-dc9b52dee765 | -7.76261 | -46.73521 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4679dfcb-8e1c-35c5-a3c0-64e7a36e8865 | -7.8189 | -44.9623 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d81077d-7c7e-3df1-9362-ad0a66f65cc9 | -7.7822 | -44.88869 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 023b45fc-4cef-31a2-b58c-fd043863cf4d | -4.25877 | -48.54211 | 2026-09-19 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3d00cf18-f64d-3dae-9a3d-e67c294ab8c8 | -7.69014 | -46.089 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1607861-9b04-370c-80f6-c89aad245af4 | -8.84231 | -50.45152 | 2026-09-19 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ba9a64-f4e6-3f37-bbca-a5c3fe356438 | -3.03469 | -48.41274 | 2026-09-19 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4a3d4055-1a27-38c4-8d38-939efbc54b14 | -7.77861 | -44.83772 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5589d417-db68-384d-a850-d8d30f15e1ee | -2.82949 | -50.45772 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 07363905-5d88-3872-8b27-f8bec5e84a55 | -9.5152 | -43.24503 | 2026-09-19 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f7b8b9f-77cd-32d2-95a4-136fa6f48aca | -3.36812 | -50.44637 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22456009-a515-3465-af8d-ff7eb9524569 | -9.55808 | -46.57746 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fe284a9-eb5a-3530-a072-6e02c73bf3f9 | -3.4522 | -50.60979 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c1476e9d-6f54-32b2-bafd-f0ff730fb455 | -4.26965 | -46.5358 | 2026-09-19 04:02:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 805c5a6c-237d-3b5a-a919-8f70656cda12 | -9.05449 | -48.72582 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b254f65e-cc36-3cac-9d04-d95204bc33a1 | -6.80584 | -43.00713 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 796bd910-9e9f-3a11-8dfa-0139bd6f1f7e | -9.55875 | -46.5735 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34336307-c768-3eb2-90de-d4dc946ea856 | -6.9844 | -42.18938 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a23dc155-ae9c-3376-afc7-9c0a53faa075 | -8.38444 | -47.24688 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d78ccb84-b12b-3454-ba32-2f48187720ce | -10.52612 | -44.8447 | 2026-09-19 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 983d2a5e-47c5-3eca-8972-3639c52033ee | -10.32196 | -45.30745 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c8fa0891-fb0d-3466-a1f7-a4d064a7fbaa | -8.78076 | -48.6772 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 23d1321f-3188-3707-97e0-1efb5a5fbac2 | -7.8837 | -46.42891 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9b3e33d5-38d8-3fec-8841-ef78a7c3efce | -7.6032 | -45.42723 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1863e068-6c16-3655-ae6b-48f462d7d2de | -8.4814 | -44.8353 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 952cc5dd-ae0c-3885-81b5-be11790cc0ae | -7.77853 | -44.86248 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfc9401b-904d-3be7-904f-c09d8343c505 | -7.76408 | -46.75303 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8d82aabb-121c-3ad4-925b-21feb28a9b48 | -3.49823 | -49.51207 | 2026-09-19 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cd40cdf-db37-3382-b8c2-b9010d5e0ed3 | -10.52907 | -44.84986 | 2026-09-19 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96490d63-e3a3-3b66-9e3a-e7726cd6defd | -6.58624 | -44.14745 | 2026-09-19 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 221f930b-9339-3e48-ba3d-45aa0d959635 | -7.08501 | -40.58836 | 2026-09-19 04:02:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6b9f654-5da5-3ae5-a706-025c6f642460 | -7.6889 | -46.11637 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a32d429-9cf0-3d5d-b1ab-d1785f357a3e | -9.04958 | -48.72505 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b15b056-996b-3608-a1e4-dbd7f8f2f562 | -7.7136 | -44.6422 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e17a910c-0631-35d3-956b-ddebcdf137cf | -6.98277 | -42.17764 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7059accc-55d9-3e83-907d-c85475ad28a4 | -6.98869 | -49.76122 | 2026-09-19 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3957eab-ff70-333f-8c6d-a4c4c23c0702 | -9.79423 | -48.33152 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fad4110c-b5c1-381b-b08e-765fbde3ab67 | -7.78383 | -44.87868 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a8e8139-113b-30e5-8dc8-6525f92f667e | -8.36741 | -47.25047 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| baf0e159-9cca-33e3-bd15-19afbe5ddfd4 | -9.9013 | -46.53637 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc9a8389-e72a-3954-8f47-76e1d2bd700f | -10.53096 | -46.74226 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e3db485-a2ee-3c88-8a8c-0c56f3540d90 | -3.03813 | -51.37461 | 2026-09-19 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3706a1d0-d668-3a45-a22a-ff479f109f5a | -4.35856 | -47.77856 | 2026-09-19 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 240f25d4-281e-3699-95ab-2f0ffd34d84b | -6.98158 | -42.1851 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9425b8dc-10f1-3aff-a3a7-935c36a2b061 | -8.47279 | -44.51401 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f88ef5d-911c-3385-b031-648bf3f812d5 | -7.69029 | -46.11304 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93c750f2-d5e2-30b8-8c13-8a89be99cd87 | -10.23427 | -48.84753 | 2026-09-19 04:02:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2813715-396e-3751-b466-043e55910286 | -4.57672 | -42.95189 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2288cc4-35b8-39de-9c63-42bc63b94919 | -7.78915 | -44.83195 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 584da4d1-8b66-3f2e-ae84-2e8ebd9f9f4b | -3.56137 | -50.05747 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37ed8252-7a3e-3b1d-be9c-cdbfa81c3d78 | -8.36497 | -47.25261 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd6c6b1f-c994-3313-a670-1487c6c9c2dc | -8.33013 | -50.86041 | 2026-09-19 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a8cf922-e03e-3848-80d8-101431b4e6f6 | -4.56475 | -42.98019 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e96b36b7-02ec-3a98-a276-d85fdc2e96a0 | -9.7594 | -46.59589 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd6b5340-c1ee-36a4-bd72-6de22148a2eb | -10.50156 | -46.2679 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29d5dc50-f1e7-38ef-a0b3-04dc6bd8e09e | -9.79075 | -48.33341 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e06476c-f953-3b02-a131-d941fb37b4de | -8.66032 | -45.44954 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 257dda7e-6fc6-301d-89d7-4a5ec4740330 | -9.98298 | -50.27773 | 2026-09-19 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aab3fe95-4863-3145-9950-fcf485a18699 | -4.36214 | -47.78189 | 2026-09-19 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 19bff3e1-94d9-3994-8636-013ac1d5c2a7 | -7.23196 | -39.35707 | 2026-09-19 04:02:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1f1265a-4012-3baa-bacd-ccb22a5ffa1d | -9.79228 | -48.34262 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| be1dec13-ae27-3cc3-a3c3-2b25e88cc1d7 | -7.78715 | -44.83403 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8233f0a6-f893-34cb-a845-3df16c7e84ec | -8.12468 | -44.82699 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d9bd5f5-8553-3e64-8a5e-c8e3ace6d2ac | -9.0387 | -48.75795 | 2026-09-19 04:02:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 432eb519-cfc1-3783-8b43-b64f21bf7fa5 | -7.86308 | -46.4464 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 28314cc8-e58a-3511-b020-a268860b1e48 | -2.82718 | -50.46453 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| a70ab15c-1225-3803-8e35-7570455311d7 | -2.83477 | -50.46331 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1b71824-21d8-3bec-aa0e-a04cd40ba390 | -7.37685 | -44.7323 | 2026-09-19 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b43cc9b3-9366-3bd5-b9f1-01a34021802d | -3.45295 | -50.6053 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README31.md)
