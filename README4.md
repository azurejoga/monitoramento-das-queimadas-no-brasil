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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2753ed29-258f-3dbd-b8b1-ff1021c191cd | -4.3131 | -41.240501 | 2026-10-10 00:09:00 | METOP-C | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33f6f61b-fcb2-391f-ad61-1c608a77b1f4 | -5.8265 | -44.934799 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09a94c14-24f7-35cc-b53d-6780f9dda007 | -12.0195 | -43.443001 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8c44c87-1169-3c67-8497-c64025c792ed | -4.0497 | -46.1688 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf3bd7f8-219e-321e-8ce7-0205ea7668eb | -4.3945 | -49.7509 | 2026-10-10 00:09:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b10fc540-4ae3-3d4a-8767-24f74ebb40be | -17.1399 | -41.365398 | 2026-10-10 00:09:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3754ec0-6240-31e9-87f8-7299426e7945 | -11.7612 | -43.528 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5086388c-315b-352a-9254-381ea527a39c | -11.9806 | -43.500801 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 208bd8a7-4350-324e-9160-c5f62c679e09 | -18.326799 | -42.382401 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8734a1c7-e7a7-3e10-95a0-16df5197e1d4 | -8.1941 | -45.7869 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac5bb10e-a61a-3e46-9a49-f5beb79cb0a0 | -9.9325 | -44.884201 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 573cca62-96c7-3476-9cb1-ee491f270e8c | -16.0019 | -43.597401 | 2026-10-10 00:09:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 129e4667-01fa-3860-9bf8-72f362808be0 | -5.8768 | -43.410599 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfee96d5-d19b-37b5-b861-3823e6bddc68 | -9.8271 | -44.7733 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc9f46fc-6d61-3a52-a4ae-c52a1e786443 | -11.9979 | -43.437801 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf4681a1-948f-3748-8608-a4fe09d9c6ac | -17.9814 | -47.2369 | 2026-10-10 00:09:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5b4896-3d63-389e-bba9-fecbecda425c | -17.2859 | -40.351398 | 2026-10-10 00:09:00 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74a9389a-1783-3617-818a-bb43bac930ac | -18.343901 | -42.263599 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12fa4a02-e7b2-3d9c-b9ac-a703fbf43435 | -14.0055 | -43.260201 | 2026-10-10 00:09:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ff46acc1-8e10-30f1-b600-79995c5c4fce | -5.0877 | -46.2272 | 2026-10-10 00:09:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 692acb8d-80ea-3b04-9244-bd27b9e738c2 | -13.9181 | -43.036499 | 2026-10-10 00:09:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cfb9520e-b6d3-38db-b3a9-61a42798320d | -5.7547 | -41.685101 | 2026-10-10 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c6a375a2-9018-3aca-821c-827f5035bff9 | -7.7605 | -43.795399 | 2026-10-10 00:09:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 467d103c-7d7c-36b3-b306-18045964a718 | -5.2394 | -42.228699 | 2026-10-10 00:09:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d807adc8-2683-3c5a-8113-6b1ded54a591 | -5.9475 | -45.388901 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33ee7e81-5ea2-310c-80f4-9f62d69adbec | -11.959 | -43.495602 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed62ec2-16a6-3a87-8c93-3d005db70871 | -11.6716 | -46.785301 | 2026-10-10 00:09:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0931c43f-0be7-3446-8cc2-95dfd3350c26 | -5.6855 | -44.439499 | 2026-10-10 00:09:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75ae37d5-9d20-352d-9f65-1523e13f31ce | -7.2042 | -44.344299 | 2026-10-10 00:09:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54fc3ced-6b64-35a7-9fc0-ebcb8eded8c0 | -9.2993 | -47.397202 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 602e4eb7-3d28-33a7-a91d-163b279197d8 | -5.3122 | -45.206402 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e594115-b7b1-313a-9542-96a325b9a8df | -3.7568 | -45.960499 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1679ed22-ee45-366c-b1d3-99499f76e77e | -14.0427 | -47.000599 | 2026-10-10 00:09:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff6515b3-4d88-3a32-a58d-a162e01c84b8 | -17.134501 | -41.3395 | 2026-10-10 00:09:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9946eb77-108e-3df2-966d-2b0c25ba72b5 | -4.1235 | -46.866402 | 2026-10-10 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88f4dd5b-9bcc-34cb-b0e1-aed0993b1fb1 | -16.115801 | -43.759602 | 2026-10-10 00:09:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7a48dded-d9f0-376e-8f8f-df9b86334c5d | -4.4023 | -43.124199 | 2026-10-10 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4328eed3-f149-39a4-b789-1f140c0c1148 | -7.5108 | -48.0289 | 2026-10-10 00:09:00 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc1a6537-a9a0-3c15-82dc-acdac2df6fc6 | -11.1187 | -43.2523 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b5b3124a-9263-3f5b-9805-ac5c041e7a98 | -11.2374 | -46.298401 | 2026-10-10 00:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70316c76-3074-38fb-9255-27e622c67ba1 | -6.0708 | -44.002201 | 2026-10-10 00:09:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e77f03b-590e-3bef-81a5-5a31a797f98d | -7.5158 | -45.299198 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1b9d86-b9f7-3c3b-97b9-22c503543b7a | -11.4901 | -47.596001 | 2026-10-10 00:09:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75dd0bc5-ba50-3962-a0cc-7d92c1d539ca | -4.1277 | -45.7841 | 2026-10-10 00:09:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46e9951f-1e04-3d78-b864-1fad734b5f8e | -16.8102 | -42.297401 | 2026-10-10 00:09:00 | METOP-C | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47e9806e-7178-3a38-bbe7-41e743dba869 | -14.4348 | -43.959301 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 263c4285-5818-32e7-91a6-7714849740f1 | -8.9757 | -45.955799 | 2026-10-10 00:09:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 340ddfdb-82cf-34af-8464-f30cdde5023c | -9.2603 | -47.405201 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e64f3e0b-f405-36f8-babc-1277bcd5f502 | -8.3483 | -48.1455 | 2026-10-10 00:09:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cab1eea-cd07-3635-8776-18ea22ee0848 | -14.9677 | -41.699699 | 2026-10-10 00:09:00 | METOP-C | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 22b68a8d-78bf-3602-8c78-1c7ad5ec6daa | -12.6886 | -43.075401 | 2026-10-10 00:09:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8764cb94-a3a1-3892-b63b-19d9bb7ed137 | -6.0531 | -44.661301 | 2026-10-10 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 517749d4-41b5-3733-ab3c-232599791e6d | -18.0895 | -42.266102 | 2026-10-10 00:09:00 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c733d2a-0039-3674-b014-eecd5d0a5157 | -11.463 | -43.377499 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd0151ba-a17b-37de-b6df-fc2fc41d0a7c | -4.0177 | -46.9888 | 2026-10-10 00:09:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc3dc0c2-1521-335a-a7f5-fe264a72bc5e | -3.2124 | -42.964699 | 2026-10-10 00:09:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56fe356c-8ef1-3fa5-ada2-377c7db83acd | -12.0077 | -43.435699 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c313b8d-b29e-38b1-b60c-5c639c662578 | -3.2419 | -50.425201 | 2026-10-10 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42180349-ce8f-3268-b8ec-7853790510d5 | -7.4876 | -42.842701 | 2026-10-10 00:09:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b18d2cf-788b-3be5-bc84-d6987a20404a | -10.2742 | -43.945999 | 2026-10-10 00:09:00 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5c473c01-6942-3af4-ae27-c2184478cd28 | -7.1747 | -52.606998 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67b57e25-70a3-37bb-8f5f-b28edbca6489 | -13.3803 | -43.890202 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 186fe622-d139-344d-8cf9-c171823918ce | -11.9725 | -43.463001 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed3a3f00-4f49-3a2d-aecc-16a632c6c168 | -13.4565 | -41.346802 | 2026-10-10 00:09:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 082a5d92-ae22-3b58-9e27-123d78c7e596 | -11.6127 | -43.599499 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 739b1169-5298-32ac-b2a9-74343ce05d28 | -11.0192 | -45.439499 | 2026-10-10 00:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd35e1b2-089d-3c1e-86e5-2d23f427421b | -4.5745 | -40.672199 | 2026-10-10 00:09:00 | METOP-C | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8ab87e94-2457-34f4-a2d2-948e75653b68 | -10.6119 | -43.278 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b32a55d8-fcc3-3b0c-a69f-2dc9d7130efa | -9.0154 | -44.376801 | 2026-10-10 00:09:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5caa327-258b-358b-aa84-6c401605a2e8 | -7.2291 | -44.1782 | 2026-10-10 00:09:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15c0d786-b4af-3e2e-93e3-88ffcca41fe0 | -16.642099 | -40.603699 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4811b799-4d6a-3971-92af-7ee7f8729282 | -4.6722 | -48.512699 | 2026-10-10 00:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a527c4f7-cf02-3965-a8fa-1aa14722dfe7 | -14.4326 | -43.948299 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a97481b3-c307-33f0-bc8e-d268fd0629df | -4.4028 | -49.788601 | 2026-10-10 00:09:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b3b169-fa57-3066-aca0-fc907f152e50 | -11.7514 | -43.530102 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b504b72a-3ba2-3db7-bce1-a2477e913220 | -3.5489 | -51.487 | 2026-10-10 00:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a150696-e2e2-316a-a713-dd2f828d21c4 | -4.5986 | -49.1978 | 2026-10-10 00:09:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d556fa-0cae-3c39-9554-bfba99d82a47 | -5.4559 | -44.791199 | 2026-10-10 00:09:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e31960f0-e9fd-3827-817d-f92a780cf997 | -11.878 | -47.3591 | 2026-10-10 00:09:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d69575f4-ac98-3b07-a06c-64b8fea524f6 | -3.167 | -50.590401 | 2026-10-10 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b42692-c723-30e6-a043-d452380b07e0 | -3.2375 | -50.405102 | 2026-10-10 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb83f97-9f87-3d5d-bba6-4dd895c3cb06 | -3.008 | -44.464901 | 2026-10-10 00:09:00 | METOP-C | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf8378c9-5a4a-3fb4-a8e9-b4de1f72d2e5 | -8.1842 | -45.740898 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a76ebb2-d2bf-3b48-8788-17d32a4d19af | -12.2831 | -47.054699 | 2026-10-10 00:09:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95eca24f-033c-3c05-9311-dfc4cb2ecfec | -13.9336 | -42.963902 | 2026-10-10 00:09:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1aec1b10-11ee-35e2-bab1-2785522125eb | -18.0875 | -42.256302 | 2026-10-10 00:09:00 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ab73798-fae8-343e-acdf-3af45ee91c6d | -8.3448 | -48.128799 | 2026-10-10 00:09:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28c9eda1-e96e-30f5-b20b-560f0b048d20 | -11.5506 | -43.692699 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8602ad52-dbc6-314a-8f30-62df52a22503 | -14.4544 | -43.9552 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c0624f90-4c3a-3d89-ae9d-96d853cc0365 | -7.7713 | -42.316799 | 2026-10-10 00:09:00 | METOP-C | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 559da6cf-1e1a-38f9-88a3-d6ed440f5fee | -15.3467 | -42.780998 | 2026-10-10 00:09:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1d51d7ee-d33f-38b0-9668-0b13dbb07c2e | -12.9252 | -47.4375 | 2026-10-10 00:09:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7691fa27-467c-39c3-ba7c-06c141ef21c5 | -4.3908 | -43.118999 | 2026-10-10 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7db14689-01dd-3623-aa44-3ee87609e9c4 | -15.3752 | -41.932899 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34782320-85ae-3ffd-89d4-a40e6accab6f | -18.316999 | -42.384399 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0eac5695-664e-36cd-b523-b46e96a635cb | -10.9145 | -45.524601 | 2026-10-10 00:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc3f4b18-f866-374c-a74b-036c9de79a1f | -11.6485 | -43.6717 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4dba1e-5ee5-3b61-b2e2-a6642c0da442 | -16.6404 | -40.595798 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2f5b745-23ec-3fd3-b416-2b1b43d9c6c8 | -15.8482 | -42.0425 | 2026-10-10 00:09:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da9dcabe-a83f-30c3-8017-b7f3d4b71850 | -4.9075 | -45.785198 | 2026-10-10 00:09:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
