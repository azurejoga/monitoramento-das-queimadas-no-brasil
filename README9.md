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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23b988a3-910d-389c-ac1c-3ac590380e42 | -6.79739 | -45.96201 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 476e72f4-8fc4-31fb-80e8-f656e1d54402 | -10.21546 | -50.3574 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 1cf1941f-c863-3b5a-a2d6-ee4c1b0cb3b9 | -4.52653 | -46.06545 | 2025-10-02 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9a429f4d-c1ed-359c-92b1-f198f23d6e6e | -3.80928 | -51.32609 | 2025-10-02 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 67897fd5-f3d9-31fe-a6bf-37bfb22c9c6c | -5.97449 | -44.60162 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e5cf4eab-fa73-3b3c-b4be-ba9f91ec5985 | -6.68943 | -46.0519 | 2025-10-02 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a7353059-76b6-31e0-8147-c9eeb48e81e4 | -6.39123 | -43.87713 | 2025-10-02 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| c17ccad0-d657-35d5-8cee-6ebd3b839793 | -7.26492 | -48.48228 | 2025-10-02 00:13:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ccb07b2b-d52a-3d8c-8703-c87a4038ff77 | -4.25621 | -48.56639 | 2025-10-02 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e6d561b6-35d5-340b-98ac-ea67a67dc491 | -3.94793 | -41.59859 | 2025-10-02 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| b364247f-3d43-3412-9925-6d905daedd6c | -4.99043 | -45.27537 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a0ecb91-773a-3644-92bb-4b0c6ff80e46 | -7.56593 | -42.39725 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4b40cda2-01b8-324d-a894-c4d574af2580 | -4.1362 | -43.83619 | 2025-10-02 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 451ebb9f-7efc-32cf-840c-d0b0823dc2d1 | -4.04862 | -49.07672 | 2025-10-02 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 2e5ec4f8-a63d-3869-badd-1cd3c9dfd06e | -6.56648 | -43.87595 | 2025-10-02 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4e5107fb-f674-30c6-a612-b78a1e63ba33 | -5.19069 | -45.06336 | 2025-10-02 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a0633829-2e8a-3b35-ba26-52ad00d69bd8 | -4.58424 | -45.60884 | 2025-10-02 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 123a53e3-633f-377b-b0c2-2f85a394306e | -8.51584 | -47.80042 | 2025-10-02 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 532f20e5-6550-3bca-a6ba-6b7e806ec78f | -7.77951 | -42.53683 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 400.6 |
| 1ea67b94-bcae-370d-85a5-da30efe40249 | -8.90104 | -46.61861 | 2025-10-02 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c730bc47-8b2b-38c4-90f1-ec6365dbc899 | -8.38484 | -47.99691 | 2025-10-02 00:13:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d8b99a73-2111-35fe-b2af-92e30e3b643b | -6.54106 | -43.37049 | 2025-10-02 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1cd02dbb-2495-342d-9abd-08636958d3f9 | -10.22075 | -50.29152 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| bbd68c49-0133-3214-88f5-ab0eef28c04e | -7.77684 | -42.51802 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 17d90773-204e-3f33-8eed-4f9c17e46563 | -3.62622 | -42.77687 | 2025-10-02 00:13:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f3351191-b175-39a8-bad5-56e0cce80c8b | -7.42373 | -42.88788 | 2025-10-02 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b5e165e6-3d40-3240-8366-c73b9b373c18 | -8.57048 | -49.59277 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 51888152-1d14-34d7-961c-08b6dea28f4d | -4.05044 | -49.09035 | 2025-10-02 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 3f827c81-edbc-3495-a826-10b18ab82432 | -6.86254 | -45.62964 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed6870ac-1d5d-34b8-af77-ceb3f2068f95 | -8.58048 | -49.61507 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e5e1ef1e-bd87-3029-88c6-0d4f0fc6d8cd | -6.24018 | -45.32296 | 2025-10-02 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1096c7a0-48a7-3caf-9bd4-e2ed88c817d3 | -6.484 | -44.28652 | 2025-10-02 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbd61b28-6a62-354a-9f82-2da64a28a6ab | -7.55643 | -42.65485 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 7cc2954a-2f42-3c4d-b1c8-f38d67f8ba5d | -6.04322 | -42.44913 | 2025-10-02 00:13:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 05d71d06-b2fe-3d55-83e8-711ee55ee624 | -5.63685 | -45.9647 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 02694a71-09c8-3fa8-b54b-6a7de2f26798 | -4.31445 | -48.08385 | 2025-10-02 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 853e9032-9597-3e24-bde5-3bec139a04a3 | -4.42515 | -47.76635 | 2025-10-02 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ab858323-9f53-37b3-a919-c49567086d5a | -6.77366 | -45.58491 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3e3fcc07-2907-3075-925a-3c81f7485f96 | -10.18119 | -50.29636 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 85bdf220-d955-355c-91e0-dc954148bd0c | -6.78395 | -45.59304 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 6a0e38da-1b57-30be-bb50-ed01a4289d2f | -7.78457 | -42.50732 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 361ff1c2-95a5-3155-bbbe-b46a0a2dbebb | -5.40499 | -41.33578 | 2025-10-02 00:13:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 1de381ac-d964-312c-b58e-bcda1580f17b | -6.44507 | -44.80161 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dab6f37a-1f09-3b24-8b45-c55e7f3cc5ac | -4.11041 | -47.93678 | 2025-10-02 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cd0bb244-0019-3f93-8a41-bb9a4ea2b983 | -6.31479 | -44.11898 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e8f0d2f-373e-30a0-bd76-8037184a67a3 | -5.97015 | -46.18075 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 624274d6-fce5-3ec3-8c91-045dd8821c04 | -6.38242 | -43.87843 | 2025-10-02 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1b38940e-882f-3120-ba5c-085cd9b77309 | -10.19438 | -50.29474 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 145dddbf-dc06-3f0a-ac5d-43149038e241 | -4.25452 | -48.5537 | 2025-10-02 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 34c284eb-cbdd-3306-a548-085cee4781c1 | -10.2045 | -50.28692 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d94a23a2-1c28-38ba-a0b8-cfa7f8b148a5 | -5.63559 | -45.95534 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 834794fd-3fcb-3448-8c2c-c733c2e409fc | -5.2368 | -45.20153 | 2025-10-02 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 932dce05-46d6-338b-bb7b-e658929e377c | -7.55381 | -42.63617 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 00e9b881-7ce7-31a8-a119-82709f1e97f2 | -4.85328 | -45.22526 | 2025-10-02 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 00851f77-3028-3dc4-ad90-91fecfffa8c2 | -8.87729 | -46.58839 | 2025-10-02 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 518749aa-2560-3c39-998e-509df2cd17c4 | -7.01375 | -44.50755 | 2025-10-02 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 475c783a-9110-3b25-80e9-42fe1c839469 | -6.38119 | -43.86962 | 2025-10-02 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 8ef2326a-9138-3087-b88f-446f2e1a4340 | -8.50365 | -47.78891 | 2025-10-02 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 67d93e86-4e3a-3cdd-8074-a6bf8ff792fc | -7.36397 | -47.04264 | 2025-10-02 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9b7cc6f5-5679-3749-a596-603158bbd304 | -8.53067 | -44.68669 | 2025-10-02 00:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c1225b63-eaeb-3147-990e-38368d2cde25 | -8.48357 | -40.60125 | 2025-10-02 00:13:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 92ab50de-5e53-3195-b822-5d5f33459629 | -3.76456 | -41.03819 | 2025-10-02 00:13:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 62b342e8-ec80-3be1-a3e2-0de6b85058c2 | -6.63255 | -43.6884 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dfa461d2-8371-3a92-860b-0be684a586d2 | -9.0051 | -46.71075 | 2025-10-02 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ddf43023-2f78-3574-9de5-042b169a44a6 | -5.41323 | -41.32253 | 2025-10-02 00:13:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 26aea1cc-7b4b-36b7-8d0f-433a6fa274b4 | -5.31304 | -44.80923 | 2025-10-02 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 8a380378-abda-3040-9e88-ea997f27fd0d | -4.31604 | -48.09552 | 2025-10-02 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| dac1e3e9-7991-375a-b74f-e389c3482aca | -6.41218 | -43.36733 | 2025-10-02 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc496f95-7d2e-3d31-85bc-4ad877ab0c32 | -3.95789 | -41.59709 | 2025-10-02 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f521fcc4-e5a1-3256-8feb-5c10c825af7f | -5.99125 | -44.57501 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 521daa52-1b10-39e0-8088-aa83437f6f18 | -5.823 | -42.78365 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 378110c7-0a0c-3047-9341-a38f52240535 | -5.83078 | -45.76447 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3410df0-7786-3d62-96db-c0f0ab7d7f3c | -5.97327 | -44.59282 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ecb9c734-b5be-3bc7-aee9-fdfdb5d7ce3f | -8.38316 | -47.98366 | 2025-10-02 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ffc5735d-06fb-3f95-a743-94d9129eb504 | -7.0265 | -44.46969 | 2025-10-02 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a222fefb-55af-3231-aa1f-22e67dea343a | -9.70624 | -48.95403 | 2025-10-02 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3530d720-40e2-3171-81c4-b84ed92fae84 | -10.20695 | -50.30828 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 672ef1fd-b65e-3ca1-8bca-f5e48f71df1c | -5.98452 | -44.60919 | 2025-10-02 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| eaf41c5e-4041-3d19-9cec-5dcc80d6d506 | -6.4683 | -44.43239 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 69a3c558-7061-38c9-8a1c-519dc2d37a87 | -7.60587 | -45.40514 | 2025-10-02 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7067d20-49da-3659-a5f2-520a6009913d | -5.92788 | -44.86593 | 2025-10-02 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b94ff0d8-a051-3873-93b6-d49673f0a264 | -6.5405 | -46.52691 | 2025-10-02 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04e93299-c29b-3707-a468-64f535ae1241 | -3.68733 | -49.041 | 2025-10-02 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 47bb8bf1-e3af-3e81-a62b-faa7e0e70f6c | -5.59216 | -46.24774 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f748c528-e23c-3034-a7e2-108235f74118 | -9.185 | -48.53363 | 2025-10-02 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fccba500-e6ad-386b-a121-7fcac04cb895 | -3.81984 | -49.09898 | 2025-10-02 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 472689d1-7f66-3cdb-9a86-eb381b92feb8 | -6.29106 | -44.07742 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e41d8c6-60a1-39af-8000-fa8f64f1dd57 | -9.4487 | -50.91242 | 2025-10-02 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| b7d24d7f-e9ff-3642-8c0e-167f8767882f | -4.42367 | -47.75532 | 2025-10-02 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 56d3de1f-b00f-3b1a-8940-19ce3749fa28 | -5.23802 | -45.2104 | 2025-10-02 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4aea57a0-0889-33cb-aef9-0faad7e2edfd | -5.79658 | -44.90884 | 2025-10-02 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cbade64-7355-381f-bee4-09e3366d5197 | -5.884 | -45.81718 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b61bbda-a26b-3e9e-83a8-e5f06cf2b916 | -7.66268 | -47.2944 | 2025-10-02 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4706f2b2-2947-35f6-9b51-96f0e93f60ea | -5.82577 | -42.8697 | 2025-10-02 00:13:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 367641f8-6c61-3990-921c-ab0628faf7c5 | -5.99246 | -44.58381 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ccebbdd4-ec4f-3a05-ae91-94e3ff29c111 | -10.20756 | -50.29313 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 0fa8156c-47a7-35ae-ab82-d7387f4164e3 | -4.90584 | -45.73894 | 2025-10-02 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4159d648-dc7b-337a-9052-479809738f15 | -7.55682 | -42.39859 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7025c293-4c22-3bbb-85ea-fea4236379cd | -3.68912 | -49.05429 | 2025-10-02 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 597d9fe6-c31f-36aa-abca-8bfa5ecc27fd | -3.96782 | -42.10761 | 2025-10-02 00:13:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |


[Clique aqui para ver as próximas entradas](README10.md)
