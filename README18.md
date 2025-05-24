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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52b43907-a88f-3857-813c-13825e1760ad | -11.75356 | -54.22512 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5340f3cf-4eb1-386f-b9a5-40d9fb9d07cc | -13.78199 | -54.30715 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63894cde-3069-34d9-8530-8a6779a0f022 | -13.98948 | -56.01814 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79835571-cbb7-3497-ae54-2243bceb14e0 | -10.05168 | -59.3579 | 2025-05-24 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2db671c5-b9bc-3314-aa74-1c7522d17844 | -13.15224 | -56.81459 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 79887cde-d0c5-3c6b-b451-08462dc03adc | -11.76319 | -54.22625 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3f0f963-0641-3726-bc1b-c89d7b463507 | -11.75292 | -54.22631 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 639cb5d4-2516-3afa-b10e-8a8003308765 | -10.36451 | -57.5078 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41e4408a-4915-3855-a5be-cf4efc1deea4 | -12.35422 | -49.92484 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c77c0819-f615-3917-a31b-5c4cb5882915 | -13.86446 | -59.72989 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e72d2ffd-f380-3c79-8f55-63a363e525fa | -14.01437 | -55.13081 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b08eb203-d7d2-3453-b2f1-61e01277433b | -12.40039 | -49.98183 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1d16cef-592d-3e3a-9525-b1fc07a5e279 | -11.993 | -57.21 | 2025-05-24 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4e8eeb1-19be-302d-9e62-93290d44864c | -13.83631 | -59.65125 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5353ffe6-fea8-3f21-a314-023185ec2608 | -14.06874 | -57.11175 | 2025-05-24 05:25:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98ab9a43-2054-3d02-ba96-309181703ced | -13.15635 | -56.81521 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56142c4b-1bad-3545-824d-180c6926541d | -10.02288 | -65.0036 | 2025-05-24 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 949404b3-fbbc-33f5-afc4-5d37ef8ba570 | -14.0184 | -55.13643 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bec95861-c675-334b-85ac-41c3e0662c4e | -10.02907 | -48.69601 | 2025-05-24 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc1c9b2d-b7d8-3502-ba5b-cfa81ed695ef | -12.66947 | -58.21668 | 2025-05-24 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 460ef611-6b69-3e22-b61c-78d18550961d | -12.39285 | -49.98312 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 41c49d85-605b-357e-b655-ddc31fcf24ea | -10.80146 | -54.04927 | 2025-05-24 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b907e47c-59d6-3704-81a5-8f6d253b00c8 | -9.41424 | -58.3132 | 2025-05-24 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2080d0c-e7d3-32b8-8d95-6e21baa2e588 | -11.57266 | -54.56218 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b07a2977-6b03-35a4-970d-989de82f7dac | -13.15994 | -56.81963 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8dd643a-d0a1-349c-9b54-e2cc56d5cf3c | -13.98563 | -56.01334 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece8435d-8bb4-3432-ac98-dae9df7aca19 | -11.74745 | -54.23092 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41e4fa11-d5df-3d45-b229-3479790ed45a | -9.86178 | -60.32026 | 2025-05-24 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c10d4e8-bf1e-36d8-a4a7-31289cd7b1b2 | -13.14863 | -56.81025 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6b064cf2-3d4c-3ccc-b81f-6f090c55b34f | -9.66044 | -65.73031 | 2025-05-24 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e326eeb-6396-36b4-8509-f9fa8829b30d | -19.87146 | -54.3664 | 2025-05-24 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a87acf9d-bd13-3ba8-8550-6d6f6267254e | -15.63021 | -57.3068 | 2025-05-24 05:27:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ab577f0-a4fa-34c5-8df3-c2330e1decac | -20.94131 | -56.5887 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5e2d27c7-26ec-38cc-a23b-ea85ce370b78 | -18.64022 | -53.31369 | 2025-05-24 05:27:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fb7b1ee-ba48-3b4b-a443-691007da90ae | -21.59952 | -56.04597 | 2025-05-24 05:27:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a606d2-dfda-38e1-b259-cb959c9b8c93 | -20.9454 | -56.59433 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b4e2627c-24e0-32cb-a5ed-f4471aff409e | -20.94337 | -56.59149 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0bf0286a-788d-3862-a3a8-ab02f63b822f | -17.15224 | -54.00509 | 2025-05-24 05:27:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe0ee54a-ace6-3a52-a0a9-c260d07d48e8 | -18.58566 | -55.93644 | 2025-05-24 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 74a4e3a8-8e97-3624-a121-cb8b76d66e8d | -21.60436 | -56.04668 | 2025-05-24 05:27:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41f7e785-5c3c-316c-97e9-c9cec44aea2e | -20.94076 | -56.59368 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 62844c81-6d10-36ff-9868-532a2c111489 | -20.94802 | -56.59205 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4eeece3b-0f10-35d3-8a7d-0658011140d9 | -15.62974 | -57.31041 | 2025-05-24 05:27:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6053ac40-d517-35f0-a8a0-07d46ab78081 | -15.62722 | -57.31093 | 2025-05-24 05:27:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d547d679-b935-31f2-9e78-9e06bb24b43e | -17.15751 | -54.00554 | 2025-05-24 05:27:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5e0bd90-ca19-3024-83b9-00c48151470c | -20.93872 | -56.59088 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b2ec029-dfc6-34c1-8696-b35725e98472 | -21.96145 | -56.07898 | 2025-05-24 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2749081b-821b-311f-9749-f6c8dc918163 | -21.95895 | -56.0766 | 2025-05-24 05:27:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8b327f7-04ec-331e-822e-459a16fafdf9 | -19.79294 | -53.83427 | 2025-05-24 05:27:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8c71177-5a17-3b94-a983-2f1ac348a782 | -18.64581 | -53.31436 | 2025-05-24 05:27:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a906f45b-244c-3282-9d2e-a5ca53ef57b4 | -19.87674 | -54.36725 | 2025-05-24 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 496efa8f-04fc-348a-b493-31c4190cba85 | -18.35803 | -55.17584 | 2025-05-24 05:27:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f636ce27-8b83-3e1c-839d-3c5a8735888c | -20.94278 | -56.59649 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e3168a90-4bd0-3cd1-b2a8-200429ce9329 | -20.94396 | -56.58648 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fce63dec-b927-3975-990d-4ad4ad41f688 | -20.94186 | -56.58364 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc183420-01a1-347f-8fca-7e82759c776c | -15.6261 | -57.30612 | 2025-05-24 05:27:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cebe100-bb7a-3631-b1a7-a35158355723 | -16.28214 | -58.67294 | 2025-05-24 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22e51d80-2172-3abb-9ebb-5a9be24bc10c | -19.87181 | -54.36309 | 2025-05-24 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7818212a-c543-366d-ad53-c6f951851e4a | -20.94651 | -56.58421 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18f29de9-ca75-3d3f-b8d6-0b7bcee8e00a | -20.93815 | -56.59582 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ac38ebb-c0f0-363d-a992-bfeb1376e091 | -15.62771 | -57.30728 | 2025-05-24 05:27:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 071a475e-608e-3ae8-ab34-6de5ae0087e7 | -21.96383 | -56.07716 | 2025-05-24 05:27:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94852da2-5a28-3433-9ce5-a1ddf0e6e279 | -20.94596 | -56.58928 | 2025-05-24 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 27c10fb7-ebc0-34ba-97d5-7638b4191f18 | -19.79257 | -53.83797 | 2025-05-24 05:27:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2fc7e86-d870-3819-a677-e4950a0acf4c | -15.62562 | -57.3098 | 2025-05-24 05:27:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e80c158-a507-3dfb-80c6-426a81b96c26 | -8.07 | -43.1216 | 2025-05-24 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 1fe61d81-a681-34de-9110-c1f4a2e324ce | -8.07 | -43.1216 | 2025-05-24 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| b2766ac4-d79b-3821-93bf-a2c8a924895c | -13.36973 | -54.26917 | 2025-05-24 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| b422a425-3dce-3b6d-bf24-a8ea7d601f51 | -13.36533 | -54.26018 | 2025-05-24 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dbe4ea63-04eb-38b0-ad58-7d4e3b55b868 | -11.75683 | -54.23235 | 2025-05-24 05:48:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6cbb507b-aa04-3edf-8fe8-9ba4227efa7f | -13.83281 | -59.64862 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04802468-38c9-3dbc-b7b3-229edabb8bca | -11.99641 | -57.21812 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 28beada2-c111-3b33-ae27-e4c0d322f89b | -9.42356 | -58.30262 | 2025-05-24 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f5b1b8f-9748-3612-a452-d2af4d64dc3c | -13.85123 | -59.72292 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b17c85d-fa19-3a59-9269-2e2c1ceea77d | -10.68122 | -57.60273 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0eac36b-53bc-328c-b827-95d0f6e2e9dd | -10.68073 | -57.60683 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b8a8458-1aec-349c-84e4-6bfed5bde262 | -13.98419 | -56.00858 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff2850d2-ef79-3a2e-a925-4c714255f6ce | -13.15192 | -56.81673 | 2025-05-24 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf995817-2950-31cb-b2b6-75bb99f5c9ec | -9.41743 | -62.32384 | 2025-05-24 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3b06336-54cd-3d10-b388-1ac49a0acd2f | -14.07029 | -57.11199 | 2025-05-24 05:48:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67f79132-cd68-3511-a94b-068829c2f35f | -10.67998 | -57.59978 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79fcb7a8-2979-3dfa-969d-583ade186b25 | -10.36671 | -57.50659 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2e0f3280-1240-3136-8ab9-7d71d67b3ab2 | -10.36773 | -57.49863 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7984c7eb-efa6-3933-a3f2-4448dc339974 | -13.9896 | -56.0204 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d3f06df-50ef-30bb-86a5-0e301bb6e7a7 | -9.91727 | -59.91083 | 2025-05-24 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0fa496c-b9ab-31e4-9b8b-0c568fdf7df8 | -14.01816 | -55.14023 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4fe89a8-f187-3c9d-be9f-040252ff17ce | -12.13289 | -54.66125 | 2025-05-24 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b777639-1880-3ea4-9e7e-40bee6ffb181 | -11.74968 | -54.23182 | 2025-05-24 05:48:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a83e2003-a232-33f9-aa74-3807244c403d | -10.68568 | -57.60064 | 2025-05-24 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d267a7b-7c5e-327c-9d68-75e9e89b6338 | -13.14627 | -56.81102 | 2025-05-24 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53e0a0ec-b437-3e76-853c-fd72fe1d0f7c | -9.41494 | -58.30236 | 2025-05-24 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 115fc42a-1da2-3479-91d4-bcaa3bc3958d | -9.42313 | -58.306 | 2025-05-24 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18db596e-5010-311d-a2c9-7b58c34a52ca | -13.15755 | -56.82257 | 2025-05-24 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3b75dc4-8ab2-3f22-afc5-3b46e070c7e6 | -13.983 | -56.01991 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5dd17cc-562a-31d7-aadc-21a061e2464c | -13.86605 | -59.73106 | 2025-05-24 05:48:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b605f670-06be-361a-a82c-53456ccbaecc | -11.99693 | -57.21377 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd580000-8749-3615-bd2a-9159dddf60aa | -13.15248 | -56.8117 | 2025-05-24 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 994b420a-3bf2-3c73-ab44-b87345c1b3fe | -14.03269 | -55.13516 | 2025-05-24 05:48:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62ed05a8-10c2-367b-846d-04163308911b | -10.0219 | -65.00329 | 2025-05-24 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4ac62d6-2986-36db-a867-ae486f776b09 | -14.07082 | -57.10718 | 2025-05-24 05:48:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README19.md)
