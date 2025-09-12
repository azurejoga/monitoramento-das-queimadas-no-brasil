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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39a45aa2-70bf-3acb-9248-8fb53f3c6af3 | -6.4987 | -43.8806 | 2025-09-12 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3746c968-cc60-36d6-bb5d-5a05ca3ea70e | -14.4588 | -47.3174 | 2025-09-12 00:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b16992cc-1d96-352d-9ebd-f1dedda69195 | -8.9563 | -46.0849 | 2025-09-12 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| feced67c-1af7-38dd-9c83-1c7804dea135 | -21.6491 | -54.0105 | 2025-09-12 00:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1ca59033-432c-38df-8c53-3dd93cc4e79b | -23.1358 | -47.4859 | 2025-09-12 00:00:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| d04fd949-46db-3197-bd0a-a8d16d2ada73 | -12.1139 | -44.877 | 2025-09-12 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 64332c80-4311-3cc0-ae7f-c294d3347771 | -12.5984 | -45.6791 | 2025-09-12 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| c453961a-bc27-3a68-ba41-18e0fc361389 | -8.8899 | -49.945 | 2025-09-12 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 214.9 |
| afe47835-bdf3-3561-b419-b409f2f94a8a | -21.6496 | -53.9886 | 2025-09-12 00:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 597ba7f9-6b6d-3d84-8f1b-652b9fb827ea | -8.8901 | -49.9236 | 2025-09-12 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 437e2a02-cdf7-3d60-92c2-da00e37f7e68 | -13.4708 | -51.7712 | 2025-09-12 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d0d1e015-36be-348d-8368-8ff35cff9327 | -12.5791 | -45.6821 | 2025-09-12 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 57ba5b20-939e-3cf6-a641-a23aa08c3fd2 | -6.4882 | -44.9373 | 2025-09-12 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b7c5bf25-2468-3af2-90f7-2cff4be725da | -6.309 | -42.2311 | 2025-09-12 00:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 87bb0e1d-d510-3166-8c59-4ffce6aac8d0 | -7.4234 | -50.6564 | 2025-09-12 00:00:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7c5edff3-b3d3-3323-b499-3e8160790b58 | -9.7134 | -64.945 | 2025-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b65d97fe-1d2d-3896-aef6-5084954d7119 | -11.9907 | -51.1405 | 2025-09-12 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d28f0331-2b04-3bfa-a277-4f9f040c05e7 | -21.9686 | -47.5287 | 2025-09-12 00:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 174.3 |
| a998caf8-fd77-330d-aa19-1a1349dfac5f | -22.9386 | -49.1171 | 2025-09-12 00:00:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 2d18e015-2634-3f92-8a6d-902273b4448b | -7.4047 | -50.6578 | 2025-09-12 00:00:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 384e7391-3af8-3404-8462-466b4b848da4 | -9.5137 | -54.6292 | 2025-09-12 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ef7c8838-19c7-37de-b53f-76ba87795c03 | -9.057 | -47.0355 | 2025-09-12 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 51c6f3d1-fe7c-3cc8-8a69-4c4c1fddb16d | -9.1125 | -47.1185 | 2025-09-12 00:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f130556d-d4ba-3d9b-b078-21dbeaf08c34 | -6.4696 | -44.916 | 2025-09-12 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9f8960ad-63ef-3788-8872-347e07300d15 | -8.9087 | -49.9433 | 2025-09-12 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ffaea087-3e74-33b8-b1b1-7403012666a0 | -9.7135 | -64.9262 | 2025-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8ab032e8-f77a-3e2f-9632-b3213ff12acb | -7.4049 | -50.6367 | 2025-09-12 00:00:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| aa973e68-caa9-3566-b4ad-7daa0ffac3d6 | -9.732 | -64.9443 | 2025-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a69524b7-85c9-3d52-9462-582872700460 | -11.1809 | -55.0821 | 2025-09-12 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 17f19d6f-51d9-333f-be7c-529ec024ff52 | -11.9717 | -51.1427 | 2025-09-12 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 572de70f-b16c-36b7-9efb-8b0b9341db6e | -9.2287 | -59.3823 | 2025-09-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 725faed6-3d44-3214-9354-6057a07651dd | -12.1143 | -44.8537 | 2025-09-12 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 74c4987e-148e-3ca8-a2f8-d4cd43b98569 | -13.3238 | -44.0945 | 2025-09-12 00:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 5b4b5ea0-385b-3f0c-9025-244f0d0135a6 | -18.1325 | -51.7096 | 2025-09-12 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 6344cd47-d3ae-3716-a18c-e1daf1f04ae6 | -8.1837 | -46.0965 | 2025-09-12 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 522c3f15-595e-3458-9fc8-8c4134587324 | -6.4694 | -44.9388 | 2025-09-12 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 327.2 |
| 620455a5-0c61-3900-bbde-9c0c04744d45 | -22.9168 | -49.1457 | 2025-09-12 00:00:00 | GOES-19 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 48.2 |
| ab033fad-0d98-39e0-b3a3-26b37bfda292 | -23.1146 | -47.4915 | 2025-09-12 00:00:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.2 |
| ace7ab6e-df47-3a28-acc6-3fc409ffe366 | -12.9292 | -54.7538 | 2025-09-12 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e7a728b9-bdb4-3523-962f-abce27b1ddc5 | -21.9679 | -47.5525 | 2025-09-12 00:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 235.4 |
| f6ef8633-37af-39a3-87a0-02235c50f5f8 | -21.947 | -47.5578 | 2025-09-12 00:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b86dd387-228c-31f9-86ea-12cb8e754a79 | -8.9089 | -49.922 | 2025-09-12 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ab85ec20-9170-398c-9eb9-3054f09400bd | -23.1139 | -47.5156 | 2025-09-12 00:00:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 081c7a7c-27c8-3f45-a992-5420b09cfedb | -22.9379 | -49.1406 | 2025-09-12 00:00:00 | GOES-19 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 1730d4be-5cdc-3335-b693-611511f30671 | -6.48 | -43.8822 | 2025-09-12 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 7b597040-5198-3154-b726-faf42c86448e | -13.3243 | -44.0708 | 2025-09-12 00:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 82252a78-2e1c-3bc8-b39f-fb729cb2ad64 | -11.1998 | -55.0805 | 2025-09-12 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 5fd34c2c-c8c0-32c8-8cb6-46b60122414d | -9.7321 | -64.9255 | 2025-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f629c842-0769-35e4-bdb2-fca9dcc2e40e | -20.4052 | -49.1278 | 2025-09-12 00:00:00 | GOES-19 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 99ac409f-bb8e-30e3-ac03-2197e46489f3 | -7.4236 | -50.6354 | 2025-09-12 00:00:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2d9893a5-2cd9-3976-834a-9d21c6f3dd68 | -21.19051 | -47.52364 | 2025-09-12 00:09:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 63403e3e-73e3-33ee-b9b5-fde21383037c | -15.55941 | -41.7887 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| a0258e39-6da8-315a-abef-45fe94a3d382 | -19.11037 | -43.18227 | 2025-09-12 00:09:00 | TERRA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 395be5b8-00fd-3a15-ac21-a6fc6bff5345 | -16.2727 | -40.17704 | 2025-09-12 00:09:00 | TERRA_M-M | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5c23b6cd-1642-33b5-9595-a0585ee9aad9 | -16.41375 | -45.69166 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 1e496741-3c81-3f68-a744-60f5196ec0e1 | -19.64803 | -41.5893 | 2025-09-12 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 02ec5782-b199-3c2e-877c-c2168725b2c3 | -23.43742 | -47.03244 | 2025-09-12 00:09:00 | TERRA_M-M | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 371fd796-6bd6-37dc-a992-8871c65b628a | -17.82759 | -46.73526 | 2025-09-12 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 90bb65ce-71e6-3343-b867-3b7877b382b0 | -14.14872 | -44.45165 | 2025-09-12 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 21d9b91f-7027-3f65-99e3-dc0117a02f6e | -14.44766 | -47.31028 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3bb0dfd6-c2ff-3e4f-a289-fa6113397685 | -17.59033 | -42.16318 | 2025-09-12 00:09:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 162cbac8-ae05-311e-845a-c953753ee173 | -20.11609 | -42.35202 | 2025-09-12 00:09:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 0ad84e04-7b7a-39a0-aea9-ca562cba7578 | -18.45382 | -47.18734 | 2025-09-12 00:09:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c590307d-7b5d-3aff-8842-204da80ecf09 | -13.24455 | -43.79588 | 2025-09-12 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 41398082-8e2e-3311-b458-2eacfc02a248 | -14.45655 | -47.31976 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1b76ba0e-a39f-3b08-ad9b-fc3c48b59d84 | -19.63911 | -41.59069 | 2025-09-12 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 1076656c-35ba-3bae-9fd7-e30de85e3751 | -22.87729 | -47.17104 | 2025-09-12 00:09:00 | TERRA_M-M | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| bf1cb51d-14f0-3e2e-b55e-6a3aba069971 | -23.11643 | -47.51342 | 2025-09-12 00:09:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.4 |
| 64743a9d-7f3c-392b-8766-840f548c59af | -13.31178 | -42.38605 | 2025-09-12 00:09:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 47.7 |
| 466ace17-45b9-331d-b72e-e33f3869c723 | -21.96881 | -47.54546 | 2025-09-12 00:09:00 | TERRA_M-M | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 154.2 |
| d994b736-e562-3b1c-ace1-8f62aa9794fa | -16.28901 | -45.68651 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 77b3a3b8-479a-34b0-a6a9-2057d9270c75 | -20.26873 | -42.11224 | 2025-09-12 00:09:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 73e55ad7-43ef-3d37-89c6-afb5abc94b13 | -18.10493 | -42.99886 | 2025-09-12 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| a36d6947-695a-33c0-aaa5-fe12b8c27df5 | -22.79388 | -47.79648 | 2025-09-12 00:09:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 551fac14-9880-312c-a875-335f8588a1f5 | -21.97099 | -47.56826 | 2025-09-12 00:09:00 | TERRA_M-M | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b91d2759-e715-3fc7-a5b3-ed592997c1eb | -16.43442 | -49.02956 | 2025-09-12 00:09:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 1fd5a41b-9f52-3262-b599-1b46778a617d | -23.10661 | -47.49635 | 2025-09-12 00:09:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.1 |
| 1cdbe98f-dfca-3885-940f-caec030f547d | -15.62267 | -41.04975 | 2025-09-12 00:09:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 2ac3715f-e8d2-3c28-8cf8-28ac0fd3665c | -12.11271 | -37.97362 | 2025-09-12 00:09:00 | TERRA_M-M | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| c3531e5e-4abc-397a-8aa0-15b0fd860fd6 | -15.83467 | -42.59092 | 2025-09-12 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f679a44e-45c4-33cc-889b-eb6a54120c2f | -19.10904 | -43.17169 | 2025-09-12 00:09:00 | TERRA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7f7625e7-bd07-31d1-8077-88f8230211a6 | -22.79019 | -47.82931 | 2025-09-12 00:09:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 87e799f6-ef96-3455-9cf2-442ae94d6ccf | -17.32814 | -46.67213 | 2025-09-12 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 23ccba66-a472-3a2e-a9dc-382e0d046cbc | -18.44904 | -47.17437 | 2025-09-12 00:09:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8ed2fe60-1c57-3af1-ab62-af79b58de8ee | -14.1342 | -45.37783 | 2025-09-12 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f3417b85-a800-363e-8d94-8b4edbe48986 | -14.443 | -47.30554 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5ab4d0d1-cd08-334a-9841-932e76ec3b52 | -21.33496 | -45.04359 | 2025-09-12 00:09:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| 46e4ed1b-c996-39b5-a88b-1f46c00ab5b6 | -18.05647 | -45.43374 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 8a44faae-8fe1-3828-ab3f-b0bb71902c6f | -18.8217 | -46.87242 | 2025-09-12 00:09:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d9eb2a88-3bbe-322d-8ef3-be95d2244985 | -20.26999 | -42.12194 | 2025-09-12 00:09:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| af1193fb-fb01-3f71-8b7f-059fbf5195b7 | -16.43159 | -49.06145 | 2025-09-12 00:09:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 30976231-e83b-36c8-9ecd-72e6a8e2ea3a | -18.05477 | -45.45434 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0930d931-6b19-36ab-892e-1b5da5c3bf9c | -20.56544 | -43.74465 | 2025-09-12 00:09:00 | TERRA_M-M | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| e9b3fbee-22c6-32cc-aa1f-5c9608d2736e | -20.40357 | -41.53202 | 2025-09-12 00:09:00 | TERRA_M-M | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| aac1ccf2-31b2-316f-91b7-88b0b093036b | -23.12019 | -47.49494 | 2025-09-12 00:09:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.0 |
| 4cb64ac8-7397-38c5-9364-792764114792 | -21.33157 | -45.01291 | 2025-09-12 00:09:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| a7df7076-447e-3ade-aeed-27df1fd0b166 | -19.16544 | -48.01978 | 2025-09-12 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 89b8dd15-483f-314c-a932-9e16ab281745 | -19.31979 | -47.51892 | 2025-09-12 00:09:00 | TERRA_M-M | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| aa641fe4-d85a-3091-af85-fbe544694b51 | -14.42609 | -47.32941 | 2025-09-12 00:09:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7a76b9f9-9e64-3770-8bf4-1f9df535f5e0 | -19.9777 | -47.60246 | 2025-09-12 00:09:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |


[Clique aqui para ver as próximas entradas](README2.md)
