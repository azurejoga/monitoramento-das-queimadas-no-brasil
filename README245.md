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

## Dados Diários - Página 245

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c02090ca-74c5-3622-9729-a4df138b4056 | -6.98979 | -43.21068 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d1608c8b-de46-3de0-ae0b-95fe426159d4 | -8.95559 | -45.15345 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 03401e64-fec8-35c4-b3ce-e95cafe55b5d | -6.37905 | -42.52866 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1e5d8f1f-3a08-3f96-b427-83eb368b3ccc | -7.87624 | -44.1495 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4a880e88-9e2f-344a-a89e-088ea01e29c4 | -9.80911 | -44.77908 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e7f66a9-d403-332c-8ef6-a28f948f995b | -6.33357 | -43.82968 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 09b09d70-e5b1-3f87-895b-d564b4fedc2b | -6.83638 | -39.54996 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 7f52e308-63d3-3345-8ad9-e434f5493c5d | -6.92867 | -43.67136 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| c9ad1c17-cab2-3120-b8b0-5cd1400f8c72 | -9.10451 | -45.12359 | 2026-10-08 15:41:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f9de6d1f-0527-3498-8493-f406cfc60345 | -9.88451 | -44.85465 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 2cb95b65-9702-37b5-a56c-304840c4069e | -11.14073 | -46.13044 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ad2362db-52c7-3faf-bdba-b619111df729 | -11.05932 | -45.85168 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2f613cc0-e386-31b1-966e-58d6482a36e8 | -5.95833 | -43.90088 | 2026-10-08 15:41:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ca41cca7-fa3b-3390-883d-1f8814acd5b0 | -6.15915 | -39.44506 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 745702ef-e891-3648-9ecd-9f7665fbeb43 | -10.1611 | -39.9084 | 2026-10-08 15:41:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 45c215b3-2a56-3bec-8691-f5568bb21fbc | -7.08325 | -41.50586 | 2026-10-08 15:41:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc844053-6849-3dd1-8eaf-75dbb3ee5a8f | -11.27286 | -45.20378 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 1f86296a-b787-37e8-a115-a6b4364ff78a | -6.33226 | -35.15928 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| ea667e04-0979-3a19-89b0-559184a9136b | -9.52143 | -45.60604 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a0e2b0f0-a83c-3c4a-ad14-98ea5936ae6e | -8.93926 | -45.18431 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 7fb9125c-2563-3eae-921e-dd7ed61f9e62 | -9.90628 | -44.81667 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 50110ed8-46d0-3c98-8c5b-cefb82f32a6e | -7.47281 | -42.84195 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 089a7d06-12f2-3d1b-96c6-3067129ded03 | -6.0159 | -42.26209 | 2026-10-08 15:41:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0cbc5dc7-d0ad-301a-b82f-d8cd57355b5a | -5.98536 | -41.3606 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 055486f4-6426-36ea-ac49-e88aeff85d2c | -6.82151 | -39.54196 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1db14d1c-fe88-33c6-b920-71fc9ae2061b | -5.77027 | -42.06949 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| afa30515-8718-31ae-9317-c0b893757908 | -9.94187 | -43.56769 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 62705ead-2a18-3621-b3ae-06c823e031f8 | -8.94449 | -45.17213 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6db2139f-84cf-3b0d-94b7-22bd86287578 | -8.88818 | -45.6073 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2c8a3506-e8b9-331b-b80e-9e05e0af0fe8 | -8.19506 | -45.78995 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4838f7df-9613-3ed5-8900-0ff95619aa53 | -5.23716 | -40.57702 | 2026-10-08 15:41:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 42d88f8c-8bba-34f8-b0b7-31c521a8ec6d | -6.0528 | -42.59568 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 13d0c89c-93c8-349a-b354-5ecdf9eb25c8 | -6.15068 | -38.33939 | 2026-10-08 15:41:00 | NOAA-21 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5e84fc36-6d54-35e9-9d74-f7df6b528bd0 | -5.76943 | -42.06335 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 564c3a1a-8dc2-3c03-9f2f-4b3c195c19a2 | -6.15854 | -39.44091 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3b167586-ba68-3d3b-9fa4-aed415b5d422 | -10.37683 | -46.32149 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dd57fe2e-6c58-3ca7-81e0-556288407466 | -5.48351 | -44.60635 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5efb4fe9-0085-384a-ba14-e1f624a21270 | -5.71793 | -41.64989 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| d985fb2d-ef99-3ed7-8728-07a7a3b94cf1 | -7.18782 | -44.33313 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0df358fb-9de3-3417-8895-23130a9b39bf | -10.8711 | -45.5462 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c9b8db46-3389-32b2-b077-735a370291d9 | -9.26124 | -40.26576 | 2026-10-08 15:41:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 276e2808-2e3c-3be9-9924-8cb5c2604be5 | -7.76598 | -39.41634 | 2026-10-08 15:41:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 63.4 |
| cf5a4147-dbce-31df-85ae-5f4c923f6211 | -5.92775 | -44.2803 | 2026-10-08 15:41:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 988f3896-a1b9-382e-9287-514bb6c65714 | -9.26577 | -45.63568 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 70bf14f1-b68a-39c0-977a-146fc3818ea6 | -8.2006 | -46.40399 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 386.6 |
| 04f9001c-114c-3f13-a6b0-f6383cc76ef4 | -8.68021 | -41.18708 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 848a63d2-13a4-3e21-9e72-cf25085d9c4c | -8.93655 | -45.16161 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 195.0 |
| ac6e58e5-086a-3d67-9c33-e3e4a14aeb8a | -9.90296 | -44.78905 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b12b4ac1-ef9b-3df2-b883-e0e1bc234c39 | -6.85445 | -41.77184 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ee78fcef-3654-3f18-bad5-dc43581965a7 | -5.51882 | -35.92673 | 2026-10-08 15:41:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 56d6af2a-9709-3ad8-b5c2-87a6a7b89d68 | -8.96749 | -45.14161 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7f1a28c9-ca6c-352e-8fb5-797855a46a49 | -5.96371 | -40.91721 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 3f04744c-c10c-3e5d-9705-5bb805cf8d58 | -8.94046 | -45.13855 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f34d10be-c7aa-33fc-a915-55f33081d8b6 | -9.90362 | -44.79454 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d93176f5-1309-3b5f-bb91-93de3d789028 | -6.85067 | -41.74435 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| 745313df-15e6-31af-b42f-4dc020fdeff5 | -7.26731 | -44.22182 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1368828e-9b51-358c-a5f7-39b40183b94c | -5.95963 | -40.92287 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| d8e8d4e5-a32d-38ea-9549-c83dff1b2771 | -6.33975 | -35.13931 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| d61219f1-d00d-3466-ba1f-1458039329da | -6.70325 | -45.29235 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d624d51a-adb8-3e4a-a200-5e6b8eb8976d | -6.35997 | -42.57235 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 00ed69dc-fc3a-3414-95fc-4189621950cd | -6.15294 | -43.38346 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45881f24-846f-333e-bacd-aea05c62bcad | -8.20582 | -46.33189 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 76c6804a-c794-3951-bf13-1c1358b64112 | -9.14664 | -45.81955 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6e9f3834-fb83-3d26-81c6-7fb066573083 | -6.38583 | -42.53835 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a220a4d5-994e-36ef-94c6-f2304d10f8d8 | -11.26797 | -45.20189 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4eca8a2f-916d-335d-90b8-d86ea62d3f31 | -6.1937 | -37.86001 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ae8138f8-7414-334e-b86e-0e3df3b3fa56 | -11.11036 | -45.67791 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| fcdc451c-aabd-3f8e-ba50-3ccfc29d14e4 | -8.59723 | -45.62637 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9e32bfb4-1e65-3614-bf8b-b9ec21a4a1a9 | -5.77291 | -43.32944 | 2026-10-08 15:41:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 676621e8-2434-3d88-bf1a-6df8d92e94f5 | -7.31493 | -44.0058 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b8ff2fbf-3ac5-376e-a785-5985269a41dc | -6.46686 | -44.03296 | 2026-10-08 15:41:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8afed17b-724b-3c34-a36d-97007481df27 | -6.96909 | -43.44271 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f07769cb-01ec-3c3b-a0bd-e000bf10bd38 | -7.10183 | -45.24697 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0297a22a-a116-3d79-9c45-0fedc47b8f2f | -6.59577 | -44.8549 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 71e9a663-9e1d-34fc-8759-1620a7f236ee | -6.88469 | -43.69774 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b02bb8c5-7b0a-36f7-b50c-78769e6b604c | -7.31215 | -44.00567 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7aafb198-0a57-34e0-9154-da16febbaf91 | -6.18982 | -37.86066 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 7e0737c4-8420-3dad-9bc8-553fd6daef26 | -8.19727 | -46.37722 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 83cfdd63-bcce-3211-83cc-97a099b2b176 | -5.73593 | -41.77479 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1d7cd7d0-1691-3420-add6-142eccff0da7 | -7.07208 | -40.94125 | 2026-10-08 15:41:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2b5d4f30-156f-30ca-82b2-e609738f47d8 | -8.8921 | -45.38914 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 0bb4c1da-126d-33f8-b349-7b0ec9ebbff8 | -11.11247 | -45.7024 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 28b4c65a-ef4b-37e9-9f51-ad04fc2fbf68 | -10.56876 | -46.29039 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 597a1d04-6a5a-3cf2-8293-de21581c2b34 | -5.02213 | -42.44149 | 2026-10-08 15:41:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 615fc74b-67a3-3406-872c-121bc764ed3f | -8.94111 | -45.14402 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 82d48703-ded8-32c0-b738-a9564146a0a5 | -6.32331 | -43.48965 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e49233e-5d27-3d18-b76c-b9f96e5faa6b | -6.23244 | -43.74006 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7739a35-059b-3b96-89dd-e2efa224034e | -6.59631 | -37.8994 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 216.4 |
| f0cd22d0-d547-39ff-b52c-09e499c0025a | -10.34085 | -46.22943 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| dd5ec415-d845-3bcf-8e49-586bd81d3e18 | -11.26321 | -45.17981 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 65fe6d4f-1db9-3c6f-9495-102d5da305fe | -5.73551 | -41.77188 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b2b9c58d-8db0-327e-a980-3a040febfbab | -5.87096 | -45.96048 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 97a27bdf-2e96-3adc-ad09-3a36d977bdf3 | -9.7832 | -44.7827 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 06c41908-9bb4-3083-b274-7a71ee19f1a2 | -5.7466 | -42.06546 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f039442e-8799-317d-98af-2606be2d76de | -10.16938 | -45.97107 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5de5602d-61a0-3e51-9e6b-75004051bdda | -9.89033 | -44.84822 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 565231ee-5332-3a0b-9596-7db638268d89 | -7.18659 | -44.3238 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e64db7cc-eef0-3988-9204-564f25bcfcd6 | -9.52537 | -39.05199 | 2026-10-08 15:41:00 | NOAA-21 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bebecca3-2817-3802-9463-0dc94ee8a65a | -7.48765 | -42.82546 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a8c44096-bcd2-3e9a-89f4-d264de1314c9 | -6.33117 | -35.1519 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |


[Clique aqui para ver as próximas entradas](README246.md)
