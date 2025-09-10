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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd726270-d9c3-3da7-8084-c36f59d0ccfe | -5.5705 | -45.0291 | 2025-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 273.2 |
| eb4b7ea6-9564-340c-8d8e-1ce4eeb9c296 | -8.9754 | -46.0603 | 2025-09-10 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b3e4dee2-f85e-30a7-b00e-1942c69afe70 | -5.535 | -42.65 | 2025-09-10 01:00:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| b3706299-6af7-3355-9a5b-e1dfcee20b53 | -8.0604 | -48.664 | 2025-09-10 01:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 7e8e79a5-74bb-383f-a292-822550fc2f81 | -11.4657 | -43.6195 | 2025-09-10 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| d96fcb8d-72b8-3625-959b-de5769f6d462 | -5.589 | -45.0505 | 2025-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 238.6 |
| ba2f66dc-3e42-3535-9397-6e88f2e0f729 | -13.1369 | -54.8966 | 2025-09-10 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2bad3b3a-6a7e-342a-b200-f6e94b98be0f | -15.801 | -52.2472 | 2025-09-10 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f220d668-fbc0-39d6-b1f3-b082ed43443f | -18.132 | -51.7315 | 2025-09-10 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 43a3267e-048f-315c-ac7f-2fea71cb5952 | -6.8519 | -47.9361 | 2025-09-10 01:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7406ecb3-8412-35d1-a4c8-4b956c81bd3e | -7.7705 | -46.0684 | 2025-09-10 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| bdfb15ad-8a74-3d23-b5e7-d77c53e6aeba | -5.5892 | -45.0278 | 2025-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 037439d4-d471-3e4e-b41d-20a258cebd89 | -6.2597 | -43.3895 | 2025-09-10 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b184ccab-8b00-3129-a5fd-ff3ae57d4df7 | -13.1367 | -54.9171 | 2025-09-10 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 66fa439c-9f71-3372-9d90-ef292aff3bb0 | -15.8869 | -51.8274 | 2025-09-10 01:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 4c841a06-436c-31c5-97f3-c9ea7cba362c | -11.4652 | -43.6432 | 2025-09-10 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e9a5f1a8-274b-39fd-b7a4-4d6748c811c5 | -8.0604 | -48.664 | 2025-09-10 01:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 012c1899-3a18-3639-bc62-20e36c39b4fc | -15.8397 | -52.2631 | 2025-09-10 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d5e8101e-d554-3dd7-98b5-0a894f0093c2 | -5.5705 | -45.0291 | 2025-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 220.5 |
| d908db1e-bb4e-3a12-9997-5ea6eea1b337 | -15.8873 | -51.8059 | 2025-09-10 01:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 0c8ee096-6497-3204-89d0-28ba17ceb285 | -13.1178 | -54.8986 | 2025-09-10 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| a026e37b-c8da-3fc1-8eee-b94c008fb3d6 | -8.0602 | -48.6856 | 2025-09-10 01:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1115936f-7c9b-3dcb-96ac-74c5d96bb217 | -20.9873 | -48.0033 | 2025-09-10 01:10:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4dbc492a-8190-3185-8562-d8acd7a8dbd2 | -20.988 | -47.9798 | 2025-09-10 01:10:00 | GOES-19 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3e8a91ed-e9b5-38cb-89ab-c048e1c0f4ef | -11.4465 | -43.6224 | 2025-09-10 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 6d6ace61-040c-3a11-9b91-61a81d7139d8 | -6.2595 | -43.4129 | 2025-09-10 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 195dca9f-f771-327a-b822-917536e73373 | -9.0768 | -46.9668 | 2025-09-10 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| d10d89a8-b487-33bb-a5b9-dab05fcd3816 | -9.4578 | -40.3392 | 2025-09-10 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 4d2c5527-e04d-3bda-88d0-c5af13cf5af4 | -9.4765 | -40.3613 | 2025-09-10 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 85cfc5d3-b27a-3318-bb26-5894d98426e3 | -9.4388 | -46.7052 | 2025-09-10 01:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5c718968-ea99-361e-bf51-0658c90c563d | -5.5703 | -45.0518 | 2025-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 877f42a5-d998-37ad-9c3d-f1441fdeab56 | -11.4657 | -43.6195 | 2025-09-10 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| aa0d963f-2d96-3057-bc7f-29cd414f7534 | -9.4769 | -40.3365 | 2025-09-10 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 151.3 |
| b56fa239-e884-3892-8f91-f43bff237d1e | -5.6548 | -43.9244 | 2025-09-10 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 4a58c874-19c5-347e-9e1e-11a78ce6da9d | -13.9762 | -48.224 | 2025-09-10 01:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| af030884-c6d2-3fdc-82f5-0be8a6e3730e | -16.0604 | -49.9741 | 2025-09-10 01:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 426bbc53-af32-3f82-a7da-2c2a61cd406c | -15.8673 | -51.8303 | 2025-09-10 01:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fd99a93e-144a-390f-99d6-f5b7a61e1413 | -15.8205 | -52.2444 | 2025-09-10 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f451d27d-61db-32d8-9fb5-925b52c874a9 | -18.1325 | -51.7096 | 2025-09-10 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6c9a22d1-a9e7-3fb5-a107-a8b5365faa00 | -13.1176 | -54.9191 | 2025-09-10 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| b2f8df9c-5c4f-3df3-8f70-2b1b5847c977 | -8.0414 | -48.6873 | 2025-09-10 01:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 77b0518a-596b-3200-92b1-b4f027e04717 | -12.0117 | -51.0104 | 2025-09-10 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d428202d-1e97-3369-b402-af2b84686808 | -11.3202 | -46.5218 | 2025-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c9d1b008-4992-355d-81f0-493534c3ad5f | -20.9873 | -48.0033 | 2025-09-10 01:20:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 52f8a438-d51c-3a99-b18e-5c2d22c8469a | -6.871 | -47.8911 | 2025-09-10 01:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| cb132f5e-dd7b-3454-b07e-965c0b51ca80 | -11.4883 | -50.4083 | 2025-09-10 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 4111effa-1778-33be-b8d9-b0677611ee46 | -11.3397 | -46.4967 | 2025-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 74309075-5af9-3774-868b-1dc6ac73a7f2 | -11.4469 | -43.5988 | 2025-09-10 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 370daa6e-7e68-3b84-bd32-d43bc0c30c5c | -11.4661 | -43.5959 | 2025-09-10 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ae494430-43cd-365d-9fdc-bf13cc5b6477 | -16.0608 | -49.9521 | 2025-09-10 01:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 6bcdf0db-7bf4-3c0f-a946-0778a8a5a205 | -21.0086 | -47.9749 | 2025-09-10 01:20:00 | GOES-19 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 49.2 |
| c83ba057-68e6-3938-8007-b1c530c500e6 | -5.5705 | -45.0291 | 2025-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 274.9 |
| 2fb72f5a-0166-382c-9b64-7ad319fae1fe | -5.535 | -42.65 | 2025-09-10 01:20:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 4b5465ec-a066-3969-aafd-5f5f89e2ca15 | -6.8899 | -47.8679 | 2025-09-10 01:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| c72047a6-b88c-3633-aeb3-b0f805c2450a | -11.4652 | -43.6432 | 2025-09-10 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 12398851-4d05-366c-84d3-1afce30186b2 | -9.4388 | -46.7052 | 2025-09-10 01:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 79ddde40-0c58-39dd-b0bb-c4f9248472c4 | -16.0412 | -49.9553 | 2025-09-10 01:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 03ef7718-b019-3caa-855c-110222b34233 | -16.0604 | -49.9741 | 2025-09-10 01:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 7f1f7455-2ad9-3de7-acb1-f4692ca27f28 | -11.3205 | -46.4992 | 2025-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a5b666f6-edf7-35c1-b158-a14394b035bc | -16.0408 | -49.9773 | 2025-09-10 01:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 227.1 |
| acb94c63-77dd-3c56-8262-c9f815705633 | -5.5892 | -45.0278 | 2025-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 281.9 |
| e966981f-6618-39fe-89c8-df53541953fb | -18.132 | -51.7315 | 2025-09-10 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2b6f169b-7bdb-3680-bbf1-ee1b83429d96 | -11.4465 | -43.6224 | 2025-09-10 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 6aa38f6b-f29e-3c15-a630-1cb4d043013b | -11.4657 | -43.6195 | 2025-09-10 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 278.5 |
| eef89de2-4f70-3efa-bc8f-fb6e4fdf2231 | -6.8897 | -47.8897 | 2025-09-10 01:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a2a7ff9f-c7cc-3991-a2dc-658065b77082 | -10.0157 | -51.6821 | 2025-09-10 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b9d0530a-bcc3-3511-a98e-773bdb5032ef | -7.7705 | -46.0684 | 2025-09-10 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 429eead2-5776-3c6f-92ef-2c074c1a1f12 | -5.5703 | -45.0518 | 2025-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 247.8 |
| d8223245-6579-3d7b-930e-043a805df88f | -18.1325 | -51.7096 | 2025-09-10 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| dd15b6e7-07ec-3787-9e19-9c2b374f534a | -6.8519 | -47.9361 | 2025-09-10 01:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7c2dd419-29ca-35f5-8b27-c64d56111404 | -6.2595 | -43.4129 | 2025-09-10 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 41bf5f7c-a7a7-3050-8532-443624d5311b | -5.589 | -45.0505 | 2025-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 249.5 |
| f817aa3f-54ba-3f29-b90a-e3b946438ad4 | -11.3389 | -46.5419 | 2025-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1332c792-8698-3880-b64c-3351c347ab58 | -11.3393 | -46.5193 | 2025-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| a45710b5-32cf-361d-b77b-601547a6e093 | -10.0346 | -51.6804 | 2025-09-10 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e63f52f2-9667-3718-867d-65c369b0225d | -10.0348 | -51.6594 | 2025-09-10 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 07906228-6b4c-3830-969c-1d59a7134066 | -9.4578 | -40.3392 | 2025-09-10 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 13663911-ba72-3d2b-8269-426632f99ca8 | -8.0414 | -48.6873 | 2025-09-10 01:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 99c8fe18-b691-3735-a2ac-5a58b341ed9f | -20.988 | -47.9798 | 2025-09-10 01:20:00 | GOES-19 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bde8a81b-9865-329a-8ace-5270a0e88818 | -9.1142 | -46.9851 | 2025-09-10 01:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f62635a9-e8f0-338d-8222-ac39e6bee8b9 | -8.0602 | -48.6856 | 2025-09-10 01:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 41d542eb-8ad4-3e9a-8b46-796163f3c283 | -19.9197 | -46.1421 | 2025-09-10 01:20:00 | GOES-19 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| dc3abee3-6367-3822-b257-9d9911b4782b | -15.8869 | -51.8274 | 2025-09-10 01:20:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0d7bca31-f05a-30ab-8dc5-f5987a940cec | -16.6335 | -49.7683 | 2025-09-10 01:20:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7899b8b4-22de-3e0c-abc3-d012b58dcd05 | -12.0117 | -51.0104 | 2025-09-10 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 08973766-1f91-3d52-8b06-c52a9633f07f | -5.589 | -45.0505 | 2025-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 737c922f-212b-3d64-a8b4-eca08ead2b0f | -20.9873 | -48.0033 | 2025-09-10 01:30:00 | GOES-19 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ddd5859b-f1fb-3ba6-9fa7-05856d470547 | -21.0086 | -47.9749 | 2025-09-10 01:30:00 | GOES-19 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d365b793-4134-352b-9606-2428dd904a22 | -11.1187 | -48.4369 | 2025-09-10 01:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 87569e60-497b-32c3-af23-06f23f275f2f | -5.5703 | -45.0518 | 2025-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 7f749f9d-d797-3e74-b76a-bb14fa0d68d2 | -11.3205 | -46.4992 | 2025-09-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 917153ea-2d49-3f77-b828-34eca42b9255 | -11.3393 | -46.5193 | 2025-09-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 503ae6ad-b0e9-355e-ba60-b1707219c2f1 | -6.8519 | -47.9361 | 2025-09-10 01:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0a147109-ba1e-3d11-84e5-93e4f61b707e | -11.4657 | -43.6195 | 2025-09-10 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 6436ddce-f289-3b5d-94d6-01d4e9a6e235 | -6.2595 | -43.4129 | 2025-09-10 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 34f77186-e901-3bad-b026-1e616f183504 | -8.0414 | -48.6873 | 2025-09-10 01:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 92.3 |
| f56732b3-ec2b-349d-bc07-60ed126eff8d | -11.3202 | -46.5218 | 2025-09-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5a5afe3f-ae1b-3d95-8e89-95601d520818 | -16.0604 | -49.9741 | 2025-09-10 01:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 26433e8d-191a-3b70-9bfb-51ce10402293 | -16.0408 | -49.9773 | 2025-09-10 01:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| fe7c6fde-b201-3fac-b85a-525af465e505 | -11.4652 | -43.6432 | 2025-09-10 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |


[Clique aqui para ver as próximas entradas](README12.md)
