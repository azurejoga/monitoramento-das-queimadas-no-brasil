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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31c037d4-d8b8-3643-8029-d8933b2c8ae7 | -6.1071 | -41.72167 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bf3826a7-bb04-37e0-a4c7-66659a9e1c0e | -5.69948 | -43.15339 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bdbab7c9-1ff6-36a8-93cc-4e4ef63cf755 | -5.03791 | -43.61695 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 89891465-d25d-3afe-b2cf-0cb5ffa00ac4 | -7.80251 | -46.41628 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b22e1ff9-2fbb-3244-b2b7-222e8f1ec4b1 | -6.30907 | -44.05694 | 2025-10-30 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c6918e0-5abf-3243-9a00-034ade570b44 | -5.23122 | -42.68085 | 2025-10-30 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c9584e9-db51-3f85-ae18-75f3d3e4dec0 | -5.0617 | -40.47137 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3c5dd761-5fc5-3c27-b7f8-dfba61e7ffab | -4.92016 | -45.71647 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a351756a-38ea-30be-a102-702fa0a81d34 | -5.50798 | -41.73094 | 2025-10-30 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ca9b73fa-1393-392e-bb30-81f4317b97b4 | -7.31894 | -44.12468 | 2025-10-30 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcf662e4-8db3-397a-abde-008d85cd1eea | -7.62544 | -43.60831 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0319132f-773e-3148-80d4-a0cbd16d0d31 | -6.1548 | -41.66488 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0025957-4442-3cd9-96d9-586fecc2bdf2 | -3.22563 | -46.87704 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 68b2d7a9-0c1c-3e88-9763-8e1854da481e | -6.85951 | -42.14323 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a826ebf9-165f-3398-a9c7-9af1c4058bac | -5.35454 | -40.79874 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3f3f232-0737-3663-ba51-8156d4fb460a | -6.86031 | -39.56238 | 2025-10-30 04:04:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 02e511f9-fe1e-35c8-8437-d9fae7f73779 | -5.92484 | -47.32053 | 2025-10-30 04:04:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a272a462-38bb-3f46-8b4e-03e5dd856c09 | -6.10831 | -41.71418 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7c29ef61-2ae0-32f9-9452-ff2861aae590 | -6.12378 | -41.70531 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f3ac6ff-d23b-37b0-b18e-45eb1191053a | -6.96792 | -39.11511 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9e8de6f-f3fe-394a-9d21-7a91236fb49d | -3.24963 | -52.9132 | 2025-10-30 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d32193e0-1b2a-31fa-a4af-c0b669efde5c | -3.58435 | -41.05188 | 2025-10-30 04:04:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e344fcb-764e-3c19-80a9-9c1db8af5f26 | -5.80824 | -40.84141 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 249879d3-f3e6-394d-a125-cae26e790b85 | -6.88798 | -38.28242 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 350f4ce9-5b9c-3087-9593-3583fc890f45 | -6.14086 | -41.70819 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 75262f6f-107f-333f-bcb0-bf855b54211a | -5.6988 | -43.1576 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| dbaad8d8-396e-3581-80f6-0f7aae804255 | -5.81927 | -44.41301 | 2025-10-30 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f843239-6856-30ca-8d31-a90438a0f974 | -5.03625 | -45.17086 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aeb0aa1f-7f6a-30db-8670-5a9f8d964eb1 | -6.48253 | -46.88577 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a95b4379-f166-3712-919d-9120ebc3f398 | -12.75136 | -43.44936 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46bbeac2-e816-3af6-a92d-34627ffca780 | -9.81476 | -47.584 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b921393-8393-3a61-8c82-10d7fab94312 | -13.61114 | -43.97347 | 2025-10-30 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 508e96ba-8fdf-3d5d-93c5-4df2bf2c5332 | -12.51454 | -50.56757 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 20fecfb2-9985-3b81-8121-c5807e47b642 | -13.37036 | -47.38086 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 240dd266-1482-3c90-aeae-0607855bba3a | -14.40801 | -42.65884 | 2025-10-30 04:06:00 | NPP-375D | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| daf15f54-fece-3305-b20e-5eb642ae434b | -9.93304 | -47.86867 | 2025-10-30 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e4dbe0b-5ef6-379d-8835-942b2df70e3b | -10.49233 | -43.32872 | 2025-10-30 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de6bbc85-a2c4-3d9e-98b1-f4db9c8ec85e | -13.29747 | -47.06808 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2440c8dd-b7bd-3cd6-9f2c-79795029fb00 | -12.85101 | -48.62389 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 017207a3-b871-3748-8bf3-db4a8d0ae69d | -10.98182 | -50.11886 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7097311d-6ae0-3a20-85a9-58cd644dd2f6 | -12.22114 | -43.70693 | 2025-10-30 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79f5156b-fc74-324b-ad64-fed21be7085d | -13.88429 | -43.93565 | 2025-10-30 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6b2ca34-0da6-343d-a987-06adaeb787f1 | -9.98121 | -37.04176 | 2025-10-30 04:06:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 52c254a3-6c09-3f9a-afee-f7779933789c | -8.79045 | -42.83152 | 2025-10-30 04:06:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b5904885-9385-3b51-8d94-2f92cd816fce | -8.70504 | -47.98344 | 2025-10-30 04:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa6dc9e0-3f60-33c3-b3fb-2892f132b005 | -9.85812 | -40.59217 | 2025-10-30 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43692e45-b642-3ca8-bd5e-7f446322adef | -10.36615 | -44.12847 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3cddf1b-9381-3541-b256-dfa6ab5bf632 | -12.2948 | -50.33093 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64dcc536-39fc-3cc3-93fa-d1f900a154b2 | -13.23536 | -47.72524 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2734b0af-b58d-306c-b2c9-012b92a50c13 | -10.26649 | -44.58301 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 905f4caa-632a-3b0a-a61b-869250447982 | -13.84347 | -44.15862 | 2025-10-30 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab264753-ccf0-31ea-af92-35056df71868 | -10.27327 | -44.56573 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9876067-b81a-33a5-b4ce-6aa0fd183bb6 | -12.74764 | -43.4291 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7c3e4ad-919d-3e74-a640-a3993d2c8be7 | -13.35665 | -43.08667 | 2025-10-30 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3f15d884-7f83-34f9-9686-b1054a0e456c | -13.3328 | -47.68496 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e89d28f8-b309-38e3-b348-d2885d658071 | -9.04906 | -47.81839 | 2025-10-30 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b5bfb6e-ebc1-3dec-aa1f-bf3a7540eec4 | -12.3147 | -50.3116 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c140dee-efad-3390-af07-042193ef0fe2 | -11.17055 | -45.2229 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 212f46cd-5bf8-3f93-9757-5d4d2c2bb141 | -12.91483 | -45.04972 | 2025-10-30 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3039b7cc-7111-3c12-8bbf-1d9855075559 | -13.11531 | -40.22777 | 2025-10-30 04:06:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 080c4930-5e77-399f-9817-cd676c91be7d | -10.75876 | -44.73607 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0c468ba-5354-3274-83a9-30022fe9628e | -9.88152 | -47.44747 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e6d434b-312e-3955-a119-dab76df4e3f6 | -12.48758 | -50.56548 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e8b7bc5-a0f9-3f2d-886b-b1b89243feb9 | -9.90342 | -44.89476 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f19c85a-926d-3f34-9458-7bde6c72919d | -13.48413 | -44.06121 | 2025-10-30 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c389c6c-754e-35ee-bb73-5234fdb9501e | -12.88027 | -48.64668 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6324ac12-5230-3cd3-b92d-f83c83de14d4 | -10.48413 | -44.00341 | 2025-10-30 04:06:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9693db80-1651-3dfe-806a-4b49b0d20e97 | -13.70362 | -44.04517 | 2025-10-30 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45a6a2f4-0d8d-3315-9349-b7c4c9d8b23d | -9.93854 | -47.17952 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0ca3891-8132-324c-b8f6-fa469a6d0118 | -10.01473 | -48.23018 | 2025-10-30 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 197e0586-0433-30d2-ae79-9aa97c229061 | -12.3143 | -48.0581 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ccf69498-87ff-3443-9300-ddfe99c56606 | -11.17135 | -45.21821 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5179798d-bba7-35c5-90ac-b28d01215eab | -11.00503 | -41.68125 | 2025-10-30 04:06:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b496405c-d82a-31db-aa65-36e79fb0fe7f | -11.72162 | -41.66045 | 2025-10-30 04:06:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 68937038-9746-350e-85bb-05ad2ec5ef5b | -11.05977 | -50.32561 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1cf8250-afaa-3aa2-b32c-99ecc56ed0c8 | -7.96083 | -46.72234 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66cdff91-9115-312d-9c26-b97502ba1f27 | -7.95779 | -46.73978 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5220e2bb-7c55-3207-9f65-17a98463101c | -10.96227 | -50.22475 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d6778dc-5943-38b2-b01d-3ed82f7bf646 | -12.81355 | -43.45149 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c29eff30-baaa-349f-b0a8-4b3369edcbe1 | -9.90041 | -44.88942 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddc3727a-c466-3198-9ade-c3b12d330045 | -10.93237 | -50.20838 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbca7103-3547-3a7d-9a89-1d8fd2ab1eb4 | -13.30293 | -47.70248 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fb6e90b7-d4bf-3465-90d1-f91a8ee4a83e | -10.34306 | -47.26001 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 097e1edb-f4ca-3406-96e0-e3c567455cc6 | -10.35007 | -44.06896 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cc9ef64-bead-359e-a917-e208ec2b86ba | -10.96709 | -50.21878 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0a91762-1a58-3bc1-b706-5799db1bf8d3 | -12.58086 | -44.96912 | 2025-10-30 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 79d7b532-082c-354b-83a3-f16108e6d8cd | -14.29014 | -42.33687 | 2025-10-30 04:06:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5aae4071-b2d1-3abb-97da-39b694053638 | -8.70269 | -47.91488 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1fe62a3-fcf6-3631-a1e5-1260c14d79cf | -12.47514 | -50.57327 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 588e6233-17d7-3652-89d7-a8fbd0cccc03 | -12.7548 | -43.44996 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 258c4d50-d2ae-3b2c-8721-484cee99932c | -13.37453 | -47.38183 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9f76a53-51b0-3a16-9bea-5bdcb062f676 | -12.14409 | -48.01581 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2b778bb-92d9-3d5c-b41b-a4ec95f769c1 | -12.17846 | -47.75529 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2742a6a8-e196-3759-b43f-1aa013ce7d92 | -12.48916 | -50.60329 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dd71b83-6bbb-3f3d-9981-947b52f0bad8 | -13.60824 | -47.59548 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2dbba9c5-86c9-34ec-a9b6-a75ed078e45c | -13.32882 | -47.465 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18de527f-c14b-36ff-ab1e-6a2e27553c77 | -13.53043 | -44.3421 | 2025-10-30 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27946ad6-2b07-3ab1-804f-c1ed1ee0ece8 | -12.18281 | -46.70811 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 844f0100-a818-3b3e-b677-51209d2945a6 | -12.51348 | -50.56342 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77ef530c-12d2-3661-b6fb-e11d1040a0fb | -10.92948 | -43.7582 | 2025-10-30 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
