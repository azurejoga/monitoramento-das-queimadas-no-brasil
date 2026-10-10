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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d7dcc6c-6c69-397f-8a9f-778491bfbead | -10.82988 | -47.36499 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 902ed5bb-7a75-3c7a-80f1-8b82caf728ba | -10.90008 | -44.79994 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c059dffd-a01b-3881-8823-bea33f34cc5e | -11.96351 | -43.48833 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d38cd53f-0b8d-3274-99fd-b91c06f88e1f | -11.95252 | -43.4721 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3a5b91e-6049-3664-8fc0-ff183d25b08c | -17.10492 | -41.56714 | 2026-10-10 04:10:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 08935fd5-605d-305f-b4e9-fa3edf7d4791 | -11.0272 | -44.02757 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4a70051-43f1-3c14-bc96-54c8e1475792 | -11.95471 | -43.47968 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6609902-b523-3e5e-8068-a0876e04a35c | -11.08787 | -44.11492 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5a422cd-3619-3f8e-a574-0b9d4246e662 | -12.02843 | -43.46685 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e271f8d1-32ff-3505-8a29-7c1686ec7f05 | -11.5955 | -43.7282 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a71de08f-74a5-38f5-b2b1-d3d9d15ba308 | -12.56457 | -44.87698 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eacd68d0-5bc6-383e-b3b1-66e74c8a3326 | -10.45288 | -47.84538 | 2026-10-10 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b02074e-222f-3a43-b0ab-6d1e894c9cd8 | -10.49481 | -51.94401 | 2026-10-10 04:10:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91604d9d-d207-32cf-80cf-6c67aa958416 | -10.24741 | -49.66488 | 2026-10-10 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6dfb8f8-8cc5-33a0-906e-134cf6beb0b8 | -12.23357 | -44.79534 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a66e5793-6ba6-365f-8321-24de88d10b91 | -10.73383 | -52.03042 | 2026-10-10 04:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 734e68ae-9be4-32dd-ab42-ee92edc826ca | -12.36341 | -46.60165 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abebca14-cddf-3d0d-bd1e-1fd5bf872d79 | -10.99648 | -45.39481 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04bd744a-cd95-3afe-87ce-c239a965e5bc | -16.58331 | -46.76501 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90c75100-b5b9-3d1a-828d-2b2830b85980 | -12.02788 | -43.47036 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85bf1b53-2ed6-3516-a400-173b54c48226 | -11.08684 | -43.99281 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9129215d-2240-3a31-82e0-7dfa2d620c45 | -11.282 | -45.19129 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbeecf0b-1551-37ed-8ebb-0922248c6438 | -11.96242 | -43.47375 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1d86403-586a-3632-ba1d-decff245ec93 | -15.21402 | -40.48069 | 2026-10-10 04:10:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0b60ea2-b76a-3f59-bb5f-e9824c332b2c | -11.60325 | -43.72224 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5396104b-1002-36c9-957f-6ca41b23be53 | -11.83298 | -43.58275 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 434ccb64-b980-3acf-81c9-a6c5eb25f5fe | -15.37566 | -41.92756 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 253ce0f3-c339-30c7-9a26-030253c976c5 | -12.77491 | -44.88147 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 558b1f5b-bfd5-399d-9d88-09e53d34e00b | -13.37977 | -43.89569 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3a0c22a6-597f-361c-a294-5375d85b3ae6 | -12.22112 | -44.64929 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 843f86d5-807a-34e5-ab25-7b5fd141c76f | -11.04692 | -44.04901 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d765aaef-e64c-3cdd-841a-d10cfa48a487 | -14.68435 | -46.85817 | 2026-10-10 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99318e21-3054-34e3-b042-03250385f758 | -14.44641 | -43.93068 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83146783-ce77-3baa-9614-add62ecbe60c | -14.46292 | -43.93342 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94d17b72-29d7-3094-9bf4-46fb188707ee | -11.27917 | -45.18688 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b3046e6-faf0-3776-832d-9c0d516309b6 | -11.69232 | -43.65399 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26de024b-a1af-3bc3-99bb-bacaf446eee8 | -11.97728 | -43.48699 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64aa99d9-b963-3b4e-87a3-74c872f98ab3 | -11.86552 | -48.02883 | 2026-10-10 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52116dc2-9541-3cdf-92a3-6c46dcaba2e8 | -13.85258 | -42.65041 | 2026-10-10 04:10:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 557da5e4-3619-390d-b32b-c2d5c87303f8 | -11.25594 | -46.34861 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42cf9c1d-de43-3631-a3ab-e0745768eaa0 | -11.84343 | -43.60254 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b0bd5c6-926b-330b-8250-9db0bed84dac | -13.7399 | -44.30605 | 2026-10-10 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a7fd2cb-f0b6-3149-8759-f85b408a99ab | -10.90268 | -44.82703 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 567975a8-e0b9-31ee-b58d-761c5b7fab04 | -11.99979 | -43.45506 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d987a4e8-ea8e-324a-9ccb-6c3ea65f2e19 | -12.03896 | -43.37861 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad07a07e-0e3e-3193-967d-94c421ca5df6 | -14.71321 | -48.22697 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5ae9a5d-cd76-30ad-8b04-3e60b05bc15e | -15.34922 | -42.77784 | 2026-10-10 04:10:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ece472fe-e1be-3fad-b489-bd0105486a5d | -12.05599 | -43.42098 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d92acb59-180f-3bc9-96a2-af51c9158851 | -13.52187 | -48.43167 | 2026-10-10 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 967d7581-e244-3710-bb3d-702f6ed8186f | -16.76431 | -47.0666 | 2026-10-10 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d76a3aa-cb46-33b8-b230-d5a788985a37 | -11.84241 | -46.79378 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f06aaff-cd2d-3dfb-93f2-9aabfe692e78 | -14.22558 | -42.76776 | 2026-10-10 04:10:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 816b8b49-d6c8-3720-8750-bcec1e10e48a | -16.13775 | -46.02967 | 2026-10-10 04:10:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07b7c55e-aacf-3d6e-9259-dbf592774a04 | -16.02487 | -45.13102 | 2026-10-10 04:10:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51cbd5e2-acc1-3ded-9eae-a92e86a9668a | -10.89704 | -44.81882 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 2aacc0bc-cbc7-34c2-8ee7-b3f7bcf9441c | -14.18194 | -43.94481 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 763ea4b2-9992-33de-891a-83b70d2c3763 | -11.2613 | -45.17286 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba67cfd-5ee9-3999-bb48-217a663fbebb | -13.37589 | -43.89869 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2445f598-db03-3689-8a53-4a0e38677b7c | -17.3468 | -42.67794 | 2026-10-10 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 792642c9-62d3-3da1-a3c2-7adf56c2fc2f | -11.79325 | -46.72392 | 2026-10-10 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 84a0e3bc-66ea-35d3-98b5-f35911fb280a | -13.77377 | -48.1233 | 2026-10-10 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57bab2e6-5dc3-38cc-a776-0921bcbbe62e | -14.32753 | -44.67466 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2f36475-6317-3589-b3a4-b2d2aad597f0 | -12.01305 | -43.43553 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a76e081d-886c-3bdd-9c14-a09754583d62 | -11.6846 | -46.85582 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d40aa6f-eb42-3dd0-950f-56d7b672df9f | -11.67883 | -47.30227 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 940980f8-9450-37d3-8c6c-a00d919366c5 | -11.96684 | -43.46722 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ddcaf63-75e9-3039-b575-7399215b23b3 | -11.94811 | -43.47856 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1463c6c8-c682-3df3-82cc-a0cf74228a22 | -13.38863 | -43.88262 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00824648-1ae6-38a1-aa43-6016c3e2b2d7 | -15.3717 | -41.93075 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 4e10b2ab-60ed-36ba-bc04-5c94ce3bfc70 | -11.62006 | -43.59465 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0358d6ff-7e0f-3296-be67-9ecc5311ff65 | -16.1323 | -42.85435 | 2026-10-10 04:10:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6498d55b-655d-3574-b5ea-8b5346f79708 | -13.26058 | -44.00351 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ebdda1e-45e4-3b9d-b06c-4826f860f506 | -14.44192 | -43.95906 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3484e01-6d15-3370-af91-871a4780bd21 | -13.52717 | -47.41741 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 880548eb-d1f0-318d-80c9-b72067e43a43 | -14.01777 | -48.75775 | 2026-10-10 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e867c22f-4e51-3446-a844-55671da12acf | -14.46174 | -43.96235 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f7f0bf2-a835-35d6-900f-6243bac3002c | -11.68089 | -46.85505 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 968610d2-4b24-3aed-8e93-070016ae155f | -15.37734 | -41.9163 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5b2a25f3-bd4b-3e98-a658-14dfd19869e6 | -8.49166 | -54.60671 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9da3b800-fe59-3d71-98a5-fde99b5dc7f2 | -10.89989 | -44.82263 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| e3b70a9a-fa6a-34d2-bd6f-de13cfa7473e | -15.02254 | -46.25648 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47f2f3dd-d502-3f19-a12f-69885f2392d4 | -16.05029 | -44.82503 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 217fab6c-5192-36e7-9762-3dbe93bd1979 | -12.38382 | -46.61425 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aa3b202-6336-32ed-95dc-d1e13dc8550b | -15.02304 | -46.26554 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fccc921-d46e-3c42-a4bc-aee75b7facc5 | -12.58847 | -44.1406 | 2026-10-10 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d22463e3-d577-37b7-a58d-e2b184ad5a15 | -11.09744 | -43.99086 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac6d5a9c-d420-37c3-8692-ea0b909167d9 | -16.65114 | -40.54033 | 2026-10-10 04:10:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1bdce952-2100-3a15-978f-b05177dbd7e5 | -11.38302 | -55.15446 | 2026-10-10 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c245426-633d-31c7-9c10-f069790088cd | -14.20871 | -42.13999 | 2026-10-10 04:10:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2d4c784-b033-3a3b-bb13-3bb499a631ff | -15.38706 | -41.90153 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 18bf63b2-e5fb-3eb7-b745-f43dc4169d72 | -14.45077 | -43.94596 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9651444-adbd-3c51-a8d0-fc55c024531c | -11.98871 | -43.5037 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4679f60-0445-3f0f-bfe1-51b4ff98efe5 | -11.60538 | -43.75174 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82f28dfb-365a-373a-bc3c-9ad4ac6ecf22 | -11.51109 | -47.60253 | 2026-10-10 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a780637d-179c-3853-9e3f-1e7d1f5c6951 | -13.41269 | -43.73048 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afe7aff9-26b9-3cdd-92ce-c22db8491fc4 | -11.57452 | -43.71035 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c45a6c4-be4c-3afa-ba5b-9b337a978ee3 | -11.56405 | -43.69057 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21907880-47a8-3243-99b7-7d1ea756f66e | -13.38145 | -43.88507 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f273fcf-27dc-3398-beba-127d49fef854 | -13.26446 | -44.00051 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78bd6770-e876-386c-b225-cdc9c399a016 | -11.91022 | -46.57056 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README53.md)
