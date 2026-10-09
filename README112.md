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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 951f64c5-e316-3f3a-a4ca-228ab76da686 | -7.88964 | -55.00342 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5c88f3c-9ff4-36be-b800-69b43f41a4cc | -11.6094 | -43.69052 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a836296a-c1b4-3324-90d0-8b041ee99f4b | -10.85657 | -59.12016 | 2026-10-09 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd885a0f-2e93-3ad7-b3b3-3a06af893849 | -8.23774 | -48.57968 | 2026-10-09 04:27:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ea86740-7f8f-3254-ad3b-4f77108ba747 | -10.73368 | -52.03152 | 2026-10-09 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bcd2947-77b3-3e3d-a254-d91e369de9e7 | -6.49942 | -55.30978 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08e7d1e2-ea78-38f9-9397-ba472a3a8e6c | -7.53944 | -47.12185 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 356ee340-7dd1-3250-b85a-137374f5e3ff | -6.49129 | -55.29544 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 726862ce-4a00-326b-86d7-95a831bf9ee1 | -14.08344 | -43.77631 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 841e5909-b688-3fb9-9376-6a1baa3d1c32 | -7.39943 | -44.74546 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 0a50283a-2b68-3661-9a2f-c42ccdf1b4e9 | -11.98122 | -57.61416 | 2026-10-09 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd0e1568-3fa9-3951-b794-daf6357d8a1a | -11.19322 | -45.29829 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9884a7f-b960-316a-90c8-ac3c8de627e7 | -13.17703 | -54.35361 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44987104-c811-3afb-8c78-100db555138d | -9.75888 | -44.78806 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07ad8e0c-5457-37b3-9184-df8c5f6a239f | -6.06799 | -53.60366 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 348e7b85-b65a-3064-be8e-6f61d15ac7d7 | -8.5645 | -46.89871 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 872b986a-20c2-3187-a1ef-a0dbd700e8f5 | -9.29203 | -47.44493 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd7af944-ed97-33f5-8876-b3801ce9e67d | -6.1005 | -55.73007 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91765665-eff9-3473-88b0-d7aab608a014 | -12.817 | -44.64686 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b45473b6-48a9-3f38-9451-ce9ffd390ab1 | -12.21366 | -57.1373 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 607f9964-c78e-3c91-9974-a0679e6ec379 | -12.22244 | -57.09052 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| e49eedf6-30eb-3554-b7a5-c8a52b663313 | -9.20683 | -60.86957 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b9da5ba7-feaf-30d0-9b5b-87d613bd33e8 | -7.90076 | -54.71297 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 78607302-3d1e-3a4d-848e-210837b75caf | -6.22844 | -52.78996 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8df37f90-011d-30b0-bf22-62e54e3464de | -12.21603 | -57.09008 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6259304-3b49-3563-b75d-e83a30d3c571 | -13.70383 | -42.39269 | 2026-10-09 04:27:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| edbb0e0e-3ed0-3685-bafe-144e6757cb00 | -9.30136 | -47.4286 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d9ea9076-0bba-3ecb-8518-a902cc99e780 | -10.2926 | -46.61192 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b28b484-c39c-30de-8b32-d68919c942e6 | -8.18636 | -46.35546 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3b98517-cad2-3c43-956b-bead0d58490a | -11.20134 | -45.31507 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 403e4882-5feb-3119-9d9e-15fa09a6aae5 | -5.85298 | -53.45292 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e23bb5b-55b1-3fec-8ddf-5c55dadee473 | -11.05239 | -44.04969 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 61b380c5-78ba-3603-9777-c199ecd16b9f | -12.02711 | -43.47273 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0103949f-1a57-3b30-a7ce-b5a8fbe56269 | -7.81629 | -50.21777 | 2026-10-09 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc308e4d-f9cb-33c7-9103-4acea66651a6 | -9.01932 | -44.37721 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 505eddb4-b89f-37cf-be6c-a3aaf9a039f5 | -12.22082 | -44.82222 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0e581f4-aeb9-397b-89b9-3ae97b29c6e0 | -13.15598 | -54.33781 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f940e7f-d8f4-3fad-9451-14c9b60e500c | -7.38162 | -55.21984 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 960153b1-bf51-3f41-a924-86d5806e4dde | -11.08771 | -44.06387 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b594d0f0-38c1-3887-a0f5-c19db0e0455d | -9.58439 | -46.83694 | 2026-10-09 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ca6e58c-18d9-3f3d-9713-324f32688607 | -6.50973 | -55.40312 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0101308f-efca-3a4b-ae62-80da03c35ddc | -6.14186 | -52.89997 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1bd7ac5-9863-3802-b15e-f89a2d070111 | -7.50337 | -54.99897 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eab3f35c-1970-3c5c-b101-320a5001ba9a | -13.1884 | -48.13772 | 2026-10-09 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5defc437-1d5d-3439-9c9c-6f28bdf99fc8 | -8.737 | -45.15402 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5c16f8e-2a8e-387c-9f2b-cf7eec31130d | -11.75749 | -44.95303 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26ec9111-e87f-3ecc-8a71-f731772b0ab4 | -13.20418 | -54.37641 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bb395fb4-cddd-355d-ae77-bca6a7556081 | -6.44315 | -55.04642 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af3eb5ac-7100-32fb-aeae-4f74bc0087b3 | -9.94238 | -43.55463 | 2026-10-09 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38d7bc78-41a6-3cd4-ba56-4b8310ba5b48 | -12.41272 | -54.36228 | 2026-10-09 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 618eb14d-1df3-3c84-9bca-94f628c1a417 | -8.02166 | -43.90672 | 2026-10-09 04:27:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93a28c1c-dede-3b3d-821e-a9035004a6b3 | -8.78971 | -47.58925 | 2026-10-09 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf4925e5-a99a-34a5-8e06-d8b514bb963d | -9.30636 | -47.46146 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a0cf3e8e-f17f-38d2-ba85-f2653e85dd25 | -8.32505 | -45.44685 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bd38a37-6bcd-3696-afdf-24764ad6b142 | -8.06343 | -45.63073 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53dac8be-5d9b-3387-a79d-d32043ca5a60 | -11.06149 | -44.06439 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99c2dbfd-4e3c-37a8-8ae4-8a77d5c1df46 | -12.20308 | -57.13521 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc578e0b-a40a-3e92-9a4b-dfe5cd490c79 | -7.1543 | -48.2393 | 2026-10-09 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aec3766-0945-3917-80d2-0de47e4d1fae | -11.62988 | -43.71455 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2af3a1e-698e-3f63-bbdf-b0d10662740e | -7.82899 | -44.57024 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec1b2670-8ed3-3282-8dc5-28f0cc725be4 | -10.41912 | -48.87634 | 2026-10-09 04:27:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a6180e9-ec15-35cd-9ef5-be15e56f6ae5 | -11.82662 | -43.52522 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b377375-4b2b-3d3b-be52-b09f19469856 | -12.00808 | -43.4692 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d662b5f-579b-3d96-9984-e6e98aa1599b | -13.15955 | -54.34284 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e28a9e99-a35b-31db-9d5d-b4a14bf2a512 | -11.17951 | -45.31943 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c5a5d04-ea64-391e-a24a-b6c094f85960 | -6.1471 | -51.94725 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60d4676c-71e7-3517-ae6d-2efe8eeb79d7 | -5.89402 | -57.72566 | 2026-10-09 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a84d99d6-23e0-38b2-9193-42bf1f928f92 | -11.46667 | -43.38801 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 168f800a-ebd5-31a8-88e8-f3a67e350cc8 | -8.89985 | -44.93359 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b91ccd67-ef6f-3052-a52b-bdfccd8b82ed | -9.29867 | -47.46736 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4fe56f2c-bfa6-3699-afec-f43471e444b0 | -13.16518 | -54.32102 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6e9c07d-6610-3dde-876c-611b4f495a79 | -12.4678 | -41.32093 | 2026-10-09 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c1cd878-c8d4-3f55-8734-34f29263ab9d | -6.48938 | -55.29879 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9bbf1a26-9f52-3059-8b24-570544ce6040 | -8.30328 | -45.72599 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebcf3561-5ed3-3d33-a970-e8f09acb40e2 | -8.7921 | -47.26839 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d4a9985-9618-3464-a9fe-cbc9f3649285 | -12.20404 | -57.10109 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22daa0c1-5039-391d-9087-ac368dfcae28 | -11.20888 | -44.86762 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92f22f86-b8d9-3b59-a851-af3d923bf4ed | -12.36342 | -46.5632 | 2026-10-09 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71867a24-be26-34fe-bab5-57586827d3e7 | -11.73933 | -44.95066 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2888771a-a25f-3851-a22c-253ecbbad1b4 | -8.96599 | -45.16977 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f963ef98-de9b-390c-8b1f-2cdf0b264eeb | -13.52859 | -44.39682 | 2026-10-09 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ece2b901-f333-30b6-9016-cc190025034b | -12.09985 | -57.15749 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac2dd45f-7dfa-3e6e-8e58-d142582ff391 | -9.72453 | -46.94453 | 2026-10-09 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de4f78b1-5633-35db-8588-b2c54cf73e91 | -11.01991 | -45.42905 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7ea66ec0-e9b0-3e94-a3cb-24e69ea0742d | -6.42648 | -55.20114 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23a271b0-0b82-3228-8d6b-267a5b7ed463 | -10.98209 | -47.79961 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ed8c215-e9a1-3de0-8a9f-63885d5f3a87 | -8.06567 | -45.63837 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9837e139-8e17-3a19-8194-37ef63dc1369 | -11.76455 | -44.95393 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c15e8da2-ab1a-3af4-b876-ea50f1b345a2 | -12.27858 | -48.14744 | 2026-10-09 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75febdca-32e6-363c-a1f0-88b0298a59d5 | -13.34951 | -43.96598 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7417b85-9279-37b2-becf-65698b8fe925 | -8.9659 | -45.12411 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6023ede4-d4a9-3ead-a45f-64274292d98b | -9.40125 | -48.99762 | 2026-10-09 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b1cc6f5-42a5-3b50-9b20-cdaa781009f8 | -8.90719 | -45.23663 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18ccd01b-5f68-3ff9-9a92-45254c36b30c | -8.90767 | -45.21021 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ded5993e-c911-3ae3-98ce-8f360a0a4093 | -10.88266 | -44.79734 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 186de90b-edf9-3f99-8993-6572457ef165 | -5.94782 | -55.34042 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 283be6d0-455c-3e30-8ecb-de6b6f99ade3 | -7.91828 | -46.81019 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10561a62-222a-31e2-a363-7f6beb61eb87 | -6.44929 | -55.04136 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5703880f-d3e3-3d66-9c46-e9d2e3112724 | -9.79311 | -44.77342 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70366416-fa0a-33cc-bfc9-52d765388afa | -11.21007 | -44.8596 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README113.md)
