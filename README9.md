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
| 667e7daa-177c-3bfd-a001-9e2b8e153a7f | -15.60475 | -48.07563 | 2026-08-09 04:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bef28409-e490-314b-bc10-cafc40a210be | -12.35308 | -53.1626 | 2026-08-09 04:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0de5b32-3880-3042-a720-382546b66b7c | -14.07967 | -53.99541 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41146a3c-d9b6-38c7-b81e-6b12fa75fd71 | -14.05064 | -53.83496 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d54637e0-1ff5-3765-82f8-c828574e78cf | -14.02591 | -53.84853 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e613e44b-5ddb-32a6-9e5c-c62ff7d7090e | -14.02051 | -53.84216 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70dc5806-d736-39df-8f05-1e1ae95b00c9 | -10.48831 | -46.62588 | 2026-08-09 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2811c8ef-a063-39d1-980d-a094009f99db | -11.04224 | -44.27803 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 639aec08-0889-3c1b-a49a-d74fbfe28a40 | -14.0492 | -53.84168 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45a808e2-9638-3330-9c06-b38a737992de | -11.26886 | -44.86926 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 42470284-2137-327c-93d5-fe653c540740 | -10.24994 | -45.81064 | 2026-08-09 04:08:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc7e367d-4bec-33e9-9bc2-20a9d01d53ad | -14.17205 | -53.99866 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b18f532-6c60-3132-aca5-0855551bd4f9 | -14.02736 | -53.84353 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47f5d334-4153-333f-a835-44728b93af01 | -14.16117 | -54.01536 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fafcdf9c-0f46-3faa-857d-490501f79d5b | -14.0799 | -53.99191 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37748a61-2508-30cb-9f08-5d3749c91e8b | -14.06583 | -53.8297 | 2026-08-09 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fd4253e-e825-3572-af04-ce857f1ba73d | -11.04618 | -44.27876 | 2026-08-09 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa375923-30ee-3fa8-a0a5-4545dbea91dc | -9.4582 | -40.3143 | 2026-08-09 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 189.0 |
| 00f15202-b149-32b9-be58-b53c6ab54b04 | -9.4769 | -40.3365 | 2026-08-09 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 276.4 |
| 74ba9746-f83f-3186-a11b-013327afe071 | -6.8388 | -56.4146 | 2026-08-09 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9e6bf5d5-f8d4-3e05-84f8-22556e220e02 | -9.4777 | -40.2867 | 2026-08-09 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 17bc26ee-8dc2-3aef-b060-5501c4492c80 | -9.4578 | -40.3392 | 2026-08-09 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 1ed5867d-4194-3e30-8a54-25b396158ebd | -9.4773 | -40.3116 | 2026-08-09 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 676.4 |
| 0802ef81-246e-32ca-8674-1b51dcdfb0a6 | -22.19193 | -42.47996 | 2026-08-09 04:10:00 | NPP-375D | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0ed49c11-1acc-332b-a85b-8bbf9b2845b2 | -22.89039 | -43.50458 | 2026-08-09 04:10:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 92f62fe1-8441-368b-98c4-cae5a84bbc91 | -20.97274 | -43.92656 | 2026-08-09 04:10:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 01c82e12-0789-358f-8802-bf64195c3969 | -19.79816 | -43.95015 | 2026-08-09 04:10:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f3a1dd3-3135-3436-9fbe-2415e5853070 | -22.22689 | -43.03711 | 2026-08-09 04:10:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| acd0a60a-f571-3276-9f95-a1ce730baa0c | -22.93921 | -43.42697 | 2026-08-09 04:10:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2e63611-f0cd-337c-b8ca-d5c19e373821 | -20.55024 | -41.02746 | 2026-08-09 04:10:00 | NPP-375D | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ceeb935f-242f-3b07-9f19-887e6437ebbe | -19.34203 | -44.53732 | 2026-08-09 04:10:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4938de3e-753a-3e47-a225-fbac380e9a2b | -20.61172 | -45.11371 | 2026-08-09 04:10:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 901bf7d8-de94-39b7-80b0-9b6593e40625 | -21.74534 | -43.32666 | 2026-08-09 04:10:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 682c49d2-373a-3260-9450-77a77d02bbf9 | -19.9384 | -44.37128 | 2026-08-09 04:10:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3202dc1d-0f3d-3066-bb98-09c5bc067100 | -18.66052 | -40.78959 | 2026-08-09 04:10:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c40bd340-424d-330a-92b1-666b6a5bec07 | -19.95854 | -40.15087 | 2026-08-09 04:10:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d16f9bdf-2beb-32db-8ff4-7fba4515839a | -22.2963 | -42.60971 | 2026-08-09 04:10:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 37265173-97f1-3312-b456-78cb6908ade1 | -21.28119 | -42.93914 | 2026-08-09 04:10:00 | NPP-375D | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5365020e-80cd-35b6-8755-5596a2753afa | -20.0755 | -45.28839 | 2026-08-09 04:10:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab7c9e6e-f443-3d00-bf74-3a4d2479b55e | -22.07565 | -42.34436 | 2026-08-09 04:10:00 | NPP-375D | CORDEIRO | RIO DE JANEIRO | Brasil | 3301504 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cea7caed-ce1a-31a2-b744-4051045749d2 | -20.38075 | -41.99892 | 2026-08-09 04:10:00 | NPP-375D | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 737eceda-69a5-3f68-9d38-f736d21b00b1 | -21.3205 | -43.77214 | 2026-08-09 04:10:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7f84bf20-eb66-30af-aab8-b0e5b38d65b2 | -19.76492 | -44.63348 | 2026-08-09 04:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 23402d10-2a7b-33d7-baae-f7b74bb79683 | -19.04434 | -43.34238 | 2026-08-09 04:10:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bbb32e3b-ba15-3d97-bce0-0a378380de7b | -20.54675 | -42.39947 | 2026-08-09 04:10:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a6fe3f97-ea5c-3b3b-b663-136333964068 | -18.91976 | -48.35225 | 2026-08-09 04:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f1f8156-3559-3bda-a0ac-4503eb8d542d | -20.38016 | -42.00259 | 2026-08-09 04:10:00 | NPP-375D | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8c61ec0f-fe70-3962-ae44-5fee09e0d1c0 | -19.93768 | -44.3754 | 2026-08-09 04:10:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a66e63c2-435c-3f82-afb2-05136f0fe165 | -20.13178 | -43.68313 | 2026-08-09 04:10:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ab4b993-9a31-322c-822b-5dcfcdd75c2e | -19.76299 | -44.6351 | 2026-08-09 04:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3876bc80-4a98-380f-bf3a-7fd959dd1f3b | -21.92545 | -43.04055 | 2026-08-09 04:10:00 | NPP-375D | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9969fda5-e6fb-3e93-8d9a-a4c705835802 | -18.03486 | -44.37344 | 2026-08-09 04:10:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d74fd78-1673-392d-b6c9-c040c972f73e | -21.66986 | -43.60979 | 2026-08-09 04:10:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 883db067-e66c-355e-9cb6-54dcd8d004f6 | -17.76069 | -42.79724 | 2026-08-09 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95772bcc-cba1-3927-b5ab-6a98a370489f | -19.5769 | -42.58648 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 95aa0be4-aa08-3d11-9f02-7bae4db0a6be | -18.00328 | -43.31363 | 2026-08-09 04:10:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61360960-b716-3690-9f56-adc6ee929313 | -20.55081 | -41.02377 | 2026-08-09 04:10:00 | NPP-375D | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f77728e5-a6f8-3fe3-be31-94574e890a1f | -15.37357 | -53.78098 | 2026-08-09 04:10:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 766a74a8-e8de-37aa-b919-2d887e8d93af | -23.40628 | -46.99687 | 2026-08-09 04:10:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65e64223-1b89-3d51-8ab1-e2f8e905d403 | -19.18833 | -47.1914 | 2026-08-09 04:10:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6f5ae49-406d-32f1-b579-411558cc47d1 | -21.66263 | -43.63223 | 2026-08-09 04:10:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 36be3efb-33f4-3758-92ac-d6248cf85534 | -19.58968 | -42.59264 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ab430f87-3f80-3d41-b1fc-939274057a43 | -19.33846 | -44.53666 | 2026-08-09 04:10:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 834a89df-b099-37ab-b161-60a462aa60d3 | -19.19054 | -47.19269 | 2026-08-09 04:10:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 83783208-e195-3a49-97e5-244a533562bd | -20.3829 | -42.00687 | 2026-08-09 04:10:00 | NPP-375D | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0c069fd2-99e9-3ba0-b4a2-c4db989280d0 | -20.57985 | -41.91603 | 2026-08-09 04:10:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 88c36358-a14c-33cf-ab31-a7ee10891c7c | -22.23293 | -43.04218 | 2026-08-09 04:10:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c6a02515-18e3-3431-b0e2-a231b8a84610 | -20.27017 | -41.6463 | 2026-08-09 04:10:00 | NPP-375D | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 53a095bf-eac1-32e7-8ab6-4fe88a92467b | -19.58237 | -42.59515 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d4cfade3-9632-3620-a711-054099392e6e | -21.33289 | -43.78167 | 2026-08-09 04:10:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1d48d1b2-40e6-38ef-82d1-25f4b266c2ed | -15.36561 | -53.7854 | 2026-08-09 04:10:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 188a0357-225b-3152-a872-a013192cd594 | -22.2969 | -42.60599 | 2026-08-09 04:10:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ceb17dc3-f80e-3904-8d20-71b3364fce0d | -19.58633 | -42.59202 | 2026-08-09 04:10:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1627f86f-691e-3f0b-863b-1e64d8b4517a | -21.08289 | -45.60418 | 2026-08-09 04:10:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 526699dc-ae82-3126-b381-6cd714092eff | -18.63617 | -49.87049 | 2026-08-09 04:10:00 | NPP-375D | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b4c6cc42-1a34-38d2-b21e-11f8002fdd18 | -18.63975 | -49.85287 | 2026-08-09 04:10:00 | NPP-375D | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 300855da-bd90-3af1-8209-122f46b96dba | -19.19245 | -47.19228 | 2026-08-09 04:10:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb65459e-ae82-32cc-8e5c-0337481c9e53 | -18.98208 | -43.35979 | 2026-08-09 04:10:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e5353652-24ee-3309-9d48-4818e0c9d16f | -21.6705 | -43.60593 | 2026-08-09 04:10:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eb952c64-35c3-3857-89b3-1900f1722202 | -18.93707 | -43.47983 | 2026-08-09 04:10:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6da96e0b-f10f-3be6-8b15-3b614ba12b97 | -20.21593 | -42.58168 | 2026-08-09 04:10:00 | NPP-375D | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 523228fa-4f1a-30fa-8211-bf9b6ab2148b | -18.98142 | -43.36368 | 2026-08-09 04:10:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e079a0ae-6908-35fe-8dd1-cb5576ac94a7 | -20.97341 | -43.9226 | 2026-08-09 04:10:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d82dc9a2-697c-310a-b6a9-8576a46b44a5 | -22.07292 | -42.34005 | 2026-08-09 04:10:00 | NPP-375D | CORDEIRO | RIO DE JANEIRO | Brasil | 3301504 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42a32418-af6f-35ff-9761-e4b65021b7f2 | -18.63737 | -49.86461 | 2026-08-09 04:10:00 | NPP-375D | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f35cdb3a-2e54-316f-9df8-979202e9a5fa | -19.18759 | -47.19519 | 2026-08-09 04:10:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b47b4dd-a354-3d5b-9beb-904da266832c | -21.2745 | -42.93789 | 2026-08-09 04:10:00 | NPP-375D | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0019540-3b63-3f08-b778-25977aafa783 | -18.63004 | -49.87527 | 2026-08-09 04:10:00 | NPP-375D | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 72e6c62c-2642-3244-9fe9-0368e344a055 | -22.89175 | -43.50467 | 2026-08-09 04:10:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e2307023-2612-3aa4-979d-c90fb66636bd | -21.32949 | -43.78101 | 2026-08-09 04:10:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5502d96f-853f-3ae1-80f3-521536495803 | -19.15037 | -43.50158 | 2026-08-09 04:10:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f38d4374-c61f-3bec-8d17-27bfa93b4acb | -19.87553 | -44.00499 | 2026-08-09 04:10:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 22ced099-754f-3c66-9f59-de66ce3e1c6b | -22.90726 | -42.93728 | 2026-08-09 04:10:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c3a5b559-e0d7-3839-978e-afa3162b5fd4 | -20.26959 | -41.64998 | 2026-08-09 04:10:00 | NPP-375D | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 21bfafe6-f1c9-306c-ae71-5771a24fd2a6 | -20.55671 | -41.24085 | 2026-08-09 04:10:00 | NPP-375D | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3cceba6a-68eb-3617-870a-f36b2d61935d | -20.38622 | -42.00745 | 2026-08-09 04:10:00 | NPP-375D | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d9cc7608-64b8-32ee-b624-cb1189e81167 | -22.90877 | -42.94918 | 2026-08-09 04:10:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 76edfb15-c985-3d16-9822-9e32f2a3403c | -21.31985 | -43.77604 | 2026-08-09 04:10:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e19ac955-64af-30aa-8aea-938890bad3e5 | -21.27785 | -42.93851 | 2026-08-09 04:10:00 | NPP-375D | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 94874832-6368-3a5a-bc46-e01e43f16c8c | -21.32325 | -43.77667 | 2026-08-09 04:10:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
