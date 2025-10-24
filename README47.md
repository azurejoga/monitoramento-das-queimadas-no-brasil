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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 522a518a-2c02-3e1a-a09e-9049d4d7b131 | -12.28998 | -47.46147 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbe9171a-eb19-374e-b5d2-9bdd84d6aa06 | -12.29577 | -47.45706 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e35e29ca-dae0-3bc7-a857-63d4e0d83166 | -12.07347 | -46.43709 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 960a5620-9af2-353b-96c8-9e0720c5f8c4 | -12.07483 | -46.4276 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ac8423b-5bd9-3f02-8930-1d330891b929 | -18.24792 | -44.19386 | 2025-10-24 04:40:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93fe52d6-76c3-348a-af9d-ab9b92315e98 | -13.52971 | -55.64976 | 2025-10-24 04:40:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 236b749a-2931-34c0-9aaf-0229121708c8 | -16.9926 | -51.47651 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa58ce0e-f7dd-3491-b463-974d332832cd | -12.26234 | -47.44886 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d584d65f-6d21-37e0-b6b4-e171cda0fa02 | -18.46531 | -44.45319 | 2025-10-24 04:40:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a816b742-baac-38a0-b1af-18f2b126c487 | -15.29475 | -59.26637 | 2025-10-24 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f505ea48-8776-36ce-8378-18f1137ccac2 | -13.25202 | -47.88488 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1e5122b1-f93a-3138-9399-0bbbdaaa6547 | -17.59991 | -46.62564 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10f18ef0-1fb1-3cfd-8149-45b2fab417e7 | -15.44355 | -48.57547 | 2025-10-24 04:40:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e80904b-7e8f-395a-b772-836301244ec4 | -13.34085 | -47.96913 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccaa8197-fb4d-36ef-af7f-750d4a3d9e34 | -10.44814 | -52.72812 | 2025-10-24 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49f55e58-5f24-36c6-a6f7-77621636bbe7 | -12.06093 | -46.41607 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ba82897-8802-3c8e-972c-abcca9ed94de | -14.2078 | -44.60102 | 2025-10-24 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e5c8c30-6aac-3e89-aae6-5bce3082a526 | -11.01791 | -49.83766 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a7fe8d4-4613-3e26-8dce-0d4fe13a75d5 | -13.02444 | -48.57561 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b40da4-f1e4-3a4c-ac5d-03c8bb059e58 | -16.12998 | -54.00461 | 2025-10-24 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 128c540f-2796-33e1-bb8c-946905ca3dfe | -17.65369 | -46.65596 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 605824cd-b3f2-305e-963b-cdae6961d995 | -15.67188 | -53.34005 | 2025-10-24 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78546c76-79b7-3543-b471-87773033cf50 | -12.73497 | -46.34527 | 2025-10-24 04:40:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41797875-6a80-339a-a24e-a26234d02d5f | -12.17486 | -46.56394 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccdede5a-96cf-3b2d-b801-dad3a024b6ac | -12.17905 | -43.60619 | 2025-10-24 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 040a62d6-841f-3e30-af10-d5464e8b87cc | -14.47626 | -47.908 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5371856f-62a6-34b0-93f9-a7cdb497dc70 | -11.02319 | -47.90959 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf52a521-0029-3d3d-889e-b87451bb8683 | -12.72332 | -46.94338 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfcaf13d-894d-3e20-ac11-caea0277b785 | -11.36001 | -45.94207 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f2bdef4-2a09-3383-8c8d-6f4000465123 | -12.06854 | -46.6318 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94ffc835-499f-3c15-a0d4-656dcd8e2266 | -13.64946 | -46.80802 | 2025-10-24 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2414e76-2081-3ce0-b940-12a68ff7c25b | -13.91008 | -48.37343 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d4e40fb-0e74-317a-8a35-eb72ed941b93 | -17.65223 | -46.66705 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4799c874-1877-309c-a66e-4eec574596d0 | -14.20513 | -48.35451 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d9ace9c-11e6-3ef1-b30e-f0291351222a | -11.34291 | -45.89435 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 988f73a7-b968-3a7d-b5b2-f9fac07d63c1 | -14.77197 | -44.97526 | 2025-10-24 04:40:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c93f0ca4-440b-36e2-a942-034faa2f11fa | -11.99263 | -45.4249 | 2025-10-24 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c59f0452-78f2-3d02-8e2c-127dd70dfca5 | -14.75757 | -46.60762 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97190550-345c-30d5-8a5a-bd94804b0a1f | -13.28439 | -47.48093 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2287a9ea-c7e1-3460-b77d-f469c9e8497f | -10.94643 | -50.37923 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e4d2f37-d042-3879-9e94-a63c99e5677c | -12.07415 | -46.43234 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9075f9f3-d6c5-31df-8338-d6bfb305dad0 | -14.74193 | -46.60563 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fac5883-f5a3-31ef-b81e-18c6e80cb3db | -14.46853 | -47.91039 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cb8e015-1f02-36d4-9c5d-fe1ba7929699 | -10.98303 | -50.36388 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6da32505-6398-31ef-b605-9de863e32d0b | -13.66754 | -47.95517 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00a4fac0-e213-3eca-9d2d-0b00b8c9030d | -15.62794 | -48.54697 | 2025-10-24 04:40:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77c4299d-8e3c-399c-b9a5-f93cbb21e89b | -15.84457 | -49.08743 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7822966f-fb0a-3837-b747-77141fafce53 | -15.3233 | -47.25153 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa8b2ea5-e650-3ddf-b44e-556e97c4a301 | -12.06161 | -46.41132 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa80d984-7434-3d79-80f9-d224bda3c6d7 | -14.20575 | -48.35035 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5a47f28-ad7f-3ce0-8654-b378adf09d29 | -11.53883 | -52.23972 | 2025-10-24 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 868c4425-a755-30ee-9db7-771de192c149 | -11.32673 | -54.26098 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e44e53da-86b2-32f0-a70d-74a45b0a9561 | -13.62124 | -49.45235 | 2025-10-24 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7d6bdd0-c9cc-351b-82a0-02b19c69226f | -13.21345 | -47.73463 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cb6517a-9c9e-3597-8cb7-176c5a4b87c1 | -12.0671 | -47.15094 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6667b2f5-50f2-3009-86da-d8b142ab2e89 | -10.60743 | -54.00286 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 457e0f9b-1a19-3c6f-931b-715398123895 | -14.74128 | -46.61029 | 2025-10-24 04:40:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cf55d44-eb86-3172-867c-586529d7b565 | -11.92644 | -46.78539 | 2025-10-24 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf5bafa-5772-33ef-96c3-2e1e1cdeef40 | -15.8376 | -49.0865 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e456fb4a-d9e3-33ba-ae1c-2f0c22261842 | -11.55471 | -54.51447 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df4f8992-76cc-36d1-aa38-4f5b0d93ef47 | -13.18879 | -47.75246 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50c3d3af-1240-3695-a7e7-ee4927374763 | -12.17896 | -43.60773 | 2025-10-24 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1fc8f61-3e2a-35b3-ae2f-606f2614de8e | -11.36913 | -45.93365 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 850778c4-11fa-3621-986d-3411203d34c4 | -12.01877 | -46.92105 | 2025-10-24 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c2d951d-47dc-3e6f-b5e6-619564ec92fc | -16.16369 | -49.9728 | 2025-10-24 04:40:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1d95a98-8a39-3ff7-9189-31ffcec7cfce | -12.37281 | -51.47236 | 2025-10-24 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 893b3060-50e4-3f2f-81f6-b2c70a3b4945 | -13.88486 | -48.36988 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0707eee-0c8f-334e-9e50-8d2d2775360b | -14.32903 | -52.56854 | 2025-10-24 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 552dc965-e856-3ad9-9911-017ccaf6ac3f | -14.43315 | -50.95057 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b9b0b05-b2f6-3b4e-9952-5a995f6d4c1d | -11.36276 | -45.92265 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b990ed55-2fc9-364d-a5c1-d11934ff3a9c | -12.84923 | -48.55748 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b87d9c15-2cc9-351f-bd83-26358c4bb139 | -17.59944 | -46.62935 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c7f10eef-f00c-3ec2-b5d2-1acdb26f517a | -12.81026 | -50.94533 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d7f19e1f-6795-36b8-be46-363c9e197343 | -11.8701 | -46.7538 | 2025-10-24 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72556759-c145-398f-9a20-02349dac9707 | -15.12913 | -47.93473 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52aaf6f6-d5f0-3fec-8293-bcdab1c024fc | -13.35924 | -47.96778 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e778e5fe-58c9-3415-9fe0-b9e9314a6112 | -13.90068 | -48.38877 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59bbf97f-c931-3bb2-91e1-54dc9ae5d997 | -11.03912 | -47.88283 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a099eda2-ef21-3ae1-a7c4-3fcde5d85a80 | -14.87474 | -59.62446 | 2025-10-24 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39dc4c76-2b81-381e-ac1b-4b3b665b1704 | -17.65272 | -46.66336 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 75662cab-3f20-3f07-b4b9-ddd662a41f99 | -14.43535 | -50.95821 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d19059a1-c2db-38ad-b661-0884ab68e65f | -12.82015 | -50.96865 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dcb99829-e876-36c6-8827-f9cb2d096fff | -11.9753 | -49.17577 | 2025-10-24 04:40:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9084842-f7bc-38c8-b462-63c5ecce8032 | -11.01445 | -47.87286 | 2025-10-24 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d082931f-cdb6-3a37-a7a1-c933a1208848 | -10.66414 | -54.31545 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd149d2a-9580-30b0-8709-de6101096980 | -14.77038 | -49.29897 | 2025-10-24 04:40:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c866f043-17be-33ad-af38-d2f85b9848e8 | -15.94454 | -51.05667 | 2025-10-24 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 116988da-fb4d-36c2-8b61-e8ab62e6bd6d | -13.35445 | -47.97561 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c3a7228c-277f-3569-adc7-4a085a48f980 | -11.36706 | -45.94826 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f313bcb4-82f2-3c80-bec0-4ad20411e79e | -11.35721 | -45.96189 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 537089ea-1375-398a-9bd0-66bac57b3e10 | -12.81302 | -50.9494 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3515e5a-8c36-32c6-a9c7-3c47d3f7b361 | -12.07438 | -46.40358 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 62a67755-71c9-3d09-9ac0-bc0bc436af3b | -13.28313 | -47.48985 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e172fa-2248-3624-adf3-79c8ddbf0ae1 | -11.9878 | -43.32765 | 2025-10-24 04:40:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d286ea7e-b5fe-3cba-a12f-ca1ebd366cad | -10.58647 | -49.64299 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78bf8591-63e2-3a40-9e74-be81de4ee5a7 | -12.82402 | -50.96567 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aab62b4-a0b7-3416-aea0-d380e87b5b79 | -15.31626 | -47.85244 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8aa23d7e-21a2-3e57-aab1-57e2682dda12 | -14.72227 | -48.32297 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dfe394c-21ae-3d92-95e7-66710646830a | -14.44033 | -50.94811 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbfb2e68-9452-3f69-a9ea-0103d8fdd161 | -13.33665 | -47.94793 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
