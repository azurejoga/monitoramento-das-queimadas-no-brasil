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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c405ad38-25e2-3e4d-bffb-4d5bd10e78fe | -13.2037 | -51.698 | 2025-10-08 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 756efe10-ca1c-37e5-9a74-33d0d3b36474 | -14.8824 | -51.4992 | 2025-10-08 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 9b1a2b58-0e0f-37bd-8bc7-e6cf8346fbe2 | -7.7935 | -42.5845 | 2025-10-08 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| a36a7268-772f-3f79-9c37-06d72ae44a8c | -14.7184 | -46.0636 | 2025-10-08 14:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| db0fcc1b-70eb-320b-ae09-c9f4aa52d566 | -11.1557 | -51.1263 | 2025-10-08 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 14a1bf95-0502-310d-bb79-b089dac5ddb3 | -13.0009 | -46.7795 | 2025-10-08 14:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 115.2 |
| ef5d2c70-5c8c-3494-8794-77b7b0cf5d27 | -13.204 | -51.6768 | 2025-10-08 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2ed6153b-e56c-38f8-abc3-d37428d41cfe | -13.3513 | -47.6042 | 2025-10-08 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 41f5fa44-63ca-3c46-8325-0a4bed883054 | -14.9022 | -51.4749 | 2025-10-08 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f413b5b3-5d95-3134-8355-a1825531171f | -7.7927 | -44.1767 | 2025-10-08 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e1689046-1862-3387-9dae-65864246a2b0 | -14.4079 | -46.026 | 2025-10-08 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 049f9066-a55b-345a-b793-e4b68f1d37e3 | -12.7157 | -47.6748 | 2025-10-08 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| dc62abcc-6240-3762-b5c5-31298900635d | -14.903 | -51.4319 | 2025-10-08 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4b92652b-49ff-3861-9a8b-5ca69678d913 | -11.4682 | -43.4774 | 2025-10-08 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d354ccf6-2819-3439-a753-d6ed21edc2cb | -7.7935 | -42.5845 | 2025-10-08 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 47.1 |
| 1569f3b4-08d9-32e6-89e8-322fd62d8478 | -9.4367 | -46.8616 | 2025-10-08 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1399e7e0-c3de-3f0c-adb9-e0cdbc788db9 | -8.199 | -43.3659 | 2025-10-08 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 20085786-7a46-3b0c-9f8c-188ea6404c56 | -7.9085 | -45.5145 | 2025-10-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 465bf1c6-7a46-3961-8317-03e6b2aa5c26 | -12.6481 | -50.5495 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 93e6cc3a-ce14-31f0-bac7-5165db18d32b | -18.0394 | -44.9438 | 2025-10-08 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| af3c2723-9121-31f2-a335-df853bcc9388 | -17.2837 | -58.0997 | 2025-10-08 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 7228e316-d341-3bf6-a75c-e69d71b28929 | -8.9309 | -46.5809 | 2025-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 3fd179c6-3c72-3db1-8e6f-a39d76d80048 | -12.4916 | -54.7364 | 2025-10-08 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 4b227453-7bae-3384-a740-ee599cd32358 | -15.3984 | -47.9938 | 2025-10-08 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| ea9c4ecc-c4f4-3707-9189-69be95d3cd64 | -13.2855 | -48.0381 | 2025-10-08 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 87093987-3fbd-33c9-a48a-f8c546eb8e3f | -10.7472 | -46.6409 | 2025-10-08 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| d244fad3-4dd5-3b2c-8f78-304651152ab0 | -12.5107 | -54.7345 | 2025-10-08 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| a42a3b26-104b-3c55-8410-8b446555bc20 | -9.6793 | -49.9569 | 2025-10-08 14:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 60dfb792-9388-3c1d-91d7-12d42c5626c6 | -8.9121 | -46.5829 | 2025-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 29d4456d-3823-30dc-81a6-895a0ae1ecbe | -12.385 | -50.281 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ae509951-99da-3bca-8d12-7c9917faf8b6 | -14.7184 | -46.0636 | 2025-10-08 14:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| fa338acb-7afd-34ed-b524-1d8ffac53e9d | -17.9224 | -57.5128 | 2025-10-08 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 878e661a-acda-3d73-8e98-cfd0b9c370ce | -17.3037 | -58.077 | 2025-10-08 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 0778b3b1-3091-351d-8364-3c68c1d83e6c | -13.3706 | -47.6013 | 2025-10-08 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 88914c01-1b67-3030-b0be-7a1683d51e9e | -11.3287 | -44.8773 | 2025-10-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3e047ce6-8d5f-3a07-9505-13389a36f314 | -12.6964 | -47.6776 | 2025-10-08 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0c1ac8f7-9d5d-3c8e-921c-9b6b041cab58 | -11.6701 | -50.9641 | 2025-10-08 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2f66f71a-dc6a-3a74-8cd3-9221fb3c6c52 | -10.4245 | -45.3907 | 2025-10-08 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 797e7462-f432-3ea2-be72-c728acd0ff15 | -3.8573 | -41.5479 | 2025-10-08 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 93e58465-ec05-3606-83f7-838a9775328b | -13.3517 | -47.5818 | 2025-10-08 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6ac95c54-d471-3a67-ad80-9cd97095b6ee | -7.777 | -42.3961 | 2025-10-08 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 54e8a651-08f3-3a4a-b734-903832e7eabb | -7.8307 | -44.1497 | 2025-10-08 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 687f3aa3-537d-3992-981d-323f4d7329a2 | -7.2966 | -44.7761 | 2025-10-08 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c1b6c599-7c99-33ff-af26-c70417657e96 | -12.6478 | -50.571 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 81628db0-89e6-3a87-940f-7ee34fa519f0 | -6.9984 | -42.8544 | 2025-10-08 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 578f3fee-b3b0-39a9-8c27-c01457c4c5b5 | -7.6825 | -42.4063 | 2025-10-08 14:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| b62f2baa-c32e-38e7-a5bd-61e2d6a194f8 | -12.2525 | -47.8728 | 2025-10-08 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 96ce162d-8381-3e02-ac7d-a269ac550e93 | -12.5297 | -54.7326 | 2025-10-08 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 972971f9-fb18-3cb9-8232-70cd4d5ad5a9 | -7.8119 | -44.1516 | 2025-10-08 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 23ee49fc-5f7d-33a7-ad25-ad4a3a10578d | -7.4857 | -43.0655 | 2025-10-08 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 120.6 |
| 1c204a1e-9e10-3137-b648-e28eabe3e866 | -11.9519 | -46.4352 | 2025-10-08 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 79da27b6-9e3a-36f4-a3b2-b8b574e85c8c | -12.6666 | -50.5901 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 388680e1-c544-3d5d-bffa-35dfc512d355 | -13.2847 | -48.0827 | 2025-10-08 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a1284b2d-fb0f-32f7-9b55-6671bdafd3af | -14.7179 | -46.0867 | 2025-10-08 14:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 34410216-10d6-365c-a3f6-9a3be20149e7 | -7.7182 | -42.5688 | 2025-10-08 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 03c6815e-13c3-3611-8de0-aa7c099c22d0 | -3.8759 | -41.5708 | 2025-10-08 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 0c9fca00-34a8-37d4-a8ee-e28cb89695c6 | -11.7846 | -45.0652 | 2025-10-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 7538f284-eb1e-3fc2-8872-29b06157e13d | -12.3846 | -50.3026 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5e859895-506e-37b7-a957-eb4e1b5a5daa | -7.7927 | -44.1767 | 2025-10-08 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 88e2504f-85c9-3390-971f-724128453eb9 | -15.321 | -46.1622 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e3cded72-9d82-3750-afde-2dae8d59de16 | -13.3513 | -47.6042 | 2025-10-08 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| be9f5e39-cf26-3bf2-92e2-7865fde4b3ea | -12.4441 | -50.166 | 2025-10-08 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 0eb339a1-1399-361b-a8d7-4e1dfe146030 | -3.2901 | -42.6213 | 2025-10-08 14:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 326326b0-ee26-3148-9534-681601963d0a | -12.3911 | -51.1153 | 2025-10-08 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6c502641-174a-32c0-a026-280db6d98cf1 | -6.9704 | -42.0023 | 2025-10-08 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 745c0f26-eceb-3d88-b711-3bb97ebef53c | -13.3967 | -47.2382 | 2025-10-08 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a4541ab2-d05f-3b3b-9a98-4efe4b1cfb6c | -13.3774 | -47.2411 | 2025-10-08 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e4c2e221-1e1a-3493-b268-1591173b4339 | -7.7932 | -42.6082 | 2025-10-08 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 10429f57-0b5d-3d89-ab75-2d77cd841a65 | -8.1804 | -43.3445 | 2025-10-08 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 197.4 |
| b45f4c03-266e-30b7-9e1b-d47e1674934b | -10.8918 | -51.0481 | 2025-10-08 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b0c1dc0a-dbff-3fa9-840e-2223204dc939 | -3.4366 | -43.1532 | 2025-10-08 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| a8593ffc-456e-3936-a2c8-5debdefc5f92 | -13.3245 | -48.0101 | 2025-10-08 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| fd9d5be2-ff32-3613-830e-2a736ccd4ead | -12.1576 | -51.4399 | 2025-10-08 14:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 38563c2e-0c02-3409-b507-07b2a9c54e97 | -9.6795 | -49.9355 | 2025-10-08 14:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9373c997-2143-3d17-ba11-0fe2b99d355e | -14.3889 | -46.0063 | 2025-10-08 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 455dbeaa-2a48-3726-a343-270cdccfa902 | -12.3908 | -51.1366 | 2025-10-08 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b4e93035-628c-3571-95a0-cf0629bf9e93 | -7.7743 | -42.6103 | 2025-10-08 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 80975b5a-92df-339e-bbee-91d9591f8091 | -3.8761 | -41.5468 | 2025-10-08 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 122155fc-33dc-30bc-a069-fcf62234db4a | -7.8116 | -44.1748 | 2025-10-08 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8a280cf0-7bb4-329c-a532-e93296e4295c | 0.9293 | -51.1248 | 2025-10-08 14:10:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 338ad492-2a24-32ff-baae-90e36a703a3b | -8.9573 | -44.6052 | 2025-10-08 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 36526b26-63af-32b4-aa4d-4f850d955d5c | -10.7468 | -46.6634 | 2025-10-08 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c74a7d12-51a9-3c2f-bc20-529176e76d4d | -12.6669 | -50.5686 | 2025-10-08 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 009f661e-7295-3177-b9bd-fab907d66236 | -8.6106 | -45.102 | 2025-10-08 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ebe2b070-2147-3adb-9a51-cfe947e01178 | 0.9292 | -51.1455 | 2025-10-08 14:10:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 172.8 |
| adfce3f2-f97d-3919-af48-c999807c3a10 | -7.793 | -44.1535 | 2025-10-08 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c88d97f1-1f65-3187-aedf-4bb905158aef | -13.3778 | -47.2185 | 2025-10-08 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0a02e9be-48e0-35e7-8097-8039175c1d13 | -7.7203 | -42.4023 | 2025-10-08 14:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 70089f34-1b92-343c-b9be-dfd585f22f32 | -8.9383 | -44.6074 | 2025-10-08 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 707b5275-c4bb-3d51-90ce-86887d68f9b5 | -10.5429 | -54.8723 | 2025-10-08 14:10:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a48a1a5c-1bc3-39d6-9d55-117d5018e3f7 | -14.9224 | -51.4292 | 2025-10-08 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9dbae371-7499-34d2-8fab-7d3e482d4374 | -3.8948 | -41.5458 | 2025-10-08 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 0a5fc976-d000-34ea-8eda-1ec03c943672 | -7.7924 | -44.1998 | 2025-10-08 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| a30e04d6-27d9-3fbc-8dd6-ee7e798e501a | -11.785 | -45.0421 | 2025-10-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ebe1342b-6cb7-3597-9ce3-a02d0ca2d6a2 | -8.9495 | -46.6013 | 2025-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 72a6bbaa-7030-324b-a540-96911e420261 | -8.4824 | -46.2912 | 2025-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 98c385d9-58c4-3e3f-97da-8d28ff04aecb | -12.4919 | -54.7158 | 2025-10-08 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 145.0 |
| d7f03134-5acf-32ea-a307-9030af2b12d3 | -13.3018 | -47.1626 | 2025-10-08 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 250.2 |
| 4cc5179b-cb87-3cab-a529-9bddb5398740 | -13.2662 | -48.0409 | 2025-10-08 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 519fa177-099a-3bef-8f52-dc1604d52a6d | -7.4669 | -43.0674 | 2025-10-08 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |


[Clique aqui para ver as próximas entradas](README109.md)
