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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d41ab38-0218-3b01-ac17-ec34e6e8f653 | -11.9717 | -51.1427 | 2025-09-12 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5a4732b3-f685-365d-81ed-9b2c02ea9acf | -11.6821 | -46.5632 | 2025-09-12 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 669136ae-10cf-313f-95e5-0dd9849c9462 | -23.1146 | -47.4915 | 2025-09-12 01:10:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.5 |
| c92c7169-2cd5-3b65-ab4c-c479e9503292 | -13.3238 | -44.0945 | 2025-09-12 01:10:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 12acc02e-7bd1-39aa-9a8f-dc27d99e9037 | -12.8651 | -62.1074 | 2025-09-12 01:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 64bbd5de-a10d-3825-94f6-157fe06a08c7 | -11.7016 | -46.5379 | 2025-09-12 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 0e3097e5-302d-3f24-a3b3-fd009e70dda2 | -12.8649 | -62.1268 | 2025-09-12 01:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 2e308d0f-1a5f-3e69-bac8-202a35209a25 | -11.7012 | -46.5605 | 2025-09-12 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 63756fe0-8cb8-3ed3-820e-627a362c1086 | -12.9289 | -54.7744 | 2025-09-12 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7f792764-6724-3b68-afcf-0fec4fafe82a | -21.9478 | -47.534 | 2025-09-12 01:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 179.7 |
| a4ff8f8f-fc97-3fed-a696-c4ebef77b1e5 | -12.8649 | -62.1268 | 2025-09-12 01:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d720a64b-38ac-3d95-b30b-1ee2ec7d462e | 2.5064 | -61.0201 | 2025-09-12 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3e6b5b47-cefc-3b83-a584-0e300d98192f | -6.2902 | -42.2327 | 2025-09-12 01:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| ab93c032-9adf-3905-ade3-eef8cf50bad1 | -11.0198 | -51.3733 | 2025-09-12 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d70a906c-0514-3baa-936d-a0dce4a21c38 | 2.5064 | -61.039 | 2025-09-12 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 7c50177b-253e-3b1b-b2ea-99fcf801cafd | -12.8286 | -61.9551 | 2025-09-12 01:20:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 04d8546c-6fa8-3838-a314-7cb7e6888dd6 | -12.846 | -62.128 | 2025-09-12 01:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 90a2d7e7-b0c2-3fc0-ba67-2ba4c354e465 | -16.4123 | -45.6728 | 2025-09-12 01:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| bdba4d49-944a-37fb-bcaf-2ad593684177 | -11.8757 | -58.8221 | 2025-09-12 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 34a8ef26-4a8c-3fbc-a876-6f6c01ae43c9 | -12.9101 | -54.7558 | 2025-09-12 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 8dd87632-1f20-342f-b0d8-90967e0ae4b2 | -16.4118 | -45.6963 | 2025-09-12 01:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ee929e0e-593f-3c7d-9c8e-3f6166a3a6fa | -21.947 | -47.5578 | 2025-09-12 01:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 334.2 |
| ac841c02-5c91-3bdf-952d-61f3aaac6240 | -21.9679 | -47.5525 | 2025-09-12 01:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 439.2 |
| e237748d-0d42-3f6c-92ea-93e45ad6f2d2 | -23.1146 | -47.4915 | 2025-09-12 01:20:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| f2c97902-5b3c-3e9c-91e1-84c0994d9a66 | -12.8651 | -62.1074 | 2025-09-12 01:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a6996ac1-e5a3-3614-a31d-d5dfd1b87fda | -9.0124 | -46.1239 | 2025-09-12 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 3f1036aa-544c-3850-a1db-cbb49d3ebf85 | -11.9907 | -51.1405 | 2025-09-12 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| cfbb2ffe-738f-353c-b8f9-3fada8f80851 | -15.5822 | -54.7429 | 2025-09-12 01:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 189806a5-cb13-395c-86cc-cd6214a2e6eb | -21.9672 | -47.5763 | 2025-09-12 01:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 70.2 |
| cd93b6f3-3bbe-35c4-93e2-f635d1d923d0 | -6.3092 | -42.2072 | 2025-09-12 01:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 372c2639-92da-37c0-92d5-f8bc478ac644 | -11.6821 | -46.5632 | 2025-09-12 01:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 74b12449-a541-318f-a174-0628c55abbf5 | -8.8899 | -49.945 | 2025-09-12 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f81b778b-d06c-312b-92d3-2b6114bd6c1e | -21.9686 | -47.5287 | 2025-09-12 01:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 6fea5fd3-bb68-3fe8-92d2-92fecacd0972 | -12.9098 | -54.7763 | 2025-09-12 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3f51bd67-1ad5-36d2-a81e-ae1b213c0a89 | -20.0192 | -47.6459 | 2025-09-12 01:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 2671d922-a9a7-37ea-9087-3c0430014493 | -12.9294 | -54.7333 | 2025-09-12 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 220553f7-404c-36a5-92dd-e4511bb2b7d7 | -11.5263 | -50.404 | 2025-09-12 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ec5811ac-a7b7-3537-8e5e-0039cc046b0c | -12.9292 | -54.7538 | 2025-09-12 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 171.4 |
| b0531498-1e14-314d-b22c-2846bec3fb85 | -11.0201 | -51.3521 | 2025-09-12 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| afe5c23c-6f91-3e4d-994b-b0b61f2e68ec | -6.309 | -42.2311 | 2025-09-12 01:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 192.1 |
| cf383cd5-2140-35ae-bb38-12ce01a2fe4a | -9.2101 | -59.3833 | 2025-09-12 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| d961a9ef-1e4c-398f-b22a-ae75682656ae | -11.5073 | -50.4062 | 2025-09-12 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a51ce610-6ffd-358d-968b-f626d80729bc | -15.5819 | -54.7637 | 2025-09-12 01:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| bf23a48c-dbf7-3c97-bb4a-0cf292e0ff81 | -12.8647 | -62.1461 | 2025-09-12 01:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 69b1062a-f588-35b2-9636-0afec9c2e5cc | -11.9717 | -51.1427 | 2025-09-12 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 824d4db7-988f-3f75-8869-139849891a54 | -12.846 | -62.128 | 2025-09-12 01:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a2f0f797-ee9b-35d9-8154-72784a65332c | -20.0192 | -47.6459 | 2025-09-12 01:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ede649c8-56f9-35af-8aa2-a018de40db2b | -6.309 | -42.2311 | 2025-09-12 01:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 213.8 |
| 0d03e719-311f-3638-89da-7666a8c8cdc0 | -12.9101 | -54.7558 | 2025-09-12 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| d3108943-52af-356e-b1c2-877e271ab744 | -6.3092 | -42.2072 | 2025-09-12 01:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 5cd1b26e-5dfa-3513-bd73-92b90608aa7f | -11.0201 | -51.3521 | 2025-09-12 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 181d4ad1-cb27-38f4-b078-a4fc0d2eb462 | 2.5064 | -61.039 | 2025-09-12 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 0f7c59cb-72bb-3e8a-b5a5-d95f3ef70efe | -13.3238 | -44.0945 | 2025-09-12 01:30:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5a0354ac-5a7d-39c2-bee5-812881b8cb7b | -11.7016 | -46.5379 | 2025-09-12 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9466cd6b-8801-3099-b588-784c1b3c5b98 | -9.2287 | -59.3823 | 2025-09-12 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b6ad5023-fdf4-3f56-9aef-52b0c7d409a7 | 2.5064 | -61.0201 | 2025-09-12 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 073aea28-5e1d-32a1-af14-526670f9480b | -11.6825 | -46.5406 | 2025-09-12 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 57fefc0f-d0b4-39fb-a791-6e3a976ea123 | -21.9672 | -47.5763 | 2025-09-12 01:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a0ba18e0-fb3d-37af-8096-ec1e9d98fb1f | -21.9679 | -47.5525 | 2025-09-12 01:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 378.5 |
| e3ea9085-f996-3dc6-b503-87c5b4eefceb | -9.5137 | -54.6292 | 2025-09-12 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e96ec075-3937-304a-ae29-5638aa27878f | -11.7012 | -46.5605 | 2025-09-12 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 32dd848f-8429-32a7-abf7-225deebef861 | -12.8649 | -62.1268 | 2025-09-12 01:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 5aeaf336-4408-34cb-a495-147742457530 | -8.8901 | -49.9236 | 2025-09-12 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 38802bfe-54be-36e1-9dcd-f7598a75a808 | -21.947 | -47.5578 | 2025-09-12 01:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 452.6 |
| 7f237e78-7baf-301a-9528-10f02ecdfb1e | -8.8899 | -49.945 | 2025-09-12 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 7407eb1e-a5bc-313a-9f42-4928d4ff90b7 | -23.1146 | -47.4915 | 2025-09-12 01:30:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| d016355f-abed-3988-982b-3dc3705451b3 | -20.2689 | -42.1022 | 2025-09-12 01:30:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| d28c4533-d10a-3834-a797-12f14afbc82e | -11.6821 | -46.5632 | 2025-09-12 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 044ef423-0bb6-31fa-be69-1ae2324b94eb | -12.9292 | -54.7538 | 2025-09-12 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 2f286eb9-b3c1-3f83-a57e-64777c526a6d | -22.6404 | -53.0946 | 2025-09-12 01:30:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 118.2 |
| 6e9d0605-49b2-385f-b9fb-4674dee9951d | -20.2681 | -42.1278 | 2025-09-12 01:30:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 828d235c-8e8e-3189-8ba2-78d0d79aab4b | -9.2101 | -59.3833 | 2025-09-12 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| b9230f44-91b7-3691-a505-1e2077713e09 | -23.1139 | -47.5156 | 2025-09-12 01:30:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| e5da4670-de43-3a86-9fdd-3eaf694f7c14 | -12.8651 | -62.1074 | 2025-09-12 01:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1b740a70-0c27-3b1d-a98a-a795b23a6c6e | -21.9478 | -47.534 | 2025-09-12 01:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 5ec4f18c-8220-3f78-8a35-9f2d1f926d6a | -6.2902 | -42.2327 | 2025-09-12 01:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 1528e5d0-b687-36e2-8c58-0801d41f8569 | -21.9686 | -47.5287 | 2025-09-12 01:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b1a2dca7-2aff-3fb8-b330-466948780a84 | 2.5064 | -61.039 | 2025-09-12 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 578ce2b4-d36b-3411-a6fc-e57d6975c24d | 2.5064 | -61.0201 | 2025-09-12 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| eb23c5e5-9f97-3288-8dfc-4f73859397ce | -8.8899 | -49.945 | 2025-09-12 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| f2cf8097-2e44-3929-8985-c117e5e71cf1 | -20.2896 | -42.0962 | 2025-09-12 01:40:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| f73a3bdd-34e2-32a1-9f32-2794f77846d1 | -8.8901 | -49.9236 | 2025-09-12 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4cb35e43-8fc2-392b-bd00-1737f3acf260 | -12.8651 | -62.1074 | 2025-09-12 01:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 027047ef-e725-32a0-adbb-bdee81af0a84 | -6.309 | -42.2311 | 2025-09-12 01:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 153.1 |
| f608f435-908a-30e1-a81c-5e8687a3a97d | -13.3238 | -44.0945 | 2025-09-12 01:40:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ac49c7c8-ec30-32e4-b551-b9becc9ca6a4 | -9.2287 | -59.3823 | 2025-09-12 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f4e9e0cd-9cc7-3f77-ad7f-075a60244c66 | -9.5137 | -54.6292 | 2025-09-12 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2517f759-c8a4-3448-b069-ca85ac8a82e3 | -11.0959 | -51.3443 | 2025-09-12 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9454b73e-7b06-3f45-a572-3c4c713b18c5 | -20.2689 | -42.1022 | 2025-09-12 01:40:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 137.4 |
| 893e965a-234e-3132-ae46-dbca459e085d | -12.9292 | -54.7538 | 2025-09-12 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| d5ff5c3f-ddde-303b-9528-c128208e1dec | -23.1146 | -47.4915 | 2025-09-12 01:40:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.7 |
| c573942c-7771-329c-885d-e089295160c9 | -12.8649 | -62.1268 | 2025-09-12 01:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ae9f2eb4-840b-380d-91fa-cdd9dfe884f7 | -11.9211 | -50.7009 | 2025-09-12 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 24da2eca-5269-358b-97ac-8338723fdb8c | -9.3017 | -65.5959 | 2025-09-12 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ded10831-5c18-3127-9e45-334e45e2686c | -20.2681 | -42.1278 | 2025-09-12 01:40:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 214.2 |
| c87d9c61-c0d6-3ca2-99f5-aae68cbe61f8 | -12.846 | -62.128 | 2025-09-12 01:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bdd83e1c-dc22-3ef5-a62e-89bb4ba54563 | -11.1149 | -51.3423 | 2025-09-12 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 8829a5fe-fea8-3b8a-b92b-9e66f2009a7f | -19.9988 | -47.6505 | 2025-09-12 01:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| a4f3317f-11c3-392d-9b47-2f6f589ea1cb | -12.9101 | -54.7558 | 2025-09-12 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 1442f874-f21b-3e05-babd-9a48ad0e410c | -20.0192 | -47.6459 | 2025-09-12 01:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |


[Clique aqui para ver as próximas entradas](README11.md)
