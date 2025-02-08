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
| 151d006c-c115-39b9-9312-51e7a386730f | -21.89062 | -53.72071 | 2025-02-08 05:20:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ecaabfe-913b-379b-a97a-0db9fa1c6ce5 | -21.8903 | -53.72384 | 2025-02-08 05:20:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8a5777b-9033-37dc-a5e8-48ab9bc90858 | -12.05 | -45.07 | 2025-02-08 12:00:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8801b30d-ef48-3f71-ae5d-186b9e91ac58 | -6.14211 | -44.75491 | 2025-02-08 12:50:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3e08e748-ef15-382f-b630-ceb23d46e215 | -6.14771 | -44.74302 | 2025-02-08 12:50:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 610a7edc-96b9-3a0d-9fa7-ece0b7a9a09d | -6.34963 | -43.37644 | 2025-02-08 12:50:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 0bdbf7c6-74f9-3c10-b68d-dc31c1f57643 | -12.96058 | -55.04673 | 2025-02-08 12:53:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ece9342b-8889-3f3b-82cf-6ba3e690fbab | -11.13496 | -52.39045 | 2025-02-08 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a121859-9e08-3d49-9a0d-5b1f7bc4e18f | -13.2515 | -53.23878 | 2025-02-08 12:53:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65b23ff5-f85c-34cc-a06f-f0e73900ca64 | -12.34915 | -52.4809 | 2025-02-08 12:53:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b8688fd1-3248-36d0-868e-ae8a6450d250 | -10.60249 | -48.32524 | 2025-02-08 12:53:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c32391b1-1f8c-32a7-bd18-38cf21c8531a | -10.73713 | -53.76569 | 2025-02-08 12:53:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d6021365-bea1-3cb2-8243-1665030043d3 | -11.85349 | -46.64586 | 2025-02-08 12:53:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b76876cf-c79e-3c1a-a248-af228bcfa54f | -13.62628 | -55.44928 | 2025-02-08 12:53:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 56c18d02-d4eb-387a-8f07-49ad39c00b22 | -12.51184 | -51.85954 | 2025-02-08 12:53:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 175275e0-502e-3bde-88a1-f2d546d018ce | -15.21508 | -50.23806 | 2025-02-08 12:53:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e92aa286-5fde-31a9-8c97-abd392dc9c8b | -13.1857 | -53.06133 | 2025-02-08 12:53:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6cf19881-28d2-36ac-b196-d2891aa0b321 | -10.46559 | -53.54167 | 2025-02-08 12:53:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ce2c0947-ab90-314f-b57b-6537116f1aa7 | -12.84165 | -50.29914 | 2025-02-08 12:53:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7a6076e7-c0cf-3266-8c7a-0bdf2328aee2 | -11.74195 | -48.73256 | 2025-02-08 12:53:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 91fdbdbf-bef4-3f07-8d6b-e94b2443e485 | -12.05161 | -55.02543 | 2025-02-08 12:53:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f71e0bac-2f26-3ae8-afca-e872db2f8e30 | -13.02755 | -51.54012 | 2025-02-08 12:53:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9cddd7d3-1a82-3d7b-b395-78d8aa9a6382 | -12.31888 | -51.27681 | 2025-02-08 12:53:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3247fd77-7154-34fe-ad50-a197168dcf7c | -9.53043 | -49.6208 | 2025-02-08 12:53:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c11df24e-062c-35c5-850e-41ccb35c13ec | -15.03526 | -51.93811 | 2025-02-08 12:53:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4a21b237-8721-370a-8f36-8cf46fcf1030 | -10.35901 | -50.94096 | 2025-02-08 12:53:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a7336071-dc70-3866-83c0-52cf740d4042 | -13.04603 | -54.10821 | 2025-02-08 12:53:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9c01d03a-2804-30a1-863b-8a869868d6fa | -10.35834 | -52.78028 | 2025-02-08 12:53:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9226c567-be8f-3e74-a14a-571c6c9273eb | -11.44423 | -52.92147 | 2025-02-08 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f3f31889-27b4-37d3-a907-f53a7e0f7c34 | -14.02042 | -49.17585 | 2025-02-08 12:53:00 | TERRA_M-T | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d0c82fc4-04dd-3a1c-98e7-b8eec3acfbed | -15.46717 | -51.94753 | 2025-02-08 12:53:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d29fe67c-2f07-346e-a554-d4d75191ec56 | -15.03396 | -51.94732 | 2025-02-08 12:53:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1f73627f-faec-3bd8-b2d5-b53ceab3dcfc | -13.5264 | -55.3676 | 2025-02-08 12:53:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e7323ffc-f8cc-3691-b303-440030da3c2a | -13.18707 | -53.05211 | 2025-02-08 12:53:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ecb5c41c-ecfe-3d6a-9c9a-05cc1beb45a9 | -10.41298 | -53.46678 | 2025-02-08 12:53:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 09037e30-f4a5-31e6-8817-c4ea4f8be0ec | -16.88465 | -49.24892 | 2025-02-08 12:55:00 | TERRA_M-T | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 67234b91-325a-3346-8048-2561c7d72aec | -19.30527 | -48.91663 | 2025-02-08 12:55:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7810c447-126c-313e-80c1-4b767e3dad14 | -18.73938 | -47.49727 | 2025-02-08 12:55:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 063c82ff-0a14-3de6-9917-3f54df20d402 | -21.35598 | -48.22626 | 2025-02-08 12:55:00 | TERRA_M-T | GUARIBA | SÃO PAULO | Brasil | 3518602 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bd026080-dfd3-3abe-89c2-00eeb25f6033 | -21.34972 | -48.21908 | 2025-02-08 12:55:00 | TERRA_M-T | GUARIBA | SÃO PAULO | Brasil | 3518602 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 557d7304-dafb-339d-851e-6fa751c4ae6d | -23.0637 | -47.0032 | 2025-02-08 12:55:00 | TERRA_M-T | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 7a7bf78e-c5da-3e79-ac3c-a8d6ed3b15b3 | -22.63643 | -46.97798 | 2025-02-08 12:55:00 | TERRA_M-T | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| e8bb5620-d265-31b1-bf2b-23c1ac91c176 | -18.87513 | -48.87498 | 2025-02-08 12:55:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3f6d6dc8-425b-3049-9a9a-84720390e495 | -16.80011 | -49.19251 | 2025-02-08 12:55:00 | TERRA_M-T | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1ed0d473-ad06-3a8b-91fb-186018f6cf7c | -20.58775 | -47.8622 | 2025-02-08 12:55:00 | TERRA_M-T | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| badc928f-8d0f-3b0e-91a7-45c2edfa8ae7 | -30.80902 | -54.69221 | 2025-02-08 12:57:00 | TERRA_M-T | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 7.2 |
| 5ac4e0c8-45fb-3f0e-a5f4-27dfc31c6890 | -28.93711 | -51.54604 | 2025-02-08 12:57:00 | TERRA_M-T | VERANÓPOLIS | RIO GRANDE DO SUL | Brasil | 4322806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| b4b93932-7b11-3bac-963d-769a493c90f9 | -29.14462 | -56.13635 | 2025-02-08 12:57:00 | TERRA_M-T | MAÇAMBARÁ | RIO GRANDE DO SUL | Brasil | 4311718 | 43 | 33 | nan | nan | nan | Pampa | 30.5 |
| da436a3e-4dbf-34ff-b5b5-2ebeee60a9ab | -29.89605 | -52.39909 | 2025-02-08 12:57:00 | TERRA_M-T | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 10.6 |
| 9f657ad2-f76b-310d-ab89-30cc1d2a3177 | -29.58763 | -51.09866 | 2025-02-08 12:57:00 | TERRA_M-T | DOIS IRMÃOS | RIO GRANDE DO SUL | Brasil | 4306403 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 2238791e-3ed7-33b3-aa6f-17c95d88c048 | -30.04852 | -55.08138 | 2025-02-08 12:57:00 | TERRA_M-T | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 7.6 |
| 6fcb6f1a-472d-3ac0-8b00-8977c53daa5d | -29.14611 | -56.12622 | 2025-02-08 12:57:00 | TERRA_M-T | MAÇAMBARÁ | RIO GRANDE DO SUL | Brasil | 4311718 | 43 | 33 | nan | nan | nan | Pampa | 8.4 |
| 3b08d9c4-2341-309d-9522-719f29645cc6 | -26.74585 | -53.67184 | 2025-02-08 12:57:00 | TERRA_M-T | BANDEIRANTE | SANTA CATARINA | Brasil | 4202081 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| eab89a79-addd-3a32-a811-80865728005b | -28.8484 | -51.89067 | 2025-02-08 12:57:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| eccd957d-b260-3196-888c-d98f65716e3b | -29.22239 | -51.34136 | 2025-02-08 12:57:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |


