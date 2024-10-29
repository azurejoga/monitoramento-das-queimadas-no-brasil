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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b4048e1-0d00-374d-8252-b59bcc314e61 | -5.9502 | -43.654099 | 2024-10-29 00:27:37 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 727d605e-0d49-32c5-98b6-cde74c1555de | -5.9357 | -43.635799 | 2024-10-29 00:27:37 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e3fe504-a779-3272-b2e5-d229f8ddf9e0 | -5.9404 | -43.6563 | 2024-10-29 00:27:37 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9eda7cd-9c04-3d8a-b9cc-faec9ffde516 | -5.9435 | -43.669998 | 2024-10-29 00:27:37 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 090226b2-37bb-3f78-abb7-e09b1dd2ef68 | -5.9451 | -43.676899 | 2024-10-29 00:27:37 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bacd855-afd0-388e-8424-bdbc6c050948 | -5.9466 | -43.683701 | 2024-10-29 00:27:37 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5be27688-7d18-3f89-b24b-e20ca7bc2498 | -5.9337 | -43.672199 | 2024-10-29 00:27:37 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b2a1a79-f2f2-334d-bfa7-083dc80b4ef8 | -5.9353 | -43.6791 | 2024-10-29 00:27:37 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13147f35-f300-3b22-b415-e46f7f51fe0b | -6.1347 | -44.693199 | 2024-10-29 00:27:38 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe46ac4-476d-3b90-b71a-c568b2fd879e | -6.1363 | -44.700298 | 2024-10-29 00:27:38 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 020e2082-864f-3973-8675-bea1040709eb | -6.086 | -44.6147 | 2024-10-29 00:27:38 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7de5a24d-390d-3857-9689-483e63be9248 | -6.0876 | -44.6217 | 2024-10-29 00:27:38 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 819f568b-6f65-3482-9a45-0a0af9e89e44 | -5.2669 | -41.228802 | 2024-10-29 00:27:39 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8549e7dc-43dc-3f64-8531-6241d02deda8 | -5.2687 | -41.236401 | 2024-10-29 00:27:39 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f612625-dddc-3c64-83ca-f33e61621aa1 | -5.9245 | -43.948399 | 2024-10-29 00:27:39 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a71443d-d72e-32b6-af3b-efe9a2491b93 | -5.926 | -43.955299 | 2024-10-29 00:27:39 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0bc6384-c6f1-3063-8ece-35a81c74ee76 | -6.0746 | -44.609798 | 2024-10-29 00:27:39 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aceb0af2-658e-32a9-9b0c-38cde5205cb9 | -6.0762 | -44.616901 | 2024-10-29 00:27:39 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0252940-54dc-3001-8a79-584928288810 | -6.0778 | -44.623901 | 2024-10-29 00:27:39 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 466ce30a-381c-30ff-8215-16943d7ae9f4 | -5.6708 | -43.199402 | 2024-10-29 00:27:40 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| e6ddeff2-10d0-3fe4-92e2-79aeaf231612 | -5.6724 | -43.2062 | 2024-10-29 00:27:40 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 49bf0685-85bb-3ced-b29a-7fe19b3da3bb | -6.6199 | -47.372501 | 2024-10-29 00:27:40 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68b8f3fd-62b3-343b-8f9f-53e5032da081 | -6.622 | -47.381901 | 2024-10-29 00:27:40 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0e3d016-8344-34f6-93cb-1ba58af93e77 | -6.6101 | -47.374599 | 2024-10-29 00:27:40 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44965748-4a5b-397a-8a8e-03c6b2882913 | -6.6122 | -47.383999 | 2024-10-29 00:27:40 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71dfd920-8a80-3a7c-be18-c352bbe63597 | -6.6142 | -47.393299 | 2024-10-29 00:27:40 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a9c84e5-a9a6-3e36-a590-f9f9ad6b6290 | -6.5238 | -47.030102 | 2024-10-29 00:27:40 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 408f55cf-5aea-3de3-ad95-0cd719cdeb74 | -6.5258 | -47.039001 | 2024-10-29 00:27:40 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71a83170-154b-38b5-9ee8-3eab88f6e464 | -6.512 | -47.0233 | 2024-10-29 00:27:40 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6cddd44-ffb9-3e40-80b9-2f6ca150935c | -6.514 | -47.0322 | 2024-10-29 00:27:40 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c6d9368-3109-3dd2-a545-14a0870a7dc5 | -6.516 | -47.0411 | 2024-10-29 00:27:40 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de99f952-db25-393a-b436-1484aa6d114f | -6.5179 | -47.049999 | 2024-10-29 00:27:40 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38e6dc8c-5c7f-3309-a900-6aaa18f724ea | -5.7304 | -43.775398 | 2024-10-29 00:27:41 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfd5279e-9d5c-3575-af19-a00cf3094658 | -5.7319 | -43.782299 | 2024-10-29 00:27:41 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcbe8a14-5c73-38d7-95c7-cf3f22371281 | -5.8201 | -44.123901 | 2024-10-29 00:27:41 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d99259-8969-39f7-87b8-456086276e02 | -5.8217 | -44.130798 | 2024-10-29 00:27:41 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 523aa420-6824-37e9-b305-3726fd135604 | -5.9145 | -44.630501 | 2024-10-29 00:27:41 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55532f43-b89f-3e0e-90b0-2d2d3db5c41b | -5.5629 | -43.223701 | 2024-10-29 00:27:42 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4726f373-6c01-3299-9e82-68a5fa9b62f7 | -5.5645 | -43.230499 | 2024-10-29 00:27:42 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc6f9d36-b69e-3e59-a93f-49148aacfca7 | -6.4346 | -47.276798 | 2024-10-29 00:27:42 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48f3b235-6794-30f2-a187-8de09d8321f9 | -5.6374 | -43.7747 | 2024-10-29 00:27:43 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e246937e-a363-3a90-82cb-c8a45c41ecd1 | -5.639 | -43.781502 | 2024-10-29 00:27:43 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbdc0c39-1ffc-3bc8-bfb9-0cbb59c1d374 | -5.6405 | -43.788399 | 2024-10-29 00:27:43 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 969aba69-41c1-355b-a6a5-17016f9497bb | -5.5311 | -43.309898 | 2024-10-29 00:27:43 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4328db5-0518-394f-909c-31b3bfb6f2a5 | -5.4852 | -43.334599 | 2024-10-29 00:27:43 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 252c7275-095d-3b14-9a3d-0673a3f9cd0e | -5.4868 | -43.3414 | 2024-10-29 00:27:43 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 791cedfe-c4fa-3a45-9718-9995c7b0237d | -5.9875 | -45.364498 | 2024-10-29 00:27:43 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abf8607a-b63e-385e-83b8-7cb2d001dca8 | -6.3016 | -47.324902 | 2024-10-29 00:27:45 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dae156cb-7d00-324a-a6c6-279ff1538f26 | -6.3036 | -47.334099 | 2024-10-29 00:27:45 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d6f7eef-b35d-3597-bc60-1a41a045fef0 | -6.3056 | -47.3433 | 2024-10-29 00:27:45 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1766a3c1-d6da-3c3b-832c-e7f0110bba82 | -5.7162 | -44.800999 | 2024-10-29 00:27:45 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba00745e-4702-3628-97c8-889383665960 | -5.7178 | -44.808102 | 2024-10-29 00:27:45 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84833492-aff5-3bb3-8803-6a836920613d | -5.7194 | -44.815201 | 2024-10-29 00:27:45 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 836356ca-bb48-375e-961c-729c7cb8ea9f | -5.5835 | -44.307598 | 2024-10-29 00:27:45 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67d75b78-d9fd-35d0-a298-d009783b9f56 | -5.5851 | -44.314499 | 2024-10-29 00:27:45 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f08ab3a-5ddf-33aa-ac38-bf08821bc9f1 | -5.9787 | -46.288502 | 2024-10-29 00:27:46 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77f28f86-1c70-3f7f-be1f-9fae154cfd07 | -5.0148 | -42.276901 | 2024-10-29 00:27:47 | METOP-C | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 384d3736-14e5-3e34-a07f-fc01a25bd804 | -5.0164 | -42.283901 | 2024-10-29 00:27:47 | METOP-C | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a32cb44f-6aee-30af-84f9-b138885fd351 | -5.005 | -42.279099 | 2024-10-29 00:27:47 | METOP-C | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2aac0fa7-dfac-3c29-8cf5-478abb721b1d | -4.9952 | -42.2813 | 2024-10-29 00:27:47 | METOP-C | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6fb8843-e65c-3185-a251-27f7494c235d | -5.7044 | -45.3419 | 2024-10-29 00:27:47 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce06ced9-a4e6-3703-bd74-72eca9513f7f | -4.5643 | -40.473701 | 2024-10-29 00:27:48 | METOP-C | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 99bee616-1783-398a-829a-6e4fdeb0d44d | -5.2464 | -43.7328 | 2024-10-29 00:27:49 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0e1f0b5-e950-3fa6-9530-45bcee40de3e | -5.248 | -43.7397 | 2024-10-29 00:27:49 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcb6b9a6-b93d-3dee-a2c2-76f8bfbbb63c | -5.2495 | -43.746498 | 2024-10-29 00:27:49 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b5ffb28-6450-3422-87d1-cbc66436d495 | -5.3481 | -44.178501 | 2024-10-29 00:27:49 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20321c04-2aab-3970-8ebd-5f7f43c804eb | -5.3496 | -44.185398 | 2024-10-29 00:27:49 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b00b503b-3039-3f25-818c-f7d97954e2f7 | -4.8626 | -42.466801 | 2024-10-29 00:27:50 | METOP-C | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4fee97f-802d-3eae-8bdd-b9f145d86c99 | -4.8643 | -42.473801 | 2024-10-29 00:27:50 | METOP-C | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cead4b55-0039-3b14-bec8-0bb33512789a | -4.8768 | -42.617901 | 2024-10-29 00:27:51 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f2b0082f-9ded-3f1e-b62e-0b8a867f0c60 | -4.8784 | -42.624901 | 2024-10-29 00:27:51 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9ce73d-6acb-3a8f-a351-d3f48e939c8d | -4.867 | -42.620201 | 2024-10-29 00:27:51 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54d38e9f-e501-3439-a64f-8e8725125cf8 | -4.8686 | -42.627102 | 2024-10-29 00:27:51 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35e2cb70-8a4a-3e2e-93af-2fe4adda59e8 | -4.8703 | -42.634102 | 2024-10-29 00:27:51 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe39fe26-4c63-3119-9b5d-883edf68a8b6 | -4.7183 | -42.6464 | 2024-10-29 00:27:53 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd0dcf5c-d2b2-3f5a-b0e6-c36fe597a97b | -5.5401 | -46.258701 | 2024-10-29 00:27:53 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af1988da-7a71-3a27-b5d8-9975cbd0701d | -5.5419 | -46.266701 | 2024-10-29 00:27:53 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5546e083-d258-3782-8bd2-4bfd2b4db0cc | -5.0655 | -44.205399 | 2024-10-29 00:27:53 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e55b14f4-a93d-3958-bbd4-82a31445da01 | -5.0671 | -44.212299 | 2024-10-29 00:27:53 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30a64d3c-098b-382e-99b9-6cf4f91ae7b0 | -5.0686 | -44.219101 | 2024-10-29 00:27:53 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdfaaf9d-c82f-3024-9972-af35c1dbf85a | -5.738 | -47.191399 | 2024-10-29 00:27:53 | METOP-C | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7e09216-bd24-34f1-8d62-a6ad8ca49f4b | -5.3721 | -45.6488 | 2024-10-29 00:27:54 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b58e02db-eccd-34f9-bbbf-17c5943c25d2 | -5.4563 | -46.344002 | 2024-10-29 00:27:55 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04417403-46b1-336f-b15a-f43809c0b1a1 | -5.4581 | -46.352001 | 2024-10-29 00:27:55 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 996b7240-862e-36c6-8184-4395b68e90e5 | -5.0209 | -44.462101 | 2024-10-29 00:27:55 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d839b343-469e-3df4-a0ca-7f6c12ab0cdc | -5.0225 | -44.469002 | 2024-10-29 00:27:55 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95529642-7e07-3a86-a482-ffa1ba895f34 | -5.3136 | -45.8918 | 2024-10-29 00:27:56 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab59505e-bed5-3eec-90aa-31b229f70dec | -5.2017 | -45.623699 | 2024-10-29 00:27:56 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1d08367-c18a-317a-a699-96db7d45451f | -5.2034 | -45.631199 | 2024-10-29 00:27:56 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2466371-025d-3b86-b5a2-bdba8f98ba18 | -5.1025 | -45.2757 | 2024-10-29 00:27:57 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a5acc84-a939-38f0-a5e1-d5629f5fd886 | -5.2968 | -46.3204 | 2024-10-29 00:27:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b74ee16-609b-329a-844d-0fd1f7001086 | -5.2986 | -46.3283 | 2024-10-29 00:27:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c991cfa6-559c-3450-b71f-a9b9d512ff55 | -4.5098 | -43.129398 | 2024-10-29 00:27:58 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0821a881-707d-31f2-82f9-6fb41b1fc02b | -4.5113 | -43.136299 | 2024-10-29 00:27:58 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 021ad82b-2fee-3efb-a524-dc0777cfaf1d | -4.9054 | -44.6339 | 2024-10-29 00:27:58 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7e40aa-7ca8-3106-b08a-6a6b9d32d8f1 | -4.907 | -44.6409 | 2024-10-29 00:27:58 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8b8e40e-f876-343f-bc8a-1526da863424 | -4.9086 | -44.6479 | 2024-10-29 00:27:58 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72c0d44e-06d1-34b4-880c-89987340298a | -4.4241 | -43.025902 | 2024-10-29 00:27:59 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95f3780b-4d65-3f13-adb1-008284e6d588 | -4.4257 | -43.032799 | 2024-10-29 00:27:59 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c01fbf4a-4ce7-308c-9b00-8aba5db30a00 | -4.4273 | -43.0396 | 2024-10-29 00:27:59 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
