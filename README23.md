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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61911620-1253-32bd-9a25-1a2de936803d | -11.2727 | -45.50731 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6ab25123-6ff6-38fc-bd85-7633b2391096 | -11.82942 | -43.53176 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17c5ec84-1d88-3fd0-9b27-cca096a643f8 | -11.65731 | -43.64776 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 86989c5c-e451-3fd7-b198-532fa3cc0588 | -10.54738 | -46.39906 | 2026-10-06 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 658a1852-4547-3269-baf6-c908183227f3 | -6.89338 | -43.68746 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4de0d2b-22ff-3a10-b415-afce622e0b4a | -8.69938 | -45.21795 | 2026-10-06 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 024ae89d-fb31-3731-9b88-728a59bfe5b8 | -7.10568 | -42.54392 | 2026-10-06 03:45:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 233c7976-37ea-32db-a2d1-8f3ff41835dd | -6.87845 | -43.685 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52cef7f6-d63c-367c-b132-78091d95de43 | -11.67663 | -43.67118 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c56940c3-26e7-378a-ac3a-59365246fbf0 | -9.26164 | -45.66161 | 2026-10-06 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 787f2011-7be2-3414-a404-650483001e2e | -11.27301 | -45.5013 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| aa4388ce-1120-307d-b317-c92839988766 | -13.02694 | -43.12053 | 2026-10-06 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 614c9413-000a-3841-824d-70f88fe8bb57 | -10.35883 | -45.02311 | 2026-10-06 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6365b2ba-4077-3e7e-acac-5152f9386ec3 | -7.76486 | -44.57986 | 2026-10-06 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d87da7f-863c-3e64-a781-2e34a1c586f4 | -11.28248 | -45.5125 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| aec7457b-af86-3919-acd6-a381f1ad3bc8 | -11.2837 | -45.50613 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 351207e2-63df-383a-ae73-cdbb885a9f94 | -7.47634 | -42.80129 | 2026-10-06 03:45:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 70a59350-09b5-345b-9fbe-918743506b66 | -11.28429 | -45.50305 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5d45babb-c8ea-3e58-88aa-497c6c3a1a95 | -10.35258 | -45.02833 | 2026-10-06 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8de979f4-0a9b-35b3-b762-720e448593ad | -10.50022 | -44.41488 | 2026-10-06 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f560c78b-9c73-378d-addb-d3248f182bee | -12.86429 | -39.93171 | 2026-10-06 03:45:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc3eab13-a5f1-3c32-89ed-ee638e3b892f | -7.29569 | -47.27611 | 2026-10-06 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7c98071-ba4b-36a1-bfe3-dcaa236be251 | -11.27361 | -45.49809 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7823c482-f0d0-3489-9a91-2344a0abcdad | -9.09588 | -47.06698 | 2026-10-06 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ed78330-1eaa-32c1-8ed2-1e7007555985 | -11.28186 | -45.51572 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 1c3e4b8e-e82a-3b94-b800-1b5755cf64fe | -11.68922 | -43.65372 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 71a474db-d49f-3f25-a405-43eb4f30539b | -6.67389 | -43.82324 | 2026-10-06 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05bc838e-0cc2-37e8-9574-7df844f11dbb | -11.66439 | -43.63477 | 2026-10-06 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5bb4d1c5-3cc0-3401-9051-01a4cb15e14c | -7.48096 | -42.8022 | 2026-10-06 03:45:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6fc05b56-cf42-3af7-8bb8-1d39e81d61a7 | -6.88393 | -43.68297 | 2026-10-06 03:45:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f44aa4e-f375-3ff8-ae3b-a72b3321ab83 | -11.26542 | -45.51327 | 2026-10-06 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55d01fa1-6478-3cd5-8819-66ad1a2bee3d | -16.23748 | -42.23257 | 2026-10-06 03:47:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92e5de3b-0d87-378a-95c0-7ce1e2777979 | -15.53006 | -42.63955 | 2026-10-06 03:47:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 79440d73-6196-3386-8cd4-de8c16ea24c0 | -14.1095 | -44.61094 | 2026-10-06 03:47:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ed97342-cf5d-3543-9e09-d56699402dd7 | -17.68375 | -42.18225 | 2026-10-06 03:47:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 59c44660-2736-3946-bda3-49ab570953d4 | -17.01495 | -40.68765 | 2026-10-06 03:47:00 | NOAA-21 | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d5ec616-15b7-3269-b92e-4b5899e723bf | -16.23915 | -42.23094 | 2026-10-06 03:47:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6e0f85d4-dfc5-3b9b-be8c-733bd5c8098c | -16.01584 | -43.60093 | 2026-10-06 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c36811ed-a16d-3d59-8b97-9b364eb3736d | -17.72651 | -42.63662 | 2026-10-06 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f75d6f08-2714-3c1f-85f1-e8c0c727799f | -18.03579 | -41.66607 | 2026-10-06 03:47:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d862195f-c08c-3ea6-ba7e-e25f761c94f4 | -14.80324 | -42.00873 | 2026-10-06 03:47:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 90ef5f7b-7a0f-3082-b395-30050a49a444 | -18.54404 | -41.29597 | 2026-10-06 03:47:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f0177e43-0ac2-3af4-b65d-4500a23f52a2 | -15.79422 | -40.31696 | 2026-10-06 03:47:00 | NOAA-21 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a586a853-2fd8-31a0-9330-3e286808f9f4 | -14.79691 | -44.35604 | 2026-10-06 03:47:00 | NOAA-21 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a6b5edf-7893-39b4-b87b-3cc62b869c18 | -18.03941 | -41.66688 | 2026-10-06 03:47:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3e5504ef-c2ff-3011-9308-4edcc5b76605 | -16.67452 | -41.84921 | 2026-10-06 03:47:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2dec607f-4338-32a9-af66-6ba595ec549d | -15.04911 | -42.03329 | 2026-10-06 03:47:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0f7a3757-c20b-368d-883c-4144f50ba0b5 | -17.19296 | -40.30064 | 2026-10-06 03:47:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 9c172260-3285-3ce6-a400-6ab51edcf17b | -15.1162 | -39.92279 | 2026-10-06 03:47:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5922f5e6-b65e-35ee-a9cb-db1967bafb6e | -15.72696 | -43.9296 | 2026-10-06 03:47:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 427fd2c9-ab46-3e2e-8e0e-5c26fe8f9092 | -14.75963 | -45.14862 | 2026-10-06 03:47:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 937b82de-718f-3e44-b8b2-fb626d1e60a1 | -15.72775 | -43.92541 | 2026-10-06 03:47:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc6e8c08-11f3-322d-89de-8432455e3c79 | -15.71618 | -42.23779 | 2026-10-06 03:47:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2bae59b-5af2-3593-ab9e-5207ee5ae69c | -17.19574 | -40.3053 | 2026-10-06 03:47:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| dcc00aee-6154-3bf9-b48d-4828b85b3e1e | -14.62585 | -43.66719 | 2026-10-06 03:47:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c04c1005-5a97-359d-8938-4fbbcc07ebed | -17.71343 | -42.27789 | 2026-10-06 03:47:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77810aed-889e-3ee6-87f9-245adb4298d3 | -17.76068 | -42.42613 | 2026-10-06 03:47:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c6a08d2-1052-3b9b-babc-00bcd66fb33d | -18.40818 | -41.15349 | 2026-10-06 03:47:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d8c62a0e-dcc4-33c3-9d25-c8841d3bb46b | -17.90299 | -41.58613 | 2026-10-06 03:47:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e46cc56-b358-3e7a-adf3-3264aff68e51 | -15.54591 | -41.00978 | 2026-10-06 03:47:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4172effa-83ec-31f4-ac54-0a4f28117765 | -16.01508 | -43.60501 | 2026-10-06 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf1e092a-c1a4-36a3-be86-a2374f6e148b | -16.01163 | -43.60013 | 2026-10-06 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a20f7576-09a2-3c0e-b2c6-91e40e37c13e | -18.53973 | -41.29966 | 2026-10-06 03:47:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 731a3f64-8f3f-35bc-b7d4-fa8b3c9bc78c | -18.54329 | -41.30035 | 2026-10-06 03:47:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 86b2940d-1c78-3443-bb08-64b94c4492ab | -3.0375 | -53.8865 | 2026-10-06 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 621473e7-e4b9-3661-9145-16fc268faa10 | -3.0932 | -53.7239 | 2026-10-06 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 08e7c55e-358c-3641-85ad-dc6d9cfdde8b | -2.8713 | -54.1518 | 2026-10-06 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| cc652a20-58e8-3da5-8b65-b30bd73b27a6 | -3.6731 | -55.9622 | 2026-10-06 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 042c07f7-48a1-3dd6-a49b-dfb5aa1534cb | -3.6732 | -55.9425 | 2026-10-06 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9cc6a5c1-ddc9-3733-a15d-8aa4d2dab012 | -3.0548 | -54.2076 | 2026-10-06 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 754657b8-dfa3-3a42-91b6-2a9e458b1384 | -3.6915 | -55.9618 | 2026-10-06 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 36cef8d3-635b-3f19-b875-84b5cf7c4eaf | -3.0915 | -54.2469 | 2026-10-06 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 26355e0f-d9f8-3543-bdd7-4a6e02a48d2f | -3.0375 | -53.9066 | 2026-10-06 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 95f7b34b-0b64-32bc-9bbb-9506ce70b655 | -3.0734 | -54.167 | 2026-10-06 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2332ae08-fffd-3458-b43a-e194fdca2c79 | -3.0932 | -53.7441 | 2026-10-06 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 743765e9-f5b2-3171-8892-057cfe84007f | -9.7312 | -65.0944 | 2026-10-06 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 120c6832-c18a-3ab6-b379-81fd70108751 | -3.0917 | -54.1666 | 2026-10-06 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 7da6c90f-98f2-344a-850e-c3d9c4c00fce | -5.8323 | -45.0105 | 2026-10-06 03:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 8a00045e-8874-3ce1-b285-1057ad9126ec | -3.0917 | -54.1867 | 2026-10-06 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ef03bfb2-f881-3933-afc7-44a8cfd0fd0d | -3.0192 | -53.887 | 2026-10-06 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 3f9b4946-ab2b-3833-9e17-5a87625fa2b4 | -3.073 | -54.2674 | 2026-10-06 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7f91d597-1545-3d36-a2f8-e366394c6956 | -3.0548 | -54.2277 | 2026-10-06 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 020cdad9-1219-3760-9eb6-0cb94155a905 | -3.3723 | -58.1957 | 2026-10-06 03:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 697ea4d2-47f9-333c-8160-a3e2d2854927 | -3.0191 | -53.9071 | 2026-10-06 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 292d592c-2c72-33b6-b2fe-d5faa9349554 | -3.1115 | -53.7637 | 2026-10-06 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ccad4e7b-67c5-304b-95dd-9217b3d2341e | -3.0731 | -54.2473 | 2026-10-06 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 07f5c8a5-2b5d-39a9-9d3d-af005fe5633b | -5.8511 | -45.0091 | 2026-10-06 03:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 616ffc5f-8825-3783-a0b0-efc24a61b7a3 | -3.4943 | -54.6367 | 2026-10-06 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2058a9da-a938-3377-a094-469a0778dd59 | -3.0732 | -54.2273 | 2026-10-06 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ebb35b3b-a2dd-3c54-9a08-76479bdd1de5 | -5.8323 | -45.0105 | 2026-10-06 04:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 197b6a20-4a4c-3051-bfec-823f98273be3 | -3.1115 | -53.7637 | 2026-10-06 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| abe73a67-a5f1-3229-8533-078175222c28 | -3.0192 | -53.887 | 2026-10-06 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 7fc9bbf8-d9f6-3fa0-97d6-7a1af4016508 | -3.0548 | -54.2277 | 2026-10-06 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f9d1a2dd-2600-3290-948d-00bdeffa6b24 | -3.0731 | -54.2473 | 2026-10-06 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 3673d890-2442-3986-a4d2-dcebbbcd3e0f | -9.7312 | -65.0944 | 2026-10-06 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 211ccd66-2abd-30fe-a8eb-d6472da30981 | -5.8511 | -45.0091 | 2026-10-06 04:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 43e75ca8-3dc9-3a1c-967e-58b650897e97 | -3.0932 | -53.7441 | 2026-10-06 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e99a0849-3ff0-3408-b09f-dc83a99584cf | -2.8714 | -54.1318 | 2026-10-06 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f2df5c78-a051-37da-a1f6-028ecda3f342 | -3.073 | -54.2674 | 2026-10-06 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2899be7d-dd9c-36da-b0f9-4682453fc51d | -3.0548 | -54.2076 | 2026-10-06 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |


[Clique aqui para ver as próximas entradas](README24.md)
