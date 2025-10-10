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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 146fed0d-0868-3d07-8e7c-b58b8236c914 | -12.03218 | -62.94888 | 2025-10-10 05:23:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 252e860a-31fa-34c1-9989-9a657182f01e | -15.0003 | -56.8205 | 2025-10-10 05:23:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 286d643c-df37-3824-838f-862adf1d6aca | -14.88641 | -48.23114 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 780408c3-0d5f-3ef9-874d-49ffbcc066a7 | -10.03951 | -59.36522 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 434d7608-6ab5-3eb4-a119-e629e47f09a9 | -11.75797 | -64.88668 | 2025-10-10 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d87cefb8-567a-398b-830f-2b3c3efb0f01 | -16.01127 | -59.55384 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c8ecef6-07d0-3f91-9713-42c42820904c | -13.32376 | -47.9923 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cab6212-1b26-3fb6-a70d-470379e28d1a | -14.92783 | -46.78881 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1c6c384-b3e8-31cd-8756-0791b9652937 | -15.45974 | -48.53695 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe593de9-9545-30a6-aa38-1abfbab3f5a9 | -15.74741 | -48.98076 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89b21ecc-0c9a-3298-9210-48a02d4fb015 | -15.97144 | -59.53973 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc904775-6c2f-34cf-a257-55eb29f1d0ce | -14.42568 | -47.98692 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a01f44a1-460a-3fe2-a463-2191c6640aeb | -10.16927 | -64.7317 | 2025-10-10 05:23:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d91a8076-ef2c-3a0c-9b3b-c1a93ad68b9a | -14.68677 | -48.06818 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e582058-45a3-3c8e-a184-1d34ab3cd2ad | -14.94449 | -46.76685 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3db71b94-8f74-381e-8d0e-c49ee4548dc0 | -15.09113 | -46.61744 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e94f1c88-0a10-3e93-969b-9b45d29a9e69 | -14.88978 | -48.23156 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5575a274-3556-35b3-9c3d-af84deee2946 | -15.43032 | -47.99284 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f4739c4-516e-326c-a902-2f8e8c52059e | -13.36376 | -47.75176 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36065bea-f1d3-3c12-ab1c-334a54b8c8f5 | -16.67038 | -47.60264 | 2025-10-10 05:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 626b003b-63e2-37d4-8d39-b7c7e6f71f99 | -14.86475 | -48.4676 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b3f4a71-e881-3f39-830a-708f8a720406 | -13.37723 | -47.75301 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 075c28ce-9894-34ee-bed2-35e7c1865d22 | -16.02723 | -59.49441 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4834166-9761-38d2-b336-9fe9dfcef897 | -15.42407 | -47.98688 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfeb5de9-0c0c-34e9-b269-de789bbd49a3 | -14.89399 | -47.22486 | 2025-10-10 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 127d6003-7d74-326d-8553-2ffca6455433 | -13.28149 | -48.01108 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd85f079-19bc-35a8-938c-8e322fd17c72 | -14.88913 | -48.23768 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb3ee44f-2e42-3846-85f9-185e9aa7b503 | -12.09228 | -64.23068 | 2025-10-10 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a893d0d-9268-35b5-9cff-60fd662cbbf4 | -14.94382 | -46.77406 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e40ddfd-80eb-3987-953b-5cea95075672 | -8.51476 | -67.00204 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d05a94fa-e525-37eb-8cba-f2444ab5a5ae | -9.79192 | -60.14151 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd35fd9c-98de-3485-9827-b92cff16c4a7 | -16.00445 | -59.55274 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c348ee69-b678-3aca-a086-ee4bf400be60 | -11.82719 | -62.445 | 2025-10-10 05:23:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc80f4c7-7dba-3694-af53-4f45737635d8 | -9.66515 | -66.82508 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ed93d51-7356-3941-94d8-6f7b1f1e7f84 | -16.00786 | -59.5533 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 946c4931-34ae-3d96-b0a3-88f086fe64c6 | -14.93056 | -46.75943 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a458535-c41e-3242-830b-d6bec72a8eba | -16.00615 | -59.54146 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bff5480-a9ec-3ccd-890d-d0df1e8a4169 | -14.42665 | -48.01019 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 781ac576-9e5c-3ad7-ac83-0bbf4b94a1eb | -15.42349 | -47.99259 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1cd271ca-6225-3d31-9aec-19603d754975 | -15.96803 | -59.53913 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 118487ad-68ce-3355-accb-ac8e260457f8 | -12.09149 | -64.23531 | 2025-10-10 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42a99ff5-2e8e-3cb2-b1cf-314b4b33ea5d | -12.03285 | -62.94485 | 2025-10-10 05:23:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bebfab3-a59c-3fb9-8fd1-76f7f80e4123 | -10.03783 | -59.35412 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08f861af-6cc9-3926-811a-3315bcf96165 | -15.97937 | -59.53351 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c1d7115-f750-3c9d-ad5e-6038cb10b454 | -8.51496 | -66.99812 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0561de1-3c64-3807-ac36-44471a9c8e71 | -9.6689 | -66.83073 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec1cf520-a6a0-37f9-ade9-40118b9ec0a2 | -21.72315 | -52.42272 | 2025-10-10 05:23:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fc3975e-07e7-32a7-804b-4066952f0733 | -14.88853 | -48.24337 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7275be58-5da4-3d63-9608-e79b22c8bc0f | -16.19936 | -59.33982 | 2025-10-10 05:23:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8b25d5f-852a-314e-b914-add6e229bfa3 | -15.4264 | -47.98594 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e7f98987-0c56-3fd3-aebe-40c6e2912ac0 | -16.05132 | -48.0688 | 2025-10-10 05:23:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af7be78c-1715-3e67-a7b4-7ba2c94e7c9d | -14.93673 | -46.77176 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba4742f1-bb8f-319b-8015-3a36e854ef66 | -15.43095 | -47.98664 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bfbf51de-d7d2-39dc-9605-dc78afa2d00f | -9.78915 | -60.13746 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97a0ba4a-e79c-36c9-b9e9-ab6bf31ad942 | -15.75324 | -48.98704 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cae2edb7-0e62-3283-9482-ca283d191bfc | -9.86474 | -59.87639 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 222b942f-0498-3a9c-b6be-c4d925b756d8 | -15.97089 | -59.54342 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f0a9ba9e-13e8-383e-92dd-8bfcec736036 | -13.31506 | -48.01039 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64bed896-0272-3018-891c-60b77c8d7bf1 | -10.00937 | -65.17631 | 2025-10-10 05:23:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38a755d7-3377-37f3-965e-01d449b2e182 | -14.88521 | -48.24333 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83ad0e96-b9e1-306e-97b3-50931d93105c | -12.08773 | -64.23463 | 2025-10-10 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ed2f08e-c25a-39e0-ab16-7312d18caf37 | -14.92921 | -46.77398 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7086c73f-2874-35ba-b39a-6910af3ee422 | -14.42944 | -47.98301 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 812eecdc-d526-37ed-a789-2b9a38f3e4c3 | -15.09211 | -46.60767 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 005ac072-db20-345c-a315-ebd2f0f86eb9 | -10.45979 | -63.24559 | 2025-10-10 05:23:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00020313-21a3-3ac1-b714-21304655a4e1 | -14.88226 | -48.23914 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0cd5137-586c-3462-b217-fa414ae4f95b | -17.21433 | -47.65757 | 2025-10-10 05:23:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec7791d9-0fea-3e08-b7b1-e3a2ff03b18f | -14.43287 | -47.98322 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d44f8d63-933d-3500-b6ba-cfeaa1e7f8f9 | -9.86197 | -59.87235 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a8784003-f991-391a-aedd-ccbe7669b90a | -14.95109 | -46.77436 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 135518e4-284d-3fb7-a7bd-130da5acc317 | -12.73845 | -59.4631 | 2025-10-10 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcb29094-2fa6-3a55-bb88-1d3ce86ad7da | -14.98576 | -47.19876 | 2025-10-10 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88d44f32-9f9d-3a37-aad4-8e1ca32a1288 | -16.26562 | -47.16263 | 2025-10-10 05:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be9c82c3-ccfe-3a91-8ab3-5194f205d3aa | -16.26625 | -47.15558 | 2025-10-10 05:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c2e4cc1-7f33-3b40-8edc-4165a0b8373c | -14.89334 | -47.23164 | 2025-10-10 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa7fb3c1-dd83-3122-b9e0-bf7184173ffd | -13.34981 | -47.75489 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbe35093-c968-322c-9205-aa23309076b0 | -15.74873 | -48.9815 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 78b9698c-c142-3c77-953f-16b75b8d3d32 | -14.9427 | -46.76413 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37caa0a6-22cb-39ae-853c-4c141c5e437a | -21.72352 | -52.41889 | 2025-10-10 05:23:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a56beb5e-5d49-3d05-81fc-30b761f3f55d | -10.63415 | -68.9712 | 2025-10-10 05:23:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae4960e1-2032-38c9-a99f-8204a4e34749 | -13.30282 | -47.99978 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d7636b9-2126-347a-bb27-1603823854a2 | -13.35721 | -47.74943 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c2be13-eb82-3c6e-8f06-12a517835841 | -16.00673 | -59.53759 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10ea96a4-a420-3d10-a324-47e59013c1ec | -10.63475 | -68.96796 | 2025-10-10 05:23:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bcba81b-d792-3516-8569-910c4cbdba81 | -13.32145 | -48.48172 | 2025-10-10 05:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5426170-4073-3688-9258-9bd7f05815c0 | -16.0073 | -59.55701 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 859a380c-88d5-3d16-8242-c18c412d503c | -9.67928 | -68.57333 | 2025-10-10 05:23:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e87097d-5019-3842-bee2-502175e1cd1a | -13.01257 | -61.43711 | 2025-10-10 05:23:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89ea9e57-0f6c-34b4-af32-2990276fe9f7 | -16.01015 | -59.53811 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52c8948a-a2b1-376b-aa27-35d6524c85f1 | -17.93021 | -57.62233 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e8610bd8-f166-3e75-a9bd-4add7a9414f1 | -17.82203 | -57.62887 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 503c39f6-5d92-3849-9475-c0b1464ab3e1 | -17.89398 | -57.66079 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bdd04640-e397-3c21-8748-7b087c615f01 | -17.90294 | -57.51072 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2bb2e418-767a-300c-92e6-dd35043586c7 | -17.94193 | -57.61687 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 63cc727d-0ae6-3c4b-aa52-9d0d8085bcc1 | -18.03204 | -57.55296 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 15e0615c-0266-3ef0-aefd-b236183a0a0c | -17.90524 | -57.52238 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 25b78f31-238c-37f4-8452-8e1ebaa1523d | -17.90598 | -57.65771 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d65b8d4a-7e66-36a8-a816-70cdcb8d54be | -17.89223 | -57.50371 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ff2731d8-5c07-3318-be5d-6e0bb324cff9 | -17.82517 | -57.65643 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6dff3108-acca-332c-8123-dba29c9bb2c5 | -17.83721 | -57.65288 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |


[Clique aqui para ver as próximas entradas](README47.md)
