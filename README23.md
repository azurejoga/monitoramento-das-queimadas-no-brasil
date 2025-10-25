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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e180105c-c500-3a74-a0f6-b6f1f9bb8d3b | -10.64148 | -45.23354 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb1e2646-bee5-3cf0-aea3-a4d8728f8bcb | -14.15477 | -44.31599 | 2025-10-25 04:00:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 663ac6f1-d635-33a1-8291-4524c4418b8e | -14.18199 | -47.31884 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 860240c2-8347-3d6f-a6b4-05697e732704 | -10.52532 | -44.22443 | 2025-10-25 04:00:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25e30783-d8ca-33b2-8362-74b634be49a2 | -13.89027 | -48.40804 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e6a1749-9176-3e8a-b303-0c7e40eb4024 | -10.34452 | -45.10376 | 2025-10-25 04:00:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef07e1eb-e2ea-39cc-a611-222e8d54d462 | -10.25412 | -48.00019 | 2025-10-25 04:00:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80248e58-15a0-345d-b25f-2f5dff45c80e | -11.91686 | -44.18043 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d530e946-49a6-3267-bbfb-83cdef95fa5d | -13.61969 | -48.45112 | 2025-10-25 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b694eed1-1b47-325f-b23b-6367371706e0 | -10.89592 | -43.82312 | 2025-10-25 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96554d08-ea05-33a7-ac4c-4736e72ede8c | -10.41521 | -44.49696 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 01f0eb5e-5bee-39ce-b5f9-ba05edeab114 | -10.76271 | -44.41379 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 242a35b4-7078-3696-83f9-53ff6c76eb1d | -14.86564 | -48.09095 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2f36c5b1-15e6-38ae-990b-6d8fc6b8e285 | -13.35628 | -47.41223 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46f7dc66-3cc1-3a3c-a3b0-35d1b58fe826 | -14.43764 | -48.07035 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09fa2305-37ef-3323-90ff-79bfbe9c8ea4 | -9.30143 | -45.18396 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82c5a412-72bc-3189-b54c-59cbffe73872 | -13.45402 | -44.07219 | 2025-10-25 04:00:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78072a94-e546-3524-bd7a-c2dc85102845 | -12.1306 | -46.7113 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e596d8b5-22e2-3d9e-8ef0-1514ba52160b | -13.74519 | -44.33364 | 2025-10-25 04:00:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77f9e58a-6b9b-3fea-9c03-01aade9328ae | -12.06667 | -46.3976 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccc2a34c-1b9d-3ccb-a255-5e23cafecfb4 | -10.70993 | -44.74526 | 2025-10-25 04:00:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a2824e-4325-381c-899d-f50fe27abc1b | -10.17787 | -44.6678 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d3efd73-327b-319b-a1c1-fdbf7a2e0a5c | -12.94596 | -48.50608 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9554314-277c-3346-b89e-759a2e3ed6fc | -15.52929 | -45.7091 | 2025-10-25 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84ce76e1-8784-3c2e-9ca4-d00e3fa5b5e3 | -14.54006 | -48.02079 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 776a5a05-f96f-3c3e-9aba-6f5891d2c216 | -14.81532 | -48.44843 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c06d2ba0-3980-3204-a344-aed0a08931cb | -14.8682 | -48.1031 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 17814d87-d216-35a3-afb9-fdb99f4a1ce0 | -9.99131 | -47.09531 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cef3b392-573a-31e5-aa62-3d2b90fa6c2a | -12.10887 | -46.70532 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84376d63-c349-3a26-b382-5028b4f08cfe | -12.00806 | -44.02366 | 2025-10-25 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb9bd4fa-4a4c-371e-806b-82fd41efe491 | -14.86473 | -48.09946 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 400b79a8-de58-3aff-8d7b-52fe9e5948c8 | -13.37977 | -44.32866 | 2025-10-25 04:00:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8696b2a-09fe-33e8-a1da-2c4b3cf0248b | -9.32111 | -45.19913 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83d28397-3ebc-3d10-9e02-56be1dc945b8 | -12.48063 | -43.86287 | 2025-10-25 04:00:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1fbd2af-5f25-3f3d-a49f-3f791066b84e | -14.33696 | -43.7364 | 2025-10-25 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d37c36e5-d8e8-37a0-b3fc-248126ba3a70 | -12.83937 | -48.64834 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ed295b4-6698-3b8b-b8dd-fe7a7ac67c22 | -14.01778 | -44.21734 | 2025-10-25 04:00:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62d09077-656d-35a6-b9e5-c1e65ae67958 | -10.66794 | -48.06614 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d12a5244-dfc4-324f-b6ae-6bdeb783b3de | -14.92247 | -48.12953 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48cbadb1-e8ad-329f-b07e-48254e5fbeb3 | -12.94909 | -48.50546 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 072eeee8-df66-3cb0-af40-ea5d9fd8d7a6 | -13.44696 | -48.60118 | 2025-10-25 04:00:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c665aa8-f63a-3c1b-be9e-c6f66ca8ab53 | -12.83692 | -48.63359 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00e838e0-ed97-360e-9757-b2424a68a9db | -10.80288 | -49.65118 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a27e0dba-2e02-333d-b057-054ff2d24e9b | -12.07554 | -46.39974 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e317b637-7bcf-3cc4-9d93-e0a5b035b843 | -12.06762 | -46.39246 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2a3be15-3872-308e-9131-1c26c29373da | -9.09536 | -47.82237 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee021038-4169-3af0-99c2-54ed020e59f5 | -13.09707 | -47.00843 | 2025-10-25 04:00:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81db7061-d012-3d60-be34-36648c3f395a | -10.63727 | -45.24157 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc6bfac6-a2aa-318f-975c-ce4da2a3580c | -12.11236 | -46.70774 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87145081-dffd-33fe-8b19-3fe8e265060d | -10.62531 | -42.30978 | 2025-10-25 04:00:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14c32b0d-e52a-3da2-a84f-cd6fa3ad2e96 | -12.26874 | -44.80299 | 2025-10-25 04:00:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29a39d34-bb27-3d1a-a895-0b945037be8f | -9.92508 | -47.99953 | 2025-10-25 04:00:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5d01874-7d51-3a95-948a-de21f954376e | -12.29715 | -47.45259 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| addff6ff-61c5-3436-8533-de5b310a2111 | -8.54887 | -50.04294 | 2025-10-25 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ca43a07-f4f6-3dcc-a317-1dc339b5a60a | -14.40169 | -51.52463 | 2025-10-25 04:00:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e63016f0-dcfe-3825-afd2-db91aefe8c99 | -12.16728 | -46.56355 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50aa4de8-3eee-3e45-8db1-559bf82f5e00 | -10.00184 | -47.59073 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d85a0bb-08e6-3b49-9fde-7fa6e9828c40 | -9.87149 | -44.8898 | 2025-10-25 04:00:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9543fc6-0acd-350c-b671-76ba253bff40 | -10.00019 | -47.59954 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2487107-49dc-3501-a602-34115fa84025 | -14.92955 | -48.52283 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ae9a12e1-be5e-3396-a31d-0dae27fc3735 | -9.23969 | -45.61547 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 181cc8a3-ea16-3256-8238-f5f88899ee65 | -12.05686 | -46.40054 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb368729-40e5-33db-838c-9b43474e711a | -9.32574 | -46.987 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a5a6e13-d547-3438-9927-da4c859f796a | -12.05195 | -46.42702 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bc2e9d6-bdb2-31e5-848c-60226320b462 | -13.41173 | -47.95108 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13eec94e-7062-3d27-903a-563300924957 | -13.34686 | -47.41071 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6eb2353-4eaa-369e-8da8-c011217cdd7f | -9.99964 | -47.60252 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0db8e657-8cd9-3ca3-92ba-721da7d29297 | -13.20898 | -44.10818 | 2025-10-25 04:00:00 | NPP-375D | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9019bf8-ce9f-363e-ac80-a8b3759b1858 | -12.12061 | -46.71421 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce31e7a3-fa3b-38f0-8b7e-2d80f62c352a | -12.94657 | -48.50282 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8747171-0ce0-3cdf-8d77-49e75be54d23 | -13.87906 | -49.04908 | 2025-10-25 04:00:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 403b2e07-6014-3487-9fbe-191f184d8a66 | -9.09014 | -47.8214 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a987b30-f23e-3eb0-8d63-421d70d48822 | -12.04434 | -46.40791 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05ddd073-8a2c-3d67-b7c9-8679266f4a9c | -13.87472 | -48.38223 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fc14d92-09c6-38fa-9a8e-817fd626385c | -12.08642 | -46.41611 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f9e61e9-2928-3593-8db0-1b2ff168530d | -13.42016 | -47.95957 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a35c4871-fcdb-372e-9ae0-d05ca5838966 | -12.2287 | -46.50794 | 2025-10-25 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23bde1a7-6b1f-34e7-a784-e0875ed925f9 | -11.85209 | -49.86052 | 2025-10-25 04:00:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c4a359b-7c14-3fcc-bba2-ff4baca73c9f | -11.77794 | -47.54957 | 2025-10-25 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2f5af7b-8678-3655-8662-dd63f2e1fbea | -10.92478 | -50.41475 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b22c9f3-a2be-32f6-9463-1c3ac2029c32 | -14.53688 | -48.03761 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba042511-95dd-3d5d-a1e9-559552759294 | -10.96196 | -50.28662 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 676eaf47-2757-32c9-8e33-ce95cc82f856 | -12.79071 | -48.67322 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad85b71d-ce70-3b10-85f2-c86c7408eef5 | -9.2451 | -45.58447 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca83ea2e-21bd-39e0-9b84-f7a929aced45 | -13.91497 | -48.41321 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91b42e08-5da8-3726-a35e-cf73b0277d9d | -13.54478 | -47.5616 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58080f07-6fee-341f-8d6c-03fc58573a64 | -14.41248 | -47.91606 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be37a7ef-b495-3bc9-b81d-4e69970db288 | -12.46965 | -44.53408 | 2025-10-25 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b16d3d5-a994-397f-b5a6-a0795d1ac130 | -12.83749 | -43.8139 | 2025-10-25 04:00:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 274e63c7-3829-306f-b272-38336f81c852 | -12.95034 | -48.4991 | 2025-10-25 04:00:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e79a6eb6-4446-3f5c-a5c8-98a1f7363aa3 | -14.88008 | -48.09298 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f5d96e5-eef4-35ea-b286-2a630765e6fb | -18.1711 | -51.76701 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44376c23-0030-3e3f-ba67-b894f2e7b9a0 | -15.00104 | -49.98681 | 2025-10-25 04:02:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7d8cb73-8dc7-3868-bd25-7c94332c3f47 | -18.56451 | -50.27341 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| cc5168af-fa2f-3193-90b7-61a4e9704c63 | -19.8576 | -44.30213 | 2025-10-25 04:02:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c516fbd3-c9bd-3272-967d-e11efaa6fbd1 | -18.70076 | -43.72964 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9097ff1f-3107-36bd-a163-dcd0cffb612a | -19.3213 | -42.28831 | 2025-10-25 04:02:00 | NPP-375D | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94dbd190-3750-3626-ac13-1594051d7822 | -21.9 | -46.55 | 2025-10-25 04:02:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40e43611-e709-3262-bf80-de7048648657 | -19.91212 | -41.89816 | 2025-10-25 04:02:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fc1fd381-6fbf-30aa-93b6-b42af7d17d00 | -19.32825 | -49.08351 | 2025-10-25 04:02:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README24.md)
