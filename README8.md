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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f844017d-f761-3ff0-8af6-2de471e46159 | -14.9134 | -58.1263 | 2025-12-12 02:10:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a33c41ad-bafc-3a46-88df-6f453906dd5b | -2.2907 | -45.5709 | 2025-12-12 02:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 215.5 |
| f0e53bfb-7b1a-3e1e-a5ac-6205341593f6 | -8.0324 | -43.1022 | 2025-12-12 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.1 |
| 935db40c-f041-3c25-b54e-d5faa52f4ce7 | -2.3092 | -45.5704 | 2025-12-12 02:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a1d8e0b7-19c1-3cef-8f81-b28b46714285 | -2.2906 | -45.5933 | 2025-12-12 02:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 527.4 |
| 9d10a225-445b-3fab-9fc7-ddda514fa316 | -3.237 | -42.0802 | 2025-12-12 02:10:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f5076e89-7646-3074-907a-3e9ad580bdeb | -2.4183 | -51.9484 | 2025-12-12 02:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9f2433e0-4e86-3c0a-bbef-19ae1baa4d2c | -2.2906 | -45.5933 | 2025-12-12 02:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 452.7 |
| f3c438d0-c327-348e-8250-fda111a5530c | -1.7517 | -54.0323 | 2025-12-12 02:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| cb99c6f0-a787-37fa-a516-a5b1e48c536c | -12.4325 | -58.0276 | 2025-12-12 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 869b7ac8-83b1-3cd8-b492-4ea93508d2bb | -2.3092 | -45.5928 | 2025-12-12 02:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 5ee1b9eb-8730-3870-a4df-35892328b876 | -2.4923 | -51.8027 | 2025-12-12 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 8104948b-e70a-3295-9c1b-f378adcd94c4 | -14.8941 | -58.1282 | 2025-12-12 02:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 20b02bda-a510-3394-818c-30439953391a | -2.2905 | -45.6157 | 2025-12-12 02:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 23c960c1-e110-3eb1-9035-0748dde545f3 | -8.0516 | -43.0765 | 2025-12-12 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| be74ae57-4cb3-3566-8e9a-2222df6a4e76 | -2.5108 | -51.8023 | 2025-12-12 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6d1d8e8a-3059-3b94-9ec2-6df23a4e21ec | -2.4367 | -51.9274 | 2025-12-12 02:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 859b59f3-67ff-3bf1-ae99-6baa575b68de | -9.9334 | -36.1246 | 2025-12-12 02:20:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.0 |
| 8e853fee-6aeb-3934-a9cc-5538f18ab29d | -8.0327 | -43.0786 | 2025-12-12 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 976f46c6-cc1a-3d9a-a5fe-7139184f83df | -2.2907 | -45.5709 | 2025-12-12 02:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 153.1 |
| bbf4266c-9451-3f97-8114-b9d17bb00bc7 | -12.3946 | -58.0307 | 2025-12-12 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 165.8 |
| fe656f69-fcbd-3bb8-a3ef-e84f48c6602e | -9.9329 | -36.1517 | 2025-12-12 02:20:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 9a5ca1c3-fb50-3225-bd7c-96a68203c404 | -12.4133 | -58.049 | 2025-12-12 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 157.0 |
| cdfe193b-4bfd-33a8-bac4-e56ea41399cf | -3.237 | -42.0802 | 2025-12-12 02:20:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 4c64a4c4-01c1-3d02-8313-b329df7b02f3 | -12.4323 | -58.0475 | 2025-12-12 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 063d4558-0a90-302e-9c47-04289368ff20 | -8.0324 | -43.1022 | 2025-12-12 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 225.2 |
| 78532292-6018-3638-8bf4-159222c2800f | -2.3092 | -45.5704 | 2025-12-12 02:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ca5379c4-9ece-3f71-9959-320df20e2d01 | -12.3943 | -58.0506 | 2025-12-12 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c0546a29-8b17-39f9-b693-becee4bf2617 | -14.9134 | -58.1263 | 2025-12-12 02:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 222f3567-ca6b-31c3-9001-51ae32732b6f | -12.4135 | -58.0292 | 2025-12-12 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 2f32e0c3-fc55-31f0-b365-208e80c58901 | -8.0135 | -43.1042 | 2025-12-12 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 09686bc8-0caf-3d02-9964-80e06b8b8671 | -8.0513 | -43.1001 | 2025-12-12 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| dea0f0dc-77d2-38a7-ae06-e12ff4fc7b03 | -2.5108 | -51.8023 | 2025-12-12 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3ddcc6af-5df0-3be9-afc4-044933c9f48a | -14.9134 | -58.1263 | 2025-12-12 02:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 751615ea-9230-36bd-89ac-293c6901f66f | -3.237 | -42.0802 | 2025-12-12 02:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 248a163a-d52e-36f5-9232-8a52d5c9735a | -2.5108 | -51.7817 | 2025-12-12 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 110b7600-994b-345c-a400-06ec92316136 | -2.2907 | -45.5709 | 2025-12-12 02:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c8268ed0-4430-3360-842b-b7c43c23a474 | -2.4367 | -51.948 | 2025-12-12 02:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 891c1ed0-c32e-3728-a2c2-a477937a633d | -2.3092 | -45.5928 | 2025-12-12 02:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f88595a9-4fe8-3650-824a-21261eb3d940 | -1.77 | -54.032 | 2025-12-12 02:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e299cf72-c11e-36ea-8d69-e616c0dd35cd | -1.77 | -54.0521 | 2025-12-12 02:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 3d1e6c41-cdce-3f9e-bc5a-26489077d116 | -2.4367 | -51.9274 | 2025-12-12 02:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 5e398874-48d1-390b-805f-0bf64351d9c4 | -2.4183 | -51.9484 | 2025-12-12 02:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 360b11db-a997-3bdc-a091-328056e603f1 | -1.7517 | -54.0323 | 2025-12-12 02:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 535ae03a-cc36-37ec-bfc2-3f7c5e9cddc5 | -2.2906 | -45.5933 | 2025-12-12 02:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 172.7 |
| f0d39c7f-b7cb-3e5f-ad71-569302517f1f | -2.4923 | -51.8027 | 2025-12-12 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5a50c46a-86e5-3512-9615-d78b381c4ddc | -14.8941 | -58.1282 | 2025-12-12 02:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| df30fb2b-4dc8-38ff-9e1f-b0012245e3d1 | -2.4183 | -51.9278 | 2025-12-12 02:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 8e80d202-43d7-341d-8a77-7ee4fc1c5eeb | -2.2906 | -45.5933 | 2025-12-12 02:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 935130c3-da19-3696-a29e-2bd721f7f326 | -14.8944 | -58.1081 | 2025-12-12 02:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d9601dfc-1bc2-3556-9951-a194628579de | -10.2187 | -36.3162 | 2025-12-12 02:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| b2293dfb-d972-3cb0-acbd-796763914de8 | -2.3092 | -45.5928 | 2025-12-12 02:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9ff50f29-c3cb-32f0-898d-072304e62a16 | -8.0327 | -43.0786 | 2025-12-12 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 171f2128-ae75-3f7e-9e7e-678c519c790b | -1.77 | -54.0521 | 2025-12-12 02:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| cff14cad-cc76-3e45-948c-de59d778972b | -1.77 | -54.032 | 2025-12-12 02:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 37a08c28-d8cc-370c-a0a4-17a6394b1044 | -3.237 | -42.0802 | 2025-12-12 02:40:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e9c9a3e9-d367-35ab-918d-080c072dd07d | -8.0513 | -43.1001 | 2025-12-12 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 36685d99-8be6-3890-b9db-d7b20a4cd434 | -14.8941 | -58.1282 | 2025-12-12 02:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c32b1236-1720-3638-8810-ffc360d84222 | -2.4923 | -51.8027 | 2025-12-12 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e2221798-07a0-3802-83bd-c12e2ff8456e | -14.9134 | -58.1263 | 2025-12-12 02:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 44c3c409-4043-3401-be43-785a2bd6ca4e | -8.0324 | -43.1022 | 2025-12-12 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 11467e92-972f-3588-b4e4-1b207e8d9647 | -2.4183 | -51.9278 | 2025-12-12 02:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8f85cd55-ca90-3648-932b-99be8ab3034c | -2.5108 | -51.8023 | 2025-12-12 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| daa5682f-660d-32df-9847-3a6288894c0a | -1.7517 | -54.0323 | 2025-12-12 02:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 04048a8b-df2c-3503-b25c-a3f52752d530 | -2.4367 | -51.9274 | 2025-12-12 02:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c8ce37a3-d9ad-3843-a185-5292f7bb3cf6 | -8.0327 | -43.0786 | 2025-12-12 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 16676b19-9554-3dc2-8ab7-c8ce7245d1d4 | -14.8941 | -58.1282 | 2025-12-12 02:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 73ae3137-dec3-3129-ab9b-0ba5b371ac1a | -2.4924 | -51.7821 | 2025-12-12 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f4e1f8ee-6f5c-3565-9eb4-1d73f802a73e | -2.5108 | -51.8023 | 2025-12-12 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 836e9024-06f8-3118-b428-0933e7b30e09 | -2.4367 | -51.9274 | 2025-12-12 02:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 0db5dfd4-6c21-3ca2-aea0-b13bf2729170 | -2.2906 | -45.5933 | 2025-12-12 02:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| eb1bc84c-d673-39e2-b1ce-5c5bcd6b52a4 | -14.9134 | -58.1263 | 2025-12-12 02:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 555f2a62-33c5-3735-8e00-5e8bbd99215f | -8.0516 | -43.0765 | 2025-12-12 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 41aabf1f-9f3a-3659-a4df-aeb3c18aa3fd | -2.4923 | -51.8027 | 2025-12-12 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 8a0c14e6-8502-34c3-bee0-34186d8c36ac | -8.0513 | -43.1001 | 2025-12-12 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.8 |
| 0ed43599-456c-3c6f-9083-d83a86f3b0cd | -2.4367 | -51.948 | 2025-12-12 02:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 78bdb5c7-999f-3972-8634-36df8d36da48 | -2.4183 | -51.9278 | 2025-12-12 02:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a8f65e37-468b-367e-a3d4-6c078131a899 | -8.0324 | -43.1022 | 2025-12-12 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 214.9 |
| c8def5e7-28a1-37e0-a524-19ae2913a998 | -8.0135 | -43.1042 | 2025-12-12 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 70b28cbb-8bb9-3bb4-8d8b-7323ce062c40 | -1.7517 | -54.0323 | 2025-12-12 02:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 142710b6-d47b-3041-a85e-557c1fb7a7c0 | -1.77 | -54.032 | 2025-12-12 02:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 3e200970-9d79-36c5-ab2e-65e818fb8561 | -1.7516 | -54.0524 | 2025-12-12 02:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 28ad6ea0-01f6-315c-a523-8717afdae9dc | -8.0513 | -43.1001 | 2025-12-12 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 49d44f32-fd53-3cee-ad16-95a8fe5a3bef | -1.77 | -54.0521 | 2025-12-12 03:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 075cdb53-b14c-376b-936e-84fc5305533f | -14.8941 | -58.1282 | 2025-12-12 03:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 93c65423-eda3-3776-b32c-1ecba088d0bf | -2.4367 | -51.9274 | 2025-12-12 03:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| bc110c5b-31f5-3965-86e5-5a10c30cb980 | -8.0516 | -43.0765 | 2025-12-12 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 3a4eccc9-1fa1-340f-b694-9389d18f0ff4 | -2.4183 | -51.9278 | 2025-12-12 03:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 66f03ccb-60db-3bfb-9287-1db34e530bfb | -2.5108 | -51.8023 | 2025-12-12 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f50191e4-317b-3f3e-a28e-d40555934cb1 | -14.9134 | -58.1263 | 2025-12-12 03:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ef5e1e8d-381e-3ed7-9835-9fdd621c5544 | -1.77 | -54.032 | 2025-12-12 03:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 5396505a-892f-3e81-82ec-329b3703ff93 | -8.0324 | -43.1022 | 2025-12-12 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.9 |
| 8636b28b-415e-3fbc-a806-864fcf6b51ed | -1.7517 | -54.0323 | 2025-12-12 03:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 3f36f5d1-b0f7-39f5-971a-c86b1fc531e5 | -8.0327 | -43.0786 | 2025-12-12 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| ed3e610e-d1b1-3531-baf1-cebe392d84e5 | -2.4923 | -51.8027 | 2025-12-12 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b363f5cd-1e8b-3d86-a05a-6cbe5c4b2a84 | -8.0321 | -43.1257 | 2025-12-12 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 2cd39855-39ec-3714-8b6d-aa1855d6f59e | -2.4183 | -51.9484 | 2025-12-12 03:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3d1fc159-628e-3440-bf8d-5eff569ca175 | -8.0324 | -43.1022 | 2025-12-12 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 165.9 |
| 7c78a714-3d07-36f7-ad83-1706b45a097f | -8.0135 | -43.1042 | 2025-12-12 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| b9b8ab84-26b6-328d-8ce5-514d0cea4270 | -8.0327 | -43.0786 | 2025-12-12 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |


[Clique aqui para ver as próximas entradas](README9.md)
