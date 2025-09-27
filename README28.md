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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5f722ae-9121-38d4-961b-b3646595ace9 | -5.07385 | -44.85845 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 460993c2-d3e3-3820-a2fa-17673a59c3d0 | -5.60204 | -45.37187 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df2666ce-f3f7-32dd-b292-e0d7b9d902c9 | -4.1418 | -39.99441 | 2025-09-27 04:21:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e769782b-4cec-3496-91ff-2331253a9c6c | -5.22078 | -44.49059 | 2025-09-27 04:21:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2e0accf-59b4-3555-84e2-06f761eb31e8 | -6.81667 | -44.47153 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08fcff4d-aea6-313e-bcda-1f3109047f53 | -6.52256 | -43.58652 | 2025-09-27 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e24e19dc-4a5a-30c3-85af-912a87df11da | -6.5529 | -43.84151 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 596a16a5-31eb-32f5-8d7d-975c07935b1d | -5.95732 | -44.56021 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4943242a-d3f1-340c-94c7-ab3edb61de0b | -4.00655 | -46.96249 | 2025-09-27 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e035fea-81f3-3ac3-b773-8d887a643158 | -2.96073 | -48.59876 | 2025-09-27 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6ff2d91-5cb2-37ed-9f8c-1f29034f3bb9 | -5.07773 | -44.8555 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 85c3767a-e341-350f-8e29-4a407767a89e | -5.31329 | -42.77284 | 2025-09-27 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f006d187-244a-37aa-be63-1a4d71b883f8 | -5.8251 | -41.29783 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 45e90634-97b1-3cc9-8ac0-c7eabdb8b17b | -7.27338 | -42.97565 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 070fba1f-334e-3879-9e81-484cc81da153 | -6.99996 | -42.38868 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1ecab22e-595e-3354-9ce2-f7c4c16824a7 | -6.06909 | -44.87698 | 2025-09-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 370130a9-b336-3c19-9365-c9abc05fc60f | -2.44771 | -49.02264 | 2025-09-27 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea31c02a-77c0-3627-93c5-e83dcffcd933 | -5.1999 | -43.72134 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0628cdf1-57a6-3e36-b8b9-473095763e1a | -6.82702 | -44.10057 | 2025-09-27 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8463ffe-a98c-367c-a12c-06e9f3e54a62 | -6.94804 | -43.25215 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0578b0be-4dfc-300b-accf-9c94b9a1803c | -5.49915 | -43.08083 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06289ce1-8440-3dc1-b3dd-4c8023cea51b | -7.11701 | -42.18729 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e2abf49-ef1e-371b-b276-b5c5e0522127 | -5.71669 | -44.51895 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0324496-b42b-3d52-92c3-f35a2e520f17 | -6.63346 | -43.82184 | 2025-09-27 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a450a45-3b7d-3895-bc1f-4a331050f74e | -6.49104 | -39.4702 | 2025-09-27 04:21:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9bdfa013-afc5-31aa-8692-79009a423d42 | -5.8002 | -42.82777 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46d68676-e0df-3612-bf20-110a971b9242 | -7.6275 | -43.84097 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 843d973a-ef49-3c57-ad98-0bcd65668e92 | -7.62302 | -43.84762 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ddea2f6-f286-366b-92c4-a88558144e07 | -5.79679 | -42.82721 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e80e95d2-612d-3264-9e2d-8ce9b86e079b | -7.28429 | -42.97353 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 08f461da-c036-347b-a414-9ce6f7e1ec24 | -6.32298 | -43.45719 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b41574ca-664b-37ed-9660-66e97b9166ca | -5.73676 | -42.64757 | 2025-09-27 04:21:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c897373-0a59-35ab-9b17-cfd7434b9063 | -4.57627 | -48.01852 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee34188-aa20-3857-83e5-2fc177a71a55 | -6.49672 | -43.28436 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a34bb4a8-85e1-385c-8e12-1d771bdaab7e | -4.97206 | -43.19136 | 2025-09-27 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92d7063d-9cb6-3c9d-bc10-b094a4461328 | -6.26875 | -44.0783 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e729287b-7232-3607-abeb-fd437d675898 | -6.93003 | -44.64965 | 2025-09-27 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c31298cc-223e-3f10-a1b9-78f4d80cbc75 | -3.33379 | -50.25176 | 2025-09-27 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75756bc1-2a4a-3425-aadf-68cf7b73b697 | -6.33415 | -43.36333 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2076140-cd50-3fa9-a69e-1121cfdcf523 | -3.82126 | -40.34571 | 2025-09-27 04:21:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44c564d1-1aae-3256-aef3-f1f9823181bd | -6.89617 | -44.16172 | 2025-09-27 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9073f09-596d-3e9a-920c-8be910c420ed | -6.27651 | -44.07235 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5ab1e9d-5b88-35b4-9b67-74a73329c015 | -5.30668 | -47.22067 | 2025-09-27 04:21:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 847bd75b-4f80-37fa-a4bc-21574277a374 | -5.98038 | -43.23871 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb2803cc-795e-3ae5-8b3b-f8d95a354d86 | -3.07249 | -42.67981 | 2025-09-27 04:21:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1039b8f2-1018-3051-8b57-329702b3fbd2 | -6.24679 | -44.09658 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca3c08f5-f1ea-3b35-a662-421c3de9b924 | -4.48126 | -47.66997 | 2025-09-27 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 044135a0-57e7-3c22-8418-cfb47b2caf66 | -6.32354 | -43.45361 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15085ada-e6d1-3c8a-996f-fc6965906b52 | -7.462 | -41.92041 | 2025-09-27 04:21:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80e97827-a10b-38f7-baef-717429dbc238 | -4.45319 | -40.97884 | 2025-09-27 04:21:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6d84be1c-84f3-34b5-a5d0-7986ed86c8e1 | -7.27683 | -42.97619 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5c84982-f634-3497-b5d9-bff801cd6d2e | -5.74598 | -42.34418 | 2025-09-27 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b3b026df-2402-3146-ab98-7b6051208e7d | -7.05337 | -43.02311 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d0904ea-1c31-3b15-bd3c-0566ed70b62f | -5.74015 | -44.96706 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 337c6948-522c-33a8-963d-7c3aaef747b3 | -6.26739 | -42.49146 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e7e275bb-1788-323c-8839-091ea108cb66 | -7.07383 | -43.86053 | 2025-09-27 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8713ba31-a5a1-3356-90a2-c58c874ef5db | -5.4788 | -43.07773 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9944f942-dba7-3a1b-82d7-d8e0eb06c652 | -5.12927 | -42.88004 | 2025-09-27 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 737043c6-a977-31d4-bd70-e4feff0e31e3 | -5.08384 | -44.86002 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df3861ac-bb48-3c97-8771-8038683607c8 | -7.11881 | -42.17532 | 2025-09-27 04:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5346246d-47d3-3fee-9a47-5526f45e0107 | -7.04535 | -43.02949 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ebbb0f2-4c85-37de-815a-0c4da6346479 | -6.25644 | -42.4702 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1f5d617d-e7eb-3ff1-8f5f-9e27b69773f7 | -4.00232 | -46.966 | 2025-09-27 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5f2ff093-9336-32f2-ac7b-ee8f30cdad0a | -7.15381 | -45.5211 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d68d2d60-9912-32f1-a4fa-14d3b2f575d4 | -7.11057 | -43.75692 | 2025-09-27 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2819d63-7bf7-3b8b-96a4-0b3ed0b346a5 | -5.72402 | -42.30175 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74f861a9-a48f-3b6a-a505-08436d53c475 | -6.89283 | -44.16119 | 2025-09-27 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e91e0a50-7035-3a66-b80c-ad4c6cd334e7 | -6.61197 | -42.21743 | 2025-09-27 04:21:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02230c7f-79a0-3e01-aa21-ddf1edb5b3bf | -6.68476 | -43.12595 | 2025-09-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef942c03-1305-3087-8308-76c463d8929d | -6.9733 | -45.33825 | 2025-09-27 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21514555-458c-3c2c-9d47-f4e6141bcc3d | -7.04936 | -43.0263 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e3086ce-d181-3628-8f65-43f38fbf16af | -6.3201 | -43.38685 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24009fc0-9690-3de6-bd72-e8d8206d1c67 | -5.48446 | -43.08598 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46b27578-ad59-3bd9-92f1-f88de53e2235 | -5.22099 | -44.67887 | 2025-09-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45b2e83b-b722-390b-80c5-91c07bc36a8d | -6.69761 | -44.85882 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e45d6d1-9c3f-33c8-ae4f-7d02f1a7cde1 | -4.32513 | -45.27903 | 2025-09-27 04:21:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34428c1b-8aaa-3b77-8405-f2a6c2e8d075 | -3.16162 | -48.60324 | 2025-09-27 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16dfa5a4-0fef-3401-9a4a-b72469eb960d | -5.97699 | -43.2382 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf83fc1c-b99d-3b85-810a-6763b51a3809 | -5.4195 | -41.32417 | 2025-09-27 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ccfe003-f918-3efe-98e0-2fc1ed4e0e48 | -6.54448 | -43.82944 | 2025-09-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 700502ba-195e-3ab3-bba3-51c93a778cb3 | -5.40378 | -42.27808 | 2025-09-27 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 38ee57ae-84ce-323f-899f-3cb8cb76204c | -5.03435 | -38.00931 | 2025-09-27 04:21:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7fded948-11f4-36bc-a312-54589dedee03 | -5.38279 | -49.66898 | 2025-09-27 04:21:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9068945b-bbe1-3bb1-8122-2613a07cdc1d | -3.15687 | -48.60764 | 2025-09-27 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7010766-85af-3c5f-b38b-100204d03e12 | -6.1298 | -43.46394 | 2025-09-27 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a4c662-1acc-3a7d-a373-22ee4e932023 | -4.57554 | -44.0765 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4507d786-fd39-3332-8d12-4f0baaa47dc0 | -5.19715 | -43.73883 | 2025-09-27 04:21:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75453ab2-24d0-31eb-859f-3245df674050 | -6.34543 | -43.78448 | 2025-09-27 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b294d01c-acfb-3a28-957b-667e49c5b966 | -5.94187 | -42.8339 | 2025-09-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c4dd2418-c1fc-3893-a50e-e96b0434ccdc | -5.73619 | -42.65128 | 2025-09-27 04:21:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 84fa0580-2493-335e-aaa1-585c8dd997a8 | -5.08217 | -44.84908 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5358c0b-44db-32d6-bc6a-5d0a6b082774 | -7.15436 | -45.5176 | 2025-09-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92207d80-54c8-3b41-ab15-232350047280 | -6.06165 | -43.20693 | 2025-09-27 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9eddd47d-29a7-3cde-940f-047a87248653 | -7.30861 | -42.94276 | 2025-09-27 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 17079a73-4947-3ee4-afac-58bc649cbd80 | -6.24834 | -42.47656 | 2025-09-27 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| faec4672-c80f-3132-8440-9ea39c97a073 | -5.72343 | -42.30556 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c056e92e-b87f-37f7-a645-fc07ec48dbb6 | -5.08051 | -44.85949 | 2025-09-27 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a577f49e-d99a-3f64-a1e8-fbc9ad2500b0 | -5.48219 | -43.07825 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6146c203-5f29-3014-82e9-7960171fe949 | -7.18881 | -41.70819 | 2025-09-27 04:21:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 03fb7cc6-2e2e-36e6-9151-f8d4b690762a | -3.80153 | -41.56999 | 2025-09-27 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |


[Clique aqui para ver as próximas entradas](README29.md)
