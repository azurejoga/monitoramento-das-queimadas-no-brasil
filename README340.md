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

## Dados Diários - Página 340

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 525da182-fb80-3024-adbd-b7d7ca49c2e6 | -14.33006 | -52.78026 | 2026-10-08 16:37:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8e90df0-58b0-38f3-8b3d-c6a6c4917990 | -9.36265 | -45.94641 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 74750499-51d0-39d2-a714-780295a064cb | -9.71103 | -45.69316 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.3 |
| cde562e7-e70d-37bf-809d-416c3d97c52f | -11.8564 | -47.36217 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6b3ca325-8249-3b19-8496-4abb87270a3f | -10.07677 | -46.00671 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 566d9b64-5919-3472-a64e-1e5e9006f1d5 | -9.01188 | -45.13464 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 42ea33e1-26ef-324a-afbb-a2b5744174a7 | -12.22945 | -49.60833 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 739934b2-845d-3843-acec-d2bd5b72cc02 | -10.24965 | -49.67817 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7e7658cf-c3a0-304e-84cb-4923e1ae94c3 | -8.30755 | -47.64133 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 63722e18-30df-33eb-9c68-5570d9ed737d | -8.9299 | -45.17628 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 87df129b-ea8d-311f-ae57-727085698ca8 | -7.07489 | -40.94154 | 2026-10-08 16:37:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| c609e137-0b76-31d0-a5e8-566a120e79e6 | -7.03834 | -45.45449 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9d73a6ee-43ed-3458-a067-172a1b37449b | -8.94472 | -45.18467 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 960ddf3b-873a-3f71-b159-8020bb6f01af | -11.7916 | -46.77724 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6e655830-f701-3431-8adf-497958583073 | -7.87209 | -54.9679 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 983180dc-d11d-316e-9bc8-9271406e81fb | -9.2609 | -45.63253 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8962867f-a5e7-3dd1-83ec-ebb137c591eb | -5.75279 | -41.72623 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| a949ce7d-d93e-3877-898a-0f0c8fbd5d01 | -7.90443 | -54.71732 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 7cfdf1fe-9a21-30bd-8b3b-be0a50057880 | -14.35634 | -55.02831 | 2026-10-08 16:37:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dac7d3d7-90ec-3f8b-b9f1-0bd148d980ba | -11.7592 | -45.49017 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d57d21d9-06d2-3904-83df-391896da3798 | -10.15439 | -39.24798 | 2026-10-08 16:37:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| df5f3799-1839-37a1-b59e-5080dd2c9812 | -11.08306 | -44.01913 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d9a4fd0f-7a7b-3648-ba24-2bdf2fef1f11 | -9.14396 | -45.82364 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1686b5db-2978-33a2-8c2b-6b3645fdc859 | -9.89549 | -44.85534 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f2e35797-111f-39cc-8a7c-0e408304608d | -12.62347 | -47.89352 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a66f99a3-489a-31cf-a4d9-f0f899bc9f78 | -7.63793 | -44.37521 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 927b345b-0505-3a12-b1eb-403c9677f409 | -6.75856 | -45.13649 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 64601553-239c-3dca-ab23-b8a91d37d68a | -11.95769 | -47.77095 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aff656c8-8495-332b-88c3-493d46572c00 | -6.05617 | -42.59285 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f3e8fd3f-e3e7-3d34-9d8c-32ca0590f527 | -5.7747 | -42.0559 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 1c08ad52-5b98-3e21-8c05-fba527e7fb8d | -9.0242 | -44.37748 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ec6c6f4e-d1d3-36a1-b072-e63196454b7d | -8.28203 | -45.71029 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41f4df7a-812e-38f3-84eb-8c080dfa56f0 | -19.22674 | -40.68287 | 2026-10-08 16:37:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| be2af9ba-dd49-37c6-9c64-75baa1268620 | -6.66764 | -45.36172 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| accbab25-1818-36dd-9e20-4f806f235887 | -6.84794 | -41.76368 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f60626c5-cf56-3466-ad37-d66184463485 | -11.68232 | -43.68258 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e88c250a-6200-370b-bcd2-239aa6e55987 | -11.31018 | -46.68677 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| c5969960-3cc4-3487-85eb-483564066150 | -17.7837 | -43.9991 | 2026-10-08 16:37:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cbc9f95-7d23-38aa-9b96-bc079351f5f9 | -11.77917 | -45.57802 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1ebf4973-a393-303a-a347-dad8c7463f98 | -7.40115 | -45.65228 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 55d48b3d-3bf9-308c-934a-93f665725750 | -6.58997 | -41.5839 | 2026-10-08 16:37:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8e907435-1921-3015-81e0-eaa216697ad0 | -6.21917 | -44.85475 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ba9dbe5f-4aa8-3887-a0a0-3b6c223b897c | -9.83355 | -44.7834 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 0473f0f0-12af-3617-b06d-7915c3926b6f | -5.7656 | -42.07156 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| df880d15-6c3c-357a-a3cf-a060a7a79a99 | -12.24514 | -44.73272 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5581da81-0ed9-3fea-b033-161d4a0a3139 | -8.96111 | -45.15684 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ecf750fb-1913-36f7-8aa1-275d2f3968a1 | -12.18851 | -44.82807 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| cc8738fb-f95d-3fa3-8b22-dd1f228166c4 | -10.24852 | -49.67096 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 44e6a2d8-1465-33dc-b301-8735526fa318 | -6.8983 | -45.89225 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a7027d23-2e10-3f55-afd8-29e467c89a2b | -7.09678 | -44.03492 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ad4d3152-a412-397a-8c0f-3f93229a8931 | -8.02066 | -47.17093 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6351b3e7-d7a8-3047-a127-ee34783d4165 | -9.84035 | -46.16782 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 61873b2e-acc2-3fcf-b3b0-64c8628bfb7c | -8.94467 | -45.138 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7b67e573-2e77-33d2-b950-fb6e8f807f8f | -11.29739 | -40.84546 | 2026-10-08 16:37:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0d01ee95-ddd9-3ddb-8f3f-c618e9311304 | -7.82329 | -38.86108 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 194.7 |
| 720a2efc-ee61-365a-8754-c44490c1d087 | -11.27003 | -45.19198 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3423ea89-174a-3c2a-9dc8-0a8fd9c70b6d | -5.76788 | -42.06171 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 5bcf0283-1279-3a83-8303-1fb42b76b8bf | -8.28851 | -45.73061 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 267.1 |
| 74c475f7-a9c6-3d39-8ca5-b1a21cf77a68 | -6.77073 | -44.12359 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 52e5613f-7dea-3f0c-a139-fc19286373f4 | -11.12039 | -47.78909 | 2026-10-08 16:37:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba5f9071-fa8c-3ae2-ac57-60432919e3bd | -13.85776 | -47.60283 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04c7a2fd-f894-3122-a8a8-c1085a05edb4 | -9.87675 | -44.8661 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 9ebaaccf-ae0d-31d4-8a0e-33906bfe539d | -13.61257 | -43.27959 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 655b9f73-b2e1-31d4-a555-21665a7529b6 | -6.72408 | -45.1776 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 124e61c7-a530-3121-b852-f207a180ac11 | -11.0814 | -44.00848 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 06beedf6-5d6a-39d2-9c28-ca523219cd47 | -11.20251 | -49.42909 | 2026-10-08 16:37:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4439ea64-4bac-39b9-8439-c841d3e0f96d | -8.64216 | -37.13493 | 2026-10-08 16:37:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 004092fa-7662-346f-9b45-78fd515c6084 | -7.2524 | -43.50672 | 2026-10-08 16:37:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| f0a5484b-99df-3921-843e-aacf2f1952bd | -7.31211 | -44.00018 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 2d0d923f-c6a6-3fab-a9d2-78599a9a7756 | -11.7945 | -46.77304 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 869f5e5c-53a1-3abf-83ce-e2ba8f69a497 | -13.36249 | -43.87543 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 1140edb9-9b1f-3cd6-99b6-8d2e150b329d | -7.66242 | -45.38692 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 694897a5-4667-3f6c-b6d9-e5a5256d0123 | -6.23886 | -43.85758 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8cc82234-1425-344f-8ebf-00d1d6050c6c | -11.10867 | -41.3199 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 82e56bf5-7ab5-3d54-8cb1-9b7cd62786bd | -13.02169 | -48.51967 | 2026-10-08 16:37:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| da5d0a21-d20e-31fd-97cc-36457718f67c | -11.2695 | -45.18846 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 158702fb-4d0b-3143-8a74-797b714193d8 | -7.1709 | -47.78326 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20469a84-ffd8-335a-af0e-6d1c88d6fdce | -8.29076 | -45.72316 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 3207636e-d5d7-394e-a90b-6ded33603610 | -7.05544 | -46.84236 | 2026-10-08 16:37:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 00108794-ccb5-3113-9b6e-bf31456e24cc | -6.60073 | -37.88168 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ec1db336-1b26-3569-ada5-1c30702e130c | -11.22416 | -45.24705 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 021502e9-5b3e-326a-8c69-e5f37ffece56 | -11.63489 | -43.59121 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 34e4b65e-10b3-3f66-8f4f-3af8992fba4d | -7.6074 | -44.80921 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6603bca8-dfb4-3963-8ef9-d6d7a05340ca | -12.23298 | -44.74184 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 53eeba0a-e720-3a05-9dfc-7a19b544e6ec | -5.49608 | -40.54005 | 2026-10-08 16:37:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2cb1dc19-bbaf-3442-a8c6-c68ef833acaf | -10.756 | -46.60391 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 2fa7eb2f-c0c8-32a4-b5be-6f11286ee7ee | -17.22432 | -39.46832 | 2026-10-08 16:37:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 1ef7cd65-96e1-3c51-87bd-269dcf88439d | -6.20253 | -37.90233 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1aedece8-8348-3710-9b92-da611d91e5b8 | -5.51818 | -37.4874 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c41a62ed-20bd-372b-9062-e3a1ece91f5c | -13.34581 | -43.9653 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d39595dd-fc7c-322a-8f4b-d9d868088eba | -6.36816 | -42.52961 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| e53da102-b28b-3712-a388-bf9595d5dd2f | -13.64763 | -47.6732 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4dd6038e-80e5-30bf-9273-d84a5e7c284c | -11.76548 | -44.94656 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a15955cf-4fde-381d-ba04-c37e11c7d64e | -11.26553 | -45.20708 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 63a2bfd4-889b-386c-a01d-6bc7f38c7161 | -6.23541 | -43.85814 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 336a4c20-ea5d-3100-8e4e-135f3d71d922 | -18.05104 | -41.66747 | 2026-10-08 16:37:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e16a47ac-1cf5-32c0-84ed-e0eed2ccbb2f | -13.12328 | -46.36671 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2821ec61-4c28-3c30-bbda-7fda10e2b8d8 | -11.63275 | -43.70955 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 600d25d0-9958-317f-8d81-5957aef15db9 | -6.40178 | -44.93438 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 13e13507-3433-31bc-be32-dc5036fde9b9 | -11.7737 | -47.74071 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |


[Clique aqui para ver as próximas entradas](README341.md)
