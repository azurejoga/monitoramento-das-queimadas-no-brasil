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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53050590-9cdc-34e8-93a3-7119e0ab4f8c | -12.53074 | -38.49738 | 2024-10-13 03:47:00 | NOAA-20 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b77de6b1-1bd6-33c9-970f-04d31c8999d3 | -5.7951 | -38.3312 | 2024-10-13 03:47:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a016a08f-611a-316a-88b2-a3235591672d | -5.76355 | -37.56625 | 2024-10-13 03:47:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a92d750-a9db-3c6a-a3aa-e104dfb8a187 | -5.33717 | -37.79242 | 2024-10-13 03:47:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16302449-393e-376a-a873-cccc88f229fc | -7.59798 | -39.05189 | 2024-10-13 03:47:00 | NOAA-20 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2749d7c9-af87-38c0-9856-d659fcc0eedb | -7.26703 | -39.01486 | 2024-10-13 03:47:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c446fdc-9c6a-3380-9e1e-024b8cfb0add | -7.26641 | -39.01863 | 2024-10-13 03:47:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f25f99de-e932-373e-89fb-372eea09cf36 | -7.26359 | -39.01432 | 2024-10-13 03:47:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 055a735e-9bcc-3919-a593-a01df4646490 | -6.65833 | -37.47465 | 2024-10-13 03:47:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 337f98d7-00d0-3739-bc8a-c724a2db1937 | -6.65778 | -37.47816 | 2024-10-13 03:47:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2633ca35-0e8a-3708-adc8-8d091f354fc5 | -6.65612 | -37.46715 | 2024-10-13 03:47:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a75bdd01-6b62-3ebe-b3b6-f1f7cc41ce6f | -6.65557 | -37.47063 | 2024-10-13 03:47:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b8af364d-440b-36a3-88c3-606ff554c895 | -6.54442 | -38.86356 | 2024-10-13 03:47:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa99249d-5609-3e23-a45f-24694652f386 | -7.88689 | -39.15116 | 2024-10-13 03:47:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 57e5eb9e-e876-381c-9df2-5aebfd2d91cf | -7.88628 | -39.1549 | 2024-10-13 03:47:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 950b3f89-63a0-3b06-b45c-2258f437f80a | -13.03786 | -39.92969 | 2024-10-13 03:47:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f90890c4-eba8-3e8e-9d30-d44ed350fd59 | -12.72013 | -40.21817 | 2024-10-13 03:47:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| be4524f9-922a-3606-a3a3-83e87d13cb29 | -12.7167 | -40.21759 | 2024-10-13 03:47:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f1ad3cb1-60b0-35ab-a1e9-71c14d31847d | -14.52184 | -40.34017 | 2024-10-13 03:47:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1be1e0cb-56b9-3481-9c31-fc2b5ba13218 | -14.52123 | -40.34392 | 2024-10-13 03:47:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f697aa52-f271-34fe-8617-9f94a26cb6bc | -4.78067 | -39.77224 | 2024-10-13 03:47:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80fba7dd-efc9-3f54-a124-e25914bfe17d | -4.77997 | -39.77655 | 2024-10-13 03:47:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dbddafb2-20f1-3d4c-9643-3afdab552fa6 | -5.8094 | -39.55122 | 2024-10-13 03:47:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 41f871ad-23d1-3ce9-ad95-457c1bb24571 | -5.50687 | -39.56455 | 2024-10-13 03:47:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95f5b700-0cca-31f1-8f6d-b20f5a47f9c4 | -5.1412 | -39.81352 | 2024-10-13 03:47:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93358df2-df2f-3c9d-b135-1e4d1e0f06fe | -6.75663 | -39.71999 | 2024-10-13 03:47:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1df055f-57b2-38e1-988b-711a8b6ff12b | -6.75598 | -39.72401 | 2024-10-13 03:47:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e9dcec8-e95d-35de-86bf-cf06ad6db5d7 | -6.51944 | -39.68401 | 2024-10-13 03:47:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9723ed2f-2e7c-305f-be32-e3360afde907 | -6.51523 | -39.68742 | 2024-10-13 03:47:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ebdbb75b-a3bc-38fe-961c-173a5ff30ebc | -7.81238 | -39.46536 | 2024-10-13 03:47:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ddc15be8-d0ba-3b02-bcc2-e3c71138ee33 | -7.80764 | -39.47256 | 2024-10-13 03:47:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7d0df65d-44d4-3e97-ad4a-02638b6757f2 | -7.72345 | -39.2536 | 2024-10-13 03:47:00 | NOAA-20 | CEDRO | PERNAMBUCO | Brasil | 2604304 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| afd610f9-c0a0-3e8f-942c-6dc5e39b98e9 | -7.39048 | -39.14249 | 2024-10-13 03:47:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46bd4498-e55d-3ce0-906c-fc4ccb6ca461 | -7.38701 | -39.14204 | 2024-10-13 03:47:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 89982e98-b4e1-3b89-a709-d553e3955b66 | -7.51451 | -40.51783 | 2024-10-13 03:47:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16f14385-ebfd-37c1-a000-ae648fd43c3e | -7.51382 | -40.52205 | 2024-10-13 03:47:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 29deb64f-4db3-3b39-8358-fae995eb5984 | -7.137 | -40.07637 | 2024-10-13 03:47:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34986225-49ec-3bac-b9ef-b139e9c17b48 | -8.07443 | -40.80081 | 2024-10-13 03:47:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 27443928-15e9-31e5-913d-f9eb5bf6a799 | -10.73933 | -41.32656 | 2024-10-13 03:47:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b00e09b7-a365-3fc2-aa87-e5ad8d100197 | -13.28586 | -41.90867 | 2024-10-13 03:47:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 70c9beb9-0c35-3f82-a615-44351bbe01dd | -13.28221 | -41.90791 | 2024-10-13 03:47:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2a87a4c6-d18b-3acf-b2e4-d2331af0461f | -13.28142 | -41.9126 | 2024-10-13 03:47:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ace3eca7-29ee-37ce-a416-63667df70f9e | -12.66668 | -41.46535 | 2024-10-13 03:47:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3c407200-e455-3c95-a278-53ef5ef2169e | -12.39709 | -40.56213 | 2024-10-13 03:47:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0a436831-c18e-30bf-a6fb-9d6e3a87f1c2 | -12.3951 | -41.4099 | 2024-10-13 03:47:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e62f473-0d93-3257-a050-9f038e24a738 | -12.39475 | -41.40682 | 2024-10-13 03:47:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b5b637c1-4cab-3fde-87b4-b8f2d5052abb | -14.08241 | -41.76714 | 2024-10-13 03:47:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dbe61262-9d31-340a-9613-39814f841df2 | -6.38723 | -41.59428 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c79593ef-0270-3134-a14f-0f33557505bf | -13.13578 | -41.97303 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fb32379b-8f52-3f11-a9e0-ecb8570050e5 | -3.44305 | -40.58117 | 2024-10-13 03:47:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca5ee6ad-8d3b-3fec-993d-e74411bd73c2 | -4.01561 | -40.39833 | 2024-10-13 03:47:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3745ea96-edcd-37cf-897c-94d1df18a774 | -4.76269 | -41.54247 | 2024-10-13 03:47:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 954414d3-3023-3be4-8a8a-b3804235c9c3 | -3.72207 | -40.71855 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| a5283580-0dfb-3e25-8155-435d692d6b41 | -3.71845 | -40.71685 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 8acc8498-e57c-3b36-a5db-591de5221a88 | -3.71815 | -40.71793 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 1a9c6723-4964-3029-8aac-9d3901509e50 | -3.71766 | -40.72187 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ac85f709-14b1-3418-95c5-a31508605aec | -3.71733 | -40.72292 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| ae2923be-c30a-3b92-af47-dfc88d18f7b9 | -3.71687 | -40.72686 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8533de9e-b195-3316-8b33-26fb0d97c911 | -3.71651 | -40.7279 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 7922ebb0-a8c4-39e4-a2fb-069bc0bfe29c | -3.71506 | -40.7123 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e6b72d54-3944-33f6-8113-8f506bfbc7c9 | -3.71453 | -40.71625 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 3da176de-3980-30f1-8d28-78b6497f734b | -3.71423 | -40.71732 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 554c5c83-7264-3c22-85c4-29baaeb66330 | -3.71373 | -40.72126 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7c79872a-c8dd-36cd-9ba2-ec4f25d651a2 | -3.7134 | -40.72233 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e02f80a4-db0c-362f-8e5d-3d750b54d7e4 | -3.71294 | -40.72626 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cf82bb90-9044-3c09-9427-d1d6d62699ed | -3.7106 | -40.71563 | 2024-10-13 03:47:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c1ed415-0b11-3a07-bcee-f7719757b7e5 | -6.39798 | -41.70053 | 2024-10-13 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6bdd8659-180b-36cd-99ab-cbbc8295913d | -6.39738 | -41.70406 | 2024-10-13 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1382344-74ce-3b7f-b3b9-400f93be38fc | -6.39278 | -41.70693 | 2024-10-13 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab1447ef-16e6-39f6-951f-59fbde737931 | -6.39003 | -41.60188 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5814a622-23b1-362f-94ac-20d0289f0683 | -6.38944 | -41.60535 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 84a44211-dfd8-3622-9cfb-98c81071a3a9 | -6.3891 | -41.59466 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5ed05292-a375-38e1-a56f-b2cae8666b98 | -6.38853 | -41.59813 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f8c7f364-7e6a-3a1d-a231-96de3416fbf1 | -6.38841 | -41.58739 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a93c7a74-f3a6-33a4-b576-b9b6a6f2c04f | -6.38797 | -41.60159 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fed0eaf5-763e-3abc-9a8d-b7a3eccadb56 | -6.3874 | -41.60506 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e14c54e5-588b-3b72-806b-d4eb0d048a38 | -6.38664 | -41.59774 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 108560ae-7665-32ea-9120-eeea8c62c9bc | -6.38624 | -41.58707 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ef3e5327-d3a9-3cd1-b000-fa0e2cf9a4ef | -6.38606 | -41.6012 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 04de203d-f2ad-388a-ae3d-6b4954b823db | -6.38547 | -41.60466 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 52cb706d-e7dc-355a-951e-1ddb2946ddef | -6.38512 | -41.59399 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5bee5e5d-9cd4-33d4-a910-016106ce82c8 | -6.38455 | -41.59745 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 33525382-1055-3fa4-a480-aa9e12058c0c | -6.38399 | -41.60091 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f33bb70e-8ed4-3759-a9a6-2b7a23b76555 | -6.38343 | -41.60438 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 80c2f4bc-e8b0-34ab-929a-08cf068db61b | -13.13422 | -41.98216 | 2024-10-13 03:47:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45d0c18b-8fd4-3c6c-ade0-1c3938a36f9e | -6.3817 | -41.58986 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad65c488-b882-3e7a-b7db-5ef5865c1a11 | -6.38058 | -41.59678 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9abe621-9b5d-34ea-b169-039e9b0d78bf | -6.38001 | -41.60023 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bb7b8598-7aa2-32b7-977e-f8ede3d6f2d8 | -6.37945 | -41.60369 | 2024-10-13 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39421b3f-3140-31d1-bf4c-114839c8e691 | -6.16574 | -41.78982 | 2024-10-13 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72cb91e1-b309-3d57-be12-b11300a2edce | -6.16114 | -41.79247 | 2024-10-13 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84967fc1-5865-3e48-8d57-7d817b8bf18e | -6.15717 | -41.79137 | 2024-10-13 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be29110c-4ec1-3fdb-a722-d931aca1882a | -6.15656 | -41.79499 | 2024-10-13 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5a380010-1b15-3436-83a6-b3b4ebe3e2a2 | -6.02409 | -40.44769 | 2024-10-13 03:47:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c4ee0017-42eb-341c-ab30-7e1c47e4e630 | -5.63859 | -40.69814 | 2024-10-13 03:47:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9d3141b3-4b4a-31d1-837a-29473b9aaf97 | -5.39777 | -40.34669 | 2024-10-13 03:47:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0045c2b0-01c7-3778-8d99-b6eaf2c57a4f | -5.39696 | -40.34442 | 2024-10-13 03:47:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d1ac2feb-82fa-33df-b320-c94ded36a318 | -5.39624 | -40.34895 | 2024-10-13 03:47:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b49122f5-223a-364f-a965-cc2156a4fda0 | -5.12595 | -41.69232 | 2024-10-13 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bdf627fd-0f1e-314d-a43f-7836789c43b9 | -5.12248 | -41.68792 | 2024-10-13 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README38.md)
