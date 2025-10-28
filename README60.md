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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e563179d-63d8-3d2b-9f76-a3dfa7fc3997 | -12.06155 | -47.8198 | 2025-10-28 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7afcbb24-b9c8-30d2-9818-83ade6375d9f | -14.43299 | -47.85152 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0dc837a-1c00-38d2-850c-d8dde61b110a | -10.59391 | -47.9383 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b7f77d5-7f54-3cd3-888c-252ea1375af0 | -11.15859 | -47.71861 | 2025-10-28 04:44:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e74b142-d966-389a-88f3-ef2d760b6bcc | -10.29632 | -49.07291 | 2025-10-28 04:44:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e89da3b-f260-3f2d-b04c-94f3fb845f33 | -14.61249 | -48.41241 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a82718e-a1bb-327c-a365-4b602852d157 | -13.61141 | -47.03412 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55b17ea8-8fc6-3d9d-8812-e5b9b45f0434 | -13.37725 | -43.45586 | 2025-10-28 04:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f590b2e-1adc-383b-b07d-8251d388464e | -9.36547 | -49.26627 | 2025-10-28 04:44:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8a80eee-028f-3594-b3dc-447af7a8e3dc | -15.15045 | -46.59879 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5312e59e-6985-365d-b628-1510715f2069 | -9.46309 | -46.88412 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 511f0de0-ff7f-3735-abcd-58c84c30697c | -13.42421 | -47.37777 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3099075e-b1d4-39fc-ad1e-9cee90bf4532 | -8.8762 | -50.3312 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e5c91df-d81f-3321-8d94-51f996e6b096 | -12.52858 | -47.55509 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 195016b5-0b8c-3314-af75-b66f8a5d547f | -15.20264 | -47.22001 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 358260e8-97d6-308e-ad57-19dc98554c75 | -10.23362 | -52.15006 | 2025-10-28 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d82e60b3-2cad-3a1d-9e71-bbdd2b645ea2 | -14.5616 | -47.98724 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 247874d6-dfda-3d1f-9af7-3ddf661b40c4 | -9.34122 | -43.09052 | 2025-10-28 04:44:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 85cd9e10-d044-379b-807a-b16db530e571 | -10.8648 | -49.63922 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef7da851-5ea5-3b21-bac9-6bb7b13f4d85 | -10.5624 | -49.82838 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ba2caa-a6d9-3324-bf44-3184666a20f2 | -12.08377 | -46.3952 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f51d54e-b754-3ee3-9c52-684c06efc44e | -10.88362 | -48.37764 | 2025-10-28 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fc5dc44-ae3e-3a62-83b9-bd2b3a554287 | -14.62152 | -48.37518 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96fd6294-0531-36e7-b8d3-4f2e478ef392 | -8.56223 | -47.73055 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 600821e8-a6e4-35ce-9305-d7133f842071 | -8.63893 | -44.78677 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8924a827-b1ea-3c92-a68f-90ad1a9bca90 | -15.23145 | -47.94995 | 2025-10-28 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e20f42e-bd51-36c6-a752-31a1fc9d2e5c | -15.57861 | -43.20028 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 12.4 |
| ecb3adb0-5235-3c33-a2a8-f77d29a0b3b0 | -15.17214 | -47.2281 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0af65cbf-19f1-3a7c-bf6a-ae55af81abba | -9.99656 | -48.1061 | 2025-10-28 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6711a061-038a-3260-b6c3-bebcc36d0d42 | -11.13442 | -47.04494 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7da9c05a-4810-30f1-917b-22aa51478609 | -10.22609 | -49.90128 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc7a011c-7e13-377b-927d-9447bddb8481 | -10.91891 | -50.27172 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a323d5ed-a5d3-3223-beaa-3e184b6cbdf6 | -8.70902 | -47.97787 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 021f0a5d-0c42-364b-a1cb-386d2291d738 | -10.58406 | -49.79922 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1c9bfd1c-876d-3078-a793-cc3201881ea6 | -8.23088 | -46.94056 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b750820-19f7-36c0-b45f-f3ed466307dc | -15.15884 | -46.58823 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 987bdc67-dd96-344c-928c-d246cd8ec16a | -12.24012 | -46.5228 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07b5f97a-8ee8-31ac-bfa8-8792f009c1b0 | -13.57807 | -48.53106 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f613b9c6-7d23-39f6-b11d-d9f8862f089e | -12.4697 | -44.49806 | 2025-10-28 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75d6d65e-7db1-3eba-896b-3556f3c770a5 | -8.70845 | -47.98165 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9e6dbad-215d-3ff6-8786-ba5ec0de8b0c | -9.5421 | -46.97692 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94feada0-a898-35eb-a201-5417b7b30e67 | -9.29096 | -45.2239 | 2025-10-28 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87151804-d56d-3013-9e98-53d7ed0e4eff | -14.66327 | -48.41594 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a40759b1-a22e-394a-85ee-9eb5a2ef9590 | -7.85744 | -50.2039 | 2025-10-28 04:44:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27845089-2e51-378d-8b56-1888ace2c688 | -14.53722 | -48.00127 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5706fd54-ef4f-391a-951e-fa1e766e2b57 | -9.95043 | -47.05821 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d3ec20f-6bcd-30ff-a4b1-1848f224b00f | -13.44707 | -44.09932 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5841a0d7-df89-3789-85fe-227bf7a13c9f | -14.72588 | -47.36434 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89671357-e033-3834-ae8d-262d17e28cea | -11.77191 | -44.63958 | 2025-10-28 04:44:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e6164e0-09c4-39f8-9517-289862c89c55 | -10.56184 | -49.83192 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1c4d12e-2fd3-30d1-a3e4-0eb32cb17220 | -10.5458 | -47.82595 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8790ec6a-7b76-30e1-ac7b-0e515aafa380 | -8.87232 | -50.33415 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7dae8af-c87f-396f-ab38-4580cfadad71 | -12.61967 | -45.07766 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27f088a0-ce9d-3648-861a-1cc1c066189f | -10.64669 | -48.04206 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75ad23f7-f94e-3045-abff-2bf748d73235 | -10.92112 | -50.25765 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9bb0940-168e-3569-8150-7da61ca337fa | -9.84842 | -49.17309 | 2025-10-28 04:44:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5a05970-ed98-3d7a-9b37-ef909a6ccfd7 | -13.62872 | -46.79528 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d903a2d-f2d5-3b60-8dfe-487c4ec401d6 | -13.42356 | -47.38219 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a91d0c64-cfaf-32de-a6d4-1d419500273d | -12.07927 | -46.39899 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8273d8dc-f10c-353b-98ec-ad60dd0307ca | -8.64523 | -45.28065 | 2025-10-28 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 7d866fc9-27c7-348d-8fc6-bccf958a3a0a | -10.29724 | -47.17911 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f67b998-ee2c-38bb-b338-561bc921c729 | -10.95219 | -50.24783 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 930a8446-ae36-3278-b696-57300bf82195 | -8.62915 | -44.79642 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b86b3e3-5796-38c2-896b-afa04503a198 | -10.63209 | -47.89972 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 302749e0-9c00-38c0-9958-6c545a37e1fc | -9.89252 | -50.04593 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acf28898-bf5a-3219-bbee-aa7bd12465f3 | -8.68296 | -47.12182 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66e6aa56-ae07-30e4-80c7-524321f55a15 | -14.14941 | -44.241 | 2025-10-28 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3e90996-2979-30a8-8aca-c25bbe32c9b2 | -10.35086 | -48.04751 | 2025-10-28 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e9d3c51-6b0e-3644-abb0-d2770bf565a1 | -10.93221 | -50.25222 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6da67125-c73e-32ce-83a9-cdac6ad8879e | -11.35325 | -46.09217 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa2d9002-ec71-3bd8-8b90-4eec4e425127 | -13.66932 | -46.52695 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2c0eb336-44cd-308f-a711-eb14c2069935 | -13.93207 | -47.73643 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d1386a1-56e5-37ae-ae52-2a37e40deeb2 | -10.94663 | -50.26897 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb1ab7a0-23e4-3599-9cd3-a4cbfdeea1e9 | -9.58834 | -47.85178 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24179db2-21d3-30dd-9ca1-92c59e0fefc1 | -10.56401 | -49.77427 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14542682-62a0-3bf4-9c27-8b352433b507 | -10.56466 | -47.89296 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd5caacf-adf9-3337-a17a-e42cc87e981e | -8.48347 | -45.56543 | 2025-10-28 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 040359e9-20a4-3ca9-b47c-70c9e9d9783a | -9.59994 | -46.86374 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f23f8585-75e7-372d-b73e-a45d9b57402c | -12.69621 | -46.31551 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29224e65-264f-3948-8665-292ad8065414 | -9.24776 | -45.60354 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3929c27f-b934-3b70-b30f-909943480419 | -10.76465 | -47.90246 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f482d4b-3bb5-3848-a5f0-11a7718b38b2 | -14.31093 | -46.51719 | 2025-10-28 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f2cedd4-ce78-3ca7-b1ce-7c4ce3073e65 | -8.34259 | -48.16843 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33ecc19f-dc8b-385c-95b5-2bcab6cd6e22 | -8.9609 | -50.33099 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45f61b81-c53f-3780-9fc6-6ff71fa92be8 | -9.88067 | -44.88944 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ca71825-7849-3527-b9bf-d2c623e1f6d3 | -11.77317 | -44.63772 | 2025-10-28 04:44:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07437566-d496-3cee-a1f9-504e12d09415 | -10.3628 | -47.16186 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adc2ec64-c335-37ac-beec-e8dee584e0ff | -10.30212 | -47.17125 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a67eed9c-6a20-34b6-9bc2-af98f210ffaa | -10.36582 | -47.16667 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 171c3aad-ece8-3fc7-99c7-34bcb3df9c16 | -8.25195 | -46.89783 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95558861-3660-322e-abc7-706dae3f8680 | -10.29823 | -47.22227 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 265f1462-6753-3d1c-bb8f-a27f63852ef8 | -10.071 | -48.20021 | 2025-10-28 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0841915-2018-3770-8431-a43a2555ca1d | -15.17602 | -47.22843 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3c03e1a-e895-38d5-994f-4674371e3a43 | -13.31767 | -48.34288 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cb0daff-b70a-3215-a9f0-f2bd8bfd42e7 | -12.16397 | -46.5607 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e9cd193-9e75-3c55-9e10-bb27bbe47917 | -9.46132 | -46.87086 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81934471-4b53-3e39-8c53-5d8e6d3ec6a9 | -10.22493 | -49.84336 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ee065d9-542c-34c2-8e38-1f59c0c5eb90 | -9.04103 | -46.94464 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fc1b7c0-e837-3076-bd91-afea1183894e | -9.21869 | -46.34651 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85133b29-cb39-3279-b419-b6ba5d55d008 | -10.9372 | -50.26384 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README61.md)
