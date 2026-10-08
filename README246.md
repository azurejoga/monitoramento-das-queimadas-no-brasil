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

## Dados Diários - Página 246

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5864549d-63d0-37b4-9ae0-8984071758ba | -7.09151 | -45.31939 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6b25482-043e-344a-85cf-9f839a3467c4 | -6.69673 | -45.29259 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 95a1107d-d0f4-3a1d-bb68-b60a87b26cef | -8.94549 | -45.16976 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1656e943-89c0-3ab7-9f4b-b3635812a7dc | -5.47325 | -41.22049 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| e3dd993d-f112-3f81-86de-a316e58bbdd2 | -5.15989 | -42.73172 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0cf6c671-3fbe-3edf-b8aa-004ad9e81b9d | -5.77799 | -42.06448 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a6242714-a69e-30af-a61a-fe1af28f225a | -5.41601 | -45.86768 | 2026-10-08 15:41:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 80bb4fc9-6a23-3b48-8b7b-58dc4c74ba49 | -7.10378 | -42.52853 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c67b6b39-8508-379e-9a8d-e0b13fec32e8 | -7.73403 | -40.56803 | 2026-10-08 15:41:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 69102527-66ef-3ded-adad-02a6dd56ff79 | -5.3902 | -42.96462 | 2026-10-08 15:41:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 8b278cbd-7558-394f-823b-76ce7096fb33 | -5.70353 | -41.72846 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 2a70d7d8-245a-335d-b0c3-64f74d58a5ce | -6.5314 | -45.3899 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b2d4537e-9fe7-3785-b510-cf54e8bbd87f | -6.66775 | -45.37159 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 0f425691-6705-3d18-aeba-168789f12020 | -7.00657 | -43.67813 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 26b84728-8ae6-3e6c-b715-9f80e2eaed0a | -7.78913 | -44.57663 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90c9b860-2b11-353a-bbef-9159d699e0a2 | -5.35956 | -43.07254 | 2026-10-08 15:41:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 269932fa-c8b6-3319-8c60-ee9d18601da8 | -9.43675 | -41.7345 | 2026-10-08 15:41:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 797d9eb2-c580-3c82-aa52-9d5bf98059b8 | -6.72674 | -45.17609 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0011be7d-3b93-334c-bc77-9a6cc8525503 | -6.1608 | -39.44159 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1de3e699-7a89-3def-b55b-4d37eb2575d2 | -7.10968 | -42.53122 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 79eaad87-4539-3131-9185-ef9726a41b20 | -8.9382 | -45.16491 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| f445eaa2-e405-3b83-b3d6-63ab8200e042 | -7.14288 | -45.3586 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0bfd94ed-c6aa-3f61-96b0-6568dd143dd2 | -11.26656 | -45.18904 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c4732baa-6d60-3c86-b9d3-e03f5b01e653 | -6.79165 | -45.06189 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| b77aef48-c095-3d2b-b9a8-6780fe9c4a32 | -9.89977 | -44.81747 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 966b94e8-8b60-3e32-88d3-157e6dd3b940 | -5.48415 | -44.60199 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bddc4b4e-ef9e-330e-9c30-eda124d0c959 | -7.18049 | -44.32463 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1ee117c0-7d54-3778-81a2-d6da75ed2f0c | -6.10972 | -38.16782 | 2026-10-08 15:41:00 | NOAA-21 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| cda9cad5-236a-3dfb-982e-342efd4aca23 | -7.06313 | -40.94818 | 2026-10-08 15:41:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 4639cdaf-81eb-35d8-b2dd-415fc6bfb584 | -5.69934 | -41.73501 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c6cc0649-921f-3d15-b5c1-4f9cf468b5c7 | -8.36386 | -44.7667 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fb444160-554e-3728-88a5-ff06f5970613 | -9.32863 | -38.09345 | 2026-10-08 15:41:00 | NOAA-21 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2115be2a-fc81-3f18-9b85-7966df410550 | -6.36661 | -45.59738 | 2026-10-08 15:41:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2675a859-701c-3346-956b-095a4cd9d7f7 | -8.84773 | -45.44778 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7977c5a5-53ea-3f51-81cb-c943c4ed7bbb | -5.72252 | -41.64621 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| 43597dfb-8b73-33a9-87af-35e39172ec66 | -5.73519 | -41.77537 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f010a8fe-8a39-36f2-8036-24fc624773bc | -9.93909 | -43.56338 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 06d227ec-0865-3c5f-8255-f9d87ab80c36 | -7.1092 | -42.52775 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f68f67a3-b24c-331e-b45f-c9102e1c7a0d | -5.88273 | -45.98026 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 95ef8368-3a32-3336-935d-e6db317e8d19 | -9.44913 | -38.0921 | 2026-10-08 15:41:00 | NOAA-21 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 65105792-318e-33c5-ae74-2ae8bb2ee0f5 | -7.48381 | -42.79607 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a6f94a7b-e2ee-3702-88c0-8bdc8e6013d6 | -5.63038 | -45.79284 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2bce7014-79ab-3531-9466-4cab862f4169 | -9.07447 | -42.62814 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f7665f54-5021-3b8f-9f9e-655a37e5b401 | -8.58236 | -45.69369 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 44f05bf8-1f26-3645-a03e-7fb67270a4a3 | -7.9996 | -39.03315 | 2026-10-08 15:41:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| af2b9678-40c1-329b-b68d-ccd32b2e1a0e | -7.76786 | -44.17348 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1f9b19ad-cfde-3b0f-94bc-cc2ab4c7fb1d | -7.7053 | -44.7479 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4ead74bb-578e-35e6-82cb-cd8da4a9a9ba | -7.0893 | -43.08896 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 819c846e-b8fa-3f24-9f31-aeaf83d46807 | -7.08128 | -35.03594 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 42b9fad2-db37-3884-bd89-afe0aa7f1cd6 | -6.96907 | -43.89325 | 2026-10-08 15:41:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e959559-f855-3d01-9427-5dba70347aba | -10.58707 | -41.20174 | 2026-10-08 15:41:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 6ad2f8d5-9175-3d3b-91c6-72f0d6c3aae7 | -9.94572 | -43.549 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8fbe0816-85c4-3db2-805b-6159ae420a27 | -6.59018 | -44.86052 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f76ba72b-1032-3fb7-bfb4-8861fb2925ef | -5.72752 | -41.64543 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| faefc968-6d32-3184-945e-69418459029c | -5.71025 | -41.73944 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 31694298-16aa-36f1-8203-128e0d562e68 | -7.26754 | -45.34929 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4c75f02c-0e6a-3159-a000-d4ea355a7c86 | -6.02 | -42.71377 | 2026-10-08 15:41:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 271abe2b-c1d9-328d-9708-893c333495ae | -8.06544 | -38.03027 | 2026-10-08 15:41:00 | NOAA-21 | CALUMBI | PERNAMBUCO | Brasil | 2603405 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 40c5fc5d-7644-30ea-b47c-556a4a530c93 | -6.69025 | -45.29315 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 39465738-0542-32b6-a0f8-5321a13fd5ba | -6.67094 | -45.35133 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a1cded04-a525-3ca5-9cc7-ed66f8073d9b | -5.97254 | -40.91078 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 1e0ea351-dd9f-3da4-addc-77715cb7183a | -11.10957 | -45.67582 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| fe1e2b90-9a84-307f-9f43-64b7a0e1a689 | -6.86517 | -41.77369 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 76141429-0fd9-3352-b683-465c816fba9e | -6.89619 | -45.8944 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ef895a9d-7519-3cf0-a4fd-918cb413fd43 | -5.0818 | -43.05734 | 2026-10-08 15:41:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b26075f2-3db5-35a8-8155-0a8a2a8f32ea | -6.93505 | -43.6746 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8794d7b2-ab8e-3ca8-ade9-eba99f45d258 | -7.47775 | -42.79295 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ada5a51b-2986-3dd4-9360-2ea5fce8ecc3 | -9.43144 | -41.73521 | 2026-10-08 15:41:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 10faec70-f524-3f19-944d-ff4902f78bcc | -7.47315 | -42.83954 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| fadc8efa-9006-38dc-84f0-90279c368651 | -11.13437 | -46.13816 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 7376348d-6eb4-38a6-a159-f93c9eb5e536 | -4.92062 | -40.3649 | 2026-10-08 15:41:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9681a7c4-ef94-32a9-ba61-f54b10e2be50 | -6.05611 | -42.59709 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 19def4c4-5a60-3080-9d57-a66bbb329faa | -5.71872 | -41.65564 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 724e4d92-783f-325c-9414-5721b86eab2f | -6.32446 | -35.13027 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 0fd1f04b-da29-32fa-b6d5-a13d0e33a4ec | -5.43099 | -46.63931 | 2026-10-08 15:41:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 82692538-309c-3683-ae83-ad0944ba3cb9 | -7.39214 | -45.64367 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 764fe354-4194-3840-8def-49f75a8423b5 | -5.73438 | -39.64631 | 2026-10-08 15:41:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e00e6885-4812-3000-997d-f0b96ed14c62 | -10.16545 | -44.66669 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e8780d43-778b-3255-acc5-37c07c4cac06 | -8.20849 | -46.41016 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 386.6 |
| 57e8fa4c-de72-3f4a-9efd-d6ea2ae1b8f2 | -5.99666 | -37.38286 | 2026-10-08 15:41:00 | NOAA-21 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 49614b63-9eb1-3baa-9bcc-0534c60b0799 | -5.38824 | -44.19133 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 1a63db03-b77d-3e0b-acbc-959f4e9927fc | -9.34575 | -45.42376 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 8b98b182-e26a-3425-b9f0-d83c5fa16ffc | -6.15049 | -39.44622 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.7 |
| faa7ff61-e25f-3a41-9019-771940f55927 | -7.53793 | -45.87574 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 319fa137-1045-3312-8eb5-4a06b2636ac0 | -11.23764 | -44.84634 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 107c1f80-ccdb-346e-94f3-e6319ee69062 | -5.72829 | -45.14951 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b3e9c8b9-c273-37d1-a04d-0e6de7511b02 | -7.04769 | -45.43963 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e5294be3-15ed-3ede-9022-157cfcfb730e | -8.20509 | -46.3829 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f7ad2672-8ffb-3072-8238-1fb4d22580ab | -10.93612 | -45.38369 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fcdbc101-aa7b-3cf7-9f5f-c73d0e46ab63 | -5.72896 | -45.15441 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0f919fc8-8965-3b4d-a9ff-d86ee0a62474 | -5.99288 | -37.38341 | 2026-10-08 15:41:00 | NOAA-21 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 4f226f00-dd78-3b46-82d1-672ad3dc51bc | -6.31752 | -35.15393 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c478b8d5-f936-389e-8cc7-d748de8a98c4 | -6.56832 | -44.11137 | 2026-10-08 15:41:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 415cc607-844e-3a23-9140-82d83e86d7b0 | -6.84842 | -41.76599 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f5a1790a-8d6e-3e09-bdb7-0583b9f5101a | -6.7282 | -45.18681 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 695c7e8b-a9da-3719-b34f-cd2b30c97db5 | -8.21465 | -46.40251 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 182cf5e3-6848-3e6b-9120-5ee36bc6af30 | -7.39453 | -44.47968 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 258eabc5-3913-39f5-8f38-8486b283aa0d | -6.3216 | -35.13447 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| decb0b0c-ed22-3a06-9e7c-1ba936dd8739 | -6.14676 | -43.3805 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5861f8f7-7fb6-3cd6-926a-5c1e0182a53e | -5.70521 | -41.74011 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |


[Clique aqui para ver as próximas entradas](README247.md)
