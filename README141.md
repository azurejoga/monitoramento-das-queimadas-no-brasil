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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3cabfe3-bef4-3fb5-92d3-dd0f65ca0f8f | -14.98566 | -49.9791 | 2025-10-04 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5cd791be-8085-364e-9df7-c0ab990d1873 | -16.33979 | -47.11387 | 2025-10-04 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5108a35e-e92f-3096-af62-16dd0531f95f | -8.7108 | -47.9822 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a0984390-61e3-36c9-8bd0-2f016f179e6f | -16.30203 | -47.79904 | 2025-10-04 12:19:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 76da33ba-4138-3862-adff-5b042a5a0d46 | -8.75734 | -49.9165 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2e6c2195-a5d4-3b6f-8e50-1015060649f4 | -8.89473 | -47.59742 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 64ffa9a3-140f-307c-aee2-f0ec73e069cf | -15.32509 | -46.37739 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bea015f5-af78-3333-98cd-261a802c1ec9 | -11.66299 | -46.99092 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c362f08a-d9f8-30d6-af72-b9a2277ab964 | -13.55247 | -47.24427 | 2025-10-04 12:19:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ec78112f-9205-337e-ae8a-c0ef22c2c4c1 | -13.31742 | -48.13491 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fc182ab0-1256-34b7-b938-36b0372271c1 | -14.88735 | -48.30247 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 660a29a0-c09d-3ba8-a66e-3c14a92d89fd | -8.97344 | -50.25654 | 2025-10-04 12:19:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0b449369-0c2f-3190-841f-e702033a855a | -13.12014 | -47.95883 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7deb1357-c021-3895-a696-1a3ffb7b599a | -11.70054 | -47.5077 | 2025-10-04 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 581c46e9-aa47-3967-b698-aca9a1a13c74 | -13.02579 | -44.91801 | 2025-10-04 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 61ea2537-2be2-3127-9222-8e203824e434 | -14.00633 | -53.33792 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| fd78750c-2007-313a-a753-d9776c99e323 | -11.00657 | -46.67861 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| ec1afe47-b5bf-35a9-b042-c1c8f137a414 | -14.59323 | -52.50301 | 2025-10-04 12:19:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| afa06dbf-884c-3fa8-9c18-f076beef8f58 | -16.08586 | -47.56261 | 2025-10-04 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ba5158ef-a5ea-338f-8d86-bd106ec916f3 | -11.79395 | -46.84431 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 30443fa1-5895-3832-82a0-36daf5a61f59 | -11.80302 | -48.91668 | 2025-10-04 12:19:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 09b86f86-c16f-35f0-81a0-5196653b5724 | -14.23251 | -46.07892 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 13ab9af6-3e60-3801-be68-f59306f06e05 | -16.0517 | -50.9276 | 2025-10-04 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4d1c3550-1075-3e31-b422-982d6e73d7a7 | -9.3335 | -45.79379 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.8 |
| cd798dc0-5391-30de-8623-067caedee46c | -9.92496 | -50.19377 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8493c2bc-e8e5-36c8-be1c-6b0d01d809a8 | -17.9428 | -47.02591 | 2025-10-04 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 91ce39f1-b4fd-399b-8007-88cbf376ea11 | -15.24051 | -49.30637 | 2025-10-04 12:19:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1d6a3262-42ff-3b41-b44d-f842f2ce6292 | -11.14095 | -47.16858 | 2025-10-04 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9f9c399e-2847-3c92-a500-4b2143f22ace | -11.51224 | -45.01871 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 57443ad8-9aa6-306c-9428-9afc775ecb6a | -12.6488 | -46.98732 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| e2e26803-bf62-3e32-a80b-9531ceeb93c9 | -14.22433 | -46.06669 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 6b797a59-6900-3c48-b40d-13c375863aec | -10.29955 | -50.28617 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5347a965-9bd4-3d12-a894-c37d6cf4c903 | -12.72986 | -48.56427 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a1c2699f-025a-358f-83fe-06d766462a82 | -17.99601 | -44.9967 | 2025-10-04 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a5e7808c-ad1d-37ea-a174-9e7490f42c27 | -13.26208 | -47.21387 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5e9b13cb-2b56-380f-89dc-bed3fd93ecf2 | -11.4532 | -43.4968 | 2025-10-04 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b4e95bb4-388f-3499-a57d-a61e5db85ee1 | -9.98604 | -48.28019 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ec1d1bac-90c4-33d2-b74e-b5261f011a18 | -14.67802 | -48.28746 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 106b3de7-8699-3132-ae76-f167911949f6 | -11.7979 | -46.81608 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dfb0508e-fa11-3c56-ab3c-2e1026e7a39f | -14.20078 | -46.06787 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b0210852-3499-31dc-9750-a52692507b4a | -13.98361 | -45.07479 | 2025-10-04 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| ef3d3c01-4cf3-3aad-be41-632da2e65483 | -14.58496 | -52.4891 | 2025-10-04 12:19:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 921ca5ba-a6bb-3c29-9c85-c496153fabe3 | -13.18911 | -50.99268 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 05fcaf46-f797-376e-a1ae-40d7b5233a89 | -13.65987 | -47.85988 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| cf9d2ce5-f2fb-3849-a705-a0e937d4828a | -11.43322 | -50.72401 | 2025-10-04 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b80ae49d-6aeb-3e96-aa1f-4b7fab184d95 | -16.43357 | -52.16159 | 2025-10-04 12:19:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| d47ba690-a85c-3360-93ad-29d44ed5742a | -9.82154 | -46.12461 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f58b3b9e-6d00-3f40-8f1b-a76eba8eb8c1 | -11.25592 | -47.78709 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7148d4a3-bfff-378e-979a-33695cb36940 | -14.62677 | -48.25481 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0bbaf4f2-7ddf-32d4-bfbb-f79535fbac47 | -12.58136 | -48.12587 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 8542e886-c480-3599-ba1b-642a62a994c2 | -14.27893 | -45.87364 | 2025-10-04 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 0c4d4943-0c73-3f64-964d-cd80f5c6bb8d | -13.34543 | -48.06501 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| afa0ea39-36f4-3a2a-af80-84b0bb18c047 | -15.54928 | -49.28469 | 2025-10-04 12:19:00 | TERRA_M-T | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 99758dfe-b6b2-3ee1-9488-19a20826c5bd | -13.30856 | -48.13364 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6d72194c-8ca9-3c4f-a2f5-750f649f7c82 | -9.18342 | -49.95864 | 2025-10-04 12:19:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| b2f8e015-ca0e-309d-97b2-9c05e276fc9f | -15.57485 | -52.4654 | 2025-10-04 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f815806d-a922-3386-a65f-717cb7c6a606 | -13.19398 | -50.96105 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a76042ea-516c-3607-9201-f04304736aa0 | -13.33399 | -48.08187 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| aba1a1c3-ca23-36dd-9f23-e97455d3cbbf | -9.437 | -47.54869 | 2025-10-04 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| dfe396ea-eb84-377f-92cc-3fb0a14d8da2 | -8.75887 | -49.90624 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d9f7fc26-169c-35a1-a128-08ae02ce3cec | -17.08665 | -46.24612 | 2025-10-04 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 488746df-64b9-3361-ae13-aac6f1ba6f2b | -10.29707 | -49.17729 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f55ff7e5-7105-37b2-a3c3-115ee9436764 | -13.16873 | -50.93557 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| cdf76f34-ba52-374c-bfa6-c231bce2cde8 | -9.60592 | -45.29088 | 2025-10-04 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 58a29b12-2fc9-38ae-a182-4ee86ebb12cd | -12.58356 | -54.75189 | 2025-10-04 12:19:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 2bea4abd-42b9-35fd-83a7-ec24c51b0d90 | -9.38872 | -45.85704 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7df11178-8001-3507-a4ca-a6cec5c459f7 | -13.33528 | -48.0728 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 903cd847-39a0-3225-91e1-f3d13b938df5 | -14.66401 | -48.32257 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3de06f06-b5ed-35b6-a51a-73dc4ef4e862 | -12.84181 | -50.49516 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d8758164-9ecc-37ba-89ed-db8bc5a9c28a | -15.31553 | -46.37612 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7b02a9e7-05f2-3fc2-8d8b-fe3d009692bc | -11.16908 | -47.74984 | 2025-10-04 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f08bc413-b22a-3f93-832c-54b15a71c956 | -10.56857 | -48.71275 | 2025-10-04 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 33b3c716-cb6a-34be-ba6d-cf44c0ce8b11 | -9.30156 | -45.95708 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f88605a5-8c6b-3b42-93de-d050d0630a7d | -11.51379 | -45.00731 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d79b108d-b5eb-3af7-b122-bb0f26ef7945 | -16.97525 | -48.39149 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 2e5d1445-db28-3348-8e2f-811a9231a504 | -15.379 | -47.95166 | 2025-10-04 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| eb32cd05-d77d-3ef3-bc02-241fbd058406 | -12.42139 | -44.07436 | 2025-10-04 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 74ef48bd-a8b7-322e-98e1-67201a1d362c | -11.51005 | -46.76691 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1b3e05eb-88ea-3654-b7f4-8e2d6069bac7 | -13.46554 | -47.27383 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6aab784c-f0fe-3634-bd19-40098ba593a9 | -13.11385 | -47.9394 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 98a0369f-bd3a-3ce8-a0ea-bf7200beaa56 | -11.43021 | -43.48736 | 2025-10-04 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c01685ad-638f-33b6-9128-2cc10990b7e3 | -10.7708 | -46.58551 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 17e21f23-6784-3402-b308-8da9638ff600 | -14.32518 | -52.91711 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 78dbdf65-ea24-3af4-881e-709da59c06b0 | -12.53576 | -45.99883 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 173a3985-eba8-3f31-abba-02ef8dfc73be | -11.51136 | -46.75748 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ee2d9f96-b673-380e-a988-2fe0bb95828b | -13.1671 | -50.94608 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| bf6b409f-edfe-3b90-adfb-f29a7e29d594 | -10.84149 | -47.19424 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 864d0a1d-4cc7-303e-a3af-3d11dc5dd08d | -10.94374 | -47.58027 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7a043f2b-13fd-3e32-a928-b8311f2f0a1b | -13.11014 | -47.90179 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 56416d55-8225-383b-a207-83d34a178108 | -14.67415 | -48.31488 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| aa5d4d6f-2b3e-373c-8406-cab796164125 | -8.98452 | -47.48933 | 2025-10-04 12:19:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7d074ee0-b3d6-3dcb-9c84-61658bd03d91 | -15.3543 | -46.30396 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 16f4310a-8ab0-3e52-be8a-bd24f9d32524 | -14.24888 | -46.103 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 6b365197-57b1-3596-8cb9-4856c62845c4 | -13.2909 | -47.60398 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d1544227-145c-3cee-890f-af560bb9a0f2 | -15.30481 | -46.30868 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5f80719a-dea0-3d1f-8362-fe9782013b92 | -17.99481 | -49.83716 | 2025-10-04 12:19:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 238.7 |
| add50df9-751e-3723-8cc5-c65c0972ecef | -13.21517 | -47.81118 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1f4033a5-7123-3a0b-a561-1daf165e422f | -12.53295 | -46.01958 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 5726a2bd-c4e8-34c9-a7a1-85cc85e5113a | -13.32532 | -47.6184 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 9f1705e9-18bd-39be-b8db-3ee83f88f7e1 | -15.97755 | -50.86988 | 2025-10-04 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README142.md)
