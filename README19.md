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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 412231c3-90b5-342c-b352-a73e5e99e78e | -12.74161 | -48.0799 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4ea0ab7-22a7-3dab-a5cd-7876a785915f | -11.32583 | -43.29639 | 2025-08-27 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5186e0f5-3f8c-3a30-922e-3e48adea5f53 | -10.31708 | -46.79502 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76a0ee36-302a-3266-9aba-b91473705e42 | -13.65929 | -46.88031 | 2025-08-27 03:38:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 741bfeeb-876a-3718-95de-204c1c897dad | -8.86615 | -47.17117 | 2025-08-27 03:38:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25ff6ae0-069c-3767-8791-20448fcf2d02 | -8.29828 | -46.32623 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f7e276f-be35-3987-a3f8-d080fb9055df | -12.90565 | -44.63181 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69027b0e-3ae3-34d5-8238-4ab775f3aefe | -11.03546 | -45.14021 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d6a1f06c-e7ae-3673-86e6-cefa5986b9a1 | -11.21102 | -41.59882 | 2025-08-27 03:38:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b7aa06bb-1228-378d-9b64-1bbf5a80c8b9 | -13.51836 | -46.88636 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9dd697a-0fc9-365a-a691-2608b2e2720c | -11.08025 | -44.78008 | 2025-08-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16f5fca0-54cd-3578-9ff8-bb4d7217e0b8 | -12.90041 | -44.65866 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e3667168-6041-39bd-a01e-8fdca96661bc | -9.30587 | -48.27879 | 2025-08-27 03:38:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25742599-54bc-3c55-bd86-0a6a4fc17338 | -11.03808 | -45.13839 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c2790071-1d9f-32de-878e-11dc4900a6ba | -11.92 | -46.74474 | 2025-08-27 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a420d6b-3e60-326e-9391-d808acc86ddf | -11.74488 | -49.09062 | 2025-08-27 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 645deb8c-0d19-36af-9c60-b58b0176126b | -12.90573 | -44.65969 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d719b3e5-df21-356e-a152-7c0bc913143c | -8.89849 | -47.32671 | 2025-08-27 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b77bfa94-5025-3ab2-bd86-d25cfa168d2b | -10.78784 | -47.06749 | 2025-08-27 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 234e575b-66d5-37e1-bc23-c7554dd61d50 | -11.13748 | -46.33661 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 11797688-4ca1-3d9e-8f13-6108763fd226 | -9.19931 | -46.73536 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7ce8dcc-a017-3089-9479-780116e448ce | -11.57827 | -44.65006 | 2025-08-27 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6f9d1ea-234c-3b75-a061-362134946a56 | -9.94341 | -46.3738 | 2025-08-27 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 211cd93e-cea3-3c08-a501-5463fc5a1e6f | -15.98614 | -42.25273 | 2025-08-27 03:38:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a7b9d242-1c4a-3633-9272-ee2a5c2ccce0 | -12.24596 | -45.06005 | 2025-08-27 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f1bc43a6-53d5-3688-bd2b-1676ee4fe2a2 | -13.22542 | -44.55097 | 2025-08-27 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8ae1ca3-cd41-3cf1-a031-7af872921a7f | -12.89907 | -44.63729 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 36044673-6749-3ed4-a6f1-2c7de9a73a45 | -11.13654 | -46.34133 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a3b1b4c5-7bd0-3695-83d5-9a472f02a1fc | -9.86669 | -44.69344 | 2025-08-27 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb202ac6-42d1-33e7-aa56-cde39b838553 | -8.46443 | -43.66187 | 2025-08-27 03:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35283408-0dbb-33a3-9e39-9e125d839c0f | -13.17633 | -45.2881 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 81d4362a-62da-3dbb-9d61-f648b2e7a3b4 | -12.76329 | -48.17288 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 961f2de9-3f48-31ed-a0cd-7b299f9762b8 | -8.45045 | -43.6776 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e1a99fc-cdd5-315a-95e1-458e22d086bf | -12.75108 | -48.19843 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 06184e7c-4257-3744-95a9-bc43fe07165a | -8.24209 | -45.13479 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57b8f105-8a2e-3780-8f59-2d7494c7f707 | -13.63597 | -45.69906 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91420125-dd7e-3193-8f0e-727905ebcd17 | -8.8673 | -47.16524 | 2025-08-27 03:38:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c32429f6-4c7d-352d-a0c7-621b6e09888f | -12.90108 | -44.65522 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0c606581-c327-3709-9fbc-6dc7389fe8f0 | -13.16961 | -45.29483 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc934408-8bac-3a5d-860f-1921cae7591c | -13.60327 | -48.15091 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d08e71aa-f486-3b9c-87e4-f29b86b69931 | -13.50122 | -46.87802 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 793618cc-7190-37cb-a58c-5aa5a045f0ea | -12.89971 | -44.63401 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a4814f59-7ad6-3a5b-8036-b566ca07f8a0 | -11.81932 | -46.79903 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6f64183-b23d-313b-96c7-5b13724a1974 | -12.42573 | -45.96506 | 2025-08-27 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bead495-bf60-3172-9612-6da5bab1896f | -13.46972 | -43.74966 | 2025-08-27 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7509872d-5326-394b-90e6-4f9d570b62c3 | -11.81312 | -46.79789 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1fdbf031-d768-377e-8180-30279969e954 | -10.77879 | -46.3821 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54264ac0-ece8-3d35-a9cf-cf3acb9c9143 | -10.66566 | -47.17185 | 2025-08-27 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae266630-637d-36dd-9285-1bf64ccfdd35 | -9.29888 | -48.27727 | 2025-08-27 03:38:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56a2ee07-7f9b-32a2-bb68-76e05f16b385 | -12.24504 | -45.06285 | 2025-08-27 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 070d560d-d340-3b6b-97fc-10314edf82b1 | -11.91387 | -46.74339 | 2025-08-27 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f1da853-e75b-36f5-9b3a-c5d814a508b8 | -11.10804 | -44.75407 | 2025-08-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ab23473-6ff7-382c-87b5-ddbdcd3e6522 | -13.64641 | -45.70502 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2350b6d3-10de-3cf8-b4b2-e8649ea2e22c | -13.52436 | -46.88777 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 790edbb8-7a5b-30b8-b1a1-81be74631a13 | -12.95828 | -44.58687 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66b7dff0-d62d-37ca-89fa-11aa7fdc83d0 | -12.7681 | -48.18285 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5fc4e0af-4c56-35ae-bc11-723c13a0f12c | -11.64501 | -44.86467 | 2025-08-27 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e487e587-143f-311c-aa50-af70f19b7583 | -13.17106 | -45.28732 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 489fb9b1-d07a-33c0-ad7c-40cb39f38aba | -11.10254 | -44.7529 | 2025-08-27 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ba51308-c3c2-3e2e-b16a-7782f72e5470 | -12.3999 | -46.5074 | 2025-08-27 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61c312f2-6e0f-3ee6-9cec-232b0bda89d5 | -13.07078 | -46.32129 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 019a22a0-12ce-34f8-b619-f0a2be871ef5 | -10.76478 | -46.38824 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab5053f2-7798-3201-91e0-863c34e03aca | -13.47505 | -47.00171 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3458087d-1b99-3701-9b1b-24cd8780dd52 | -8.45937 | -43.68988 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17a40a62-7b99-324e-a3d9-28b6b515190b | -10.76381 | -46.39304 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0920e8cc-5d08-308e-bbd0-a1e5484ac4cd | -8.26401 | -45.11615 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e0b7eab-2ddb-38b7-bb1e-e4c4eb1a53ea | -13.60207 | -48.15652 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d257236d-7b9c-3b0b-b15c-cfd54a6d558f | -14.1304 | -45.40293 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f575b7a7-2682-3473-8c79-8639ec72013a | -14.1295 | -45.40282 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf36bfe1-861b-3bf9-8a46-855d43609177 | -13.22608 | -44.54763 | 2025-08-27 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 001c4edc-13aa-3db6-ae9e-b129bdd6b2f7 | -12.89974 | -44.66211 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 55628f8c-e52f-3978-8f1e-8f0fe83f13d9 | -12.24527 | -45.0637 | 2025-08-27 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6aeeeacb-934a-3c39-b2be-5ca8362a58c8 | -13.39876 | -46.88074 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c4fa337-da54-3358-840e-b3111a752f2f | -14.06984 | -40.19039 | 2025-08-27 03:38:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8af30dbd-bc2d-359e-97c9-90a0432537b1 | -13.62696 | -48.19935 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95700f2f-6390-3ea4-bd44-5200ff09e12d | -11.03727 | -45.14252 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cfd13a7b-1475-30d0-8763-ec3ddc736005 | -13.06711 | -46.3302 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0dccad14-1a6e-3536-ace9-b5d2a0ee396b | -13.61225 | -48.20466 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f77f7fa9-5dfd-3b8f-ad83-33748b306368 | -10.7865 | -46.37912 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 877eb5a4-ccd2-38de-86ec-9d85b19692d8 | -8.26227 | -45.12542 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9641a876-bf02-32e5-ac96-3c3a7e96a311 | -12.70526 | -48.18687 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 194b8f90-7932-3d6f-9ee9-6d6a450c33c1 | -9.6483 | -40.5973 | 2025-08-27 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 94c324a4-5749-3b1e-ae3c-cb6a0ced635f | -8.45714 | -43.67141 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f6f9166-a257-3b3c-a960-8f0302b6814e | -13.47567 | -47.00018 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0caa2ba-4d86-3785-854f-0f23ae6adbee | -8.24562 | -45.14866 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b758673-9d30-3cec-98b8-906061a6026e | -10.32041 | -46.77823 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a16e7710-02e1-327c-a795-574e040cdc03 | -8.29683 | -46.3245 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 860b556b-dbd1-389e-8a45-97d1252c50e8 | -10.31721 | -46.76118 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f73f35b-b9eb-3c19-8f9b-efe9ec2de8dd | -13.62361 | -48.21526 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| daf5be5d-5043-38f3-906d-48b7421e1c30 | -12.70835 | -48.18373 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 772eee9d-acce-3543-be5f-065a85e14f83 | -12.89777 | -44.64397 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 95d4b602-f28e-3d2e-a63e-7d28caf26cdc | -12.43074 | -45.97027 | 2025-08-27 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 937497e1-e6c8-3c9c-bdc1-bd0813c3c171 | -13.16931 | -45.29454 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0414f20e-0d03-376a-99a7-bc18d2c4bcc8 | -12.95368 | -44.58227 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c46c2dd3-36a9-3e7a-9039-7981a96496a8 | -13.06988 | -46.32585 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3d2589f6-0f6f-36fa-9c03-fc6a6c0684bd | -8.45461 | -43.68538 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0171262e-54e9-3fb2-b843-3905ffdf74e6 | -13.82513 | -45.89307 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cb1bac2-fe98-36bd-9d9f-b78a1a12fecd | -13.50714 | -46.8798 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a298bb3-92df-3b2d-820e-7e6bdde06b0e | -12.87885 | -48.10189 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 333006c8-b31c-3b5a-b916-49feb35cfc73 | -13.50756 | -46.87186 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README20.md)
