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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55bd1a5b-4294-3efd-acbd-4fbeb2166d3a | -5.7344 | -41.75563 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70e651d3-eea2-3b82-badc-952ec63a98a6 | -5.966 | -40.91835 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6044b56c-304f-395b-8103-47f2a95987c6 | -6.6372 | -43.73141 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1ccfe9e5-4c5d-3628-9d16-9a3561f8b448 | -6.16101 | -39.44363 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 7defe6f8-96c7-3385-808d-c6164e643508 | -8.21777 | -46.33517 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4409b18-c45f-371e-b507-aab3f017b87c | -4.68259 | -40.82906 | 2026-10-08 03:42:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8b81b06-2b1b-3944-9218-be9be60bfc6e | -8.21089 | -46.3694 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17c781dd-47be-3858-babd-9bc9ef733470 | -6.16118 | -39.43417 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 6d005515-f547-3896-89c1-78a48dd9e9b7 | -8.73211 | -45.1717 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4037b5d1-fd0d-3a4f-aa55-e08d1d4d2c45 | -5.96545 | -40.92152 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f14a34f5-9414-3f7f-a86e-2d068a265b75 | -8.72669 | -45.16412 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| beea43cd-370b-39d1-b045-ce8da3a65d09 | -6.95352 | -45.26602 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11125ca5-7828-3d9f-99e3-c3322e5789a8 | -6.15622 | -39.44269 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f14f907b-6c6f-3c21-9878-efc639639b9e | -5.73413 | -45.15974 | 2026-10-08 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9322abb-f9bb-34ad-9369-91cd61d125d1 | -5.98983 | -40.93912 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e04130e6-a046-38ec-b8dd-10826ef9af04 | -6.84243 | -39.54805 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1ca6cfc-7323-384d-8b91-6e2276bafbfd | -5.71479 | -41.76766 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17de176c-a170-3430-a485-05f55d7fa5ba | -8.38458 | -46.2901 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 293cc6cb-a024-3e94-ab77-0a6d68044dc0 | -7.60548 | -42.38113 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3901fa1f-a319-3949-89ad-cbd2c059a819 | -8.71779 | -45.17444 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dbb661b7-2375-39b3-a09a-7fe27f0a8602 | -5.75011 | -42.06976 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a4e4de76-ba5a-3aec-9246-09d275c24523 | -7.47293 | -42.84573 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c60aa337-47df-33d3-93e1-175358eb5c97 | -7.2298 | -44.27208 | 2026-10-08 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69747577-a115-3514-b1a7-8cb19fdcc77d | -5.48274 | -42.86019 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1956575-93fb-3a0d-907f-1395456d3867 | -8.72898 | -45.15234 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a5f1a85f-f1f6-3e98-8488-7955fd76ad25 | -4.34791 | -43.8027 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 52cec5da-7504-316d-852f-ea9a17523cb5 | -7.0747 | -40.93963 | 2026-10-08 03:42:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c86c28fa-b38c-3b9b-8e71-7aae1f366f72 | -4.34235 | -43.79578 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 886687b7-0a11-393b-a4fb-bde84bee7f3e | -9.56333 | -40.33772 | 2026-10-08 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 74bcd4a6-713c-32de-b013-07b01cf43090 | -5.48442 | -42.84874 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 05720276-3740-38d8-9fb0-29021f234251 | -6.95231 | -45.27232 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9dad7bc3-acde-3aa3-ad8d-e0e569d2a958 | -6.15799 | -39.4323 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 642fbbd0-eef5-32c4-9b78-2b48acfe324f | -4.33915 | -43.80116 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fd90762d-1b4a-36dc-8684-b71207d33741 | -4.35641 | -43.79264 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 06651bf9-db80-380c-a4c7-fd391e9c12aa | -5.62518 | -43.04655 | 2026-10-08 03:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b143e54b-bbbe-338f-b553-89939e3f54af | -9.55935 | -40.33961 | 2026-10-08 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 85bdc45b-83e1-379d-a7bb-a697260a0cdb | -8.60498 | -45.64238 | 2026-10-08 03:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2538382f-8847-34c8-ba15-cc71ee0b3e3a | -9.55852 | -40.33683 | 2026-10-08 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1d67a5dd-c0c1-3e4e-ba89-dc1710dcf2fe | -10.24497 | -36.33228 | 2026-10-08 03:42:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 3afecfa9-f943-3f14-be75-4d0559392640 | -5.73287 | -45.16656 | 2026-10-08 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d8d1db8-39ba-3d39-a8d6-2b4876984f74 | -6.94261 | -45.28712 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29fbc975-8206-38b4-ba46-714ade27097b | -5.7566 | -42.06676 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fce3585b-d676-3f5c-9c06-8929fd2dbc02 | -4.72376 | -37.84351 | 2026-10-08 03:42:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d68e7f5-929c-3dd6-80cf-fafa7974b23a | -5.98925 | -40.94247 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bf36d4e6-aa9b-391f-8696-3348b8c27f7d | -5.7166 | -41.72454 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 309c4eff-66c2-34de-b4ef-9ae87928c0d4 | -8.39036 | -46.29824 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fdbd72d3-e9e4-3f5b-a36c-c9a0ab6df5df | -5.96656 | -40.91521 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd0bdc14-08fc-3933-94e2-9d6930dfd238 | -5.99041 | -40.93578 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0629a88f-eada-3cba-b9ca-659df0d80103 | -6.32346 | -43.3587 | 2026-10-08 03:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 045d23e5-acf7-38df-a035-ea406ffa8dbf | -5.98391 | -40.94153 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e63c43f-5874-3636-889c-0df98916ef0d | -5.75155 | -42.06175 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1773437-c46e-3b39-bc79-f8fd633aaee7 | -8.21553 | -46.37157 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f01c070d-b245-3daf-89a1-0fc34042c798 | -7.47216 | -42.84996 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6adf9d13-f7a8-3fcc-9a00-fc22ff8129eb | -6.94568 | -45.26975 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66663554-805a-3780-bf3e-39452d7c9ade | -6.62999 | -43.7351 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| c7ada7f8-56d6-3b35-959f-ecc2ed0b9192 | -8.39473 | -36.4664 | 2026-10-08 03:42:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| be874b7f-8a9a-3da3-899e-aa0ebb4d178b | -7.06886 | -40.94208 | 2026-10-08 03:42:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e768a2a-a576-38e7-acc5-5cd66d976426 | -4.34018 | -43.79548 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 411bcb4c-f7a5-3359-93bb-1fd3d500582f | -5.24787 | -37.58173 | 2026-10-08 03:42:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b7cec0a-7174-397e-875a-9c2ed4ba1f00 | -6.87742 | -43.69271 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a81638e2-aba3-35cd-8aaa-4f983917626d | -5.7458 | -42.06063 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18e9489a-2628-3fc9-952a-a99b4476d4e2 | -6.83206 | -39.55096 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35fe0adb-4be3-33d2-9567-4539cb29847a | -5.74651 | -42.05669 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1321a768-3433-3b7c-96e9-e154c88cc17d | -7.1999 | -45.35039 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1932c78b-61ad-3b99-a9c2-7505dc7b2466 | -8.38899 | -46.30512 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7229e90b-c006-3697-9f14-8176b8038b0e | -6.36028 | -42.57538 | 2026-10-08 03:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7c7fca17-c91d-34dc-a2ae-433c48f6e7da | -5.26378 | -45.40861 | 2026-10-08 03:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4afc6e07-5fe7-3c78-999a-55455e7f3c03 | -5.49048 | -42.85212 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0aa684e9-2efd-3276-87f2-4cfefead3b7b | -7.22874 | -44.27764 | 2026-10-08 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f196068b-9487-3a45-8e87-3e0b4a3635ba | -6.93215 | -43.65832 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 53636296-655d-3b5f-8ef9-09d97106d831 | -5.95839 | -40.93037 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34a48464-710a-30e1-86f5-085dc3b2e728 | -5.48965 | -42.85669 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f9b88c3-6e57-3b67-b36c-890378eccfc1 | -6.88908 | -43.69979 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a870d08-6f26-32a1-b59c-db3da20cf542 | -8.71088 | -45.20991 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6bd7ce4-9575-354c-845e-0d7a70a89c1a | -6.84721 | -39.54893 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3aeb6a59-174a-3703-8908-48580ff409f6 | -7.46548 | -42.85322 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 61c4f22d-d870-3c9b-b063-a8beb5378f24 | -5.9845 | -40.93817 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 839e2a3d-b3c8-35d9-aacf-725cd6e62f6f | -7.10151 | -42.53245 | 2026-10-08 03:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 378a939e-70c3-30f9-9b66-780d056f2864 | -8.60386 | -45.64805 | 2026-10-08 03:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 885ecc55-1472-3bab-aa13-45c43d988eb3 | -6.60264 | -37.89669 | 2026-10-08 03:42:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 151b73ef-3f0e-38b1-800b-8011e8edd3f9 | -8.38187 | -46.30378 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1ef8acf-5355-3579-8b89-1b956e9b798b | -8.21635 | -46.34226 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ae9b9a8-9323-3041-b9ee-aaa00d0672a3 | -8.71551 | -45.18616 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7de4cc9c-431e-31ac-a66a-e220d8d24d97 | -8.06162 | -44.81037 | 2026-10-08 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7695db48-b626-31fa-accd-488334092ff4 | -6.64247 | -41.71898 | 2026-10-08 03:42:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43713b57-40ee-3f5f-8672-2ea5aa715b52 | -6.1619 | -39.43843 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 6a621095-b559-3fdd-961c-5eeb60759053 | -6.16505 | -39.44028 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e7130321-9d3d-3494-9f49-5c15819da5a0 | -4.3467 | -43.79684 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| af067ad8-fecb-3561-af0b-cf9d2ff9e1e1 | -7.20547 | -45.35853 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2e240dc-f28a-3396-81a3-0f601d76e3bb | -8.71894 | -45.16857 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 61f724d3-b6a8-316a-9d80-343b509dcc28 | -6.88373 | -43.69365 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 410d1d13-dee6-3648-910e-335424177aad | -5.74939 | -42.07378 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8bb232cb-b6dc-3b4a-b3b7-38eaeff2562f | -6.94368 | -45.28134 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 469d0e38-beba-3bcc-83e1-f671ceb61dbc | -6.33053 | -43.35493 | 2026-10-08 03:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c4fd4db-6633-3865-856f-611409736252 | -7.06304 | -40.94449 | 2026-10-08 03:42:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2af651c1-26b6-3809-991f-ec61bddac985 | -8.72091 | -45.19386 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 567e4e59-3d7a-332e-8718-75f9d6d37b53 | -9.78966 | -37.32011 | 2026-10-08 03:42:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f1995f5-2a62-31a6-a1cb-0af63591309d | -7.07413 | -40.94286 | 2026-10-08 03:42:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09655d7e-9480-3e61-8b37-a1fff75338c3 | -8.72123 | -45.15681 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3334f563-8d58-3fde-92cc-8792c39ea5d7 | -6.94916 | -45.28867 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README58.md)
