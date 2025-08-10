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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dd384af-b8ec-332a-9536-6b9bed46ade4 | -11.78345 | -44.95028 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 201397e7-f6dc-3ae7-9daf-0a462eefea3d | -7.57802 | -44.93761 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 852e224b-b628-3402-ba2c-bd4378f5a614 | -9.49303 | -46.277 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5717b93-4304-3d7a-94a9-38cc4e51002d | -8.98642 | -45.68121 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10d41b67-3cc6-380b-a252-85b8442c6c3c | -4.29651 | -48.07436 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4453d5ae-1b57-302a-9f5a-9ae9ef9300e2 | -4.07008 | -47.97448 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a43e884-b39b-31c6-8845-d4e107a16202 | -8.96314 | -46.74348 | 2025-08-10 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce2d4060-3632-3484-943e-7e6dbf4dfa26 | -11.73891 | -44.9503 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40d65637-cf7b-3d70-9a95-506eb3865288 | -7.58864 | -44.39749 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28fd8dfa-07cf-3619-8b22-6d95686fc0c7 | -8.77162 | -46.4106 | 2025-08-10 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ad47478-defe-3cc2-b1a5-16e506505d99 | -5.41159 | -44.42714 | 2025-08-10 04:21:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46c0ed04-e3d3-3b72-aa7a-dd3b2c778c64 | -7.29739 | -39.63691 | 2025-08-10 04:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 659bcb3a-e665-34c8-933f-f2f684cc7fa5 | -9.48968 | -46.27644 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 117673ec-17b7-3bef-983c-d057195b9108 | -9.49744 | -46.2923 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1738299b-5202-32d3-ae1d-663e4c84a340 | -7.16328 | -44.06594 | 2025-08-10 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 47958908-242a-37f8-9dfc-23b47c923205 | -7.05145 | -43.54882 | 2025-08-10 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a68d2a71-ea05-3643-ac6a-279f00d0a82e | -7.43005 | -43.98495 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a91e8840-81e5-3903-b66b-39466130ce89 | -4.0592 | -46.93491 | 2025-08-10 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a067844-3739-3702-83c0-1fbdb8995a3d | -7.2146 | -52.60839 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a17d3c6c-d685-38ed-8699-ec533c84078b | -6.98007 | -44.80376 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 682653a6-6e13-3b47-bd26-494d2382873f | -10.45369 | -44.39 | 2025-08-10 04:21:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c825bbf-271a-3467-a524-07b2e80222d3 | -7.87251 | -45.55284 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcfea44f-b5cd-342b-8381-e01c6bf778a1 | -7.26842 | -45.37342 | 2025-08-10 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cd08f9b-8856-371f-96f8-12edf665a829 | -5.47696 | -44.6999 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 440e45a1-8c5d-3ea3-9cd4-3cab910ac72f | -7.73997 | -42.33627 | 2025-08-10 04:21:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7aed5e7c-f1a4-36fb-afaf-3e2ba8015442 | -7.31878 | -44.69322 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f000549-74fb-3b3a-824b-cdb965b90a51 | -6.61403 | -43.37921 | 2025-08-10 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 10d007c3-9fee-3e29-8c7b-4ec3783c629e | -6.83369 | -41.05469 | 2025-08-10 04:21:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c6c1ad4-a61b-380e-b432-b4d092154198 | -8.25011 | -45.83707 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34535efa-b954-3e6e-ba6c-33e554be53e2 | -8.99196 | -45.68929 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a932c8ec-8901-3208-90c1-50c75771f11f | -6.96569 | -44.485 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8621833-f6f9-3e66-a632-555c8dbf29e2 | -7.70633 | -45.53663 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eff7a75d-3abf-3355-971b-70e8fcd253fd | -10.59253 | -50.5094 | 2025-08-10 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ceac62d-3d81-3827-ad5f-3b9aaccbd61c | -10.41952 | -50.38194 | 2025-08-10 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84095fac-8feb-386e-aea5-2c39772e8ab5 | -4.95896 | -47.59649 | 2025-08-10 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 450dadfb-8074-373f-bf99-3acacdbf4e5b | -8.17369 | -39.0826 | 2025-08-10 04:21:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 80ac783f-f079-3fc8-bcb8-1e09af56c11f | -8.3723 | -46.98351 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cba815a-c4d0-3785-ba68-cbff7ed65df6 | -6.96092 | -41.62562 | 2025-08-10 04:21:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c3e22a2-b772-3cd1-8522-81ccc8d6ea54 | -6.56538 | -42.83684 | 2025-08-10 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| be7409f9-79fc-3a48-8923-cb3f3c7eee99 | -6.19432 | -46.09937 | 2025-08-10 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa59afa1-d30f-3dc7-8198-d77154a2310d | -10.83012 | -49.3805 | 2025-08-10 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14693d0c-6faf-33fc-a7e5-46e8af66e0a1 | -6.95144 | -44.55384 | 2025-08-10 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 71e6a4bb-a0fa-3128-8807-6c88aff5c3a3 | -8.88098 | -44.78427 | 2025-08-10 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 347b0791-1b09-3cdf-8b11-0b7e0659aea3 | -6.19522 | -45.43996 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5167281-96dc-38a7-8d25-901f1676f730 | -6.98189 | -43.73082 | 2025-08-10 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeeaa613-c6ba-3f73-8d79-225c76e6f58d | -3.64957 | -48.32338 | 2025-08-10 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cca4f14b-66c5-3714-844b-d07a1f95821b | -9.49131 | -46.28765 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f8ff137d-2cb9-3c8c-b615-daccba44be65 | -5.68953 | -39.23021 | 2025-08-10 04:21:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0296aeb-531d-3a2d-a015-0e307aee8a3d | -8.50286 | -44.75996 | 2025-08-10 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fe2caa7-31f8-370a-a0ea-15113ff60207 | -10.45954 | -46.22233 | 2025-08-10 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57c15a1c-f50a-3052-a4d0-cbee41f4fddc | -6.18741 | -45.44593 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eba2c5a-7d50-3b3f-9967-3ade9b1b05d9 | -6.61066 | -43.37871 | 2025-08-10 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bb23816e-0a06-3910-8d67-1a9960029646 | -5.43121 | -41.24818 | 2025-08-10 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e66353f-46a5-3d5b-a56d-2ccca71c3165 | -5.8272 | -44.10604 | 2025-08-10 04:21:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e03be7c9-daaa-3b69-8b48-0920a043ead8 | -7.5881 | -44.40098 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7212fe5-0302-37ec-9896-272263aaebac | -6.52758 | -47.43183 | 2025-08-10 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7762bab-a74a-3621-a13e-1cd236647a52 | -5.2056 | -45.618 | 2025-08-10 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41151e21-287e-3781-a9a2-6749ea240310 | -6.67288 | -44.73334 | 2025-08-10 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9475ffdd-a0ec-39b7-a8ab-81928e3d2674 | -7.70968 | -45.49413 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6057503a-de61-3730-b1bf-d566c3ce76a2 | -10.45915 | -44.33212 | 2025-08-10 04:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ed200b4-b86d-3d0b-870f-cb67a2e4be81 | -6.98284 | -44.80775 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b5e3ee0-501b-3f44-9f1c-b44fd6cc02dd | -4.29727 | -48.0698 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c97681db-1b3a-31d9-ba86-a281d6795333 | -7.29152 | -44.15768 | 2025-08-10 04:21:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c08285a9-0353-3604-9adc-60e3f1f8bde7 | -9.48911 | -46.28 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7e5e1eb-be30-3ef3-8d21-dd08291ba914 | -7.88989 | -43.54552 | 2025-08-10 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3caf733-996f-3b0c-be01-557e20ed4fa0 | -11.73235 | -45.01508 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f679eaa6-f7ed-33d9-95d9-09ff1d6fb503 | -5.58999 | -51.1298 | 2025-08-10 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5565d6ba-3ce0-304a-ba03-f67334fc1bd8 | -7.88933 | -43.54914 | 2025-08-10 04:21:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95bd537b-4624-3dfb-b8ba-5c4f2662f2f6 | -9.5205 | -45.42614 | 2025-08-10 04:21:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58492f25-47bb-3f17-be48-8debbec25efc | -8.0749 | -46.85132 | 2025-08-10 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6a578c9-6bb4-3e3b-86e9-636ea8d6f814 | -4.31468 | -48.08201 | 2025-08-10 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a13a2546-b835-3e4c-b130-1d9a87ee8e46 | -7.51551 | -49.55925 | 2025-08-10 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9989f387-47da-34ed-865b-c469b96f84ef | -5.99425 | -44.27435 | 2025-08-10 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0daf05be-6e0d-3443-8cb2-fb8232b430f7 | -10.41553 | -50.38123 | 2025-08-10 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c94d9123-cbba-3788-a3a5-ed1b1c3cf4ed | -6.19466 | -45.44349 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 27a57c8b-36cc-37e2-9a40-cde2fcaacf90 | -7.88707 | -43.54137 | 2025-08-10 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61fdc46f-b8f4-38ac-84f4-0ec4aa8036e1 | -7.15995 | -44.06542 | 2025-08-10 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2fef7ea9-7c4c-32df-adb0-14207deff540 | -9.57318 | -48.44269 | 2025-08-10 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28ed408f-fb1c-3cde-b18b-5a9ad467123c | -7.87584 | -45.55337 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a70cede-465d-339a-ae7b-f2cf089a43f1 | -6.97605 | -43.85643 | 2025-08-10 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c280eb4-2327-3114-80ce-c8ceca383d5f | -10.49978 | -44.87806 | 2025-08-10 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| afaff016-c914-3b9a-8823-4bc6746902d4 | -6.94703 | -44.56026 | 2025-08-10 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a08b48aa-0ef2-35b8-a91b-eabcedf55fc8 | -9.48576 | -46.27946 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7adb9b30-cb4d-3a7b-a18a-c72bc327f5f2 | -9.49686 | -46.29586 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35735eba-5058-36d1-8d10-6b0d9d2ae73a | -7.68 | -44.86804 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcc65069-c0ec-3845-9557-01a4a00f0097 | -7.703 | -45.53609 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 028024e8-82a8-3910-be7a-ee85d9d4390a | -8.50008 | -44.75594 | 2025-08-10 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a556cca1-e535-3645-b54b-e57b13ac6e4d | -10.35505 | -46.6263 | 2025-08-10 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f62677c0-e7e1-3b7c-a428-339915ee32ec | -3.84069 | -47.74657 | 2025-08-10 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1e0d122-6003-300e-a285-4c6a29a485ae | -4.06277 | -46.93549 | 2025-08-10 04:21:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 394ff152-971b-3686-98b1-992c0be86fb1 | -10.41857 | -50.38048 | 2025-08-10 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6ab8022-60d1-341e-97f8-60aebcb70d5b | -6.19188 | -45.43942 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ab3d112-81ba-3c46-9b5f-0ec5f03d7bc3 | -10.96037 | -44.85312 | 2025-08-10 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f57a1006-39ab-3fc4-8abb-8ccff8f3f7b2 | -9.49466 | -46.28819 | 2025-08-10 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5e58246-bb6b-3023-87e1-d6b4c3a44bce | -6.24511 | -42.78521 | 2025-08-10 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c73538c-5153-34b4-8aaf-989be15cb9fc | -6.97239 | -43.72571 | 2025-08-10 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9e2c053-71f3-3cb4-ac32-7698cd6f8797 | -7.286 | -44.17115 | 2025-08-10 04:21:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48bcbd76-54f4-385f-a426-a4a5ff31d162 | -6.27706 | -43.70158 | 2025-08-10 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 943c4f90-6bce-3e8c-bd4b-217f3078bb40 | -8.98142 | -45.6912 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a04c719-af88-3ca0-819a-ae27e08f830b | -7.70188 | -45.54311 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
