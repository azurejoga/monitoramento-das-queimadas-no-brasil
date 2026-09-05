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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fadd400-14e4-3b2f-a837-aff6eedc5a0a | -1.1811 | -53.834301 | 2026-09-05 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66c0b9a4-1ac4-3c72-813b-236e2fbea8db | -4.1629 | -49.708302 | 2026-09-05 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac1acd9-0d70-370a-929f-2b7128592b3e | -5.772 | -45.064301 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba94972-f2ba-3ed4-9a51-52aff0a429f4 | -17.5772 | -44.969601 | 2026-09-05 00:31:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c3dd4436-1342-317d-9db1-b5ad334454ab | -21.008499 | -43.153099 | 2026-09-05 00:31:00 | METOP-C | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a897118a-afbf-3624-acbf-17fb8660e956 | -13.3274 | -44.037601 | 2026-09-05 00:31:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5324d39-9ef3-310b-b74b-492e00cc616d | -6.5615 | -44.7757 | 2026-09-05 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d090dfc-6f47-395f-8a2c-4ce874b2a2bb | -19.262501 | -46.875702 | 2026-09-05 00:31:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 50cc52aa-aea4-35e1-a0ac-2f87e8718868 | -1.1756 | -53.810299 | 2026-09-05 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d435fb5-8093-3de2-8b6f-050d2748391f | -2.7605 | -49.473598 | 2026-09-05 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db28689e-8c8f-36c3-bae4-079aa0c63568 | -18.8985 | -47.046299 | 2026-09-05 00:31:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf30348d-e5cb-37a1-9808-7cbb92add880 | -3.5838 | -51.474899 | 2026-09-05 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe49b290-afe9-3262-b68c-9dc95b819c52 | -11.8627 | -42.544498 | 2026-09-05 00:31:00 | METOP-C | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8b32e7bf-8068-351f-a1ca-25093eb23bab | -3.4406 | -52.804001 | 2026-09-05 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02da5799-b354-3b79-8a2a-94e4520567aa | -4.2756 | -54.7658 | 2026-09-05 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604d56f8-a785-3119-9686-18cab44c452c | -19.818501 | -49.611401 | 2026-09-05 00:31:00 | METOP-C | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14d2490a-2b2a-39c1-a09b-658188404b52 | -4.1611 | -49.7006 | 2026-09-05 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e50b0a4-1a63-37c6-a202-2cf5820a9471 | -20.9897 | -45.8139 | 2026-09-05 00:31:00 | METOP-C | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 272f4f82-cfa7-3dd9-88fb-dbc33eca96be | -2.453 | -47.5849 | 2026-09-05 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 851fb653-f715-3823-b0a7-3aa01907d954 | -13.4426 | -43.820599 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1164c47e-c1d1-3dfc-8206-f011bf847aca | -13.4328 | -43.823002 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18822ae5-e279-3d52-88ea-ba3e192c1833 | -7.6974 | -44.334202 | 2026-09-05 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46c867ff-3602-3df6-8329-ecc3ba778634 | -6.127 | -43.7551 | 2026-09-05 00:31:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f1e3b25-e380-34e0-8762-42ce40b021a1 | -13.5674 | -44.0938 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38df0ef6-8997-373d-9498-a67c5d8c0015 | -5.7622 | -45.066601 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c68c2c4a-a35f-38b0-aa6e-f43af2912924 | -6.2271 | -38.895802 | 2026-09-05 00:31:00 | METOP-C | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a2934368-d126-3601-919e-3d9e903b4140 | -13.674 | -42.510601 | 2026-09-05 00:31:00 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 287d8664-306f-381e-8956-7d9e9b5d5c4c | -20.7369 | -47.145901 | 2026-09-05 00:31:00 | METOP-C | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e161da48-375c-37f2-842d-2acb76dc42d7 | -10.4732 | -46.0406 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd5d5afc-352b-3b98-984d-aef4cd609a24 | -2.8069 | -48.681999 | 2026-09-05 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 123c9dae-c30a-3697-9394-73fff31074b8 | -9.1226 | -44.292198 | 2026-09-05 00:31:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dedf2715-9057-362a-9d3f-e6183dcb37c0 | -5.7753 | -45.0788 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3386d120-4c3e-33cc-bb1a-14b65f91768a | -13.6759 | -42.518501 | 2026-09-05 00:31:00 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 094c8768-7183-38ff-9af4-e864a94a87de | -10.7812 | -44.455002 | 2026-09-05 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be768a7c-50a9-3ea6-9935-855882856c76 | -2.8053 | -48.674999 | 2026-09-05 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 419dc096-825b-3e50-bfc5-65133d6290c0 | -7.7071 | -44.331902 | 2026-09-05 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd57124-1fbd-3c2c-9eff-0a71f09f2f02 | -19.8064 | -49.601101 | 2026-09-05 00:31:00 | METOP-C | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd99e413-24ec-35de-a6ba-c1e57770f859 | -13.4312 | -43.815701 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 456de26c-f840-3d2b-a5be-5993dbccb6e2 | -1.8407 | -47.928799 | 2026-09-05 00:31:00 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8887a50-0bb9-3ee7-8a29-54e0d1eb6a04 | -10.7829 | -44.4622 | 2026-09-05 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ba58e0b-c8a8-33fc-8604-53f52a6184e2 | -2.82 | -46.712601 | 2026-09-05 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a698fe80-cf70-3c98-9355-1769efdd2b3a | -10.4587 | -46.021999 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97c8e24a-b9fd-3033-bf40-ddb716fa56b9 | -20.8253 | -46.312698 | 2026-09-05 00:31:00 | METOP-C | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f2d91945-9535-3cc9-ae0a-16fe519df27e | -15.0682 | -52.5434 | 2026-09-05 00:31:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea7356d6-4fe1-3142-b2b0-62aebcd69c9e | -15.0748 | -52.525299 | 2026-09-05 00:31:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f214facf-ba07-36a1-834e-75e7d3c1b045 | -19.250999 | -46.869202 | 2026-09-05 00:31:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f2e66f4-e209-360c-a24f-3d3cc8f0bd98 | -19.811001 | -49.625801 | 2026-09-05 00:31:00 | METOP-C | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 111c1db4-6d5d-3ad0-af17-8e94854078ec | -10.4571 | -46.015099 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b5c72f1-6e1a-366a-a7d8-63b332052d41 | -13.316 | -44.0327 | 2026-09-05 00:31:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5712718-f129-36ad-9d3a-da67281a175b | -3.2264 | -50.573898 | 2026-09-05 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 691911fd-94e9-3e20-9f2e-ba68979564b5 | -4.279 | -54.781502 | 2026-09-05 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60bd78d7-d3a0-3b91-9b01-e013cff8d30a | -13.4443 | -43.8279 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe13f15-63c1-3d8a-a2de-bef6835f266c | -7.3501 | -45.462299 | 2026-09-05 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a304fc9d-df9f-3fa1-ac82-2560d06a84b9 | -13.4362 | -43.837399 | 2026-09-05 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7fb6a18-60e9-3f0e-9666-0dbc38dd50c1 | -5.4959 | -45.119598 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96454528-625c-36cc-8aa0-8d214aa61189 | -19.8162 | -49.599098 | 2026-09-05 00:31:00 | METOP-C | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b69f2a04-a41d-3cf0-9a31-422c948fff99 | -11.8108 | -44.803902 | 2026-09-05 00:31:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0c6e713-c77c-3913-9c0c-d46567780e70 | -4.6599 | -55.635399 | 2026-09-05 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b50faf9f-e823-37ec-9177-546557d68c80 | -7.1319 | -42.243999 | 2026-09-05 00:31:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 534012e7-0153-3397-9d9a-2fdc917d4736 | -12.9333 | -42.438599 | 2026-09-05 00:31:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5592d18f-a25a-3bd7-ac27-5c2e0c822691 | -15.0651 | -52.527199 | 2026-09-05 00:31:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 288b79ee-edd4-309a-80d1-24651cbe4313 | -6.3561 | -46.1194 | 2026-09-05 00:31:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2627bd9c-7b30-344d-b0ef-1e668fc7b4af | -13.569 | -44.100899 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6470514c-1091-34c8-b678-72e8a6965a65 | -12.9295 | -42.422501 | 2026-09-05 00:31:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 45db4795-ebd6-3fe8-9722-2ccdd933ceca | -6.1185 | -44.690201 | 2026-09-05 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d30a76f-482a-3ec8-b761-02e2d938bb7a | -9.6146 | -48.5606 | 2026-09-05 00:31:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a43b6ce-1663-3253-935b-937debe7efc5 | -10.4845 | -46.0453 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27e999c2-f1fa-31c5-ba13-a65ca4670ecf | -3.7874 | -55.878601 | 2026-09-05 00:31:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca158bd5-5209-3d44-bb2e-8737840df495 | 2.3761 | -50.7649 | 2026-09-05 00:31:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 62b244ae-277e-38c1-b012-b31176eebaff | -19.835199 | -42.703098 | 2026-09-05 00:31:00 | METOP-C | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83236a3b-7597-3d0f-9f4c-7d7af50742f9 | -1.1784 | -53.8223 | 2026-09-05 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2a1a10-f22d-3c56-8b9e-864c4a37f92e | -20.256901 | -46.334599 | 2026-09-05 00:31:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d4210335-7474-38b7-abc0-1e5b5ad890ce | -4.1531 | -49.710499 | 2026-09-05 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2a1e96a-ac4a-3639-b51d-2d184e488eff | -12.4383 | -43.409199 | 2026-09-05 00:31:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 075fa080-eb85-365b-8e72-e41539d55025 | -5.8562 | -52.051601 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd2033f1-6a80-3b59-acd3-f304ef55916a | -12.9217 | -42.432899 | 2026-09-05 00:31:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b21a9f3f-5a97-3e90-bdc7-341c68714eaf | -5.8538 | -52.040798 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47f9dc98-499a-3e7d-bbf1-623c4a655a38 | -4.3647 | -47.7826 | 2026-09-05 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0661646e-f3f1-3d38-a830-8cba1a1d7890 | -18.900299 | -47.054901 | 2026-09-05 00:31:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e53fcc4f-acdc-3eb2-8549-c35ab60e9e2f | -3.4309 | -52.806099 | 2026-09-05 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 329d623b-af31-30ef-89c5-4c56e51411df | -4.1257 | -49.452801 | 2026-09-05 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73f2304d-d944-3cc7-9dcf-964906e13e41 | -7.6763 | -46.073799 | 2026-09-05 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3fa8e25-f486-3e2b-b8ba-ec77e86843fc | -5.9257 | -47.8936 | 2026-09-05 00:31:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb7f4ca0-3473-30bc-b35f-2068492a25e5 | -5.7737 | -45.071602 | 2026-09-05 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a00d9dc2-60f2-3325-a01e-3416f74719e4 | 2.3778 | -50.7575 | 2026-09-05 00:31:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6a72ecef-d70b-34dd-9e4f-cd8990c06e8d | -5.844 | -52.0429 | 2026-09-05 00:31:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b00ec6a-1848-3738-854e-c38ff1f7f28f | -7.6747 | -46.066898 | 2026-09-05 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39b6d29a-f739-3778-a878-720e83cb2863 | -6.2696 | -43.2644 | 2026-09-05 00:31:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ddc9c0b-6c40-3ac8-87d1-c2cf71beee92 | -4.6697 | -55.633301 | 2026-09-05 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1fdeafe-e6ac-370c-a539-f0ec1ee083f4 | -7.3517 | -45.469299 | 2026-09-05 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86a26b7e-002d-392d-be41-84fd0ec0fd13 | -10.483 | -46.038399 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07c70bbe-9230-3d60-97bb-b2cdd2469db0 | -11.8124 | -44.810902 | 2026-09-05 00:31:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 504b6ddf-63e9-3887-b2e0-6534f2e389e1 | -2.7771 | -47.784401 | 2026-09-05 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa827271-dc43-3958-8946-ef8c0c097fcb | -10.4814 | -46.031399 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4abcf5d3-2dcd-3b05-9a77-be6391a61b9e | -12.8494 | -44.382999 | 2026-09-05 00:31:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3f5d027-3e88-32df-9832-00f929c23ea9 | -2.7622 | -49.480999 | 2026-09-05 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74bd4d9b-4f8f-30e8-bfc0-480448b54438 | -10.47 | -46.026699 | 2026-09-05 00:31:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42fc639a-a407-3270-b77d-c92c7a476d89 | -2.7755 | -47.777599 | 2026-09-05 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbfbf5dc-0e16-3604-9fc5-7453f01fe8fa | -12.9236 | -42.441002 | 2026-09-05 00:31:00 | METOP-C | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c6c47fa5-04f2-338e-9bc4-770f7b8d0079 | -4.6657 | -55.615101 | 2026-09-05 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
