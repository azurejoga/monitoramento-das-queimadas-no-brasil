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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b339e3e-b5d0-3a2b-8721-142d98f17f17 | -8.21554 | -43.31778 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c997b3cb-68bf-3ffd-8ba5-6dcf4fb29024 | -5.86363 | -43.86971 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7dffacda-2bd3-3fa5-9462-110d25ebc2a1 | -5.48436 | -48.65434 | 2025-10-15 04:57:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce1797e6-edff-3a4e-bd85-ca6999c52644 | -5.87572 | -43.86667 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6893f5c-7da7-3b37-9f38-0248845c2b8f | -6.896 | -43.96109 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a7cefd3-5cad-394a-9fb7-95bf2ab437d2 | -12.04619 | -47.66104 | 2025-10-15 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 124eab7c-53ae-37d3-9150-bb3f10969110 | -7.95154 | -44.13592 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9320704f-bb09-3058-bd26-df273e42b8c5 | -5.20353 | -47.68149 | 2025-10-15 04:57:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf98fb3d-dcc5-3f70-a177-96e6b7f0893b | -8.73315 | -43.8624 | 2025-10-15 04:57:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 970be9ca-ba8d-3e4f-9e05-342d1445b34a | -5.38967 | -43.22371 | 2025-10-15 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e006244-0a39-3450-bb75-9069055a5832 | -6.46098 | -41.84075 | 2025-10-15 04:57:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14665f72-19f2-33bc-b508-7f75d7d715e4 | -4.89922 | -49.95346 | 2025-10-15 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9606296-f907-3702-827d-befb20c09f99 | -8.26574 | -43.36286 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| c4530562-4a93-33ec-8c0d-0a0f18a951a7 | -5.18829 | -46.17234 | 2025-10-15 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f971a200-5310-3d1c-8363-32d4700f10cb | -5.85735 | -42.33247 | 2025-10-15 04:57:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6832d64c-d3a2-32ff-a366-39cb7bd4c0c0 | -5.13848 | -46.10419 | 2025-10-15 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60fc91a2-9d5b-3fb3-87f7-ccaff5c92f30 | -5.4304 | -44.42601 | 2025-10-15 04:57:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6fece8c-b217-36aa-95f6-91c88560eb96 | -7.57071 | -43.83591 | 2025-10-15 04:57:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5187d40e-19df-3daf-b603-3445e796ca83 | -5.16609 | -45.16666 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e24cd54f-07cd-3f07-bfc5-85b3a9819259 | -7.50152 | -42.14286 | 2025-10-15 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d994d0db-0caf-33fe-9f38-a47bdb6b12eb | -7.1646 | -42.49658 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c76056ff-ef59-309c-afba-fbc18fdc2be6 | -8.22493 | -44.08382 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e11043a-6aec-32ab-8bfd-10ab3f3400c1 | -4.90019 | -49.95566 | 2025-10-15 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b49a1ffa-6b23-381a-8831-0799aa16f058 | -7.49488 | -42.14312 | 2025-10-15 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ca9f30fe-e5c5-3311-8a61-499cde40fdc4 | -6.89545 | -43.96517 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a060e775-a96c-35eb-b6fc-24e88c4068b3 | -5.60305 | -46.24852 | 2025-10-15 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb589fde-95bb-3baa-a37e-389b4f6e307d | -7.57464 | -42.70905 | 2025-10-15 04:57:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 25921974-db28-3dc5-ba55-1fdb15b5c247 | -8.21383 | -44.03088 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9acbf86e-6cac-3152-ba6e-65aecca452cd | -5.47105 | -44.64701 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1e23a47-feeb-3393-aa30-3ac1fe64f006 | -8.2101 | -44.0132 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 197ffa11-b3a3-3d6e-b79f-74fcb2457baa | -6.31219 | -42.99502 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d14cbc99-33fe-37ac-98d2-50d2a265e455 | -5.85803 | -42.32751 | 2025-10-15 04:57:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 24c3ffe4-eaf5-3897-8882-9ecb9c3ac86c | -8.19732 | -43.98009 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f55f5cb-017c-39d7-9be8-cd30f0232314 | -10.51739 | -43.36922 | 2025-10-15 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7baf951f-51e8-3be4-8e2c-40b6b8a03103 | -8.21965 | -44.07877 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eedec451-48a0-31fd-87e5-700034c99a6c | -5.46822 | -44.64659 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28386a99-e5d8-30bd-b2bc-eba2597bef88 | -8.19201 | -43.97504 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 83556ba6-c3b3-36e2-8ac0-b40e196e0842 | -7.93419 | -44.13353 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aacf7e4-54c3-3846-a979-d4864a8137ec | -8.21893 | -44.08582 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e365fcd9-09ae-38dd-9154-8867bf0d3ba0 | -5.87515 | -43.87075 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 13da8047-10ab-3afa-9bb1-a55ecb51bdff | -8.21457 | -43.32013 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 24c47018-eb84-3792-b6dc-71668245bd83 | -5.40873 | -44.22074 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8f8d093-e9db-33e9-96e9-a0bfa4f96184 | -6.57827 | -42.96793 | 2025-10-15 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41acf529-5aba-30e8-a4b4-e240eebe883e | -5.95058 | -43.75861 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 282d658c-d16a-36f7-a34d-7cf26e7b5ba1 | -7.16142 | -42.50136 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8b19626c-913c-35d0-a2be-54b8caeaa7a6 | -5.34572 | -43.74935 | 2025-10-15 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9df697fd-2b78-31be-a300-9500f99179e7 | -6.30107 | -42.97736 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78e8968e-6906-3a82-99e4-dda5f5a94dc1 | -5.79457 | -43.88928 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3d09ef43-8a2a-394e-acaa-38b1b77308c6 | -5.86884 | -43.87417 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 702c91a5-e2a7-39b4-a2ab-c2ce14bf3e47 | -8.21913 | -44.03603 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b99e5356-aae0-32cb-abba-880d5828cf51 | -6.79074 | -45.47701 | 2025-10-15 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b97f880-df78-31f3-84f9-de44b5cff2d2 | -6.55649 | -43.9289 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5aae070-124a-382c-9d07-d00aa9b73fbc | -7.15892 | -42.49043 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cbc587ab-fb95-3e61-aac5-b0dd48140d0e | -5.42498 | -44.22142 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 02b6b053-4785-380c-8411-e529c3724284 | -7.25556 | -44.91531 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6de30b3-a6f7-3294-8df5-f8dd8b63fcee | -7.16071 | -42.50654 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dcc38ed1-9045-35de-af69-c0c8eaa37ed4 | -5.44218 | -44.21986 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 608ef3cf-efc6-33ca-be32-d496e8b6e166 | -6.0568 | -41.89429 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d0bf5f10-1037-31cb-885c-b60407508133 | -8.19677 | -43.98426 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae734305-25a1-3ed2-a4d8-ca879007c2e0 | -5.43053 | -44.22221 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3fd04701-66da-36ad-af94-e911ac739d88 | -7.7948 | -46.01918 | 2025-10-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38ace39c-0b93-3a0c-b37a-c9aa4dfb9e4f | -5.83222 | -42.32824 | 2025-10-15 04:57:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 372c371e-29cb-3dec-a011-5dc4556a57f5 | -5.76955 | -46.01175 | 2025-10-15 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9d00102-af04-3531-b0ce-d081290db3cb | -8.26515 | -43.36745 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 10f12636-5c2e-3e78-9487-6617d746822a | -6.45231 | -44.57558 | 2025-10-15 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 350ef013-6838-3d50-b41d-bd34a77ceea8 | -6.33692 | -44.01635 | 2025-10-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 926c53ab-2035-3764-b10f-1b1df7962a59 | -6.33638 | -44.02028 | 2025-10-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85e8283f-7110-3ef2-8031-41f7960bb3d0 | -5.8722 | -43.85022 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4be6dc07-e101-31fa-988f-0b9abacc1dc0 | -6.80561 | -44.54468 | 2025-10-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf1c989d-6b38-303f-bbe5-99a50fd00b87 | -5.02183 | -49.99568 | 2025-10-15 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71bf7aa7-9273-34aa-816a-3ba18b486ca3 | -5.47407 | -44.6441 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c904c9b-d6bf-3c9c-8650-f58f4769e355 | -5.43559 | -44.22662 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0f2a3026-d5e1-35d8-94b8-aa4d7d7419d8 | -5.19422 | -47.04076 | 2025-10-15 04:57:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d4f55c4-6369-375f-bc08-7b15481848f5 | -5.00623 | -45.87016 | 2025-10-15 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2454088d-7844-3ba8-8e23-16f0bd9e192d | -7.57529 | -42.70401 | 2025-10-15 04:57:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eeeb1344-973a-37d5-aa12-669eb21fb64d | -6.31141 | -42.99253 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a05352c7-cf4d-3dd8-b007-436544d03085 | -8.18443 | -44.03271 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a77d43b-6b41-32c2-b9a3-890877cec63a | -5.18966 | -47.04017 | 2025-10-15 04:57:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4edfcf73-1d72-36e0-aa43-9d6519b6571d | -5.94535 | -43.75381 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d37d2cb2-e5ac-37ff-abb0-e540adcade5c | -5.89274 | -43.74564 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f18eb4f2-75a8-3323-9431-9733989f9715 | -8.22475 | -44.0867 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d82fd4e-7dce-3ffb-be0c-cbee18c23244 | -6.05607 | -41.89986 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8ca91ef2-7bb1-31fc-88de-0581de3fd2bd | -6.46169 | -41.83523 | 2025-10-15 04:57:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5155d79-a83f-3c0b-b14e-f11b297e1487 | -6.34337 | -42.66691 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c6cf5a11-f6e9-39f3-a5fa-9dff4adbca7f | -5.67421 | -44.25367 | 2025-10-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d996ad60-11fc-3db6-b2c0-a6b53482b335 | -8.20206 | -43.98932 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 228db7d8-ad91-3290-89ba-1739152af3cc | -6.45183 | -44.57917 | 2025-10-15 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3dc0d070-6ca1-3156-8f62-39d82e2202e1 | -7.75231 | -42.45669 | 2025-10-15 04:57:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 18f38ec6-0a9c-3031-9a0c-49ef34eb9528 | -6.89434 | -43.97336 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a77f01c0-9382-3d56-b740-7e495fa1b690 | -6.89022 | -43.96032 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da504ef7-0f99-3200-980f-da1a631dcc68 | -5.79095 | -43.89 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8f0eb5c-5c7b-3770-aff6-df9a9790bb70 | -5.87661 | -44.21373 | 2025-10-15 04:57:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eff26350-5af0-3ba2-9fcf-230949f1ebec | -5.88643 | -43.7487 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c3009ad0-9db9-35bc-ba51-07090710e1e0 | -8.22167 | -43.31849 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e943c8ce-c748-3a2a-97ff-803ed62e8365 | -7.0334 | -42.74049 | 2025-10-15 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f97fdebf-43b3-3140-acfb-c207b20b3809 | -7.95044 | -44.14423 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dd05019-2550-3cec-af60-88010f069f92 | -6.19829 | -43.28369 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 859d9de7-8d87-383a-8283-4e61c025b7a2 | -6.25264 | -44.02208 | 2025-10-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8560a9ad-19f2-3263-be38-b81c9897636a | -5.8587 | -42.82351 | 2025-10-15 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 907e2d21-5507-33ea-b9c0-6d11ff41ce0c | -6.34469 | -42.65725 | 2025-10-15 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README45.md)
