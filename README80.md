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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a642528f-a5c0-31a6-8b7b-e4e327688c76 | -11.3549 | -50.4447 | 2025-09-09 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 0b06af8e-2e69-3107-9d0b-e61018a6b7dd | -5.6738 | -43.9 | 2025-09-09 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c97e58a7-4212-3f79-9190-da6ee333d924 | -5.589 | -42.9048 | 2025-09-09 13:50:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 407.6 |
| c0eb0e7b-aede-3828-ba48-f6b11089542b | -11.3389 | -46.5419 | 2025-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| a0151ee9-8f98-35d1-9023-f51e86482704 | -11.1061 | -51.9958 | 2025-09-09 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7f015a14-bbdb-3165-9d82-c66d387f9a93 | -11.4322 | -50.3504 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 96d302a0-ae45-3a62-8cb8-c909fd597531 | -11.9551 | -50.9743 | 2025-09-09 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| d2d85fc0-ffd7-3879-baf6-ddac1761dd31 | -11.9739 | -50.9935 | 2025-09-09 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 04d4559d-7000-38a5-add5-fd5b7291ccaf | -14.432 | -52.9619 | 2025-09-09 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| fd28ca58-47f7-33b4-bf67-46272c2fd657 | -11.4482 | -49.2704 | 2025-09-09 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| b823a9ce-8f0b-3ee3-ac70-62e097de88ad | -11.4465 | -43.6224 | 2025-09-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| dfbbe133-472a-3947-b1db-3175c34d96a1 | -8.3929 | -49.1101 | 2025-09-09 13:50:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9d38c8ca-adb5-377c-a773-e701c52a1774 | -17.2967 | -46.7032 | 2025-09-09 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 3d8fcfa3-a794-3a26-b70a-6e49c95620e7 | -11.4469 | -43.5988 | 2025-09-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| e002266a-6cac-3904-b45c-4abdab643263 | -5.4587 | -42.797 | 2025-09-09 13:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 9a2dd2e0-e0ba-34bc-a021-883f25795731 | -11.4272 | -43.6254 | 2025-09-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 7d5239e0-0df6-31bf-802c-5abb708d056e | -5.0438 | -43.1314 | 2025-09-09 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 86bd14e3-6731-3120-9225-86d88d040da2 | -15.7388 | -53.5295 | 2025-09-09 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 21258db6-5d8c-3c6d-93b3-760cf2e264fa | -12.529 | -45.2756 | 2025-09-09 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| a0844e58-e78f-3813-adfe-19594ebce142 | -14.4664 | -53.2099 | 2025-09-09 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 40a290af-738d-3565-8547-10bf9469dd3a | -6.2407 | -43.4144 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| eff7eb77-2a86-3865-b15e-9164391f3148 | -5.4343 | -43.4538 | 2025-09-09 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 386.4 |
| e8555b9e-4105-3951-955b-a6b832d24f73 | -6.199 | -45.8186 | 2025-09-09 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 2e67c105-85a9-350d-a1b7-b8f77755a2f6 | -11.446 | -43.6461 | 2025-09-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 460d789b-de2b-3014-a57f-98b90ee9e02c | -9.4435 | -60.5307 | 2025-09-09 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 7bd0cdce-2fe9-3d06-a1b5-2aafd404546d | -11.2196 | -54.9975 | 2025-09-09 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 99f5b19a-8b83-32ed-be73-ced130ea1b09 | -6.527 | -44.7974 | 2025-09-09 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e6c6d91a-1cfd-371c-bb9b-dd113012f067 | -11.3014 | -46.5018 | 2025-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 349.9 |
| 5e6eef39-7164-3dfa-b2d7-16da636260c0 | -9.7206 | -46.8302 | 2025-09-09 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| ac754798-cff2-3db5-84bf-5c4fef3dd5ce | -11.4281 | -43.578 | 2025-09-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| cf674697-2932-36c2-9c92-e0f71dbdc712 | -5.453 | -43.4525 | 2025-09-09 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 227.8 |
| b68fb9df-6afe-3308-9050-7ede9eb61362 | -12.1991 | -53.8817 | 2025-09-09 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 428.7 |
| 9dff9bf0-8420-3dd6-ad04-1c7f28bd504f | -18.6904 | -52.594 | 2025-09-09 13:50:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 4de54ab6-1b2b-3fec-b319-ab30c73447c7 | -5.6738 | -43.9 | 2025-09-09 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 25dc84b1-af24-3cfd-aa76-d6d44e4be5c2 | -11.3172 | -50.4275 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 1e2205eb-b099-305a-8ecb-cfc929783f5c | -19.9545 | -49.2928 | 2025-09-09 13:50:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.5 |
| 128f1d5d-6f10-3696-aefb-b1e73e878ac7 | -12.1988 | -53.9024 | 2025-09-09 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 286.7 |
| 04a789a9-cbc2-3aa2-9661-7350038c76b3 | -17.5799 | -49.8019 | 2025-09-09 13:50:00 | GOES-19 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4750299e-542c-3e17-866c-f3c55c53c422 | -4.7345 | -44.4685 | 2025-09-09 13:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9d831b93-7f6c-32f0-862f-82e8da4fcc77 | -9.7017 | -46.8323 | 2025-09-09 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 92a3adf9-8ad9-31d3-83ed-667106e9ae59 | -5.8218 | -44.0965 | 2025-09-09 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 58d9576d-0b78-3ccf-ad88-01ff206db90b | -8.4116 | -49.1085 | 2025-09-09 13:50:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 213.8 |
| fd8d45e2-21d9-3077-b1ea-c3453d89b321 | -5.3482 | -44.7943 | 2025-09-09 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| bb471a9c-fbd2-3f69-9e45-9a718c33a78c | -12.5093 | -45.3017 | 2025-09-09 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d37576f6-58a7-3cdb-ac3d-26dde3061a91 | -11.3552 | -50.4233 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| fe590a17-e3e7-3ce4-8958-d7482407f1cb | -11.9726 | -51.0788 | 2025-09-09 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 0569e77e-d135-3b84-bff6-84ed9adbd29e | -12.6343 | -56.9725 | 2025-09-09 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| ca61cd65-18c9-397f-b7b6-d1b8a2989e16 | -9.8076 | -46.0345 | 2025-09-09 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ac6c996b-0d7c-3eb4-a819-d51d1fa10f53 | -17.2762 | -46.7305 | 2025-09-09 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b02e1877-fe3e-343b-9fce-1b2e131805e2 | -7.7888 | -46.1116 | 2025-09-09 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f3f98ed6-f0c2-3576-8007-751791905c39 | -22.1499 | -47.6954 | 2025-09-09 13:50:00 | GOES-19 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 2fae04d2-e277-31f9-9fd9-17d12ace2e59 | -4.7346 | -44.4457 | 2025-09-09 13:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 1bdafa21-b503-391a-85a1-1202f16563a8 | -5.5506 | -45.1664 | 2025-09-09 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ea81281b-3453-39e1-8bde-a634bc6d5928 | -11.2823 | -46.5043 | 2025-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 44497782-0055-3604-98ba-eb9c7faad32d | -5.4585 | -42.8206 | 2025-09-09 13:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| cb06e4a6-61ae-34a2-aa0e-bbaec144fca4 | -14.2932 | -45.0261 | 2025-09-09 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| bf99d301-4756-39e7-a784-cc14bbfea2f1 | -15.8205 | -52.2444 | 2025-09-09 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 168.0 |
| f44d97e7-83f5-3e84-b782-d980bb75d86c | -11.3549 | -50.4447 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 03250f2d-041d-3558-8095-52d6cd108d43 | -6.2224 | -43.3693 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 17d7bb6e-3b55-3bc3-b470-eeb3dbf70163 | -5.8582 | -44.2088 | 2025-09-09 13:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| b5151bdb-379d-3f7a-8161-e99c39a9d20f | -13.1367 | -54.9171 | 2025-09-09 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| ed7c2fe0-e237-360d-9060-2c3cdb42f717 | -5.5504 | -45.1891 | 2025-09-09 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 14cc534d-b7b7-3037-b31a-54006c909f99 | -11.3011 | -46.5244 | 2025-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 381.9 |
| edebf456-02f3-3511-be1a-e22905e75796 | -8.0606 | -48.6423 | 2025-09-09 13:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 2d2eb217-d46c-33a7-a272-39b072e3e993 | -11.9923 | -51.034 | 2025-09-09 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8bf0b131-65ca-3612-ac81-a1bba798a509 | -9.4623 | -60.5104 | 2025-09-09 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 95ca45af-df6a-3131-b55f-49f46d1288e3 | -7.789 | -46.0891 | 2025-09-09 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 3b0bf2d9-0233-3014-8dfc-d156b4deff68 | -7.5611 | -44.6597 | 2025-09-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d12694db-f170-34bb-ac40-6576a7384ce0 | -12.2178 | -53.9005 | 2025-09-09 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3b457114-4fdf-3402-b8b1-307e7186a527 | -8.4612 | -51.4595 | 2025-09-09 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ba1ec012-b1e0-3278-8711-d9285e268988 | -11.2007 | -54.9992 | 2025-09-09 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 07d0770b-cee6-33f6-a572-f65d598f1289 | -9.1914 | -59.3843 | 2025-09-09 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 676256a0-b8c1-3406-aa2d-88f8db05c33f | -6.2226 | -43.3459 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 7b51e247-801c-36a1-ad51-bd0b898b5af8 | -12.1993 | -53.8611 | 2025-09-09 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 1a86ddeb-8895-337f-aee9-18579039c608 | -8.4514 | -47.2952 | 2025-09-09 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f2b3e97d-127c-3582-88f6-aa308dd4e637 | -6.9134 | -45.5142 | 2025-09-09 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 99170f8c-2581-3d04-a601-8744b34ddc24 | -9.4621 | -60.5297 | 2025-09-09 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 29b632ed-cc19-3dc0-a2c3-a107b572954b | -11.4672 | -49.2681 | 2025-09-09 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 5302aeba-4805-371a-a210-1a1ca51b0003 | -16.3602 | -43.0349 | 2025-09-09 13:50:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 62307f19-b394-38c6-a5bc-d37e87a8f2f4 | -10.0993 | -48.1595 | 2025-09-09 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fb6d5443-edc7-37bc-9ef7-4e5b1cbac0c2 | -6.3467 | -44.0782 | 2025-09-09 13:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 18df3ad9-9357-33f5-a841-6e244f35e697 | -11.282 | -46.5269 | 2025-09-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 42b4ac06-92ec-3820-98a7-069738192e7c | -12.18 | -53.8836 | 2025-09-09 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 79a8c929-0f92-37ca-b9b8-f04f49acc824 | -12.5286 | -45.2987 | 2025-09-09 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 44bcd569-8e4e-3d96-a665-b8c985c94455 | -5.8397 | -44.1872 | 2025-09-09 13:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| e61886d9-bd66-302f-9b54-90596d7176cb | -12.0291 | -51.1149 | 2025-09-09 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 165.3 |
| d277aed2-8fb4-3588-bcff-592605e63351 | -12.5098 | -45.2786 | 2025-09-09 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| a63a80ef-fe0d-37d3-975d-7b78935a9761 | -9.2181 | -60.8305 | 2025-09-09 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 43b6840a-99c2-3d26-b04d-7d59c9199e0b | -12.6153 | -56.9742 | 2025-09-09 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 53cd4ddc-f56e-389c-a2d9-3fea72221a43 | -15.7194 | -53.5321 | 2025-09-09 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f1d75a1a-f8ad-34aa-9055-3abda04d987b | -8.4119 | -49.0869 | 2025-09-09 13:50:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| f79d48c5-4a0f-30f5-8057-3af72beddb0f | -5.8395 | -44.2103 | 2025-09-09 13:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 291.6 |
| b71cb582-506d-3423-95cb-ec0c289acf62 | -7.5799 | -44.6579 | 2025-09-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 196e71bb-216d-3174-935a-2b210fd21169 | -14.4471 | -53.2124 | 2025-09-09 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| aad1b6d8-e7fa-3596-b67f-0ce206ae5f06 | -11.4277 | -43.6017 | 2025-09-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 87af9db8-44b0-3440-9dc0-178d8602c103 | -11.9926 | -51.0126 | 2025-09-09 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| e920aded-9547-366e-abb8-4f7f42a6612f | -15.1044 | -48.0659 | 2025-09-09 13:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9d3611ea-c35e-38a3-8863-3ec4e9d528fa | -9.4436 | -60.5114 | 2025-09-09 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 328.1 |
| 87d59200-b125-3df8-9410-7a2169b96d2d | -5.975 | -45.7901 | 2025-09-09 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d8516f96-f9d7-3691-95f3-51a70d957e1b | -17.7127 | -44.4684 | 2025-09-09 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 151.3 |


[Clique aqui para ver as próximas entradas](README81.md)
